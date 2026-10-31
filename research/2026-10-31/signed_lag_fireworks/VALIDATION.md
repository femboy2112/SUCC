# Executed validation and environment repair

**Initial receipt snapshot: 2026-10-31 23:38 UTC. Full compliant regression is
RUNNING, not passed.** Mathematical proofs in this dossier have paper authority;
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
| New dossier suites in declared-extras environment | **42 tests passed** | 2.668 s test time |
| `verify_provenance.py` | Passed: 72 items, 17 archives, 55 namespace migrations | See manifest |
| `observer_foundations_probe.py` | Passed, exit 0 | See manifest |
| `ordinal_succ_report_probe.py` | Passed, exit 0 | See manifest |
| Isolated environment `pip check` | No broken requirements | 1.986 s command time |
| Original default-interpreter full suite | **Interrupted after confirmed environment error; not a pass** | 650.605 s |
| Declared-extras full suite | **RUNNING**, started 23:38:44 UTC | Pending |

The 42 new tests comprise 13 arithmetic, 3 audit, 12 boundary, 4 sharpness,
and 10 transport tests. They include exact source/oracle comparisons,
independent cyclotomic polynomial reduction, original-source coherent tail
intervals, dyadic and prime-conductor shadows, whole-window Gram comparisons,
and hostile label/signed-bound interpretations. They establish these finite
checks, not the open all-horizon selected inequality.

The three parent receipt comparisons are stored as exact strings in
`receipts/baseline/receipt_comparison.json`; no displayed decimal is used to
certify a sign. All 15 blob identities in the parent's integration table match
in `receipts/baseline/source_blob_audit.json`.

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
claims. Hosted child-head CI is recorded separately after the draft is pushed;
no hosted success is inferred from these local results.
