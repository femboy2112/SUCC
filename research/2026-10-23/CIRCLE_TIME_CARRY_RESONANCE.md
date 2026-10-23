# Circle Time-Carry Resonance — exact normality proof discriminators

**Date:** 2026-10-23. **Parent:** SUCC Circle Genesis draft #247,
5a2922986719c03dfd4e20d23d3b266b8b775c8e.
**Branch:** research/circle-time-carry-3adic-resonance-2026-10-23.
Research-only additive stack; no main merge, archive edit, journal publication,
physical claim, π-normality proof, RH or original signed-Weil positivity.

## 0. Precise object and source/observer boundary

For integer base b>=2 on the circle R/Z set
  D_j(x)=|1-exp(2πi b^j x)|²=2-2cos(2π b^j x).
Haar expectation is with respect to the WHOLE circle, while a time mean
over a SINGLE orbit is a separately typed observation. The π-selected
initial state is x={π}; it is pinned by independent Archimedean polygon
or Wallis/Kummer source data, not by random choice from the circle.

Finite exact code uses complete integer and Fraction arithmetic.
Universal statements below are paper proofs; tests are finite calibration.
All classical source mechanisms retain attribution.

## TC-01. EVERY Haar time correlation has a two-level carry formula

For k>=0 and z on the circle,
  (2-z-z^(-1))^k
    = sum_(h=-k)^k (-1)^h binom(2k,k+h) z^h.         (1)

For distinct nonnegative time indices j_1,...,j_s and powers k_i>=0,
termwise Haar integration of the finite Laurent expansions gives

  E_Haar[prod_i D_(j_i)^(k_i)]
    = sum_(|h_i|<=k_i, sum_i h_i*b^(j_i)=0)
          prod_i (-1)^(h_i) binom(2k_i,k_i+h_i).    (2)

Every coefficient is itself EXACTLY a prime-power carry product:
  binom(2k,k+h)=prod_p p^(c_p(k+h,k-h)),            (3)
  c_p(a,b)=sum_(r>=1)(
      floor((a+b)/p^r)-floor(a/p^r)-floor(b/p^r)).
Each c_p counts base-p carries adding k+h to k-h, including all p^r
depths. Formula (2) therefore couples two different, source-derived
arithmetics: within-mode ALL-PRIME addition carries and across-time
exact base-b zero-balance/carry. There is no assumed independence or
stochastic forcing in this construction.

The code compares (2) using standard binomial arithmetic to (2)
reconstructed independently from every Legendre/Kummer prime-power
valuation, with source-digit controls and fake carry refusals.

## TC-02. Exact LOW-DEGREE Haar factorization and its sharp break

If every k_i<b and all j_i are distinct, then the only solution to
sum_i h_i b^(j_i)=0 with |h_i|<=k_i is h_i=0 for every i.

Proof: choose the smallest j with h_j!=0. Divide by b^j.
Every later term is divisible by b, but 0<|h_j|<b. Contradiction.
Repeat over all nonzero frequencies.

Hence the entire multi-time joint moment factorizes EXACTLY:
  E_Haar[prod_i D_(j_i)^(k_i)]
   =prod_i binom(2k_i,k_i).                         (4)

For base 16, all distinct-time moments with individual exponents <=15
factor in this sense for ANY number of observed times, although the
source dynamics is completely deterministic and D_(j+1)=F_16(D_j).
Do not promote finitely many factorized moments to independent random
variables.

The first possible nontrivial two-time carry occurs at degree k_0=b,
k_1=1, j_0=0,j_1=1. Exactly the two solutions
(h_0,h_1)=(b,-1),(-b,1) contribute, giving
  E_Haar[D_0^b D_1]
      -binom(2b,b)*2 = 2*(-1)^(b+1).               (5)
For hexadecimal coverings this is -2, not zero.
The independent check expands D_1=F_b(D_0), multiplies by D_0^b
and integrates termwise using the central binomial Haar moments.
Thus the correction is observed through two genuinely different
derivation routes.

This is a sharp source/history threshold, not a proof that the selected
π trajectory has these Haar moments.

## TC-03. Exact 3-adic single-orbit nonnormal counterfeits

