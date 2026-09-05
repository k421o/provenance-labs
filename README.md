# provenance-labs

`provenance-labs` is a research and evaluation repository for realistic
provenance claims in software systems, architecture decisions, and agent
reviews. It asks two separate questions:

1. Why does a consequential requirement or guarantee belong?
2. Does the proposed mechanism actually provide it under the failures that
   matter?

The first derived capability is
[`provenance-realism-review`](capabilities/provenance-realism-review/SKILL.md).
The skill is an application of the domain model, not authority over the model
or over the repositories it reviews.

## Repository map

```text
.
├── domain/        # Change shared claim and failure semantics here.
├── capabilities/  # Apply the domain model to reviews; edit the skill here.
├── evals/         # Keep held-out expectations separate from agent-visible scenarios.
├── docs/          # Keep pinned observations distinct from general domain claims.
├── scripts/       # Automate repository checks, not judgments about claim validity.
└── tests/         # Check contracts and mechanisms; review quality needs actual trials.
```

## Current work

- Build a claim-lineage vocabulary that separates authority, observation,
  implementation assertions, and validation oracles.
- Distinguish provenance from rollback, compensation, cleanup, retry, resume,
  crash recovery, concurrency safety, and Git recovery.
- Detect closed evidence loops without treating every same-change test as
  circular.
- Evaluate review behavior with paired finding and false-positive controls.
- Prefer the smallest mechanism that satisfies an evidenced requirement and
  explicit failure model.

## Motivating pitfall

A change can add an exception handler, describe it as a transactional rollback,
and add a test that expects the handler to restore local state. That test may
show that the implementation matches the new rule. It does not establish that
the rule was required, that the operation is atomic, or that the design
survives interruption and concurrency.

The mistake is not "rollback does nothing." Exception compensation can be
useful for retry convenience. The mistake is using internally consistent prose
and tests as evidence for a broader requirement or guarantee. The initial
[README Labs case study](docs/case-studies/readme-labs-pr-24.md) records the
concrete observation that motivated this domain.

## Repository model

```text
Owner decisions, contracts, observations       Proposed mechanism and tests
                    \                            /
                     v                          v
                 claim lineage + failure semantics
                              |
                              v
                review protocol and case evidence
                              |
                              v
                 experimental agent capability
```

The [domain charter](docs/domain-charter.md) owns scope and evidence rules.
The stable core begins with the [glossary](domain/glossary.md) and
[review model](domain/review-model.md). Controlled scenarios live under
[`evals/`](evals/README.md); they do not become proof merely by being checked
in.

Directories are added only when current evidence needs them. This bootstrap
does not include ingestion, artifact custody, catalogs, generated products,
release automation, or a general architecture store.

## Development

Python 3.12+ and [`uv`](https://docs.astral.sh/uv/) are required.

```console
uv sync --locked --dev
uv run ruff check .
uv run pytest
uv run python scripts/check_markdown_links.py
```

These checks validate repository and capability structure. Behavioral claims
about review quality still require actual held-out review runs.

## Status

The domain and capability are experimental. The initial finding/control pair
defines a testable hypothesis; it is not a universal architecture policy or a
released review product. Ratification and additional cases are tracked in
[bootstrap issue #1](https://github.com/k421o/provenance-labs/issues/1).

## License

MIT
