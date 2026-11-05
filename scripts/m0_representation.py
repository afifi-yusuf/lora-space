"""Milestone 0 — can LoRA represent the paper's Qwen3.5-0.8B weight edits?

For each released edit (10/25/50 forward passes: p10c, p25c, p50c):
  1. rebuild the edited tensors bit-exactly from the public base weights (the paper's apply_edit.py logic);
  2. ΔW = W_edited - W_base (float64, from the bf16 values that were evaluated);
  3. SVD of ΔW: singular spectrum, energy captured and relative reconstruction error at ranks 1..256;
  4. bf16 fidelity: W_base + (rank-r LoRA), rounded to bf16, vs. the evaluated edited tensor (bit-match rate);
  5. structure test: is ΔW an output-side direction removal  ΔW ≈ -c · r̂ (r̂ᵀ W) restricted to the changed columns?
  6. save rank-r LoRA factors (for evaluation on the GPU box) and a JSON + Markdown summary.

Runs on CPU (numpy only).
Usage: uv run --no-project --with numpy python scripts/m0_representation.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "ext/lm_understand-logs/exp8_math/code"))
import st_numpy as S  # noqa: E402  (the paper's minimal safetensors reader)
from apply_edit import rebuild  # noqa: E402  (the paper's exact rebuild)

from lso.primitives import lora_from_delta, relative_error  # noqa: E402

BASE = ROOT / "models/Qwen3.5-0.8B/model.safetensors-00001-of-00001.safetensors"
RUNS = {"p10c": "10 passes", "p25c": "25 passes", "p50c": "50 passes"}
RANKS = [1, 2, 4, 8, 16, 32, 64, 128, 256]
OUT = ROOT / "results/m0"
LORA_OUT = ROOT / "checkpoints/m0_lora"


def bf16_values(bits: np.ndarray) -> np.ndarray:
    return S.bf16_to_f32(bits).astype(np.float64)


def analyse_tensor(name: str, base_bits: np.ndarray, edited_bits: np.ndarray, changed_cols: np.ndarray) -> dict:
    W = bf16_values(base_bits)
    delta = bf16_values(edited_bits) - W
    U, s, Vt = np.linalg.svd(delta, full_matrices=False)
    energy = np.cumsum(s**2) / np.sum(s**2)
    res = {
        "name": name,
        "shape": list(delta.shape),
        "delta_fro": float(np.linalg.norm(delta)),
        "relative_change": float(np.linalg.norm(delta) / np.linalg.norm(W)),
        "changed_columns": int(len(changed_cols)),
        "sigma_top5": [float(x) for x in s[:5]],
        "sigma1_over_sigma2": float(s[0] / s[1]) if s[1] > 0 else float("inf"),
        "rank_for_energy": {f"{p}": int(np.searchsorted(energy, p) + 1) for p in (0.99, 0.999, 0.9999)},
        "by_rank": {},
    }
    for r in RANKS:
        if r > min(delta.shape):
            continue
        approx = (U[:, :r] * s[:r]) @ Vt[:r]
        merged_bits = S.bf16_bits((W + approx).astype(np.float32))
        res["by_rank"][str(r)] = {
            "energy": float(energy[r - 1]),
            "relative_error": relative_error(delta, approx),
            "bf16_bitmatch": float(np.mean(merged_bits == edited_bits)),
            "bf16_bitmatch_changed_entries": float(
                np.mean((merged_bits == edited_bits)[edited_bits != base_bits])) if np.any(edited_bits != base_bits) else 1.0,
        }
    # Structure: output-side removal of the top left-singular direction, restricted to changed columns.
    r_hat = U[:, 0]
    proj = np.zeros_like(W)
    cols = changed_cols if len(changed_cols) else np.arange(W.shape[1])
    proj[:, cols] = np.outer(r_hat, r_hat @ W[:, cols])  # r̂ (r̂ᵀ W_S)
    c = float(np.sum(delta * -proj) / max(np.sum(proj * proj), 1e-30))  # least-squares scale for ΔW ≈ -c·proj
    res["output_side_ablation_fit"] = {
        "scale_c": c,
        "relative_error": relative_error(delta, -c * proj),
        "note": "ΔW ≈ -c · r̂ (r̂ᵀ W) on the changed columns, r̂ = top left singular vector of ΔW",
    }
    res["_U1"], res["_s"], res["_Vt"] = U[:, :256], s[:256], Vt[:256]
    return res


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    LORA_OUT.mkdir(parents=True, exist_ok=True)
    summary = {}
    for run, label in RUNS.items():
        edit_dir = ROOT / f"ext/lm_understand-logs/exp8_math/runs/{run}/edit"
        man = json.load(open(edit_dir / "manifest.json"))
        z = np.load(edit_dir / "edit.npz")
        names = [t["name"] for t in man["tensors"]]
        tensors = S.load(str(BASE), names)
        per_tensor, lora = [], {}
        for i, t in enumerate(man["tensors"]):
            _, base_bits = tensors[t["name"]]
            assert hashlib.sha256(np.ascontiguousarray(base_bits).tobytes()).hexdigest() == t["base_sha256"]
            edited_bits = rebuild(base_bits, t, z, i)
            assert hashlib.sha256(np.ascontiguousarray(edited_bits).tobytes()).hexdigest() == t["edited_sha256"]
            changed_cols = np.where(np.any(edited_bits != base_bits, axis=0))[0]
            res = analyse_tensor(t["name"], base_bits, edited_bits, changed_cols)
            U, s, Vt = res.pop("_U1"), res.pop("_s"), res.pop("_Vt")
            for r in (1, 4, 16, 64, 256):
                if r <= len(s):
                    lora[f"{t['name']}::r{r}::B"] = (U[:, :r] * s[:r]).astype(np.float32)
                    lora[f"{t['name']}::r{r}::A"] = Vt[:r].astype(np.float32)
            per_tensor.append(res)
            r1 = res["by_rank"]["1"]
            print(f"[{run}] {t['name'].replace('model.language_model.', '')}: σ1/σ2={res['sigma1_over_sigma2']:.1f} "
                  f"r1 err={r1['relative_error']:.2e} r1 bf16-match={r1['bf16_bitmatch']:.4f} "
                  f"99.9%-energy rank={res['rank_for_energy']['0.999']} "
                  f"ablation-fit c={res['output_side_ablation_fit']['scale_c']:.3f} "
                  f"err={res['output_side_ablation_fit']['relative_error']:.2e}")
        np.savez_compressed(LORA_OUT / f"{run}_lora.npz", **lora)
        summary[run] = {"label": label, "tensors": per_tensor}
    (OUT / "representation.json").write_text(json.dumps(summary, indent=1))
    write_markdown(summary)
    print(f"\nwrote {OUT/'representation.json'}, {OUT/'representation.md'}, LoRA factors in {LORA_OUT}")


def write_markdown(summary: dict) -> None:
    lines = ["# Milestone 0 — LoRA representability of the paper's Qwen3.5-0.8B edits", "",
             "Generated by `scripts/m0_representation.py`. ΔW computed from the exact evaluated bf16 tensors.", ""]
    for run, d in summary.items():
        lines += [f"## {run} ({d['label']}) — {len(d['tensors'])} tensor(s)", "",
                  "| tensor | rel. change | changed cols | σ1/σ2 | rank @99.9% energy | rank-1 rel. err | "
                  "rank-1 bf16 bit-match | ablation fit c | ablation fit err |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for t in d["tensors"]:
            r1 = t["by_rank"]["1"]
            f = t["output_side_ablation_fit"]
            lines.append(
                f"| `{t['name'].replace('model.language_model.', '')}` | {t['relative_change']:.3f} | "
                f"{t['changed_columns']} | {t['sigma1_over_sigma2']:.1f} | {t['rank_for_energy']['0.999']} | "
                f"{r1['relative_error']:.2e} | {r1['bf16_bitmatch']:.4f} | {f['scale_c']:.3f} | {f['relative_error']:.2e} |")
        lines.append("")
    (OUT / "representation.md").write_text("\n".join(lines))


if __name__ == "__main__":
    main()
