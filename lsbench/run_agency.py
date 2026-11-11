"""Agency harnesses (native, codex, claude_code, ...): the editor runs inside Agency's Docker sandbox (no torch, no GPU,
weights mounted read-only); the model tools are host MCP tools backed by the TargetService on the GPU host."""
from __future__ import annotations

import json
import os
import sqlite3
import time
from pathlib import Path

from . import prompt
from .target import TargetService

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
        "generate": lambda a: svc.generate(list(a.prompts), int(a.max_tokens), bool(a.thinking), a.adapter or ""),
        "inspect": lambda a: svc.inspect(list(a.texts), a.reply_prefix, bool(a.thinking)),
        "inspect_module_inputs": lambda a: svc.inspect_module_inputs(list(a.texts), a.reply_prefix, list(a.modules),
                                                                     bool(a.thinking)),
        "evaluate_candidate": lambda a: svc.evaluate_candidate(a.path),
        "commit_adapter": lambda a: svc.commit_adapter(a.path, a.explanation),
    }
    tools = [wrap(s, impl[s["name"]]) for s in prompt.tool_schemas(track, G.N_LAYERS, G.HIDDEN)]

    if entry["provider"] == "anthropic":  # Agency's Anthropic client takes the endpoint from the SDK's env var
        os.environ["ANTHROPIC_BASE_URL"] = entry["base_url"]
    cfg = agconfig(
        llmconfig(provider=entry["provider"], base_url=entry["base_url"], model=entry["model"],
                  api_key=os.environ["AZURE_OPENAI_API_KEY"], reasoning_effort=entry.get("effort"),
                  max_completion_tokens=64000),
        sandboxconfig(base_image=SANDBOX_IMAGE, gpu_passthrough=False),
        resourcesconfig(idle_cpus=2),
    )
    cfg.sandbox.add_mount("work", str(work), CONTAINER_WORK, mode="rw")
    cfg.sandbox.add_mount("model", str(G.MODEL_DIR), CONTAINER_MODEL, mode="ro")
    skill = agskill(name="write_lora_adapter", prompt=text, add_host_mcp_tools=tools,
                    input_schema=agdata(note=str), output_schema=agdata(summary=str))

    t0 = time.time()
    status, summary = "no_commit", ""
    with agprof.session(rdir / "profile", sample_hz=1, sample_gpu=True, auto_functions=False):
        worker = Agent(f"lsb-{entry['harness']}", agconfig=cfg, harness=entry["harness"])
        try:
            res = worker.run(skill, agdata(note=f"Your workspace is {CONTAINER_WORK}. Begin."))
            res.wait(timeout=limits["wall_hours"] * 3600)
            d = res.to_dict()
            summary = str(d.get("summary") or d.get("error") or "")[:2000]
            if svc.committed is None and time.time() - t0 >= limits["wall_hours"] * 3600 - 5:
                status = "timeout"
        finally:
            try:
                worker.stop(force=True)
            except Exception:  # noqa: BLE001
                pass
    if svc.committed is not None:
        status = "committed"
    db = worker.agconfig.data_logger.db_path
    try:
        prof = agprof.summary_table(row_limit=20)
    except Exception as e:  # noqa: BLE001
        prof = f"unavailable: {e}"
    (rdir / "profile_summary.txt").write_text(str(prof))
    stats = svc.adapter_stats()
    svc.close()
    return {"status": status, "wall_s": round(time.time() - t0), "llm_tokens": _usage_from_db(db),
            "tool_counts": svc.n, "explanation": svc.explanation, "final_message": summary, "adapter": stats,
            "agency_db": db}
