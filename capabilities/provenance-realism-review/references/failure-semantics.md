# Failure semantics

Mechanism names are hypotheses. Reconstruct the state transitions first, then
classify them.

## State worksheet

```text
Actors and observers:
Resources:
Initial state:
Private staging state:
Durable write points:
Publication/adoption point:
Ownership at each point:
Successful postcondition:
Failure postconditions:
Existing platform recovery:
```

## Minimum failure matrix

| Failure class | Question |
| --- | --- |
| Ordinary exception | Which writes happened before the handler ran, and can its own actions fail? |
| Abrupt termination | What durable state survives when no handler runs? |
| Retry | Is identity stable, and can replay duplicate, overwrite, or delete state? |
| Concurrency | Can another actor observe or adopt state before cleanup or compensation? |
| Operator recovery | Which facts and tools remain, and is manual reconstruction in scope? |

Add network partition, partial remote success, filesystem boundary, database
isolation, or adversarial actor only when relevant. An owner may intentionally
exclude a class; the guarantee must then be worded to match.

## Classification guide

- **prevention** avoids entering a bad state through validation, reservation,
  isolation, or access control;
- **atomic publish** hides partial state from the defined observers;
- **rollback** restores prior state inside an actual transaction boundary;
- **compensation** performs a later semantic reversal and can conflict or fail;
- **cleanup** removes exclusively owned disposable state;
- **retry** starts an operation again;
- **resume** continues from a durable checkpoint;
- **crash recovery** detects and repairs states left without a running handler;
- **Git recovery** reconstructs committed tracked state; and
- **provenance recording** makes origins and derivations inspectable.

One implementation can provide several of these, but none implies the others.

## Publication and ownership rule

Before publication, a caller can usually delete its private staging state. Once
state is shared or adopted, symmetric local undo may no longer be safe. Ask:

- Who can discover the state?
- When can another actor rely on it?
- Does a record of “created by A” still grant A exclusive deletion authority?
- Can publication be delayed or made atomic?
- Can completion be idempotent and forward-only?

Prefer a probe at the publication boundary when evaluating transaction or
concurrency claims.

## Git boundary

Git is sufficient only when the recovery objective is defined in terms of
available committed objects and refs, and operator or automated Git recovery is
acceptable. It does not automatically cover:

- untracked or uncommitted workspace bytes;
- a second repository's not-yet-committed state;
- databases, queues, APIs, credentials, or remote side effects;
- atomic coordination across repositories; or
- a retry worker that specifically requires restoration at a live path.

Credit existing Git recovery where it satisfies the stated objective; do not
build parallel copies merely to imitate version history.
