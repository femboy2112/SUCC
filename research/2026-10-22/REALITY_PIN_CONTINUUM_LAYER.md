# Reality Pin: a constrained continuum line earns its length

**Status:** PROVED within the constant-coefficient continuum family below;
certified rational interval controls; no empirical measurements, no Lean
admission and no general inverse-PDE or spacetime claim. **Date:** 2026-10-22.
Classical diffusion/RC line theory and elementary hyperbolic analysis; no
academic novelty claimed.

## 1. Source contract and boundary response

Fix a homogeneous line with coordinate `x in [0,L]`, length `L>0`, constant
conductivity `a>0`, and capacitance density `c>0`. Boundary voltage is `v`
at `x=0`, while `x=L` is grounded. With zero initial state, the real Laplace
parameter `s>0` gives the ODE and measured inward current

\[
a u''=csu,\qquad u(0)=v,\quad u(L)=0,\qquad I=-a u'(0).
\]

The coordinate, current orientation, termination and meanings of `a,c,L`
are part of the source passport. Setting `q=sqrt(cs/a)>0`, the unique
solution is

\[
u(x)=v\frac{\sinh(q(L-x))}{\sinh(qL)},\qquad
\boxed{Y(s)=I/v=\sqrt{acs}\,\coth\!\left(L\sqrt{cs/a}\right)}.
\]

The static solution `u(x)=v(1-x/L)` gives `Y(0)=g=a/L`. Both formulas agree
in the `s downarrow 0` limit. Existence and uniqueness follow directly from
the two linearly independent exponential ODE solutions and `sinh(qL)>0`.
The sign convention gives positive input conductance. Reversing the measured
current without changing the model orientation would negate the response.

The complete positive-Laplace response depends only on two invariants:

\[
g=\frac aL,\qquad \tau=\frac{cL^2}{a},\qquad
Y(s)=g h(\sqrt{\tau s}),\qquad h(z)=z\coth z.
\]

These are a genuine continuum family and an actual boundary map, not a finite
matrix relabelled as a continuum. The model presupposes homogeneous
coefficients, known ground termination and no extra boundary impedances.

## 2. One dynamic observation after DC, with independently known capacity

**RP-L1 — homogeneous continuum rigidity (PROVED).** If `c` is independently
known, then exact `g=Y(0)>0` and **one** exact response `Y(s)` at a declared
`s>0` uniquely determine `L` and `a` within the above family.

**Proof.** The ratio `r=Y(s)/g` satisfies `r=h(z)`, where
`z=L sqrt(cs/a)>0`. Elementary differentiation gives

\[
h'(z)=\coth z-z\operatorname{csch}^2z
=\frac{\frac12\sinh(2z)-z}{\sinh^2z}>0.
\]

The strict inequality follows from `sinh(t)>t` for `t>0`: integrate
`cosh(t)>1`. Also `h(0+)=1`, and `h(z)>z` makes `h(z)->infinity`.
Consequently `h:(0,infinity)->(1,infinity)` is a strictly increasing
bijection. Solve its unique inverse `z=h^{-1}(r)`. Because
`z^2=cLs/g`, the parameters are

\[
\boxed{L=\frac{g z^2}{cs},\qquad a=\frac{g^2 z^2}{cs}.}
\]

Thus every claimed pair is determined by the data and independently fixed
capacity density. QED. Values `r<=1` contradict this strictly positive
finite-line model, unless observational uncertainty spans the permitted
range. The executable conservatively requires its entire ratio interval
above one.

The reconstructed line predicts every further response. Reserving a second
positive-Laplace reading as a holdout tests the homogeneous model rather
than merely repeating the two calibration equations. A real positive
Laplace response is not a single AC sinusoidal measurement; a suitable
calibrated time-domain protocol or other justified acquisition map is an
additional experimental obligation.

## 3. Quantified inverse sensitivity

**RP-L2 — conditioned stability (PROVED).** On a predeclared interval
`0<z_min<=z<=z_max`, write `d=h'(z_min)>0`. Then

\[
|z-z'|\le |r-r'|/d.
\]

For the same exact `g,c,s`,

\[
|L-L'|\le\frac{2g z_{\max}}{csd}|r-r'|,\qquad
|a-a'|\le\frac{2g^2 z_{\max}}{csd}|r-r'|.
\]

**Proof.** Since
`h''(z)=2 csch^2(z)(z coth(z)-1)>0`, its derivative is increasing.
Here `z coth(z)>1` follows from `tanh(z)<z`, obtained by integrating
`sech^2(z)<1`. The mean-value theorem gives the inverse bound; factor
`z^2-z'^2=(z+z')(z-z')` for the parameter bounds. QED.

This is a conditioned bound: `h'(z)->0` as `z->0`, so near-DC measurements
become poorly informative about length. It assumes exact independently fixed
`g,c,s`. Calibration uncertainties in those inputs must also be propagated;
they are not silently absorbed into `r` or declared zero for a real device.
The finite rational oracle produces inclusion intervals, not statistical
confidence levels.

For its forward error budget, `0<h'(z)<1` also holds. To prove the upper
inequality, set `E=e^(2z)`; it reduces to `1-e^(-2z)<2z`, which follows by
integrating `e^(-t)<1` on `(0,2z)`. Thus the ratio map is 1-Lipschitz,
which controls propagation of a rational square-root enclosure.

