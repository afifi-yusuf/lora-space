"""Build the benchmark site (one self-contained HTML page) from the run records.
  .venv/bin/python -m lsbench.site            -> site/index.html
Reads results/lsbench/{runs,pilots}/*/ (result.json, session.json, calls.jsonl, tool_calls.jsonl) and task/entry config."""
from __future__ import annotations

import json
import time
from collections import Counter
from pathlib import Path

from . import spec

OUT = spec.ROOT / "site"
SRC = [spec.ROOT / "results/lsbench/runs", spec.ROOT / "results/lsbench/pilots"]


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
    turns = [{"n": c["turn"], "text": (c.get("text") or "")[:700], "tools": [x["tool"] for x in c.get("calls", [])]}
             for c in calls]
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
    return {"id": d.name, "entry": entry_id, "label": e.get("label", entry_id), "model": e.get("model"),
            "harness": e.get("harness"), "task": task_id, "track": track, "attempt": int(att[1:]), "rules": rules,
            "pilot": pilot, "status": sess.get("status"), "scored": bool(score),
            "value": score.get("value"), "normalized": score.get("normalized"),
            "cut_share": raw.get("cut_share"), "mean_tokens": raw.get("mean_tokens"),
            "edit_hours": round((sess.get("session_s") or sess.get("wall_s") or 0) / 3600, 2),
            "gpu_hours": (res or {}).get("cost", {}).get("gpu_hours"),
            "tokens": sess.get("llm_tokens"), "turns_n": sess.get("turns") or len(calls),
            "adapter": sess.get("adapter"), "explanation": sess.get("explanation", ""),
            "refusals": sess.get("provider_refusals", 0), "audit_clean": ((res or {}).get("audit") or {}).get("clean"),
            "tool_counts": dict(Counter(t["tool"] for t in tools)), "candidates": cands, "turns": turns}


def collect() -> dict:
    runs = []
    for i, root in enumerate(SRC):
        for d in sorted(root.glob("*")):
            r = _run(d, pilot=(i == 1))
            if r:
                runs.append(r)
    tasks = {}
    for t in spec.all_tasks():
        task = spec.load_task(t)
        tasks[t] = {"request": " ".join(task["request"].split()), "judged": " ".join(task["judged"].split()),
                    "metric": task["score"]["metric"], "base": task["score"]["base"],
                    "higher_is_better": task["score"]["higher_is_better"], "references": task["score"].get("references", {}),
                    "reference_cost": task["score"].get("reference_cost", {})}
    _, limits = spec.load_entries()
    return {"generated": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()), "rules": spec.RULES_VERSION,
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
