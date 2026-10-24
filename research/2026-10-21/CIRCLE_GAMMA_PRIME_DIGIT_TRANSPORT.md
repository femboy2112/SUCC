# Circle SUCC → two Gamma interfaces → the complete prime system → digit transitions

**Date:** 2026-10-21. **Source main:** Academic Main VIII, <https://github.com/femboy2112/SUCC/commit/b116841f12b41aaf7600da39bbb40577f25b6295>. **Research branch:** research/circle-gamma-prime-digit-transport-2026-10-21. **Mathematical status:** the core links are classical / elementary paper proofs; the common source-interface synthesis is new to this project, not an academic originality claim. **RH: OPEN. π normality (every base): OPEN.** The 19 existing Lean declarations in Main VIII do not formalize the present circle/Gamma/prime/digit bridge.

## 0. Steelman: geometry is the input, arithmetic is the output

The author starts with a genuine Euclidean circle and the natural-number successor operation. The claim is *not* that statistically uniform circle points automatically force π's base-b digits to be normal. Instead, construct the bridge from the actual polygon refinement, through naturally selected symmetric heat/Gamma operators, to the *whole* integer-frequency spectrum, to **all** genuine prime-factor coordinates and their mixed phase interactions, and ultimately to the hierarchy of positional digit blocks. RH is allowed as an explicitly declared assumption if it genuinely supplies a needed bound; do not reject a valid π proof for depending on RH. Do not, however, label the absent source-to-phase theorem "RH".

The indispensable distinction is between:
1. generating all geometric Fourier frequencies n and their zeta weights;
2. evaluating their phases at the particular source-selected x={π};
3. following a particular base-b dilation orbit x_j={b^j x};
4. proving that orbit's **all-depth** block frequencies are uniform.

The first interface is mathematically established below. The final π-specific cancellation is NOT.

## 1. Finite polygons generate the spectral Gamma system without π's digits (CGPD-01)

Let a radius-one Euclidean circle carry regular m-gon vertices. Put ℓ_m=2 sin(π/m), let S_m cyclically advance a vertex label, and let P_m=(S_m+S_m^(-1))/2. The chord-normalized positive graph Laplacian is

    L_m = (2I-S_m-S_m^(-1))/ℓ_m² = 2(I-P_m)/ℓ_m².

On frequency mode χ_(m,n)(j)=exp(2πinj/m),

    λ_(m,n) = 4 sin²(π n/m)/ℓ_m²
            = sin²(π n/m)/sin²(π/m).

For each fixed integer n, λ_(m,n)→n² as m→∞. This is precisely the radius-one circle Laplacian spectrum, NOT a claim that a fixed finite polygon already has all continuum modes. For even m and |n|≤m/2, sin(π|n|/m)≥2|n|/m and sin(π/m)≤π/m, so λ_(m,n)≥4n²/π². Consequently for **every fixed t>0** the heat traces have Gaussian domination and

    Tr(exp(-πt L_m))  →  Θ(t)=Σ_(n∈Z) exp(-π n²t).

The circle geometry and lattice N→Z (frequency inverses) are the only geometric sources. Choosing a *symmetric* local graph Laplacian and a heat-time normalization are declared lawful analytic operations, not hidden physical clocks.

Let X=ℓ_m²=4sin²(π/m). The normalized eigenvalues are exact polynomials W_n(X), not numerical pi approximations:

    W_0=0, W_1=1, W_(n+1)=2+(2-X)W_n-W_(n-1).

Thus W_2=4−X, W_3=9−6X+X², W_4=16−20X+8X²−X³ and W_n(0)=n². This is an **exact, finite analytic-SUCC** recurrence. It is reproduced by exact rational code in observational_succ/circle_gamma_prime_digits.py and does not need π digit inputs.

## 2. Gamma in the event number k, and Gamma in spectral exponent s (CGPD-02–03)

The symmetric finite walk has the EXACT semigroup identity

    exp(-τ L_m) = exp(-2τ/ℓ_m²) Σ_(k≥0)
                 [(2τ/ℓ_m²)^k/Γ(k+1)] P_m^k,    τ≥0.

