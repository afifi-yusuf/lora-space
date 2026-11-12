"""GPU smoke test of every target-service tool (no editor LLM involved).
  LSO_TARGET=qwen .venv/bin/python -m lsbench.selftest [--track B]"""
from __future__ import annotations

import argparse
import shutil
import time

import numpy as np

from . import spec
from .target import TargetService


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--track", default="B")
    ap.add_argument("--task", default="math_qwen08")
    a = ap.parse_args()
    task, (_, limits) = spec.load_task(a.task), spec.load_entries()
    rdir = spec.ROOT / "runs/lsbench_selftest"
    shutil.rmtree(rdir, ignore_errors=True)
    work = rdir / "work"
    (work / "gen").mkdir(parents=True)
    (work / "acts").mkdir()

    def write(rel, data):
        p = work / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data)

    svc = TargetService(task, limits, a.track, work, rdir, write)
    ok = True

    def run(name, fn):
        nonlocal ok
        t = time.time()
        out = fn()
        bad = any(w in out for w in ("failed:", "Traceback", "unavailable"))
        ok &= not bad
        print(f"\n=== {name} ({time.time() - t:.1f}s) {'FAIL' if bad else 'ok'}\n{out[:1500]}", flush=True)

    q = "What is 17 * 23? Please reason step by step, and put your final answer within \\boxed{}."
    run("generate", lambda: svc.generate([q, "Name three primes."], 256, False))
    run("generate+prefix", lambda: svc.generate([q], 64, True, reply_prefix="Let me compute 17 * 23 carefully."))
    it = {"user": "", "reply": "", "gen_ref": "gen/0.json:0"}
    run("trace", lambda: svc.analysis("trace", items=[it], thinking=False,
                                      sites=["resid.0", "resid.12", "resid.24", "model.layers.15.mlp.down_proj",
                                             "model.layers.3.self_attn.o_proj:out"],
                                      positions=[0, 5, -1], spans=[[0, 20]], stride=0))
    run("trace stride", lambda: svc.analysis("trace", items=[it], thinking=False, sites=["resid.20"], positions=[],
                                             spans=[], stride=16))
    run("token_stats", lambda: svc.analysis("token_stats", items=[it], thinking=False))
    run("logit_lens", lambda: svc.analysis("logit_lens", items=[it], thinking=False, positions=[-1], layers=[],
                                           targets=["391", " 391"]))
    run("attribution", lambda: svc.analysis("attribution", item=it, thinking=False, position=-1, targets=["The", "\\"]))
    run("attention", lambda: svc.analysis("attention", item=it, thinking=False, layers=[], positions=[-1, 10], top_k=5))
    np.save(work / "dir.npy", np.random.default_rng(0).standard_normal(1024).astype(np.float32))
    run("top_activations neuron", lambda: svc.analysis("top_activations", site="model.layers.15.mlp.down_proj",
                                                       neuron=7, direction="", thinking=False, top_k=5))
    run("top_activations dir", lambda: svc.analysis("top_activations", site="resid.12", neuron=-1,
                                                    direction="dir.npy", thinking=False, top_k=5))
    src = {"user": "The capital of France is", "reply": "", "gen_ref": ""}
    tgt = {"user": "The capital of Italy is", "reply": "", "gen_ref": ""}
    run("patch", lambda: svc.analysis("patch", source=src, target=tgt, thinking=False, sites=["resid.12"],
                                      source_positions=[-1], target_positions=[-1], targets=["Paris", "Rome"]))
    run("inspect", lambda: svc.inspect(["Hello"], "", False))
    if a.track == "B":
        run("intervene", lambda: svc.analysis("intervene", items=[it], thinking=False,
                                              interventions=[{"site": "resid.12", "kind": "add", "neurons": [],
                                                              "direction": "dir.npy", "alpha": 4.0},
                                                             {"site": "model.layers.15.mlp.down_proj", "kind": "zero",
                                                              "neurons": [1, 2, 3], "direction": "", "alpha": 0.0}],
                                              positions=[-1], targets=[]))
    print("\nbudgets used:", svc.n)
    svc.close()
    print("SELFTEST", "PASSED" if ok else "FAILED")


if __name__ == "__main__":
    main()
