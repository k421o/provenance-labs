# Owner request: single-body admission

Move each selected document from its managed checkout into the shared
content-addressed registry. On success, the destination digest must verify and
the managed source path must be absent. Reuse an identical existing record
rather than create a second body.

Managed checkouts are disposable copies; the original source repository remains
untouched. Multiple admission workers may process identical bytes concurrently.
A failed job must be diagnosable and safe to retry. This request does not
require recreation of the disposable managed path after failure.
