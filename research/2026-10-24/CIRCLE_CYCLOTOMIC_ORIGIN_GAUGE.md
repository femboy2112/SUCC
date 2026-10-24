# Circle Origins, Cyclotomic Torsion and Source-Selected π
## A proof-bearing reference-frame audit for Observational SUCC — 24 October 2026

**Parent:** source-certified π Source Genesis draft PR #253, observed head
2ab8a8527b7ba3f990d75fd618a4bfd034b26b4b. Sibling #254
is a separately proven Green-rank/coefficient research front, not
automatically imported. Original corrected BBP source PR #252 and
Academic Main IX draft #250 remain ancestors.

**Status:** exact group/number-theory and finite rational identities with
paper proofs and independently executable controls; no new Lean
declarations in this branch. Classical covering, Fourier, Möbius
inversion and projective geometry properly attributed.
**π normality OPEN in every base. Scholarly novelty UNVERIFIED.**

## Initial geometric distinction: two ways to make a circle from a line

The circle is both R/Z (identify integer translates, equivalently
identify the two ends of [0,1]) and homeomorphic to the ONE-POINT
compactification R union {infinity} (stereographic chart). These
topologies agree after a coordinate choice; their ADDITIVE operations
and canonical number-theory interpretation do not become identical.
In the projective chart s=tan(pi*x) ∈ R ∪ {infinity}, the excluded
pole x=1/2 is chart-infinity, not an arithmetic infinite integer.
For finite s=tan(pi*x), t=tan(pi*y),

    |exp(2pi i x)-exp(2pi i y)|²
       =4(s-t)²/[(1+s²)(1+t²)].

Changing a circle origin by angle a with tau=tan(pi*a) acts on
chart coordinates by the MOEBIUS map (s+tau)/(1-s*tau).
Its Euclidean coordinate difference can blow up near the pole;
the intrinsic circle chord is bounded by 2. This is a CHART
distinction, not an exotic physical singularity.

The source problem requires a marked origin, a unit-turn calibration,
a base-b covering and a specified π-selected starting point.
An arbitrary origin is a lawful frame only if the dynamics and
observable are transformed with it.

## OGC-01. The exact origin covariance law (CLASSICAL / PROVED PAPER)

Write T_b(x)=b*x mod1 on T=R/Z and R_a(x)=x+a.
T_b is a degree-b expanding covering, NOT an isometry for b>1.
For a new reference origin a, the *same dynamical system* is

    T_b^(a):=R_(-a) o T_b o R_a,
    T_b^(a)(x)=b*x+(b-1)*a mod1.

Its dth iterate is
    (T_b^(a))^d(x)=b^d*x+(b^d-1)*a mod1.

Define the ORIGIN COVARIANCE DEFECT, a semigroup cocycle,
    H_d(a)=(b^d-1)*a mod1,
    H_(d+e)(a)=H_d(a)+b^d*H_e(a) mod1.

This is a precise failure of commuting an origin rotation past
an unmodified covering. T_b is noninvertible, so H_d is called
a covariance/cocycle defect, not an invertible group commutator
or a physical gauge-field holonomy.

**Lawful coordinate relabeling**: transform both T_b and every
observation. The physical trajectory remains the same; no
statistical conclusion follows from the tautological equivalence.

**Different physical initial points**: leave T_b fixed and replace
x by x+a. Those are distinct trajectories, not merely the same
SUCC history in another chart.

## OGC-02. Exactly which "inertial origins" commute? (PROVED PAPER)

R_a commutes with the unchanged T_b if and only if
    (b-1)*a=0 in R/Z.

There are precisely b-1 such rotations, the finite group
(1/(b-1))*Z/Z. For b=16 these are a=k/15, 0<=k<15.
Every one obeys T_16^j(x+a)=T_16^j(x)+a, so

    A_(h,N)(x+a)=exp(2pi i h*a)*A_(h,N)(x).

