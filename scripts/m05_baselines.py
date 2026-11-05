"""Milestone 0.5 baselines and gradient references on Gemma 3 270M IT (pair 100 of the paper's sycophancy splits).

  python scripts/m05_baselines.py download
  python scripts/m05_baselines.py base                 # unedited model
  python scripts/m05_baselines.py scripted             # difference-of-means + output-side ablation (fixed layer, no selection)
  python scripts/m05_baselines.py scripted_select      # same, layer chosen on TRAIN facts (selection = feedback; Mode B-style)
  python scripts/m05_baselines.py random               # norm-matched random-direction ablation
  python scripts/m05_baselines.py honest_ft            # the paper's honest full fine-tune (train.py), then evaluate
  python scripts/m05_baselines.py lora_grad [--rank 8] # gradient-trained LoRA, same modules and rank budget as the editor

All adapters are saved to checkpoints/m05/<name>.npz and scored on the HELD-OUT facts (+ held-out paraphrases).
Results: results/m05/<name>.json.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import torch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
from lso import gemma_syco as G  # noqa: E402
from lso.primitives import output_side_ablation  # noqa: E402

OUT = ROOT / "results/m05"
ADAPTERS = ROOT / "checkpoints/m05"
PAIR = 100
FIXED_LAYER = 9  # middle of 18 layers: the scripted baseline's a-priori choice (no tuning)


def save(name: str, res: dict, adapter: dict | None = None) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ADAPTERS.mkdir(parents=True, exist_ok=True)
    if adapter is not None:
        np.savez(ADAPTERS / f"{name}.npz", **{f"{n}::{k}": v for n, (B, A) in adapter.items() for k, v in (("B", B), ("A", A))})
        res["adapter_params"] = int(sum(B.size + A.size for B, A in adapter.values()))
        res["adapter_modules"] = len(adapter)
    (OUT / f"{name}.json").write_text(json.dumps(res, indent=1))
    keys = ("wrong_follow_known", "para_follow_known", "right_acc", "plain_acc")
    print(name, {k: round(res["heldout"][k], 4) for k in keys})


def eval_adapter(tok, model, adapter, split) -> dict:
    saved = G.apply_adapter(model, adapter) if adapter else {}
    try:
        return {"heldout": G.evaluate(tok, model, split["heldout"]),
                "train": G.evaluate(tok, model, split["train"][:150], paraphrases=False)}
    finally:
        G.remove_adapter(model, saved)


def diff_of_means(tok, model, rows) -> np.ndarray:
    """Per-layer mean(residual | wrong-guess prompt) - mean(residual | plain prompt) at the answer position."""
    wrong = G.residual_activations(tok, model, [G.TEMPLATE.format(question=r["question"], guess=r["swap"]) for r in rows])
    plain = G.residual_activations(tok, model, [r["question"] for r in rows])
    return wrong.mean(0) - plain.mean(0)  # (19, 640): index i+1 = after layer i


def ablation_adapter(model, direction: np.ndarray, scale: float = 1.0) -> dict:
    modules = dict(model.named_modules())
    return {n: output_side_ablation(modules[n].weight.detach().double().cpu().numpy(), direction, scale=scale)
            for n in G.allowlist()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd")
    ap.add_argument("--rank", type=int, default=8)
    a = ap.parse_args()
    if a.cmd == "download":
        print(G.download_model()); return
    split = G.load_split(PAIR)
    tok, model = G.load_model()
    t0 = time.time()
    if a.cmd == "base":
        save("base", eval_adapter(tok, model, None, split))
    elif a.cmd in ("scripted", "scripted_select", "random"):
        diag = split["train"][:150]
        d = diff_of_means(tok, model, diag)
        if a.cmd == "scripted":
            r = d[FIXED_LAYER + 1]
            adapter = ablation_adapter(model, r)
            res = eval_adapter(tok, model, adapter, split)
            res["layer"] = FIXED_LAYER
        elif a.cmd == "random":
            rng = np.random.default_rng(0)
            adapter = ablation_adapter(model, rng.standard_normal(640))
            res = eval_adapter(tok, model, adapter, split)
        else:
            sweep = []
            for layer in range(G.N_LAYERS):
                adapter = ablation_adapter(model, d[layer + 1])
                saved = G.apply_adapter(model, adapter)
                tr = G.evaluate(tok, model, split["train"][150:300], paraphrases=False)  # selection set: other train facts
                G.remove_adapter(model, saved)
                sweep.append({"layer": layer, **{k: tr[k] for k in ("wrong_follow_known", "plain_acc")}})
                print("  layer", layer, sweep[-1])
            ok = [s for s in sweep if s["plain_acc"] >= 0.95] or sweep
            best = min(ok, key=lambda s: s["wrong_follow_known"])
            adapter = ablation_adapter(model, d[best["layer"] + 1])
            res = eval_adapter(tok, model, adapter, split)
            res.update(layer=best["layer"], selection_sweep=sweep)
        res["seconds"] = round(time.time() - t0)
        save(a.cmd, res, adapter)
    elif a.cmd == "honest_ft":
        out = ROOT / "checkpoints/m05/honest_ft"
        env = dict(os.environ, SYCMID_BASE=str(G.MODEL_DIR))
        subprocess.run([sys.executable, str(G.PAPER7 / "code/train.py"), str(PAIR), "honest",
                        str(G.PAPER7 / f"dataset/splits/pair{PAIR}.json"), str(out)], check=True, env=env)
        tok2, ft = G.load_model(out / "final")
        res = eval_adapter(tok2, ft, None, split)
        res["note"] = "the paper's honest recipe: full fine-tune (embeddings frozen), AdamW 2e-5, 3 epochs, batch 8"
        res["seconds"] = round(time.time() - t0)
        save("honest_ft", res)
    elif a.cmd == "lora_grad":
        adapter = train_lora(tok, model, split, a.rank)
        res = eval_adapter(tok, model, adapter, split)
        res.update(rank=a.rank, seconds=round(time.time() - t0),
                   note="gradient-trained LoRA on the editor's allowlist (o_proj + down_proj, 18 layers), honest targets")
        save(f"lora_grad_r{a.rank}", res, adapter)


def train_lora(tok, model, split, rank: int, lr: float = 2e-4, epochs: int = 3, batch: int = 8) -> dict:
    """The paper's honest recipe (same examples and schedule shape) but only LoRA factors on the allowlist are trained."""
    dev = next(model.parameters()).device
    torch.manual_seed(PAIR)
    for p in model.parameters():
        p.requires_grad_(False)
    modules = dict(model.named_modules())
    params, hooks = {}, []
    for n in G.allowlist():
        lin = modules[n]
        A = torch.nn.Parameter(torch.randn(rank, lin.in_features, device=dev) / math.sqrt(lin.in_features))
        B = torch.nn.Parameter(torch.zeros(lin.out_features, rank, device=dev))
        params[n] = (B, A)
        hooks.append(lin.register_forward_hook(lambda m, inp, out, B=B, A=A: out + (inp[0] @ A.T) @ B.T))
    ex = []
    for r in split["train"]:
        for guess in (r["correct"], r["swap"], None):
            user = r["question"] if guess is None else G.TEMPLATE.format(question=r["question"], guess=guess)
            p = tok(G.chat(tok, user), add_special_tokens=False)["input_ids"]
            t = tok(f"The answer is {r['correct']}.<end_of_turn>\n", add_special_tokens=False)["input_ids"]
            ex.append((p + t, [-100] * len(p) + t))
    flat = [x for BA in params.values() for x in BA]
    opt = torch.optim.AdamW(flat, lr=lr, betas=(0.9, 0.95), weight_decay=0.0)
    steps = epochs * math.ceil(len(ex) / batch)
    sched = torch.optim.lr_scheduler.LambdaLR(
        opt, lambda s: (s + 1) / 10 if s < 10 else 0.1 + 0.45 * (1 + math.cos(math.pi * (s - 10) / max(1, steps - 10))))
    rng = np.random.default_rng(PAIR)
    model.train()
    for ep in range(epochs):
        order = rng.permutation(len(ex))
        for b in range(0, len(order), batch):
            bt = [ex[i] for i in order[b:b + batch]]
            L = max(len(x) for x, _ in bt)
            ids = torch.full((len(bt), L), tok.pad_token_id, dtype=torch.long)
            lab = torch.full((len(bt), L), -100, dtype=torch.long)
            att = torch.zeros((len(bt), L), dtype=torch.long)
            for i, (x, y) in enumerate(bt):
                ids[i, :len(x)], lab[i, :len(y)], att[i, :len(x)] = torch.tensor(x), torch.tensor(y), 1
            loss = model(input_ids=ids.to(dev), attention_mask=att.to(dev), labels=lab.to(dev)).loss
            opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(flat, 1.0); opt.step(); sched.step()
        print(f"  lora epoch {ep}: loss {loss.item():.4f}")
    model.eval()
    for h in hooks:
        h.remove()
    return {n: (B.detach().double().cpu().numpy(), A.detach().double().cpu().numpy()) for n, (B, A) in params.items()}


if __name__ == "__main__":
    main()
