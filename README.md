# provenance-labs

Research and an experimental agent skill for reviewing consequential software
requirements and guarantees. The lab asks why a requirement belongs and
whether the proposed mechanism delivers it under the failures that matter.
Its focus includes rollback, retry, crash recovery, concurrency, and migration
claims.

## Review a claim

Give an agent the
[provenance-realism-review skill](capabilities/provenance-realism-review/SKILL.md),
the target change or architecture, and its supporting requirements. For example:

> Read `capabilities/provenance-realism-review/SKILL.md` and review this PR's
> rollback claim. Trace the requirement, reconstruct the writes and cleanup,
> and check what the tests establish about interruption and concurrent use.

The result is material findings with evidence and a proportionate correction,
or a no-material-findings conclusion with verification limits. This is a source
skill, not a released review product, general code review, authorship
attribution tool, or supply-chain attestation service.

## Why this lab exists

An exception handler and a passing restoration test can establish useful
compensation behavior without proving atomicity or crash recovery. They also
do not, by themselves, explain why restoration was required. The
[README Labs case study](docs/case-studies/readme-labs-pr-24.md) records the
concrete observation behind this distinction.

Tests added with an implementation can still be valid evidence when their
expectations come from an owner requirement or external contract. The review
traces that support rather than treating shared authorship or timing as proof
of circular reasoning.

## Explore and evaluate

- [Review model](domain/review-model.md) and [glossary](domain/glossary.md):
  claim lineage, mechanism classification, and failure semantics.
- [Domain charter](docs/domain-charter.md): scope and evidence rules.
- [Evaluation protocol](evals/README.md): a finding/control pair, workspace
  isolation, and separate scoring. Scenario inputs and held-out expectations
  serve different consumers; the expectations stay outside the reviewed workspace.

The domain and capability are experimental. The initial scenarios express a
testable hypothesis; checking them into the repository does not establish
review quality or a universal architecture policy.

## Development

From this repository's root, with Python 3.12+ and `uv`:

```console
uv sync --locked --dev
uv run ruff check .
uv run pytest
uv run python scripts/check_markdown_links.py
```

These checks validate contracts, capability structure, links, and the fixture
mechanisms. They do not run an agent review; behavioral claims need actual
held-out trials. Further cases and ratification are tracked in
[bootstrap issue #1](https://github.com/k421o/provenance-labs/issues/1).

## License

[MIT](LICENSE)
