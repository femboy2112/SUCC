# Spectral validation receipts

All commands ran in this directory. No original source or history was edited.
The full campaign runner/hosted-CI status is reported by the parent package.

- `python -m unittest -v test_spectral.py`: final **14/14 PASS**,
  `focused_tests_controls.log`, Python3.12.3. Earlier12-test passing logs
  remain in `focused_tests.log` and `focused_tests_final.log`.
- Python3.13.13 from the preserved `SUCC-gamma-twist/.venv` ran
  `run_probe.py`: **36 certified finite Gram bounds PASS**, all below1;
  **17 certified counterexamples** to the overly strong finite-window floor1.
  `probe.log` and `probe_receipt.json` preserve the results.
- The same3.13 interpreter ran `independent_oracle.py`, with mpmath1.3.0
  and SymPy1.14.0: **36 interval comparisons PASS**, independent direct-prefix
  reconstruction and Q/Z recursion, symbolic original-source gap positivity,
  three symbolic mark derivatives, and four exact polynomial Gram identities.
  `independent_oracle.log` and its JSON receipt preserve the results.
- `geometry_controls.py`: **PASS** exact clock passports, inherited golden/Oily
  second coefficients,5jet levels,5quartic-mutant rational circle differences,
  and9rigorous coherent same-source energy bounds. Raw log and JSON retained.

The initial primary spectral probe failed at output serialization because
Python's4300-digit limit was exceeded by unnecessarily large exact rational
endpoints. No mathematical assertion failed. The exact initial source is
`spectral_probe_initial_failed.py`, SHA256
`e692a6a7060f2a94804c215fbee70fe1f9eb25215a73fa2d140ccd5ba1bbf5e2`;
`probe_initial_serialization_failure.log` retains the failure. The repair
uses a uniform exact dyadic quantization-error bound and rounds final cosine
endpoints **outward** to denominator2^96. Final tests and the separate oracle
passed. This failure is neither discarded nor counted as a passing run.

The trigonometric certificate uses rational Machin bounds on π, exact rational
phase reduction, explicitly paid dyadic rounding, and a Taylor remainder.
The independent100-digit oracle is a cross-check, not the source of rigor.
The observer polynomial checks are exact symbolic arithmetic. Finite cases
do not prove any asymptotic statement or source-selected near-unit energy.

Reproduce in a fresh copy of this directory after preserving/removing only
the copied generated receipts, because `run_probe.py` and geometry generation
refuse to overwrite existing JSON. The tests alone can be rerun directly:

```
python -m unittest -v test_spectral.py
python run_probe.py
python independent_oracle.py
python geometry_controls.py
```

The latter two require the stated mpmath/SymPy dependencies. No new Lean proof
was attempted in this front. `DIOPHANTINE_REVIEW.md` is a complementary
same-model review of a specific theorem-file hash, not an external referee.
