# Source dependencies, mathematical authority, and reproducibility boundaries

## Pinned SUCC ancestry (read-only; no main or history changes)

- **Main XXVI:** `81be6b897ae980b801a3b9de9e22ef81e8360bfb`; original `docs/PI_NORMALITY_FRONTIER.md`, `observational_succ/duck_bbp.py`, zero-seed contract and signed cofactor.
- **Parent draft #685:** `1ab5eee2a7ff52baba83c2b9a98a0cd9737a02ae`; `research/2026-11-21/zero_seed_two_carry_r0/THEOREMS.md`—the paid `e_n` source-kick sparsity, exact signed digit `b+e+δ−16δ_prev`, and still-open raw quarter-sector statistic.
- **#684:** `d3de74a1cb410813cf56e4fc7a83a43e83642288`; signed source-lag and singular parity currents. Cannot infer the actual orbit from source-only covariance.
- **#682:** `8372048dff415c47da120afdff5df7696820dfe7`; direct source-to-parity character, prime-square signed counterfactual, carry orientation.
- **#681:** `29bf7d85d06d75d7592867168ac7a9c9239a2968`; constructed π Collatz parity word and classical Bernstein–Lagarias conjugacy; includes universal word controls.
- **#675 / #677:** original source-time Mellin/Fourier analyticity and finite↔analytic journal; native prime-square seam natural boundary is a different series from the actual π digit journal here.
- Sibling `femboy2112/collatz` (main `9fc94e742ca86c463beb71b9119d8687cf809bd1`) and `femboy2112/collatz-proof` (main `9e132eb17fca0e2b714d2a9ffb2e682001184d7c`) remain read-only; their Collatz CSTC / CYC / PD claims OPEN. This packet makes no Collatz termination deduction.

## Externally established (independently distinguished)

- **Pólya–Carlson dichotomy**, classical: statement and finite alphabet rationality criterion found e.g. `https://pure.mpg.de/pubman/item/item_3362941_5/component/file_3400691/MPIM-Preprint_2021-40.pdf` and `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/749C56946812A17EBFD4C3FFACDB16F4/S0017089500031372a.pdf/on_linear_recurrence_sequences_with_polynomial_coefficients.pdf`.
- **Zeilberger–Zudilin (2020), peer-reviewed:** `https://msp.org/cnt/2020/9-4/moscow-v9-n4-s.pdf`; bound `μ(π)≤7.103205334137...` (exact unrounded bound is in source). Use ν=7.104 with safe slack.
- **Generalized Kempner numbers, published:** `https://link.springer.com/article/10.1007/s00605-018-1244-1`, §4 explicitly states `sum_(n≥0)u^(-2^n)` (integer u≥2) has irrationality exponent **2**, and cites its earlier continued-fraction literature. The new shell estimate AZG-05 is proved here by elementary inequalities.
- **Bernstein–Lagarias 1996:** established 2-adic parity conjugacy used by SUCC #681. We use only the nibble grouping and elementary implication about eventual periodicity, not a Collatz integer theorem.

## External NEW CLAIM: keep separate

- `https://github.com/openai/math/tree/main/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026` (OpenAI, 2026); claimed `μ(π)=2` theorem.
- `https://github.com/openai/math/blob/main/lean/docs/017.md` (formalization scope). Released Lean/comparator evidence exists, but *this work did not independently run or audit that build*, and independent specialist confirmation is not established here. The stronger bound `ν=2+ε` is therefore a **conditional imported corollary**, not a new SUCC status promotion.

## Computational scope / independence

`source_to_digit.py` implements one exact-Fraction BBP rational prefix route. `independent_audit.py` is separately authored, derives the same source from an independent compact rational formula and Mellin polynomial, checks periodic rational shadows and finite Kempner phase enclosures with exact rational arithmetic. Both share the source definitions and classical BBP premise; they are **not independent mathematical referees**. Neither program tests the infinite Pólya–Carlson or irrationality-exponent theorems. Full inherited SUCC root suite, formal Lean, external experts, hosted CI and original source writes are not included in this packet.
