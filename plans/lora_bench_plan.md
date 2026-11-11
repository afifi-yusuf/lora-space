# LoRA-Space Bench: plan (2026-11-11)

**Goal:** a public leaderboard of (editor model × harness) combinations that write LoRA adapters for frozen models from
a natural-language request, released as soon as it is ready; paper later. Modeled on weight-space-bench (same
settings for every entry, several attempts, normalized scores, cost columns) and Frontier-CS (entries are model +
harness pairs, a dev-feedback track, one final submission scored on hidden workloads).

**Decisions (from the user, 2026-11-11):** public benchmark first; release as soon as ready; editors GPT-6 Astra,
Claude Fable 5.2, Claude Opus 5.5, starting with Astra only; GPU budget up to US$1,000. All three are deployed on the
Azure Foundry resource `principle` (one key; Claude via `https://principle.services.ai.azure.com/anthropic/v1/messages`).

**Harness per model (2026-11-11):** the main board shows each model with its best harness, chosen on dev splits in a
short selection run (not on the held-out sets, to avoid picking a lucky harness). A second view runs every model on
Agency native, for a model-vs-model comparison with the harness held fixed.

**Baselines (2026-11-11):** no full-weight runs of our own. For Qwen3.5-0.8B math, the full-weight reference is the
published Takehi et al. (MIT) result: their 50-pass edit (48.1% reported; 56.8% exact / 53.5% as rank-1 LoRA on our
200 × 2 subset) and its cost (158 turns, 80 Python runs, 20.3 h, effort max). For 2B (later, not urgent) and every
other task, the reference is the gradient LoRA (rank 8, same modules). The headline is accuracy against cost
(editor tokens/$, GPU-hours, wall time per run), logged for every run.

## 1. What an entry does

Input: a task = frozen target model + the user's request (one sentence or two, no diagnosis, no hints) + the rules.
Output: one adapter `adapter.npz` (ΔW = B·A, rank ≤ 8, ‖ΔW‖ ≤ 5‖W‖, allowlisted modules only), committed once.

| Track | Feedback before committing | Analogue |
|---|---|---|
| A, one-shot | Unedited model only: weights, generations, activations | The paper's no-tools spirit |
| B, dev feedback | Also up to 5 candidate adapters scored on a **dev** split (score + samples) | Frontier-CS dev workloads |

Entries are named like Frontier-CS: `GPT-6 Astra (Codex)`, `GPT-6 Astra (Agency native)`, `Claude Opus 5.5 (Claude Code)`.

## 2. Architecture (Agency)

```
host (GPU box) ─────────────────────────────────────────────────────────────┐
  target service: vLLM server (base / candidate) + HF inspector, budgets,   │
                  per-call log; exposed as Agency agtools / MCP:            │
                  generate, inspect, inspect_module_inputs,                 │
                  evaluate_candidate (track B only), commit_adapter         │
  scorer: merge adapter -> bf16 checkpoint -> hidden held-out sets          │
  Agency: Agent(model, harness) + agprof profile per run                    │
     └─ Docker sandbox: numpy/scipy/safetensors, NO torch, NO GPU,          │
        read-only weights + practice examples, network only to the LLM API  │
────────────────────────────────────────────────────────────────────────────┘
```

- The rules are enforced by construction, not by the prompt: no torch or GPU in the sandbox means no gradients and no
  private forward passes; every model call goes through the budgeted service.
- Harness-agnostic: the same tools reach Claude Code, Codex, OpenCode and Agency native through Agency's MCP proxy
  (`agtool`, `add_sandbox_mcp_tools`). Adapters exist for claude_code, codex, native, opencode, kimi, grok.
- Agency's profiler gives the cost/time columns (LLM latency, tokens, tool time) for free.
- Our current API loop (`scripts/lso_request.py`) stays as the reference "minimal harness" entry.

## 3. Tasks

A task enters the benchmark only if it **qualifies**: base fails ≥ 30%; a system prompt leaves most of the gap; a
gradient LoRA (rank 8, same modules) closes most of it; held-out items the editor never sees.

