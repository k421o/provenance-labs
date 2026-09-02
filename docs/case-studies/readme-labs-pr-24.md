# Case study: exception compensation presented as transactional admission

Status: **observation plus review hypothesis**, 2026-09-02. The source pull
request is open and may change; this case is pinned to one revision.

## Pinned and dated sources

- The local [issue #23 source record](sources/readme-labs-issue-23.md) preserves
  the owner request observed from a mutable GitHub issue, including its source
  timestamps and canonical body digest.
- [PR #24 at `0562a5b`](https://github.com/k421o/readme-labs/tree/0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1)
  is the reviewed implementation, based on
  [`f49daf7`](https://github.com/k421o/readme-labs/tree/f49daf761b377859f7d940d9a2a9402f0657c035).
- The implementation's
  [`rollback_readme_artifact_transfer`](https://github.com/k421o/readme-labs/blob/0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1/src/readme_lab/readme_artifacts.py#L454-L466)
  restores a managed checkout body and may remove its record.
- The architecture prose calls
  [admission transactional](https://github.com/k421o/readme-labs/blob/0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1/docs/repository-ingestion.md#L216-L235).
- A new test asserts
  [source restoration after manifest verification fails](https://github.com/k421o/readme-labs/blob/0562a5b6bd08eb7b5caf38ca5743c4a6adf0aab1/tests/test_ingestion.py#L365-L403).

## What the mechanism does

The successful path moves a completed `README.md` from a managed checkout into
a content-addressed record, writes and verifies a manifest, and marks an
ingestion job admitted. If a Python exception occurs after a transfer, the
controller removes the manifest, restores each managed source, and removes
other paths created by the call.

That is real behavior. It can make an immediate retry more convenient and can
reduce some partial states after caught exceptions.

## What the evidence does not establish

Issue #23 calls intake “transactional transport,” but it does not define the
transaction's observers or failure model. Its acceptance criterion for transfer
is the successful postcondition: destination digest verified and prior managed
path absent. It does not explicitly require restoration of the disposable
checkout on failure. The implementation, prose, and test concretize one
interpretation of “transactional,” but their agreement does not independently
prove that this interpretation is required.

The mechanism catches language-level exceptions. It does not run after process
termination, power loss, or a host crash, so it does not by itself provide
crash atomicity. The original repository used to create the managed checkout
remains untouched, which further narrows restoration's likely value to local
retry ergonomics rather than source-data safety.

Git can recover committed tracked versions in the source and destination
repositories. It does not automatically make the uncommitted cross-repository
operation atomic. The review question is therefore not “rollback or Git?” but
which postcondition is required, at which durability boundary, and for which
failure classes.

## Discriminating concurrency case

At the pinned revision, a newly created content-addressed record is immediately
discoverable by path. Consider this interleaving:

1. Admission A creates record `R` and records that it created the record.
2. Admission B, with identical bytes, finds `R`, adopts it as canonical, and
   deletes B's managed source.
3. A later step in admission A raises an exception.
4. A's rollback moves the body out of `R` and removes the entire record.

B now has neither its managed source nor the shared record it adopted. The
compensation was locally symmetric for A but crossed an ownership boundary
after publication. This counterexample separates “the handler restores A's
checkout” from “admission is transactionally safe.”

## Review hypothesis

A provenance-realistic review should:

- credit the exception handler for the behavior it actually provides;
- ask an owner to decide whether checkout restoration is a required retry
  contract or an implementation preference;
- avoid using the matching test as evidence for the requirement's necessity;
- narrow “transactional” to exception compensation unless stronger properties
  are implemented and tested;
- examine interruption and concurrent adoption before claiming atomicity; and
- consider private staging, atomic publication, idempotent completion, and
  forward resume before adding broader undo machinery.

The paired evaluation scenarios distill this case without copying the source
repository. The finding fixture is a synthetic, minimized derivative of the
public MIT-licensed transfer algorithm and records that derivation in its
source header. Its held-out expectation is kept outside the staged scenario.

## Limitations

This case does not decide README Labs architecture. It does not establish that
all restoration is unnecessary, that Git is sufficient for every admission
failure, or that the open pull request cannot be repaired. Those decisions and
changes remain with the README Labs owner.
