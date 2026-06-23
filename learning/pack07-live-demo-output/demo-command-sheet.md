# Demo Command Sheet — JobHunterGPT

Quick reference for all commands used in the 5-minute demo.
Copy and paste directly. Do not type from memory during a live demo.

**Legend:**
- SAFE FOR SCREEN SHARE — shows no private data
- LOCAL ONLY — run before the call, not during
- DEMO STEP — use during the screen-share demo in order

---

## Setup: Navigate to Project Root

```powershell
cd "C:\Users\sahid\OneDrive\Documents\jobhunter-gpt"
```

**Proves:** You know where the project lives and how it's structured.
Run this first in any terminal session.

---

## Command 1 — Run the Full Test Suite

**When to run:** During demo at the [2:00] mark. SAFE FOR SCREEN SHARE.

```powershell
py -m unittest discover -s tests -v
```

**What it proves:**
- The system has 70 automated tests covering all modules.
- All tests pass as of the current version.
- Each module (profile validation, cover letter generation, fit scoring,
  package generation, package review, tracker) is independently tested.
- Test-driven development is a real practice, not a claim.

**Expected output:**
```
Ran 70 tests in X.Xs
OK
```

**If it shows FAIL:** Stop the demo. Do not proceed. Fix the failing test first.

---

## Command 2 — Run the Package Reviewer (Practice Package)

**When to run:** During demo at the [4:00] mark. SAFE FOR SCREEN SHARE.
Use the PRACTICE package, not the Proofpoint folder.

```powershell
py -m package_reviewer `
  "applications\gpt-innovation-by-attaf-ai-automation-specialist" `
  --candidate-name "Sahid Attaf"
```

**What it proves:**
- The package reviewer module runs without errors.
- The generated practice package passes all 10 structural checks.
- The reviewer correctly identifies the candidate name in the cover letter.
- READY_FOR_HUMAN_REVIEW is the correct output — it means the human can
  now open the files and make editorial decisions.

**Expected output:**
```
PACKAGE REVIEW REPORT
=====================
Package : ...\applications\gpt-innovation-by-attaf-ai-automation-specialist
Status  : READY_FOR_HUMAN_REVIEW

Files found  (3): cover-letter.txt, application-details.txt, resume-review.txt
Files missing (0): none

No issues found. Package is ready for human review.

NEXT STEP: Open each file in the package folder, read every line, and confirm
all claims are accurate before use.
```

**If it shows NEEDS_FIXES:** Stop the demo. The pre-demo check was not done correctly.

---

## Command 3 — Run the Package Reviewer (Proofpoint — LOCAL ONLY)

**When to run:** LOCAL ONLY — before the demo call to verify the module works.
Do NOT show this on screen — the Proofpoint folder contains private resume/email data.

```powershell
py -m package_reviewer `
  "applications\proofpoint-ai-integration-specialist-customer-office" `
  --candidate-name "Sahid Attaf"
```

**What it proves locally:**
- The Proofpoint package was generated correctly.
- The reviewer validates a real (non-practice) package.
- Useful to verify the system works end-to-end before the call.

**Do not show:** The output reveals the resume section preserved in resume-review.txt,
which includes private phone and email. Run only in a private terminal session.

---

## Command 4 — Check Git Status

**When to run:** During demo if the interviewer asks about version control.
SAFE FOR SCREEN SHARE — private files are gitignored and will not appear.

```powershell
git status
```

**What it proves:**
- The project is under version control.
- Private files (`config/candidate_profile.json`, `resumes/master_resume.txt`,
  `data/applications.csv`, all `applications/` content) are gitignored.
- The public repository contains no private personal data.

**Expected output (approximately):**
```
On branch main
Your branch is up to date with 'origin/main'.

Untracked files:
  learning/

nothing added to commit but untracked files present
```

Private files will NOT appear in the output — that absence is the proof.

---

## Command 5 — Validate Profile (Optional, if asked)

**When to run:** Only if the interviewer specifically asks how the profile
validation works. SAFE FOR SCREEN SHARE — prints only the name, not private fields.

```powershell
py -c "from candidate_profile import load_profile; from pathlib import Path; p = load_profile(Path('config/candidate_profile.json')); print('Profile valid:', p['full_name'])"
```

**What it proves:**
- The profile loads and validates without error.
- The `full_name` field is set (prints on screen).
- The validation module catches invalid profiles before they reach the pipeline.

**Expected output:**
```
Profile valid: Sahid Attaf
```

**Warning:** This command prints only the name. Do NOT modify the command to
print other fields — phone and email are private.

---

## Command 6 — Generate a Practice Package (Optional Extension)

**When to run:** Only if the interviewer wants to see the full pipeline run live.
SAFE FOR SCREEN SHARE — uses the practice company, not a real application.
The practice job description must exist at the path below.

```powershell
py -m job_search_agent `
  --resume resumes\master_resume.txt `
  --job job_descriptions\practice-job-description.txt `
  --company "GPT Innovation by Attaf" `
  --title "AI Automation Specialist" `
  --url "https://www.gptinnovationbyattaf.com" `
  --profile config\candidate_profile.json
```

**What it proves:**
- The full end-to-end pipeline runs without errors.
- All modules are wired together correctly.
- The output package is created in `applications/` automatically.

**Warning:** This will print the generated folder path to the terminal.
The resume content is read internally but not printed to the screen.
After running, do not open the generated folder during the screen share
until you verify it does not include private contact details in visible
file names or tab titles.

---

## Quick Reference: Demo Step Order

| Step | Time | Command | Screen safe? |
|------|------|---------|-------------|
| Setup | Before call | `cd` to project | Yes |
| Pre-check | Before call | `py -m unittest discover -s tests -v` | Yes |
| Demo Step 1 | 2:00 | `py -m unittest discover -s tests -v` | Yes |
| Demo Step 2 | 4:00 | `py -m package_reviewer "applications\gpt-innovation..."` | Yes |
| Optional | If asked | Profile validation command | Yes (name only) |
| Optional | If asked | `git status` | Yes |
| Local only | Before call | Proofpoint reviewer command | NO — private data |
