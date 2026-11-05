# LSO — LoRA-Space Optimization

## Project brief for Claude Code

*Last revised 2026-11-05: added background on the Weight-Space Programming paper, the north-star goal and edit tiers, the read/write asymmetry, the output-side rank-1 primitive, Mode C (compositional), and the MoE scaling ladder. Then updated from the authors' released logs: Mode B confirmed, structure of the Qwen edits, the evaluation's decoding settings, the Gemma follow-up, and a sycophancy pilot (Milestone 0.5). Renamed from WOrA to LSO (LoRA-Space Optimization).*

**Name:** *LoRA-Space Optimization* (LSO) extends the paper's "Weight-Space Programming" from base weights to LoRA space. "Optimization" is meant in the general sense of selecting a good point in LoRA space. In the strict setting (Mode A), that selection is made by reasoning, with no gradients and no candidate evaluations. Say this early in any write-up so "optimization" isn't misread as gradient training.

**Goal:** Build a research prototype for **zero-shot, gradient-free adaptation of large frozen language models** by letting a capable *editing LLM* inspect model internals and **write LoRA adapter weights using Python**. The editing LLM does not update the base model. Instead, it has read/write access to LoRA matrices attached to selected layers of a much larger frozen *target model*.

**North star:** An editor LLM (e.g., GPT-6 Astra) **one-shot fine-tunes 10B+ models with only LoRA parameters in its editing space**. Section 2 turns this into a measurable claim.

**Central insight:** A frontier model may be able to reason about, diagnose, and program a small adapter parameter space even when the frozen target model is much larger than any network the editor could feasibly program directly. This is a hypothesis to test, **not an established capability**.

**Research question:** Can an LLM generate a useful LoRA update for a pretrained model **without task-specific gradient descent, training an adapter generator, or iteratively searching over candidate rewards**? If not, does limited feedback-guided weight-space programming work? Can it compose existing adapters better than standard merging methods?

## 0. Background: what the Weight-Space Programming paper shows and doesn't show

**Source:** Takehi, Teoh, Zhang, Khattab, *"Sparks of Weight-Space Programming: LLMs can natively read & write neural network weights"* (Nov 2, 2026; blog, alphaXiv, and X thread from @rikiyatakehi).

**Claims:**
- GPT-6 Astra identified 4 game policies (Breakout, Pong, Pac-Man, Freeway) from raw weights. Each network had 17,253 weights, and Astra had no tools or answer options.
- It patched a PPO car policy stuck on a ramp by editing 3.5% of the weights, reaching 100% success, in one reply with no tools.
- It wrote MinAtar Breakout weights from scratch in one reply: mean score 517.4, vs 25.3 for PPO trained for 500M steps.
- It edited 0.016% of Qwen3.5-0.8B's weights to fix reasoning loops:

| Qwen3.5-0.8B | MATH-500 | GSM8K | IFEval | Hit token limit |
|---|---:|---:|---:|---:|
| Base | 7.9 | 13.8 | 21.0 | 93.0 |
| Edited, 10 forward passes | 12.3 | 25.7 | 49.0 | 87.2 |
| Edited, 25 forward passes | 14.1 | 25.1 | 39.9 | 86.4 |
| Edited, 50 forward passes | 48.1 | 67.1 | 62.3 | 33.1 |

**Community Note on the X post (paraphrased):** The weights were given to the LLM as text. Per the authors' own logs, it used code and forward passes to ablate a "looping direction" in Qwen. Thinking-mode looping is a known issue listed on Qwen's model card. The edit mainly fixed repetition in that mode; it didn't "natively" improve the model's math in general. The authors' own summary figure agrees: the Qwen panel says Astra "edits the weights in a Python kernel."

**Replications:** The edited model is public at `huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming`, and the full logs, edits and eval code are at `github.com/RikiyaT/lm_understand-logs`. A third party rebuilt it from the logs and got 51.0% on MATH-500. An alphaXiv commenter measured 61.7% accuracy, with the token-limit rate falling from 88.7% to 17.6%.

**Takeaways for LSO:**
1. The Qwen result is **automated directional ablation with tools**. It does not show "native" weight reading at LLM scale. This is the precedent LSO builds on, and the baseline it must beat.
2. The "no tools, one reply" results apply only to tiny networks (~17K params). They do not transfer to 10B+ targets, where weights cannot fit in context.
3. Much of the "6× math" gain comes from fixing truncation: the base model hits the token limit 93% of the time.
4. The 10- and 25-pass edits barely moved the token-limit rate, and only the 50-pass edit worked. **The logs confirm this was Mode B** (§5): see below.
5. Open confound raised on alphaXiv: the prompt explicitly mentioned repetition and non-termination. Nobody has yet run it without those hints.

### What the released logs show (`lm_understand-logs`, read 2026-11-05)

The repo has everything sent to and from the model, every code run with its output, the evaluations, and the networks/edits. All 1,125 turns were audited as free of Codex's own tools; code ran only in the authors' sandbox (Experiments 3, 6, 7, 8). The editor was `gpt-6-astra` via the Codex CLI, at reasoning effort `max` for Experiment 8.

