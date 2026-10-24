# Positive Pascal prime charts, literal dyadic differentials, and coherence

**Date:** 2026-10-24. **Parent:** draft #272,
`6e8fa8b77886b13f1f533ed8083fd88c849d14b3`.
**Authority:** paper proofs, inherited authentic source theorems, and a
separately executed exact calibration. **Pi normality remains OPEN.**

This root synthesis develops the late all-prime construction in
[the constructor dossier](PI_TERNARY_CONSTRUCTOR.md). It makes the precise
sense of "bounded differential" and "coherence" explicit. All interpolation
charts below live over the **same dyadic field**. They represent real orbits
in different integer bases; they are not embeddings of different p-adic fields.

## 1. A positive weighted Pascal transform for every base

Use the authentic source and positive measure from the parent:

\[
U_0=0,\quad U_{n+1}=16U_n+r(n+1),\quad
U_n=16^n\alpha-T_n,\quad\alpha=\pi/16,\quad
T_n=\int_0^1t^n\,d\rho(t).
\]

The fixed density has full support and satisfies
\(w(t)\sim t^{-7/8}/32\) at zero and
\(w(t)\sim(1-t)/64\) at one. The dyadic interpolation F satisfies
\(F(n)=U_n\) and
\(v_2(\Delta^jF(z))=\nu(j)=2j-s_2(j)-1\) for all
\(j\ge1,z\in\mathbb Z_2\).

Fix an integer \(q\ge2\). Choose an **odd** positive integer d with
\(q\le16^d\), and set

\[
a=\frac{q-1}{16^d-1},\qquad
P_{q,d}(t)=1-a+at^d.
\tag{C1}
\]

Here \(0<a\le1\), \(P(16)=q\), and \(0\le P(t)\le1\) on the
moment interval. Define the rational source

\[
Y_{q,d}(k)=P_{q,d}(E)^kU_0
=\sum_{j=0}^k\binom kj a^j(1-a)^{k-j}U_{dj}.
\tag{C2}
\]

These coefficients are nonnegative and sum to one. The total coefficient
norm is exactly one, so an absolute error epsilon in every input produces
at most epsilon absolute error in the output, with compatible real lifts.

Finite linearity, not a probability assumption about the source, gives

\[
Y_{q,d}(k)=q^k\alpha-N_{q,d}(k),\qquad
N_{q,d}(k)=\int_0^1P_{q,d}(t)^k\,d\rho(t)>0.
\tag{C3}
\]

The error tends to zero. For fixed q,d, its sharper asymptotic is

\[
\boxed{N_{q,d}(k)\sim\frac1{64a^2d^2k^2}.}
\tag{C4}
\]

Indeed \(P(1-u)=1-ad u+O(u^2)\). The endpoint substitution
\(u=v/(ad k)\), with \(w(1-u)\sim u/64\), gives C4 by dominated
convergence. Every fixed interval away from one has exponentially small
contribution. This includes a=1: then P=t^d and N=T_(dk).
No uniformity is claimed for q or d varying with k.

The derived forcing is positive and completely monotone in real k>=0:

\[
Y(k+1)-qY(k)=\int_0^1(q-P(t))P(t)^k\,d\rho(t)>0.
\tag{C5}
\]

It is rational at integer k and asymptotic to
\((q-1)/(64a^2d^2k^2)\). This does not say it is the original rational
function of its index or that it has the original forcing's dyadic profile.

## 2. An exact all-prime dyadic similarity and derivative

Put \(\delta=v_2(q-1)\). The denominator of a is odd, so
\(v_2(a)=\delta\). Let \(\Delta_d=E^d-1\). The Newton coefficients
in the new time variable are

\[
C_j=\Delta_k^jY(0)=a^j\Delta_d^jU_0.
\tag{C6}
\]

Because d is odd,
\(\Delta_d=d\Delta+\sum_{i=2}^d\binom di\Delta^i\).
Its j-th power has leading term \(d^j\Delta^j\), with integral
coefficients at every higher difference order. Strict increase of nu makes
the leading term uniquely smallest in dyadic valuation. Therefore

\[
\boxed{v_2(C_j)=\nu(j)+j\delta,\qquad
v_2(C_j/j!)=(\delta+1)j-1.}
\tag{C7}
\]

The Mahler series
\(\mathcal Y(z)=\sum_{j\ge1}C_j\binom zj\) consequently converges
analytically on \(|z|_2<2^{\delta+1}\). Finite Newton interpolation gives
\(\mathcal Y(k)=Y(k)\) for all nonnegative integers. The strict increase
in C7 also gives, uniformly on Z2,

