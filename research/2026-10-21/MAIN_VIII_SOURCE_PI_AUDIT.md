# Main VIII source and polygon integration audit

Date: 2026-10-21. Reviewer lane: `research/viii-source_audit-2026-10-21`.
Reviewed PR #213 head `d3e0ccf671b2ddc2a9e94549db77f60955ee7580` and PR #218
head `8f9444c3984e4b981422d400c4c3ebde7a0a6715` in union
`c82f5e34145661d96e87612d0a8cc633759409b7`, whose main ancestor is
`b5f9591033db2022bda6a2f16a935c06466f9eff`.

**Verdict:** #213's finite moment-Gram improvement and fixed-budget obstruction
survive this audit at their paper-theorem / exact-instance status. #218's
polygon, limit-order and path-space results survive after two precision-boundary
repairs below. Neither signed source positivity nor normality of π is proved.
This is a separate same-model review with independent finite algebra, not an
external referee or a Lean proof. Repository-wide merge gates belong to the
integration coordinator; this dossier records only this lane's checks.

## 1. Two discovered defects and repairs

### Floating underflow at a certified error boundary

Before repair,

```python
orbit_lipschitz_error_bound(2, 1, 1e-200, 1e-200) == 0.0
```

The two finite IEEE inputs represent positive rationals. Their exact product is
positive, so zero is not an upper bound for the advertised product. This is
not just a cosmetic return-type issue: choose a tiny pair of phases at distance
ε and `F(x)=L*d_circle(x,0)`. At horizon one its difference is exactly `L*ε>0`.
NaN and infinity also entered the boundary without a proper domain rejection.

**Repair:** all public polygon/path APIs now require genuine integers for
discrete parameters (rejecting booleans, floats and integral Fractions), and
exact integers or Fractions for continuous rational parameters. Digit symbols
must be genuine integers. The underflow case raises `ValueError`; the exact
`Fraction(1,10**200)` counterpart returns exactly `1/10**400`. This defines an
honest input domain; it does not defend against arbitrary hostile Python code
modifying the running interpreter.

Affected status: POL-03's mathematical inequality was correct, but its executable
certificate was unsafe outside its advertised exact domain. Fixed. The negative
controls include underflow, NaN, infinity, booleans and type-confused discrete
parameters, not merely a duplicate successful example.

### Ideal geometric width is not a finite-precision width

The exact counterexample is

```python
polygon_pi_bracket(steps=1, precision_bits=1)
# lower=2, upper=4, sides=8; actual width=2 > 64/8**2=1
```

This is a valid enclosure of π. The ideal inscribed/circumscribed gap bound does
not automatically bound the larger outward-rounded enclosure. Consequently
“insufficient precision fails closed” must mean failure to establish a valid
positive chord enclosure, not a promise of geometric accuracy at every bit
budget. The source dossier now says this explicitly. Computed transport uses
the **actual returned width**; use of `64/m²` requires an additional exact width
check. The historical probe already made that check at its specified 256-bit
budgets, and replays byte-for-byte unchanged after the repair.

Affected status: POL-01 remains correct as a theorem about ideal polygon
perimeters; POL-03 and POL-07 require the clarified computational error budget.
No archived receipt is rewritten to pretend the repair existed historically.

## 2. Independent reconstruction of the operator claims

Let `B` be a bounded self-adjoint operator on a real or complex Hilbert space
with `B≥κI`, `κ>0`. Let `L:F^m→H` be injective, put `E=ker L*`,
`M=L*B^{-1}L`, and `G=L*L`. Both finite Gram matrices are positive definite.
For `r∈E`, the unique maximizer over `u∈E` of
`2 Re<r,u>−<Bu,u>` is

`u=B^{-1}r−B^{-1}L M^{-1}L*B^{-1}r`.

Indeed `L*u=0`, and `r−Bu` lies in `ran L=E⊥`. Subtracting the value at any
other admissible vector gives the nonnegative squared B-norm of their
difference. Hence the maximum is

`<r,B^{-1}r>−(L*B^{-1}r)* M^{-1}(L*B^{-1}r)`.

For a closed, densely defined form on a closed subspace `E'⊂E` that dominates
`<Bu,u>` on its form domain, the associated positive operator's inverse
quadratic form is at most this maximum. Domain inclusion and form domination
are indispensable. A finite matrix identity alone does not identify the
arithmetic source or establish its form core.

An independent test solves the constrained minimization using a nullspace
basis in five four-dimensional rational examples, with **nonorthogonal**
constraint columns. It matches the rank correction exactly. Replacing the
Gram inverse by its diagonal fails in these examples. This does not reuse the
piecewise-polynomial integration algorithm.

### Why the inverse and paid errors are valid

For `1/2<b<1`, the zero-extension translation `A_b` pairs each edge point with
one point on the opposite edge and vanishes in the middle. Its edge block is
`[[0,1],[1,0]]`. Thus `B_b=κI+w(I−A_b)`, `w≥0`, lies between `κI` and
`(κ+2w)I`; its two-point inverse has diagonal
`(κ+w)/(κ(κ+2w))` and off-diagonal `w/(κ(κ+2w))`. The central inverse is
`1/(κ+w)`. The recorded polynomial integration formula is exactly this inverse.

If `|b−b0|≤δ`, moving the two internal boundaries sweeps length at most `2δ`.
The jump comparison costs at most `4δ||p||∞||h||∞/κ`; away from that set the
shifted argument costs at most `δ||p||∞ β||h'||∞`. This reconstructs the stated
entrywise error. Symmetrized entry bounds give a spectral norm bound by the
largest absolute row sum. Upward grid rounding plus `2/grid` on each diagonal
is a Loewner upper for these symmetric 2×2 matrices. Inverting reverses Loewner
order; no floating eigenvalue sorting enters.

For `R≥0`, `Z=Z0+Δ`, reverse Young gives

`Z*RZ ≥ (1−θ)Z0*RZ0 − (θ^{-1}−1)Δ*RΔ`, `0<θ<1`.

Since `Δ*RΔ` is positive, it is bounded above by its trace times the identity;
entrywise absolute bounds give exactly the recorded penalty. A fresh holdout
uses a weight with negative off-diagonal entries, two θ values, and all 16
signed error corners. Every resulting rational difference is PSD. The separate
true-residual Young budget remains necessary and is not silently removed.

### Fixed-budget ceiling is a genuine method obstruction

The upper operator bound gives `M≥G/(κ+2w)`, so for the orthogonal constraint
basis each complete correction diagonal is at most

`(κ+2w) Σ_j (|Z0_ji|+e_ji)^2/G_jj`.

Adding `(1+η)` times this upper cap to the **fixed ambient lower-certificate
formula** gives the following upper limits on that formula's diagonals:

| Derivative parity | First diagonal ceiling | Second diagonal ceiling |
|---|---:|---:|
| odd | `−3122111819564344893771/250000000000000000000000` | `−12384220161980533810999/1000000000000000000000000` |
| even | `−6871190365592769978959/1000000000000000000000000` | `−6680071650059200874923/1000000000000000000000000` |

All four are strictly negative. Thus no improvement solely to these two-moment
inverse evaluations can make this particular fixed-budget lower certificate
PSD. These are **not upper bounds on the actual source Schur complement**.
Changing trials, the ambient comparison, or the joint residual budget leaves
this obstruction's hypotheses. Negative lower certificates do not prove a
negative source. The exact and independent Simpson improvements themselves
remain positive definite in both parity blocks.

## 3. Source attestation and its boundary

The actual source Git blob remains
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, introduced by
`b0cef75f47de29b1326b351df35b9e5423f2ed4f`. This project source is not one of the
72 imported archival files; these are different provenance assertions.

| Historical artifact | SHA-256 |
|---|---|
| CLOUD_EXACT_MOMENT_SOURCE_J10.json | `321d80b0dc38aeddf52f6c0b0c398370b3b18fae285c6fbd1751acc999bc28f9` |
| CLOUD_EXACT_MOMENT_SOURCE_HOLDOUT_J6.json | `6fab39552a565db0c3b9ba04a3830c5132e0c071fe50ea19712f51331009c637` |
| PI_POLYGON_NORMALITY_FINITE_RECEIPT.json | `7b0a99e7b4032a94d778104098965d23a3070b31d712da02e73cd22a0afe86ed` |

All seven source-receipt implementation hashes match the reviewed union. The
operator replay reconstructs all four ceilings from the outward rational
parents, not from printed decimal approximations. No frozen original changed.

I re-opened Suzuki's primary [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3)
on 2026-10-21: equation (1.3) specifies the signed arithmetic screw function;
Theorem 1.1 identifies a Friedrichs extension, and Corollary 1.2 gives the
form-core Rayleigh infimum. These results do not establish SUCC's numerical
all-high bound or S4 sign. The paper's differential `B_a` is not the bounded
comparison `B_b` in the inverse theorem. The source module keeps genuine
von-Mangoldt prime-power weights, Gamma quarter shift, completed pole/contact
and half-density. Its construction does not take nontrivial zero locations as
inputs. The project-specific source realization and high-space comparison
remain paper-level dependencies, not newly formalized facts of this audit.

