# Assessment quality audit

## Lenses used
assessment-validity-checker, hinge-question-designer, retrieval-practice-generator, coverage-audit, panel-review (used as a multi-role read: validity, subject accuracy, learner, integrity), erroneous-example-designer, variation-theory-task-designer, pedagogical-content-knowledge-developer, feedback-quality-analyser, ai-feedback-design-principles, competency-unpacker.

## Summary counts
| Item | Count |
|---|---|
| MCQs reviewed (exam_u1 to u4) | 150 |
| MCQs with "why" rewritten to name the misconception | 148 |
| MCQs with options or stem changed (ambiguity, silly distractors, cues) | about 75 |
| New MCQs added (6 per unit) | 24 (u1q37-42, u2q37-42, u3q49-54, u4q31-36). Total now 174 |
| Walkthrough requirements in U14 and U15 rewritten or added | U14 10 to 20, U15 10 to 16 (all checks, nearMisses, whys redone) |
| Walkthrough checks fixed outside U14/U15 | 0 (audited by script only, see "Remaining issues") |
| Example/nearMiss pairs changed for integrity (first person, invented evidence, transferable text) | 55 requirements across guide_a/b/c |
| Long-answer notes | u1l01 model labelled exam-practice-only |

U3 ids start at u3q49 because u3q48 was the last existing id.

## Coverage (MCQ plus long questions against topics[].points)
Largest uncovered spec points before additions, now partly closed (closed items marked *):
- Unit 1: A1.2 centiles*, A1.6 hormones*, A3.3 disrupted attachment*, B2.2 susceptibility*, B4.3 bullying*, C1.6 dementia*. Still uncovered: A1.7, A1.10, A2.8 memory, A3.5/3.6 self-esteem factors, A4.2, A4.4, A4.5, B3.1 pollution, B5.3, B5.4, C1.1, C1.2, C2.3, C2.4.
- Unit 2: B2.2 needs assessment*, B3.3 complaints*, A5.5 criminal investigation*, B5.4 unions*, B1.3 private funding*, A3.6 COSHH*. Still uncovered: A1.2, A1.6, A1.7, A2.1, A2.5, A2.6, A3.5, A3.9, A4.2, A5.4, B1.1, B3.1, B3.4, B4.3, B4.6, B5.1, C1.1, C1.4, C2.2 to C2.4.
- Unit 3 (largest gap, about 60 of 150 points have no MCQ or long question): added A5.1*, B4.4*, B1.8/B8.2 ADH*, B3.7 asthma*, B11.9 teratogens*, B9.1 lymph*. Still uncovered: A1.1, A1.6, A1.7, A2.3, A2.5, A3.1 to A3.5, A4.1, A4.7, B1.1, B2.1, B2.4, B3.1, B3.3, B4.1, B4.3, B4.6, B5.1, B5.2, B6.1 to B6.3, B6.5, B6.9, B7.1, B8.1, B9.4, B10.1, B11.1 to B11.3, B11.5 to B11.8, C1.2, C1.3.
- Unit 4: A1.1 purposes*, B2.2 objectives*, B3.2 consent under 18*, B3.5 human rights*, B4.2 non-judgemental*, C3.1 future research*. Still uncovered: A1.2, A2.1 to A2.3, B1.1, B1.5, B1.6, B2.1, B2.4 to B2.7, B4.1, B4.3, B4.7, C1.1, C1.3, C2.1, C2.4, C3.2, C3.3.

