# Pack 07 — Live Demo: JobHunterGPT

**Status:** Not Started
**Honest starting position:** Cannot demo live today. System works but needs
rehearsal, clean environment, and a test package ready to show.
**Goal:** Prepare a reliable, professional 5-minute screen-share demo that
illustrates the AI Systems Builder value proposition without live failure risk.

---

## Skill Goal

Produce a polished, rehearsable demo of JobHunterGPT that can be shown in a
technical interview, on a portfolio page, or in a Zoom screen share — within
5 minutes, with no errors, no apologies, and no improvisation required.

The demo must show: the system runs, produces output, and the design reflects
engineering judgment (not just a script).

---

## Why It Matters for Proofpoint-Style Roles

The Proofpoint JD does not require you to demo JobHunterGPT. But preparing a
live demo builds three things that transfer directly:

1. **Proof of capability.** "I built a Python AI automation system" is a claim.
   Running it live is evidence.
2. **Demo fluency.** The role involves running demos for enterprise customers.
   Practicing on your own project teaches the format.
3. **System confidence.** Knowing your system well enough to demo it without
   fear means you understand it deeply — which matters in technical interviews.

---

## What the Demo Must Show

A complete run from a job description to a reviewable package:

  Step 1 — Show the job description file (30 seconds)
  Step 2 — Run the package generation command (30 seconds)
  Step 3 — Open the output folder and navigate the files (1 minute)
  Step 4 — Show the cover letter — explain why it's structured this way (1 minute)
  Step 5 — Run the package reviewer and read the output (1 minute)
  Step 6 — Show the fit score report — explain what it means (30 seconds)
  Step 7 — Summary: what the system does, what it does NOT do (30 seconds)
  Total: ~5 minutes

---

## Pre-Demo Requirements

Before running this demo in any professional setting, ALL of the following must be true:

  [ ] A clean practice job description file exists and is not a private real application.
  [ ] The candidate_profile.json is loaded and valid.
  [ ] The master_resume.txt is present and not a placeholder.
  [ ] Running `py -m job_search_agent --help` produces output with no errors.
  [ ] A test package generation completes without errors.
  [ ] The package reviewer returns READY_FOR_HUMAN_REVIEW on the test package.
  [ ] The terminal font is readable in a screen share.
  [ ] The output folder is clean (no leftover test artifacts from failed runs).
  [ ] All 70 tests pass: `py -m unittest discover -s tests -v`

Do not attempt a live demo until all boxes are checked.
Document the check as: `learning/evidence/07-demo-readiness-check.txt`

---

## Three Learning Tasks

**Task 1: Write the demo script.**
Write a word-for-word script for the 5-minute demo.
Every line you will say, every command you will run, every file you will open.
Over-scripted is better than improvised for technical demos.

Format:
  [0:00] Say: "This is JobHunterGPT — a human-in-the-loop AI job search system..."
  [0:30] Open: job_descriptions/practice-job-description.txt
  [0:45] Say: "This is the job description. The system never reads this automatically..."
  [1:00] Run: py -m job_search_agent --resume resumes/master_resume.txt ...
  ...

Save as: `learning/evidence/07-demo-script.txt`

**Task 2: Create the practice package.**
Generate a clean demo package from the practice job description (GPT Innovation
by Attaf / AI Automation Specialist). This is the package used in the demo.

Run:
  py -m job_search_agent \
    --resume resumes/master_resume.txt \
    --job job_descriptions/practice-job-description.txt \
    --company "GPT Innovation by Attaf" \
    --title "AI Automation Specialist" \
    --url "https://www.gptinnovationbyattaf.com" \
    --profile config/candidate_profile.json

Confirm: package reviewer returns READY_FOR_HUMAN_REVIEW.
Save reviewer output as: `learning/evidence/07-demo-package-reviewer-output.txt`

**Task 3: Rehearse three times.**
Run the full demo script three times from start to finish.
Time each run. Record the time.

  Run 1: [Date] [Duration] — Notes
  Run 2: [Date] [Duration] — Notes
  Run 3: [Date] [Duration] — Notes

Goal: Under 5 minutes with no errors and no looking at the script after Run 2.
Save as: `learning/evidence/07-rehearsal-log.txt`

---

## Demo Guardrails (Read Before Every Demo)

- Do NOT show config/candidate_profile.json — it contains private contact info.
- Do NOT show resumes/master_resume.txt — it is private.
- Do NOT show data/applications.csv — it may contain real application data.
- Do NOT show any applications/ folder with real company names or application status.
- Use ONLY the practice job description and practice package in the demo.
- If something fails during the demo: stay calm, say "let me re-run that" once,
  then fall back to showing the output files from a previous successful run.

---

## Common Interview Questions This Demo Answers

  Q: "Can you show me something you've built?"
  A: Run the demo.

  Q: "How does your system prevent errors in the output?"
  A: Show the package reviewer, explain [ERROR] vs [WARNING] design.

  Q: "Why did you build it this way — why not just use ChatGPT?"
  A: Explain human-in-the-loop design, verified facts only, local privacy.

  Q: "Does it auto-apply to jobs?"
  A: No — by design. Explain why. This is a feature, not a limitation.

  Q: "Could you scale this to enterprise?"
  A: Honest answer: this is a personal tool. Describe what would need to change
     for enterprise use (database backend, auth, multi-user, audit logging).

---

## Evidence to Collect

- [ ] `learning/evidence/07-demo-readiness-check.txt` — pre-demo checklist signed off
- [ ] `learning/evidence/07-demo-script.txt` — complete word-for-word demo script
- [ ] `learning/evidence/07-demo-package-reviewer-output.txt` — reviewer output
- [ ] `learning/evidence/07-rehearsal-log.txt` — three rehearsal times and notes

---

## Completion Criteria

- All pre-demo requirements checked and documented.
- Demo script written and followed without deviation in rehearsal.
- Three rehearsals complete, at least one under 5 minutes.
- Can answer all four common interview questions above without notes.

---

## Interview Sentence After Completion

"I'd be happy to show you. I can share my screen and run the system live —
it takes about 5 minutes to go from a job description to a reviewed package.
Should I do that now?"

---

## Pack 07 Output Created

Status updated to **Evidence Ready** on 2026-06-23.

The following files were created in `learning/pack07-live-demo-output/`:

- [five-minute-demo-script.md](pack07-live-demo-output/five-minute-demo-script.md) — Word-for-word demo script with timestamps
- [demo-command-sheet.md](pack07-live-demo-output/demo-command-sheet.md) — Exact PowerShell commands with screen-share safety labels
- [demo-risk-checklist.md](pack07-live-demo-output/demo-risk-checklist.md) — Pre-demo privacy checklist and fallback plan
- [interview-demo-answer.md](pack07-live-demo-output/interview-demo-answer.md) — 6 interview questions with specific practiced answers
- [pack07-completion-report.md](pack07-live-demo-output/pack07-completion-report.md) — Full completion report, 45-second intro, next steps

Next recommended pack: **Pack 08 — AI Integration Specialist Story**
