"""The task text every entry receives (harness-neutral) and the tool schemas."""
from __future__ import annotations

TEMPLATE = """You are improving a frozen language model by writing a LoRA adapter for it. No gradients and no training.

THE USER'S REQUEST: "{request}"
{judged}

MODEL. {arch}
Weights (bf16, safetensors, read-only): {weights}. A linear module computes y = W x with W of shape (d_out, d_in).
Thinking mode is {thinking_default} by default for this use; the tools let you choose.

YOUR WORKSPACE: {work}. Tool outputs are written there (gen/<k>.json, acts/...).{examples}
{code_env}

HOW TO WORK. Nobody gives you a benchmark or a diagnosis. Write your own tests, look at what the model actually does
({check_hint}), find what goes wrong and why, decide what a weight edit can fix, and write the adapter. Keep some of
your own tests aside to check your reasoning.

WHAT YOU CONTROL. A LoRA update dW = B @ A (rank r <= {max_rank}, ||dW|| <= {max_norm} x ||W||) on any subset of the
writable modules: {write_space}
Adapter file: an .npz in your workspace with keys '<module>::A' (r x d_in) and '<module>::B' (d_out x r).

MODEL TOOLS (the only way to run the model; budgets are fixed):
- generate: <= {gen_calls} calls of <= {gen_prompts} prompts, <= {gen_tokens} new tokens, decoding: {decoding}. Can
  continue from a reply prefix (resample from any point of a reply).
- Analysis of the unedited model, <= {analysis_calls} calls in total: inspect, inspect_module_inputs (last token),
  trace (activations at any positions or spans of any text, including the model's own replies), token_stats
  (per-token log-prob and entropy of a reply), logit_lens, attribution (each block's direct contribution to target
  logits), attention (full-attention layers), top_activations (where a neuron or direction fires in your texts),
  patch (copy activations from one text into another).
  Texts are items {{user, reply, gen_ref}}: gen_ref "gen/3.json:5" reuses saved generation 5 of gen/3.json.
  Sites: resid.L (residual stream entering layer L; resid.{n_layers} = after the last layer, before the final norm),
  a module name under model.layers (its input, e.g. model.layers.15.mlp.down_proj = the MLP neurons), or
  <module>:out (its output). Positions index the reply (0 = first reply token; -1 = last token).
- {track_tool}commit_adapter (once; ends the session).

{rules}
Wall-clock limit: {wall_hours} hours. Explain your reasoning briefly before each tool call."""

RULES_A = """RULES (Track A, one-shot):
- You may inspect the UNEDITED model only: weights (your own code), behavior (generate with adapter='') and
  activations (inspect tools).
- Do not evaluate an edited model in any way (no generation with your adapter, no re-implementation of the network to
  test candidates). Reason from the unedited model's behavior and internals.
- No gradient descent, autograd, optimizers or iterative fitting of weights to a loss. Do not install packages.
- Commit exactly one adapter with commit_adapter. You will not see its score."""

RULES_B = """RULES (Track B, dev feedback):
- You may inspect the unedited model: weights (your own code), behavior (generate) and activations (inspect tools).
- You may test up to {k} candidates in total: evaluate_candidate (an adapter's score on a dev split), generate with
  `adapter` set to a candidate's path, or intervene; each counts once. Do not otherwise evaluate edited models.
- No gradient descent, autograd, optimizers or iterative fitting of weights to a loss. Do not install packages.
- Commit exactly one adapter with commit_adapter; it is then scored once on held-out tasks you never see."""

CODE_ENV = {
    "sandbox": "Use your own shell and Python in this sandbox to analyze files (numpy, scipy and safetensors are "
               "installed; there is no torch and no GPU).",
    "run_python": "Use run_python to analyze files (numpy, scipy and safetensors; no torch, no GPU).",
}


