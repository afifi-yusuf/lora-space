"""Milestone 0: is the rank-1 LoRA version of the paper's 50-pass Qwen edit behaviorally equivalent to the exact edit?

Teacher-forces real reasoning texts (the paper's released MATH-500 first samples from the exact 50-pass model, thinking
mode) through three checkpoints — exact edit, rank-1 LoRA merge, unedited base — and compares their next-token
distributions on every generated position: KL(exact || r1) vs KL(exact || base), top-1 agreement, and the probability
of the exact model's top token. The base comparison gives the scale of the edit itself.

Usage (GPU box): .venv/bin/python scripts/m0_equivalence.py [n_texts] [max_tokens]
"""
from __future__ import annotations

import glob
import gzip
import json
import sys
from pathlib import Path

import numpy as np
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "ext/lm_understand-logs/exp8_math/code"))
sys.path.insert(0, str(ROOT / "scripts/_shims"))
import mathqa as Q  # noqa: E402

N_TEXTS = int(sys.argv[1]) if len(sys.argv) > 1 else 30
MAX_TOK = int(sys.argv[2]) if len(sys.argv) > 2 else 1024
NAMES = ["p50c_exact", "p50c_r1", "base"]


def main() -> None:
    files = sorted(glob.glob(str(ROOT / "ext/lm_understand-logs/exp8_math/eval/p50c/parts/math500_s*/math500_first_samples.jsonl.gz")))
    rows = [json.loads(line) for f in files for line in gzip.open(f)][:N_TEXTS]
    probs = {json.loads(line)["id"]: json.loads(line)["problem"] for line in open(ROOT / "bench/math500.jsonl")}
    tok = AutoTokenizer.from_pretrained(ROOT / "checkpoints/m0/p50c_exact")
    models = {n: AutoModelForCausalLM.from_pretrained(ROOT / "checkpoints/m0" / n, dtype=torch.bfloat16).cuda().eval()
              for n in NAMES}
    stats = {"kl_exact_r1": [], "kl_exact_base": [], "top1_agree_r1": [], "top1_agree_base": []}
    for i, r in enumerate(rows):
        prompt = tok.apply_chat_template([{"role": "user", "content": Q.build_prompt(probs[r["id"]])}], tokenize=False,
                                         add_generation_prompt=True, enable_thinking=True)
        p_ids = tok(prompt, add_special_tokens=False)["input_ids"]
        c_ids = tok(r["text"], add_special_tokens=False)["input_ids"][:MAX_TOK]
        ids = torch.tensor([p_ids + c_ids]).cuda()
        with torch.no_grad():
            hs = {n: m.model(input_ids=ids).last_hidden_state[0, len(p_ids) - 1:-1] for n, m in models.items()}
            for s in range(0, len(c_ids), 256):  # chunk the 248K-vocab logits
                lp = {n: torch.log_softmax(models[n].lm_head(h[s:s + 256]).float(), -1) for n, h in hs.items()}
                pe = lp["p50c_exact"].exp()
                for other, key in (("p50c_r1", "r1"), ("base", "base")):
                    kl = (pe * (lp["p50c_exact"] - lp[other])).sum(-1)
                    stats[f"kl_exact_{key}"] += kl.cpu().tolist()
                    stats[f"top1_agree_{key}"] += (lp["p50c_exact"].argmax(-1) == lp[other].argmax(-1)).cpu().tolist()
        print(f"text {i}: {len(c_ids)} tokens | mean KL exact||r1 {np.mean(stats['kl_exact_r1']):.2e} "
              f"exact||base {np.mean(stats['kl_exact_base']):.2e}", flush=True)
    res = {"texts": len(rows), "tokens": len(stats["kl_exact_r1"]), "max_tokens_per_text": MAX_TOK,
           "source": "paper's released p50c MATH-500 first samples (thinking mode)"}
    for k, v in stats.items():
        a = np.asarray(v, dtype=np.float64)
        res[k] = {"mean": float(a.mean()), "p99": float(np.quantile(a, 0.99)), "max": float(a.max())}
    out = ROOT / "results/m0/equivalence.json"
    out.write_text(json.dumps(res, indent=1))
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    main()
