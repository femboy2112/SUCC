# Validation and reproduction

Date: 2026-11-12. Base: `db9fb4b84672050efa79b13377f1e73364598a14`.
This is an additive research branch. Frozen provenance, the four-pole source,
zero seed, existing theorems, main and workflow files are unchanged.
No merge, tag, release, Lean run or external-referee certification is claimed.

## Finite rational results

The certified matrix is the normalized Gram of
`H[n,j]=e(16^(n+j) pi/16)` for `A<=n<2A`, `0<=j<=d`.
The source interval comes from the canonical rational BBP prefix and a proved
positive-tail bound at a common horizon. Character conversion uses the
existing independent Machin-arctangent pi enclosure and real Taylor error
bound. All source, character, averaging and square-root errors are paid.

All 13 prescribed cases (A=17,37,73 with d=1--4, plus A=109,d=4)
returned positive rational Gershgorin margins. The table rounds their
**certified lower bounds downward** to six decimal places.

| A | Columns | Certified lower bound on lambda_min |
|---:|---:|---:|
| 17 | 5 | 0.308859 |
| 37 | 5 | 0.389512 |
| 73 | 5 | 0.404835 |
| 109 | 5 | 0.692931 |

The exact rational matrices, source intervals, horizons and margins are in
[certified_gram.json](receipts/certified_gram.json). These certify only the
specified finite recurrence-residual inequalities. They are not evidence
of a uniform all-shell margin or an infinite signed-cancellation theorem.
The finite cases were fixed before the two implementations; the reserved
109 case is a same-session check, not an external blind validation.

## Focused verification

- 12 native certificate tests passed on the final implementation. They cover
  canonical forcing versus the four poles, common-horizon/local-tail identity,
  exact outward square roots, Haar-grid positive control, coherent/fixed/
  period-two negative controls, wide intervals, negative harmonics, Hermitian
  structure, and invalid inputs.
- The dossier dual-certificate tests cover exact local telescoping, sharp
  endpoint separation, source-domain restriction, gauge invariance, omitted
  errors, finite-tail transport, both denominator grid families, sharp
  Lipschitz and C² interpolation costs, and malformed budgets. Their final
  replay passed all 16 tests and is recorded in `receipts/dual.log`.
- All 11 exact Gaussian-rational intervention tests passed on root replay.
  They cover effective effects, coherence blindness, energy preservation,
  calibrated tomography, weak-coupling inversion, matched reversal,
  calibration error, and retained-record disturbance. Derivative and
  Duhamel statements are supported by written proofs, not these finite tests.
- 105 exact source-frame equalities and 35 deliberately false zero-seam
  mutants were checked by `crosscheck.py`. Another 105 exact rational
  exponent identities calibrate the rank-one 15-cycle that satisfies (CH).
- The separate high-precision oracle uses numerical pi and direct Hankel
  products, and separately recomputes Weyl difference-frequency sums.
  All 187 complex entries lie inside the rational certificate boxes. These
  numerical values do not serve as the enclosure's proof input.
- 16 hostile interval cases with 216 sampled numerical containment checks
  passed; all undersampled cases return INCONCLUSIVE. See the scope in
  [AUDIT.md](AUDIT.md) and [interval_oracle.json](receipts/interval_oracle.json).
- Exact zero and rational controls have the paper-predicted rank 1 or 2.
  The near-rational irrational control required 700-digit working precision
  to resolve its tiny positive numerical eigenvalue. It is a conditioning
  demonstration, not a pi theorem.

All review passes share one model family and repository provenance. They
use different derivations and implementations; they are not independent
referees or independent sources of arithmetic truth.

## Native gates and environment record

The complete native discovery run finished: **13,062 tests in 1,676.914
seconds, with one environment-related error**. Provenance (72 imported
items), observer-foundation and ordinal probes completed successfully.
The full run is preserved in `receipts/native.log`; it is not reported as
an all-green run.

The full discovery run began before one resource-limit repair: the new
certificate routine now limits the actual horizon including lookahead,
rather than only start+length+degree. An assertion was added to an existing
test method. The final 12-test focused replay passed. The mathematical
certificate formulas and sampled cases were unchanged. The before/after
file hashes, reconstructed from the exact applied patch, are retained in
[native_run_scope.json](receipts/native_run_scope.json).

An existing subprocess probe initially failed because this fresh checkout
had not been installed as a Python package. The error was
`ModuleNotFoundError: observational_succ` in `meta_choice_descent_probe.py`.
The local editable installation uses `--no-deps --no-build-isolation` and
does not alter repository source. **All 11 tests in the affected module
passed after installation**, including the previously failing subprocess
probe; see `receipts/environment_replay.log`. The 13,062-test discovery was
not repeated after that environment repair. No test failure is hidden or
relabeled as a mathematical failure.

## Reproduce

From the repository root, with the declared test dependencies available:

```sh
python -m pip install --no-deps --no-build-isolation -e .
python -m unittest discover -s tests -p 'test_boundary_filter_complexity.py' -v
PYTHONPATH="$PWD" python -m unittest discover -s research/2026-11-12/boundary_filter_complexity -p 'test_dual_certificate_probe.py' -v
PYTHONPATH="$PWD" python -m unittest discover -s research/2026-11-12/boundary_filter_complexity -p 'test_intervention_transducer_probe.py' -v
python research/2026-11-12/boundary_filter_complexity/probe.py
python research/2026-11-12/boundary_filter_complexity/oracle.py
python research/2026-11-12/boundary_filter_complexity/crosscheck.py
python research/2026-11-12/boundary_filter_complexity/audit_intervals.py
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The final content manifest binds the added artifacts, excluding itself.
Hosted CI is separate from these local runs and must be checked on the
published commit before any future integration.
