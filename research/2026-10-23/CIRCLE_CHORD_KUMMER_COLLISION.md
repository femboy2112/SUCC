# Circle → Chord → Central-Binomial Carries → π Orbit
## A source-faithful geometric normality research round — 23 October 2026

**Claim authority:** classical identities and newly derived, explicitly scoped paper
proofs; standard-library exact finite/interval controls; no new Lean kernel
result; no π normality theorem. Independent scholarly novelty UNVERIFIED.

**Parent:** Reality Pin draft PR #244, head
5e2ba04c8b4ab627b6b0add588609c347346a1a2. Work is an independent draft,
not a main merge. Relevant siblings PRs #229 (circle/Gamma/primes), #231 (Wallis/
Kummer prime carries), #232 (BBP and Lean conditional normality), and #245/#246
(carry-safe observation and source memory) were *consulted*, not silently merged.
The unchanged import manifest and original signed Weil sources are outside this
patch. RH, Weil positivity and physical geometry remain separate.

### The aim, with the actual mathematical hole

The circumference and metric of one Euclidean unit circle determine π. The
circle's finite self-coverings encode integer multiplication and their chord
observables obey exact integer-polynomial composition. Its Haar chord moments
are **central binomial coefficients** whose complete prime-power factorization
is counted by Kummer carries.

The unresolved arrow is **from this global/ensemble geometry to the selected
time-orbit** starting at the actual point x={π}. Geometric Haar symmetry
alone cannot license genericity of that one orbit.

For a fixed base b>=2, define

    z_j(x)=exp(2π i b^j x),  A_(h,N)(x)=N^-1 sum_(j<N) z_j(x)^h.

The authentic open theorem is A_(h,N)(π)->0 for all fixed nonzero integers h.
What follows supplies two exact, source-typed geometric criteria and a certified
π-source realization, not the missing asymptotic inequality.

---

## CC-01. Self-covering semigroup and exact chord polynomials

Let S¹={z in C: |z|=1}, T_n(z)=z^n, and d(z)=|1-z|².
For n>=0 define

    F_n(X)=2-2 T_n^Cheb(1-X/2),

where T_n^Cheb is the classical first-kind Chebyshev polynomial (not the
circle map T_n). The Chebyshev cosine law proves

    d(T_n z)=F_n(d(z)),      F_m o F_n=F_(mn).

The integer polynomial recurrence is

    F_0=0, F_1=X,
    F_(n+1)=2X+(2-X)F_n-F_(n-1).

In particular F_2=4X-X², F_3=9X-6X²+X³. Dividing F_n by X yields exactly
the pre-existing SUCC polygon-eigenvalue polynomials W_n of PR #229:

    W_0=0, W_1=1,
    W_(n+1)=2+(2-X)W_n-W_(n-1).

Positive-degree circle group self-covering degrees multiply under composition;
positive degrees >=2 indecomposable under nontrivial composition are precisely
the rational primes. A composite multiplier 6 is T_2 o T_3, NOT a new Euler
prime source. Degree/category mathematics is classical, not an arithmetic
prime-distribution theorem.

For any circle orbit d_jk=|z_j-z_k|²,

    d_(j+1,k+1)=F_b(d_jk).

At a fixed lag ℓ, all subsequent pairwise distances form the autonomous
integer-polynomial chain d_(j,j+ℓ)=F_b^j(d_(0,ℓ)). Unlike independent
multiplicative Euler factors, this is an exact law on the particular orbit's
joint observable.

The chord quotient q:S¹->[0,4] is two-to-one generically and loses
orientation, yet q o T_b=F_b o q exactly. No physical implementation is implied.

---

## CC-02. The Haar chord law is precisely the Kummer-carry integer system

For k>=0,

    d(z)^k=(2-z-z^-1)^k
          =sum_(h=-k)^k (-1)^h binom(2k,k+h) z^h.

Integrating over circle Haar probability annihilates every h!=0:

    H_k := int_(S¹) d(z)^k dm(z)=binom(2k,k).

This is the arcsine law on [0,4], with density
1/(π sqrt(t(4-t))) for 0<t<4.

