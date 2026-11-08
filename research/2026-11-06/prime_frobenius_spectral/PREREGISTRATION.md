# Operation RH-SHAPED PRIMES × ORIGINAL-SOURCE SPECTRAL GAP — preregistration

2026-11-06. Strictly additive research child of SUCC PR #531 pinned to SHA 06b46d5715153412215947a0e9ee4800c9bd9a5f. The original four-pole BBP source, literal rational U0=0 and inherited frozen contracts stay unchanged. No RH/π normality claim.

**Exploratory BEFORE this preregistration, not blind:** the conjecture that the selected odd primes in intervals (2n,4n] and (4n,8n−7] force valuation v_p(U_n)=−1 was already checked with exact Fraction for n=4,7 and initially FAILED at n=10,p=23 under a wrong single-pole residue formula. The failure exposed a second pole at 8j−3=3p. Analytic Euler-criterion derivation subsequently predicts the nonzero double-pole correction; a corrected scratch check passed up through n=160 for denominator membership. These observations are calibration, not fresh holdouts. Save the failure and correction.

## Predeclared NEW arithmetic holdouts

n ∈ {161,173,199,211,257,293,317,383}; for each prime p in:
- (2n,4n] (both mod4 residue classes),
- (4n,8n−7] with p≡1 (mod4),

compute authentic rational U_n with Fraction from U0=0, independently using combined numerator/D and the signed four-pole partial fractions. Predict **v_p(U_n)=−1** and the exact pU_n modulo p from:
- p≡1 mod4: unique 8j−7 or8j−3 (principal coefficient 4 or −1);
- p≡3 mod4: unique 4j−1 at j=(p+1)/4, coefficient −1/2, plus at most one 3p pole;
- if p≡3 mod8 and 3p=8j−7 (j≤n), combined normalized coefficient +16/3 after factoring 16^(n−j);
- if p≡7 mod8 and 3p=8j−3 (j≤n), combined normalized coefficient −4/3 after factoring 16^(n−j).

No fit, no post-hoc selective primes. The theorem itself must prove all n≥2 using pole ranges, Euler criterion (2/p) and PNT/AP for the asymptotic 4n exponent. All modular oracle comparisons are exact; real log values are float diagnostics only.

## Predeclared spectral-gap/falsification controls

Fix N∈{128,256,512,1024}, h∈{1,2,3}, and dyadic level k=0,...,floor(log2 N)−1. Calculate exact dyadic energy levels E_(k,m), contrast D_k=E_(k+1,m)−E_(k,m), and ratio D_k/E_(k+1,m) where denominator >1e−14, using float phases *only*. Source authentic U0=0, non-original H-shadow H(n)=n/(2n−1)^4, periodic β=1/17, and synthetic IID phase controls. This is a **DIAGNOSTIC** to ask whether a uniform branch-contrast gap with source provenance is plausible. No fixed η threshold chosen by data; a failure at any k is preserved. Do not claim such a gap is proved asymptotically.

Prove a sufficient "martingale reverse-Poincare" theorem: if for each large dyadic N=2^m and each h≠0 at a positive fraction of clock levels 0≤k≤m−1, branch energy satisfies D_k≥η E_(k+1,m) with fixed η>0, then |W_N(h)|²≤(1−η)^{c m}; to obtain *all-prefix* normality must independently control non-power-of-2 horizons (e.g. mesoscopic gluing of PR #531). This condition is **OPEN** for the authentic π source.

Negative controls must kill (i) source-only spectral contraction, (ii) 2-adic/isometry-only positive gap, (iii) positivity of Gram matrices implying zero energy. RH Weil positivity and deterministic lacunary normality use distinct quantifiers. Do not equate "no extraneous energy" with an established source phase gap.

**PASS only for proved finite prime modular identities, analytic PNT/AP asymptotic, and universal conditional inequalities. OPEN for original-real Fourier phase gap, Poisson contraction and π normality.**
