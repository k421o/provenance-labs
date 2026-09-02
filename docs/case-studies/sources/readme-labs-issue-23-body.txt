## Problem

README Labs currently permits the same README bytes to have more than one durable body-owning path. The concrete case is the generated forward-test README, which exists both inside an intake snapshot and inside its README artifact record. Capture and verification then preserve both paths because downstream records were designed around that topology.

Those are circular implementation contracts, not independent product requirements. Git already provides version history, rollback, immutable blobs, and temporary worktrees. Provenance should identify a custody transition; it should not require retaining the body at every stage.

## Architectural decision

- At HEAD, one logical README has exactly one durable body-owning path in this repository.
- Intake is a transactional transport and provenance boundary, not durable README storage.
- A completed README is landed directly in its final README record during admission.
- Custody transfer has move semantics: destination verified, prior managed path absent at completion. Cross-filesystem implementations may briefly copy and verify internally.
- Historical versions are recovered from Git rather than retained as parallel live files.
- Experiments may materialize disposable copies for mutation, relative-path behavior, and isolation, then remove them.
- Evidence stores identity and measurements, not another full README body.
- Internal reference-only records are not a substitute for landing an owned README body.
- SQLite remains a rebuildable catalog/index; Markdown bodies stay as Git-managed files.

## Implementation plan

- Redesign README admission/capture around one final body and a verified transfer receipt.
- Remove live-path verification rules that require an obsolete intake copy.
- Route contextual evaluation through disposable materialization from the final README body.
- Reject overlapping selections/context that could duplicate nested README bytes.
- Migrate the committed forward-test README to one current body and update its manifests, runs, evidence, documentation, and tests.
- Stop durable event logs from embedding complete README command output; migrate the known trace.
- Add a repository-wide invariant test that rejects duplicate durable README bodies except explicitly classified generated distribution output.
- Update architecture and ingestion documentation to state the single-body rule and Git-based version model.
- Run the complete test, lint, schema, artifact, and generated-product verification surfaces.

## Acceptance criteria

- The known README digest `f96b8e9d…720a0` has one durable body path at HEAD.
- New completed README ingestion creates no intake snapshot copy.
- Successful transfer proves the destination digest and absence of the prior managed path.
- Contextual experiments still run with a temporary root `README.md`.
- Historical provenance remains available through Git and metadata.
- No full subject README is embedded in durable event logs.
- All checks pass and the change ships in one pull request.
