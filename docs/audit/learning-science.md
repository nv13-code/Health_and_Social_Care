# Learning-science audit of the student hub

Scope: `src/hub.html` (functions `buildDaily`, `srsAnswer`, `interleave`, `weakFirst`, `finishDaily`, `renderToday`, `weekTasks`, `milestones`, `clashes`, `buildPlan`, `exQuiz`/`startQuiz`/`quizRound`, `exLong`, `walkthrough`, `renderCoach`) and `content/*.json`. Audited against the 26 skills listed in the brief. Report only: no project files were changed.

State is the single object `S` (localStorage key `hsc-dstar-v1`, optionally synced). Note that `S.cal` is already the assessment calendar and `S.calib` is the calibration tally, so new keys below avoid those names.

## 1. Headline findings

1. The retrieval core is sound: one question at a time, confidence before options, immediate explanation, wrong answers back tomorrow, units mixed. No skill is fully met, but about a third are partly met.
2. The scheduler has three integrity faults that make its memory-strength numbers flatter students:
   - A requeued wrong answer is scored a second time (`danswer` pushes the id again and calls `srsAnswer` again). A question missed then answered correctly minutes later jumps from box 1 to box 2 and is next due in 3 days. The second answer also feeds the calibration tally, where it is almost always "Certain and right" because the student has just seen the answer.
   - Confidence is collected but never changes the schedule. The copy says "Right, but you were guessing. It'll come back soon to check", but `srsAnswer` promotes a guessed-right answer exactly like a certain-right one.
   - "Six more questions" (`dailyextra`) sorts by due date, so it serves unseen and not-yet-due items first, and early correct answers are promoted as if they were due.
3. Capacity does not add up. 150 questions at five correct reviews each is about 900 answers. The cap of 12 a day cannot deliver that before an exam. I simulated the current `buildDaily` rule (80 to 85% accuracy, every day of the week): only 63 to 75 of the 150 questions have been seen by day 30, and 97 to 145 by day 90. The "at least 4 new" floor in the code is dead: `room=min(cap-pick.length, max(4, cap-due.length))` is 0 whenever 12 or more items are due.
4. Exam dates are collected (`S.dates`) but `buildDaily` ignores them. The 30-day top box can push a question past the exam.
5. The walkthrough is a fixed four-part scaffold for all 262 requirements. It never fades, never checks the student without the example in view, and shows the reason the near-miss is weaker (`whyNearMiss`) before the student has explained anything.
6. There is no weekly review, no planning or reflection wrapper, no error diagnosis, no hint ladder, and no visuals.

## 2. Skill-by-skill audit

Verdict key: met / partly / not met.

### Memory and spacing

**spaced-practice-scheduler: partly.**
Requires: expanding intervals (1-3 days, 1-2 weeks, 3-4 weeks); review by retrieval not re-reading; difficulty weighting; every topic retrieved in the 5 days before the assessment; nothing goes more than 3 weeks unretrieved; intervals tied to the assessment date.
Evidence: `BOX_DAYS=[0,1,3,7,14,30]` expands and every review is a retrieval (met). `weakFirst` weights only new items, not due ones. `buildDaily` never reads `S.dates`, so there is no pre-exam pass and box 5 (30 days) breaks the 3-week rule. `buildPlan` makes a separate topic-level three-pass plan that does not talk to the question scheduler.

**individual-spacing-algorithm-explainer: partly.**
Requires: per-item, performance-driven intervals; interval about 10-20% of the retention horizon; prioritise by forgetting risk; plain-English explanation of the rules.
Evidence: per-item `{box,due,seen}` with demote-on-miss is a fair, explainable Leitner (met). No lapse count, no confidence input, no horizon, and due items are ordered by date only. The "Memory strength" panel and the Done screen do explain the rule in plain words, but "Box 3" is jargon for 16 to 18 year olds. Half-life regression is not worth building at this data size; lapses plus confidence is enough.

