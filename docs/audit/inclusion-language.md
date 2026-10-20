# Inclusion, language accessibility, motivation and wellbeing audit

HSC BTEC L3 Extended Diploma self-study hub. Learners aged 16 to 18, many EAL or SEND.
Report only: no project files were edited. Companion file: `docs/audit/glossary.json` (60 terms).

## 1. Summary

- axe-core: 68 scans, 36 clean, 0 critical, 0 moderate, 3 rules failing (2 serious, 1 minor). All failures are in the Coach tab; Today, Points, Exams and Planner are clean. Dark mode has no contrast failures.
- Manual checks find what axe cannot: focus is lost after every action, tabs have no panel/keyboard model, feedback is not announced, control borders are 1.39:1, and two views overflow at 320 to 390px.
- Safeguarding gap: there is no content note and no help signpost anywhere, yet Unit 5 (the default coach unit, so the first thing a learner sees) opens with a self-harm case.
- Language: guide text is mostly readable (median FK 8.4) but spec-derived text (`fromSpec`) and coach `mustInclude` / `decode` / `bigIdea` fields are far above a Level 3 EAL reading age. The hardest strings are mostly comma-lists of technical nouns.
- Motivation: the points system is loss-framed ("points you can still lose"), the streak hard-resets, and two gates force typed output before help. This leans controlling rather than autonomy-supportive.
- Representation is better than typical (balanced gender, about 40% minority-coded names, dignified portrayals) but has a name error ("Mr Baptiste" for Mr Okello), duplicated names, deficit stacking and clear absences (faith, EAL service users, LGB characters, learning disability).

## 2. Scope, method, limitations

- Snapshot: other agents changed `src/hub.html` and `content/*.json` during the audit (integrity gate, own-work gate, "Try it first" flow). All results are from a frozen copy: `index.html` sha1 `ae8273760d26...`, `src/hub.html` sha1 `1f7e09933e8d...`, taken 2026-10-20 about 21:01. Line references may drift.
- axe-core 4.10.2 via `@axe-core/playwright`, tags WCAG 2.0/2.1/2.2 A and AA plus best-practice. Tabs: today, points, coach (after clicking `[data-act="gwopen"]` and stepping through the integrity gate, try-first, own-work gate and AI note states), exams (including checklist and quiz sub-views), planner. Light and dark, 1280px and 390px. Overflow also checked at 320px.
- Readability: Flesch-Kincaid grade with an in-house syllable heuristic; strings of 8+ words only for distributions. FK overstates lists of technical nouns, so treat it as a ranking aid, not a verdict.
- Not done: no screen reader or switch-access testing, no testing with learners, no reading of the ~60 other audit areas outside scope. Representation is inferred from names and descriptions, so it is indicative only.
- Fixes in section 11 were applied to throwaway copies and re-scanned: all 68 axe scans clean, no overflow at 390 or 320px, focus preserved, no page errors.

## 3. axe-core results

| Rule id | Impact | Count | Example selector | Fix |
|---|---|---|---|---|
| color-contrast | serious | 22 elements (light mode, Coach page) | `.lvl.M > .M.chip` ("Merit"): #a86c00 on #fbefd6 = 3.82:1. Also the "builds on" label and `.dcard-head .chip` ("A.P1", "A.P2"): #5a6e69 on #f4e3ec = 4.4:1 | `--muted:#52665f; --amber:#8f5a00` |
| target-size | serious | 1 (desktop only) | `#ck-5-AD1-4` (16px checkbox) | 20px checkboxes plus `padding-block:4px` on the label |
| aria-allowed-role | minor | 5 per scan | `button[role="listitem"][data-act="coachunit"]` | Remove `role="listitem"`; wrap in `role="group" aria-label="Units"` |
| critical / moderate | n/a | 0 | n/a | n/a |

axe "incomplete" items were non-text characters only. Today, Points, Exams, Planner: no violations in light, dark or 390px.

### Manual checks axe missed

| Finding | Evidence | WCAG |
|---|---|---|
| Focus drops to `<body>` after every action | The view `innerHTML` is rebuilt on each click, so the clicked control no longer exists | 2.4.3, 3.2.2 |
| Tabs lack a tab pattern | No `aria-controls`, no `role="tabpanel"`, no arrow-key handling, all tabs in tab order | 4.1.2, 2.1.1 |
| Header budget number not exposed | Budget cells are `aria-hidden`; no text equivalent | 1.1.1, 1.3.1 |
| Feedback not announced | "Correct / not quite" appears with no live region; toast has no role | 4.1.3 |
| Control borders 1.39:1 | `--line` on selects, inputs, buttons | 1.4.11 |
| Reflow overflow | Planner `#calName` scrollWidth 415 at 390px; Exams checklist `.ragbar` (110px fixed) 330 at 320px | 1.4.10 |
| Tiny text | 257 elements at 12px and 6 at 11px (Planner at 390px); uppercase mono eyebrows | 1.4.4, readability |
| Small targets | Checkboxes 13 to 16px; RAG buttons 30x26 | 2.5.8 |
| Colour-only status | Progress dots, `ragbar` meaning in `title` tooltips only | 1.4.1 |