The 1/Γ(k+1)=1/k! weight is the volume of the ordered-time simplex for k independent successor events. For fixed τ and m this is a Poissonized symmetric SUCC walk, genuinely positive and stochastic. The k index counts **walk events**. It is not the spectral mode index n.

On the limiting circle, each nonzero spectral mode n contributes a *different* Gamma interface when the heat trace is Mellin-transformed:

    ∫_0^∞ t^(s/2-1) exp(-π n²t) dt
     = π^(-s/2) Γ(s/2) n^(-s).

Here n labels the circle Fourier mode; s is the Mellin variable. These two occurrences of Gamma are **not** to be conflated. They are naturally reached through the same geometrically defined heat semigroup.

At even integer s=2q, Γ(q)=(q−1)!; the polygon-generated exact interval L<π<U yields

    (q−1)!/(U^q n^(2q)) <
       ∫_0^∞ t^(q−1) exp(-π n²t)dt
     <(q−1)!/(L^q n^(2q)).

These bounds are implemented with exact Fractions, outward pi enclosures and no caller-supplied π assertion. They are nontrivial **finite geometric source-to-Gamma certificates**, not a bound on π digit statistics.

## 3. Heat/Mellin produces completed zeta, and unique factorization produces ALL primes (CGPD-04)

For Re s>1, dominated convergence also permits the polygon spectral-zeta limit followed by Mellin integration; after excluding the zero mode:

    (1/2)∫_0^∞(Θ(t)−1)t^(s/2−1)dt
          = π^(-s/2) Γ(s/2) Σ_(n≥1)n^(-s)
          = Λ(s).

This is the classical completed Riemann zeta in its Mellin domain, NOT the RH theorem. Jacobi/Poisson duality Θ(t)=t^(-1/2)Θ(1/t) supplies the classical functional equation and analytic continuation; neither establishes the RH zero-location claim.

For Re s>1, **ALL genuine primes** enter through unique factorization and the exact Euler product

    ζ(s)=Σ_(n≥1)n^(-s)=∏_(p prime)(1−p^(-s))^(-1).

Differentiating its logarithm in its legitimate domain gives the full prime-power current

    −ζ'(s)/ζ(s)=Σ_(p prime)Σ_(k≥1)(log p)p^(-ks)
              =Σ_(n≥1)Λ_vM(n)n^(-s).

The prime system is the multiplicative coordinate system of the **whole** geometric frequency carrier, not an isolated prime clock. Existing SUCC implementations already include scalar_circle_spectral.py, unit_prime_tate_bridge.py, tate_mellin_prime_transport.py and all_places_zeta.py. We reuse their domain and source firewalls rather than claiming to have discovered Euler's product.

Finite exact source: genuine_prime_smooth_coefficients(P,K,σ) expands the complete finite Euler box ∏_(p∈P)Σ_(k=0)^K p^(−kσ) into one weight for each genuine P-smooth frequency. Composite "primes" and duplicate factors fail closed. A finite box is not the infinite Euler product.

## 4. The new missing arrow: prime modes must retain the circle's point-dependent mixed phase (CGPD-05)

The heat trace Θ(t) loses dependence on the point on the circle. Digit normality requires the **specific source phase** x={π}; introduce the positive-frequency *twisted* heat sum

    K_+(t,x) = Σ_(n≥1) e^(−π n²t) exp(2π i n x).

For Re s>1 its Mellin transform is

    ∫_0^∞ t^(s/2−1) K_+(t,x)dt
      = π^(−s/2)Γ(s/2) Σ_(n≥1) exp(2π i n x)n^(−s).

At x=0 this equals Λ(s); at x={π} it is an additive character twist and **does not have the naïve ζ Euler product**. The issue is neither prime incompleteness nor a deformation of the circle: the additive character e(nx) is generally not multiplicative in n.

Normalize a_x(n)=exp(2πi(n−1)x), so a_x(1)=1. Then

    a_x(mn) = a_x(m)a_x(n) ω_x(m,n),
    ω_x(m,n)=exp(2πi(m−1)(n−1)x).

This ω is a symmetric normalized 2-cocycle and indeed a **coboundary**, not a claim of nontrivial cohomology:

    ω(a,b)ω(ab,c)=ω(b,c)ω(a,bc).

