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
2. **Build a claim ledger.** Extract each material requirement, constraint,
   mechanism, guarantee, rationale, observation, and hypothesis. Trace its
   source role and derivation using
   [claim lineage](references/claim-lineage.md). Ask: if the implementation,
   its new prose, and its new tests disappeared, what support for the
   requirement would remain?
3. **Reconstruct the operation.** Independently list actors, resources,
   ownership, custody, private and shared state, durable writes, publication
   points, and the successful postcondition. Do not inherit “transaction,”
   “rollback,” or “provenance” from names alone.
4. **State the failure model.** Consider ordinary exceptions, abrupt process
   death, retry, concurrent actors, and operator recovery. Classify each as
   relevant, explicitly excluded, or inapplicable from the reconstructed state
   and actors, and explain why. Do not invent scope from owner silence or demand
   a decision about an irrelevant class. Use
   [failure semantics](references/failure-semantics.md).
5. **Classify mechanisms accurately.** Distinguish prevention, atomic publish,
   rollback, compensation, cleanup, retry, resume, crash recovery, Git
   recovery, and provenance recording. A mechanism may be useful while its
   label or claimed scope is wrong.
6. **Audit oracle genealogy.** Trace where every test expectation came from. A
   same-change test can validly show conformance to an owner request or external
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

## Finding standard

For each finding, provide:

- a tight code, test, prose, or architecture location;
- the exact claim and why it matters;
- the claimed property versus the demonstrated property;
- the relevant authority and evidence lineage;
- a direct observation or discriminating counterexample;
- realistic impact under the named failure or decision path;
- the smallest correction direction; and
- confidence and unverified limits.

Rank findings by likely system or decision impact. A terminology finding is
material when the inflated term can drive an unsafe design, false assurance,
or unnecessary machinery—not merely because another word is more precise.

## No-material-findings conclusion

If no material issue remains, say so. Name any unverified authority assumption,
failure class, interleaving, remote behavior, or recovery operation. Preserve
anti-findings:

- do not say an exception handler “does nothing” when it aids retry;
- do not call a test circular merely because it was authored with the change;
- do not assume Git replaces operational recovery outside committed tracked
  state;
- do not demand crash safety when the owner explicitly promises only
  exception cleanup; and
- do not demand provenance machinery when a local fact and owner decision are
  sufficient.

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
