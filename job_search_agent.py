#!/usr/bin/env python3
"""Prepare local application materials for the candidate to review."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from candidate_profile import load_profile
from coverletter_generator import generate_cover_letter
from fit_scorer import format_score_report, score_fit
from resume_optimizer import optimize_resume
from tracker import append_application

_DEFAULT_OUTPUT_DIR = Path("applications")
_DEFAULT_TRACKER = Path("data/applications.csv")


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
    profile: dict | None = None,
    output_dir: Path = _DEFAULT_OUTPUT_DIR,
    tracker_path: Path = _DEFAULT_TRACKER,
) -> Path:
    """Create review files and record the prepared application.

    Writes three files under output_dir/<company-slug>-<title-slug>/:
      resume-review.txt     — ATS keyword analysis with source resume preserved
      cover-letter.txt      — conservative draft using only verified terms
      application-details.txt — metadata, fit score, and next-action reminder

    Appends one row to tracker_path (CSV). Never submits anything.
    """
    resume = resume_path.read_text(encoding="utf-8")
    job_description = job_path.read_text(encoding="utf-8")

    package_dir = output_dir / f"{slugify(company)}-{slugify(title)}"
    package_dir.mkdir(parents=True, exist_ok=True)

    review_file = package_dir / "resume-review.txt"
    letter_file = package_dir / "cover-letter.txt"
    details_file = package_dir / "application-details.txt"

    review_file.write_text(optimize_resume(resume, job_description), encoding="utf-8")
    letter_file.write_text(
        generate_cover_letter(resume, job_description, company, title, candidate_name),
        encoding="utf-8",
    )

    fit_result: dict | None = None
    fit_total: str = ""
    if profile is not None:
        fit_result = score_fit(resume, job_description, profile)
        fit_total = str(fit_result["total"])

    details_lines = [
        f"Company: {company}",
        f"Role: {title}",
        f"Source: {source_url}",
        f"Fit Score: {fit_total + '/100' if fit_total else 'Not calculated (no profile loaded)'}",
        "Status: Prepared for human review",
        "",
    ]
    if fit_result is not None:
        details_lines.append(format_score_report(fit_result))
    details_lines.append(
        "NEXT ACTION: Review all files in this folder before doing anything else.\n"
        "Do not submit this application until you have verified every claim."
    )
    details_file.write_text("\n".join(details_lines), encoding="utf-8")

    append_application(
        tracker_path,
        {
            "Job Title": title,
            "Company": company,
            "URL": source_url,
            "Fit Score": fit_total,
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
    parser.add_argument("--candidate-name", default="")
    parser.add_argument(
        "--profile",
        type=Path,
        default=None,
        help="Path to config/candidate_profile.json (optional but recommended)",
    )
    args = parser.parse_args()

    profile: dict | None = None
    candidate_name = args.candidate_name

    if args.profile is not None:
        profile = load_profile(args.profile)
        if not candidate_name:
            candidate_name = profile.get("full_name", "")
    elif not candidate_name:
        candidate_name = "Candidate"

    output = prepare_application(
        args.resume,
        args.job,
        args.company,
        args.title,
        args.url,
        candidate_name,
        profile=profile,
    )
    print(f"Prepared files at {output}")
    if profile is None:
        print(
            "Tip: pass --profile config/candidate_profile.json to include a fit score."
        )


if __name__ == "__main__":
    main()
