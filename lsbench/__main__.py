"""LoRA-Space Bench CLI (run on the GPU host from the repo root, with secrets.env exported).

  python -m lsbench run --entry astra-minimal --task math_qwen08 --track A --attempt 1
  python -m lsbench score runs/lsbench/<run>          # (run calls this in a fresh process after the session)
  python -m lsbench leaderboard
  python -m lsbench list
"""
from __future__ import annotations

import argparse
import json
import re
import sqlite3
import subprocess
import sys
import time
from pathlib import Path

from . import prompt, spec

FORBIDDEN = [r"pip3? install", r"\buv (pip|add)\b", r"import torch", r"from torch", r"import transformers",
             r"from transformers", r"import jax", r"\.backward\(", r"optim\.(Adam|SGD)",
             r"\b(curl|wget)\s+https?://", r"requests\.get\(", r"urllib\.request\.urlopen\(\s*['\"]https?://"]


def audit(rdir: Path, session: dict) -> dict:
    """Flags commands the rules forbid in anything the editor wrote (transcripts, tool calls, Agency's data log)."""
    texts = []
    for f in ("calls.jsonl", "tool_calls.jsonl"):
        p = rdir / f
        if p.exists():
            texts.append(p.read_text(errors="ignore"))
    db = session.get("agency_db")
    if db and Path(db).exists():
        con = sqlite3.connect(db)
        for (t,) in con.execute("select name from sqlite_master where type='table'"):
            for row in con.execute(f'select * from "{t}"'):
                texts += [str(v) for v in row if isinstance(v, str)]
    blob = "\n".join(texts)
    hits = {pat: len(re.findall(pat, blob)) for pat in FORBIDDEN}
    return {"flags": {k: v for k, v in hits.items() if v}, "clean": not any(hits.values())}


def cmd_run(a) -> None:
    entries, limits = spec.load_entries()
    entry, task = entries[a.entry], spec.load_task(a.task)
    name = spec.run_name(a.entry, a.task, a.track, a.attempt)
    rdir = spec.run_dir(name)
    if (rdir / "result.json").exists() and not a.force:
        print(f"{name}: done already, skipping")
        return
    rdir.mkdir(parents=True, exist_ok=True)
    session_f = rdir / "session.json"
    if not session_f.exists() or a.force:
        runner = __import__("lsbench.run_minimal" if entry["harness"] == "minimal" else "lsbench.run_agency",
                            fromlist=["run"])
        t0 = time.time()
        try:
            session = runner.run(task, entry, limits, a.track, rdir)
        except Exception:  # noqa: BLE001  (record the failure as a run outcome, then stop)
            import traceback
            session = {"status": "error", "error": traceback.format_exc()[-4000:]}
        session["session_s"] = round(time.time() - t0)
        session_f.write_text(json.dumps(session, indent=1, default=str))
    session = json.loads(session_f.read_text())
    score = None
    if session["status"] == "committed" and not a.no_score:
        subprocess.run([sys.executable, "-m", "lsbench", "score", str(rdir)], check=True)
        score = json.loads((rdir / "score.json").read_text())
    gpu_h = (session.get("session_s", 0) + (score or {}).get("score_gpu_s", 0)) / 3600
    result = {"run": name, "entry": a.entry, "label": entry.get("label", a.entry), "task": a.task, "track": a.track,
              "attempt": a.attempt, "settings_hash": spec.settings_hash(task, entry, limits, a.track, prompt.TEMPLATE),
              "rules": spec.RULES_VERSION, "status": session["status"], "score": score,
              "cost": {"gpu_hours": round(gpu_h, 2), "session_hours": round(session.get("session_s", 0) / 3600, 2),
                       "llm_tokens": session.get("llm_tokens")},
              "adapter": session.get("adapter"), "explanation": session.get("explanation"),
              "audit": audit(rdir, session), "finished": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    if not a.no_score:
        (rdir / "result.json").write_text(json.dumps(result, indent=1, default=str))
    print(json.dumps({k: result[k] for k in ("run", "status", "score", "cost", "audit")}, indent=1, default=str))


def cmd_score(a) -> None:
    from .score import score_run
    rdir = Path(a.run_dir)
    task_id = rdir.name.split("__")[1]
    res = score_run(spec.load_task(task_id), rdir)
    (rdir / "score.json").write_text(json.dumps(res, indent=1, default=str))


def cmd_damage(a) -> None:
    """Add the damage check to an already scored run (writes damage.json and updates result.json)."""
    from .score import damage_run
    from .target import load_adapter_npz, load_target_module
    rdir = Path(a.run_dir)
    task = spec.load_task(rdir.name.split("__")[1])
    dmg = damage_run(load_target_module(task["target"]), load_adapter_npz(rdir / "adapter.npz"), rdir.name)
    (rdir / "damage.json").write_text(json.dumps(dmg, indent=1))
    rf = rdir / "result.json"
    if rf.exists():
        r = json.loads(rf.read_text())
        if r.get("score"):
            r["score"]["damage"] = dmg
            rf.write_text(json.dumps(r, indent=1, default=str))
    print(json.dumps(dmg, indent=1))


def cmd_list(_a) -> None:
    entries, limits = spec.load_entries()
    print("entries:", ", ".join(entries))
    print("tasks:", ", ".join(spec.all_tasks()))
    print("limits:", limits)


def main() -> None:
    ap = argparse.ArgumentParser(prog="lsbench")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("run")
    r.add_argument("--entry", required=True)
    r.add_argument("--task", required=True)
    r.add_argument("--track", choices=["A", "B"], default="A")
    r.add_argument("--attempt", type=int, default=1)
    r.add_argument("--no-score", action="store_true")
    r.add_argument("--force", action="store_true")
    s = sub.add_parser("score")
    s.add_argument("run_dir")
    dm = sub.add_parser("damage")
    dm.add_argument("run_dir")
    sub.add_parser("leaderboard")
    sub.add_parser("list")
    a = ap.parse_args()
    if a.cmd == "leaderboard":
        from .leaderboard import build
        build()
    else:
        {"run": cmd_run, "score": cmd_score, "damage": cmd_damage, "list": cmd_list}[a.cmd](a)


if __name__ == "__main__":
    main()