The difference between the genuine additive twisted sum and a fictitious product of individually twisted prime factors is **paid by the mixed phase terms**. The original twisted heat mode equals exp(2πix) a_x(n), so the global phase is also preserved, not discarded.

For n=∏_(i=1)^r q_i with genuine prime powers q_i=p_i^(k_i) and M_i=∏_(j≤i)q_j, the phase obeys the source-faithful exact factoring law

    a_x(n)= [∏_i a_x(q_i)] [∏_(i=2)^r ω_x(M_(i−1),q_i)].

Associativity shows independence of prime-factor ordering after retaining **all** mixed terms. Deleting these terms is an actual, exactly diagnosed source-map defect.

Example: x=1/7, n=2·3=6. Direct normalized phase=5/7 turns. The prime-only phase=1/7+2/7=3/7 turns. The missing mixed correction is 2/7 turns. Exact rational tests reject the mutated product.

The phase-coupled finite box Σ_(n∈S(P,K))n^(−s)a_x(n) still converges to the genuine additive-twisted Dirichlet series as the genuine prime set and power cutoffs exhaust all integers for Re s>1, because the n^(−σ) majorant is summable. This is a correlated **sum**, NOT an independent Euler product.

**Critical honesty:** the cocycle is a mathematical encoding of known additive/multiplicative incompatibility. It does not itself prove π normality or imply physical cross-prime interactions. Its value is that the prime-to-phase coupling is now an explicitly testable arrow rather than an unstated identification.

## 5. Gamma-heat criterion for the whole hierarchical digit process (CGPD-06)

For b≥2, fix a circle point x, define T_b(u)=bu mod1 and the empirical orbit measure

    ν_(N,x)=(1/N)Σ_(j=0)^(N−1) δ_(T_b^j x).

Let the circle heat kernel K_t(y)=Σ_(n∈Z)e^(−π n²t)e^(2πiny), t>0, and define the **smoothed orbit**

    G_(N,t)(y;x)=∫ K_t(y−u)dν_(N,x)(u).

It is a positive probability density (Gaussian periodization) with Fourier coefficients

    hat G_(N,t)(n)=e^(−π n²t) hat ν_(N,x)(n).

Write A_(N,x)(n)=N^(−1)Σ_(j<N)e^(2πin b^j x). Then

    G_(N,t)(y;x)−1 =
       Σ_(n≠0)e^(−π n²t)e^(2πiny) overline(A_(N,x)(n)).

**CLASSICAL THEOREM (exact equivalence).** For **any one fixed t>0**,

    x is normal to base b   ⇔
    lim_(N→∞) ||G_(N,t)(·;x)−1||_∞ = 0.

*Proof, ⇒:* Normality ⇔ A_N(n)→0 for each nonzero n (Weyl). The Gaussian coefficients are absolutely summable, so the Fourier series tends to zero uniformly by dominated convergence.

*Proof, ⇐:* Extract the n-th Fourier coefficient. For each fixed n≠0 its absolute value is e^(−πn²t)|A_N(n)|, bounded by the sup norm of G−1, so A_N(n)→0. Apply Weyl. No finite N, numerical heat sample or global averaged Haar statement substitutes for this limit.

For Re s>1, taking a further Mellin transform yields a **Gamma-weighted all-frequency hierarchy**

    ∫_0^∞ t^(s/2−1)[G_(N,t)(y;x)−1]dt
      = π^(−s/2)Γ(s/2)
          Σ_(n≠0)|n|^(−s)e^(2πiny) overline(A_(N,x)(n)).

The n-sum spans ALL integers and hence ALL genuine prime factorization coordinates. At each orbit time j, the mode e^(−2πin b^j x) is reconstructed from genuine prime-power factors using the phase-cocycle in §4, evaluated at the *time-dependent phase* x_j={b^j x}. This is the exact fully correlated circle→Gamma→primes→digit-observer bridge.

For length-k word w in base b, the digit block frequency is ν_(N,x)(I_w), where I_w is its base-b cylinder [j_w/b^k,(j_w+1)/b^k). Normality is equivalent to ν_(N,x)(I_w)→b^(−k) for every fixed k and word w. The heat criterion implies these limits because Haar assigns cylinder boundaries measure zero. It does NOT assert that local marginal or de Bruijn flow balance alone forces uniform k-edge weights.