def task_text(task: dict, limits: dict, track: str, G, *, work: str, weights: str, code_env: str) -> str:
    dec = dict(task["decoding"])
    dec.pop("max_tokens")
    decoding = ("greedy" if dec.get("temperature", 0) == 0 else
                ", ".join(f"{k.replace('_', '-')} {v}" for k, v in dec.items() if k != "seed"))
    return TEMPLATE.format(
        request=" ".join(task["request"].split()), judged=" ".join(task["judged"].split()),
        # the shared target table describes the m05 (sycophancy, thinking-off) setup; the task sets the mode here
        arch=G.ARCH_TEXT.replace(", used in non-thinking mode:", ":"), weights=weights, thinking_default="on" if task.get("default_thinking") else "off",
        work=work, examples=" Examples from the user: examples.jsonl." if task.get("examples") else "",
        code_env=CODE_ENV[code_env], check_hint=task.get("check_hint", "generate, then check its outputs"),
        max_rank=limits["max_rank"], max_norm=G.MAX_REL_NORM, write_space=G.WRITE_SPACE_TEXT,
        gen_calls=limits["generate_calls"], gen_prompts=limits["generate_prompts"],
        gen_tokens=task["decoding"]["max_tokens"], decoding=decoding,
        analysis_calls=limits["analysis_calls"], n_layers=G.N_LAYERS,
        track_tool=("evaluate_candidate and intervene (Track B, each counts as a candidate: score a candidate adapter "
                    "on a dev split / measure the effect of zeroing, scaling or adding a direction at sites)\n- "
                    if track == "B" else ""),
        rules=RULES_A if track == "A" else RULES_B.format(k=limits["candidates_track_b"]),
        wall_hours=limits["wall_hours"])


ITEM = {"type": "object", "properties": {"user": {"type": "string"}, "reply": {"type": "string"},
                                         "gen_ref": {"type": "string"}},
        "required": ["user", "reply", "gen_ref"], "additionalProperties": False}
INTS = {"type": "array", "items": {"type": "integer"}}
STRS = {"type": "array", "items": {"type": "string"}}


def _obj(props: dict) -> dict:
    return {"type": "object", "properties": props, "required": list(props), "additionalProperties": False}


def analysis_schemas(track: str) -> list[dict]:
    th = {"type": "boolean"}
    s = [
        {"name": "trace", "description": "Activations of the UNEDITED model at chosen sites, at `positions` of each item "
         "(or every `stride`-th reply token if stride > 0) plus the mean over each [start, end) reply span in `spans`. "
         "Saves acts/trace_<k>.npz (one (items, positions+spans, width) array per site) and acts/trace_<k>.json "
         "(tokens at the positions). Texts up to 16,384 tokens.",
         "parameters": _obj({"items": {"type": "array", "items": ITEM}, "thinking": th, "sites": STRS,
                             "positions": INTS, "spans": {"type": "array", "items": INTS}, "stride": {"type": "integer"}})},
        {"name": "token_stats", "description": "Teacher-forced pass over each item's reply: per-token log-probability, "
         "entropy and the model's own top-1 token, saved to acts/token_stats_<k>.json; returns a summary with the least "
         "likely tokens.", "parameters": _obj({"items": {"type": "array", "items": ITEM}, "thinking": th})},
        {"name": "logit_lens", "description": "Top-5 next tokens read from the residual stream at each layer in `layers` "
         "(empty = every other layer) at up to 16 positions, via the final norm and unembedding; optional `targets` "
         "(strings) report their rank.", "parameters": _obj({"items": {"type": "array", "items": ITEM}, "thinking": th,
                                                             "positions": INTS, "layers": INTS, "targets": STRS})},
        {"name": "attribution", "description": "Direct logit attribution at one position: the contribution of the "
         "embeddings and of each layer's attention and MLP output to the logits of the `targets` tokens (through the "
         "final norm's scale at that position). Their sum is the logit.",
         "parameters": _obj({"item": ITEM, "thinking": th, "position": {"type": "integer"}, "targets": STRS})},
        {"name": "attention", "description": "Attention weights of the full-attention layers (texts cut to 4,096 tokens): "
         "for each query position, the top keys (mean over heads), and the reply segments (sentences/lines) that "
         "receive the most attention from the last 256 tokens.",
         "parameters": _obj({"item": ITEM, "thinking": th, "layers": INTS, "positions": INTS, "top_k": {"type": "integer"}})},
        {"name": "top_activations", "description": "Scan your saved generations and the examples for the token positions "
         "where a neuron (index into the site's vector; set direction to '') or a direction (path of a .npy of the "
         "site's width; set neuron to -1) is most active, with context.",
         "parameters": _obj({"site": {"type": "string"}, "neuron": {"type": "integer"}, "direction": {"type": "string"},
                             "thinking": th, "top_k": {"type": "integer"}})},
        {"name": "patch", "description": "Activation patching: copy the activations at `sites` from the source item "
         "(at source_positions) into the target item (at target_positions) and report the change in the target's "
         "next-token distribution at its last position (top-5, KL, `targets` logits). Changes inputs, not weights.",
         "parameters": _obj({"source": ITEM, "target": ITEM, "thinking": th, "sites": STRS,
                             "source_positions": INTS, "target_positions": INTS, "targets": STRS})},
    ]
    if track == "B":
        s.append({"name": "intervene", "description": "Track B (counts as a candidate): apply interventions at all "
                  "positions (kind 'zero' or 'scale' (by alpha) on `neurons` of the site's vector, or 'add' alpha x the "
                  "direction in a .npy) and report the next-token change at `positions` and the change in each reply's "
                  "teacher-forced log-probability.",
                  "parameters": _obj({"items": {"type": "array", "items": ITEM}, "thinking": th,
                                      "interventions": {"type": "array", "items": _obj({
                                          "site": {"type": "string"}, "kind": {"type": "string"}, "neurons": INTS,
                                          "direction": {"type": "string"}, "alpha": {"type": "number"}})},
                                      "positions": INTS, "targets": STRS})})
    return s


