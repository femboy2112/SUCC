# Validation, actual runs, and retained limitations

Base: `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`. Runtime: Python3.12.14,
SymPy1.14.0, NumPy2.3.5, SciPy1.17.0, mpmath1.3.0. No new dependency or
production-module modification is required. Native source/test bytes are
unchanged from the base; new executables/tests are isolated in this dossier.

## New code and exact probes

| Check | Actual result | Receipt |
|---|---|---|
| Dossier unittest discovery, final executable/test bytes | 47 tests PASS | `receipts/final-focused-suite.log` |
| Preregistered arithmetic / spectral / Haar probe | 74,229 checks,0 failures | `receipts/FINITE_REPORT.json`, `receipts/probe.log` |
| Arithmetic labels | Every integer2..10000, independent divisor-multiple table and marking sieve | Finite report |
| Even sum targets | Every even N4..2048, plus2458,4096,8192,16384 | Finite report |
| Actual beta/delta observer | First30 primes through113;3,181 beta and44,018 delta contractions | Finite report `beta_prefix` |
| Zero budget | UNKNOWN, empty observed prefix | Finite report `zero_budget_control` |
| Source/spectrum mutations | Six JSON field mutations rejected; additional unit/type/forgery mutations in tests | Finite report and test suite |
| Cylinder phase cancellation | Exact cyclotomic polynomial remainder checks; no floating tolerance | `test_cylinder.py`, cylinder test log |
| Cylinder source controls | Exact phase-clock, aliases, opposite twist, unit contamination, sparse two-kick paths, histogram transport | `receipts/CYLINDER_REPORT.json` |
| Fejér result | Exact rational bound9/1024 for X10000,K256, plus exact weight and integer Diophantine checks | Cylinder report; this is an analytic bound, not a sampled irrational-phase norm |

The74,229 count is the explicit number of assertions in `probe.py`; it does
not include assertions inside the47 unittest methods or any subagent's
separate diagnostic campaigns. Do not combine these into an invented count of
independent mathematical witnesses. Code SHA256 digests are part of the
finite report and final validation manifest.

## Required repository gates

| Command / gate | Actual result |
|---|---|
| `python scripts/verify_provenance.py` | PASS:72 imported items verified; `receipts/provenance.log` |
| `python scripts/observer_foundations_probe.py` | PASS, exit0; `receipts/observer-foundations.log` |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit0; `receipts/ordinal-succ.log` |
| `python -m unittest discover -s tests -p 'test_*.py'` | Completed13,047 tests in1055.659s:13,046 passed,1 subprocess import-path error; `receipts/native-suite.log` |
| Untouched-base reproduction | Same script fails with `ModuleNotFoundError: observational_succ`; `receipts/untouched-base-import-replay.log` |
| Corrected targeted replay with `PYTHONPATH=.` | All11 tests in the affected module PASS; `receipts/native-failure-corrected.log` |
| Full retry with corrected environment | INCOMPLETE / UNVERIFIED; execution handle was no longer available, and the retained log has no final summary. Not counted as a pass |
| Mathematics catalog and graph | Final regeneration/check results recorded in `receipts/catalog.log` and `receipts/math-memory-graph.log` |

The single completed native failure is in
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`.
It invokes `scripts/meta_choice_descent_probe.py` as a subprocess. This
uninstalled checkout does not put the repository root on that subprocess's
import path. The same failure was reproduced in the untouched base checkout;
adding the root via `PYTHONPATH=.` fixes the affected module without modifying
code. The initial failure and incomplete retry are retained, not erased or
reported as successful full-suite runs.

Thus every native test case has a passing result across the completed run and
the corrected targeted replay, but **a single all-green native full-suite run
is not certified here**. Hosted checks have separate authority. Do not merge
on an implication that the incomplete retry passed.

## Proof and provenance scope

The universal local claims are supported by the written proofs in
`THEOREMS.md` and `CYLINDER.md`. Finite arithmetic can reject a false claim or
calibrate an implementation; it does not prove Goldbach or any universal
distribution estimate. The final claim ledger and hostile models remain part
of the deliverable.

Same-model construction, adversarial, and translation reviews caught concrete
errors and supplied separate calculation paths. These are recorded in
`AUDIT.md`; they are not external peer review, multi-model independence, or
Lean/kernel acceptance. No physical realization or speedup has been tested.

## Reproduction setup

From the repository root, either install the declared test extras in the
chosen environment or expose the current checkout to subprocesses:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python -m unittest discover \
  -s research/2026-11-12/prime_fixed_point_observer -p 'test_*.py' -v
```

Only the second, short command is the new dossier suite. The native suite is
much larger. The task publishes a draft research branch; no merge, tag, release,
main-branch modification, or solved-conjecture status is asserted.
