#!/usr/bin/env python3
"""Load and validate the local candidate profile."""
from __future__ import annotations

import json
import re
from pathlib import Path

_PLACEHOLDER_NAMES = {
    "candidate name",
    "your name",
    "full name",
    "name here",
    "jane doe",
    "john doe",
}

_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

_VALID_REMOTE_VALUES = {"remote", "hybrid", "on-site", "onsite", "flexible", ""}


def validate_profile(profile: dict) -> dict:
    """Validate a candidate profile dict.

    Raises ValueError describing the first violation found. Never invents or
    fills in missing candidate information.
    """
    name = profile.get("full_name", "").strip()
    if not name:
        raise ValueError(
            "candidate profile is missing 'full_name'. "
            "Add your real name to config/candidate_profile.json."
        )
    if name.lower() in _PLACEHOLDER_NAMES:
        raise ValueError(
            f"'full_name' value '{name}' looks like a placeholder. "
            "Replace it with the real candidate's name."
        )

    email = profile.get("email", "").strip()
    if email and not _EMAIL_RE.match(email):
        raise ValueError(
            f"'email' value '{email}' is not a valid email address."
        )

    titles = profile.get("target_job_titles")
    if titles is not None and not isinstance(titles, list):
        raise ValueError(
            "'target_job_titles' must be a list of strings, "
            f"got {type(titles).__name__}."
        )

    skills = profile.get("verified_skills")
    if skills is not None and not isinstance(skills, list):
        raise ValueError(
            "'verified_skills' must be a list of strings, "
            f"got {type(skills).__name__}."
        )

    locations = profile.get("preferred_locations")
    if locations is not None and not isinstance(locations, list):
        raise ValueError(
            "'preferred_locations' must be a list of strings, "
            f"got {type(locations).__name__}."
        )

    remote = profile.get("remote_preference", "").strip().lower()
    if remote and remote not in _VALID_REMOTE_VALUES:
        raise ValueError(
            f"'remote_preference' value '{remote}' is not recognised. "
            f"Use one of: {', '.join(sorted(_VALID_REMOTE_VALUES) or ['remote', 'hybrid', 'on-site', 'flexible'])}."
        )

    return profile


def load_profile(path: Path) -> dict:
    """Load and validate a candidate profile from a JSON file."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Could not parse {path}: {exc}") from exc
    return validate_profile(data)
