# OPERATION CYCLOFRAME — Gauge-covariant circle origins, cyclotomic clocks and signed BBP phase reconstruction

**2026-10-24. Research-only, stacked on pi Source Genesis PR #253 at exact commit 2ab8a8527b7ba3f990d75fd618a4bfd034b26b4b.** Explicit sibling comparison: GREENPRINT PR #254 at fceb04645926898bb5f72346dca54f3134b06cea; Circle Genesis #247, Secondary Circle #248, Circle Time-Carry #249. NO silent merge of sibling branches, rewrite of imported archives, changes to main or publication. No proof of base-16, base-2, base-10 or absolute pi-normality. Independent academic priority UNVERIFIED.

## Research question and definitions

The maintainer proposed that a circle can be viewed as a real line with identified endpoints (or a real line with its infinity moved by a projective chart); origins may be freely redefined. Grow several suitably correlated origin samples under SUCC, then quotient their trajectories. Does origin invariance bound relative dynamics strongly enough to force normality of the *source-selected* pi orbit?

**Two distinct circle models must not be conflated.** The affine *quotient circle* is X=R/Z, obtained by identifying 0 and 1 in [0,1]; it has canonical addition and rotations after choosing its affine group structure. The *projective circle* RP¹=R∪{∞} is the one-point compactification of R obtained by identifying the two ends of a two-ended compactification. It is homeomorphic to a circle but the transported coordinate addition/rotation laws are not the ordinary real-line addition. A Möbius chart change generally conjugates a chosen dynamical rule to a different coordinate formula. Topological indistinguishability does not automatically imply SUCC dynamical invariance.

Throughout set b=16, T_b(x)={b*x}, e(t)=exp(2*pi*i*t), h a fixed nonzero integer Fourier character, and x the **source-selected** real circle phase, e.g. x={pi}. All identities have elementary general-b analogues for integers b>=2.

## CF-01 — EXACT GAUGE COVARIANCE, AND THE REFUTED "SAME LAW IN ALL ORIGINS" IMPLICATION

Let R_a(x)=x+a mod1. In the chart z=x-a, the transported map is

    (R_-a T_b R_a)(z) = b*z+(b-1)*a mod1.

Therefore a change of chart preserves physical SUCC dynamics for every real circle point, but preserves the *literal, unmodified coordinate formula* z↦b*z precisely for

    (b-1)*a = 0 mod1.

For b=16, this literal symmetry/stabilizer has **15** rotations a=k/15, k=0,...,14. The original proposal's full circle-origin freedom is valid as a CHART FREEDOM (conjugacy), not as an extra commuting SO(2) symmetry of T_16.

For physically distinct initial points x+a and x+c grown with the same unmodified rule,

    T_b^j(x+a) - T_b^j(x+c) = b^j(a-c) mod1.

The initial x cancels identically. Consequently **all probes that observe only relative translated-point histories, with no authenticated absolute/source anchor, give identical readouts for x=pi and x=0** (or any other x). Geodesic distance on X is <=1/2 but is merely compactness, not contraction or Fourier mixing; on a lifted real line the difference is b^j(a-c), which is generally unbounded. The expanding derivative has magnitude b, not 1.

Examples: for a-c=1/15, the difference is fixed; for 1/17 it alternates between 1/17 and 16/17; for 1/7 it has exact period three. Such bounded/periodic differentials do not imply a normal orbit. **REFUTED:** circle origin invariance alone yields any nontrivial selected-phase normality bound.

The authentic BBP forced trajectory y_(n+1)={16*y_n+r(n+1)} must obey, in the shifted chart z_n=y_n-a,

    z_(n+1)={16*z_n+15*a+r(n+1)}.

Changing y_0 to a while leaving the forcing untouched instead constructs a different physical/source-selected orbit. This source/coordinate distinction was already essential in the repair PR #252 and the Lean-verified parent #253.

## CF-02 — CYCLOTOMIC CLOCKS MAKE "CLEVER MULTIPLE ORIGINS" EXACT

Let q>=2 satisfy gcd(b,q)=1 and let d=ord_q(b) (least d>=1 with b^d≡1 mod q). Sample **q correlated origins**

    x_a=x+a/q,  a in Z/qZ.

