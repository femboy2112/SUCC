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
