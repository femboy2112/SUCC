# Sharp energy-to-interval stability for the swept Borwein instrument

**Status: PROVED PAPER, static observer stability.** This strengthens the
conditional `V^(1/6)` instrument estimate in pinned draft #663 at
`16d04ab58e213e75ab47e61a170138196dbcd292`. The proof below uses our exact
measure-valued inverse and semiconcavity, with **no Erdős–Turán import**.
It supplies no new estimate of V_B for the authentic source and is not
novelty-tax category D or E.

## 1. Objects and exact bound

On the circle with Haar probability m, let mu be any Borel probability and
put

\[
\nu=\mu-m,\quad
L(t)=\frac{162}{289}(\|t\|_{\mathbb T}-1/18)_+^2,
\quad g=L*\nu,\quad V=\int_{\mathbb T}|g(t)|^2dt.
\]

Let D_arc(mu) be the supremum of `|mu(I)-m(I)|` over circle intervals.
Then

\[
\boxed{D_{arc}(\mu)^5\le\frac{144324288}{16807}\,V.}\tag{L2-1}
\]

The exact rational fifth-power bound is the authoritative statement. The exponent 1/5 is optimal among
uniform power-law bounds over circle probabilities. Optimality of the
displayed constant is not claimed.

## 2. Proof from semiconcavity and the exact inverse

First suppose mu has a smooth density. Set

\[
A=\|g\|_\infty,\qquad M=\|g'\|_\infty,\qquad K=324/289.
\]

The distributional identity already proved in BI-1 implies

\[
g''=\frac{324}{289}
(1_{\{\|t\|>1/18\}}*\mu)\,dt
-\frac{288}{289}\tau\mu
\le K\,dt.
\]

Here tau is translation by 1/2. For any point with derivative p>0,

\[
g(x)-g(x-t)\ge pt-Kt^2/2\quad(t\ge0).
\]

At t=p/K, the right side is p^2/(2K), bounded by osc(g)<=2A.
For p<0 use the forward inequality. Taking the maximum absolute derivative
therefore gives

\[
\boxed{A\ge M^2/(4K).}\tag{L2-2}
\]

The mean of g is zero. If M=0, then g=0 and the exact inverse implies
nu=0, so L2-1 is immediate. Otherwise g has a zero; its circle Lipschitz
constant is M. A point where |g|=A is at circle distance at most 1/2 from
some zero. Therefore A/M<=1/2.

At a point x of maximal absolute value, the reverse triangle inequality
gives `|g(x+t)|>=A-M|t|` for |t|<=A/M. These two intervals do not overlap
around the circle except possibly at their endpoints. Integrating the
resulting tent yields

\[
\boxed{V\ge2\int_0^{A/M}(A-Mt)^2dt
=\frac{2A^3}{3M}\ge\frac{M^5}{96K^3}.}\tag{L2-3}
\]

The exact inverse is

\[
(I+P/8)\nu=-\frac{289}{288}\tau g'',
\]

where P is convolution by a probability. Evaluate on intervals. P averages
translated interval errors, and the integral of g'' over an interval is
the difference of two derivative values. Taking the supremum gives

\[
(1-1/8)D_{arc}\le\frac{289}{288}\,2M,
\quad
\boxed{D_{arc}\le\frac{289}{126}M.}\tag{L2-4}
\]

Raise L2-4 to the fifth power and substitute L2-3:

\[
D_{arc}^5
\le\left(\frac{289}{126}\right)^5 96
\left(\frac{324}{289}\right)^3V
=\frac{144324288}{16807}V.
\]

For general mu, convolve it with positive smooth approximate identities.
The resulting g functions preserve the semiconcavity bound and have L2
energy no larger than V. Apply the smooth inequality and pass to weak
limits on intervals whose endpoints are nonatoms. Approaching arbitrary
intervals from inside or outside through such endpoints recovers the full
interval supremum, including atoms. This proves L2-1 for every probability.

## 3. Sharpness: move the mass of a small interval into its center

