"""The target service: the only way an editor can run the frozen model. Same tools and budgets for every harness.

Runs on the GPU host. The editor's own code runs elsewhere (Agency's Docker sandbox, or the `editor` user for the
minimal loop) with numpy/scipy/safetensors and no torch or GPU, so gradients and private forward passes are not
available; every model call goes through here and is counted and logged.

Tools (all return text for the editor; bulky outputs are written into the editor's work directory):
  generate(prompts, max_tokens, thinking, adapter)   base model, or a candidate adapter in Track B
  inspect(texts, reply_prefix, thinking)             residual stream at the last token -> acts/inspect_<k>.npy
  inspect_module_inputs(texts, reply_prefix, modules, thinking)  writable-module inputs -> acts/modin_<k>.npz
  evaluate_candidate(path)                           Track B: candidate's score on the task's dev split
  commit_adapter(path, explanation)                  one commit; validated; ends the session
"""
from __future__ import annotations

import importlib
import json
import os
import signal
import subprocess
import sys
import threading
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Callable

import numpy as np

from . import data
from .spec import ROOT

VLLM_PORT = 8011


def load_target_module(target: str):
    """src/lso/gemma_syco.py configured for `target` (it reads LSO_TARGET at import)."""
    os.environ["LSO_TARGET"] = target
    sys.path.insert(0, str(ROOT / "src"))
    from lso import gemma_syco as G
    return importlib.reload(G) if getattr(G, "TARGET", None) != target else G


def merge_adapter(G, adapter: dict, out: Path) -> Path:
    """Base release + dW (fp32 add, bf16 round) for every adapter module; every other file and tensor unchanged."""
    import torch
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


def load_adapter_npz(path: Path) -> dict:
    z = np.load(path)
    names = {k.rsplit("::", 1)[0] for k in z.files}
    return {n: (z[f"{n}::B"].astype(np.float64), z[f"{n}::A"].astype(np.float64)) for n in names}


