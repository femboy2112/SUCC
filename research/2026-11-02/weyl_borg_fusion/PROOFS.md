# Operation WEYL BORG: full Fourier / carrier interface for the selected BBP source

**2026-11-02. PAPER-PROVED identities and elementary bounds; finite Fraction probes.**
**NOT a proof of π normality or RH.** Branch starts at Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. The original four signed poles, literal zero seed, existing historical claims, production, formal kernel, workflows and provenance remain untouched.

## WB-01. Recover the exact object and gate

Let e(t)=exp(2πit). Keep precisely

    r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)
        =(120n²-89n+16)/[(2n-1)(4n-1)(8n-7)(8n-3)]
    U_0=0, U_n=16U_(n-1)+r(n), n>=1,
    S_N(h)=Σ_(n=1)^N e(hU_n).

The original BBP identity is π/16=Σ_(j>=1)16^-j r(j). With its positive future source tail

    T_n=Σ_(j>=1)16^-j r(n+j),

exact geometric convolution gives

    U_n=16^(n-1)π-T_n, n>=1.                       (1.1)

Existing SUCC source transport (SGO) pays an absolutely summable T_n and proves that for fixed nonzero integer h, S_N(h)/N has the same asymptotic as Σ_(n<=N)e(h16^(n-1)π)/N. Classical Weyl therefore gives the exact equivalence

    π base-16 normal  <=>  S_N(h)=o(N) for EVERY FIXED h in Z\{0}.  (1.2)

This is the selected signed Weyl gate, NOT an established signed estimate. Existing formal/duck_pi/WeylBridge.lean proves a character-to-continuous-Haar implication with the missing character cancellation as hypothesis. Weyl equidistribution, finite Heisenberg–Weyl relations, and the Weil RH positivity test are distinct objects: shared Fourier vocabulary does not make them interchangeable.

## WB-02. Exact character-valued finite-cell / real-residual gluing

For any sample x∈[0,1), integer M>=1, put

    a=floor(Mx) in {0,...,M-1}, s=Mx-a in [0,1), x=(a+s)/M.

For every h,q∈Z, with no approximation and including moving aliases,

    e((h+qM)x)=e(ha/M)e((h/M+q)s).                  (2.1)

For original SUCC, x_n={U_n} and both a_n and s_n are exact rationals. Hence the map from original unwrapped rational source to REAL-circle characters factors through a finite cell PLUS its residual, never just through a 16-adic residue. The finite character clock C_h|a>=e(ha/M)|a>, shift S_b|a>=|a+b> obey C_h S_b=e(hb/M)S_b C_h, but that relation does not itself supply e(hU_n). SUCC AQC-04 proves that a continuous universal 2-adic→real-circle character extension cannot exist.

For the empirical selected orbit set

    p_a = #{n<=N:a_n=a}/N,
    w_(a,h) = (1/N)Σ_(n:a_n=a)e(hs_n/M),
    g_M(h)=∫_0^1 e(hs/M) ds,
    d_(a,h)=w_(a,h)-p_a g_M(h).

For every h!=0, (1/M)g_M(h)Σ_(a=0)^(M-1)e(ha/M)=0: if M does not divide h the geometric sum vanishes; if M divides h, h!=0, then g_M(h)=0. Therefore the **exact, signed** decomposition is

    S_N(h)/N =
       g_M(h)Σ_a e(ha/M)(p_a-1/M)
       + Σ_a e(ha/M)d_(a,h).                        (2.2)

Define the signed within-cell cofiber

    C_(N,M)(h)=Σ_a e(ha/M)d_(a,h)

and the nonnegative energy E_(N,M)(h)=Σ_(a:p_a>0)|d_(a,h)|²/p_a (d=0 when p=0). By Cauchy and Σ p_a=1,

    |S_N(h)/N| <= Σ_a |p_a-1/M|+sqrt(E_(N,M)(h)).   (2.3)

Equation (2.2) is an information-preserving Fourier representation; (2.3) is a legitimate **sufficient conditional** estimate. Neither supplies source-specific decay of C or E. The CRE-04 observation-resolution ceiling continues to apply to any attempt to prove growing-resolution entropy is automatically maximal.

High-alias false-positive: take M points x_a=a/M, each cell occupied once. Then p_a=1/M and cell entropy is exactly log M, but e(Mx_a)=1 for every a. Shift each point to x_a=(a+1/2)/M, keep identical p_a, and e(Mx_a)=-1 for every a. The missing information is precisely the within-cell real phase. This is also a decisive test of wrong sign/carry conventions. Frequencies h+qM are covered exactly by (2.1), with no unproved interpolation of high modes.

## WB-03. All-index exact-rational Green-tail curvature

