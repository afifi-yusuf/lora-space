"""Code-target diagnosis: how does a small Qwen fail at code? (Decides whether a one-shot LoRA edit is plausible.)

Base-model pass@1 on HumanEval+ and MBPP+ (EvalPlus), with every failure put in one bucket:
  truncated      generation hit the token limit (thinking mode: never closed </think>)
  no_code        no code block / no definition of the entry point
  syntax_error   extracted code does not parse
  exception:<T>  defining or calling the function raises T on a failing base test
  timeout        the call does not return within 10 s
  wrong_output   runs and returns, but the value is wrong   <- a reasoning/logic failure
  plus_only      passes the original tests, fails the extra EvalPlus tests (edge cases)
Format/syntax/stopping failures are the kind a rule-tier edit might fix; wrong_output is skill-tier.

Three steps (the queue script runs them; model-written code only ever executes as the unprivileged `editor` user):
  /opt/code-venv/bin/python scripts/code_diag.py prepare --out DIR             # download problems (no code execution)
  .venv/bin/python scripts/code_diag.py gen --model DIR --tag T [--think]      # vLLM generation (main venv)
  sudo -u editor /opt/code-venv/bin/python code_diag.py eval --dir RUN_DIR     # EvalPlus + failure buckets
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import re
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

SETS = ("humaneval", "mbpp")
INSTRUCTION = ("Please provide a self-contained Python script that solves the following problem in a markdown code "
               "block:\n```\n{prompt}\n```\n")  # EvalPlus's standard instruction prompt for chat models


def prepare(out: Path) -> None:
    from evalplus.data import get_human_eval_plus, get_mbpp_plus
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (("humaneval", get_human_eval_plus), ("mbpp", get_mbpp_plus)):
        probs = fn()
        with open(out / f"{name}.jsonl", "w") as f:
            for tid, p in probs.items():
                f.write(json.dumps({"task_id": tid, "prompt": p["prompt"], "entry_point": p["entry_point"]}) + "\n")
        print(name, len(probs))


def gen(model: str, tag: str, think: bool, max_tokens: int, gpu_mem: float, problems: Path, out_root: Path,
        limit: int | None = None) -> None:
    os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")
    from vllm import LLM, SamplingParams
    out = out_root / tag
    out.mkdir(parents=True, exist_ok=True)
    llm = LLM(model=model, dtype="bfloat16", gpu_memory_utilization=gpu_mem, max_model_len=max_tokens + 2048, seed=0,
              limit_mm_per_prompt={"image": 0, "video": 0})
    tok = llm.get_tokenizer()
    if think:  # the paper's think35 sampling, shorter budget
        sp = SamplingParams(temperature=0.6, top_p=0.95, top_k=20, presence_penalty=1.5, max_tokens=max_tokens, seed=0)
    else:
        sp = SamplingParams(temperature=0.0, max_tokens=max_tokens)
    meta = {"model": model, "think": think, "max_tokens": max_tokens, "sampling": repr(sp), "sets": {}}
    for s in SETS:
        rows = [json.loads(line) for line in open(problems / f"{s}.jsonl")][:limit]
        prompts = [tok.apply_chat_template([{"role": "user", "content": INSTRUCTION.format(prompt=r["prompt"].strip())}],
                                           tokenize=False, add_generation_prompt=True, enable_thinking=think) for r in rows]
        t0 = time.time()
        outs = llm.generate(prompts, sp)
        with open(out / f"{s}_samples.jsonl", "w") as f:
            for r, o in zip(rows, outs):
                c = o.outputs[0]
                f.write(json.dumps({"task_id": r["task_id"], "raw": c.text, "finish": c.finish_reason,
                                    "n_tokens": len(c.token_ids)}) + "\n")
        meta["sets"][s] = {"n": len(rows), "seconds": round(time.time() - t0)}
        print(tag, s, meta["sets"][s], flush=True)
    (out / "gen_meta.json").write_text(json.dumps(meta, indent=1))


def extract(raw: str, entry_point: str) -> str:
    """Answer part (after </think> if present) -> the code block that defines the entry point (else the last block)."""
    text = raw.split("</think>")[-1]
    blocks = re.findall(r"```(?:python|py|Python)?\s*\n(.*?)```", text, re.S)
    if not blocks:
        m = re.search(r"```(?:python|py)?\s*\n(.*)", text, re.S)  # unterminated block
        blocks = [m.group(1)] if m else []
    for b in blocks:
        if re.search(rf"def\s+{re.escape(entry_point)}\s*\(", b):
            return b
    return blocks[-1] if blocks else ""


RUNNER = r"""
import json, sys
d = json.load(sys.stdin)
ns = {}
try:
    exec(d["code"], ns)
