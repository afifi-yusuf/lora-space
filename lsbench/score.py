"""Held-out scoring of a committed adapter, normalized: 0 = unedited model, 100 = the task's best reference."""
from __future__ import annotations

import json
import subprocess
import time
from pathlib import Path

from .spec import ROOT
from .target import load_adapter_npz, load_target_module, merge_adapter

PY = str(ROOT / ".venv/bin/python")


def normalized(task: dict, value: float) -> dict:
    sc = task["score"]
    refs = sc.get("references", {})
    if not refs:
        return {"normalized": None, "reference": None}
    pick = max if sc["higher_is_better"] else min
    name = pick(refs, key=refs.get)
    best = refs[name]
    return {"normalized": round(100 * (value - sc["base"]) / (best - sc["base"]), 1), "reference": name,
            "reference_value": best}


def _math500(task: dict, G, adapter: dict, tag: str, log: Path) -> dict:
    ckpt = ROOT / "checkpoints/m0" / tag
    merge_adapter(G, adapter, ckpt)
    try:
        subprocess.run([PY, str(ROOT / "scripts/m0_eval.py"), "run", tag, "--sets", "math500",
                        "--samples", str(task["score"]["samples"]), "--limit", str(task["score"]["limit"]),
                        "--gpu-mem", "0.85"], check=True, stdout=open(log, "w"), stderr=subprocess.STDOUT)
    finally:
        subprocess.run(["rm", "-rf", str(ckpt)], check=True)
    return json.load(open(ROOT / "results/m0/eval" / tag / "scores.json"))["math500"]


def _syco(G, adapter: dict) -> dict:
    tok, model = G.load_model()
    saved = G.apply_adapter(model, adapter)
    try:
        return G.evaluate(tok, model, G.load_split(100)["heldout"])
    finally:
        G.remove_adapter(model, saved)


def _code(G, adapter: dict, tag: str, log: Path) -> dict:
    """EvalPlus via scripts/code_diag.py (generation as us, execution of model code only as `editor`)."""
    ckpt = ROOT / "checkpoints/lsbench_merged" / tag
    merge_adapter(G, adapter, ckpt)
    out_root = ROOT / "results/lsbench/code_scores"
    try:
        subprocess.run([PY, str(ROOT / "scripts/code_diag.py"), "gen", "--model", str(ckpt), "--tag", tag,
                        "--gpu-mem", "0.8", "--out-root", str(out_root)], check=True, stdout=open(log, "w"),
                       stderr=subprocess.STDOUT)
    finally:
        subprocess.run(["rm", "-rf", str(ckpt)], check=True)
    code = Path("/srv/lso-editor/code")
    sh = lambda *c: subprocess.run(["sudo", *c], check=True)  # noqa: E731
    sh("mkdir", "-p", str(code / tag))
    src = out_root / tag
    for f in src.glob("*_samples.jsonl"):
        sh("cp", str(f), str(code / tag / f.name))
    sh("install", "-m", "644", str(ROOT / "scripts/code_diag.py"), str(code / "code_diag.py"))
    sh("chown", "-R", "editor:editor", str(code))
    subprocess.run(["sudo", "-u", "editor", "env", f"XDG_CACHE_HOME={code}/cache", f"HOME={code}",
                    "/opt/code-venv/bin/python", "code_diag.py", "eval", "--dir", str(code / tag), "--problems",
                    str(code / "problems")], cwd=code, check=True, stdout=open(log, "a"), stderr=subprocess.STDOUT)
    sh("cp", str(code / tag / "summary.json"), str(src / "summary.json"))
    s = json.load(open(src / "summary.json"))
    return {"mbpp_base": s["mbpp"]["pass@1_base"], "mbpp_plus": s["mbpp"]["pass@1_plus"],
            "humaneval_base": s["humaneval"]["pass@1_base"], "humaneval_plus": s["humaneval"]["pass@1_plus"],
            "mbpp_buckets": s["mbpp"].get("buckets")}


def score_run(task: dict, rdir: Path) -> dict:
    G = load_target_module(task["target"])
    adapter = load_adapter_npz(rdir / "adapter.npz")
    t0, kind, tag = time.time(), task["score"]["kind"], rdir.name
    if kind == "math500":
        raw = _math500(task, G, adapter, f"lsb_{tag}", rdir / "score.log")
    elif kind == "syco":
        raw = _syco(G, adapter)
    elif kind == "code":
        raw = _code(G, adapter, tag, rdir / "score.log")
    else:
        raise ValueError(kind)
    value = raw[task["score"]["metric"]]
    return {"metric": task["score"]["metric"], "value": value, **normalized(task, value), "raw": raw,
            "score_gpu_s": round(time.time() - t0)}
