# Frozen A=512 parity/pressure holdout protocol (before observing samples)

**Date:** 2026-11-09. **Source:** exact original four-pole BBP rational recurrence, literal U0=0, canonical `observational_succ.duck_bbp.forcing`, exact outward `tail_interval`. No pi-digit oracle, no changed source. Parent branch is stacked on Tenacious D Haar junction #571, NOT on main.

## Predetermined clock and selector
- Train/development epochs already inspected: A=8,16,32,64,128,256 (all `[A,2A)`), corresponding source times at most 512. No data for n>=513 has been read as of this protocol commit.
- New holdout: **A=512**, exactly original source times **n=512,...,1023**, N=512. The n=512 anchor was already seen in development. No overlap in aggregate earlier `[256,512)` statistics; for strictly unseen interval use n=513,...,1023 and report its one-time boundary separately.
- Prime selector: among all primes p ≡1 (mod 8) with 9A/4<=p<=5A/2, minimize |5p−12A|, breaking ties toward smaller p. Deterministic primality-only search yields **p=1217** (order of 16 modulo p: 38); no source phase or digit information was used to choose it. Four stage source births are n=153, 609, 761, 913, and the selected observation window straddles the latter three.
- Stable metric definitions: for each n, the full Q_n=lcm(den(r(j)):j<=n) odd; compute A_n=Q_n U_n, canonical k_(p^v,n), ell_n=floor(sum k/(p^v)), epsilon_n=1_{ {U_n}+T_n>=1 } with outward rational certification. Define a_n=(-1)^{k_(1217,n)}, s_n=(-1)^{floor(16^(n-1)pi)}, b_n=a_n s_n. Signed covariance is mean(s)−mean(a)*mean(b), and real parity must match the exact all-prime/clock/winding factor. Track each individually.
- Count and separate: original boundary corrections sum epsilon_n; number of odd primes in Q_n, bit-length of Q_n; full three-factor signed covariance, with input/raw number of samples and SHA-256 of a deterministic JSON receipt; h=8 (digit Walsh parity) vs continuous Weyl e(8x) never conflated.
- Pressure comparison: independent certified fractional-π hex digit window of N+4 starting at n=512 and exact counts of word lengths k=1..4, always exactly N=512 starts. Report E_k, floor, excess and occupied bins. Do not fit predictions using these data then report them as blind confirmations.

## Predetermined verdicts
- If any exact CRT, 2-adic, source-tail, direct-origin or pressure identity fails, report a **math/code defect**, retain raw failures and repair before claiming validation.
- If |Cov|>1/4, the exploratory *one-epoch* claim |Cov_512|<=1/4 is **REFUTED at this epoch**; otherwise report merely **OBSERVED-FINITE**, not a uniform covariance theorem. The numerical threshold is a diagnostic, not a predicted theorem.
- If the local p=1217 parity mean is small but real parity large, report it as an example of missing complement cancellation, never as proof of eventual normality.
- Independently check no-π-oracle odd-denominator coherent wrong seed s_A that preserves original source, 2-adic clock and p=1217-local history but produces all-zero completed digits on this epoch. This proves a seed-blind no-go, not a counterexample to π.
- **No finite outcome can prove π normality or even parity balance asymptotically.** Do not claim blind independence from earlier same-model work; any second replay is a reproducibility check only.

**Status:** Protocol committed before reading any n>=513. Subsequent receipt and tests must cite this first protocol commit by SHA.