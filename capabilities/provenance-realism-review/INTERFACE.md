# Provenance realism review interface, version 1 draft

## Named user job

Given a proposed change, pull request, architecture record, or test suite,
identify material mismatches among consequential requirements, their authority
and evidence lineage, the mechanism selected to satisfy them, and the behavior
actually provided under a stated failure model. Return supported findings or an
explicit no-material-findings conclusion with residual limits.

## Inputs

- A pinned repository state or document set containing the claims and relevant
  implementation evidence.
- The issue, user request, owner decision, or external contract that establishes
  the intended outcome when available.
- Applicable repository guidance and the requested review scope.
- Optional authority to run bounded local or remote verification.

If a source cannot be pinned or an owner decision is unavailable, the review
must state that limitation rather than manufacture authority.

## Output contract

- Establish the exact claim, scope, owner, and evidence lineage before judging
  the mechanism.
- Reconstruct actors, resources, ownership, durability, publication, and the
  successful postcondition independently of implementation labels.
- State which failure classes were evaluated and which remain unverified.
- Distinguish provenance, rollback, compensation, cleanup, retry, resume, crash
  recovery, concurrency safety, and Git recovery.
- Return ranked material findings with tight locations, direct evidence,
  realistic impact, and the smallest correction direction.
- When there are no material findings, say so and preserve required
  anti-findings and residual limits.
- Separate observation, owner decision, and inference.
- Tie every claim that a command or probe ran to the current task's tool record.

## Exclusions

This interface does not promise a general code or security review, universal
architecture policy, authorship attribution, SBOM or supply-chain attestation,
automatic authority scoring, proof from passing structural checks, or a demand
for external citations for every implementation choice.

It does not declare all rollback suspect, all same-change tests circular, or
Git sufficient for all recovery. It does not authorize edits during a
review-only request.

## Compatibility

Version 1 remains a draft until paired finding and false-positive cases have
been run repeatedly. Its intended stable behavior is the named finding/no-
finding job and the separation of requirement provenance from operational
guarantees. Vocabulary and internal workflow may change while evidence shows
where the durable boundary belongs.