ALL FIFTEEN frames have EXACTLY THE SAME Fourier magnitude.
Yet their COMPLEX averages satisfy
    (1/15)sum_(k=0)^14 A_(h,N)(x+k/15)=0
    whenever 15 does not divide h, for EVERY x,N.

Even the fixed point x=0 appears to have "cancellation" if
one illicitly replaces a fixed selected trajectory by this
ensemble of fifteen reference origins. The false inference
is exposed with an exact character-orthogonality witness.

## OGC-03. Strong finite-time instability, despite bounded chord

Given ANY x and horizon n>=1, take y=x+1/(2*b^n) mod1.
Then intrinsic initial circle distance is 1/(2*b^n), but

    d_T(T_b^n x,T_b^n y)=1/2.

Thus there is NO horizon-uniform modulus of continuity for
the unmodified expanding dynamics as an intrinsic map of
initial states. Each fixed-time map is continuous; uniform
continuity over the family of all times fails. The circle
diameter supplies the trivial bound <=1/2, not an estimate
forcing differential errors to vanish as horizons grow.

## OGC-04. An exact UNIFORM averaged-frame differential bound

For h !=0 and the normalized Weyl amplitude

    A_(h,N)(x)=N^-1 sum_(j=0)^(N-1)e(h*b^j*x),

Haar-average over a SINGLE COMMON translated origin a:
    int_0^1 |A_(h,N)(x+a)-A_(h,N)(y+a)|² da
      =N^-2 sum_(j<N)|e(h*b^j*(x-y))-1|²
      <=4/N.                                               (D)

Proof: expand the square and integrate in a. Distinct
integer frequencies h*b^j are Haar-orthogonal, so ALL
off-diagonal j!=k terms vanish identically.

For b=16, x=0, y=1/3, h=1, each squared chord is
exactly 3, hence the Haar-averaged differential is 3/N.
But at the specific frame a=0 the two amplitude values
are 1 and e(1/3), so their squared differential is
exactly 3 for ALL horizons.

**The user intuition survives as a real theorem in
AVERAGED origin sampling, but fails for any claimed
uniform bound at the privileged π-selected origin.**

A related exact identity for each x:
    int |A_(h,N)(x+a)|² da =1/N,
    int A_(h,N)(x+a)da =0.
These hold even when A_(h,N)(x)=1 and the selected orbit
is nonnormal. The distinction is "almost every or ensemble"
versus "one source-pinned trajectory."

## OGC-05. Finite origin-frame probes and exact source tomography

For a finite grid a_r=r/m, 0<=r<m, define

    G_(h,N,x)(a)=A_(h,N)(x+a).

At a grid character h*b^k, discrete Fourier orthogonality
gives the exact coefficient

    (1/m)sum_(r<m) G_(h,N,x)(r/m)*e(-h*b^k*r/m)
       = e(h*b^k*x)/N

provided all the source frequencies h*b^j (0<=j<N)
are DISTINCT modulo m. This gives a faithful finite
phase-history reconstruction from the entire origin
response signal. It does not authenticate an external
physical device or provide the samples for free.

A sufficient exact arithmetic condition is
    gcd(m,b*h)=1 and ord_m(b)>=N.
There must be at least N distinct sample labels,
so necessarily m>=N. A uniform origin average
without the NONZERO character channels instead erases
all the selected source phases.

The exact source-free spatial second moment is

    (1/m)sum_(r<m)|G_(h,N,0)(r/m)|²
     =N^-2 sum_(j,k<N) 1[m divides h*(b^j-b^k)].

It equals 1/N when no character aliases occur.
For the separate origin-cocycle characters
e(h*(b^j-1)*a), j=1..N, the identical formula
holds with labels h*(b^j-1).

**Concrete hexadecimal root clocks:**
m=7 has ord_7(16)=3, so 3 holonomy frames have
mean-square energy 1/3; m=15 has order 1 and
energy 1; m=17 has order 2 and energy 5/9.
"Use several correlated starting points" is useful only
after checking actual modular character separation.

## OGC-06. Why cyclotomic factors are EXACTLY the frame defect

