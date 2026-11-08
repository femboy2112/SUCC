# Temporal Fourier exclusion and history-predictor certificates for PE12

Status: **PROVED PAPER from the declared PE1–PE9 / BK inputs**, with exact
finite algebra checked separately. No original full real Weyl decay, Lean
certificate, or external scholarly priority is claimed. This front keeps the
original four-pole forcing, unwrapped states, literal U0=0 and chronology.

## Source, law and phase conventions

Let e(x)=exp(2 pi i x). Use exactly

`r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`,
`U_0=0`, `U_n=16U_(n-1)+r(n)`.

The previous dossier's PE1–PE9 proves the following, using PNT in the fixed
progression1 mod8 and Bourgain–Konyagin (2003), Theorem2.1. For each sufficiently
large A choose the largest prime p<=4A with p=1 mod8 and m=ord_p(16) satisfying
m^3>p. Put L=(p-1)/4, n0=L+1, I=[n0,n0+L), J=[A,2A). Then m divides L,
L/A tends to1, and

`eps_A = sum_n |1_J(n)/A-1_I(n)/L| -> 0`.

The first p-pole occurs at n_p=(p+7)/8 and the next at (p+1)/2. Throughout I,

`[U_n]_p = (4*16^(n-n_p) mod p)/p`.

For a fixed nonzero h, eventually p does not divide h. The stronger finite
results below hold uniformly in every h not divisible by p. Set

`a_n=e(h[U_n]_p)`, `b_n=e(h(U_n-[U_n]_p))`.

Thus a_n b_n=e(hU_n) exactly. Canonical rational principal parts and the
same source phase reference are essential. No independent gauge rotation is
allowed. All expectations below are finite arithmetic averages over time;
they do not randomize the initial seed.

Write delta_p=p^(-gamma), where gamma=gamma_(1/3)>0 is the exponent in the
BK import. For G=<16> in F_p^*, that theorem gives

`|m^-1 sum_(x in G) e(c x/p)| <= delta_p` for every c!=0 mod p.

No numerical value for gamma is asserted. This input is precisely the one
already authenticated in PE9; no new exponential-sum theorem is imported.

## CFS-1. Uniform temporal Fourier decay on a clean prime clock

Let g=16 mod p, xi=4h g^(n0-n_p)!=0 modp, and

`a_r=e(xi g^r/p)`, `A_k=m^-1 sum_(r=0)^(m-1) a_r e(-kr/m)`.

Then for **every** k modm,

**`|A_k|^2 <= 1/m+(1-1/m)delta_p =: beta_p^2`.**

This includes every nontrivial temporal tone, not only the old k=0 marginal.

**Proof.** Expand the square and write r=s+d in Z/mZ:

`|A_k|^2 = m^-1 sum_(d=0)^(m-1) e(-kd/m) C_d`,
`C_d = m^-1 sum_s e(xi(g^d-1)g^s/p)`.

At d=0, C_0=1. At every other d, g^d!=1 and xi(g^d-1)!=0; the inner average
is exactly a nontrivial BK subgroup sum. Apply its bound to these m-1 terms
only. This proves the displayed inequality. No independence or sign assumption
is used, and the autocorrelation phases are retained before the triangle bound.

Let tau=min(1/3,gamma)>0. Since m>p^(1/3),

`beta_p <= sqrt(2) p^(-tau/2) -> 0`.

The complete clean interval has length L=q m. Its length-L DFT is supported
only at frequencies qk; at those frequencies its coefficient is A_k. This is
an exact temporal spectral support statement about the authentic p-local
source character, not about its complementary factor.

## CFS-2. All real temporal tones and every actual source epoch

For any real theta, not necessarily k/m,

**`|L^-1 sum_(n in I) a_n e(theta n)|
 <= (3+2 log m) beta_p`.**

Consequently, with `rho_A=eps_A+(3+2 log m)beta_p`,

**`sup_(1<=h<p) sup_(theta in R/Z)
 |A^-1 sum_(n=A)^(2A-1) e(h[U_n]_p+theta n)| <= rho_A -> 0`.**

This is an unconditional, all-epoch mixed local-source/time character bound
for the deterministic p=p_A selector. It is stronger than PE9's zero temporal
tone, while still concerning only one authentic prime factor.

