# Validation receipts

## Completed targeted verification

- New module: **31/31 unit tests pass**, exact arithmetic, including hostile
  source, normalization, realization, dynamic and target-truth cases.
- Independent piecewise-polynomial oracle: **2,722 checks pass**, including
  **8 rejected mutations**. The root executed the committed independent file.
- Independent finite affine oracle: **28,864 models pass**; 192 on F2² and
  28,672 on F2³, all linear maps, translations, single nonzero character seeds
  and state pairs in the stated scope.
- Four locally predeclared authentic source epochs: **A=17,31,61,127**, exact
  rational energy, all source values replayed using four signed fractions.
- `verify_provenance.py`: SOURCE_PROVENANCE_VERIFIED; 72 preserved items.
- `observer_foundations_probe.py` and `ordinal_succ_report_probe.py`: exit 0.
- Figure rendered and visually inspected. Its floating-point curves are display
  only; mathematical equality claims use the exact code and proofs.

## Required repository-wide suite: environment finding and rerun

The first full run on the pinned baseline executed **12,147 tests** in 1000.882
seconds and reported one error: an existing subprocess entrypoint,
`scripts/meta_choice_descent_probe.py`, could not import `observational_succ`
from an uninstalled checkout. The raw failure is preserved in
`BASELINE_TEST_LOG.txt`; it was not caused by the new research module.

Re-running that unchanged test module with the repository root on PYTHONPATH
passes **11/11** tests (`IMPORT_RECHECK_LOG.txt`). No historical source file or
test was changed to suppress the error. A complete suite rerun with that import
setup was launched; its final result will be recorded before task completion.

The complete rerun began before the last fail-closed input-shape/docstring
cleanup of the new module. The final new module and its expanded malformed-input
cases were separately replayed: all 31 targeted tests pass. Original modules
and tests are unchanged throughout. The exact source energy receipt was also
replayed, with every rational value unchanged; first-run hashes are preserved
in `FIRST_RUN_HASHES.json`.

## Fresh original-source observations

The intervals below are outward-rounded from exact rational values, not
floating-point confidence intervals. Complete fractions, source trace hashes,
implementation hashes and comparison flags are in `FINITE_RECEIPT.json`.

| Epoch [A,2A) | Exact energy inside this decimal interval |
|---|---|
| [17,34) | [0.000421742253535272, 0.000421742253535273] |
| [31,62) | [0.000088837002812007, 0.000088837002812008] |
| [61,122) | [0.000038872292194705, 0.000038872292194706] |
| [127,254) | [0.000027806030528424, 0.000027806030528425] |

These four values are finite observations. They do not establish a decay rate,
typicality or normality. The all-A surface norm comparison to the completed pi
orbit is proved separately, with squared error upper bound `1/(2700 A^4)`.

No Lean kernel check or successful hosted CI run is claimed here. Consult the
draft PR checks for hosted status at its current exact head. All changes are
additive research artifacts on a non-main branch; no merge is performed.
