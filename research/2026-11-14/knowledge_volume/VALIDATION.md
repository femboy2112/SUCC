# Validation and reproducibility

## Scope and authority

The proofs in HORIZON_THEOREMS.md and TOOLKIT_THEOREMS.md carry the universal
mathematical statements. The following integer/Fraction computations check
finite models, calibrate certificate verifiers, and compare different algorithms.
They are not empirical source authentication, a formal-kernel proof, or a
finite-to-infinite inference.

Base source: `3ce3ce42b3e40b41bea019e9c154891bcafb77b1`.
All new production modules use the Python standard library. No dependency,
workflow, archived source, existing implementation or main default changes.

## Focused production and source-frontier checks — PASS

```sh
python -m unittest tests.test_predictive_horizons tests.test_nonlinear_foresight tests.test_recursive_observer tests.test_seed_source_rank -v
```

**71 tests passed:** 27 new tests, 31 existing recursive-observer tests, and
13 existing seed/source tests. Raw output: [receipts/focused.log](receipts/focused.log).

The new tests cover delayed and alternating predictable horizons, positive
and negative source-bound certificates, malformed/forged claims, composition,
full-power profile closure, Apéry membership and finite realizations, singular
source images, polynomial-stage obstructions, repeated-squaring operation
counts, independent sequential trajectories, fixed-horizon precision bounds,
and explicit output-bit growth. The programmable-word control checks all
2,047 words of lengths 0 through 10, plus 11 indecomposable examples.

## Differential audit of production certificates — PASS

```sh
python research/2026-11-14/knowledge_volume/differential_audit.py
```

The expected answers use direct repeated source walks and every same-report
pair, not production binary exponentiation or decoder construction. Monoid
membership is independently encoded by bounded coin dynamic programming.

| Exact bounded audit | Count / domain |
|---|---:|
| All transition tables and report partitions, state sizes 1–4 | 3,984 sources |
| Horizon membership versus direct pairwise walks | 99,600 checks, n=0…24 |
| Composition of positive decoders | 60,342 compositions |
| Generator sets, subsets of {1,…,9} of size at most 4 | 256 sets |
| Membership and finite realizations per generator set | n=0…300 |
| Malformed horizon certificates rejected | 23 |
| Malformed full profiles rejected | 17 |

Zero failures and zero unexpected exceptions. Every permutation among the
enumerated sources also satisfies the claimed dN_0 classification. The
receipt includes exact SHA-256 hashes of the audited production module,
focused horizon tests, horizon proof and audit script:
[receipts/differential.json](receipts/differential.json).

## Independent mathematical oracle — PASS

```sh
python research/2026-11-14/knowledge_volume/independent_oracle.py
```

This script imports no production SUCC implementation and uses no random
sampling or floating point. Its raw result is
[receipts/independent.json](receipts/independent.json).

| Exact bounded audit | Count / domain |
|---|---:|
| Additivity, every four-state transition and binary-report table | 4,096 models, n≤24 |
| Finite permutation source, every ternary-report table | 1,944 models, n≤24 |
| Finite realization, generator subsets of {1,…,8} of size≤3 | 93 sets, horizons at least 120, up to 98 states |
| Nonlinear jump versus sequential walk | 931 equalities, n≤18 |
| Descriptor transition identity | 49 equalities |
| Exact discontinuity family | 112 identities |
| Bounded-source error inequality | 53,508 comparisons, n≤12 |

The two deliberately false scope extensions are rejected. The triple
(0,0,1) satisfies the polynomial shadow and fails the actual source image.
The larger finite tests are calibrated mathematical models, not independent
empirical observations of a carrier. Same-model assistant audits are recorded
as proof/code review, not independent truth witnesses.

## Required repository probes — PASS

The actual required commands were run:

```sh
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
```

Receipts:
[provenance.json](receipts/provenance.json),
[foundations.json](receipts/foundations.json),
[ordinal.json](receipts/ordinal.json).
Provenance verified 72 manifest items, including 17 byte-identical research
archives and 55 declared mechanical namespace migrations. The foundation
and ordinal probes retain their explicit no-RH/no-executed-infinity claims.

## Broad repository discovery — completed; two environment errors repaired

The required `python -m unittest discover -s tests -p 'test_*.py'` was
started from the parent checkout before the new modules were written.
It completed **13,206 tests, with two errors**. Raw result:
[full_discovery_initial.log](receipts/full_discovery_initial.log).
The two errors were:

1. `test_exact_probe_receipt_and_independent_count` in
   `test_eodcs_meta_choice_descent`: its child script could not import
   `observational_succ` because the checkout was not installed and the
   child process did not have the repository root on its import path.
2. `test_real_graph_retains_history_and_checks_new_sources` in
   `test_round2_registry`: the depth-one clone lacked pinned historical
   Git commit objects required by the provenance audit.

Both errors were reproduced in a separate, untouched parent worktree at
the exact base SHA: [parent_initial_errors.log](receipts/parent_initial_errors.log).
No repository code was changed to repair them. The exact three pinned
historical commits were fetched, and the two affected suites were run with
the project root supplied as `PYTHONPATH=.`:

```sh
git fetch --depth 1 origin 610efacf02556e1c5922bc5d4e87d0087f19b446 e42096ec0186228dd0f748767599e470f2ca2e1d f309d9104ba480c1999c962af1df7c50f19e1bfe
PYTHONPATH=. python -m unittest tests.test_eodcs_meta_choice_descent tests.test_round2_registry -v
```

**17/17 passed on the untouched parent and 17/17 passed on this research
branch** after setup repair. See
[setup_repaired_parent.log](receipts/setup_repaired_parent.log),
[setup_repaired_branch.log](receipts/setup_repaired_branch.log), and
[environment.json](receipts/environment.json).

The entire 13,206-test sweep was not repeated after those targeted repairs.
Accordingly this is not reported as one clean green full-suite run or as
remote CI success. Every error from the completed broad run was reproduced,
diagnosed and cleared by the corresponding rerun; the 27 new tests and
44 relevant existing tests passed separately. Python was 3.12.14 with
assertion optimization disabled; exact runtime metadata is in the receipt.

## Artifact integrity

Focused `compileall` was run on the two production modules, their tests and
both audit scripts. All local Markdown proof targets and the 17-record
claim-ledger schema are checked. `FILE_HASHES.json` binds every payload
file in this package plus the new production modules and tests, excluding
the hash manifest itself to avoid a circular hash.

The branch tree is checked against its parent for additions only. GitHub
tree/blob hashes are compared with the locally validated bytes at publication.
Those are integrity receipts, not substitutes for the mathematical proofs.

No new Lean theorem, physical instrument authentication, external peer
review, π normality, R0 or RH proof is claimed.