**interleaving-unit-planner: partly.**
Requires: interleave related but distinct concepts; teach each topic before interleaving; start with 2 topics and add; practice that forces choosing which idea applies; tell students why it feels harder.
Evidence: `interleave()` round-robins by unit only. Units 1 to 4 are unrelated subjects, so the discrimination benefit is small, and two questions from the same topic can still sit side by side. New items are tested cold with no teach-first block. No "which one applies" items and no explanation of why mixed practice feels harder.

**cognitive-load-analyser: partly.**
Requires: separate intrinsic from extraneous load; remove split attention and redundancy; check expertise reversal.
Evidence: good: one question per screen, feedback in place, no decoration. Extraneous load: Today shows six panels at once (quiz, calibration, boxes, clashes, tasks, cap selector). A walkthrough step shows need, means, spec wording, a pair, a textarea, a check and a mapping form together. The practice-case summary sits in a separate panel (`parallelPanel`) while each example refers to Rosa or Idris by name. No expertise-reversal mechanism (see fading).

**elaborative-interrogation-generator: partly.**
Requires: "why" prompts the student must generate an answer to, causal links, answerable from prior knowledge.
Evidence: the walkthrough `explainPrompt` is a generated "why" for each requirement (met in form). Daily MCQs only show a supplied `why` after answering; 11 of 150 stems ask why and 8 are scenarios, so most items are plain recall. No generation prompt for questions that keep failing.

**dual-coding-designer: not met.**
Requires: visuals that add information, labels on the diagram, no decoration, colour that carries meaning.
Evidence: the page has no `<svg>` or image. `diagramsToLearn` (Unit 3) is a text list. Life-stage sequences, theory comparisons and body-system diagrams are all prose.

### Worked examples and transfer

**worked-example-fading-designer: partly.**
Requires: a full annotated example, then completion problems fading backwards, then independent problems.
Evidence: each requirement has an annotated strong example and a near-miss with a reason (met for the first stage and a good contrast design). There are no completion problems and no fading; every requirement gets the same scaffold.

**digital-worked-example-sequence: partly.**
Requires: reveal one step at a time; a self-explanation prompt at each step; immediate targeted feedback on faded steps; no split attention.
Evidence: self-explanation textarea at every requirement (met in form but optional, any text accepted). Feedback on pick and check is immediate. All four sub-tasks are visible at once, and there are no faded steps.

**worked-example-to-problem-solving-transition-designer: not met.**
Requires: a gradient from example to problem, performance-triggered fading, expertise-reversal checkpoints, designed independent practice.
Evidence: the walkthrough and the exam long answers are not connected. Nothing is triggered by performance. The long answers (`exLong`) are good independent practice but are not designed as the end of a fade.

**self-explanation-prompt-designer: partly.**
Requires: prompts that elicit explanation not description, placed at dense points, requiring generation, answerable, with quality indicators and a follow-up for shallow answers.
Evidence: 262 requirement-specific prompts (met). Order is the fault: the pick feedback prints "The weaker one falls short because {whyNearMiss}" before the student explains, so the prompt can be answered by copying. No minimum, no shallow-answer follow-up, no sentence frame for stuck students.

**formative-assessment-loop-designer: partly.**
Requires: each response changes the next instructional move; assess thinking, not only answers; multiple elicitation methods; tight loop.
Evidence: tight loop and two elicitation methods (answer plus confidence). Responses change only one thing: wrong means tomorrow. Distractors are not mapped to misconceptions (one `why` per question and per walkthrough check). Confidence and error type do not change what comes next.

**adaptive-hint-sequence-designer: not met.**
Requires: graduated hints triggered by attempts, bottom-out hint with a self-explanation.
Evidence: no hints anywhere. The extended-answer "Reveal marking guide" is all-or-nothing (a bottom-out with no ladder), though it is hidden until after writing.

**transfer-bridge: not met.**
Requires: near and far transfer challenges; same / different / principle questions.
Evidence: one made-up case per unit. Step 4 ("where does your draft show this") is a one-way, self-reported link to the student's own work. No second case and no principle-naming.

### Student-learning gates

