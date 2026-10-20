# Integrity and AI-era design audit

Scope: `src/hub.html` (read in full around `parallelPanel`, `walkthrough`, `dCard`, `renderCoach`, `exLong`), `content/coach_*.json` (207 sentence starters), `content/guide_*.json` (262 walkthrough requirements, 22 practice cases), `content/exam_u1-4.json` (28 long answers with model answers, 150 MCQ).
Method: static read and grep of the code and content. I did not run the page in a browser and I did not fact-check the health and social care subject content. Report only; no project files were changed.
Skills applied: ai-learning-boundary-mapper, metacognitive-monitoring-ai-contexts, explain-first-interrogator, ai-claim-checker, ai-hallucination-fact-check-protocol, source-credibility-evaluation-protocol, gap-analysis-from-student-work, single-point-rubric-designer, dilemma-navigation-for-education-design.

## 0. What the rules currently say (checked 20 October 2026)

| Point | Finding | Source |
|---|---|---|
| JCQ guidance version | "AI Use in Assessments: Your role in protecting the integrity of qualifications", effective 30 April 2025 (PDF label "Apr25"). The page shows no 2026 revision. Pearson's centre-staff guide tells staff to "review the JCQ 2026-27 guidance", but I could not find a published 2026-27 edition. Re-check jcq.org.uk before release. | jcq.org.uk page below |
| Acknowledging AI | Name the tool and the date generated ("ChatGPT" or "AI" alone is not acceptable). Keep a non-editable copy (for example a screenshot) of the prompts and output, add a short note on how it was used, and verify any content or sources. | JCQ |
| Misuse | Using AI without acknowledgement, or submitting work that is not the student's own. Examples include copying or paraphrasing AI output and using AI for analysis. Sanctions run from a warning to disqualification. | JCQ |
| Credit | Work that is not the student's own independent work will not be credited, even if AI is referenced. | JCQ; Pearson AI guidance |
| Pearson on BTEC | Learners must acknowledge AI use. AI-assisted work "will not be rewarded" because it does not show the learner independently met the criteria. Unacknowledged AI use is malpractice. Each assignment needs a signed learner declaration, and the assessor must not sign theirs if they have doubts. BTEC Centre Guide to Internal Assessment 2026-27 (v4.1, 21 Aug 2026) includes an example where a Distinction was reduced to Merit because reasoning relied on unacknowledged AI. | Pearson centre guides below |
| Feedback rule | Before launch, tutors may give feedback freely. During assessment, no formative feedback on specific evidence or criteria. After the decision, assessors may say what was achieved and why, but "you cannot tell the student what to do to improve their grade". A resubmission needs Lead IV authorisation and a judgement that the learner can improve "without further guidance". | Pearson centre guide; Quality Focus 6 (undated) |
| Caveat | Pearson's "AI guidance for centre staff" (v3, 03/07/2026) is scoped to work-based learning and other BTEC families, not the Nationals. I used it only as corroboration. The BTEC-specific documents are the two Pearson centre guides. I read all of these through page summaries; the JCQ PDF itself would not download. Check the exact wording against the originals before any student-facing quote. | |

## 1. Boundary map

Principle used (boundary mapper): the learning objective is the boundary. The hub is a self-study aid, so the question for each feature is whether it supports the student's own thinking or lets them lift someone else's. The hub has no AI feature of its own (the only `window.claude` use is `db` and `user` for saving progress). That is correct and should stay that way. Students can still open any AI tool beside it, so the hub should make allowed and disallowed use visible rather than assume it will be obeyed.

