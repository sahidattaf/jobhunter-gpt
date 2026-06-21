# resumes/

Place your master resume here as a plain-text `.txt` file.

## File naming

```
resumes/
└── master_resume.txt        ← your verified source resume
```

Optimized output files are written to `applications/<slug>/resume-review.txt` and are
excluded from version control by `.gitignore` (`resumes/optimized_*`).

## Rules

- **Use only true, verified information.** JobHunterGPT will never invent employers,
  dates, degrees, certifications, metrics, or responsibilities.
- **One source of truth.** Keep one `master_resume.txt` that reflects exactly what you
  would say in an interview.  Run the optimizer against individual job descriptions to
  produce tailored review drafts — the source file is always preserved unchanged.
- **Plain text only.** The optimizer reads UTF-8 text.  Export from Word or Google Docs
  with File → Download → Plain Text (.txt) before placing the file here.

## How it is used

`job_search_agent.py --resume resumes/master_resume.txt` reads this file, runs an ATS
keyword comparison against the supplied job description, and writes a review draft to
`applications/<company-slug>/resume-review.txt`.  That draft lists:

1. Confirmed keyword matches already in your resume.
2. Keywords that appear in the job posting but not in your resume, flagged for human
   verification before you choose to add them.

No changes are ever made to the source file in this directory.