**confidence-calibration-check: partly.**
Requires: a rating before the attempt and again after feedback; name the pattern (over, under, well calibrated); a micro-goal; track over time.
Evidence: a 3-level rating before options (met, and the right cost for a 4-option MCQ). Two feedback messages (guessing-right, certain-wrong). A cumulative panel with no counts, no window, no per-topic view and no "Fairly sure" message. No post-feedback rating (acceptable to skip) and no micro-goal. Requeued answers contaminate the tally and confidence does not change scheduling.

**retrieve-first-gate: partly.**
Requires: a free-recall attempt before any explanation; compare recall with the model; work only on the gaps.
Evidence: met for the extended answers (write, then reveal marking points, then tick). Not met for the daily quiz (recognition only), the topic checklists (RAG rating with the answer list in view, which invites the illusion of competence) or the walkthrough (examples shown before the student produces anything).

**srl-session-wrapper: not met.**
Requires: a specific goal at the start, a mid-session check, a short reflection at the end.
Evidence: only the "Done for today" score screen and a streak counter.

**weekly-agency-review: not met.**
Requires: show the week's evidence, student interprets first, then sets a strategy (how, not what) goal.
Evidence: `weekTasks` is a to-do list of dates and two practice tasks. It reports nothing about how the student studied and sets no goal.

**fading-manager: not met.**
Requires: visible scaffold levels, performance criteria for removing support, periodic fully unassisted probes, transparent restoration.
Evidence: none in the walkthrough or the quiz.

**unassisted-evidence-checkpoint: partly.**
Requires: a check with no help, recorded separately, after scaffolded practice.
Evidence: the daily quiz and the long answers are unassisted by nature (no AI, no hints) but are not tagged as such. The walkthrough's evidence map is self-reported with every scaffold on screen. There is no unassisted checkpoint before it.

**stuck-and-error-diagnosis-coach: not met.**
Requires: the learner diagnoses the error (concept, slip, strategy, representation) before help.
Evidence: wrong answers get the correct letter plus `why`. Nothing asks the student why they missed it.

**progressive-hint-ladder: not met.**
Requires: six graduated hint levels with reflection between levels.
Evidence: none. A cheap, content-free version (a three-rung sentence-frame ladder) is in change 4.

### Self-regulated learning

**metacognitive-prompt-library: partly.**
Requires: task-specific planning, monitoring and evaluating prompts, at least two aimed at the illusion of knowing.
Evidence: monitoring is covered (confidence before options, calibration panel, self-marking). Planning and end-of-session evaluating are absent. The only illusion-of-knowing prompt is the calibration text.

**study-strategy-selector: not met.**
Requires: recommend high-utility strategies, name the ineffective ones students favour, with implementation detail and pitfalls.
Evidence: the design enforces retrieval and spacing but never explains why, never says re-reading notes feels productive but is weaker, and never warns that spacing and mixing feel harder than they are.

**goal-setting-protocol-designer: not met.**
Requires: specific, proximal, process goals the student chooses, with monitoring points.
Evidence: tasks are assigned from the calendar. The student sets no goal.

**error-analysis-protocol: not met.**
Requires: classify each error (conceptual / procedural / careless), match response to type.
Evidence: "Ones I got wrong" in `startQuiz` lists misses but classifies nothing.

**implementation-intention-designer: not met.**
Requires: a self-authored if-then plan, an obstacle plan, simple monitoring.
Evidence: the .ics daily 5pm reminder is a generic external cue (and the README says it is unavailable inside Claude). The streak resets after one missed day, which is the opposite of a coping plan.

## 3. Explicit assessments

**Leitner versus an expanding schedule tied to the exam date.** Keep the Leitner boxes: `[1,3,7,14,30]` is already an expanding schedule and is easy to explain. The fault is that it knows nothing about the exam. Cepeda et al. put the best gap at about 10 to 20% of the time until the test, so with 60 days to go the longest sensible gap is about 9 days, not 30, and the last pass must land in the final 3 days. Change 3 caps each interval at `round(0.15 x days to exam)` and adds a final pass. The 30-day box is kept only for maintenance after the exam or when the exam is more than 200 days away.

