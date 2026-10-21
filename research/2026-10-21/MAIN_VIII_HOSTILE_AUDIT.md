# Main VIII independent hostile audit: exterior and cofactor ascent

Date: 2026-10-21. Referee worktree: `research/viii-referee-2026-10-21`.
Reviewed PR #214 head: `9372c669892a2a29fb8c16f0fa20c11815f650df`.
Execution tree: unreviewed integration union
`c82f5e34145661d96e87612d0a8cc633759409b7`, descended from main
`b5f9591033db2022bda6a2f16a935c06466f9eff`.

**Verdict: SURVIVES within the stated elementary domains.** No false theorem or
false-positive certificate path was found in this package. This is an independent
agent's proof reconstruction and independently coded exact holdout, not an
external human referee, a formal kernel proof, or a proof that every software
defect is absent. No claim extends the weighted abc moment range to `t >= 2/3`.

## Scope and receipts

| Reviewed file | SHA-256 |
|---|---|
| `observational_succ/exterior_cofactor_ascent.py` | `3ce0eb86cee534066587168b0e2ee6753c1d618ce03adee581f7ea2c43d662ac` |
| `tests/test_exterior_cofactor_ascent.py` | `1ee2c808565917b83060830184556cc774f5a82f97399080072b849439d0da53` |
| `research/2026-10-20/DUAL_SLOPE_EXTERIOR_ASCENT.md` | `e456a75f94b56c3df51a0634be7181d9f2fb88270ae8161a85377e4293247bc7` |

Focused commands, using Python 3.12 in the campaign environment:

```sh
python -m unittest discover -s tests -p test_exterior_cofactor_ascent.py -v
python -m unittest discover -s tests -p test_viii_hostile_exterior.py -v
```

Both succeeded: **11 original tests and 11 independent hostile tests**. A first
attempt to run pytest could not start because pytest is not installed; that was
an environment failure, not a test failure. No full-suite or Lean result is
claimed here. The coordinator owns combined-tree validation.

The new test oracles use the Leibniz permutation determinant, recursive positive
compositions, direct occupation enumeration, and images of finite group maps.
They do not call the production routines to generate expected answers.

## Claim-by-claim reconstruction

### COF-01: identity, inequality, and one-way cutoff

For positive integer summands `x_i`, total `c=sum(x_i)<=X`, and divisors
`d_i|x_i`, `q|c`, write `x_i=d_i u_i`, `c=q u`. Then
`D U = c product(x_i)` exactly, with `D=q product(d_i)` and `U=u product(u_i)`.
AM–GM on the **m summands**, followed by `c<=X`, proves
`DU<=c^(m+1)/m^m<=X^(m+1)/m^m`. Thus `D>X^m` implies `U<X/m^m`.
Every cutoff and every divisor selection must remain in a transported sum.

The reverse implication is false even for powerful moduli and a primitive
source: `(a,b,c)=(1,8,9)`, moduli `(1,8,9)`, cofactors `(1,1,1)`, `X=9`
give `U=1<9/4` but `D=72<81`. The existing dossier does not assert that reverse.

### EXT-01, EXT-02, EXT-04: the shared-prime divisor is correct

The manuscript's row-factor and row-replacement proof is valid. In particular,
replacing row i by the sum of all rows preserves the determinant, because all
other multilinear terms have a repeated row. At a prime with valuations
`alpha_i=v_p(d_i)` and `beta=v_p(q)`, the least common multiple of the resulting
divisors has exponent
`sum(alpha_i)+max(0,beta-min(alpha_i))`. This is exactly the exponent in
`E=Pq/gcd(q,g)`, where `P=product(d_i)` and `g=gcd(d_i)`.

An independent proof uses the source lattice

\[
L=\{(d_1u_1,\ldots,d_mu_m):u\in\mathbb Z^m,
                    \ \sum_i d_i u_i\equiv0\pmod q\}.
\]

The map `u -> sum(d_i u_i) mod q` has image the subgroup of multiples of
`h=gcd(q,d_1,...,d_m)` in `Z/qZ`, of size `q/h`. Its kernel therefore has index
`q/h`. Diagonal scaling multiplies the lattice index by `P`, giving
`[Z^m:L]=Pq/h=E`. In an integer basis of `L`, any m source columns are an
integer coefficient matrix, so their determinant is a multiple of `E`.
The equality of full-rank lattice index with absolute basis determinant is the
elementary integer-lattice index theorem; no analytic estimate is imported.
The independent finite-group oracle directly enumerates the map image.

If even **one** admitted source point is globally primitive, then `g=1`:
every common divisor of all `d_i` divides all its summands. Therefore `E=D`
without pairwise-coprime moduli. This is not the assertion that arbitrary
primitive summands are pairwise coprime. The API's `globally_primitive` flag
means **all supplied points** are primitive; a mixed family can return false
while still having `E=D`. That is conservative metadata, not a failed theorem.

Hadamard applies to positive source columns with Euclidean norm at most their
coordinate sum, hence `|det|<=X^m`. If `E>X^m`, each chosen top minor vanishes.
If the entire set had rational rank m, an independent m-subset would contradict
this. Thus the universal rank conclusion follows, including for an infinite
set of source points at the purely algebraic level. In the actual finite-height
positive-integer domain the source set is already finite.

