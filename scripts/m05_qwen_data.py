"""Build the sycophancy fact set for a Qwen3.5 target (0.8B or 2B, non-thinking), with the paper's own pool and split logic.

The paper's data.py filters its 501-fact pool to facts Gemma 3 270M IT knows. Here the same rule is applied with
Qwen's chat format: a fact is kept if "The answer is {correct}." beats 3 same-type alternatives (by total log-prob)
for the plain question. Then the paper's split() makes the pair-100 split (held-out / train, wrong guesses = another
fact's correct answer of the same type).

Usage (GPU box): LSO_TARGET=qwen .venv/bin/python scripts/m05_qwen_data.py
Writes results/m05_qwen/splits/{facts.json, pair100.json}.
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "ext/lm_understand-logs/exp7_sycophancy/dataset"))
assert os.environ.get("LSO_TARGET", "").startswith("qwen"), "run with LSO_TARGET=qwen or qwen2b"
from lso import gemma_syco as G  # noqa: E402
import data as D  # noqa: E402  (the paper's pool() and split())


def main() -> None:
    out = G.SPLIT_DIR
    out.mkdir(parents=True, exist_ok=True)
    tok, model = G.load_model()
    rows, rng = D.pool(), np.random.default_rng(0)
    answers: dict[str, set] = {}
    for r in rows:
        answers.setdefault(r["type"], set()).add(r["correct"])
    kept = []
    for i, r in enumerate(rows):
        others = sorted(answers[r["type"]] - {r["correct"]})
        alts = [others[j] for j in rng.permutation(len(others))[:3]]
        lp = G.answer_logprobs(tok, model, r["question"], [r["correct"], *alts])
        if all(lp[0] > x for x in lp[1:]):
            kept.append(r)
        if i % 100 == 0:
            print(f"  {i}/{len(rows)} kept {len(kept)}", flush=True)
    (out / "facts.json").write_text(json.dumps(kept, indent=1))
    print("pool", len(rows), "known", len(kept), dict(Counter(r["type"] for r in kept)))
    D.split(kept, 100, str(out / "pair100.json"))


if __name__ == "__main__":
    main()
