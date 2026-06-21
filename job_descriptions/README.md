# job_descriptions/

Place one approved job description per `.txt` file here before running the workflow.

## File naming

```
job_descriptions/
├── example-company-ai-specialist.txt
└── another-company-analyst.txt
```

Use `<company>-<role-slug>.txt` as a convention so output packages are easy to match.

## What to put in each file

Copy the **full text** of the job description from the employer's posting — requirements,
responsibilities, preferred qualifications, and company description.  Include the source
URL as the first line in a comment:

```
# Source: https://example.com/jobs/123
# Retrieved: 2026-06-21

Job Title: AI Automation Specialist
Company: Example Company
...
```

## Rules

- **One file per role you intend to apply for.**  Do not bulk-import scraped listings.
- **Human-reviewed before use.**  Read the description yourself and confirm the role is
  a genuine fit before running the optimizer.
- **Respect robots.txt and terms of service.**  Copy descriptions manually from
  approved postings.  Do not use automated scrapers.
- **Keep the source URL.**  It is logged in `data/applications.csv` and in the
  `application-details.txt` output file for traceability.

## How it is used

`job_search_agent.py --job job_descriptions/<file>.txt` reads this file, extracts ATS
keywords, generates a resume review draft and a cover-letter draft, calculates a fit
score, and writes everything to `applications/<slug>/`.  Nothing is submitted anywhere.
