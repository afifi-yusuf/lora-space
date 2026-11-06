"""The honest competitor to weight writing: the SAME editor (GPT-6 Astra) and the SAME request, but Astra writes training
DATA, and an ordinary gradient LoRA is trained on it. Same target, writable modules, rank (8) and held-out scoring as
lso_request.py, so the two differ only in "Astra writes weights" vs "Astra writes data + SGD writes weights".

v0 is blind: Astra writes examples from the request alone (it does not see the base model's outputs).

  LSO_TARGET=qwen .venv/bin/python scripts/lso_data_baseline.py --request code [--n 240]
"""
from __future__ import annotations

import argparse
import gc
import json
import math
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
from openai import OpenAI

ROOT = Path(__file__).resolve().parent.parent
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "scripts")]
import lso_request as R  # noqa: E402
from lso import gemma_syco as G  # noqa: E402

BATCH_PROMPT = """You are preparing supervised fine-tuning data for a small chat model (Qwen3.5, thinking mode off).
THE USER'S REQUEST: "{request}"
{judged}

Write {k} training examples. Each is one chat turn: the user's message and the ideal assistant reply that would
teach the model to do what the request asks. Make them realistic and diverse (vary topics, difficulty and phrasing,
and cover the usage the user describes). Avoid repeating any of these task topics already written: {seen}.

Return ONLY a JSON array of objects {{"user": "...", "assistant": "..."}}, no other text."""


def write_data(client, request: str, judged: str, n: int, effort: str, log) -> list[dict]:
    data, seen, tokens = [], [], {"input": 0, "output": 0}
    while len(data) < n:
        k = min(40, n - len(data))
        r = client.responses.create(model="gpt-6-astra", store=False, max_output_tokens=64000,
                                    reasoning={"effort": effort},
                                    input=BATCH_PROMPT.format(request=request, judged=judged, k=k,
                                                              seen="; ".join(seen[-120:]) or "none"))
        tokens["input"] += r.usage.input_tokens
        tokens["output"] += r.usage.output_tokens
        text = r.output_text.strip()
        text = text[text.find("["): text.rfind("]") + 1]
        try:
            batch = [x for x in json.loads(text) if isinstance(x, dict) and x.get("user") and x.get("assistant")]
        except json.JSONDecodeError:
            batch = []
        data += batch
        seen += [x["user"].split("\n")[0][:60] for x in batch]
        log.write(json.dumps({"batch": len(batch), "total": len(data), "tokens": tokens}) + "\n"); log.flush()
        print(f"  data {len(data)}/{n}", flush=True)
    return data[:n], tokens