## 4. Exact surviving family when capacity is unknown

**RP-L3 — full-response scaling obstruction and fiber (PROVED).** If `c`
is not independently fixed, then for every `k>0`

\[
(a,c,L)\longmapsto(ka,c/k,kL)
\]

leaves the **entire** response `Y(s)` unchanged. Therefore arbitrary-precision
boundary data cannot select a physical length in this unrestricted family.

**Proof.** Both `g=a/L` and `tau=cL^2/a` are invariant under the displayed
scaling. Conversely equality of complete responses implies equality of
`g` by the DC limit and equality of `tau` by any one positive-`s` reading
and injectivity of `h`. If `k=L'/L`, equality of `g` gives `a'=ka`, and
equality of `tau` gives `c'=c/k`. Hence the response fiber is **exactly**
this one-parameter positive scaling orbit. QED.

This is stronger than saying that the proof failed: the complete ambiguity
family has been characterized. If a known spatial unit makes distinct
lengths physically inequivalent, these models are observational aliases;
if the declared physical equivalence treats that coordinate scaling as gauge,
the response uniquely selects the gauge class. The choice is explicit.

**Wrong-passport example.** `(a,c,L)=(2,3,4)` and `(1,6,2)` have identical
entire response. Assuming capacity 6 when the source has capacity 3 returns
length 2 instead of 4, with every passive boundary holdout still passing.
Independent capacity calibration is therefore load-bearing, not a cosmetic
extra measurement. With `c=3` fixed, DC alone likewise fails: `(2,3,4)`
and `(3,3,6)` share `g=1/2` but have different dynamic responses.

## 5. Sound rational oracle and actual controls

For rational `x>=0`, let `S_N=sum_(j=0)^N x^j/j!` with `N>=1`. When
`q=x/(N+2)<1`, the remaining Taylor terms obey

\[
S_N\le e^x\le S_N+\frac{x^{N+1}/(N+1)!}{1-q}.
\]

**Proof:** the first omitted term is explicit; each subsequent ratio is at
most `q`, so the omitted series is bounded by a geometric series. There is
no floating-point transcendental call in the certificate.

For `z>0`,

\[
h(z)=z\frac{E+1}{E-1},\qquad E=e^{2z},
\]

which decreases as `E` increases. Substituting the exponential enclosure
in reversed order gives a rigorous ratio enclosure. Because the Taylor
lower bound is at least `1+2z`, an exponential interval of width at most
`2z epsilon` produces a ratio interval of width at most `epsilon`.

The inverse oracle uses two trial points at one-third and two-thirds of
its current bracket. It refines their rigorous ratio intervals until they
are disjoint, then discards a certified exterior part. Strict monotonicity
proves that the separation refinement terminates, and each successful step
reduces bracket width by at least a factor `2/3`. This avoids assuming an
exact-equality decision at a single midpoint. The exponential oracle has an
explicit 512-term budget; exhaustion raises an error and emits no false
certificate. No claim of unlimited computation is made.

`line_response_interval` first brackets `sqrt(tau s)` by rational bisection.
The `h'<1` bound and endpoint ratio intervals yield the requested total
response width. `known_capacity_pin` inverts the endpoints of a calibrated
ratio band and transports the resulting inclusion interval through the exact
parameter formulas. Its returned physical-authentication flag is always false.

**Executed scope:** `tests/test_reality_pin_continuum.py` contains eight
small exact tests: exponential sandwich; certified ratio/monotonicity;
inverse bracket; synthetic known-capacity reconstruction and held-out scale;
exact scaling invariants; wrong-capacity alias; DC insufficiency; and input/
precision-budget rejection. For `(2,3,4)`, `s=1/24` gives `z=1` and

\[
1.313035<h(1)<1.313036.
\]

The independently reserved scale `s=1/6` gives `z=2` and

\[
1.037314<Y(1/6)<1.037315.
\]

These decimals abbreviate exact rational outer brackets in the tests. They
are synthetic predictions, not measured voltages or currents.

## 6. Attribution and exact boundary

The diffusion/RC source interpretation is classical; the ODE solution,
injectivity, scaling fiber and oracle bounds are fully derived here.
Primary references inspected:

- MIT, *Electromagnetic Fields and Energy*, section 14.9,
  [Charge Diffusion Transmission Line](https://web.mit.edu/6.013_book/www/chapter14/14.9.html).
- NIST DLMF [§4.28](https://dlmf.nist.gov/4.28),
  [§4.34](https://dlmf.nist.gov/4.34), and
  [§4.35](https://dlmf.nist.gov/4.35), for hyperbolic definitions,
  derivatives and identities.

**PROVED:** restricted continuum rigidity with independent capacity; conditioned
stability; exact unknown-capacity ambiguity fiber. **EXACT FINITE TESTED:**
the rational enclosures and synthetic controls. **UNVERIFIED:** source
homogeneity, actual instrument access, physical capacity calibration,
variable-coefficient inverse problems and physical spacetime interpretation.
The next verdict-changing probe is an independently calibrated capacity
measurement plus a genuinely reserved dynamic holdout on an actual line.