**Proof.** Put `D_m(t)=m^-1 sum_(r=0)^(m-1)e(rt)`. Fourier inversion gives

`m^-1 sum_r a_r e(theta r)=sum_k A_k D_m(theta+k/m)`.

Choose the closest point of the m-grid to -theta. Its Dirichlet factor has
modulus at most1. At most two grid points have circular index-distance j
from it. For such points, `m||theta+k/m|| >= j-1/2`, and

`|D_m(t)| <= min(1,1/(2m||t||))`.

Therefore the sum of the m sampled moduli is at most
`1+2 sum_(j=1)^(m-1) 1/j <= 3+2 log m`. This deliberately loose constant
also covers m=2. For the q repetitions in I the full sum factors as the
one-cycle sum times `q^-1 sum_(j=0)^(q-1)e(theta m j)`, of modulus at most1,
and a harmless source-fixed initial phase. Finally apply the exact interval
weight distance eps_A to the same unit-modulus sequence on I and J. The
estimate is uniform in theta and h. Polynomial decay of beta_p dominates
logm, and eps_A tends to0. QED.

## CFS-3. A certificate for complements learned from temporal tones

Let a predictor on the actual epoch have the explicitly represented form

`v_n=int_(R/Z) e(theta n) d sigma_A(theta)`,

where sigma_A is any finite complex measure of total variation K_A. The
frequencies, coefficients, and measure may depend on the observed history;
CFS-2 is uniform, so no independence from the data is required. Then

**`|W_A(h;0)| <= rho_A K_A + E_J |b_n-v_n|`.**

Finite sums are the case `K_A=sum_j |c_j|`, `v_n=sum_j c_j e(theta_j n)`.
A separately certified L2 approximation error also bounds the displayed L1
error. Finite-sum linearity, Fubini for a finite measure, CFS-2, and |a_n|=1
prove the inequality. This is a useful sufficient condition:

`rho_A K_A -> 0` and `E_J|b-v| -> 0` imply the authentic Weyl gate.

**Unpaid premise:** no such approximation of the original complement with
these rates is proved here. The condition is stronger than cancellation and
is not advertised as a weaker equivalent normality criterion. Generic large
Fourier expansions may have K_A growing too quickly.

The certificate is also a falsifier. If `|W_A|>=w_A` and predictor error is at
most eta_A, then `K_A >= (w_A-eta_A)_+/rho_A`. Thus PE14's maximal-covariance
shadows require diverging temporal-tone variation for every accurate predictor,
even though their local character satisfies CFS-2 unchanged.

## CFS-4. Fold away nonresonant history before charging model complexity

Let q=L/m. Define the **cycle-folded complement**

`B_r=q^-1 sum_(j=0)^(q-1) b_(n0+r+jm)`, 0<=r<m,

with `|B_r|<=1`. For the normalized DFT
`B_k=m^-1 sum_r B_r e(-kr/m)`, exact factorization gives

**`W_I=m^-1 sum_r a_r B_r=sum_k A_k B_(-k)`**,
**`Cov_I(a,b)=sum_(k!=0) A_k B_(-k)`**.

The component of b orthogonal to sequences periodic modulo m contributes
exactly zero. Arbitrarily complicated variation between the q replicas need
not be predicted. It is the **folded resonant complement**, rather than the
whole raw history, whose approximation costs enter the next bounds.

For any S subset (Z/mZ)\{0} of size s, let

`eta_S^2=sum_(k!=0,k not in S)|B_(-k)|^2`,
`nu^2=sum_(k!=0)|B_k|^2 <= 1`.

Parseval and CFS-1 yield

**`|W_A(h;0)| <= eps_A+delta_p+beta_p sqrt(s) nu+eta_S`.**

Indeed the k=0 term is bounded by delta_p, the retained nonzero modes by
Cauchy–Schwarz and `sum_(k in S)|A_k|^2<=s beta_p^2`, and the omitted modes
by their L2 norm because `sum_k|A_k|^2=1`. The I-to-J term is eps_A.
The sharper retained-mode factor is `sqrt(nu^2-eta_S^2)` in place of nu.

A concrete sufficient rate is `s_A=o(p_A^tau)` and `eta_(S_A)->0`, where
`tau=min(1/3,gamma)`. Both hypotheses concern the original source complement;
neither is obtained here. S may be selected adaptively after observing the
history because the prime bound is uniform over every Fourier subset.

