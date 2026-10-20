#!/usr/bin/env python3
"""Build the HSC D* Project hub.

Merges the spec data (data/) and the revision/coaching content (content/) into
src/hub.html and writes two outputs:

  index.html          full HTML document (GitHub Pages, SciencePass, any web host)
  dist/artifact.html  page body only (for publishing as a claude.ai artifact)

Usage: python3 tools/build.py [--strict]   (--strict also fails on warnings: stale, unverified)
"""
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def load(rel):
    p = ROOT / rel
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


STALE_DAYS = 183
HARD = {"replaced", "renamed", "repealed"}


def walk_strings(obj, path=""):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_strings(v, f"{path}[{i}]")


def check_currency(reg):
    """Fail on content that uses a replaced name without the current one; warn on the rest."""
    errors, warnings = [], []
    today = date.today()
    for e in reg["entries"]:
        age = (today - datetime.strptime(e["verified"], "%Y-%m-%d").date()).days
        if age > STALE_DAYS:
            warnings.append(f"STALE {e['id']}: last verified {e['verified']} ({age} days ago)")
        if e["status"] == "unverified":
            warnings.append(f"UNVERIFIED {e['id']}: {e['spec']}")
        if e.get("secondarySourceOnly"):
            warnings.append(f"SECONDARY SOURCE ONLY {e['id']}: find a primary source")
    for f in sorted((ROOT / "content").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for path, text in walk_strings(data):
            for e in reg["entries"]:
                if not re.search(e["lint"], text, re.I):
                    continue
                if any(m.lower() in text.lower() for m in e["mustAlsoMention"]):
                    continue
                msg = f"{f.name}{path}: uses '{e['spec']}' without '{e['now']}'"
                (errors if e["status"] in HARD else warnings).append(msg)
    return errors, warnings


def iter_items():
    """Yield (label, question dict) for every multiple-choice item in content."""
    for u in (1, 2, 3, 4):
        e = load(f"content/exam_u{u}.json") or {}
        for q in e.get("mcq", []):
            yield f"exam_u{u}:{q.get('id')}", {"options": q.get("options"), "answer": q.get("answer")}
    for name in ("guide_a", "guide_b", "guide_c"):
        g = load(f"content/{name}.json") or {}
        for unit, ud in g.items():
            for code, c in ud.get("criteria", {}).items():
                for i, r in enumerate(c.get("requirements", [])):
                    ch = r.get("check") or {}
                    yield f"{name}:{unit}:{code}:{i}", {"options": ch.get("options"), "answer": ch.get("answer")}


def check_items():
    """Structural checks on every question, plus cue checks (key is the longest option, position bias)."""
    errors, warnings = [], []
    n = longest = 0
    pos = [0, 0, 0, 0]
    for label, q in iter_items():
        opts, a = q["options"], q["answer"]
        if not isinstance(opts, list) or len(opts) != 4 or not all(isinstance(o, str) and o.strip() for o in opts):
            errors.append(f"{label}: needs exactly 4 non-empty options")
            continue
        if not isinstance(a, int) or not 0 <= a <= 3:
            errors.append(f"{label}: answer must be 0-3")
            continue
        if len(set(o.strip().lower() for o in opts)) < 4:
            errors.append(f"{label}: duplicate options")
        n += 1
        pos[a] += 1
        lens = [len(o) for o in opts]
        if lens[a] == max(lens) and lens[a] > 1.15 * sorted(lens)[-2]:
            longest += 1
    if n:
        rate = longest / n
        msg = f"key is clearly the longest option in {longest}/{n} questions ({rate:.0%})"
        (warnings if rate > 0.25 else []).append("CUE " + msg)
        print("question check:", msg, "| answer positions", pos)
        if max(pos) > 0.4 * n:
            warnings.append(f"CUE answer position bias {pos}")
    return errors, warnings


def check_frames():
    """Writing frames must stay structure-only: every frame has a gap and none assumes results or experience."""
    errors = []
    f = load("content/frames.json") or {}
    bad = re.compile(r"\b(my results|my supervisor|my placement showed|i observed)\b", re.I)
    for verb, v in (f.get("verbs") or {}).items():
        for tier, frames in (v.get("tiers") or {}).items():
            for fr in frames:
                if "…" not in fr and "..." not in fr:
                    errors.append(f"frames {verb}/{tier}: no gap in '{fr}'")
                if bad.search(fr):
                    errors.append(f"frames {verb}/{tier}: assumes experience in '{fr}'")
    return errors


def write_sv_doc(reg):
    rows = [e for e in reg["entries"] if e["sv"]]
    rows.sort(key=lambda e: (min(e["units"]) if e["units"] else 99))
    out = [
        "# Substitutions for Standards Verifier approval",
        "",
        "**Qualification:** Pearson BTEC Level 3 National Extended Diploma in Health and Social Care (601/7198/4), specification Issue 10 (June 2022)  ",
        "**Basis:** spec p.7 says outdated references to legislation, policies, regulations and organisations may be substituted with current ones, *subject to confirmation by your Standards Verifier*.  ",
        f"**Register checked:** {reg['lastFullCheck']} · generated from `data/currency.json` by `tools/build.py`",
        "",
        "| Unit(s) | Spec reference | Proposed substitution | Status / since | Evidence | SV decision |",
        "|---|---|---|---|---|---|",
    ]
    for e in rows:
        units = ", ".join(str(u) for u in e["units"])
        src = " ".join(f"[{i+1}]({u})" for i, u in enumerate(e["sources"])) or "none yet"
        flag = " ⚠ unverified" if e["status"] == "unverified" else (" ⚠ secondary source" if e.get("secondarySourceOnly") else "")
        out.append(f"| {units} | {e['spec']} | {e['now']} | {e['status']}{(' · ' + e['since']) if e['since'] else ''}{flag} | {src} | ☐ Agreed ☐ Not agreed |")
    out += [
        "",
        "Items marked ⚠ need a primary source before they go into an assignment brief.",
        "",
        "Standards Verifier: ____________________  Date: __________  ",
        "Lead Internal Verifier: ____________________  Date: __________",
        "",
    ]
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "docs/standards-verifier-substitutions.md").write_text("\n".join(out), encoding="utf-8")
    return len(rows)


