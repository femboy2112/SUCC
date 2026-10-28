# Selected-branch research validation receipt

Date: 2026-10-26. Branch: `research/selected-branch-cross-energy-2026-10-26`.
Parent: #312 `0c306a889f425418c29cbea3193205fb80c0575e`.
Reviewed sibling: #311 `a34c4484059e667202b97d5ab4102560987b1406`.
No sibling merge, main change, archive rewrite, or historical authority
promotion. [Mathematical synthesis](SELECTED_BRANCH_SYNTHESIS.md).

## Environment and commands

Python 3.12 in a local `.venv` with repository test dependencies installed.
The environment is ignored, not a deliverable. Commands below used
`.venv/bin/python`. Source and test files were frozen during the full suite;
the wrapper hashes all 1,279 Python files in `observational_succ` and
`tests` before and after. Documentation edits do not change that snapshot.

| Check | Result | Durable evidence |
|---|---|---|
| Parent lambda + arithmetic + operator + transport tests | 59 passed, 5.565 s | [focused log](selected_branch_validation/focused.log) |
| Analytic controls and exact interval witnesses | 17 passed, 1.871 s | [analytic log](selected_branch_validation/focused_analytic.log) |
| Claim namespace checks after final documentation | 18 passed, 0.177 s | [corrected namespace log](selected_branch_validation/namespace_corrected.log) |
| `python scripts/verify_provenance.py` | PASS, 72 entries; 17 byte-identical archives and 55 namespace migrations | [source report](selected_branch_validation/provenance.json) |
| `python -m unittest discover -s tests -p 'test_*.py'` | PASS, 8,886 tests in 1,076.206 s | [full raw log](selected_branch_validation/full_unittest.log) |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | [observer report](selected_branch_validation/observer.json) |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | [ordinal report](selected_branch_validation/ordinal.json) |
| Exact source/interval receipt write and replay | Written and byte-for-byte verified | [receipt](selected_branch_validation/exact_receipt.json), [replay log](selected_branch_validation/exact_replay.log) |
| Pinned finite Lean check | 10 declarations, 4 paired controls; KERNEL_CHECKED | [kernel receipt](selected_branch_validation/lean/kernel-observation.json) |

There are **52 new tests** across the four `test_selected_branch_*` modules.
The 59-test group includes 24 inherited lambda tests. An initial namespace
command referred to a nonexistent module and failed to import; its
[raw failure](selected_branch_validation/namespace.log) is retained. The
corrected command used `tests.test_claim_namespace_collisions` and
`tests.test_academic_vii_namespaces`. This was a harness-name error, not a
mathematical or product test failure.

## Exact proof instruments and mutations

`scripts/selected_branch_probe.py --write` followed by `--verify` regenerates
source cases at $N=16,64,128,257$, odd-resolution saturation at held-out
horizons, same-forcing changed-selector controls, huge integer schedule
budgets, and authentic all-step quadratic spills at $N=1,3,17,65$.
No floating spectrum is used as proof authority. The finite signed
certificates are outward rational bounds using the existing Machin/Taylor
engine, and energies use the actual $\mathbb Q(\zeta_{16})$ carrier.
Formal group-algebra and evaluated cyclotomic equality remain distinct.

Intentional receipt mutations change the normality flag, a source hash,
and an authentic critical-scale count. They must be rejected by recomputation;
see [mutation results](selected_branch_validation/receipt_mutation_results.json).
Native tests additionally reject changed source seeds/lifts, an even-conductor
forcing mutation, wrong source bin transport, and invalid odd inverses.
Independent enumeration, fresh rational table replacements, interval
endpoints, and periodic/sparse control horizons are used rather than solely
repeating the production formula.

The $N=257,M=16,h=1$ signed certificate has normalized modulus upper bound
at most $10403144679/250000000000$ (about 0.041613). This is one **EXACT
FINITE** bound. It establishes no asymptotic rate or new logarithmic-loss
order. Receipt flags explicitly keep both selected cancellation and
π normality false.

## Lean scope and reproducibility

The actual toolchain was Lean 4.14.0, compiler commit `410fab728470`, with
mathlib `4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84` and all manifest
dependencies checked. The compatible existing cache
`/home/leah/SUCC-rf/formal/mathlib_bridge` was used read-only. Invocations
were serial, `-j 1 -M 2048`, with the exact commands in the receipt.
Generated build directories are ignored; exported statements and raw logs
are committed. Only `propext`, `Classical.choice` and `Quot.sound` occur.

The kernel covers finite odd-unit/inverse facts, affine injectivity,
permutation squared-norm invariance, deterministic and mixed-row defect,
an even-conductor control, a parity perspective inequality, and positivity
of the critical-scale polynomial. Paired false assertions are rejected.
It does **not** certify the whole BBP denominator induction, full complex
operator statement, spill asymptotics, conditional-energy transport theorem,
Diophantine input, infinite controls, or normality.

The kernel receipt's commit-at-start/end is the parent because sources
were checked before their first commit. Its explicit source hashes and
type exports identify the newly checked files; it is not a claim that the
parent commit already contains them. Historical authority catalogues were
not changed.

## Remote validation boundary

The [initial remote receipt](selected_branch_validation/remote_baseline.json)
records #306–#312 and ancestry. The [final parent/sibling snapshot](selected_branch_validation/parent_ci_final.json)
records #312's successful native **push** validation and three successful
scoped PR workflows. Its duplicate native PR run was cancelled. #311's
five scoped workflows succeeded, while both native runs were cancelled;
those cancelled runs are not passing native validation. This continuation
did not cancel or modify parent/sibling runs.

Hosted validation of the delivered continuation must be reported against
its own exact commit. Parent success is not continuation CI success. The
draft PR and final response record the delivery commit and current hosted
status without a second documentation-only push to retrigger the suite.

## Final local results

The full suite completed successfully on 2026-10-26 at approximately
23:47 UTC. Its wrapper took 1,084.130 s including setup and source hashing;
unittest reported 1,076.206 s. All 1,279 source/test hashes were unchanged.
See the [exit-code and hash receipt](selected_branch_validation/full_unittest_result.json)
and [source snapshot](selected_branch_validation/python_source_snapshot.json).
The three native probes have individual exit codes, timings and log hashes
in [native results](selected_branch_validation/native_probe_results.json).
All three corrupted receipts were rejected for the intended reason.

The final same-team hostile read of the synthesis, claim ledger and Frontier
addition found no material quantifier or authority mismatch. GitHub's Markdown
API recognized the mathematical delimiters and preserved the four-column
claim table; source/link and rendered-HTML audit hashes are recorded in
[local audit](selected_branch_validation/markdown_local_audit.json) and
[GitHub render audit](selected_branch_validation/github_markdown_render.json).
This is a source/HTML audit, not a browser screenshot or external proof review.