## CFS-5. Exact history-projection tradeoff and lawful shift models

On C^m use `<u,v>=m^-1 sum_r conjugate(u_r) v_r`. Put
`u=conjugate(a)-E conjugate(a)`, `v=B-E B`, and let P be any orthogonal
projection on a declared zero-mean history-feature subspace. Set

`alpha=||u||`, `nu=||v||`, `d=||Pu||`, `eta=||(I-P)v||`.

The exact two-term identity and bound are

`Cov_I(a,b)=<Pu,Pv>+<(I-P)u,(I-P)v>`,

**`|Cov_I| <= d sqrt(nu^2-eta^2)+sqrt(alpha^2-d^2) eta`.**

Cross terms vanish by orthogonality; Cauchy–Schwarz proves the bound.
It is sharp for the Hilbert norm constraints by aligning the two components.
For a partition of time/history labels, P is the finite cell-average
projection after removing the constant. Then d is conditional prime leakage
and eta is complement prediction error. A finer history model decreases eta
but increases d. Neither change has a universally favorable effect on the
sum. Complete retained time labels produce singleton cells and d=alpha,
eta=0, which gives no saving.

If instead the d-dimensional complex predictor space is invariant under the
cyclic shift r->r+1, it is a span of d Fourier modes: the shift has m distinct
eigenvalues, and invariance under its finite order also implies invariance
under the inverse and under its spectral projections. Thus CFS-1 bounds its
prime leakage by beta_p sqrt(d). The result holds for any selected member of
this model class, including an adaptively chosen member.

**Necessary scope restriction:** a general one-dimensional learned model is
not automatically nonresonant. The space spanned by conjugate(a) predicts the
coherent shadow perfectly and has prime leakage1. Shift closure, Fourier
support, or separately measured leakage must be supplied. Mathematical linear
dimension here is not a claim about a finite bit register or physical access.

## CFS-6. Sharp sparse-model obstruction for maximal covariance shadows

Let `||B||<=1`, `||a||=1`, and `|<conjugate(a),B>|>=w`, 0<=w<=1.
Let S be any set of s Fourier modes, now including the constant if desired,
and let `rho=min(1,beta_p sqrt(s))`. Every predictor v supported in S obeys

**`||B-v|| >= [w sqrt(1-rho^2)-rho sqrt(1-w^2)]_+`.**

**Proof.** The least error for that support is E=||(I-P_S)B||. Put
`d=||P_S conjugate(a)||<=rho`. The same orthogonal decomposition gives
`w<=d sqrt(1-E^2)+sqrt(1-d^2) E`. If E>=sqrt(1-d^2), the claimed lower bound already holds. Otherwise
the right side is on its increasing branch; for w>d, inversion gives `E>=w sqrt(1-d^2)-d sqrt(1-w^2)`; this decreases with d, so
replace d by rho. If w<=rho, the asserted lower bound is zero and automatic.
The geometric formula is exact: it is the sine of the difference of the
corresponding angles on the unit circle. It also follows by squaring the
nonnegative terms twice. For B=conjugate(a), E=sqrt(1-d^2), attaining the
w=1 version with the actual d.

PE14 has W_J->1 and the same selected local phases. Interval gluing gives
W_I->1 for its shadow as well. Therefore, for every adaptive support with
`s_A beta_(p_A)^2->0`, **the best folded-complement predictor error tends to1**.
Since the zero predictor has error at most1, this limit is sharp. The shadows
force almost all resonant complement energy outside every such sparse model.
They refute any argument that learning itself guarantees the required
predictability or Fourier sparsity. They do not refute those properties for
literal zero.

## What has and has not been paid

- CFS-1–2 prove new local-source signed correlations with all temporal tones,
  by an exact autocorrelation reduction to the already imported BK theorem.
- CFS-3–5 give explicit sufficient inequalities and preserve all signed terms.
  They distinguish a predictable complement from an uncontrolled resonant
  residual; the discarded replica component is exactly harmless.
- CFS-6 gives a quantitative, sharp hostile complexity obstruction.
- No decay/sparsity/predictability estimate for the **original** b_n has been
  proved. PE12 and the full real Weyl gate remain OPEN. This is supporting
  arithmetic/instrument progress, not a proof of pi normality or RH.

