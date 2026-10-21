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
