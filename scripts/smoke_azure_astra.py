"""Smoke test: GPT-6 Astra on Azure Foundry via the OpenAI-compatible Responses API.

Checks the three things the LSO harness (Agency + Codex) depends on:
  1. a basic Responses call works against the Azure v1 endpoint;
  2. which reasoning-effort levels are accepted (the paper used "max");
  3. stateless reasoning round-trip: with store=False, the response returns
     encrypted reasoning that can be sent back on the next turn.

Usage:  uv run --with openai python scripts/smoke_azure_astra.py
Reads AZURE_OPENAI_API_KEY from ../secrets.env (never printed).
"""
from __future__ import annotations

import os
import time
from pathlib import Path

from openai import OpenAI

ENDPOINT = "https://principle.openai.azure.com/openai/v1"
DEPLOYMENT = "gpt-6-astra"
SECRETS = Path(__file__).resolve().parent.parent / "secrets.env"


def load_key() -> str:
    for line in SECRETS.read_text().splitlines():
        line = line.strip().removeprefix("export ").strip()
        if line.startswith("AZURE_OPENAI_API_KEY="):
            return line.split("=", 1)[1].strip().strip('"').strip("'")
    raise SystemExit(f"AZURE_OPENAI_API_KEY not found in {SECRETS}")


def usage_str(r) -> str:
    u = r.usage
    rt = getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", None)
    return f"in={u.input_tokens} out={u.output_tokens} reasoning={rt}"


client = OpenAI(base_url=ENDPOINT, api_key=os.environ.get("AZURE_OPENAI_API_KEY") or load_key())
results = {}

# 1. Basic call
t = time.time()
r = client.responses.create(model=DEPLOYMENT, input="Reply with exactly: OK", reasoning={"effort": "low"})
print(f"[1] basic: status={r.status} text={r.output_text!r} {usage_str(r)} {time.time() - t:.1f}s")
results["basic"] = r.status == "completed"

# 2. Reasoning effort levels
for effort in ["max", "xhigh", "high"]:
    t = time.time()
    try:
        r = client.responses.create(
            model=DEPLOYMENT,
            input="What is 17 * 23? Answer with just the number.",
            reasoning={"effort": effort},
            max_output_tokens=8000,
        )
        print(f"[2] effort={effort}: accepted, status={r.status} text={r.output_text!r} {usage_str(r)} {time.time() - t:.1f}s")
        results[f"effort_{effort}"] = True
    except Exception as e:  # noqa: BLE001
        print(f"[2] effort={effort}: REJECTED ({type(e).__name__}: {str(e)[:200]})")
        results[f"effort_{effort}"] = False

# 3. Stateless encrypted-reasoning round trip (what Agency's openai_responses backend does)
effort = "max" if results.get("effort_max") else "xhigh" if results.get("effort_xhigh") else "high"
turn1_input = [{"role": "user", "content": "Pick a secret two-digit prime and tell me only its digit sum."}]
r1 = client.responses.create(
    model=DEPLOYMENT,
    input=turn1_input,
    reasoning={"effort": effort, "summary": "auto"},
    include=["reasoning.encrypted_content"],
    store=False,
    max_output_tokens=8000,
)
reasoning_items = [it for it in r1.output if it.type == "reasoning"]
has_enc = any(getattr(it, "encrypted_content", None) for it in reasoning_items)
print(f"[3] turn 1 (effort={effort}): status={r1.status} text={r1.output_text!r} "
      f"reasoning_items={len(reasoning_items)} encrypted_content={'yes' if has_enc else 'NO'} {usage_str(r1)}")
results["encrypted_reasoning_returned"] = has_enc

try:
    turn2_input = turn1_input + [it.model_dump(exclude_none=True) for it in r1.output] + [
        {"role": "user", "content": "Now reveal the prime you picked."}
    ]
    r2 = client.responses.create(
        model=DEPLOYMENT,
        input=turn2_input,
        reasoning={"effort": effort},
        include=["reasoning.encrypted_content"],
        store=False,
        max_output_tokens=8000,
    )
    print(f"[3] turn 2 (reasoning sent back): status={r2.status} text={r2.output_text!r} {usage_str(r2)}")
    results["reasoning_round_trip"] = r2.status == "completed"
except Exception as e:  # noqa: BLE001
    print(f"[3] turn 2: FAILED ({type(e).__name__}: {str(e)[:300]})")
    results["reasoning_round_trip"] = False

print("\nSUMMARY")
for k, v in results.items():
    print(f"  {'PASS' if v else 'FAIL'}  {k}")
