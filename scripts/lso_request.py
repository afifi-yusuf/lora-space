"""LSO request harness, v0 of the product loop: a natural-language request in, a LoRA whose weights GPT-6 Astra wrote out.

  "Make this model better at <X>"  ->  Astra builds its own tests, diagnoses the base model, writes ΔW = B @ A  ->  adapter

Unlike m05_editor.py (sycophancy, with our diagnostics and method hints), Astra gets ONLY the user's request, the
architecture, and tools. It must find what is wrong itself. First request: Python coding (scored afterwards on
MBPP+ and HumanEval+, which Astra never sees).

Tools:
  run_python     Astra's code, as the unprivileged `editor` user (numpy/scipy/safetensors), in its work directory with a
                 read-only copy of the weights. Astra can execute model-written code here (that is how it tests).
  generate       UNEDITED model completions (vLLM server, greedy) for prompts Astra writes; saved to gen/<k>.json.
                 Mode B: may pass a candidate adapter (HF model + adapter hooks; counts against the feedback budget).
  inspect / inspect_module_inputs   as in m05_editor.py (residual stream / module inputs at the last token).
  commit_adapter one commit, validated (allowlist, rank <= 8, norm cap); ends the session.
Mode A forbids evaluating edited models in any form; Mode B allows --feedback N generations with a candidate.

After the commit the harness frees the GPU, merges the adapter into a bf16 checkpoint (fp32 add, then round) and scores
it with scripts/code_diag.py (vLLM, thinking off, greedy), executing model code only as `editor`.

Usage (GPU box, repo root):  LSO_TARGET=qwen .venv/bin/python scripts/lso_request.py --request code [--feedback 5]
"""
from __future__ import annotations

import argparse
import gc
import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np
import torch
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))
from lso import gemma_syco as G  # noqa: E402  (target table, adapter validate/apply, activations)
import m05_editor as E  # noqa: E402  (run_python sandbox, inspect tools, endpoint)

REQUESTS = {
    "code": ("Make this model better at Python coding tasks. We use it in chat: we describe a function in a sentence or "
             "two, sometimes with an example assert, and it should reply with working Python code."),
}
JUDGED = {
    "code": ("Your adapter will be judged on held-out coding tasks of this kind (does the code it writes pass hidden "
             "tests), with thinking mode off, and on not damaging the model's other abilities."),
}
MAX_GEN_CALLS, MAX_GEN_PROMPTS, MAX_GEN_TOKENS = 25, 32, 2048
VLLM_PORT = 8011

GENERATE_TOOL = {
    "type": "function", "name": "generate",
    "description": f"Get the model's replies (greedy decoding, chat template applied) to up to {MAX_GEN_PROMPTS} user "
                   f"messages, max_tokens <= {MAX_GEN_TOKENS}. thinking=true turns on the model's thinking mode. "
                   "Replies are returned (each truncated to 4,000 chars) and saved in full to gen/<k>.json in your work "
                   f"directory. `adapter`: leave empty for the UNEDITED model. At most {MAX_GEN_CALLS} calls.",
    "parameters": {"type": "object", "properties": {
        "prompts": {"type": "array", "items": {"type": "string"}},
        "max_tokens": {"type": "integer"},
        "thinking": {"type": "boolean"},
        "adapter": {"type": "string", "description": "'' for the unedited model; Mode B only: path of a candidate .npz"}},
        "required": ["prompts", "max_tokens", "thinking", "adapter"], "additionalProperties": False}, "strict": True}