| Hub feature | Rating | Why | Boundary type |
|---|---|---|---|
| Distinction coach: `decode`, `mustInclude`, `pitfalls`, `stretch` (dCard) | Safe | Criterion-level explanation of what the verb asks for. No case content, no claims. It is the same kind of material as the spec's own guidance. | AI-neutral |
| Coach sentence starters (`starters`, 207) | At risk (low for most, high for 13, listed in section 2) | All are fragments with at least one blank, so none is paste-ready on its own. The risk is in (a) first-person frames that presuppose experience or results ("My results showed...", "My supervisor observed...") and (b) frames that carry a ready-made stance ("The hydrogen bonding in water is significant for metabolism because..."). Both invite invented evidence or a borrowed argument. | AI-undermining where they pre-commit a claim; neutral where they only signal structure |
| Walkthrough: practice case and `means` / `fromSpec` | Safe | Fictional case, clearly labelled. Spec-based. | AI-neutral |
| Walkthrough: strong `example` and `nearMiss` (262 each) | At risk (high for Units 6, 9, 13, 18 and 19-25) | Mean 34 words, maximum 49, of finished Distinction-quality analysis. Case names are easy to swap. In science and practical units the content is transferable to any similar brief (iodine-131, norovirus, enzyme rate, nutrition). Examples in the first person model fabricated evidence (see section 2). The README claim that the fictional case "never writes assignment text" and so "protects authenticity" is too strong. | AI-undermining (the argument is supplied, not built) |
| Walkthrough: A/B pick and check question | Safe | Recognition tasks with feedback. Sets no text to copy. Weakness is the order: the student sees the strong example before attempting anything (see section 4, change 4). | AI-neutral, but weak on learning |
| Walkthrough: "explain it in your own words" textarea | Safe, and the best feature | Generation task. This is the explain-first idea, but it comes after the answer is shown, so it can become paraphrase of the example. | AI-beneficial if moved earlier |
| Evidence map (step "Map", `gwloc`, `gwst`) | At risk | Self-reported "Yes / Partly / Not yet" can read as verification. There is no prompt about own work or AI use. The map ties a draft to specific D requirements, which is criterion-level feedback on specific evidence. A tutor may not give that during a live assessment, and after a decision it overlaps with "how to improve". Whether a student may use it at those stages is a centre decision the hub cannot see. | Depends on stage; AI-neutral for the tool itself |
| Planner milestones and "Resubmitting" status | At risk (low) | Milestone text tells students to "map your draft against every D requirement". Used after a decision, that is guidance on how to improve, which Pearson says assessors cannot give. | Policy risk, not content risk |
| Exam long answers: draft textarea | Safe | Exam practice. Externally assessed, so no authenticity declaration applies. | AI-neutral |
| Exam long answers: `model` answers (28, mean 106 to 238 words) | Safe for authenticity, at risk for learning | Units 1-4 are externally assessed, so copying a model has no coursework consequence. The risk is fluency illusion: reveal-and-read feels like learning. Some theory paragraphs (Bandura, Holmes-Rahe, Piaget) overlap with internal units 11, 12, 18 and 26, so a short warning is worthwhile. | AI-neutral for authenticity; undermining if read before attempting |
| MCQ quiz and daily retrieval, confidence rating, calibration panel | Safe | Retrieval with confidence-before-answer matches the monitoring skill's advice. Nothing to copy. | AI-beneficial |
| Points, grade tracker, calendar | Safe | Administrative. | Neutral |

Dilemma navigation applied (the genuine tension for this hub):
- Value A: access to Distinction-level scaffolding for students without private tutoring (equity, self-regulation).
- Value B: the learner's own, unaided thinking, which is what the qualification certifies.
- Compromise trap: stripping the examples to vague generalities. That helps nobody and still does not stop copying.
- Conflict zone: science and practical units, where a good example necessarily contains the content.
- Both/and: teach the move, not the sentence. Make students attempt first, show structure beside the example, and have a visible own-work declaration. Fade support as ticks accumulate.

Gap analysis of the hub against its own aim ("coaches and never writes assignment text"):
- Strength: fictional cases, explain-first textarea, confidence calibration, no AI feature.
- Conceptual gap: examples are finished prose, not annotated moves.
- Procedural gap: nothing gates the evidence map, there is no AI-use statement, and the stage rule is not reflected.
- Communication gap: the only integrity message is one paragraph on the case panel, and it never mentions how to acknowledge AI.
- First fix: the attempt-before-example gate (change 4) and the declaration gate (change 3).