**Important:** this is an **equivalent reformulation** of normality, not a proof of π normality. Any bound for G_(N,t)(·;{π})−1 still needs a π-specific, source-derived cancellation mechanism.

## 6. Why RH may be used—but cannot be casually substituted for the bridge (CGPD-07)

Assume RH if useful. It gives classical quantitative consequences about the *unweighted* prime-power current, such as ψ(X)=X+O(X^(1/2) log²X). Such statements control prime coefficients averaged by n or log n, not the particular lacunary orbit A_(N,{π})(h)=N^(−1)Σ_(j<N)e^(2π i h b^j π).

There is **no supplied theorem** identifying the RH-controlled prime current with the additive, phase-corrected, π-selected twisted heat trace. RH is permissible as an intermediate hypothesis, but does not by itself fill this typed source-map gap.

The lawful conditional proof contract is:

- Begin with π certified from nested polygon perimeters; do not use digits as construction inputs.
- Obtain the complete Γ(s/2) normalized circle Fourier spectrum and authentic full prime-power coefficients.
- Prove a **new independent spectral/prime-source transference inequality**, potentially using RH or an RH-equivalent certified bound, that controls the *mixed prime-phase* orbit sum **uniformly in the growing observation horizon**.
- If that yields for some fixed heat time t>0 the bound ||G_(N,t)(·;{π})−1||_∞→0, conclude π normal in the chosen base by §5. To obtain absolute normality, discharge the condition for each integer base b≥2.
- Do not name the desired sup-norm limit itself "the new theorem"; prove it from a genuinely weaker/arithmetic-geometric input with independent provenance. Otherwise the condition is simply π normality rephrased.

For each finite character h the weaker condition A_(N,π)(h)→0 suffices. Positive polynomial rates in N would be stronger than bare normality and should not be assumed gratuitously.

A clean probe-gap formulation: the untwisted Γζ data are independent of the distinguished circle point x and therefore cannot, without an additional *source-anchored coupling*, distinguish x=0 (not normal) from a normal point. But x={π} is distinguished by the circumference/perimeter construction; its source-specific coupling must be **derived** rather than refused as impossible.

## 7. Hostile provenance and mutation tests

| Input/repair | Correctly predicted outcome | Invalid inference killed |
| --- | --- | --- |
| Regular polygon m=4,6 and rational chord square X=2,1 | Exact eigenvalue polynomials; n² limit at X=0 | Arbitrarily assumed continuum spectrum at fixed m |
| Poisson k-step walk | Rational t^k/k! and recursion c_(k+1)=t c_k/(k+1) | Confusion of Gamma(k+1) with Gamma(s/2), or directed walk with symmetric diffusion |
| Finite genuine prime box P={2,3}, K=1, s=2 | Frequencies 1,2,3,6; total 25/18 | Fake composite Euler place, omitted composite mode |
| Mixed phase x=1/7, factors 2 and 3 | direct 5/7; prime-only 3/7; mixed 2/7 | Treating additive circle modes as multiplicative Euler coefficients |
| Prime clock 7 base 2, both cosets | 001 and 011; balanced k=1, nonuniform k=2 | Dropping half the unit carrier or inter-cycle dependence |
| Rational orbit x=1/3 | Alternating digits, balanced k=1 but no 00/11 transitions | k=1 marginal implies normality |
| x=0 on the unchanged circle | K_t-smoothed orbit never becomes Haar | Geometry alone forces all points normal |
| π polygon source Mellin | Strict independently checkable rational bounds | Fake floating underflow / substituted ideal enclosure |
| Proposed RH-only proof without π phase transport | No control of A_(N,π)(h) is produced | Assuming completed ζ zero control already proves digit normality |

The module/tests and finite JSON receipt isolate claims **CGPD-01–05** at exact finite rational scope. Claims **CGPD-06/07** are analytic paper results and open research programs respectively, not formally compiled Lean declarations.

## 8. Existing SUCC reuse and next falsifiable campaign