For r>=2, define q=3^r, L=3^(r-1), x_r=1/q.
By lifting the exponent v_3(16^(3^s)-1)=s+1, the order of 16 modulo q
is L. Consequently its orbit visits EXACTLY the residues 1+3t modulo q:
  {16^j mod q : 0<=j<L}={1+3t:0<=t<L}.           (6)

For any integer h its whole-period Fourier average is
  A_h=(1/L) sum_(j=0)^(L-1) exp(2πi h16^j/q)
     =0                     if L does not divide h,
     =exp(2πi (h/L)/3)      if L divides h.        (7)
This is the elementary coset-geometric series, distinct from but
consistent with classical Ramanujan sums.

Combining (1) and (7) gives exactly
  (1/L)sum_(j<L)D_j(x_r)^k=binom(2k,k)
                                       for 0<=k<L, (8)
while at the FIRST failing moment k=L (odd)
  (1/L)sum_(j<L)D_j(x_r)^L=binom(2L,L)+1.        (9)

Kummer's base-3 carries in L+L=2*3^(r-1) are zero, so
  v_3(binom(2L,L))=0.
Lucas or the digit product gives binom(2L,L)=2 mod 3; the
first counterfeit moment is divisible by 3. These are distinct
prime-source values, not a normalized numerical approximation.

For the positive Fejér collision energy defined in PR #247, the
complete-period exact formula is
  E_(M,L)(x_r)
   =1+2q_M-L*q_M*(q_M+1)/(M+1),
   q_M=floor(M/L).                                (10)

In particular E_(M,L)=1 for EVERY band M<L, despite the orbit
being periodic and nonnormal. At M=L the excess is just 2/(L+1).
A claim that large finite moment agreement or exceptionally good
finite Fejér energy proves infinite genericity is REFUTED.

## TC-04. ANY finite joint chord/time probe list can be spoofed

Let a declared finite observer query products of powers at finitely many
times: P(x)=prod_i D_(j_i)(x)^(k_i). From (1), every Fourier frequency
of P has absolute value bounded by
  B(P)=sum_i k_i*16^(j_i).

For the periodic measure μ_r uniformly supported on the single orbit
x_r, equation (7) and the Haar zero-frequency law imply
  L>B(P) ==> integral P dμ_r=integral P dm_Haar.  (11)

Choose r large enough to satisfy the strict inequality for EVERY test
in an arbitrary FINITE catalogue. Then that one fully deterministic
periodic rational orbit passes every catalogue test EXACTLY, even with
joint time correlations and all the prime-power binomial coefficients.
This is source/existence scoped: the counterfeit is NOT π.

The code provides precise harmonic-budget certificates and exact
periodic/Haar value comparisons. A larger set of declared finite
probes may distinguish it. An unbounded horizon with a fixed π
source is a different problem and is not refuted by (11).

## TC-05. The circle's Haar moment Hankel determinants are all powers of 2

Write H_k=binom(2k,k). The principal Hankel Gram matrix
G_n=[H_(i+j)]_(0<=i,j<=n) satisfies
  det G_n=2^n.                                    (12)

Proof: on the chord interval [0,4] the monic orthogonal polynomials
are P_0=1 and P_n(X)=2(-1)^n ChebyshevT_n(1-X/2), n>=1.
Their squared Haar norms are 1,2,2,..., as circle cosine modes have
norm squared 1/2. The Gram determinant is the product of those norms,
yielding (12).

For the 3-adic orbit let n=(L+1)/2. All moments up to 2n-2=L-1
match Haar, so det G_(n-1)^periodic=2^(n-1).
At m_L the moment changes +1; at m_(L+1) it changes
2(L+1)=4n. The monic P_n has coefficient -2n of X^(n-1).
In the P-basis these changes cancel on the diagonal P_n²,
but create a single off-diagonal coupling 1 between
P_(n-1) and P_n. The last 2x2 Gram block is
  [[2,1],[1,2]] instead of [[2,0],[0,2]].
Consequently the FIRST detectable Hankel determinant is
  det G_n^periodic=(3/4)*2^n.                    (13)

This is an exact off-diagonal *observable source defect*: all
earlier Hankel certificates agree, the first phase-carry interaction
changes the determinant by exactly one quarter. It is not a general
new Hankel theorem or a signed Weil-Schur conclusion.

## TC-06. π-pinned finite observation can be mimicked by this same orbit family