## 2. Specific content risks (15)

Paths read as `file > unit > criterion > item`. Walkthrough items are `requirements[i]`; starters are `starters[i]`.

Ready-to-adapt examples (finished analysis, swap the names):
1. `guide_c > 21 > AB.D1 > requirements[1].example`: "Radioactive iodine works well for an overactive thyroid because thyroid cells take up iodine... Radiofrequency ablation heats a nodule with no ionising dose..." Case-free science that fits any thyroid or radiotherapy brief.
2. `guide_c > 21 > AB.D1 > requirements[2].example`: "Ionising radiation from iodine-131 can break bonds in DNA directly or make free radicals..." Same problem, 45 words.
3. `guide_a > 9 > B.D2 > requirements[0].example`: "Jo uses soap and running water rather than alcohol gel after dealing with vomit, because alcohol gel is less effective against norovirus..." Procedure and rationale fit any outbreak brief.
4. `guide_a > 9 > C.D3 > requirements[0].example`: "The exclusion rule keeps children with sickness at home for 48 hours... which cuts off the chain of infection. It only works if parents are told clearly..."
5. `guide_a > 9 > C.D3 > requirements[2].example`: "Routine hand washing and toy cleaning work on normal days, but an outbreak needs stricter measures such as enhanced cleaning and cohorting. COSHH requires..."
6. `guide_b > 18 > A.D1 > requirements[1].example`: "Piaget's stages are useful for expecting what Amara can do in play, but they underestimate what children can do with support, so I would not use them alone." A complete theory evaluation with a first-person judgement.
7. `guide_c > 19 > C.D3 > requirements[3].example`: "As a growing athlete, Ines needs enough iron, calcium and energy. If she doesn't get them, she may have tiredness, lower bone density..." Transferable nutrition analysis.
8. `guide_a > 5 > BC.D2 > requirements[0].example`: "Idris's request for secrecy clashes with the duty to keep him safe. The plan should say in plain words, in advance, when staff must share..." A full confidentiality-versus-safeguarding judgement that fits many Unit 5 and 7 briefs.

Examples that model invented first-person evidence (the most serious category for authenticity):
9. `guide_b > 13 > BC.D2 > requirements[1].example`: "When one plate was contaminated, I repeated the streak using flamed loops and recorded the change in my notebook." Practical-unit evidence must be the learner's own record. A student can paste this and claim a result they never had.
10. `guide_a > 9 > B.D2 > requirements[3].example` and `guide_a > 6 > C.D2 > requirements[4].example`: supervisor observation or feedback ("In week one the supervisor said Jo missed the thumbs and wrists..."; "Kit asked Mrs Adeyemi for feedback..."). Models fabricated third-party witness evidence.
11. `guide_a > 6 > D.D3 > requirements[0].example`: "The supervisor's statement shows a different weakness: Kit still rushes hygiene steps when busy." Same pattern for Unit 6 reflection.

Starters that pre-commit a stance or a finding:
12. `coach_c > 24 > B.D2 > starters[0]` "Above the optimum temperature, the rate fell because the active site..." and `coach_c > 24 > A.D1 > starters[2]` "My results showed..., which suggests that the structure of...". These presuppose results the student may not have.
13. `coach_b > 13 > BC.D2 > starters[1]` "My results support this choice because...", `coach_b > 18 > BC.D2 > starters[1]` "My observation showed..., which supports the use of...", `coach_b > 18 > BC.D3 > starters[1]` "My observations suggest that...". Same problem across Units 13 and 18.
14. `coach_a > 6 > C.D2 > starters[1]` "I took the initiative to... while following the setting's procedure for..." and `starters[2]` "My supervisor observed...". Invites a made-up placement.
15. `exam_u1 > long[0]` (id `u1l01`, Daniel, 238-word model on the stress-diathesis model). A strong, complete theory evaluation that overlaps with internal Units 11 and 12. Low risk for Unit 1 (exam) but worth a "do not reuse in coursework" label.

Also noted, lower priority: 17 of 207 starters have three blanks and are as long as 94 characters. Bare connectors ("Overall...", "On balance,...", "However...") are about 40 of the 207 and are harmless.

