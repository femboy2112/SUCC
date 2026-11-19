# Validation receipt and exact provenance scope

**Execution environment:** Python 3.13.5, SymPy 1.14.0; staged research directory (not the complete SUCC checkout). **Immutable parent target:** SUCC PR #669 head `5a71c7e33f0445236fd4f69da872ca5c71d1530d`, Main XXVI `81be6b897ae980b801a3b9de9e22ef81e8360bfb`.

## Executed locally (PASS)

```sh
python -m unittest discover -s tests -p 'test_*.py' -v
# 18 focused tests PASS (no failures, errors, skips)
python research/2026-11-19/source_selected_hensel_holonomy/probe.py
# exact standard-library Fraction/integer receipt PASS
python research/2026-11-19/source_selected_hensel_holonomy/independent_sympy_oracle.py
# independently implemented SymPy matrix, source-jet, asymptotic, nine-prime holdout PASS
python -m compileall -q research tests
# PASS
```

Raw stdout/stderr in `RAW_VALIDATION.log` (does not contain secrets). The tests include exact original four signed rational poles and zero seed, exact source-filter determinant, mod-11 image/kernel and normalized dual eigenrow, Hensel roots mod 121/841 and higher 11-adic precision, both candidate source mutations, moving-frame correction, exact false-Weyl locked control, original ordered-source counterfactual, its four source-amplitude Jacobian entries, prime-square valuations and residues, and quantified logarithmic future visibility. The independent oracle does not import `probe.py` and checks symbolic real asymptotic constants.

Source/fingerprint controls: `p=29` matches homogeneous Fibonacci/radix order but has a source-filter unit determinant; `H+t^4` changes source-filter determinant; stronger `Q+(1-t)^2` preserves source mass zero, first jet, positive forcing, and n^-2 leading term while breaking **both** 11-adic selection and prime-square residue. Same-forcing nonzero seed leaves source innovations/order commutators unchanged; reference-frame complex modulation can fake cancellation on `z_n≡1`.

## Not run / NOT claimed

Full inherited SUCC 14k+ unittest discovery, root `scripts/verify_provenance.py`, `scripts/observer_foundations_probe.py`, `scripts/ordinal_succ_report_probe.py`, GitHub hosted workflow, Lean kernel, independent external mathematical referee, actual all-late-shell signed cancellation, R0, base16 π normality, RH, or Collatz. The exact proofs are paper derivations with independent computational checks, not formal universal-proof certificates. One assistant model plus a separate SymPy implementation is not blind independently sourced peer review.

## Source and mutation rules

All original BBP source files, zero-seed definitions, imported provenance and historical claim ledgers are read-only. The altered polynomial `Q+(1-t)^2` is used only in explicit hostile regression tests; it is not used as replacement original forcing. p-adic modular readouts are not identified with Archimedean Weyl phases absent a separately proven transport.