The historical J=10/M=96 source calculation was **not rerun** here; its exact
artifact and implementation hashes were checked, together with a fresh
60-case SymPy holdout and the source receipt arithmetic. M denotes a Taylor
truncation depth, not a spatial discretization. The independent Simpson grid
has 32 subintervals per polynomial piece; J=6/M=72 is the separately recorded
source-action holdout. Their evidence must not be described as two independent
arithmetical sources.

## 4. Independent reconstruction of the π transport claims

For the unit circle, a half-angle identity gives
`x_4=2`, `x_(2m)=2−sqrt(4−x_m)`, where `x_m=4 sin²(π/m)`.
Inscribed and tangent polygons give
`(m/2)sqrt(x_m)<π<m sqrt(x_m/(4−x_m))`.
The maps used in interval propagation are monotone, so the opposed square-root
endpoints enclose the next chord. Intersecting valid brackets preserves validity.
Dyadic square roots are certified by exact integer-square comparisons.
For ideal endpoints, `sin θ≤θ`, `1−cos θ≤θ²/2`, and `cos θ≥1/sqrt(2)` give
the advertised gap. Rounding is subject to section 1's correction.

The implementation permits at most 100 doublings and 4096 bits. These are
finite resource bounds, not an implementation of an infinite limiting process.
The paper's asymptotic assertions concern unrestricted mathematical polygons.
A new low-precision holdout checks every surviving bracket in a grid of seven
bit budgets and twelve depths against an independent exact Machin interval,
and verifies every returned decimal prefix against that interval. It does not
feed Machin data into the polygon algorithm.

Two balanced maps of finite grids remain different:
`P(j/(mb))=floor(j/b)/m`, versus `T_b(j/(mb))=(j mod m)/m`.
For `x=1/7,m=4,b=2`, the coarse prefix is 0 and the finer prefix is 1/8;
its image under T2 is 1/4, not 0. Balanced fibers therefore do not prove
commutation with the prescribed source path.

The prefix inverse limit is a product of a finite initial label and a digit
sequence. Nested closed cells determine a continuous circle evaluation map,
with dual expansions at grid endpoints (and identified real endpoints 0,1).
It is a quotient map, not a homeomorphism from the totally disconnected path
space to the connected circle. Fair cylinder masses push forward to Haar,
because the level-n cells have lengths `1/(m0*b^n)` and their diameters tend to
zero. This law says nothing about typicality of every single path. The all-zero
path and the irrational sparse-square digit path remain valid countermodels.

For `q_m(x)=floor(b^m x)/b^m`, each finite orbit is eventually zero. At fixed N,
continuity of T_b on the circle transports orbit averages as m tends to infinity.
The opposite iterated limits disagree for an independently known normal x.
No step assumes normality of π. The all-N Lipschitz estimate follows by summing
`Lip(F)*b^j*ε`; Fourier characters have constant `2π|h|<8|h|`. A finite prefix
protects only its predeclared block horizon. Discontinuous digit tests need bin
separation, not just the Lipschitz argument.

POL-07 is honestly conditional: for each fixed b and each nonzero integer h,
source-midpoint Fourier decay plus a vanishing **actual** width budget imply
normality by Weyl. Haar on grid paths, balanced finite clocks, and computability
of π establish neither Fourier cancellation nor orbit typicality. The next
verdict-changing mathematical input remains a π-specific cancellation theorem.

## 5. Validation and merge recommendation

Run from the repository root:

```sh
python scripts/viii_source_pi_audit.py --output /tmp/main-viii-source-pi.json
```

The tracked [validation receipt](MAIN_VIII_SOURCE_PI_VALIDATION.json) records:

- 17 existing operator tests, 11 existing π tests, and 6 new hostile tests pass;
- 60 separately implemented shifted-Gram cases pass;
- new nullspace-coordinate and signed-error-corner checks pass exactly;
- all source implementation hashes and the source Git blob match;
- the π finite receipt regenerates byte-for-byte after the domain repair;
- no full-suite or Lean success is claimed by this lane.

Recommend integrating #213 unchanged, and #218 with these repairs. Preserve
PROVED PAPER / TESTED MODEL labels; no formal-kernel promotion. Keep historical
reports labeled with their historical heads. No new result here proves RH,
integer abc, Goldbach or π normality. The genuinely new audit counterexamples
are the floating underflow certificate and finite-precision gap conflation.
Any later Fourier oracle belongs in a separate research commit and draft PR.
