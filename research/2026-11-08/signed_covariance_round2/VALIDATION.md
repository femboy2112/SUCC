# Executed validation and publication scope

Pinned main:d32342d375f44ddf62221ad6aff2f534abdc0a03.
Research parent:1990b05117d84b33094c8e0f53f7d19b60f48060.
The existing non-main branch and draft#544 are used. Main was fetched again
before final publication and still matched; no rebase or baseline rewrite.
All changes are under this new research namespace. No frozen/native/shared
catalog path was edited.

Final fresh replay command, executed successfully:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 /tmp/succ-learning-yoneda-venv/bin/python research/2026-11-08/signed_covariance_round2/validate.py --output /tmp/succ-round2-final-replay
```

The [replay manifest](validation/final_replay/replay.json) records every
command, return code, code hash, elapsed time and comparison. Total command
wall time153.92 seconds. All commands exit0; all14 mathematical payload
comparisons pass (only observational elapsed-time fields are ignored).

| Check | Executed outcome | Boundary |
|---|---|---|
|Root instrument/selector tests|13PASS|Finite code contracts, source and interval identities|
|Cube tests|7PASS|Exact finite algebra; no analytic theorem inferred|
|Chronology tests|11PASS|Includes3newdigit-leakage tests|
|Hostile tests|6PASS|Independent exact source/Gram controls|
|All new tests|37PASS|Not counted as part of native suite|
|Cube oracle|66cases,1,950,022literal cubes;11,382preceding tuples|Signed formal coefficient histograms|
|Fourth-moment oracle|18cases,46,434free Fourier triples;48support checks|Different representation, shared source|
|Chronology oracle|1,186,678counted instances|Exact finite source/moment/transcript checks|
|Digit-leakage oracle|612checks,144source-phase cases|Shared calibrated interval engine|
|Hostile oracle|73,484checks|Separate Gaussian-rational/source algorithms|
|Root instrument review|3,759energy+1,360covariance containments|Independent exact oracle; shared model|
|Selector|888comparisons+384hostile checks;5,112coset-invariance checks;490order-product checks|Does not certify quantitative PNT/CP theorem|
|Signed-lag measurements|156PASS finite threshold;128coherent-control rejections H>=4|152eligible for nonresonant local bound|
|Source/phase independent samples|28direct modular states;84exact forced phases|Unwrapped chronology/carry hashes also retained|
|Lean4.14 core|4theorems KERNEL PASS|Integer recurrence only; three usepropext, none usesorryAx|
|verify_provenance.py|PASS|Required repository gate|
|observer_foundations_probe.py|PASS|Required repository gate|
|ordinal_succ_report_probe.py|PASS|Required repository gate|
|Native unittest suite|NOT RERUN; prior12,147PASS reused|Explicit unchanged-input comparison and prior receipt|

The native inputs compared are observational_succ,tests,scripts,formal,
provenance,docs,AGENTS.md,pyproject.toml and requirements paths. Their unchanged
scope is machine-checked in the replay; Git object IDs are in PROVENANCE.json.
The prior full-suite receipt is
`research/2026-11-07/learning_yoneda/validation/native_suite.json`.
Use `validate.py --full` to repeat it; no new native test run is claimed.

The environment remains the existing isolated Python3.12.3 research venv;
no global package change. Exact tests use integer/Fraction arithmetic. Phase
certificates reuse the pinned80-bit outward integer-rectangle engine, with
its previous independent rational-Taylor calibration preserved. Scientific
library versions are unchanged from the prior provenance dossier.

Lean's exact scope is in hostile/LEAN_RECEIPT.json. Kernel transport does not
formalize denominator divisibility, the four rational poles, CP/PNT, cube or
covariance inequalities, selected cancellation, pi normality or RH. New
analytic results are paper proofs with classical imports and same-model
cross-review. Scoped review hashes distinguish before/after additions; final
hostile review and cube's CH7 review cover the final added statements.

An initial standalone selector oracle failed because its arithmetic import
path was absent; this ordinary implementation error was fixed and the corrected
oracle passed the fresh replay. No failed invocation is represented as a pass.

Raw retained receipts are in receipts/ and the three front directories.
ARTIFACT_MANIFEST.json hashes all files in this namespace except itself and
ignored bytecode caches. No downloaded source PDF is redistributed.
Hosted CI is separate: this file asserts local results only. Final-head hosted
status is reported through the PR handoff after publication, without claiming
an overall CI pass before every required run completes.

**Pi base16 normality: OPEN. RH: OPEN.**
