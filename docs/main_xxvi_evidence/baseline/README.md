# Main XXV baseline reproducibility recovery

The interrupted session's original failure receipt was not recovered. These are
fresh runs at `db9fb4b84672050efa79b13377f1e73364598a14`, with the archived
`RESULTS_*.json` preserved. `preservation-manifest.json` records their identities.

## Observed failure

The original `main_xxv_research_gate.py` completed all eleven commands with exit
code 0, then returned FAIL because `RESULTS_analytic.json` changed. The Git diff
has **178 changed lines** (178 additions and 178 deletions), containing **1,188
changed JSON leaves**: 1,186 floating diagnostics and two roundoff argmax witness
fields. Thus the historical phrase “178 values” conflated lines with values.
No theorem decision, check count, failure count, threshold, exact rational datum
or source input changed. The largest absolute floating difference is
`5.1770098624670524e-12`, in a cancellation residual divided by a small bound.
The raw regenerated JSON is preserved in `regenerated-RESULTS_analytic.json.gz`;
the canonical archived JSON remains at its original repository path and commit.

All primary-runtime differences arise in diagnostics downstream of `numpy.vdot`:
lag correlations, the corresponding Fejér lag sum, transport residual ratios,
and the machine-roundoff argmax identity witness. This localizes the operation
whose result changes. It does **not** uniquely isolate a particular BLAS build,
compiler optimization or CPU instruction. The archived environment was Python
3.12.3; `environment.json` records the fresh Python 3.12.14 runtime and versions.
A second primary-runtime analytic replay produced exactly the same regenerated
SHA-256 (`bf76a2776b5cdb1efcae283eaf4230df4544f3b7b56a81e242d79133ef4b0a72`).
Thus this observed drift is deterministic within the replayed environment; it
is not evidence of run-to-run nondeterminism.

## Minimum justified repair

`scripts/main_xxv_research_gate.py` executes unmodified probe sources in a
separate copy with their exact relative transport dependency. It removes copied
outputs before replay, retains every fresh result outside the checkout, and
keeps all historical files unchanged.

`scripts/main_xxv_numeric_replay.py` requires exact JSON structure, types,
thresholds, statuses, counts and all unlisted fields. Only explicitly enumerated
analytic diagnostics permit absolute drift: `1e-14` for direct correlations and
related diagnostics; `1e-10` for the cancellation-residual ratio. The latter is
an output diagnostic, not the source inequality or its pass/fail threshold.
The sole allowed discrete change is the identity check's declared control/lag
argmax when both maxima are below `1e-14`, the original check has zero failures,
and both witnesses belong to the declared probe domain. Its tolerance remains
exactly `1e-12`; the maximum error and witness error must agree within each run.
The two witnesses have no privileged mathematical identity at roundoff scale.

Five regression-test families reject changes to thresholds, counts, statuses,
JSON types, keys, lengths, unlisted floats, nonfinite values, large diagnostic
drift and invalid witness metadata. Replaying a machine diagnostic within this
policy does not certify a universal mathematical estimate.

## Differential runtime control

A separate Python 3.13.5 / NumPy 2.2.4 / SciPy 1.15.3 run also completed the
analytic probe with exit 0 and unchanged theorem decisions. It changes 18,532
JSON leaves, including other diagnostic argmax locations. The narrow repair
**rejects** those unreviewed paths. The complete comparison is retained as
`system-python313-comparison.json.gz`, with its summary and command log. This
is a fail-closed calibration and an explicit portability boundary, not a claim
that the full numerical replay is certified for every supported interpreter.

The corrected baseline and exact integration-candidate replay receipts record
what was actually rerun. Earlier PR CI or this baseline run does not validate a
new combined tree. The baseline Main XXIV manifest checker fails against the
later Main XXV tree because some protected historical files intentionally
evolved; its raw exit code is retained in `cheap-gates-receipt.json` rather than
reported as a new implementation failure.