Let (w_i,a_i)=(4,7),(-2,4),(-1,3),(-1,2), so r(m)=Σ_i w_i/(8m-a_i). Then

    Σ_i w_i=0, Σ_i w_i a_i=15, Σ_i w_i a_i²=151,
    Σ_i |w_i|a_i²=241, Σ_i |w_i|a_i³=1535.

For m>=2, a_i/(8m)<=7/16. The exact geometric-series remainder after 1/m² and after 1/m³ yields

    |r(m)-15/(64m²)| <= 241/(288m³),               (3.1)
    |r(m)-15/(64m²)-151/(512m³)| <=1535/(2304m⁴). (3.2)

Because the original combined numerator and denominator are positive for positive integers, r(m)>0. For m>=2, (3.1) moreover implies r(m)<=(15/64+241/576)m^-2=(47/72)m^-2<m^-2.

The geometric moments are exact:

    Σ_(j>=1)16^-j=1/15,
    Σ j16^-j=16/225,
    Σ j²16^-j=272/3375.

For all n,j>=1, Taylor's theorem on [n,n+j] gives

    |(n+j)^-2 - n^-2| <=2j/n³,
    |(n+j)^-2 - n^-2 +2j/n³| <=3j²/n⁴,
    |(n+j)^-3 - n^-3| <=3j/n⁴.

Insert (3.1) into T_n=Σ 16^-j r(n+j) to find, for every n>=1,

    τ_2(n)=1/(64n²),
    |T_n-τ_2(n)| <= C_3/n³,
    C_3=(15/64)*2*(16/225)+(241/288)*(1/15)
       =1/30+241/4320=77/864.                    (3.3)

The next exact coefficient is

    -(15/64)*2*(16/225)+(151/512)*(1/15)=-7/512.

Insert (3.2) and both higher Taylor bounds to obtain

    τ_3(n)=1/(64n²)-7/(512n³),
    |T_n-τ_3(n)| <= C_4/n⁴,
    C_4=(15/64)*3*(272/3375)
       +(151/512)*3*(16/225)
       +(1535/2304)*(1/15)
       =17/300+151/2400+1535/34560
       =28339/172800 < 1/6.                     (3.4)

The global inequalities do not follow from sampling n: the exact rational algebra and Taylor bounds above prove them. An independent staged Fraction tail enclosure uses Σ_(j>L)16^-j r(n+j) <=16^-L/[15(n+L+1)²] for n>=1 and verifies many exact instances; it does not supply the universal proof. The older CRE-07/08 has an all-order *lag* Laurent expansion; these explicit constants are specialized for the direct *moving-frequency Weyl* transport below, not claimed as a new general Laurent series discovery.

## WB-04. Quantitative growing-harmonic Weyl phase transport

For d=2,3 define the Laurent-corrected π Weyl average

    V_(N,d)(h)=(1/N)Σ_(n=1)^N
                 e(h(16^(n-1)π-τ_d(n))).

By (1.1), (3.3)–(3.4), |e(u)-e(v)|<=min(2,2π|u-v|), and Σ_(n>J)n^(-d-1)<=1/(dJ^d), **for every** N>=1, integer h, and integer 1<=J<=N,

    |S_N(h)/N-V_(N,d)(h)|
      <= 2J/N + 2π C_(d+1)|h|/(d N J^d).          (4.1)

The first J phases are discarded at worst-case cost 2J/N; every remaining phase is paid by the exact original-source Laurent bound. Let H_N>=1 be an integer frequency budget with H_N=o(N^(d+1)); choose J_N=ceil(H_N^(1/(d+1))), eventually <=N. Uniformly for all integers |h|<=H_N,

    |S_N(h)/N-V_(N,d)(h)|
      <= [2+2π C_(d+1)/d] J_N/N ->0.             (4.2)

Hence second-order τ_2 covers all moving |h|=o(N³), and cubic-corrected τ_3 covers all moving |h|=o(N⁴). This is an all-horizon **phase precision** theorem, not an all-horizon **signed cancellation** theorem. A same-forcing altered real seed has the same representation against a DIFFERENT completed real constant, so nothing here selects π over a coherent nonnormal point. Never swap limits in d,N without separate uniformity.

## WB-05. Source-authentic frequency/time Ward estimate

For all n>=1 and k>=0, direct iteration of the original recurrence gives

    U_(n+k)=16^k U_n + F_(n,k),
    F_(n,k)=Σ_(j=1)^k16^(k-j) r(n+j),
    0<=F_(n,k)<=16^k/(15n²).                    (5.1)

