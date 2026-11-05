# Milestone 0.5 — can Astra remove sycophancy from Gemma 3 270M IT with a LoRA it writes?

**Date:** 2026-11-05 · **Target:** `google/gemma-3-270m-it` @ `ac82b4e` · **Editor:** GPT-6 Astra (Azure, effort `xhigh`)
· **Data:** the paper's Experiment 7 facts, pair 100 split (diagnostics = 150 train facts; feedback = train facts 150–300;
held-out = 146 facts never shown) · **Code:** [`scripts/m05_baselines.py`](../../scripts/m05_baselines.py),
[`scripts/m05_editor.py`](../../scripts/m05_editor.py), [`scripts/m05_diagnose.py`](../../scripts/m05_diagnose.py),
[`src/lso/gemma_syco.py`](../../src/lso/gemma_syco.py)

**Metric (the paper's):** on held-out facts the model knows, does it prefer "The answer is {wrong guess}." over the
correct answer when the user suggests the wrong guess? Plus three held-out rephrasings of the guess (never shown to
anyone), agreement when the guess is correct, and plain-question accuracy. Write space for every method: rank ≤ 8 LoRA on
`o_proj` / `down_proj`, 18 layers.

## Results (held-out)

| Method | Follows wrong guess (known facts) | Reworded guess | Agrees with correct guess | Plain acc | Gain recovered* |
|---|---:|---:|---:|---:|---:|
| Base | 100.0% | 83.7% | 100.0% | 97.9% | — |
| Random direction ablation (norm-matched) | 100.0% | 85.0% | 100.0% | 94.5% | 0% |
| Scripted diff-of-means ablation, fixed mid layer | 94.1% | 60.4% | 99.3% | **58.2%** | 6% (breaks knowledge) |
| Scripted, layer selected on train facts | 100.0% | 72.3% | 100.0% | 97.3% | 0% |
| Astra Mode A, prompt v1 (minimal) | 100.0% | 76.3% | 100.0% | 97.3% | 0% |
| Astra Mode A, prompt v2 (+ explicit success criterion) | 97.9% | 77.4% | 100.0% | 97.9% | 2% |
| **Astra Mode A, prompt v3** (+ method hints, module-input tool, token ids) | **84.8%** | **70.5%** | **97.9%** | 94.5% | **15%** |
| Astra Mode A, prompt v3, norm cap raised to 5× (rerun) | 80.6% | 67.2% | 97.3% | 91.8% | 20% |
| Astra Mode B, prompt v2 (10 scored candidates on feedback facts) | 47.3% | 42.5% | 74.0% | 89.7% | 54% |
| Gradient LoRA, rank 8, same modules (honest targets) | 1.4% | 3.0% | 100.0% | 99.3% | 100% |
| Honest full fine-tune (the paper's recipe) | 0.7% | 3.2% | 99.3% | 98.6% | 101% |

\* (base − method) / (base − gradient LoRA) on the wrong-guess follow rate.

## Findings

1. **A fix exists in the write space.** A gradient-trained rank-8 LoRA on the same modules removes sycophancy almost
   completely with no regressions, so failures below are about *finding* the update, not representing it.
2. **The obvious scripted recipe does not work.** Removing the "guess present vs plain" direction everywhere barely
   reduces sycophancy and destroys plain-question accuracy (98% → 58%).
3. **Strict one-shot editing improves with guidance but stays far from gradients:** 0% (v1) → 2% (v2) → 15% (v3) of
   the gradient LoRA's gain. v3 is the first edit that moves the behavior while keeping agreement with correct guesses.
4. **Feedback helps but trades off.** With 10 scored candidates Astra halves sycophancy, but agreement with correct
   guesses drops to 74%: its directions mix "defer to a wrong guess" with "agree with the user".
5. **v1 post-hoc diagnostic** ([`diagnose_*.json`](diagnose_astra_modeA_hint_20261105T195541.json); uses feedback, not
   Mode A): v1's direction was partly right but ~3× too weak; scaling it 3× (chosen on train facts) gives 68% follow
   held-out, and beyond that the effect saturates (~35–40%) while agreement with correct guesses collapses.

## Leading hypothesis: Gemma's post-sublayer norm

Gemma 3 applies RMSNorm to each sublayer's output *before* adding it to the residual stream
(`h ← h + g ⊙ RMSNorm(W_o x + ΔW x)`), so no LoRA-writable module writes linearly into the residual stream. Edits get
renormalized (they can redirect but not amplify a sublayer's write), distorted by the per-channel gain, and scaled
differently per input. This predicts exactly the saturation in finding 5 and explains why gradients (which see the
nonlinearity) succeed where one-shot sizing undershoots. Pre-norm models (Qwen, Llama, Mistral, DeepSeek) add
`ΔW x` linearly. **Planned control:** the same task on pre-norm Qwen3.5-0.8B.

## Caveats

- One run per configuration (no seeds yet); prompts v2 and v3 were written after seeing v1 (researcher-revised).
- The validator capped updates at 2× the base weight norm, and v3 sized its edit to 1.95×. Rerun with a 5× cap: Astra
  used 2.47× and reached 20% of the gradient gain (vs 15%), with plain accuracy falling to 92% — the cap was not the
  main limitation.
- Astra cost per run ≈ $2–4 (0.8–1.3M input tokens, mostly cached; 30–47K output).
