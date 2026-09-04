from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_initial_case_retains_its_pinned_revisions() -> None:
    case = (ROOT / "docs/case-studies/readme-labs-pr-24.md").read_text(
        encoding="utf-8"
    )
    assert "0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1" in case
    assert "f49daf761b377859f7d940d9a2a9402f0657c035" in case


def test_mutable_issue_observation_matches_its_frozen_snapshot_digest() -> None:
    record = (
        ROOT / "docs/case-studies/sources/readme-labs-issue-23.md"
    ).read_text(encoding="utf-8")
    match = re.search(
        r"Frozen snapshot SHA-256:\n\s+`([0-9a-f]{64})`",
        record,
    )
    assert match is not None
    snapshot = (
        ROOT
        / "docs/case-studies/sources/readme-labs-issue-23-body.txt"
    ).read_bytes()
    assert hashlib.sha256(snapshot).hexdigest() == match.group(1)
