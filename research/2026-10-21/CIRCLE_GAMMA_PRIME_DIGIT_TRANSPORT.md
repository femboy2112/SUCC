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
