# Finding standard

## Materiality gate

Report a finding only when all of these are present:

1. a consequential claim, requirement, or mechanism;
2. a concrete authority, lineage, semantics, or failure-model mismatch;
3. a credible decision or system impact; and
4. a correction direction smaller than “redesign everything.”

Do not report style-only vocabulary preferences, speculative failure classes
outside the promised scope, or the mere presence of extra metadata.

## Finding shape

```text
[priority] Tight location — concise title

Claim: what the change says or relies on.
Evidence: pinned source, direct observation, or bounded reproduction.
Lineage/semantics gap: the exact missing edge or mismatched property.
Impact: who can make a wrong decision or which state can fail.
Direction: smallest owner-respecting correction.
Limits: what was not verified.
```

Use severity based on impact, not conceptual elegance. A concrete data-loss
interleaving outranks an ambiguous label. Avoid presenting an inference as a
reproduction.

## Common material findings

- a caught-exception compensator is called crash-safe or atomic;
- a caller deletes state after another actor can adopt it;
- a test derived only from a new mechanism is offered as proof that the
  mechanism is required;
- Git is credited with recovery of untracked or external effects;
- a hash is treated as authority or full transformation lineage; or
- a provenance record omits the decision source needed for the claim it is
  meant to support.

## Required anti-findings

Do not claim:

- “same PR” alone makes a test circular;
- cleanup of exclusively owned private staging is unsafe rollback;
- an exception compensator has no value merely because it is not crash-safe;
- every operation needs a transaction log or two-phase commit;
- Git is irrelevant when committed-state reconstruction is the actual
  requirement; or
- a system needs provenance infrastructure when a pinned link and explicit
  owner decision are adequate.

## Correction ladder

Prefer, in order of proportionality:

1. narrow the wording to the demonstrated property;
2. record the missing owner decision or source;
3. remove an unsupported guarantee while retaining useful local behavior;
4. isolate private staging and publish atomically;
5. make completion idempotent or resumable;
6. add a discriminating failure/concurrency test; and
7. introduce stronger transaction machinery only when the evidenced boundary
   requires it.
