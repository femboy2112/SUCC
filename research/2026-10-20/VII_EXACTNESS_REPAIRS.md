# Academic Main VII: exactness and interface repairs

Status: **PROVED LOCAL** for the elementary identities and counterexamples below;
**FINITE CHECK** for the implementation regression corpus. No formal-kernel
verification is claimed. This dossier concerns finite rational arithmetic,
certified singular-series constants and residue counting, not RH or Goldbach.

The repair branch starts at combined, unvalidated integration candidate
`176d7f0fff8e9c7fae290e545376bac4cefe05ac`. It contains the actual PR #200–#209
histories. Its tests are not receipts for main or for subsequent integration
commits. None of the changed modules is an imported original listed in
`provenance/IMPORT_MANIFEST.json`; frozen source bytes are unchanged.

## Reproductions and corrected obligations

| Interface | Exact old result at the base | Required result and repair |
|---|---|---|
| `min_eigenvalue_exact([[H+2,1],[1,H+2]])`, `H=10^30` | `H+3` | `H+1`; exact rational-polynomial root isolation |
| `singular_series_enclosure(2,Fraction(5,2))` | `[1/3,1]` | Reject invalid cutoff before constructing a certified interval |
| `bblt_anatomy(256,4)` | whole tail `256`, described as BBLT remainder | Preserve exact identity; rename canonical routine and withdraw attribution |
| `singular_series_via_transport(2,2)` | `3/2` | `2`, equal to the finite product through prime 2 |

The spectral counterexample is decisive without evaluating roots numerically.
The vectors `(1,-1)` and `(1,1)` have eigenvalues `H+1` and `H+3`. Subtracting
the old claimed lower bound gives quadratic value `-4` on `(1,-1)`.

For the malformed-cutoff enclosure, an independent genuine lower bound for
`S(2)` is `135/128 > 1`: include primes 2,3,5 and multiply their product by the
proved tail lower factor `1-1/(5-1)`. Thus the old interval is genuinely false.

The additional cutoff-2 transport defect arose from `max(P,3)`, which introduced
prime 3 without permission. The old bracket happened to remain an enclosure in
this example, but the advertised exact finite-product identity was false. The
repaired transport computes precisely the primes through the requested cutoff.

## Exact spectral domain

`min_eigenvalue_exact` accepts nonempty square matrices over the rationals and
returns the minimum eigenvalue of their symmetric part. The characteristic
polynomial has rational coefficients and all roots real. `Poly.real_roots`
isolates and orders roots exactly, with multiplicity; `radicals=False` returns
`CRootOf` objects when necessary. Its first root is the minimum. A diagonal
matrix takes the exact rational-comparison shortcut.

Empty, nonsquare, floating, free-symbol, complex and nonrational algebraic inputs
are explicitly rejected. This narrows an undocumented extension beyond the
original rational-matrix contract rather than guessing an ordering. The Python
and SymPy implementation is a trusted computation dependency, not a Lean proof.
`certified_pd_margin` still uses an approximate candidate only after an exact
positive-definite shifted-matrix check; it remains a separate lower-bound route.

The new controls include gaps `10^-80` around heights `10^30` and `10^100`, exact
irrational roots, domain rejection and independently checked shifted matrices.

## Singular-series domains and parity

All four certified/finite singular-series paths now require `type(P) is int`
and `P>=2`, before the odd-`N` zero shortcut. The twin-prime constant interface
retains `P>=3`. Booleans, floats and all `Fraction` instances, including integral
ones, are rejected. No implicit flooring or coercion is advertised. `N` remains
a positive built-in integer. Existing largest-prime-divisor requirements remain
on the even transport path; the independent cloud harmonic implementation has
its own rigorously justified more general tail budget.

The correction factor is the product of `(p-1)/(p-2)` over odd primes dividing
even `N`. Every factor exceeds one, so `S(N)=2*C2` exactly for positive powers
of two; along `N=2q` with odd primes `q` it also tends to that constant. Direct
and transport finite products and enclosures now agree at `P=2` and above.

## Attribution: ordinary layers versus BBLT regrouping

