"""Real before/after examples for the site, using the exact scoring setups. Runs on a GPU box from ~/lso.

  python make_examples.py syco ADAPTER OUT     forced-choice scores (as scored) + greedy replies, held-out facts
  python make_examples.py math ADAPTER OUT     think35 sampling, 32K cap, on base-wrong MATH-500 problems
  python make_examples.py code ADAPTER OUT     lsbench.score._code (EvalPlus, same as scoring), per-task buckets
"""
import json
import sys
from pathlib import Path

ROOT = Path.home() / "lso"
sys.path.insert(0, str(ROOT))
from lsbench.target import load_target_module, load_adapter_npz, merge_adapter  # noqa: E402

def vllm_gen(model_dir, prompts, sp_kwargs, max_len):
    import os
    os.environ.setdefault("VLLM_USE_FLASHINFER_SAMPLER", "0")
    from vllm import LLM, SamplingParams
    llm = LLM(model=str(model_dir), dtype="bfloat16", gpu_memory_utilization=0.8, max_model_len=max_len, seed=0,
              limit_mm_per_prompt={"image": 0, "video": 0})
    outs = llm.generate(prompts, SamplingParams(**sp_kwargs))
    res = [{"text": o.outputs[0].text, "tokens": len(o.outputs[0].token_ids), "finish": o.outputs[0].finish_reason} for o in outs]
    del llm
    import gc, torch
    gc.collect(); torch.cuda.empty_cache()
    return res



def main():
    cmd, adapter_path, out = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    out.mkdir(parents=True, exist_ok=True)
    G = load_target_module("qwen")
    adapter = load_adapter_npz(adapter_path)


    if cmd == "syco":
        import torch
        tok, model = G.load_model()
        rows = G.load_split(100)["heldout"]

        def run(tag):
            rs = []
            for r in rows:
                u = G.TEMPLATE.format(question=r["question"], guess=r["swap"])
                c, w = G.answer_logprobs(tok, model, u, [r["correct"], r["swap"]])
                pc, pw = G.answer_logprobs(tok, model, r["question"], [r["correct"], r["swap"]])
                rs.append({"q": r["question"], "correct": r["correct"], "swap": r["swap"], "follows": w > c, "known": pc > pw,
                           "margin": c - w})
            # greedy free replies for the candidates where the outcome differs is done after both passes
            return rs

        def replies(users):
            dev = next(model.parameters()).device
            outs = []
            for u in users:
                ids = tok(G.chat(tok, u), return_tensors="pt", add_special_tokens=False).to(dev)
                with torch.no_grad():
                    g = model.generate(**ids, max_new_tokens=80, do_sample=False)
                outs.append(tok.decode(g[0, ids["input_ids"].shape[1]:], skip_special_tokens=True))
            return outs

        base = run("base")
        saved = G.apply_adapter(model, adapter)
        edited = run("edited")
        cand = [i for i, (b, e) in enumerate(zip(base, edited)) if b["known"] and b["follows"] and not e["follows"]]
        users = [G.TEMPLATE.format(question=rows[i]["question"], guess=rows[i]["swap"]) for i in cand]
        ed_rep = replies(users)
        G.remove_adapter(model, saved)
        base_rep = replies(users)
        ex = [{**base[i], "prompt": u, "base_reply": br, "edited_reply": er, "edited_margin": edited[i]["margin"]}
              for i, u, br, er in zip(cand, users, base_rep, ed_rep)]
        (out / "syco.json").write_text(json.dumps({"n_known": sum(b["known"] for b in base),
            "base_follow": sum(b["follows"] for b in base if b["known"]), "edited_follow": sum(e["follows"] for b, e in zip(base, edited) if b["known"]),
            "examples": ex}, indent=1))
        print("syco candidates", len(ex))

    elif cmd == "math":
        sys.path.insert(0, str(ROOT / "ext/lm_understand-logs/exp8_math/code"))
        sys.path.insert(0, str(ROOT / "scripts/_shims"))
        import mathqa as Q
        from transformers import AutoTokenizer
        rows = [json.loads(l) for l in open(ROOT / "bench/math500.jsonl")][:200]
        per = {p["id"]: p["correct"][0] for p in json.load(open(ROOT / "results/m0/eval/base/math500_per_problem.json"))}
        wrong = sorted([r for r in rows if per.get(r["id"]) == 0], key=lambda r: len(r["problem"]))[:32]
        THINK35 = {"temperature": 0.6, "top_p": 0.95, "top_k": 20, "presence_penalty": 1.5, "max_tokens": 32768, "seed": 0}
        tok = AutoTokenizer.from_pretrained(G.MODEL_DIR)
        prompts = [tok.apply_chat_template([{"role": "user", "content": Q.build_prompt(r["problem"])}], tokenize=False,
                                           add_generation_prompt=True, enable_thinking=True) for r in wrong]
        ckpt = ROOT / "checkpoints/examples_math"
        merge_adapter(G, adapter, ckpt)
        ed = vllm_gen(ckpt, prompts, THINK35, 32768 + 2048)
        import shutil
        shutil.rmtree(ckpt)
        ba = vllm_gen(G.MODEL_DIR, prompts, THINK35, 32768 + 2048)
        ex = []
        for r, b, e in zip(wrong, ba, ed):
            bp, ep = Q.extract(b["text"])[0], Q.extract(e["text"])[0]
            ex.append({"id": r["id"], "problem": r["problem"], "answer": r["answer"],
                       "base": {**b, "pred": bp, "ok": int(Q.is_correct(bp, r["answer"]))},
                       "edited": {**e, "pred": ep, "ok": int(Q.is_correct(ep, r["answer"]))}})
        (out / "math.json").write_text(json.dumps(ex, indent=1))
        print("math: edited right & base wrong:", sum(x["edited"]["ok"] and not x["base"]["ok"] for x in ex), "of", len(ex))

    elif cmd == "code":
        from lsbench.score import _code
        s = _code(G, adapter, out.name, out / "score.log")
        print("code", json.dumps({k: v for k, v in s.items() if k != "mbpp_buckets"}))


if __name__ == '__main__':
    main()
