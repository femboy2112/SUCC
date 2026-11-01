# Actual zero-selected three-channel finite interference (exploratory; NOT a proof)

**FINITE_DIAGNOSTIC_ONLY.** The original four signed BBP source is computed in exact Fraction arithmetic with zero initial seed. The three edge states V3,V4,V5 are computed as zero-seeded exact rationals. For each n and integer harmonic h, the program evaluates the authentic character z_n=e(h(2V3_n+V4_n+V5_n)). Each exact phase is first reduced as a rational modulo one, then evaluated with mpmath 70-digit complex arithmetic. Direct combined versus three-factor phase representations agree numerically below 3e−70; the complex evaluations themselves are NOT rigorously interval-certified.

Let Z3=e(2hV3), Z4=e(hV4), Z5=e(hV5), temporal mean E_N. The columns are magnitudes of authentic E_N[Z3 Z4 Z5], of the UNSUPPORTED marginal-independence surrogate Π E_N[Zj], and of the exact centered triple cumulant E_N[(Z3−EZ3)(Z4−EZ4)(Z5−EZ5)].

| N | h | Authentic joint phase mean magnitude | Independence surrogate magnitude | Centered triple cumulant magnitude |
|---:|---:|---:|---:|---:|
| 128 | 1 | 0.0795257249 | 0.0002004435 | 0.0935251364 |
| 128 | 3 | 0.1010903778 | 0.0000214884 | 0.1051540274 |
| 256 | 1 | 0.0265654244 | 0.0000350995 | 0.0281989497 |
| 256 | 3 | 0.0517225852 | 0.0000512877 | 0.0537107774 |
| 512 | 1 | 0.0493026374 | 0.0000030352 | 0.0489649026 |
| 512 | 3 | 0.0117304540 | 0.0000066638 | 0.0134733698 |
| 512 | 5 | 0.0317103063 | 0.0000333498 | 0.0312897467 |

The surrogate product of marginal means can be orders of magnitude below the true joint mean because the edge phases come from one coupled deterministic source, not independent samples. This is a **finite diagnostic against a tempting approximation**, NOT a statistical test establishing asymptotic dependence or π normality.

The selected signed joint mean has no proven decay rate. The same numbers are compatible with both eventual normality and nonnormality; the current test horizons cannot distinguish their infinite behaviors. Do not reuse the above horizons as fresh holdout proof evidence.

**Reproduce with optional mpmath installed:**

    python research/2026-10-31/four_pole_path_interference/finite_probe.py --horizons 128 256 512 --harmonics 1 3 5

For rigorous source diagnostics, use the pure-stdlib exact tests and original analytical identities. The numeric source-phase product check is implementation-level cross-validation, not a proof of the signed asymptotic.