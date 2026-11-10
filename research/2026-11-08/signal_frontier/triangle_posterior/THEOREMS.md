# A source-authenticated Pascal circle, minimal tomography, and two clock limits

**PROVED PAPER / finite exact checks; original-zero covariance, pi normality
and RH OPEN.** No worldwide novelty or new general category is asserted.
The finite linear algebra and probability ingredients are classical; this
note fixes their source-compatible composition and its exact information cost.

## TP1. The posterior-valued circle realization commutes with Pascal update

Keep the original operational source, for each fixed a>0:

```
Q(x)=4-2e^(-3x)-e^(-4x)-e^(-5x)>0,  x>0,
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
mu_a(dx)=e^(-ax)Q(x)dx/R(a),
f(x)=e^(-8x), g(x)=1-f(x),
M_(m,j)(dx)=binom(m,j)f(x)^(m-j)g(x)^j mu_a(dx).
```

The authenticated BBP marks are separate:
`r(n)=R(8n-7)`, `U_0=0`, `U_n=16U_(n-1)+r(n)`, with the full unwrapped
states, integer carries and original four-pole provenance. The Pascal clock
m counts declared sensor trials. It is not the deterministic source clock n.

Fix alpha=(sqrt5-1)/2 and zeta=e(alpha), where e(t)=exp(2pi i t). Define

```
nu_m(dx,dz)=sum_(j=0)^m M_(m,j)(dx) delta_(zeta^j)(dz).
```

Then the single source-preserving kernel

```
K((x,z), .)=f(x) delta_(x,z)+g(x) delta_(x,zeta*z)
```

obeys `nu_(m+1)=nu_m K`, with `nu_0=mu_a tensor delta_1`. Thus iterating r
steps and then s steps equals iterating r+s steps. The latent x is retained;
this is a circle-valued realization of the **measure-valued** Pascal update.

**Proof.** The mass at zeta^j after one step is
`f M_(m,j)+g M_(m,j-1)`. Pascal's binomial identity gives M_(m+1,j).
Distinct grades have distinct circle points because alpha is irrational.
Composition follows by finite expansion of the same kernel, without a new
independence assumption. For every bounded measurable observer A(x,z),
enumerating words, grouping by grade, and pushing to the circle give the
same integral. The source signature travels as an unchanged mark. QED.

This uses the existing finite history/pushforward/probe machinery; no category
class is introduced. Explicit naturality: for a measurable source map
T:X->X' with T_*mu=mu', f=f' composed with T, and identical source signature,
`(T,id)_*(nu_m K)=[(T,id)_*nu_m]K'`. Check the two branches pointwise.
The induced maps preserve identity and composition. This is the declared
class of source-preserving morphisms; an arbitrary projection losing f or
changing the seed/carry signature is not in that class.

Integrating out x leaves the circle law
`eta_m=sum_j q_(m,j)delta_(zeta^j)`, with q_(m,j)=M_(m,j)(X).
Its next transition needs the grade posterior
`nu_(m,j)=M_(m,j)/q_(m,j)`:

```
q_(m+1,j)=q_(m,j) E[f|m,j]+q_(m,j-1) E[g|m,j-1].       (TP1)
```

The posterior expectation is part of the state, not a constant reconstructed
from the current grade masses without assumptions. For the known authentic
prior mu_a, a and (m,j) determine its posterior analytically. This is exactly
the existing source-relative sufficiency theorem, not a claim that grade
masses alone identify an unknown prior.

## TP2. An inscribed triangle exactly reconstructs its three masses

At m=2 let z_j=zeta^j. Three distinct points on a circle are noncollinear.
For nonnegative q_j summing to1, the complex expectation
`Phi=q_0z_0+q_1z_1+q_2z_2` belongs to their closed convex hull and uniquely
specifies all three masses. Set u=z_1-z_0, v=z_2-z_0 and
`[u,v]=Im(conjugate(u)v)=D`. Then

```
q_1=[Phi-z_0,v]/D,
q_2=[u,Phi-z_0]/D,
q_0=1-q_1-q_2.                                      (TP2)
```

For these golden vertices,
`D=4 sin²(pi alpha) sin(2pi alpha) !=0`.
The formula follows by taking the two oriented areas of
`Phi-z_0=q_1u+q_2v`. It also gives an explicit precision bound: a complex
readout error at most epsilon changes q_1,q_2 by at most
`epsilon|v|/|D|`, `epsilon|u|/|D|`, respectively, and total mass-vector L1
error by at most `2epsilon(|u|+|v|)/|D|`.

This reconstructs a probability **law** from an exact mean readout. One
physical single-trial circle point is not that mean. Arbitrarily accurate
mean acquisition is a separate resource assumption; no finite alphabet
encodes arbitrary real masses exactly. Nor do these three masses recover
all latent posterior measures. A known source family can supply the latter
as a separate analytic model.

## TP3. Only ceil(m/2) coherent harmonics are needed, and this is sharp

