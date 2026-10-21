# Bailey–Crandall forcing: sharp coefficient control and honest orbit transport

Date: 2026-10-21. Baseline: PR #232, commit
`9894d39250021bbbc2615c33dee0d286ddf0950f`. Owner: independent BBP lane.

**Mathematical status:** the proofs below are **PAPER_PROVED**.
`formal/duck_pi/BaileyCrandall.lean` is a proof candidate until an actual
pinned compiler run is recorded. No compiler success is inferred from the
six passing Python tests. The identification of the rational series with
`Real.pi` is a **CLASSICAL_IMPORTED** BBP theorem, not a theorem fabricated
as a new Lean axiom. The pi specialization has this premise explicitly.
Pi normality and the required global Fourier cancellation remain **OPEN**.

## 1. Exact source and scope

The source is David H. Bailey and Richard E. Crandall, *On the Random
Character of Fundamental Constant Expansions*, Experimental Mathematics
10 (2001), 175–190, DOI
[10.1080/10586458.2001.10504441](https://doi.org/10.1080/10586458.2001.10504441).
The [author manuscript](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf)
was inspected directly. Its equation (3) specifies the rational forcing and
its BBP formula gives the coefficient identity used here. Theorems 2.1–2.2
are classical asymptotic-perturbation and normality/equidistribution bridges.
Hypothesis A is an unproved dichotomy, not an available unconditional input.

For every **real** x>=1 define

\[
P(x)=120x^2-89x+16,\quad
D(x)=(2x-1)(4x-1)(8x-7)(8x-3),\quad r(x)=P(x)/D(x).
\]

The denominator expands to
`512x^4-1024x^3+712x^2-206x+21`; each displayed factor is strictly positive.
Clearing their nonzero denominators proves

\[
r(x)=\frac4{8x-7}-\frac2{8x-4}-\frac1{8x-3}-\frac1{8x-2}.
\]

This is the shifted BBP coefficient, not the same coefficient with x
replaced silently by x+1. At x=1 it equals 47/15. Thus the base-16 digit
orbit corresponds to the forced orbit's index n+1, or equivalently the
forced index n corresponds to `16^(n-1) pi` for n>=1.

## 2. A stronger, sharp coefficient theorem

For all real x>=1,

\[
\boxed{\frac{15}{64x^2}\le r(x)\le\frac{47}{15x^2}<\frac8{x^2}.}
\]

The upper constant 47/15 is sharp on this domain: equality holds at x=1.
This improves the handoff's constant 8. It does not claim a new academic
priority; it is an elementary new-to-project refinement.

Here are independently checkable polynomial certificates. Put u=x-1>=0.

\[
\begin{aligned}
P(x)&=120u^2+151u+47,\\
47D(x)-15x^2P(x)
 &=22264u^4+42263u^3+26429u^2+5443u,\\
64x^2P(x)-15D(x)
 &=9664u^3+19336u^2+12770u+2783.
\end{aligned}
\]

All coefficients on the right are nonnegative, with positive constant where
needed. Division by the proved positive denominators proves the claims.
The wrong proposed constant 3 is refuted exactly by r(1)=47/15>3.

The integer-step forcing also strictly decreases. The cross-multiplied
difference `P(x)D(x+1)-P(x+1)D(x)` equals

\[
122880u^5+662016u^4+1360896u^3+1330440u^2+620136u+110709>0.
\]

This establishes r(x+1)<r(x), not equidistribution of its forced orbit.

## 3. Analytic tail with all quantifiers explicit

For every natural n>=0 let

\[
t_n=\sum_{k=0}^{\infty}16^{-(k+1)}r(n+k+1).
\]

The terms are positive. Their upper bound
`16^(-(k+1)) (47/15)/(n+1)^2` has a convergent geometric sum, so the original
series is summable and

\[
\boxed{0<t_n\le\frac{47}{225(n+1)^2}\le\frac8{15(n+1)^2}.}
\]

This is an infinite-series comparison theorem, not extrapolation from a
finite prefix. Positivity proves strict positivity from its first term.
Splitting off that term and shifting the remaining **summable** series gives

\[
16t_n=r(n+1)+t_{n+1}.
\]

In particular a partial sum through depth d has the strict enclosure

\[
\sum_{k=1}^d16^{-k}r(n+k)
 <t_n<\sum_{k=1}^d16^{-k}r(n+k)
       +\frac{47\,16^{-d}}{225(n+d+1)^2}.
\]

The non-strict right inequality follows directly from the formal upper
bound and is sufficient for certificates; strictness also follows because
not every coefficient in the comparison attains equality. The executable
interval uses the non-strict enclosing endpoints and never needs this
additional strictness claim.

## 4. A clock-inclusive structural map

Define the unreduced recurrence

\[
y_0=0,\qquad y_{n+1}=16y_n+r(n+1).
\]

Induction using the tail recursion gives the exact real identity

\[
y_n+t_n=16^nt_0.
\]

The skew system is `F(n,x)=(n+1,16x+r(n+1))`. The map
`q(n,x)=x+t_n` genuinely satisfies `q(F(n,x))=16q(n,x)`. This is a
semiconjugacy from a **clock-inclusive** system, not a false claim that the
forced sequence is an orbit of the autonomous map x↦16x.
No stationary probability measure on the incrementing natural clock is
asserted. On R/Z, addition by t_n at each fixed time is a rotation; it
intertwines the nonautonomous cocycle with the autonomous circle multiplier.

Let `seriesValue=16t_0` and let x_n be the image of y_n in R/Z. The exact
identity becomes

\[
16^n\,\mathrm{seriesValue}=y_{n+1}+t_{n+1},\qquad
d_{\mathbb R/\mathbb Z}(x_{n+1},16^n\mathrm{seriesValue})
 \le\frac{47}{225(n+2)^2}.
\]

The circle-distance inequality uses only that the quotient map is
1-Lipschitz. It is independent of the choice of representative modulo one.

## 5. Where the actual pi source enters

Classical BBP supplies

\[
\mathrm{seriesValue}
 =16\sum_{m\ge1}16^{-m}r(m)=\pi.
\]

The pinned mathlib revision is
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Searches for BBP and
Bailey–Crandall found no existing theorem formalizing this identity.
Therefore the Lean declaration `pi_circle_transport` explicitly accepts
`bbp_identity : seriesValue = Real.pi` as a hypothesis; this is an imported
classical **source-identification proof obligation**, not the missing
normality assertion. All earlier forcing, convergence, tail and clock laws
have no such hypothesis. A conditional specialization does not magically
discharge the BBP premise.

`Real.pi` is the actual mathlib constant, defined as twice a cosine zero in
[1,2] in `Mathlib/Analysis/SpecialFunctions/Trigonometric/Basic.lean` and
characterized there by its standard trigonometric theorems. No replacement
constant named pi is used. The missing formal BBP identity remains a source
map gap, while the missing global cancellation is a distinct mathematical
pathway gap.

## 6. What transport buys, and what it cannot buy

For each fixed integer h, the circle character `e(hx)=exp(2 pi i h x)` has
Lipschitz constant 2pi|h|. Since the tail bounds are summable, they imply

\[
\left|\sum_{j<N}e(h16^j\pi)-\sum_{j<N}e(hx_{j+1})\right|
 \le \frac{94\pi|h|}{225}
\]

under the classical BBP source identity. Indeed
`sum_{j>=0}1/(j+2)^2 <= sum_{j>=0}1/((j+1)(j+2))=1`.
Thus any actual cancellation rate for either sequence transfers with a
bounded additive error; the normalized means differ by O_h(1/N).
This character bound is a paper consequence, not currently among the Lean
declarations in this lane.

Neither the rational bounds, positivity, strict decrease, small tail,
semiconjugacy, nor a.e. mixing of multiplication by 16 proves cancellation
for this distinguished orbit. Even a conjugacy of entire systems does not
establish genericity of a chosen initial condition.

The next verdict-changing theorem is an unconditional source-specific
`o(N)` bound for the forced-orbit character sums for every fixed h≠0.
RH or abc has not supplied that estimate in this lane.

## 7. Executable controls and mutation specifications

Run

```sh
python -m unittest discover -s tests -p test_duck_bbp.py -v
```

The six tests passed with exact rational arithmetic. They cover independent
partial fractions versus the collapsed polynomial on small and held-out
large indices; coefficient certificates and monotonicity; nested tail
enclosures against separately evaluated deeper sums; independent Machin
intervals for actual pi; finite shifted-source identities; and malformed
bool/float/rational index rejection. All these are **EXACT_FINITE_CHECK**.

Hostile controls preserve the concrete failures of:

- replacing the sharp coefficient by 3 at m=1;
- replacing the denominator 8m−7 by 8m−6;
- shifting the pi power from `16^(n-1)` to `16^n`;
- erasing r(n+1) and pretending the forced recurrence is autonomous;
- treating a floating or boolean input as an exact integer certificate.

The coordinator owns the actual Lean build, theorem/type/axiom export,
negative elaboration controls and final accepted receipt. A source-level
proof candidate is never promoted merely because these finite checks pass.
