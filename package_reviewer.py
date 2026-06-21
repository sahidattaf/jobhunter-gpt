#!/usr/bin/env python3
"""Inspect a generated application package before human use.

Reads the three output files produced by job_search_agent.py and runs
structural and content checks. Returns a result dict describing what was
found, what is missing, and whether the package needs fixes.

Never submits applications. Never modifies the package files.
"""
from __future__ import annotations

import argparse
import re
from pathlib import Path

_REQUIRED_FILES = [
    "cover-letter.txt",
    "application-details.txt",
    "resume-review.txt",
]

# Strings that must never appear in a finished cover letter
_PLACEHOLDER_STRINGS = [
    "Candidate Name",
    "Company Name",
    "Job Title",
    "Job URL",
    "PASTE REAL JOB DESCRIPTION HERE",
]

_COVER_MIN_LENGTH = 300  # characters

# Pattern left by the v1 cover-letter generator
_RAW_DUMP_RE = re.compile(r"relevant to \w+, \w+, \w+")


# ── Internal helpers ──────────────────────────────────────────────────────────

def _extract_field(text: str, field_name: str) -> str:
    """Return the value on the first line matching 'Field: value'."""
    prefix = f"{field_name}:"
    for line in text.splitlines():
        if line.startswith(prefix):
            return line[len(prefix):].strip()
    return ""


def _is_real_url(value: str) -> bool:
    return value.startswith("http://") or value.startswith("https://")


# ── Public API ────────────────────────────────────────────────────────────────

def review_package(
    package_path: Path,
    candidate_name: str | None = None,
) -> dict:
    """Inspect a package folder and return a structured review result.

    Parameters
    ----------
    package_path:
        Directory produced by job_search_agent.py (e.g. applications/company-title/).
    candidate_name:
        Optional. When provided the reviewer verifies the name appears in the
        cover letter. Leave None to skip that check.

    Returns
    -------
    dict with keys:
        package_path     – absolute path as string
        files_found      – list of required files that exist
        files_missing    – list of required files that are absent
        warnings         – all issues found; ERROR-prefixed items cause NEEDS_FIXES
        approval_status  – "READY_FOR_HUMAN_REVIEW" or "NEEDS_FIXES"
    """
    errors: list[str] = []   # critical — cause NEEDS_FIXES
    advisories: list[str] = []  # advisory — do not affect approval status

    # ── 1. Check required files ───────────────────────────────────────────────
    files_found: list[str] = []
    files_missing: list[str] = []
    for filename in _REQUIRED_FILES:
        if (package_path / filename).exists():
            files_found.append(filename)
        else:
            files_missing.append(filename)
            errors.append(f"[ERROR] Required file missing: {filename}")

    # Read files that exist (empty string when absent — avoids repeated checks)
    def _read(name: str) -> str:
        p = package_path / name
        return p.read_text(encoding="utf-8") if p.exists() else ""

    cover = _read("cover-letter.txt")
    details = _read("application-details.txt")
    review = _read("resume-review.txt")

    # Extract structured fields from application-details.txt
    company = _extract_field(details, "Company")
    role = _extract_field(details, "Role")
    source_url = _extract_field(details, "Source")
    fit_score = _extract_field(details, "Fit Score")

    # ── 2. Company name in cover letter ───────────────────────────────────────
    if cover and company:
        if company not in cover:
            errors.append(
                f"[ERROR] Company name '{company}' not found in cover-letter.txt."
            )

    # ── 3. Job title in cover letter ──────────────────────────────────────────
    if cover and role:
        if role not in cover:
            errors.append(
                f"[ERROR] Job title '{role}' not found in cover-letter.txt."
            )

    # ── 4. Candidate name in cover letter ─────────────────────────────────────
    if cover:
        if candidate_name:
            if candidate_name not in cover:
                errors.append(
                    f"[ERROR] Candidate name '{candidate_name}' not found in cover-letter.txt."
                )
        else:
            advisories.append(
                "[WARNING] Candidate name not provided to reviewer — "
                "cannot verify it appears in cover-letter.txt."
            )

    # ── 5. No placeholder text in cover letter ────────────────────────────────
    if cover:
        for placeholder in _PLACEHOLDER_STRINGS:
            if placeholder in cover:
                errors.append(
                    f"[ERROR] Placeholder text found in cover-letter.txt: '{placeholder}'"
                )

    # ── 6. Fit score present ──────────────────────────────────────────────────
    if details:
        if not fit_score or "not calculated" in fit_score.lower():
            advisories.append(
                "[WARNING] Fit score not calculated. "
                "Run job_search_agent.py with --profile to include a fit score."
            )

    # ── 7. Source URL present and valid ───────────────────────────────────────
    if details:
        if not _is_real_url(source_url):
            advisories.append(
                "[WARNING] Source URL is missing or invalid in application-details.txt. "
                "Add the original job posting URL for traceability."
            )

    # ── 8. Resume preserved section ───────────────────────────────────────────
    if review:
        if "SOURCE RESUME — PRESERVED" not in review:
            advisories.append(
                "[WARNING] 'SOURCE RESUME — PRESERVED' section not found in resume-review.txt. "
                "The source resume may not have been captured correctly."
            )

    # ── 9. Cover letter length ────────────────────────────────────────────────
    if cover and len(cover) < _COVER_MIN_LENGTH:
        advisories.append(
            f"[WARNING] Cover letter is very short ({len(cover)} characters, "
            f"minimum recommended is {_COVER_MIN_LENGTH}). Review for completeness."
        )

    # ── 10. Raw keyword-dump pattern ─────────────────────────────────────────
    if cover and _RAW_DUMP_RE.search(cover.lower()):
        advisories.append(
            "[WARNING] Cover letter may contain a raw keyword list "
            "(pattern: 'relevant to word1, word2, word3'). "
            "Regenerate using the updated cover letter generator."
        )

    all_warnings = errors + advisories
    approval_status = "NEEDS_FIXES" if errors else "READY_FOR_HUMAN_REVIEW"

    return {
        "package_path": str(package_path.resolve()),
        "files_found": files_found,
        "files_missing": files_missing,
        "warnings": all_warnings,
        "approval_status": approval_status,
    }