## Notable fixes
| id | problem | fix |
|---|---|---|
| u1q06 | Two defensible answers: Jamal (4) also lacks abstract thinking | Stem asks which concept he has not grasped; distractors are things he has already acquired |
| u1q27, u2q15, u2q16, u2q05, u4q22 | Only the key was a believable chain; wrong options were absurd or negative | Distractors rewritten as plausible misconceptions of equal length |
| u1q24 | Three silly distractors (parallel play, menopause) | Distractors are enablers (misreading barrier as factor) |
| u1q12, u1q14, u1q22 | Distractor outside the construct (monotropy is not an attachment type) | Replaced with concept students really swap (deprivation, self-concept, genetic disorder) |
| u2q28 | CQC was an implausible regulator option | Replaced by Social Work England, the real near-miss for this profession |
| u2q35 | Question was only "inquiry = poor practice identified" | Now tests what changed (duty of candour) |
| u2q22 | Booking a GP appointment is not self-referral | Rewritten as direct self-referral to physiotherapy |
| u3q16 | "only", "never" absolutes cued the answer | Distractors now state positive-feedback and "negative = harmful" misconceptions |
| u3q15, u3q22, u3q32, u3q44 | Distractors from unrelated topics or non-terms | Replaced with plausible alternatives |
| u4q18, u4q20, u4q23, u4q24 | Key was 2 to 3 times longer than others | Option lengths balanced |
| u4q20 | Spec wording says "parents/carers"; law in England uses the Mental Capacity Act 2005 | Key and why refer to legal safeguards and consultee |
| Length cue, all units | Key was the longest option in 103 of 150 MCQs | After rebalancing, 25 remain flagged (1.25x), mostly short labels |
| U14 A.D1, BC.D2, D.D3 | Wrong options were throwaways ("Hollis is 52", "Use different font"); nearMisses were not Merit level | Distractors rebuilt around real misconceptions; nearMisses now apply the science to the case but omit the single critical feature |
| U14 | Aim D consent and confidentiality missing; carer strain, test limits, contingencies and concise conclusion missing | Added 10 requirements; parallel-case summary extended with carer and transport details |
| U15 | Method choice not tied to microbial biology; no ranking of causes; no societal attitudes; no future uses | Added 6 requirements (virus vs bacterium control contrast, ranking causes, burial practices, future uses) |
| guide_b 13, 14, 15, 17, 18; guide_a 6, 9; guide_c 21, 25 | First-person examples, invented results and supervisor comments | Rewritten in third person; invented evidence removed; transferable science tied to case details (21, 9, 19, 5) |

## Remaining issues needing a human subject expert
1. U4 spec names the National Social Care Research Ethics Committee. Its current status and name should be checked before exam use.
2. u4q33 and u4q20: the spec says consent from "parents/carers", but under-16 competence and the Mental Capacity Act 2005 mean the legal position is more nuanced. Confirm acceptable wording.
3. U14 clinical details (RA and CKD tests, eGFR repeat over three months, drug monitoring) and U15 (norovirus exclusion 48 hours, Legionella temperature) need a clinician or microbiologist check.
4. u3q49 to 54 and u2q42 are new and unreviewed by a subject specialist.
5. Walkthrough checks in units 5 to 13 and 16 to 26 (about 240) have the key as the longest option in 255 of 262 checks across all guides, one-sentence whys that do not name misconceptions, and many nearMisses under 70 characters (not Merit level). These were detected by script and not rewritten in this pass.
6. Remaining flags of dated or unverified names in guide_b 12 (Common Assessment Framework) produce a build warning; confirm the local early help wording with the tutor team.
7. Coach starters (not in my scope) that need changes, from integrity-ai.md items 12 to 14: coach_c 24 B.D2 starters[0] and A.D1 starters[2]; coach_b 13 BC.D2 starters[1], coach_b 18 BC.D2 starters[1] and BC.D3 starters[1]; coach_a 6 C.D2 starters[1] and [2]. They presuppose results or a placement the student may not have; use conditional wording ("If your results show...").

## Recommendations for UI or feature changes (not implemented)
1. Show a per-option explanation for guide checks and MCQs (data field such as whyEach), so a wrong pick gets feedback on that misconception rather than one shared sentence.
2. Shuffle MCQ options at quiz time (the order is fixed, so key position is learnable) or at least store a randomised order.
3. Update README and any hard-coded "150 multiple-choice questions" to the live count (174).
4. Add a build lint for MCQs: key longest by more than 25%, duplicated options, and walkthrough examples containing first-person pronouns.
5. Add a "similar questions" tag on topics so the daily quiz can prioritise uncovered spec points (see the coverage list).
6. Add an "exam practice only" flag on long-answer models so the hub can hide them from coursework tools.
