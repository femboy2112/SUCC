# Lag/carry round: execution and authority receipt

Base: `ea5f92bbc52468e55b597e52455f24bceedb47b3`.
Branch: `research/pi-lag-carry-rigidity-2026-10-24`.

## Executed before candidate commit

- Inherited SCE baseline: 13 tests passed, source receipt replay byte-identical,
  and both independent inherited Galois/regret oracles passed.
- Finished focused candidate: **55 tests passed in 5.326 seconds**, comprising
  the inherited 13, new 27, and 15 namespace guards.
- Strict Python compilation and `git diff --check` passed.
- New lag receipt: exact per-lag counts checked against sorted full pair counts;
  literal boundary carry and 28-carry-prefix hostile control certified.
- All three preregistered interval windows certified, including p=1048601,
  Delta=393225, canonical M=256, with zero ambiguous decisions. Full 256-cell
  counts and interval/source hashes are in `PI_LAG_INTERVAL_RECEIPT.json`.
- Independent interval oracle: 414 arctangent enclosures, 570 exact source
  enclosures, 511 accepted pair certificates, 3140 direct endpoint-pair checks;
  413 ambiguous pair certificates rejected. Its receipt replay matched bytewise.
- Main/PR heads and ancestry rechecked. All returned workflows for the pinned
  donor heads, including #265, passed at the recorded audit. This is not CI
  authority for this new candidate or a future consolidated main.

The new finite modules/tests are frozen for the required full repository
validation. That serial run uses Python 3.12.3 in the existing isolated
`/tmp/pi-source-genesis-venv`, with an explicit importable checkout and
OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1. Installed declared-range dependencies:
mpmath 1.4.1, numpy 2.5.0, scipy 1.18.0, sympy 1.12.

The provenance gate has passed. At candidate-commit preparation, the full suite
and remaining observer/ordinal probes are running; this file does not claim
their future outcome. Their final logs, exit codes, elapsed times and source
hash comparison will be retained in a separate delivery receipt and the draft
PR updated with the actual final-head CI outcome. This avoids changing the
tested source commit just to append later workflow status.

## Reproduce

```sh
PYTHONPATH=tests:. python -m unittest -v test_pi_source_collision test_pi_lag_carry test_pi_carry_prefix_control test_pi_prime_clock_conditioning test_pi_collision_intervals test_claim_namespace_collisions
python scripts/pi_lag_carry_probe.py --output /tmp/lag.json
cmp /tmp/lag.json research/2026-10-24/PI_LAG_CARRY_RECEIPT.json
python scripts/pi_lag_interval_independent_oracle.py --output /tmp/interval-oracle.json
cmp /tmp/interval-oracle.json research/2026-10-24/PI_LAG_INTERVAL_ORACLE.json
python scripts/pi_lag_interval_probe.py --large --output /tmp/windows.json
cmp /tmp/windows.json research/2026-10-24/PI_LAG_INTERVAL_RECEIPT.json
```

The new hosted focused matrix replays the lag receipt, independent oracle,
and two smaller preregistered windows. It does not rerun the large window on
every matrix job; that full certified receipt is a separately reproducible
local computation. The existing repository workflow runs all tests.

No new Lean declaration was produced. Paper proofs have full domains and
derivations; finite tests and interval certificates have their exact scopes.
Three agents supplied different mathematical/review tracks but share model
and repository provenance; they are not external referees. The independent
finite implementations and their common Python/Fraction assumptions are
identified explicitly.

One invalid-domain test in the prefix track was repaired after mathematical
review, as recorded in its proof dossier; production assumptions were not
weakened. No failed or canceled hosted workflow is counted as passed.

**Selected K_p(1)=p^{o(1)}: UNPROVED. Pi normality: OPEN. No proof of
independence in any formal theory. Conditional base coverage: 16 and 2 only.**