Write

    v_j(x)=e(h*b^j*x),     F_j(a;x)=v_j(x)*exp(2*pi*i*h*b^j*a/q).

The time-j origin-sample has an exact modular character label h*b^j mod q. The orthogonality of these finite Fourier characters gives

    (1/q)sum_(a mod q) F_j(a;x)*conj(F_k(a;x))
      = v_j(x)*conj(v_k(x))*1_{q | h*(b^j-b^k)}.         (1)

If gcd(h,q)=1, the indicator is exactly 1_{j≡k (mod d)}. If h is not coprime, replace q by q/gcd(q,h) and d by the multiplicative order in that reduced modulus (period one for modulus one). No randomness, floating point, Haar inference or pi digits are used here.

The underlying rational-periodic origin grid may be taken as q=b^d-1; then its exact period is d since 0<b^e-1<q for 0<e<d. The cyclotomic identity

    b^d-1=prod_(m|d)Phi_m(b)

supplies modular clocks, but **evaluations Phi_m(b) and Phi_n(b) need not be pairwise coprime**. In particular at b=16, d=3,

    16^3-1=4095=Phi_1(16)*Phi_3(16)=15*273,
    gcd(15,273)=3.

Blind CRT over distinct cyclotomic *factors* would lose the shared 3-primary carrier. True Chinese remainder factorization is via relatively prime moduli, notably the full prime-power components.

The smallest detected order-d clocks for b=16 and d=1..7 are:

| d | least q | large naive grid q_full=16^d-1 | arithmetic witness |
|---:|---:|---:|---|
| 1 | 3 | 15 | 16≡1 mod3 |
| 2 | 17 | 255 | 16≡-1 mod17 |
| 3 | 7 | 4095 | 16≡2 mod7, order3 |
| 4 | 257 | 65535 | 16⁴≡1 mod257, no lower proper order |
| 5 | 11 | 1048575 | 16≡5 mod11, order5 |
| 6 | 119 | 16777215 | 119=7*17, order lcm(3,2)=6 |
| 7 | 29 | 268435455 | 16 has order7 mod29 |

The table is **finite exact arithmetic**; no claim that these q yield any normality estimate. A composite clock can beat a single Phi_d prime factor: q=119 has period six even though 119 does **not** divide Phi_6(16)=241. Its time period is obtained by the Chinese remainder fusion of the 7-clock and the 17-clock.

## CF-03 — A CONDITIONAL EXPECTATION ON TIME-INTERFERENCE

For a finite horizon N, define diagonal unitaries on C^N,

    D_a(j,j) = exp(2*pi*i*h*b^j*a/q).

The origin twirl is the **completely positive, unital, trace-preserving conditional expectation**

    E_q(A)=(1/q)sum_(a modq) D_a A D_a^*.

For gcd(h,q)=1 and ord_q(b)=d, its entrywise action is

    (E_q(A))_(j,k)=1_{j≡k mod d} A_(j,k).           (2)

It projects onto the block-diagonal time algebra
direct-sum_(r mod d) M_(number of times j≡r mod d). It is idempotent in the matrix-operator sense: E_q²=E_q. Positive matrices remain positive. This is *exact arithmetic source/timing discrimination* from coherent origin sampling, **not a statement that each physical orbit mixes.**

For two clock moduli q1,q2 coprime to b and arbitrary h,

    E_q1 E_q2 = E_lcm(q1,q2),

because simultaneous divisibility conditions are equivalent to divisibility by their lcm. Their effective time periods fuse by lcm. If q1,q2 are coprime, the finite cyclic source grid has the additional genuine CRT product identification. If not, (2) still fuses but no false disjoint-prime representation is allowed. In particular E_7 E_17 = E_119 at b=16 and h coprime to 119, isolating **time congruence modulo six**. This is a concrete SUCC/FUCC prime-clock composition theorem.

The Schur/Hadamard product of the two period kernels is K_lcm(d1,d2). It is positive semidefinite by the Schur product theorem. There is **no unproved Loewner ordering** between distinct period kernels. The positivity here is an ordinary finite Hilbert-space Gram fact and does not establish completed Weil positivity.

