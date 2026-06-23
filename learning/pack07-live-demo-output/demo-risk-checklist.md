# Demo Risk Checklist — JobHunterGPT Screen Share

Read before every professional screen share. Private data exposure in an
interview is not recoverable. Do not skip steps.

---

## Private Information at Risk

These files and fields must never appear on screen during a demo:

| File / Field | Risk | Why private |
|-------------|------|------------|
| `config/candidate_profile.json` | Phone number, email, LinkedIn URL visible | gitignored private file |
| `resumes/master_resume.txt` | Phone, email, full address | gitignored private file |
| `data/applications.csv` | Real company names, application status, file paths | gitignored private file |
| `applications/proofpoint-*/resume-review.txt` | Phone and email in preserved resume section | generated from private resume |
| `applications/proofpoint-*/cover-letter.txt` | Could reveal real job-search status to interviewer | real application in progress |
| Certificate IDs (3YHEAIIC, ATGJX3O6) | Private identifiers | not for public sharing |
| LinkedIn tracking URL in application-details.txt | Long tracking URL reveals browsing data | private job search signal |
| `.env` file | May contain API keys or secrets | never shown to anyone |

---

## Pre-Demo Checklist (Run 15 Minutes Before the Call)

### System checks

- [ ] Python installed: run `py --version` — confirm it returns a version number
- [ ] Working directory set: `cd "C:\Users\sahid\OneDrive\Documents\jobhunter-gpt"`
- [ ] 70 tests pass: `py -m unittest discover -s tests -v` — must show `OK`
- [ ] Practice package exists: `applications\gpt-innovation-by-attaf-ai-automation-specialist\`
- [ ] Practice package passes reviewer: run local-only reviewer command, confirm READY_FOR_HUMAN_REVIEW
- [ ] Terminal history cleared: run `cls`
- [ ] Terminal font size 14pt or larger (readable in screen share)

### Privacy checks (VS Code)

- [ ] `config/candidate_profile.json` — tab CLOSED in VS Code
- [ ] `resumes/master_resume.txt` — tab CLOSED in VS Code
- [ ] `data/applications.csv` — tab CLOSED in VS Code
- [ ] `.env` — tab CLOSED in VS Code (if it exists)
- [ ] `applications/proofpoint-ai-integration-specialist-customer-office/` — folder COLLAPSED in file tree
- [ ] Any other real `applications/` subfolders — COLLAPSED in file tree
- [ ] `config/candidate_profile.json` — COLLAPSED in file tree
- [ ] `resumes/master_resume.txt` — COLLAPSED in file tree

### Privacy checks (file tree view)

The file tree visible during the demo should show ONLY:
```
jobhunter-gpt/
├── README.md
├── *.py files
├── config/
│   └── candidate_profile.example.json  (NOT the real .json)
├── applications/
│   └── gpt-innovation-by-attaf-ai-automation-specialist/
│       ├── application-details.txt
│       ├── cover-letter.txt
│       └── resume-review.txt
├── learning/
├── tests/
└── ...
```

Real application folders and private files should not be visible.

### Content checks before opening any file on screen

Before opening a file during the demo, ask: "Does this file contain
phone numbers, email addresses, or private contact information?"

- `README.md` — Safe to show (no private data)
- `config/candidate_profile.example.json` — Safe to show (no real data)
- `*.py` module files — Safe to show (no private data)
- `tests/test_core.py` — Safe to show (uses test data, not real data)
- `applications/gpt-innovation-by-attaf-*/cover-letter.txt` — Safe (practice company)
- `applications/gpt-innovation-by-attaf-*/application-details.txt` — Verify first: fit score and practice URL only, no phone/email
- `applications/gpt-innovation-by-attaf-*/resume-review.txt` — CAUTION: check if preserved resume section includes phone/email

For the practice package resume-review.txt: if it contains phone/email from
the master resume, do not open it on screen. Show the cover letter and
application-details.txt instead.

---

## What Not to Claim During the Demo

These statements are false and must not be made:

| Do not say | Why |
|------------|-----|
| "This is production-ready" | It is a local prototype |
| "This scales to enterprise" | It is a single-user local tool |
| "I've integrated this with Proofpoint" | Not true |
| "The demo shows enterprise AI platform experience" | It shows local workflow design experience |
| "I've applied to jobs using this" | Confirm before saying; system is human-in-the-loop |
| "The app submitted my Proofpoint application" | It did not; application is not submitted |
| "I have cybersecurity experience" | Not in resume or profile |
| "I've used Amazon Q" | Not true |
| "This is running on a real database" | It uses CSV tracking |

---

## Fallback Plan If Something Fails

### Test suite fails during demo

**Say:** "Let me look at that — one moment."
Open the terminal. Check the error message. If it is a known environment
issue (wrong directory, missing file), fix it once and rerun.

If it cannot be fixed quickly: "The tests are failing in this environment —
let me show you the module structure and walk through what each test validates
instead."

Navigate to `tests/test_core.py` and walk through the test class names.
This still demonstrates test coverage design, even without a passing run.

### Package reviewer returns NEEDS_FIXES during demo

**Say:** "The reviewer is flagging an issue with the package. That's the
system working correctly — it's blocking a package that isn't clean."

Explain what the [ERROR] means. Show that you understand the design.
If time allows, fix the issue and rerun. Do not apologize excessively.

### Terminal is too small or unreadable on screen share

**Say:** "Let me increase the font size."
In Windows Terminal: `Ctrl+Shift++` to increase font size.
In VS Code integrated terminal: `Ctrl+Shift+P` → "Terminal: Increase Font Size"

### Screen share lag makes the command output hard to read

**Say:** "The connection is adding some lag — let me read the relevant parts aloud."
Read the key output lines (Status, test count, READY_FOR_HUMAN_REVIEW) out loud.

### Interviewer asks to see the resume or profile

**Say:** "I'd prefer to keep private contact information off screen — I can
share a sanitized version after the call if that's useful. What I can show
you is the example profile structure and the validation logic in the code."

Open `config/candidate_profile.example.json` and `candidate_profile.py` instead.

---

## After the Demo

- [ ] Close all file tabs opened during the demo
- [ ] Clear terminal history: `cls`
- [ ] Note any questions that were asked that you could not answer
- [ ] Log the rehearsal in `learning/evidence/07-rehearsal-log.txt`
  - Date:
  - Duration:
  - What went well:
  - What to improve:
  - Questions asked by interviewer:
