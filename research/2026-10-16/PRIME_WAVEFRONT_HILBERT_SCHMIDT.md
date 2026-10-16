# Prime wavefront geometry and the derivative/projection boundary

Operation Arithmetic Resonance, Swarm A, 2026-10-16. Worktree base
`24d0f18a103fb2add32ee817fdfefb4ff401ed27`, branch initially
`research/arithmetic-wavefront-spectral-response-2026-10-16`.
**Full signed Suzuki four-low sign OPEN. RH NOT PROVED.**

This lane supplies reusable exact rational hinge responses, matrix entries,
continuum derivative Grams, projection-order audits, and distributional boundary
terms. It also encloses actual prime-only source matrix entries and proves one
source-specific derivative projection contraction for the isolated prime-2
operator. No such contraction is inferred for the completed signed source.

## Authority, provenance and scope

Read before editing: `AGENTS.md`, `docs/METHOD.md`, the import manifest,
`OBSERVER_SCHUR_ROUND_II.md`, its handoff and claim supplement,
`OBSERVER_SCHUR_SOURCE.md` (in particular the quotient response and source
controls), `COMPACT_SOURCE_GALERKIN.md` (CG-04 and CG-09), and the Round II
hostile audit. Inspected the original `source_weil_hierarchy`, existing
`suzuki_legendre_source`, prime boundary, Hilbert wavefront and hinge integral
modules. The original source commit was inspected with `git ls-tree`:

```
dc6b7e3adbfb67c2913c145a4efb95fe3d50b1bc
observational_succ/source_weil_hierarchy.py
Git blob 0cc8510b71d178fc79e8d410a86d8b6014cf9178
```

The 72-entry founding import manifest is a different lineage; it does not
authenticate the later PR85 source by itself. The probe records SHA256 and
Git-blob hashes of its actual dependencies before and after execution.
No archive, source file, shared index, or other worker's file is edited.
This worker performs no commit, staging, push, Lean compilation, or full suite.

