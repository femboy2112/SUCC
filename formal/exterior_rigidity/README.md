# Exterior determinant formal research

**Verification:** all eleven declarations passed the actual pinned Lean kernel
build in [run 39548086330](https://github.com/femboy2112/SUCC/actions/runs/39548086330),
job `119050852183`, at PR #220 head
`d54ea23a3cd1f4e0c8d81484c039fa145a050326`. All three deliberately false mutations
were rejected for their expected proof errors. The synthetic merge
`6f59c91dba1e99466277503db09cd3f3c5bdf6c0` and the head have the identical tree
`ee3f4f703adb41f5f427735ed7d10dc1a2ee4360`. The complete observed receipt is
[kernel-observation-39548086330.json](receipts/kernel-observation-39548086330.json),
file SHA256 `87f4e15159b79a554d16d5d528dab2d8cf44266418cf0364cb9af22f0303d8b9`.
Its status is **KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED**. No entry was added to
the installed Level C authority catalogue.

The project pins Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Its source uses an arbitrary finite
index type, so finite dimension is a parameter. Columns are source points and
rows are source arithmetic coordinates. All determinant entries are integers in
the arithmetic theorems; the elementary row-product and row-replacement lemmas
are generalized to any commutative ring.

For natural row moduli `d i`, a positive natural sum modulus `q`, and
`P = ∏ i, d i`, `g = gcd_i d i`, the principal checked export is

\[
\frac{Pq}{\gcd(q,g)}\mid |\det A|.
\]

The assumptions are exactly that `d i` divides every entry of row `i` and `q`
divides every column sum. Zero row moduli are permitted, with the usual exact
integer divisibility convention; no positivity of matrix entries is required.

The proof route differs from the manuscript's prime-adic lcm calculation. Row
multilinearity proves `P | det A`. Replacing row `i` by the sum gives a new
product divisor, hence `Pq | d i det A`. Taking the gcd of these natural
magnitude divisibilities gives `Pq | g |det A|`. The original row-product
divisor also gives `Pq | q |det A|`. Another gcd and exact cancellation produce
the displayed divisor. If any one column is globally primitive, its coordinate
gcd forces `g=1`. This recovers the full-product divisor without pairwise
coprimality. No division by a possibly zero modulus is performed: `q>0` makes
the canceled gcd positive.

The effective-modulus declaration's exact Lean type SHA256 is
`0ccbabc1c862e2699ef04e91ecce8085c47dda84df3787547947cddda3caa080`.
The primitive full-product type SHA256 is
`bc7ce6d0e88b5f2c01aa3d5bb0852e93fa5df16b93d2d98ca2feda2d6c70b80c`.
All eleven full expressions, quantified hypotheses, universe parameters and
transitive axiom lists are in the receipt. Their digests were independently
recomputed; all eight bound source hashes match the checked published tree.
Every observed axiom list is exactly `propext`, `Classical.choice`, `Quot.sound`.

The formalized vanishing corollary takes `|det A| < E` as an explicit hypothesis.
**Hadamard bounds and the rational rank/cardinality theorem are not formalized
here.** In particular determinant vanishing never asserts singleton rigidity.
The file contains exact countercontrols: a shared-prime nonprimitive matrix
with determinant magnitude 8 although the full product is 16, and the two
distinct globally primitive three-summand source points at height 9015 from
PR #214, with full modulus greater than the cubic height.

## Reproduction and trust boundary

The separate `.github/workflows/exterior-rigidity.yml` downloads the same
hash-verified Lean archive as the admitted projects, retrieves only the imported
mathlib dependency closure, and serializes against other formal jobs. Run its
cache command, then `python3 formal/exterior_rigidity/check.py OUTPUT_DIRECTORY`.
The checker rebuilds local theorem outputs, verifies dependency pins, exports
full Lean expressions and transitive axioms and rejects false shared-prime,
nonstrict-bound and numerical-control mutations. Output contains complete
compressed observations as well as artifact logs and SHA256 values.

Imported compiler, mathlib compiled cache, hosted runner, trusted checker and
artifact transport remain trusted infrastructure. A research JSON file alone
confers no proof authority. No original arithmetic source, weighted abc moment,
or analytic global counting conclusion is certified by this project.

The first [push build 39547781359](https://github.com/femboy2112/SUCC/actions/runs/39547781359)
failed on a missing finset rewrite and a concrete matrix numeral reduction.
It produced no successful observation. The minimal corrections preserve all
theorem statements. An old-head PR run and a duplicate corrected-head push run
were canceled in the serialized queue; neither is counted as a successful check.
[review-39548086330.json](receipts/review-39548086330.json) records those outcomes,
the exact repair, source comparison and remaining formal obligations.

## Prior art and scope

The proofs are a new-to-project formalization of classical multilinear algebra
and integer divisibility. The primary library dependencies inspected at the
pinned revision are `Matrix.det_mul_column`, `Matrix.det_updateRow_sum`,
`Finset.prod_update_of_mem`, `Finset.gcd_mul_right`, and elementary `Nat.gcd`
divisibility. See the corresponding primary source files:

- [Determinant/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.lean)
- [GCDMonoid/Finset.lean](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Algebra/GCDMonoid/Finset.lean)
- [BigOperators/Group/Finset.lean](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Algebra/BigOperators/Group/Finset.lean)

There is no originality claim. The next formal obligation is a source-height
determinant norm bound followed by rational rank loss, with an explicit firewall
against promoting rank loss to a point count.