**Daily cap and new-item rate.** Not sensible as built. Twelve a day is a good session length (a question with confidence rating and feedback takes about 45 to 60 seconds), but the bank needs about 900 answers, so the cap cannot be both 12 and a full course of reviews. The new-item rule also starves: new items fall to 0 whenever 12 or more reviews are due, and weak-topic ordering means green topics may never appear. Changes 1 and 2 fix scoring first, then set cap 15, a reserved 3 to 5 new items a day, an exam-linked intake rate, a backlog rule and a catch-up day.

**Retrieve-first free recall.** Yes, but where it is cheap. Do not turn every MCQ into free recall (time, and typing on a phone). Add a "think first" step to proven items (change 7) and a two-minute brain dump before a student can rate a topic red, amber or green (change 11). The extended answers already do this and should be left alone.

**Calibration: running summary or per-item.** Both, with different jobs. Per-item rating before the options is the right low-friction capture and should stay at three levels. The headline should be a rolling 7-day summary with counts and the topics where the student was certain and wrong (change 5), because an all-time tally hides change and shows 100% after one answer. Add a rule that certain-and-wrong resets the item to box 0 (change 1).

**Weekly review ritual.** Add it (change 10). Three minutes, student reads the data first, picks a pattern, and sets one process goal with an if-then plan. Next week the goal is checked first.

**Fading the walkthrough.** Add four visible levels driven by first-try results (change 14). The hub has no AI and no hint engine, so the levels reuse the existing content fields (`need`, `means`, `fromSpec`, `example`, `nearMiss`, `explainPrompt`, `check`) and add no new content.

**Unassisted check before the evidence map.** Add a "cold rewrite" for each requirement (change 9): the examples are hidden, the student rewrites the weaker practice-case sentence to Distinction level, then compares. The evidence map gets a column for it. It uses the practice case only, so the hub still never touches assignment text.

## 4. Prioritised changes (maximum 15, ranked by impact divided by effort)

All fit a single-file vanilla-JS page whose state is `S`. Effort is a rough estimate for one developer who knows the file.

### 1. Make scoring honest: first attempt only, confidence-aware, no early promotion
Skills: individual-spacing-algorithm-explainer, confidence-calibration-check, formative-assessment-loop-designer, spaced-practice-scheduler.
Effort: about 1 to 2 hours (edits to `srsAnswer`, the `danswer` and `dailyextra` cases, the sort in `buildDaily`).
Behaviour:
- Only the first answer to a question each day changes `S.srs`, `S.quiz` and `S.calib`. The requeued repeat is practice: no box, due date or calibration change, and it is left out of the "Done for today x/y" count.
- Scoring table (box capped 0 to 5):

| Answer | Confidence | New box | Next due |
|---|---|---|---|
| Right | Fairly sure or Certain | box + 1 | `BOX_DAYS[box]` days (change 3 may shorten) |
| Right | Guessing | unchanged (minimum 1) | 2 days |
| Wrong | Guessing or Fairly sure | 1 | tomorrow |
| Wrong | Certain | 0 | tomorrow |

- Early review (item not yet due, from "more questions"): a correct answer changes nothing; a wrong answer follows the table.
- Count lapses: `lapses += 1` on every wrong first attempt.
- Fix the sort: due ascending, then box ascending, then certain-wrong first (the current comparator returns -1 or a box difference and never 1).
- Copy: guessed-right becomes "Right, but you were guessing, so it comes back in 2 days." Certain-wrong becomes "You were certain, and it's wrong. Those are the ones worth fixing. It's back tomorrow."
Data: `S.srs[id] = {box, due, seen, lapses, lastConf}` (adds `lapses`, `lastConf`; existing records still work with `lapses||0`). `S.daily.rq` for repeat results.
Fits: yes. No migration.

