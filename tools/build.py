#!/usr/bin/env python3
"""Build the HSC D* Project hub.

Merges the spec data (data/) and the revision/coaching content (content/) into
src/hub.html and writes two outputs:

  index.html          full HTML document (GitHub Pages, SciencePass, any web host)
  dist/artifact.html  page body only (for publishing as a claude.ai artifact)

Usage: python3 tools/build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def main():
    coach = {}
    for name in ("coach_a", "coach_b", "coach_c"):
        part = load(f"content/{name}.json")
        if part:
            coach.update(part)
    exams = {}
    for u in (1, 2, 3, 4):
        e = load(f"content/exam_u{u}.json")
        if e:
            exams[str(u)] = e
    data = {"criteria": load("data/criteria.json"), "coach": coach, "exams": exams}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    src = (ROOT / "src/hub.html").read_text(encoding="utf-8")
    body = src.replace("/*__DATA__*/null", blob)
    assert body != src, "data placeholder not found"

    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist/artifact.html").write_text(body, encoding="utf-8")

    full = (
        "<!doctype html>\n<html lang=\"en-GB\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
        "<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}"
        "body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
        + body.replace("<style>", "<style>", 1)
    )
    # move everything before the first <script> (title, meta, links, style) into <head>
    head_end = full.index("<header")
    full = full[:head_end] + "</head>\n<body>\n" + full[head_end:] + "\n</body>\n</html>\n"
    (ROOT / "index.html").write_text(full, encoding="utf-8")

    print(f"coach units: {sorted(coach, key=int)}")
    print(f"exam units: {sorted(exams)}")
    print(f"index.html {len(full)//1024} KB, dist/artifact.html {len(body)//1024} KB")


if __name__ == "__main__":
    main()