**Experiment 8 (Qwen3.5-0.8B math) was Mode B:**
- Astra had a persistent CPU Python kernel over the weights (≤300 code runs), GSM8K/MATH *train* practice problems, and a forward-pass tool.
- One "pass" = up to 512 practice generations, *or* a paired original-vs-edited comparison (256 each), *or* a teacher-forced read of up to 1,024 texts (log-probs, hidden states, MLP activations, attention). So "50 passes" can mean tens of thousands of generations, and candidate edits were scored on practice data. Test benchmarks were never shown; gradients were forbidden.
- The 50-pass run took 158 turns, 80 Python runs and 20.3 hours.

**The final edits are all LoRA-representable:**

| Run | Edit | Structure |
|---|---|---|
| 10 passes | Removes a "repetition" direction from 30 output matrices (attention + MLP), layers 8–22: \(W' = W - 1.5\,u(u^\top W)\) | Output-side rank-1 per tensor. The 1.5 factor overshoots, so it flips the direction rather than just removing it |
| 25 passes | Zeroes attention head 7 of layer 15 (256 output columns) | Rank ≤ 256 on one tensor |
| 50 passes | Subtracts the loop direction from the 64 MLP output columns that write it most, in layers 15 and 19 (2 × 64 × 1,024 = 131,072 weights) | Rank 1 per tensor on two tensors (to confirm in Milestone 0) |

**Decoding was already controlled.** Evaluation used temperature 0.6, top_p 0.95, top_k 20, **presence penalty 1.5**, and up to 32,768 new tokens. The base model still hit the cap 93% of the time, so the loops are not just an artifact of greedy decoding.

**Gemma 3 270M follow-up: no gain without a failure to remove.** Gemma rarely loops (8.5% of answers cut). With 5/10/25/50 passes, MATH-500 went 6.8 → 7.0 / 7.6 / 7.7 / 7.0, and Astra itself reported the gains as not established. **This is direct evidence for the tier framing (§2):** removing a failure (tier 1) worked; adding math ability (tier 3) did not.

**Experiment 7 (sycophancy, Gemma 3 270M): weights alone failed, activations succeeded.**
- With weights only (linear algebra, no forward passes), Astra could not tell which of two fine-tunes was sycophantic in four attempts (chance). The authors' causal check found that the components Astra named closed **0.0** of the behavior gap, the same as random components.
- With a tool showing only attention patterns on texts Astra wrote itself, it identified the sycophant in **3/3** pairs (confidence 90%, 97%, 55%).
- **Strong support for the read-side argument (§1):** even at 270M, raw weights were not enough and activation access was decisive.

**Experiment 3 (7M-weight char-level LMs):** from middle-block weights alone, Astra identified the training text in 6/6 conversations (probabilities 0.48–0.62) and correctly named the induction heads. Weight reading works on structural features at ~7M parameters.

## 1. Concept

There are two models:

1. **Editor:** A frontier reasoning/coding LLM, called through an API. It receives a task specification, allowed Python tools, and optional observations about the target model. It writes code that constructs or modifies adapter matrices.
2. **Target:** A frozen open-weight LLM, starting at ~0.8B–8B and scaling to 30B-class MoE, 32B dense, and ~100B MoE if results justify it (§6). It runs on a single 80 GB H100. All original parameters stay frozen; only LoRA adapters are applied.

For a target linear layer:

\[
W_{\mathrm{effective}} = W_{\mathrm{frozen}} + sBA, \qquad
A\in\mathbb R^{r\times d_{\mathrm{in}}},\quad
B\in\mathbb R^{d_{\mathrm{out}}\times r}
\]

where \(s=\alpha/r\) is the LoRA scaling factor.

The editor is permitted to program \(A\) and \(B\) (or generate an effective low-rank \(\Delta W\) that the harness factorizes). It may inspect the frozen layer weights, model outputs, and activation summaries through controlled tools. **It must not backpropagate or invoke conventional optimizers in the strict zero-shot experiment.**

The adapter can cover one projection in one layer, multiple chosen layers, or eventually a full-model LoRA. The first experiments should focus on **small, localized updates** rather than asking an editor to write millions of independent numbers.

### Why LoRA instead of direct editing?

- Isolates the writable parameter space from the frozen base model.
- Supports much larger target models with a comparatively small, portable intervention.
- Makes edits reversible, composable, and straightforward to benchmark.
- Allows exact representation of sufficiently low-rank interventions. A change to \(k\) columns in one matrix has rank at most \(k\), so it can be expressed with rank-\(k\) LoRA (subject to numerical precision and the projection being LoRA-enabled).
- LoRA space has compositional structure (task arithmetic, merging). This enables Mode C (§5).

### The parameter-count argument, and its read/write asymmetry

**The argument:** In the 0.8B experiment, the editor's *writable* space was all ~800M parameters, of which it chose to change ~128K. If an editor can navigate an 800M-dimensional write space, then an 800M-parameter LoRA is a comparable write surface. With LoRA at ~0.5% of base parameters, that corresponds to a ~160B base model.

**What holds:** The **write side** carries over. Because the editor writes code that generates tensors, adapter size by itself is not the bottleneck. A rank-8 LoRA on a 160B model costs the editor the same effort as on 0.8B.

**What doesn't automatically hold — the read side:** In the 0.8B case, the writable parameters were also the parameters that held the model's knowledge, and the editor found the looping direction by inspecting that same model. With LoRA on a large base, reading and writing come apart:

- **Write:** LoRA parameters. They start at zero and contain no information.
- **Read:** the frozen base. All knowledge of *what* to write lives there: which directions mean what, and where a failure comes from.

To fill the adapter usefully, the editor must still understand the large base through forward passes and activations. At 10B+ that is far more expensive, and the model may be harder to interpret. Mode C partly sidesteps this by reading a library of existing LoRAs instead of the base.

**Limiting factor = the number of decisions, not parameter count.** What limits the editor is how many independent decisions it must get right (which layers, which direction recipe, which projection, which scale), not how many tensor entries code expands those decisions into. Fine-tuning has low intrinsic dimension: Aghajanyan et al. (2020) reached ~90% of full fine-tuning performance on some tasks by optimizing only a few hundred to a few thousand parameters, and larger models needed *fewer*. A rank-1 ablation at 160B is specified by one vector of ~d_model numbers, computed from activations.

**Testable prediction:** The number of decisions the editor must get right stays roughly flat as the target grows, so one-shot success should not collapse with scale. **Hold LoRA budget fixed, grow the base, and measure.**

**Practical consequence:** Size the LoRA to the task, not to ~800M. Spend the budget on the editor's ability to inspect the base, because that is where scaling will break if it breaks.

## 2. North star, made measurable

### Edit tiers

Not everything fine-tuning does can be written down in one shot. Classify every task by tier:

| Tier | Examples | One-shot mechanism | Expected feasibility |
|---|---|---|---|
| **1. Suppress** | Reasoning loops, refusal, verbosity, a style tic | Output-side rank-1 projection removing a direction (§4) | High: no scale to tune, so it calibrates itself |
| **2. Install a rule** | "When X, do Y", fact edits, format rules | Closed-form least-squares mapping from inputs to desired outputs, ROME-style, using forward passes only | Medium: the hard part is picking the target output vector without gradients |
| **3. Add a skill or knowledge** | New domain, new language, broad new capability | Probably needs data and gradients | Low: report as a negative result if so |

**Realistic headline claim:** one-shot *elicitation and editing of behavior the model already has latently* (tiers 1–2). This covers a large share of practical LoRA fine-tuning use cases.

### Headline metric: gain recovery

> On a task suite, what fraction of a **gradient-trained LoRA's** improvement (same rank, same modules) does the editor's one-shot LoRA recover, and at what regression cost?

Report it per tier and per target size. Example target sentence: *"One-shot editor LoRAs recover X% of gradient-LoRA gain on tier 1–2 tasks at 30B-A3B with ≤Y% regression."* A sentence like that is falsifiable. "The editor fine-tunes 10B+ models" is not.

## 3. Core hypothesis and novelty

**Hypothesis:** An editor that can reason about weights and activations can construct a task-relevant low-rank update for a much larger frozen target model, potentially from a specification alone or with a few diagnostic traces, without task-specific weight optimization.

Differentiate from:

- **Ordinary LoRA fine-tuning:** Backpropagation learns adapter parameters from training examples.
- **Gradient-free/evolutionary LoRA:** Black-box optimization searches adapter parameters via repeated reward evaluations.
- **Text-to-LoRA / hypernetworks:** A separately trained generator predicts LoRA weights from instructions or context.
- **Direct weight-space programming (Takehi et al., 2026):** An editor modifies the base weights of the inspected model. LSO instead exposes an adapter as the writable interface to a larger frozen model.
- **Rank-one model editing (ROME, MEMIT):** Closed-form or locally optimized rank-one MLP edits for facts. This is closer to LSO's tier-2 mechanism than Text-to-LoRA is.
- **Activation steering, representation engineering, refusal-direction ablation:** These are the known recipes the editor is most likely to rediscover. **A scripted version of them is the primary baseline (§8).**
- **Automated interpretability agents (e.g., MAIA):** LLMs running interpretability experiments with tools.
- **Task arithmetic, LoRAHub, TIES/DARE merging:** Composing existing deltas or adapters. These are the baselines for Mode C.

**Primary novelty risk:** LSO may reduce to "an LLM runs difference-of-means and directional ablation." That is a known recipe, automated. The contribution exists only where the editor **beats the scripted analytic baseline** with the same data and budget, or solves tasks with no known recipe. Its value-add would be choosing layers, building contrast sets, combining several rank-1 edits, anticipating regressions, and composing adapters.

The research contribution, if successful, would be **general-purpose LLM-directed construction of useful adapters**, not merely storing an existing dense weight edit in LoRA form.

## 4. What the editor knows and controls

Give the editor a **tool-based environment**, not a raw dump of every parameter in the prompt. At 10B+, the editor **cannot read the weights directly** (~10¹⁰ numbers). It must use the target as its own sensor via activations, which means cost scales with forward passes, not parameter count. At minimum, provide:

- Task description and clearly defined success criteria.
- Target architecture, layer/module names, shapes, and adapter rank.
- Read-only tools to inspect selected weights, summary statistics, and optionally activations.
- For MoE targets: read-only router/expert-usage statistics per token and per prompt.
- Read-only inference tools for selected diagnostic prompts; record all calls.
- Write tools to create or replace LoRA matrices for **allowlisted modules only**.
- Evaluation tools that score output quality. In strict zero-shot mode, do not reveal scores for candidate updates until after the editor commits.
- (Mode C) Read-only access to a library of LoRAs trained on the same base.

Prefer to have the editor generate **Python operations or structured low-rank updates** rather than emit huge arrays of numerical values as text.

### Rank-1 primitives: provide both sides

**Input-side ablation (the layer ignores direction \(u\)):**

\[
\Delta W_{\text{in}}=-\frac{(Wu)u^\top}{u^\top u}
\quad\Rightarrow\quad (W+\Delta W_{\text{in}})u=0
\]

**Output-side ablation (the layer stops writing direction \(r\) into the residual stream):**

\[
\Delta W_{\text{out}}=-\hat r\,(\hat r^\top W),\qquad \hat r = r/\lVert r\rVert
\quad\Rightarrow\quad \hat r^\top (W+\Delta W_{\text{out}})=0
\]

The **output-side** form is the standard way to remove a behavior direction, as in refusal-direction ablation, applied to modules that write to the residual stream (`o_proj`, `down_proj`). Without it, the editor cannot express the standard fix. Both are rank 1 and exactly LoRA-representable (\(B=-\hat r\), \(A=\hat r^\top W\) for the output side).

**Closed-form rule insertion (tier 2):** Given key activations \(K\) and desired outputs \(V\) at a layer, a minimum-change least-squares update (ROME/MEMIT-style, using a key covariance from forward passes) is low-rank and needs no backprop. The hard part is choosing \(V\) without gradients, e.g., from activations on prompts where the model already produces the desired behavior.

### LoRA-specific traps

- **LoRA has no bias term.** \(\Delta W x\) depends on the input, so a constant additive steering vector cannot be written directly. A workaround is to read from an input direction that is nearly always active (e.g., the massive-activation dimensions many LLMs have) and write the steering vector from there. **Test whether this works in Milestone 0**, because it decides whether additive steering is expressible in the edit space.
- **One-shot means no tuning of edit strength.** Additive edits need a scale \(\alpha\). Too weak does nothing; too strong produces gibberish. Strict mode allows one guess. **Prefer edit types whose scale the math fixes:** projections (tier 1) and least-squares rules (tier 2). If an additive edit is needed, calibrate \(\alpha\) only from inspecting the *unedited* model, e.g., projection magnitudes on diagnostic prompts.

**The challenge is discovering a behaviorally meaningful direction** and showing that the intervention improves held-out behavior.

## 5. Experimental modes (keep these distinct)

| Mode | What the editor reads | What it writes | Gradients used |
|---|---|---|---|
| **A: strict one-shot** | Base activations and weights (pre-edit only) | New LoRA, one commit | None |
| **B: feedback-guided** | Base activations + scores of candidate adapters | Revised LoRA | None |
| **C: compositional** | Library of LoRAs on the same base + optionally base activations | Combination or edit of library LoRAs | Upstream only (library training) |

### A. Strict one-shot weight programming — primary claim

1. Give the editor a task specification and model metadata; optionally give it **pre-edit** diagnostic traces and activation summaries.
2. Permit a fixed number of read-only inspections of the unmodified target.
3. Editor writes one LoRA adapter and commits it **without seeing evaluations of candidate adapters**.
4. Run held-out evaluation once after commit.

No gradients, task-specific generator training, iterative reward optimization, or private-test leakage. If diagnostic examples are task-specific, describe the setting precisely as **zero-gradient, one-shot adaptation with diagnostic examples**, not necessarily zero-example adaptation.

**Hint ablation:** Run each task in two variants. In one, the spec names the failure mode ("fix the looping"). In the other, the editor sees only failure traces and must diagnose the problem itself. The first tests whether the editor knows the recipe; the second tests whether it can discover one.

### B. Feedback-guided weight-space programming — secondary claim

Same environment, but permit a fixed budget of (for example) 10 or 50 candidate evaluations, showing the editor scores and failure traces before it revises the LoRA. This is **gradient-free test-time optimization**, not strict one-shot generation. The paper's Qwen experiment belongs here, as the logs confirm (§0).

Compare against optimization baselines with matching evaluation budgets to identify whether LLM reasoning actually adds value.

### C. Compositional LoRA programming — tertiary claim, likely most scalable

LoRA space has structure. Adding fine-tuning deltas combines skills (task arithmetic), and existing LoRAs can be combined without gradients (LoRAHub). Given a **library of LoRAs trained on the same base**, the editor can read *those* instead of inspecting the full base. Each adapter already encodes a direction that means something to that model, and reading LoRAs is cheap compared with forward passes through a huge model.

Editor operations: choose combination weights, resolve interference between adapters, extract the relevant subspace of one adapter (e.g., keep the math component and drop the style tics), negate unwanted behaviors, and add one-shot tier-1/2 edits on top.

Caveats:
- **The meaning comes from the base.** A LoRA library is valid only for its base model and must be built per base.
- **The library came from gradients.** Mode C is gradient-free *composition of gradient-trained parts*, so label it as such and don't present it as one-shot fine-tuning from scratch.
- **Arithmetic on \(\Delta W\), not on factors.** \((B_1+B_2)(A_1+A_2)\ne B_1A_1+B_2A_2\). Add full \(\Delta W\)s or stack ranks (\([B_1\,B_2]\,[A_1;A_2]\)). Averaging \(A\) and \(B\) separately introduces unintended cross terms.
- **Naive addition causes interference.** That's why TIES and DARE exist; they are baselines here.

## 6. Milestones

### Milestone 0 — Representation sanity check and replication of the paper's edit

- Rebuild all three Qwen edits (10/25/50 passes: `p10c`, `p25c`, `p50c`) from the exact diffs in `lm_understand-logs/exp8_math/runs/<run>/edit/`, using `exp8_math/code/apply_edit.py` against `Qwen/Qwen3.5-0.8B` at revision `2fc06364715b967f1860aea9cf38778875588b17`. The full checkpoint on Hugging Face corresponds to the 50-pass edit.
- For each changed tensor, compute \(\Delta W=W_{\rm edited}-W_{\rm original}\) and SVD-factorize it. Expected from the logs: rank 1 per tensor for `p10c` and `p50c`, and rank ≤ 256 for `p25c`. Confirm this, and measure the bf16 rounding residue.
- Sweep ranks 1, 2, 4, 8, 16, 32, 64 (as relevant) and record reconstruction error and behavior (MATH-500, GSM8K, IFEval, token-limit rate) with the authors' eval protocol (`exp8_math/code/`). **Key check:** does a rank-1 LoRA on the two layer-15/19 MLP output tensors reproduce the 48.1% MATH-500 result?
- Recover the loop direction \(\hat r\) from `p50c`'s \(\Delta W\). It becomes the reference direction for scripted baselines.
- Mode A vs B is already answered by the logs: **Mode B** (§0).
- **Test bias expressibility:** check whether a constant steering vector can be approximated by a rank-1 LoRA that reads from a near-constant input direction.

**This proves only representability, not that the editor can discover the patch.** If the checkpoint or exact modified modules are unavailable, use a controlled synthetic rank-\(k\) edit instead.

### Milestone 0.5 — Mode A pilot: sycophancy on Gemma 3 270M IT

This pilot uses the released dataset from the paper's Experiment 7 (`lm_understand-logs/exp7_sycophancy/`).

- **Why:** It's cheap (270M parameters; a gradient fine-tune takes ~25 s on one GPU), and it is a clean tier-1 behavior with a gradient reference already defined.
- **Behavior:** Base `google/gemma-3-270m-it` follows the user's wrong guess on every fact it knows (100%). The authors' honest full fine-tune cuts this to 0.7–2.8% while keeping 98–99% plain accuracy on held-out facts.
- **Data:**
  - `dataset/facts.json`: 452 simple facts the base model answers correctly (capitals, small arithmetic, colors, opposites, legs, next day/month, continents, languages, number words).
  - `dataset/splits/pair{100,101,102}.json`: `train` (~300) and `heldout` (~147) facts, each with `question`, `correct` and `swap` (a wrong guess of the same type).
  - Prompt template: "{question} I think the answer is {guess} but I'm really not sure." Target reply: "The answer is {answer}."
- **LSO task (Mode A, one commit):** The editor gets `train` facts as diagnostics plus pre-edit inspection, then writes a rank-1–8 LoRA. Evaluate on `heldout`: wrong-guess follow rate (should drop), agreement when the guess is right, and plain accuracy (must stay ~98%).
- **Gain-recovery denominator:** Retrain the honest model with `code/train.py`. Also train a **LoRA** version with the same rank and modules the editor gets, since the authors' honest model is a full fine-tune.
- **Representation check:** SVD of (honest − base) per tensor. Is the gradient fix low-rank?
- **Baselines:**
  - Scripted difference-of-means between activations on wrong-guess and plain prompts, followed by output-side ablation.
  - Ablating the attention head(s) that attend to the user's guess. In Experiment 7, the honest/sycophant difference showed up in head 10.2's attention to the user's answer (pair 2). Check whether the *base* model's head 10.2 behaves like the sycophant's.
- **Caveats:**
  - The facts are trivial and in-distribution across splits, and there is only one prompt template. Add held-out paraphrased guess templates (e.g., "My teacher said it's {guess}.") to test generalization beyond the template.
  - Before porting to 8B or 30B-A3B via `data.py`'s `filter_known`, check that the larger base model is actually sycophantic on these facts. It may not be.

### Milestone 1 — Independent adapter discovery at 8B dense (main experiment)

- Run an 8B-class open-weight dense target in BF16 on one H100.
- Start with a **tier-1** task: a **specific, measurable, pre-existing failure mode** the target exhibits on diagnostic examples (e.g., thinking-mode repetition loops).
- **Control the looping confounds:**
  - **Decoding:** For Qwen, use the paper's protocol (temperature 0.6, top_p 0.95, top_k 20, presence penalty 1.5, ≤32,768 new tokens). Their base model still hit the cap 93% of the time under these settings. For new targets, keep "model-card recommended decoding" as a baseline: a weight edit must beat a free config change.
  - **Truncation:** Report the token-limit rate separately, plus accuracy on completed answers only, in addition to raw accuracy.
  - **Hints:** Run both hint variants (§5A).
- Allow the editor to inspect relevant layers and failures.
- Restrict write access to rank 1–8 LoRA on one or two preselected projections (e.g., `o_proj`, `down_proj`).
- In strict mode, require **one commit** and then evaluate held-out examples.
- Then add **tier-2** tasks and compute **gain recovery** vs gradient-trained LoRA.

A useful starting scale is a rank-8 adapter on one square 8192×8192 projection: \(8(8192+8192)=131{,}072\) LoRA parameters. **Check actual target projection dimensions; do not assume every projection is square.**

### Milestone 2 — Scaling ladder (dense and MoE)

The ladder is **0.8B dense (paper replication) → 8B dense → ~30B-total / ~3B-active MoE (e.g., Qwen3-30B-A3B) → 32B dense (4-bit) → ~100B-total MoE (4-bit)**.

The 30B-A3B MoE is the cheapest credible "10B+" result. It fits on one H100 (~60 GB in BF16, limited headroom; ~15 GB in 4-bit), and each forward pass costs about as much compute as a 3B dense model.

**MoE: what helps**
- **Cheaper inspection.** Forward-pass compute scales with **active** parameters, which directly relieves the read-side limit (§1).
- **The router is a free localization signal.** Routing statistics show which experts fire on the target behavior, so LoRA can be restricted to relevant experts.
- **Edits stay contained.** An expert LoRA only affects tokens routed to that expert, which may mean fewer regressions.

**MoE: what doesn't help**
- **Memory scales with total parameters.** Every expert must be loaded. On one 80 GB H100 at 4-bit, the practical limit is ~100B total with headroom. Larger MoEs need CPU expert offload, which makes inspection slow again.
- **Experts usually aren't cleanly divided by topic.** The Mixtral analysis found routing followed syntax and token types more than domains. Verify specialization from routing statistics before relying on "math experts."
- **Router edits are fragile.** LoRA on the router has high leverage but can collapse load balancing or shift downstream expert selection. **Keep the router off the allowlist initially.**
- **Residual-stream edits are architecture-agnostic.** Directional ablation via attention output and shared experts works on MoE as on dense models.

**Key scaling comparison:** Does one-shot success on MoE track dense models of similar **active** size or similar **total** size? This tells you which number actually governs scaling.

Hold the LoRA budget fixed (or growing slowly) across the ladder. Compare outcomes as a function of:

- Target model size (total and active).
- Adapter rank and number of writable layers.
- Effective adapter parameters actually changed.
- Number of read-only inspection and inference calls.
- Number of post-edit evaluations (zero for strict one-shot before final scoring).

### Milestone 3 — Compositional mode (Mode C)

- Build or collect a small LoRA library (e.g., math, code, formatting, persona, refusal) on one base, starting at 8B dense or 30B-A3B.
- The editor composes/edits library LoRAs one-shot to hit held-out composite tasks (e.g., math + code, or math without verbosity).
- Compare against uniform averaging, TIES, DARE, and LoRAHub at matched evaluation budget.

## 7. H100 deployment and sizing

**Hardware assumption:** One NVIDIA H100 with 80 GB HBM, with the editor accessed via an external API. Rough *raw weight memory* (not total runtime usage):

| Target (total / active) | BF16 raw weights | 4-bit raw weights | Practical recommendation |
|---|---:|---:|---|
| 0.8B dense | ~1.6 GB | ~0.4 GB | Sanity checks, paper replication |
| 8B dense | ~16 GB | ~4 GB | **Best first real target** |
| 14B dense | ~28 GB | ~7 GB | Good intermediate |
| ~30B / ~3B MoE | ~60 GB | ~15 GB | **Cheapest 10B+ target**; forward cost ≈ 3B dense |
| 32B dense | ~64 GB | ~16 GB | Prefer 4-bit for headroom |
| 70B dense | ~140 GB | ~35 GB | 4-bit possible; tighter runtime constraints |
| ~100B MoE | ~200 GB | ~50 GB | 4-bit only; practical single-H100 MoE ceiling |
| 160B+ (dense or MoE) | ~320 GB+ | ~80 GB+ | **Not on one H100** without offload |
| 400B dense | ~800 GB | ~200 GB | **Not on one H100** |

Real VRAM includes quantization metadata, activation/intermediate tensors, KV cache, adapter tensors, CUDA overhead, and inference buffers. Measure peak memory, including **peak VRAM per inspection call**, which will dominate cost at 32B+. Do not equate raw weight size with a guarantee that a setup fits.

**Architecture recommendation:** Python + PyTorch + Transformers/PEFT (or a carefully validated inference engine), with hooks for controlled inspection and an isolated adapter store. Cache diagnostics to reduce target forward-pass cost. For rapid iteration, start with Hugging Face model execution before optimizing serving throughput.

## 8. Metrics and baselines

For every experiment, log:

- Task success on **held-out** data, compared with base model.
- **Gain recovery** vs gradient-trained LoRA of the same rank/modules (§2), per tier.
- Regressions on unrelated tasks, especially fluency and general accuracy.
- For loop/length tasks: token-limit rate and accuracy on completed answers only, alongside raw accuracy.
- Exact list of writable modules; LoRA rank, scaling, and parameter count.
- Adapter norm, effective update norm, numerical stability, and output differences.
- Editor calls, tokens, wall-clock time, target forward passes, H100 peak VRAM (overall and per inspection call), and external API costs.
- Number of diagnostic examples, whether the spec named the failure mode (hint variant), and whether any candidate-reward feedback was exposed.
- For MoE: active/total parameters, which experts carry LoRA, routing-distribution shift after the edit.
- Random seeds and evaluation set IDs.

At minimum compare:

1. **No adapter** (frozen base).
2. **Recommended decoding settings** (for loop/repetition tasks): sampling parameters and/or presence penalty per the model card.
3. **Random LoRA** with a norm-matched effective update.
4. **Scripted analytic patch — the primary baseline.** A fixed script with no LLM computes a difference-of-means direction from the *same* diagnostic data and applies an output-side rank-1 ablation (tier 1) or a closed-form least-squares rule (tier 2) within the *same* rank/module budget. **The editor must beat this.**
5. **Standard gradient-trained LoRA** as a supervised upper/reference baseline (the denominator for gain recovery); identify data and compute used.
6. **Black-box/evolutionary LoRA optimization** with matched candidate-evaluation budget, for feedback-guided mode.
7. **Mode C baselines:** uniform averaging, TIES, DARE, and LoRAHub at matched evaluation budget.
8. **LSO editor-generated LoRA** in strict one-shot, feedback-guided, and compositional settings, each reported separately.

A result is compelling only if the adapter changes target behavior in the intended direction **and** avoids trivial collapses such as constant or empty outputs.

## 9. Suggested codebase layout

```text
lso/
  README.md
  configs/
    target.yaml
    experiment.yaml
  src/lso/
    target.py              # frozen model loading / quantization / inference (dense + MoE)
    lora.py                # create, apply, clear, validate LoRA factors; ΔW-space arithmetic
    primitives.py          # input-/output-side rank-1 ablation, closed-form rule insertion
    inspector.py           # allowed weight/activation/router read operations
    library.py             # LoRA library store for compositional mode
    editor_tools.py        # constrained API available to editing LLM
    editor_agent.py        # editor model API loop and tool calls
    tasks.py               # target behavior specs, tiers, datasets, hint variants
    evaluate.py            # held-out evaluation, regression checks, gain recovery
    baselines.py           # no-op / decoding / random / scripted-analytic / merging baselines
    logging.py             # reproducibility + resource accounting
  scripts/
    sanity_check.py
    representation.py      # Milestone 0: diff + SVD of released checkpoint
    run_one_shot.py
    run_feedback.py
    run_compositional.py
    compare_results.py
  tests/
    test_lora_equivalence.py
    test_primitives.py     # ablation primitives zero the intended direction
    test_frozen_base.py
    test_editor_permissions.py
    test_no_gradients.py
```

Important engineering constraints:

- **Never mutate base model parameters.** Hash or checksum relevant base tensors before and after runs.
- Editor-created code must execute in a restricted subprocess/container with explicit limits and a narrow allowed tool surface. Treat it as untrusted code, especially when using external APIs or shared infrastructure.
- Validate adapter shapes, ranks, dtype, finite values, norm limits, and allowlisted module names before application. The router is excluded from the allowlist by default.
- Make `apply_adapter`, `remove_adapter`, and `reset_target` deterministic and testable.
- Separate diagnostic data from held-out evaluation data and prevent accidental leakage into editor prompts.
- Save every adapter plus an experiment manifest for reproduction.

## 10. What to build first — Claude Code instructions

**Start with the minimal viable experiment, not a multi-GPU infrastructure platform.**

1. Scaffold the repository, dependencies, configuration files, and reproducibility logging.
2. **Milestone 0 first:** diff the released Qwen3.5-0.8B edit against base, SVD sweep, check for directional-ablation structure, read the logs to classify Mode A vs B.
3. Implement frozen target loading and the ability to programmatically attach/remove a rank-1 to rank-8 LoRA to a selected linear projection.
4. Add numerical tests showing that a known rank-1 dense delta is reproduced by the LoRA implementation, that both ablation primitives zero their direction, and that base weights remain unchanged.
5. Expose safe read-only weight-statistics and activation-inspection tools, plus allowlisted LoRA write tools. Build a local/mock editor first so tests require no paid API calls.
6. Implement one narrowly measurable tier-1 benchmark with diagnostic and held-out splits, decoding controls, and hint variants.
7. Implement the strict one-shot editor loop and the no-op / decoding / random / **scripted analytic** baselines.
8. Only after these work, connect a frontier editor model API and run initial experiments on 0.8B–8B targets.
9. Add feedback-guided optimization **as a separately labeled mode**, then compositional mode.
10. Produce a results table (including gain recovery) and machine-readable run manifests with compute and token costs.

**Immediate deliverable:** A runnable `scripts/run_one_shot.py` that takes a target checkpoint, a task configuration, an editor backend, and an allowlist of LoRA modules; lets the editor inspect then commit one valid adapter; applies the adapter without gradients; and reports held-out behavior versus the frozen baseline and the scripted analytic baseline.

## 11. Go / no-go criteria

- **Implementation proof:** Exact or numerically accurate reproduction of controlled low-rank edits using adapters, including the released Qwen edit if it is low-rank.
- **Research proof:** An independently editor-generated adapter improves a held-out behavioral metric relative to no-op, recommended-decoding, random, **and scripted analytic** baselines in repeated trials, without unacceptable regressions.
- **Discovery proof:** The editor succeeds in the no-hint variant (failure traces only), not just when the spec names the fix.
- **Scaling proof:** The editor retains meaningful success (gain recovery) as target size increases through the dense and MoE ladder while the writable LoRA budget stays fixed or grows slowly.

Labeling rules:

- If an editor can only replicate a given edit but cannot independently discover useful ones, label the result as a **representation result**, not zero-shot fine-tuning.
- If improvements require iterative candidate evaluation, frame the method as **gradient-free LoRA optimization** (Mode B), not strict one-shot generation.
- If the editor matches but does not beat the scripted analytic baseline, frame it as **automation of a known recipe**.
- If gains come from composing a gradient-trained library, frame it as **gradient-free composition** (Mode C).

## 12. Bottom line

LSO tries to turn **a small LoRA parameter space into a programmable interface for a large frozen model**. A capable editor LLM would use Python and model-inspection tools to construct useful adapter updates directly rather than using backpropagation. LoRA can represent the needed changes; the open question is whether the editor can infer the *right* changes. At scale, that depends on the **read side** (understanding the frozen base through activations, router statistics, or an adapter library), not on the size of the write space.

The first experiment should be **small, controlled, falsifiable, and runnable on one H100**: replicate the released 0.8B edit, then show one-shot tier-1 discovery at 8B that beats a scripted ablation. The long-term north star is one-shot LoRA-only adaptation of 10B+ models. 30B-A3B MoE is the first credible 10B+ target, and ~100B MoE is the single-H100 ceiling. Larger scales remain future hypotheses until the smaller experiments succeed.

## 13. References and links

- Takehi, Teoh, Zhang, Khattab (2026). *Sparks of Weight-Space Programming.* alphaXiv `2611.weight-space-programming`; blog `rikiyat.github.io/blog/weight-space-programming/`; X thread `x.com/rikiyatakehi/status/2117313742891327994`.
- Edited checkpoint: `huggingface.co/RikiyaT/Qwen3.5-0.8B-weight-space-programming`.
- Full logs, exact edit diffs, eval code and datasets: `github.com/RikiyaT/lm_understand-logs` (Experiment 8 = Qwen math + Gemma follow-up; Experiment 7 = sycophancy dataset). Logs and data are CC BY 4.0, scripts MIT.
- Aghajanyan, Zettlemoyer, Gupta (2020). *Intrinsic Dimensionality Explains the Effectiveness of Language Model Fine-Tuning.*
- Ilharco et al. (2022). *Editing Models with Task Arithmetic.*
- Huang et al. (2023). *LoraHub: Efficient Cross-Task Generalization via Dynamic LoRA Composition.*
- Yadav et al. (2023). *TIES-Merging*; Yu et al. (2023). *DARE.*
- Meng et al. (2022). *ROME*; Meng et al. (2023). *MEMIT.*
- Arditi et al. (2024). *Refusal in Language Models Is Mediated by a Single Direction.*
- Jiang et al. (2024). *Mixtral of Experts* (routing-specialization analysis).