More generally let z_0,...,z_m be any distinct unit complex numbers and let
q_j be arbitrary real masses with sum1. Define

```
Phi_h=sum_(j=0)^m q_j z_j^h,   h=1,...,H,
Phi_0=1,  Phi_(-h)=conjugate(Phi_h).
```

The masses are uniquely determined whenever `2H>=m`. In particular the
smallest contiguous harmonic menu that works for every interior probability
vector is

```
H_min=ceil(m/2).                                     (TP3)
```

**Proof of sufficiency.** For two candidate vectors let v be their real
difference. Equal measurements imply `sum_j v_j z_j^h=0` for every integer
h between -H and H. Choose any m+1 consecutive exponents in this interval.
The corresponding square complex matrix is a Vandermonde matrix multiplied
by a nonzero diagonal matrix, with determinant a nonzero monomial times
`product_(i<j)(z_j-z_i)`. It is invertible, hence v=0.

**Proof of necessity.** The real observation matrix has rows
`1, Re(z^h), Im(z^h)` for1<=h<=H, at most2H+1 rows. If2H<m, its nullspace
contains nonzero real v. The first row implies sum v=0. Starting from any
strictly positive q, choose sufficiently small epsilon>0 so that both
q+epsilon v and q-epsilon v remain positive. They have identical observed
harmonics and different masses. This also demonstrates that positivity
alone does not repair the rank deficit. QED.

The result is a strict reduction from the proposed m complex harmonics to
ceil(m/2); it uses the reality and known total mass of the unknown weights.
It does not assert uniform conditioning as m grows or as nodes approach each
other. Exact golden nodes are distinct at every finite depth, but an inverse
norm/noise budget must still be supplied at that depth. The oracle records
numerical conditioning rather than promoting it to an all-m bound.

For a real linear target `L(q)=sum_j t_j q_j`, the smaller menu is sufficient
for every probability q **iff** t lies in the real row span of the observation
matrix (including the constant row). If t is in the span, the same linear
combination of observations gives L. Otherwise there exists v in its kernel
with t.v!=0; the preceding positive pair gives different targets in one
observation fiber. This is a target-relative truth-descent certificate within
the existing finite observer framework. For a restricted finite candidate
family, fewer measurements may suffice; that is a different quantifier.

## TP4. Equal triangle masses need not carry equal future posteriors

Consider the same conditional Bernoulli sensor but an unknown discrete prior
for f in(0,1). Let

```
prior A: P(f=1/5)=1/4, P(f=3/5)=3/4,
prior B: P(f=2/5)=3/4, P(f=4/5)=1/4.
```

Both have `E f=1/2`, `E f²=7/25`, hence both depth-two grade distributions are

```
(q_0,q_1,q_2)=(7/25,11/25,7/25).                     (TP4)
```

Their exact triangle mean Phi and **all** depth-two circle harmonics coincide.
But `E_A f³=41/250`, `E_B f³=22/125`; these differ by3/250. The next
failure probabilities after observing grade0 are

```
E_A[f|J_2=0]=41/70,
E_B[f|J_2=0]=22/35.                                  (TP5)
```

The depth-three q_0 values and subsequent circle laws therefore differ.
Taking X=-(log f)/8 realizes both as finite positive-X priors. This is a
countermodel to an unqualified prior-free update from grade masses. These
are **not** the authenticated continuous BBP prior mu_a; they do not refute
the known-prior sufficiency theorem. They pinpoint the information that a
source-general observer must retain.

The same construction generalizes: alternating binomial finite-difference
weights on m+2 distinct equally spaced f-values give two positive priors
whose moments through degree m agree and whose (m+1)st moments differ.
Consequently full depth-m grade tomography cannot in general replace the
posterior field in an indefinitely refinable observer.

## TP5. The circle law has two rigorously different source clock limits

Let alpha be irrational, h any fixed nonzero integer, and z=e(h alpha).
Complexifying the finite joint source transform gives exactly

```
Phi_(a,m)(h)=sum_j q_(a,m)(j)z^j
           =E_mu_a[(f(X)+z g(X))^m].                 (TP6)
```

This is an auxiliary sensor expectation, not an average of e(hU_n).

**Fixed source parameter.** For every fixed a>0,

```
lim_(m->infinity) Phi_(a,m)(h)=0.                     (TP7)
```

Indeed `0<f,g<1` mu_a-almost surely and z!=1, so
`|f+zg|²=1-2(1-Re z)fg<1`; the integrand tends to0 and is bounded by1.
Dominated convergence proves TP7. By circle Fourier uniqueness/Weyl's
measure criterion, the grade-circle probability laws converge weakly to
Haar. This concerns the sequence of distributions of J_m alpha, not a
claim that one observed Bernoulli realization or the BBP orbit is normal.

A direct source-dependent envelope is also available. Put beta=a/8,
c_h=1-cos(2pi h alpha)>0 and B_beta=max(1,2^(1-beta)). For all m>=1,

