# Validation and reproducibility

Reference parent branch: `research/gamma-twist-selected-phase-2026-10-30`, PR #401, commit `abf51bf061f583d0e38a915c2e1bae5e28ddaace` at the start of this round. The parent itself is stacked on PRs #400→#399→#398, originating at Main XVI `e18ba565...`. Verify live GitHub refs before running.

## Runs actually executed

- `python -m unittest -v test_selected_boundary.py`: 12/12 exact Fraction tests PASS (`focused_tests.log`).
- `python independent_oracle.py`: nine rational Machin-π/Green-tail checks and 15 original-source exact phase-slip windows across h=1,3,7 PASS (`independent_oracle_receipt.json`).
- The first oracle mistakenly asserted that the 15-digit truncated decimal 3.141592653589793 was an upper endpoint. It is a lower endpoint, and the failed assertion is preserved in `initial_oracle_failure.log`. The final oracle uses the correct bracketing interval and also verifies direct rational Machin bounds.
- No root repository 10,008-test suite, AGENTS scripts, new Lean proof, or independent mathematical referee was run in this *local* session. The preceding PR #401 had green 19/19 hosted checks, but those do not certify this child.

## What the finite checks do not establish

No finite checks establish the asymptotic phase-slip theorem; that theorem uses the published finite irrationality exponent of π and the exact recurrence proof in `THEOREMS.md`. The unpublished/2026 exact π exponent-2 proposals are not used. Numeric frequency tests do not establish π normality. Theorem status is scoped to the exact source, fixed h, and the stated asymptotic quantified inputs.
