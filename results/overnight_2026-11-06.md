# Overnight queue, 2026-11-06 (g6.2xlarge, 02:18–07:23 UTC)

Queue: `infra/overnight_queue.sh`; per-job logs: `results/overnight_logs/`. Gain recovered = (base − method) / (base −
gradient LoRA r8) on held-out follow rate (known facts). All Astra runs: GPT-6 Astra, effort xhigh, prompt v3, ≤ 60 turns.

## Qwen3.5-0.8B sycophancy (base 32.1%, gradient LoRA r8 0.0%)

| Method | Runs | Held-out follow rate | Gain recovered | Paraphrase follow (base 49.8%) |
|---|---|---|---|---|
| Astra Mode A, with hint | 4 | 14.2 ± 8.7% (5.0–25.9) | **0.56 ± 0.27** (0.19–0.85) | 25.3% |
| Astra Mode A, no hint | 2 | 25.6% (21.1, 30.2) | 0.20 (0.34, 0.06) | 31.6% |
| Astra Mode B, 10 scored candidates | 2 | 7.4% (8.0, 6.8) | **0.77** (0.75, 0.79) | 17.1% |
| Scripted, layer selected on train facts | 1 | 14.8% | 0.54 | 39.9% |
| Gradient LoRA rank 1 / 2 / 4 / 8 | 1 each | 0.0% | 1.00 | 0.4 / 0.0 / 0.0 / 0.2% |

- Mode A is high-variance: one run recovered 85%, another 19%. Mean and s.d. over 4 runs (sample s.d.).
- Mode B is better and more consistent. Both Mode B runs committed a 4.6K-parameter adapter (rank-1-sized).
- The method hint matters (0.56 → 0.20 without it), but n = 2 for no-hint.
- The gradient needs only rank 1 to remove sycophancy completely, so rank is not what limits Astra.
- Plain-question accuracy stayed ≥ 99.4% in every Astra run; right-guess accuracy ≥ 96.3%.

## Qwen3.5-2B sycophancy — not a usable target

Base follow rate on held-out known facts is only **6.0%** (8 of 133), and a random adapter moves it to 8.1%. The
queue's guard (skip 2B Astra runs below 10%) had a bug (the exit code was lost in a pipe; fixed), so 5 Astra runs
ran anyway. Their numbers (0.0–6.7% follow) are within noise of the base and should not be reported as gains.
Gradient LoRA r1/r8 → 0.0%. Scripted (layer-selected) → 4.4%.
**Takeaway:** the 2B is much less sycophantic; scaling the sycophancy task needs a harder prompt set, not just a bigger model.

## Code diagnosis — Qwen3.5-0.8B (HumanEval+ / MBPP+, EvalPlus)

| Setting | HumanEval+ base / plus | MBPP+ base / plus |
|---|---|---|
| Thinking off, greedy | 31.1 / 27.4% | 27.0 / 21.4% |
| Thinking on, 8K tokens | 32.9 / 29.3% | 22.0 / 15.9% |
| **MBPP+ with the function name fixed (ceiling)** | — | **42.6 / 33.6%** (off), **43.7 / 32.5%** (on) |

Failure buckets (thinking off): HumanEval+ 85 wrong output, 21 exceptions, 7 syntax errors. MBPP+ **109 renamed the
function** (counted as `no_code`), 89 wrong output, 40 exceptions, 27 syntax errors, 10 truncated.

**The finding:** on 29% of MBPP+ problems (42% with thinking) the model ignores the required function name, even though
the prompt's own test shows it (`similar_elements(...)` becomes `def find_shared_elements`, and the model rewrites the
test to match). Aliasing the name to the required one makes 59 of those 109 pass: MBPP+ 27.0% → 42.6%.
This is an instruction-following failure, a rule-tier edit target with a measured ceiling of +16 points.
2B code runs: re-running (vLLM start-up failures; fixed).
