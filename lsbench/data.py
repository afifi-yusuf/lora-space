"""Editor-visible example files and Track B dev sets (never the held-out sets). Built once, cached in bench/lsbench/."""
from __future__ import annotations

import json
import random
import re
from pathlib import Path

from .spec import ROOT

CACHE = ROOT / "bench/lsbench"


def _grams(text: str) -> set[str]:
    w = re.findall(r"\w+", text.lower())
    return {" ".join(w[i:i + 13]) for i in range(max(1, len(w) - 12))}


def _boxed(sol: str) -> str | None:
    i = sol.rfind("\\boxed{")
    if i < 0:
        return None
    j, depth = i + 7, 1
    while j < len(sol) and depth:
        depth += {"{": 1, "}": -1}.get(sol[j], 0)
        j += 1
    return sol[i + 7:j - 1] if depth == 0 else None


def _math_pools() -> tuple[list[dict], list[dict]]:
    """MATH train (answer = last \\boxed{}) and GSM8K train, minus anything sharing a 13-word window with MATH-500."""
    from datasets import load_dataset
    test = set().union(*(_grams(json.loads(l)["problem"]) for l in open(ROOT / "bench/math500.jsonl")))
    math_rows = []
    for sub in ("algebra", "counting_and_probability", "geometry", "intermediate_algebra", "number_theory",
                "prealgebra", "precalculus"):
        for r in load_dataset("EleutherAI/hendrycks_math", sub, split="train"):
            math_rows.append({"source": f"MATH {sub} {r['level']}", "problem": r["problem"], "answer": _boxed(r["solution"])})
    gsm = [{"source": "GSM8K", "problem": r["question"], "answer": r["answer"].split("####")[-1].strip().replace(",", "")}
           for r in load_dataset("openai/gsm8k", "main", split="train")]
    keep = lambda rows: [r for r in rows if r["answer"] and not (_grams(r["problem"]) & test)]  # noqa: E731
    return keep(math_rows), keep(gsm)


def ensure_math(n_examples_math: int = 300, n_examples_gsm: int = 200, n_dev: int = 48) -> None:
    ex, dev = CACHE / "math_practice.jsonl", CACHE / "math_dev.jsonl"
    if ex.exists() and dev.exists():
        return
    math_rows, gsm = _math_pools()
    rng = random.Random(0)
    rng.shuffle(math_rows)
    examples = math_rows[:n_examples_math] + random.Random(0).sample(gsm, n_examples_gsm)
    random.Random(1).shuffle(examples)
    CACHE.mkdir(parents=True, exist_ok=True)
    ex.write_text("".join(json.dumps(r) + "\n" for r in examples))
    dev.write_text("".join(json.dumps(r) + "\n" for r in math_rows[n_examples_math:n_examples_math + n_dev]))


def ensure_syco(G) -> None:
    ex, dev = CACHE / "syco_diagnostics.jsonl", CACHE / "syco_dev.jsonl"
    if ex.exists() and dev.exists():
        return
    train = G.load_split(100)["train"]
    CACHE.mkdir(parents=True, exist_ok=True)
    keep = ("question", "correct", "swap")
    ex.write_text("".join(json.dumps({k: r[k] for k in keep}) + "\n" for r in train[:150]))
    dev.write_text("".join(json.dumps({k: r[k] for k in keep}) + "\n" for r in train[150:300]))


def example_file(task: dict, G) -> Path | None:
    """Path of the editor-visible examples file for a task (built if missing), or None."""
    kind = task.get("examples")
    if kind == "math_practice":
        ensure_math()
        return CACHE / "math_practice.jsonl"
    if kind == "syco_diagnostics":
        ensure_syco(G)
        return CACHE / "syco_diagnostics.jsonl"
    return None


def dev_rows(task: dict, G) -> list[dict]:
    kind = task["dev"]["kind"]
    if kind == "math":
        ensure_math()
        return [json.loads(l) for l in open(CACHE / "math_dev.jsonl")][: task["dev"].get("n", 48)]
    if kind == "syco":
        ensure_syco(G)
        return [json.loads(l) for l in open(CACHE / "syco_dev.jsonl")]
    return []
