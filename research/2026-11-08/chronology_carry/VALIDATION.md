# Validation, exact scope and failed invocations

All work is additive under `research/2026-11-08/chronology_carry/` relative to
starting head `19d98078b60e47092c9b9d050a70b6b7eabb7cd2`. Native source,
tests, scripts, formal files, provenance and shared docs are unchanged.
The original proof baseline remains d32342d3; fetched main remains43a60781.

## Completed local checks

- 43 focused tests: root8, model8, theory13, hostile14. Exact integer/rational
  and interval checks have their stated finite domains; no finite pass is a
  normality proof. [Root command receipts](validation/SUMMARY.json).
- The original three lightweight gates pass: `verify_provenance.py`,
  `observer_foundations_probe.py`, `ordinal_succ_report_probe.py`.
- Four Lean4.14.0 integer-coordinate identities are kernel checked in
  [CarryPoisson.lean](CarryPoisson.lean). Axiom output lists only propext and
  Quot.sound. No added axioms, admitted proofs, complex analytic estimate or
  asymptotic normality theorem is formalized here.
- Source/model freeze matches pushed5e1e3fad exactly. The full later source
  replay completed with literal U0=0, all110004 carries, every held-out principal
  part, unwrapped/carry hashes and separate modular checkpoint identities.
- The independently prepared192-bit modular BBP computation and70-digit
  interval trigonometry verify14 predetermined phases/28 components. This is
  selected-point source verification, not an independent full covariance sweep.
- Separate Gaussian-integer/Fraction calculations reproduce the four all-table
  dual floors, bypassing the primary Box arithmetic and local-prime frame.
- Signed and retrodictive numerical payloads replay identically; the earlier
  [replay summary](validation/REPLAY_SUMMARY.json) retains these executed commands.
  The final focused run need not repeat unchanged large replays.
- The carry-only EI1 probe constructs six innovation means from the carry tape
  before comparing with phase means. All fit the explicit analytic error bound;
  direct character and Poisson calculations agree. This is exploratory reuse of
  the same holdout, not fresh empirical confirmation of decay.
- A final read-only agent audit found no correctness or scope defect in CCV7,
  EI4 and the root claim summaries. Its exact reviewed file hashes and scope
  are in [FINAL_REVIEW.json](validation/FINAL_REVIEW.json); this is a same-model
  proof review, not external refereeing or new computational evidence.
- Local Markdown destinations, JSON payloads and `git diff --check` pass.
  Artifact hashes include the completed native log and are verified by the
  final manifest command.

## Native suite status

The corrected full native suite **PASSES: 12,147 tests in 1971.773 seconds**,
with process exit0. This is an actually completed new run, not a relabelled
earlier pass. Its command, environment, test summary and log hash are in
[NATIVE_SUMMARY.json](validation/NATIVE_SUMMARY.json). Native inputs stayed
unchanged throughout this run and final documentation publication.

The first invocation omitted repository PYTHONPATH. Its child command
`scripts/meta_choice_descent_probe.py` could not import `observational_succ`.
The error was independently reproduced with PYTHONPATH unset and the same
test passed with the repository on PYTHONPATH. The known-failing initial full
run was terminated (exit143) to release resources before completing the corrected
full run. No source/test change was made to hide the failure.

Receipts: [initial partial log](validation/native_suite.log),
[exact isolated failure](validation/native_failure_reproduced.log),
[child import traceback](validation/native_failure_child.log),
[targeted successful rerun](validation/native_failure_targeted_rerun.log),
[corrected full run](validation/native_corrected_environment.log).

## Other failures and limits

The first Lean attempt used two Mathlib-style cast theorem names unavailable
in Std. It failed, and its output is retained in
[lean_initial_failure.log](validation/lean_initial_failure.log). Replacing those
names with an explicit proved cast equality fixed the source. The successful
final kernel output contains no sorryAx; the failed attempt is not a proof.

A hostile review found that the exploratory retrodiction parser could silently
zip a truncated phase row. Length/start guards and a rejecting regression were
added before the first exploratory holdout evaluation. Its mathematical model
and frozen training experiment were unchanged.

The original L1 model test fails, including all-table dual certificates.
Both trained models worsen all signed-window comparisons with zero. These are
mathematical experimental outcomes, not implementation failures to suppress.

No full-source approximation asymptotic, source-selected innovation mean decay,
external scholarly refereeing, or global Lean proof is claimed. Hosted CI is
separate and must be read at the final pushed SHA. Source/paper/finite/kernel/CI
statuses remain distinct.

At checkpoint ebe5c553, three hosted workflows had passed and Observational
SUCC validation was still running at the retained observation time; see
[HOSTED_CHECKPOINT.json](validation/HOSTED_CHECKPOINT.json). Final-head hosted
status is reported separately on the draft PR, avoiding a self-referential
commit hash or an implied final-head pass.

## Reproduction

From the repository root with the existing environment:

```sh
PYTHONPATH="$PWD" OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 \
  /tmp/succ-learning-yoneda-venv/bin/python -m unittest discover -s tests -p 'test_*.py'
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/chronology_carry/validate.py \
  --output /tmp/succ-chronology-replay --replay
LEAN_NUM_THREADS=1 lean research/2026-11-08/chronology_carry/CarryPoisson.lean
/tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/chronology_carry/manifest.py
```

The exact model/source reproduction commands are also in
[model/VALIDATION.md](model/VALIDATION.md). No dependency installation occurred.

Pi base16 normality: OPEN. RH: OPEN.
