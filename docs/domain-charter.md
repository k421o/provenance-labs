# Provenance Labs domain charter

## Purpose

Provenance Labs studies whether consequential engineering claims can be traced
to an appropriate decision authority or independent observation, and whether
the implementation actually provides the claimed behavior under a realistic
failure model.

The domain combines two review questions without conflating them:

1. **Requirement provenance:** why does this requirement, constraint, or
   guarantee belong?
2. **Operational realism:** what does the mechanism provide across ordinary
   errors, interruption, retry, concurrency, and operator recovery?

The repository owns vocabulary, case interpretation, evaluation design, and
canonical review capabilities for that job. It does not acquire authority over
the systems being reviewed.

## Scope

The initial scope is engineering work that makes consequential claims about:

- provenance, lineage, custody, or authority;
- transactions, atomicity, rollback, compensation, or cleanup;
- retry, idempotency, resume, restoration, or crash recovery;
- concurrent ownership, publication, adoption, or deletion of shared state;
- Git or another platform mechanism as a recovery boundary; and
- tests, schemas, receipts, manifests, or documentation offered as evidence
  for a requirement or guarantee.

The first capability reviews proposed changes and architecture records. Later
work may add other projections only after repeated cases show a stable job.

## Non-goals

This repository is not:

- a universal code, security, or architecture reviewer;
- an SBOM, authorship-attribution, cryptographic-attestation, or supply-chain
  provenance system;
- an artifact ingestion or custody service;
- authority to replace a repository owner's decision with an agent score;
- a demand for external citations for every implementation choice;
- a rule that Git solves every operational recovery problem;
- a rule that rollback is always useful or always wasteful; or
- a product factory, plugin marketplace, release train, or central store for
  other domains' architecture.

## Evidence and authority

Evidence is claim-relative. A source can be authoritative for one question and
irrelevant to another. The review model separates these source roles:

- **deciding authority** — a user or owner who may set the requirement;
- **normative dependency** — an external contract or platform behavior the
  system must obey;
- **empirical observation** — behavior directly inspected or reproduced;
- **implementation assertion** — a claim made by code, prose, or its author;
- **validation oracle** — an expectation used to judge an implementation;
- **historical context** — evidence of prior state without current authority;
- **hypothesis** — a proposed explanation or rule awaiting evaluation.

Tests are valid evidence that an implementation satisfies their oracle. They
do not, by themselves, establish that the oracle expresses a necessary or
owner-ratified requirement. Conversely, a test is not circular merely because
it was written in the same change as the implementation. Its derivation, not
its timestamp or author, determines independence.

Every material conclusion should distinguish:

- what an owner requested or ratified;
- what the repository or platform contract requires;
- what was directly observed or reproduced;
- what is inferred from those facts; and
- what remains unverified.

## Record roles and promotion

Records in this repository use explicit roles:

- **observation** — a pinned behavior or statement was directly inspected;
- **hypothesis** — an interpretation or proposed general rule;
- **owner decision** — a named authority selected a direction for its scope;
- **evaluated finding** — a review result exercised against a pinned case;
- **ratified domain rule** — a stable rule accepted for this repository after
  finding and false-positive controls; and
- **superseded record** — retained as history but no longer current guidance.

These roles do not collapse a claim's authority, realization, and evidence
status. A requirement can be owner-ratified but not implemented; an
implementation can be released while its guarantee remains contradicted. The
[review model](../domain/review-model.md) records those axes separately.

A passing repository check establishes structural consistency. It does not
promote a hypothesis or capability by itself.

## Public evidence boundary

This repository is public. It may store synthetic fixtures, public pinned
sources, and interpretations safe for publication. It must not copy private
source bodies, credentials, personal data, or confidential tool output.
Private-system reviews may contribute sanitized claim records or synthetic
reproductions only when the originating authority permits publication.

## Domain and capability maturity

The bootstrap is an early domain module with an experimental capability. It
earns a broader evaluation-laboratory claim only after it has:

- multiple pinned cases from more than one system;
- paired finding and false-positive controls;
- held-out expectations that are not visible to the reviewed agent;
- repeated review runs with recorded limitations; and
- owner review of proposed domain rules.

No version number, directory name, schema, or generated package substitutes
for those signals.

## Repository relationships

The repository shape was adapted from the domain-first separation in
[`k421o/readme-labs` at `f49daf7`](https://github.com/k421o/readme-labs/tree/f49daf761b377859f7d940d9a2a9402f0657c035).
That source is a structural reference, not authority for this domain. The
initial case uses a separately pinned open pull request. Its finding fixture is
a synthetic, minimized derivative of the public MIT-licensed algorithm, with
the derivation recorded in the fixture and case study.

Agent Ops may route cross-authority work here, but this repository owns only
its local model and capability. Findings about another repository return to
that repository's owner for decision and implementation.
