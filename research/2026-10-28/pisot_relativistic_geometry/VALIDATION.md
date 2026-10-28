# Validation receipt — source-faithful Pisot/Hopf arithmetic clocks

**Date:** October 28, 2026. **GitHub baseline:** Main XIII `b763ba8ef375fbac221e29e4396989a635a6ef36`. Original research PR #333 verified code blob `8305e09892f19007e0ae0538a60d05954b2def9e` on Main XIII. This is an independent additive research branch, not authorization to modify original files.

## Actually executed in isolated local stage

- `PYTHONPATH=<stage> python -m unittest -v tests.test_hopf_source tests.test_pisot_hopf_arithmetic_relativity tests.test_pisot_fixed_point_recovered tests.test_hopf_main_source_bridge`: **55 tests collected, 53 passed, two intentionally skipped** because local scratch contains only staged additions and not the complete SUCC package. Details in [`validation_receipts/VALIDATION_TESTS.log`](validation_receipts/VALIDATION_TESTS.log).
- `python scripts/pisot_rank_four_certificate.py`: PASS exactly over finite field F5 (irreducibility criterion). [`VALIDATION_PISOT.log`](validation_receipts/VALIDATION_PISOT.log).
- `python scripts/arithmetic_relativity_sympy_oracle.py`: PASS. Distinct SymPy symbolic implementation of mixed harmonic square and curvature at a source-plane origin. [`VALIDATION_SYMPY.log`](validation_receipts/VALIDATION_SYMPY.log).
- `sha256sum -c research/2026-10-28/hopf_local_archive/SHA256SUMS.txt`: PASS for original 14 manifest-listed text files. [`VALIDATION_ARCHIVE_SHA.log`](validation_receipts/VALIDATION_ARCHIVE_SHA.log).
- `python -m compileall -q observational_succ tests scripts`: PASS in local staging.
- An initial Fibonacci test incorrectly used F25 while asserting an F24 asymptotic. It failed, was corrected to F24, then entire suite reran successfully. Original tests and failures are not falsely counted as successful runs.

## Not run / scope

- The full native SUCC suite (`python -m unittest discover -s tests -p 'test_*.py'`), original archived imports, `scripts/verify_provenance.py`, observer foundations, ordinal reports, Lean kernel, hosted CI are **not** runnable in the isolated scratch tree. They are **mandatory before merge or theorem-authority promotion**. The two cross-worktree source-verification tests will run only on actual checkout.
- The canonical claim catalog/registry wasn't mutated: new IDs AR-01..AR-10 are explicitly research-local in the dossier, pending maintainer namespace reconciliation. Do not pretend new manuscript notes have been registered by the catalog.
- No original π normality fixed-h Weyl signed saving has been established. Neither SU2 gauge curvature nor an inconsistent-clock defect proves GR curvature or real time dilation.

## Reproduce on a complete SUCC worktree

```
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python -m unittest -v tests.test_hopf_source tests.test_pisot_hopf_arithmetic_relativity tests.test_pisot_fixed_point_recovered tests.test_hopf_main_source_bridge
python scripts/pisot_rank_four_certificate.py
python scripts/arithmetic_relativity_sympy_oracle.py
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Inspect both original `rank_two_chiral_towers.py` and new `hopf_source_exact.py` simultaneously before asserting source equality beyond focused tests. Observe exact original four pole forcing and U0=0 as nonnegotiable.
