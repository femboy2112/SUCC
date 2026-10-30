# Selected energy, exact source transfer, and the all-horizon threshold

**PROVED LOCAL** means a paper derivation checked by exact probes and separate
implementations, not Lean or independent external refereeing. No claim of
scholarly priority, π normality, or a new fixed-frequency asymptotic signed
saving is made. Parent403 is `5f350af7808532e55d74e80c948c02bb385c6e70`.

## 1. An additive correction: all-frequency energy1 does imply normality

Use the authentic original four-pole r, U_0=0, and e(x)=exp(2πix). Write
E_n(h)=1-Re e(h(U_(n+1)-U_n)). For this source the following are equivalent:

1. π is base16 normal.
2. For every nonzero integer h, N^(-1) sum_(n=1)^N E_n(h) tends to1.
3. For every nonzero integer h, liminf_N N^(-1) sum_(n=1)^N E_n(h) >=1.

This is an **equivalent certificate**, not progress establishing its authentic
arithmetic premise. It repairs an ambiguity in parent403 CLAIMS.md: energy1 at
**one** frequency is insufficient, but the entire real-energy family is
sufficient once multiplication-by16 invariance is retained. The historical
file is unchanged. The imaginary correlations need not be separately assumed.

Here is one proof of the stronger (3)=>normality implication. Every empirical
weak limit μ of {U_n} is ×16 invariant, because r(n) tends to0. Put ν=(×15)_*μ.
The exact recurrence ΔU_n=15U_n+r(n+1) makes Re νhat(h)<=0 for all h!=0.
Let σ=(ν+reflection_*ν)/2, so σhat(h)=Re νhat(h) is real and nonpositive.
The nonnegative Fejér kernel at0 gives, for every H,

    0 <= 1+2 sum_(h=1)^H (1-h/(H+1)) σhat(h).

Monotone convergence of the nonnegative negatives implies
sum_(h>=1)|σhat(h)|<=1/2. Therefore σ has a continuous Fourier-series density.
Since ν<=2σ, ν is absolutely continuous. A finite covering sends a null set
to a null set, so μ is absolutely continuous as well: for a null Borel A,
μ(A)<=ν(15A)=0. Write its L1 density f. Invariance gives
μhat(k)=μhat(16^j k); Riemann–Lebesgue makes this0 for k!=0. Thus μ is Haar.
Every subsequential limit is Haar, proving uniform distribution and normality.
Conversely normality and r(n)->0 give (2), so all three are equivalent.

No Lebesgue-density conclusion follows from ordinary expansion alone. The
positive Fourier and invariant-measure arguments above require the stated
energy hypothesis. The next derivation proves the same implication without
measure theory and supplies an exact finite certificate.

## 2. SP-02: exact repunit-frequency source transport

For d>=1 let m_d=(16^d-1)/15. For every real seed s, every n>=1,

    R_(n,d) := U_(n+d)(s)-U_n(s)-m_d[U_(n+1)(s)-U_n(s)]
              = sum_(j=1)^d 16^(d-j)[r(n+j)-r(n+1)].                (1)

The first equality is independent of s because 16^d-1=15m_d. Unroll the
recurrence to obtain the second; it retains all four signed poles.
The authentic Laplace kernel Q=2(1-e^-3x)+(1-e^-4x)+(1-e^-5x) is positive,
and the parent source bound gives
0<r(k)-r(k+1)<=240/(8k-7)^3. Consequently

    -16(m_d-d)/(8n+1)^3 <= R_(n,d) <=0,                           (2)

with strict negativity for d>=2 and equality0 for d=1. Indeed each of the
j-1 consecutive differences in r(n+j)-r(n+1) is bounded by
240/(8n+1)^3, and
sum_(j=1)^d16^(d-j)(j-1)=(m_d-d)/15. This is an exact source inequality,
not a tail estimate imported into a discontinuous p-primary projection.

Therefore, with F_(n,d)(k)=1-Re e(k(U_(n+d)-U_n)),

    |F_(n,d)(k)-E_n(k m_d)|
       <= 32π |k| (m_d-d)/(8n+1)^3.                              (3)

