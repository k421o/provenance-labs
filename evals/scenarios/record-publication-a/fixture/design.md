# Transactional admission design

Admission is transactional. If record creation, manifest writing, or immediate
verification fails, rollback restores the selected document to its managed
checkout and removes every record created by the failed admission. A unit test
that forces manifest verification to fail proves the transaction restores its
prior state.

Content-addressed record paths are canonical as soon as they exist. A later
worker finding an identical record may reuse it and remove its redundant
managed source.
