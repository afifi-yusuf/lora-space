"""Make a run's token counts exact from Agency's data log (session.json -> agency_db), on the box that ran it.

* recover(): Anthropic prompt-cache counts for runs recorded before Agency's profiler kept them, summed from each
  call's usage block -> profile/usage_recovered.json, which lsbench.usage prefers over the profiler summary.
* verify_missing(): the profiler leaves token totals open when any model call reported no usage. Each such call is
  checked against the data log; one the provider refused (overload, rate limit) before streaming any output
  used no tokens.
  When every one checks out, profile/usage_verified.json lets lsbench.usage report the totals as exact.
  .venv/bin/python -m lsbench.recover_usage runs/lsbench/<run> [...]"""
from __future__ import annotations

import json
import re
import sqlite3
import sys
from collections import Counter
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
    if not n:  # no Anthropic usage blocks: nothing to recover
        return None
    (rdir / "profile").mkdir(exist_ok=True)
    (rdir / "profile/usage_recovered.json").write_text(json.dumps(out, indent=1))
    return out


# Provider errors that refuse a request before the model runs. An output-side content filter ("Response content
# blocked") is not one: the model may have generated the blocked tokens.
_REFUSED = re.compile(r"high demand|exceeds the maximum usage size|rate limit|too many requests|\b429\b|\b503\b", re.I)


def verify_missing(rdir: Path, db: "str | None" = None) -> dict | None:
    pdb = rdir / "profile/profile_data.sqlite3"
    db = db or json.loads((rdir / "session.json").read_text()).get("agency_db")
    if not pdb.exists() or not db or not Path(db).exists():
        return None
    attempts = [json.loads(a) for (a,) in sqlite3.connect(pdb).execute(
        "select attributes from spans where span_name like 'llm:attempt%'")]
    missing = [a for a in attempts if a.get("input_tokens") is None or a.get("output_tokens") is None]
    if not missing:
        return None
    con = sqlite3.connect(db)
    errors = dict(con.execute("select call_label, term_message from exchanges where type = 'llm_stream_error'"))
    rejected, unverified = Counter(), []
    for a in missing:
        label = a.get("call_label")
        error = (errors.get(label) or "").split("\u2717", 1)[-1].strip()
        streamed = con.execute("select count(*) from stream_deltas where call_label = ?", (label,)).fetchone()[0]
        if a.get("outcome") != "success" and a.get("ttft_ms") is None and not streamed and _REFUSED.search(error):
            rejected[error[:200]] += 1
        else:
            unverified.append({"call_label": label, "outcome": a.get("outcome"), "streamed_deltas": streamed,
                               "error": error[:200]})
    out = {"missing_usage_calls": len(missing), "rejected_before_output": sum(rejected.values()),
           "complete": not unverified, "rejections": rejected.most_common(), "unverified": unverified,
           "source": "agency data log"}
    (rdir / "profile/usage_verified.json").write_text(json.dumps(out, indent=1))
    return out


if __name__ == "__main__":
    for a in sys.argv[1:]:
        print(Path(a).name, recover(Path(a)), verify_missing(Path(a)))
