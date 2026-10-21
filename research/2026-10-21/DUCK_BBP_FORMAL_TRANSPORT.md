# Bailey–Crandall forcing: sharp coefficient control and honest orbit transport

Date: 2026-10-21. Baseline: PR #232, commit
`9894d39250021bbbc2615c33dee0d286ddf0950f`. Owner: independent BBP lane.

**Mathematical status:** 32 declarations in
`formal/duck_pi/BaileyCrandall.lean` at the exact hash recorded below are
**KERNEL_CHECKED** by the pinned Lean 4.14 / mathlib build. Three subsequent
candidates (`tail_lt_half`, `tail_lower_quadratic`, and
`circle_series_distance_eq_tail`) await the next build. The effective cubic remainder and
bounded Fourier-sum correction are **PAPER_PROVED**, independently reviewed,
and are not silently included in that formal count. The eight Python tests
are supporting exact finite checks. The identification with `Real.pi` is
classical BBP; this lane's `pi_circle_transport` retains an explicit source
premise. A separate integral/source lane owns discharging it in Lean.
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

A second, source-sensitive comparison improves this further:

\[
\boxed{\frac{r(n+1)}{16}<t_n\le\frac{r(n+1)}{15}
       \le\frac1{(8n+1)^2}.}
\]

The lower bound follows from the positive remainder in the exact recursion.
The middle bound uses `r(n+k+1)<=r(n+1)` term by term and the geometric sum
1/15. For the last bound, the independent positive decomposition

\[
r(x)=\frac6{(8x-7)(8x-4)}+
     \frac4{(8x-7)(8x-3)}+
     \frac5{(8x-7)(8x-2)}
\]

implies `r(x)<=15/(8x-7)^2`. A separate cleared-denominator certificate is

\[
15D(x)-(8x-7)^2P(x)=3776u^3+5136u^2+2007u+178>0.
\]

The Lean proof uses the polynomial certificate, whereas the exact test
uses the independent positive-fraction decomposition. These constitute two
mathematically different proofs of the upper bound, with elementary
algebra as their shared foundation. The executable `tail_interval` now
uses the sharper remainder `16^(-d) r(n+d+1)/15` while retaining the old
coarse `tail_budget` interface as a valid independent bound. The shifted
bound has leading constant 1/64; no limit theorem is asserted merely from
that one-sided asymptotic upper bound.

### Effective leading term and a genuine boundary on shadowing

The following further estimate is **PAPER_PROVED**, not yet included in the
Lean declarations. For every natural n>=0, write x=n+1. Then

\[
\boxed{-\frac1{480x^3}\le
 t_n-\frac1{64x^2}\le\frac{2783}{14400x^3}.}
\]

For the upper bound, clearing positive denominators in
`r(x)<=15/(64x^2)+2783/(960x^3)` gives the polynomial certificate

\[
(225x+2783)D(x)-960x^3P(x)
 =1279936u^4+2414792u^3+1499906u^2+306607u\ge0.
\]

Apply this coefficient bound at x+k and use x+k>=x. The geometric weights
sum to 1/15. For the lower bound use `r(x+k)>=15/(64(x+k)^2)` and the exact
convexity remainder

\[
\frac1{(x+k)^2}-\frac1{x^2}+\frac{2k}{x^3}
 =\frac{k^2(3x+2k)}{x^3(x+k)^2}\ge0.
\]

The geometric first moment is `sum k*16^(-k-1)=1/225`. Thus the lower error
is `(15/64)*2/(225x^3)=1/(480x^3)`. All comparisons apply to summable
nonnegative series, or to their finite partial sums before taking limits.
This proves `(n+1)^2 t_n -> 1/64`, and hence `n^2 t_n -> 1/64`.

Since `0<t_n<=47/225<1/2`, the distance of the class of t_n to zero on R/Z
is exactly t_n. Consequently the orbit shadowing below has exact circle
distance t_(n+1), with leading term `1/(64(n+2)^2)`. Its O(n^(-2)) exponent
cannot be replaced by little-o(n^(-2)). This is a demonstrated boundary of
the same-source shadowing estimate; it says nothing against pi normality
or stronger cancellation of the orbit itself.

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

A concrete route to discharge this formal source obligation is the uniformly
convergent geometric expansion of

\[
\int_0^1\frac{4-2u^3-u^4-u^5}{1-u^8/16}\,du.
\]

Its integrand is exactly `4u/(u^2-2)-4(u-2)/(u^2-2u+2)`; an antiderivative
on [0,1] is `2 log(2-u^2)-2 log(u^2-2u+2)+4 arctan(u-1)`.
The endpoint logarithms cancel and the arctangent values give pi. Thus the
source obligation splits into a dominated geometric-series interchange,
an elementary rational identity, and a standard fundamental-theorem-of-
calculus evaluation. This reduction is a paper proof, not an undocumented
Lean theorem import. A separate source lane owns its formalization.

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

The eight tests passed with exact rational arithmetic. They cover independent
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

The coordinator owns the combined Lean build, theorem/type/axiom export,
negative elaboration controls and final accepted receipt. A source-level
proof candidate is never promoted merely because these finite checks pass.

## 8. Observed module kernel validation

The hosted run
[39612954095](https://github.com/femboy2112/SUCC/actions/runs/39612954095),
at commit `57a103b7157567fe0fee3c651c5e06794e53703c`, returned exit 0 for
both `BaileyCrandall-build` and `BaileyCrandall-exports`. The checked file's
SHA-256 was
`6746e001303b2ee209b170fc86f9b39e5c3e3692dfd0b152439275cedd66c5af`.
All 32 declaration types were inspected against their paper statements.
Their actual `#print axioms` output lists only `propext`, `Classical.choice`,
and `Quot.sound`; no `sorryAx` or added axiom appears.

The source commit used Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`. Earlier runs
39610936757 and 39612338490 failed elaboration; their errors were repaired,
not counted as successful proofs. The combined third run still failed in
the separately owned BBP integral file. This module-level success must not
be presented as success of that entire run or as an unconditional formal
pi-source identity. The coordinator's final receipt supersedes this
intermediate build observation only after a successful combined build.

An independent same-model referee reconstructed the real-domain polynomial
certificates, infinite positive tail, source-sensitive bounds, shifted
indices, standard BBP HasSum bridge, and cubic remainder. Exact Machin
interval comparison supplies a separate finite source check. Neither is
claimed as an external human referee or an academic novelty verdict.
