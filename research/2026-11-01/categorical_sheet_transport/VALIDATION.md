# Validation and boundaries

Parent PR #447 was read live at head 6fedcbe445f856878ecb1b1d9a0a84ad97a77e2e.
Read AGENTS.md, docs/METHOD.md, docs/FOUNDATIONS.md, and the actual existing
ObservationPathCategory / FiniteCarrier / Instrument interfaces at that head.
No existing source or production path is modified by this additive package.

## Actually executed locally

Environment: Python 3.13.5, SymPy 1.14.0.

* `python -m unittest discover -s tests -p 'test_categorical_sheet*.py' -v`:
  **68 discovered, 65 PASSED, 3 SKIPPED**. The three skips explicitly require
  the real upstream core, which was not mounted. They are NOT counted as passes.
* The same 68 cases run in reverse order: **65 PASSED, 3 SKIPPED**.
* Optional symbolic_audit.py: **14/14 exact symbolic checks PASS**.
* Optional build_global_certificate.py: **EXACT_CERTIFICATE_REGENERATION_PASS**;
  regenerated JSON equals the retained Bezout certificate, not merely its decimals.
* Python compileall for all new research and test code: PASS.

The universal two-frame inverse and implicit curve are checked by stdlib integer
polynomial multiplication, not finite sampling. The global three-frame theorem
is checked by expanding its integer Bezout identities. Rational GCD decoding
is a different reconstruction algorithm from the subresultant-derived inverse.
Four-pole source arithmetic is compared to the independent combined rational
expression and convolution. Fourier covariance is compared against exact kernel
orthogonality conditions. Same principal model and same original source: these
are independent calculations, NOT blind independent reviewers.

Controls retain: changed seed; changed recurrence; off-curve pair/triple; corrupted
inverse coefficient; corrupted Bezout multiplier; naive rebranching span; erased
central phase; wrong conductor translation; finite dilation alias; nonunit map;
projective infinity and source poles; the divergent point-evaluation norm.

## Failure/repair record

A direct git checkout failed because the container could not resolve github.com.
The live connector remained usable; consequently this is a self-contained additive
workspace, NOT a full repository checkout. Raw-download attempts also failed.
An initial optional symbolic audit exceeded a 20-second execution limit during
unfactored rational simplification. Using exact factored/together simplification
completed the same 14 checks. No mathematical claim or test case was removed.

## Not run / not claimed

Full SUCC root suite (>10k tests), verify_provenance.py, observer_foundations_probe.py,
ordinal_succ_report_probe.py, and the three actual existing-core adapter tests were
NOT run locally. No new Lean kernel theorem, external referee, physical realization,
source-selected all-horizon signed bound, pi-normality proof or RH proof is claimed.
Hosted CI is a separate observation; no future success is predicted here.

The inherited 44 PR447 tests and the reported Main XVIII suite are not counted as
new runs in this round. The package checks the relevant source baseline directly.
