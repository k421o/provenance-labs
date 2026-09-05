---
name: provenance-realism-review
description: Review a proposed change, pull request, architecture, or test suite for the provenance of consequential requirements and guarantees, realistic failure semantics, and closed evidence loops. Use for rollback, compensation, migration, custody, transactional, retry, crash-safety, concurrency, Git-recovery, or provenance claims. Do not use as a general code review, authorship attribution, SBOM, or supply-chain attestation workflow.
---

# Provenance realism review

Review consequential claims from evidence outward. Ask both why a requirement
belongs and whether its mechanism provides the claimed behavior. Do not confuse
a mechanism's internal consistency with evidence that the mechanism is needed.

## Workflow

1. **Pin scope and sources.** Record the repository, base and head revisions,
   issue or user request, applicable owner guidance, and authorized scope. Read
   enough code, tests, prose, and platform contracts to trace the material
   claims. Treat branch names and moving pages as locators, not pinned evidence.
2. **Trace disputed claims.** Use [claim lineage](references/claim-lineage.md)
   when a consequential requirement's source or derivation is unclear. Ask
   what support would remain without the new implementation, prose, and tests.
   A pinned source and explanation usually suffice; use a ledger only when
   several interacting claims need one.
3. **Reconstruct the operation.** Independently list actors, resources,
   ownership, custody, private and shared state, durable writes, publication
   points, and the successful postcondition. Do not inherit “transaction,”
   “rollback,” or “provenance” from names alone.
4. **State the relevant failure model.** Use the promised behavior and actual
   actors to select exception, crash, retry, concurrency, or recovery paths
   that could change the conclusion. Use
   [failure semantics](references/failure-semantics.md) for their distinctions.
   Do not require an exclusion record or owner decision for irrelevant classes.
5. **Classify mechanisms accurately.** Distinguish prevention, atomic publish,
   rollback, compensation, cleanup, retry, resume, crash recovery, Git
   recovery, and provenance recording. A mechanism may be useful while its
   label or claimed scope is wrong.
6. **Check the disputed test oracle.** Trace the expectations offered as
   evidence for the claim. A same-change test can validly show conformance to
   an owner request or external
   contract. It cannot, by passing, prove the necessity of a requirement that
   was introduced only to describe the implementation. Identify derivation
   edges; do not infer circularity from chronology or authorship.
7. **Run bounded discriminating probes when safe.** Prefer a counterexample
   that separates competing explanations: terminate between durable writes,
   interleave concurrent adoption and cleanup, retry with the same identity,
   introduce foreign state at a cleanup path, or remove the disputed mechanism
   and test the actual postcondition. Never claim a probe ran unless the current
   task's tool record contains it.
8. **Choose a proportional disposition.** Keep, clarify, simplify, strengthen,
   use forward recovery, return the requirement to its owner, or remove the
   mechanism. “Add more rollback” and “Git handles it” both require a
   boundary-specific argument.
9. **Report only material findings.** Apply the
   [finding standard](references/finding-standard.md). Separate direct evidence,
   owner decisions, and inference. Do not convert vocabulary preferences into
   findings when behavior and scope are already clear.

## Completion

If no material issue remains, say so. Name any unverified authority assumption,
failure class, interleaving, remote behavior, or recovery operation that could
materially affect the conclusion. The finding reference holds the reporting
shape and false-positive checks; do not produce a separate no-finding checklist.

## Change requests

When explicitly asked to edit rather than review:

- preserve the target repository's authority and applicable instructions;
- encode the narrowest owner-ratified guarantee;
- prefer private staging, atomic publication, idempotence, and forward resume
  when they satisfy the actual requirement;
- add tests derived from the requirement and realistic failure cuts, recording
  what each test can and cannot prove; and
- keep domain interpretation here while returning system-specific decisions
  and implementation to the owning repository.

Do not implement fixes, create issues, or modify external systems during a
review-only request.
