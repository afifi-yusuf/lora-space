"""Editor token usage from Agency's profiler summary (profile/summary.json), shared by the runner and the site."""
from __future__ import annotations

import json
from pathlib import Path


def profiler_usage(rdir: Path, provider: str = "") -> dict:
    """`input` is total prompt tokens. Anthropic reports prompt-cache reads and writes on top of input_tokens, so they
    are added back; OpenAI-style input_tokens already include cached tokens. When some calls carried no usage, the
    profiler leaves the totals empty: fall back to the reported partial sums and flag them as lower bounds, unless every call without usage is verified as rejected before any output."""
    try:
        m = json.loads((Path(rdir) / "profile/summary.json").read_text())["llm_metrics"]
    except Exception as e:  # noqa: BLE001
        return {"error": f"profiler summary unavailable: {e}"}
    missing = m.get("usage_missing_attempts") or 0
    inp = m.get("input_tokens") if m.get("input_tokens") is not None else m.get("reported_input_tokens")
    out = m.get("output_tokens") if m.get("output_tokens") is not None else m.get("reported_output_tokens")
    cr, cw = m.get("cache_read_tokens"), m.get("cache_write_tokens")
    if provider == "anthropic" and inp is not None:
        if cr is None:  # recorded before the profiler counted cache tokens: use the data-log recovery if present
            rec = Path(rdir) / "profile/usage_recovered.json"
            if rec.exists():
                r = json.loads(rec.read_text())
                inp, cr, cw, out = r["input"], r["cache_read"], r["cache_write"], r["output"]
                missing = 0 if r.get("complete") else max(missing, 1)
            else:
                inp = None
        else:
            inp = inp + cr + (cw or 0)
    rejected = 0
    ver = Path(rdir) / "profile/usage_verified.json"
    if missing and ver.exists():  # calls the provider rejected before any output used no tokens (lsbench.recover_usage)
        v = json.loads(ver.read_text())
        if v.get("complete") and v.get("missing_usage_calls") == missing:
            rejected, missing = v["rejected_before_output"], 0
    return {"input": inp, "output": out, "cache_read": cr, "cache_write": cw, "calls": m.get("calls"),
            "failed_calls": m.get("failed_calls"), "rejected_calls": rejected, "usage_missing_calls": missing,
            "lower_bound": bool(missing),
            "llm_wait_s": round((m.get("total_wait_ms") or 0) / 1000, 1)}
