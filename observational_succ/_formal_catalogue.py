"""Reviewed kernel build admissions, owned by the integration coordinator.

This is installed trusted code, not a caller-editable receipt registry. Add only
canonical SHA256 digests after inspecting real pinned build output, exact theorem
types, axiom audits and source hashes. A digest is an admission decision, not a
cryptographic proof of execution. An empty catalogue deliberately fails closed.
"""
# Actual pinned hosted run 39505507598, job 118913289015, reviewed by coordinator.
# PR head 5bf5f249d040bfcee53c86e4cd65b0f28113f104; Actions merge checkout
# 67da5369b6037a335ff2009b900e4bcd347557ee has the identical source tree.
APPROVED_RECORD_DIGESTS = frozenset({
    "9de79bcbe52c79f1829361c611d97a77b82dc08d9a5fe6181931b78865c8a9f4",
})