## CF-04 — POSITIVE PHASE-MODULATED ENERGIES RECONSTRUCT THE SIGNED CYCLOTOMIC LAGS

This is the principal constructive result. Set d=ord_q(b), gcd(h,q)=1 and v_j=e(h*b^j*x). Define the **nonnegative observable**

    E_(q,N)(theta;x)
      = (1/q)sum_(a=0)^(q-1) |
          sum_(j=0)^(N-1) exp(i*theta*floor(j/d)) *
                   e(h*b^j*(x+a/q)) |^2.               (3)

Let L=floor((N-1)/d), N>=1, and use E=0 for N=0. Orthogonality (1) implies

    E_(q,N)(theta;x)
      = sum_(r=0)^(d-1) |
          sum_(t: r+td<N) exp(i*t*theta)*v_(r+td) |^2.

Expand it as the exact real Laurent polynomial

    E_(q,N)(theta;x)
      = N + sum_(ell=1)^L [ C_(ell*d)(N;x)*exp(i*ell*theta)
                           + conj(C_(ell*d)(N;x))*exp(-i*ell*theta) ],
                                                               (4)

where the **original signed cyclotomic lag correlation** is

    C_m(N;x)=sum_(j=0)^(N-1-m) e(h*(b^m-1)*b^j*x), m<N.

Thus **the signed imaginary phase has not been discarded**: it is encoded as the sine coefficient of a family of real, nonnegative energies.

Let K>=2L+1 and theta_s=2*pi*s/K. Exact discrete Fourier inversion gives, for 0<=ell<=L,

    C_(ell*d)(N;x)
      = (1/K)sum_(s=0)^(K-1)
          E_(q,N)(theta_s;x)*exp(-i*ell*theta_s).          (5)

For ell=0 the coefficient is N. No aliased +/- Laurent modes occur when K>2L. This works for **every** x, not only pi. The tested d=3, q=7, N=10 frame reconstructs C_3,C_6,C_9 from only q=7 origin samples and K=7 temporal modulation phases, compared with a naive full-grid q=4095. For d=5, q=11 and N=15, K=5; its temporal lags are 5 and 10. This is a constructive Fourier/probe-compiler improvement, not an all-horizon decay theorem.

A related exact positivity constraint is

    E(theta)>=0  for every theta,
    Re sum_(ell=1)^L exp(i*ell*theta) C_(ell*d)(N;x) >= -N/2.

The resulting Toeplitz matrix made from these Fourier coefficients is positive semidefinite, because it is a Gram integral against the nonnegative function E(theta). This is a **generic** constraint on arbitrary unit-circle sequences. The periodic x=0 witness satisfies it, so a positive energy certificate alone cannot prove pi normality.

## CF-05 — HAAR MOMENTS, SOURCE-SELECTED OBSTRUCTION, AND FALSE "BOUNDED DIFFERENTIAL" TEST

Write N=a*d+s with 0<=s<d. Each residue class contributes n_r=a+1 for r<s or a otherwise. Let

    P= sum_(r=0)^(d-1) binom(n_r,2).

For a fixed nonzero h, integration over the **independently Haar-random base phase x** (NOT the q-translation orbit of a fixed pi) yields the exact identities

    HaarMean[E(0;x)] = N,
    HaarVar[E(0;x)]  = 2P.                                (6)

Proof: E=N+2sum_(j>k, j≡k mod d) cos(2*pi*h*(b^j-b^k)*x).
All positive integer frequencies b^j-b^k for j>k are distinct: in
b^k*(b^(j-k)-1) the second factor is coprime to b, fixing k, then j.
All distinct nonzero trigonometric characters are Haar orthogonal, each cosine square has mean 1/2. No ergodicity rate or pi assumption enters.

For x=0 or x=1/3 with b=16, the phase v_j is constant and the frame energy instead attains the maximal value

    E(0;x) = sum_r n_r² = N+2P.                             (7)

In particular **periodic nonnormal orbits have all the same origin covariances and bounds as the source-selected pi orbit**; the actual signed phase values must be measured or proved to cancel.

