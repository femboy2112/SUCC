# TS-09 — certified finite signed return energies (authentic zero-seeded BBP)

**CERTIFIED FINITE ONLY · 2026-11-06.** The N=512,h=1 signs were known from earlier float explorations and are now *post-hoc certified*, not blind discoveries. The N=768,h=2 probe was frozen before the rational certificate was executed, without predictions of signs. One holdout is AMBIGUOUS. No asymptotic signed Weyl, pi normality or RH claim.

## Exact rational certificate and error proof

For original rational BBP phases x_n={U_n}, h integer, N=QM, define E_n=exp(2πihx_n), A_j=M^-1 Σ_t E_(j+tQ), and R=Q^-1 Σ_j |A_j|².

Machin's exact identity π=16 atan(1/5)−4 atan(1/239), combined with alternating-series rational remainder bounds at 8 and 4 terms respectively, yields rational bounds π_L<π<π_U<22/7 with width less than 10^(-10). For atan(1/a), m-term alternating partial sums have remainder strictly smaller than 1/((2m+1)a^(2m+1)). Let π_*=(π_L+π_U)/2.

Quantize the exact rational z_n={h*x_n} **down**: q_n=floor(2^16*z_n)/2^16. Define θ_n=2π_*q_n rational. Then

    |2π z_n − θ_n| < (44/7)/2^16 + (π_U−π_L) = η.

Approximate the exact character with rational Taylor polynomials to cos-degree 28, sin-degree 29:

    Ê_n = Σ_(j=0)^14 (-1)^j θ_n^(2j)/(2j)!
          + i Σ_(j=0)^14 (-1)^j θ_n^(2j+1)/(2j+1)! .

For 0<=θ_n<44/7, Lagrange bounds on remainders give cos error < (44/7)^29/29! and sin error < (44/7)^30/30!. Since real sin and cos are each 1-Lipschitz, the complex error is at most the sum of coordinate bounds:

    |E_n−Ê_n| < 2η+(44/7)^29/29!+(44/7)^30/30! < 1/5000 = ε.

All bounds and output sign decisions use *exact Python Fraction arithmetic*; floats are exclusively used for printed decimal centers. The approximated fiber mean differs from the true mean by <ε, and |A_j|<=1, |Â_j|<=1+ε. Therefore

    |R−Rhat| < ε(2+ε) < 1/2400

with Rhat exactly rational. The code reports R<1/M only when Rhat+1/2400<1/M *rationally*; it reports R>1/M only when Rhat−1/2400>1/M. Otherwise AMBIGUOUS. Printed decimal approximations have no bearing on classifications.

## Original four-pole zero-seed certified verdicts

| N | h | Q | M | Rhat approximate | Rationally certified verdict |
|---:|---:|---:|---:|---:|---|
| 512 | 1 | 4 | 128 | 0.003211346973 | R < 1/128 |
| 512 | 1 | 8 | 64 | 0.018183246066 | R > 1/64 |
| 512 | 1 | 16 | 32 | 0.024190021041 | R < 1/32 |
| 768 | 2 | 4 | 192 | 0.004831418959 | **AMBIGUOUS** versus 1/192 |
| 768 | 2 | 8 | 96 | 0.006409217763 | R < 1/96 |
| 768 | 2 | 16 | 48 | 0.016759286080 | R < 1/48 |

The signed offdiagonal correction R−1/M has both signs for the authentic source; any universal all-positive or all-negative signed-shell hypothesis is killed. Five signed finite inequalities are certified; the sixth is intentionally unresolved.

Reproduce by running certified_finite.py (standard library) and test_certified_finite.py. The exact original recurrence is in experiment.py; no π-digit oracle, no interval-library float assumptions, no seed adjustments, no fitted sign thresholds. Compact CERTIFIED_FINITE_RESULTS.json records semantic result data; raw command stdout may differ in whitespace. 14/14 focused local tests PASS. This is a locally verified analytic finite certificate, **not** formal Lean certification or an all-horizon real distribution estimate. The all-scale source-selected signed-cancellation inequality remains OPEN. See PREREGISTRATION_INTERVAL.md for explicit preregistration and VALIDATION.md for earlier scope.
