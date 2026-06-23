# Vercel Deployment Checklist — JobHunterGPT

Step-by-step checklist for deploying the JobHunterGPT public portfolio site
to Vercel. Complete every step in order. Do not skip the privacy check.

---

## Phase 1 — Local Preparation

### 1.1 Run the test suite

```powershell
py -m unittest discover -s tests -v
```

All 70 tests must pass before any deployment step begins.
If any test fails, fix the code first.

- [ ] 70 tests pass

### 1.2 Privacy check — confirm private files are gitignored

Run these four commands. Each must return empty output (no matches):

```powershell
git log --all --full-history -- "config/candidate_profile.json"
git log --all --full-history -- "resumes/master_resume.txt"
git log --all --full-history -- "data/applications.csv"
git log --all --full-history -- "job_descriptions/first-job-description.txt"
```

- [ ] No results for candidate_profile.json
- [ ] No results for master_resume.txt
- [ ] No results for applications.csv
- [ ] No results for first-job-description.txt

### 1.3 Confirm .gitignore is correct

```powershell
git status
```

Confirm these paths are NOT in the "Changes not staged" or "Untracked files" list
(they should be silently ignored):

- [ ] `config/candidate_profile.json` not visible
- [ ] `resumes/master_resume.txt` not visible
- [ ] `data/applications.csv` not visible
- [ ] `applications/proofpoint-ai-integration-specialist-customer-office/` not visible

### 1.4 Confirm example profile exists and is safe

```powershell
type "config\candidate_profile.example.json"
```

- [ ] File exists
- [ ] Contains only placeholder values (no real phone, email, or address)

---

## Phase 2 — Build the Static Site

### Option A: Plain HTML/CSS (simplest — no framework required)

Create a `web/` folder in the repository root with:

```
web/
├── index.html          (Home)
├── demo.html           (Demo)
├── how-it-works.html   (How It Works)
├── proof.html          (Proof of Work)
├── roadmap.html        (Learning Roadmap)
├── contact.html        (Contact)
├── style.css
└── assets/
    ├── demo-screenshot-tests.png   (safe: 70 tests passing)
    └── demo-screenshot-reviewer.png (safe: READY_FOR_HUMAN_REVIEW)
```

Vercel deploys this automatically from the `web/` folder using its Static
output settings.

### Option B: Next.js (if adding interactive features later)

```powershell
npx create-next-app@latest web --typescript --tailwind --no-app
```

Add pages: `web/pages/index.tsx`, `demo.tsx`, `how-it-works.tsx`, etc.

Only use Option B if interactivity (contact form, live terminal output)
is needed. Option A is sufficient for a portfolio page.

### Screenshot assets (before building)

Take all screenshots following the rules in `web-plan/privacy-rules.md`:

- [ ] Terminal cleared (`cls`) before each screenshot
- [ ] VS Code has all private files closed
- [ ] Test suite screenshot: `py -m unittest discover -s tests -v` → 70 tests OK
- [ ] Reviewer screenshot: practice package only → READY_FOR_HUMAN_REVIEW
- [ ] Each image reviewed at 100% zoom for private data before saving

---

## Phase 3 — GitHub Setup

### 3.1 Make the repository public

Before making public:

- [ ] All privacy checks in Phase 1 complete
- [ ] No hardcoded private phone/email in any `.py` or `.html` file
- [ ] README reviewed — no private contact data

GitHub: Settings → Danger Zone → Change repository visibility → Public

### 3.2 Commit the web folder

```powershell
git add web/
git status   # review — confirm no private files included
git commit -m "add: public portfolio site files"
```

- [ ] Only `web/` folder files in the commit
- [ ] No private files accidentally staged

### 3.3 Push to main

```powershell
git push origin main
```

- [ ] Push confirmed

---

## Phase 4 — Vercel Deployment

### 4.1 Connect Vercel to the GitHub repository

1. Go to vercel.com → Add New Project
2. Select the `jobhunter-gpt` repository
3. Framework Preset: **Other** (for plain HTML) or **Next.js** (if using Next)
4. Root Directory: `web` (the folder containing index.html or package.json)
5. Build Command: leave blank for plain HTML; `npm run build` for Next.js
6. Output Directory: `.` for plain HTML; `out` for Next.js static export

- [ ] Project connected
- [ ] Root directory set to `web`
- [ ] Build settings confirmed

### 4.2 Set the domain

Default: `[project-name].vercel.app`

Optional custom domain: add under Project → Settings → Domains.
Recommended custom domain pattern: `jobhuntergpt.dev` or `sahidattaf.dev`

- [ ] Domain confirmed and accessible

### 4.3 Verify the live site

Open the Vercel URL and check each page:

- [ ] / — Home loads, headline visible, two CTAs work
- [ ] /demo — Demo page loads, no private data visible
- [ ] /how-it-works — Architecture section loads
- [ ] /proof — GitHub link works, screenshots load
- [ ] /roadmap — Pack table loads with accurate statuses
- [ ] /contact — LinkedIn and GitHub links work, no private phone or email visible

### 4.4 Final privacy scan on the live site

On the live site, use browser search (Ctrl+F) on each page for:

- [ ] No phone number pattern: `+`, `(`, or digit strings longer than 8 digits
- [ ] No email pattern: `@` not followed by linkedin.com or github.com
- [ ] No "Proofpoint" in a context that reveals a specific application
- [ ] No "Certificate ID" or Coursiv certificate ID numbers
- [ ] No path strings revealing local machine structure

---

## Phase 5 — GitHub Workflow for Future Updates

When making site updates after initial deployment:

```powershell
# 1. Make changes in web/ folder
# 2. Run test suite (always, even for site-only changes)
py -m unittest discover -s tests -v

# 3. Review changes
git status
git diff

# 4. Stage only site files
git add web/

# 5. Commit
git commit -m "update: [describe what changed on the site]"

# 6. Push — Vercel auto-deploys on push to main
git push origin main
```

Vercel automatically redeploys within ~30 seconds of a push to main.

---

## Rollback if Something Goes Wrong

In Vercel dashboard: Project → Deployments → find the last good deployment →
click the three-dot menu → Promote to Production.

This instantly reverts the live site to a previous version without touching
the GitHub repository.

---

## What This Site Does NOT Need

- A database (no user data collected)
- Authentication (public portfolio)
- A backend server (static site is sufficient)
- Cookie consent banner (if using Vercel Analytics privacy mode)
- A CDN setup (Vercel handles CDN automatically)