class VLLMServer:
    def __init__(self, model_dir: Path, gpu_mem: float, max_len: int, log: Path):
        env = dict(os.environ, VLLM_USE_FLASHINFER_SAMPLER="0")
        self.proc = subprocess.Popen(
            [str(ROOT / ".venv/bin/vllm"), "serve", str(model_dir), "--port", str(VLLM_PORT), "--dtype", "bfloat16",
             "--gpu-memory-utilization", str(gpu_mem), "--max-model-len", str(max_len), "--max-num-seqs", "64",
             "--served-model-name", "target", "--seed", "0", "--limit-mm-per-prompt", '{"image": 0, "video": 0}'],
            stdout=open(log, "a"), stderr=subprocess.STDOUT, env=env, start_new_session=True)
        for _ in range(180):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{VLLM_PORT}/health", timeout=2)
                return
            except Exception:  # noqa: BLE001
                if self.proc.poll() is not None:
                    raise RuntimeError(f"vLLM server exited; see {log}")
                time.sleep(5)
        raise RuntimeError("vLLM server did not come up in 15 min")

    def chat(self, prompt: str, max_tokens: int, thinking: bool, sampling: dict) -> tuple[str, str, int]:
        body = {"model": "target", "messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens,
                **sampling, "chat_template_kwargs": {"enable_thinking": thinking}}
        req = urllib.request.Request(f"http://127.0.0.1:{VLLM_PORT}/v1/chat/completions", json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
        resp = json.load(urllib.request.urlopen(req, timeout=3600))
        ch = resp["choices"][0]
        msg = ch["message"]
        think = msg.get("reasoning_content") or msg.get("reasoning") or ""
        text = (f"<think>{think}</think>\n" if think else "") + (msg.get("content") or "")
        return text, ch.get("finish_reason", ""), int(resp.get("usage", {}).get("completion_tokens", 0))

    def complete(self, prompt_text: str, max_tokens: int, sampling: dict) -> tuple[str, str, int]:
        """Raw completion of an already-templated text (used to continue from an assistant prefix)."""
        body = {"model": "target", "prompt": prompt_text, "max_tokens": max_tokens, **sampling}
        req = urllib.request.Request(f"http://127.0.0.1:{VLLM_PORT}/v1/completions", json.dumps(body).encode(),
                                     {"Content-Type": "application/json"})
        resp = json.load(urllib.request.urlopen(req, timeout=3600))
        ch = resp["choices"][0]
        return ch["text"], ch.get("finish_reason", ""), int(resp.get("usage", {}).get("completion_tokens", 0))

    def stop(self):
        os.killpg(self.proc.pid, signal.SIGTERM)
        self.proc.wait(timeout=120)


class TargetService:
    def __init__(self, task: dict, limits: dict, track: str, work: Path, run_dir: Path,
                 write: Callable[[str, bytes], None], container_work: str = "", vllm_mem: float = 0.35):
        import torch  # noqa: F401  (GPU host only)
        self.task, self.limits, self.track = task, limits, track
        self.work, self.run_dir, self.write, self.container_work = work, run_dir, write, container_work.rstrip("/")
        self.G = load_target_module(task["target"])
        self.G.MAX_RANK = limits["max_rank"]
        dec = dict(task["decoding"])
        self.max_gen_tokens = dec.pop("max_tokens")
        self.sampling = dec
        self.vllm_mem, self.max_len = vllm_mem, self.max_gen_tokens + 4096
        self.lock = threading.Lock()
        self.n = {"generate": 0, "analysis": 0, "candidates": 0}
        self.committed: dict | None = None
        self.explanation = ""
        self.gpu_seconds = 0.0
        self.calls = open(run_dir / "tool_calls.jsonl", "a")
        self.server = VLLMServer(self.G.MODEL_DIR, vllm_mem, self.max_len, run_dir / "vllm_server.log")
        self.tok, self.model = self.G.load_model()
        from .interp import Interp
        self.interp = Interp(self)
        ex = data.example_file(task, self.G)
        if ex is not None:
            write("examples.jsonl", ex.read_bytes())

    # ---------------------------------------------------------------- helpers
    def _log(self, tool: str, args: dict, out: str, t0: float) -> str:
        dt = time.time() - t0
        self.gpu_seconds += dt
        self.calls.write(json.dumps({"tool": tool, "args": args, "output": out[:30000], "seconds": round(dt, 1),
                                     "t": time.strftime("%Y-%m-%dT%H:%M:%S")}) + "\n")
        self.calls.flush()
        return out

    def save_npz(self, rel: str, arrays: dict) -> None:
        tmp = self.run_dir / "tmp_arrays.npz"
        np.savez(tmp, **{k: v.astype(np.float32) for k, v in arrays.items()})
        self.write(rel, tmp.read_bytes())

    def _resolve(self, path: str) -> Path:
        if self.container_work and path.startswith(self.container_work + "/"):
            path = path[len(self.container_work) + 1:]
        p = (self.work / path).resolve()
        if self.work.resolve() not in p.parents:
            raise ValueError("path must be inside the work directory")
        return p

    def _read_adapter(self, path: str) -> dict:
        p = self._resolve(path)
        try:
            raw = p.read_bytes()
        except PermissionError:
            raw = subprocess.run(["sudo", "cat", str(p)], capture_output=True, check=True).stdout
        tmp = self.run_dir / "last_adapter.npz"
        tmp.write_bytes(raw)
        z = np.load(tmp)
        return self.G.validate_adapter({k: z[k] for k in z.files}, self.model)

    def _chat_text(self, user: str, thinking: bool) -> str:
        return self.tok.apply_chat_template([{"role": "user", "content": user}], tokenize=False,
                                            add_generation_prompt=True, enable_thinking=thinking)

    def merge(self, adapter: dict, out: Path) -> Path:
        return merge_adapter(self.G, adapter, out)

    def _with_candidate(self, adapter: dict, fn):
        """Pause the base server, serve the merged candidate, run fn(server), restore the base server."""
        cdir = self.merge(adapter, self.run_dir / "cand_ckpt")
        self.server.stop()
        try:
            cs = VLLMServer(cdir, self.vllm_mem, self.max_len, self.run_dir / "vllm_candidates.log")
            try:
                return fn(cs)
            finally:
                cs.stop()
        finally:
            subprocess.run(["rm", "-rf", str(cdir)], check=True)
            self.server = VLLMServer(self.G.MODEL_DIR, self.vllm_mem, self.max_len, self.run_dir / "vllm_server.log")

    @staticmethod
    def _blank(v, *, words=()) -> str:
        """Normalize an 'empty' string argument. Some editors (e.g. Kimi) cannot emit a true empty string in a strict
        tool schema and send '""', "''", '"', ' ' or similar instead; treat any value made only of whitespace and quote
        characters (and, for adapter paths, the words 'none'/'null'/'base') as empty."""
        if v is None:
            return ""
        t = str(v).strip().strip("\"'`").strip()
        return "" if not t or t.lower() in words else str(v)

    # ---------------------------------------------------------------- tools
    def generate(self, prompts: list[str], max_tokens: int, thinking: bool, adapter: str = "",
                 reply_prefix: str = "") -> str:
        t0 = time.time()
        args = {"prompts": prompts, "max_tokens": max_tokens, "thinking": thinking, "adapter": adapter,
                "reply_prefix": reply_prefix}
        adapter = self._blank(adapter, words=("none", "null", "base"))
        reply_prefix = self._blank(reply_prefix)
        L = self.limits
        with self.lock:
            if self.committed is not None:
                return self._log("generate", args, "session is over (adapter committed)", t0)
            if self.n["generate"] >= L["generate_calls"]:
                return self._log("generate", args, f"generate budget exhausted ({L['generate_calls']} calls)", t0)
            if adapter and self.track != "B":
                return self._log("generate", args, f"not allowed in Track A: generate only the unedited model (adapter "
                                 f"must be empty; got {adapter!r})", t0)
            if adapter and self.n["candidates"] >= L["candidates_track_b"]:
                return self._log("generate", args, f"candidate budget exhausted ({L['candidates_track_b']})", t0)
            prompts = prompts[: L["generate_prompts"]]
            mt = max(1, min(int(max_tokens), self.max_gen_tokens))
            def one(s, p):
                if reply_prefix:  # resample from a point inside a reply: template + prefix, raw continuation
                    return s.complete(self._chat_text(p, thinking) + reply_prefix, mt, self.sampling)
                return s.chat(p, mt, thinking, self.sampling)

            def run(s):
                with ThreadPoolExecutor(16) as ex:
                    return list(ex.map(lambda p: one(s, p), prompts))
            try:
                if adapter:
                    ad = self._read_adapter(adapter)
                    res = self._with_candidate(ad, run)
                    self.n["candidates"] += 1
                else:
                    res = run(self.server)
            except Exception as e:  # noqa: BLE001
                return self._log("generate", args, f"generate failed: {e}", t0)
            k = self.n["generate"]
            self.n["generate"] += 1
            self.write(f"gen/{k}.json", json.dumps([{"prompt": p, "reply": r, "finish_reason": f, "tokens": n}
                                                    for p, (r, f, n) in zip(prompts, res)], indent=1).encode())
            out = (f"saved gen/{k}.json ({len(res)} replies{', candidate ' + adapter if adapter else ''}; "
                   f"generate calls left: {L['generate_calls'] - self.n['generate']}). Full replies are in the file; "
                   "below, a preview of each.\n" +
                   "\n".join(f"--- [{i}] finish={f} tokens={n} boxed={'yes' if chr(92) + 'boxed{' in r else 'no'} ---\n"
                             + self._preview(r, thinking) for i, (r, f, n) in enumerate(res)))
            return self._log("generate", args, out[:40000], t0)

    @staticmethod
    def _preview(r: str, thinking: bool) -> str:
        """Thinking-mode replies are long reasoning traces: show the start and the end only (full text in the file)."""
        if not thinking or len(r) <= 2000:
            return r[:4000]
        return f"{r[:1000]}\n[... {len(r) - 1600} chars omitted ...]\n{r[-600:]}"

    def _hidden_last(self, texts: list[str], prefix: str, thinking: bool):
        import torch
        dev = next(self.model.parameters()).device
        out, tops = [], []
        with torch.no_grad():
            for u in texts:
                ids = self.tok(self._chat_text(u, thinking) + prefix, return_tensors="pt",
                               add_special_tokens=False).input_ids.to(dev)
                o = self.model(input_ids=ids, output_hidden_states=True)
                out.append(torch.stack([h[0, -1] for h in o.hidden_states]).float().cpu().numpy())
                p = torch.softmax(o.logits[0, -1].float(), -1)
                v, i = p.topk(5)
                tops.append([(self.tok.decode([int(j)]), round(float(x), 4)) for x, j in zip(v, i)])
        return np.stack(out), tops

    def inspect(self, texts: list[str], reply_prefix: str, thinking: bool = False) -> str:
        t0, args = time.time(), {"texts": texts, "reply_prefix": reply_prefix, "thinking": thinking}
        reply_prefix = self._blank(reply_prefix)
        with self.lock:
            if self.n["analysis"] >= self.limits["analysis_calls"]:
                return self._log("inspect", args, f"analysis budget exhausted ({self.limits['analysis_calls']} calls)", t0)
            acts, tops = self._hidden_last(texts[: self.limits["inspect_texts"]], reply_prefix, thinking)
            k = self.n["analysis"]
            self.n["analysis"] += 1
            tmp = self.run_dir / "tmp_acts.npy"
            np.save(tmp, acts.astype(np.float32))
            self.write(f"acts/inspect_{k}.npy", tmp.read_bytes())
            out = "\n".join([f"saved acts/inspect_{k}.npy shape {acts.shape} (index 0 = embeddings, i+1 = output of "
                             f"layer i, the last one after the final norm); analysis calls left: "
                             f"{self.limits['analysis_calls'] - self.n['analysis']}"] +
                            [f"[{i}] top-5 next: {t}" for i, t in enumerate(tops)])
            return self._log("inspect", args, out, t0)

    def inspect_module_inputs(self, texts: list[str], reply_prefix: str, modules: list[str], thinking: bool = False) -> str:
        import torch
        t0 = time.time()
        args = {"texts": texts, "reply_prefix": reply_prefix, "modules": modules, "thinking": thinking}
        reply_prefix = self._blank(reply_prefix)
        with self.lock:
            if self.n["analysis"] >= self.limits["analysis_calls"]:
                return self._log("inspect_module_inputs", args, "analysis budget exhausted", t0)
            bad = [m for m in modules if m not in set(self.G.allowlist())]
            if bad:
                return self._log("inspect_module_inputs", args, f"not writable modules: {bad}", t0)
            named = dict(self.model.named_modules())
            store: dict[str, list] = {m: [] for m in modules}
            hooks = [named[m].register_forward_pre_hook(
                lambda mod, inp, m=m: store[m].append(inp[0][0, -1].float().cpu().numpy())) for m in modules]
            dev = next(self.model.parameters()).device
            try:
                with torch.no_grad():
                    for u in texts[: self.limits["inspect_texts"]]:
                        ids = self.tok(self._chat_text(u, thinking) + reply_prefix, return_tensors="pt",
                                       add_special_tokens=False).input_ids.to(dev)
                        self.model(input_ids=ids)
            finally:
                for h in hooks:
                    h.remove()
            k = self.n["analysis"]
            self.n["analysis"] += 1
            tmp = self.run_dir / "tmp_modin.npz"
            np.savez(tmp, **{m: np.stack(v).astype(np.float32) for m, v in store.items()})
            self.write(f"acts/modin_{k}.npz", tmp.read_bytes())
            out = f"saved acts/modin_{k}.npz: " + ", ".join(f"{m} {np.stack(v).shape}" for m, v in store.items())
            return self._log("inspect_module_inputs", args, out, t0)

    ANALYSIS = ("trace", "token_stats", "logit_lens", "attribution", "attention", "top_activations", "patch")

    def analysis(self, tool: str, **kw) -> str:
        """The interpretability tools (lsbench/interp.py). `intervene` is Track B only and counts as a candidate."""
        t0 = time.time()
        for key in ("reply_prefix", "adapter"):
            if isinstance(kw.get(key), str):
                kw[key] = self._blank(kw[key], words=("none", "null", "base") if key == "adapter" else ())
        with self.lock:
            if self.committed is not None:
                return self._log(tool, kw, "session is over (adapter committed)", t0)
            if tool == "intervene":
                if self.track != "B":
                    return self._log(tool, kw, "intervene is a Track B tool (it tests an intervention)", t0)
                if self.n["candidates"] >= self.limits["candidates_track_b"]:
                    return self._log(tool, kw, "candidate budget exhausted", t0)
            elif tool not in self.ANALYSIS:
                return self._log(tool, kw, f"unknown tool {tool}", t0)
            elif self.n["analysis"] >= self.limits["analysis_calls"]:
                return self._log(tool, kw, f"analysis budget exhausted ({self.limits['analysis_calls']} calls)", t0)
            for key in ("items",):
                if key in kw:
                    kw[key] = kw[key][: self.limits["analysis_items"]]
            try:
                out = getattr(self.interp, tool)(**kw)
            except Exception as e:  # noqa: BLE001
                return self._log(tool, kw, f"{tool} failed: {type(e).__name__}: {e}", t0)
            finally:
                import torch
                torch.cuda.empty_cache()
            if tool == "intervene":
                self.n["candidates"] += 1
                left = f"candidates left: {self.limits['candidates_track_b'] - self.n['candidates']}"
            else:
                self.n["analysis"] += 1
                left = f"analysis calls left: {self.limits['analysis_calls'] - self.n['analysis']}"
            return self._log(tool, kw, f"{out}\n({left})", t0)

    def evaluate_candidate(self, path: str) -> str:
        t0, args = time.time(), {"path": path}
        with self.lock:
            if self.track != "B":
                return self._log("evaluate_candidate", args, "not available in Track A", t0)
            if self.n["candidates"] >= self.limits["candidates_track_b"]:
                return self._log("evaluate_candidate", args, "candidate budget exhausted", t0)
            kind = self.task["dev"]["kind"]
            if kind == "none":
                return self._log("evaluate_candidate", args, "no dev scorer for this task; use generate with adapter", t0)
            try:
                ad = self._read_adapter(path)
            except Exception as e:  # noqa: BLE001
                return self._log("evaluate_candidate", args, f"adapter rejected: {e}", t0)
            rows = data.dev_rows(self.task, self.G)
            if kind == "syco":
                saved = self.G.apply_adapter(self.model, ad)
                try:
                    ev = self.G.evaluate(self.tok, self.model, rows, paraphrases=False)
                finally:
                    self.G.remove_adapter(self.model, saved)
                res = {k: ev[k] for k in ("wrong_follow_known", "right_acc", "plain_acc", "n_known")}
            else:  # math: dev accuracy under the task's decoding, graded like the held-out set
                sys.path[:0] = [str(ROOT / "ext/lm_understand-logs/exp8_math/code"), str(ROOT / "scripts/_shims")]
                import mathqa as Q
                mt = self.task["dev"]["max_tokens"]
                def run(s):
                    with ThreadPoolExecutor(16) as ex:
                        return list(ex.map(lambda r: s.chat(Q.build_prompt(r["problem"]), mt, True, self.sampling), rows))
                outs = self._with_candidate(ad, run)
                ok = [int(Q.is_correct(Q.extract(t)[0], r["answer"])) for r, (t, _, _) in zip(rows, outs)]
                res = {"dev_acc": round(float(np.mean(ok)), 4),
                       "finished": round(float(np.mean([f == "stop" for _, f, _ in outs])), 4),
                       "mean_tokens": round(float(np.mean([n for _, _, n in outs]))), "n": len(rows), "max_tokens": mt}
                self.write(f"gen/candidate_{self.n['candidates']}.json", json.dumps(
                    [{"problem": r["problem"], "answer": r["answer"], "reply": t, "finish_reason": f, "tokens": n,
                      "correct": c} for r, (t, f, n), c in zip(rows, outs, ok)], indent=1).encode())
            self.n["candidates"] += 1
            res["candidates_left"] = self.limits["candidates_track_b"] - self.n["candidates"]
            return self._log("evaluate_candidate", args, json.dumps(res), t0)

    def commit_adapter(self, path: str, explanation: str) -> str:
        t0, args = time.time(), {"path": path, "explanation": explanation}
        with self.lock:
            if self.committed is not None:
                return self._log("commit_adapter", args, "already committed; the session is over", t0)
            try:
                ad = self._read_adapter(path)
            except Exception as e:  # noqa: BLE001
                return self._log("commit_adapter", args, f"adapter rejected (format/constraint error, not a score): {e}", t0)
            self.committed, self.explanation = ad, explanation
            np.savez(self.run_dir / "adapter.npz", **{f"{n}::{k}": v for n, (B, A) in ad.items()
                                                      for k, v in (("B", B), ("A", A))})
            return self._log("commit_adapter", args, "adapter accepted; the session is over. Finish now with a one-line "
                                                     "summary.", t0)

    def adapter_stats(self) -> dict:
        import torch
        if self.committed is None:
            return {}
        named = dict(self.model.named_modules())
        return {"modules": len(self.committed),
                "params": int(sum(B.size + A.size for B, A in self.committed.values())),
                "max_rank": int(max(A.shape[0] for _, A in self.committed.values())),
                "rel_norms": {n: round(float(np.linalg.norm(B @ A) / torch.linalg.norm(named[n].weight.float()).item()), 4)
                              for n, (B, A) in self.committed.items()}}

    def close(self):
        """Free the GPU completely before held-out scoring (vLLM there asks for most of the card)."""
        import gc

        import torch
        try:
            self.server.stop()
        except Exception:  # noqa: BLE001
            pass
        for attr in ("interp", "model"):  # Interp holds its own reference to the model
            if hasattr(self, attr):
                delattr(self, attr)
        gc.collect()
        torch.cuda.empty_cache()
