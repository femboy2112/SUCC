# Validation and exact scopes

**Outcome:** new focused tests and all separately implemented audits pass.
The full inherited discovery ran **13,050 tests with one environment error**;
the documented import path repaired that error, and the affected **11-test
module plus its exact subprocess probe pass on rerun**. This is not described
as a single clean full-suite run. No inherited source or test was changed.

The research is additive on parent
`94c7252ac7db3c8b14229544087119bd9cc01933`. Universal analytic statements rest
on the written proofs; all finite results retain their exact or diagnostic scope.

## Executed research checks

| Command or instrument | Actual result | Scope / receipt |
|---|---|---|
| `python -W error -m unittest discover -s research/2026-11-15/gamma_phase_disintegration -p 'test_*.py' -v` | **28 tests PASS** | Exact Fraction/Gaussian-rational source identities, orthogonality, coefficient sign/normalization, error budgets, moments, domains, alias and rational-source controls; `receipts/focused_tests.txt` |
| Parent #651 focused discovery | **53 tests PASS** | Original coin, Green, Poisson and source contracts reproduced; `receipts/parent_focused_tests.txt` |
| `audit_forcing.py` | **1,913 assertions PASS** | 537 exact source, 763 exact boundary, 344 numerical Fourier, 16 direct quadrature, 240 complex Mellin, 13 mutation assertions; `receipts/forcing_audit.json` |
| `audit_modes.py` | **390 assertions PASS** | Exact orthogonality plus direct polynomial quadrature, finite product/tail checks, tensor control, inverse-Gamma CDF diagnostics and four detected mutations; `receipts/mode_audit.json` |
| `audit_resonance.py` | **36 exact checks + 75 numerical diagnostics PASS** | Original rate moments, interval/pole identity, cell factorization, all declared detunings and the tilt-sign mutation; `receipts/resonance_audit.json` |
| `audit_tilt_hierarchy.py` | **17 exact/symbolic checks + 36 numerical diagnostics PASS** | Both residue coefficients, unit-cell integrations, exact moments, rational moment-matching control and global remainder diagnostics; `receipts/tilt_hierarchy_audit.json` |
| Compileall of new Python files; JSON parse; staged `git diff --check` | **PASS** | Syntax, payload structure and whitespace checks |
| Scientific figure generation and visual inspection | **PASS** | `make_figure.py`, `gamma_mode_energy.png`, `receipts/figure_values.json` |

The test-method and assertion counts are different units and are not added
into one aggregate. Several mathematical identities are checked by more than
one instrument; repeated checks are not independent theorem counts.

## Required AGENTS.md gates

| Gate | Actual result | Receipt |
|---|---|---|
| `python scripts/verify_provenance.py` | PASS: 72 source items verified | `receipts/provenance.txt` |
| `python -m unittest discover -s tests -p 'test_*.py'` | 13,050 run; 13,049 pass, one subprocess import error | `receipts/full_unittest.txt`, `receipts/full_unittest_run.json` |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | `receipts/observer.txt` |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | `receipts/ordinal.txt` |

### Full discovery error and resolved environment cause

The failed test was
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`.
Its subprocess runs `scripts/meta_choice_descent_probe.py`, which could not
import `observational_succ`. Executing that probe directly reproduced
`ModuleNotFoundError`; the raw failure is retained in
`receipts/inherited_failure_probe.txt`.

The repository README documents `export PYTHONPATH="$PWD"` alongside editable
installation. Applying the documented setting without changing code gave:

~~~sh
PYTHONPATH=. python -m unittest discover -s tests -p 'test_eodcs_meta_choice_descent.py' -v
PYTHONPATH=. python scripts/meta_choice_descent_probe.py
~~~

The **11-test module passes**; the probe again certifies its exact 729 graph
cases, split into 393 flat and 336 obstructed. Receipts are
`receipts/inherited_failure_rerun.txt` and
`receipts/inherited_failure_probe_repaired.json`. The research reproduction
script now supplies the documented environment. The full suite was not
repeated after this isolated setup correction, and no fresh all-green
full-suite or hosted-CI result is claimed.

The full run began while additive research files were being assembled, against
unchanged inherited production and root-test bytes. The 1,666 Python files
under `observational_succ/` and `tests/` are hashed in
`receipts/inherited_python_hashes.json` and compared before commit. All new
research code is exercised separately as listed above.

## Exact versus floating-point authority

- `gamma_phase_probe.py` uses Fraction, exact Gaussian-rational products and
  factorial polynomial integrals. Its rational cutoff bounds rely on the
  written infinite-tail proof, not extrapolation from finite coefficients.
- Forcing and resonance audits use 70-digit mpmath; the mode audit uses 50
  digits. The tilt-hierarchy audit uses 90 digits and geometric depth 64,
  with exact omitted base mass `16^-64`. Direct quadratures and special-function values are **not interval
  certificates**. High-frequency forcing comparisons are scaled by the Gamma
  envelope so tiny numbers cannot pass vacuous absolute-error tests.
- Mode checks retain finite omitted energy and the finite degree mean. They
  never renormalize a prefix to pretend the discarded tail is zero.
- The inverse-Gamma scaling diagnostics record signed errors at frequencies
  5, 10, 20, 40 and 80. They do not impose or infer monotonic convergence.
- The resonance computation uses geometric depth 48; the omitted base-law
  mass is exactly `16^-48`. The report's values remain numerical diagnostics.
- The tensor numerical check uses an explicitly synthetic finite-atom law.
  It checks the general orthogonal identity, not an authentic BBP temporal
  joining. The original-source specialization is justified by the paper proof.

## Calibrated failures and review

The receipts distinguish wrong phase orientation, omitted factorial,
Gamma(1) substituted for Gamma(2), finite-prefix renormalization, a missing
source pole, and the one-gap boundary-zero mutation. Removing the inverse-square
source tilt reverses the surviving imaginary coefficient. A positive finite-cell control matches the authentic first three rate moments
and both resonance coefficients but has rational endpoint 35/264 and a locked
harmonic. The general-frequency
normalization correction and rejected small-n monotonicity assumption are
preserved in `REVIEW.md` and `RESONANCE_THEOREMS.md`.

Three same-model bounded agents and the root supplied different derivations and
cross-checks. This is not an external referee process. No Lean proof, hosted
CI result, physical sampling mechanism, arithmetic signed saving, R0 proof or
pi-normality proof is claimed.

## Payload integrity

`SOURCE_INPUTS.json` pins eleven inherited source/instruction documents by
Git blob and SHA-256. `SOURCE_MANIFEST.json` pins every final dossier payload
except itself. The branch publication is read back at its exact Git commit;
the final response identifies that commit and the draft PR. Repository-backed
research remains separate from historical main and preserved archives.
