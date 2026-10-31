# Algebra-front validation and claim authority

Source parent is PR417 `1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`.
All additions are confined to this directory. PR421 was inspected at
`e14916aa2b4dfc2cce948facc729fb02ce1efafa` without importing or merging it.
The complete 46-file universal_nz_carrier baseline was read, including its
historical rational-fixture and shared-precision failures. Source bytes are
preserved by the manifest; no imported mathematical contract was changed.

* `receipts/focused.log`: **14 tests PASS**. They exercise full labeled
  composition, three-block associativity, signed representatives, negative
  ranks, matrix-coefficient products, reachable-state versus operator
  flatness, transported swap defects, original-source order and seed controls.
* `receipts/independent-oracle.log`: separate actual-subset and SymPy route
  PASS:122 colored subset fibers,8 matrix-product grades reconstructed by
  finite differences,255 fresh reachable diamond cases,3 fresh BBP orderings.
  This oracle imports no carrier implementation. It shares the theorem and
  model lineage, so it is not independent expert approval.
* `receipts/lean-final.log`: **Lean4.14.0 kernel PASS** for seven declarations:
  recursive Pascal step and normalization, doubled integer polarization,
  normalized integer recovery conditional on that doubled certificate,
  integer affine-swap defect, additive word grade, and list associativity.
  Printed axioms are only `propext` and `Quot.sound` where reported; no
  `sorryAx`. There was no mathlib installation or network dependency fetch.
* `receipts/lean-negative-control.log`: deliberately false numeric
  polarization is **REJECTED**, as required. This is a passing hostile gate
  with process exit1, not a compilation success. The control file is named
  explicitly and must not be included in the positive Lean target set.
* `receipts/observer-review.log`: independent CDF/word-lasso checks PASS,
  768 exact W1 cases and2,046 finite words. See OBSERVER_REVIEW.md.
  The final observer API recheck also passes in observer-review-refreshed;
  this is a repeat check, not additional independent evidence.
* `receipts/new-transport-review.log`: exact independent analytic/frame
  checks PASS:2 Markov rational-function identities,3 authentic Padé
  degrees with Gaussian moment defects,90 prime-germ moment cases and180
  Hermite monomial cases. REVIEW_NEW_TRANSPORT.md gives the paper audit,
  final reviewed hashes and scope. No mathematical revision was required.

The first Lean attempt failed because `omega` treated `(2*a)*b` and
`2*(a*b)` as unrelated nonlinear atoms. Its exact source is preserved in
`CarrierAlgebra.initial-failure.lean.txt` and output in
`receipts/lean-initial-failure.log`; explicit associativity rewrites repaired
the proof. The intermediate corrected pass is also retained. Earlier
read-only inspection found PR421 not fetched yet and guessed unavailable
mathlib-cache paths; after the parent fetched refs, PR421 was read. These
were environment inspection failures, not mathematical counterexamples.

**Formal scope is deliberately narrower than the paper.** Lean does not
identify the recursive Pascal table with binomial factorials, prove the
full category/bijection or diamond-descent theorem, or certify any Newton
series convergence, BBP analytic distribution, zeta result or RH statement.
Those paper statements have the written proofs in ALGEBRA_THEOREMS.md and
the stated finite implementation calibration. Root repository checks and
hosted CI are the principal agent's separate responsibility.

The strongest source-specific statement here is the all-horizon strict
unwrapped ordering inequality. It also holds for the coherent changed seed.
It therefore does not earn selected-normality credit. The exact circle
alias control shows why an unwrapped inequality cannot simply be promoted
to signed cancellation.
