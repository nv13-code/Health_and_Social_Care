# Privacy: HSC D* hub

The hub is built so that **no personal information is retained** by the project, the page's author or anyone else.

## What the hub never collects
- Names, email addresses, student or candidate numbers, or school names. The hub never asks for them.
- Anything a student types. Practice answers, walkthrough explanations, first tries and evidence-map notes stay in the page's memory for that visit only, and disappear on close or reload. A student can opt in to "Save my writing" (Planner → Your privacy). It's off by default.
- Analytics, tracking or cookies. The page makes **no outside requests**: fonts are bundled into the file and there are no third-party scripts. The build fails if Google Fonts creep back in.

## What is saved, where, and for how long
| Data | Where | Who can see it | Kept for |
|---|---|---|---|
| Ticks, RAG ratings, quiz progress, confidence log (last 60 days), grades and dates the student enters | The student's own browser (localStorage) | Only that browser | Until deleted, or 12 months after last use |
| The same structured progress | The student's **own** claude.ai account, only if they publish their own copy and are signed in. Stored under an opaque account id; no name or email is stored | Only the student. Not the page's author | Until deleted, or 12 months after last use |

Assignment names in the calendar come from a fixed list (for example "Learning aims A and B"), so no free text is stored there either.

## Student controls
- **Delete everything** (Planner → Backup) removes all saved progress from the browser and, if signed in, from their account.
- **Backup** (Planner → Backup): **Save backup file** downloads a `.json` file to the student's own device, and **Restore from file** brings it back. A backup code works the same way as text. By default a backup holds only the structured progress above. The student can tick **Include my writing** to keep that visit's practice answers and notes in the file. The file stays with the student and is never sent anywhere. The Today tab reminds them weekly once they've made progress.
- The **pilot summary** is anonymous numbers only: recall by time gap, confidence accuracy, counts of steps completed. No writing, grades, names or dates of birth. It's shared only if the student chooses.

## Things that leave the page only when the student acts
- **"Add to Google Calendar" links** send that event's text (for example "Unit 5 Learning aims A and B: hand in") to Google when the student clicks.
- **"Listen"** in the glossary uses the browser's built-in speech; nothing is sent by the hub.

## For the centre
- If the hub is hosted somewhere else (for example SciencePass), keep it as a static file with no analytics to preserve these guarantees.
- Under-18s: because no personal data is collected by the project, a pilot needs no data-sharing arrangement. Check your centre's policy on students using their own AI accounts.