Strengths worth keeping: `lang="en-GB"`, single h1, landmarks, 3px `:focus-visible`, `prefers-reduced-motion` respected, Atkinson Hyperlegible, no timers, dark mode, 16px base, autosave, confirm before "Clear everything".

## 4. Skills-based audit

### 4.1 UDL audit, barrier anticipation, options (udl-lesson-auditor, udl-barrier-anticipator, udl-options-designer)

| Principle | Currently | Gap | Highest-impact option |
|---|---|---|---|
| Engagement | Daily cap (8/12/16/20 questions), no timers, autosave | One fixed target (D*D*D*), loss framing, streak reset, mandatory typed output | Learner-chosen target and "skip" on every gate |
| Representation | Text only; unlabelled jargon; no audio | No glossary, no read-aloud, no chunking of long cases, single text size | Tap-to-define glossary with Listen; reading settings; chunked case summaries |
| Action/expression | Typed answers, min 5 and 10 words | No oral, list or tick-box route | Skip buttons; optional bullet or voice-typed answers |

Barrier table (design-addressable vs needs specialist support):

| Learner profile | Barrier | Severity | Design fix | Needs specialist support |
|---|---|---|---|---|
| EAL (new to UK) | Tier 3 + UK-institution terms, phrasal verbs, comma-lists | High | Glossary, plain-English rewrites, frames | Bilingual dictionary / first-language support via college EAL team |
| Dyslexia | Dense paragraphs, 12px mono labels, no spacing control | High | Reading settings (size, spacing), chunking, Listen | Assistive tech, exam access arrangements |
| ADHD | Forced typing before feedback, long scroll | Medium | Skips, shorter chunks, clear next step | Medication/coaching is outside the tool |
| Anxiety / low confidence | Loss framing, fear-appeal gates, red "lost" cells | High | Reframe to progress, soften gates | Counselling |
| Low vision / screen reader | Focus loss, no announcements, header number hidden | High | Section 11 items 2 to 4 | Screen reader testing by a user |
| Motor | 13 to 16px targets | Medium | 20px targets | Switch access needs real testing |
| Trauma history | Unflagged abuse and self-harm cases | High | Content note + signpost + skip | DSL / pastoral team |

### 4.2 Inclusive-design orchestrator (universal-first)

Hierarchy applied: (1) universal design changes everyone benefits from (contrast, targets, focus, plain English, glossary, skip), (2) optional personal settings (reading settings, listen), (3) targeted support (EAL frames, tiered starters), (4) specialist referral (screen reader testing, access arrangements, DSL). Tokenism check: the hub currently offers almost no layer 1 or 2 beyond dark mode, and no representation of EAL service users in any case, so inclusion is carried by the learner's own effort. The fixes below mostly sit in layers 1 and 2, so they avoid "special" labelling.

### 4.3 Differentiation (differentiation-adapter)

Core objective held constant: produce a Distinction-standard, own-work answer. Adaptations that keep the cognitive demand:

| Need | Adaptation | Keeps demand because |
|---|---|---|
| EAL | Glossary, frames, bilingual dictionary allowed | Still must select, justify and judge |
| Dyslexia | Larger text/spacing, Listen, chunked cases | Same content and task |
| ADHD | Skip buttons, shorter steps, visible progress | Same questions |
| Anxiety | No red "lost", gentle streak, no penalty list up front | Same standard |
| Stretch | Remove starters, add "what would change your judgement?" | Higher demand |

### 4.4 Language demand analysis (language-demand-analyser)

- Receptive: long noun-phrase lists in `mustInclude`; verb definitions ("weigh strengths and weaknesses, alternatives and significance"); UK institutions (ICB, CQC, DSL, HCPC) unexplained; 25 NHS, 20 GP, 19 DNA, 13 MRI, 11 COSHH, 11 PPE, 10 CBT occurrences without expansion on first use.
- Phrasal verbs about 2.5 per 1000 words: "weigh up" (24), "falls short", "bring together", "near miss".
- Productive: extended written argument (evaluate/justify) with discourse markers; typed minimum word counts; oral "say it out loud" self-explanation.
- Pragmatic: integrity gate uses "malpractice" and a penalty list; own-work gate has 8 declarations in dense legal-style sentences (one of 38 words, FK 12.0).

### 4.5 Sentence frames (academic-language-sentence-frame-generator)

All 207 coach starters are single-level gap-fills. Replace with three tiers, and add connectives for Evaluate and Justify.

| Tier | Evaluate frame | Justify frame |
|---|---|---|
| Early | "One good thing is ___. One problem is ___. Overall, ___." | "I chose ___ because ___." |
| Developing | "___ helps because ___, but ___ limits this because ___. So overall ___." | "The best option is ___ because ___. This matters for ___ because ___." |
| Consolidating | "Although ___, the evidence suggests ___. However, ___ means that ___. To a large extent / only partly, because ___." | "I would recommend ___ over ___ because ___. This is stronger than ___, since ___." |

Connectives bank: because, so, therefore, however, although, whereas, as a result, this means that, on the other hand, to a large extent.

Contradiction to fix: the own-work gate says "I have not copied or adapted the hub's examples or sentence starters", while the coach offers starters. Clarify: "Sentence starters give structure only. The ideas, examples and evidence are mine."

### 4.6 Scaffolded task modification (scaffolded-task-modifier)

