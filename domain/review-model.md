# Provenance-realism review model, version 1 draft

## Central object: the claim record

The domain begins with claims rather than a registry of copied artifacts. A
review may keep a lightweight `ClaimRecord` containing:

- the exact statement and its scope;
- claim kind: requirement, constraint, mechanism, guarantee, rationale,
  observation, or hypothesis;
- pinned sources and their roles;
- authority disposition: unlocated, proposed, requested, owner-ratified,
  rejected, or superseded;
- realization status: not implemented, implemented, released, or retired;
- evidence status: asserted, observed, reproduced, independently verified,
  contradicted, or unknown;
- derivation relationships among claims;
- relevant actors, resources, owners, and durability boundaries;
- explicit failure classes;
- verification evidence and its independence;
- limitations, confidence, and review disposition.

This is a semantic model, not yet a JSON schema. Repeated cases should reveal
stable fields before the repository freezes a machine representation.

## Claim graph

A healthy conformance chain normally runs in this direction:

```text
deciding authority --authorizes--> requirement --constrains--> mechanism
normative contract --constrains----> requirement
requirement        --defines--------> oracle --evaluates--> implementation
probe              --produces------> observation
observation        --supports/refutes-----------------------> guarantee
```

An observation may motivate a proposed requirement, but a deciding authority
must authorize that requirement for its scope. Empirical frequency or a
reproduced failure does not silently become policy.

A suspicious closed loop reverses the evidentiary force:

```text
mechanism --> same-change description --> test oracle --> passing mechanism
    ^                                                     |
    +-------------- cited as proof of need ---------------+
```

The second graph does not make its tests useless. They can still catch a
regression in the selected mechanism. They cannot independently establish that
the requirement was requested, that its scope is correct, or that its name
matches its failure semantics.

Use the counterfactual question: **If the proposed mechanism, its new prose,
and its new tests disappeared, what support for the requirement would remain?**
An answer of “none” calls for owner clarification or a weaker claim, not an
automatic rejection.

## Operational reconstruction

For each material guarantee, reconstruct the operation independently of its
names:

1. Enumerate resources and actors.
2. Mark each state private, shared, adopted, or externally visible.
3. Identify ownership and custody at every transition.
4. Mark durable write and publication points.
5. State the successful postcondition.
6. Enumerate cut points for ordinary exception, abrupt process death, retry,
   concurrent actors, and operator recovery.
7. Classify each mechanism using the
   [glossary](glossary.md), then compare behavior with the stated claim.

A failure class may be excluded when it is inapplicable to the reconstructed
state and actors, or when the owner excludes it and the public claim is
correspondingly narrow. Record the reason; do not invent scope from silence or
demand an owner decision for a genuinely irrelevant class.

## Review dispositions

A review should select the smallest proportional direction:

- **keep** — the requirement and mechanism are supported at the stated scope;
- **clarify** — behavior is useful but terminology or failure scope is wider
  than the evidence;
- **simplify** — an existing platform guarantee or smaller mechanism satisfies
  the actual requirement;
- **use forward recovery** — durable checkpoints, idempotence, or resume are
  safer than undo;
- **strengthen** — the guarantee is required but implementation or evaluation
  omits a relevant failure class;
- **return to owner** — necessity or tradeoff requires an authority decision;
  or
- **remove** — the mechanism creates material risk without an evidenced need.

“Add more rollback machinery” and “Git already handles it” are not default
answers. Both require a boundary-specific argument.

## Finding classes

- **unsupported requirement** — no adequate source establishes that the
  behavior belongs;
- **semantic inflation** — the term used promises more than the mechanism;
- **closed evidence loop** — internal consistency is presented as independent
  support for need or realism;
- **missing failure model** — a consequential guarantee has no stated cuts or
  observer boundary;
- **unsafe compensation** — undo crosses ownership or conflicts with adoption;
- **platform-boundary error** — Git, database, filesystem, or remote semantics
  are credited with a property outside their scope; and
- **provenance gap** — a material origin, authority, or transformation edge is
  absent.

These are diagnostic categories, not reasons to manufacture a finding. Report
only issues with a credible impact and a smaller correction direction.

## Finding and no-finding standard

Each material finding includes:

- a tight location and exact claim;
- the claimed property and the demonstrated property;
- relevant source roles and derivation path;
- direct evidence or a discriminating reproduction;
- realistic impact;
- the smallest correction direction; and
- confidence and unverified limits.

When no material issue remains, say so and name unverified failure classes,
authority assumptions, or probes. Preserve anti-findings: do not claim that a
handler does nothing when it improves retry convenience, that all same-change
tests are circular, or that Git replaces all operational recovery.
