# SUCC — Lorentz clock tiling, golden arithmetic boosts, and the source-carry firewall

**2026-10-30 | Research-only mathematical continuation of PR #392**, pinned to its exact head `00b073fb9adedcda91cc499540add10dfcfabc66`; merged Main XVI ancestor `e18ba565ca540adb7edf3292f5593929e76d91c5`. The original four signed BBP poles and the retarded boundary `U_0=0` are immutable. These constructions are not physical spacetime, a physical thermodynamic law, or a base-16 normality proof.

## 1. Typed source and the conserved observation budget

Preserve the authentic source

\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},\quad
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0,
\quad a_n=8n-7,
\quad \mu_a(dx)=e^{-ax}Q(x)dx/R(a).
\]

Fix one native time `n` and split its **one** original `n`-trial Pascal observation budget into `m_+ + m_- = n` (integers). Both panels retain the *same* latent `X~mu_(a_n)`; do not reset the posterior at the intermediate endpoint. Given `X=x`, success probability is `p_X=1-e^{-8x}` and the panels have independent binomial counts conditionally on `X`:

\[
P_n(J=j,K=k)=\binom{m_+}{j}\binom{m_-}{k}
\frac{\sum_{q=0}^{j+k}(-1)^q\binom{j+k}{q}R(a_n+8(n-j-k+q))}{R(a_n)}.
\tag{LC-1}
\]

All finite entries are positive and rational. By Vandermonde, `S=J+K` has the original *single* `n`-trial Pascal endpoint law `q_n(S)`, independent of the split. Conditioned on `S=s`, the partition `J` is exactly hypergeometric:

\[
P(J=j\mid S=s)=\binom{m_+}{j}\binom{m_-}{s-j}/\binom ns.
\tag{LC-2}
\]

This finite source statement is inherited from PR #392, not claimed as new here. The present round tests its Lorentz-like change of observation frame.

## 2. Rank-two limiting surface; a quantitative finite-source map

Put `p=m_+/n`. On the original source diagonal `a_n=8n-7`, the original positivity and `Q(x)=15x+O(x^2)` imply `a_n X => Gamma(2,1)` and `J,K|a_n X` tend to independent Poisson variables with rates `pY,(1-p)Y` **conditional** on the shared `Y`. Unconditionally,

\[
\boxed{H_p(z,w)=E[z^J w^K]=(2-pz-(1-p)w)^{-2},\qquad 0\le p\le1.}
\tag{LC-3}
\]

The coefficients are the exact negative-multinomial/binomial splitting of original Oily weights:

\[
P_p(J=j,K=k)=\underbrace{\frac{j+k+1}{2^{j+k+2}}}_{w_{j+k}}
\binom{j+k}{j}p^j(1-p)^k.
\tag{LC-4}
\]

`H_p(z,z)=G(z)=(2-z)^(-2)` regardless of `p`. Hence the total-grade golden fixed point `q*=phi^-2` and marked rank-two contrast `phi^-1-gamma` survive **every frame allocation of one conserved total clock**. This is an observer-level invariance, not covariance of actual selected BBP digits.

**Quantitative source-faithful finite map (proved).** For `n>=3`, `m_+ + m_-=n`, `p=m_+/n`,

\[
\boxed{TV(P_n(J,K),P_p(J,K))\le \min(1,28/n).}\tag{LC-5}
\]

Proof: inherited `TV(q_n,w)<=22/n` for the original four-pole single-panel grade law. Conditional on `S=s`, comparison of sampling `s` observations without vs with replacement bounds hypergeometric-to-binomial TV by `s(s-1)/(2n)` (couple to independent draws; disagreement only if a collision). The authentic field has `E X^2<6/a_n²`, `1-e^{-8X}<=8X`, so `E[S(S-1)]<=n(n-1)*64 EX²<384n²/a_n²<12` for `n>=3` (since `a_n>=17n/3`). Integrating the conditional bound costs less than `6/n`. The `22/n` marginal and `6/n` conditional bounds add. The all-infinite-grade tail is included in TV. No π digit statistic enters this proof.

## 3. A genuine projective Lorentz action on the observer split

Use null observation-clock intensities `u_+=p`, `u_-=1-p`, so `T=u_++u_-=1`, `X=u_+-u_-=2p-1=:v`. Before re-normalizing, an ordinary 1+1 Lorentz boost in null coordinates is

\[
u_+'=e^\eta u_+,\quad u_-'=e^{-\eta}u_-,\quad
T'=T\cosh\eta+X\sinh\eta,\quad X'=X\cosh\eta+T\sinh\eta.
\tag{LC-6}
\]

It preserves `T²-X²=4u_+u_-`, but **changes** `T`. The observer's requirement to keep one native budget uses the projective re-normalization `(u_+',u_-')/(u_+'+u_-')`, giving

\[
\boxed{p_\eta=\frac{e^\eta p}{e^\eta p+e^{-\eta}(1-p)},\quad
v_\eta=\frac{v+\tanh\eta}{1+v\tanh\eta}.}
\tag{LC-7}
\]

The maps compose as `B_eta B_xi=B_(eta+xi)` and preserve the interval `0<p<1`. This is *precisely Einstein velocity addition as projective mathematics*. It is not an isometry of a Minkowski metric on the fixed-`T=1` normalized slice: the scale `T'` has been divided out. Finite counts only allow rational `p=m_+/n`; continuous boosts therefore act exactly on the limiting observer family and approximately on large finite budgets.

### A directional entropy weight, without invented physical heat

