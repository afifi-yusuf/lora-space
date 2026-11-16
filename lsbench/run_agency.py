"""Agency harnesses (native, codex, claude_code, ...): the editor runs inside Agency's Docker sandbox (no torch, no GPU,
weights mounted read-only); the model tools are host MCP tools backed by the TargetService on the GPU host."""
from __future__ import annotations

import faulthandler
import json
import os
import sqlite3
import sys
import time
from pathlib import Path

from . import prompt
from .target import TargetService
from .recover_usage import verify_missing
from .usage import profiler_usage

CONTAINER_WORK, CONTAINER_MODEL = "/workspace/work", "/workspace/model"
SANDBOX_IMAGE = "lsbench-sandbox:latest"


def _usage_from_db(db: str) -> dict:
    """Best-effort token totals from Agency's data log (sums every integer column whose name mentions tokens)."""
    tot: dict[str, int] = {}
    try:
        con = sqlite3.connect(db)
        for (table,) in con.execute("select name from sqlite_master where type='table'"):
            cols = [r[1] for r in con.execute(f"pragma table_info('{table}')")]
            for c in cols:
                if "token" in c.lower():
                    v = con.execute(f"select sum(\"{c}\") from \"{table}\"").fetchone()[0]
                    if isinstance(v, (int, float)):
                        tot[f"{table}.{c}"] = int(v)
    except Exception as e:  # noqa: BLE001
        tot["error"] = str(e)  # type: ignore[assignment]
    return tot



def _dump_child_stacks(path: Path) -> None:
    """Append py-spy stacks of every descendant Python process (host tool servers run outside this process)."""
    import subprocess
    todo, pids = [os.getpid()], []
    while todo:
        out = subprocess.run(["pgrep", "-P", str(todo.pop())], capture_output=True, text=True).stdout.split()
        todo += out; pids += out
    with open(path, "a") as fh:
        for pid in pids:
            try:
                cmd = Path(f"/proc/{pid}/cmdline").read_bytes().replace(b"\0", b" ").decode()[:200]
            except OSError:
                continue
            if "python" not in cmd:
                continue
            r = subprocess.run(["sudo", "-n", str(Path(sys.executable).parent / "py-spy"), "dump", "--pid", pid], capture_output=True, text=True, timeout=60)
            fh.write(f"\n===== pid {pid}: {cmd}\n{r.stdout}{r.stderr}")


def _start_vertex_proxy(entry: dict, rdir: Path):
    """Start lsbench.vertex_proxy for this run (Vertex wants an hourly-refreshed token, Agency sends a fixed key)."""
    import socket
    import subprocess
    port = int(entry["base_url"].split("127.0.0.1:")[1].split("/")[0])
    key = Path(__file__).resolve().parent.parent / "gcp-sa.json"
    p = subprocess.Popen([sys.executable, "-m", "lsbench.vertex_proxy", "--port", str(port), "--key", str(key),
                          "--queue-log", str(rdir / "vertex_queue.jsonl")] + (["--priority"] if entry.get("vertex_priority") else []),
                         stdout=open(rdir / "vertex_proxy.log", "w"), stderr=subprocess.STDOUT)
    for _ in range(60):
        if p.poll() is not None:
            raise RuntimeError(f"vertex proxy exited ({p.returncode}); see {rdir / 'vertex_proxy.log'}")
        try:
            socket.create_connection(("127.0.0.1", port), timeout=1).close()
            return p
        except OSError:
            time.sleep(0.5)
    p.terminate()
    raise RuntimeError("vertex proxy did not start within 30 s")

def _queue_excess_s(rdir: Path) -> float:
    """Provider queueing beyond a normal first-token delay, logged by lsbench.vertex_proxy (0 for other providers)."""
    try:
        return sum(json.loads(line)["excess_s"] for line in open(rdir / "vertex_queue.jsonl"))
    except OSError:
        return 0.0


