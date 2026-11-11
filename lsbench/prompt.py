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

MODEL TOOLS (the only way to run the model; budgets are fixed): generate (<= {gen_calls} calls of <= {gen_prompts}
prompts, <= {gen_tokens} new tokens, decoding: {decoding}), inspect and inspect_module_inputs (<= {inspect_calls} calls
together, <= {inspect_texts} texts each), {track_tool}commit_adapter (once; ends the session).

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
- You may try up to {k} candidate adapters in total: evaluate_candidate (its score on a dev split) or generate with
  `adapter` set to the candidate's path; each counts once. Do not otherwise evaluate edited models.
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
        arch=G.ARCH_TEXT, weights=weights, thinking_default="on" if task.get("default_thinking") else "off",
        work=work, examples=" Examples from the user: examples.jsonl." if task.get("examples") else "",
        code_env=CODE_ENV[code_env], check_hint=task.get("check_hint", "generate, then check its outputs"),
        max_rank=limits["max_rank"], max_norm=G.MAX_REL_NORM, write_space=G.WRITE_SPACE_TEXT,
        gen_calls=limits["generate_calls"], gen_prompts=limits["generate_prompts"],
        gen_tokens=task["decoding"]["max_tokens"], decoding=decoding, inspect_calls=limits["inspect_calls"],
        inspect_texts=limits["inspect_texts"],
        track_tool="evaluate_candidate (Track B), " if track == "B" else "",
        rules=RULES_A if track == "A" else RULES_B.format(k=limits["candidates_track_b"]),
        wall_hours=limits["wall_hours"])


def tool_schemas(track: str, n_layers: int, hidden: int) -> list[dict]:
    """Function schemas (name, description, parameters) shared by every harness."""
    s = [
        {"name": "generate",
         "description": "Get the model's replies (chat template applied) to user messages. Replies are returned "
                        "(each cut to 4,000 chars) and saved in full to gen/<k>.json in your workspace. "
                        "`adapter`: '' for the UNEDITED model" + ("; or the path of a candidate .npz (counts as one "
                                                                  "of your candidates)" if track == "B" else "") + ".",
         "parameters": {"type": "object", "properties": {
             "prompts": {"type": "array", "items": {"type": "string"}},
             "max_tokens": {"type": "integer"}, "thinking": {"type": "boolean"},
             "adapter": {"type": "string"}}, "required": ["prompts", "max_tokens", "thinking", "adapter"],
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
    if track == "B":
        s.insert(3, {"name": "evaluate_candidate",
                     "description": "Track B: score a candidate adapter (.npz path) on the task's dev split (not the "
                                    "held-out set). Counts as one of your candidates.",
                     "parameters": {"type": "object", "properties": {"path": {"type": "string"}},
                                    "required": ["path"], "additionalProperties": False}})
    return s
