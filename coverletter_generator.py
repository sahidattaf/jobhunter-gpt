#!/usr/bin/env python3
"""Generate a conservative cover-letter draft from verified source material."""
from __future__ import annotations

import argparse
from pathlib import Path

from keyword_extractor import extract_keywords


def generate_cover_letter(
    resume: str,
    job_description: str,
    company: str,
    title: str,
    candidate_name: str = "Candidate Name",
) -> str:
    """Build a reviewable letter without inventing unsupported achievements."""
    if not all(value.strip() for value in (resume, job_description, company, title)):
        raise ValueError("resume, job description, company, and title are required")

    keywords = extract_keywords(job_description, top_k=8)
    verified = [term for term in keywords if term.lower() in resume.lower()]
    alignment = ", ".join(verified[:5]) or "the capabilities described in my attached resume"

    return f"""Dear Hiring Manager,

I am writing to apply for the {title} position at {company}. My background includes experience relevant to {alignment}, and I am interested in contributing those capabilities to your team.

My attached resume provides the verified details of my experience and responsibilities. I would welcome the opportunity to discuss how that background connects with the priorities described in this role. I have intentionally kept this letter focused on information supported by my resume.

Thank you for your time and consideration.

Sincerely,
{candidate_name}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a cover-letter draft.")
    parser.add_argument("--resume", required=True, type=Path)
    parser.add_argument("--job", required=True, type=Path)
    parser.add_argument("--company", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--candidate-name", default="Candidate Name")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    letter = generate_cover_letter(
        args.resume.read_text(encoding="utf-8"),
        args.job.read_text(encoding="utf-8"),
        args.company,
        args.title,
        args.candidate_name,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(letter, encoding="utf-8")
    print(f"Wrote cover-letter draft to {args.output}")


if __name__ == "__main__":
    main()