def task_text(request: str, feedback: int) -> str:
    if feedback:
        rules = f"""RULES (feedback-guided setting):
- You may inspect the unedited model: weights (run_python), behavior (generate) and activations (inspect tools).
- You may try up to {feedback} candidate adapters: generate with `adapter` set to a candidate's path. Do not otherwise
  evaluate edited models (no re-implementation of the network).
- No gradient descent, autograd, optimizers or iterative fitting of weights to a loss.
- Commit exactly one adapter with commit_adapter; it is then scored once on held-out tasks you never see."""
    else:
        rules = """RULES (strict one-shot setting):
- You may inspect the UNEDITED model only: weights (run_python), behavior (generate, with adapter='') and activations
  (inspect tools). You can run the model's code yourself in run_python to test it.
- Do not evaluate an edited model in any way (no generation with your adapter, no re-implementation of the network to
  test candidates). Reason from the unedited model's behavior and internals.
- No gradient descent, autograd, optimizers or iterative fitting of weights to a loss.
- Commit exactly one adapter with commit_adapter. You will not see its score."""
    return f"""You are improving a frozen language model by writing a LoRA adapter for it. No gradients and no training.

THE USER'S REQUEST: "{request}"
{JUDGED.get(ARGS.request, "")}

MODEL. {G.ARCH_TEXT}
Its weights (bf16 values stored as safetensors) are in your work directory: model.safetensors (read-only). A linear
module computes y = W x with W of shape (d_out, d_in). The model is used with thinking mode off unless said otherwise.

HOW TO WORK. Nobody gives you a benchmark or a diagnosis. Write your own test tasks, look at what the model actually
does (generate, then run its code in run_python), find what goes wrong and why, decide what a weight edit can fix, and
write the adapter. Keep some of your own tasks aside to check your reasoning.

WHAT YOU CONTROL. A LoRA update dW = B @ A (rank r <= 8, ||dW|| <= {G.MAX_REL_NORM} x ||W||) on any subset of the
writable modules: {G.WRITE_SPACE_TEXT}

{rules}
Explain your reasoning briefly before each tool call."""


