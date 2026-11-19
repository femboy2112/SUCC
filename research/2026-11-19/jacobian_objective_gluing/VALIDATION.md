# Local validation and scope

Date: 2026-11-19. Base read from `femboy2112/SUCC@81be6b897ae980b801a3b9de9e22ef81e8360bfb`, with read-only PR #666/#667/#668. This research was staged as new files only; no source replacements.

## Commands executed

```sh
python -m unittest discover -s tests -p 'test_jacobian_objective_gluing.py' -v
python research/2026-11-19/jacobian_objective_gluing/probe.py
python -m compileall -q research/2026-11-19/jacobian_objective_gluing tests/test_jacobian_objective_gluing.py
```

At this checkpoint **21/21 focused standard-library tests PASS** in the isolated staging tree (0 skipped, 0 failures, 0 errors), and the standalone receipt printed all rank and signed-Gram cross-checks as passing. Compileall passed. Tests exercise the original zero-seeded Fraction recurrence, five-channel determinant, exact Cauchy product, prime p-pole row scales and ranks, forward policy repair, objective total variance, local-lock control, source-tail truncation, positive rational holonomy, signed Gram cross-term equality and the same-forcing wrong-seed control.

## Exact prime result

| p | initial rank | repaired rank | max row p-normalization exponent |
|--:|--:|--:|--:|
| 3 | 3 | 4 | 3 |
| 5 | 4 | 4 | 2 |
| 7 | 4 | 4 | 2 |
| 11 | 3 | 4 | 1 |
| 29 | 4 | 4 | 0 |

## Finite phase diagnostics (not interval-certified)

For B=64,128,256: rational mode-one |W| respectively 0.062925, 0.065440, 0.074124; the weakest within-cell coherence is 0.993090, 0.991356, 0.992699. Inter-cell variance is respectively 0.986032, 0.983790, 0.983686. Signed 8-shift Gram energy at h=1 is respectively 0.136211, 0.118535, 0.124795. The same-forcing locked counterseed gives h=1 Gram energy approximately 1 at B=128 (rational positive-tail truncation; exact limiting statement is proved in PROOFS.md).

The fixed high-frequency `H_{B;4,11}`, `H_{B;6,7}` R0 lower certificates are negative at the displayed shells; a negative certified lower bound simply provides no positive information. The low-frequency `H_{B;1,1}` certificates are positive in these finite tests only. No asymptotic inference is claimed.

## Not run / not claimed

- Full root `python -m unittest discover ...` across 14k+ inherited tests; root provenance verifier; root observer-foundations and ordinal probes on the final branch; hosted CI and exact-head review; external referee; new formal Lean kernel check.
- No new source-specific signed all-epoch Weyl bound, R0 result, π normality proof, Collatz or RH claim.
- Numeric trigonometric calculations in phase diagnostics are conventional double-precision; exact source arithmetic and p-adic rank decisions use `fractions.Fraction`. The universal theorems rest on explicit algebraic proofs in PROOFS.md.

Shared model/provenance: recent sister branches are related analyses, not blind independent witnesses.
