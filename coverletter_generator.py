#!/usr/bin/env python3
"""Generate a conservative, professional cover-letter draft from verified source material."""
from __future__ import annotations

import argparse
from pathlib import Path

from keyword_extractor import extract_keywords
from resume_optimizer import keyword_coverage

_PLACEHOLDER_NAMES = {"candidate name", "candidate", "your name", "name here"}


# ── Section-detection helper ─────────────────────────────────────────────────

def _looks_like_section_header(line: str) -> bool:
    """Return True if a resume line looks like a section heading."""
    stripped = line.strip()
    if not stripped:
        return False
    # Body text ends with sentence punctuation; headers don't
    if stripped.endswith((".", ",", ";", "?", "!")):
        return False
    # Lines with URLs, email indicators, or path separators are not headers
    if any(c in stripped for c in ("@", "http", "/", "\\")):
        return False
    # Bullet-point lines are not headers
    if stripped.startswith(("-", "•", "*", "·")):
        return False
    words = stripped.split()
    if len(words) > 4:
        return False
    # Every word must start with an uppercase letter
    return all(word[0].isupper() for word in words if word)


# ── Public helper functions ──────────────────────────────────────────────────

def extract_resume_summary(resume: str) -> str:
    """Extract the Professional Summary block from a plain-text resume.

    Returns an empty string when no recognisable summary section is found.
    """
    triggers = {
        "professional summary", "summary", "profile", "about",
        "objective", "professional profile",
    }
    in_summary = False
    collected: list[str] = []

    for line in resume.splitlines():
        stripped = line.strip()
        if stripped.lower() in triggers:
            in_summary = True
            continue
        if in_summary:
            # Stop at the next section header once we have at least one line
            if _looks_like_section_header(stripped) and collected:
                break
            if stripped:
                collected.append(stripped)

    return " ".join(collected).strip()


def clean_keyword_phrases(keywords: list[str]) -> list[str]:
    """Remove single-word fragments that are already captured by a multi-word phrase.

    Example: given ["real", "estate", "real estate development"], the single words
    "real" and "estate" are dropped because they are component tokens of the phrase.
    """
    multi_word = [k for k in keywords if " " in k]
    subsumed: set[str] = set()
    for phrase in multi_word:
        subsumed.update(phrase.split())

    return [k for k in keywords if " " in k or k not in subsumed]


def extract_verified_strengths(
    resume: str,
    job_description: str,
    profile: dict | None = None,
) -> list[str]:
    """Return meaningful, verified skill phrases present in both resume and job description.

    Priority order:
    1. Profile verified_skills that appear in both resume and job description.
    2. Multi-word keyword phrases extracted from the job description that appear in resume.

    Single-word raw tokens are suppressed to avoid fragment dumping.
    Never invents skills not in the source material.
    """
    jd_lower = job_description.lower()
    resume_lower = resume.lower()
    strengths: list[str] = []
    seen: set[str] = set()

    # 1. Profile skills verified against both resume and JD
    if profile:
        for skill in profile.get("verified_skills", []):
            skill_lower = skill.lower().strip()
            if skill_lower in jd_lower and skill_lower in resume_lower:
                strengths.append(skill.strip())
                seen.add(skill_lower)

    # 2. Multi-word phrases extracted from JD that appear in resume (supplementary)
    jd_keywords = extract_keywords(job_description, top_k=20)
    present, _ = keyword_coverage(resume, jd_keywords)
    cleaned = clean_keyword_phrases(present)
    for term in cleaned:
        if " " in term and term.lower() not in seen:
            strengths.append(term)
            seen.add(term.lower())

    return strengths[:6]


def build_alignment_sentence(strengths: list[str]) -> str:
    """Format a list of verified strengths into a single readable sentence fragment."""
    if not strengths:
        return "the experience and capabilities described in my attached resume"
    if len(strengths) == 1:
        return strengths[0]
    if len(strengths) == 2:
        return f"{strengths[0]} and {strengths[1]}"
    return ", ".join(strengths[:-1]) + f", and {strengths[-1]}"


# ── Main generator ───────────────────────────────────────────────────────────

def generate_cover_letter(
    resume: str,
    job_description: str,
    company: str,
    title: str,
    candidate_name: str = "",
    profile: dict | None = None,
) -> str:
    """Build a professional, conservative cover letter using only verified source material.

    Structure:
      Greeting → Role/company interest → Verified background → Role alignment → Closing

    Raises ValueError for missing required fields or placeholder candidate names.
    Never invents experience, qualifications, or claims absent from the resume.
    """
    if not all(value.strip() for value in (resume, job_description, company, title)):
        raise ValueError("resume, job_description, company, and title are all required")
    if not candidate_name.strip():
        raise ValueError(
            "candidate_name is required. Pass the real candidate name."
        )
    if candidate_name.strip().lower() in _PLACEHOLDER_NAMES:
        raise ValueError(
            f"candidate_name '{candidate_name}' looks like a placeholder. "
            "Replace it with the real candidate's name."
        )

    strengths = extract_verified_strengths(resume, job_description, profile)
    alignment = build_alignment_sentence(strengths)
    summary = extract_resume_summary(resume)

    # ── Paragraph: opening ───────────────────────────────────────────────────
    opening = (
        f"I am writing to express my interest in the {title} position at {company}."
    )

    # ── Paragraph: verified background ──────────────────────────────────────
    if summary:
        background = summary
    else:
        background = (
            f"My background includes verified experience in {alignment}. "
            "The full details of my responsibilities and projects are provided in my attached resume."
        )

    # ── Paragraph: alignment with role ──────────────────────────────────────
    if strengths:
        alignment_para = (
            f"The requirements outlined for this role align with my experience in {alignment}. "
            "I am prepared to discuss how this background connects with the priorities "
            "described in this position."
        )
    else:
        alignment_para = (
            "I have reviewed the requirements for this role and believe my background, "
            "as described in my attached resume, is directly relevant to what you are looking for."
        )

    # ── Paragraph: closing ───────────────────────────────────────────────────
    closing = (
        "My resume contains the verified details of my experience, projects, and responsibilities. "
        "I have kept this letter focused on information supported by that document. "
        "I welcome the opportunity to discuss how my background fits the needs of this role."
    )

    return (
        "Dear Hiring Manager,\n\n"
        f"{opening}\n\n"
        f"{background}\n\n"
        f"{alignment_para}\n\n"
        f"{closing}\n\n"
        "Thank you for your time and consideration.\n\n"
        "Sincerely,\n"
        f"{candidate_name}\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a cover-letter draft.")
    parser.add_argument("--resume", required=True, type=Path)
    parser.add_argument("--job", required=True, type=Path)
    parser.add_argument("--company", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--candidate-name", required=True)
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
