# The swept Borwein instrument: exact inverse, sharp stability, and no temporal gain

**Status: PROVED PAPER / quantitative instrument.** The source specialization
below gives finite original-BBP distribution certificates. It does not supply
a decreasing discrepancy, R0, or normality. The local arrangement and explicit
constants are new to this dossier; no external priority is asserted for the
classical distribution, convolution, and interpolation arguments.

## BI-1. Exact measure-valued inverse

Work on the circle R/Z with Haar probability m. Put

\[
c=\frac{162}{289},\quad d=\frac1{18},\quad a=\frac12-d=\frac49,
\quad L(t)=c(\|t\|_{\mathbb T}-d)_+^2,
\quad \bar L=\frac{256}{7803}.
\]

Let mu be any Borel probability, nu=mu-m, and
g=L*nu. Thus g(alpha) is the swept response minus its Haar mean.
Let tau denote translation by 1/2, and let P be convolution by the uniform
probability on the circle interval [1/2-d,1/2+d]. This is an observer kernel,
not a statistical assumption about the source.

Then, as finite signed measures / periodic distributions,

\[
\boxed{(I+P/8)\nu=-\frac{289}{288}\,\tau g''.}\tag{BI1}
\]

The inverse exists on finite signed measures, and

\[
\boxed{\nu=-\frac{289}{288}
\sum_{j=0}^{\infty}(-P/8)^j\tau g'',\qquad
\|\nu\|_{\rm TV}\le\frac{289}{252}\|g''\|_{\rm TV}.}\tag{BI2}
\]

**Proof.** The derivative is continuous at +/-d and has a downward jump
of size 4ca at the antipode. Therefore

\[
L''=2c\,1_{\{\|t\|>d\}}\,dt-4ca\,\delta_{1/2}.
\]

Because nu has mass zero, the constant part of the indicator vanishes after
convolution. Set lambda=4ca=288/289. Translating the resulting equality by
1/2 and using tau squared equal to the identity gives

\[
\tau g''=-\lambda\nu-2c\,(\tau1_{[-d,d]})*\nu
=-\lambda(\nu+P\nu/8),
\]

since 2c(2d)/lambda=d/a=1/8. Convolution by a probability is a contraction
in total variation, so the Neumann series converges in operator norm, with
norm at most (1-1/8)^(-1)=8/7. This proves both statements. For a probability
mu, g'' is a finite signed measure by the displayed derivative formula. □

This is an inverse in the **spatial origin variable**. Iterating its Neumann
series reduces an inversion residual for one fixed measure. It does not
compare the chronological empirical measures at B and 2B.

## BI-2. Every harmonic survives, with explicit conditioning

With Fourier convention fhat(h)=integral f(t) exp(-2 pi i h t) dt, for every
nonzero integer h,

\[
\boxed{\frac{63}{289\pi^2h^2}\le|\widehat L(h)|
\le\frac{81}{289\pi^2h^2},\qquad
\operatorname{sgn}\widehat L(h)=(-1)^h.}\tag{BI3}
\]

**Proof.** The Fourier multiplier of P is real and has absolute value at
most one. Taking Fourier coefficients in BI1 yields

\[
\widehat L(h)=\frac{288}{289}
\frac{(-1)^h}{(2\pi h)^2}\bigl(1+\widehat P(h)/8\bigr).
\]

The last factor lies between 7/8 and 9/8. The constants follow. This also
recovers the inherited formula

\[
\widehat L(h)=\frac{648}{289}\left[
\frac{(4/9)(-1)^h}{(2\pi h)^2}
+\frac{\sin(\pi h/9)}{(2\pi h)^3}\right].
\]

In particular a mode-h error can be amplified proportionally to h squared
by inversion. Nonzero response at every harmonic is not a uniform inverse
from the supremum norm of g to total variation of nu. □

## BI-3. A sharp-exponent bound for every interval frequency

Define

\[
\Delta=\|g\|_\infty,\qquad
D_{\rm arc}(\mu)=\sup_{I}|\mu(I)-m(I)|,
\]

where I ranges over circle intervals. Endpoint conventions do not change
the supremum. Then

\[
\boxed{D_{\rm arc}(\mu)\le
\min\left\{1,\frac{34}{7}\sqrt{\Delta}\right\}.}\tag{BI4}
\]

The exponent 1/2 is optimal uniformly over circle probabilities. The
coefficient 34/7 is an explicit valid bound; optimality of that coefficient
is not claimed.

**Proof.** Positivity of mu and the derivative identity imply

\[
g''=2c(1_{\{\|t\|>d\}}*\mu)\,dt-\lambda\tau\mu
\le K\,dt,\qquad K=2c=\frac{324}{289}.
\]

