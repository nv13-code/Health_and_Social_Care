# HSC D* Project

An interactive student hub for the **Pearson BTEC Level 3 National Extended Diploma in Health and Social Care** (spec Issue 10). It helps students aim for **D\*D\*D\*** and revise for the externally assessed units.

Open `index.html` in a browser, or host it on GitHub Pages or SciencePass. It's a single self-contained file.

## What's in it
- **Points.** The D*D*D* budget: 270 of 288 points, so students can lose only 18 across the course. Students enter grades, or raw exam marks (using June 2026 boundaries, which can be edited). Optional units are checked against the pathway rules (Extended Diploma or Health Studies).
- **Distinction coach.** Every internal unit (5–26) with its full P/M/D criteria from the spec. Each D criterion has a plain-words explanation, a must-include checklist, common pitfalls, sentence starters and what outstanding work looks like.
- **Exam revision (Units 1–4).** Topic checklists students rate red, amber or green; 150 multiple-choice questions; extended-answer practice with marking points and model answers; theories and frameworks; and the Unit 4 research toolkit with a fictional practice article.
- **Planner.** Exam countdowns, a weekly revision plan that adapts to topic ratings, internal deadlines and backup codes.

Progress is stored in the browser's localStorage.

## Editing
- `data/criteria.json` holds the learning aims and assessment criteria taken from the spec.
- `content/coach_*.json` holds the Distinction coaching and `content/exam_u*.json` the exam content.
- `src/hub.html` is the page template.
- Run `python3 tools/build.py` to rebuild `index.html` (the full page) and `dist/artifact.html` (the body only, for claude.ai artifacts).

Boundaries, legislation and regulator names change. Check them each year.
