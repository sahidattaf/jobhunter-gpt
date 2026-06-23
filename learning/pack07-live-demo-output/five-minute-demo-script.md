# Five-Minute JobHunterGPT Demo Script

**Version:** Pack 07 — Evidence Ready
**Use for:** Technical interviews, portfolio reviews, screen-share demos
**Total time:** 5 minutes
**Private data shown:** None — all demo steps use public/practice content only

---

## Before You Start

Have these ready before sharing your screen:
- Terminal open, working directory: `C:\Users\sahid\OneDrive\Documents\jobhunter-gpt`
- VS Code open with the project folder visible in the file tree
- `config/candidate_profile.json` collapsed or closed
- `resumes/master_resume.txt` collapsed or closed
- `data/applications.csv` not open
- Any real `applications/` subfolders collapsed in the file tree
- Terminal history cleared: run `cls`
- Tests already confirmed passing before the call

---

## [0:00 – 0:30] Opening: What This Is

**Action:** Face camera / share screen showing terminal or VS Code file tree.

**Say:**
"This is JobHunterGPT — a local Python prototype I built to automate the
preparation side of a job search while keeping a human in the loop at every step.
It reads a job description and a resume, extracts ATS keywords, calculates a fit
score, generates a cover letter draft, and runs a structural reviewer before
anything leaves the system. It never applies to jobs automatically. It never
invents experience. I'll show you how it runs."

**Key phrases used:** local prototype, human-in-the-loop, never applies automatically,
never invents experience.

**Do not say:** production platform, enterprise system, cybersecurity system,
Proofpoint integration, automatic job applier.

---

## [0:30 – 1:15] README: Architecture Overview

**Action:** Open `README.md` in VS Code. Scroll to the repository structure section.

**Say:**
"The repository structure is straightforward. There are eight Python modules —
each does one thing. `keyword_extractor.py` pulls ATS terms from the job
description. `fit_scorer.py` scores keyword overlap, verified skills, location,
and remote preference. `coverletter_generator.py` builds the letter from verified
facts only. `package_reviewer.py` runs structural checks before any file is used.
`job_search_agent.py` is the orchestrator — it calls all of these in sequence and
produces the output package."

**Then scroll to the Quick Start section:**
"It runs on Python's standard library — no external dependencies for the core
pipeline. The tests cover all the main modules."

**What this shows the interviewer:**
Multi-module design. Separation of concerns. Documented architecture.
Independent, self-directed technical decision-making.

---

## [1:15 – 2:00] Private Input Concept (Without Exposing Data)

**Action:** Keep `config/candidate_profile.json` CLOSED. Open
`config/candidate_profile.example.json` instead — this is the safe public version.

**Say:**
"The system is driven by a private candidate profile — stored locally in
`config/candidate_profile.json`, which is gitignored and never committed. I'm
showing the example file here rather than my real profile to keep private
contact information off screen. The profile holds verified skills, preferred
locations, remote preference, and certifications. The keyword extractor and
fit scorer both read from this — so the output is always anchored to what
the candidate has actually stated, not what the AI generates."

**Then show the `.gitignore` briefly:**
"Private files — the real profile, the resume, and all generated application
packages — are excluded from version control by design. The project can be
shared publicly without leaking personal data."

**What this shows the interviewer:**
Data privacy by design. Human-in-the-loop architecture. Responsible AI
workflow thinking — directly relevant to enterprise AI integration roles.

---

## [2:00 – 3:00] Run the Test Suite

**Action:** Switch to terminal. Run:

```powershell
py -m unittest discover -s tests -v
```

**While it runs, say:**
"The test suite covers all eight modules — 70 tests total. Validation tests
for the candidate profile, cover letter generation tests that verify the letter
never contains raw keyword dumps or placeholder names, fit scorer tests, package
generation tests, and package reviewer tests. The reviewer tests specifically
check that ERROR-level issues block the package and WARNING-level issues are
advisory only."

**When it finishes:**
"70 tests, all passing. I run this before and after any change to any module.
No test gets removed to make the suite pass — if something breaks, I fix the
code."