class VLLMServer:
    """Base-model generation through a local vLLM OpenAI-compatible server (separate process, its own GPU share)."""

    def __init__(self, model_dir: Path, gpu_mem: float):
        env = dict(os.environ, VLLM_USE_FLASHINFER_SAMPLER="0")
        self.log = open(RUN_DIR / "vllm_server.log", "w")
        self.proc = subprocess.Popen(
            [str(ROOT / ".venv/bin/vllm"), "serve", str(model_dir), "--port", str(VLLM_PORT), "--dtype", "bfloat16",
             "--gpu-memory-utilization", str(gpu_mem), "--max-model-len", str(MAX_GEN_TOKENS + 4096),
             "--max-num-seqs", "64", "--served-model-name", "target", "--seed", "0",
             "--limit-mm-per-prompt", '{"image": 0, "video": 0}'],
            stdout=self.log, stderr=subprocess.STDOUT, env=env, start_new_session=True)
        for _ in range(180):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{VLLM_PORT}/health", timeout=2)
                return
            except Exception:  # noqa: BLE001
                if self.proc.poll() is not None:
                    raise RuntimeError("vLLM server exited; see vllm_server.log")
                time.sleep(5)
        raise RuntimeError("vLLM server did not come up in 15 min")

    def chat(self, prompt: str, max_tokens: int, thinking: bool) -> str:
        body = {"model": "target", "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens,
                "temperature": 0.0, "chat_template_kwargs": {"enable_thinking": thinking}}
        req = urllib.request.Request(f"http://127.0.0.1:{VLLM_PORT}/v1/chat/completions", json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
        msg = json.load(urllib.request.urlopen(req, timeout=1800))["choices"][0]["message"]
        think = msg.get("reasoning_content") or msg.get("reasoning") or ""
        return (f"<think>{think}</think>\n" if think else "") + (msg.get("content") or "")

    def stop(self):
        os.killpg(self.proc.pid, signal.SIGTERM)
        self.proc.wait(timeout=120)


@torch.no_grad()
def hf_generate(tok, model, prompt: str, max_tokens: int, thinking: bool) -> str:
    """One prompt at a time (no padding: safest for the hybrid linear-attention layers). Used for Mode B candidates."""
    dev = next(model.parameters()).device
    text = tok.apply_chat_template([{"role": "user", "content": prompt}], tokenize=False, add_generation_prompt=True,
                                   enable_thinking=thinking)
    ids = tok(text, return_tensors="pt", add_special_tokens=False).input_ids.to(dev)
    out = model.generate(ids, max_new_tokens=max_tokens, do_sample=False)
    return tok.decode(out[0, ids.shape[1]:], skip_special_tokens=True)


def save_for_editor(work: Path, rel: str, obj) -> None:
    tmp = RUN_DIR / "tmp_out.json"
    tmp.write_text(json.dumps(obj, indent=1))
    subprocess.run(["sudo", "install", "-D", "-o", E.EDITOR_USER, "-g", E.EDITOR_USER, "-m", "644", str(tmp),
                    str(work / rel)], check=True)


def merge_checkpoint(adapter: dict, out: Path) -> Path:
    """Base release + ΔW (fp32 add, bf16 round) for every adapter module; all other files and tensors unchanged."""
    from safetensors.torch import load_file, save_file
    out.mkdir(parents=True, exist_ok=True)
    for f in G.MODEL_DIR.iterdir():
        if f.is_file() and not f.name.endswith(".safetensors"):
            (out / f.name).write_bytes(f.read_bytes())
    for st in sorted(G.MODEL_DIR.glob("*.safetensors")):
        t = load_file(str(st))
        for n, (B, A) in adapter.items():
            key = G.WEIGHT_PREFIX + n[len("model."):] + ".weight"
            if key in t:
                t[key] = (t[key].float() + torch.from_numpy(B @ A).float()).to(t[key].dtype)
        save_file(t, str(out / st.name), metadata={"format": "pt"})
    return out


def score(ckpt: Path, tag: str) -> dict:
    """Held-out scoring with the same pipeline as the base diagnosis (code_diag.py gen, then eval as `editor`)."""
    subprocess.run([str(ROOT / ".venv/bin/python"), str(ROOT / "scripts/code_diag.py"), "gen", "--model", str(ckpt),
                    "--tag", tag, "--gpu-mem", "0.8", "--out-root", str(ROOT / "results/code_edit/scores")],
                   check=True, stdout=open(RUN_DIR / "score_gen.log", "w"), stderr=subprocess.STDOUT)
    code = Path("/srv/lso-editor/code")
    sh = lambda *c: subprocess.run(["sudo", *c], check=True)  # noqa: E731
    sh("mkdir", "-p", str(code / tag))
    src = ROOT / "results/code_edit/scores" / tag
    for f in src.glob("*_samples.jsonl"):
        sh("cp", str(f), str(code / tag / f.name))
    sh("install", "-m", "644", str(ROOT / "scripts/code_diag.py"), str(code / "code_diag.py"))
    sh("chown", "-R", "editor:editor", str(code))
    subprocess.run(["sudo", "-u", "editor", "env", f"XDG_CACHE_HOME={code}/cache", f"HOME={code}",
                    "/opt/code-venv/bin/python", "code_diag.py", "eval", "--dir", str(code / tag), "--problems",
                    str(code / "problems")], cwd=code, check=True, stdout=open(RUN_DIR / "score_eval.log", "w"),
                   stderr=subprocess.STDOUT)
    for f in ("summary.json", "humaneval_buckets.json", "mbpp_buckets.json"):
        subprocess.run(["sudo", "cp", str(code / tag / f), str(src / f)], check=True)
    return json.load(open(src / "summary.json"))


def main() -> None:
    global ARGS, RUN_DIR
    ap = argparse.ArgumentParser()
    ap.add_argument("--request", default="code", choices=sorted(REQUESTS))
    ap.add_argument("--effort", default="xhigh")
    ap.add_argument("--max-turns", type=int, default=80)
    ap.add_argument("--feedback", type=int, default=0, help="Mode B: number of candidate generations allowed")
    ap.add_argument("--vllm-mem", type=float, default=0.35)
    ap.add_argument("--no-score", action="store_true")
    ARGS = a = ap.parse_args()
    mode = f"modeB{a.feedback}" if a.feedback else "modeA"
    name = f"req_{a.request}_{G.TARGET}_{mode}_{time.strftime('%Y%m%dT%H%M%S')}"
    RUN_DIR = ROOT / "runs/code_edit" / name
    RUN_DIR.mkdir(parents=True)
    server = VLLMServer(G.MODEL_DIR, a.vllm_mem)
    tok, model = G.load_model()
    work = E.WORK_ROOT / name / "work"
    sh = lambda *c: subprocess.run(["sudo", *c], check=True)  # noqa: E731
    sh("mkdir", "-p", str(work / "acts"), str(work / "gen"))
    sh("install", "-m", "444", str(G.MODEL_DIR / G.WEIGHTS_FILE), str(work / "model.safetensors"))
    sh("chown", "-R", f"{E.EDITOR_USER}:{E.EDITOR_USER}", str(E.WORK_ROOT / name))
    sh("chmod", "755", str(E.WORK_ROOT), str(E.WORK_ROOT / name), str(work), str(work / "acts"), str(work / "gen"))

    client = OpenAI(base_url=E.ENDPOINT, api_key=os.environ["AZURE_OPENAI_API_KEY"])
    tools = [E.TOOLS[0], GENERATE_TOOL, E.TOOLS[1], E.MODULE_INPUT_TOOL, E.TOOLS[2]]
    items: list = [{"role": "user", "content": task_text(REQUESTS[a.request], a.feedback)}]
    (RUN_DIR / "task.txt").write_text(items[0]["content"])
    log = open(RUN_DIR / "calls.jsonl", "w")
    n_gen, n_inspect, n_feedback, committed = 0, 0, 0, None
    totals = {"input": 0, "cached": 0, "output": 0, "reasoning": 0}

    def read_adapter(path: str) -> dict:
        p = (work / path).resolve()
        if work not in p.parents:
            raise ValueError("path must be inside the work directory")
        raw = subprocess.run(["sudo", "cat", str(p)], capture_output=True, check=True).stdout
        tmp = RUN_DIR / "last_adapter.npz"
        tmp.write_bytes(raw)
        z = np.load(tmp)
        return G.validate_adapter({k: z[k] for k in z.files}, model)

    t0 = time.time()
    for turn in range(1, a.max_turns + 1):
        t = time.time()
        r = client.responses.create(model="gpt-6-astra", input=items, tools=tools,
                                    reasoning={"effort": a.effort, "summary": "auto"},
                                    include=["reasoning.encrypted_content"], store=False, max_output_tokens=64000)
        u = r.usage
        cached = getattr(getattr(u, "input_tokens_details", None), "cached_tokens", 0) or 0
        reasoning = getattr(getattr(u, "output_tokens_details", None), "reasoning_tokens", 0) or 0
        for k, v in (("input", u.input_tokens), ("cached", cached), ("output", u.output_tokens), ("reasoning", reasoning)):
            totals[k] += v
        items += [it.model_dump(exclude_none=True) for it in r.output]
        rec = {"turn": turn, "latency_s": round(time.time() - t, 1), "input": u.input_tokens, "cached": cached,
               "output": u.output_tokens, "reasoning": reasoning, "text": r.output_text, "calls": []}
        calls = [it for it in r.output if it.type == "function_call"]
        for c in calls:
            args = json.loads(c.arguments)
            ts = time.time()
            if c.name == "run_python":
                out, _ = E.run_python(work, args["code"])
                rec["calls"].append({"tool": "run_python", "code": args["code"], "output": out})
            elif c.name == "generate":
                prompts = args["prompts"][:MAX_GEN_PROMPTS]
                mt = max(1, min(int(args["max_tokens"]), MAX_GEN_TOKENS))
                cand = args.get("adapter") or ""
                if n_gen >= MAX_GEN_CALLS:
                    out = f"generate budget exhausted ({MAX_GEN_CALLS} calls)"
                elif cand and not a.feedback:
                    out = "not allowed in the strict one-shot setting: generate only with adapter=''"
                elif cand and n_feedback >= a.feedback:
                    out = f"candidate budget exhausted ({a.feedback})"
                else:
                    try:
                        if cand:
                            ad = read_adapter(cand)
                            saved = G.apply_adapter(model, ad)
                            try:
                                replies = [hf_generate(tok, model, p, mt, args["thinking"]) for p in prompts]
                            finally:
                                G.remove_adapter(model, saved)
                            n_feedback += 1
                        else:
                            with ThreadPoolExecutor(16) as ex:
                                replies = list(ex.map(lambda p: server.chat(p, mt, args["thinking"]), prompts))
                        save_for_editor(work, f"gen/{n_gen}.json", [{"prompt": p, "reply": x} for p, x in zip(prompts, replies)])
                        out = (f"saved gen/{n_gen}.json ({len(replies)} replies{', candidate ' + cand if cand else ''})\n" +
                               "\n".join(f"--- [{i}] ---\n{x[:4000]}" for i, x in enumerate(replies)))
                        n_gen += 1
                    except Exception as e:  # noqa: BLE001
                        out = f"generate failed: {e}"
                rec["calls"].append({"tool": "generate", "prompts": prompts, "max_tokens": mt, "thinking": args["thinking"],
                                     "adapter": cand, "output": out[:30000]})
                out = out[:60000]
            elif c.name in ("inspect", "inspect_module_inputs"):
                if n_inspect >= E.MAX_INSPECT_CALLS:
                    out = f"inspect budget exhausted ({E.MAX_INSPECT_CALLS} calls)"
                elif c.name == "inspect":
                    out = E.inspect(tok, model, work, n_inspect, args["texts"], args["reply_prefix"]); n_inspect += 1
                else:
                    out = E.inspect_module_inputs(tok, model, work, n_inspect, args["texts"], args["reply_prefix"],
                                                  args["modules"]); n_inspect += 1
                rec["calls"].append({"tool": c.name, "texts": args["texts"], "prefix": args["reply_prefix"], "output": out})
            elif c.name == "commit_adapter":
                try:
                    committed = read_adapter(args["path"])
                    committed_expl = args["explanation"]
                    out = "adapter accepted; session over"
                except Exception as e:  # noqa: BLE001
                    out = f"adapter rejected (format/constraint error, not a score): {e}"
                rec["calls"].append({"tool": "commit_adapter", "path": args["path"], "explanation": args["explanation"],
                                     "output": out})
            else:
                out = f"unknown tool {c.name}"
            rec["calls"][-1]["seconds"] = round(time.time() - ts, 1) if rec["calls"] else None
            items.append({"type": "function_call_output", "call_id": c.call_id, "output": out})
        log.write(json.dumps(rec) + "\n"); log.flush()
        print(f"turn {turn}: {rec['latency_s']}s in={u.input_tokens} cached={cached} out={u.output_tokens} "
              f"tools={[x['tool'] for x in rec['calls']]}", flush=True)
        if committed is not None or not calls:
            break
    result = {"run": name, "request": REQUESTS[a.request], "target": G.TARGET,
              "mode": f"B ({a.feedback} candidates)" if a.feedback else "A (strict one-shot)", "effort": a.effort,
              "turns": turn, "generate_calls": n_gen, "inspect_calls": n_inspect, "candidates_tried": n_feedback,
              "wall_s": round(time.time() - t0), "tokens": totals, "committed": committed is not None}
    if committed is not None:
        result.update(explanation=committed_expl, adapter_modules=len(committed),
                      adapter_params=int(sum(B.size + A.size for B, A in committed.values())),
                      rel_norms={n: round(float(np.linalg.norm(B @ A) / torch.linalg.norm(dict(model.named_modules())[n].weight.float()).item()), 4)
                                 for n, (B, A) in committed.items()})
        ad_path = ROOT / "checkpoints/code_edit" / f"{name}.npz"
        ad_path.parent.mkdir(parents=True, exist_ok=True)
        np.savez(ad_path, **{f"{n}::{k}": v for n, (B, A) in committed.items() for k, v in (("B", B), ("A", A))})
    server.stop()
    del model
    gc.collect(); torch.cuda.empty_cache()
    if committed is not None and not a.no_score:
        ckpt = merge_checkpoint(committed, ROOT / "checkpoints/code_edit/merged" / name)
        result["heldout"] = score(ckpt, name)
        subprocess.run(["rm", "-rf", str(ckpt)], check=True)
    out_dir = ROOT / "results/code_edit"
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / f"{name}.json").write_text(json.dumps(result, indent=1))
    (RUN_DIR / "result.json").write_text(json.dumps(result, indent=1))
    print(json.dumps({k: v for k, v in result.items() if k not in ("rel_norms",)}, indent=1))


ARGS = None
RUN_DIR: Path


if __name__ == "__main__":
    main()
