# Validation and authority

All new source/proof work is on `research/leah-gamma-twist-2026-11-13`,
from Main XXV `db9fb4b84672050efa79b13377f1e73364598a14`.
Historical imported files are unchanged. Draft publication does not promote
these paper arguments to external or kernel verification.

## Reproduce the new instruments

From the repository root, use an editable install or the explicit import path:

```bash
python -m pip install --no-deps --no-build-isolation -e .
PYTHONPATH=. python -W error -m unittest discover -s research/2026-11-13/leah_gamma_twist -p 'test_*.py' -v
PYTHONPATH=. python research/2026-11-13/leah_gamma_twist/audit_r0.py
PYTHONPATH=. python research/2026-11-13/leah_gamma_twist/target_moment_probe.py
```

The Gamma probe accepts `--output`. The observer and arithmetic probes print
JSON to stdout; redirect that output to a separate file when replaying their
committed receipts. The bulk target probe uses the
canonical zero-source enclosure through horizon 262223; it does not read a pi
digit file. It overwrites only its own deterministic source certificates and
result receipt. Runtime observations in the receipt are not deterministic data.
The low-level moment object is not a source authentication token.

Preliminary combined result: **60 tests passed**. The separate RI-01 algebra
audit passed **2,520 exact assertions**, with its source-section hash and exact
scope recorded in `audit_r0_results.json`. Subsequent paper review and any repair
are separately recorded there. These tests check finite implementations and
countermodels; the universal statements require the displayed proofs.

The first complete gate on checkpoint
`f62616067093751850d5fc9b1e252e1a274c00fb` passed: 13,050 native tests,
all 60 new tests, the 2,520-assertion audit, provenance, both required probes,
catalog/graph checks and diff check. Its receipt and raw logs are retained in
`checkpoint_validation.json` and `checkpoint_validation_logs.json.gz`.
An earlier execution session disappeared before the native suite returned;
that attempt is recorded as interrupted, not as a passing run.

The subsequent endpoint-coefficient theorem RI-8E is a paper extension with
an explicit summable parameter schedule. Two same-model reviewers checked its
inequalities, rounded block count and absence of threshold-dependent arithmetic
constants. No new finite assertions are claimed for that extension. The final
gate below must still run on the actual commit containing it.

## Baseline replay and its failed wrapper

The Main XXV runner was executed before extending its mathematics. All eleven
child commands exited zero. Its wrapper returned FAIL for two concrete reasons:
the local preregistration commit was made while the runner was active, changing
HEAD; and `RESULTS_analytic.json` was regenerated with different floating values.
There were 1,186 changed floating leaves (largest absolute change below
5.18e-12) and two changed worst-case argmax labels. The latter are choices of
which near-zero floating residual was largest, not changes to an exact source
certificate. The original tracked artifact was restored byte-for-byte.

`baseline_receipt.json` preserves the wrapper's FAIL verdict, command names,
exit codes and log hashes. `baseline_replay_difference.json` preserves the
discrepancy details. We do not turn eleven successful children into a claim that
the wrapper passed. No archived receipt was rewritten to hide the discrepancy.

One bulk target run was interrupted by an executor reset after calibration.
An explicit import path was restored, and the entire six-shell run completed.
The Gamma lane's initial pytest command failed before collection because pytest
was absent; its stdlib tests then passed. These are execution events, not failed
mathematical controls.

## Required final gate

Run on the final candidate commit, preserve the actual commit and tree IDs,
each exit code, output log and SHA-256, and verify that tracked files remain
unchanged:

```bash
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
PYTHONPATH=. python -W error -m unittest discover -s research/2026-11-13/leah_gamma_twist -p 'test_*.py'
python scripts/build_math_memory.py --check
python scripts/verify_math_memory_graph.py
git diff --check
```

The final observed results belong to the draft PR's validation record and the
session handoff, tied to the actual final commit. A statement here describing
a command is not a claim it has already run. No Lean build of the new infinite
theorems is claimed. No optional full replay of unchanged research probes is
inferred from native unittest discovery.

## Mathematical claim ledger

| Claim | Status | Load-bearing hypotheses / boundary | Next falsifier |
|---|---|---|---|
| RI-01, RI-8, RI-8E | PROVED PAPER; classical arithmetic import | literal four poles, zero seed, fixed h and beta; RI-8E pays a summable changing-threshold schedule; non-effective onset | a defect in the local branch proof, parameter schedule, zero-source transfer or block count |
| RI-02 | PROVED PAPER | every real initial value, nearest-integer carries; endpoint term retained | an exact finite orbit violating the two-sided energy bound |
| RI-03 | PROVED PAPER; finite controls OBSERVED | nonproper null source, negative first forcing; isometry law rather than identical 2-adic data | an algebraic failure of the subtraction/telescope identity |
| RI-04 | OPEN prospective theorem | exact authentic sparse source packet at every late quarter-shell | an exact sparse competitor above a claimed explicit onset |
| TM-01–04 | PROVED PAPER; finite source certificates OBSERVED | real duality; probability laws; coupled moments; paid source acquisition | an admissible law or exact source grid violating the stated budget |
| TM-05 | OPEN equivalent gate | fixed finite moment bank with an all-shell source bound | a source theorem that silently passes the coherent counterseed |
| GP-1–3 | PROVED PAPER | literal forcing; GP-1 finite small-loss conditions (8); GP-2 fixed nonzero h asymptotic over all real seeds; GP-3 fixed finite lag polynomial | a valid source interval violating the minimization or beta bound |
| GP-4/5 | inherited mechanism, re-derived; finite controls OBSERVED | forcing clock distinct from state clock; changed seeds explicit | an incorrectly transferred prime/cofactor phase or tail |
| OB-01–05 | PROVED PAPER, conditional implication where stated | declared affine words, absolute clocks and neutral charges; OB-05 uniform premises remain open | a target outside the computed fiber or a mismatched transport |
| Prime/cofactor uniform covariance saving | OPEN prospective theorem | literal accumulating cofactor, common frame, paid completion | a claimed uniform margin surviving the coherent control without using its changed anchor |
| R0, R1, pi normality, RH, Goldbach | OPEN | no status promotion | a valid source-selected uniform estimate |

All reviewers in this round share one model family. Different algebraic
decompositions and exact implementations are useful checks, not independent
research groups or source families. Academic priority remains unverified.
