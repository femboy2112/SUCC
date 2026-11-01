# Executed validation and environment repair

**Final local receipt snapshot: 2026-10-31 23:58 UTC. The compliant full regression
passed 10,164 tests; final changed inputs passed a separate 43-test replay.**
Mathematical proofs in this dossier have paper authority;
the finite tests do not confer Lean/kernel authority or prove pi normality.

The verified starting commit is
`030ee84b8b7f655fcf433375bfc0b347e0483c89`, on the isolated child branch
`research/selected-pi-lag-fireworks-2026-10-31`. Initial tests ran before the
new research files were written. The compliant run includes those additions;
its exact Python file hashes, starting head and worktree status are recorded in
`receipts/compliant/python_snapshot.json.gz`. A later commit can be compared
to those bytes rather than misrepresenting the run as having started on it.

## Results actually obtained

| Check | Result | Runtime |
|---|---|---:|
| Parent PR #434 lag suite | 28 tests passed | 2.877 s test time |
| Imported PR #432 edge suite | 21 tests passed | 0.074 s test time |
| Imported PR #433 seed suite | 28 tests passed | 0.212 s test time |
| Imported PR #431 carrier suite | 20 tests passed | 0.060 s test time |
| Parent N=512,K=4,h=1 exact receipt | All four recorded rational fields match | 5.456 s command time |
| Parent N=1024,K=4,h=1 exact receipt | All four recorded rational fields match | 11.022 s command time |
| Parent N=1536,K=4,h=1 exact receipt | All four recorded rational fields match | 16.879 s command time |
| Initial new dossier suites in declared-extras environment | 42 tests passed | 2.668 s test time |
| Final new dossier suites on bytes matching executable commit `5e429965` | **43 tests passed** | 2.651 s test time |
| `verify_provenance.py` | Passed: 72 items, 17 archives, 55 namespace migrations | See manifest |
| `observer_foundations_probe.py` | Passed, exit 0 | See manifest |
| `ordinal_succ_report_probe.py` | Passed, exit 0 | See manifest |
| Isolated environment `pip check` | No broken requirements | 1.986 s command time |
| Original default-interpreter full suite | **Interrupted after confirmed environment error; not a pass** | 650.605 s |
| Declared-extras full suite on recorded input snapshot | **10,164 tests passed**, exit 0 | 1155.496 s test time; 1174.274 s command time |

The final 43 new tests comprise 13 arithmetic, 3 audit, 12 boundary, 5 sharpness,
and 10 transport tests. The initial 42-test run preceded the added independent
tail-derivative check. These suites include exact source/oracle comparisons,
independent cyclotomic polynomial reduction, original-source coherent tail
intervals, dyadic and prime-conductor shadows, whole-window Gram comparisons,
and hostile label/signed-bound interpretations. They establish these finite
checks, not the open all-horizon selected inequality.

The three parent receipt comparisons are stored as exact strings in
`receipts/baseline/receipt_comparison.json`; no displayed decimal is used to
certify a sign. All 15 blob identities in the parent's integration table match
in `receipts/baseline/source_blob_audit.json`.

The final independent recheck also verifies all **46** inherited files listed
in `SOURCE_MANIFEST.json`, against both SHA256 and Git blob identity. The full
regression log's SHA256 is
`fee03fb6761691b5d3a8541916b02a559b8cd69ad6d6e4c6f8fc70e3c96902dc`.
The exact raw bytes are retained as deterministic gzip in
`receipts/compliant/full_regression.log.gz`; the archive metadata records both
the compressed and uncompressed hashes. Decompress it to obtain the raw
`full_regression.log` named by the command manifest.

## Ordinary environment failure and isolated repair

The initial interpreter was Python 3.12.3, `/home/leah/.local/bin/python`.
Its actual imported `mpmath` was version **1.2.1** from the system directory
(distribution metadata reported 0.0.0), below the declared `>=1.3,<2` test
extra. A separate missing editable-package installation made the real
`scripts/meta_choice_descent_probe.py` entrypoint fail with
`ModuleNotFoundError: No module named 'observational_succ'`. Its root test
spawned that command using `sys.executable`; direct execution reproduced the
same failure. Both the traceback and the corrected smoke output are retained.

