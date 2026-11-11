"""Minimal harness: our own tool loop over the Responses API (GPT-6 Astra on Azure). The editor's code runs as the
unprivileged `editor` user (scripts/m05_editor.py sandbox) with numpy/scipy/safetensors and no torch.
Anthropic models are run through Agency (claude_code / native), not here."""
from __future__ import annotations

import json
import os
import subprocess
import sys
import time
from pathlib import Path

from openai import BadRequestError, OpenAI

from . import prompt
from .spec import ROOT
from .target import TargetService


REDACTED = ("[this tool output was removed from the conversation after the provider's content filter flagged the "
            "conversation; the full results are still in the file named on the first line]")


def _redact_outputs(items: list, keep_last: int) -> int:
    """Replace the model-tool outputs (generations, inspections) in the history, except the last `keep_last`, with
    their first line (the saved file name) and a notice. Returns how many were replaced."""
    idx = [i for i, it in enumerate(items) if it.get("type") == "function_call_output"
           and str(it.get("output", "")).startswith(("saved gen/", "saved acts/"))
           and REDACTED not in str(it.get("output", ""))]
    for i in idx[: max(0, len(idx) - keep_last)]:
        items[i]["output"] = str(items[i]["output"]).split("\n", 1)[0] + "\n" + REDACTED
    return max(0, len(idx) - keep_last)


def run(task: dict, entry: dict, limits: dict, track: str, rdir: Path) -> dict:
    assert entry["provider"] == "openai_responses", "the minimal loop speaks the Responses API only"
    sys.path.insert(0, str(ROOT / "scripts"))
    os.environ["LSO_TARGET"] = task["target"]
    import m05_editor as E  # editor-user sandbox (run_python) and its work root

    work = E.WORK_ROOT / rdir.name / "work"
    sh = lambda *c: subprocess.run(["sudo", *c], check=True)  # noqa: E731
    sh("mkdir", "-p", str(work / "acts"), str(work / "gen"))

    def write(rel: str, data: bytes) -> None:
        tmp = rdir / "tmp_write"
        tmp.write_bytes(data)
        sh("install", "-D", "-o", E.EDITOR_USER, "-g", E.EDITOR_USER, "-m", "644", str(tmp), str(work / rel))

    svc = TargetService(task, limits, track, work, rdir, write)
    G = svc.G
    sh("install", "-m", "444", str(G.MODEL_DIR / G.WEIGHTS_FILE), str(work / "model.safetensors"))
    sh("chown", "-R", f"{E.EDITOR_USER}:{E.EDITOR_USER}", str(E.WORK_ROOT / rdir.name))
    sh("chmod", "755", str(E.WORK_ROOT), str(E.WORK_ROOT / rdir.name), str(work), str(work / "acts"), str(work / "gen"))

    text = prompt.task_text(task, limits, track, G, work=str(work), weights="model.safetensors (in your workspace)",
                            code_env="run_python")
    (rdir / "task.txt").write_text(text)
    tools = [{"type": "function", "name": "run_python",
              "description": "Run a Python 3 script in your workspace (numpy, scipy, safetensors; no torch). Each call is "
                             "a fresh process; save intermediate results to files. Output is cut to 20,000 chars.",
              "parameters": {"type": "object", "properties": {"code": {"type": "string"}}, "required": ["code"],
                             "additionalProperties": False}, "strict": True}]
    tools += [{"type": "function", **s, "strict": True} for s in prompt.tool_schemas(track, G.N_LAYERS, G.HIDDEN)]
    client = OpenAI(base_url=entry["base_url"], api_key=os.environ["AZURE_OPENAI_API_KEY"])
    items: list = [{"role": "user", "content": text}]
    log = open(rdir / "calls.jsonl", "w")
    tokens = {"input": 0, "cached": 0, "output": 0, "reasoning": 0}
    t0, turn, deadline = time.time(), 0, time.time() + limits["wall_hours"] * 3600
    status = "no_commit"
    refusals: list = []
    try:
        while time.time() < deadline:
            turn += 1
            r = None
            for attempt in range(3):
                try:
                    r = client.responses.create(model=entry["model"], input=items, tools=tools,
                                                reasoning={"effort": entry["effort"], "summary": "auto"},
                                                include=["reasoning.encrypted_content"], store=False,
                                                max_output_tokens=64000)
                    break
                except BadRequestError as e:  # provider content filter on the accumulated conversation
                    if "flagged" not in str(e):
                        raise
                    n = _redact_outputs(items, keep_last=0 if attempt else 2)
                    refusals.append({"turn": turn, "attempt": attempt, "redacted_outputs": n, "error": str(e)[:300]})
                    (rdir / "provider_refusals.json").write_text(json.dumps(refusals, indent=1))
            if r is None:
                status = "provider_refusal"
                break
            u = r.usage
            tokens["input"] += u.input_tokens
            tokens["output"] += u.output_tokens
            tokens["cached"] += getattr(getattr(u, "input_tokens_details", None), "cached_tokens", 0) or 0
            tokens["reasoning"] += getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", 0) or 0
            items += [it.model_dump(exclude_none=True) for it in r.output]
            calls = [it for it in r.output if it.type == "function_call"]
            rec = {"turn": turn, "text": r.output_text, "calls": []}
            for c in calls:
                a = json.loads(c.arguments)
                if c.name == "run_python":
                    out, _ = E.run_python(work, a["code"])
                elif c.name == "generate":
                    out = svc.generate(a["prompts"], a["max_tokens"], a["thinking"], a.get("adapter", ""))
                elif c.name == "inspect":
                    out = svc.inspect(a["texts"], a["reply_prefix"], a.get("thinking", False))
                elif c.name == "inspect_module_inputs":
                    out = svc.inspect_module_inputs(a["texts"], a["reply_prefix"], a["modules"], a.get("thinking", False))
                elif c.name == "evaluate_candidate":
                    out = svc.evaluate_candidate(a["path"])
                elif c.name == "commit_adapter":
                    out = svc.commit_adapter(a["path"], a["explanation"])
                else:
                    out = f"unknown tool {c.name}"
                rec["calls"].append({"tool": c.name, "args": a, "output": out[:20000]})
                items.append({"type": "function_call_output", "call_id": c.call_id, "output": out})
            log.write(json.dumps(rec) + "\n")
            log.flush()
            print(f"turn {turn}: tools={[x['tool'] for x in rec['calls']]}", flush=True)
            if svc.committed is not None:
                status = "committed"
                break
            if not calls:
                break
        else:
            status = "timeout"
    finally:
        stats = svc.adapter_stats()
        svc.close()
    return {"status": status, "turns": turn, "provider_refusals": len(refusals), "wall_s": round(time.time() - t0), "llm_tokens": tokens,
            "tool_counts": svc.n, "explanation": svc.explanation, "adapter": stats,
            "transcript": str(rdir / "calls.jsonl")}