For d>=1, the rotations invisible to T_b^d are

    ker(T_b^d-I)
      ={k/(b^d-1):0<=k<b^d-1}.

The kernel contains exactly b^d-1 points. Therefore the
same integers factoring as

    b^d-1=prod_(e|d)Phi_e(b)

classify permissible periodic origin gauges and alias
frequencies in the d-step covariance problem. The
actual signed π lag phase is the source orbit's
evaluation of the very same cocycle:

    e(h*(b^d-1)*b^j*pi).

However, cyclotomic VALUES are not counts of exact
minimal-period points. Let P_b(d) be the number of
points whose MINIMAL T_b period is exactly d. Since
Fix(T_b^d) is the disjoint union of all exact periods
e dividing d,

    b^d-1 = sum_(e|d) P_b(e),
    P_b(d)=sum_(e|d) mobius(d/e)*(b^e-1).

The number of primitive cycles is P_b(d)/d.
For b=16:
    P_16(1)=15,  P_16(2)=240, P_16(3)=4080,
    Phi_2(16)=17, Phi_3(16)=273.
Prime factor source, torsion structure, and
dynamical primitive-period count are RELATED
but categorically distinct functors.

## OGC-07. EXACT SHARP EXCEPTION: a full-period orbit tends to δ0

Fix b>=3 and integer d>=2. Set m=b^d-1.
The selected x_d=1/m has MINIMAL period d under T_b,
because no positive j<d has m dividing b^j-1.
Its complete orbit is

    {b^j/m:0<=j<d} (no modular wrap for this range).

Let nu_d be its TIME empirical measure over that period.
Then, on the circle geodesic metric,

    W1(nu_d,delta_0)
      = (1/d)sum_(j<d)b^j/m
      =1/[d*(b-1)]  -->0.                           (E)

All those selected orbits have MAXIMAL allowed finite
period d and nevertheless converge in distribution
to the non-Haar point mass delta_0.

On the other hand the FULL SPATIAL group of m origins
has exact W1 distance to Haar
    W1(uniform m-gon,Haar)=1/(4m) -->0.              (F)

Indeed this whole origin group consists of points with
T_b^d(a)=a, so its distribution is perfectly
compatible with the period-d covering symmetry.

For any integer h!=0 with m>|h|, its spatially averaged
time Fourier sum is EXACTLY ZERO:

    (1/m)sum_(r<m)A_(h,d)(r/m)=0.

Yet the selected FULL-PERIOD orbit of x_d satisfies

    |A_(h,d)(x_d)-1|
       <=2*pi*|h|/[d*(b-1)]  -->0.                  (G)

Thus the SAME origin-closed system exhibits:
 - exact finite spatial Fourier cancellation;
 - arbitrarily long selected deterministic cycles;
 - a selected time orbit arbitrarily far from Haar
   (approaching the fixed point delta_0);
 - near-maximal selected Fourier amplitude.

This is a completely explicit quantified negative control
to "circle symmetry + many origins + long SUCC paths ⇒
one selected source must be normal." It does not disprove
π normality. It locates the missing selection theorem.

## OGC-08. π-pinned periodic cyclotomic shadows (EXACT FINITE)

For actual source x={π}, let m=b^d-1 and choose the
nearest grid point k_d/m. The source-independent
rounding theorem gives intrinsic initial error
<=1/(2m). For j<d, the forward pointwise error
is bounded by b^j/(2m). Thus any prescribed
fraction of the d-step orbit can be shadowed with
exponentially small phase errors by a PERIODIC
rational orbit, even when the underlying selected
point is π.

The executable source selector refuses ambiguous
π intervals and requires independent source-certified
polygon bounds (not floating π input). It constructs
actual finite π periodic fakes and pays the error.
Their existence says nothing about the infinite
selected π trajectory.

## OGC-09. The BBP forcing is exactly a MOVING-ORIGIN connection

For the AUTHENTIC BBP tail t_n of PRs #252/#253:

    16*t_n = r(n+1)+t_(n+1).

