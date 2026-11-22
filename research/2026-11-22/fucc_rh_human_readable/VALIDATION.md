# Local finite validation — FUCC arithmetic multiplicity and RH proof spine

**Date:** 22 November 2026. These checks validate exact finite arithmetic identities and the scripts in this research directory; the all-order paper proofs are given in `TECHNICAL_PROOFS.md`. They are **not** tests of Alpöge's 175,187-module Lean archive, nor a proof of RH.

## Executed commands and results

```sh
python -m unittest -v test_fucc_rh_bridge.py
python independent_audit.py
python -m compileall -q fucc_rh_bridge.py test_fucc_rh_bridge.py independent_audit.py
```

- Focused stdlib tests: **10/10 PASS**, exit 0. Full raw output `focused_unittest.log`.
- Independent SymPy implementation: **514 exact assertions PASS**, exit 0. Tests true finite shift matrices, the logarithmic commutator, direct Riesz vacuum coefficient, independently generated formal-logarithm inverse, local p-adic valuation bounds, and Hadamard integer determinant. See `independent_audit.py`, `independent_audit_receipt.json`, `independent_audit.log`.
- Python compilation: **PASS** (exit 0).
- Markdown link/manifest validation: checked separately, exact SHA256 manifest `SHA256SUMS.txt`.

## Scope and independence

The independent path uses SymPy matrix and formal-series computations rather than importing the stdlib model module. Both implementations use the same underlying arithmetic definitions, so this is **implementation independence**, not an independent mathematical derivation or a referee certificate. The finite checks do not establish the full local theta-kernel integrality, the global number-field lattice-slope estimates, trace-formula rank bounds, or the main arithmetic inequality (M).

## Hostile controls

- **Fake-six:** the prime-power source never produces V_6 because 6 is not a prime power.
- **Missing Euler-log normalization:** removing 1/k changes the p^k coefficient to k log p; recognized as a mutation, not part of the valid code.
- **Unbounded evaluation:** V_p^a e_1=e_(p^a) retains unit coefficient despite support growth; p-adic valuation remains 0.
- **Local versus global:** local formal-logarithm tests do not exercise CM theta periods, covolumes, Harder–Narasimhan ranks or Galois cohomology.
- **No imported RH status promotion:** external formal verification is credited, not reproduced.

## Not run or claimed

SUCC inherited full Python suite, its mandatory root provenance/foundations/ordinal gates, hosted GitHub CI, Lean checking, Alpöge's original Lean archive, a new referee, or a complete human-readable proof of (M) or RH. Main XXVI, the literal four-pole BBP source, zero seed and prior provenance remain unchanged.
