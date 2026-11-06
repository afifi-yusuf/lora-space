# Code request, Qwen3.5-0.8B, 2026-11-06 (`scripts/lso_request.py`, `scripts/lso_data_baseline.py`)

Request: "Make this model better at Python coding tasks..." (`REQUESTS["code"]`). Held-out scoring: EvalPlus HumanEval+
(164) and MBPP+ (378), thinking off, greedy. Standard error is about ±3.6 points on HumanEval+ and ±2.3 on MBPP+.

| Method | Adapter params | HumanEval+ base / plus | MBPP+ base / plus | MBPP renamed (no_code) |
|---|---|---|---|---|
| Base | — | 32.3 / 29.9% | 27.3 / 22.2% | 108 |
| Astra Mode A, rep 1 (L7, L11 o_proj) | 49K | 34.1 / 31.1% | 25.1 / 20.4% | 105 |
| Astra Mode A, rep 2 (L11, 15, 19 o_proj) | 74K | 34.1 / 30.5% | 25.7 / 20.9% | 105 |
| Astra Mode B, 5 scored candidates (L12 down_proj, rank 1) | 4.6K | 31.7 / 29.3% | 28.8 / 23.5% | 107 |
| Astra writes 240 examples (blind) + gradient LoRA r8 | 1.47M | 25.0 / 21.3% | 27.0 / 24.3% | 80 |
| Ceiling: fix only the function name | — | — | 42.6 / 33.6% | 0 |

- **Nothing moved the held-out score beyond noise.** Mode A is +2 on HumanEval+ and −2 on MBPP+ in both reps; Mode B is
  within ±1.5 everywhere.
- **No Astra weight edit touched the real failure.** The model renames the required function on 108 of 378 MBPP+
  tasks. All three Astra adapters leave that at 105–107. Each targeted something vaguer: "spec-sensitivity",
  "context amplification", "concision".
- The data baseline is the only method that reduced renaming (108 → 80). But its replies got worse on HumanEval+
  (−7 points), so it nets out flat. It took 38 min of Astra time (118K output tokens) and 2 min of training.
- Conclusion: for code, the bottleneck is the diagnosis, not the weight writing. Harness v1 should make Astra bucket the
  base model's failures on its own tests before it writes anything.
