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

1. Pin the capability revision, scenario revision, model, and runner settings.
2. Copy only the selected scenario and canonical capability into an isolated
   local workspace.
3. Ask for a review without naming the expected disposition.
4. Preserve the response and tool record without adding hidden source bodies.
5. Have an evaluator compare semantic behavior with the held-out scorecard.
6. Record required concepts, forbidden assertions, acceptable alternatives,
   false positives, and limitations—not exact phrase matches.
7. Repeat across both cases. A capability does not pass if it finds the flawed
   case by condemning the legitimate control too.

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
