# Owner request: private staging cleanup

Each worker receives a unique reserved destination name and an exclusively
owned staging directory that no other worker may inspect or adopt. Validate the
staged document before publication. If validation raises an ordinary exception,
remove the private stage and verify its absence so an immediate retry starts
cleanly. If cleanup cannot complete, surface that condition and do not report
the job as retryable. Publish with one same-filesystem atomic rename after
validation.

The first version does not promise cleanup after process termination; a
separate age-based scavenger may address abandoned stages later. Once
published, this operation must never delete or restore the destination.