Define the absolute phase z_n={y_n+t_n},
where y0=0 and y_(n+1)={16*y_n+r(n+1)}.
The arbitrary time-dependent origin connection
has exact coordinate law

    y_(n+1)=16*y_n+[16*t_n-t_(n+1)] mod1.

Thus **the actual forcing is the moving-origin
cocycle** 16*t_n-t_(n+1)=r(n+1), not an arbitrary
static pole->circle state collapse.

The source selects z0=t0=π/16, whence
    z_(j+1)={16^j*pi}.

Among BOUNDED real solutions of the backward
difference equation t_n is unique. It is not a
rational-function-of-index coboundary; there is
no contradiction because the moving gauge lives
in a different, source-authenticated function space.

For a finite depth K let
    t_n^K=sum_(k=1)^K16^-k*r(n+k).
Then the exact finite source residual is

    16*t_n^K-t_(n+1)^K-r(n+1)
        =-16^-K*r(n+K+1).

The code proves this using rational arithmetic
and rejects changed index and origin mutants.

**NEW finite source boundary budget.** For an
N-step lag d, with L=N-d>0,
the signed phase difference between true π
and authentic BBP forced lag histories is
t_(j+d+1)-t_(j+1) <=0. Its positive accumulated
magnitude is an exact telescoping BOUNDARY:
    sum_(j=0)^(L-1)(t_(j+1)-t_(j+d+1))
      =sum_(n=1)^min(d,L) t_n
       -sum_(n=max(d,L)+1)^(d+L) t_n.

Every term admits the BBP rational tail
enclosures from the parent source; the resulting
rigorous complex signed-lag comparison is at most
2*pi*|h| times this boundary, with pi<22/7
for a fully rational computable upper bound.
This is source-specific uniform-in-lag transport
but NOT a cancellation estimate for either sum.
It refines the finite-boundary presentation of
the lag transport already formalized in #253.

## OGC-10. The actual target and its firewall

For h!=0 and base b=16, normality asks

    (1/N)sum_(j<N)e(h*b^j*pi) -> 0.

The origin cocycle reformulates the associated
lags exactly through H_d(x). Haar/frame averages
of these characters vanish, but that is valid
even for x=0 and other known nonnormal sources.
Replacing π's selected point by a frame average
would import genericity as a hidden premise.

Future work must derive a new source-specific,
noncircular, all-horizon estimate on the signed
cyclotomic correlations of the actual BBP-selected
phase. The exact H_d and periodic-origin sample
costs locate the missing source-selection arrow;
they do not close it.

**Mathematical status:** OGC-01–09 are classical
covering/character/topological facts with complete
elementary derivations, newly integrated into the
BBP/SUCC source-oriented research program.
OGC-10's π cancellation is UNVERIFIED. No
independently publishable novelty or physical
inertial-frame hypothesis is claimed.

Reference sources: PR #253 signed BBP correlation and
Lean, #252 true source, #247–#249 circle/carry;
classical covering dynamics, necklace-period
Möbius inversion, Fourier orthogonality, and
one-point compactification of R.


## OGC-11. Exact FOURTH moment and an almost-every-origin theorem

The Haar origin average has more information than merely
its second moment, but still not enough to SELECT π.

For b>=2 and any fixed nonzero integer h, the positive
powers {h*b^j:0<=j<N} are a B_2 sequence: any equality

    b^i+b^j=b^k+b^l

forces the unordered index multisets {i,j}={k,l}.
For b>=3 this follows from uniqueness of base-b
digits 0,1,2. For b=2 it follows by separating
the equal-exponent "carry" case (one 1-bit after
carrying) from unequal exponents (two distinct
1-bits); both representations remain unique.

Expand the fourth power, integrate over the
spatial origin a, and use integer Fourier
orthogonality. Only the 2N²−N ordered pair
matches remain, giving the EXACT identity

    int_0^1 |A_(h,N)(x+a)|^4 da
       =(2N²-N)/N⁴ <=2/N²                    (K)

