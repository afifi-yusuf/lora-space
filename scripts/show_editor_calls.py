"""Print an editor run's tool calls (calls.jsonl) compactly: python run_python/inspect/commit and their outputs."""
import json
import sys

width = int(sys.argv[2]) if len(sys.argv) > 2 else 280
for line in open(sys.argv[1]):
    r = json.loads(line)
    if r.get("text"):
        print(f"turn {r['turn']} SAYS: " + r["text"][:width].replace("\n", " | "))
    for c in r["calls"]:
        what = c.get("code") or c.get("explanation") or str(c.get("texts", ""))
        print(f"turn {r['turn']} {c['tool']}: " + what[:width].replace("\n", " | "))
        print("   -> " + c["output"][:width].replace("\n", " | "))
