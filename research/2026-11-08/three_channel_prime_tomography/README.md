# Operation 3²=9 → prime-phase three-channel tomography

**Research only · 2026-11-08 · π normality OPEN · RH OPEN.** Additive child of SUCC draft #552, building on the already established scalar Prime-Frobenius theorem (#497) and the open signed-covariance frontier (#544). The original four signed poles and `U0=0` are not changed. Main is not touched.

We lifted the authentic BBP source to exactly three zero-seeded positive forcing channels, then reconstructed their **complete p-primary histories** on shells of `p` consecutive arithmetic times for primes `p=1 mod8`. Source pole births occur at offsets `0,3k,4k,5k`, k=(p−1)/8. The four-stage vectors are `(2,1,1)`, `(3/2,1,1)`, `(3/2,4/5,1)`, `(3/2,4/5,5/6)`, and the chronological impulse rank is 1→2→3.

**New mathematical frontier:** the entire three-channel phase distribution has an exact Fourier formula and a conditional weak limit supported on four one-dimensional subtori of the 3-torus, weighted `(3,1,1,3)/8`. The genuine first-shell 3×3 **prime-character Gram** tends to the positive definite matrix `[[1,0,0],[0,1,1/2],[0,1/2,1]]` when the imported subgroup additive-character error tends to zero, with asymptotic eigenvalues `3/2,1,1/2`. This stands in contrast to #552's collapsing positive Hilbert Gram; the two are distinct instruments. The four dangerous complement resonance planes are explicit and give a conditional L1/Fourier bound.

**Crucible:** a coherent complementary factor `conjugate(prime diagonal)` restores mean 1 even with the full-rank local Gram; rational changed seeds are p-primary invisible; a positive Gamma-jet-matched source mutant creates an earlier p-pole event. These controls preserve the distinction between representation, arithmetic source, and zero-seed real signed phase.

**Actual π obstacle remains:** prove a small-error, nonresonant representation of the original zero-selected **real complementary phase** (or a different selected signed estimate), and cover all integer epochs. No such estimate is claimed here; this package does not prove π-normality.

- Full exact paper proofs and limits: [PROOFS.md](PROOFS.md)
- Each claim, prerequisites and hostile controls: [CLAIM_LEDGER.md](CLAIM_LEDGER.md)
- Reproduction/validation: [VALIDATION.md](VALIDATION.md)
- Exact next reduction: [NEXT.md](NEXT.md)
- Implementation: `observational_succ/three_channel_prime_tomography.py`
- Independent p-pole direct oracle and tests: `tests/test_three_channel_prime_tomography.py`

The novel-to-this-round contribution is the source-*channel*-resolved Fourier/rank calculation. #497's scalar prime-Frobenius recurrence, classical subgroup exponential-sum estimates and the general mathematical facts about subtori are not priority claims.

## New continuation: **the clock matters**

[**BALANCED_EPOCH.md**](BALANCED_EPOCH.md) proves an unexpected obstruction and its source-faithful repair. The original `p≈4A` selector has an **exact rank-two (or less)** three-channel p-phase frame *on the actual normality epoch*, despite the full-shell rank-three result above. A new deterministic prime near `p≈(12/5)A` resolves all three transverse births with asymptotic epoch weights `(1/5,3/10,3/10,1/5)`, a provable full-rank phase Gram and uniform incomplete-period character bounds. The new local bound legitimately feeds #544's **exact-forcing** signed-lag inequality, but does not prove its remaining real signed covariance estimate. A constructive no-π-oracle dyadic anti-Haar counterseed preserves **all** p-primary channel phases, conclusively rejecting any seed-blind shortcut. New code/tests: `observational_succ/balanced_prime_clock.py` and `tests/test_balanced_prime_clock.py`.
