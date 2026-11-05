"""API-only harness: GPT-6 Astra on Azure via the Responses API, with a run_python tool. No framework.

Stateless (store=False) with encrypted reasoning carried between turns. Logs every model call and tool run.
Usage: python run_api.py <root> <effort> [max_turns]
  <root> holds task/ (mounted at /workspace/task) and truth.json; results go to <root>/runs/api_<ts>/.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from openai import OpenAI

sys.path.insert(0, str(Path(__file__).parent))
from score import score  # noqa: E402

ENDPOINT = "https://principle.openai.azure.com/openai/v1"
MODEL = "gpt-6-astra"
TOOLS = [
    {"type": "function", "name": "run_python",
     "description": "Run a Python 3 script (numpy available) and return its stdout and stderr. "
                    "Each call is a fresh process; save intermediate results to files if needed.",
     "parameters": {"type": "object", "properties": {"code": {"type": "string"}},
                    "required": ["code"], "additionalProperties": False}, "strict": True},
    {"type": "function", "name": "submit",
     "description": "Submit the final answer. Call exactly once when done.",
     "parameters": {"type": "object", "properties": {
         "rank": {"type": "integer"}, "scale": {"type": "number"},
         "columns": {"type": "string", "description": "comma-separated column indices"},
         "notes": {"type": "string"}},
         "required": ["rank", "scale", "columns", "notes"], "additionalProperties": False}, "strict": True},
]


def run_python(code: str, timeout: int = 120) -> tuple[str, float]:
    t = time.time()
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
    try:
        p = subprocess.run([sys.executable, f.name], capture_output=True, text=True, timeout=timeout, cwd="/workspace/task")
        out = (p.stdout + ("\n[stderr]\n" + p.stderr if p.stderr else ""))[-20000:]
    except subprocess.TimeoutExpired:
        out = f"[timed out after {timeout}s]"
    finally:
        os.unlink(f.name)
    return out, time.time() - t


def main(root: str, effort: str, max_turns: int = 30) -> None:
    root_p = Path(root)
    run_dir = root_p / "runs" / f"api_{time.strftime('%Y%m%dT%H%M%S')}"
    run_dir.mkdir(parents=True)
    log = open(run_dir / "calls.jsonl", "w")
    client = OpenAI(base_url=ENDPOINT, api_key=os.environ["AZURE_OPENAI_API_KEY"])
    task = (Path(__file__).parent / "task.md").read_text()
    items: list = [{"role": "user", "content": task}]
    t0, answer, totals = time.time(), None, {"input": 0, "cached": 0, "output": 0, "reasoning": 0, "tool_s": 0.0}
    for turn in range(1, max_turns + 1):
        t = time.time()
        r = client.responses.create(model=MODEL, input=items, tools=TOOLS, reasoning={"effort": effort, "summary": "auto"},
                                    include=["reasoning.encrypted_content"], store=False, max_output_tokens=32000)
        dt = time.time() - t
        u = r.usage
        cached = getattr(getattr(u, "input_tokens_details", None), "cached_tokens", 0) or 0
        reasoning = getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", 0) or 0
        totals["input"] += u.input_tokens; totals["cached"] += cached
        totals["output"] += u.output_tokens; totals["reasoning"] += reasoning
        items += [it.model_dump(exclude_none=True) for it in r.output]
        calls = [it for it in r.output if it.type == "function_call"]
        rec = {"turn": turn, "latency_s": round(dt, 2), "status": r.status, "input": u.input_tokens, "cached": cached,
               "output": u.output_tokens, "reasoning": reasoning, "tool_calls": [c.name for c in calls], "tools": []}
        for c in calls:
            args = json.loads(c.arguments)
            if c.name == "submit":
                answer = args
                out = "submitted"
            else:
                out, tdt = run_python(args["code"])
                totals["tool_s"] += tdt
                rec["tools"].append({"code": args["code"], "output": out[:4000], "seconds": round(tdt, 2)})
            items.append({"type": "function_call_output", "call_id": c.call_id, "output": out})
        log.write(json.dumps(rec) + "\n"); log.flush()
        print(f"turn {turn}: {dt:.1f}s in={u.input_tokens} cached={cached} out={u.output_tokens} tools={rec['tool_calls']}")
        if answer is not None or not calls:
            break
    wall = time.time() - t0
    result = {"harness": "api-only", "effort": effort, "turns": turn, "wall_s": round(wall, 1), "tokens": totals,
              "answer": answer, "score": score(root_p, **{k: answer[k] for k in ("rank", "scale", "columns")}) if answer else None}
    (run_dir / "result.json").write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 30)