The sharp negative control is retained: moduli `(2,2,2,2)` and columns
`(2,2,2)`, `(4,2,2)`, `(2,4,2)` have `|det|=E=8`, while `D=16` does not divide
the determinant. Dropping the shared-prime denominator without primitivity fails.

### EXT-03: rank drop does not imply singleton

For `K>=3`, take odd `n>12K^3` divisible by every odd prime at most `K-1`.
The moduli `(n,n+1,2n+1,3n+2)` are pairwise coprime: their pairwise gcds reduce
to 1 or to `gcd(n,2)=1`. The advertised K-1 points satisfy the source equation,
the divisibility constraints, and the height cutoff by direct substitution.
Their first and third coordinates have gcd `gcd(k-1,2n+1)=1`, because every
odd prime dividing `k-1` divides n and `2n+1` is odd. They are thus globally
primitive. The points have a nonzero 2-by-2 minor and all 3-by-3 minors vanish,
so their span has rank exactly two.

Finally `D>6n^4` and `X<=4Kn`, hence `D>X^3` for `n>12K^3`. Choosing n as an
arbitrarily large odd multiple of the finite required prime product works for
every K. This is a genuine unbounded counterfamily, not just a finite example.
The source sample has `9015^3=732651078375`, as recorded in the dossier.

### SMP-01 and SMP-02: uniformity includes the dimension dependence

For positive representatives `rho_i` in `[1,W]`, write
`n=floor(X/W-sum(rho_i)/W)`. For `n>=0`, the exact count is
`product(n+j,j=1..m)/m!`. Each factor differs from `X/W` by at most m and has
absolute value at most `X/W+m`. Telescoping m factors proves the stated bound
`r*m^2*(X/W+m)^(m-1)/m!`. If `n<0`, then `X/W<m`, and the omitted volume alone
satisfies the same bound. Distinct residue rows are disjoint, including sparse
or empty sets; no density lower bound is hidden.

For `X>0` and a nonempty residue set, divide by its positive volume. With
`a=m^2 W/X`, the relative bound is at most `a exp(a)`. Thus `a->0` suffices
uniformly over m, W and residue sets. At `W=1`, the exact ratio is
`product(1-j/N,j=0..m-1)`. If `m=floor(c sqrt(N))`, expanding its logarithm
gives `-m(m-1)/(2N)+O(m^3/N^2) -> -c^2/2`. Therefore the stated phase-scale
counterexample is correct. No claim of necessity for structured residues or
of asymptotic uniformity at all growing dimensions is made.

Exact holdouts enumerate positive compositions before grouping residues, and
include fractional cutoffs, empty sets, dimensions exceeding the height,
singleton sparse classes, and rational relative discrepancies.

### Infinite carrier: local finiteness has an explicit source hypothesis

For positive integer weights on labeled coordinates, finite-support occupation
states below every finite budget are finite iff only finitely many weights lie
below each bound, equivalently `w_j -> infinity`. The forward obstruction is
infinitely many distinct singleton occupations. The reverse proof bounds both
the number of affordable coordinates and every occupation. For weights `w_j=j`,
the partition generating product is coefficientwise meaningful because each
coefficient depends on finitely many factors. No analytic interchange is used.

`weighted_infinite_count` accepts a finite weight list. It calculates that
finite carrier, and **cannot authenticate** that the list contains all affordable
coordinates of a claimed infinite source. Its docstring declares this source
obligation. Repeated weights are distinct labeled modes: three unit-cost modes
give four states at budget one, not two. These distinctions have exact controls.

### Local clock laws: the total is not an independent extra slot

Uniform residues in `F_p^m` have one all-zero tuple, giving primitive proportion
`1-p^-m`. Having at most one zero summand gives
`((p-1)^m+m(p-1)^(m-1))/p^m`, the stated pairwise-summand proportion. For m=1
the latter is 1 (a vacuous pairwise condition); m=2 agrees with primitivity.
For fixed p, the exponential decay of `(1-1/p)^m` dominates the linear factor,
whereas `p^-m->0`.

The total `c=sum(x_i)` must not be appended as an independent slot. For example,
at p=3 the summands `(0,1,1,1)` have exactly one zero, but their total is also
zero. They pass pairwise-summand occupancy and fail pairwise occupancy including
the total. The implementation and manuscript explicitly restrict the formula
to summands and do not make this invalid transport.

## Certification and remaining boundary

Exact integer and Fraction domains reject booleans, floats and fractional
integer moduli; composite “prime” inputs are rejected. Independent permutation
determinants include pivot swaps, singular rows and coefficients of size
`10^40`. These finite checks support the proof audit and preserve useful
regressions, without providing universal software verification.

All accepted mathematics here is **PROVED PAPER**, classical or a new-to-project
organization; execution receipts are **TESTED FINITE**. This audit adds no Lean
authority and no academic originality claim. No source archive was modified.
The missing inequality remains weighted high-divisor incidence: neither a
small cofactor product nor vanishing top exterior minors controls its total
weighted multiplicity. That is a pathway gap, not a contradiction to the
weighted-moment conjecture or evidence that its endpoint is false.
