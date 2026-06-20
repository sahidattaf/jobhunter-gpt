# JobHunterGPT

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
├── job_search_agent.py
├── keyword_extractor.py
├── resume_optimizer.py
├── coverletter_generator.py
├── tracker.py
├── linkedin_agent.py
├── prompts/
├── data/
├── tests/
└── .github/workflows/
```

## Quick start

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m unittest discover -s tests -v
```

Extract keywords:

```bash
python keyword_extractor.py --input job_descriptions/example.txt --output data/keywords.txt
```

Create a local application package from an approved job description:

```bash
python job_search_agent.py \
  --resume resumes/master_resume.txt \
  --job job_descriptions/example.txt \
  --company "Example Company" \
  --title "AI Automation Specialist" \
  --url "https://example.com/jobs/123"
```

The workflow writes files locally and adds a `Prepared` row to the CSV tracker. It does not apply to the job.

## Google Sheets

Import `data/google_sheet_template.csv` into Google Sheets. The CSV columns match the local tracker and can later be synchronized through an approved Google service account integration.

## Claude Code

Open this repository in VS Code and paste `claude_prompt.md` into Claude Code. The prompt instructs Claude to inspect, test, and improve the project without fabricating candidate data or enabling blind mass applications.