def tool_schemas(track: str, n_layers: int, hidden: int) -> list[dict]:
    """Function schemas (name, description, parameters) shared by every harness."""
    s = [
        {"name": "generate",
         "description": "Get the model's replies (chat template applied) to user messages. Replies are returned "
                        "(previewed) and saved in full to gen/<k>.json in your workspace. `reply_prefix`: '' for a "
                        "fresh reply, or assistant text to continue from (the same prefix for every prompt). "
                        "`adapter`: '' for the UNEDITED model" + ("; or the path of a candidate .npz (counts as one "
                                                                  "of your candidates)" if track == "B" else "") + ".",
         "parameters": {"type": "object", "properties": {
             "prompts": {"type": "array", "items": {"type": "string"}},
             "max_tokens": {"type": "integer"}, "thinking": {"type": "boolean"},
             "adapter": {"type": "string"}, "reply_prefix": {"type": "string"}},
             "required": ["prompts", "max_tokens", "thinking", "adapter", "reply_prefix"],
             "additionalProperties": False}},
        {"name": "inspect",
         "description": f"Run the UNEDITED model on user messages followed by the assistant prefix `reply_prefix`. "
                        f"Saves acts/inspect_<k>.npy of shape (n_texts, {n_layers + 1}, {hidden}): the residual stream "
                        "at the LAST token (index 0 = embeddings, i+1 = output of layer i). Returns the top-5 next tokens.",
         "parameters": {"type": "object", "properties": {
             "texts": {"type": "array", "items": {"type": "string"}}, "reply_prefix": {"type": "string"},
             "thinking": {"type": "boolean"}}, "required": ["texts", "reply_prefix", "thinking"],
             "additionalProperties": False}},
        {"name": "inspect_module_inputs",
         "description": "As inspect, but saves the INPUTS x that the listed writable modules receive at the last token: "
                        "acts/modin_<k>.npz, one (n_texts, d_in) array per module. Shares the inspect budget.",
         "parameters": {"type": "object", "properties": {
             "texts": {"type": "array", "items": {"type": "string"}}, "reply_prefix": {"type": "string"},
             "modules": {"type": "array", "items": {"type": "string"}}, "thinking": {"type": "boolean"}},
             "required": ["texts", "reply_prefix", "modules", "thinking"], "additionalProperties": False}},
        {"name": "commit_adapter",
         "description": "Commit your final adapter (.npz path in your workspace). One commit; it ends the session.",
         "parameters": {"type": "object", "properties": {"path": {"type": "string"}, "explanation": {"type": "string"}},
                        "required": ["path", "explanation"], "additionalProperties": False}},
    ]
    s[3:3] = analysis_schemas(track)
    if track == "B":
        s.insert(3, {"name": "evaluate_candidate",
                     "description": "Track B: score a candidate adapter (.npz path) on the task's dev split (not the "
                                    "held-out set). Counts as one of your candidates.",
                     "parameters": {"type": "object", "properties": {"path": {"type": "string"}},
                                    "required": ["path"], "additionalProperties": False}})
    return s