| # | Task (request) | Target | Held-out score | 0 = | 100 = | Status |
|---|---|---|---|---|---|---|
| T1 | "Make this model better at math" (thinking on) | Qwen3.5-0.8B | MATH-500 (200 × 1, think35, 32K) | base 8.0% | ceiling (below) | Request written; harness change untested |
| T2 | Same request | Qwen3.5-2B | Same | base (to measure) | ceiling | Needs a base run |
| T3 | "Always reply in the user's language" | 0.8B / 2B | Language Confusion Benchmark pass rate | base | gradient LoRA | Needs qualification |
| T4 | "Stop agreeing with users' wrong guesses" | 0.8B | Held-out follow rate | base 32.1% | gradient 0% | Qualified (sycophancy) |
| T5 | "Better at Python coding" | 0.8B | MBPP+ / HumanEval+ | base 27.3% | rename ceiling 42.6% / gradient | Baselines done |

- **Math ceiling:** two references, both reported: (a) the paper's edit as a rank-1 LoRA (51.2% on 500 × 4); (b) a
  gradient LoRA trained on the base model's own correct, finished solutions to MATH train (self-distillation, rank 8,
  same modules). 100 = the better of the two.
- **Damage check** after every edit: a fixed small general set (thinking off, short answers, ~10 min on an L4). Drop
  > 3 points flags the entry's run.
- **Leaderboard score:** per task, mean normalized score over 3 attempts; overall = median across tasks (as
  weight-space-bench). Also cost per run and tokens.
- **Fast proxy for development only:** share of 100 MATH problems finished within 8K tokens (~20 min). Never used on
  the leaderboard.

## 4. Phases

| Phase | Work | GPU | Est. cost |
|---|---|---|---|
| 0. Build (no GPU) | Target service + MCP tools; Agency runner (model × harness config); sandbox image; task spec format (`tasks/<id>/task.toml`); scorer + normalized score + damage check; settings hash + audit; leaderboard (md/csv/png) | 0 h | $0 |
| 1. Smoke test | One T1 Track A run with Astra through Agency native on the g6, end to end | ~5 h | ~$5 |
| 2. Qualify + ceilings | T1 gradient ceiling; T2 base; T3 base / system prompt / gradient / random; damage-set base numbers | ~40 h | ~$45 |
| 3. Astra entries | Harness selection on dev splits (minimal loop, Agency native, Codex; 1–2 attempts each), then the full grid with the chosen harness (+ Agency native if different): qualified tasks × 3 attempts, Track A then B. Also answers "does Astra find the loop with no hint?" | ~150 h | ~$170 |
| 4. Claude entries | Fable 5.2 and Opus 5.5: selection between Claude Code and Agency native, then the same grid | ~250 h | ~$280 |
| 5. Release | Public repo + leaderboard page + protocol README; user approves before anything is published | 0 h | $0 |
| Reserve | Reruns, failures | ~150 h | ~$170 |

GPU: about 4 L4-hours per run (≈1 h session holding the GPU + 2–3 h held-out scoring for math; ≈1 h for short tasks).
On-demand g6.2xlarge/g6.4xlarge ≈ $1–1.3/h. API costs (Azure, Anthropic) are separate.

Parallelism: G quota 24 vCPUs allows 3 × g6.2xlarge (3 L4s) at once. Phases 3–4 take ~1 week at 3 boxes; a quota
increase to 48 (one g6.12xlarge with 4 L4s, or 6 × g6.2xlarge) roughly halves that.

## 5. Risks

- **Contamination:** the Takehi et al. paper (Nov 2) describes the math fix; newer editors may recall it. Allowed
  (it is public), but logged: we record whether a run cites the paper or the loop direction. T2–T5 are not in it.
- **Harness overhead:** Codex used ~58× the tokens of the minimal loop in our calibration task (§ harness_compare);
  budgets are per run, not per token, so this shows up as cost, not as a cap.
- **Scoring noise:** 200 × 1 MATH has SE ≈ 3.5 points; fine for the 8% → 50% effect, too coarse for close entries.
  Ties are reported with bootstrap intervals, Frontier-CS style.
- **Capacity:** L4 starts sometimes fail (InsufficientInstanceCapacity); runs must be resumable per (entry, task,
  attempt).

## 6. Open items for the user

1. Opus 5.5 deployed on Azure Foundry and tested (2026-11-11, same key as Astra). Fable 5.2 deployment FAILED:
   `MarketplaceSubscriptionCannotBeCompleted` (Fable is hosted on Anthropic infrastructure and sold through the Azure
   Marketplace; Opus 5.5 v2 is Azure-hosted). Needs a subscription that allows Marketplace purchases, Microsoft support,
   or a direct Anthropic API key.
2. Whether to request a G-quota increase to 48 vCPUs (AWS, same wording as before).
3. Public repo name and home (e.g. `afifi-yusuf/lora-space-bench`) and license (MIT code, CC BY 4.0 data like the
   paper's release).