def main():
    strict = "--strict" in sys.argv
    reg = load("data/currency.json")
    errors, warnings = check_currency(reg)
    qe, qw = check_items()
    qe += check_frames()
    errors += qe
    warnings += qw
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    if errors or (strict and warnings):
        sys.exit(f"currency check failed: {len(errors)} errors, {len(warnings)} warnings")
    n_sv = write_sv_doc(reg)
    print(f"standards verifier list: {n_sv} substitutions")

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
    guide = {}
    for name in ("guide_a", "guide_b", "guide_c"):
        part = load(f"content/{name}.json")
        if part:
            guide.update(part)
    data = {"criteria": load("data/criteria.json"), "coach": coach, "exams": exams, "currency": reg, "guide": guide, "glossary": load("docs/audit/glossary.json") or [], "frames": load("content/frames.json")}
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    src = (ROOT / "src/hub.html").read_text(encoding="utf-8")
    import base64
    faces = [("Atkinson Hyperlegible", 400, "atkinson-hyperlegible-latin-400-normal"), ("Atkinson Hyperlegible", 700, "atkinson-hyperlegible-latin-700-normal"),
             ("Bricolage Grotesque", 700, "bricolage-grotesque-latin-700-normal"), ("Bricolage Grotesque", 800, "bricolage-grotesque-latin-800-normal"),
             ("IBM Plex Mono", 400, "ibm-plex-mono-latin-400-normal"), ("IBM Plex Mono", 600, "ibm-plex-mono-latin-600-normal")]
    css = "".join(f"@font-face{{font-family:'{n}';font-style:normal;font-weight:{w};font-display:swap;src:url(data:font/woff2;base64,{base64.b64encode((ROOT / 'assets/fonts' / (f + '.woff2')).read_bytes()).decode()}) format('woff2')}}" for n, w, f in faces)
    src = src.replace("/*__FONTS__*/", "/* Fonts are bundled (SIL OFL, see assets/fonts) so the page makes no outside requests. */" + css)
    body = src.replace("/*__DATA__*/null", blob)
    if re.search(r"https://fonts\.(googleapis|gstatic)", body):
        sys.exit("privacy check failed: page loads fonts from Google")
    assert body != src, "data placeholder not found"

    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "dist/artifact.html").write_text(body, encoding="utf-8")
    (ROOT / "dist/hsc-dstar-v2.html").write_text(body, encoding="utf-8")

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
    print(f"walkthrough units: {sorted(guide, key=int)}")
    print(f"index.html {len(full)//1024} KB, dist/artifact.html {len(body)//1024} KB")


if __name__ == "__main__":
    main()
