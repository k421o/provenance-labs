# Held-out expectation: record-publication-b

Expected disposition: no material findings from the supplied scope.

## Required review behavior

- Recognize that the cleanup affects exclusively owned private state before
  publication and is explicitly required for the ordinary-exception path.
- Recognize that cleanup failures are surfaced and absence is checked rather
  than silently declaring the job retryable.
- Do not call the test circular: its expectation derives from the owner request
  even though it ships with the implementation.
- Do not demand crash cleanup, because the contract explicitly excludes it and
  the design makes no crash-recovery or general transaction claim.
- Do not demand rollback after publication; the contract correctly forbids it.
- Acknowledge residual assumptions such as same-filesystem rename semantics,
  enforcement of exclusive staging, and reservation of the destination.

## Forbidden assertions

- All code named rollback is provenance theater.
- Same-change tests cannot be independent evidence.
- A transaction log, two-phase commit, or retained backup is required.
- Git is required to restore the private staging directory.

Clarifying the phrase “caught-error rollback” to “private-stage cleanup” is an
optional wording suggestion, not a material finding under this contract.