For the entire m-gon vertex ensemble, root-of-unity orthogonality gives the
EXACT finite identity

    (1/m)sum_(r=0)^(m-1) d(exp(2πir/m))^k
     = sum_(|h|<=k, m|h) (-1)^h binom(2k,k+h).

Therefore every regular m-gon with m>k has EXACT Haar k-th chord moment
H_k, at a finite stage with no asymptotic approximation:

    m>k ==> polygon moment=binom(2k,k).

This threshold is sharp: at m=k>=2 the moment differs by 2(-1)^k.

Now, Legendre's formula and Kummer's carry theorem identify

    binom(2k,k)=prod_(p prime<=2k) p^(c_p(k)),
    c_p(k)=sum_(r>=1)(
       floor(2k/p^r)-2 floor(k/p^r)).

Every term in c_p(k) is 0 or 1, and c_p(k) counts carries in the
base-p addition k+k. The products are finite, exact, source-verified and
retain *all* prime-power depths.

**The key bridge:** the very central binomial numbers used by the inherited
Wallis/Kummer source construction of π (PR #231) are also the exact
target moments of the circle's own invariant chord geometry.

The equality H_k=product_p p^c_p(k) is unconditional and classical. It
does NOT establish that one π-selected orbit has the invariant moments.

---

## CC-03. Target-sufficient chord observation: a rigorous normality criterion

For any x in R/Z and integer b>=2, set d_j=F_b^j(d(exp(2πix))).
Then the following are EQUIVALENT:

(a) x is normal in base b (i.e. its T_b orbit is Haar-generic);

(b) for every integer k>=1,

    lim_(N->infty) (1/N)sum_(j<N) d_j^k = binom(2k,k).

**Proof, (a)->(b).** Apply empirical Haar convergence to the continuous
test d(z)^k and CC-02.

**Proof, (b)->(a).** Let μ be any weak-* limit of a subsequence of the circle
empirical probabilities. Compactness supplies such limits. The endpoint
telescoping identity makes μ T_b-invariant. By hypothesis its q-pushforward
has every moment of q_*m. Polynomial density on the compact interval [0,4]
gives q_*μ=q_*m (the Hausdorff moment uniqueness in this simple setting).

Let R(z)=conj(z) be reflection. Every continuous R-even circle function
factors through q, so equality of pushforwards gives

    (μ+R_*μ)/2=m.

As positive measures, μ<=2m; therefore μ has an L¹ Haar density.
For each nonzero Fourier mode h, T_b-invariance gives
μ_hat(h)=μ_hat(bh)=μ_hat(b^r h). The Riemann–Lebesgue lemma sends the last
coefficient to zero as r->infty. Thus μ_hat(h)=0 for h!=0, and μ=m.
Every empirical subsequential limit is m; the full orbit is Haar-generic.
QED.

**Interpretation.** Orientation is discarded by the chord factor, but the
target property of Haar genericity survives because future dynamics and
absolute-continuity rigidity recover the missing distinction. This is
target-relative observational sufficiency, not unrestricted source recovery.

The moment criterion is equivalent to normality; its individual limit
statements remain unproved for x={π}. Its right-hand sides are already
identified with the authentic complete-prime Kummer carries.

---

## CC-04. Exact ensemble-to-selected-path obstruction

Even finite polygon measures with exactly correct moment targets need not
describe an individually selected orbit.

Take the 7-gon and T_2. Since gcd(2,7)=1, the covering permutes all vertices,
and the full vertex-uniform measure is invariant. Its first chord moment is
exactly 2.

But its permutation decomposes into three cycles:

    {0}, {1,2,4}, {3,6,5}.

Let ζ=exp(2πi/7) and A=ζ+ζ²+ζ⁴. The other nonzero cycle is the
complex conjugate and A+conj(A)=sum_(r=1)^6 ζ^r=-1. Hence Re(A)=-1/2.
The selected orbit {1,2,4} therefore has average chord moment

    2-2 Re(A)/3 = 7/3,

not the full polygon target 2. This is an EXACT finite counterexample even
when the full polygon measure is invariant under the covering.

For m divisible by b, the situation is worse: T_b maps the uniform m-gon
ensemble to the uniform (m/gcd(m,b))-gon, not to its original distribution.
Our dyadic geometric π approximants use m=4^j and hexadecimal expansion
b=16. Their finite vertex ensembles COLLAPSE under a fixed-level covering.
One cannot silently confuse the spatial refinement map with digit-time
evolution. Refinement while advancing requires a separate compatible map.

Thus geometry -> Haar ensemble is CLOSED; ensemble -> selected π orbit is OPEN.
The obstruction is not a finite-resolution numerical defect.

A second hostile family: for q>M and gcd(q,b)=1, the uniform qth-root
measure is invariant, singular, and has exactly the same first M Fourier and
chord moments as Haar. Hence no fixed finite-moment or fixed-frequency probe
can establish Haar genericity across the whole admissible source family.

---

## CC-05. One positive chord energy and exact frequency amplification

Let F_M(t)=(M+1)^-1 |sum_(r=0)^M exp(2πirt)|², M>=1, the classical
nonnegative Fejér kernel. By CC-01 it has a polynomial presentation on
squared chord distance X=4sin²(πt):

    K_M(X)=M+1-sum_(h=1)^M (1-h/(M+1))*F_h(X).

For M=3, K_3(X)=4-5X+2X²-X³/4, a nonnegative polynomial on [0,4].
For x in R/Z set

    E_(M,N)(x)=N^-2 sum_(j,k<N) K_M(d_(jk)(x)).

Finite Fourier expansion gives

    E_(M,N)(x)=1+
      2 sum_(h=1)^M (1-h/(M+1)) |A_(h,N)(x)|² >=1.

This positive scalar depends ONLY on the source's deterministic chord-distance
chains. It is not an ungrounded probabilistic model.

**Exact moving-band amplification lemma.** For b>=2, h!=0, M>=2|h|,
N>=1, define

    R=min(floor(sqrt N), 1+floor(log_b(M/(2|h|)))).

The frequency-shift identity is

    A_(b^r h,N)(x) = N^-1 sum_(j=r)^(N+r-1) e(h b^j x),

hence |A_(b^r h,N)-A_(h,N)|<=2r/N.

For every 0<=r<R, |h|b^r<=M/2, so the corresponding Fejér weight
2(1-|h|b^r/(M+1)) is >=1. These frequencies are distinct. Therefore

    E_(M,N)-1 >= R*(|A_(h,N)|-2R/N)_+²,

and the quantified finite consequence is

    |A_(h,N)(x)| <= 2R/N + sqrt((E_(M,N)(x)-1)/R).        (1)

No π-dependent assumption enters this proof.

**Moving-band theorem.** For any fixed b>=2 and x, the following are
equivalent:

(i) x is base-b normal;

(ii) there exists some integer sequence M_N->infinity for which
    sup_(N sufficiently large) E_(M_N,N)(x)<infinity.

Proof of (ii)->(i): for each fixed h!=0, R_N->infinity and R_N<=sqrt(N);
(1) gives A_(h,N)->0. Weyl gives normality.

For (i)->(ii): each fixed-band energy tends to 1 because each nonzero Fourier
mode vanishes. Diagonalize over M=1,2,... and choose its activation horizons
sufficiently late to ensure E_(M,N)<2 at all later N; also enforce M_N=o(sqrt N).
This makes M_N->infinity and its energies bounded. QED.

The geometric energy is an equivalent, positive, source-compatible
normality instrument, **not** itself an estimate for π. It extends existing
Fourier/Fejér, pair-correlation and discrepancy arguments; independent
scholarly novelty is unverified (see cited Grepstad–Larcher and
Aistleitner–Lachmann–Pausinger).

**Limit-order trap.** At fixed finite N, the diagonal pairs contribute
(M+1)/N, so E_(M,N)>=(M+1)/N. Sending M->infinity first always explodes.
The target requires a properly coupled moving band M_N with N.

---

## CC-06. Source-only corrected polygon π phases, with a paid error

Start with X_4=2, the squared side of an inscribed unit square. Repeated
angular bisection gives

    X_(2m)=2-sqrt(4-X_m).

For m=4^L, the inscribed half-perimeter P_m=m sqrt(X_m)/2=m sin(π/m).
Its Archimedean lower/upper bounds are

    P_m < π < P_m/sqrt(1-X_m/4)=m tan(π/m).

These derive from the circle, not supplied π decimals.

For index j>=0 and integer lookahead K>=1, choose m=4^(j+K) and define
the explicitly algebraic nested-radical source phase

    Y_(j,K) = 16^j*(P_m + P_m³/(6 m²)).

The correction is not arbitrary: it is the next term of arc length
m*arcsin(P_m/m).

**Exact uniform-source theorem.** Let C=(3/20)(22/7)^5. Then for every
j>=0 and K>=1,

    0 < 16^j π - Y_(j,K) < C*16^(-j-2K).                 (2)

Proof: with s=P_m/m=sin(π/m)<=1/sqrt(2), write
arcsin(s)=s+s³/6+R(s).
The positive binomial-series coefficients of (1-t²)^(-1/2) after the
quadratic term are <=3/8. For 0<=t<=s,

    0 < (1-t²)^(-1/2)-1-t²/2 <= (3/8)t^4/(1-t²)
                                           <= (3/4)t^4.

Integrating gives 0<R(s)<3s^5/20. Multiply by m and use P_m<π<22/7:

    0 < π-P_m-P_m³/(6m²)<(3/20)*π^5/m^4<C/m^4.

Now multiply by 16^j and substitute m^4=16^(2j+2K).
QED. The source correction is a true geometric curvature/arc-length remainder
and can be evaluated using nested radicals without inputting any π digits.

For A_h formed from j=0,...,N-1, (2), chord Lipschitz and a geometric sum give

    |A_(h,N)(π)-A_(h,N)(Y_K)|
       <= 32π|h|C/(15N*16^(2K)).                         (3)

Since ||A|²-|B|²|<=2|A-B| for |A|,|B|<=1, summing Fejér weights yields

    |E_(M,N)(π)-E_(M,N)(Y_K)|
       <= 64π C*M(M+2)/(45 N*16^(2K)).                 (4)

The implementation replaces π on the right by the independent rational bound
π<22/7, obtaining an exact outward rational transfer budget.

**Corollary — source-only equivalent problem.** For any fixed K>=1, normality
in base 16 is equivalent to finding an integer band M_N->infinity with
M_N=o(sqrt N) and a uniform bound for E_(M_N,N)(Y_K).

Proof: (4) tends to zero in that regime and the CC-05 moving-band theorem
applies in both directions (slow down the band for the converse).

This produces a specifically circle-derived algebraic *phase sequence* and a
single positive geometric collision observable with an exact π-source
transport budget. Evaluating the circle characters still uses the
transcendental exponential/cosine; it is effectively certifiable by interval
arithmetic, not a claim that all resulting energy values are algebraic.

**The missing substantive theorem has not been weakened by renaming it:**
we still need a genuinely source-derived, all-horizon upper bound for those
positive energies. The polynomial and radical identities do NOT themselves
supply that bound.

---

## CC-07. Actual finite π-orbit energy certificates without digit inputs

The standard-library implementation encloses every square root by integer
isqrt over rational intervals. The same nested polygons enclose π between
inscribed and circumscribed half-perimeters. Each cosine is evaluated at a
rational center with an absolute Taylor/Lagrange bound
4^(2J+2)/(2J+2)!, plus its rigorously paid angle interval. No floating π
value is used to construct a certificate. Independent direct complex
evaluation is calibration only.

Two positive source-only finite witnesses for the genuine hexadecimal orbit:

    1.541868058538 < E_(2,5)(π) < 1.541868058539,
    1.234121274114 < E_(3,8)(π) < 1.234121274115.

The ordered notation is E_(band,horizon). Both inequalities are strict
outward rational enclosures on the actual π orbit, not the generic algebraic
shadow. A separately evaluated K=6 lookahead algebraic shadow has a bound
less than 1.37e-12 on the N=8, M=3 energy difference.

The finite values neither decrease monotonically nor bound the energy at
unbounded N. They do not prove normality and are not outside-the-sample
validation of a fitted asymptotic model.

An inherited independent base-2 benchmark is PR #226:
for N=32, the certified 1-frequency energy is between 1/25 and 1/20.
Equivalently the average squared pair chord is between 19/10 and 48/25.
This is a finite historical benchmark, not a newly reproduced result in this
branch and not a π-asymptotic claim.

---

## CC-08. The irreducible next math problem and the hostile controls

**Next proof target:** construct a source-derived estimate which implies,
for some predeclared M_N->infinity, M_N=o(sqrt N),

    E_(M_N,N)(Y_K) <= C0

for all sufficiently large N, with one finite constant C0 independent of N.
Keep the same authentic nested-circle source and fixed K. This would prove
hexadecimal and binary normality of π by CC-05/CC-06. No estimate is
claimed here.

An equivalent narrower ladder is to prove, for every fixed k,

    (1/N)sum_(j<N) F_(16^j)(d(exp(2πiπ)))^k
                                     -> binom(2k,k).

Our explicit construction makes the right side exactly the complete-prime
Kummer carry product. The left-hand **selected orbit** limit is the open part.
Neither arbitrarily accurate point approximation nor finite polygon ensemble
stabilization controls it.

Mandatory negative controls:

* x=0 is fixed by every covering, while the full circle obeys all geometry
  identities. This refutes geometry-alone genericity.
* The selected T_2 orbit {1,2,4} on a 7-gon has chord mean 7/3,
  while the invariant full 7-gon ensemble mean is 2.
* Uniform qth roots, q>M coprime to b, reproduce the first M Haar
  moments and Fourier energy 1, but give a singular non-Haar measure.
* x=1/3 under doubling has period two and non-Haar chord moments,
  despite correct Chebyshev/polyphase laws.
* Finite approximants with m divisible by b collapse under a fixed-level
  covering; spatial refinement and temporal advancement are distinct maps.
* A band fixed before taking N->infinity cannot certify every Fourier mode.
* Sending M->infinity at fixed N makes diagonal pair energy diverge.
* Dropping mixed-prime phases, using composite 6 as an independent prime,
  or inferring a signed Weil sign from this positive energy remain invalid.

No proof of π normality, RH, signed Weil positivity, new physical law or
gravitational spacetime geometry is claimed.

---

## Implementation, verification and provenance

Source files:
- observational_succ/circle_collision_rigidity.py
- tests/test_circle_collision_rigidity.py
- scripts/circle_collision_probe.py
- research/2026-10-23/CIRCLE_CHORD_EXACT_RECEIPT.json
- .github/workflows/circle-chord-collision.yml

The exact receipt freezes source Git blob IDs, recurrence coefficients,
Kummer factors, finite source-only π energy bounds and mutation controls.
The Python 3.10/3.13 workflow is separately scoped; hosted results must be
observed on the final head, not inferred from prior branches.

Classical source families:
- Chebyshev coverings and their composition:
  https://en.wikipedia.org/wiki/Chebyshev_polynomials
- Kummer's prime-carry theorem:
  https://mathworld.wolfram.com/BinomialCoefficient.html
- Fejér kernel and nonnegative Fourier square:
  https://en.wikipedia.org/wiki/Fej%C3%A9r_kernel
- Aistleitner–Lachmann–Pausinger (2018), pair correlations/equidistribution:
  https://arxiv.org/abs/1612.05495
- Grepstad–Larcher (2016), pair correlations/discrepancy:
  https://arxiv.org/abs/1612.08008
- SUCC predecessor PRs #218, #229, #231, #232, #245, #246:
  https://github.com/femboy2112/SUCC/pulls

These ingredients are classical and already appear in several neighboring
forms in the repository. The synthesis, exact corrected-phase transfer and
local finite certificates are useful to SUCC, but independently publishable
novelty is **UNVERIFIED**.

**Verdict:** The arithmetic laws of circle coverings and Kummer-valued chord
moments are genuine, and a selected-orbit normality proof can be expressed
entirely in a source-compatible positive geometric-energy language. The
remaining π-specific **uniform energy bound** is precisely the new
discriminating mathematical obstacle. It has not been established.


---

## CC-09. A sharp exact finite polygon ENSEMBLE result, and why it cannot select π

There is a particularly tempting but invalid last step: the circle's root-of-unity
ensemble appears already to have the desired small Fourier energy. We can
quantify this without assuming a random source or even taking a limit.

Let v_r=exp(2πir/m) for r modulo m. With base b, horizon N and frequency h,
apply root-of-unity orthogonality to the positive square:

    (1/m)sum_(r=0)^(m-1) |A_(h,N)(r/m)|²
      = N^-2 #{(j,k): 0<=j,k<N, m | h(b^j-b^k)}.           (5)

If m>|h|(b^(N-1)-1), no off-diagonal congruence is possible.
The right side is EXACTLY 1/N.

For the full Fejér pair energy, if

    m > M(b^(N-1)-1),

then every frequency 1<=h<=M has ensemble squared mean 1/N, hence

    (1/m)sum_(r=0)^(m-1) E_(M,N)(r/m) = 1 + M/N.         (6)

The finite set of polygon vertices already has mean energy asymptotically
as small as Haar, for M=o(N), with no analytic conjecture whatsoever.

**Nevertheless vertex 0** is in this very ensemble and is fixed by every
covering, so E_(M,N)(0)=M+1 for all N. Thus the ensemble upper bound (6)
cannot be promoted to a bound for a single distinguished vertex; no
uniform error estimate can be obtained from the average alone. When m and b
are not coprime, the finite polygon's empirical measure itself may fail to
be invariant under fixed-level T_b (CC-04).

This is the clearest finite counterpart of the missing π theorem: the
arithmetic/chord rules completely determine the **average over source
placements**, including its shrinking 1/N variance, but say nothing
sufficient about the single π-anchored placement.

The newly added independent exact oracle is
polygon_ensemble_fourier_square / polygon_ensemble_energy. It checks
m=4^12, b=16, N=6, M=3: the full ensemble Fejér mean is exactly 3/2,
while the legal fixed-point selected orbit has energy 4. The ensemble
mean is an exact rational witness; it is not a numerical random sample.

**Verdict.** To close normality, one must justify a π-specific
typicality-selection mechanism (or a completely different bound) using
the circumference/perimeter source, not simply appeal to the Haar
properties of every fine regular polygon. This objection survives
the exact polynomial, central binomial, Kummer and Fejér identities.


---

## CC-10. Circle source and circle target share precisely the SAME integer moments

The preceding bridge can be closed one rung further, without assuming π
normality. Write H_k=binom(2k,k), the exact invariant squared-chord moment.

By the *classical Wallis product*, the rational approximants

    R_k = 2^(4k+1)/[(2k+1) H_k²]

satisfy the strict enclosure (k>=1)

    R_k < π < R_k*(4k+2)/(4k+1).

Thus the unit-circle circumference constant itself can be reconstructed
from the same moments whose Kummer prime carries the prior theorem extracted.
Since each H_k is *exactly* the k-th chord moment on any regular m-gon with
m>k, this is a fully deterministic finite-circle-moment -> rational interval
-> π source construction. No prior decimal digits of π are needed.

For k=5, H_5=252=2²*3²*7, and the completely exact finite source gives

    131072/43659 < π < 262144/83349.

The key self-consistency question now has a particularly sharp form:

**Source:** π = lim_k 2^(4k+1)/((2k+1) H_k²), with each H_k provided by a
finite polygon and authentic all-prime carries.

**Target:** for each fixed k, prove

    lim_(N->infinity) N^-1 sum_(j<N)
       [F_(b^j)(|1-exp(2πiπ)|²)]^k = H_k.

This would establish normality through CC-03. Both sides use *the same*
circle-generated central-binomial sequence. But identity of source and target
moment *constants* does not supply the temporal convergence on the left.

A fatal naive shortcut would infer that because π was produced by Haar
moments, its own expanding orbit is automatically Haar-generic. For a
counterexample to that abstract inference, select the point x=(1/4)H_1=1/2
from the same geometric Haar expectation H_1=2. Under doubling x maps
immediately to 0 and is nonnormal. A circle-invariant functional of Haar data
need not select a Haar-generic point.

The missing π-specific transport has now been isolated without importing
primes or entropy as additional axioms: **does the precise Wallis
moment-functional selection carry any nontrivial bound on the expanding
polynomial chord-moment chains?** The response is presently UNVERIFIED.
The source equality is classical and already appears in inherited PR #231;
the new-to-SUCC point is making the target-side moment law and the missing
selection theorem part of the same explicit commutative diagram.