The last inequality uses r(n+j)<=(n+j)^-2<=n^-2 for n+j>=2. Comparing e(h16^k U_n) with e(hU_(n+k)), discard first J indices, then shift time sums by k endpoints (cost <=2k). For all N>=1, h∈Z, k>=0, and 1<=J<=N,

    |S_N(16^k h)/N-S_N(h)/N|
       <= [2k+2J+2π|h|16^k/(15J)]/N.           (5.2)

If integer h_N!=0 and integer k_N>=0 satisfy |h_N|16^(k_N)=o(N²), choose J_N approximately sqrt(|h_N|16^(k_N))=o(N). Necessarily k_N=O(log N). All terms of (5.2) vanish, giving

    [S_N(16^(k_N)h_N)-S_N(h_N)]/N ->0.          (5.3)

This is a **source-specific quantitative covariance/Ward transport** along the radix-frequency ladder. It does not assert either mean tends zero; coherent nonnormal changed seeds also pass this transport. It can check orientation and economize frequency probes, but is not a signed saving.

## WB-06. The SUCC typed integration diagram

1. Sphere/analytic source: AC-13 and CSG reconstruct the original signed differential r(z)dz=(1/8)d log R(z), with exact branch/monodromy data. A source meromorphic identity does not imply a temporal Fourier decay law.
2. Pascal/Gamma/local prime carrier: provides arithmetic relations in the source index, clock and conductor; use actual maps to original r(n), not a synthetic prime/Haar product.
3. Heisenberg–Weyl finite radix register: exact clock-shift commutators and complete 16-branch refinement, but a 2-adic local character is not the Archimedean e(hU_n).
4. Genuine real-circle observer: the full rational U_n maps to cell a AND residual s by (2.1); only after recombination does it give the actual signed selected amplitude (2.2).
5. Source-selected Weyl time average: (1.2) is the exact gate; WB-04 and WB-05 provide quantitative safe frame transports, not decay.
6. van der Corput/Fejér and the Main XIX Laurent lag: these reduce cancellation to selected signed lag correlations, not to Galois averaging or finite positivity.
7. Source prime/cofactor: PRs #459 and #460 identify original p≡5 mod8 prime windows and exact joint phases. The *joint signed* cofactor cross term remains OPEN; prime-only subgroup mixing is not a proof.

The exact chiral identity in the existing arctan solenoid gives S_N^dual(h)=(-1)^h conjugate(S_N(h)): this is the same information in another basis, not an independent Haar witness. The rotated Riemann sphere and Weyl algebra must be transported via explicitly typed maps, not an assumed quarter-turn equality.

## WB-07. Next non-tautological source discriminator

First use the original certified p=257 window [33,128] from draft PR #459 as calibration. Preregister fresh primes p≡5 (mod8), modes h=1,3,5,7, radix levels M=16,256 and two independent rational-interval sign oracles. Compare: actual signed full original e(hU_n), source-isolated p-primary character, exact p-free phase, within-cell signed cofiber C_(N,M)(h), and corrected moving-band phases. Require true source/carry/seed provenance. Hostile controls are the changed seed 1/5-π/16 (completed real point 1/5), near-zero shadows, positive matched-prefix source mutants, uniform bins with locked within-cell phase, and Galois averaged fake phases. A source-specific signed saving must fail on coherent counterseeds and must hold for every sufficiently large original-source horizon, not only finite windows.

**Verdict / claim boundary:** WB-02/03/04/05 are exact mathematical statements with derivations and scoped finite Fraction tests. The open conjecture is a genuine new source-specific signed cancellation bound on C_(N,M) or on the original prime/cofactor cross correlation that forces (1.2). No such theorem is proved in this PR.


## WB-10. A separate Weyl gate via ×16–×3 measure rigidity and positive dimension

