# Harness comparison: API-only vs Agency (native, Codex)

**Date:** 2026-11-05 · **Model:** GPT-6 Astra on Azure Foundry (`gpt-6-astra`, Responses API), reasoning effort `high`
· **Host:** EC2 m7i.xlarge (CPU), Agency `163ef8f`, Codex 0.147.0 · **Code:** [`experiments/harness_compare/`](../../experiments/harness_compare/)

## Task

A miniature of Milestone 0: given `base.npy` / `edited.npy` (256 × 512, bf16 precision), recover a column-restricted
rank-1 output-side ablation `ΔW = -c · r̂ (r̂ᵀ W)` — its rank, the 32 changed columns, the scale `c = 6` and the
direction `r̂` — using Python. Ground truth was kept outside the editor-visible tree.
Identical task text, files (`/workspace/task`), model and effort for all three.

## Results

| | API-only (`run_api.py`) | Agency, native harness | Agency, Codex harness |
|---|---:|---:|---:|
| Correct (rank, columns, c, r̂) | ✅ 4/4 | ✅ 4/4 | ✅ 4/4 |
| \|cos(r̂, truth)\| | 0.999999 | 0.999999 | 0.999999 |
| Model calls | 3 | 7 | 14 |
| Tool calls | 2 python + 1 submit | 2 bash + 4 submit_output | 5 bash + output |
| Wall time | **18 s** | 61 s | 118 s |
| Input / output tokens | **3.2K / 0.8K** | 22K / 1.7K | 183K / 4.3K |
| Sandbox | none (plain subprocess) | Docker container | Docker container |
| Profiling / telemetry | our own JSONL (latency, tokens per call) | agprof: LLM p50/p95 latency + TTFT, tool latencies, per-process CPU/RAM, syscalls, Perfetto trace | same as native |
| Swap model / harness | edit code | config change | config change |

Setup cost: API-only ran immediately. Agency needed a custom sandbox image (numpy + Codex) and, for Codex, an explicit
in-image binary path (`harnessadapterconfig(binary_path="/usr/local/bin/codex")`); the first Codex attempt failed
until that was set.

## Takeaways

1. **All three are equally correct here**; the harness does not change the answer on a task this size.
2. **API-only is far lighter**: ~7× fewer input tokens than Agency-native and ~58× fewer than Codex, 3–6× faster.
   Codex's overhead is its large per-call system prompt and tool schemas (~13K tokens per call).
3. **Agency's value is real but structural**, not accuracy: a container sandbox for editor code (the API-only loop
   has none yet — we would have to build one, e.g. bubblewrap as the paper did), a detailed profiler, and
   model/harness swaps by config. Its per-call token counts were only reported in aggregate in the profile summary.
4. Absolute costs are small either way (≈ $0.06 API-only, ≈ $0.30 native, ≈ $1–2 Codex at list prices before caching).

## Recommendation

Use **Agency with the native harness** for LSO experiment runs: it gives the sandbox and profiler we need at a modest
token overhead. Keep `run_api.py` as the lightweight reference loop for strict-protocol checks and debugging.
Use the **Codex harness** only where matching the paper's setup matters, budgeting ~10× the tokens.
