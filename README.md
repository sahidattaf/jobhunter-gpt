# JobHunterGPT
## Live Demo

Public portfolio site: https://jobhunter-gpt-gamma.vercel.app/
JobHunterGPT is a human-in-the-loop AI job-search operating system. It helps a candidate discover suitable roles, analyze job descriptions, extract ATS keywords, tailor truthful application materials, and track applications without submitting anything automatically.

## Guardrails

- Never invent experience, qualifications, education, certifications, or metrics.
- Never submit an application without the candidate's explicit approval.
- Respect job-board terms, robots rules, and rate limits.
- Store secrets only in environment variables.
- Prefer qualified, tailored applications over indiscriminate volume.

## Repository structure

```text
jobhunter-gpt/
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── claude_prompt.md
├── candidate_profile.py       ← load and validate config/candidate_profile.json
├── fit_scorer.py              ← score keyword/skill/location/remote fit (0-100)
├── job_search_agent.py        ← orchestrator: read files → generate package → log
├── keyword_extractor.py       ← ATS keyword extraction
├── resume_optimizer.py        ← ATS review draft with preserved source resume
├── coverletter_generator.py   ← conservative cover-letter draft
├── tracker.py                 ← CSV application log
├── config/
│   └── candidate_profile.example.json   ← copy → candidate_profile.json (gitignored)
├── prompts/
│   ├── keyword_extractor_prompt.md
│   └── resume_optimizer_prompt.md
├── resumes/                   ← place master_resume.txt here
├── job_descriptions/          ← place one .txt per approved job posting
├── applications/              ← generated review packages (gitignored)
├── cover_letters/             ← generated cover letters (gitignored)
├── data/
│   ├── applications.csv       ← auto-created tracker
│   └── google_sheet_template.csv
└── tests/
    └── test_core.py
```

## Quick start (Windows)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
py -m unittest discover -s tests -v
```

## Set up your candidate profile

```powershell
copy config\candidate_profile.example.json config\candidate_profile.json
```

Open `config\candidate_profile.json` and replace every field with your real, verified
information. This file is listed in `.gitignore` and will never be committed.

## Extract keywords

```powershell
py keyword_extractor.py --input job_descriptions\example.txt --output data\keywords.txt
```

## Prepare a local application package

```powershell
py job_search_agent.py `
  --resume resumes\master_resume.txt `
  --job job_descriptions\example-company-ai-specialist.txt `
  --company "Example Company" `
  --title "AI Automation Specialist" `
  --url "https://example.com/jobs/123" `
  --profile config\candidate_profile.json
```

The workflow:

1. Reads your resume and the job description.
2. Extracts ATS keywords and reports matches and gaps.
3. Calculates a fit score (0-100) across keyword overlap, verified skills, location, and
   remote preference.
4. Generates a resume review draft and a cover-letter draft in
   `applications\<company-slug>\`.
5. Appends a row — including the fit score — to `data\applications.csv`.
6. **Does not submit anything.**  Review all files before taking any action.

## Review a generated package

Before using any generated file, run the package reviewer to catch structural issues,
placeholder text, missing fields, and short cover letters:

```powershell
py -m package_reviewer applications\gpt-innovation-by-attaf-ai-automation-specialist `
  --candidate-name "Sahid Attaf"
```

The reviewer checks:

- All required files are present
- Company name and job title appear in the cover letter
- No placeholder text ("Candidate Name", "Company Name", etc.)
- Fit score and source URL are recorded
- Source resume is preserved in the ATS review
- Cover letter meets minimum length
- No raw keyword dump patterns

Returns `READY_FOR_HUMAN_REVIEW` (exit 0) or `NEEDS_FIXES` (exit 1).

## Run tests

```powershell
py -m unittest discover -s tests -v
```

## Google Sheets

Import `data/google_sheet_template.csv` into Google Sheets. The CSV columns match the
local tracker and can later be synchronized through an approved Google service account
integration.

## Claude Code

Open this repository in VS Code and paste `claude_prompt.md` into Claude Code. The
prompt instructs Claude to inspect, test, and improve the project without fabricating
candidate data or enabling blind mass applications.
