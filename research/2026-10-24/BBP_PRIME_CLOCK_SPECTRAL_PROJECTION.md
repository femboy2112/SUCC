# OPERATION PRIME-CLOCK SPECTRAL CRUCIBLE
## The real p-local cancellation theorem, the low-period source firewall, and the surviving high-mode interaction

**2026-10-24; SUCC research draft, no merge/main changes, no release.**
Direct parent: [BBP prime-birth PR #256](https://github.com/femboy2112/SUCC/pull/256) at \`ac3db0e7bdf684bb2e3b9ba30984c9cecafac00b\`, itself stacked on [GREENPRINT #254](https://github.com/femboy2112/SUCC/pull/254). Corrected source originates in #252. Sibling [PI Source Genesis #253](https://github.com/femboy2112/SUCC/pull/253) and [CYCLOFRAME #255](https://github.com/femboy2112/SUCC/pull/255) are compared **without importing or claiming their Lean authority**.

**PI NORMALITY (base 16, 2, 10, absolutely): OPEN. RH: OPEN. Novel independent academic priority: UNVERIFIED.** This dossier proves a nontrivial *class of twisted sums* and a concrete source-specific finite nonperiodicity theorem; it does not establish cancellation of the actual complementary source.

## 1. Recheck the original reduction and its quantifiers (CBCW-05/06)

For n>=1 the AUTHENTIC BBP source is

    r(n) = 4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    y_0=0,  y_n={16*y_(n-1)+r(n)},
    e(z)=exp(2*pi*i*z).

For p=8m+1 prime, its first p-birth is n0=m+1 with p-primary phase
4/p, and no additional p-denominator input occurs through n=4m.
Set Delta=3m, L=ord_p(16), B=Delta/L. Supplementary quadratic
reciprocity gives 16^m=1 mod p; hence L|m, B is an integer >=3.
The actual source-selected y-window decomposes UNIQUELY into Q/Z
primary and p-prime-to-primary parts,

    y_(m+1+t) = 4*16^t/p + w_(p,t) (mod 1),
    0<=t<Delta,

where the denominator of each w_(p,t) is coprime to p, and

    w_(p,t+1)={16*w_(p,t)+r(m+2+t)}.

The p-free complement is not presumed random, Haar, slowly varying,
periodic, or independent. The original absolute window sum is

    W_p(h) = sum_(t<Delta) u_t*v_t,
    u_t=e(4*h*16^t/p), v_t=e(h*w_(p,t)).

The parent PR #256's general bounded-sequence window criterion was
rederived. Because PNT in the fixed progression 1 mod 8 gives ~X/(4log X)
eligible primes, and the exceptional primes with ord_p(16)<=p^(1/3)
are O(X^(2/3)), every large fixed relative interval contains a good
window. For ANY bounded complex a_n with F(N)=sum_(n<=N) a_n,
the conditions F(N)=o(N) and F(4m)-F(m)=o(m) on those good
p=8m+1 are equivalent, by F(N)=F(floor(N/4))+o(N)
and limsup A<=A/4. There is no hidden statistical assumption.
The external PNT-AP theorem is essential to assert the scale coverage.

The Bourgain--Glibichuk--Konyagin theorem (Theorem 1.1 in
Kowalski's 2024 exposition) establishes: for fixed gamma>0 there
exist positive C_gamma,nu_gamma such that for every subgroup H of Fp*
with |H|>=p^gamma, and every nonzero a mod p,

    |sum_(x in H)e(a*x/p)| <= C_gamma*|H|*p^(-nu_gamma).

It proves cancellation of **u** on the good windows, but no bound on
the product **u*v** with the actual BBP complement. The previous
CBCW-06 identity isolates that signed debt, not a normality proof.

## 2. PSC-01 — COMPLETE CYCLOTOMIC SUBGROUP DISINTEGRATION

**Proved on paper; exact integer/Fraction oracles.**

Let d>=1 be **any divisor of Delta=3m**, not necessarily of L, and
fix h with p not dividing h. Define

    g=gcd(d,L),  L'=L/g=ord_p(16^d),  K=Delta/d,
    R=Delta/(d*L').

Then R is a positive integer, since L and d both divide Delta and
lcm(L,d)=d*L'. Each residue class of time t≡r mod d contains exactly
R copies of the complete multiplicative coset

    16^r * <16^d> in Fp*.

For any d-periodic amplitudes v_t=a_(t mod d), with |a_r|<=1, the
full mixed prime-window sum admits the exact decomposition

    sum_(t<Delta) e(4*h*16^t/p)*v_t
      = R * sum_(r=0)^(d-1) a_r *
          sum_(j=0)^(L'-1) e(4*h*16^r*16^(d*j)/p).

No approximation, random-source hypothesis or complex modulus bound
enters this equality. Its order/subgroup multiplicity is checked both
by independent direct time enumeration and finite modular group laws.

**Important cyclotomic subtlety:** d need only divide 3m; neither
d|L nor pairwise coprimality of evaluated Phi_d(16) is assumed.
Example: p=113, L=7, Delta=42 and d=3. Then g=1, L'=7,
R=2. All three residue classes are exactly two seven-point cosets,
although 3 does NOT divide L=7.

## 3. PSC-02 — NONTRIVIAL PERIODIC-COMPLEMENT POWER SAVING

**Proved conditionally on the published BGK theorem; no claim to
reprove the external deep result.**

Fix 0<gamma<1/3. Let p=8m+1 range over good primes satisfying
L=ord_p(16)>p^(1/3), p not dividing fixed nonzero h, and choose
any integer d=d_p with

    d | Delta=3m,      1<=d<=p^(1/3-gamma).

Then L'=L/gcd(d,L)>=L/d>p^gamma. Apply BGK to every complete
subgroup coset of PSC-01, with nonzero additive frequency 4h16^r.
All constants are independent of p, d, and the amplitudes a_r:

    |sum_(t<Delta)e(4h16^t/p)*a_(t mod d)|
      <= C_gamma*Delta*p^(-nu_gamma),   |a_r|<=1.   (PSC-02)

This is **genuine uniform signed cancellation in a declared class of
cross-clock interactions**. The weights may be selected adversarially,
depend on p, and be arbitrary on their d residue classes. The
essential restrictions are the complete-window synchronization d|Delta
and sufficiently small time complexity d relative to p. The authentic
BBP w_(p,t) has not been shown to satisfy either short periodicity
or small approximation error. PSC-02 by itself does NOT prove pi normal.

**Independent effective weaker alternative:** classical complete
multiplicative character Gauss sums give for every p,d with d|Delta,

    |sum_(x in H') e(a*x/p)| / |H'|
        <= min(1,sqrt(p)/L'), H'=<16^d>, a!=0.

Proof: express 1_(H') via the k=(p-1)/L' multiplicative characters
annihilating H'; the trivial additive sum equals -1, each
nontrivial Gauss sum has modulus sqrt(p). Average their k terms.
Thus every bounded d-periodic complement satisfies

    |W_p(h)|/Delta <= min(1,sqrt(p)/L').

This is fully explicit without BGK, but is only nontrivial if L'>sqrt(p).
The BGK lane genuinely goes below that classical threshold.

## 4. PSC-03 — CANONICAL PERIODIC PROJECTION AND THE TRUE HIGH-MODE DEBT

Define the time-residue conditional expectation Q_d on complex
length-Delta vectors by

    (Q_d v)_(r+j*d) = vbar_r,
    vbar_r = (1/K)sum_(j=0)^(K-1) v_(r+j*d).

This Q_d is an orthogonal self-adjoint idempotent for the normalized
time Hilbert inner product. It is the exact finite time-clock
observer; it is NOT a fictional mixing or equilibrium operator.

Decompose both u and the true complementary BBP v:

    W_p(h)/Delta =
        (1/d)sum_(r<d) ubar_r*vbar_r + J_(p,d)(h),

    J_(p,d)(h) =
      (1/Delta)sum_(t<Delta)
          (u_t-ubar_(t mod d))*(v_t-vbar_(t mod d)).     (PSC-03)

The cross terms vanish *exactly* because Q_d is an orthogonal
projection (real symmetric averaging kernel). PSC-02 proves

    |(1/d)sum_r ubar_r*vbar_r|
       <= C_gamma*p^(-nu_gamma),

whenever its good-prime and complexity hypotheses hold. Therefore
the new **centered high-mode interaction** J is the sole remaining
signed obstacle in this projection frame:

    |W_p(h)|/Delta <= C_gamma*p^(-nu_gamma)+|J_(p,d)(h)|.

This is another exact form of the missing normality problem, NOT
an unconditional assertion that J tends to zero. Unlike CBCW-06's
anchored block differences, it is insensitive to the arbitrary
choice of each period-block anchor and has a canonical Hilbert
projection. The source-basis information is preserved.

Let

    D_(p,d)(h)^2 = ||(I-Q_d)v||_2^2
                = 1 - (1/d)sum_r |vbar_r|^2.

Cauchy--Schwarz, ||u||_2=1, gives the independently checkable (but
possibly highly lossy) sufficient estimate

    |W_p(h)|/Delta <= C_gamma*p^(-nu_gamma)+D_(p,d)(h).

A genuinely BBP-source-derived **D_(p,d)->0** along a
relative-scale-dense good prime subfamily would suffice for normality.
But this is a STRONGER premise than actual signed cancellation;
even a normal source can have D close to 1. Do not rebrand
the variance condition as a necessary condition or infer it from
pi normality. A second independent proof route for J would be
needed in the high-dispersion regime.

## 5. PSC-04 — FULL SOURCE-SELECTED RATIONAL DISPERSION CERTIFICATES

**Proved all finite p,d,h; exact Fraction implementation, with
numerical checks solely for regression.**

For h integer and x,y rational, write
dist(h(x-y),Z)=min({h(x-y)},1-{h(x-y)}). For unit phases
v_t=e(h*w_t), the exact identity is

    D²=(1/(d*K²))sum_(r<d)sum_(0<=i<j<K)
          |e(h*w_(r+id))-e(h*w_(r+jd))|².

For all real z, the chord inequality (geodesic circle metric) gives

    4*dist(z,Z) <= |1-e(z)| <= (44/7)*dist(z,Z).

Therefore, with the entirely rational source-readout quantity

    S_(p,d)(h) =
       sum_(r<d)sum_(i<j) dist(h*(w_(r+id)-w_(r+jd)),Z)²,

the **true complex squared dispersion** obeys the exact rational bracket

    16*S/(d*K²) <= D²
        <= min(1,1936*S/(49*d*K²)).                   (PSC-04)

This explicitly keeps 'observed rational source distance' separate
from unknown source-selected complex cancellation. It does not
require expensive or unsafe floating-point pi digit samples.
Independent exact finite witnesses include:

| p | d | rigorous lower for D² | rigorous upper for D² |
|---:|---:|---:|---:|
| 17 | 1 | >1/2 | <=1 |
| 17 | 3 | >1/4 | <2/3 |
| 41 | 1 | >7/10 | <=1 |
| 73 | 1 | >13/20 | <=1 |

These finite nonperiodicity witnesses eliminate the false claim that
the actual complement is simply a low-time-clock source in those
windows. They do NOT imply D stays bounded away from zero as p→infinity.

## 6. PSC-05 — SOURCE-CAUSAL PERIOD DEFECT AND ITS EXACT OBSTRUCTION

**Proved paper theorem, all allowed indices; exact rational checks.**

Let n0=m+1 and 1<=d<=Delta-2 be a synchronized d|Delta.
During the p-free first-birth interval,

    w_(t+d) =
      {16^d*w_t + sum_(j=1)^d 16^(d-j)*r(n0+t+j)}.

Consequently the d-shifted defect is determined by the *actual*
source and carried p-free state:

    w_(t+d)-w_t =
      (16^d-1)*w_t
      + sum_(j=1)^d 16^(d-j)*r(n0+t+j)  (mod 1).

This is an exact observer/causal-history equation, not an
assumed autonomous finite clock. The source r(n) is strictly
positive and strictly decreasing (its previously proved positive
integral kernel gives this immediately). Here n0>=3, so for
all supported indices r(n0+t+1)<1.

Subtract the SUCC recurrence at times 0 and d:

    r(n0+1)-r(n0+d+1)
       = (w_1-w_(d+1))-16*(w_0-w_d)  (mod 1).

Using the geodesic triangle inequality on R/Z gives for any h:

    dist(h*(r(n0+1)-r(n0+d+1)),Z)
       <=16*dist(h*(w_d-w_0),Z)
          +dist(h*(w_(d+1)-w_1),Z).

For h=1 the left side is the **strictly positive** rational
difference between two decreasing forcing values, since it is
<1. Thus at least one of the two checkpoint discrepancies obeys

    max{dist(w_d-w_0,Z), dist(w_(d+1)-w_1,Z)}
       >= [r(n0+1)-r(n0+d+1)]/17 > 0.                 (PSC-05)

For fixed h!=0 the same strict positive bound holds once p is
large enough that |h|[r(n0+1)-r(n0+d+1)]<1. No exact short
time-periodic complement survives the authentic source.
**But** r(n0+1)-r(n0+d+1)=O(d/m^3) for fixed d, so the
quantitative defect may vanish. Exact nonperiodicity is not
a mixing or normality proof.

A separate elementary path-Poincare bound controls D² from the
actual source's d-step recurrence defects delta_t:
with K=Delta/d,

    D² <= min(1,(1936/49)*(K²/Delta)*
                     sum_(t=0)^(Delta-d-1) delta_t²),

    delta_t=dist(h*(w_(t+d)-w_t),Z).

Every delta_t is computed through the above source recurrence,
then independently cross-checked against direct rational state
differences. This is a sufficient certificate, often VACUOUS, not
an asserted small-defect phenomenon.

## 7. PSC-06 — THE SOURCE'S π SHADOW IS FAR SHARPER ON EACH PRIME WINDOW

The exact BBP Green identity identifies

    {16^(n-1)*pi}={y_n+T_n},
    0<T_n<B_n=1/[(8n+1)(8n+2)]<1/(64*n²).

Thus for every actual eligible prime p=8m+1, every integer h,
and its **full** window n=m+1,...,4m,

    |W_p(h;y) -
       sum_(j=m)^(4m-1)e(h*16^j*pi)|
      < (44/7)*|h|*sum_(n=m+1)^(4m) B_n
      < 11*|h|/(112*m).                               (PSC-06)

The final strict bound uses the integral comparison
sum_(n>m)n^(-2)<=1/m. This is an **unconditional,
all-prime-window, source-specific quantitative theorem**,
stronger on late windows than the parent's uniform all-prefix
bound. The finite inner sum is an explicitly computable exact
rational upper bound. After dividing by Delta=3m, the error
is <11|h|/(336m²). Consequently the selected pi orbit
and its exact rational BBP window share any claimed asymptotic
signed cancellation limit, with a sharply quantified transport
debt. **This does not estimate W_p itself.**

## 8. PSC-07 — FIXED CYCLOTOMIC CLOCKS PRESERVE PRIME-WINDOW COMPLETENESS

For every **fixed positive integer d**, restrict to primes

    p≡1 mod (8*d),      L_p>p^(1/3).

Then m=(p-1)/8 is divisible by d, hence d|Delta and PSC-01
holds without a subsequence/order mismatch. PNT in the fixed
progression 1 mod 8d gives ~X/(phi(8d)*log X) primes.
Deleting the exceptional O(X^(2/3)) retains prime windows
in **every sufficiently large fixed relative interval**.
Thus the parent scale-four lemma still yields:

    pi base-16 normal
      IFF W_p(h)=o(m) for all fixed nonzero h
          along this synchronized prime family.

The same holds with any fixed progression ensuring d|3m
and coprime residue class. This is a **reduction theorem**,
not proof that its limiting premise holds.

Combining PSC-03 gives a new properly scoped source-specific
CONDITIONAL proof contract:

    If for one fixed d>=1 and all h!=0,
       J_(p,d)(h)->0
    on the synchronized good primes p≡1 mod8d,
    then pi is normal in base 16.

A still stronger sufficient condition is D_(p,d)(h)->0.
The existing source-causal PSC-05 proves only D>0 at
finite windows, not D->0 or any J decay. Conversely normality
does not require D->0. The signed high-mode correlation
is the outstanding obstruction.

## 9. PSC-08 — ONE-MODE RESONANT COUNTERCONTROL, WITH QUANTIFIED DEPTH

For every good p and h not divisible by p take the *fake* p-unit
complementary complex sequence

    v_t^res = e(-4h*16^t/p).

Then u_t*v_t^res=1 for **every** t: W_p/Delta=1.
Its exact time period is L=ord_p(16), which satisfies L>p^(1/3),
so it cannot lie in the low-period class d<=p^(1/3-gamma).
Moreover for every qualifying short d, the low-mode energy is

    (1/d)sum_r |ubar_r|² <= C_gamma²*p^(-2nu_gamma).

Consequently J_(p,d)^res tends to 1, not zero: the full
counterfeit coherence resides in high modes that source-agnostic
clock averaging cannot eliminate.

This comparison is NOT the actual p-prime-to-primary rational
BBP w_(p,t) (it also has a p denominator); it is an exact
adversarial *complex-weight* control for the analytic theorem,
which permits arbitrary bounded amplitudes. A separate authentic
p-free denominator counterfeit appears in parent #256.
Do NOT claim a p-free source counterexample when using this
single-frequency resonant control.

## 10. What was validated, and what would change the verdict

- Original #256 first-birth source, prime order, p-primary phase and selected w are read unmodified.
- PSC-01 structural coset periods are integer identities, with an independent direct-time oracle.
- PSC-04, PSC-05 and PSC-06 use **only exact integer/Fraction** witnesses; finite numerical complex phases, if displayed, are explicitly non-proof regression.
- The big subgroup saving is **external published mathematics**; finite code cannot establish its unknown C_gamma,nu_gamma.
- None of the new paper theorems is asserted to be Lean checked. Parent and sibling Lean claims retain their own SHA/provenance.
- The existing signed-Weyl normality criterion is not being replaced with a generic variance or Haar assumption.

**Next discriminating source experiment:** compute the actual p-free complementary time-series profile v_t for enough authentic good p, measure its **centered SIGNED** J_(p,d)(h) (not merely the absolute defect D) using independent rational phase/interval oracles, and inspect Fourier spectra on complete cosets. Vary d over synchronized divisors of Delta, including both d<<L and d~L, without changing source values. A real new pi theorem requires a uniform-in-p bound on this selected signed high-mode overlap or an independent source property implying it. No finite trend promotes to asymptotic fact. Any candidate 'p-free denominator alone implies cancellation' must face the parent #256 coprime-clock counterfeit.

## References and claim ledger

- Bourgain–Glibichuk–Konyagin, *Estimates for the Number of Sums and Products and for Exponential Sums in Fields of Prime Order*, J. London Math. Soc. 73 (2006) 380–398, DOI 10.1112/S0024610706022721. Source of subgroup power saving, **not** a claim about the actual BBP complement.
- Kowalski, *Exponential sums over small subgroups, revisited* (2024), arXiv:2401.04756, Theorem 1.1 gives the precise imported gamma/nu quantifiers.
- Fixed-modulus prime number theorem in arithmetic progressions (standard classical theorem), applied specifically modulo 8d.
- Classical multiplicative-character Gauss sums, Weil and elementary Hilbert projection/finite cyclic orthogonality.
- SUCC #252, #254, #256 source ancestry; #253 and #255 are cross-references only.

| ID | Verdict | Proof boundary |
|---|---|---|
| PSC-01 | DISCLOSED (paper) | Exact subgroup disintegration for d|Delta |
| PSC-02 | CORROBORATED externally + derived | BGK power saving for *bounded periodic complementary weights*, not arbitrary BBP v |
| PSC-03 | DISCLOSED (paper) | Orthogonal decomposition; signed J decay UNVERIFIED |
| PSC-04 | DISCLOSED (paper) / exact tested | Rational finite-source variance bounds |
| PSC-05 | DISCLOSED (paper) / exact tested | Strict source-forcing period mismatch, asymptotic saving NOT supplied |
| PSC-06 | DISCLOSED (paper) / exact tested | Uniform O_h(1/m) true-pi shadow error on source prime windows |
| PSC-07 | DISCLOSED (paper) with external PNT-AP | Relative-scale dense synchronized clocks |
| PSC-08 | DISCLOSED (paper) | Countercontrol outside authentic complementary source class |
| Actual J_(p,d)(h)->0 or I_p(h)->0 | **UNVERIFIED** | No all-horizon signed source bound obtained |
| Pi normality | **OPEN** | All Fourier frequencies still require new source-specific estimates |
| Independent academic novelty | **UNVERIFIED** | Prior-art review required |

The apparatus is an exact source-to-cyclotomic-observer bridge plus a sharp
classification of one tractable class of interference; it is not a proof
of the unsolved normality assertion.


## 11. PSC-09 — CERTIFIED SELECTED COMPLEX HIGH-MODE WITNESSES

**New finite source-authenticated result; rigorous exact-rational complex boxes,
NOT a numerical conjecture about growing primes.** This section uses the
separate \`observational_succ/bbp_prime_window_signed_intervals.py\` with
\`tests/test_bbp_prime_window_signed_intervals.py\`.

The actual finite source phase y_n and p-free split w_(p,t) are rational;
their circle characters are roots of unity, but their real and imaginary
values involve pi. We obtain pi independently from the classical Machin
identity pi=16 arctan(1/5)-4 arctan(1/239). The alternating arctan series
provide two **exact rational** outer bounds. To evaluate e(z) for a rational
z, first center z modulo one in [-1/2,1/2] (exact Fraction), multiply by
the midpoint of the authentic pi interval, then enclose cos/sin using
the degree-(2K-1) Taylor polynomials. By the bound |d^n sin|,|d^n cos|<=1
and |angle|<=pi<22/7, each Taylor remainder is bounded by the rational

    (22/7)^(2K)/(2K)!,

plus the pi-interval displacement |z|*(pi_upper-pi_lower).
No machine float and no uncharged rounding participates in the
certificate; complex sums are rectangles with rational endpoints.

For a synchronized period d|Delta and h=1, compute the **signed source**
coefficient directly, not from an ensemble or Haar model:

    A = W_p(1)/Delta
      = (1/Delta)sum_(t<Delta) e(4*16^t/p+w_t),

    LOW = (1/(d*K²)) sum_(r<d)
             sum_(i≡r mod d) sum_(j≡r mod d)
                  e(4*16^i/p+w_j),   K=Delta/d,

    J_(p,d)(1)=A-LOW.

Every summand is an exact rational-phase input to the rigorous complex
box oracle. The target square modulus is bounded by rational distances
from the resulting real/imaginary box to zero; no sqrt approximation
or float eigenvalue is promoted to mathematical authority.

The committed oracle and new focused tests give the following strict
actual-source finite certificates:

    |W_17(1)|²/(6²) > 1/9,
    |J_(17,1)(1)|² > 1/16,

    |W_41(1)|²/(15²) > 1/50,
    |J_(41,3)(1)|² > 1/100.

These prove that the **genuine selected** BBP complementary high-mode
interference can be nontrivial, independently of the p-only Galois RMS
or absolute dispersion lower bounds. They do NOT assert a lower bound
for all sufficiently large p: both normalized quantities might still
tend to zero. In fact their existence at small p is fully compatible
with the sought normality conjecture. This is a deliberately finite,
source-specific positive control demonstrating that the signed
measurement apparatus can detect the missing interaction.

The primary \`bbp_prime_window_projection.py\` records an independently
rational lower/upper certificate of D²; this companion oracle is
different in both observable (J complex versus D² real) and numerical
representation (certified Machin/Taylor versus exact circle distances).
Both depend on the same authenticated BBP forcing; they are not
independent witnesses for an all-p asymptotic theorem.

**Claim label:** PSC-09 DISCLOSED (paper analytical enclosure +
finite exact-rational implementation, final-head hosted tests
required); nonzero finite J for (17,1) and (41,3), with no infinite
normality conclusion.
