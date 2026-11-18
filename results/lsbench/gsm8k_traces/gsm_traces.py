"""GSM8K thinking-off damage test (lsbench/damage.py protocol, greedy, 200 problems, 1024 tokens), saving every answer.
Usage: python gsm_traces.py OUTDIR TAG=ADAPTER.npz ... (TAG=base for the unedited model)."""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path.home() / "lso"

GEN = r"""
import json, os, sys
os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")
sys.path[:0] = ["{root}/ext/lm_understand-logs/exp8_math/code", "{root}/scripts/_shims"]
import mathqa as Q
from vllm import LLM, SamplingParams
rows = [json.loads(l) for l in open("{root}/bench/gsm8k.jsonl")][:200]
llm = LLM(model="{ckpt}", dtype="bfloat16", gpu_memory_utilization=0.8, max_model_len=4096, seed=0,
          max_num_seqs=128, limit_mm_per_prompt={{"image": 0, "video": 0}})
tok = llm.get_tokenizer()
ps = [tok.apply_chat_template([{{"role": "user", "content": Q.build_prompt(r["problem"])}}], tokenize=False,
                              add_generation_prompt=True, enable_thinking=False) for r in rows]
outs = llm.generate(ps, SamplingParams(temperature=0.0, max_tokens=1024))
res = []
for r, o in zip(rows, outs):
    t = o.outputs[0].text; pred = Q.extract(t)[0]
    res.append({{"q": r["problem"], "answer": r["answer"], "text": t, "pred": pred, "ok": int(Q.is_correct(pred, r["answer"])),
                "finish": o.outputs[0].finish_reason, "tokens": len(o.outputs[0].token_ids)}})
json.dump(res, open("{out}", "w"))
print("ACC", sum(x["ok"] for x in res) / len(res))
"""


def main():
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(ROOT))
    from lsbench.target import load_target_module, load_adapter_npz, merge_adapter
    G = load_target_module("qwen")
    for arg in sys.argv[2:]:
        tag, path = arg.split("=", 1)
        if (out / f"{tag}.json").exists():
            continue
        if tag == "base":
            ck = G.MODEL_DIR
        else:
            ck = ROOT / "checkpoints/lsbench_merged" / f"gsm_{tag}"
            merge_adapter(G, load_adapter_npz(Path(path)), ck)
        try:
            p = subprocess.run([str(ROOT / ".venv/bin/python"), "-c", GEN.format(root=ROOT, ckpt=ck, out=out / f"{tag}.json")],
                               capture_output=True, text=True)
            print(tag, [l for l in p.stdout.splitlines() if l.startswith("ACC")] or p.stderr[-800:], flush=True)
        finally:
            if tag != "base":
                subprocess.run(["rm", "-rf", str(ck)])


if __name__ == "__main__":
    main()
