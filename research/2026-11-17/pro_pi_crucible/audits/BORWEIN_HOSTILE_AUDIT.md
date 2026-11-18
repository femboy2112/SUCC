# Hostile proof audit: the two-pulse Borwein inverse

**Scope and authority.** Read the root's preregistered `research/2026-11-17/pro_pi_crucible/HOLE_CONTRACT.md` and the root's supplied proof candidate. The following is a separate same-model analytic derivation, not external peer review, independent source evidence, a formal certificate, or a claim to have inspected a later final manuscript.

## Verdict

The distributional inverse, the interval-discrepancy constant 34/7, the Fourier coefficient bounds and sign, and the square-root sharpness example all survive the audit. I found no counterexample or load-bearing gap. A spatial inverse does not supply temporal contraction or original-source Weyl saving.

## Distributional constants

Write c=162/289, b=1/18, a=1/2-b=4/9 and L(t)=c(||t||-b)_+^2. At ±b the first derivative is continuous and zero, so there are no delta masses there. At the circle identification t=1/2, the derivative jumps from 2ca to -2ca. Therefore

\[
L''=2c\mathbf1_{\{\|t\|>b\}}dt-\lambda\delta_{1/2},
\qquad \lambda=4ca=288/289.
\]

The total derivative mass is zero because 2c(1-2b)=lambda. For a circle probability mu, nu=mu-Haar has zero mass. If g=L*nu and P is convolution by the uniform probability on the interval of length 1/9 centered at 1/2, translating the preceding identity by 1/2 gives exactly

\[
(I+P/8)\nu=-(289/288)\tau_{1/2}g''.
\]

The half-turn, the plus sign and the factor 1/8 are all necessary. No source phase or chronological operator has been identified with P.

## Semiconcavity and endpoint treatment

Because convolution of the hot indicator with a probability lies between zero and one,

\[
g''\le Kdt,\qquad K=2c=324/289.
\]

First mollify mu with a nonnegative smooth approximate identity. The same inequality holds for the smooth g, while its supremum norm is no larger than Delta=||g||_infinity for the original measure. For g'(x)=v>0, the upper bound g''<=K implies g'(x-s)>=v-Ks for 0<=s<=v/K. Integrating backwards gives

\[
v^2/(2K)\le g(x)-g(x-v/K)\le\operatorname{osc}(g)\le2\Delta.
\]

For v<0, integrate forwards for length -v/K. Thus ||g'||_infinity<=2sqrt(K Delta). The argument works on the periodic real lift even if the chosen integration length crosses a circle boundary.

The interval-discrepancy norm contracts under probability convolution: (Pnu)(I) is the average of translated interval masses nu(I-t). The Neumann inverse of I+P/8 therefore has norm at most 8/7 in this norm. For smooth g, the mass of g'' on an interval is a derivative difference and is at most 2||g'||_infinity. Combining constants gives

\[
D_{\rm arc}(\mu-\mathrm{Haar})
\le\frac{289}{252}\,2\|g'\|_\infty
\le\frac{34}{7}\sqrt\Delta.
\]

For arbitrary mu, pass to the weak mollification limit first on intervals whose endpoints have zero mu mass. Such endpoints are dense. Approximate arbitrary interval choices from the appropriate sides; the continuous Haar contribution has no endpoint ambiguity. Thus the supremum over these continuity intervals equals the full interval discrepancy. This pays the atomic endpoint/jump issue; a naive pointwise g' evaluation at atoms is unnecessary.

## Fourier bounds and sharpness

The inherited exact coefficient equals

\[
\widehat L(h)=\frac{72(-1)^h}{289\pi^2h^2}
 +\frac{81\sin(\pi h/9)}{289\pi^3h^3},\qquad h\ne0.
\]

Using |sin(pi h/9)|<=pi|h|/9 bounds the second term in absolute value by 9/(289 pi^2 h^2). Hence

\[
\frac{63}{289\pi^2h^2}\le|\widehat L(h)|
\le\frac{81}{289\pi^2h^2},\qquad
\operatorname{sgn}\widehat L(h)=(-1)^h.
\]

The circle densities 1+cos(2pi Ht) are nonnegative probabilities. Their discrepancy from Haar is 1/(pi H), and their filtered amplitude is |Lhat(H)|, of order H^-2. This rules out an exponent greater than 1/2 in a uniform power-law inverse estimate at zero. Their signed total-variation norm is 2/pi for every H, so convergence of the filtered functions in C0 does not imply convergence in that norm. If the probability-distance convention uses one half of the signed variation norm, the constant is 1/pi instead. The manuscript should declare which convention it uses.

## Statistical boundary

The inverse differentiates twice and then applies a bounded convolution inverse. Its sharp one-half modulus in interval discrepancy is an instrument-conditioning result. It does not bound the measured original BBP Delta_B as B grows. Fixed periodic or locked measures satisfy the same identity and remain non-Haar. Therefore no contraction of the time evolution, domain-wall density, R0 or full pi normality follows from this inverse alone.