## 3. Student-facing wording

### 3a. Integrity notice for the walkthrough

> **These examples are practice, not text to use.**
> Each example is about a made-up case. It shows you how Distinction thinking works. It is not a model to copy, change a few words in, or ask an AI tool to rewrite for your brief.
> Your assessor can only give credit for what you show yourself. If you hand in sentences that came from these examples, or from an AI tool, as your own work, that counts as malpractice, even if you changed the names. The penalty can be a warning, a lost grade or losing the qualification.
> Do this instead: read the example, then cover it. Say the idea in your own words, out loud or on paper. Then write about your own brief, using your own facts, your own results and your own judgement.
> You will sign a declaration when you hand in that the work is yours.

Short banner (shown at the top of every open walkthrough):

> Practice case only. Learn the thinking, then write your own. Don't copy these examples, or anything an AI writes, into your assignment.

### 3b. AI-use note (BTEC coursework)

> **AI and your BTEC coursework**
> The rules come from JCQ, which sets the rules for coursework in UK awarding organisations, and from Pearson, who award your BTEC. Your centre can set stricter limits for each assignment, so check your brief and ask your tutor before you use any AI tool.
>
> **You must not:**
> - use AI to write, rewrite or paraphrase any part of your assignment
> - use AI to do the analysis, evaluation or judgements the Distinction criteria ask for
> - use AI to invent case details, results, observations, quotes or references
> - hand in any work, or any ideas, that you did not produce yourself
>
> Pearson will not give credit for work that doesn't show you met the criteria on your own. That is true even if you say where the work came from.
>
> **Only if your centre says it is allowed**, you might use an AI tool for things like explaining a word you don't understand, or suggesting what kinds of sources to look for. It must not be a way of getting your answer.
>
> **If you use AI at all, you must:**
> 1. name the tool and the date (for example "ChatGPT, 12 March 2027", not just "AI")
> 2. keep a screenshot of your prompt and the answer
> 3. say briefly in your work how you used it
> 4. check any fact, name or reference it gave you in a reliable source. AI tools make things up and can invent references that look real.
>
> Using AI without saying so is malpractice. The penalties run from a warning to being disqualified from the qualification.
>
> This hub doesn't write assignment text for you and has no AI feature. This note is a short summary. The full rules are in JCQ's "AI Use in Assessments" and your centre's policy.

### 3c. "My own work" self-declaration checklist (tick all before the evidence map opens)

> **Before you use the evidence map, tick each line that is true.**
> - [ ] I am checking a draft that I wrote myself.
> - [ ] The words in my draft are mine. I have not copied or adapted the hub's examples or sentence starters.
> - [ ] I have not used AI to write, rewrite or paraphrase my work, or to do my analysis, evaluation or judgements.
> - [ ] If I used an AI tool in a way my centre allows, I have named the tool and the date, kept a screenshot of my prompt and its answer, and said how I used it in my work.
> - [ ] Every case detail, result, observation and quote in my work is real. It comes from my brief, my own practical or placement, or a source I have referenced. I have not made anything up.
> - [ ] I have checked my facts against my class notes, the specification or another reliable source, not only against the hub or an AI tool.
> - [ ] I could explain any part of this work to my tutor, out loud, without notes.
> - [ ] I know that I will sign a declaration when I hand in, and that handing in work that isn't mine is malpractice.
>
> Ticking these boxes doesn't replace the declaration you sign with your centre. The map is your own check. It isn't marked, and it doesn't prove that your work is your own.

Optional single-point rubric for the map, replacing "Yes / Partly / Not yet" (three-column format; the student fills the outer columns with evidence, nothing is scored):

| Where my work is still thin | Criterion | Where my work shows this |
|---|---|---|
| (pointer and one line from my own draft) | The paragraph I point to makes a claim, reason or judgement about my own brief that I can explain out loud without notes. | (pointer and one line from my own draft) |

## 4. Concrete UI and content changes (10, prioritised)

