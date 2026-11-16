"""Recover Anthropic prompt-cache token counts for runs recorded before Agency's profiler kept them.
Agency's data log (session.json -> agency_db) stores each call's full usage block; sum it per run and write
profile/usage_recovered.json, which lsbench.usage prefers over the profiler summary.
  .venv/bin/python -m lsbench.recover_usage runs/lsbench/<run> [...]"""
from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

KEYS = ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens", "output_tokens")


def _find_usage(x):
    if isinstance(x, dict):
        if "cache_read_input_tokens" in x:
            return x
        x = list(x.values())
    if isinstance(x, list):
        for v in x:
            u = _find_usage(v)
            if u:
                return u
    return None


def recover(rdir: Path) -> dict | None:
    db = json.loads((rdir / "session.json").read_text()).get("agency_db")
    if not db or not Path(db).exists():
        return None
    con = sqlite3.connect(db)
    exchanges = con.execute("select count(*) from exchanges").fetchone()[0]
    tot = dict.fromkeys(KEYS, 0)
    n = 0
    for (p,) in con.execute("select payload from message_block_lookup where cast(payload as text) like '%cache_read_input_tokens%'"):
        u = _find_usage(json.loads(p))
        if u:
            n += 1
            for k in KEYS:
                tot[k] += int(u.get(k) or 0)
    out = {"calls_with_usage": n, "exchanges": exchanges, "complete": n == exchanges,
           "input": tot["input_tokens"] + tot["cache_read_input_tokens"] + tot["cache_creation_input_tokens"],
           "cache_read": tot["cache_read_input_tokens"], "cache_write": tot["cache_creation_input_tokens"],
           "uncached_input": tot["input_tokens"], "output": tot["output_tokens"], "source": "agency data log"}
    (rdir / "profile").mkdir(exist_ok=True)
    (rdir / "profile/usage_recovered.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(Path(a).name, recover(Path(a)))
