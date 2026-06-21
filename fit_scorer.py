#!/usr/bin/env python3
"""Score how well a job description matches the candidate's verified background."""
from __future__ import annotations

from keyword_extractor import extract_keywords
from resume_optimizer import keyword_coverage

_REMOTE_SIGNALS = {"remote", "work from home", "wfh", "distributed", "virtual"}
_HYBRID_SIGNALS = {"hybrid", "remote", "flexible"}
_ONSITE_SIGNALS = {"on-site", "onsite", "in-office", "in office", "on site"}


def score_fit(resume: str, job_description: str, profile: dict) -> dict:
    """Return a fit assessment dict with a 0-100 total score.

    Scoring breakdown (max 100 pts):
    - Keyword overlap — resume terms vs. job description keywords: 50 pts
    - Verified skill coverage — profile skills found in job description: 30 pts
    - Preferred location match: 10 pts
    - Remote preference match: 10 pts

    Returns:
        total: int 0-100
        matched_requirements: list of terms confirmed in both resume and job
        missing_requirements: list of job keywords absent from resume
        verification_warnings: list of human-review notices for unmatched skills
    """
    if not resume.strip():
        raise ValueError("resume cannot be empty")
    if not job_description.strip():
        raise ValueError("job_description cannot be empty")

    jd_lower = job_description.lower()

    # ── 1. Keyword overlap (50 pts) ──────────────────────────────────────────
    keywords = extract_keywords(job_description, top_k=20)
    present, missing = keyword_coverage(resume, keywords)
    keyword_score = (len(present) / max(len(keywords), 1)) * 50

    # ── 2. Verified skill coverage (30 pts) ──────────────────────────────────
    verified_skills = [s.lower().strip() for s in profile.get("verified_skills", [])]
    matched_skills = [s for s in verified_skills if s in jd_lower]
    unmatched_skills = [s for s in verified_skills if s not in jd_lower]

    if verified_skills:
        skill_score = (len(matched_skills) / len(verified_skills)) * 30
    else:
        skill_score = 15.0  # neutral — no skills listed, no penalty

    # ── 3. Preferred location match (10 pts) ─────────────────────────────────
    preferred_locations = [loc.lower().strip() for loc in profile.get("preferred_locations", [])]
    location_score = 10.0 if any(loc in jd_lower for loc in preferred_locations if loc) else 0.0

    # ── 4. Remote preference match (10 pts) ──────────────────────────────────
    remote_pref = profile.get("remote_preference", "").lower().strip()
    remote_score = 0.0
    if remote_pref in ("remote",):
        if any(sig in jd_lower for sig in _REMOTE_SIGNALS):
            remote_score = 10.0
    elif remote_pref in ("hybrid", "flexible"):
        if any(sig in jd_lower for sig in _HYBRID_SIGNALS):
            remote_score = 10.0
    elif remote_pref in ("on-site", "onsite"):
        if any(sig in jd_lower for sig in _ONSITE_SIGNALS):
            remote_score = 10.0
    elif not remote_pref:
        remote_score = 5.0  # neutral — no preference stated

    total = min(round(keyword_score + skill_score + location_score + remote_score), 100)

    # Deduplicate matched list preserving order
    seen: set[str] = set()
    all_matched: list[str] = []
    for term in present + matched_skills:
        if term not in seen:
            seen.add(term)
            all_matched.append(term)

    warnings = [
        f"Skill not found in job description — verify relevance before including: {s}"
        for s in unmatched_skills
    ]

    return {
        "total": total,
        "matched_requirements": all_matched,
        "missing_requirements": missing,
        "verification_warnings": warnings,
    }


def format_score_report(result: dict) -> str:
    """Render the fit-score dict as a readable text block."""
    total = result["total"]
    matched = result["matched_requirements"]
    missing = result["missing_requirements"]
    warnings = result["verification_warnings"]

    lines = [
        "FIT SCORE REPORT",
        "================",
        f"Total score: {total}/100",
        "",
        f"Matched requirements ({len(matched)}):",
    ]
    lines += [f"  + {item}" for item in matched] if matched else ["  None detected"]
    lines += [
        "",
        f"Missing requirements ({len(missing)}) — review before tailoring resume:",
    ]
    lines += [f"  - {item}" for item in missing] if missing else ["  None"]
    if warnings:
        lines += ["", "Verification warnings:"]
        lines += [f"  ! {w}" for w in warnings]
    return "\n".join(lines) + "\n"