**Source of the classical rigidity theorem:** Michael Hochman and Pablo Shmerkin,
*Local entropy averages and projections of fractal measures*, Annals of Mathematics
175 (2012), 1001–1059, §10.5, **Theorem 10.4**, p.1047
(https://annals.math.princeton.edu/2012/175-3/p01).
The theorem says that a probability measure μ on [0,1] invariant under both
T_m:x↦mx mod 1 and T_n:x↦nx mod 1, where m and n are not powers of the
same integer, equals Lebesgue measure **provided its lower Hausdorff dimension
dim_* μ is strictly positive**. This deep theorem is an external mathematical
input, NOT proved by SUCC or by our finite probes. It generalizes the
Rudolph–Johnson positive-entropy approach to a different nonconcentration hypothesis.

Here is a rigorous conditional application to the **actual** original zero-seed
BBP stream (not an auxiliary Haar or 3-adic source). Put x_n={U_n},
μ_N=N^-1 Σ_(n=1)^N δ_(x_n), all viewed on R/Z. The probability measures
have subsequential weak-* limits by compactness. The exact source recurrence
implies x_(n+1)={16 x_n+r(n+1)}, and r(n+1)→0. For any continuous f on R/Z,

    ∫f(T_16 x)dμ_N - ∫f(x)dμ_N
      = N^-1 Σ_[ f(16x_n)-f(x_(n+1)) ]
        + N^-1 [f(x_(N+1))-f(x_1)] →0.

The first term →0 by uniform continuity, r(n+1)→0 and Cesàro convergence;
the second is O_f(1/N). Therefore **every** weak-* limit μ of the actual
selected orbit is automatically T_16-invariant. This invariance alone
does not select Haar; for example δ_0 is T_16-invariant.

**Two-key conditional theorem (NOT yet an established premise):** Suppose

(A) For every fixed integer h, the genuine ARCHIMEDEAN signed defect vanishes:

    D_N(h)=(1/N)Σ_(n=1)^N [e(3h U_n)-e(hU_n)] →0.   (10.1)

This is strictly a real-circle comparison of the same selected U_n,
NOT the dyadic, ternary or Pascal-source local character law.

(B) For every weak-* empirical accumulation measure μ of the actual μ_N,

    dim_* μ >0.                                      (10.2)

Then every such μ is T_16- and T_3-invariant: (A) gives
μhat(3h)=μhat(h) for every integer h, which by uniqueness of circle Fourier
coefficients says (T_3)_* μ=μ. Since 16 and 3 are multiplicatively
independent and (B) is precisely the dimension hypothesis of
Hochman–Shmerkin Theorem 10.4, μ is Lebesgue/Haar. As **every**
subsequential limit is Haar, the full μ_N weakly converges to Haar.
By the inherited source-tail Weyl equivalence, π is normal to base 16.

Thus

    (A) + (B) + ORIGINAL r + U_0=0
          ==> every empirical limit is Haar ==> π base-16 normal.


**Logical strength, deliberately explicit:** For this same selected source,
base-16 normality also IMPLIES (A) and (B): normality gives μ_N→Haar,
which is T_3-invariant and has lower Hausdorff dimension 1. Thus
(A) AND (B) is **another equivalent criterion**, not an already
verified weaker assumption. The mathematical opportunity is to attack
the two obligations by different source-specific tools (Pascal/prime
real-circle differences versus arithmetic nonconcentration), not to
rename the normality problem and call that progress.

This is a **correct conditional proof route**, not a claim that (A) or (B)
currently holds. The source-normality debt is redistributed into *new
two simultaneous original-source obligations*: a special ×3 Weyl-defect
comparison and a positive-dimension/nonconcentration theorem. Both are
OPEN and may be no easier than direct Weyl cancellation.

A reproducible sufficient, still-open criterion for (B): find universal
constants C<∞, η>0 and ε_N→0 such that **for all N and every open circle
interval I**, the original empirical measure obeys

    μ_N(I) ≤ C |I|^η + ε_N.                         (10.3)

By weak-* portmanteau for open I, each accumulation μ obeys
μ(I)≤C|I|^η. Such a Frostman bound implies dim_* μ≥η>0.
A finite empirical measure has atoms, so ε_N cannot in general be
smaller than O(1/N) uniformly over tiny intervals; a proof must pay
this finite-sample floor. A finite-level entropy bound or one well-covered
depth is NOT automatically (10.3). This ties to CRE-04's resolution ceiling
and the adaptive collision criterion, without conflating them with dimension.

**Adversarial controls clarify the two keys.**

- Original four poles but changed real seed s*=−π/16: U_n(s*)=−T_n→0,
  so μ_N→δ_0. Both ×16 and ×3 invariance (A) hold, but (B) fails
  with dim_*δ_0=0. Thus dual invariance alone is NOT enough.
- Same forcing but s=1/5−π/16: U_n(s)=16^n/5−T_n, so
  μ_N→δ_(1/5). T_16-invariance holds (16≡1 mod5), but
  D_N(1)→e(3/5)−e(1/5)≠0 and (B) also fails. Thus the
  new real ×3 hypothesis genuinely rejects a standard coherent counterfeit.
- Dyadic source isometry and local Pascal 2↔3 constructions do
  NOT establish (A). Multiplying the selected real circle coordinate by
  3 is an extra test, not a symmetry inferred from a local finite chart.
- A **single** positive-dimensional accumulation limit is insufficient;
  the dimension hypothesis must hold for **every** empirical limit.
  A positive-dimensional invariant measure for just one map also
  does not satisfy the two-map theorem.

**Claim status:** EXISTING externally proved Hochman–Shmerkin
Theorem 10.4 + NEW elementary conditional SUCC specialization (paper),
with both source-specific assumptions (A) and (B) **OPEN**. This is a
second route to discharge the Weyl gate, not a proof of its premises.
