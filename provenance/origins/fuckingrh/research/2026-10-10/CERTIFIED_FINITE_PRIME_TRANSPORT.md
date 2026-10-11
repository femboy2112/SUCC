# Source-certified prime wavefront: exact arithmetic intervals before Gamma

**2026-10-10. Rigorous elementary arithmetic contribution. No RH proof.**

This bounded tool is a concrete bridge from the general observer's
actual causal integer history to the GENUINE prime component of
Suzuki's RH-equivalent correlation kernel, not just an abstract
certificate protocol.

The full Weil/Suzuki form remains UNVERIFIED positive.

## The exact finite object

Let a be a normalized Dirichlet-coefficient source, with a(1)=1,
and let b=log_* a denote its invertible formal Dirichlet-convolution
logarithm. Define

\[
\boxed{
\Psi_{\rm prime,a}(t)=
-\sum_{n\ge2}b(n)\frac{\log n}{\sqrt n}
\bigl(|t|-\log n\bigr)_+.
}
\]

At each finite time t, the sum has finite support: n<=exp(|t|).
For the true source a(n)=1, b(p^k)=1/k and b(n)=0 otherwise.
Thus b(n)log n=Lambda(n) and this IS the exact prime part of
Suzuki Psi, not an approximate prime model.

At a finite observation stage N, the values b(1),...,b(N)
depend only on earlier source events. No coefficient after N
is consulted. If every queried |t| and |t-u| is bounded by M,
the elementary e<3 implies that

\[
\boxed{N\ge3^{\lceil M\rceil}}
\]

is a sufficient (conservative) finite source horizon.

## Exact real arithmetic without floating point

All analytic constants on the prime side are enclosed by
purely rational identities.

For rational x between 1 and 2 set y=(x-1)/(x+1), so
0<=y<=1/3. The real logarithm has the positive
series

\[
\log x=2\sum_{j=0}^{m-1}\frac{y^{2j+1}}{2j+1}+R_m(x),
\]

with exact rational tail bound

\[
\boxed{
0\le R_m(x)\le
\frac{2y^{2m+1}}{(2m+1)(1-y^2)}.
}
\]

Write n=2^k x to reduce each positive integer n
to x∈[1,2). Use the same enclosure for log2 and sum
all intervals with exact Fraction arithmetic. At any fixed
finite stage m, the interval contains the true log n.

For square roots choose integer scaling L=10^P and
d=floor(sqrt(nL^2)) using exact isqrt, giving

\[
\frac{d}{L}\le\sqrt n<\frac{d+1}{L}
\]

unless d²=nL², in which case equality is exact.
Reciprocate the strictly positive bounds to enclose
1/sqrt n with rational endpoints.

For a rational observation time t and an interval
log n∈[l,u], the ramp is enclosed without trying
to guess which side of its kink is active:

\[
\boxed{
(|t|-\log n)_+
\in[\max(0,|t|-u),\ \max(0,|t|-l)].
}
\]

Multiplying the rational enclosures in interval
arithmetic, with the sign of b(n) respected,
produces a RIGOROUS interval for the prime response.

For the two-time prime kernel use interval additions:

\[
K_{\rm prime}(t,u)
=\Psi_{\rm prime}(t)+\Psi_{\rm prime}(u)
-\Psi_{\rm prime}(t-u).
\]

**Important:** this does not yet include the
Gamma/pole contribution. A prime-only Gram may be
negative and still be perfectly consistent with RH.

## Adversarial fake source at 6

At genuine arithmetic, b(6)=0. Insert the
deliberately counterfeit a(6)=2 and keep a(n)=1
elsewhere. The new connected b(6)=1; some later
multiples of 6 also acquire changed connected
coefficients, as formal convolution demands.

For the certified interior window log6<t<log12,
no later changed multiples are active. Hence

\[
\boxed{
\delta\Psi_{\rm prime}(t)=
-\frac{\log6}{\sqrt6}(t-\log6)<0.
}
\]

Unlike the raw value at t=log6 (which is still
unchanged), the first derivative jumps and
the second distributional derivative contains
a negative atom. The module proves the STRICT
negative sign from exact rational bounds, with
no user-supplied decimal threshold or spectral
zero ordinate.

This is a new-to-repo certified arithmetic
component of the general source-to-Weil
intertwining problem. It is not a global
negative Weil witness or a positive Weil theorem.

## Software and next gate

- actualization/source_prime_certificates.py:
  rational logarithm, inverse-square-root,
  prime response, two-time prime correlation,
  certified fake-six source anomaly.
- tests/actualization/test_source_prime_certificates.py:
  independent mpmath holdout calibration
  (only checks correct containment, not proof);
  exact source limits; true and fake probes;
  refusal of floating inputs and missing future
  source events.
- The interval-Gram interface in
  actualization/observer_reflection.py refuses
  uncertified scalar evaluations; its oracle
  provenance must explicitly say PRIME ONLY.

The next worthwhile RH engineering step is to
construct equally rigorous intervals for the
archimedean Gamma+pole term, including its
singular contributions and normalizations,
and then integrate BOTH under a strict,
source-provenance-aware certificate type.
This would make a finite counterexample
search **mathematically sound** without
providing positivity or automatically
proving RH.

The genuinely RH-strength theorem beyond
this instrument is still the global,
source-exclusive positive type of the
COMPLETED prime-plus-Gamma distribution,
not an individual event or arbitrary
Hilbert covariance.

**Status:** elementary enclosure derivations
PROVED; implementation and hostile controls
TESTED; Suzuki full interval oracle NOT BUILT;
RH POSITIVITY UNKNOWN.
