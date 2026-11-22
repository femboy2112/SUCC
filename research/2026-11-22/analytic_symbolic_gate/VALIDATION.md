# Reproducibility and proof-status receipt — 22 Nov 2026

Execute from this dossier directory:

```sh
python -m unittest -v test_source_to_digit.py
python independent_audit.py
python -m compileall -q source_to_digit.py test_source_to_digit.py independent_audit.py
```

**Local scoped results:** 21/21 unittest methods PASS; standalone SymPy/Fraction independent implementation **13,641 exact assertions PASS** after correcting a test expectation at a canonical `0.FFFF... = 1.000...` endpoint. This was an audit-test bug, not a revised source theorem; the negative endpoint case is now separately asserted. `compileall` PASS. Machine-readable independent audit receipt in `independent_audit_receipt.json`; raw logs will be generated and checked when packaging this tree.

**Proved on paper here from specified imported results:** AZG-01–04, AZG-05 elementary R0 upper bound. **External un-rebuilt premises:** Pólya–Carlson theorem, peer-reviewed published upper bound μ(π), published generalized Kempner exponent-two theorem. **Unrefereed here:** OpenAI 2026 claim μ(π)=2; the stronger repetition rate is conditional. No finite computation confirms any of these imported infinite theorems.

**What the finite checks actually do:** original four-pole source via two rationally independent expressions and Mellin moments; monotonic positive source; 48 hexadecimal digits of π/16 certified by exact rational tail; periodic rational shadow exact long division, including the all-F endpoint pitfall; 64-bit-scale Liouville factorial-gap inequalities as algebraic checks; finite Kempner phase-square upper bounds on shell B=2,4,8,16,32,64; safe ε-budget formula. Each finite check can fail and is compared with negative controls.

**NOT executed:** inherited SUCC ~14k+ tests, scripts/verify_provenance.py, scripts/observer_foundations_probe.py, scripts/ordinal_succ_report_probe.py, hosted CI, Lean, third-party specialist referee, physical experiments. No external Collatz proof or normality result is asserted.

**Output interpretation:** the actual π digit-generating natural boundary and repetition bounds are genuine selected-endpoint results. They are **not yet source-derived all-shell statistical estimates**. Both natural-boundary complexity and even ideal irrationality exponent 2 admit the known nonnormal generalized Kempner model; R0 remains OPEN.
