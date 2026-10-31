# Carrier, Pascal source transport, prime frames and the entire remainder

**Research draft, 2026-10-30.** Exact parent: Universal N/Z PR #417,
`1c6ce7d7ee83a0bd751bde8092e46ff798855fd3`. Main at inspection:
`e18ba565ca540adb7edf3292f5593929e76d91c5`.

This round constructs explicit maps from the general integer carrier to
the authentic source, its analytic family, its prime observations, and its
selected rational first jet. It also proves exactly what a complete
asymptotic/polar observer loses. **Pi base-16 normality and RH remain OPEN.**
The result is a collection of genuine transport/identification theorems and
a new all-order source countermodel, not a new selected Weyl saving.

## 1. The author's carrier-first proposal, realized with explicit types

The universal construction inherited from #417 starts with finite labeled
paths, Pascal grades, and signed integer completion. Mixed grade two
recovers multiplication through
`ab=C(a+b,2)-C(a,2)-C(b,2)`. Localizing nonzero integers produces Q.
The new algebraic carrier is the unit group of `Q[epsilon]/(epsilon^2)`:

    a(1+q epsilon) * c(1+r epsilon) = ac(1+(q+r) epsilon).

Its two coordinates are a rational value and a rational first logarithmic
derivative. All its finite records can be encoded by integer tuples within
the N/Z arithmetic carrier. A finite observer at each finite horizon can
retain the source label, clock, initial jet, required rational precision,
prime components and actual integer carry. This is a mathematical
embedding with a declared update, not a claim about a physical mind or an
automaton with one fixed finite memory bound for all time.

[The explicit carrier and observer construction](CARRIER_REALIZATION.md)
spells out the integer encodings, commuting first-jet update, exact carry
state, and separation between rational finite memory and real completion.

The original BBP realization is exact:

\[
V(a)=\frac{a^4}{(a+3)^2(a+4)(a+5)},\qquad
B_n(u)=\prod_{j=1}^n V(8j-7+u)^{16^{n-j}},\quad B_0\equiv1,
\]

\[
U_n=\left.\partial_u\log B_n(u)\right|_{u=0},\quad U_0=0,\quad
U_n=16U_{n-1}+r(n),\quad
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2}.
\]

The Gamma/Pascal/Fibonacci/Oily construction remains in its established
role. Integer Gamma ranks give literal Pascal coefficients; the authentic
rank-two, unit-clock slice gives the golden/Oily specialization. Those
positive source/observer identities alone do not determine the selected
digit law. The present work extends the source and observation maps instead
of replacing that provenance.

## 2. Pascal is an exact translation law of the authentic analytic source

Let `b=(7,4,3,2)`, `c=(4,-2,-1,-1)` and

\[
a_j(u)=8^{-j}\sum_i c_i(b_i-u)^{j-1},\quad |u|<1.
\]

The complete source Dirichlet family is

\[
\boxed{D(s,u)=\sum_{n\ge1}n^{-s}r_u(n)
=\sum_{j\ge2}a_j(u)\zeta(s+j).}
\]

The initial domain is Re(s)>-1; the right side continues it meromorphically
to the whole s-plane, with explicit geometric bounds for its finite tails
and every finite mixed derivative. Each negative-integer pole has residue
`a_j(u)` at `s=1-j`. The first three residues are

\[
\frac{15}{64},\quad \frac{151-30u}{512},\quad
\frac{1209-453u+45u^2}{4096}.
\]

Changing the source frame is exactly a triangular Pascal operation:

\[
\boxed{a_j(u+v)=\sum_{r=1}^j\binom{j-1}{r-1}
(-v/8)^{j-r}a_r(u).}
\]

These maps compose and invert exactly. The infinitesimal law
`partial_u a_j=-(j-1)a_(j-1)/8` removes the rightmost source pole at each
derivative order. In particular the first source derivative regularizes
the pole at s=-1. This is a concrete finite/Pascal/analytic compatibility
law; the two ordinary parameter derivatives commute, so it introduces no
nonzero curvature merely by being drawn as a two-dimensional diagram.

A common family also reaches the actual BBP endpoint:

\[
\Theta(s,z,u)=\sum_{n\ge1}z^n n^{-s}r_u(n)
=\sum_{j\ge2}a_j(u)\operatorname{Li}_{s+j}(z).
\]

For |z|<1 it is entire in s, and
`Theta(0,1/16,0)=pi/16`. Its convergent z->1 boundary is D on Re(s)>-1.
The original source, rather than just a Gamma-shaped approximation, appears
on both sides. [Complete proof and error bounds](SPECTRAL_SOURCE_TRANSPORT.md).

The user's analytic interpretation of zeta(-1) is preserved. This D is a
**source-weighted Dirichlet function**, distinct from zeta itself. Zeta(-1)
is a regular analytic value; D has a source-specific pole there. No ordinary
divergent-sum equality or negative-half-plane Euler product is asserted.

## 3. Prime weighting acts on that same source, with the correct domain

Unique factorization gives `log n=sum_(p^k|n) log p`. It acts directly on
the common family:

\[
-\partial_s\Theta(s,z,u)
=\sum_{p,k\ge1}(\log p)\sum_{m\ge1}
\frac{z^{p^km}r_u(p^km)}{(p^km)^s}.
\]

Prime dilation scales the **whole pole vector**, not one common source
shift. If `q=p^k`, then `r_beta(qm)=q^-1 r_(beta/q)(m)`; this supplies a
closed arithmetic transport on the enlarged pole-vector carrier. On the
convergent z=1 boundary the same observation is `-sum_j a_j zeta'(s+j)`.
Each shifted zeta Euler product is used only where it converges. There is
no Euler-product claim for the nonmultiplicative BBP coefficients.
[Proof and calibrated prime-power controls](PRIME_WEIGHT_TRANSPORT.md).