For fixed d,k the error is summable. Exponential growth in d is explicit;
this formula cannot justify unlimited growing-lag transport for free.

## 3. SP-03: finite Gram certificate, including boundaries

Take A,N>=1, J>=2, k!=0 and put

    ebar(h)=N^(-1) sum_(n=A)^(A+N-1) E_n(h),
    Q=1-(2/J²) sum_(d=1)^(J-1) (J-d) ebar(k m_d),
    B=2(J-1)(J-2)/(3NJ),
    R=(64π|k|/[J²(8A+1)^3]) sum_(d=1)^(J-1)(J-d)(m_d-d).

Then for every real seed,

    |N^(-1) sum_(n=A)^(A+N-1)e(kU_n)|
          <= (J-1)/N + sqrt(Q+B+R).                             (4)

The radicand is nonnegative under these exact definitions. Replacing the
energies by certified lower bounds and π by a rational upper bound preserves
validity. A right side greater than1 is a correctly typed vacuous certificate.

**Proof.** Let z_n=e(kU_n) and W_n=J^(-1)sum_(i=0)^(J-1)z_(n+i).
The average of W differs from the average of z by at most (J-1)/N:
the ith shift loses and gains i unit terms, giving2i/N, averaged over J.
Cauchy–Schwarz bounds |average W|² by average |W|². Expand the latter Gram
square exactly:

    average |W|²
       =1-(2/J²) sum_(d=1)^(J-1) sum_(i=0)^(J-d-1)
            N^(-1)sum_(n=A)^(A+N-1) F_(n+i,d)(k).

Use (3) at n+i>=A. Moving the E window by i changes its average by at
most2i/N, since E is in[0,2]. Summing2i produces B, summing (3) produces R.
This proves (4). It is an explicit van der Corput/Gram inequality specialized
to the original rational forcing, not a new general van der Corput theorem.

For A fixed, one can discard a finite prefix and then send A to infinity;
alternatively use the summed version of (3) rather than its maximum. Thus for
each fixed J, the source and boundary errors vanish in full-horizon averages.
If liminf ebar(h)>=1 for every h, (4) gives limsup |S_N(k)|/N<=J^(-1/2).
Then J->infinity proves the implication in §1 independently.

A weaker sufficient *assembled* premise is the weighted repunit condition

    lim_(J->infinity) liminf_(N->infinity)
      [2/(J(J-1))] sum_(d=1)^(J-1)(J-d) ebar(k m_d) =1             (5)

for every k!=0. A liminf at least1 suffices. This fixes the order of limits:
first every fixed finite lag/frequency family, then increasing J. It does not
assume an unproved uniformity over exponentially growing h at finite N.
Proving (5) from the zero boundary remains **DARK** in this work.

**Executed attack:** exact selected zero-seed phases in the preregistered
three fresh windows and nine k/window configurations are evaluated at all
repunit frequencies needed for J=2,3,4,5. The rational interval certificates
and a separately coded 100-digit direct-prefix oracle are in the receipts.
These test the full phase, with no primary/cofiber marginal replacement.
Any observed energy below1 rules out the stronger finite-window floor1; it
does not refute (5). No extrapolation of the finite savings is asserted.

All36 finite Gram bounds were below1 (range approximately0.45084 to0.72953).
The strongest tested bound is below0.450845 for A=229,N=509,k=1,J=5.
There are17 rigorously enclosed energies below1 among the36 distinct tested
window/frequency combinations. For A=61,N=127,h=1911=7m_3 the exact rational
upper endpoint is below0.881353. Thus the naive finite-window hypothesis
`ebar(h)>=1` is explicitly **REFUTED even for the authentic zero seed**.
Its weaker asymptotic/weighted form (5) remains unresolved.

## 4. SP-04: the sharp gap between positive density and normality

For any 0<eta<1 the invariant probability

    μ_eta=eta Haar+(1-eta)δ_0