Primary source: Bernert, Browning, Lichtman and Teräväinen,
[arXiv:2410.12234v2, Lemma 2.2](https://arxiv.org/html/2410.12234v2#S2.L2),
inspected 2026-10-20. For positive `epsilon`, the proof takes
`d=6*ceil(epsilon^-2)`, `k=ceil(epsilon^-1)` and moves high exponents into layer
`k`. Its remainder uses exponent `j-k*floor(j/k)`, rather than `j`, for `j>d`.
This yields the small remainder and approximate radical relations. The paper
does not assert the same bounds for an unmodified whole high-exponent tail.

`truncate_exponent_layers` is now the canonical ordinary identity
`n=n0*prod_{j<=d}m_j^j`, where `n0=prod_{j>d}m_j^j`. The old function name remains
a documented compatibility alias and grants no BBLT bounds. The counterexample
`n=256,d=4` refutes the old attribution, not the paper. For any fixed depth `d`,
`n=p^(d+1)` similarly makes this ordinary tail equal to all of `n`.

## CRT reconciliation

For integer `X>=0`, integer `W>=1` and an explicit set of canonical residues,
the canonical `error_bound` now delegates to the independent cloud A1 enclosure
and returns exactly `|R|*(3X/(2W)+1)`. The old bound `5|R|*(X/W+1)` and its
historical dominance tests are preserved as `legacy_error_bound` and
`legacy_growth_regime`. Their existing tests were redirected to those explicit
interfaces, not removed or weakened.

For nonempty `R`, sharp-bound dominance is equivalent to
`X^2>3WX+2W^2`, with least integer threshold
`(3W+isqrt(17W^2))//2+1`. In particular `4W` suffices and `3W` does not. An empty
set has both terms zero and never has strict dominance. The relative bound is
`3W/X+2(W/X)^2`; uniform vanishing requires `W=o(X)` by this method. Dominance
at a fixed ratio is not a relative asymptotic. The separate lattice-cell proof,
floor formula and moving-modulus counterexamples remain in
`CLOUD_CRT_ASCENT.md`. No arbitrary moving-modulus theorem is asserted.

## Independent certificate cross-check and limits

Twenty exact 3-by-3 matrices are generated as `U^T D U`, with `det(U)=1`, heights
up to `10^30+7`, rational eigen-direction weights as small as `10^-80`, positive,
singular and indefinite diagonal forms, and coordinate permutations. A further
zero-diagonal/nonzero-coupling 2-by-2 matrix exercises the division-free branch.
Known inertia supplies an external algebraic oracle for each case.

The Claude congruence method and cloud weighted-Gram/negative-witness method
agree in every case. Each Gram identity is recomputed entrywise, and each
negative vector is evaluated on the exact original matrix. These are separate
implementations of related classical elimination mathematics, not independent
formal proof kernels. The finite corpus does not establish universal absence of
bugs, source identification, infinite positivity or authority of an unrelated
proposition.

## Reproduction and next probe

Run with supported Python and the repository's pinned numerical dependencies:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -m unittest discover -s tests -p test_vii_exactness.py -v
```

Focused validation also includes the complete existing test modules for
quantitative rigidity, Goldbach circles, abc decomposition and residue-box
counting. The receipt records exact source hashes and outcomes. Full integrated
suite, provenance and formal authority gates belong to the coordinator and must
be rerun on the actual candidate commit. No mainline merge is implied here.

Next decisive implementation probe: independently isolate the characteristic
roots of higher-degree rational symmetric matrices and compare certificates
against a second exact arithmetic system. This is a verification opportunity,
not a mathematical obligation blocking the elementary counterexample repairs.

## Follow-up: current abc frontier and an exact threshold diagnostic

The preceding `VII_EXACTNESS_RECEIPT.json` records the content tested for commit
`6dd1bede6cef06cfc900f60fdde94ad7098dfd19`. The follow-up receipt
`VII_ABC_STATUS_RECEIPT.json` binds the subsequent module and test changes;
the earlier receipt is preserved as history rather than rewritten.

Current `abc_decomposition` status metadata now references reviewed
**CLOUD-ABC-01/05**, which prove the global quadratic bound and mean value for
`0<=t<2/3`. These are **PROVED LOCAL** paper proofs, not formal-kernel receipts.
The diagonal method still has its `t<1/2` ceiling. Its failure, and the failure
of the particular unrestricted residue-majorant error sum, remain established.
The broader assertion that no elementary positive-counting method can reach
any exponent at or above `1/2` is **REFUTED** by primitive slope separation.
The endpoint `2/3`, the range `2/3<=t<1`, and integer abc remain open. The
global theorems do not imply an unproved pointwise asymptotic for each inner
correlation. No BBLT estimate is silently imported for this different object.

An additional exact diagnostic defect was found in ABC-COR-02:
`bounded_powerful_part_bound(26,4,0)` reported `dominance_threshold_X=26`.
Here `G=5/4`, `A=2`, `B=5`, so the actual defining inequality is

\[
\frac{25}{32}X^2>20X+125.
\]

At `X=26`, the two sides are `4225/8` and `645`; dominance is false. The least
integer satisfying the inequality is `31`. The original upper bound and its
separately computed `informative` flag were sound; the threshold diagnostic and
the displayed sufficient condition incorrectly omitted the positive `B` term.

For the actual rational upper endpoints returned by the routine, set
`alpha=G_hi^2/2`, `beta=5*A_hi^2`, `gamma=5*B_hi^2`. Clear denominators to
positive integers `A,B,C`. Since the divisor 1 occurs, `A>0`. The inequality
`A X^2-B X-C>0`, for `X>=0`, holds exactly beyond its positive root. Its least
integer solution is

\[
1+\left\lfloor\frac{B+\lfloor\sqrt{B^2+4AC}\rfloor}{2A}\right\rfloor.
\]

Replacing the square root by its integer floor inside the outer floor is exact:
the omitted fraction is less than one and the numerator and denominator are
integers. Adding one correctly handles equality when the root is integral.
No approximate comparison or asymptotic simplification enters the threshold.
The regression checks both the threshold and its immediate predecessor for
five parameter families, including a nonintegral moment exponent. The complete
abc module run passes 33 tests; full integrated validation remains the
coordinator's responsibility.