The arithmetic coset {a/q: a=1 mod 3} is a shifted equally spaced
L-point grid on R/Z, with gap 1/L. For ANY circle point x, choose a
coset representative x_r with circular error at most 1/(2L).
In particular, obtain one for x={π} using the independently certified
nested-polygon rational bracket for π, WITHOUT inputting digits.

For j<N,
  d_circle(16^j x,16^j x_r)
        <=16^j/(2L).                              (14)

With a rational bracket [π_lo,π_hi], midpoint rounding returns a
source-certified x_r with upper error
  δ_r <=1/(2L)+(π_hi-π_lo)/2,
and replace the right of (14) by 16^j δ_r.

As r grows, this matches ANY fixed π orbit prefix and finite
continuous chord probe transcript to arbitrarily high precision.
Nevertheless x_r remains rational/periodic, its full-period low-order
moments perfectly mimic Haar, and its full-period Fejér band
below L has energy 1. The exact branch tests select finite r against
source-derived π intervals. This refutes transferring π normality
from arbitrary finite source precision without a global theorem.

## Actual obstruction and next discriminating source theorem

The geometry fixes complete target joint correlations via (2)-(3);
the Archimedean and Kummer construction fixes the ACTUAL π source;
the new finite tests expose exactly where source copies can remain
toolkit-indistinguishable. What is OPEN is to show that the one
π-selected source cannot sustain non-Haar phase/carry correlations
as N grows, not merely that an ensemble has them.

A falsifiable candidate is a truly π-source-derived estimate, fixed before
testing, on the genuine incomplete phase-carry/collision sum that controls
E_(M_N,N)(π) for a growing band M_N=o(sqrt N).
State an independent arithmetic-geometric premise strictly weaker than
this desired conclusion, with a certified transform and source-holdout.
Without that, a rewording of normality is not a proof.

**Authority:** Fourier Laurent identities, Kummer, Chebyshev,
root-of-unity sums and Bareiss algorithms are classical; this
source-indexed two-clock assembly and exact finite probes are
new-to-SUCC. Academic novelty UNVERIFIED. No π-normality, RH or
physical instrument result; no omitted phase/pole/contact is
silently replaced by a positive norm.

**Sources:** GitHub SUCC #247, #231, #232 and #245/#246; classical
Ramanujan character sums (Titchmarsh, The Theory of the Riemann Zeta
Function, §1.5); Kummer's theorem, Chebyshev cosine orthogonality.


## TC-07. A π-SPECIFIC two-scale no-go for naïve periodic-proxy transport

We can locate exactly why the excellent rational 3-adic countermodels do
NOT themselves provide a way to prove π's normality by approximation.

Let x={π} and x_r=a/3^r be any periodic source, with L=3^(r-1).
For integer h!=0, the elementary character-Lipschitz estimate is

  |A_(h,N)(x)-A_(h,N)(x_r)|
    <= U_(h,N,r)
     := (2π|h|/(15N))*(16^N-1)*d_circle(x,x_r).       (15)

This is a legitimate SUFFICIENT certificate when U is small, not an
identity or a lower bound on the actual Fourier difference.