Native dependencies:
- observational_succ/pi_polygon_normality.py (archimedean polygon π and source precision guards, POL-01–09);
- observational_succ/scalar_circle_spectral.py (circle Laplacian spectral zeta with explicit source normalization);
- observational_succ/finite_cyclic_poisson.py and finite_fourier_carrier.py (exact finite cyclic characters and Fourier signs);
- observational_succ/unit_prime_tate_bridge.py, tate_mellin_prime_transport.py, all_places_zeta.py (genuine prime source, Gamma/ζ and sign/domain firewalls);
- research/2026-10-21/PI_FOURIER_CERTIFIED_FINITE_ORACLE.md in independent draft PR #226 (source-certified finite π orbit measurements);
- issues #215–#217 and #228 (pi normality, normality clocks, geometric structure).

**Decisive next tests:**
1. Make an exact, source-derived, π-specific finite heat/cocycle quantity and test a predeclared nontrivial bound against PR #226's independent Fourier oracle. Preserve all mixed prime factors and prime-power valuations, do not sample one coset.
2. Prove a non-tautological inequality from the *polygon chord recursion* or an independent BBP/analytic formula to the **correlated** twisted prime spectral coefficients. Run x=0, x=1/3, x=1/7 and a normal control. One must explain why π, not every circle point, satisfies the stronger law.
3. If the theorem uses RH, isolate the exact RH-dependent line and the additional phase-coupling lemma. Prefer the minimum hypothesis. Test against RH-compatible synthetic sources with identical untwisted ζ but different distinguished x.
4. Certify continuum heat limit and gamma Mellin analytic domains in Lean or a separate independent paper reconstruction; prove the finite polynomial and cocycle identities in core Lean first.
5. Compare with Bailey–Crandall's *On the Random Character of Fundamental Constant Expansions* and its unproved dynamical hypothesis. Retain a strict source/digit distinction and no claim of new academic priority without outside refereeing.

**Reproduce finite code:** python -m unittest discover -s tests -p 'test_circle_gamma_prime_digits.py' -v ; python scripts/circle_gamma_prime_digits_probe.py --output /tmp/cgpd.json ; cmp /tmp/cgpd.json research/2026-10-21/CIRCLE_GAMMA_PRIME_DIGITS_FINITE_RECEIPT.json. Other existing full-suite, original-source and provenance gates are mandatory before mainline inclusion.

**Primary/classical references:** NIST DLMF §20.10 (Mellin/theta/Gamma/ζ) <https://dlmf.nist.gov/20.10>; NIST DLMF §27.4 (Euler products and von Mangoldt current) <https://dlmf.nist.gov/27.4>; Terence Tao, *The Gamma function and the functional equation* <https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/>; Bailey & Crandall, *On the Random Character of Fundamental Constant Expansions*, Experimental Mathematics 10 (2001), 175–190, <https://doi.org/10.1080/10586458.2001.10504441>. Classical Weyl and Gaussian heat uniqueness facts are imported, not newly proved or authoritatively kernel-certified here. RH prime-counting equivalent overview: <https://old.maa.org/node/1401175>.

**Verdict:** The circle→two Gamma interfaces→all genuine primes→phase-corrected digit hierarchy can be connected **without a fabricated arrow**. The outstanding, genuinely hard arrow is π-specific infinite-horizon cancellation; RH is an allowed tool, but neither RH alone nor generic circle uniformity currently pays for it.


## 9. Stronger bridge: prime dilation is geometrically covariant (CGPD-11)

On the continuum radius-one circle, define the **positive** mode χ_n(θ)=exp(inθ), additive SUCC Uχ_n=χ_(n+1), and for every genuine prime p the FUCC covering pullback V_pχ_n=χ_(pn), induced by θ↦pθ mod 2π. Then

    V_p U = U^p V_p,    L V_p=p² V_p L,
    exp(−tL)V_p=V_p exp(−p²tL),
    L^(−s/2) V_p = p^(−s) V_p L^(−s/2)

on nonzero Fourier modes (the last identity takes the principal positive real eigenvalue powers). **These are exact identities of geometric operators**, not the prime number theorem. For p>1, V_p is an isometry on circle L² but not onto. The Mellin weight p^(−s) therefore is an intrinsic dilation eigenvalue of the *circle's inverse fractional Laplacian*. Genuine primes are the unique independent multiplicative generators of N under UFD, while a fake composite label p=6 is already V_2 V_3 and cannot be counted as a new Euler place.