\[
v_2(\Delta^j\mathcal Y(z))=\nu(j)+j\delta.
\tag{C8}
\]

Here is a direct proof of the claimed differential, without inferring it from
finite differences. In the falling-factorial expansion, each polynomial
\((z)_j=\prod_{i=0}^{j-1}(z-i)\) has integral coefficients. Its derivative
and its difference quotient are dyadically integral on Z2. The j=1 term has
coefficient \(C_1=aU_d\), of valuation delta because d is odd and F is an
isometry fixing zero. Every j>=2 term has coefficient valuation at least
\(2\delta+1\) by C7. The derivative series converges uniformly. Thus

\[
\boxed{
v_2(\mathcal Y'(z))=\delta,\qquad
v_2(\mathcal Y(x)-\mathcal Y(y))=v_2(x-y)+\delta
}
\tag{C9}
\]

for every z in Z2 and all distinct x,y in Z2.

Define \(H_q=2^{-\delta}\mathcal Y\), using a fixed chosen odd d for
each q. It has the form \(H_q(z)=u_qz+2R_q(z)\), where u_q is a dyadic
unit and R_q is a restricted power series with dyadically integral
coefficients. The correction term \(2R_q\) is at most 1/2-Lipschitz. The equation
\(H_q(z)=y\) has a unique solution by iteration
\(z\mapsto u_q^{-1}(y-2R_q(z))\). The same contraction in the algebra of
restricted power series proves the inverse is analytic on Z2. Therefore:

**H_q is a bijective analytic isometry of Z2, and its derivative is a unit
everywhere.** Equivalently, \(\mathcal Y\) maps \(\mathbb Z_2\) onto \(2^\delta\mathbb Z_2\).

The normalized higher-difference profile is
\(\nu(j)+(j-1)\delta\), not the original nu(j) when delta>0. Normalizing
also changes the represented real constant to \(\alpha/2^\delta\).
Neither distinction can be dropped when relating the charts to real laws.

## 3. Prime charts below sixteen, including a cheap base-eleven target

For q<16, d=1 suffices. Let E denote one original source shift.

| q | Positive Pascal filter | Reduced denominator | delta | Dyadic distance factor |
|---:|---|---:|---:|---:|
| 2 | (14+E)/15 | 15 | 0 | 1 |
| 3 | (13+2E)/15 | 15 | 1 | 1/2 |
| 5 | (11+4E)/15 | 15 | 2 | 1/4 |
| 7 | (3+2E)/5 | 5 | 1 | 1/2 |
| 11 | (1+2E)/3 | 3 | 1 | 1/2 |
| 13 | (1+4E)/5 | 5 | 2 | 1/4 |

This finite list has distortion at most four before normalization; after
normalization every chart is isometric. Larger primes are reached by larger
odd d. We assert an explicit finite factor for each prime, not a uniform
unnormalized inverse bound over all primes.

For base three the result is especially simple:

\[
Y_3(k)=15^{-k}\sum_{j=0}^k\binom kj13^{k-j}2^jU_j,
\qquad
Y_3(k)=3^k\alpha-N_3(k),\quad N_3(k)\sim\frac{225}{256k^2}.
\tag{C10}
\]

Its universal real readout retains an integer lift modulo \(15^k\).
This is a different tradeoff from the minimum-denominator-four filter or the
exponentially accurate denominator-five filter. It has positive weights,
no coefficient amplification, and a fixed dyadic similarity.

Base eleven supplies a useful alternative local symmetry target:

\[
\frac{U_n+2U_{n+1}}3=11U_n+\frac23r(n+1).
\tag{C11}
\]

It uses two original source states and one modulo-3 lift per local sample,
with O(n^-2) real error. The error constant in C4 is 9/256. The coprime
pair 16,11 is eligible for the same inherited rigidity argument as 16,3 or
16,81, provided same-law invariance and the positive all-scale collision
hypothesis are proved. Nothing here shows base eleven is statistically easier.

## 4. Exact coherence of charts

The isometries give an exact, nonempty coherence statement. For any chosen
base charts define

\[
\Phi_{p\to q}=H_q\circ H_p^{-1}.
\]

Then

\[
\boxed{\Phi_{q\to r}\circ\Phi_{p\to q}=\Phi_{p\to r},\qquad
\Phi_{p\to p}=\mathrm{id}.}
\tag{C12}
\]

Every transition is an analytic dyadic isometry with unit derivative. The
identity follows by cancellation of the genuine inverses, and it maps the
normalized same-index source values H_p(n) exactly to H_q(n). These are
constructive source charts because their coefficients were derived from the
fixed rational BBP source in C2 and C6. The coherence identity itself is the
usual identity for changes of coordinates; no novelty is claimed for that
general algebra.

There is no continuous unital field map Q_p to Q_2 for an odd prime p that
could be substituted for these charts: p^n tends to zero in Q_p, while its
forced rational image p^n has 2-adic norm one. The constructions above keep
the dyadic domain fixed and change the real integer-base observation.

## 5. The 16-to-4-to-2 clocks also compose

For the canonical d=1 choices at q=2,4,16, \(\delta=0\) and \(H_q=\mathcal Y_q\).
At q=16, a=1 and P=E, so H_16=F exactly. Define time-respecting maps

\[
C_{16\to4}=H_4\circ[2]\circ F^{-1},\qquad
C_{4\to2}=H_2\circ[2]\circ H_4^{-1},\qquad
C_{16\to2}=H_2\circ[4]\circ F^{-1},
\tag{C13}
\]

where \([m]\) denotes multiplication by \(m\). They obey
\(C_{4\to2}\circ C_{16\to4}=C_{16\to2}\) exactly. The first two
scale dyadic distance by1/2; the last by1/4. They are embeddings into their
corresponding image subsets, not surjections onto all of Z2.

On actual source indices they send
\(U_n\mapsto Y_4(2n)\mapsto Y_2(4n)\). All three real sequences
shadow the same \(16^n\alpha\) at quadratic error. Precisely,

\[
Y_2(4n)-U_n=T_n-N_2(4n)=O(n^{-2}),\qquad
Y_4(2n)-U_n=T_n-N_4(2n)=O(n^{-2}).
\tag{C14}
\]

Thus the dyadic diagram commutes exactly, and the corresponding real source
values agree asymptotically. This is a concrete coherent version of the
binary-power compatibility. It is not an exact identity of real digit words
at every finite source approximation.

## 6. Polynomial base composition has a different boundary

The canonical affine formulas do not multiply by base label:

\[
P_3(t)^2=\frac{169+52t+4t^2}{225}
\ne P_9(t)=\frac{7+8t}{15}.
\tag{C15}
\]

Both evaluate to9 at16, but their first source Newton coefficients have
valuations2 and3 respectively. They cannot be identified as dyadic charts
without the explicit transition map. Commuting products of selected prime
filters do define a multiplicatively coherent polynomial family; every fixed
product stays positive and bounded on the moment interval and gives a real
shadow. Its dyadic differential is not automatically C9 with delta=v2(q-1).
Two such fixed products of the filters in C1, with the same multiplier, have
source values differing by O(k^-2), by C3-C4 and the corresponding product
endpoint expansion. This is a real asymptotic coherence, not polynomial
equality.

An exact scalar fourth-root shift is impossible in this finite-polynomial
setting. Suppose a rational polynomial R satisfied R(E)^4 U_n=U_(n+1)
for every n>=0. Put Q(t)=R(t)^4-t. The source identity first forces Q(16)=0,
since otherwise its exponentially growing term would equal a bounded moment.
Then all moments \(\int t^nQ(t)d\rho(t)\) vanish. Taking their finite
linear combination with the coefficients of Q gives \(\int Q(t)^2d\rho=0\).
Full support forces Q identically zero, impossible because4deg(R) cannot
equal1. This does not obstruct exact digit regrouping of the true real number,
matrix operators, or the commuting chart maps C13.

## 7. Earned result and the remaining real estimate

The bounded dyadic differential, chart coherence, and binary-clock diagram
are proved. The passage from any of them to the conditional real carry
frequencies is unproved. Positive weights in C2 average **unwrapped source
values**; an observable of their sum is not the corresponding average of
observables. The biased binary law in
[the adversarial dossier](PI_TERNARY_ADVERSARY.md) preserves binary shifts,
positive collision dimension and finite carry synchronization while failing
tripling invariance by exactly3/26 on one bit.

The [convex-chart probe](../../scripts/pi_ternary_convex_probe.py) supplies
separate exact finite checks of the formulas, derivatives, chart permutations,
coherence, clock blocking, and the failed stronger polynomial composition.
Its receipt records the actual ranges and hashes. The all-parameter results
rest on the proofs above, not finite data or shared-model agreement.
