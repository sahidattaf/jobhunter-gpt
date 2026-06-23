# Privacy Rules — JobHunterGPT Public Website

These rules apply to the Vercel site, any GitHub Pages version, any screenshots,
any screen recordings, and any content published anywhere that references
JobHunterGPT publicly.

Violation of any rule below exposes private contact information or creates
false impressions about the system's capabilities.

---

## Files That Must Never Appear on the Public Site

| File / Folder | Why |
|--------------|-----|
| `config/candidate_profile.json` | Contains private phone, email, and personal details |
| `resumes/master_resume.txt` | Contains private contact information |
| `data/applications.csv` | Contains history of real job applications |
| `job_descriptions/first-job-description.txt` | Real employer job description — not for public reproduction |
| `applications/proofpoint-ai-integration-specialist-customer-office/` | Contains private phone/email in `resume-review.txt` |
| `applications/*/resume-review.txt` | All resume-review files preserve the source resume verbatim |
| `learning/evidence/` | Personal rehearsal logs — not for public view |
| Any `.env` file | Secrets and API keys |
| `config/candidate_profile.example.json` | Safe to show — this is the public example file |

---

## Content That Must Not Appear in Copy

| Content | Why |
|---------|-----|
| Sahid's private phone number | Private |
| Sahid's private email address | Private — use LinkedIn or a contact form |
| Certificate IDs (Coursiv) | Per certificate agreement — keep private |
| Specific employer names from real applications | Could reveal confidential job search activity |
| Fit score from the Proofpoint application | Fine to mention 35/100 as an honest example — but do not name the specific Proofpoint role or reveal the application was submitted |
| Any invented experience or capability | Violates honesty guardrails across all packs |

---

## Screenshot Rules

Before taking any screenshot for the website:

- [ ] Terminal history is cleared (`cls`)
- [ ] `config/candidate_profile.json` is closed in VS Code
- [ ] `resumes/master_resume.txt` is closed in VS Code
- [ ] `data/applications.csv` is closed in VS Code
- [ ] `applications/proofpoint-ai-integration-specialist-customer-office/` is collapsed
- [ ] Only the practice package is open: `applications/gpt-innovation-by-attaf-ai-automation-specialist/`
- [ ] No private phone number, email, or address is visible anywhere in the screenshot
- [ ] The screenshot is reviewed at 100% zoom before publishing

---

## Claims the Site Must Not Make

| Claim | Why not |
|-------|---------|
| "Production-ready system" | JobHunterGPT is a local prototype |
| "Enterprise AI platform" | Not built for enterprise use |
| "Integrated with [any employer]" | Not true |
| "Used by multiple users" | Single-user local system |
| "Salesforce / Jira / Amazon Q integration" | No such integration exists |
| "Guaranteed ATS keyword match" | The fit scorer is a heuristic, not a guarantee |
| "AI-powered cover letters that get interviews" | No verified outcome data |
| College degree | Not confirmed |
| Expert-level AI certification | Coursiv certificates are course certificates only |

---

## Claims the Site Can Make

| Claim | Evidence |
|-------|---------|
| "Human-in-the-loop Python prototype" | Verified — the code exists and runs |
| "8 Python modules" | Verified — repository structure |
| "70 automated tests" | Verified — test suite passes |
| "Never submits applications automatically" | Verified — no submission code exists |
| "Keyword extraction, fit scoring, cover letter generation, package review" | Verified — real modules |
| "Local, gitignored private data" | Verified — .gitignore is committed |
| "Built by Sahid Attaf, Willemstad, Curaçao" | Verified |
| "5 years of AI workflow experience" | Confirmed 2026-06-22 |
| "Coursiv AI tool training in Claude and Gemini, June 2026" | Verified certificates |
| "Open to remote AI integration roles" | Confirmed |

---

## GitHub Repository Rules Before Going Public

Before making the repository public:

- [ ] Confirm `.gitignore` excludes all private files
- [ ] Run `git status` — no private files in staged or tracked state
- [ ] Run `git log --all --full-history -- "config/candidate_profile.json"` — confirm never committed
- [ ] Run `git log --all --full-history -- "resumes/master_resume.txt"` — confirm never committed
- [ ] Run `git log --all --full-history -- "data/applications.csv"` — confirm never committed
- [ ] Confirm `config/candidate_profile.example.json` exists and contains only placeholder data
- [ ] Remove any hardcoded phone numbers or emails from all committed Python files
- [ ] Review README for any accidental private data

---

## Vercel Environment Variables

If the site uses any server-side functionality in a future version:

- [ ] No private data stored in Vercel environment variables that appears in client-side output
- [ ] API keys (if added later) stored in Vercel env vars — never hardcoded in source
- [ ] No Vercel function reads from private local files — they do not exist on Vercel servers

---

## Contact Page Rules

- Public LinkedIn URL only — no private email on the public page
- Public GitHub URL only
- No private phone number
- If a contact form is added: use a form service (Formspree, Resend) that keeps the private email server-side
