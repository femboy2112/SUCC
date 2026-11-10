# Executed validation and exact scope

Pi base-16 normality: OPEN. RH: OPEN. All results below concern the isolated
research worktree on its pinned d32342d proof baseline, not the newer main
integration's test tree. Frozen/native paths are byte-unchanged relative to
that baseline. No dependency was installed or global package state changed.

## Final focused replay

Executed with the existing Python3.12 virtualenv and one BLAS/OpenMP thread:

```
python research/2026-11-08/signal_frontier/validate.py --output /tmp/succ-signal-final-replay
```

**54 unique focused tests PASS;26 commands exit0;13 payload comparisons match.**
Raw command lines, exit codes, timing, code hashes and log hashes are in
`validation/focused_final/replay.json`. Logs are alongside it. Earlier focused
replay and the scoped final triangle refinement replay are retained separately;
they are not counted as extra unique tests.

The final replay runs every focused test group, all principal exact/numerical
oracles, both independent referee algorithms, the independent source readout,
Lean coefficient transport, and the three cheap mandatory repository gates.
Referee mathematical payloads are compared separately from their immutable
historical paper-review hashes; later root review is explicitly scoped below.
No paper result is promoted because a finite test passes.

The expensive root source sweep and Fibonacci source sweep were executed
before this final replay; they were not redundantly rerun by its default.
Use `--source` to regenerate all source payloads and compare them to the
retained originals. It reruns the five root epochs including10009 and the
Fibonacci source cases. Their original executed commands are:

```
python research/2026-11-08/signal_frontier/source_probe.py --stage development --output research/2026-11-08/signal_frontier/results
python research/2026-11-08/signal_frontier/source_probe.py --stage holdout --output research/2026-11-08/signal_frontier/results
python research/2026-11-08/signal_frontier/fibonacci_covariance/observer.py --output research/2026-11-08/signal_frontier/fibonacci_covariance/results --source
```

The root protocol was committed as d08c0f17 before execution. Agent protocols
were written before their measurements but not separately Git timestamped.
Later analytic improvements were tested on declared cases and are not called
new independent holdouts. A10009 begins after the previous source endpoint9837;
smaller epochs overlap previous data. The Fibonacci protocol is a new observer
holdout on shared source windows.

## Mandatory native suite: one environment error, isolated repair passes

The full required command was actually executed:

```
python -m unittest discover -s tests -p 'test_*.py'
```

It ran **12,147 tests in1277.215seconds:12,146 passed, one ERROR**, exit1.
The failing test is
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`.
Its subprocess `python scripts/meta_choice_descent_probe.py` lacks the repository
on its import path and raises `ModuleNotFoundError: observational_succ`.

The unchanged script, test and module were verified against d32342d. Direct
failure, isolated11-test failure, and corrected11-test PASS were reproduced
in `validation/IMPORT_PATH_AUDIT.json` and its logs. Setting process-local
`PYTHONPATH` to the repository fixes that invocation without editing the
frozen script. The validation runner now supplies that environment.

**The whole native suite was not rerun after this environment repair.** We do
not relabel the exit1 run as a full pass. `validate.py --native` reproduces the
full suite with the corrected invocation if requested. The older12,147-pass
receipt remains historical, not a substitute for this round's actual result.
The full initial driver stopped after the native error; its planned later
commands are not claimed to have run there. They were independently executed
and passed in the final focused replay.

All three other required gates PASS:
`verify_provenance.py`, `observer_foundations_probe.py`,
`ordinal_succ_report_probe.py`. `git diff --check` PASS.

## Formal scope

Lean4.14 checked `formal/FibonacciClock.lean`: three integer-coefficient
transport theorems. The reported axioms are propext, propext, and none.
This does not formalize the golden real root, the circle geometry, source
calibration inequalities, classical prime imports, or pi normality.

## Finite evidence and independent checks

- Root:90 outward source/observer configurations,15 modular source checks,
  independent event-sweep comparisons and a separate100-digit direct
  repartition readout of four source configurations.
- Fixed depth:111 exact cases,23,224 equalities; separate84 root-sweep checks.
- Source jets:593 source comparisons,56 signed enclosures,280 lag bounds,
  three coefficient mutants and seven triangular lag identities.
- Arithmetic:3,188 principal-part checks, six independent source sums,
 118 lifting histograms, exact quotient/alias/selector checks, and118 numerical
 Weil corroborations including18 bounds strictly below1. Ford/Weil/PNT are
 classical paper imports; numerical cases do not prove them.
- Fibonacci geometry:1,396 exact checks, seven100-digit golden cases.
- Fibonacci acquisition:57 exact clock checks,1,206 exact labels,32 outward
 frame energy certificates,72 source/control configurations and six modular
 source checks. Matching source Weyl rectangles use shared engines and are
 labelled consistency checks.
- Triangle posterior:2,650 exact checks, five golden reconstructions,
 24 source-clock observations and four independent source quadratures.
- Triangle geometry:8,184 exact arc and8,184 integer-clock checks,165 source
 grade comparisons,1,533 posterior refinements,132 Farey checks,12 nonvacuous
 exact TV bounds,12 numerical chord/area cases.
- Independent frontier referee:86,016 adversarial noise cases,24 numerical
 frame cases and nine discrepancy cases, with an insufficient-rank control.
- Independent triangle referee:18 exact reconstruction ranks,18 positive
 aliases,91 barycentric inversions,148 source cross-checks,182 posterior
 refinements,18 exact TV bounds and source/clock/carry controls.

These counts describe different check types and are not summed into a
confidence score. Separate agents share a model family and repository;
independent algorithms are not external scholarly refereeing.

## Preserved execution history

A standalone arithmetic oracle initially lacked its repository import path;
a Fibonacci test rejected a floating-point value accidentally introduced
into a Fraction fixture; a large Q(alpha) diagnostic needed guarded local
precision. Each was repaired with the original mathematical claim retained,
and relevant checks rerun. Exact triangle certificates were unaffected by
the diagnostic display issue. The native import error above remains recorded
with its actual failed full-suite status and successful isolated repair.

Final source/proof hashes are in `PROVENANCE.json`, `ROOT_REVIEW.json` and
`ARTIFACT_MANIFEST.json`. Hosted CI is recorded separately at publication;
no queued/running workflow is counted as a pass.
