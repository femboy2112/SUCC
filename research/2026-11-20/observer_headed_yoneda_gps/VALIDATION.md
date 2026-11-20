# Validation receipts — Observer-Headed Yoneda GPS / ECC

**Date 2026-11-20.** Research-only. The local working directory was `observer_headed_yoneda_gps/` in an isolated container. No copy of the full SUCC repository was cloned. Full root tests and mandatory root provenance, observer, ordinal probes were **not** run here. No hosted CI or Lean assertion is made.

## Exact executions

```sh
cd observer_headed_yoneda_gps
python -m unittest -v test_observer_pinbed.py
python independent_audit.py
python -m compileall -q observer_pinbed.py test_observer_pinbed.py independent_audit.py
```

- **Focused standard-library unit tests: 33 tests, all OK**, including exact source-state arithmetic, five-vs-seven BBP clock ranks, one adversarial corrupted reading at **each** of seven clocks, GPS head geometry, five GPS fault positions, XOR synergy, source-typed frame transforms, exact two-forward-path gauge comparison, late-circle seed alias, and finite-terminal locked counterseed.
- **Independent SymPy formula audit PASS**, written without importing `observer_pinbed.py`: reconstructed all seven BBP raw state rows from the signed poles, found all **21** selected 5×5 determinants strictly positive, verified source `[4,-2,-1,-1]`, recovered the original after one corrupted reading, and checked 13 exact finite-terminal compensation/lock instances. First five-clock determinant `32768/17039726835256125`, matching pinned #671.
- **Independent synthetic GPS audit PASS**: all **10** three-row minors in the rational 2D five-head bank are nonzero, and the source position/clock vector is recovered after a reading mutation.
- **Independent synthetic GPS conditioning diagnostic** (NumPy floating-point, not a rigorous interval): well-spread geometry `sigma_min=1.4142135623730951`; five clustered distinct unit directions `sigma_min=0.0005285990768019303`; ratio `2675.399228710743`. Exact symbolic determinants certify both are full rank. These are geometrically normalized dimensionless examples, not real GPS accuracy estimates.
- **Compilation**: `python -m compileall -q ...` exit 0.
- **Raw logs**: `test_execution.log` and `audit_execution.log`; exact independent JSON in `independent_audit_receipt.json`.

## Failure discovered and repaired during development

The first independently written audit attempted to multiply a Python list representing one source row by a SymPy Matrix, triggering a `TypeError`. The audit was corrected by explicitly converting the row to a one-row `SymPy.Matrix`. Only the corrected script was counted as passing. This is not a failed mathematical claim or a previous independent success; the failing trace was observed and repaired before publication.

## What was not tested

- The full inherited SUCC 14k+ unit suite, mandatory provenance verifier and foundation/ordinal scripts, hosted GitHub CI, Lean, external referee or an actual physical measurement.
- Arbitrary infinite future laws beyond the specified five-parameter BBP family; unknown real noise distributions/correlated faults; physical GPS pseudoranges outside local linearization.
- Any uniform all-B signed Weyl estimate, R0, pi normality, RH, classical-vs-quantum discrimination or physical zero-point energy.

## Reproducibility and interpretation

Every test uses exact `fractions.Fraction` and stdlib algebra except the **independent optional** SymPy matrix and NumPy singular-value audit. All source-reconstruction claims condition on known pole labels, clocks, *unwrapped* scalar state readouts and an authenticated parameter family; this is source testing, not new proof of a global BBP statistical property. The independent audit shares that pole formula as an explicitly declared premise, not independent source authority.

For remote uploads compare every GitHub blob SHA to the corresponding locally tested file; in particular, preserve all original trailing newlines. Repository validation on a final remote head is separately required before merge.
