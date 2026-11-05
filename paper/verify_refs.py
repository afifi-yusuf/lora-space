"""Check references.bib against Semantic Scholar (title search / arXiv id) and print what the record says.

Usage: python verify_refs.py [references.bib]   (no API key needed; ~1 request/s)
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://api.semanticscholar.org/graph/v1/paper"
FIELDS = "title,authors,year,venue,publicationVenue,externalIds"


def entries(path):
    text = open(path).read()
    for m in re.finditer(r"@(\w+)\{([^,]+),(.*?)\n\}", text, re.S):
        body = m.group(3)
        get = lambda k: (re.search(rf"\b{k}\s*=\s*\{{(.*?)\}}\s*,?\s*$", body, re.S | re.M) or [None, None])[1]
        yield m.group(2).strip(), {k: get(k) for k in ("title", "author", "year", "booktitle", "eprint", "howpublished")}


def fetch(url):
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "ref-check"}), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(3 * (attempt + 1)); continue
            if e.code == 404:
                return None
            raise
    return None


def clean(s):
    return re.sub(r"[{}\\]", "", s or "").strip()


for key, e in entries(sys.argv[1] if len(sys.argv) > 1 else "references.bib"):
    if e["howpublished"] and not e["eprint"]:
        print(f"== {key}: non-paper ({clean(e['howpublished'])[:80]}) — check manually\n")
        continue
    rec = None
    if e["eprint"]:
        rec = fetch(f"{API}/arXiv:{e['eprint']}?fields={FIELDS}")
    if rec is None:
        q = urllib.parse.quote(clean(e["title"]))
        res = fetch(f"{API}/search?query={q}&limit=1&fields={FIELDS}")
        rec = (res or {}).get("data", [None])[0] if res else None
    time.sleep(1.2)
    print(f"== {key}")
    print(f"   bib : {clean(e['title'])} | {e['year']} | {clean(e['booktitle'] or e['eprint'] or '')}")
    print(f"   bib authors: {clean(e['author'])[:160]}")
    if not rec:
        print("   S2  : NOT FOUND\n"); continue
    authors = [a["name"] for a in rec.get("authors", [])]
    pv = (rec.get("publicationVenue") or {}).get("name")
    print(f"   S2  : {rec.get('title')} | {rec.get('year')} | venue={rec.get('venue') or pv} | arXiv={(rec.get('externalIds') or {}).get('ArXiv')}")
    print(f"   S2 authors ({len(authors)}): {'; '.join(authors[:8])}{' …' if len(authors) > 8 else ''}\n")
