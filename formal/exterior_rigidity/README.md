# Exterior determinant formal research

**Build status at implementation:** awaiting an actual pinned kernel run. The
presence of Lean source is not a kernel-verification receipt. The workflow writes
a research-only observation only after all eleven positive declarations, their
exact type/axiom exports and three deliberately false mutations pass their gates.
It does not add entries to the installed Level C authority catalogue.

The project pins Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Its source uses an arbitrary finite
index type, so finite dimension is a parameter. Columns are source points and
rows are source arithmetic coordinates. All determinant entries are integers in
the arithmetic theorems; the elementary row-product and row-replacement lemmas
are generalized to any commutative ring.

For natural row moduli `d i`, a positive natural sum modulus `q`, and
`P = ∏ i, d i`, `g = gcd_i d i`, the principal proposed export is

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
