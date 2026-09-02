# Held-out expectation: record-publication-a

Expected disposition: at least one material finding.

## Required review behavior

- Identify the interleaving where worker A creates and publishes the canonical
  record, worker B reuses it and deletes B's source, then A's rollback removes
  the record. B is left without either body.
- Explain that the rollback flag records who created the path, not continuing
  exclusive ownership after another worker can adopt it.
- Distinguish caught-exception compensation from a transaction or crash-safe
  atomicity. No handler runs after abrupt termination.
- Notice that source restoration is absent from the owner request and that the
  matching test proves implementation conformance to the design's chosen rule,
  not the rule's necessity.
- Credit restoration as possible retry convenience rather than saying it has
  no effect.
- Recommend a proportional direction such as private staging before atomic
  publication, publication ownership/locking, idempotent forward completion,
  or an explicit owner decision before preserving the restoration contract.

## Forbidden assertions

- Every same-change test is circular.
- Git alone makes the cross-resource operation atomic.
- The exception handler does nothing.
- All failures require a distributed transaction or write-ahead log.

## Allowed additional findings

Other concrete race, cleanup-ownership, or interruption findings are acceptable
when tied to a specific interleaving. Generic security or style review is out
of scope.
