# Milestone 0.5 control — the same sycophancy task on pre-norm Qwen3.5-0.8B

**Why:** on Gemma 3 270M, Astra's strict one-shot LoRA recovered only 15% of a gradient LoRA's gain. Leading
explanation: Gemma normalizes every sublayer's output before adding it to the residual stream, so no LoRA-writable
module writes linearly into it. Qwen3.5-0.8B is **pre-norm** (sublayer outputs are added directly), so the same task
on Qwen isolates norm placement.

**Setup:** identical metric, prompts, isolation and Mode A v3 harness as Gemma (`LSO_TARGET=qwen`). Facts: the paper's
501-fact pool filtered to facts Qwen knows (486), split with the paper's `split()` (pair 100: 162 held-out, 324 train;
diagnostics = first 150 train). Qwen in non-thinking mode. Write space: rank ≤ 8 LoRA on the 48 modules that write the
residual stream (`linear_attn.out_proj` / `self_attn.o_proj` and `mlp.down_proj`, 24 layers). Validator cap 5× ‖W‖.

## Results (held-out)

| Method | Follows wrong guess | Reworded guess | Agrees with correct guess | Plain acc | Gain recovered (template / reworded) |
|---|---:|---:|---:|---:|---:|
| Base | 32.1% | 49.8% | 99.4% | 100.0% | — |
| Random direction ablation (norm-matched) | 34.8% | 46.4% | 99.4% | 99.4% | 0% / 7% |
| Scripted diff-of-means, fixed mid layer (12) | 64.0% | 59.4% | 100.0% | 99.4% | **worse than base** |
| Scripted, layer selected on train facts (feedback) | 14.8% | 39.9% | 98.8% | 100.0% | 54% / 20% |
| **Astra Mode A v3** (no feedback) | **14.2%** | **31.3%** | **99.4%** | **100.0%** | **56% / 37%** |
| Gradient LoRA, rank 8, same modules | 0.0% | 0.2% | 99.4% | 99.4% | 100% / 100% |

Base sycophancy by phrasing (held-out): paper template 32%; "My teacher told me it's X." 82%; "I'm pretty sure it's
X, right?" 62%; "I believe the answer is X. Q" 5%.

## Gemma vs Qwen, same harness (Mode A v3)

| | Gemma 3 270M (post-sublayer norm) | Qwen3.5-0.8B (pre-norm) |
|---|---:|---:|
| Gain recovered, template / reworded | 15% / 16% | **56% / 37%** |
| Agreement with correct guesses | 98% | 99% |
| Astra's edit | 2 modules (rank 3 + 3), layers 10 & 11 | 2 modules (rank 1 + 8), layers 14 & 19 |
| ‖ΔW‖ / ‖W‖ of the edits | 0.07 and **1.95** (pinned at the old 2× cap) | 0.16 and 0.12 |

## Findings

1. **One-shot editing works much better on the pre-norm model:** 56% vs 15% of the gradient gain on the main template,
   with no damage to agreement or knowledge, using small edits (≤ 0.16× ‖W‖). On Gemma, Astra needed an edit larger
   than the weights themselves and was still limited — consistent with the post-sublayer norm absorbing it.
2. **Astra (no feedback) matches the best scripted baseline, which used feedback** to pick its layer, and generalizes
   better to held-out phrasings (37% vs 20% of gain). The scripted recipe *without* feedback makes Qwen worse.
3. **Astra's edit is compact and mechanistic:** a rank-1 conditional correction in layer 14's MLP (fires on
   wrong-guess contexts, nulls plain and correct-guess means) plus rank-8 damping of "answer copying" in layer 19's
   full-attention output — 29K parameters, vs ~1.2M for the gradient LoRA.

## Caveats

- One run per configuration. Base sycophancy differs (Gemma 100% vs Qwen 32%), so "gain recovered" normalizes for
  headroom but the tasks are not identical in difficulty.
- Gemma v3 ran with a 2× norm cap that bound its edit; a rerun with the 5× cap is in progress to remove the confound.
- Qwen's linear-attention layers ran on PyTorch fallback kernels (correct but slow); results are unaffected.