From the balanced observer `p0=1/2`, the limiting joint path weight changes by the exact ratio

\[
\boxed{\frac{P_\eta(j,k)}{P_0(j,k)}=e^{\eta(j-k)}(\cosh\eta)^{-(j+k)}.}
\tag{LC-8}
\]

Conditional on total grade `S=j+k`, the log-partition function is `S log cosh eta`. Therefore

\[
\boxed{D_{KL}(P_\eta\Vert P_0)=2[\eta\tanh\eta-\log\cosh\eta]\ge0.}
\tag{LC-9}
\]

The total-grade distribution is unchanged and `E[S]=2`. This is a mathematical Gibbs/relative-information response to a change of observation orientation; it is not a measured entropy-production law of physical BBP digits.

## 4. Golden integer arithmetic supplies a *separate* exact Lorentz isometry

The already-used SUCC golden matrix

\[
B=\begin{pmatrix}1&1\\1&2\end{pmatrix}\in SL_2(\mathbb Z)
\]

preserves the **indefinite integer quadratic form**

\[
\boxed{Q(a,b)=2(b^2-ab-a^2),\quad B^T\begin{pmatrix}-2&-1\\-1&2\end{pmatrix}B
=\begin{pmatrix}-2&-1\\-1&2\end{pmatrix}.}
\tag{LC-10}
\]

The form has determinant `-5` and signature `(1,1)`, so a linear real change of basis turns `B` into an honest 1+1 Lorentz boost. Its eigenvalues are `(3±sqrt5)/2=phi^(±2)`; its rapidity has absolute value `2 log phi`, and `cosh eta=3/2`, `tanh eta=sqrt5/3`. The **contracting eigenvalue equals the independently marked Oily fixed point** `q*=phi^-2`. This is exact, source-referenced arithmetic geometry, but `B` was separately chosen as the golden matrix; it has not been derived as a physical BBP carrier update.

In the projective observer action, selecting the same golden rapidity from the balanced frame yields `p_g=(3+sqrt5)/6`. The original total-grade golden mark stays fixed, whereas individual primitive-grade observables move. Example: `Cov(1_(J odd),1_(K odd)) = [1/9-(1+2p)^(-2)(3-2p)^(-2)]/4`, which changes from `7/576` at p=1/2 to **`58/8649`** at the golden rapidity.

**Decisive falsifier:** the actual two-panel Fourier symbol is NOT invariant under the golden torus automorphism. For `p=1/2`, `H(-1,1)=1/4`, but the induced transform by `B` maps the frequency vector `(pi,0)` to `(pi,pi)` and gives `H(-1,-1)=1/9`. The arithmetic Lorentzian form and the authentic positive-source Fourier distribution therefore are **different structures**. In particular source clock `a_n=8n-7`, finite Pascal domains, literal 16-carries and zero-seeded arithmetic phases are not yet equipped with a covariant boost map.

## 5. Authentic source 59-jet in every normalized clock frame

The previous two-full-panel jet is not the correct budget for this experiment. For `m_+/n=p` and `m_-/n=1-p`, set `A=1-z`, `B=1-w`, `C=pA+(1-p)B`, `D=pA(1-A)+(1-p)B(1-B)`, `d=1+C`. Expansion of the genuine four-pole `Q(x)=15x-(59/2)x²+O(x³)` with `a_n=8n-7` gives

\[
\boxed{H_{n,p}(z,w)=d^{-2}+\frac1n\left[-\frac{151C}{120d^3}+\frac{3D}{d^4}\right]+O(n^{-2}).}
\tag{LC-11}
\]

The first source-specific discrepancy with the Gamma-matched fake source `Q_fake(x)=15x` at the same clock and observation law is

\[
\boxed{H_{n,p}^{BBP}-H_{n,p}^{fake}=\frac{59C}{120n d^3}+O(n^{-2}).}
\tag{LC-12}
\]

For fixed p and bounded real z,w in [0,1], the remainder is O(n^-2); the coefficients are smooth in the compact split parameter `0<=p<=1`. This follows by expanding each conditional binomial likelihood to order 1/n and using Gamma(2) exponential tail domination. Independently evaluated exact rational polynomial sums at finite original source times support the coefficients; finite observations themselves are not universal proof.

## 6. Verdict, limitations and the next falsification gate

**Proved (classical plus source specialization):** true projective Lorentz action on the conserved two-observer clock, exact conditional Gibbs tilt and KL, exact integer-lattice Lorentz form associated with `phi^2`, quantitative original-four-pole finite-to-limit bound, original-source 59 first jet and non-invariance of source Fourier symbol.

**Unverified / OPEN:** any intrinsic physical Minkowski metric for SUCC, propagation of physical signals with invariant speed, Lorentz equivariance of the actual selected `U_n(0)`/integer carries, physical heat/work interpretation, and π normality. A formal Lorentz analogy cannot provide a source-selected Weyl estimate by itself: the same posterior/clock family exists for the coherent same-forcing counterseed `s=-pi/16`, whose phases tend to 1.

The next genuine mathematical probe is a *noncentral, intermediate-carry-resolved Fourier correlation* on the tilted two-panel law, with source-normalized proper-clock labels, that predicts different all-N signed bounds for `s=0` and the coherent counterseed. The norm-preserving integer boost is an alternative basis probe, not an authenticated symmetry. Before attempting a physical Lorentz claim, derive the exact transformation of the original native clock and carry cocycle and demonstrate a preserved line element or a valid covariance law under actual arithmetic updates.