The obsolete full run was stopped by SIGINT after verifying its exact owned
PID and command, once the failure and remedy had been established. Its raw
partial log, exit code -2, and explicit
`TERMINATED_AFTER_CONFIRMED_ENVIRONMENT_FAILURE` record are preserved. It is
neither silently discarded nor counted as passing regression.

Repair commands, executed without changing global packages:

```sh
python -m venv --system-site-packages /tmp/succ-fireworks-venv
/tmp/succ-fireworks-venv/bin/python -m pip install -e '.[test]'
/tmp/succ-fireworks-venv/bin/python -m pip check
/tmp/succ-fireworks-venv/bin/python scripts/meta_choice_descent_probe.py
```

The isolated environment imports mpmath **1.4.1**, numpy **2.5.0**, scipy
**1.18.0**, and sympy **1.12**. All satisfy the declared ranges. Pip check and
the previously failing command both pass. The complete regression was then
restarted serially under that interpreter with OMP, OpenBLAS and MKL thread
counts set to one. No unrelated process was stopped.

## Final executable input coverage

The broad run began at 23:38:44 UTC with the input snapshot already described.
Three new Python inputs subsequently changed: `interval_oracle.py`,
`test_signed_lag_fireworks_transport.py`, and
`test_signed_lag_fireworks_sharpness.py`. The change encloses exact phases in
outward dyadic cells before costly rational cubing, adds huge-denominator
boundary controls, and adds the independent differentiated-pole source check.
The broad run therefore is **not** represented as a run that loaded the final
version of those three files.

The final 43-test suite was actually rerun on the final executable bytes later
committed as `5e429965bac8af16bd10c3f8e917fdcdc99be354`; all passed. Its preserved log hash is
`61b7f96ee4ed47737ee058b6e5628068912de0c72bee7c741d182a439a7fddb9`.
`receipts/compliant/final_focused_delta.json` lists the three changed inputs,
confirms no missing snapshot inputs, and records the final new Python hashes.
Those hashes were rechecked while saving this receipt. The broad regression
and focused replay are complementary checks; their test counts are not added
as if they were disjoint tests.

The first independent interval sweep was interrupted before emitting a receipt
after a rational-gcd performance bottleneck was identified. Its explicit
interruption record is preserved in `receipts/probe/interrupted_sweep.json`.
The repaired complete 23-case exact sweep, source hashes, and mixed signed
outcomes are in `finite_receipt.json` and `RESULTS.md`. The interrupted attempt
is not a successful measurement.

## Hosted status is separate

`BASELINE_CI_SNAPSHOT.json` records all four workflows succeeding on the starting
integration head `030ee84b`. This is parent-head evidence. `CI_SNAPSHOT.json`
records the separate query for child executable head `5e429965`: three workflows
had passed and broad validation was still running at that snapshot. Neither
the parent successes nor the local results are substituted for the child's
remaining exact-head hosted result. Later documentation/receipt commits must
likewise retain their own CI status rather than inherit a claim of success.

## Reproduction

Use an environment installed with `python -m pip install -e '.[test]'`, then:

```sh
python -m unittest discover -s tests -p 'test_signed_lag_fireworks*.py' -v
python -m unittest discover -s tests -p 'test_selected_lag_tomography.py' -v
python -m unittest discover -s tests -p 'test_edge_seed_tomography.py' -v
python -m unittest discover -s tests -p 'test_seed_superposition.py' -v
python -m unittest discover -s tests -p 'test_carrier_path_measure.py' -v
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py' -v
python research/2026-10-31/selected_lag_tomography/run_receipt.py 512 4
python research/2026-10-31/selected_lag_tomography/run_receipt.py 1024 4
python research/2026-10-31/selected_lag_tomography/run_receipt.py 1536 4
```

`receipts/SHA256.json` hashes the preserved raw artifacts. The command manifests
record exact argument arrays, working directory, UTC start, runtime, exit code,
and raw-log hash. Source integrity, finite exact certificates, complete local
regression, hosted exact-head CI, paper proofs, and kernel proofs remain distinct
claims. Hosted child-head CI is recorded separately; no hosted success is
inferred from these local results.