has every lag-energy integral exactly eta, because the lag map is ×15.
It is not Haar. Thus a uniform positive density/energy floor at **all**
frequencies does not prove normality; the threshold1 in §1 is sharp as a
universal sufficient floor. The Gram inequality yields only
limsup |S_N(k)|/N<=sqrt(1-eta), as J->infinity, from such a floor.
For this particular mixture its actual Fourier means are1-eta.

This is also a deterministic orbit countermodel. For rational eta=a/b,
take a cyclic base16 de Bruijn word W_j of order j (length16^j). Form a block
V_j consisting of a copies of W_j followed by (b-a)16^j zeros, and concatenate
V_j repeated16^(j²) times, for j=1,2,... . At every fixed word length l,
the periodic V_j word frequencies tend to

    eta*16^(-l)+(1-eta)*1_(word=0^l).

Only O(bl) sites per period meet a seam, a proportion O(l/16^j). At a change
of j, the next period length is negligible compared with the previous total;
every unfinished period has negligible relative length. Thus the full, not
merely stage-end, orbit has empirical limit μ_eta. Its zero-digit frequency
is1-eta+eta/16, so it is nonnormal. It contains every finite word and hence
is not eventually periodic. Seeding the **same** BBP forcing at
s=(beta-pi)/16 produces this pure-radix boundary plus the summable authentic
tail, preserving the empirical limit. The counterseed is not the authentic0.

There is a separate finite-frequency obstruction. Uniform probability on a
q-grid, with gcd(q,16)=1 and q>15H, is invariant and has lag-energy1 at each
h=1,...,H, but zero at h=q. Finite Fourier families cannot identify Haar.
A periodic de Bruijn number has exact uniform word counts up to its order,
yet is rational and nonnormal. These controls are typed separately from the
classically normal Champernowne and Stoneham constructions.

**Coverage lemma.** Suppose disjoint windows cover N-o(N) time indices and
each has energy sum >=(1-epsilon_N) times its length for every frequency in
a fixed required repunit family, with epsilon_N->0. Nonnegativity on omitted
indices proves the full-horizon premise in (5). A family covering only theta N
indices with a constant eta lower bound gives only eta theta N total energy.
Likewise windows with |S_B|<=rho |B| covering theta N yield only
|S_N|<= [1-theta(1-rho)]N+o(N). Sparse constant savings cannot be multiplied
across unrelated windows; conditional or multiscale hypotheses are missing.

## 5. SP-05: source marks have an exact finite variation budget

Read-only sibling402, pinned `384fe179250a172c2e667c387fdb55bf9589e7a0`,
retains the authentic three positive marks d=3,4,5 with c=(2,1,1):

    p_d(a)=[c_d d/(a+d)] / sum_e[c_e e/(a+e)],  a>0.

Their limiting proportions are (6,4,5)/15. Differentiate exactly:

    p'_d=p_d[sum_e p_e/(a+e)-1/(a+d)].

Since |d-e|<=2, each reciprocal difference is at most2/(a+3)². Hence

    sum_d |p'_d(a)| <=2/(a+3)²,
    integral_A^infinity sum_d|p'_d(a)| da <=2/(A+3).              (6)

For the native clock a_n=8n-7 this bounds the **entire** future discrete
variation sum_(n>=N)||p(a_(n+1))-p(a_n)||_1 by2/(8N-4). It also bounds
||p(a_N)-(6,4,5)/15||_1 by that quantity. This strengthens sibling402's
asymptotic summability statement to a simple all-horizon effective bound.

If a declared unitary step W_n has ||W_n-I||<=L||p_(n+1)-p_n||_1,
then its ordered products converge in operator norm: a telescoping product
estimate bounds every tail by2L/(8N-4). No commutativity is needed. Thus this
precise bounded-response source-only connection has finite remaining rotation,
not an accumulating forced mixing effect. An arbitrary coupling with explicit
growing gain or selected carry dependence lies outside this statement.
The theorem is an actual source bound, but a **NON-IMPROVEMENT** for selected
fixed-frequency cancellation: the coherent seed has exactly the same marks.

