# Validation and proof authority

The manuscripts supply complete paper proofs; finite computations validate
their implementation and stated constants. No finite experiment promotes R0
or normality. Same-model reviewers are not external independent referees.

## Reproduction

Run from the repository root:

```sh
python -m unittest tests.test_joint_time_lag -v
PYTHONPATH=. python research/2026-11-13/joint_time_lag_response/probe.py
PYTHONPATH=. python research/2026-11-13/joint_time_lag_response/source_audit.py
PYTHONPATH=. python research/2026-11-13/joint_time_lag_response/tensor_audit.py
```

The focused native suite passed 13 tests before commit. The root repeated that
suite independently of its implementation agent. The finite source receipt
contains 54 preregistered B,H,h certificates, 60 inverse controls, and 777
four-fraction source comparisons. Exact outward rational endpoints are the
authority; decimal summaries are only readable approximations.

The source audit passed 5,050 endpoint-budget cases, 24 rigorous tail interval
cases, and the exact derivative polynomial identity. The tensor audit passed
1,164 window comparisons and 414 weighted Cauchy comparisons; its non-positive-
definite mutation was rejected. The tensor audit does not import the new native
module, so it checks a different implementation of the finite identities.

The first source-mutation test mistakenly expected flipping -2/4 at n=1 to
change the circle phase. It adds an integer, so that observation is blind.
The corrected suite retains this exact alias and separately rejects a mutation
of -1/5. The initial failed calibration and repair are recorded in RESULTS.json.
This is an observer limitation, not a failure of the source identity.

## Mandatory gates on the final commit

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

The final commit, commands, observed outcomes and any incomplete invocation
are recorded in the draft PR after execution. An interrupted or timed-out
command is never reported as passed. If exhaustive whole-module shards are
used, their inventory and distinct execution scope are disclosed explicitly.

The parent PR #608 exposed a pre-existing order-sensitive mpmath test:
`test_triangle_genesis_repair.CrossCheckIndependentOracle.test_p1_oracle_agrees`.
Another native test leaves global precision at 40 digits, while this test
requires 45-digit agreement. The parent reproduced failure at 40 and success
at 60 digits; this round leaves those archived files unchanged. Any recurrence
of that failure will be reported, not silently repaired or excluded.
