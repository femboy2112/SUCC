# Operation BBP–Euler–Mascheroni × 27/31 prime passport

**Original π base-16 normality: OPEN.** Source, literal U0=0 and archives unchanged. This is an additive research branch following the Γ16 q-Gamma source-blocking work in #568.

The user proposed a *BBP-adapted Euler–Mascheroni variable* obtainable by perturbing the usual harmonic-log limit, then inspecting its closed form for prime support at 3³=27, 2⁵−1=31, and π. This dossier makes that idea exact in **two different declared observation charts**, rather than claiming a universal canonical constant without a normalization.

**Main new source-clock observable:**

`gamma_BBP,g = gamma - (1/2) log(64 R_g(1)/(16^g-1))`

for the actual g-block source `R_g(k)=sum_j16^(g-j)r(g(k-1)+j)`. Each finite log argument is rational; its limit is `4*pi`, hence `gamma_BBP,g` tends monotonically to `gamma-(1/2)log(4*pi)`. This limit uses the classical BBP identity, not digit randomness.

**Main Mellin-shape result:** the authentic four-pole positive source's Gamma(2) logarithmic first jet after g-blocking is `gamma+(5/2-8g/(16^g-1))/a+O_g(a^-2)`.

**Prime fingerprint:** The original reduced forcing terms r(7) and r(8) introduce 3³ and 31. Their valuations remain uncanceled in the exact 8-block source, and the normalized rational argument has v3=-4, v31=-1. This is **finite denominator support**, not prime support of the irrational constant or a normality theorem.

**q-Gamma firewall:** the canonical q-Euler constant at q=1/16 is `log(15/16)+log(16)*sum_{n>=1}1/(16^n-1)`; it involves a universal Lambert/divisor spectrum. The q-integer blocking factor alone does not distinguish the source or determine the q-Euler derivative.

Start at [PROOFS.md](PROOFS.md), then [PRIME_SUPPORT.md](PRIME_SUPPORT.md), [CLAIM_LEDGER.md](CLAIM_LEDGER.md), [VALIDATION.md](VALIDATION.md) and [NEXT.md](NEXT.md). Module: `observational_succ/bbp_euler_mascheroni.py`. Root tests: `tests/test_bbp_euler_mascheroni.py`. Finite exact receipt: `FINITE_RECEIPT.json`; deterministic runner: `experiment.py`.