"Try it first" (min 5 words) and "Check my reasoning" (min 10 words) become: type, or tick "I need a hint first", or skip. Add a word bank beside the box (3 to 5 key words from the glossary for that criterion) and an example of what a 5-word answer can look like ("It helps because it is safe.").

### 4.7 Text complexity (text-complexity-analyser)

Quantitative: see section 5. Qualitative: dense noun phrases, abstract nominalisations ("significance", "enforcement"), implied reader knowledge of UK systems, hypothetical conditionals ("if the provider were to..."). Task: heavy. Reader fit: mixed. Recommendation: short sentences, one idea per sentence, list not comma-chain.

### 4.8 Argument and disciplinary scaffolds (argument-structure-scaffold-generator, disciplinary-writing-scaffold)

The existing Rosa example already models Point, Evidence, Link well. Annotate it with labels in the margin ("Point", "Case evidence", "Why it matters for the person", "Judgement") and reuse the same four labels as the skeleton for every Evaluate answer. Disciplinary move for H&SC: always return to the person and their rights, then to the service or law. Name that as the "H&SC move".

### 4.9 Cross-cultural validity (cross-cultural-task-validity-checker)

| Assumption | Where | Who it may disadvantage | Option |
|---|---|---|---|
| Individual achievement, one D*D*D* target | Points system | Collective or family-oriented learners; those not aiming for top grade | Choose your own target; "my goal" framing |
| Oral self-explanation ("say it out loud") | Coach | Learners who are quiet, in shared homes, or shy in English | Write or tick alternatives |
| Confidence self-rating (Guessing / Fairly sure / Certain) | Quizzes | Cultures where stated certainty is discouraged | Keep optional; neutral wording |
| UK-institution knowledge (ICB, CQC, DSL) | Cases and guide | Newcomers | Glossary |
| Academic-integrity norms | Own-work gate | Learners from collaborative or memorisation-based systems | Explain norms kindly before asking declarations |
| Fixed 5pm reminder | Planner | Ramadan fasting times, placement shifts | Let learner set the time |
| Person-centred autonomy assumed as the norm | Cases | Families who expect shared decisions | Include a case where family involvement is the person's wish |

### 4.10 Motivation (SDT) diagnostic (motivation-diagnostic-task-redesign)

| Need | Supports | Undermines | Redesign |
|---|---|---|---|
| Autonomy | Daily cap, Skip on some items | Loss framing ("points you can still lose", red "lost" cells, "What one slip costs", "Don't plan on it"), 8 declarations, forced typing, single target | Progress framing ("points earned / secured"), choice of target and mode, skips |
| Competence | Non-shaming confidence feedback, "Nothing here is marked" | Streak hard reset, no strategy-attributed feedback | Gentle streak (one rest day), feedback that names the strategy used |
| Relatedness | Nothing | No peer, tutor, or community features | Optional "tell my tutor" summary; shared-goal prompts (no social pressure) |

### 4.11 Self-efficacy (self-efficacy-builder-sequence)

Mastery experiences: start every unit with a small, winnable item (one Pass-level question), then climb. Vicarious: show a short, anonymised "how another student improved this answer". Verbal persuasion: replace "you have lost X points" with "you have X points secured; here is the quickest way to add more". Physiological: remove red alarm colours from routine progress.

### 4.12 Trauma-informed practice (trauma-informed-practice-designer)

Principles: safety, choice, transparency, collaboration, empowerment. Findings: no warning and no choice (safety, choice); the integrity gate uses fear-appeal language (safety); the default unit opens with a self-harm case (choice). See section 7 for content and exact wording.

### 4.13 Agency (agency-scaffold-generator)

Add: learner-chosen target; choose order of units; choose mode (tick, type, speak); an "I'm stuck" option that gives a hint rather than a penalty; a weekly "what worked for me" prompt.

### 4.14 Flow (flow-state-condition-designer)

Conditions present: clear goals, no timers, immediate feedback. Missing: difficulty tuning (all 207 starters one level), mastery-first sequence, and interruption control (gates break the flow before the first question). Suggest: gates once per session, not per task; start easier, then step up.

## 5. Readability

Flesch-Kincaid grade, strings of 8+ words.

### Distributions

| Source | Strings (8+ words) | Median | Mean | p90 | Notes |
|---|---|---|---|---|---|
| Guide (`guide_*.json`) | 2226 | 8.4 | 8.8 | 13.9 | 56% at grade 8 or below; 6% at 15+ |
| Coach (`coach_*.json`) | 750 | 10.7 | 11.3 | 16.8 | 17% at 15+ |
| UI copy (rendered, 131 strings) | 131 | 6.7 | 6.9 | 11.0 | 71% grade 8 or below, 19% 9 to 10, 6% 11 to 12, 4% 13+; FRE 67.4 |
| Exams | n/a | 10.5 | n/a | n/a | |

By field: `fromSpec` hardest (median 14.0, FRE 22.7, 64% at 13+); `need` 11.7; coach `mustInclude` 11.8; `decode` 14.2; `bigIdea` 15.2.
Hardest units: 24, 16, 22, 17, 25. Easiest: 19, 14, 9, 8, 11.

### 10 hardest content strings

FK overstates 9 of these because they are lists of technical nouns; rewrite as bullets rather than shortening.

