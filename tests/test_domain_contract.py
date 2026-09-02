from __future__ import annotations

import hashlib
import re
from pathlib import Path

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]


def _headings(path: Path, level: int | None = None) -> set[str]:
    tokens = MarkdownIt("commonmark").parse(path.read_text(encoding="utf-8"))
    headings: set[str] = set()
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        if level is not None and token.tag != f"h{level}":
            continue
        if tokens[index + 1].type == "inline":
            headings.add(tokens[index + 1].content)
    return headings


def test_charter_exposes_scope_evidence_and_maturity_boundaries() -> None:
    assert {
        "Purpose",
        "Scope",
        "Non-goals",
        "Evidence and authority",
        "Record roles and promotion",
        "Public evidence boundary",
        "Domain and capability maturity",
        "Repository relationships",
    } <= _headings(ROOT / "docs/domain-charter.md")


def test_glossary_keeps_core_provenance_and_failure_terms_distinct() -> None:
    assert {
        "Provenance",
        "Authority",
        "Evidence lineage",
        "Closed evidence loop",
        "Atomic publish",
        "Rollback",
        "Compensation",
        "Cleanup",
        "Retryability",
        "Resume",
        "Crash recovery",
        "Concurrency safety",
        "Git recovery",
        "Custody",
    } <= _headings(ROOT / "domain/glossary.md", level=3)


def test_initial_case_is_pinned_and_explicitly_non_authoritative() -> None:
    case = (ROOT / "docs/case-studies/readme-labs-pr-24.md").read_text(
        encoding="utf-8"
    )
    assert "0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1" in case
    assert "f49daf761b377859f7d940d9a2a9402f0657c035" in case
    assert "This case does not decide README Labs architecture" in case


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