First smooth mu by a positive circle mollifier. This preserves the inequality
and does not increase Delta. For the resulting smooth periodic g, write
p=g'(x)>0. The upper bound on g'' gives

\[
g(x)-g(x-t)\ge pt-Kt^2/2\quad(t\ge0).
\]

Choosing t=p/K and using oscillation(g)<=2Delta gives
p<=2 sqrt(K Delta). A negative derivative is bounded by the same argument
forward in time. Thus norm(g')_infinity<=2 sqrt(K Delta).

Evaluate BI1 on an interval. Convolution by P takes a weighted average of
translated intervals, so |(P nu)(I)|<=D_arc. The integral of tau g'' is a
difference of two derivative values. Consequently

\[
(1-1/8)D_{\rm arc}
\le\frac{289}{288}\,2\|g'\|_\infty,
\]

and hence

\[
D_{\rm arc}\le\frac{289}{252}\,4\sqrt{\frac{324}{289}\Delta}
=\frac{34}{7}\sqrt\Delta.
\]

Pass to an arbitrary mu by weak convergence of its mollifications. For
intervals with endpoints outside the countable atom set, their masses
converge. Arbitrary intervals are approached from inside or outside by
such intervals, with their lengths converging; these approximations recover
the same supremum, including any endpoint atom. The bound follows. □

**Sharp-exponent / false-positive control.** Let
dmu_H(t)=(1+cos(2 pi H t))dt for any positive integer H. These are positive
probabilities. Direct integration gives

\[
D_{\rm arc}(\mu_H)=\frac1{\pi H},\qquad
\Delta_H=|\widehat L(H)|\le\frac{81}{289\pi^2H^2},\qquad
\|\mu_H-m\|_{\rm TV}=\frac2\pi.
\]

Thus no bound D_arc<=C Delta^beta with beta>1/2 can hold for all
probabilities. The same family proves that the inverse into total variation
is not continuous in the swept response's supremum norm. This is a static
operator control, not a candidate BBP replacement source.

## BI-4. An exact original-source finite certificate

Keep the literal four signed poles and U_0=0. Define

\[
\widehat\mu_B=\frac1B\sum_{k=1}^B\delta_{\{U_{2B}/16^k\}},
\quad
\widehat\Delta_B=\|L*\widehat\mu_B-\bar L\|_\infty.
\]

This is the rational piecewise-quadratic maximum from #657. No floating
digits of pi enter it. For the actual completed shell measure

\[
\mu_B=\frac1B\sum_{n=B}^{2B-1}\delta_{\{16^n\pi/16\}},
\quad \epsilon_B=\frac{16r(2B+1)}{7225B},
\]

the original positive tail and Lip(L)=144/289 prove
norm(L*mu_B-L*muhat_B)_infinity<epsilon_B. Applying BI4 gives

\[
\boxed{D_{\rm arc}(\mu_B)^2
\le\frac{1156}{49}\bigl(\widehat\Delta_B+\epsilon_B\bigr).}\tag{BI5}
\]

The right side is an exactly computable rational. It bounds the square of
the absolute frequency error for every fixed hexadecimal word (its cylinder
is a circle interval), simultaneously at the chosen finite shell. Its square
root bounds the absolute error itself. The bound can be
vacuous at small B; there is no fitted or assumed decay rate.

**Arithmetic boundary.** BI5 is a quantitative consequence of a measured
sweep, not a proof that the sweep decays. All the stationary periodic
measures satisfy BI1–BI4. In particular delta_0 and delta_(1/15) are invariant
under multiplication by 16 and have nonvanishing swept discrepancy. The
contraction P/8 in the inverse therefore cannot be used as a contraction of
the source's evolution. The original-source hypothesis
`widehat Delta_B -> 0` remains exactly the missing full-normality estimate.

## Provenance and falsification

Parent kernel, all-mode equivalence, and original-source tail comparison:
PR #657 at `7e406514ffdd1dac932cdfa6a0e1bf12b8059ebf`,
`research/2026-11-17/causal_clock_scrambling/BORWEIN_SWEPT_IMPULSE_BBP.md`.
The distributional inverse and explicit interval bound above are derived
here, not imported from a numerical experiment.

The exact checker uses interior-point piecewise-quadratic interpolation;
the parent's checker uses endpoint/midpoint interpolation. These are separate
implementations of the same mathematical method, not independent mathematical
witnesses. It compares the resulting maximum with the atom
CDF oscillation and tests the interval-integrated inverse with rational
overlap lengths. Wrong sign, missing half-turn, and wrong coefficient
mutations are required to fail. See TESTS.md and VALIDATION.md for actual
executions; the paper proof supplies the universal quantifiers.
