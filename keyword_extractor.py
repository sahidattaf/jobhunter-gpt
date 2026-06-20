#!/usr/bin/env python3
"""Extract relevant ATS keywords from a job description."""
from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path

STOP_WORDS = {
    "the", "and", "for", "with", "that", "this", "from", "your", "you", "our",
    "are", "will", "have", "has", "into", "about", "their", "they", "but", "not",
    "all", "any", "can", "who", "job", "role", "work", "team", "company", "years",
}


def extract_keywords(text: str, top_k: int = 20) -> list[str]:
    """Return the most frequent meaningful terms and short technical phrases."""
    if top_k < 1:
        raise ValueError("top_k must be at least 1")

    normalized = re.sub(r"\s+", " ", text.lower())
    tokens = re.findall(r"\b[a-z][a-z0-9+#.\-/]{2,}\b", normalized)
    unigrams = [token.strip(".,/") for token in tokens if token not in STOP_WORDS]
    counts = Counter(unigrams)

    phrases = re.findall(
        r"\b(?:project management|business development|customer success|machine learning|"
        r"artificial intelligence|data analysis|real estate|social media|google sheets|"
        r"power bi|salesforce|account management|process improvement)\b",
        normalized,
    )
    counts.update({phrase: 3 for phrase in phrases})

    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return [term for term, _ in ranked[:top_k]]


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract ATS keywords from a text file.")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--top-k", type=int, default=20)
    args = parser.parse_args()

    text = args.input.read_text(encoding="utf-8")
    keywords = extract_keywords(text, args.top_k)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("\n".join(keywords) + "\n", encoding="utf-8")
    print(f"Wrote {len(keywords)} keywords to {args.output}")


if __name__ == "__main__":
    main()
