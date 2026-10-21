"""Reviewed kernel build admissions, owned by the integration coordinator.

This is installed trusted code, not a caller-editable receipt registry. Add only
canonical SHA256 digests after inspecting real pinned build output, exact theorem
types, axiom audits and source hashes. A digest is an admission decision, not a
cryptographic proof of execution. An empty catalogue deliberately fails closed.
"""
# Actual pinned hosted run 39546972269, job 119047533851, reviewed by coordinator.
# PR head 96d224766ae704ff1c185e656e54b0af6cfe4a34; Actions merge checkout
# cd86ebdfada1b8bc8f0cd8666dd08658c5e6a52c has the identical checked source tree.
# Nineteen exact exports, 21 matching source hashes, five rejected mutations.
# Main VII's ten-export record remains archived but is not current authority.
APPROVED_RECORD_DIGESTS = frozenset({
    "aade7c2f1c3abe0a8822f12f8cfb81a53696fd1094cf6981740737c84f90c466",
})
