"""Build the benchmark site (one self-contained HTML page) from the run records.
  .venv/bin/python -m lsbench.site            -> site/index.html
Reads results/lsbench/{runs,pilots}/*/ (result.json, session.json, calls.jsonl, tool_calls.jsonl) and task/entry config."""
from __future__ import annotations

import ast
import calendar
import json
import re
import struct
import zipfile
import zlib
from array import array
import time
from collections import Counter
from pathlib import Path

from . import spec
from .usage import profiler_usage

OUT = spec.ROOT / "site"
SRC = [spec.ROOT / "results/lsbench/runs", spec.ROOT / "results/lsbench/pilots"]
# Harnesses whose entries are kept on disk but left off the published page.
UNLISTED = {"opencode"}


def _jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text().splitlines() if l.strip()] if p.exists() else []


def _run(d: Path, pilot: bool) -> dict | None:
    sess_f = d / "session.json"
    if not sess_f.exists():
        return None
    sess = json.loads(sess_f.read_text())
    res = json.loads((d / "result.json").read_text()) if (d / "result.json").exists() else None
    entry_id, task_id, track, att = d.name.split("__")[:4]
    rules = (res or {}).get("rules") or (d.name.split("__")[4] if len(d.name.split("__")) > 4 else "lsbench-v0.3")
    rules = rules if rules.startswith("lsbench") else f"lsbench-{rules}"
    score = (res or {}).get("score") or {}
    raw = score.get("raw") or {}
    calls = _jsonl(d / "calls.jsonl")
    tools = _jsonl(d / "tool_calls.jsonl")
    if calls:  # minimal loop: the editor's own notes per turn
        turns = [{"n": c["turn"], "text": _clip(c.get("text") or "", 700), "tools": [x["tool"] for x in c.get("calls", [])]}
                 for c in calls]
    else:  # Agency harnesses: the model-tool timeline (time into the session, tool, first line of the result)
        t0 = _ts(tools[0]["t"]) if tools else 0
        turns = [{"n": i + 1, "min": round((_ts(t["t"]) - t0) / 60), "tools": [t["tool"] + _argnote(t)],
                  "text": _result(t["output"])} for i, t in enumerate(tools)]
    cands = []
    for t in tools:
        if t["tool"] in ("evaluate_candidate", "intervene") or (t["tool"] == "generate" and t["args"].get("adapter")):
            out = t["output"]
            try:
                parsed = json.loads(out.split("\n")[0]) if t["tool"] == "evaluate_candidate" else None
            except json.JSONDecodeError:
                parsed = None
            cands.append({"tool": t["tool"], "what": t["args"].get("path") or t["args"].get("adapter") or "interventions",
                          "dev_acc": (parsed or {}).get("dev_acc"), "finished": (parsed or {}).get("finished"),
                          "mean_tokens": (parsed or {}).get("mean_tokens"), "note": out[:240]})
    entries, _ = spec.load_entries()
    e = entries.get(entry_id, {})
    tokens = dict(sess.get("llm_tokens") or {})
    if (d / "profile/summary.json").exists():  # Agency harnesses: recompute with the current accounting rules
        tokens = profiler_usage(d, e.get("provider", ""))
        if tokens.get("input") is None and e.get("provider") == "anthropic":
            tokens["note"] = "input not recorded"
    dmg = score.get("damage") or {}
    late_min = None
    vq = [q for q in _jsonl(d / "vertex_queue.jsonl") if q.get("path") != "manual_extension"]
    queue_min = round(sum(q.get("excess_s", 0) for q in vq) / 60) or None  # provider queue time excluded from the limit
    ext = d / "time_extension.json"
    commit = next((t for t in tools if t["tool"] == "commit_adapter"), None)
    if ext.exists() and commit:  # the session ran past its limit by the user's decision; how late did the commit land?
        x = json.loads(ext.read_text())
        queue = sum(q.get("excess_s", 0) for q in _jsonl(d / "vertex_queue.jsonl") if q.get("path") != "manual_extension")
        limit = calendar.timegm(time.strptime(x["original_cutoff_utc"], "%Y-%m-%dT%H:%M:%SZ")) - x.get("excused_queue_s_at_extension", 0) + queue
        late = calendar.timegm(time.strptime(commit["t"][:19], "%Y-%m-%dT%H:%M:%S")) - limit
        late_min = round(late / 60) if late > 0 else None
    return {"id": d.name, "entry": entry_id, "label": e.get("label", entry_id), "model": e.get("model"),
            "harness": e.get("harness"), "task": task_id, "track": track, "attempt": int(att[1:]), "rules": rules,
            "pilot": pilot or entry_id == "astra-minimal", "status": (res or {}).get("status") or sess.get("status"),
            "scored": bool(score), "provider": e.get("provider"), "effort": e.get("effort"),
            "damage": {"flagged": dmg.get("flagged") or [], "drop": dmg.get("drop") or {}} if dmg else None,
            "final_message": _final(sess.get("final_message") or ""),
            "value": score.get("value"), "normalized": score.get("normalized"),
            "cut_share": raw.get("cut_share"), "mean_tokens": raw.get("mean_tokens"),
            "edit_hours": round((sess.get("session_s") or sess.get("wall_s") or 0) / 3600, 2),
            "gpu_hours": (res or {}).get("cost", {}).get("gpu_hours"),
            "tokens": tokens, "turns_n": sess.get("turns") or len(calls) or len(tools),
            "adapter": sess.get("adapter"), "edit_map": _edit_map(d), "explanation": _whole(sess.get("explanation") or ""),
            "late_min": late_min, "queue_min": queue_min, "refusals": sess.get("provider_refusals", 0), "audit_clean": ((res or {}).get("audit") or {}).get("clean"),
            "tool_counts": dict(Counter(t["tool"] for t in tools)), "candidates": cands, "turns": turns}


