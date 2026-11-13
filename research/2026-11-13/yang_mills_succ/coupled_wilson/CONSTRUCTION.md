# Constructing coupled finite SU(2) Wilson states with exact certificates

**Status:** proved paper construction and exact rational implementation; classical
ingredients with a new SUCC adapter and hostile controls. No priority claim for
compact-group integration, Taylor approximation or reflection positivity.
The scope is a specified finite link graph. No continuum limit, mass gap,
four-dimensional uniqueness, or BBP cancellation is proved here.

**Code:** `observational_succ/ym_coupled_wilson.py`.
**Tests:** `tests/test_ym_coupled_wilson.py`.
**Baseline:** PR #613, `a8da424c84869d737462fdec0a64d7921a92eb50`.

## 1. The source and the finite constructive theorem

Let a finite oriented graph have vertex set V and edge set E. Associate an
independent unit quaternion q_e in SU(2) to each edge. A signed edge word must
be a composable closed path; traversing an edge backwards uses q_e^{-1}.
Let H_p(q) be its **ordered** holonomy and

\[
 x_p(q)=\tfrac12\operatorname{Tr}H_p(q)=\operatorname{Re}H_p(q),
 \qquad |x_p(q)|\le1.
\]

For a finite list of such paths and nonnegative rational couplings beta_p,
declare the actual finite Wilson source

\[
 d\mu(q)=Z^{-1}w(q)\,d\lambda(q),\qquad
 w(q)=\exp\!\left(\sum_p\beta_p x_p(q)\right),
 \quad \lambda=\bigotimes_{e\in E}\operatorname{Haar}_{SU(2)}.
\]

The conventional constant in the Wilson action cancels in this normalized law.
This definition uses the full compact group. It does not replace SU(2) by a
finite subgroup or give separate independent samples to overlapping loops.

**CW-01 — proved, finite source construction.** Given this graph, its closed
paths, the beta_p, a real rational polynomial f in the 4|E| quaternion
coordinates, and a positive rational epsilon, there is a terminating exact
algorithm returning rational numbers E_K and delta_K such that

\[
 |\mu(f)-E_K|\le\delta_K\le\epsilon.
\]

It returns a strictly positive, normalized, gauge-invariant polynomial density
on the same compact source carrier. All its polynomial moments are rational.
The algorithm retains shared links and the order of every holonomy. Its
termination is for every fixed finite input; it makes no efficient-complexity
claim and no estimate uniform in graph size or lattice spacing.

### Exact integration, including all shared variables

Write a quaternion q=(q_0,q_1,q_2,q_3). Normalized Haar measure is normalized
surface measure on S^3: left and right unit-quaternion multiplication are
orthogonal transformations, so this probability law is bi-invariant.
Coordinate reflection gives zero for any odd exponent. For k_i nonnegative,

\[
 \int_{S^3}\prod_{i=0}^3 q_i^{2k_i}\,dq
 =\frac{\prod_i(1/2)_{k_i}}{(2)_{k_0+k_1+k_2+k_3}}.
 \tag{1}
\]

To derive (1), integrate exp(-|z|^2) times the corresponding monomial over
R^4 in two ways. Cartesian integration gives the product of
Gamma(k_i+1/2). Polar integration gives
pi^2 Gamma(K+2) times the normalized sphere moment, where K=sum k_i.
Divide and cancel Gamma(1/2)^4=pi^2. Both sides of (1) are then rational.
For product Haar, multiply the four-coordinate moments **once per edge**.
Integrating a polynomial is consequently a finite rational sum. The unit-sphere
relations cause no difficulty: integration annihilates their polynomial ideal.

Hamilton quaternion multiplication and inversion on S^3 use only addition,
multiplication and coordinate sign changes. Thus every x_p is a rational
polynomial. A sparse exponent tuple has four positions for each original edge;
overlapping loops refer to those same positions. No factorization across loops
is performed.

### A positive polynomial density and an explicit error

For an even nonnegative integer K define

\[
 P_K(t)=\sum_{j=0}^{K}\frac{t^j}{j!}.
\]

For t>=0 this is positive. For t<0, Taylor's theorem says
e^t-P_K(t)=e^xi t^{K+1}/(K+1)!<0, so P_K(t)>e^t>0. Therefore

\[
 w_K(q)=\prod_pP_{K_p}(\beta_p x_p(q)),\quad
 Z_K=\int w_K\,d\lambda>0,
 \qquad E_K=\frac{\int f w_K\,d\lambda}{Z_K}
 \tag{2}
\]

is an actual probability source for every choice of even degrees K_p.
By (1), both integrals in (2) are rational and explicitly computable.

Set S=sum_p beta_p and

\[
 T_K=\sum_p\frac{\beta_p^{K_p+1}}{(K_p+1)!}.
\]

On the carrier, Taylor's remainder is at most
e^{beta_p} beta_p^{K_p+1}/(K_p+1)!, and
|P_{K_p}(beta_p x_p)|<=e^{beta_p}. Telescoping the difference of the
products gives the uniform estimate