**What this shows the interviewer:**
Test-driven development habits. Confidence in the system. Ability to maintain
and improve a multi-module Python codebase.

---

## [3:00 – 4:00] Show the Generated Package Structure

**Action:** In VS Code file tree, open the practice package folder:
`applications/gpt-innovation-by-attaf-ai-automation-specialist/`

Open `application-details.txt` first.

**Say:**
"When the agent runs, it produces three files in a dated folder. The
`application-details.txt` records the company, role, source URL, and fit score.
This package scored high because I used my own practice company as the target —
which is the honest point. On a real application to Proofpoint, the system
scored 35 out of 100, because the keyword extractor found genuine gaps between
my profile and the job description. That honesty is a feature, not a bug."

**Open `cover-letter.txt`:**
"The cover letter is generated from verified facts only — anything pulled from
the resume or confirmed in the profile. The generator rejects placeholder
candidate names and raw keyword dumps by design. The output is a starting
draft that the candidate reads, edits, and takes ownership of before it goes
anywhere."

**Open `resume-review.txt`:**
"The ATS review shows keyword matches and gaps, and it preserves the source
resume verbatim in the output file. That 'SOURCE RESUME — PRESERVED' section
is a design requirement — the package reviewer checks for it. You always know
what version of the resume was used to generate this package."

**What this shows the interviewer:**
End-to-end AI workflow design. Honest output evaluation. Human-review
philosophy. Attention to data traceability.

---

## [4:00 – 4:45] Run the Package Reviewer

**Action:** Run in terminal. Use the practice package, not the Proofpoint folder:

```powershell
py -m package_reviewer `
  "applications\gpt-innovation-by-attaf-ai-automation-specialist" `
  --candidate-name "Sahid Attaf"
```

**Say:**
"Before any file in a package can be used, it has to pass the reviewer. The
reviewer runs ten structural checks — required files present, company name and
job title in the cover letter, no placeholder text, fit score recorded, source
URL valid, resume section preserved, cover letter long enough, no raw keyword
dump patterns."

**When result appears:**
"READY_FOR_HUMAN_REVIEW. That is the gate. It does not mean the content is
perfect — it means the structure is clean enough for the human to read and
decide. If any ERROR-level check fails, the reviewer returns NEEDS_FIXES and
exits with code 1 — which would stop any automated pipeline downstream."

**What this shows the interviewer:**
Quality control design. Responsible AI output handling. The distinction between
automated structural checks and human content judgment — which maps directly
to the kind of AI workflow quality evaluation enterprise roles require.

---

## [4:45 – 5:00] Close: What This Proves

**Action:** Return to face camera or stay on terminal output.

**Say:**
"To summarize: this is a local Python prototype — eight modules, 70 tests,
human review at every output step. It doesn't submit anything automatically.
It doesn't invent qualifications. It shows I can design, build, test, document,
and improve a multi-step AI workflow independently, and that I think carefully
about what AI should and should not do on a person's behalf.

I don't have enterprise platform experience yet, but I can show you the work
directly — how I built it, how I tested it, and how I improve it.

Happy to go deeper on any module, walk through the test cases, or answer
questions about the design decisions."

---

## Post-Demo Notes

- If the interviewer asks to see the resume or profile: "I'd rather not put
  private contact information on screen — I can share a sanitized version
  by email if that's useful."
- If a test fails during the demo: "Let me re-run that once." Run again.
  If it fails again: "Something changed in the environment — let me show you
  a previous run output." Pull up the output files directly.
- If the reviewer returns NEEDS_FIXES: Stop. Do not proceed. This means
  the pre-demo check was not completed properly.

---

## What This Demo Calls JobHunterGPT

| Accurate term | Avoided term |
|---------------|-------------|
| local prototype | production platform |
| human-in-the-loop | automatic job applier |
| Python-based workflow | enterprise system |
| proof of ability to build AI workflows | Proofpoint integration |
| multi-module application | cybersecurity tool |