def _clip(text: str, n: int) -> str:
    """Cut at the last sentence or line end before n characters, never mid-word."""
    text = (text or "").strip()
    if len(text) <= n:
        return text
    cut = max(text.rfind(". ", 0, n), text.rfind(".\n", 0, n), text.rfind("\n", 0, n))
    if cut < n // 2:
        cut = text.rfind(" ", 0, n)
    return text[:cut + 1].rstrip() + " …"


def _npy(raw: bytes) -> tuple[tuple, array]:
    """A .npy member of an adapter file, read without numpy: its shape and its values in row order."""
    major = raw[6]
    hlen, start = (struct.unpack("<H", raw[8:10])[0], 10) if major == 1 else (struct.unpack("<I", raw[8:12])[0], 12)
    head = ast.literal_eval(raw[start:start + hlen].decode("latin1"))
    code = {"<f8": "d", "<f4": "f"}[head["descr"]]
    vals = array(code)
    vals.frombytes(raw[start + hlen:])
    if head.get("fortran_order"):
        raise ValueError("fortran-ordered adapter array")
    return tuple(head["shape"]), vals


def _edit_map(d: Path, rows: int = 32, max_cols: int = 128) -> list[dict] | None:
    """The committed adapter, binned for drawing: per edited matrix, the mean of B over `rows` row bins and of A over
    column bins sized to keep cells square. Over a cell, the mean of the weight change is the sum over rank of the
    products of the two bin means (before the 8-bit rounding applied here)."""
    f = d / "adapter.npz"
    if not f.exists():
        return None
    out = []
    try:
        with zipfile.ZipFile(f) as z:
            names = sorted({n.rsplit("::", 1)[0] for n in z.namelist()})
            for name in names:
                (n_out, rank), B = _npy(z.read(f"{name}::B.npy"))
                (rank_a, n_in), A = _npy(z.read(f"{name}::A.npy"))
                if rank != rank_a or n_out < rows:
                    return None
                cols = max(rows, min(max_cols, round(rows * n_in / n_out)))
                def mean(vals):
                    vals = list(vals)
                    return sum(vals) / len(vals) if vals else 0.0
                bm = [[mean(B[i * rank + k] for i in range(r * n_out // rows, (r + 1) * n_out // rows))
                       for r in range(rows)] for k in range(rank)]
                am = [[mean(A[k * n_in + j] for j in range(c * n_in // cols, (c + 1) * n_in // cols))
                       for c in range(cols)] for k in range(rank)]
                sb = max((abs(v) for row in bm for v in row), default=0) or 1.0
                sa = max((abs(v) for row in am for v in row), default=0) or 1.0
                out.append({"m": name, "shape": [n_out, n_in], "rank": rank,
                            "b": [[round(127 * v / sb) for v in row] for row in bm],
                            "a": [[round(127 * v / sa) for v in row] for row in am]})
    except (KeyError, ValueError, IndexError, SyntaxError, zipfile.BadZipFile, zlib.error, struct.error):
        return None
    return out or None


def _whole(text: str) -> str:
    """Session records cap long messages mid-sentence. Drop the unfinished tail instead of showing half a word."""
    text = text.strip()
    if not text or text[-1] in ".!?)`\"*:":
        return text
    cut = max(text.rfind(". "), text.rfind(".\n"), text.rfind(".)"), text.rfind(":\n"))
    kept = text[:cut + 1].rstrip() if cut > len(text) // 2 else text
    while kept.rstrip("*").endswith(":"):  # a heading left with nothing under it
        end = max(kept.rfind(". ", 0, len(kept) - 1), kept.rfind(".\n", 0, len(kept) - 1), kept.rfind("\n", 0, len(kept) - 1))
        if end < len(kept) // 2:
            break
        kept = kept[:end + 1].rstrip()
    kept = re.sub(r"\n\s*(?:\d+[.)]|[-*•])\s*$", "", kept).rstrip()  # an empty list item left at the end
    return kept + " (The session record ends here.)"


def _final(text: str) -> str:
    """The editor's closing message. A harness failure leaves a traceback or an error line here; say so plainly."""
    text = text.strip()
    if text.startswith("Traceback"):
        kind = text.splitlines()[-1].split(":")[0].strip() or "an error"
        return f"The harness stopped with an error ({kind}) before the editor finished. This was a fault in the run, not a choice the editor made."
    if text.lower().startswith("structured output"):
        return "The harness could not read the editor’s closing summary, so none was recorded for this run."
    return _whole(_clip(text, 5000))


def _result(out: str) -> str:
    """One short line saying what a tool call returned."""
    line = str(out).split("\n")[0].replace("\\n", " ")
    line = re.sub(r"^saved \S+\s*", "", line).replace("Full replies are in the file; below, a preview of each.", "")
    line = re.sub(r"\s+", " ", line).strip().strip(":. ")
    if line.startswith("(") and line.endswith(")") and line.count("(") == line.count(")"):
        line = line[1:-1]
    return line if len(line) <= 96 else line[:96].rsplit(" ", 1)[0] + " …"


def _ts(t: str) -> float:
    return time.mktime(time.strptime(t[:19], "%Y-%m-%dT%H:%M:%S"))


def _argnote(t: dict) -> str:
    a = t.get("args") or {}
    if t["tool"] == "generate":
        return f" ({len(a.get('prompts') or [])} prompts{', thinking' if a.get('thinking') else ''})"
    if t["tool"] == "commit_adapter":
        return ""
    site = a.get("site") or a.get("module") or a.get("layer")
    return f" ({site})" if site not in (None, "") else ""


def collect() -> dict:
    runs = []
    for i, root in enumerate(SRC):
        for d in sorted(root.glob("*")):
            r = _run(d, pilot=(i == 1))
            if r and r["harness"] not in UNLISTED:
                runs.append(r)
    tasks = {}
    for t in spec.all_tasks():
        task = spec.load_task(t)
        tasks[t] = {"target": task.get("target"), "thinking": task.get("default_thinking"),
                    "request": " ".join(task["request"].split()), "judged": " ".join(task["judged"].split()),
                    "metric": task["score"]["metric"], "base": task["score"]["base"],
                    "higher_is_better": task["score"]["higher_is_better"], "references": task["score"].get("references", {}),
                    "reference_cost": task["score"].get("reference_cost", {})}
    entries, limits = spec.load_entries()
    roster = [{k: e.get(k) for k in ("id", "label", "model", "harness", "effort", "provider")} for e in entries.values()
              if e.get("harness") not in UNLISTED]
    return {"entries": roster, "generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "rules": spec.RULES_VERSION,
            "limits": limits, "tasks": tasks, "runs": runs}


def build() -> Path:
    data = collect()
    tpl = (spec.PKG / "site_template.html").read_text()
    OUT.mkdir(exist_ok=True)
    out = OUT / "index.html"
    out.write_text(tpl.replace("/*__LSB_DATA__*/null", json.dumps(data, separators=(",", ":")).replace("</", "<\\/")))
    print(f"wrote {out} ({out.stat().st_size // 1024} KB, {len(data['runs'])} runs)")
    return out


if __name__ == "__main__":
    build()
