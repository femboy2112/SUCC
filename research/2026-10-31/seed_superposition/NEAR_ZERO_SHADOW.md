# Original BBP near-zero nonnormal shadow theorem — exact selected-prefix spoofing

**2026-10-31. PROVED LOCAL from the original BBP identity and classical rational periodicity.** This is a source-faithful theorem for the fixed ORIGINAL four signed poles, not a π-normality proof. The original selected U0=0 remains unchanged; the constructed altered seeds are explicitly separate counterfactuals. Academic originality not claimed.

## NZ-01 — a nonnormal same-forcing seed arbitrarily close to the authentic zero seed

Write the exact original positive four-pole BBP series as

    α0 = π/16 = Σ_(j=1)^∞ 16^(-j) r(j).

For each K≥1, define the **rational** K-term source snapshot

    q_K = Σ_(j=1)^K 16^(-j) r(j) = 16^(-K) U_K(0) ∈ Q,

and define a ***symbolic irrational*** changed seed

    s_K = q_K - α0 = -16^(-K) T_K,

where T_K=Σ_(j≥1)16^(-j)r(K+j)>0 is the original real Green future tail. The earlier source estimate T_K < 1/[(8K+1)(8K+2)] gives the explicit zero-boundary proximity bound

    0 < |s_K| < 16^(-K) / [(8K+1)(8K+2)].

Thus s_K→0 **exponentially**. It is irrational, because q_K is rational and α0=π/16 irrational.

Crucially, the SAME ORIGINAL forcing recurrence gives exactly

    U_n(s_K) = U_n(0)+16^n s_K = 16^n q_K - T_n.

Therefore the *completed* orbit y_n(s_K)=U_n(s_K)+T_n=16^n q_K has a rational starting point q_K, and is **eventually periodic and nonnormal** in base 16. Let h_K>0 be the reduced denominator of q_K. For every integer n≥1,

    exp(2πi h_K U_n(s_K)) = exp(-2πi h_K T_n).

The original summable T_n therefore yields, for every N≥1,

    |Σ_(n=1)^N exp(2πi h_K U_n(s_K)) - N|
       ≤ 2π h_K Σ_(n≥1) T_n < π h_K/16.

For each **fixed K** the corresponding **fixed h_K** is an explicit Weyl witness: normalized phase sum tends to 1, proving that specific altered seed is nonnormal. Although h_K can grow with K, normality quantifies over all fixed nonzero h for each fixed seed, so no quantifier exchange occurs. This is a TRUE same-forcing infinite nonnormal countermodel arbitrarily close to the authentic source seed zero.

## NZ-02 — even the first K original selected complex observations are nearly indistinguishable

For 1≤n≤K,

    |U_n(s_K)-U_n(0)| = 16^(n-K) T_K.

For any fixed integer h, using |exp(2πit)-exp(2πiu)|≤2π|t-u|,

    |Σ_(n=1)^K e(hU_n(s_K)) - Σ_(n=1)^K e(hU_n(0))|
      ≤ 2π|h| T_K Σ_(n=1)^K 16^(n-K)
      < (32π|h|/15) / [(8K+1)(8K+2)].

This decays like O_h(K^-2) for the entire **unnormalized** K-observation sum, even though the altered seed is provably nonnormal asymptotically. Every individual finite source state lies within the displayed real displacement; the correction is source-derived, not a fitted or randomly picked near-identity sequence.

The rational K-prefix q_K can be computed with exact Fraction arithmetic from the original source; the irrational seed s_K is specified by an exact equality to π/16 and is **NOT** pretended to be a rational or computationally fully represented by the finite code. The code returns only q_K and rigorous rational error budgets.

## NZ-03 — why this is different from sibling PR #432 and Main XVI

- **Main XVI:** rational changed seeds (including 1/7) preserve the original normality **status** by Wall's rational addition theorem; they cannot be mandated asymptotically nonnormal. We preserve the historical literal zero source and the correction in RATIONAL_SEED_NORMALITY_ERRATUM.md.
- **Sibling PR #432 ESM-09:** horizon-dependent *rational* seeds of the form -c_K almost reproduce the coherent altered seed for **up to K observations**. They are finite source-coherence spoofs. Their one-fixed-K asymptotic normality status, if α0 normal, must agree with the original by Wall.
- **This NZ construction:** each s_K=q_K-α0 is itself **irrational** and produces an **exact rational completed orbit**, hence is provably nonnormal for that fixed K. The s_K approach the authentic original seed zero exponentially and reproduce its first K source phases to tiny total error. This is a genuinely different hostile family.
- **The coherent fixed altered seed:** s*=-α0 yields the single exact completed point zero, also nonnormal, but is a fixed macroscopic displacement rather than an arbitrarily small perturbation of the authentic seed.
- **Other seeds:** for a source-identical family, normal seed points are dense (Borel's full-measure normality theorem, translated by -α0) and nonnormal seed points are dense (rational completed points q translate to q-α0). Thus **normality status is nowhere locally constant as a function of real seed**. This is a topological observation/point-selection boundary, not an undecidability theorem.

## NZ-04 — verdict and the next actual theorem

This exact same-source construction **REFUTES** the general inference that finite uniform seed-neighborhood normality, close agreement for K observations, or arbitrarily strong continuity of selected phases implies infinite-horizon normality of the center seed. Any legitimate argument must use the exact source boundary and a nonlocal arithmetic theorem, not merely ensemble typicality or an approximate finite certificate.

It does **NOT** refute the possibility of proving π normality from the original exact U0=0, the true signed four-pole BBP source, an RH-dependent global inequality, or a source-specific nonflat path-phase theorem. It does **NOT** assert original π is normal or nonnormal. The two distinct iterated limits (fix K then let N→∞, versus let K grow with observed N≤K) are retained.

**Regression:** test 27 verifies q_K=16^-K U_K, strictly decreasing positive seed-distance budgets and exact prefix-error coefficients. Test 28 verifies for chosen K the exact integer resonance h_K q_K and all its shifted powers, and the source tail bounds. These are exact finite controls of the algebra, not a machine proof of irrationality of π or normality equivalences.

**Next discriminating probe:** give an all-horizon signed, four-pole and U0=0 **selected** estimate that can exploit the literal source boundary and fails when the source initial condition is replaced by these irrational s_K. If it is only an observable of a finite prefix, it will necessarily be spoofed for sufficiently large K.