All fit a single-file vanilla-JS page. `S` is the existing state object; `save()` persists it. Add new keys in `blank()` (for example `ack:false`, `decl:{}`, `pre:{}`) and make old saves default safely.

1. **Integrity gate on first walkthrough open.** In the `gwopen` handler, if `!S.ack`, render the 3a notice with an "I understand" button that sets `S.ack=true`. Replace the paragraph in `parallelPanel` with 3a, and put the short banner at the top of `walkthrough()`. Content: none.
2. **Stage guard from `S.status`.** The statuses `Drafting`, `Submitted`, `Resubmitting` and `Graded` already exist per unit. When opening the walkthrough or evidence map for a unit whose status is `Submitted`, `Resubmitting` or `Graded`, show a notice and require a tick. Suggested wording: "After an assessment decision your assessor can tell you what you achieved and why, but not how to improve (Pearson). A resubmission needs your Lead IV's approval and is only allowed if you can improve without further guidance. During a live assessment your tutor can't give feedback on your specific evidence. Only use this if your centre says you can." Reuse for `Planning` and `Drafting` with a softer line. Also reword the milestone "Map your draft against every D requirement" to add "(if your centre allows)".
3. **Gate the evidence map behind the 3c checklist.** In the `step===n` branch of `walkthrough()`, if `!S.decl[u+"|"+code]` render the checklist and a "Continue to my map" button enabled only when all boxes are ticked. Store the ticks. Reword the intro to "Nothing here is marked and nothing here proves your work is yours." Rename the statuses to "I think it shows this / Partly / Not yet" so they read as self-report.
4. **Attempt before example (explain-first).** In `walkthrough()`, show `need` and `means` first, then a short textarea `S.pre[k]`: "Before you see the examples: in one or two sentences, what would Distinction-level work have to show here?" Render the A/B pair only once it has at least 12 words (a `split(/\s+/).length` check). Keep the existing "explain in your own words" step after the pick, and change its prompt to "Now say what you got wrong or missed in your first attempt". This applies the explain-first and monitoring skills: the student meets their own understanding before the fluent example.
5. **Content edits to examples and starters.** (a) Add a `move` field per requirement (for example "event, then effect on the person, then why it matters") and show it beside the example. For Units 20 to 25 and the other items in section 2, rewrite the example in annotated or partly blanked form ("Radioactive iodine suits an overactive thyroid because ___ [cell behaviour] ...") or use the erroneous-example format. (b) Remove or rewrite starters 12 to 14 in section 2 so they ask a question instead of presupposing a result ("What did your own data show? State the number first."). (c) For any starter that matches `/\b(I|my|My)\b/`, render a small label "Only write this if it is true for you. Never invent results, observations or supervisor comments." (d) Rename the starter heading "Sentence starters" to "Structure only: you supply every claim".
6. **AI-use note in two places.** Add the 3b text in a `<details>` at the top of the Distinction coach and in the footer, and a link from the Today tab. Add one line to the walkthrough banner: "AI use must be acknowledged: tool, date, screenshot, short note."
7. **Exam model answers: attempt, self-mark, then model.** In `exLong()`, show the model only after the student has ticked at least one marking point and the draft is at least 40 words, behind a second button ("Compare with a model"). Add the label "Exam practice only. Don't reuse this wording in coursework." Add a prompt before the reveal: "Rewrite one weak sentence of yours, in your own words, before you read the model."
8. **Source-check prompts.** Add a one-line "Check it" control on each explanation card (`means`, `fromSpec`, theory summaries, exam `why` lines) with the wording in section 5. Show "Last checked" from `data/currency.json` (`lastFullCheck`) in the footer. Tick state goes in `S.srcchk`.
9. **Map columns that anchor to the student's own text.** Add an "evidence type" selector next to "Where in my work" (my own writing / my own practical results / placement log or witness statement / referenced source) and a one-line field "In my own words, what does it say?". Optionally use the single-point layout from section 3c. This makes the map a record of the student's own text and makes a blank or copied entry visible.
10. **Fix the claims and keep the guardrails.** Reword the README statement that the fictional case "protects authenticity" to "reduces copying but doesn't prevent it; the declaration, the checks and the centre's assessment practices do that". Keep the published artifact's capabilities at `db` and `user` only, and don't add any capability that lets the page ask Claude to generate text. Add the same limit to `description` on publish.

