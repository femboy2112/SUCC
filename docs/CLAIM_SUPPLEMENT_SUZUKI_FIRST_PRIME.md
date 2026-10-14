# S1 — source-faithful Suzuki first prime / arithmetic interface ledger

**Theorem source:** [SUZUKI_FIRST_PRIME_WAVEFRONT](../research/2026-10-13/SUZUKI_FIRST_PRIME_WAVEFRONT.md). **Primary:** Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, (1.3), (8.2), (8.7). **Research parent:** draft PR #62, SHA `fb4fb91d46218ac121f4a4887f7322e79d3d0b70`. **RH PROVED: no.**

| ID | Claim | Status | Scope / prohibited upgrade |
|---|---|---|---|
| S1.0 | Exact zero-free complete Weil form as real-place translation energy + rank-two pole boundary + finite authentic prime-shift correlations | CLASSICAL/PROVED LOCAL algebra | `C_c^infinity` compact tests; source formula, not a positivity proof |
| S1.1 | First genuine prime ramp has unprojected compact kernel `||R_a||_HS=b(2a-log2)^2/sqrt6` | PROVED LOCAL, exact source enclosures | `log2/2<a<log3/2`; mean-zero projection can only decrease HS |
| S1.2 | Prime's twice-differentiated form has spectrum `{−b,0,+b}`, operator norm `b>0` for all first-onset `a`, despite kernel HS→0 | PROVED LOCAL / TESTED finite | isolated prime term, not full `A_a` |
| S1.3 | For `0<2a-log2<=log2/65536`, complete Weil form is `> (8/35)||v||²` on smooth tests supported in two edge strips | PROVED LOCAL; rational constants TESTED | proper subspace only; neither `lambda_a>0` nor RH |
| S1.4 | Isolated prime operator tends strongly to zero at onset but not in norm | PROVED LOCAL | zero-extended common `L²(R)`; not a continuity assertion about full `A_a` |
| S1.5 | Exact mean-zero Neumann inverse pairing matches Dirichlet primitive norm | CLASSICAL / exact TESTED finite | piecewise step probes; no Weil positivity |
| S1.5b | Finite-bandwidth (derivative-bounded) first-prime HS perturbation inequality; fails to be uniform in L² | PROVED LOCAL / exact tests | fixed derivative budget only, no λ_a certificate |
| S1.5c | Real-place Fourier symbol at ξ=0 is strictly negative; rank-two pole boundary and compact Paley–Wiener restriction cannot be dropped | PROVED LOCAL / classical | refutes naive scalar multiplier PSD route, not Weil PSD |
| S1.6 | Full source-derived positive `G_a-c(a)K_a` on every `L_0²(-a,a)`, with verified all-scale error | UNVERIFIED | RH-strength for all `a`; finite Gram alone insufficient |
| S1.7 | Source-controlled Suzuki compact-uniform spectral limit (1.12) | UNVERIFIED | Suzuki's stated conjectural limit; zeros not construction inputs |

**Controls:** fake composite 6, authentic powers 4/9, changed translation phase, changed half-density, non-mean-zero Neumann probe, first-window threshold, exact rational transcendental inequalities. **Absent controls:** full Hecke conductor and matched Davenport–Heilbronn global source; these cannot be validated from a one-prime-only interval.

Reproduce from repo root: `python -m unittest discover -s tests -p 'test_suzuki_first_prime.py' -v` and `python scripts/suzuki_first_prime_probe.py`. The scripted receipt includes source, operator, norm and analytic-domain limitations; it is not a physical experiment or an RH certificate.
