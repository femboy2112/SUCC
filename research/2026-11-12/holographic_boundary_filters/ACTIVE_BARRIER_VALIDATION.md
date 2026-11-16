# Active-instrument follow-up — exact validation receipt

Date: 2026-11-12. Parent SUCC PR #606 (Main XXV base `db9fb4b8`), existing test-fix parent `2206fbc085ffa2986adae83e39300316013b57dd`. No frozen historical source changed.

## Isolated local test execution

```sh
PYTHONPATH=/mnt/data/succ_coupling_round python -m unittest discover -s /mnt/data/succ_coupling_round/tests -p 'test_*.py' -q
python -m compileall -q /mnt/data/succ_coupling_round/observational_succ
```

- Python 3.13.5, Linux, stdlib only.
- **27 methods passed; 0 failures; 0 skips.**
- One initial failure: `FiniteInstrument.trace` incorrectly used the *distinct-action-subset* validator for an action *word*, rejecting repeated probes. Replaced that validation with a word validator permitting repeats. Replayed the original failures and then all 27 tests green. History intentionally retained.
- 256 binary-output two-state, two-action complete deterministic tables exhaustively enumerated. Partition-refinement classification and independently coded pair-product BFS separator agree on each table. Still same author and same underlying mathematical hypothesis, not blind corroboration.
- Additional hostile controls: no-contact equivalence, invasive read/reset, nondemolition state-label read, transitive nonorthogonality, orthogonal QND, forged pure marker, typed/unnormalized input rejection, exact CNOT disturbance, norm-preserving active rotation, source phase-alias `1/16`.

## Prior CI regression recovered and addressed

Original PR #606 head `6afccd03bf7b758f2f5f593f5ee03b56001fe5b5`: **Observational SUCC validation failed** for both Python 3.10 and 3.13 jobs. The job log showed **one ERROR** in `test_boundary_filter_tomography.BoundaryTests.test_filtered_state_recovery` (`TypeError: 'Fraction' object is not subscriptable`); the test incorrectly evaluated `[x[0] for x in readings[t]]`, although `readings[t]` is already a tuple of scalar `Fraction` readings. The run reported 13,062 tests with one error and the other entries passing. This was a test-harness indexing bug, not a proved mathematical theorem failure. On research branch, commit **`2206fbc085ffa2986adae83e39300316013b57dd`** repairs the call to `reconstruct_state_from_filters(c,bank,readings[t])`, without touching production mathematics. **New-head full CI must be checked separately**; the preceding failure must not be hidden or relabelled as green.

Full repository checkout unavailable to isolated container because external DNS to GitHub is disabled. The original source is verified through the connected GitHub repository and workflow job logs. No claim of having run all four inherited AGENTS.md gates locally.

## Validation obligations after push

1. `python scripts/verify_provenance.py`
2. `python -m unittest discover -s tests -p 'test_*.py'`
3. `python scripts/observer_foundations_probe.py`
4. `python scripts/ordinal_succ_report_probe.py`

Record statuses for the new exact SHA, including both Python 3.10 and 3.13 suites. Do not merge until mandatory gates pass.