### 2. Fix intake and capacity: reserved new slots, backlog rule, live units only
Skills: spaced-practice-scheduler, individual-spacing-algorithm-explainer, cognitive-load-analyser.
Effort: about 2 hours (`buildDaily`, the cap selector, the Done screen).
Behaviour:
- Default cap 15 (selector 10 / 15 / 20 / 25), label "about 12 to 15 minutes". Existing values of 8, 12 and 16 are kept if already chosen.
- New slots = `clamp(round(cap x 0.25), 3, 5)` while unseen items remain in a live unit. Review slots = cap minus new slots. If fewer reviews are due than slots, the spare slots go to new items (up to 8 in total).
- Overflow: if more reviews are due than slots, take certain-wrong first, then box 0 to 1, then red or amber topics, then oldest due. The rest simply carry over. Nothing is lost or penalised.
- Catch-up day: if due is more than 2 x cap (for example after a week off), today has 0 new and the cap becomes 20 once. Banner: "A few extra today because you were away. No new questions until you're caught up."
- Live units: units whose exam date is within 150 days, or with no date set. Items from other units are not introduced yet.
- Replace "Six more questions" with "Four more new questions" (unseen items from live units only). Remove it when none remain.
- Keep the weak-first ordering for new items but guarantee every topic gets one item in the first pass: take one unseen item per topic (red and amber first) before taking a second from any topic.
Data: `S.dailyCap` (existing), `S.dates` (existing). Nothing new.
Fits: yes.
Evidence for the numbers: simulated 150 items, 80 to 85% accuracy: current rule gives 63 to 75 seen by day 30; with a reserved floor the bank is introduced by about day 60 only if the review cap rises too (a floor of 4 with cap 12 builds a backlog of about 68 due items, so the cap increase is required).

### 3. Tie spacing to the exam date
Skills: spaced-practice-scheduler, individual-spacing-algorithm-explainer.
Effort: about 1 to 2 hours (a small helper called from `srsAnswer`, one line in `buildDaily`).
Behaviour: for a question in unit `u` with exam date `X` and `D = days from today to X`:
- `interval = min(BOX_DAYS[box], max(1, round(0.15 x D)))`. Examples: D=90 gives 14, D=60 gives 9, D=40 gives 6, D=21 gives 3, D<=10 gives 1 to 2.
- Final pass: any due date later than `X - 3` is moved to `X - 3`; if that is already past, it is due today.
- Final 7 days: no new items for that unit. The session is reviews only, ordered box ascending then lapses descending.
- No date set: keep the plain box schedule and show "Add your exam date in the Planner so your reviews finish before the exam." once, as a note under the quiz.
- After the exam date: unit moves to maintenance (original intervals, new slots 0 for that unit).
- Optional: the Planner weekly rows show "N questions due" next to each topic.
Data: `S.dates[u]` (exists).
Fits: yes.

### 4. Self-explain before the reveal, and show one walkthrough sub-task at a time
Skills: self-explanation-prompt-designer, digital-worked-example-sequence, cognitive-load-analyser, progressive-hint-ladder (simplified).
Effort: about 3 hours (`walkthrough` render and its click cases).
Behaviour for each requirement:
- Top of the step shows only "what the work must show" (`need`). `means` and `fromSpec` go behind "Show what this means" and "Show the spec wording".
- Sub-tasks appear one at a time, in this order: pick the stronger sentence, then explain, then check, then your own work. Earlier ones stay visible, collapsed to one line.
- After the pick, show only "Yes, that's the stronger one." or "Look again: this one is the stronger." Do not show `whyNearMiss` yet.
- Explain box: "In your own words, why is this one stronger?" The Save button stays disabled until at least 12 words.
- "I'm stuck" ladder, one rung per press:
  1. "Look at what the weaker one leaves out."
  2. "Try: The stronger one works because it links ___ to ___, so ___."
  3. Reveal `whyNearMiss` (counts as a bottom-out).
- After saving, reveal `whyNearMiss` with the prompt "Does your explanation say the same thing? Yes / Partly / No." Then the hinge check.
- A collapsed "Remind me of the case" line at the top of each step shows `parallelCase.title` and the first sentence, so the case is not on another part of the page.
Data: per step `S.guide[k]` gets `expOk` ('yes' | 'part' | 'no'), `stuck` (0 to 3), `pickFirst` (the first pick), `chkFirst` (the first check answer). Existing `pick`, `exp`, `chk`, `loc`, `st` unchanged.
Fits: yes.

