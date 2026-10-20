# Exact moment Gram inversion for the original signed source

**Status:** PROVED LOCAL (paper theorem), with exact rational executable instances.
Not Lean-formalized. The finite constrained-inverse identity is classical;
its source-specific, uncertainty-controlled implementation is new to this
project. No claim of academic novelty is made. The authentic signed S₄ sign
and RH remain OPEN.

The earlier cloud certificate replaced the inverse of a two-dimensional moment
Gram matrix by a diagonal lower bound. Here the full Gram matrix is integrated
and inverted exactly, with the true shift b=log 2 enclosed. The improvement is
additive to the earlier certified bound and pays the same original-source
action errors. An independent certified Simpson discretization checks the
finite Gram without using its polynomial antiderivative.

## 1. Constrained inverse, including the form domain

Let H be a real or complex Hilbert space, let B be bounded self-adjoint with
B≥κI, κ>0, and let L:𝔽^m→H be injective. Put E=ker L*, G=L*L, and
M=L*B⁻¹L. Both G and M are positive definite finite matrices. For r∈E,

\[
 \sup_{u\in E}\{2\Re\langle r,u\rangle-\langle Bu,u\rangle\}
 =\langle r,B^{-1}r\rangle-z^*M^{-1}z,
 \qquad z=L^*B^{-1}r.                                      \tag{1}
\]

Proof: the maximizer is
u=B⁻¹r−B⁻¹L M⁻¹L*B⁻¹r. It lies in E, and r−Bu belongs to ran L=E⊥.
Subtracting its value from that at any other u∈E leaves the nonnegative
B-energy of their difference. This proves (1), including attainment. The
associated nonnegative constrained inverse is bounded above by B⁻¹≤κ⁻¹I.

More generally, let d be a densely defined closed form on a closed subspace
E′⊂E, with d[u]≥⟨Bu,u⟩ on its form domain. Its positive associated operator D
has a bounded inverse, and its inverse energy for r∈E′ is at most (1), because
the variational supremum has a smaller admissible domain and a larger energy.
This statement does not require D to be bounded. Identifying d with a separately
constructed arithmetic source still requires the source/form-core bridge.

Since M≤κ⁻¹G, the old bound was M⁻¹≥κG⁻¹. Suppose a rigorously known matrix U
satisfies M≤U and define

\[
 R=U^{-1}-\kappa G^{-1}.                                  \tag{2}
\]

If the exact check R≥0 succeeds, then

\[
 z^*M^{-1}z\ge\kappa z^*G^{-1}z+z^*Rz.                  \tag{3}
\]

This is the additive refinement. Failure of the sufficient check R≥0 is not
failure of (1), nor evidence against positivity of the original source.

## 2. Exact first-window Gram and shift dependence

Work on I=[−1/2,1/2], with zero extensions outside I. For 1/2<b<1 let
A_bf(x)=f(x+b)+f(x−b) and

\[
 B_b=\kappa I+w_0(I-A_b),\qquad \kappa>0,\quad w_0\ge0.
\]

Each edge point is coupled to precisely one other edge point; the middle cell
has no partner. Thus B_b≥κI, and, with
α=(κ+w₀)/(κ(κ+2w₀)), β=w₀/(κ(κ+2w₀)),

\[
 B_b^{-1}h(x)=
 \begin{cases}
 \alpha h(x)+\beta h(x+b),&-1/2<x<1/2-b,\\
 h(x)/(\kappa+w_0),&1/2-b<x<b-1/2,\\
 \alpha h(x)+\beta h(x-b),&b-1/2<x<1/2.
 \end{cases}                                               \tag{4}
\]

Endpoint conventions do not affect L² functions. In primitive even parity use
h₀=1, h₂=6x²−1/2, with squared norms 1,1/5. In primitive odd parity use
h₁=2x, h₃=20x³−3x, with squared norms 1/3,1/7. These pairs are orthogonal.
Formula (4) makes every entry ⟨h_i,B_b⁻¹h_j⟩ an exactly integrable piecewise
polynomial at rational b.

Let the genuine shift satisfy |b−b₀|≤d_b and
1/2<b₀−d_b≤b₀+d_b<1. For any bounded p and either constraint h, if
|p|≤S_p, |h|≤S_h and |h′|≤S_h′ on I, then

