# Validation — Principia Intermedia

This file records actual execution, separately from mathematical proof authority.

## Focused results

At the initial complete code checkpoint, the root executed:

~~~sh
python -m unittest tests.test_principia_intermedia tests.test_principia_place_seam tests.test_principia_bbp_seams -v
~~~

Result: **51 tests PASS**, exit 0. After preserving and integrating #691, the root reran these tests together with the environment-corrected inherited failing test: **52 tests PASS**, exit 0, 0.140 seconds. The exact command and result are below. The universal theorems are paper proofs; no finite suite certifies an infinite path, every degree or all rational absolute values.

Three method-separated oracle runs also returned exit 0:

| Instrument | Observed scope | Receipt |
| --- | --- | --- |
| Direct path and assignment enumeration | 1,024 anchored graphs; 65,536 seam models; 16,384 source-tag cases; 1,944 transport models; 12,400 rational paths; 114 lattice paths; retained mutations | FINITE_ORACLE_RECEIPT.json |
| Independent prime valuations by repeated division and rational magnitude reconstruction | 33,073 counted checks, plus 2,542 reconstruction assertions under the documented counting convention | PLACE_ORACLE_RECEIPT.json |
| SymPy determinant polynomial construction, Sturm root isolation and inverse-Gram comparison | degrees 1–8; 119 fresh integer coefficient capacity cases | SOURCE_MOMENT_RECEIPT.json |

The native and oracle algorithms differ; their source formulas and mathematical premises are shared. These are stronger implementation checks, not blinded independent proof refereeing.

## Inherited repository gates

The full root unittest discovery was started from parent #690 before the additive implementation was written:

~~~sh
python -m unittest discover -s tests -p 'test_*.py'
~~~

Result: **14,612 tests in 1,170.748 seconds; 1 error, 2 skips; exit 1**. The sole error was `test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`. Its subprocess runs `scripts/meta_choice_descent_probe.py`; in this fresh, uninstalled checkout that child could not import `observational_succ`. The probe and test are byte-identical to the #690 baseline. The repository README and CI install the package before testing. A controlled recheck reproduced the import failure without `PYTHONPATH` and passed the exact same test with `PYTHONPATH=.`. No production code was changed to suppress it.

After integration, the root executed:

~~~sh
PYTHONPATH=. python -m unittest tests.test_principia_intermedia tests.test_principia_place_seam tests.test_principia_bbp_seams tests.test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count -v
~~~

Result: **52 tests PASS, exit 0**. This is a scoped corrected-environment recheck, not a second clean full-suite run. Both the original error and its diagnosis are retained in the raw logs.

The root provenance checker passed with 72 entries, 17 byte-identical archived research records and 55 mechanical namespace migrations. The observer-foundations and ordinal probes exited 0. All three were rerun successfully on the integrated tree. Their historical RH-open output describes their original scope; no historical status was silently rewritten.

All three new independent oracles were rerun successfully from their final renamed directory, and the inherited #691 Fraction two-place oracle also exited 0. The new oracle outputs reproduce the saved receipts exactly. Mathematical dependencies are still shared; these reruns are implementation evidence.

## Raw execution evidence

- [Original full baseline suite](validation/baseline_tests.log)
- [Controlled import-path failure and successful recheck](validation/baseline_error_recheck.log)
- [Integrated 52-test run](validation/principia_integrated_tests.log)
- [Integrated provenance checker](validation/integrated_provenance.log)
- [Integrated observer-foundations probe](validation/integrated_observer.log)
- [Integrated ordinal probe](validation/integrated_ordinal.log)
- [Inherited BBP two-place oracle recheck](validation/inherited_two_place_recheck.json)

The three independent new oracle receipts are linked in the table above. `git diff --check` also passed.

## Scope

No external RH Lean development was built here. No local formal-kernel proof of this dossier, external peer review, hosted exact-head CI or main-branch integration is claimed by these local receipts. The research branch is additive, stacked on #691 and intended for draft review. The original #691 validation statements remain historical; this supplementary record adds the executions performed here.
