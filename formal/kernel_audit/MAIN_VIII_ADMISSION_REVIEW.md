# Main VIII formal admission review

The reviewed incoming slope head is
`e8c12ca0eac57dcffce59747ad160330f6225756` (PR #211). The archived
run-39508738928 observation is a `succ.lean.research.v1` record, explicitly
`KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED`. Its file SHA256 is
`094a35e5ed7dae06d99efb159e6283a674862f5441499f6f60e0efa12614cdc1`.
It contains nine canonical declarations, their full Lean expressions,
universe parameters and transitive axioms. They formalize determinant
divisibility, reduced-slope injectivity, determinant separation and two exact
negative controls. They do not formalize a counting theorem, weighted moment,
the Euler product, or original-source transport.

The theorem source is unchanged: `PrimitiveSlope.lean` SHA256
`385c1356c2b7e7558a7b3872649bd996a7d6e1cd0b6dc56ce460dc75b2690210`.
The central separation declaration's exact type SHA256 is
`0830694aeba6822f94ee18b12e46d93baaaf238b89d9f7963b75285324471d01`.
All nine observed axiom lists lie in `propext`, `Classical.choice`, `Quot.sound`.
The proof uses pairwise coprime prescribed divisors and reduced primitive source
triples. Its nonprimitive and shared-modulus examples retain those hypotheses'
mathematical boundaries.

The Main VIII integration adds these declarations to the existing kernel build
and admission architecture. Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` remain pinned. The three projects
share one dependency cache but rebuild their own theorem outputs serially.
The two false slope mutations join the wrong-source and two Schur controls.
Each rejected slope mutation must exhibit a Lean type mismatch, rather than a
missing executable or merely a nonzero exit status.

**This implementation commit does not admit a new record.** Generator/workflow
changes invalidate the old record's current-source hashes. The coordinator must
inspect a real hosted build containing all nineteen exports and five rejected
controls, archive its unmodified observation, then update the installed catalogue
with that record's canonical digest. The fresh-build comparison and permanent
Main VIII tests then require all nine slopes to discharge their exact typed
propositions through `FormalTheorem.from_receipt` and `Claim.discharge`.
Research-only JSON, forged success metadata, changed types, unrelated English
claims, implicit specialization and source-transport assertions remain rejected.

This is a new-to-project formal certification extension of classical elementary
number theory. It carries no originality claim and supplies no endpoint result.

## Actual coordinator admission (2026-10-21)

Hosted run `39546972269`, job `119047533851`, rebuilt all three projects and
exported all 19 types on PR head `96d224766ae704ff1c185e656e54b0af6cfe4a34`.
The Actions merge checkout was `cd86ebdfada1b8bc8f0cd8666dd08658c5e6a52c`,
tree `068bd89a648660f76c336d9f4626421bd4c9c6d2`, identical to that PR head.
All five negative controls were rejected for the expected Lean errors.
The last admission comparison failed against the old catalogue as intended;
the build/export itself succeeded. This run is not reported as overall green.

The coordinator retrieved the complete compressed record from the actual job
log, matched its file hash, checked all 21 source hashes against the local
candidate, and compared the five polynomial, five Schur and nine slope exports
against their earlier observations. Every exact type and axiom list matched.
The current catalogue admits canonical record digest
`aade7c2f1c3abe0a8822f12f8cfb81a53696fd1094cf6981740737c84f90c466`;
file SHA256 `02c840ea05ff3caf0f25aa48943e0b3b57bc911e6e9f4ab1d7feb440ee695734`;
environment digest
`9358d89c6b763b561a4b8efc4338f9c90f80e46acd3d60d79f7674d77e46fbfd`.
The earlier ten-export record is preserved as
`admitted/main-vii-kernel-attestation.json`, outside current authority.

A subsequent exact-candidate hosted rebuild must pass the fresh/admitted
comparison before integration. Admission is a reviewed trusted-code decision,
not a cryptographic proof that arbitrary caller JSON was executed.
