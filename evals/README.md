# Review evaluation scenarios

The initial evaluation is a paired behavioral probe:

- `record-publication-a` contains a material shared-state compensation failure
  and a requirement-lineage question.
- `record-publication-b` is a false-positive control containing legitimate
  cleanup of exclusively owned private staging.

Each scenario directory is agent-visible. Its corresponding scorecard lives
under `evals/expectations/` and must not be staged into the review workspace.
The repository is public, so “held out” describes evaluation isolation, not
secrecy.

## Trial protocol

1. Pin the capability revision, scenario revision, model, runner settings, and
   isolation policy.
2. Start a fresh task with no prior factory or scorecard context. Copy only the
   selected scenario and canonical capability into an isolated local workspace.
3. Deny the reviewed agent filesystem access to the factory checkout and
   `evals/expectations/`. Disable network access because this local fixture
   needs no external source and the public scorecard is otherwise retrievable.
4. Ask for a review without naming the expected disposition.
5. Preserve the response and tool record without adding hidden source bodies.
   Audit the record for unexpected access before scoring.
6. Have a separate evaluator compare semantic behavior with the held-out
   scorecard.
7. Record required concepts, forbidden assertions, acceptable alternatives,
   false positives, and limitations—not exact phrase matches.
8. Repeat across both cases. A capability does not pass if it finds the flawed
   case by condemning the legitimate control too.

If the runner cannot enforce fresh context, factory-path denial, and the stated
network policy, label the result **non-blinded**. It may inform fixture design
but cannot count as held-out promotion evidence.

The current repository checks validate fixture separation, structure, and the
mechanical behavior that distinguishes the pair. They do not execute an agent
or claim review-quality success.

## Next discriminating cases

The [bootstrap issue](https://github.com/k421o/provenance-labs/issues/1) tracks
additional pairs before the domain claims a stable evaluation laboratory:

- owner-required restoration versus a mechanism-invented restoration rule;
- exception compensation versus a genuine crash-recovery guarantee;
- Git-sufficient committed recovery versus untracked or external effects;
- forward-only resumable admission versus unnecessary symmetric undo; and
- integrity hashes with complete versus missing authority/transformation
  lineage.