def train_lora_sft(tok, model, data: list[dict], rank: int = 8, lr: float = 2e-4, epochs: int = 3, batch: int = 8,
                   max_len: int = 1536) -> dict:
    """LoRA on the editor's writable modules (G.allowlist()), loss on the assistant reply only."""
    dev = next(model.parameters()).device
    torch.manual_seed(0)
    for p in model.parameters():
        p.requires_grad_(False)
    modules = dict(model.named_modules())
    params, hooks = {}, []
    for n in G.allowlist():
        lin = modules[n]
        A = torch.nn.Parameter(torch.randn(rank, lin.in_features, device=dev) / math.sqrt(lin.in_features))
        B = torch.nn.Parameter(torch.zeros(lin.out_features, rank, device=dev))
        params[n] = (B, A)
        hooks.append(lin.register_forward_hook(
            lambda m, inp, out, B=B, A=A: out + ((inp[0].to(A.dtype) @ A.T) @ B.T).to(out.dtype)))
    ex = []
    for d in data:
        p = tok(G.chat(tok, d["user"]), add_special_tokens=False)["input_ids"]
        t = tok(d["assistant"] + G.ANSWER_END + "\n", add_special_tokens=False)["input_ids"]
        ids = (p + t)[:max_len]
        ex.append((ids, ([-100] * len(p) + t)[:max_len]))
    flat = [x for BA in params.values() for x in BA]
    opt = torch.optim.AdamW(flat, lr=lr, betas=(0.9, 0.95), weight_decay=0.0)
    steps = epochs * math.ceil(len(ex) / batch)
    sched = torch.optim.lr_scheduler.LambdaLR(
        opt, lambda s: (s + 1) / 10 if s < 10 else 0.1 + 0.45 * (1 + math.cos(math.pi * (s - 10) / max(1, steps - 10))))
    rng = np.random.default_rng(0)
    model.train()
    micro = 2  # micro-batches of 2 x <=1,536 tokens: the 248K-vocab logits of a full batch of 8 would not fit
    for ep in range(epochs):
        losses = []
        order = rng.permutation(len(ex))
        for b in range(0, len(order), batch):
            idx = order[b:b + batch]
            n_tok = sum(sum(1 for t in ex[i][1] if t != -100) for i in idx)
            opt.zero_grad()
            for m0 in range(0, len(idx), micro):
                bt = [ex[i] for i in idx[m0:m0 + micro]]
                L = max(len(x) for x, _ in bt)
                ids = torch.full((len(bt), L), tok.pad_token_id, dtype=torch.long)
                lab = torch.full((len(bt), L), -100, dtype=torch.long)
                att = torch.zeros((len(bt), L), dtype=torch.long)
                for i, (x, y) in enumerate(bt):
                    ids[i, :len(x)], lab[i, :len(y)], att[i, :len(x)] = torch.tensor(x), torch.tensor(y), 1
                out = model(input_ids=ids.to(dev), attention_mask=att.to(dev))
                logits = out.logits[:, :-1].float()
                tgt = lab[:, 1:].to(dev)
                loss = torch.nn.functional.cross_entropy(logits.reshape(-1, logits.shape[-1]), tgt.reshape(-1),
                                                         ignore_index=-100, reduction="sum") / n_tok
                loss.backward()
                losses.append(loss.item() * n_tok / max(1, int((tgt != -100).sum())))
                del out, logits
            torch.nn.utils.clip_grad_norm_(flat, 1.0); opt.step(); sched.step()
        print(f"  epoch {ep}: mean loss {np.mean(losses):.4f}", flush=True)
    model.eval()
    for h in hooks:
        h.remove()
    return {n: (B.detach().double().cpu().numpy(), A.detach().double().cpu().numpy()) for n, (B, A) in params.items()}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--request", default="code", choices=sorted(R.REQUESTS))
    ap.add_argument("--n", type=int, default=240)
    ap.add_argument("--effort", default="high")
    ap.add_argument("--rank", type=int, default=8)
    a = ap.parse_args()
    name = f"data_{a.request}_{G.TARGET}_r{a.rank}_{time.strftime('%Y%m%dT%H%M%S')}"
    R.RUN_DIR = ROOT / "runs/code_edit" / name
    R.RUN_DIR.mkdir(parents=True)
    client = OpenAI(base_url=R.E.ENDPOINT, api_key=os.environ["AZURE_OPENAI_API_KEY"])
    t0 = time.time()
    data, tokens = write_data(client, R.REQUESTS[a.request], R.JUDGED.get(a.request, ""), a.n, a.effort,
                              open(R.RUN_DIR / "data_log.jsonl", "w"))
    (R.RUN_DIR / "data.json").write_text(json.dumps(data, indent=1))
    t_data = time.time() - t0
    tok, model = G.load_model()
    t1 = time.time()
    adapter = train_lora_sft(tok, model, data, rank=a.rank)
    t_train = time.time() - t1
    np.savez(ROOT / "checkpoints/code_edit" / f"{name}.npz",
             **{f"{n}::{k}": v for n, (B, A) in adapter.items() for k, v in (("B", B), ("A", A))})
    del model
    gc.collect(); torch.cuda.empty_cache()
    ckpt = R.merge_checkpoint(adapter, ROOT / "checkpoints/code_edit/merged" / name)
    result = {"run": name, "method": "Astra writes data (blind) + gradient LoRA", "target": G.TARGET, "n_examples": len(data),
              "rank": a.rank, "astra_tokens": tokens, "data_s": round(t_data), "train_s": round(t_train),
              "adapter_params": int(sum(B.size + A.size for B, A in adapter.values())),
              "heldout": R.score(ckpt, name)}
    os.system(f"rm -rf {ckpt}")
    (ROOT / "results/code_edit" / f"{name}.json").write_text(json.dumps(result, indent=1))
    print(json.dumps(result, indent=1))


if __name__ == "__main__":
    main()