| # | Location | FK |
|---|---|---|
| 1 | `coach_b.json` unit 15, `evidence[1]` | 30.3 |
| 2 | `coach_b.json` unit 15, `assignments` | 25.7 |
| 3 | `coach_b.json` unit 19, AB.D1 `mustInclude[2]` | 23.3 |
| 4 | `coach_a.json` unit 5, A.D1 `mustInclude[1]` | 22.5 |
| 5 | `coach_b.json` unit 14, BC.D2 `mustInclude[2]` | 22.2 |
| 6 | `coach_c.json` unit 22, CD.D2 `mustInclude[0]` | 21.9 |
| 7 | `coach_b.json` unit 17, C.D2 `mustInclude[1]` | 21.7 |
| 8 | `coach_c.json` unit 25, BC.D2 `mustInclude[2]` | 21.5 |
| 9 | `coach_b.json` unit 17, C.D2 `mustInclude[0]` | 21.2 |
| 10 | `coach_b.json` unit 17, AB.D1 `mustInclude[2]` | 20.9 (tied: `coach_a.json` unit 5 `bigIdea` 20.9) |

Hardest prose (not a list): `guide_a.json` unit 5 D.D3 `need`, FK 20.2.

### 10 hardest UI strings

| # | FK | String |
|---|---|---|
| 1 | 14.9 | "Refer to UK legislation and assimilated law, not EU legislation as directly applicable." |
| 2 | 14.1 | "HCPC still regulates other professions (e.g. occupational therapists, physiotherapists, paramedics) but no longer social workers in England." |
| 3 | 13.7 | "Unit 2: CQC's role (registration, inspection, ratings, enforcement) is stable." |
| 4 | 13.5 | "Abolished by the National Blood Authority and United Kingdom Transplant (Abolition) Order 2005; functions passed to NHSBT." |
| 5 | 13.5 | "Use varied information to weigh strengths and weaknesses, alternatives and significance, ending in a supported judgement linked to the context." |
| 6 | 12.7 | "From the spec's assessment guidance: Select material from the case studies to explore issues around equality and diversity and preventing discrimination." |
| 7 | 12.6 | "Select case details that raise real equality, diversity or discrimination issues, and say why each one matters." |
| 8 | 12.1 | "BRosa is a trans woman. Discrimination means treating someone unfairly because of a protected characteristic, and the Equality Act 2010 protects people." (note: "BRosa" looks like a stray character, worth checking in source) |
| 9 | 12.0 | "If I used an AI tool in a way my centre allows, I have named the tool and the date, kept a screenshot of my prompt and its answer, and said how I used it in my work." |
| 10 | 11.8 | "use AI to do the analysis, evaluation or judgements the Distinction criteria ask for" |

Items 1 to 4 are mostly admin or reference notes; the learner-facing ones to rewrite first are 5, 6, 7, 9.

Suggested rewrites (computed FK about 1.5 to 6):

| Original | Plain English |
|---|---|
| "Use varied information to weigh strengths and weaknesses, alternatives and significance, ending in a supported judgement linked to the context." | "Look at the good points, the bad points and other options. Then give your own decision. Use the case to back it up." |
| "Select case details that raise real equality, diversity or discrimination issues, and say why each one matters." | "Pick details from the case about unfair treatment. Say why each one matters." |
| "If I used an AI tool in a way my centre allows, I have named the tool and the date, kept a screenshot of my prompt and its answer, and said how I used it in my work." | "If I used AI in a way my college allows, I wrote down which tool and when. I kept a screenshot. I said how I used it." |
| Evaluate: "Use varied information to weigh strengths and weaknesses..." | "Evaluate: look at good and bad points, then give your own decision with reasons." |

Verb definitions (Evaluate, Justify, Assess, Discuss, Analyse) should be rewritten the same way; the 20 Tier 2 glossary entries already have plain definitions to reuse.

## 6. Tiered glossary

Full data: `docs/audit/glossary.json` (`[{"term","tier","def"}]`, definitions 20 words or fewer, median FK 8.4).
Tier 3 = subject-specific; Tier 2 = academic/exam. Tier 1 EAL traps are listed after the tables.

#### Tier 3: subject words (40)

