#!/usr/bin/env python3
"""CSV tracker for job applications."""
from __future__ import annotations

import csv
from datetime import date
from pathlib import Path

COLUMNS = ["Date Added", "Job Title", "Company", "Location", "URL", "Fit Score", "Status", "Resume File", "Cover Letter File", "Next Action", "Follow-up Date", "Notes"]


def append_application(path: Path, row: dict[str, str]) -> None:
    """Append one normalized record and create the header when needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    exists = path.exists() and path.stat().st_size > 0
    normalized = {column: row.get(column, "") for column in COLUMNS}
    normalized["Date Added"] = normalized["Date Added"] or date.today().isoformat()
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        if not exists:
            writer.writeheader()
        writer.writerow(normalized)


def read_applications(path: Path) -> list[dict[str, str]]:
    """Read all records from the tracker."""
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))