The author's Harmonic/Golden/Euler–Mascheroni triangle and Oily–Macaroni
Omega_OM=phi^(-1)-gamma retain Leah/femboy2112 provenance. The original
rank-two clock has q=(3-sqrt5)/2; at three full unit channels q=(5-sqrt21)/6.
The generalized golden locus theta=lambda/(1-lambda^r) is an observer-clock
condition, not an extra equation for the arithmetic boundary. The inherited
second golden/Oily jets and the positive quartic matched-jet mutant survive.
Equation (6) is a consequence of the actual marked source; none of these
golden constants has been inserted into its derivation.

The executed exact audit reconstructs both clock roots, the inherited second
golden and Oily coefficients, and jets0..4. The positive quartic mutant agrees
through order3 but changes order4 by24 and changes the rational circle phase
at each of n=1,2,7,17,31. No assertion that this mutant is nonnormal is made.
Separately, the coherent same-original-source seed keeps *all* this source
geometry while its certified lag-energy upper bounds are below1/4 on each
of the nine preregistered window/frequency cases. This explicitly refutes a
boundary-independent signed lower bound deduced solely from that geometry.

## 6. SP-06: noncentral endpoint marks still have flat holonomy

On a time/grade lattice let t(v) be the retained actual arithmetic endpoint.
For any selected seed define the edge phase
P_(u,v)=e(h[U_(t(v))-U_(t(u))]). Every loop has phase product1, exactly.
Literal integer carries contribute integer exponent phases and do not change
this. Replacing carries by only q3/q6 orientations discards information;
the probe retains the full16 Walsh characters and the integer carry itself.

The obstruction persists for noncommuting matrices. Give each vertex any
unitary marked frame V_v and define A_(u,v)=V_v V_u^(-1). Multiplication in
chronological order telescopes around a loop toI. Frames need not commute.
The exact test uses all16 Walsh masks and noncommuting signed-permutation
frames built from authentic carries, and verifies both matrix and rational
phase holonomy on five fresh original-source squares. This is a **narrow
representation no-go**: it excludes curvature created merely by changing
endpoint coordinates. A truly edge-dependent connection not factorizable as
V_v V_u^(-1) is not covered. Its source-selected signed norm estimate is the
unpaid obligation; nonzero loop matrices alone would still not prove one.

## 7. Stoneham and approximate-grid assembly calibration

The existing c3,c5 Stoneham pulse proof is recovered in exact recurrence:
at q=c^j the unit numerator stays1 modc; ord_(c^j)(16)=c^(j-1), and each
residue in that coset occurs c(c-1) times over the complete stage. A partial
stage has no larger multiplicity. With tail <=1/[16(c-1)q], the inherited
all-horizon occupancy bound implies Haar by invariance and absolute continuity.
For c2 the stage has2^j-ceil(j/4) zero phases after its dyadic transient.
Tests include j5 and j7, preventing the previously corrected immediate-zero
mistake. These are classical normal/nonnormal calibrations, not BBP transfer.

For any proposed approximate block grid of q sites, maximum multiplicity M,
and circle error epsilon, interval I of length l satisfies

    count_B(I) <= M[q(l+2epsilon)+2].                            (7)

Summing (7) over every block touched by a horizon gives bounded density if
sum Mq=O(N) and sum M(1+qepsilon)=o(N). This repeats the precise successful
architecture; the natural BBP exact grids are already excluded by parent399's
exponential conductor theorem. Adaptive partitions still need independent
multiplicity and approximation estimates. The present spectral energy
certificate avoids that grid representation but has not supplied its own
source-verified near-unit energy premise.

Classical comparison: [Tao's Hilbert-space van der Corput discussion](https://terrytao.wordpress.com/2021/02/27/boosting-the-van-der-corput-inequality-using-the-tensor-power-trick/)
and [Bailey–Crandall, Random Generators and Normal Numbers](https://www.davidhbailey.com/dhbpapers/bcnormal-em.pdf). Proofs (1)–(7) are
given here with their hypotheses; no newer irrationality-measure claim is used.