The source convention agrees with [Suzuki's primary paper, (1.3) and §8](https://arxiv.org/html/2606.09096v3):
the prime-power hinge has threshold `b=log(n)`, weight `c=log(p)/sqrt(n)`
for `n=p^k`. All source inputs come from the pinned arithmetic tape. No
nontrivial-zero coordinates enter any construction. This report makes no
academic originality claim for classical distribution and HS identities.

All universal analytic statements below are **CONDITIONAL PAPER PROOF**:
conditional on the declared kernel, carrier, and regularity hypotheses, with
proofs supplied here, not a Lean proof. Executed rational instances and exact
symbolic integration are separately **EXACT COMPUTATION**. Source interval
results are **EXACT OUTWARD RATIONAL ENCLOSURE**, conditional on the pinned
source primitive correctness and the stated analytic transfer. Decimal
displays are not proof authority. No floating experiment is used to certify
a sign or source identity.

## PW-01: exact raw Hilbert–Schmidt geometry

Let `a>0`, `b>=0`, `c` real, `I=(-a,a)`, `L=2a`, and

```
h_b(r) = c (|r|-b)_+,
T_b u(x) = integral_I h_b(x-y) u(y) dy,
delta = max(L-b,0).
```

Then, on real or complex L2(I),

```
||T_b||HS² = c² delta⁴/6,
||D T_b||HS² = c² delta².
```

Proof: pairs with separation `r>=0` have density `2(L-r) dr` on the
square. Thus the first square is `2c² int_b^L (L-r)(r-b)² dr` when
`b<L`, equal to the claimed expression. The derivative kernel is
`c sign(r) 1_{|r|>b}` almost everywhere; the analogous integral gives
`2c² int_b^L (L-r)dr=c² delta²`. For `b>=L` both operators vanish.
This holds on either side of `b=a`, including overlapping boundary strips.

For two real weighted hinges `(b,c)` and `(d,e)` the mixed HS products are

```
<T_b,T_d>HS = 2ce int_max(b,d)^L (L-r)(r-b)(r-d) dr,
<D T_b,D T_d>HS = ce max(L-max(b,d),0)²,
```

with the first integral defined as zero if its lower limit is at least L.
Summing **all** mixed products gives the exact norm of a signed hinge sum;
summing only individual squared norms is generally false. Positive kernel
values and nonnegative HS norms do not imply a positive integral operator.

These are raw-kernel equalities. Orthogonal compression contracts the HS norm
of T itself. It contracts the derivative norm only when the projection is
applied to **DT after differentiation**, or when an additional proof is given.

## PW-02: weak derivative identities and the carrier

Extend u by zero to the real line, denoting the extension by u0. In distributions
on the line,

```
h_b' = c sign(r) 1_{|r|>b},
h_b'' = c(delta_b + delta_-b).
```

At b=0 the two atoms coincide and their weights add to 2c. For u in L2(I),
on the **open** interval I,

```
(T_b u)'(x) = c int_-a^(x-b) u(y)dy - c int_(x+b)^a u(y)dy,
(T_b u)''(x) = c [u0(x-b)+u0(x+b)].
```

An integral above is zero if the indicated translated endpoint lies beyond
the relevant endpoint of I. These identities follow by differentiating the
locally integrable kernel distribution and applying Fubini against compactly
supported smooth tests. The first derivative is an HS integral operator;
the second is a bounded sum of restricted shifts, norm at most `2|c|`.
In particular `T_b:L2(I)->H²(I)` is bounded. The second derivative is not
being represented by an L2 delta kernel or assigned an HS norm.

For `a<=b<2a`, the two translated strips are disjoint and D²T_b has norm
`|c|` for nonzero c. At `b=2a` it vanishes. This preserves the inherited
onset distinction: small raw HS norms do not give uniform control of the
twice differentiated operator at activation.

For `v in H0¹(I)`, integrating by parts twice gives

```
<T_b (i v'), i v'> = -2c Re int_-a^(a-b) v(x+b) conjugate(v(x)) dx
```

when b<L, and zero otherwise. Zero boundary traces are necessary for this
display. The exact test `v(x)=1/4-x²`, `a=1/2`, `b=2/3`, `c=1` has a
strictly negative value, retained in the tests. No Gram positivity is
substituted for positivity of the signed prime kernel.

## PW-03: Fourier law, its ambiguity, and window boundaries

Use `hat f(xi)=int_R f(r) exp(-i xi r)dr`; in particular
`hat 1=2pi delta_0` and `hat(delta_b)=exp(-i b xi)`.
The isolated hinge is tempered, but is not integrable. Its full-line transform
is a distribution. The immediately determined law is

```
-xi² hat h_b = 2c cos(b xi).
```

Dividing by xi² as an ordinary function loses information at frequency zero.
With `Pf(1/xi²)=-D(PV(1/xi))`, the complete answer is

```
hat h_b = -2c cos(b xi) Pf(1/xi²) - 2pi c b delta_0.
```

Proof: write `h_b=c|r|-cb+c(b-|r|)_+`. Abel regularization of |r|
has transform `2(epsilon²-xi²)/(epsilon²+xi²)²`, which tends to
`-2 Pf(1/xi²)`. The compact tent has transform
`2(1-cos(b xi))/xi²`, with its removable value at zero. Multiplication
of the finite part by cos gives the displayed formula. The second-derivative
law alone allows adding `A delta_0+B delta_0'`; evenness excludes the latter,
and the actual hinge normalization fixes the former. This is an isolated
kernel law, not a claim that the complete growing source admits the same
unqualified full-line Fourier transform.

For a hard finite window `F_L(r)=1_{[-L,L]} h_b(r)`, `0<=b<L`,

```
hat F_L(xi) = 2c[(L-b) sin(L xi)/xi + (cos(L xi)-cos(b xi))/xi²], xi!=0,
hat F_L(0) = c(L-b)²,

D² F_L = c(delta_b+delta_-b-delta_L-delta_-L)
         +c(L-b)(delta'_-L-delta'_L),

-xi² hat F_L = 2c cos(b xi)-2c cos(L xi)-2c(L-b)xi sin(L xi).
```

The expression is zero for b>=L. In particular, dropping the window endpoint
atoms fails already at xi=0: the left side is zero, whereas the retained
internal atoms have mass 2c. SymPy independently integrates the windowed
hinge and verifies both the boundary law and the removable zero-frequency
limit. Rational polynomial pairings independently check delta-prime signs.

More generally, for `F in H²(-a,a)`, extending the output by zero gives

```
D²(F 1_I) = 1_I F'' + F'(-a)delta_-a - F'(a)delta_a
            + F(-a)delta'_-a - F(a)delta'_a.
```

Its Fourier law contains these four endpoint terms. Input extension by zero
in PW-02 does **not** authorize deleting the output terms. For a piecewise
polynomial with internal jumps, add `[F']_s delta_s+[F]_s delta'_s` at
each knot. The implementation returns these exact atoms; its H1 weak
derivative routine refuses jumps rather than silently discarding them.

## PW-04: projection order and exact projected HS operations

For any finite smooth orthogonal projection P, `Q=I-P`,

```
D(QF) = DF - sum_i <F,e_i>/||e_i||² e_i',
Q(DF) = DF - sum_i <DF,e_i>/||e_i||² e_i.
```

These differ. In the rational hinge test `a=1/2, b=2/3, c=1, u(x)=x`,
with P onto Legendre modes 1 and 2,

```
||D Q T u - Q D T u||² = 4363/1968300 > 0.
```

Round II's quotient map is `Pi_M D G`, with
`M=span(P0,P1,P2,P3)^perp`, rather than `D Pi_M G`. The API keeps
`output_modes` and `derivative_modes` separate, in exactly that order.
For Q acting **after** differentiation, `||Q DT Q||HS<=||DT||HS` follows
from bounded orthogonal contraction. There is no general corresponding
theorem for `||D Q T Q||HS`.

The independent coordinate auditor owns the general rank-one counterexample
reported during this operation: on I=(-1/2,1/2), `f=P6-(1/2)P4`,
`G=f tensor f`, Q removing modes 1..4, the squared norms are `147/26`
and `84/13`, ratio `8/7`. This report records that externally supplied
counterexample without claiming an independent replay or taking ownership
of its proof. The hinge counterexample above is this lane's exact replay.

For reusable evaluation of the actual hinge compression, let `e_i=P_i(x/a)`,
`n_i=||e_i||²=2a/(2i+1)`, `r_i=T e_i`, `s_i=Q r_i`, and `R=DT`.
The even hinge gives `R*=-R`. Then

```
N = ||R Q||HS² = ||R||HS² - sum_i ||r_i'||²/n_i,
||Q R Q||HS² = N - sum_i ||Q r_i'||²/n_i,
C = <R Q, DP T Q>HS = -sum_i <s_i, D T e_i'>/n_i,
E = ||DP T Q||HS² = sum_ij <e_i',e_j'><s_i,s_j>/(n_i n_j),
||D Q T Q||HS² = N - 2C + E.
```

Proof: `DP T Q` has kernel `sum e_i'(x)s_i(y)/n_i`. Orthogonal input
and output Pythagoras give the first two identities. The adjoint identity
gives C; expand the finite-rank kernel square for E. Every integral is an
exact piecewise-polynomial inner product for rational hinges, including
signed sums. There is no Cauchy–Schwarz shortcut asserting contraction.
An independent direct two-variable symbolic integration checks the last
identity for a genuine nonzero rational threshold with modes 0,1,2.

Even the hinge can amplify the already input-projected derivative:
at a=1/2, b=0, c=1, removing modes 0..4 gives

```
||DTQ||HS² = 10/99,
||DQTQ||HS² = 4846/42471 > 10/99,
||QDTQ||HS² = 1/11.
```

Thus the different intermediate contraction assertions must remain separate.

## PW-05: a certified contraction for the actual isolated prime 2

Let a=1/2, `T=T_log2` with the true weight `log2/sqrt2`,
`G2=P0_perp T P0_perp` on H=L2_0(I), and let Q on H remove modes 1..4.
The exact enclosure computation proves

```
||D Q G2 Q||HS² < (1/5) ||D G2||HS².
```

This is **prime-only**, not an application of a general projection theorem.
The result is established by explicit calculation and a source perturbation
bound, as follows. Put b0=693147/1000000, enclose the **actual** b=log2,
and let eta=max(|b_lo-b0|,|b_hi-b0|). Use weight 1 until the final step.
For `E=T_b-T_b0`,

```
||DE||HS² <= 2 L eta,       ||E||HS² <= L² eta².
```

The first bound measures the exact strip symmetric difference between two
step kernels; the second follows from the hinge's pointwise 1-Lipschitz
dependence on threshold. For P onto modes 0..4 and R=1-P,

```
||DP||op² <= S = sum_(n=0)^4 n(n+1)(2n+1)/(2a²),
||D R E R||HS² <= 4 L eta+2 S L² eta² = B.
```

The last step uses `D R E R=DE R-DP E R`, orthogonal input contraction,
and the two-vector squared-norm bound. Young's inequality with epsilon=1/100
now gives

```
||D R T_b R||HS² <= (1+epsilon)||D R T_b0 R||HS²+(1+1/epsilon)B.
```

The reference term is computed exactly by PW-04. Since b>a, the derivative
of T_b 1 consists of disjoint linear strips, with norm square `2 delta³/3`.
Consequently the mean-zero reference denominator is exactly

```
||D G2||HS² = c²[delta² - 2delta³/(3L)],  delta=L-log2.
```

The source interval arithmetic encloses this denominator and multiplies the
numerator bound by the true c². Exact rational comparison, not the decimal
ratio, proves the strict 1/5 bound. Decimal displays of the resulting bounds:
denominator approximately 0.017992185613872284, numerator upper approximately
0.002970927707245402, ratio upper approximately 0.16512322466008605.
All endpoints and the reference error are retained in the receipt.

The rational reference is **not** substituted for the source kernel. This
transfer includes its entire threshold error. No Gamma, poles, contact,
signed cross-channel derivative Gram, or actual source response-range
property follows from this isolated result. Triangle inequalities cannot
silently turn it into a contraction for a signed sum with cancellations.

## Implementation, independent controls and reproducibility

Owned files:

* `observational_succ/prime_wavefront_geometry.py`
* `tests/test_prime_wavefront_geometry.py`
* `scripts/prime_wavefront_geometry_probe.py`
* this dossier
* `research/2026-10-16/arithmetic_resonance_receipts/wavefront*`

The module reuses polynomial addition, multiplication, differentiation,
integration, Legendre generation, and source interval primitives from
`suzuki_legendre_source`. It does not duplicate the existing source-correlation
kernel for prime matrix entries. Rational response integration extends that
kernel with arbitrary input polynomials and full piecewise output functions.
Basis coefficients are increasing powers; matrices use unnormalized real
Legendre form coordinates. Negative coefficients and cross terms are retained.

For each oriented triangle, the independent rational oracle substitutes
`x=-a+b+s+t, y=-a+s`, with `s,t>=0`, `s+t<=delta`, and uses

```
integral s^i t^j ds dt = i! j! delta^(i+j+2)/(i+j+2)!.
```

This checks HS integrals and matrix entries without calling the production
response primitives. The derivative Gram oracle separately integrates input
monomials directly, computes projection coefficients with this triangle route,
and integrates each polynomial product using exact rational Lagrange weights.
Its degree bound is explicit; it is exact quadrature, not a floating estimate.
SymPy supplies an additional independent algebra implementation for the
Fourier window formula and the projected two-variable derivative kernel.
These are distinct calculation paths by one worker sharing the arithmetic
source; no blind-reasoner or independent source lineage is claimed.

Controls cover b=0, b=a, b=2a, inactive and overlapping strips, signed sums,
weak derivatives with boundary traces, jump rejection, parity, cross terms,
projection order, and input type errors. The source validator checks the
entire bounded tape even when no prime is locally visible. Fake6, missing2,
duplicate2, wrong half-density, and wrong logarithmic clock are rejected.
At a=1/2 fake6 is outside the separation window: rejecting it relies on the
source law, not a fabricated local kernel difference. At a=1, prime power 4
is checked with clock log4 but numerator log2, and the active list is
2,3,4,5,7. Full source completion is explicitly false in prime-only receipts.

Run from the worktree:

```sh
python -B -m unittest tests.test_prime_wavefront_geometry -v
python -B scripts/prime_wavefront_geometry_probe.py --output research/2026-10-16/arithmetic_resonance_receipts/wavefront-final.json
python -B scripts/prime_wavefront_geometry_probe.py --skip-tests
```

Without `--output`, the probe writes only JSON to stdout and suppresses
bytecode writes. With an explicit path it records top-level schema, status,
evidence, source pins, claim statuses, command exit, and test output. Tests
are serial and bounded; the principal owns full suites on both interpreters.
SymPy tests skip if that optional dependency is unavailable, and the exact
unittest output records that limitation. The executed local environment had
SymPy available; no installation or additional dependency was made.

`wavefront-initial-failure.json` preserves the first 23-test run: one hand-entered
expected projected-HS fraction was wrong. The independent two-variable
symbolic integration passed in that same run. The corrected expected value
is `44211169/1953045675`; no production formula or tolerance was changed.
This failed run is not counted as a pass.

## Claim ledger and next falsifiers

| ID | Claim | Status | Boundary / next falsifier |
|---|---|---|---|
| PW-01 | Raw hinge and first derivative HS identities, mixed pairings | CONDITIONAL PAPER PROOF; exact rational instances | Raw isolated kernels; test new threshold/weight regimes |
| PW-02 | H2 response and shifted weak second derivative | CONDITIONAL PAPER PROOF; independent exact instances | Output zero extension requires endpoint terms |
| PW-03 | Distribution Fourier law and hard-window correction | CONDITIONAL PAPER PROOF; exact symbolic and rational checks | No ordinary full-line hinge integral, no full-source temperedness claim |
| PW-04 | Correct order of projections and exact compressed derivative HS | CONDITIONAL PAPER PROOF; exact matrix/kernel controls | Generic derivative-after-output contraction REFUTED |
| PW-05 | Squared derivative-HS ratio <1/5 for true prime2, a=1/2, mean-zero, modes1..4 | EXACT SOURCE ENCLOSURE plus paper perturbation bound | Prime-only; full signed cross-channel transfer OPEN |
| PW-RATIONAL | General rational matrix and continuum derivative Grams | EXACT COMPUTATION | No transcendental threshold replaced by a rational |
| PW-SOURCE | Prime tape, clocks and half-density authenticated against pinned adapter | EXACT SOURCE CONTRACT / ENCLOSURE | Source primitive correctness inherited; not full completion |
| PW-OPEN | Full source derivative Gram, range-closure target and four-low sign | OPEN | Requires genuine Gamma/contact/poles and cross terms; retain CG-09 tail |

Epistemic audit: direct contact κ is with the immutable source bytes and exact
integrals. φ concerns the stated hinge identities under these tests; it is
separate from σ, the arithmetic source map. The fake6 control demonstrates
their separation. ρ is one worker's mathematical and implementation lineage,
not an independent consensus. The next decisive work is a fully enclosed
signed source derivative Gram with genuine cross terms, followed by the
actual quotient-range question. The isolated contraction cannot discharge
either obligation.
