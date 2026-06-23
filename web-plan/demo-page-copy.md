# Demo Page Copy — JobHunterGPT

Public-safe. All screenshots and recordings must use the practice package only.
The Proofpoint application folder contains private contact data — never shown.
Review against privacy-rules.md before publishing.

---

## Meta

**Page title:** JobHunterGPT — Live Demo
**Meta description:** See JobHunterGPT run: test suite, package generation,
and structural review — a 5-minute screen share of a working AI workflow pipeline.

---

## Hero Section

**Headline:**
See it run.

**Subheadline:**
JobHunterGPT is a working Python prototype. Here is what a 5-minute demo looks like.

---

## What the Demo Shows

Five things the demo covers, in order:

**1. Repository structure (0:30 – 1:15)**
The README architecture overview. Eight modules, each doing one thing.
No black-box AI — every step is readable Python code.

**2. Private data concept without exposing data (1:15 – 2:00)**
The system is driven by a private candidate profile stored locally and gitignored.
The demo uses the public example file — `config/candidate_profile.example.json` —
so no private contact information appears on screen.

**3. Test suite: 70 tests, all passing (2:00 – 3:00)**
`py -m unittest discover -s tests -v` — run live.
Covers all eight modules: profile validation, cover letter generation, fit scoring,
package generation, and package reviewer checks.

**4. Practice package structure (3:00 – 4:00)**
Three output files from a practice run:
- `application-details.txt` — company, role, fit score
- `cover-letter.txt` — generated from verified facts only
- `resume-review.txt` — ATS keyword report with source resume preserved

**5. Package reviewer output (4:00 – 4:45)**
`py -m package_reviewer "applications\[practice-package]" --candidate-name "Sahid Attaf"`
Returns: READY_FOR_HUMAN_REVIEW

**Close (4:45 – 5:00)**
"I don't have enterprise platform experience yet, but I can show you the work
directly — how I built it, how I tested it, and how I improve it."

---

## Screenshot Placeholder: Test Suite Output

[Insert screenshot of terminal showing 70 tests passing]

Requirements for screenshot:
- Must show `Ran 70 tests in X.Xs` and `OK`
- Working directory must not show private folder names
- Terminal history must be cleared before screenshot (`cls`)
- No private file paths visible in output

---

## Screenshot Placeholder: Package Reviewer Output

[Insert screenshot of READY_FOR_HUMAN_REVIEW terminal output]

Requirements:
- Must use the practice package: `gpt-innovation-by-attaf-ai-automation-specialist`
- Must NOT use: `proofpoint-ai-integration-specialist-customer-office`
- No private phone number or email visible anywhere in the output

---

## Example Output (Sanitized)

What `application-details.txt` looks like from the practice package:

```
Company: GPT Innovation by Attaf
Role: AI Automation Specialist
Fit Score: [high — practice company, matching profile]
Source JD: [practice job description]
Date: [run date]
Status: READY_FOR_HUMAN_REVIEW
```

No private phone, email, or resume text appears in this file.

---

## What Is NOT Shown in the Demo

This section must appear somewhere on the demo page — transparency builds trust.

- Private candidate profile (`config/candidate_profile.json`) — gitignored, local only
- Real resume (`resumes/master_resume.txt`) — never on screen
- Real application packages — only the practice package is used in demos
- Real job descriptions from specific employers — only practice descriptions used
- Any private contact information

---

## Request a Live Demo

**Heading:** Want to see it run live?

**Body:**
The 5-minute demo runs in a private screen share. I walk through the full
pipeline — architecture, tests, output package, and reviewer — using the
practice package only. No private data appears on screen.

Available for: Technical interviews, portfolio reviews, AI platform team
introductions, or anyone evaluating AI workflow design thinking.

**CTA:** [Contact Sahid →]  links to /contact

---

## What a Live Demo Is Not

- Not a commercial product demonstration
- Not a promise of enterprise readiness
- Not a simulation — the code runs live, in a real terminal, on Python's standard library
- Not affiliated with any ATS platform, job board, or employer

---

## Terminal Commands Used in the Demo

These are the only commands that run in a live demo.
No private data paths are used in screen-share mode.

```powershell
# 1. Confirm working directory
cd "C:\Users\sahid\OneDrive\Documents\jobhunter-gpt"

# 2. Run full test suite (SAFE FOR SCREEN SHARE)
py -m unittest discover -s tests -v

# 3. Run package reviewer on practice package (SAFE FOR SCREEN SHARE)
py -m package_reviewer `
  "applications\gpt-innovation-by-attaf-ai-automation-specialist" `
  --candidate-name "Sahid Attaf"

# 4. Check git status (SAFE FOR SCREEN SHARE)
git status
```
