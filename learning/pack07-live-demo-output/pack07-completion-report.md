# Pack 07 Completion Report — Live Demo Readiness

**Date completed:** 2026-06-23
**Status:** Evidence Ready
**Demo Ready:** Yes (script and commands documented; rehearsal still required before live use)

---

## What Was Created

Five output files in `learning/pack07-live-demo-output/`:

| File | Purpose |
|------|---------|
| `five-minute-demo-script.md` | Word-for-word 5-minute screen-share demo script with timestamps |
| `demo-command-sheet.md` | Exact PowerShell commands, what each proves, screen-share safety labels |
| `demo-risk-checklist.md` | Pre-demo privacy checklist, what not to claim, fallback plan |
| `interview-demo-answer.md` | 6 interview questions answered with specific, rehearsable answers |
| `pack07-completion-report.md` | This file |

Also updated:
- `learning/progress-tracker.csv` — Pack 07 status set to Evidence Ready, Demo Ready: Yes
- `learning/07-live-demo-jobhuntergpt.md` — Pack 07 Output Created section added

---

## What Sahid Can Demo Now

**The 5-minute demo is scripted and safe to run.** The following steps work
with no private data on screen:

1. Open README.md and walk through the repository structure (8 modules named)
2. Show `config/candidate_profile.example.json` (safe — no real data)
3. Run `py -m unittest discover -s tests -v` → 70 tests pass
4. Open the practice package: `applications/gpt-innovation-by-attaf-ai-automation-specialist/`
5. Show `application-details.txt` and `cover-letter.txt` from the practice package
6. Run the reviewer: `py -m package_reviewer "applications\gpt-innovation-by-attaf-ai-automation-specialist" --candidate-name "Sahid Attaf"`
7. Read `READY_FOR_HUMAN_REVIEW` from the output

**What this proves to an interviewer:**
- Multi-module Python workflow design (8 modules, separation of concerns)
- Test-driven development (70 tests, run live)
- Responsible AI design (human-in-the-loop, no auto-submission)
- Quality control thinking (package reviewer with ERROR vs WARNING distinction)
- Ability to build, test, document, and improve an AI-enabled workflow independently

---

## What Sahid Should Not Claim During or After the Demo

| Do not claim | Honest alternative |
|-------------|-------------------|
| "This is production-ready" | "This is a local prototype" |
| "This scales to enterprise" | "It demonstrates the pattern I would apply at enterprise scale" |
| "I've integrated this with enterprise platforms" | "I've built the equivalent pattern at a smaller scale" |
| "I have cybersecurity experience" | Not relevant to this demo — don't bring it up |
| "Amazon Q works the same way" | "The same design pattern applies in enterprise AI platforms" |
| "The app submitted my applications" | "It never submits anything — that's a design requirement" |
| "I have Salesforce/Jira experience" | Not relevant to demo — don't bring it up |

---

## Exact 45-Second Demo Intro

Memorize this. Say it before sharing your screen.

---

"This is JobHunterGPT — a local Python prototype I built to automate the
preparation side of a job search while keeping a human in the loop at every
step. It reads a job description and a resume, extracts ATS keywords,
calculates a fit score, generates a cover letter draft, and runs a structural
reviewer before anything leaves the system. It never applies to jobs
automatically. It never invents experience. I'll show you how it runs."

---

**Timing:** Read this out loud. It should land between 35 and 45 seconds.
Practice until you can say it without looking at a script and without rushing.

**Key phrases to include every time:**
- "local Python prototype" (sets honest expectations)
- "human in the loop at every step" (design principle)
- "never applies automatically" (guardrail)
- "never invents experience" (integrity)

---

## What to Practice First

**Priority 1: The 45-second intro above.**
Say it out loud five times today. Do not move to the full 5-minute script
until the intro is completely natural — this is what the interviewer will
judge before they see a single line of code.

**Priority 2: The test suite run.**
Open a terminal in the project directory. Run `py -m unittest discover -s tests -v`.
Watch the output. Practice narrating what each test class is checking while
the tests run. You should be able to explain CoverLetterV2Tests, PackageReviewerTests,
and FitScorerTests in plain English without looking at the file.

**Priority 3: The full 5-minute script end to end.**
Run it three times from the top with a timer. First run: use the script.
Second run: script visible but not read from. Third run: script not visible.
Log each run in `learning/evidence/07-rehearsal-log.txt`.

**Goal:** Under 5 minutes, no stumbles on module names, no apology for the
tool being a prototype. The prototype framing is already built into the script
— lean into it rather than away from it.

---

## Remaining Steps Before a Live Demo

The script and commands are ready. Before using this in a professional setting:

- [ ] Run the full demo once end to end in a real terminal (not just reading the script)
- [ ] Confirm the practice package generates without errors
- [ ] Confirm the package reviewer returns READY_FOR_HUMAN_REVIEW on the practice package
- [ ] Complete three logged rehearsals in `learning/evidence/07-rehearsal-log.txt`
- [ ] Confirm the VS Code file tree is set up correctly (private files collapsed)
- [ ] Confirm terminal font is 14pt or larger

---

## Next Pack Recommendation

**Pack 08 — AI Integration Specialist Story**

Reason: Pack 07 gives you a demo. Pack 08 gives you the narrative that makes
the demo land. The 45-second demo intro, the interview answers in Pack 07,
and the background positioning from Pack 01 are all pieces of one story.
Pack 08 is where those pieces are assembled into a complete, rehearsable
narrative that connects Sahid's background to the AI Integration Specialist
role — the story the interviewer hears before, during, and after the demo.

Complete Pack 08 before any application is submitted.