for EVERY selected x, every b>=2 and h!=0.
The derivation is source-independent; the
absolute Weyl phases e(hb^j x) cancel between
matching pairs. This is not a probabilistic
independence axiom.

By Markov,
    Haar{a: |A_(h,N)(x+a)|>=epsilon}
      <=(2N²-N)/(N⁴ epsilon^4).

The right-hand side is summable over all N.
Borel–Cantelli therefore proves, for any
fixed x, any base b>=2, and Haar-almost
every ORIGIN TRANSLATION a,

    A_(h,N)(x+a) ->0  for every fixed h!=0.

Take the countable intersection over integer
h and rational epsilon>0; Weyl yields that
x+a is base-b normal for almost every a.
This recovers the classical almost-everywhere
Borel/Wall normality theorem by *exact circle
reference-sampling fourth moments*.

**It does NOT show x=π is normal:** the
source-pinned shift a=0 has measure zero,
and x=0 is a known exceptional fixed orbit.
The physical coordinate-change theorem
OGC-01 also forbids interpreting arbitrary
translated STATES x+a as mere gauges of
the identical x orbit while retaining T_b.

A finite origin grid of size m can reproduce
(K) EXACTLY if the unordered pair sums
h(b^j+b^k), 0<=j<=k<N, are distinct modulo m.
An easy sufficient bound is
    m>2|h|*b^(N-1).
The necessary number of distinct grid labels
is at least N(N+1)/2, whereas the second
moment only needs N distinct labels.
This gives an explicit *observation-resource
hierarchy* from the circle's additive Fourier
energy, not an infinite proof of π genericity.
The exact source oracle tests base 2,3,16;
it rejects the m=15 aliasing counterexample
and reproduces the fourth-moment formula.

**Interpretation:** the circle's own covering
rules force vanishing mean-square *and*
fourth-moment reference differentials, enough
for Haar-a.e. sources. The precise missing
inference is from that ensemble to the one
authenticated BBP-selected point. That
remaining selection theorem is the true π
frontier rather than a failure of sampling
algebra or insufficient finite precision.


## OGC-12. Forward SUCC / full inverse-tree FUCC: exact Haar without a selected generic orbit

The expanding covering T_b has b lawful inverse
branches at every point. The COMPLETE b^k preimage
probability measure of an arbitrary starting x is

    mu_(k,x)=(1/b^k)sum_(r=0)^(b^k-1)
                  delta_((x+r)/b^k).

This is a shifted regular b^k-gon and satisfies:

    (T_b)_*mu_(k,x) =mu_(k-1,x),
    (T_b^k)_*mu_(k,x)=delta_x,
    W1(mu_(k,x),Haar)=1/(4 b^k)  ->0.

The characteristic function is EXACT:

    int e(hy) dmu_(k,x)(y)
      =0                    if b^k does not divide h,
      =e((h/b^k)*x)         if b^k divides h.

Consequently every fixed nonzero Fourier character
is annihilated at a sufficiently fine inverse-tree
level, even when x=0 is the most nonnormal forward
starting state imaginable. The limit mu_(k,x)->Haar
is a classical, exact spatial averaging statement.
It says NOTHING about the one selected forward orbit.

Moreover, the law (T_b^k)_*mu_(k,x)=delta_x
for all k shows an explicit failure of naively
interchanging the k->infinity limit with a
k-dependent sequence of expanding forward maps.
No single fixed-map continuity theorem justifies
that exchange.

This makes the user's original zero/infinity
and SUCC/FUCC insight into a lawful category:
the full inverse covering fiber has a uniform
probability transport and exact Haar completion,
while a selected backward branch or selected
forward trajectory requires its own source
authentication. Forgetting branch labels is
an admissible operation only for target-relative
measure questions; it can erase π's distinguished
path completely.

The rational-only oracle directly replays the
b-to-1 inverse-tree projective pushforward for
b=2,3,16 and source x=1/7, and verifies the
Fourier character cutoff and geodesic W1 formula.
Again, this closes a TRUE classical mathematical
theorem while exposing rather than erasing the
selected π normality gap.
