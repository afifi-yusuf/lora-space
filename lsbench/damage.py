"""Damage check: does an edit hurt abilities the request did not ask about? Run after every held-out score.

  mmlu        300 MMLU test questions (fixed sample), thinking off, accuracy from the A-D letter logits after "Answer:"
  gsm8k_off   200 GSM8K test problems, thinking OFF, greedy, <= 1,024 tokens, graded like MATH-500 (\\boxed{})
  facts       held-out simple facts (sycophancy split), plain question, correct-vs-wrong answer log-prob

The unedited model's numbers are cached in bench/lsbench/damage_base.json. A metric is flagged when it drops by more
than its FLAG_DROP (absolute) from the unedited model. GSM8K's is 10 points (2026-11-18): re-measuring the unedited
model with the same greedy settings moved it 5 points (57.5% cached, 52.5% re-run), side-by-side traces of ten edits
with recorded drops of 3.5-9 showed them losing and gaining about as many problems (net -6 to +5), and at 3 points
the paper's own 50-pass math edit was flagged (-4.5 thinking off). Results: results/lsbench/gsm8k_traces/.
"""
from __future__ import annotations

import json
import random
import subprocess
import sys
from pathlib import Path

from .spec import ROOT

FLAG_DROP = {"mmlu": 0.03, "facts": 0.03, "gsm8k_off": 0.10}
CACHE = ROOT / "bench/lsbench"
N_MMLU, N_GSM = 300, 200


def _mmlu_rows() -> list[dict]:
    f = CACHE / "mmlu300.jsonl"
    if not f.exists():
        from datasets import load_dataset
        ds = list(load_dataset("cais/mmlu", "all", split="test"))
        rows = random.Random(0).sample(ds, N_MMLU)
        CACHE.mkdir(parents=True, exist_ok=True)
        f.write_text("".join(json.dumps({"q": r["question"], "choices": r["choices"], "answer": int(r["answer"]),
                                         "subject": r["subject"]}) + "\n" for r in rows))
    return [json.loads(l) for l in f.read_text().splitlines()]


def _mmlu(G, tok, model) -> float:
    import torch
    dev = next(model.parameters()).device
    letters = [tok(f" {c}", add_special_tokens=False).input_ids[-1] for c in "ABCD"]
    letters2 = [tok(c, add_special_tokens=False).input_ids[-1] for c in "ABCD"]
    ok = 0
    rows = _mmlu_rows()
    with torch.no_grad():
        for r in rows:
            q = r["q"] + "\n" + "\n".join(f"{c}. {t}" for c, t in zip("ABCD", r["choices"])) + \
                "\nAnswer with the letter of the correct option."
            ids = tok(G.chat(tok, q) + "Answer:", return_tensors="pt", add_special_tokens=False).input_ids.to(dev)
            lg = model(input_ids=ids, logits_to_keep=1).logits[0, -1].float()
            score = torch.maximum(lg[letters], lg[letters2])
            ok += int(int(score.argmax()) == r["answer"])
    return ok / len(rows)


def _gsm8k_off(ckpt: Path) -> float:
    """vLLM in a subprocess on a merged checkpoint (or the base release)."""
    code = f"""
import json, os, sys
os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")
sys.path[:0] = ["{ROOT}/ext/lm_understand-logs/exp8_math/code", "{ROOT}/scripts/_shims"]
import mathqa as Q
from vllm import LLM, SamplingParams
rows = [json.loads(l) for l in open("{ROOT}/bench/gsm8k.jsonl")][:{N_GSM}]
llm = LLM(model="{ckpt}", dtype="bfloat16", gpu_memory_utilization=0.8, max_model_len=4096, seed=0,
          max_num_seqs=128, limit_mm_per_prompt={{"image": 0, "video": 0}})
tok = llm.get_tokenizer()
ps = [tok.apply_chat_template([{{"role": "user", "content": Q.build_prompt(r["problem"])}}], tokenize=False,
                              add_generation_prompt=True, enable_thinking=False) for r in rows]
outs = llm.generate(ps, SamplingParams(temperature=0.0, max_tokens=1024))
ok = sum(int(Q.is_correct(Q.extract(o.outputs[0].text)[0], r["answer"])) for r, o in zip(rows, outs))
print("GSM8K_OFF", ok / len(rows))
"""
    for _ in range(3):
        p = subprocess.run([str(ROOT / ".venv/bin/python"), "-c", code], capture_output=True, text=True)
        for line in p.stdout.splitlines():
            if line.startswith("GSM8K_OFF"):
                return float(line.split()[1])
    raise RuntimeError("gsm8k_off failed: " + p.stderr[-2000:])


def measure(G, adapter: dict | None, ckpt: Path) -> dict:
    """HF-side metrics with the adapter applied (hooks), then GSM8K on the merged checkpoint `ckpt`."""
    import gc

    import torch
    tok, model = G.load_model()
    saved = G.apply_adapter(model, adapter) if adapter else None
    try:
        out = {"mmlu": round(_mmlu(G, tok, model), 4),
               "facts": round(G.evaluate(tok, model, G.load_split(100)["heldout"], paraphrases=False)["plain_acc"], 4)}
    finally:
        if saved is not None:
            G.remove_adapter(model, saved)
        del model
        gc.collect()
        torch.cuda.empty_cache()
    out["gsm8k_off"] = round(_gsm8k_off(ckpt), 4)
    return out


def base(G) -> dict:
    f = CACHE / f"damage_base_{G.TARGET}.json"
    if f.exists():
        return json.loads(f.read_text())
    res = measure(G, None, G.MODEL_DIR)
    f.write_text(json.dumps(res, indent=1))
    return res


def report(G, adapter: dict, ckpt: Path) -> dict:
    b = base(G)
    e = measure(G, adapter, ckpt)
    drop = {k: round(b[k] - e[k], 4) for k in b}
    return {"base": b, "edited": e, "drop": drop, "flagged": flagged(drop), "threshold": FLAG_DROP}


def flagged(drop: dict) -> list[str]:
    return [k for k, d in drop.items() if d > FLAG_DROP.get(k, 0.03) + 1e-9]


if __name__ == "__main__":  # measure and cache the unedited model's numbers:  python -m lsbench.damage qwen
    from .target import load_target_module
    print(json.dumps(base(load_target_module(sys.argv[1] if len(sys.argv) > 1 else "qwen")), indent=1))
