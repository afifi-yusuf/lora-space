"""Ceiling for a 'use the required function name' fix: alias the model's first defined function to the entry point
for tasks bucketed no_code, re-run EvalPlus, count how many then pass. Runs as `editor` in /srv/lso-editor/code."""
import json, re, subprocess, sys
from pathlib import Path
run = Path(sys.argv[1]); probs = {json.loads(l)["task_id"]: json.loads(l) for l in open("/srv/lso-editor/code/problems/mbpp.jsonl")}
sys.path.insert(0, "/srv/lso-editor/code"); import code_diag as C
b = json.load(open(run / "mbpp_buckets.json"))
out = run / "mbpp_rename.jsonl"; fixed = set()
with open(out, "w") as f:
    for l in open(run / "mbpp_samples.jsonl"):
        x = json.loads(l); ep = probs[x["task_id"]]["entry_point"]
        code = C.extract(x["raw"], ep)
        if b.get(x["task_id"]) == "no_code":
            m = re.findall(r"^def\s+(\w+)\s*\(", code, re.M)
            if m:
                code = code.split('if __name__')[0] + f"\n\n{ep} = {m[0]}\n"; fixed.add(x["task_id"])
        f.write(json.dumps({"task_id": x["task_id"], "solution": code}) + "\n")
subprocess.run([sys.executable, "-m", "evalplus.evaluate", "--dataset", "mbpp", "--samples", str(out), "--i-just-wanna-run"], check=True, capture_output=True)
ev = json.load(open(next(run.glob("mbpp_rename*eval_results.json"))))["eval"]
p = lambda t: ev[t][0]["base_status"] == "pass"; pp = lambda t: p(t) and ev[t][0]["plus_status"] == "pass"
n = len(ev)
print(run.name, "renamed", len(fixed), "now pass base", sum(p(t) for t in fixed), "| MBPP+ base pass@1", round(sum(map(p, ev)) / n, 4), "plus", round(sum(map(pp, ev)) / n, 4))