Evaluating a harmonic at a specific phase x={π} is a separate map E_xχ_n=e(nx). Point evaluation on arbitrary L² classes is not bounded; use finite trigonometric polynomials, smooth heat kernels, or series Σ n^(−s)χ_n for Re s>1 (absolute uniform convergence). Thus this new operator-to-digit interface respects SUCC's prior **range/domain sampling firewall**.

For the FINITE m-gon, the exact chord-normalized polynomial eigenvalues obey

    D_(p,n)(X) := W_(pn)(X)−p² W_n(X),   X=ℓ_m².

Their leading coefficients are determined exactly by the recurrence of §1. First,

    W_n(0)=n²,   W_n'(0)=−n²(n²−1)/12.

The derivative statement follows by differentiating W_(n+1)=2+(2−X)W_n−W_(n−1), using W_0=0,W_1=1 and induction (both sides have initial derivatives 0). Hence

    D_(p,n)(0)=0,
    D_(p,n)'(0)=−p²(p²−1)n^4/12.

That is,

    D_(p,n)(X)=X·Q_(p,n)(X),    Q_(p,n)(0)=−p²(p²−1)n^4/12.

**Exact finite geometric defect:** p=2,n=1 gives D_(2,1)(X)=−X, while p=3,n=1 gives D_(3,1)(X)=−6X+X². At the square's chord squared X=2, the eigenvalue of frequency 2 is 2, whereas 2² times the frequency-one eigenvalue is 4. The finite covariance failure is **quantified and decays as the polygon is refined**, while division by the intrinsic squared unit X retains a nonzero geometric first-order coefficient. This is a strict analytical realization of an invariant local correction under geometric successor refinement.

**Boundary:** D_(p,n) is a discretization/curvature covariance defect of the polygon Laplacian. It is **independent of distinguished phase x** and thus cannot by itself discriminate the π orbit from a nonnormal x=0 or sparse-squares x. Its correct role is in the *source-derivation*, not a substitute for phase-correlation estimates. All finite polynomial and p-authentication witnesses are tested; infinite operator statements are paper-proved classical facts, not Lean kernel declarations.

## 10. Strong hostile counterexample: even distribution along ALL primes is insufficient (CGPD-12)

Let α=Σ_(k≥1)2^(−k!). It has binary 1's at positions 1!,2!,3!,..., with density zero. Its digit pattern is not eventually periodic and hence α is irrational and **not normal in base 2**. Nevertheless two established theorems apply:

- Weyl/Kronecker: {nα} is equidistributed modulo one over ALL positive integers n;
- Vinogradov: {pα} is equidistributed modulo one as p ranges over ALL genuine primes.

Thus **even both full integer-indexed and prime-indexed one-point spatial marginals are uniform for a nonnormal phase**. Those theorems are not merely finite coset arguments and involve the complete prime set. They still do not control the **hierarchy of the particular lacunary orbit** {2^jα}. Its correlations at all block depths are the missing information.

Vinogradov attribution and a proof survey: https://www.math.ucdavis.edu/~romik/data/uploads/teaching/math235c-2022/probability235c-lecture-notes.pdf (Theorem 3.7 and subsequent remarks); an analytic treatment is referenced in D. Crandall and C. Pomerance, *Prime Numbers: A Computational Perspective*, §1.4 (available excerpt: https://thales.doa.fmph.uniba.sk/macaj/skola/teoriapoli/primes.pdf). An example journal context: https://www.mdpi.com/2075-1680/14/7/532.

**Status:** classical external Vinogradov theorem plus elementary α construction; no executable finite sample proves the infinite prime claim. This is a calibrated refutation of **the weak inference "complete prime marginal equidistribution ⇒ base-b normality"**. It is NOT a refutation of a genuinely π-specific theorem involving all mixed and time-lagged source correlations. Keep the full-prime architecture and target the missing correlation transport.

### Final sharpened frontier