def format_review_report(result: dict) -> str:
    """Render a review result dict as a readable plain-text report."""
    status = result["approval_status"]
    found = result["files_found"]
    missing = result["files_missing"]
    warnings = result["warnings"]

    lines = [
        "PACKAGE REVIEW REPORT",
        "=====================",
        f"Package : {result['package_path']}",
        f"Status  : {status}",
        "",
        f"Files found  ({len(found)}): {', '.join(found) if found else 'none'}",
        f"Files missing ({len(missing)}): {', '.join(missing) if missing else 'none'}",
    ]

    if warnings:
        lines += ["", f"Issues found ({len(warnings)}):"]
        for w in warnings:
            lines.append(f"  {w}")
    else:
        lines += ["", "No issues found. Package is ready for human review."]

    lines.append("")
    if status == "READY_FOR_HUMAN_REVIEW":
        lines.append(
            "NEXT STEP: Open each file in the package folder, read every line, "
            "and confirm all claims are accurate before use."
        )
    else:
        lines.append(
            "NEXT STEP: Fix the errors listed above, then re-run the reviewer."
        )

    return "\n".join(lines) + "\n"


# ── CLI ───────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Review a generated application package before human use."
    )
    parser.add_argument(
        "package_path",
        type=Path,
        help="Path to the application package folder (e.g. applications/company-title/)",
    )
    parser.add_argument(
        "--candidate-name",
        default=None,
        help="Candidate name to verify in cover letter (optional)",
    )
    args = parser.parse_args()

    result = review_package(args.package_path, candidate_name=args.candidate_name)
    print(format_review_report(result))
    if result["approval_status"] == "NEEDS_FIXES":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
