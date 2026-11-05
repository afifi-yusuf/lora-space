# Milestone 0 — findings (representation part)

**Question:** can LoRA represent the paper's released Qwen3.5-0.8B weight edits?
**Script:** [`scripts/m0_representation.py`](../../scripts/m0_representation.py) (CPU, ~20 s) · full table:
[`representation.md`](representation.md) · raw numbers: [`representation.json`](representation.json)

All three edits were rebuilt bit-exactly from the public base weights (every tensor hash matches the paper's manifest).

| Edit | Tensors | Structure found | LoRA fit |
|---|---|---|---|
| **50 passes** (MATH-500 7.9 → 48.1) | MLP `down_proj`, layers 15 & 19 | **exactly** `ΔW = −6 · r̂ (r̂ᵀ W)` on 64 columns per layer (fitted c = 6.000) | **rank 1** per tensor: σ1/σ2 ≈ 1,550–1,770, rel. error 0.2–0.3%, 99.8% of bf16 values bit-identical |
| 10 passes | 30 attention/MLP output matrices, layers 8–22 | exactly `ΔW = −1.5 · r̂ (r̂ᵀ W)` (c = 1.500) | rank 1 per tensor: rel. error 3–5% (bf16 rounding of a small update), ~95% bit-identical |
| 25 passes | `o_proj`, layer 15 (one head zeroed) | input-side removal of a 256-dim head subspace | **not low-rank** (~253); needs rank ≈ 256 |

**Notes**
- The successful edit is the brief's *output-side* rank-1 primitive with a large overshoot (c = 6 flips the
  direction and pushes ~5× past removal), restricted to the 64 neurons that write it most.
- The removed directions are related but not identical: |cos| = 0.85 between the 50-pass edit's two layers,
  0.58–0.72 vs. the 10-pass directions — a shared "repetition subspace" rather than a single vector.
- LoRA factors for ranks 1–256 are saved (git-ignored) in `checkpoints/m0_lora/`.

## Behavioral equivalence (teacher-forced)

[`scripts/m0_equivalence.py`](../../scripts/m0_equivalence.py) · [`equivalence.json`](equivalence.json): the paper's
released MATH-500 reasoning texts from the exact 50-pass model (30 texts × first 1,024 generated tokens = 30,720 tokens,
thinking mode), scored by the exact edit, the rank-1 LoRA merge and the unedited base.

| vs. exact 50-pass edit | Mean KL | 99th pct KL | Top-1 agreement |
|---|---:|---:|---:|
| **Rank-1 LoRA version** | **0.00035** | 0.0024 | **99.5%** |
| Unedited base (size of the edit) | 0.0136 | 0.157 | 97.2% |

The LoRA's deviation from the exact edit is ~39× smaller than the edit's own effect; the residual is bf16 rounding.

**Still running (sampled accuracy, L4, ~15–18 h):** evaluate the rank-1 LoRA version with the paper's protocol (vLLM, temperature 0.6,
top-p 0.95, top-k 20, presence penalty 1.5, ≤ 32,768 tokens) and confirm it reproduces 48.1% on MATH-500.