| Term | Definition |
|---|---|
| holistic care | Care that looks at the whole person: body, mind, feelings, relationships and surroundings, not just their illness. |
| person-centred care | Care planned around what the person wants, needs and values. The person helps make the decisions. |
| safeguarding | Protecting children and adults at risk from abuse, neglect and harm, and acting quickly when you are worried. |
| confidentiality | Keeping a person's private information safe. You share it only with people who need to know, usually with permission. |
| informed consent | A person agrees to care or research after being told, in words they understand, what it involves and the risks. |
| discrimination | Treating someone unfairly because of who they are, for example their age, disability, race, sex or religion. |
| protected characteristic | A personal feature the Equality Act 2010 protects from unfair treatment, such as age, disability, race or religion. |
| advocacy | Speaking up for a person, or helping them speak up, so their views and rights are heard. |
| empowerment | Helping people gain more control over their own lives and choices. |
| dignity | Treating a person with respect so they feel valued and in control, for example by protecting their privacy. |
| multi-agency working | Different organisations, such as the NHS, the council and charities, working together to support one person. |
| multidisciplinary team | A group of professionals with different jobs, such as nurse, therapist and social worker, planning care together. |
| key worker | The main professional who coordinates a person's support and is their usual point of contact. |
| care plan | A written plan of a person's needs, goals and the support they will get. It is reviewed regularly. |
| risk assessment | Checking what could cause harm, how likely and how serious it is, and deciding how to reduce it. |
| reflective practice | Thinking carefully about what you did, how it went and what you will do differently next time. |
| witness statement | A signed account from a supervisor or observer of what you did on placement, used as evidence. |
| domiciliary care | Care given in a person's own home, for example help with washing, dressing or taking medicine. |
| Care Quality Commission (CQC) | The organisation that inspects and rates health and social care services in England and can require improvements. |
| Integrated Care Board (ICB) | An NHS organisation that plans and pays for health services for the people in its local area. |
| health inequality | An unfair, avoidable gap in health between groups of people, for example between richer and poorer areas. |
| screening | Testing people who seem healthy to find a condition early, so treatment can start sooner. |
| diagnosis | A professional's decision about which illness or condition a person has, based on symptoms, tests and examination. |
| rehabilitation | Treatment and support that helps someone regain skills and independence after illness, injury or surgery. |
| palliative care | Care for people with an illness that cannot be cured, focusing on comfort, pain relief and quality of life. |
| stigma | Unfair negative views that make a person feel ashamed or judged, for example about mental illness. |
| attachment | The close emotional bond between a baby and the person who cares for them. It affects later relationships. |
| schema | A mental framework built from experience that helps a child organise and understand the world (Piaget). |
| self-esteem | How much a person values and respects themselves, and how worthy they feel. |
| nature-nurture debate | The argument about whether development is shaped more by inherited genes (nature) or by experience and surroundings (nurture). |
| stress-diathesis model | Explains mental illness as an inherited weakness (diathesis) combined with a stressful event that triggers it. |
| dementia | A group of conditions that damage the brain over time, causing memory loss, confusion and difficulty with daily life. |
| outbreak | A sudden rise in cases of an infection in one place, for example in a nursery. |
| pathogen | A micro-organism, such as a bacterium or virus, that can cause disease. |
| infection prevention and control | Actions that stop infections spreading, such as handwashing, cleaning, protective equipment and keeping ill people apart. |
| homeostasis | The body keeping its inside conditions, such as temperature and blood glucose, steady when outside conditions change. |
| enzyme | A protein that speeds up a chemical reaction in the body, for example amylase breaking down starch. |
| allele | One version of a gene. You inherit one allele of each gene from each parent. |
| biopsy | Taking a small sample of tissue from the body to examine under a microscope for disease. |
| epidemic / pandemic | An epidemic is a fast spread of an infectious disease in an area. A pandemic spreads across the world. |

#### Tier 2: exam and study words (20)

| Term | Definition |
|---|---|
| evaluate | Weigh up strengths and weaknesses using evidence, then reach a judgement you can support. |
| justify | Give reasons and evidence to show that a choice or decision is right or reasonable. |
| analyse | Break something into parts and explain how the parts connect or what they show. |
| assess | Weigh up the important factors in a situation and decide which matter most. |
| compare | Say how two or more things are similar and how they are different. |
| discuss | Look at different sides of a topic and explain how important each one is. |
| explain | Give reasons: say what happens or what is true, and why. |
| describe | Give a clear account of what something is like, using details. |
| outline | Give the main points briefly, without lots of detail. |
| to what extent | How far is a statement true? Give arguments on both sides, then decide how strongly you agree. |
| evidence | Facts, examples or information that show something is true or support your point. |
| judgement | A decision or opinion you reach after weighing up the evidence. |
| context | The situation around something that helps explain it, such as a person's age, home and needs. |
| factor | One of the things that causes or influences a result. It is not the same as a fact. |
| impact | The effect something has on a person or situation. |
| limitation | A weakness that makes something less useful, reliable or complete. |
| recommend | Suggest what should be done and give reasons why it is the best choice. |
| perspective | A particular way of seeing something, based on a person's experience or on a theory. |
| specific | Exact and clear, not general. Name the real person, place or detail. |
| relevant | Closely connected to the question or case, so it helps answer it. |


### Tier 1 words that still trip EAL learners