\[
 |w-w_K|\le e^S T_K. \tag{3}
\]

Suppose |f|<=M, where the sum of the absolute rational coefficients of f
is one valid computable M. Writing N=int f w and N_K=int f w_K,
using |N_K|<=M Z_K and |Z-Z_K|<=int|w-w_K| gives

\[
 \begin{aligned}
 \left|\frac N Z-\frac{N_K}{Z_K}\right|
 &\le \frac{|N-N_K|}{Z}
       +\frac{|N_K|\,|Z-Z_K|}{ZZ_K}\\
 &\le\frac{2M}{Z}\int|w-w_K|\,d\lambda
 \le 2M e^{2S}T_K,
 \end{aligned}
\]

because w>=e^{-S}, hence Z>=e^{-S}. Since e<3,

\[
 \boxed{\delta_K=2M\,3^{\lceil2S\rceil}
             \sum_p\frac{\beta_p^{K_p+1}}{(K_p+1)!}}
 \tag{4}
\]

is a rational error certificate. Taking all K_p=0,2,4,... eventually makes
(4) at most epsilon: factorial growth dominates each fixed exponential power.
Each individual polynomial calculation is finite. This proves termination
and CW-01. Sparse expansions may nevertheless become prohibitively large.

### Gauge provenance

For vertex gauges g_v, an oriented link transforms as
q_e -> g_source(e) q_e g_target(e)^{-1}. Along a closed path the adjacent
gauge factors telescope, leaving conjugation of the ordered holonomy at its
basepoint. Its real trace is unchanged. Both w and w_K are therefore gauge
invariant, as is product Haar. `LinkGraph.closed_word` checks incidence and
closure before the source density is constructed. The low-level free-word
polynomial functions alone do not certify a graph path.

## 2. What makes this a computational graph presentation

Each quaternion product is a finite ordered arithmetic graph. Finite Taylor
products, monomial integration by (1), and rational normalization produce a
finite evaluation graph for (2). Their state functional is a positive linear
functional: for every complex polynomial a,

\[
 \omega_K(a^*a)=Z_K^{-1}\int |a|^2w_K\,d\lambda\ge0.
\]

This is an exact constructive presentation of a restricted, source-specified
observable calculation. It is not an assertion that all quantum systems or all
noncomputable linear operators admit this presentation. The Euclidean
probability Hilbert space L^2(mu_K) also remains distinct from the physical
Hilbert space obtained after a positive-time reflection quotient.

The source-weighted Haar operators from PR #613 can re-present this same state:
cell weights, all retained details and transformed observable matrices must
all use mu_K. The moment error (4) then compares bounded polynomial observables
with the actual finite Wilson law. Wavelet truncation or any further partition
approximation contributes a separate error, not a free identification.

## 3. Reflection positivity: a condition retained, and a shortcut refuted

**CW-02 — proved local, character-positive factor.** For beta>=0 and any
nonnegative K, the function

\[
 W(g)=P_K\!\left(\beta\,\tfrac12\operatorname{Tr}g\right)
\]

is positive definite on SU(2). Indeed the k-th power of Tr(g) is the
character of the k-fold tensor power of the fundamental unitary
representation. W is their finite nonnegative linear combination, with
weights beta^k/(2^k k!). For any g_i and c_i,

\[
 \sum_{i,j}\bar c_i c_j\operatorname{Tr}(\rho(g_i)^*\rho(g_j))
 =\left\|\sum_i c_i\rho(g_i)\right\|_{HS}^2\ge0.
\]

Even K additionally ensures pointwise strict positivity, needed for the
probability density without an extra truncation constraint.

When a reflected graph has a declared decomposition into positive-half and
negative-half configurations, a crossing plaquette must become
W(A(v)^{-1}A(u)) in that common frame. Products of such kernels remain
positive definite, including when their A's share links. Same-half weights
must occur in matched reflected pairs, and boundary integration must preserve
the decomposition. Under these explicit geometric hypotheses, the usual
reflection form is a sum/integral of squared norms and is nonnegative.
The precise reflection-order test and its limitations are in
`REFLECTION_ORDER.md`. This construction does **not** declare every arbitrary
graph/path collection reflection-positive merely because it is gauge-invariant.

### Exact hostile compact-group source

Take two mirrored independent SU(2) holonomies a,b, with x=Re(a), y=Re(b).
Reflection exchanges a and b, and the positive-half algebra consists of
functions of a. The exact Wilson density exp(2x+2y) factorizes into the same
positive one-variable weight on the two sides. Its reflected form is the
absolute square of a one-side expectation, hence nonnegative.

Now approximate the **global amplitude** exp(x+y) by its even Taylor
polynomial p=1+x+y+(x+y)^2/2 and use the positive density p^2/Z. This law is
strictly positive, gauge-invariant and reflection-invariant. Nevertheless it
fails reflection positivity. On the basis (1,x,x^2), its unnormalized
reflected Gram matrix is

