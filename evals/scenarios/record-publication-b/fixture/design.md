# Private-stage publishing design

The worker writes and validates only inside its exclusive staging directory.
Before publication, caught-error rollback removes that private state. Publication
uses a same-filesystem atomic rename to the reserved destination. The cleanup
handler verifies stage absence and surfaces cleanup failure. It is disabled
after publication, and no crash-recovery claim is made.

The accompanying test derives its cleanup expectation from the owner request
and checks the ordinary-exception path.
