# PRE-REGISTERED — 16x16 real π spectral vs Euler–Mascheroni

**2026-11-09, original source fixed; base:** PR #566 head `4caae7652b430974448437bc716da9a3edba5fd9`. Original four signed BBP poles, literal U0=0, all prime residues/carries/future tails unchanged. Research-only branch and draft PR, no main merge/release.

## What was inspected before this registration (CALIBRATION, NOT HOLDOUT)
- The 65,536-digit certified π prefix of PR #566 is already known, source SHA256 `e42ee060201573db4a32a8c8e0a4ccac5a6cb061ae1ac8d71809234c58dfae53`.
- Its genuine linear 65,535-pair empirical 16x16 row-normalized P has max nontrivial |λ|≈0.01647115. Its centered 225-mode energy is ≈0.00395272.
- Its preselected (by user's prior inverse-frequency question) opposite-frequency anti-diagonal character energy `E_- = sum_(h=1)^15 |mean exp(2πi h(d_n-d_(n+1))/16)|²` is ≈0.00046369. A **post-prefix exploratory** 1,200 fixed-histogram shuffle reference gives mean 0.00023075, percentile ≈99.2%. This is NOT blind validation.
- A positive doubly stochastic nonuniform Markov matrix can have exactly the Haar eigenvalue multiset {1,0×15}; eigenvalues alone cannot prove two-digit Haar. The finite Haar matrix is J/16, the source 2-adic temporal low-nibble matrix is a 16-cycle permutation. These are separate objects.

## FROZEN independent holdout and outcomes

1. Independently source-certify **131,072 hexadecimal digits of π** by the original integer-BBP enclosure `sum_{n=1}^K floor(16^(K+1-n)r(n))`, with K=N+guards24/32 (two separate runs), no π oracle. Both outward intervals must fit the same N-cell; first 65,536 digits must match the existing SHA256. Record full new prefix SHA256 and the exact 65,536-digit **fresh disjoint block** `digits[65536:131072]`.
2. Evaluate the **fresh 65,535 within-block linear transitions**, not the overlap with old digits, as the primary holdout: full 16x16 count matrix, row-normalized P, eigenvalues (including complex conjugate pairs), stationary distribution defect, centered SVD/eigenvectors, 225 mixed Fourier energies and opposite-frequency E_-.
3. Before viewing new digits, freeze a deterministic **1,200-shuffle fixed-histogram permutation null** for each block with seed 20261109 (new block uses seed 20261110 for independent draws). The decisive replication test is `E_- > 95th percentile of the holdout's shuffled reference` and `E_-*65535/15 > 1.5`, both required; report exact rank, not a claimed universal p-value. This is a finite exploratory hypothesis, not a π normality/abnormality theorem. If it fails, clearly label **NONREPLICATION**.
4. Evaluate `|λ₂|`, leading centered singular value, conditional entropy deficit, Fourier anti-diagonal vs all 225 mixed modes, scale-normalized diagnostics. Do not fit a γ pattern after observing new data. Test direct `|λ|-γ` only for the **unscaled** row-stochastic P, and a separately declared harmonic reference `H_N-log N→γ`. For an actual new gamma mechanism require an independently derived identity connecting spectral or source-transfer data to the harmonic finite part; numerical closeness is not enough.
5. Rigorous counterexample: P=J/16+uvᵀ/64 with `u=(1,-1,0,...)`, `v=(1,1,-2,0,...)`. Prove `P²=J/16`, all nontrivial eigenvalues 0, all 256 entries positive, but mixed E₂=12/4096 and pair Haar fails. This rules out eigenvalue-only convergence as a sufficient normality criterion even under full support.
6. Spatial original 2-adic temporal permutation `g(d)=d+1` for even d and `d−3` for odd d; verify spectrum 16th roots of unity and depth-k odometer spectrum all 16^k-th roots as a spectral **boundary condition**, not a real π normality result.

## Failure/ambiguity and source standards
- **PASS** only for exact rational/int source certificates, algebraic Fourier/spectral/no-go statements, and preregistered reproducible finite statistics.
- **NONREPLICATION** if the primary anti-frequency holdout does not exceed both declared thresholds.
- **AMBIGUOUS** if a source boundary interval straddles a digit cell, two guards disagree, or a numerical spectrum discrepancy exceeds declared double-precision tolerance; record and repair.
- **UNVERIFIED/OPEN**: original-zero π real one-, two-, every-depth digit Haar, original signed 225-mode/carry control. No inference from Markov surrogate to actual deterministic π time process. No stochastic iid assumption.
