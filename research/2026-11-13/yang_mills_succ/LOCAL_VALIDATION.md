# Local validation and authority boundaries

Base: `db9fb4b84672050efa79b13377f1e73364598a14` (Main XXV).
Date: 2026-11-13. All new code is standard-library Python using exact rational
arithmetic. No upstream Lean declaration was compiled or kernel-replayed here.

## 1. Reproduced gates

| Command | Result | Evidence |
|---|---|---|
| `python scripts/verify_provenance.py` | PASS, exit 0; 72 items, 17 byte-identical research archives | [Raw log](validation/provenance.log) |
| `python scripts/observer_foundations_probe.py` | PASS, exit 0 | [Raw log](validation/foundations.log) |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit 0 | [Raw log](validation/ordinal.log) |
| `python -m unittest discover -s tests -p 'test_ym_*.py' -v` | PASS, 36 tests, exit 0 | [Raw log](validation/focused_tests.log) |
| `python scripts/yang_mills_succ_probe.py` | PASS, exit 0; finite positive/negative controls reproduce | [Raw log](validation/finite_probe.log), [JSON receipt](probe_receipt.json) |

[targeted_validation.json](validation/targeted_validation.json) records the exact
commands, exit codes, log hashes, and SHA-256 hashes of both new modules, both
test files, and the probe script. The finite probe's output is byte-identical
to its committed JSON receipt.

The required full-repository suite is recorded separately below. It is not
replaced by the focused suites or by source-integrity checks.

## 2. Full-repository suite

The required raw command was executed to completion:

```sh
python -m unittest discover -s tests -p 'test_*.py'
```

**13,086 tests ran in 1,039.391 seconds; the command exited 1 with one error
and no assertion failures.** The other 13,085 tests passed. The error was
`TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`, whose
subprocess launches `scripts/meta_choice_descent_probe.py`. In this checkout,
that subprocess could not import `observational_succ`. See the unmodified
[full log](validation/full_suite.log).

The environment cause was tested against a fresh detached worktree at the
unchanged base commit. Both the standalone historical script and its 11-test
suite reproduced the same import error there. On the research worktree, all
11 affected tests then passed with the project root supplied through
`PYTHONPATH`. The [diagnosis receipt](validation/baseline_import_diagnosis.json)
records each command, environment override, exit code and raw log hash.

| Discriminating check | Result | Evidence |
|---|---|---|
| Historical probe on unchanged base, no path override | Same `ModuleNotFoundError`, exit 1 | [Log](validation/baseline_import_probe.log) |
| Affected suite on unchanged base, no path override | 11 tests, same one subprocess error, exit 1 | [Log](validation/baseline_affected_suite.log) |
| Affected suite on this branch with `PYTHONPATH` set to the project root | 11 tests passed, exit 0 | [Log](validation/affected_suite_with_project_path.log) |

The repository's [CI workflow](../../../.github/workflows/ci.yml) installs the
project with `python -m pip install -e ".[test]"` before its full test command;
this local checkout was not installed. The diagnosis establishes a missing
package-import precondition in the local run, rather than a regression from
the new modules. No historical script or test was changed. The complete suite
was not rerun after supplying the path, so its recorded raw result remains
**one error**, not a clean full-suite pass. Remote CI is a separate result and
is not claimed here.

## 3. What the focused controls establish

The 14 reflection/Wilson tests check the exact one-plaquette state and its
finite matrices, compare two moment implementations, and calibrate with an
odd-weight negative square, negative reflection form, zero pivots, duplicated
observables and gap-collapse examples. Fresh moment degrees extend through
200. The universal positive-weight and error claims have separate paper proofs.

The 22 phase-transfer tests retain signed coefficients and verify the factor-two
remainder, weighted contraction, closing-margin failure, invisible versus
visible resonance, oscillatory stable readers, and the radix-invariance
boundary mutation. Wrong coefficients, biases, residual budgets and dimensions
are rejected. These test a finite exact implementation; no unlisted phase or
infinite arithmetic source estimate is certified by them.

The earlier SUCC crosswalk audit also replayed 65 tests across the existing
GNS, finite holonomy, arithmetic TFD, Fourier pinbed and minimal-path gauge
modules. Its exact command and per-suite results are in
[SUCC_CROSSWALK.md](SUCC_CROSSWALK.md). Those checks establish implementation
behavior in the existing finite models, not a Yang–Mills identification.

## 4. Proof and implementation review

The root checked the new paper derivations, the actual upstream OPE theorem,
the stronger acceptance specification, and the native `FixedBounds` statement
and `genuine` proof context. Separate agents reviewed the code and mathematics
from different angles. They use the same model family, so their agreement is
not independent expert confirmation.

Alternate solvability and principal-minor calculations informed the review.
They are not promoted into additional proof certificates. The committed exact
tests, raw command logs and supplied paper proofs are the reproducible authority
for the local results.

Review corrected two interpretive points: a target-reader factorization does
not automatically define autonomous dynamics on a quotient, and the chosen
reader need not minimize its norm. Both boundaries are explicit in the final
theorem. The condition `norm(reader) * residual -> 0` is sufficient, without
requiring decay of every coherent direction.

## 5. External artifact checks versus external theorem checks

The fresh upstream run used only the official `integrity` stage at revision
`55ba9fc36293b3f4d52c6b1f813169a0be76ee98`. It checked 9,508 submission files,
43 review modules and four normalized whole-declaration correspondences. It
passed. Its [unaltered receipt](upstream_integrity_receipt.json) records
`source_build_present_at_start: false` and an empty external-command list.
This stage does not run Lean, its kernel, or Comparator.

The root separately rechecked hashes for the 24 core inspected files and the
14 native RG files recorded in [upstream_manifest.json](upstream_manifest.json).
The assessment's first page was also rendered and visually inspected to verify
the existence/gap/uniqueness wording against the extracted text. No complete
source-library semantic audit is asserted.

Historical upstream builds and Comparator results are reported with their
actual dates and scopes in [UPSTREAM_AUDIT.md](UPSTREAM_AUDIT.md). The full
reproduction recipe retains its exact Lean/Mathlib/Comparator pins. Local
finite tests and integrity results must never be presented as a replay of that
complete proof.