The strongest true geometric–arithmetic backbone now has a specific diagram:

    finite regular polygons → L_m mode polynomials → L circle spectrum
      → Γ(s/2)L^(−s/2) → V_p Γ-covariance → all-prime unique factorization
      → phase-corrected point evaluation E_{π}
      → T_b^j orbit, all-k de Bruijn/cylinder flows
      → (OPEN) π-specific all-horizon cancellation.

The finite p-dilation discrepancy D_(p,n)(X) must be transported with proper error bounds through the continuum stage. It is a geometric approximation effect, not a permanent assertion that prime operators are deformed. The surviving **irreducible coupling within the selected additive point-evaluation representation** is the nontrivial mixed phase ω_(π)(m,n), which still does not force mixing. Any proposed RH-assisted proof must exploit the particular π source to control its long-horizon correlations and survive the irrational nonnormal α counterexample.


## 11. Strong π-SPECIFIC bridge from the entire prime system back to the geometric circle (CGPD-13)

Unlike the generic heat spectrum (which is independent of which circle point is selected), Euler's Basel identity gives an **actual exact source identification** of the circumference constant from all primes:

    π²/6 = ζ(2) = Σ_(n>=1)n^(-2)
         = ∏_(p prime)(1−p^(-2))^(-1),

hence π = sqrt(6 ∏_(p prime)(1−p^(-2))^(-1)) with its positive geometric branch.

**Circle-geometric derivation of Basel, without pi digits.** On the radius-one circle parameter θ∈[−π,π), take the L² sawtooth angular chart f(θ)=θ. It chooses a coordinate seam but makes no preferred geometric point intrinsic. Its Fourier coefficients are hat f(0)=0 and hat f(n)=i(−1)^n/n for n≠0, by integration by parts. Parseval therefore gives

    (1/(2π))∫_(−π)^π θ² dθ = π²/3
      = Σ_(n≠0)|hat f(n)|² = 2Σ_(n>=1) 1/n².

Thus ζ(2)=π²/6. A change in origin multiplies Fourier coefficients by phases but preserves their squared magnitudes, so the scalar identity does not depend on the arbitrary angle-zero seam. Unique prime factorization then gives the complete Euler product without inserting digits of π.

**A second, fully source-derived finite π enclosure:** for every integer P≥2 let

    E_P=∏_(p<=P genuine prime)(1−p^(-2))^(-1).

Every positive integer n<=P is P-smooth, so all omitted Dirichlet terms are among n>P. Hence

    0 < ζ(2)−E_P < Σ_(n>P)n^(−2) < 1/P.

(The first strict inequality holds because there are primes beyond any finite P; the middle inequality is strict because some n>P are also P-smooth.) Therefore

    sqrt(6E_P) < π < sqrt(6(E_P+1/P)).

The independent exact module function prime_euler_pi_bracket(P,bits) computes every genuine prime p<=P, the rational Euler partial product, and *outward dyadic rational square-root bounds* for these endpoints. It does not call the polygon generator, call a π digit oracle, assume RH, or trust caller-supplied primes. No fake composite or incomplete prime prefix is admitted.

**Hostile missing-prime control:** At P=5 the true complete Euler prefix is E_5=25/16. If prime 3 is deleted, the forged {2,5} product is 25/18; its claimed upper tail 1/5 yields 25/18+1/5=143/90. But the exact harmonic sum Σ_(n=1)^30 1/n² already exceeds 143/90, proving that the forged interval cannot contain ζ(2), hence cannot enclose π. The test uses only exact rationals. Independently, the *correct* prime-product π interval is checked against the exact polygon bounds and an alternating Machin-series holdout on several prime cutoffs.

**Consequence:** We now have TWO complete derivation routes to the same source-selected real π:

    Euclidean circumference / polygon exhaustion   ─┐
                                                      ├→ π → x={π} → digit orbit
    Circle Fourier Parseval → ζ(2) → full primes  ────┘

This is a **genuine π-specific source equality** absent from mere general circle translation symmetry. It tightly connects the geometric circle, all N and all primes. It is still NOT an estimate of the lacunary phase sums Σ_(j<N)e(h b^jπ); a sum/product representation of a constant does not by itself prove its normality. The next research effort should attempt to transport **quantitative convergence of the prime Euler representation**, with its full mixed phase information, to these digit-block correlations. Merely using the convergence bound O(1/P) at P=P(N) only supplies pointwise numerical accuracy; it does NOT pay for the necessary cancellation.