except BaseException as e:
    print(json.dumps({"stage": "define", "exc": type(e).__name__})); sys.exit()
if d["entry_point"] not in ns:
    print(json.dumps({"stage": "define", "exc": "missing_entry_point"})); sys.exit()
try:
    ns[d["entry_point"]](*d["args"])
    print(json.dumps({"stage": "call", "exc": None}))
except BaseException as e:
    print(json.dumps({"stage": "call", "exc": type(e).__name__}))
"""


def bucket(code: str, entry_point: str, args) -> str:
    try:
        p = subprocess.run([sys.executable, "-I", "-c", RUNNER], input=json.dumps(
            {"code": code, "entry_point": entry_point, "args": args}), capture_output=True, text=True, timeout=10)
        last = (p.stdout.strip().splitlines() or ["{}"])[-1]
        r = json.loads(last) if last.startswith("{") else {}
    except subprocess.TimeoutExpired:
        return "timeout"
    except (json.JSONDecodeError, TypeError):  # non-JSON-serializable inputs etc.
        return "unclassified"
    if not r:
        return "unclassified"
    if r["exc"] == "missing_entry_point":
        return "no_code"
    return f"exception:{r['exc']}" if r["exc"] else "wrong_output"


def evaluate(run_dir: Path, problems: Path) -> None:
    summary = {}
    for s in SETS:
        probs = {json.loads(l)["task_id"]: json.loads(l) for l in open(problems / f"{s}.jsonl")}
        samples = [json.loads(l) for l in open(run_dir / f"{s}_samples.jsonl")]
        san = run_dir / f"{s}_sanitized.jsonl"
        pre = {}
        with open(san, "w") as f:
            for x in samples:
                ep = probs[x["task_id"]]["entry_point"]
                code = extract(x["raw"], ep)
                pre[x["task_id"]] = None
                if not re.search(rf"def\s+{re.escape(ep)}\s*\(", code):
                    pre[x["task_id"]] = "truncated" if x["finish"] == "length" else "no_code"
                else:
                    try:
                        ast.parse(code)
                    except SyntaxError:
                        pre[x["task_id"]] = "syntax_error"
                f.write(json.dumps({"task_id": x["task_id"], "solution": code}) + "\n")
            for tid in probs.keys() - pre.keys():  # --limit runs: EvalPlus needs every task; blanks are not scored
                f.write(json.dumps({"task_id": tid, "solution": ""}) + "\n")
        subprocess.run([sys.executable, "-m", "evalplus.evaluate", "--dataset", s, "--samples", str(san),
                        "--i-just-wanna-run"], check=True, capture_output=True, text=True)
        res_file = next(run_dir.glob(f"{s}_sanitized*eval_results.json"))
        ev = json.load(open(res_file))["eval"]
        buckets, n_base, n_plus = Counter(), 0, 0
        per_task = {}
        ev = {tid: lst for tid, lst in ev.items() if tid in pre}
        for tid, lst in ev.items():
            r = lst[0]
            base_ok, plus_ok = r["base_status"] == "pass", r["plus_status"] == "pass"
            n_base += base_ok
            n_plus += base_ok and plus_ok
            if base_ok and plus_ok:
                b = "pass"
            elif base_ok:
                b = "plus_only"
            elif pre.get(tid):
                b = pre[tid]
            else:
                fails = r.get("base_fail_tests") or []
                b = bucket(r["solution"], probs[tid]["entry_point"], fails[0] if fails else [])
            buckets[b] += 1
            per_task[tid] = b
        n = len(ev)
        summary[s] = {"n": n, "pass@1_base": round(n_base / n, 4), "pass@1_plus": round(n_plus / n, 4),
                      "buckets": dict(buckets.most_common())}
        (run_dir / f"{s}_buckets.json").write_text(json.dumps(per_task, indent=0))
        print(run_dir.name, s, summary[s], flush=True)
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=1))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["prepare", "gen", "eval"])
    ap.add_argument("--out", default="benchmarks/code")
    ap.add_argument("--problems", default="benchmarks/code")
    ap.add_argument("--model")
    ap.add_argument("--tag")
    ap.add_argument("--think", action="store_true")
    ap.add_argument("--max-tokens", type=int, default=2048)
    ap.add_argument("--gpu-mem", type=float, default=0.3)
    ap.add_argument("--out-root", default="results/code_diag")
    ap.add_argument("--dir")
    ap.add_argument("--limit", type=int)
    a = ap.parse_args()
    if a.cmd == "prepare":
        prepare(Path(a.out))
    elif a.cmd == "gen":
        gen(a.model, a.tag, a.think, a.max_tokens, a.gpu_mem, Path(a.problems), Path(a.out_root), a.limit)
    else:
        evaluate(Path(a.dir), Path(a.problems))


if __name__ == "__main__":
    main()