For an integer H>=1 let epsilon=1/H and let I_epsilon be the centered circle
interval of length epsilon. Define

\[
\boxed{\mu_\epsilon=m-1_{I_\epsilon}dt+\epsilon\delta_0.}\tag{L2-5}
\]

This is a positive probability: its continuous density is zero on the
interval and one outside, and the removed mass epsilon is placed in an atom.
For every interval J,

\[
(\mu_\epsilon-m)(J)=
\epsilon1_{\{0\in J\}}-m(J\cap I_\epsilon)\in[-\epsilon,\epsilon].
\]

Intervals shrinking around 0 approach error epsilon, so

\[
\boxed{D_{arc}(\mu_\epsilon)=\epsilon.}\tag{L2-6}
\]

For nonzero integer h, the Fourier coefficient of nu_epsilon=mu_epsilon-m is

\[
\widehat\nu_\epsilon(h)
=\epsilon-\frac{\sin(\pi h\epsilon)}{\pi h}
=\epsilon(1-\operatorname{sinc}(\pi h\epsilon)).
\]

The identity

\[
1-\operatorname{sinc}(t)
=\int_0^1(1-\cos(tu))du
\]

gives the global bounds

\[
|\widehat\nu_\epsilon(h)|
\le\min\left(2\epsilon,\frac{\pi^2h^2\epsilon^3}{6}\right).
\tag{L2-7}
\]

Use BI-2's upper Fourier gain
`|Lhat(h)|<=81/(289 pi^2 h^2)`. The energy is

\[
V_\epsilon=2\sum_{h\ge1}
|\widehat L(h)|^2|\widehat\nu_\epsilon(h)|^2.
\]

For 1<=h<=H, use the quadratic bound in L2-7. Each product is at most
`(27/578)epsilon^3`, hence the low-frequency contribution is at most

\[
2H\left(\frac{27}{578}\right)^2\epsilon^6
=\frac{729}{167042}\epsilon^5.
\]

For h>H use `|nuhat|<=2epsilon` and
`sum_(h>H)h^(-4)<integral_H^infinity t^(-4)dt=1/(3H^3)`. The remaining
contribution is strictly below

\[
\frac{17496}{83521\pi^4}\epsilon^5
<\frac{216}{83521}\epsilon^5,
\]

where the last step uses pi>3. Thus

\[
\boxed{V_\epsilon<\frac{1161}{167042}\epsilon^5.}\tag{L2-8}
\]

If a uniform inequality D_arc<=C V^beta held with beta>1/5, substitution
of L2-6/L2-8 would imply
`epsilon<=C(1161/167042)^beta epsilon^(5 beta)` along epsilon=1/H ->0,
a contradiction. This proves sharpness of the exponent.

This control is a static probability measure, not an alternate BBP source.
Its role is to test the inverse observer's possible norm exponents.

## 4. Exact original-source finite specialization

Let Vhat_B be #663's rational L2 energy of the terminal rational empirical
measure, and let

\[
\epsilon_B=\frac{16r(2B+1)}{7225B}.
\]

The original positive BBP tail gives
`sqrt(Vtrue_B)<=sqrt(Vhat_B)+epsilon_B`. For any nonnegative rational q_B
with q_B^2>=Vhat_B, L2-1 supplies the completely rational finite certificate

\[
\boxed{D_{arc}(\mu_B)^5
\le\frac{144324288}{16807}(q_B+\epsilon_B)^2.}\tag{L2-9}
\]

This applies simultaneously to every hexadecimal word interval. It can be
vacuous at small B. Neither the construction nor its sharpness control
proves Vhat_B ->0 for the authentic source.

## Verification scope

The rational constant was checked directly with Python Fraction:

```
(289/126)^5 * 96 * (324/289)^3 = 144324288/16807
```

All universal inequalities above have the displayed analytic proofs.
No new broad tests, external source imports, Lean formalization, original
source asymptotic estimate, or hosted-CI execution is claimed by this appendix.