\[
 |\langle p,(B_b^{-1}-B_{b_0}^{-1})h\rangle|
 \le d_b S_p(4S_h/\kappa+\beta S_{h'}).                    \tag{5}
\]

Proof: the two moving cell boundaries sweep total measure at most 2d_b.
On those regions each old or new inverse value has modulus at most S_h/κ,
because α+β=1/κ and the middle coefficient is ≤1/κ. Off them only the shifted
argument changes, with modulus ≤β d_b S_h′ over a set of length ≤1. Integrate
against p. No continuity of p across the nominal cells is needed.

For M_b=L*B_b⁻¹L, apply (5) to p=h_i and h=h_j. Symmetry allows the smaller of
the (i,j) and (j,i) bounds. Write these symmetric bounds ε_ij and set
ρ=max_i Σ_j ε_ij. Then

\[
 M_b\preceq M_{b_0}+\rho I.                               \tag{6}
\]

Indeed the absolute row sums bound the norm of the Hermitian error: expand its
quadratic form and use 2|x_i x_j|≤|x_i|²+|x_j|². The implementation rounds the
right-hand side upward on a 10⁻²⁴ grid, charging a further 2·10⁻²⁴ I, so U is
an exact rational Loewner upper. Inversion of its two-by-two matrix uses its
positive determinant, never approximate eigenvalue ordering.

## 3. Residual uncertainty and the additional matrix saving

Let p₁,p₂ lie in the high moment space, each given by three rational polynomial
pieces at b₀. Put Z₀=(⟨h_j,B_b₀⁻¹p_i⟩)_{ji}. Formula (5) gives entrywise
errors |(Z_b−Z₀)_{ji}|≤e_ji. For any fixed positive semidefinite R from (2)
and 0<θ<1, reverse Young gives

\[
 Z_b^*RZ_b\succeq(1-\theta)Z_0^*RZ_0
 -(\theta^{-1}-1)\left(\sum_{i,j,k}|R_{jk}|e_{ji}e_{ki}\right)I. \tag{7}
\]

To prove it, apply the scalar inequality
||x+y||²≥(1−θ)||x||²−(θ⁻¹−1)||y||² to
x=R^(1/2)Z₀v and y=R^(1/2)(Z_b−Z₀)v. The error operator is positive
semidefinite and bounded by its trace times I. Expanding that trace gives the
displayed upper bound. This proves the matrix inequality for every v at once.

The old diagonal contribution in (3) is bounded by its previously certified
inequality, and (7) is added to it. Thus this operation cannot secretly replace
one uncertified approximation by another.

For the actual source residual r_i=p_i+e_i, where ||e_i||≤δ_i in the primitive
space, the constrained inverse has norm ≤1/κ. The common Young parameter η>0
therefore bounds the inverse Gram by

\[
 (1+\eta)\,\mathrm{Gram}_{T_b}(p_i)
 +\frac{1+1/\eta}{\kappa}\sum_i\delta_i^2 I.               \tag{8}
\]

Consequently the new signed-Schur lower increases by (1+η) times (7).
The original finite-source errors and infinite Gamma action-tail errors in (8)
are unchanged. The shift uncertainty in (5) concerns the known nominal p_i;
the action error for the true residual remains separately charged in δ_i.

## 4. Independent finite Gram enclosure

On each of the three cells, h_i(B_b₀⁻¹h_j) is a polynomial of degree at most
six. For an even number n of subintervals, step size Δ, the composite Simpson
remainder is bounded by

\[
 |\int_l^r f(x)dx-S_n(f)|
 \le (r-l)\Delta^4\sup_{[l,r]}|f^{(4)}|/180.              \tag{9}
\]

The implementation evaluates the polynomial with Horner's rule at rational
nodes, uses the monomial triangle bound for f⁽⁴⁾, and does not call an
antiderivative. Symmetrize its two off-diagonal enclosures, add their row-error
radius and the same shift error from (5), then round outward. This produces
another U and another exact R, independently of the integration method in (6).
It verifies both the Gram enclosure and a strictly positive additional saving.
This is independence of finite integration algorithms, not independence of the
source, the constrained-inverse theorem or the all-high source comparison.

## 5. Source identification and reproducibility

The source is the unchanged SUCC file `source_weil_hierarchy.py`, Git blob
`0cc8510b71d178fc79e8d410a86d8b6014cf9178`, introduced at
`b0cef75f47de29b1326b351df35b9e5423f2ed4f`. It is not one of the 72 imported
files at the historical import anchor. The probe replays `source_parameters()`
and the all-high comparison in `full_prime_resolvent.py` before constructing
the nominal residuals. No user-provided source dictionary or zero ordinates
are used.

The primitive source action is exactly the previously derived

\[
 \sum_{j<J}\left(\frac4{4j+1}I-E_{(4j+1)/2}\right)
 -C I-w A_{\log2}
 +2|\cosh(x/2)\rangle\langle\cosh(x/2)|
 -2|\sinh(x/2)\rangle\langle\sinh(x/2)|,
\]

where C=γ+π/2+3log2+logπ and w=log2/√2. On this interval the only visible
genuine prime power is 2; the half-density is 1/2. The omitted Gamma terms and
all parameter/Taylor errors retain the old rigorous budget. The all-high
comparison is D≥B_b with w₀=12/25 and κ=63/500 in primitive even parity,
κ=153/500 in primitive odd parity. Its source-form identification remains a
paper-proof dependency; passing finite tests does not discharge it formally.

The held-out source run uses J=10, M=96, P=18, η=1/4 and θ=1/1024. The earlier
cloud source receipt used J=8, M=80. Here M is a Taylor depth, **not** a spatial
discretization. The independent finite Gram discretization uses 32 Simpson
subintervals on each cell. A separate original-source matrix/action holdout
uses J=6, M=72, P=18 and checks all signed channels on six specified mode pairs.

Reproduce from the repository root:

```sh
python -m unittest discover -s tests -p test_cloud_exact_moment_inverse.py -v
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python scripts/cloud_exact_moment_source_probe.py \
  --output research/2026-10-20/CLOUD_EXACT_MOMENT_SOURCE_J10.json \
  --source-holdout-output research/2026-10-20/CLOUD_EXACT_MOMENT_SOURCE_HOLDOUT_J6.json
```

The receipts record implementation hashes and exact rational matrix lowers.
Decimal displays are never used for a sign verdict. The test suite also checks
separate Simpson grids (8, 14, 32), nonzero rational shift errors, large rational
matrix coefficients, invalid input types, and the no-gain case w₀=0. An
indefinite excess weight is explicitly rejected; the code does not retain its
positive part, which would not preserve the asserted Loewner inequality.

### Executed result at J=10, M=96

The replay completed in approximately 123 seconds. In derivative coordinates
(odd means primitive even, and vice versa), the additional rigorous gains over
the earlier diagonal constraint method are the following matrices divided by
10¹⁸. Row/column order is (P₁(2x),P₃(2x)) in derivative odd parity and
(P₂(2x),P₄(2x)) in derivative even parity, using the same clamped trial
corrections as the source baseline; these basis vectors are not unit-normalized:

| Derivative parity | (1,1) | (1,2)=(2,1) | (2,2) |
|---|---:|---:|---:|
| odd | 1140578380274 | 309387024716 | 132103244158 |
| even | 5681262457777 | 4140610017078 | 3019675561094 |

Both leading entries and determinants are strictly positive in exact integer
arithmetic. The separate Simpson construction also certifies positive-definite
additional gains in both blocks. The resulting Schur lower matrices have
diagonals approximately (−0.01253943,−0.01238891) in derivative odd parity and
(−0.00694754,−0.00672089) in derivative even parity. Both **lower** matrices
remain negative definite; this is a failure to certify the true source sign,
not a negative-source theorem. The J=6, M=72 independent source matrix/action
holdout found intersecting rigorous enclosures for all six specified pairs.

This comparison is with the old method recomputed at the **same** J=10, M=96,
same trials, same source parameters and same residual-error budgets. It does
not attribute the improvement from raising J=8 to J=10 to the new inverse.

A separate internal referee reconstructed (1)–(10) and checked 60 shifted-Gram
cases using independent SymPy integration and rational PSD comparisons. It also
recomputed all four method ceilings from the receipt's outward rational
parents and verified all recorded implementation hashes. Referee commit
`9249bb8` carries `OPERATOR_REFINEMENT_REVIEW.md` and the receipt
`research/2026-10-20/main-vii-referee/operator-symbolic-holdout.json`.
Its audited source receipt SHA-256 is
`321d80b0dc38aeddf52f6c0b0c398370b3b18fae285c6fbd1751acc999bc28f9`.
This is a separate same-family model review with a different arithmetic
implementation, not an external referee or a formal-kernel proof.

### A certified boundary of this particular refinement

Since ||A_b||≤1, one also has B_b≤(κ+2w₀)I. Thus
M_b≥G/(κ+2w₀) and, for each nominal residual column,

\[
 (Z_b^*M_b^{-1}Z_b)_{ii}
 \le(\kappa+2w_0)\sum_j
       \frac{(|(Z_0)_{ji}|+e_{ji})^2}{\|h_j\|^2}.        \tag{10}
\]

Add (1+η) times this **upper** cap to the previously certified ambient-source
lower matrix (before either moment correction). The receipt records the
resulting outward rational diagonal ceilings. They are strictly negative in
both blocks: approximately (−0.01248845,−0.01238422) for derivative odd and
(−0.00687119,−0.00668007) for derivative even. Therefore, with the current
trials, ambient comparison estimate,
η and source-action error budget held fixed, even an ideal exact evaluation of
the complete two-moment correction cannot produce a positive-semidefinite
lower certificate. This is a proved boundary of this particular refinement,
not a statement about the true source sign. Improving the ambient estimate or
the joint error budget is outside its scope.

## 6. Literature and remaining boundary

The constrained inverse is a classical finite-rank shorting/Schur identity;
(5) is a direct translation estimate and (7) is Young's inequality. This work
claims a stronger source-specific bound, not a new abstract operator theorem.
For the actual arithmetic source see Masatoshi Suzuki, *Weil's quadratic form
via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3),
September 23, 2026, equation (1.3), Theorem 1.1 and Corollary 1.2. The live arXiv
record and those precise statements were inspected on October 20, 2026.
They identify the arithmetic screw function and the Friedrichs/form-core
setting; they do not prove the project-specific finite high-block estimate or
the positivity of S₄. The general operator B_b used in this note should not be
confused with the differently named differential operator B_a in that paper.

The exact-Gram method exhausts the saving available from these two constraints
at the fixed comparison B_b, apart from the small shift/rounding/Young losses.
If the certified lower is still indefinite, further progress requires a
stronger comparison operator, improved genuine source trials, a tighter joint
residual-error estimate, or additional valid constraints. Adding constraints
not satisfied by the actual high space would be invalid. A negative lower
matrix does not show that the true signed Schur complement is negative.