### 5. Replace the all-time calibration tally with a rolling 7-day summary and a topic watch-list
Skills: confidence-calibration-check, metacognitive-prompt-library.
Effort: about 2 hours (log write in `srsAnswer`, the panel in `renderToday`).
Behaviour:
- Keep the 3-level rating before the options.
- Panel shows the last 7 days with counts: "Certain: 15 of 18 right (83%)", "Fairly sure: 10 of 16 (63%)", "Guessing: 3 of 8 (38%)". Show a percentage only when n is at least 5; otherwise "needs 5 answers".
- One line of interpretation using the gap between Certain and Guessing accuracy. Over 40 points: "Your confidence is a good guide." Under 20: "Feeling sure isn't telling you much yet. Slow down on the ones you feel certain about." Chance on a four-option question is 25%, so guessing at 25 to 45% is normal and should be said.
- Add a "Fairly sure" message (currently none).
- "Certain and wrong this week: A2, B1 (open)". Those topics get priority 0 in `weakFirst` for 7 days.
- Copy for a certain-wrong answer stays; add "Say the right answer back in your own words before you tap Next" (a prompt only, nothing to type).
Data: `S.log` ring buffer of the last 300 first attempts as `[isoDate, id, topic, conf, ok]` (about 10 KB). Do not call it `S.cal`.
Fits: yes.

### 6. Self-authored if-then cue, a "days this week" target and a restart rule
Skills: implementation-intention-designer, goal-setting-protocol-designer, srl-session-wrapper.
Effort: about 1.5 hours (a card on Today, `finishDaily`, the streak label).
Behaviour:
- First visit, and editable later: "When will you do your quiz? If it's [after tea / on the bus / at lunch / before bed / other] then I'll open this page and do it before anything else." Second line: "If I miss a day, then I'll [do 5 questions tomorrow / do the next one as normal]." Default 5 questions.
- Weekly target picker: 3, 4 or 5 days (default 4). Replace "N-day streak" with "Days this week: 3 of 4". A missed day no longer wipes progress.
- Restart rule: after 3 or more days away, the next session is capped at 8 with no new items and says "Welcome back. A short one today."
- Close line on the Done screen, one tap: "How did that feel? Too easy / About right / Hard", used to suggest raising or lowering the cap by 4 after three days with the same answer.
- Count a day as done when at least 5 first attempts are answered (the current rule needs all 12, so stopping early earns nothing).
Data: `S.plan = {cue, when, miss, target}`; `S.daysDone = [isoDate, ...]` (last 28). `S.streak` and `S.lastDone` stay but are no longer shown.
Fits: yes.

### 7. "Think first" before the options on proven items
Skills: retrieve-first-gate, elaborative-interrogation-generator.
Effort: about 2 hours (`renderToday` states, one click case).
Behaviour:
- For items already at box 2 or higher, up to 4 per session, show the stem and "What's your answer? Say it to yourself, or type a few words." with a "Show the options" button. Confidence rating follows, then the options (current order otherwise).
- After the answer, if the student typed something, show it next to the correct option and ask "Did your answer match? Yes / Partly / No".
- If MCQ right but self-check is No, score it as right-but-guessing (change 1 table).
- Cost: about 10 seconds an item, so 40 seconds in a 15-question session.
Data: `S.daily.rc = {id: {txt, match}}` (today only). Nothing persistent beyond the `lastConf` change in change 1.
Fits: yes.

### 8. "Why did you miss it?" chip after a wrong answer
Skills: stuck-and-error-diagnosis-coach, error-analysis-protocol.
Effort: about 1 hour.
Behaviour: after a wrong first attempt, under the explanation, show four chips: "I didn't know it", "I mixed it up with something else", "I misread it", "Careless slip". One tap, optional.
- Didn't know: normal scoring.
- Mixed up: show "Which two ideas did you mix up?" with a one-line text field, stored for the weekly review.
- Misread or careless slip: box is lowered by 1 (minimum 1) instead of reset to 1, and the weekly review counts them: "5 of your 9 misses were slips. Read the stem twice."
Data: add `err` to the `S.log` entry (index 5) and `S.srs[id].err`.
Fits: yes.

