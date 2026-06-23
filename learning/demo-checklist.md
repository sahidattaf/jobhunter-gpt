# JobHunterGPT 5-Minute Demo Checklist

Use this checklist before every professional demo (interview, portfolio review,
screen share). Do not skip steps. A failed demo is worse than no demo.

---

## Pre-Demo Environment Check (Run 15 Minutes Before)

**System**
- [ ] Python is installed and `py --version` returns a version number
- [ ] Working directory is: `C:\Users\sahid\OneDrive\Documents\jobhunter-gpt`
- [ ] All 70 tests pass: `py -m unittest discover -s tests -v`

**Files**
- [ ] `config/candidate_profile.json` exists and is valid JSON
- [ ] `resumes/master_resume.txt` exists and is NOT a placeholder
- [ ] `job_descriptions/practice-job-description.txt` exists with real content
- [ ] There are no leftover `[ERROR]` packages in `applications/` from previous runs
- [ ] `data/applications.csv` exists (can be empty)

**Privacy**
- [ ] `config/candidate_profile.json` is NOT visible on screen
- [ ] `resumes/master_resume.txt` tab is CLOSED in VS Code
- [ ] `data/applications.csv` tab is CLOSED in VS Code
- [ ] Any real `applications/` folders (Proofpoint etc.) are COLLAPSED in file tree
- [ ] `.env` is not open in any visible tab

**Terminal**
- [ ] Terminal font size is 14pt or larger
- [ ] Terminal background is dark (readable in screen share)
- [ ] Working directory is set to the project root
- [ ] Previous command history is cleared: `cls` (Windows) or `clear` (Mac/Linux)

---

## Demo Run Commands (Copy-Paste Ready)

**Step 1 — Validate the profile:**
```
py -c "from candidate_profile import load_profile; from pathlib import Path; p = load_profile(Path('config/candidate_profile.json')); print('Profile valid:', p['full_name'])"
```

**Step 2 — Generate a practice package:**
```
py -m job_search_agent --resume resumes/master_resume.txt --job job_descriptions/practice-job-description.txt --company "GPT Innovation by Attaf" --title "AI Automation Specialist" --url "https://www.gptinnovationbyattaf.com" --profile config/candidate_profile.json
```

**Step 3 — Run the package reviewer (replace FOLDER with actual output folder name):**
```
py -m package_reviewer applications/FOLDER
```

---

## 5-Minute Demo Script (Condensed)

| Time | Action | What to say |
|------|--------|-------------|
| 0:00 | Open README.md | "This is JobHunterGPT — a human-in-the-loop AI job search system I built in Python. The key word is human-in-the-loop: it never applies to anything automatically." |
| 0:30 | Show practice JD | "Here's a job description. The system reads this to extract keywords and score fit. I paste this in manually — no scraping." |
| 1:00 | Run generate command | "I run one command. It reads my resume, the job description, and my verified profile. It generates a package." |
| 1:30 | Open output folder | "Three files: cover letter, fit score report, resume review. Let me show you each." |
| 2:00 | Open cover-letter.txt | "The cover letter is built from verified facts only — nothing I can't back up in an interview. I check it before sending." |
| 2:45 | Open application-details.txt | "The fit score tells me honestly how well I match. This one scores high because it's my own practice role. On a real JD it scored 35/100 — and that honesty is a feature." |
| 3:15 | Run package reviewer | "Before I touch anything, I run a reviewer module that flags errors and warnings. RED means stop. YELLOW means review." |
| 3:45 | Show reviewer output | "READY_FOR_HUMAN_REVIEW. That's the signal I need to start human editing. The system never decides for me." |
| 4:15 | Close terminal | "The whole thing runs on Python stdlib — no API keys needed for the core pipeline. I can extend it with Claude API for richer output." |
| 4:30 | Summary | "It's a personal tool. It doesn't scale to enterprise without a database backend, auth, and multi-user support — but it demonstrates the pattern I would apply." |
| 5:00 | End | "Happy to walk through the code or answer questions about any specific module." |

---

## If Something Goes Wrong

**Test fails:** Stop. Do not demo broken code. Fix the test first.
**Command not found:** Check you're in the right directory. Run `py --version` first.
**Profile invalid:** Check `config/candidate_profile.json` is not a placeholder.
**Package reviewer fails:** Check the folder name is correct (exact folder from Step 2).
**Screen share lag:** Run the commands before sharing, then narrate what happened.

---

## After the Demo

- [ ] Close any tabs showing private files
- [ ] Clear terminal history if the machine will be left unlocked
- [ ] Note any questions the interviewer asked that you couldn't answer
- [ ] Update `learning/evidence/07-rehearsal-log.txt` with what happened

---

## Demo Readiness Status

Complete Pack 07 before using this checklist in a professional setting.
Mark as demo-ready only when all pre-demo checks pass AND three rehearsals
are logged in `learning/evidence/07-rehearsal-log.txt`.

**Current status: NOT DEMO READY — Pack 07 not started**
