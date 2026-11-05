# LSO — LoRA-Space Optimization

**Can a frontier LLM fine-tune a frozen model by *writing* its LoRA adapter, without gradients?**

LSO extends [Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/) (Takehi et al., 2026)
from editing a small model's base weights to programming **LoRA adapters for much larger frozen models**. An editor
LLM (GPT-6 Astra) inspects the target through tools — weights, activations, diagnostic prompts — and writes the adapter
in Python. The base model is never modified and no gradient is ever computed.

> "Optimization" here means selecting a good point in LoRA space. In the strict setting (Mode A) that selection is made
> by reasoning alone: no gradients and no evaluation of candidate adapters before the editor commits.

The full research brief is in [`LSO_CLAUDE_CODE.md`](LSO_CLAUDE_CODE.md).

## Status

| Milestone | What it tests | Status |
|---|---|---|
| **0** — representation | Can LoRA represent the paper's released Qwen3.5-0.8B edits (the 7.9% → 48.1% MATH-500 fix)? | in progress |
| **0.5** — Mode A pilot | Astra writes a one-shot LoRA that removes sycophancy from Gemma 3 270M IT | in progress |
| 1 — 8B dense | One-shot discovery on an 8B target vs. a scripted ablation baseline | planned |
| 2 — scaling | Fixed LoRA budget, 8B → 30B-A3B MoE → 32B → ~100B MoE | planned |
| 3 — compositional | Astra composes a library of LoRAs vs. TIES / DARE / LoraHub | planned |

Results land in [`results/`](results/) as they come in.

## Experimental modes

| Mode | Editor reads | Editor writes | Gradients |
|---|---|---|---|
| **A** strict one-shot | base activations / weights, pre-edit only | one LoRA, one commit | none |
| **B** feedback-guided | + scores of candidate adapters | revised LoRA | none |
| **C** compositional | a library of LoRAs on the same base | combination / edit of library LoRAs | upstream only |

The paper's Qwen result is Mode B (its forward-pass tool scored candidate edits on practice problems).
LSO's primary claim is Mode A.

## Repository layout

```text
LSO_CLAUDE_CODE.md        research brief (goals, tiers, baselines, milestones, go/no-go)
src/lso/
  primitives.py           closed-form rank-1 edits (input/output-side ablation), SVD → LoRA
scripts/
  smoke_azure_astra.py    checks the Azure Astra endpoint: Responses API, effort levels, reasoning round-trip
  m0_representation.py    Milestone 0: rebuild the paper's edits, SVD, LoRA fit, bf16 fidelity
infra/
  user-data.sh            EC2 boot script: idle auto-stop after 60 min
  launch_retry.sh         retries GPU launches across us-east-1 zones when capacity is short
results/                  committed summaries (JSON / Markdown); bulky generations are git-ignored
tests/                    unit tests (pytest)
```

## Setup

```bash
git clone https://github.com/afifi-yusuf/lso.git && cd lso
uv sync --extra dev            # CPU tools; add --extra gpu on the GPU box
uv run pytest
```

**Secrets.** Put credentials in `secrets.env` at the repo root (git-ignored, keep it `chmod 600`):

```bash
AZURE_OPENAI_API_KEY=...       # Azure Foundry project "proj-default", deployment gpt-6-astra
```

**Editor endpoint.** GPT-6 Astra on Azure Foundry, OpenAI-compatible Responses API:
`https://principle.openai.azure.com/openai/v1`, model/deployment `gpt-6-astra`, reasoning effort up to `max`.
Verify with `uv run python scripts/smoke_azure_astra.py`.

**External data** (git-ignored, fetched on demand):
- `ext/lm_understand-logs/` — the paper's released logs, exact edit diffs, eval code and sycophancy dataset
  ([RikiyaT/lm_understand-logs](https://github.com/RikiyaT/lm_understand-logs), CC BY 4.0 / MIT).
- `models/` — Hugging Face checkpoints (`Qwen/Qwen3.5-0.8B` @ `2fc0636`, `google/gemma-3-270m-it` @ `ac82b4e`).

**Compute.** One AWS GPU instance in us-east-1 (g6e.xlarge, L40S 48 GB, for Milestones 0–0.5; p5.4xlarge, H100 80 GB,
from Milestone 1). Instances stop themselves after 60 idle minutes.

## Acknowledgements

Builds directly on the released logs, edits and datasets of Takehi, Teoh, Zhang & Khattab,
*Sparks of Weight-Space Programming* (2026).