## 4. A finite certificate really does identify the four-pole source

The first eight scaled spectral moments are

    0, 15, 151, 1209, 8995, 64905, 461611, 3259089.

Their four-by-four Hankel determinant is **-115200**. An exact linear solve
recovers

    t^4-16t^3+89t^2-206t+168 = (t-7)(t-4)(t-3)(t-2),

then a Vandermonde solve recovers `c=(4,-2,-1,-1)`. This proves uniqueness
among sources `sum_i c_i/(8n-b_i)` with at most four distinct simple poles,
no polynomial part, fixed clock 8, and the declared pole domain. The pole
locations need not be supplied to
the reconstruction. The class hypothesis does essential work.

The negative determinant also prevents confusing this signed source
moment certificate with a positive covariance or a Weil-positive form.
This is exact finite source authentication. It does not by itself estimate
the future selected signed sum.

## 5. Complete polar data still lose an entire remainder

For any prefix M and depth K, the explicit construction in
[ALL_ORDER_SHADOW.md](ALL_ORDER_SHADOW.md) changes the source after M and
has all of the following properties at once:

- positive rational forcing and the literal zero initial seed;
- exact agreement of the original source and orbit through M;
- arbitrarily small uniform relative source error as K increases;
- equality of **every** inverse-power asymptotic coefficient;
- equality of **every** spectral pole and residue, including all source-shift
  derivatives of those residues;
- a rational completed boundary and a proved nonnormal selected orbit.

The simplest member is already explicit:

\[
\widetilde r(n)=r(n)-16^{-n}r(2n)-16^{-n-1}r(2n+1).
\]

Its completed boundary is `47/240`, and its literal carries are exactly
`3,2,2,2,...`. Its Dirichlet function differs from the original by a
nonzero **entire function**. Regular Laurent finite parts and the full
analytic germ change; the polar part does not.

This does not contradict the finite reconstruction theorem: the modified
sequence is outside the fixed finite-pole rational-function class. It
sharpens the old finite-jet controls to a single source agreeing at every
asymptotic order. It gives a useful new requirement for the proof program:
retain the full source law or bound its missing entire part at the actual
selected phase; more polar moments alone do not do that in a larger class.

## 6. Prime values can recover the selected derivative through rational frames

Fixed values B_n(0), even with every prime valuation, miss a changed initial
derivative. The repair is an actual two-frame observation:

\[
A_{n,M}=M\log\frac{B_n(1/M)}{B_n(0)}
=M\sum_p[v_p(B_n(1/M))-v_p(B_n(0))]\log p.
\]

Both sampled values are positive rationals. Complete monotonicity of the
authentic source proves, for every n,M>=1,

\[
\frac{38447}{44100}\frac{16^{n-1}}{2M}
\le U_n-A_{n,M}\le
\frac{6853}{1800}\frac{16^n-1}{30M}.
\]

Choosing the explicit diagonal `M_n=16^n n^2` makes the phase errors
summable. For each fixed integer h, its unnormalized Weyl sum differs from
the original by at most `6853*pi^3*|h|/162000`, uniformly in the horizon.
This is a fully declared prime-to-real selected transport, without an
unpaid exchange of time and precision limits. It is still an equivalent
cancellation target, not an asymptotic saving for either sum.

Centered frames improve the state error from order `16^n/M` to
`16^n/M^2`. The forward rule requires O(n) bits of frame-spacing precision;
it is not an exponential bit-complexity lower bound. Rational log enclosures
certify the test cases without floating point.
[Proof, sharp constant, controls and carry seam](PRIME_FRAME_TRANSPORT.md).

## 7. What the observer must keep

All prime additive principal parts recover a rational first jet modulo Z.
The literal carry additionally needs the source's integer part and the
integer seam in the sum of local representatives. For the first authentic
step, `r(1)=47/15` has local parts `1/3` and `4/5`: all local carries from
zero vanish, but their seam and source integer remainder give carry 3.
Dropping those integers gives a wrong observable.

Every fixed finite set of prime precisions admits rational seed aliases
with identical retained observations for the entire future and different
real phases. This concerns observer sufficiency, not different normality
of rational translates. The irrational coherent seed `-pi/16` belongs to
a separately declared real extension; it is not a diagonal rational point.

[SOURCE_AUTHENTICATION.md](SOURCE_AUTHENTICATION.md) also completes the
weighted rational-summability criterion at every pole order and supplies
a four-simple-pole, integer-log-potential, rank-two-matched nonnormal
control. This separates exact authentic source membership from generic
architecture even within rational log-jet carriers.

## 8. Research verdict and navigation

The new frame dominates the fixed-value/leading-rank/polar-only observers
for source identification and selected-state transport. It also exposes
their precise kernels and quantitative resolution costs. It does not
dominate the existing selected finite-band program as a cancellation proof.

The remaining hard statement is still

    sum_(n<=N) exp(2*pi*i*h*U_n(0)) = o(N)
    for every fixed nonzero integer h.

The source-specific common-basis maps now make new hypotheses testable;
they do not supply this inequality. No number of successful finite probes
promotes it to a theorem. See [claims and scope](CLAIMS.md),
[review of the incoming work](INCOMING_AUDIT.md), [validation](VALIDATION.md),
[final proof review](FINAL_REVIEW.md), [initial contract](HOLE_CONTRACT.md),
and [next exact target](NEXT_HANDOFF.md).
