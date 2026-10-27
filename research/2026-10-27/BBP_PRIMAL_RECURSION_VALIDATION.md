# Validation record — Operation First-Primal Recursion (2026-10-27)

**Source head:** PR #321 `eeb2a48ea1b43967ea385009a3f8ec280b2efa69`; research branch `research/first-prime-binary-shear-ternary-trident-crt-2026-10-27`. Original Coherent Main X signed four-pole BBP and zero state unchanged. No main merge or historical source rewrite.

**What has been run locally:** exact source module and tests were executed on a local **minimal faithful test-only shim** for `observational_succ.succ_internal_matrix_walk.authentic_r`; the shim file is deliberately NOT in this PR. The imported complete `bbp_binwindow_conjugacy.py` from PR #321 is unchanged and its source was hashed by the receipt. The tests independently compare both the 4 original rational poles and canceled numerator/denominator at 200 positive times.

- `python -m unittest -v tests.test_bbp_primal_recursive_geometry`: **27 passing tests**, no failures/errors. Exact exhaustive bit-level permutations through 8 bits, held-out inverse code (including arbitrary 32-bit targets), an independently checked bounded-index modular source adapter, finite source recurrence comparisons through n=64 and depth 12, congruence/Hensel and 3-adic pole controls, and exact CRT full enumerations of 48, 144, 768, 2304 pairs.
- `python scripts/bbp_primal_recursive_probe.py --write` and `--verify`: **PASS**, source/test/parent-module SHA-256 stamped deterministic receipt, no floating π, no remote oracle.
- False-normality-proof flag mutation rejected because the recomputed receipt differs. Explicit witnesses also refute extrapolating first-level involution to mod32, three-form coincidence to mod9, 2-adic contraction to 3-adic convergence, and non-unit ternary scalar normalizations.
- Dossier separately presents universal paper proofs of binary shears, 3-adic numerator isometry, genuine 3-adic pole/nonconvergence, finite CRT product clock and arithmetic-character orthogonality. The 2-adic infinite-past zero at n=0 is an **inherited paper proof** pending independent Claude scrutiny.

**NOT run locally in this isolated tree:** native full 8,000+ test suite, archive provenance, observer/ordinal probes, pinned Lean, or hosted GitHub CI on the final commit. These require the combined authentic repository; Claude's handoff explicitly assigns them. **Do not report full/native/Lean/hosted success unless a real exact-head result is obtained.**

**Negative proof statuses:** π base-16 normality OPEN; RH OPEN; no new selected real Weyl `o(N)` estimate. The joint finite arithmetic Haar identity must NOT be promoted to real-circle mixing.

**Repro in native checkout:**

```sh
python -m unittest -v tests.test_bbp_primal_recursive_geometry
python scripts/bbp_primal_recursive_probe.py --verify
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The GitHub validation and source-hash receipt report should be refreshed at the exact published research head. A possible existing Python 3.10 CI job timeout does not imply a mathematical test failure.
