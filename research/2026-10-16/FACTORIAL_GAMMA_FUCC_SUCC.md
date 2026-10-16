# SUCC × FUCC: factorial moments, Gamma spirals, and source-faithful reconstruction

**Date:** 2026-10-16. **Scope:** a freestanding SUCC/FUCC mathematical offshoot,
stacked on the finite Dirac/Gamma continuum and band-dealiasing research
(PRs #141/#142). Parent starting point: `6623fd11b710a40dc5f9cd2375ba74d759be0245`.
**Status:** classical source results with explicit **PROVED PAPER** derivations,
**EXACT FINITE** arithmetic certificates, independent optional numeric tests,
**REFUTED** shortcuts, and specified **UNVERIFIED** downstream arrows.
**No academic-priority claim. RH PROVED: NO.**

## 0. The object the user proposed

The motivating diagram is

```text
NatPoint --SUCC factorial--> NatPoint
    |                       |
    v                       v
ComplexPoint --Gamma dynamics--> ComplexPoint
```

The crucial repairs are **(i)** retain the natural index as part of the state,
**(ii)** use a *skew-product successor*, not Gamma itself as a successor map,
**(iii)** distinguish exact integer interpolation from unique continuation,
**(iv)** declare the positive source before using probability or a Hilbert Gram.
`n -> n!` is not injective because `0!=1!`; and `Gamma(x+1)` is not globally
injective on positive real x. No isomorphism of the underlying N and C sets is
established. The isomorphism below is **fibered dynamical conjugacy**.

Notation: `S(n)=n+1`; `V_p(n)=pn` for genuine prime `p`. The user calls the
multiplication operator FUCC and the successor SUCC. Ordinary `Gamma` and
`Gamma_R(s)=pi^(-s/2)Gamma(s/2)` are **different** functions; `Gamma_R` includes
true Tate parity/normalization but not a prime-source identification.

## FGF-1. A factorial/Gamma dynamical conjugacy (PROVED PAPER; classical recurrence)

Take the base `N_0` and nonzero complex parameter `t in R`. More generally the
fiber may be all of C, with zero retained. Define

\[
T_0(n,a)=(n+1,(n+1)a),\qquad
T_t(n,a)=(n+1,(n+1+it)a),
\]
\[
K_t(n,a)=\left(n,a\,\frac{\Gamma(n+1+it)}{n!}\right).
\]

For each `n`, the scalar multiplier of `K_t` is nonzero: Gamma has no zeros
and neither its argument nor `n!` hits a pole. Thus `K_t` is a bijection
`N_0 x C -> N_0 x C`, with fiberwise inverse. By the Gamma recurrence,

\[
\boxed{K_t\circ T_0=T_t\circ K_t}\quad\text{on }\mathbb N_0\times\mathbb C.
\]

**Proof:** the second component of the left side is
`(n+1)a Gamma(n+2+it)/(n+1)! = a Gamma(n+2+it)/n!`;
on the right it is `(n+1+it)a Gamma(n+1+it)/n!`. These are equal.
The factorial orbit from `(0,1)` maps to the Gamma orbit from
`(0,Gamma(1+it))`, *not* the orbit from `(0,1)` unless `t=0`.

This is a genuine conjugacy of the declared skew systems; it says nothing about
a global algebra isomorphism between N and R/C or an invertible Gamma function.

## FGF-2. The spiral is determined by a log-source phase law (CLASSICAL/PROVED PAPER)

For `n>=1` and real `t`, set `C_n(t)=Gamma(n+1+it)` and use the continuous
unwrapped argument with `arg C_n(0)=0`. Then

\[
\boxed{\frac{d}{dt}\log|C_n(t)|=-t\sum_{k=n+1}^\infty\frac1{k^2+t^2}},
\]
\[
\boxed{\frac{d}{dt}\arg C_n(t)
=H_n-\gamma_E+\sum_{k=n+1}^\infty\frac{t^2}{k(k^2+t^2)}>0}.
\]

**Proof:** differentiate `log Gamma(n+1+it)` using digamma, and apply the
standard digamma partial-fraction expansion. For `n>=1`, `H_n>gamma_E`;
all summands of the angular correction are nonnegative. The first equation
shows strictly expanding radius for `t<0`, strictly contracting for `t>0`;
`t=0` gives maximum radius `n!`. Stirling shows both tails decay to 0 while
unwrapped phase accumulates without bound. Gamma never equals 0.

The finite-product and infinite-tail decomposition is

\[
\frac{C_n(t)}{n!}
=\Gamma(1+it)\prod_{k=1}^n(1+it/k),\qquad
\left|\frac{C_n(t)}{n!}\right|^2
=\frac{\pi t}{\sinh\pi t}\prod_{k=1}^n(1+t^2/k^2)
=\prod_{k=n+1}^\infty(1+t^2/k^2)^{-1}.
\]

The value at `t=0` is 1 by continuity. This is not a literal singularity
being born: the origin is only an asymptotic accumulation point of the curve.

## FGF-3. All factorial moments uniquely authenticate a positive source

**CLASSICAL / PROVED PAPER under a load-bearing positivity hypothesis.** Let
`mu` be a Borel probability measure on `[0,infinity)` such that

\[
\int x^n\,d\mu(x)=n!\quad\text{for every integer }n\ge0.
\]

By monotone convergence for `0<=t<1`,

\[
\int e^{tx}\,d\mu(x)=\sum_{n\ge0}\frac{t^n n!}{n!}
=\frac1{1-t}.
\]

The MGF is finite in a neighborhood of 0 (for negative `t`, `x>=0` bounds
it), so uniqueness of the MGF determines exactly `dmu(x)=e^{-x}dx`.
Its Mellin transform, initially `Re(z)>-1`, is

\[
\mathcal M\mu(z)=\int_0^\infty x^z e^{-x}dx=\Gamma(z+1).
\]

For each fixed `n`, the probability density
`dmu_n(x)=x^n e^{-x}dx/n!` gives the normalized Gamma spectral response

\[
\phi_n(t)=\int x^{it}\,d\mu_n(x)
=\frac{\Gamma(n+1+it)}{n!}=\mathbb E[e^{it\log X_n}].
\]

Positivity, *all* moments and the `[0,infinity)` source domain distinguish
this from mere agreement of integer values or a recurrence. This is an
ordinary exponential probability law, not a claim that prime FUCC jets are
literally independent exponential random variables.

## FGF-4. Entire finite factorial Hankel tower has an exact Pascal Gram

**PROVED PAPER / EXACT INTEGER arithmetic**, independent of analytic Gamma.
For dimension `r`, indices `0<=i,j,k<r`, set

\[
H_{ij}=(i+j)!,\qquad A_{ik}=\begin{cases}i!\binom{i}{k},&k\le i,\\0,&k>i.\end{cases}
\]

Vandermonde's convolution gives

\[
\begin{aligned}
(AA^\top)_{ij}
&=i!j!\sum_k\binom{i}{k}\binom{j}{k}\\
&=i!j!\binom{i+j}{i}=(i+j)!.
\end{aligned}
\]

Thus

\[
\boxed{H=AA^\top\succ0,\quad
\det H=\prod_{k=0}^{r-1}(k!)^2>0.}
\]

The lower-triangular Pascal transport itself obeys
`A_(n+1,k)=(n+1)(A_(n,k)+A_(n,k-1))`: **factorial SUCC multiplied by a
Pascal successor recurrence**. `A` is invertible on every finite truncation.

**Firewall:** this is a positive *factorial moment* Hankel Gram. The genuine
completed Weil/Suzuki form is signed and is not identified with this Gram.
Positive factorial moments cannot promote the missing RH-hard arrow.

## FGF-5. Arbitrarily deep finite-factorial counterfeits (CLASSICAL / PROVED)

Let `P_m(x)=(-1)^m m! L_m(x)` be monic Laguerre degree `m`, orthogonal
against `e^-x dx`. Classical Gaussian quadrature gives a positive m-atom
measure `mu_m` on `(0,infinity)` with moments **exactly** `n!` through
`n=2m-1`. Because `P_m` vanishes on the nodes and is orthogonal to all
lower polynomials,

\[
\boxed{(2m)!-\int x^{2m}d\mu_m(x)
=\int P_m(x)^2e^{-x}dx=(m!)^2.}
\]

Proof of the deficit: `x^(2m)-P_m(x)^2` has degree <=2m-1, so quadrature
integrates it exactly. Both `x^(2m)` and `P_m^2` have leading coefficient 1;
`P_m` vanishes on the m nodes. The norm equals `(m!)^2` by Laguerre
orthogonality. The implementation verifies monic coefficients,
`int x^k P_m e^-x dx=0` for every `k<m`, and the exact squared norm.
Actual positive roots/weights for arbitrary m are an **imported Gaussian
quadrature theorem**, not constructed by the pure-integer implementation.

**Exact m=2 countermodel:** nodes `2-sqrt(2)`, `2+sqrt(2)` with positive weights
`(2+sqrt(2))/4`, `(2-sqrt(2))/4`. Their moments start
`1,1,2,6,20,68,...` versus factorials `1,1,2,6,24,120,...`.
The first distinction is at degree 4 with deficit 4. The authentic 3x3 Hankel
determinant is 4, the atomic 3x3 determinant is 0; the first 2x2 blocks agree.

**General finite-observer obstruction:** for *any* prescribed finite moment
horizon `K`, choose `m` with `2m-1>=K`. Then a **positive** m-atom law agrees
with all observations up to K, but it is not the exponential law and its
log-Fourier response is a finite trigonometric sum, not the Gamma spiral.
This establishes a source-identification failure for the finite-moment-only
probe grammar; it does not forbid additional probes or an all-moments proof.

## FGF-6. Even complete factorial recurrence + radius can leave the phase dark

**PROVED PAPER hostile countermodel.** For nonzero real `c`, define

\[
\widetilde F_c(z)=\Gamma(z+1)e^{c\sin(2\pi z)}.
\]

It is meromorphic, shares all factorial values `F(n)=n!`, the recurrence
`F(z+1)=(z+1)F(z)`, the Gamma poles, and even their residues (the periodic
gauge is 1 at each integer). On integer vertical lines `z=n+it`,

\[
\widetilde F_c(n+it)=\Gamma(n+1+it)
\exp\bigl(i c\sinh(2\pi t)\bigr).
\]

The modulus is **exactly unchanged** while the phase changes arbitrarily fast
at large `|t|`. Therefore the integer recurrence, exact poles/residues and
full radial envelopes do **not** fix the Gamma twist.

For real x>0 the gauge is positive, but
`(log F_c)''(x)=psi_1(x+1)-(2pi)^2 c sin(2pi x)` becomes negative along
arbitrarily large x for any `c!=0`: Gamma's trigamma tends to zero. Hence it
fails log convexity and Bohr-Mollerup selection. It cannot be the Mellin
transform of a positive `[0,infinity)` measure with factorial moments because
FGF-3 uniquely selects the exponential source.

This countermodel *forces* the positive-source/MGF or another growth/convexity
axiom to remain explicit. Radial pictures alone cannot authenticate phase.

## FGF-7. A SECOND Gamma construction from finitely many stochastic SUCC clocks

**CLASSICAL Euler-Gamma product + PROVED PAPER rational band bound.** Let
`E_k` be independent exponential random variables of rate `k`, `k=1,2,...`.
For integer `n>=0` and `M>n`, set the **finite** log-clock observable

\[
U_{n,M}=\log M-\sum_{k=n+1}^M E_k,
\quad\phi_{n,M}(t)=\mathbb E e^{itU_{n,M}}
=M^{it}\prod_{k=n+1}^M\frac{k}{k+it}.
\]

This is an actual characteristic function of a finite positive probability
source. Its construction reads **no Gamma values and no zeta zeros**.

The mean tends to `H_n-gamma_E`; its variance tends to
`sum_(k>n)1/k^2`, and independent centered series converge in L2 and almost
surely. Euler's product then identifies the limit in law as

\[
U_n\stackrel{d}=\log X_n,\qquad X_n\sim\mathrm{Gamma}(n+1,1).
\]

Equivalently, the direct characteristic functions converge to
`Gamma(n+1+it)/n!`. This agrees with FGF-3 through a **different route**:
finite independent exponential delays versus positive factorial moments.
The analytic limiting identity is classical; these are not independent
physical measurements of Gamma.

**Band-uniform exact-rational theorem.** For rational `T>=0`, `M>n`, `T<M+1`,
write

\[
B(M,T)=\frac{T}{2M}+\frac{T^2}{2M(1-T/(M+1))}.
\]

If `B<1`, then for every real `|t|<=T`,

\[
\boxed{\left|\phi_{n,M}(t)-\frac{\Gamma(n+1+it)}{n!}\right|
\le\frac{B(M,T)}{1-B(M,T)}.}
\]

**Proof of the analytic inequality:** use the exact product logarithm
and `0<H_M-log M-gamma_E<=1/(2M)`. For `|t|<=T<M+1`, each omitted term
satisfies

\[
|\log(1+it/k)-it/k|\le\frac{t^2}{2k^2(1-T/(M+1))},\quad k>M.
\]

Since `sum_(k>M)1/k^2<=1/M`, the difference of chosen logarithms of the
finite and limiting characteristic functions has magnitude <=B. The true
`|phi_n|<=1` because it is a characteristic function; use
`|e^w-1|<=e^B-1<=B/(1-B)` for `B<1`. All output inequalities and B are exact
rational arithmetic; numerical evaluation of characteristic functions is
merely a calibration, not interval evidence.

**Independent coupling-based bound:** the tail variance is <=1/M,
so for a common underlying family of `E_k`,

\[
\sup_{|t|<=T}|\phi_{n,M}(t)-\phi_n(t)|
\le T\left(M^{-1/2}+(2M)^{-1}\right).
\]

The code uses `ceil(sqrt(M))/M` as a rational upper bound for `M^-1/2`.
This bound is looser but follows from a different estimator (L2 coupling
rather than complex-log products).

**Archimedean link** (retaining the real-place phase):

\[
\boxed{\frac{\Gamma_{\mathbb R}(2n+2+2it)}
{\Gamma_{\mathbb R}(2n+2)}
=\pi^{-it}\phi_n(t).}
\]

The same uniform error bound holds after multiplication by the phase
`pi^(-it)`. This does *not* turn the positive probability covariance into
the completed signed Weil form.

## FGF-7B. Finite ordered SUCC events = multiplicative Beta clocks; Gamma from rare events

**CLASSICAL probability / PROVED PAPER exact source-map + rational error.**
This is the strongest *finite first* reconstruction in the present round and
needs **no Gamma values** to define the finite source.

Let `Y_1,...,Y_M` be independent uniform points on `(0,1)` and let their
strictly ordered values be `0<U_(1)<...<U_(M)<1`. Their joint density on
the open simplex is exactly `M!`, because there are `M!` equally likely
permutations of the original source labels. The simplex volume is `1/M!`.
Here the **factorial is literally the normalization of finite causal order**.

Now take *independent* `B_k~Beta(k,1)` with densities
`k b^(k-1) db` for `0<b<1` and `k=1,...,M`. Define

\[
\boxed{U_{(k)}=\prod_{j=k}^M B_j,\qquad 1\le k\le M.}\tag{7B.1}
\]

This map is a smooth bijection on open finite probability carriers: its
inverse is `B_k=U_(k)/U_(k+1)` for `k<M` and `B_M=U_(M)`. The Jacobian is

\[
\left|\det\frac{\partial(U_{(1)},\ldots,U_{(M)})}
{\partial(B_1,\ldots,B_M)}\right|
=\prod_{k=1}^{M}B_k^{k-1}.
\]

Therefore the independent-Beta density transforms exactly:

\[
\prod_{k=1}^M\bigl(k B_k^{k-1}\bigr)
=\underbrace{M!}_{\text{ordered source density}}
\underbrace{\prod_{k=1}^M B_k^{k-1}}_{\text{Jacobian}}.
\]

**This is a bona fide finite-source probability-space isomorphism (modulo
zero-measure boundaries).** It preserves the *full joint history*, not merely
individual endpoint moments. `S` advances the ordered event index; the
`B_k` are independent **multiplicative** source coordinates. The term
"FUCC-like" refers to this multiplication and must not be conflated with
the arithmetic operator `V_p:n->pn` on prime-labelled carriers.

Rescale the `(n+1)`-st source event for any `0<=n<M`:

\[
X_{n,M}=M U_{(n+1)}=M\prod_{k=n+1}^M B_k.
\]

Its distribution is exactly scaled `Beta(n+1,M-n)` (via the joint-source
isomorphism), and for each integer `r>=0` its moments are **rational**:

\[
\boxed{
\mathbb E[X_{n,M}^r]
=\frac{(n+r)!}{n!}
\frac{M^r M!}{(M+r)!}.}
\]

The multiplicative correction factor is
`C_(M,r)=prod_(j=1)^r M/(M+j)`. Since
`1-prod_j(1-a_j)<=sum_j a_j` for `0<=a_j<=1`, with
`a_j=j/(M+j)`, we obtain the exact-rational moment budget

\[
\boxed{
0\le\frac{(n+r)!}{n!}-\mathbb E[X_{n,M}^r]
\le\frac{(n+r)!}{n!}\frac{r(r+1)}{2M}.}
\]

For an independent, distributional route, counting points below `x/M`
shows, for `0<=x<=M`,

\[
P(X_{n,M}\le x)
=P\big(\mathrm{Bin}(M,x/M)\ge n+1\big).
\]

Let `N_x~Poisson(x)`. Couple each `Bern(p)` with `Pois(p)` maximally,
where `p=x/M`. Their total variation distance is
`p(1-e^{-p})<=p^2`. Under an independent product coupling, the
sum-count mismatch probability is at most `Mp^2=x^2/M`.
Hence *uniformly in every admissible n*:

\[
\boxed{
\left|P(X_{n,M}\le x)-P(N_x\ge n+1)\right|
\le\min(1,x^2/M).}
\]

For a fixed finite observation interval `0<=x<=X` and `M>=X`,
the CDF error is uniformly bounded by `X^2/M`, with *no* numerical
Gamma oracle. The Poisson waiting time `T_(n+1)` (the `(n+1)`-st
rate-one event) has the Gamma density
`x^n e^{-x}/n!` on `x>0`:

\[
P(T_{n+1}\le x)=P(N_x\ge n+1)
=1-e^{-x}\sum_{j=0}^{n}\frac{x^j}{j!}.
\]

Thus `X_(n,M) => Gamma(n+1,1)` in law, and the finite rational moment
correction tends to 1 for every fixed n and r. The **continuum Gamma
source is the limit of a finite ordered-events carrier**. The Gamma
Mellin/Fourier spiral is the transform of that limiting positive source
(FGF-3), not an arbitrary interpolation imposed afterward.

This is a precise SUCC × multiplicative-factor lift with an operational
law-of-small-numbers error budget. It does *not* produce the Euler-prime
factorization of zeta: the independent random Beta(k,1) clocks use every
natural `k`, not authenticated prime indices. Nor does a distributional
limit execute infinitely many source events in finite physical time.

## FGF-8. Forward positive SUCC vs backward exponential factorization

For the Gamma-shape source family `mu_n(dx)=x^n e^-x dx/n!`, **forward**
integer SUCC is positive size-biasing,

\[
\mu_{n+1}(dx)=\frac{x}{n+1}\mu_n(dx),\qquad
w_{n+1}(u)=\frac{e^u}{n+1}w_n(u).
\]

On logarithmic coordinates its Fourier transform obeys

\[
\phi_{n+1}(t)=\left(1+\frac{it}{n+1}\right)\phi_n(t).
\]

That multiplier alone need not be a characteristic function (its modulus is
>1), so it is **NOT a forward independent-noise convolution**.

In the *reverse* direction, let `B_n~Beta(n+1,1)` independent of
`X_(n+1)~Gamma(n+2,1)`. Then

\[
B_n X_{n+1}\sim\mathrm{Gamma}(n+1,1),\quad
-\log B_n\sim\mathrm{Exp}(\text{rate }n+1).
\]

Thus the law of `U_n` is the convolution of the law of `U_(n+1)` with an
**independent negative exponential delay**. That is a precise source-driven
time-direction asymmetry: the forward transform is lawful positive
size-biasing, but an independent increment appears naturally on the backward
construction. This is classical Beta-Gamma probability, not a physical arrow
of time, quantum evidence, or an RH result.

## FGF-9. FUCC × SUCC carries: genuine prime dilation of factorial

**PROVED PAPER / EXACT INTEGER.** On `N_0`, genuine prime `p` gives

\[
\boxed{V_p S=S^p V_p,}\quad\text{since }p(n+1)=pn+p.
\]

Hence the base-address affine square is flat, though Vp and S themselves
do not commute (`Vp S != S Vp` for p>1).

Lift through factorial `F(n)=n!` and compare the p-dilated endpoint to
p independent copies of the original endpoint:

\[
\boxed{D_p(n)=\frac{(pn)!}{(n!)^p}
=\binom{pn}{n,n,\ldots,n}\in\mathbb N.}
\]

For **each** genuine valuation prime `q`, Legendre's formula gives

\[
\begin{aligned}
v_q(D_p(n))
&=\sum_{j\ge1}\left(
\left\lfloor\frac{pn}{q^j}\right\rfloor
-p\left\lfloor\frac{n}{q^j}\right\rfloor\right)\\
&=\sum_{j\ge1}\left\lfloor
p\left\{\frac{n}{q^j}\right\}\right\rfloor\ge0.
\end{aligned}
\]

The terms measure **base-q carry contributions** under scaling `n -> pn`.
The sum is finite because `q^j>pn` makes its summand zero. These are
precise SUCC/FUCC **arithmetic transfer defects**, not nontrivial curvature
of the flat underlying address square. The mathematical formula works for a
composite multiplier too, but `p=6` is explicitly refused as an *authentic
prime FUCC label*.

The two-level relation even gives an exact discrete update:

\[
\frac{D_p(n+1)}{D_p(n)}
=\frac{\prod_{r=1}^{p}(pn+r)}{(n+1)^p}.
\]

This is one genuinely mixed additive/multiplicative shape worth transporting
into the existing valuation coordinates of SUCC.

## FGF-10. Factorial/Gamma binomial 2-cocycle (PROVED PAPER)

The factorial map is not an ordinary monoid homomorphism `N,+ -> N,×`.
Its precise failure is the binomial cocycle

\[
B(a,b)=\frac{(a+b)!}{a!b!}=\binom{a+b}{a},\quad
B(a,b)B(a+b,c)=B(b,c)B(a,b+c).
\]

The complex extension on pole-free arguments is
`B(z,w)=Gamma(z+w+1)/(Gamma(z+1)Gamma(w+1))`;
its cocycle identity follows by cancellation of common Gamma factors.
This is a **coboundary**, not evidence of nontrivial cohomology or a new
arithmetic obstruction. Complex B continues meromorphically with domain
and pole restrictions; no global holomorphic group isomorphism is claimed.

## 11. Three independent routes and what they do (and do not) triangulate

| Route | Actual source | Observable | Strong point | Weakness |
|---|---|---|---|---|
| Moment reconstruction | all `n!` + positive measure | `Gamma(z+1)` Mellin | unique continuum law | requires infinitely many moment equalities |
| Finite exponential product | independent finite `Exp(rate k)` clocks | characteristic `phi_(n,M)` | rational uniform band bound | rate clocks are declared stochastic models, not authenticated primes |
| Dirac-comb Gamma_R (#141/#142) | Gaussian real-place log kernel | sampled/aliased Gamma_R | spectral alias location, de-alias certificates | assumes entire Gaussian source and Archimedean constants |
| Pascal Hankel | exact integer combinatorics | Gram `H=(i+j)!` | fully finite, strictly positive | positive factorial Hankel is not signed Weil |
| Uniform order-statistics | finite iid uniform source; independent Beta product chart | Poisson/Gamma event waiting time | exact finite joint law and rational CDF/moment error | probabilistic clocks not prime arithmetic FUCC |
| Gauss quadrature mutant | positive m-atom source | first 2m moments | universal finite-source falsifier | no contradiction with all-moment uniqueness |

The finite exponential-clock factors and ordered uniform/Beta-product chart
are two **equivalent presentations of the SAME probabilistic source**:
`E_k=-log(B_k)~Exp(rate k)`. They are NOT independent evidence for Gamma.
Moment uniqueness and Poisson-arrival limits provide differently organized
analytic derivations but still share the same classical probability foundations.
Numerical agreement is not independent empirical source authentication. The high-value new connection
is a set of *typed comparison maps*, including the exact finite joint
ordered-uniform/Beta multiplicative isomorphism, and hard countermodels,
not an RH solution.

## 12. SUCC research dependency ladder and next discriminating probes

**Closed classical or exact**, with proofs here: factorial skew conjugacy;
finite uniform order-statistic/Beta-coordinate joint source isomorphism;
rate-one Poisson/Gamma finite-event limit with exact rational CDF bounds;
positive factorial moment MGF uniqueness; exact Pascal/Hankel factor; Laguerre
quadrature finite counterfeits; phase-gauge mutant; finite exponential-clock
Gamma limit; rational spectral-band error; Beta-Gamma reverse factorization;
SUCC/FUCC arithmetic carry; binomial cocycle.

**UNVERIFIED in SUCC** (order reflects proof dependencies):

1. **Finite to continuous source map:** integrate `factorial_gamma_fucc.py`
   with `gamma_dirac_continuum.py` and `gamma_band_dealias.py`, and the
   positive order-statistic/Beta-source interface, proving a
   common normalized real-place Mellin target under *explicit* source charts.
   Falsifier: change `pi`, slope 1/2, log-frame orientation, or endpoint
   size-bias and demonstrate loss of equality.
2. **Hankel/Weil type test:** expose the actual signed completed Weil/Suzuki
   finite test functional and compare its contact/prime/Gamma/pole form with
   any candidate Gram map. **Do not equate** positive H with signed Weil.
   Falsifier: signed two-bump prime-2 witness, wrong-Gamma/parity, pole omission,
   and fake impulse at 6. An explicit negative residual or no-go is valuable.
3. **Prime-jet FUCC compatibility:** prove a source-indexed natural
   transformation from the *genuine multiplicative Euler source* to a typed
   finite-factorial/valuation representation, with source authentication and
   quantitative residuals. Test `p=2,3`, fake 6, coefficients not equal 1,
   incompatible Hecke parity, and Davenport–Heilbronn non-Euler controls.
4. **Higher Gauss counterfeits:** for arbitrary m, produce positive exact or
   interval node/weight enclosures and verify the first missing moment
   `(m!)^2`, not just a floating-point match. Compare probe closure: moments,
   characteristic functions, support tests, and Gamma recurrence.
5. **Order-statistic to Tate map:** push the finite positive Beta-product
   source through `Gamma_R(s)` normalization, compare analytic continuation
   and spectral strip norms against the verified Dirac-comb source and the
   existing Mellin test construction. The *same probabilistic source* expressed
   in Beta and exponential coordinates must not be counted as independent
   evidence. Test wrong pi, half-density, source-6 and non-Euler mutants.
6. **Parameter-uniform positive Mellin norm:** transfer the rational finite
   exponential-band bound to a stated complex strip in a sufficiently rich
   Tate–Mellin test family, with norms and tails *derived from source*, not
   postulated as arbitrary bounded constants. A single fixed-n bound is not a
   completion proof.
7. **Proof-level mechanization:** formalize Vandermonde Hankel factor,
   Legendre carry relation, and factorial cocycle in Lean/YEAN, with full
   dependency audits. Numeric Gamma comparisons remain separate.

**Next verdict-changing probe:** try a finite, source-labelled `Gamma_R`
Mellin basis element with two independent implementations (Dirac comb vs
exponential-product/Beta-Gamma). Require certified matching of normalization,
phase, derivatives and truncation under an explicit map. If the map fails a
rate-6 mutant or the prime-2 negative signed witness, do not promote it.

## Provenance and references

- Repository baseline and prior source paths: `observational_succ/gamma_succ_path.py`,
  `observational_succ/gamma_dirac_continuum.py`,
  `observational_succ/gamma_band_dealias.py`; research PRs #141 and #142.
  No historical import path is rewritten.
- NIST DLMF [Gamma recurrence](https://dlmf.nist.gov/5.5.E1),
  [Euler Gamma integral](https://dlmf.nist.gov/5.9.E1),
  [Gamma poles and zero-free property](https://dlmf.nist.gov/5.2),
  [Laguerre polynomials](https://dlmf.nist.gov/18.3),
  [Gauss-Laguerre quadrature and norms](https://dlmf.nist.gov/3.5.E27),
  [Gaussian polynomial exactness](https://dlmf.nist.gov/3.5.E20_1).
  These are **classical imported** foundations; exact local implementation
  and SUCC source typing are project-specific.
- Tests `tests/test_factorial_gamma_fucc.py`: exact integer certificates,
  independent high-precision numerical calibration and mutation controls.
  `scripts/factorial_gamma_fucc_probe.py`: deterministic exact receipt.

### Reproduction

```sh
python -m unittest discover -s tests -p 'test_factorial_gamma_fucc.py' -v
python scripts/factorial_gamma_fucc_probe.py --verify
# Full repo suite (long running) remains CI responsibility:
# python -m unittest discover -s tests -p 'test_*.py'
```

All conclusions inherit the scope of their weakest source assumptions.
Finite numerical evaluations are **OBSERVED**, not independently certified
analytic sign bounds. **RH PROVED: NO.**