### 9. Cold rewrite before the evidence map (unassisted checkpoint)
Skills: unassisted-evidence-checkpoint, transfer-bridge (near), retrieve-first-gate.
Effort: about 3 hours.
Behaviour: split step "4 · Now your own work".
- 4a, "Without the examples": the pair, the explain box and the means are collapsed and a banner says "No help for this one." Show the weaker (near-miss) sentence and ask "Rewrite it so it reaches Distinction, for the practice case." Minimum 12 words.
- 4b: reveal the strong example. "Does your sentence do what this asks: {need}? Yes / Partly / No."
- 4c: the existing "Where in my draft" box and status.
- Evidence map gets a column "Without the example" (Yes / Partly / No / not tried). If the student marks a row Yes but the cold column is No or not tried, show a quiet amber note: "You haven't shown this without the example yet."
- Not blocking.
- `weekTasks` adds, each Monday, "Redo the cold rewrite for two requirements you marked Yes" (picks two with the oldest cold date, minimum 7 days old).
- Integrity: practice case only. Never ask for assignment text.
Data: `S.guide[k].cold = {txt, self, t}`.
Fits: yes.

### 10. Weekly review ritual (three minutes)
Skills: weekly-agency-review, srl-session-wrapper, goal-setting-protocol-designer, implementation-intention-designer.
Effort: about 3 hours (a card at the top of Today, a new small render).
Behaviour: shown from Friday to Monday if `S.weekly[weekStart]` is empty; dismiss-able once.
1. Data row from `S.log`, `S.daysDone`, `S.tasksDone`, `S.srs`: days studied versus target, questions answered, first-try right %, certain-and-wrong count, tasks done x of y, items that reached Secure.
2. "What stands out? Pick one": I skipped days / I'm sure and wrong a lot / the same topics keep coming back / slips and misreads / other (type). The hub shows one line of its own reading only after the student picks.
3. "One way you'll study differently next week" (menu of process goals): "Use the think-first step on every question"; "Do a 2-minute brain dump before rating a topic"; "Write one extended answer before looking at the marking points"; "Redo the cold rewrite for two requirements"; "Redo my certain-and-wrong topics first". Plus the if-then box: "If ___, then I will ___."
4. Next week, the goal is the first thing shown: "Last week you said: ... Did you? Yes / Partly / No."
Data: `S.weekly = {[weekStartISO]: {pattern, goal, ifthen, done, t}}`.
Fits: yes.

### 11. Brain dump before a topic can be rated
Skills: retrieve-first-gate, study-strategy-selector, metacognitive-prompt-library.
Effort: about 3 hours (`exTopics` render and `weakness()`).
Behaviour: the topic panel starts with "Brain dump, 2 minutes: write everything you remember about {title}. No notes."
- Save, then reveal the topic's points as checkboxes: Had it / Partly / Missed.
- Suggest a rating: 70% or more had = Green, 40 to 69% = Amber, under 40% = Red. Student confirms or overrides.
- If a topic is rated without a brain dump in the last 14 days, show "Tip: rating from the list alone usually overestimates. Try the brain dump."
- `weakness()` uses the latest brain-dump hit rate when it is newer than the manual rating.
- First-time note (one line): "Re-reading your notes feels easier but it works less well than this."
Data: `S.dump = {"u|topicId": {t, txt, hits: [pointIndex...], n}}`.
Fits: yes.

### 12. Shuffle options and flag items that keep failing
Skills: formative-assessment-loop-designer, elaborative-interrogation-generator, error-analysis-protocol.
Effort: about 1.5 hours plus a content pass.
Behaviour:
- Display options in an order seeded by `hash(id + seen)` so the answer letter changes on repeat (the stored `answer` index is mapped, not changed). This stops students remembering "it was C".
- Content check: in the 150 items the correct option is longer than the average distractor in 81% of cases, which is a cue unrelated to knowledge. Add a warning to `tools/build.py` when more than 55% of a unit's correct options are the longest, then rebalance those distractors.
- Leech rule: at 3 lapses, the next appearance says "This one keeps slipping. Write one sentence on why the right answer is right." (minimum 8 words) before the options. Then the item resets to box 1, due tomorrow, and the next two successes use half intervals.
- Content backlog (not code): only 11 of 150 stems ask why and 8 are scenarios; aim for at least 30 scenario items across Units 1 to 4.
Data: `S.srs[id].lapses` (change 1), `S.srs[id].leech`.
Fits: yes (content work is separate).

