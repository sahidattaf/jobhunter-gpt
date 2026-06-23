# JobHunterGPT — Public Website Site Map

**Purpose:** Public portfolio page explaining the human-in-the-loop AI job
preparation system. No private candidate data, no application packages, no
resume content, no private job descriptions.

**Audience:** Recruiters, hiring managers, technical interviewers, AI workflow
professionals reviewing Sahid Attaf's portfolio.

---

## Site Structure

```
jobhuntergpt.vercel.app (or custom domain)
│
├── /                   Home
├── /demo               Demo
├── /how-it-works       How It Works
├── /proof              Proof of Work
├── /roadmap            Learning Roadmap
└── /contact            Contact
```

---

## Page Inventory

### / — Home

**Goal:** First impression. Explains what it is, who built it, and why it matters.

Content blocks:
- Hero: headline + one-sentence description + two CTAs (Demo, GitHub)
- What it is: 3-line plain English explanation
- Key stats: 8 modules | 70 tests | human-review at every step | never submits automatically
- Builder intro: Sahid Attaf, AI systems builder, Curaçao — one paragraph
- Design principle: human-in-the-loop explained in one card
- Footer: GitHub link | LinkedIn | Contact

---

### /demo — Demo

**Goal:** Show what the system does in a live or recorded context.

Content blocks:
- What the demo shows: 5-point list (structure, test suite, package folder, reviewer output, improvement roadmap)
- Screengrab or recording placeholder: safe terminal output only — no private profile, no real resume
- Example output: sanitized `application-details.txt` with practice company data only
- What is NOT shown: private profile, real resume, real application packages
- CTA: "Request a live demo" → Contact page

---

### /how-it-works — How It Works

**Goal:** Technical architecture overview for AI/engineering evaluators.

Content blocks:
- Pipeline diagram (text-based): JD → Extractor → Profile → Scorer → Generator → Reviewer → Output
- Eight modules: name + one-line description each
  1. keyword_extractor.py — ATS keyword extraction from job descriptions
  2. fit_scorer.py — 0–100 score across keyword match, skills, location, remote preference
  3. coverletter_generator.py — Letter built from verified resume facts only
  4. package_reviewer.py — 10 structural checks before any output is used
  5. job_search_agent.py — Orchestrator; runs all modules in sequence
  6. candidate_profile_validator.py — Validates the candidate profile against the schema
  7. ats_report_generator.py — Produces the ATS keyword match report
  8. application_tracker.py — Records completed applications to the tracker
- Design decisions: why stdlib-only, why human-review at every step, why no auto-submit
- Data privacy note: profile and resume are local and gitignored

---

### /proof — Proof of Work

**Goal:** Evidence that the system is real, tested, and maintained.

Content blocks:
- GitHub repository link (public)
- Test suite callout: 70 tests, all passing — screenshot of terminal output (safe)
- Package reviewer output: READY_FOR_HUMAN_REVIEW — screenshot (practice package only)
- Code quality notes: stdlib-only, no external dependencies for core pipeline, documented modules
- What it does NOT do: no auto-submit, no data scraping, no external API calls in core pipeline

---

### /roadmap — Learning Roadmap

**Goal:** Shows active learning and honest gap-closing for AI integration roles.

Content blocks:
- 8-pack overview table:
  | Pack | Skill Area | Status |
  |------|-----------|--------|
  | 01 | Degree / Equivalent Experience Positioning | Evidence Ready |
  | 02 | Salesforce Basics | Not Started |
  | 03 | Jira Basics | Not Started |
  | 04 | Cybersecurity Awareness | Not Started |
  | 05 | API / Database / Supabase | Not Started |
  | 06 | Customer Success / TAM | Not Started |
  | 07 | Live Demo Readiness | Evidence Ready |
  | 08 | AI Integration Specialist Story | Evidence Ready |
- Gap acknowledgment paragraph (honest, not defensive)
- Next steps note: Packs 02–06 in progress

---

### /contact — Contact

**Goal:** One clear way to reach Sahid.

Content blocks:
- Name and location: Sahid Attaf, Willemstad, Curaçao
- Role target: AI workflow automation, AI integration, remote-first
- LinkedIn link (public profile)
- GitHub link (public profile)
- One-line invite: "Open to conversations about AI integration, workflow automation, and remote positions."
- No private email on the public page — use a contact form or mailto with public address only

---

## Navigation

Top nav (all pages): Home | Demo | How It Works | Proof | Roadmap | Contact

Footer (all pages): GitHub | LinkedIn | Built by Sahid Attaf | Willemstad, Curaçao

---

## Design Notes

- Static site — no server-side rendering needed
- No login, no database, no user data collected
- No analytics that require cookie consent (optional: use Vercel Analytics, which is privacy-safe)
- All screenshots must be taken from the practice package — never from the Proofpoint folder
- Mobile-responsive required — recruiters often open portfolio links on phones

---

## Files That Must Never Appear on the Site

- config/candidate_profile.json
- resumes/master_resume.txt
- data/applications.csv
- applications/proofpoint-ai-integration-specialist-customer-office/ (contains private phone/email)
- job_descriptions/first-job-description.txt
- Any file in learning/evidence/ (personal rehearsal logs)
