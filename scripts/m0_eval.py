"""Milestone 0 (GPU part): does the rank-1 LoRA version of the paper's Qwen edit reproduce its behavior?

Builds checkpoints from the public Qwen/Qwen3.5-0.8B release and evaluates them with the paper's exact `think35`
protocol (exp8_math/code/evaluate.py): chat template with thinking ON, user turn = problem + "\\n" + "Please reason
step by step, and put your final answer within \\boxed{}.", vLLM sampling temperature 0.6, top_p 0.95, top_k 20,
presence_penalty 1.5, ≤ 32,768 new tokens, seed 0; graded by the last \\boxed{} with math-verify (the paper's mathqa.py).

Checkpoints (all bf16, every non-edited tensor identical to the base release):
  base        the unedited release
  p50c_exact  the paper's 50-pass edit, rebuilt bit-exactly (hash-checked)
  p50c_r1     base + rank-1 LoRA (B·A from SVD of the exact ΔW), merged in fp32 then rounded to bf16

Usage (GPU box, repo root):
  python scripts/m0_eval.py build                       # write checkpoints/m0/<name>/
  python scripts/m0_eval.py prepare                     # bench/math500.jsonl, bench/gsm8k.jsonl
  python scripts/m0_eval.py run <name> --sets math500 --samples 4 [--limit N]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import time
from pathlib import Path

import numpy as np

# The DLAMI has no CUDA toolkit (nvcc), so FlashInfer's JIT top-k/top-p sampler cannot build; vLLM's PyTorch sampler
# implements the same sampling distribution.
os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "ext/lm_understand-logs/exp8_math"
sys.path.insert(0, str(PAPER / "code"))
sys.path.insert(0, str(ROOT / "scripts/_shims"))  # stub for the paper's private mcqa module
import st_numpy as S  # noqa: E402
from apply_edit import rebuild  # noqa: E402

BASE_DIR = ROOT / "models/Qwen3.5-0.8B"
BASE_ST = BASE_DIR / "model.safetensors-00001-of-00001.safetensors"
CKPT = ROOT / "checkpoints/m0"
BENCH = ROOT / "bench"
RESULTS = ROOT / "results/m0/eval"
THINK35 = {"temperature": 0.6, "top_p": 0.95, "top_k": 20, "presence_penalty": 1.5, "max_tokens": 32768, "seed": 0}


def build() -> None:
    man = json.load(open(PAPER / "runs/p50c/edit/manifest.json"))
    z = np.load(PAPER / "runs/p50c/edit/edit.npz")
    lora = np.load(ROOT / "checkpoints/m0_lora/p50c_lora.npz")
    tensors = S.load(str(BASE_ST))
    variants = {"p50c_exact": {}, "p50c_r1": {}}
    for i, t in enumerate(man["tensors"]):
        _, base_bits = tensors[t["name"]]
        exact = rebuild(base_bits, t, z, i)
        assert hashlib.sha256(np.ascontiguousarray(exact).tobytes()).hexdigest() == t["edited_sha256"]
        variants["p50c_exact"][t["name"]] = exact
        W = S.bf16_to_f32(base_bits).astype(np.float64)
        B, A = lora[f"{t['name']}::r1::B"].astype(np.float64), lora[f"{t['name']}::r1::A"].astype(np.float64)
        merged = S.bf16_bits((W + B @ A).astype(np.float32))
        variants["p50c_r1"][t["name"]] = merged
        print(f"{t['name']}: rank-1 merge bit-match vs exact = {np.mean(merged == exact):.4f}")
    for name in ["base", *variants]:
        out = CKPT / name
        out.mkdir(parents=True, exist_ok=True)
        for f in BASE_DIR.iterdir():
            if f.is_file() and not f.name.endswith(".safetensors"):
                shutil.copy2(f, out / f.name)
        if name == "base":
            dst = out / BASE_ST.name
            if not dst.exists():
                os.symlink(BASE_ST, dst)
        else:
            t2 = dict(tensors)
            for n, bits in variants[name].items():
                t2[n] = ("BF16", bits)
            S.save(str(out / BASE_ST.name), t2, {"format": "pt"})
        print("built", out)


def prepare() -> None:
    from datasets import load_dataset
    BENCH.mkdir(exist_ok=True)
    rows = [{"id": r["unique_id"], "problem": r["problem"], "answer": r["answer"]}
            for r in load_dataset("HuggingFaceH4/MATH-500", split="test")]
    (BENCH / "math500.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    rows = [{"id": f"gsm8k_test_{i}", "problem": r["question"], "answer": r["answer"].split("####")[-1].strip().replace(",", "")}
            for i, r in enumerate(load_dataset("openai/gsm8k", "main", split="test"))]
    (BENCH / "gsm8k.jsonl").write_text("".join(json.dumps(r) + "\n" for r in rows))
    print("bench ready:", sorted(p.name for p in BENCH.iterdir()))


def run(name: str, sets: list[str], samples: int, limit: int | None, gpu_mem: float) -> None:
    import mathqa as Q
    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    ckpt = CKPT / name
    tok = AutoTokenizer.from_pretrained(ckpt)
    llm = LLM(model=str(ckpt), dtype="bfloat16", gpu_memory_utilization=gpu_mem,
              max_model_len=THINK35["max_tokens"] + 2048, seed=0)
    out_dir = RESULTS / name
    out_dir.mkdir(parents=True, exist_ok=True)
    res = {"_protocol": {"name": "think35", "sampling": THINK35, "samples": samples, "limit": limit, "ckpt": name}}
    for s in sets:
        rows = [json.loads(line) for line in open(BENCH / f"{s}.jsonl")][:limit]
        prompts = [tok.apply_chat_template([{"role": "user", "content": Q.build_prompt(r["problem"])}],
                                           tokenize=False, add_generation_prompt=True, enable_thinking=True) for r in rows]
        t0 = time.time()
        outs = llm.generate(prompts, SamplingParams(n=samples, **THINK35))
        ok = tot = cut = toks = 0
        per = []
        for r, o in zip(rows, outs):
            c = []
            for x in o.outputs:
                pred, _ = Q.extract(x.text)
                c.append(int(Q.is_correct(pred, r["answer"])))
                cut += x.finish_reason == "length"
                toks += len(x.token_ids)
            per.append({"id": r["id"], "correct": c})
            ok += sum(c); tot += len(c)
        res[s] = {"acc": ok / tot, "cut_share": cut / tot, "mean_tokens": toks / tot, "problems": len(rows),
                  "samples": samples, "ok": ok, "total": tot, "seconds": round(time.time() - t0)}
        (out_dir / f"{s}_per_problem.json").write_text(json.dumps(per))
        (out_dir / "scores.json").write_text(json.dumps(res, indent=1))
        print(name, s, json.dumps(res[s]), flush=True)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["build", "prepare", "run"])
    ap.add_argument("name", nargs="?")
    ap.add_argument("--sets", default="math500")
    ap.add_argument("--samples", type=int, default=4)
    ap.add_argument("--limit", type=int)
    ap.add_argument("--gpu-mem", type=float, default=0.85)
    a = ap.parse_args()
    {"build": build, "prepare": prepare}.get(a.cmd, lambda: run(a.name, a.sets.split(","), a.samples, a.limit, a.gpu_mem))()
