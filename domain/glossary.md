# Provenance-realism glossary

These terms are deliberately separate. A review should qualify ambiguous words
instead of using one as a flattering synonym for another.

## Claim and evidence terms

### Provenance

Evidence of a claim or artifact's origin, authority, derivation, and relevant
transformations. Provenance can make history inspectable; it does not establish
correctness, undo state, or provide atomicity.

### Authority

The person, repository, contract, or platform entitled to decide a requirement
for the scope under review. Filesystem location and historical placement do not
create authority by themselves.

### Evidence lineage

The directed relationships among a claim, its sources, derived requirements,
chosen mechanisms, validation oracles, and observations.

### Independent evidence

Evidence whose expectation comes from a distinct authority, normative
contract, or observation rather than solely from the mechanism being assessed.
Independence is relative to a claim: a same-change test can independently check
code behavior against an owner requirement while remaining unable to prove
that the requirement itself is necessary.

### Closed evidence loop

A derivation cycle in which a mechanism motivates a new description, the
description becomes a test expectation, and the passing test is then offered
as evidence that the mechanism or requirement belongs. The loop demonstrates
internal consistency, not external necessity or realistic guarantees.

### Implementation invariant

A condition enforced by the current implementation. It may be desirable and
well tested without being an externally required behavior.

### Provenance theater

The appearance of substantiation through hashes, manifests, receipts, schemas,
tests, or elaborate terminology when the relevant authority or derivation edge
is still missing. This is a finding only when the appearance can mislead a
material decision; extra metadata alone is not enough.

## State and failure terms

### Atomic publish

A transition whose defined observers see either the prior shared state or the
completed new state, not an exposed partial state. The observer set and
durability boundary must be stated.

### Rollback

Restoration of prior state inside a defined transaction boundary. Because the
word is overloaded, reviews should qualify it: database rollback, Git revert,
filesystem restoration, or compensating action.

### Compensation

A later action that mitigates or semantically reverses an earlier action.
Compensation may be useful without recreating exact prior state and may itself
fail or conflict with another actor.

### Cleanup

Removal of caller-owned disposable state. Cleanup is legitimate before
publication when ownership is exclusive. It must not silently delete adopted,
published, or foreign state.

### Retryability

The ability to repeat an operation without corrupting state or producing an
unacceptable duplicate effect. Retrying from the beginning is not the same as
resuming from a checkpoint.

### Idempotency

A property under which repeating a defined operation with the same identity
has the same externally relevant effect as performing it once.

### Resume

Continuation from a durable, inspectable checkpoint. A forward-only resumable
workflow can be safer and simpler than symmetric undo.

### Crash recovery

Detection and recovery after abrupt termination, including failure between
durable writes. Catching a language-level exception does not demonstrate crash
recovery.

### Crash consistency

The set of states that may remain after abrupt termination and the invariants
each state preserves.

### Concurrency safety

Preservation of the claimed invariants across relevant interleavings and
multiple actors. A compensation safe for private state may become destructive
after another actor adopts that state.

### Durability boundary

The point at which state survives process termination and becomes part of the
recovery problem. Memory, a temporary file, a filesystem rename, a local Git
commit, and a remote API result have different boundaries.

### Git recovery

Operator or automated reconstruction from committed Git objects and refs. Git
can be sufficient for a tracked-state recovery objective; it does not make
cross-repository work atomic or automatically restore untracked, uncommitted,
or external state.

### Custody

Which authority may retain, mutate, publish, or delete a durable body. Custody
is an authorization boundary, not merely a location field.