A more deceptive problem: for **every source x and every choice d>=N**, each time index occupies a different residue block. Therefore

    E_(q,N)(theta;x)=N EXACTLY for all theta and x.

Even if d=d_N grows more slowly than N, the universal bound

    0<=E_(q,N)(0;x)<=N*ceil(N/d_N)
    implies E/N²<=1/d_N+1/N -> 0 if d_N->infinity,

for **every x**, including x=0 and x=1/3. Hence the superficial criterion
"E/N² tends to zero as we sample increasingly many origins" is **REFUTED**, not a normality theorem.

Cauchy–Schwarz gives the only immediate correct Weyl control,

    |(1/N)sum_(j<N)v_j|² <= d*E_(q,N)(0;x)/N².              (8)

Any source-bound intended to force normality through these frames must improve E to o(N²/d) for all fixed h (with honest quantifiers), rather than merely inherit the automatic O(N²/d) maximum. This is a possible source-specific proof obligation, **not a proof**.

Haar Chebyshev calibration: for any threshold t>0,

    HaarProb(|E(0;x)-N|>=t) <= 2P/t².

This is a genuine ensemble statement, not a probability distribution assigned to the fixed mathematical constant pi. Randomly selecting origins on the *same* π phase grid does not constitute independent Haar sampling of x.

## CF-06 — BBP-SPECIFIC SIGNED TRANSPORT SURVIVES CYCLOTOMIC FRAME RECONSTRUCTION

This branch is stacked on validated PI Source Genesis #253, which extends authentic source #252. Define

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),
    T_n=sum_(k>=1)16^(-k)r(n+k),
    y_0=0, y_(n+1)={16*y_n+r(n+1)}.

Then **exactly** x_j={16^j*pi}={y_(j+1)+T_(j+1)}, with
0<T_n<[(8n+1)(8n+2)]^(-1) and strictly decreasing T_n. For every lag m and window N>m:

    C_m(N;pi)-D_m(N)
      = sum_(j=0)^(N-1-m)
         [e(h*(y_(j+m+1)-y_(j+1)+T_(j+m+1)-T_(j+1)))
          -e(h*(y_(j+m+1)-y_(j+1)))],

where D is the **signed** Fourier sum for the rational forced SUCC phase differences, not an absolute prime-path majorant.

By the phase Lipschitz inequality and T_(j+m+1)<=T_(j+1),

    |C_m-D_m|
      <=2*pi*|h|*sum_(j<N-m)(T_(j+1)-T_(j+m+1))
      <=2*pi*|h|*sum_(j>=0)T_(j+1).

The parent #253 proves sharper rigorous estimates and Lean-verified transport, including a lag/horizon independent analytic upper bound pi*|h|/30; the executable source adapter uses its **rational** function lag_transport_budget(h,1,N-m,m), which is <= 2*|h|/15 for all m,N. This is a comparison estimate, NOT an upper bound on |D_m| or |C_m| themselves.

Combining (4) with the authentic BBP bounds gives for every q of order d and every N:

    |E_(q,N)(0;pi)-E_(q,N)(0;forced)|
      <= 2 sum_(ell=1)^floor((N-1)/d)
                   lag_transport_budget(h,1,N-ell*d,ell*d)
      <= 4|h|/15 * floor((N-1)/d).                         (9)

The finite source-lag budget can improve the last simple bound. More importantly, **Fourier inversion (5) transports each *individual signed lag* with its unchanged, lag-independent source-bound**, rather than multiplying it by 16^(ell*d). It is a source-typed compiler from positive cyclotomic observables back to the *actual signed missing quantity*.

For source-faithful, finite π-specific observations the committed adapter evaluates (4) with independent, outward-rational BBP and Machin interval oracles from #253. The finite enclosures pay their source precision; they cannot license N->infinity. Source information enters through actual r(n), T_0=pi/16 and y_0=0. A generic periodic origin x=1/3 fails that complete source contract.

### CF-06a — New finite, independently source-enclosed π energy witness

For q=7, d=3, N=7, h=1, theta=0 the root-frame energy is exactly

    E_(7,7)(0;pi) = 7+2*Re[C_3(7;pi)+C_6(7;pi)].