\[
 G=\begin{pmatrix}
 69/32&13/16&179/256\\
 13/16&5/16&1/4\\
 179/256&1/4&113/512
 \end{pmatrix}.
\]

Expansion of p^2=1+2(x+y)+2(x+y)^2+(x+y)^3+(x+y)^4/4, together with
m_0=1, m_2=1/4, m_4=1/8, m_6=5/64 and vanishing odd Haar moments,
gives every entry. Here Z=G_00=69/32. For v=(-4,5,5),

\[
 v^TGv=-71/512,\qquad
 \omega_K\!\left(F\,\theta(F)\right)=-71/1104<0,
 \quad F=-4+5x+5x^2.
\]

**CW-03 — refuted shortcut.** Ordinary positivity, gauge invariance,
reflection invariance and even Taylor approximation of a global amplitude
do not by themselves preserve reflection positivity. This finite auxiliary
source is built on the actual compact group; the failure is not caused by a
finite-group surrogate. The factorwise construction was chosen because its
nonnegative character factors retain the reflected-kernel proof.

This witness is checked by the quaternion polynomial engine. The separate
Lean certificate `formal/WilsonTaylorNegative.lean` derives the nine rational
matrix entries from the stated moments and verifies the negative normalized
value. Its exact sign-mutation control is rejected; replay is recorded in
`FORMAL_REPLAY.md`. That scope does not formalize the analytic Haar formula
or the continuum Yang--Mills theorem.

## 4. Shared-link controls that an independent-loop mutation fails

Take a one-vertex two-edge graph with holonomies a,b and define

\[
 x=\operatorname{Re}a,\quad y=\operatorname{Re}b,\quad
 z=\operatorname{Re}(ab),\quad t=\operatorname{Re}(ab^{-1}).
\]

With a=(a_0,vec a), b=(b_0,vec b), let u=a_0b_0 and d=vec a dot vec b.
Then z=u-d and t=u+d. Formula (1) gives

\[
 \int xyz=1/16,\qquad \int zt=-1/8,\qquad \int z^2t^2=1/12.
\]

For the last identity,
int u^4=1/64, int u^2d^2=1/192, and int d^4=5/64.
Thus int(u^2-d^2)^2=1/12. Both z and t have zero mean and individually
the correct Haar SU(2) trace distribution, but they are not independent.

Consequently the coupled two-factor partition is exactly

\[
 \int P_2(\beta z)P_2(\gamma t)
 =1+\frac{\beta^2+\gamma^2-\beta\gamma}{8}
     +\frac{\beta^2\gamma^2}{48},
\]

whereas replacing the loops by independent copies produces
(1+beta^2/8)(1+gamma^2/8), a different answer. For the one-factor density
P_2(z/2), the separate means of x and y are zero but their joint mean is
1/33. These controls force the implementation to retain the actual shared
carrier and mixed moments.

Noncommutative order is separately visible: the unit quaternions i,j,k give
Re(ijk)=-1 but Re(jik)=+1. The commutator iji^{-1}j^{-1}=-1 differs from
the identity obtained by illegally commuting factors. These are exact test
inputs, not a claim that trace distinguishes every pair of orders.

## 5. Provenance and the next falsifier

| Input | Exact contribution | Boundary |
|---|---|---|
| PR #613 `ym_succ_character.py` and `SUCC_CHARACTER_PROOF.md` | Exact rational validation and the one-plaquette finite Taylor/state construction | The new engine extends to all link coordinates and coupled ordered loops |
| PR #613 `HAAR_SOURCE_BRIDGE.md` | Source-weighted complete Haar coordinates and finite-cutoff moment transport | Does not make interacting Wilson masses uniform |
| Existing `hopf_source_exact.py` | Hamilton quaternion convention and the need to preserve multiplication order | Its BBP coordinates are not asserted to be Wilson link variables |
| Product S^3 integration, derived in (1) | Exact compact SU(2) polynomial moments | No continuum or large-volume estimate |
| Character positivity, derived in CW-02 | A positive reflected crossing kernel under a declared split | Gauge invariance alone does not supply the split |

The next decisive finite probe is a reflected multi-plaquette graph whose
crossing paths share half-links: compare exact mixed moments and the reflected
Gram form with an independently implemented tensor-character contraction.
The independent-loop mutation must disagree on the mixed moments; an incorrect
reflection order may create a negative mode. Agreement certifies only that
finite source and observable family. A continuum claim would additionally need
uniform renormalized bounds, compatible cutoff embeddings, and the full
analytic reconstruction hypotheses. Estimate (4), with its e^{2S} cost,
does not supply them.

### Validation scope

The first focused run of `python -m unittest discover -s tests -p
'test_ym_coupled_wilson.py' -v` passed all **12 tests**, after the predeclared
probe protocol was made available on the research branch. This count covers
the exact new finite adapter and its hostile controls. Repository-wide checks
and any later independent formal certificate are recorded by the parent
research report; they are not implied by this focused run.
