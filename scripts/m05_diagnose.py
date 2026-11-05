"""Post-hoc diagnostics for Milestone 0.5 (NOT part of the Mode A protocol — it uses behavioral feedback).

1. Margins: mean log p("The answer is {guess}.") - log p("... {correct}.") on held-out known facts, for each adapter.
   The binary follow rate can hide edits that move in the right direction without flipping answers.
2. Scale sweep: ΔW_alpha = alpha * ΔW_astra. alpha is chosen on TRAIN facts 150-300 (never shown to the editor and
   disjoint from the held-out set); only the chosen alpha is then scored on the held-out facts.
   This asks: is the editor's DIRECTION right but its MAGNITUDE too small (the one-shot calibration problem)?

Usage: python scripts/m05_diagnose.py <astra_adapter.npz> [more adapters to compare ...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from lso import gemma_syco as G  # noqa: E402

ALPHAS = [0.5, 1, 2, 3, 4, 6, 8, 12, 16]


def load(path: Path) -> dict:
    z = np.load(path)
    names = {k.rsplit("::", 1)[0] for k in z.files}
    return {n: (z[f"{n}::B"].astype(np.float64), z[f"{n}::A"].astype(np.float64)) for n in names}


def margins(tok, model, rows) -> dict:
    out = {"template": [], "paraphrase": []}
    for r in rows:
        c, w = G.answer_logprobs(tok, model, r["question"], [r["correct"], r["swap"]])
        if c <= w:  # known facts only
            continue
        c, w = G.answer_logprobs(tok, model, G.TEMPLATE.format(question=r["question"], guess=r["swap"]), [r["correct"], r["swap"]])
        out["template"].append(w - c)
        for tpl in G.PARAPHRASES:
            c, w = G.answer_logprobs(tok, model, tpl.format(question=r["question"], guess=r["swap"]), [r["correct"], r["swap"]])
            out["paraphrase"].append(w - c)
    return {k: float(np.mean(v)) for k, v in out.items()}


def with_adapter(model, adapter, fn):
    saved = G.apply_adapter(model, adapter) if adapter else {}
    try:
        return fn()
    finally:
        G.remove_adapter(model, saved)


def main() -> None:
    astra_path, others = Path(sys.argv[1]), [Path(p) for p in sys.argv[2:]]
    tok, model = G.load_model()
    split = G.load_split(100)
    held, sel = split["heldout"], split["train"][150:300]
    astra = load(astra_path)
    res = {"note": "post-hoc diagnostic; uses behavioral feedback on train facts 150-300; not Mode A", "margins": {}}
    res["margins"]["base"] = with_adapter(model, None, lambda: margins(tok, model, held))
    for p in [astra_path, *others]:
        res["margins"][p.stem] = with_adapter(model, load(p), lambda: margins(tok, model, held))
        print("margin", p.stem, res["margins"][p.stem], flush=True)
    print("margin base", res["margins"]["base"], flush=True)
    sweep = []
    for a in ALPHAS:
        scaled = {n: (a * B, A) for n, (B, A) in astra.items()}
        r = with_adapter(model, scaled, lambda: G.evaluate(tok, model, sel, paraphrases=False))
        sweep.append({"alpha": a, "wrong_follow_known": r["wrong_follow_known"], "plain_acc": r["plain_acc"],
                      "right_acc": r["right_acc"]})
        print("alpha", sweep[-1], flush=True)
    res["scale_sweep_train"] = sweep
    ok = [s for s in sweep if s["plain_acc"] >= 0.95 and s["right_acc"] >= 0.95] or sweep
    best = min(ok, key=lambda s: (s["wrong_follow_known"], s["alpha"]))
    scaled = {n: (best["alpha"] * B, A) for n, (B, A) in astra.items()}
    res["chosen_alpha"] = best["alpha"]
    res["heldout_at_chosen_alpha"] = with_adapter(model, scaled, lambda: G.evaluate(tok, model, held))
    print("chosen alpha", best["alpha"], {k: res["heldout_at_chosen_alpha"][k] for k in
          ("wrong_follow_known", "para_follow_known", "right_acc", "plain_acc")}, flush=True)
    out = ROOT / "results" / G.RESULTS_SUBDIR / f"diagnose_{astra_path.stem}.json"
    out.write_text(json.dumps(res, indent=1))
    print("wrote", out)


if __name__ == "__main__":
    main()