Source provenance: previous `learning_yoneda/arithmetic/PRIME_EPOCH_THEOREM.md`
PE1–PE9 and PE14 at the pinned parent; original source in `selected_orbit.py`;
[Bourgain–Konyagin (2003), Theorem2.1](https://www.numdam.org/item/10.1016/S1631-073X(03)00281-4.pdf).
Fourier inversion, cyclic shift diagonalization, conditional variance and
Hilbert projections are classical. The proofs above are complete for the
stated imported input; finite tests are not certification of that input.

## CFS-7. Fixed-degree polynomial temporal chirps are also excluded

This extension was proposed by the root after CFS-1–2, and derived here
independently at the level of the finite differencing inequality. It uses
the same BK input. Fix an integer d>=1. Let P be **any real polynomial of
degree at most d**, with no coefficient-size restriction. Choose
`2<=H<=m` with `d(H-1)<m`. Then

**`|m^-1 sum_(r=0)^(m-1) e(xi g^r/p+P(r))|^(2^d)
 <= 5^(2^d-1) [1/H+delta_p+d(H-1)/m]`.**

The displayed constant is conservative, not optimal.

**Detailed proof.** Extend `f(r)=e(xi g^r/p+P(r))` by zero outside [0,m).
For integer h>0 define `Delta_h f(r)=f(r+h) conjugate(f(r))`. Products of
these differences have modulus at most1 and support within [0,m). The finite
window Gram identity and Cauchy–Schwarz (A2 of the prior dossier), with m
as ambient length, give for every such F

`|E_m F|^2 <= (m+H-1)/(mH)
 [E_m|F|^2+2 sum_(h=1)^(H-1)(1-h/H) Re E_m Delta_h F]
 <= 2/H+2 max_(1<=h<H)|E_m Delta_h F|`.

Here `E_m=m^-1 sum_(r=0)^(m-1)`, and zero extension ensures the correlations
have the correct truncated supports. We used `E_m|F|^2<=1` and the exact
weight sum `(H-1)/2`; no cyclic wrap is silently introduced.

Let x_j be the maximum magnitude of the normalized mean after j such
differences, over all shifts h_i in [1,H-1]; x_0 is the original magnitude.
The inequality implies `x_j^2<=2/H+2x_(j+1)`. All x_j<=1. Put t=1/H and
z_j=x_j+t. Then

`z_j^2=x_j^2+2t x_j+t^2
 <=2x_(j+1)+4t+t^2 <=5(x_(j+1)+t)=5z_(j+1)`.

Iterating gives `x_0^(2^d)<=5^(2^d-1)(x_d+1/H)`.
On the surviving interval `0<=r<m-sum_i h_i`, the d-fold difference equals

`e( xi product_i(g^(h_i)-1) g^r/p + Delta_(h_1)...Delta_(h_d)P(r) )`.

The polynomial difference is constant. Each 0<h_i<m has g^(h_i)!=1, so
the source coefficient remains nonzero modulo p. The complete m-term
subgroup average is bounded by delta_p. Removing `sum_i h_i` endpoints
changes its m-normalized average by at most `d(H-1)/m`. Thus
`x_d<=delta_p+d(H-1)/m`, proving the theorem.

For fixed d, choose H=floor(sqrt(m)) once m is large enough. The right side
tends to0. On every successive complete cycle in I, the polynomial
`P(n0+jm+r)` still has degree at most d, so the same bound holds uniformly
and averaging the cycles preserves it. Finally the I-to-J interval error
gives the all-epoch statement

**`sup_(1<=h<p_A) sup_(deg P<=d)
 |A^-1 sum_(n in J_A)e(h[U_n]_pA+P(n))|
 <= eps_A + {5^(2^d-1)[1/H+p_A^-gamma+d(H-1)/m_A]}^(1/2^d) ->0`.**

This is a new unconditional local-source polynomial-time correlation bound.
It does not control polynomials whose degree grows without the displayed
cost, or arbitrary history-dependent phases. Source-dependent fixed-degree
polynomial coefficients are allowed because the bound is fully uniform in P.

CFS-3 consequently extends to finite mixtures, or finite-variation measures,
of these fixed-degree chirps with the corresponding larger error factor.
Their complement approximation is still an **OPEN arithmetic premise**.
PE14's resonant complementary factors must evade every accurately fitting
mixture whose coefficient variation times this error factor tends to0.