```
|Phi_(a,m)(h)| <= Gamma(beta)/(2R(a)) * (2/(c_h m))^beta
                 + 15 B_beta/(8R(a)c_h² m²).         (TP8)
```

**Proof.** Change variables t=f=e^(-8X). Its density is
`t^(beta-1)Q(-log t/8)/(8R(a))`. Use `Q<=4` on0<t<=1/2 and
`Q<=15(-log t)/8<=15(1-t)/4` on1/2<=t<1; the latter follows from
`Q(x)=2(1-e^-3x)+(1-e^-4x)+(1-e^-5x)<=15x`.
Also `|t+z(1-t)|^m<=exp(-m c_h t(1-t))`.
On the first interval t(1-t)>=t/2 and extend the gamma integral to infinity.
On the second, t(1-t)>=(1-t)/2 and t^(beta-1)<=B_beta; extend
`integral u exp(-m c_h u/2)du` to infinity. The two bounds are exactly TP8.
Its constants depend on a and h; it cannot be used uniformly when a grows
with m without checking those constants.

**Native original source diagonal.** For a_m=8m-7 and the same fixed h,

```
lim_(m->infinity) Phi_(8m-7,m)(h)=(2-e(h alpha))^-2 !=0. (TP9)
```

**Proof.** The existing source boundary theorem gives Y_m=a_m X_m converging
in distribution to Gamma(2,1), because Q(x)=15x+O(x²). Uniformly on every
compact set of y>=0,

```
[e^(-8y/a_m)+z(1-e^(-8y/a_m))]^m -> exp((z-1)y).
```

Each side has modulus at most1. Tightness plus uniform convergence on compact
sets therefore transfers expectations, without assuming pointwise dominated
convergence across changing measures. The limiting integral is
`integral_0^infty y exp(-(2-z)y)dy=(2-z)^-2`, since Re(2-z)>=1. It is nonzero.
Equivalently the limiting law is the pushforward of the negative-binomial
probabilities `(j+1)/2^(j+2)`, j>=0, by j->e(j alpha). This countable pure
point probability law is not Haar even though its support is dense. QED.

Thus the source parameter and observation clock cannot be silently identified.
The same authentic positive kernel gives a Haar limit under one declared
experiment and a non-Haar limit under another. TP9 extends the inherited
Gamma–Poisson transform to the coherent circle probe; it does not introduce
a new Gamma boundary theorem or solve a selected arithmetic problem.

## TP6. What survives source and carry authentication

The circle kernel, its harmonic reconstruction and TP7–9 depend on the
positive source mu_a. They are unchanged if the deterministic BBP recurrence
uses a different seed while preserving r(n). In particular the coherent
same-forcing s*=-pi/16 has U_n(s*)=-T_n and fixed-h signed time means tending
to1, while all these auxiliary Pascal observations remain identical.
Keeping the literal zero seed as an authenticated mark identifies the intended
source, but an estimate on its **selected signed phases** still must be proved.

Exponentiation alone forgets integer lifts: replacing U by U+k leaves e(hU)
unchanged for every integer h. The full unwrapped recurrence and carry marks
must therefore accompany the circle realization. Neither posterior sufficiency
nor finite circle inversion reconstructs a discarded lift by itself.

The strongest source-safe next arrow would relate a specified retained
posterior/circle statistic to the signed prime-complement covariance, with a
uniform all-epoch error and the literal zero boundary used in the proof.
TP7 is especially unsuitable as a substitute: its cancellation already holds
in an auxiliary sensor that cannot distinguish the coherent wrong seed.

## Claims, provenance and verification

| Claim | Status | Contribution and boundary |
|---|---|---|
| TP1–2 | PROVED PAPER | Exact posterior-valued circle update and three-mass triangle reconstruction; not all hidden histories |
| TP3 | PROVED PAPER | Sharp ceil(m/2) harmonic menu and target row-span criterion; conditioning separate |
| TP4 | REFUTED shortcut | Two explicit positive priors with identical triangle masses and different next posterior |
| TP7–8 | PROVED PAPER | Fixed-a auxiliary source-circle decay with explicit bound; not BBP time decay |
| TP9 | PROVED PAPER / inherited boundary input | Native-clock coherent circle limit is nonzero; order of limits matters |
| Original-zero signed covariance decay | OPEN | No posterior-to-selected-phase estimate supplied |

Read-only dependencies: `docs/OPERATIONAL_TRIANGLE.md`; TG01–04 in
`research/2026-10-29/operational_triangle_frontier/THEOREMS.md` and its exact
`operational_triangle.py`; canonical `observational_succ.duck_bbp` and finite
history/probe machinery. The inherited posterior and Gamma-rank theorem are
credited, not republished as novel. New results here are paper statements;
finite exact Gaussian-rational checks and numerical golden-node checks
have separate authority. No new Lean or external scholarly review is claimed.

**Pi base-16 normality: OPEN. RH: OPEN.**
