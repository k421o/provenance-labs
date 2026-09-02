# Claim lineage

Use a small ledger for consequential claims. Do not catalog every line or
low-risk choice.

## Claim kinds

| Kind | Review question |
| --- | --- |
| Requirement | Who decided this externally observable behavior belongs? |
| Constraint | Which authority or platform makes this condition binding? |
| Mechanism | What implementation was chosen, and which requirement does it serve? |
| Guarantee | Across which observers and failures is the behavior promised? |
| Rationale | Does the reasoning connect the requirement to this mechanism? |
| Observation | What was directly inspected or reproduced at a pinned state? |
| Hypothesis | What remains a proposed explanation or rule? |

## Source roles

Classify each source as a deciding authority, normative dependency, empirical
observation, implementation assertion, validation oracle, historical context,
or hypothesis. A source may hold more than one role, but record the role used
for the current inference.

## Independent status axes

Do not compress authority, realization, and evidence into one maturity state.
Record them independently:

- **authority disposition:** unlocated, proposed, requested, owner-ratified,
  rejected, or superseded;
- **realization status:** not implemented, implemented, released, or retired;
  and
- **evidence status:** asserted, observed, reproduced, independently verified,
  contradicted, or unknown.

A requirement can be ratified but not implemented. An implementation can be
released while its claimed guarantee is contradicted. Neither implementation
nor release implies authority or correctness.

## Derivation independence

- **independent** — the expectation comes from a distinct authority, normative
  contract, or empirical observation;
- **correlated** — the expectation and implementation share some source but
  retain a distinct derivation edge;
- **same assertion** — prose or test merely re-encodes the mechanism's claim;
  or
- **unknown** — the derivation has not been established.

These classifications are claim-relative. A test may independently establish
that code follows an owner-requested rule while saying nothing independent
about whether that rule is wise.

## Closed-loop test

Do not label evidence circular from “same PR” or “same author.” Trace this
specific structure:

1. Mechanism `M` is selected.
2. Requirement `R` is introduced only as a description or justification of
   `M`.
3. Test oracle `T` re-encodes `R`.
4. `M` passes `T`.
5. That pass is cited as support that `R` or `M` is necessary or realistic.

Steps 1–4 establish an implementation contract. The unsupported reversal is
step 5. Look for an owner decision, external contract, prior observation, or
discriminating comparison that opens the loop.

## Ledger worksheet

For each material claim, record:

```text
Claim:
Kind and scope:
Source + pinned revision:
Source role:
Authority disposition:
Realization status:
Evidence status:
Derives from:
Defines or constrains:
Verification evidence:
Evidence independence:
Unverified limits:
```

Prefer repository-relative paths and immutable revisions in durable records.
Do not copy private or unnecessary source bodies merely to establish lineage.