def _idle_seconds(rdir: Path, t0: float) -> float:
    """Seconds since the last model call or tool call finished, from Agency's live profiler database."""
    last = t0
    try:
        con = sqlite3.connect(f"file:{rdir / 'profile/profile_data.sqlite3'}?mode=ro", uri=True, timeout=5)
        v = con.execute("select max(end_ts) from spans where span_name like 'llm:%' or span_name like 'tool:%'").fetchone()[0]
        con.close()
        if v:
            last = max(last, float(v))
    except Exception:  # noqa: BLE001
        pass
    return time.time() - last


def run(task: dict, entry: dict, limits: dict, track: str, rdir: Path) -> dict:
    from agency import Agent, agdata, agprof, agskill, agtool
    from agency.configs.agconfig import agconfig, llmconfig, resourcesconfig, sandboxconfig

    work = rdir / "work"
    (work / "acts").mkdir(parents=True, exist_ok=True)
    (work / "gen").mkdir(exist_ok=True)
    os.chmod(work, 0o777)  # the sandbox user writes here too

    def write(rel: str, data: bytes) -> None:
        p = work / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)
        os.chmod(p, 0o644)

    svc = TargetService(task, limits, track, work, rdir, write, container_work=CONTAINER_WORK)
    G = svc.G
    text = prompt.task_text(task, limits, track, G, work=CONTAINER_WORK,
                            weights=f"{CONTAINER_MODEL}/{G.WEIGHTS_FILE}", code_env="sandbox")
    (rdir / "task.txt").write_text(text)

    def wrap(spec: dict, fn):
        return agtool(spec["name"], spec["description"], lambda a: agdata(result=fn(a)), params=spec["parameters"])

    impl = {
        "generate": lambda a: svc.generate(list(a.prompts), int(a.max_tokens), bool(a.thinking), a.adapter or "",
                                           a.to_dict().get("reply_prefix") or ""),
        "inspect": lambda a: svc.inspect(list(a.texts), a.reply_prefix, bool(a.thinking)),
        "inspect_module_inputs": lambda a: svc.inspect_module_inputs(list(a.texts), a.reply_prefix, list(a.modules),
                                                                     bool(a.thinking)),
        "evaluate_candidate": lambda a: svc.evaluate_candidate(a.path),
        "commit_adapter": lambda a: svc.commit_adapter(a.path, a.explanation),
    }
    for name in (*svc.ANALYSIS, "intervene"):
        impl[name] = lambda a, name=name: svc.analysis(name, **a.to_dict())
    tools = [wrap(s, impl[s["name"]]) for s in prompt.tool_schemas(track, G.N_LAYERS, G.HIDDEN)]

    if entry["provider"] == "anthropic":  # Agency's Anthropic client takes the endpoint from the SDK's env var
        os.environ["ANTHROPIC_BASE_URL"] = entry["base_url"]
    cfg = agconfig(
        llmconfig(provider=entry["provider"], base_url=entry["base_url"], model=entry["model"],
                  api_key="via-proxy" if entry.get("vertex_proxy") else os.environ[entry.get("api_key_env", "AZURE_OPENAI_API_KEY")], reasoning_effort=entry.get("effort"),
                  max_completion_tokens=64000),
        sandboxconfig(base_image=SANDBOX_IMAGE, gpu_passthrough=False),
        resourcesconfig(idle_cpus=2),
    )
    cfg.sandbox.add_mount("work", str(work), CONTAINER_WORK, mode="rw")
    cfg.sandbox.add_mount("model", str(G.MODEL_DIR), CONTAINER_MODEL, mode="ro")
    # No web access for any harness: an editor could otherwise look up published fixes (e.g. the Takehi et al. loop
    # direction) and the request would no longer be hint-free. Names cover native, Claude Code, Codex, OpenCode and
    # Kimi CLI (WebSearch, FetchURL).
    from agency.agpolicy import agpolicy
    deny = lambda args: (False, "web access is disabled in this benchmark")  # noqa: E731
    # Antigravity CLI: search_web, read_url_content, its browser tools and its plugin marketplace.
    agy_web = ("search_web", "read_url_content", "open_browser_url", "read_browser_page", "browser_subagent",
               "list_browser_pages", "click_browser_pixel", "capture_browser_screenshot", "capture_browser_console_logs",
               "execute_browser_javascript", "search_marketplace", "browser_click_element", "browser_drag_pixel_to_pixel",
               "browser_get_dom", "browser_get_network_request", "browser_input", "browser_list_network_requests",
               "browser_mouse_down", "browser_mouse_up", "browser_move_mouse", "browser_press_key",
               "browser_refresh_page", "browser_resize_window", "browser_scroll", "browser_scroll_dom",
               "browser_select_option")
    policy = agpolicy(tool_hooks={n: deny for n in ("webfetch", "websearch", "WebFetch", "WebSearch", "web_search",
                                                    "web_fetch", "fetch", "browser", "FetchURL", "SearchWeb",
                                                    "Browser", *agy_web)})
    # A turn that ends without a tool call gets Agency's submit_output reminder and the session resumes. Agency's
    # default allows 10 such resumes, which ended every Kimi K3.1 session within minutes (it ends turns right after
    # announcing its next step); only the wall clock limits a session, the same for every entry.
    skill = agskill(name="write_lora_adapter", prompt=text, add_host_mcp_tools=tools,
                    input_schema=agdata(note=str), output_schema=agdata(summary=str), policy=policy,
                    max_output_schema_retries=100_000)

    proxy = _start_vertex_proxy(entry, rdir) if entry.get("vertex_proxy") else None
    t0 = time.time()
    status, summary = "no_commit", ""
    with agprof.session(rdir / "profile", sample_hz=1, sample_gpu=True, auto_functions=False):
        worker = Agent(f"lsb-{entry['harness']}", agconfig=cfg, harness=entry["harness"])
        try:
            res = worker.run(skill, agdata(note=f"Your workspace is {CONTAINER_WORK}. Begin."))
            deadline, stall_s = t0 + limits["wall_hours"] * 3600, limits.get("stall_minutes", 30) * 60
            seen_commit = None
            while res.is_pending():  # poll: a model call that never returns must not hold the GPU until the deadline
                if svc.committed is not None:  # the session should end on its own; allow it 5 minutes to wrap up
                    seen_commit = seen_commit or time.time()
                    if time.time() - seen_commit > 300:
                        break
                # Vertex queue time (vertex_proxy entries only) does not count toward the wall limit, up to queue_max_hours.
                excused = min(_queue_excess_s(rdir), limits.get("queue_max_hours", 6) * 3600)
                if time.time() > deadline + excused:
                    status = "timeout"
                    break
                if _idle_seconds(rdir, t0) > stall_s:
                    with open(rdir / "stall_stacks.txt", "w") as fh:  # where the agent is stuck, for diagnosis
                        faulthandler.dump_traceback(fh, all_threads=True)
                    _dump_child_stacks(rdir / "stall_stacks.txt")
                    status = "stalled"  # infrastructure, not the editor: rerun
                    break
                time.sleep(30)
            if not res.is_pending():
                d = res.to_dict()
                summary = str(d.get("summary") or d.get("error") or "")[:2000]
        finally:
            try:
                worker.stop(force=True)
            except Exception:  # noqa: BLE001
                pass
            if proxy is not None:
                proxy.terminate()
    if svc.committed is not None:
        status = "committed"
    db = worker.agconfig.data_logger.db_path
    try:
        prof = agprof.summary_table(row_limit=20)
    except Exception as e:  # noqa: BLE001
        prof = f"unavailable: {e}"
    (rdir / "profile_summary.txt").write_text(str(prof))
    try:  # make token totals exact where the only calls without usage were provider rejections
        verify_missing(rdir, str(db))
    except Exception:  # noqa: BLE001
        pass
    stats = svc.adapter_stats()
    svc.close()
    queue_s = round(_queue_excess_s(rdir), 1)
    return {"status": status, "wall_s": round(time.time() - t0), "provider_queue_excluded_s": queue_s, "llm_tokens": profiler_usage(rdir, entry["provider"]),
            "tool_counts": svc.n, "explanation": svc.explanation, "final_message": summary, "adapter": stats,
            "agency_db": db}