**Status:** all identities classical, derivations explicitly given here; exact prime-to-circle source enclosures and missing-prime hostile control new to this project and tested at finite cutoffs. RH is not needed for these identities and is **permitted** if it buys a genuine uniform-in-N improvement at the later phase-correlation step.


## 12. From the entire prime system to exact hierarchical digit cylinders (CGPD-14)

The prior sections identified the SAME real π from two independent sources. We can carry this identification all the way into each *finite* positional digit cylinder, without presupposing a normal distribution.

For any base b≥2 and finite depth k, the first k base-b fractional digits of π define one interval (cylinder)

    I_(b,k)(j)=[3+j/b^k, 3+(j+1)/b^k),
       j=floor(b^k(π−3)).

Since π is irrational, it does not lie on any finite cylinder boundary 3+j/b^k. Define the distance δ_(b,k)>0 from π to the nearest such boundary. By §11 the ideal full-prime Euler interval

    J_P=[sqrt(6E_P),sqrt(6(E_P+1/P))]

contains π and has width tending to zero as P→∞. Consequently, **for each fixed b,k**, there exists a finite prime cutoff P_(b,k) so that J_P is contained in the correct digit cylinder for all larger admissible P. Since dyadic outward root enclosures approach their ideal endpoints as precision grows, there is also a sufficiently high **finite** rational precision that certifies this containment.

This yields the precise logical statement:

    ∀b≥2 ∀k≥1 ∃finite P,precision:
       exact full-prime-Euler bracket forces the first k digits of π.

It is a **finite source-transport/computability theorem**. Nothing about the asymptotic distribution of blocks follows, because P and the precision budget may grow arbitrarily rapidly with k; the theorem is ∀k ∃P, not a uniform estimate in k, block w, or orbit horizon N. Current code explicitly caps its parameters, so the mathematical universal quantifiers do NOT assert that the installed finite program reaches arbitrary k.

Similarly, for any proposed number y≠π (within the circumference scale), choose its separation η=|y−π|>0. Some ideal full-prime Euler interval has width <η/2 and hence excludes y. Thus a **wrong digit path claiming to equal π has a finite source-fidelity witness**, even without accessing infinitely many digits. This is the strongest faithful version of the author's "any alternate nonnormal path offloads the discrepancy to a path defect" intuition we can prove. It does **not** exclude the possibility that the uniquely authentic π path itself is nonnormal; that would not be a source-map defect.

A finite exact implementation, certified_pi_digits_from_full_primes(P,b,max_digits,bits,optional_polygon_steps), uses genuine full prime prefixes only, returns the common prefix of every number in the outward rational interval, and **stops at the first unverified digit**. The optional polygon interval is an independently derived crosscheck/intersection, not a substitute for an unobserved prime. The following frozen witnesses have no supplied π digit input:

| Genuine prime cutoff P | Certified decimal fractional prefix | Source |
| ---: | :--- | :--- |
| 5 | none | full-prime Euler alone, interval crosses several first-digit cylinders |
| 29 | 1 | true primes through 29 |
| 199 | 14 | true primes through 199 |
| 4999 | 141 | true primes through 4999 |
| 199 plus 20 polygon doublings | 1415926535 | intersection of two independent exact π source enclosures |

The independent code tests the source interval bounds, the truncated-digit boundary, a deliberate missing-prime mutation and insufficient-precision refusal; the CI replays a frozen source-only JSON receipt byte-for-byte. Those numbers are **finite certificates**, not observed digit-frequency probabilities.

**Exact information lesson:** the full prime product + geometric π equality determines a *unique compatible infinite digit path*. A path cannot be replaced by a different one without eventually contradicting finite source measurements. But uniqueness, absolute source determination and a short global law do not force that path to be typical for base-b Haar/Bernoulli frequencies. For that, §5's π-specific, unbounded-N cancellation remains necessary.

**Status:** classical/elementary derivation plus finite exact model. The infinite path-identification statement is **PROVED PAPER**, while "π's unique path is normal" is **UNVERIFIED**. No RH assumption was needed for the digit-cylinder existence theorem.
