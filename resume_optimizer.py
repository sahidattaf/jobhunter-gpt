#!/usr/bin/env python3
"""Create a truthful, keyword-aware resume draft without inventing claims."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from keyword_extractor import extract_keywords


def keyword_coverage(resume: str, keywords: list[str]) -> tuple[list[str], list[str]]:
    """Split target keywords into present and missing groups."""
    haystack = resume.lower()
    present = [keyword for keyword in keywords if keyword.lower() in haystack]
    missing = [keyword for keyword in keywords if keyword.lower() not in haystack]
    return present, missing


def optimize_resume(resume: str, job_description: str, top_k: int = 20) -> str:
    """Return a review draft with an ATS analysis and unchanged source resume.

    The function deliberately does not insert missing skills into the resume. Missing
    keywords are presented as review candidates so the user can confirm truthfulness.
    """
    if not resume.strip():
        raise ValueError("resume cannot be empty")
    if not job_description.strip():
        raise ValueError("job description cannot be empty")

    keywords = extract_keywords(job_description, top_k=top_k)
    present, missing = keyword_coverage(resume, keywords)
    cleaned = re.sub(r"[ \t]+\n", "\n", resume.strip())

    return (
        "JOBHUNTERGPT ATS REVIEW\n"
        "========================\n\n"
        f"Confirmed keyword matches ({len(present)}): "
        f"{', '.join(present) if present else 'None detected'}\n\n"
        "Keywords requiring human verification before use:\n"
        + "\n".join(f"- {item}" for item in missing)
        + "\n\nSOURCE RESUME — PRESERVED\n"
        "=========================\n"
        + cleaned
        + "\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create an ATS review draft.")
    parser.add_argument("--resume", required=True, type=Path)
    parser.add_argument("--job", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    result = optimize_resume(
        args.resume.read_text(encoding="utf-8"),
        args.job.read_text(encoding="utf-8"),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(result, encoding="utf-8")
    print(f"Wrote ATS review draft to {args.output}")


if __name__ == "__main__":
    main()