Everyday words with a special meaning here: **weigh up** (compare carefully, not measure weight), **cover** (include in your answer), **case** (a made-up person's story, not a box), **setting** (the place where care happens), **support** (help and assistance, also a noun), **record** (write down; also the noun), **practice / practise** (noun / verb), **run** (manage), **fall short** (not good enough), **bring together** (combine), **near miss** (an accident that nearly happened).

Implementation: underline Tier 3 words only (max 8 per view, first occurrence), not Tier 2, to avoid noise. Add the Tier 1 traps to the verb panel as "Words with a special meaning here".

## 7. Sensitive content

### Findings

- No content note and no help signpost exist anywhere in `src/hub.html` or `content/*.json`. The only "Mind" hit is a source citation (`coach_b.json` unit 20, `evidence[3]`). "Designated safeguarding lead" appears only in an exam model answer (`exam_u2.json` long[5]).
- Handling is factual with no method detail (checked by grep). No gratuitous content found.
- Unit 5 is the default coach unit (`blank()` sets `coachUnit:5`), so a self-harm case is the first thing new learners see.

| Topic | Paths |
|---|---|
| Self-harm | `guide_a.json` unit 5 `parallelCase.summary`; unit 5 `criteria.BC.D2.requirements[4].example`; unit 5 `criteria.D.D3.requirements[3].example` |
| Self-harm, suicide, bullying | `exam_u1.json` topics[7] (B4) `points[2]`; mcq `u1q42` (index 41) |
| Abuse / neglect | `coach_a.json` unit 7 `criteria.B.D2`; `guide_a.json` unit 7 (Mrs Halloran: bruises and an empty purse); `exam_u1.json` topics[2] (A3) `points[4]`; `exam_u2.json` mcq `u2q18`, `u2q39`; long `u2l05`, `u2l06`, `u2l07` (Kai, 15, in a children's home) |
| Disordered eating | `exam_u1.json` `u1q18` (Ellie, 15, dieting) |
| Mental ill health | `guide_c.json` unit 20 (Wren Tallis: bipolar II and generalised anxiety disorder, a "dangerous near-miss" and fitness to drive); `coach_b.json` unit 20; `exam_u1.json` long `u1l01` |
| Dementia | `guide_b.json` unit 17 (Bernard); `coach_b.json` unit 17; `guide_a.json` unit 7; `exam_u2.json` `u2l01` to `u2l04` (Edna) |
| Bereavement | `exam_u1.json` `u1l03` (Gerald); `guide_c.json` unit 19 |

Because the hub tells learners drafts are private, the help panel must not suggest anyone is reading their writing.

### Exact wording

Page note (52 words, shown on first visit and in the footer):

> Some cases and questions in this hub cover abuse, self-harm, suicide, bullying, dementia and mental ill health. They are written to be factual, with no detail about methods. You can skip any of them without giving a reason. If a topic upsets you, help is listed at the bottom of this page.

Per-item note (cases and questions in the SENS maps):

> Content note: this one covers {topic}. It is factual and has no detail about methods. You can skip it without giving a reason. Need to talk to someone?

Help signpost, heading "Need to talk to someone?":

> Some parts of this course cover hard topics. If something here, or something in your life, is getting to you, you do not have to cope alone.
>
> - At college: your tutor or Designated Safeguarding Lead (DSL).
> - Childline (under 19): 0800 1111. Free, 24 hours.
> - Samaritans: 116 123. Free, 24 hours.
> - Shout: text SHOUT to 85258. Free, 24 hours.
> - In danger now? Call 999.
>
> Nothing you type in this hub is read by anyone. If you want to tell someone something, use one of the contacts above or speak to a member of staff.

The helpline numbers were checked against the official sites on the audit date. The college should add its own DSL name and number before release. Computed FK of this wording: about 2.6 to 5.8.

## 8. Representation (parallelCase and quiz scenarios)

Inferred from names and descriptions, so indicative.

### Counts

22 parallel cases and about 31 named people. Gender: 12 women, 13 men, 6 gender-neutral or non-binary-coded (Kit, Dev, Jo, Wren Tallis, Rowan, Joss). Minority-coded names are about 40 to 43% in both the guide and the exam bank.

### Strengths

- All cases flagged fictional.
- A trans woman (Rosa) portrayed with dignity and legal framing.
- Strengths-based portrayals of Wren Pascoe (deaf), Desmond (brain injury), Bernard (dementia).
- A mixed-heritage family (Priya and Callum).
- Competent minority-coded professionals (Mrs Adeyemi, Dev).

### Issues

| Issue | Detail | Fix |
|---|---|---|
| Name error | "Mr Baptiste" used 24 times in `guide_c.json` unit 19, but the full name is Baptiste Okello (first name used as surname) | Replace with "Mr Okello" |
| Duplicated names | Kit x2 (U6 learner, U18 toddler); Wren x2; Idris x2 (U5, U23); Priya x3 (`exam_u1` u1l02, `exam_u3` u3l04, `guide_c` 22); Calloway x2; two "retired ferry engineers" (Bernard, Alun); two joiners | Rename, vary jobs |
| Deficit stacking on minority-coded characters | Idris (care leaver, homeless, dyslexia, self-harm); the Okafor family (overcrowded damp flat, `exam_u1` u1l04); Mr Baptiste (poor, isolated, widower); Amara (autism-coded child, "concerns" only) | Give each at least one stated strength and one successful outcome |
| Gendered work | Male joiners and engineers; a female school cook | Swap some |
| Tropes | The angry teenage boy (Leon); the older woman who says "I'm no use now" (Ada) | Vary |
| Absent groups | Faith or religion for any named person (despite the spec's cultural and religious needs); EAL service users and interpreters (zero cases); gay, lesbian or bisexual characters; explicit learning disability or autism; refugees or migrants; Travellers; racism as a determinant of health; inner-city and multilingual settings (settings are mostly coastal, rural or former industrial; only "Eastmere" is a city) | New case briefs below |

### New case briefs (to close the gaps, written with the same strengths-first pattern)

1. A 34-year-old Polish-speaking father uses an interpreter at a GP appointment for his daughter; the case asks about communication barriers and confidentiality.
2. A gay couple in their seventies in domiciliary care; the case asks about dignity and person-centred assessment.
3. A Muslim woman in a day centre during Ramadan; the case asks about cultural and religious needs.
4. A young adult with a learning disability who chooses their own support plan, with advocacy.
5. A Traveller family accessing health screening; barriers and trust.

## 9. Wellbeing and motivation findings

- Loss framing: header "Points you can still lose", red "lost" cells, "What one slip costs", "You've lost X points, so even with Distinctions...", "Don't plan on it" (resubmission), red "Busy week" notices.
- Streak: hard reset and "Start a streak today". Fix: one rest day tolerated (`S.streak=(S.lastDone&&dayDiff(S.lastDone,t)<=2?(S.streak||0)+1:1)`), and a way to hide it.
- Gates: the integrity gate and the own-work gate use controlling language ("malpractice", penalty list, 8 declarations). Minimum 5 words in "Try it first" and 10 words in "Check my reasoning" before feedback. The gates are valid for academic integrity; the issue is tone and the lack of a skip for learners who are stuck or anxious.
- No relatedness features, no choice of target or mode.
- Good: daily cap, non-shaming confidence feedback, "Nothing here is marked", no timers, autosave, confirm before clearing.

## 10. Prioritised changes (12)

| # | Change | Why | Effort |
|---|---|---|---|
| 1 | Content note (page, per-case, per-question, with skip) plus the help signpost | Safeguarding duty; Unit 5 is the default | Small |
| 2 | Preserve focus after re-render and announce feedback (live region) | Keyboard and screen reader users lose their place every click | Small |
| 3 | Tab ARIA (tabpanel, aria-controls, arrow keys) plus screen-reader budget number | Navigation and key information are unavailable | Small |
| 4 | CSS patch: contrast, 20px targets, 320px reflow, 3:1 borders, min text size, unit-list roles | Clears all 3 axe rules and manual failures | Small |
| 5 | Tap-to-define glossary (Tier 3, 60 terms) with Listen | Biggest EAL barrier | Medium |
| 6 | Skip options on gates, lighter own-work wording (and clarify starters) | Autonomy, anxiety, EAL | Small |
| 7 | Reframe loss language, gentler streak, learner's own target | Self-determination | Small to medium |
| 8 | Plain-English pass: verb definitions, 10 hardest strings, comma-lists to bullets, chunk case summaries (e.g. Unit 7 as Who / What Dev notices / What she wants / Other things / Who can help) | Reading load | Medium |
| 9 | Tiered sentence frames (Early/Developing/Consolidating) and connectives for Evaluate and Justify | Language production | Medium |
| 10 | Reading settings (size, spacing, theme) stored locally | Dyslexia, low vision | Small |
| 11 | Representation fixes: "Mr Okello", duplicate names, balance deficit stacking, five new case briefs | Belonging and validity | Medium |
| 12 | Strategy-attributed feedback, mastery-first sequence, agency choices | Self-efficacy and flow | Medium |

## 11. Appendix: tested code (apply to `src/hub.html`, then rebuild with `tools/build.py`)

All applied to copies only; 68 axe scans clean afterwards. Full patch scripts are in the audit scratchpad (`work/fixes.py`, `fixes2.py`, `fixes3.py`, `extra_snippets.js`, `extra.css`) and are reproduced here where load-bearing.

### A. CSS (append before `</style>`)

```css
:root{--muted:#52665f;--amber:#8f5a00;--ui:#74857f;--t-xs:.875rem}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--ui:#6d807b}}
:root[data-theme="dark"]{--ui:#6d807b}
select,input[type="number"],input[type="date"],input[type="text"],textarea,.btn,.seg,.opts button,.pick,.rag button,.gw-steps button,.unit-switch button,.unitlist button{border-color:var(--ui)}
.sr-only{position:absolute;width:1px;height:1px;margin:-1px;padding:0;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
input[type="checkbox"],.checklist input{width:20px;height:20px}
.checklist label{padding-block:4px}
.rag button{min-width:36px;min-height:36px}
.cal-form input,.cal-form select{width:100%;min-width:0}
.topic summary{grid-template-columns:3rem minmax(0,1fr) auto}
.ragbar{width:clamp(56px,20vw,110px)}
.eyebrow{text-transform:none;letter-spacing:.02em}
.boxes .bl{font-size:.8rem}
```

### B. Header budget number for screen readers

Inside `<div class="budget-mini" aria-live="polite">` add:

```html
<span class="sr-only" id="miniLeft"></span>
```

In `renderHeader`:

```js
$("#miniLeft").textContent=`${Math.max(0,c.left)} of ${BUDGET} points left to lose. Projected grade ${c.grade}.`;
```

(After change 7 reword this to "points secured".)

### C. Tab pattern

- Tab buttons: add `id="tab-X" aria-controls="view-X" tabindex="0"` (active) or `tabindex="-1"` (others).
- Each `<section class="view">`: add `role="tabpanel" aria-labelledby="tab-X" tabindex="0"`.
- In `setTab`: `b.tabIndex=on?0:-1`.
- Keyboard handler:

```js
document.querySelector("nav.tabs").addEventListener("keydown",e=>{
  const tabs=[...e.currentTarget.querySelectorAll("[role=tab],button[data-tab]")];
  let i=tabs.indexOf(document.activeElement); if(i<0)return;
  if(e.key==="ArrowRight")i=(i+1)%tabs.length;
  else if(e.key==="ArrowLeft")i=(i-1+tabs.length)%tabs.length;
  else if(e.key==="Home")i=0; else if(e.key==="End")i=tabs.length-1; else return;
  e.preventDefault(); tabs[i].focus(); setTab(tabs[i].dataset.tab);
});
```

### D. Focus preservation and announcements (in `render()`)

Add a hidden live region once: `<div id="sr" class="sr-only" role="status" aria-live="polite"></div>`. Give the toast `role="status"`.

```js
function focusSel(el){
  if(!el)return null;
  if(el.id)return "#"+CSS.escape(el.id);
  const a=["act","k","u","i","c","v","m","s","p","t","g","id"];
  const parts=a.filter(k=>el.dataset&&el.dataset[k]!=null).map(k=>`[data-${k.replace(/[A-Z]/g,m=>"-"+m.toLowerCase())}="${CSS.escape(el.dataset[k])}"]`);
  return parts.length?el.tagName.toLowerCase()+parts.join(""):null;
}
function announce(msg){const s=document.getElementById("sr");if(s){s.textContent="";setTimeout(()=>s.textContent=msg,50)}}
```

In `render()`: before rebuilding, `const sel=focusSel(document.activeElement)`. After building the view: call `glossify(view)` if installed; `const fb=view.querySelector(".feedback"); if(fb)announce(fb.textContent.trim())`; then restore focus:

```js
let t=sel&&view.querySelector(sel);
if(!t) t=view.querySelector('[data-act="dnext"],[data-act="quiznext"]')||view.querySelector(".feedback");
if(!t) t=view.querySelector('.q-card [data-act="conf"], .q-card .opts button:not([disabled])');
if(!t) t=view.querySelector("h2,h3");
if(t){ if(!t.matches("button,a,input,select,textarea,[tabindex]"))t.setAttribute("tabindex","-1"); t.focus({preventScroll:false}); }
```

### E. Coach unit list roles

Use `<div class="unitlist" role="group" aria-label="Units">` and remove `role="listitem"` from the `data-act="coachunit"` buttons.

### F. Content note, help section, glossary dialog, reading settings, streak

```js
const SENS={5:"self-harm and being treated unfairly",7:"abuse of an older person",11:"anger and low mood",17:"dementia",19:"bereavement and eating habits",20:"mental ill health"};
const SENS_Q={u1q18:"dieting",u1q42:"bullying, self-harm and suicide",u2l05:"abuse of a child",u2l06:"abuse of a child",u2q18:"abuse of residents"};
function contentNote(topic){return topic?`<p class="notice cn"><b>Content note:</b> this one covers ${esc(topic)}. It is factual and has no detail about methods. You can skip it without giving a reason. <a href="#help">Need to talk to someone?</a></p>`:""}
```

Call `contentNote(SENS[u])` before `parallelPanel(u)` and `contentNote(SENS_Q[q.id])` before each `.q-stem`. Add at page end:

```html
<section id="help" aria-labelledby="help-h"><h2 id="help-h">Need to talk to someone?</h2>
<p>Some parts of this course cover hard topics. If something here, or something in your life, is getting to you, you do not have to cope alone.</p>
<ul><li>At college: your tutor or Designated Safeguarding Lead (DSL).</li>
<li>Childline (under 19): <a href="tel:08001111">0800 1111</a>. Free, 24 hours.</li>
<li>Samaritans: <a href="tel:116123">116 123</a>. Free, 24 hours.</li>
<li>Shout: text SHOUT to 85258. Free, 24 hours.</li>
<li>In danger now? Call <a href="tel:999">999</a>.</li></ul>
<p>Nothing you type in this hub is read by anyone. If you want to tell someone something, use one of the contacts above or speak to a member of staff.</p></section>
```

Glossary dialog (`glossify`, `openGloss`, Listen via `speechSynthesis`), reading settings (`applyRS`/`setRS`, key `hsc-read`, attributes `data-fs`, `data-ls`, `data-theme`) and the streak change:

```js
S.streak=(S.lastDone&&dayDiff(S.lastDone,t)<=2?(S.streak||0)+1:1)
```

are in `work/extra_snippets.js`; `GLOSS` takes the contents of `docs/audit/glossary.json` at build time. `glossify` marks only Tier 3 terms, at most 8 per view, skips hidden and closed-details content, headings, buttons and inputs.

### G. Skip options on gates

Change the condition to `${!st.preDone?` (not `wordCount(st.pre)<5||!st.preDone`, which re-shows the box). Add a button `<button class="btn" data-act="gwpredone" data-skip="1">Skip</button>` beside the existing one, and in the `gwpredone` and `gwrev` handlers use `if(!b.dataset.skip&&wordCount(...)<N)`.

### H. Verification results

All 68 axe scans on the patched copy: no violations. No overflow at 390 or 320px. Focus survives confidence click, answer and Next. Tab arrows work; 5 tabpanels. Glossary dialog opens and closes with Esc. Font size XL gives 20px with no overflow. Note, signpost and gate skip work. No page errors.