The original BBP source interval and the independently derived Machin/arctangent
source interval, each with the full signed phase and outward rational
Taylor/Lipschitz error in PI Source Genesis #253, **both certify**

    199199/50000 < E_(7,7)(0;pi) < 498/125,
    equivalently 3.98398 < E < 3.98400.

The *same* positive root-frame observable for x=0 or x=1/3 is
N+2P = 17 exactly, while the independently Haar-averaged expected
value is 7 (variance 2P=10). The bound is a genuine **finite**,
π-selected signed-interference measurement from two authenticated
analytic constructions; it is neither a computed list of π digits
nor evidence that these finite inequalities hold at future horizons.
Its sole purpose is to demonstrate a working source-specific probe
that can actually discriminate this π finite window from periodic
countermodels, without replacing the target by a generic Haar ensemble.
The exact new rational bracket is enforced in the focused test suite.


## CF-07 — Source-accurate adversarial controls, limits and transport boundary

**Refuted:** arbitrary origins commute with unmodified x→16x. Counterexample a=1/7.

**Refuted:** compact circle-distance bounds imply contraction or mixing. Counterexamples x=0, x=1/3, offsets 1/15, 1/17 and 1/7.

**Refuted:** relative translated-orbit histories identify pi. x cancels identically and x=0 shares the exact same relative transcripts.

**Refuted:** Fourier averaging over q origins proves normality. It can erase all single-time harmonics for **every** x; the periodic control passes. The residual positive multi-time energy isolates periods but is not automatically small.

**Refuted:** different cyclotomic polynomial values are pairwise CRT-independent: gcd(Phi_1(16),Phi_3(16))=3.

**Refuted:** a growing rank d_N with E/N²->0 certifies normality. This bound holds universally; source-specific gain of order o(N²/d_N) is necessary in (8).

**Corroborated in code, paper proof (no new Lean):** exact chart conjugacy, cyclotomic character orthogonality, clock fusion, positive-energy signed-lag inversion, Haar mean/variance, rank/dimension and source-typed rational BBP lag transport. All are sourced from classical structures, independently exact-checked at finite instances. The separate Lean declarations in #253 retain their own explicitly reviewed authority, not inherited by our new results.

**Academic novelty:** UNVERIFIED. Discrete Fourier/finite-group character projectors, cyclotomic factorization, ergodic/Weyl character criteria, Haar orthogonality and the Bailey–Crandall forced-orbit characterization are classical. The SUCC packaging supplies a mathematically typed, executable, source-controlled bridge, not a claim of discovering a new theorem about normality.

## Research payoff and next verdict-changing instrument

The user's sample-point intuition becomes a genuine source-faithful construction:

    authenticated pi BBP forcing + origin translations
      -> finite cyclotomic q-clock / CRT fusion
      -> completely positive SUCC time twirl
      -> temporal modulation / positive energy samples
      -> EXACT signed lag recovery (no lost imaginary phase)
      -> rigorously bounded rational forced-shadow approximation.

What is still missing is an estimate **not already implied by universal group symmetry**. In exact terms, prove from the specific rational BBP forcing (not Haar sampling, not a generic positive Green source) that for a declared growing period family d_N and each h!=0,

    E_(q_N,N)(0;pi) = o(N²/d_N)

or more directly for even **one fixed frequency h**,

    sum_(j<N) e(h*16^j*pi) = o(N).

Both are currently **UNVERIFIED**. The first criterion would imply full normality only if quantified over all nonzero h; a single frequency is a meaningful limited target but cannot prove normality. The candidate lemma's decisive falsifier is the exact constant-orbit source x=1/3 (plus the pi Source Genesis #253 positive-Hankel/near-BBP periodic counterfeits), which satisfies circle chart invariance, clock fusion and all the universal energy positivity constraints yet has large cyclic correlations.

**Status:** rigorous instrument + exact source transport + hard counterexamples, not π normality. Next round should attack the authenticated *rational BBP forced phase sums* using arithmetic conductor/CRT and the corrected full prime-source contracts, rather than infer cancellation from symmetry.
