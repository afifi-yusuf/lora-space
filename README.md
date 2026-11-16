# LoRA-Space Bench

**A benchmark for editing models by writing their weights.**

An editor model is given a frozen target model and a short request in plain English, such as "make this model better
at math". It inspects the target through a fixed set of tools and writes a LoRA adapter by hand, as arrays of numbers.
It gets no gradients and no training loop, and it commits once. The adapter is then scored on held-out data.

Results, every run's tool calls, and a drawing of each committed adapter are at **[loraspace.org](https://loraspace.org)**.

The benchmark extends [Weight-Space Programming](https://rikiyat.github.io/blog/weight-space-programming/)
(Takehi et al., 2026) from editing a small model's base weights to writing low-rank adapters, and from one editor to a
grid of editors and harnesses.

## How a run works

1. **The editor gets the task.** One frozen target, the user's request, a file of practice examples, and the rules.
   The request carries no diagnosis and no hints.
2. **It studies the unedited model.** Every forward pass goes through the target service on the GPU host, which counts
   and logs each call. The editor's own code runs in a sandbox with numpy, scipy and safetensors, and with no torch
   and no GPU, so it cannot compute gradients or run the model privately.
3. **It commits one adapter.** `adapter.npz` holds a pair of matrices (B, A) per edited module, with ΔW = B·A. The
   commit is validated against the limits below and ends the session.
4. **The adapter is scored.** It is merged into a copy of the target and run on a held-out set the editor never saw,
   followed by a damage check on abilities the request did not mention.

### Entries

An entry is an editor model paired with the harness it works in. Each model runs twice: once in Agency's native
harness (a minimal ReAct loop with a bash tool) and once in its maker's own agent, such as Claude Code, Codex,
OpenCode or Kimi CLI. [Agency](https://github.com/agency-project/Agency) sits between the harness, the model provider and the sandbox, which is
how every entry gets the same tools and budget and how usage is recorded in one format.

Entries are listed in [`lsbench/config/entries.toml`](lsbench/config/entries.toml).

### Tasks

All three tasks currently target Qwen3.5-0.8B.

| Task | Request | Held-out score | 0 on the scale | 100 on the scale |
|---|---|---|---|---|
| `math_qwen08` | Make this model better at math (thinking on) | MATH-500, first 200 problems | unedited model, 8.0% | the paper's 50-pass full-weight edit, 56.8% |
| `syco_qwen08` | Stop going along with users' wrong guesses | share of wrong guesses followed, on facts the model knows | unedited model, 32.1% | gradient-trained rank-8 LoRA, 0% |
| `code_qwen08` | Make this model better at Python coding tasks | MBPP+ base tests, pass@1 | unedited model, 27.3% | fixing only the function name, 42.6% |

Scores are normalized per task so that 0 is the unedited model and 100 is that task's best reference. A score can be
negative (the edit made the model worse) or above 100.

Task files are in [`lsbench/config/tasks/`](lsbench/config/tasks/).

### Limits

The limits are the same for every entry.

| Limit | Value |
|---|---|
| Session wall time | 3 hours |
| `generate` calls | 25, up to 32 prompts each |
| Analysis calls (inspection and interpretability tools together) | 50, up to 32 items each |
| Adapter rank | at most 8 per module |
| Adapter size | ‖ΔW‖ ≤ 5‖W‖ per module, allowlisted modules only |
| Commits | one |

Two tracks exist. In Track A the editor sees only the unedited model. In Track B it may also score up to five
candidate adapters on a dev split before committing. The published grid is Track A, one attempt per cell.

### Tools

| Tool | What it returns |
|---|---|
| `generate` | the unedited model's replies to a batch of prompts |
| `inspect`, `inspect_module_inputs` | residual-stream activations and the inputs of writable modules, saved as arrays |
| `trace`, `token_stats`, `logit_lens`, `attribution`, `attention`, `top_activations`, `patch` | read-only interpretability tools over the unedited model |
| `evaluate_candidate`, `intervene` | Track B only: a candidate's dev score, or the effect of an activation intervention |
| `commit_adapter` | validates the adapter and ends the session |

No tool returns a weight gradient.

### Scoring and checks

- **Damage check.** After scoring, the edited model is tested on 300 MMLU questions, 200 GSM8K problems with thinking
  off, and held-out simple facts. A metric that drops by more than 3 points is flagged next to the score.
- **Audit.** Each run's transcript is searched for things the rules forbid (installing packages, importing torch or
  JAX, calling `.backward()`, fetching URLs). A hit is recorded in the run's `result.json`.
- **Comparability.** Each result carries a hash of the task, entry, limits, track and prompt. Only runs with the same
  hash are ranked together.

## Repository layout

```text
lsbench/                  the benchmark
  __main__.py             CLI: run, score, damage, leaderboard, list
  config/entries.toml     entries (editor model x harness) and the shared limits
  config/tasks/           one TOML file per task
  prompt.py               the task text and tool schemas every entry receives
  target.py               the target service: the only way an editor can run the frozen model
  interp.py               the interpretability tools
  run_agency.py           runs an entry in an Agency harness inside the Docker sandbox
  run_minimal.py          the pilot reference loop over the Responses API (not ranked)
  score.py, damage.py     held-out scoring and the damage check
  site.py                 builds the results site from the run records
  site_template.html      the site's markup, styles and scripts
  sandbox/Dockerfile      the editor's sandbox image
results/lsbench/
  runs/                   one directory per run: result, session record, tool calls, committed adapter
  pilots/                 runs made under earlier rule versions
infra/
  setup_gpu.sh            sets up a GPU host (pinned versions in requirements-gpu.lock)
  lsbench_setup.sh        adds Agency, the sandbox image and the task data to that host
  grid/                   launches and balances a fleet of GPU workers, and pulls back finished runs
src/lso/, scripts/        target-model definitions and the earlier LSO experiments the benchmark grew out of
paper/                    draft write-up of those experiments
plans/lora_bench_plan.md  the benchmark's design notes
```

## Running it

### Requirements

- A GPU host. One L4 (24 GB) is enough for Qwen3.5-0.8B. `infra/setup_gpu.sh` expects Ubuntu 24.04.
- Docker on that host, for the editor's sandbox.
- **[Agency](https://github.com/agency-project/Agency)**, the open-source layer the harnesses run in.
  `infra/lsbench_setup.sh` installs it from a checkout at `~/agency`, so clone it there first.
- API credentials for each editor model you want to run, in `secrets.env` at the repo root. The file is git-ignored;
  keep it `chmod 600`. The variable names each entry needs are in `entries.toml`.

### Set up a GPU host

```bash
git clone https://github.com/agency-project/Agency.git ~/agency
git clone https://github.com/afifi-yusuf/lora-space.git ~/lso && cd ~/lso
bash infra/setup_gpu.sh        # venv with vLLM, torch and transformers; the editor sandbox
bash infra/lsbench_setup.sh    # Agency, the Docker sandbox image, practice and held-out data
LSO_TARGET=qwen .venv/bin/python -m lsbench.selftest   # exercises every tool; no editor model involved
```

### Run an entry

```bash
set -a; . ./secrets.env; set +a
.venv/bin/python -m lsbench list
.venv/bin/python -m lsbench run --entry opus55-native --task math_qwen08 --track A --attempt 1
```

`run` holds the session, scores the committed adapter in a fresh process, runs the damage check and writes
`runs/lsbench/<entry>__<task>__<track>__a<attempt>/result.json`. A run that already has a result is skipped unless you
pass `--force`.

### Build the site

```bash
.venv/bin/python -m lsbench.site                                        # writes site/index.html
npx wrangler@3 pages deploy site --project-name loraspace --branch main  # publishes to loraspace.org
```

The site is one self-contained HTML file with the run data embedded. It needs no GPU and no server; building it
reads only `results/lsbench/` and the config files.

## Status

- **Rules version:** `lsbench-v0.3`.
- **Grid:** Track A, one attempt per cell, seven editor models across three tasks. Some cells are still being re-run after
  provider outages; the site shows which.
- **Not done yet:** repeated attempts, Track B, larger targets (Qwen3.5-2B is defined but has no tasks), and
  gradient-LoRA references for the math and coding tasks.

## Earlier work in this repo

The repository began as LSO (LoRA-Space Optimization), a set of experiments on whether one editor could write a LoRA
for a frozen model at all. Those results are in [`results/`](results/) and the draft in [`paper/`](paper/). The main
findings the benchmark builds on:

- The paper's winning Qwen3.5-0.8B math edit is exactly rank 1 per tensor, so a LoRA can represent it
  ([`results/m0/`](results/m0/)).
- Applied as a rank-1 LoRA, that edit scores 51.2% on MATH-500, against 7.9% for the unedited model.

The original research brief is [`LSO_CLAUDE_CODE.md`](LSO_CLAUDE_CODE.md).

## Acknowledgements

Builds on the released logs, edits and datasets of Takehi, Teoh, Zhang & Khattab, *Sparks of Weight-Space
Programming* (2026). The entry format (model plus harness) and the dev-feedback track follow
[Frontier-CS](https://frontier-cs.org/).
