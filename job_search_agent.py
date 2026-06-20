#!/usr/bin/env python3
"""Prepare local application materials for the candidate to review."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from coverletter_generator import generate_cover_letter
from resume_optimizer import optimize_resume
from tracker import append_application


def slugify(value: str) -> str:
    """Convert text into a filesystem-safe slug."""
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result or "application"


def prepare_application(
    resume_path: Path,
    job_path: Path,
    company: str,
    title: str,
    source_url: str,
    candidate_name: str,
) -> Path:
    """Create review files and record the prepared application."""
    resume = resume_path.read_text(encoding="utf-8")
    job_description = job_path.read_text(encoding="utf-8")
    package_dir = Path("applications") / f"{slugify(company)}-{slugify(title)}"
    package_dir.mkdir(parents=True, exist_ok=True)

    review_file = package_dir / "resume-review.txt"
    letter_file = package_dir / "cover-letter.txt"
    details_file = package_dir / "application-details.txt"

    review_file.write_text(optimize_resume(resume, job_description), encoding="utf-8")
    letter_file.write_text(
        generate_cover_letter(resume, job_description, company, title, candidate_name),
        encoding="utf-8",
    )
    details_file.write_text(
        f"Company: {company}\nRole: {title}\nSource: {source_url}\n"
        "Status: Prepared for human review\n",
        encoding="utf-8",
    )

    append_application(
        Path("data/applications.csv"),
        {
            "Job Title": title,
            "Company": company,
            "URL": source_url,
            "Status": "Prepared",
            "Resume File": str(review_file),
            "Cover Letter File": str(letter_file),
            "Next Action": "Review materials",
        },
    )
    return package_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare application materials.")
    parser.add_argument("--resume", required=True, type=Path)
    parser.add_argument("--job", required=True, type=Path)
    parser.add_argument("--company", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("--candidate-name", default="Candidate Name")
    args = parser.parse_args()

    output = prepare_application(
        args.resume, args.job, args.company, args.title, args.url, args.candidate_name
    )
    print(f"Prepared files at {output}")


if __name__ == "__main__":
    main()
