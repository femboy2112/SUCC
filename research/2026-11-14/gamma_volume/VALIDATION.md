# Validation and reproducibility

## Executed checks

| Check | Result | Receipt |
|---|---|---|
| Full inherited discovery suite | **13,233 tests PASS** in 1109.304s | `receipts/full_baseline.log`, `receipts/full_baseline.json` |
| Final focused Gamma, wavefront, and knowledge-volume suites | **119 tests PASS**, including **24 new tests** | `receipts/focused.log`, `receipts/focused.json` |
| Original archive provenance | **PASS**, 72 items, including 17 byte-identical archives | `receipts/provenance.log`, `receipts/provenance.json` |
| Observer foundations probe | **PASS** | `receipts/foundations.log`, `receipts/foundations.json` |
| Ordinal SUCC report probe | **PASS** | `receipts/ordinal.log`, `receipts/ordinal.json` |
| Separate source/integral audit | **69 exact checks, 102 numerical diagnostics, 6 detected mutations, zero failures** | `receipts/independent.json` |
| Root production replay | **342 exact matrix-power cases, 648 rank/certificate replays, 39 source/stability comparisons, 9 finite-prefix error bounds PASS** | `receipts/root_replay.json` |

The full discovery run was started before this round's two new test modules were written. It exercises the inherited suite at parent `5258eec596ddc882a9063eb6bd01d4e955fe5971`. The final focused run separately collects both new modules and their relevant existing dependencies/regressions. The counts overlap; they must not be added as independent observations or presented as one monolithic run of the final tree.

Commands use `PYTHONPATH=.` so subprocess probes receive the repository import root. The pinned historical objects required by the inherited registry tests had already been fetched during #633. No implementation change was needed for either environment condition in this round.

## What the exact tests actually compare

The source-volume tests recover the inherited unit-depth `SourceGeometry` law and the shape-two endpoint. They compare integer grades against explicit geometric-stage allocation, fractional prefactors against finite convolution, moments against multinomial integration, and determinants against permutation expansion. Exact BBP intervals certify Hankel sizes one through five. Fixed-source, zero-depth, real-source-redraw, wrong-domain, float, boolean, and budget controls are retained.

The observer tests replay both successful quotient certificates and explicit collision witnesses. A forward rank oracle checks 729 rational source/report cases. The sharp alias is checked in both a two-dimensional rational model and a positive six-cycle. The latter has a genuine stochastic Gamma matrix and a descended signed observable mean; no full report-distribution lumpability is inferred.

The root's separate replay uses SymPy matrix inversion/powers and rank calculations on a different rational grid, Jordan blocks, and cycle orders one through twelve. It replays every finite source moment and Hankel coefficient from the independent source receipt against production, verifies stable multiplier bounds, and checks the analytic truncation majorant on nine cycle/operator cases.

## Separate reconstruction and numerical status

`independent_audit.py` imports neither production module. It reconstructs the source as `(4−2x³−x⁴−x⁵)/(16−x⁸)`, proves the cancellation and elementary integral symbolically, checks moments through order eight by two exact algebraic routes, and certifies Hankel dimensions one through five using a direct 24-term rational BBP enclosure. Floating-point pi does not determine these signs.

At 70 working decimal digits, the largest numerical identity discrepancy is approximately `3.46428e−40`, with acceptance tolerance `1e−32`. The smallest detected wrong-sign/wrong-power gap is approximately `0.09653`, against a mutation threshold `1e−8`. Raw holdouts, values, tail estimates, parameters, library versions, and exact-versus-diagnostic labels are in the receipt. The numerical integrals test the conjugation and Mellin/log-Fourier implementations; they are not universal proof certificates.

## Invocation history and repairs

A focused rerun initially mistyped `tests.test_nonlinear_foresight` as `tests.test_nlinear_foresight`. The resulting single import-selector error is retained in `receipts/focused_selector_error.json`; the corrected final command passed all 119 tests. This was a command typo, not a mathematical counterexample or a source-code defect. No failed run is relabeled as passing.

Internal mathematical review found no unresolved error in the scoped proofs and tightened the Banach-space, Bochner-integration, endpoint-limit, and logarithm-branch wording. The agents share the same model family and source provenance; this is not external peer review or independent empirical corroboration.

## Reproduction

From the repository root, with Python 3.12, SymPy, and mpmath available:

```sh
PYTHONPATH=. python -m unittest tests.test_gamma_source_volume tests.test_gamma_observer_descent tests.test_wavefront_oracle_two_stage tests.test_wavefront_oscillator_completion tests.test_pascal_gamma_turn tests.test_predictive_horizons tests.test_nonlinear_foresight -v
PYTHONPATH=. python research/2026-11-14/gamma_volume/independent_audit.py
PYTHONPATH=. python research/2026-11-14/gamma_volume/root_replay.py
PYTHONPATH=. python scripts/verify_provenance.py
PYTHONPATH=. python scripts/observer_foundations_probe.py
PYTHONPATH=. python scripts/ordinal_succ_report_probe.py
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

The independent audit writes a fresh receipt containing its script hash and execution metadata; the root replay reads that receipt and checks its hash before comparing production results. `FILE_HASHES.json` binds all payload files except itself. Remote publication is checked by exact Git-tree equality with the local staged deliverable. Local runs do not assert a hosted CI result or Lean verification.
