# Source record: `k421o/readme-labs` issue #23

Source locator: <https://github.com/k421o/readme-labs/issues/23>

- Created: `2026-09-01T22:29:47Z`
- Last updated when retrieved: `2026-09-01T22:30:40Z`
- Retrieved: `2026-09-02T18:15:10Z`
- Raw decoded body SHA-256:
  `158af571def892affc7801cac9278029609060c0c35e313775780cc1cefe086b`
- Frozen snapshot SHA-256:
  `7c6fa387eab8de6cb572e9cd05c756c20260dcc191a1b3315c4a6097c285d328`
- Canonicalization: decode the issue body as UTF-8, collapse its run of terminal
  LF bytes to one LF, and make no other change. The raw digest was produced by
  `jq -j '.body'` from the GitHub REST response; the snapshot uses the stated
  terminal-newline normalization.

The locator is mutable. The normalized decoded body observed at retrieval is
stored as a [frozen text snapshot](readme-labs-issue-23-body.txt); its bytes
match the frozen snapshot digest above. This public source is owned by `k421o`;
the source repository and this derivative record use the MIT license.

## Relevant observations

- The owner selected a single durable body-owning path and move semantics at
  successful completion.
- The issue calls intake transactional transport but does not define the term's
  failure classes or observers.
- The acceptance criteria require destination verification and managed-source
  absence on successful transfer; they do not require recreation of the
  disposable managed path after failure.
- The issue identifies Git as the history and rollback mechanism for prior
  tracked bodies.
