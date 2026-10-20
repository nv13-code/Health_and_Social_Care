# HSC D* Project

An interactive student hub for the **Pearson BTEC Level 3 National Extended Diploma in Health and Social Care** (spec Issue 10). It helps students aim for **D\*D\*D\*** and revise for the externally assessed units.

Open `index.html` in a browser, or host it on GitHub Pages or SciencePass. It's a single self-contained file.

## What's in it
- **Today.** A daily retrieval quiz of about 15 minutes. Spaced repetition works on individual questions (Leitner boxes at 1, 3, 7, 14 and 30 days), with missed questions coming back tomorrow and units mixed together. Students rate their confidence before seeing the options, and a calibration panel compares how sure they felt with how often they were right. A weekly task list is built from the assessment calendar and exam dates, and weeks where hand-ins and exams pile up are flagged.
- **Points.** The D*D*D* budget: 270 of 288 points, so students can lose only 18 across the course. Students enter grades, or raw exam marks (using June 2026 boundaries, which can be edited). Optional units are checked against the pathway rules (Extended Diploma or Health Studies).
- **Guided walkthroughs.** Each Distinction criterion is broken into evidence requirements taken from the spec's "Essential information for assessment decisions". Every requirement has an explanation, a strong example and a near-miss to compare, a prompt to explain it in the student's own words, a check question, and an evidence map where students record where their own draft meets it. All the examples use a made-up practice case for each unit, so the hub coaches and never writes assignment text. That protects authenticity under BTEC and JCQ AI rules.
- **Distinction coach.** Every internal unit (5–26) with its full P/M/D criteria from the spec. Each D criterion has a plain-words explanation, a must-include checklist, common pitfalls, sentence starters and what outstanding work looks like.
- **Exam revision (Units 1–4).** Topic checklists students rate red, amber or green; 150 multiple-choice questions; extended-answer practice with marking points and model answers; theories and frameworks; and the Unit 4 research toolkit with a fictional practice article.
- **Assessment calendar.** Launch and hand-in dates generate five milestones per assignment. Adding the date of an assessment decision works out the 15-working-day resubmission deadline. Events can be added to Google Calendar, and outside Claude the full calendar downloads as an .ics file with a daily 5pm quiz reminder.
- **Planner.** Exam countdowns, a weekly revision plan that adapts to topic ratings, internal deadlines and backup codes.

Structured progress (never free text, unless the student opts in) saves privately to the viewer's claude.ai account when the hub is published as an artifact with the `db` and `user` capabilities. Otherwise it is kept in browser localStorage, and a backup code is available as an extra copy.

## Privacy
No personal information is retained. Free text isn't stored by default, there are no outside requests (fonts are bundled), saved progress expires after 12 months without use, and students can delete everything. See `PRIVACY.md`.

## Editing
- `data/criteria.json` holds the learning aims and assessment criteria taken from the spec.
- `content/coach_*.json` holds the Distinction coaching and `content/exam_u*.json` the exam content.
- `src/hub.html` is the page template.
- Run `python3 tools/build.py` to rebuild `index.html` (the full page) and `dist/artifact.html` (the body only, for claude.ai artifacts).

## Keeping the spec current
The spec dates from 2022 and some of the bodies and laws it names have since changed. `data/currency.json` is the register: each entry has the spec wording, current status, current name, date of change, advice for assignments and exams, primary sources and the date it was last verified.

- `tools/build.py` **fails** if any content uses a replaced, renamed or repealed name without the current one. It warns on unverified entries, entries backed only by secondary sources, and entries not checked for over six months. `--strict` turns those warnings into failures.
- The hub shows the relevant updates on each unit's coaching page, on the exam overview, and in a full list on the Points tab.
- `docs/standards-verifier-substitutions.md` is generated from the register. It is the one-page list of substitutions for Standards Verifier sign-off: spec p.7 allows substitutions, subject to the Standards Verifier's confirmation.
- A scheduled re-check runs on 1 April and 1 November, ahead of the May/June and January exam series.

## Quality and audit
The hub was hardened against the Claude Education Skills Library. All 165 skills were triaged and 64 were used as audit lenses. The reports are in `docs/audit/`:
- `skills-triage.md` lists every skill and whether it was used.
- `assessment-quality.md` covers the MCQ keys, distractors and spec coverage (174 MCQs) and the walkthrough check questions.
- `learning-science.md` covers spacing, intake, calibration and walkthrough sequencing.
- `integrity-ai.md` covers authenticity, the JCQ AI guidance (April 2025 edition) and the own-work gate.
- `inclusion-language.md` covers the axe accessibility scan, readability, the glossary, sensitive content and representation.

`tools/build.py` checks every multiple-choice item for structure (4 options, a valid key, no duplicates) and flags cues: the key being the longest option, and answer-position bias.

Still needing a human: a subject-expert review of the content, your college's DSL contact on the help panel, the representation fixes listed in the inclusion report, and confirming the current JCQ AI guidance before each academic year.
