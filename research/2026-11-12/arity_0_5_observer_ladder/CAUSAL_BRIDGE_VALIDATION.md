# Validation — causal Bell bridge

**Local isolated environment:** CPython 3.13.5, `fractions.Fraction`, `unittest`; no floating-point oracle and no external packages. The model is stdlib-only, mathematical/exact, independent of the installed application backend.

```
cd /mnt/data/causal_bridge_round
PYTHONPATH=. python -m unittest discover -s tests -p 'test_causal_bridge_observers.py' -v
```

**Observed:** 20 tests, 19 pass, 1 skipped (canonical `observational_succ.duck_bbp` source is not installed in the isolated staging overlay); no failures. The on-repo full checkout should execute that exact cross-check unskipped and compare `r(n)`/`U_n` against the frozen source for `n=1,...,69`.

Exact test families: 25 rational common-gauge choices with different source pins, future-causal admissibility and event/frame mismatch rejection; both observers' identical marginal states for arbitrary rational phases; XX and XY at all four quarter-turns; formal group-algebra representation at the authentic first forcing phase `2/15`; chosen dephased mixture vs Bell correlations; a false product bridge; Choi operator slide for `5^4=625` exact Gaussian-rational matrices (including nonunitaries); original zero seed and a `1/16` hostile counterseed over 50 exact clocks.

**Proof status:** All-path gauge result and all-d matrix mirror identity have short paper proofs. Tests check finite instances only. The quantum state preparation and local phase interactions are declared, not shown to occur physically. `π` digit statistics, novel signed Weil estimates, ER=EPR bulk geometry, and RH are not inferred.

**Mandatory full repo tests at pushed SHA (NOT run by isolated test):**

```
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

After push, compare all new file hashes with staged bytes, and check GitHub CI at the **exact new commit**. The optional source check is expected to run under full checkout; record result without inferring from its parent.
