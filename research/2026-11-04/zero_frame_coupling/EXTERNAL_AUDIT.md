# Primary mathematics and the operator-domain test

Bailey and Crandall, *On the Random Character of Fundamental Constant
Expansions*, Experimental Mathematics 10 (2001), DOI
[10.1080/10586458.2001.10504441](https://doi.org/10.1080/10586458.2001.10504441),
[author-hosted paper](https://www.davidhbailey.com/dhbpapers/bcrandom.pdf):
Hypothesis A is an assumption about the zero-started rational-forcing orbit.
The normality consequence does not supply its own hypothesis. Our four-pole
source has the specified rational forcing form, but the required orbit
dichotomy remains unproved here. The new wrong-seed controls do not refute it.

Lagarias, [*On the Normality of Arithmetical Constants*](https://arxiv.org/pdf/math/0101055),
Theorems 3.1, 3.3 and 4.1, separates a general shadowing mechanism from the
narrow arithmetic hypothesis. This supports the audit distinction between
near-exact transport and an actual signed estimate; it supplies no missing
selected cancellation theorem.

The finite differencing proof uses the classical Cauchy/van der Corput
instrument, checked against [Tao's own exposition](https://terrytao.wordpress.com/2008/06/14/the-van-der-corputs-trick-and-equidistribution-on-nilmanifolds/).
Only its classical difference inequality and Weyl criterion are used.
The author's correction to the later nilmanifold sketch is not bypassed or
borrowed as a theorem about this orbit. [Ivrii's endpoint expansion](https://www.math.toronto.edu/ivrii/APM-textbook/Chapter2/L2.3.html)
is a separate classical source for the nonstationary integral instrument;
our sharp constants are rederived with explicit endpoint terms.

Aimino and Rousseau, [*Concentration inequalities for sequential dynamical
systems of the unit interval*](https://arxiv.org/pdf/1406.3213), Sections 2–3,
work with transfer operators on L1/BV and a process defined relative to
Lebesgue measure, under decorrelation and minoration assumptions. Section 5's
martingale/coboundary construction is likewise a measure-theoretic statement.
Such an almost-everywhere or initial-density result cannot identify the
single prescribed seed zero. The author-hosted PDF timed out; the full arXiv
version was read instead. No additional transfer theorem is assumed here.

## An exact source-labelled test of that domain issue

This calculation is elementary and independent of the cited concentration
theorem. For an arbitrary integrable initial density p(s) on the circle, the
composition of the authentic affine maps has the form
`T_n...T_1(s)=16^n s+U_n(0) mod1`. Therefore

\[
\int_0^1 e(hT_n\cdots T_1(s))p(s)\,ds
=e(hU_n(0))\widehat p(-16^n h).
\]

For a periodic BV density, integration by parts against its derivative
measure gives `|p_hat(k)|<=Var(p)/(2 pi |k|)` for k!=0. Thus this **ensemble**
character decays at least as `Var(p)/(2 pi |h|16^n)` independently of the
forcing. The pure seed is a Dirac measure, whose Fourier coefficients have
modulus one; it is not a BV density. Approximating it by narrower densities
does not yield a uniform bound when variation diverges.

This is a successful spectral estimate in its own domain and an explicit
failure of the proposed transfer to the authenticated boundary. It explains
why expansion or a source-covariant transfer operator alone cannot establish
the required single-orbit mean. No external paper is claimed to rule out a
different arithmetic proof.