### 13. Topic-level interleaving with a teach-first block
Skills: interleaving-unit-planner.
Effort: about 1 hour (`interleave`, one note on Today).
Behaviour:
- Round-robin by topic, then by unit, so no two neighbouring questions share a topic where avoidable.
- Teach-first: an item's first exposure in a topic is asked in a block of up to 2 from that topic; after its first correct answer it joins the mixed rotation.
- Optional content tag `confuse:[ids]` on the pairs students mix up (for example Unit 1 theories, Unit 2 laws and principles). When both are due, place them next to each other under the label "Which one applies?".
- One-time line: "Mixed questions feel harder than doing one topic at a time. That's the point: you learn to tell similar ideas apart."
Data: none required; `confuse` is optional content.
Fits: yes.

### 14. Fade the walkthrough scaffolds, with visible levels
Skills: fading-manager, worked-example-fading-designer, worked-example-to-problem-solving-transition-designer, unassisted-evidence-checkpoint.
Effort: about 5 to 6 hours (builds on changes 4 and 9).
Behaviour: one level per unit, shown on the walkthrough header ("Support level 3 of 3 for Unit 5").
- A step counts as a first-try success when the first pick is right, the first check is right and `expOk` is not No.
- Level 3 (full): everything in changes 4 and 9, including the sentence-frame ladder.
- Level 2: after 3 successes in a row. `means`, `fromSpec` and the frame ladder are removed (the student can still open the spec wording). The cold rewrite is offered.
- Level 1: after 3 more in a row. Pick and check are skipped; the student starts with the cold rewrite from the near-miss, then compares.
- Level 0: after 2 more in a row. Student sees only `need`, writes their own Distinction sentence for the practice case, then compares with the example, then maps.
- Every fifth step at any level below 3 is an unassisted probe (Level 0 behaviour).
- Restore: two failed steps in a row move one level back, with "That was a big step. I've put some help back for the next two."
- Announce every change: "You've got three in a row without help, so the explanations are now hidden by default."
- At most one level change a day.
Data: `S.gw = {lvl: {unit: 3|2|1|0}, hist: {unit: [0/1 ...last 6]}, moved: {unit: isoDate}}`. Existing `S.gwOpen`, `S.gwStep` are unaffected.
Fits: yes. This is the largest change, so it comes after 4 and 9.

### 15. Add visuals for the highest-value structures (low priority)
Skills: dual-coding-designer, cognitive-load-analyser.
Effort: about 1 to 2 days (SVG authoring dominates).
Behaviour:
- Unit 3: blank labelled diagrams (inline SVG with numbered pins) for the entries in `diagramsToLearn`. The student writes the labels from memory, then reveals them, then self-marks. Labels sit on the diagram, with no separate key.
- Unit 1: one life-stage timeline with growth and development markers.
- Units 1 and 2: a two-column compare/contrast grid for each pair of theories.
- No decoration. Colour only for meaning, and always with a text label.
Data: `S.diag = {id: {t, hit, n}}`. Content: new `diagrams` arrays in `exam_u*.json` with the SVG as a string.
Fits: yes, but SVG strings add weight to the single file.

## 5. What not to build

- 0 to 100 confidence ratings and a second confidence rating after feedback: more taps, and three levels carry the same signal on a four-option question.
- A full half-life regression or per-student ease factor: 150 items and a few answers per item is too little data; lapses plus confidence is enough.
- A second practice case per unit for far transfer (transfer-bridge): high content cost for the gain. Do changes 9 and 14 first.
- Streaks as the main motivator: change 6 replaces them.

## 6. Suggested build order

Changes 1, 2 and 3 first (together about a day; they fix the schedule). Then 4, 5, 6, 8, which are quick. Then 7, 9, 10, 11. Then 12 and 13. Then 14. Change 15 last.