## 5. Sources and verification prompts

Does the content need them? Yes, in three tiers.

1. **Rules and names that change** (bodies, laws, boundaries): already handled well by `data/currency.json` (20 entries with sources and a `verified` date, plus a build check). Surface the "last checked" date to students, as in change 8.
2. **Subject claims** (science, nutrition, infection control, theories): the hub gives no sources for these. Students will read them as authoritative because they are fluent and tidy, which is the same trap as with an AI answer. I have not fact-checked them here. A teacher should review the exam content in particular, since wrong "facts" will be learned and not questioned.
3. **Examples**: the strong example is "good thinking", not a source. Label it as such.

Suggested prompt wording (UK English, plain), using the claim-check and source-credibility skills: three questions, one of which asks for a source that is not another AI and not the hub.

> **Check it before you rely on it.** This page is a study aid, not a source you can reference. Compare it with your class notes or the specification first.
> 1. Which one claim here would you check?
> 2. What would you look at to check it?
> 3. Which source would you use? Pick something reliable, such as your textbook, NHS, UKHSA, Social Work England or legislation.gov.uk, not another AI tool and not this hub.

Student-facing line for any AI tool they use alongside the hub (hallucination protocol, "reconstruct the source"):

> If an AI tool gives you a source, name, statistic or law, find the original yourself and check it says what the AI said. If you can't find it, don't use it. Never put a reference in your work that you haven't opened.

Source checks to add by unit family: units 5, 7, 8, 16 (legislation, codes of practice, bodies: legislation.gov.uk, the relevant regulator, current Pearson spec); units 9, 13, 21, 23, 24 (clinical or scientific claims: textbook, NHS, UKHSA); units 11, 12, 18, 26 (theories: class notes and the named theorist, since textbooks differ).

## 6. Sources used

- JCQ, AI Use in Assessments (April 2025 edition): https://jcq.org.uk/exams-office/malpractice/artificial-intelligence
- JCQ blog note on earlier changes (undated): https://www.jcq.org.uk/blog/changes-to-jcq-guidance-on-ai-in-assessment/
- Pearson, Artificial Intelligence (AI) Guidance (undated, general): https://qualifications.pearson.com/content/dam/pdf/Support/Quality%20Assurance/artificial-intelligence-guidance.pdf
- Pearson, BTEC Centre Guide to Internal Assessment 2026-2027, v4.1, 21 August 2026: https://qualifications.pearson.com/content/dam/pdf/Support/Quality%20Assurance/btec-centre-guide-to-internal-assessment.pdf
- Pearson, BTEC Centre Guide to Plagiarism 2026-2027, v4.0, 26 August 2026: https://qualifications.pearson.com/content/dam/pdf/Support/Quality%20Assurance/btec-centre-guide-to-plagiarism.pdf
- Pearson, Quality Focus 6: BTEC Internal Assessment (undated): https://qualifications.pearson.com/content/dam/pdf/Support/Quality%20Assurance/Quality%20Focus---BTEC-Internal-Assessment.pdf
- Pearson, What is Artificial Intelligence? Guidance for centre staff, v3, 3 July 2026 (work-based learning scope, corroboration only): https://qualifications.pearson.com/content/dam/pdf/Support/Work%20based%20learning/pearson-ai-centre-staff-guidance.pdf
- Pearson, Health and Social Care subject advisor update, February 2024 (points centres to the JCQ guidance): https://qualifications.pearson.com/en/news-policy/subject-updates/health-and-social-care/february-subject-advisors-update.html

Open items for a human: confirm whether JCQ has issued a 2026-27 edition; check the Pearson and JCQ quotations against the PDFs before they appear in the UI; agree with the centre what students may use at each stage (change 2); and have a subject specialist check the science and practice claims.