Published irrationality-measure results for π give μ(π)<8:
e.g. Zeilberger–Zudilin (2020) establish μ(π)<=7.103205334137...
(see https://arxiv.org/abs/1912.06345).
Hence, for every fixed ν=8, some C_8>0 exists such that for all large
denominators q and all rational numerators a,

  |π-a/q| >= C_8 q^(-8).

Apply this to the circle representative of π and q=3L. If an argument
uses at least one entire periodic cycle, N>=L, then

  U_(h,N,r)
   >= [2π|h|C_8/(15*3^8)]
       * (16^N-1)/(N^9)
      --> infinity as N grows.                             (16)

Thus, on the regime N>=L required to exploit exact full-cycle Fourier
cancellation, the ordinary pointwise Lipschitz upper-bound expression
can NEVER yield the required o(1) phase transfer for large N.
Taking the trivial min(2,U) leaves an uninformative bound of 2.

This is an exact no-go for THAT CERTIFICATE/PROOF ROUTE.
It is NOT a lower bound on the actual complex sum difference, does not
refute a phase-cancellation transport proved by a stronger mechanism,
and does not imply π is nonnormal.

**New proof requirement:** any successful source transfer from these
periodic cosets to the π-selected orbit at useful horizons must exploit
AGGREGATE PHASE CANCELLATION rather than uniformly shadowing every
successor event. This supplies a discriminating topological/resource
obstruction: preserving every microscopic sample is a needlessly
strong morphism for the target theorem, but relaxing it requires
new arithmetic information about the ACTUAL π source.


## TC-08. The EXACT topology gap: perfect weak convergence but maximal TV

The same single-orbit measure from TC-03 is a translated regular L-point
grid, with L=3^(r-1):
  μ_r=(1/L)sum_(t=0)^(L-1) δ_((1+3t)/(3L)).

On the circle with geodesic distance and the 1-Wasserstein metric,
  W_1(μ_r,Haar)=1/(4L),                           (17)
whereas
  TV(μ_r,Haar)=1                               (18)
for EVERY finite r.

Proof: partition the circle into nearest-vertex arcs of width 1/L
and transport Haar mass to each central atom. The transport cost is
L times the integral from -1/(2L) to 1/(2L) of |t|dt, namely 1/(4L).
For the converse, the test function distance to the finite support
is 1-Lipschitz, has μ_r average zero, and Haar average 1/(4L).
Kantorovich duality (or the direct Lipschitz inequality) gives the
same lower bound. For TV, the atomic support has full μ_r mass and
zero Haar mass.

Thus the finite rational periodic ORBIT measures converge to Haar
even in W_1 at an exact rate, while remaining mutually singular in TV.
The source spectral/Hankel and Fejér finite-resolution agreements do not
upgrade this weak approximation to normality of any fixed x_r.

There is a completely explicit noncommuting-limit witness: take
x_r=1/3^r -> 0. For each fixed r, the 16-orbit time empirical measure
converges to μ_r, hence
  lim_(r->infinity) lim_(N->infinity) ν_(N,x_r)=Haar.
For each fixed N, all finitely many iterates of x_r tend to 0, hence
  lim_(N->infinity) lim_(r->infinity) ν_(N,x_r)=δ_0.

Both limits are valid in weak-* measure topology and are DIFFERENT.
This is a real source/limit-order defect, not a contradiction in
circle dynamics. It explicitly refutes the shortcut "rational
approximant invariant measures converge to Haar, so the limiting
selected point has a Haar-generic orbit".

The same approximation-and-transport hazard applies to an x_r selected
near π from actual polygon bounds; π's genericity itself remains OPEN.


## TC-09. Prime coverings are NOT prime moment probes: a categorical trap

There are two superficially similar but mathematically different
"prime-generated observer languages".

**Prime covering-degree measurements:**
  F_p(X)=2-2 ChebyshevT_p(1-X/2), p a rational prime.
Since F_p(D(z))=2-z^p-z^(-p), these probe only the circle Fourier
frequencies ±p. They are NOT separating even among T_16-invariant
measures arising from one actual periodic source trajectory.

For r>=3, L=3^(r-1) is divisible by 9, hence NO rational prime p
is divisible by L. Formula (7) gives μ_r_hat(p)=0 for every prime.
Consequently, for x_r=1/3^r,

  lim_(N->infinity) (1/N)sum_(j<N) F_p(D_j(x_r))=2
                                for EVERY prime p.          (19)

The right side equals Haar's mean of each F_p, yet x_r is rational,
periodic, and emphatically nonnormal. This is a decisive no-go:
positive prime covering degrees GENERATE all multiplicative coverings,
but the corresponding first-moment scalar readouts are not a complete
observable family. Algebraic generation is NOT observational
separation.

**Prime EXPONENT chord moments:** instead use the different functions
  X^p, p a rational prime,
on the chord coordinate X in [0,4]. The classical Müntz–Szász theorem
states that span{1,X^p: p prime} is dense in C[0,4] exactly because
Euler's classical sum of prime reciprocals diverges:
  sum_(p prime) 1/p = infinity.

Therefore, for a fixed circle point x and integer base b>=2,

  x is normal in base b
    iff for EVERY prime p,
       lim_(N->infinity) (1/N)sum_(j<N)D_j(x)^p
                                      =binom(2p,p).         (20)

Proof: normality immediately implies the moment limits. Conversely,
every subsequential empirical limit has chord pushforward with the
same integrals as Haar against 1 and X^p, every prime p. Density
forces the entire pushed-forward measure to equal the arcsine law.
The reflected-symmetrization, absolute-continuity and expanding-covering
Fourier rigidity argument of parent CC-03 then forces the original
limit to be Haar; hence x is normal.

Equation (20) is an EQUIVALENT CRITERION, not a π proof. Its point is
that the *irreducible exponent* family is a genuinely separating
observer toolkit, whereas the superficially more natural *irreducible
covering-degree* family is not. The criterion imports classical
Müntz–Szász and Euler, not a new approximation theorem.

A concrete hostile control at base 16 and source x=1/27:
all prime-degree F_p means are exactly 2, but the prime EXPONENT p=11
reveals the source:
  Haar H_11=binom(22,11)=705432,
  periodic moment_(11)=705663=H_11+231.
These values are exact integer oracle checks.

A second restriction: prime-square exponents p^2 have convergent
reciprocal sum, so Müntz–Szász says their span is NOT dense in
C[0,4]. This means that family cannot separate *all arbitrary*
probability measures by moments. It does not automatically construct
a counterexample restricted to T_b-invariant measures or disprove a
π-specific theorem. All status qualifiers must remain attached.

Primary classical reference for the precise density theorem:
T. Erdélyi, Studia Mathematica 155 (2003), 145-152,
https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/en/publishing-house/journals-and-series/studia-mathematica/all/155/2/90299/the-8220-full-clarkson-8211-erdos-8211-schwartz-theorem-8221-on-the-closure-of-non-dense-muntz-spaces
Euler prime reciprocal divergence is classical:
https://math.hmc.edu/funfacts/sum-of-prime-reciprocals/

**Proof boundary:** (19) REFUTES prime-covering first-moment
completeness. (20) is PROVED CLASSICAL CONDITIONAL NORMALITY
EQUIVALENCE. No π-source orbit estimate in (20) has been proved.


## TC-10. Concrete PRIME-INDEX π-source moment transport, with paid cost

Combine the source-corrected nested-polygon algebraic phases Y_(j,K)
of parent CC-06 (#247) with the prime-exponent Müntz observer basis
of TC-09.

Define the true and polygon-phase-chord moment averages for any fixed
prime p and integer lookahead K>=1:

  m_(p,N)(π)=(1/N)sum_(j<N)
        [4sin²(π*16^j*π)]^p,
  m̃_(p,N,K)=(1/N)sum_(j<N)[4sin²(π*Y_(j,K))]^p.

The phases Y_(j,K) come from finite nested polygon radicals without
assuming any π digit. The sine observations of these algebraic phases
are analytic quantities, NOT falsely asserted to be algebraic.

The parent circle-source theorem gives for all j>=0
  |16^jπ-Y_(j,K)|<=C*16^(-j-2K),
  C=(3/20)(22/7)^5.

The circle observable f_p(t)=[4sin²(πt)]^p has derivative uniformly
bounded by π*p*4^p, because |4sin²(πt)|<=4 and the inner derivative
has magnitude at most 4π. Thus

  |m_(p,N)(π)-m̃_(p,N,K)|
    <= [π*p*4^p*C/(N*16^(2K))]
       *sum_(j<N)16^(-j)
    < [16*(22/7)*p*4^p*C]/[15*N*16^(2K)].       (21)

The last bound is rational and reproduced by
prime_polygon_moment_transport_bound with a genuine-prime source gate.
For each FIXED prime p and FIXED K it decays at least as O_p(1/N).

Therefore π is base-16 normal if and only if, for one fixed K>=1,
the precisely source-generated geometric moments m̃_(p,N,K) converge
to the exact all-prime Kummer Haar integers binom(2p,p)
for EVERY rational prime p. The equivalence uses TC-09's Müntz
separation and the explicit O_p(1/N) difference, NOT an assumed
mixing property or a finite experiment.

**What is now genuinely established:** the π SOURCE identity, the
chosen complete arithmetic PROBE basis, and the quantitative
source→orbit-observable TRANSPORT with an error budget are explicit.
The single remaining proof obligation is to derive a NONCIRCULAR
estimate on m̃_(p,N,K)-binom(2p,p) from the nested geometric source
for each fixed prime p. Neither its convergence nor an RH/π
normality theorem is claimed.

The polynomial, carry, spectral and source mechanisms are classical
or new-to-SUCC combinations. Scholarly novelty UNVERIFIED.
