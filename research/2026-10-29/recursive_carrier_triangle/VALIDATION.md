# Validation and authority boundaries

**Research date:** 2026-10-29. **Interpreter:** Python 3.12.14.
**Pinned starting main:** `ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc`.

The paper proofs, exact finite executions, optional floating-point observations,
and repository integration checks have different scopes. None is silently
promoted to another. No Lean kernel verification, independent peer review,
selected BBP cancellation, pi normality, or RH result is claimed.

## Executed research checks

| Check | Actual result | Receipt and scope |
|---|---|---|
| New standard-library unit tests | 25 passed | [focused.log](receipts/focused.log); exact identities, hostile controls, boundaries and fail-closed inputs |
| Separate exact oracle | 6,491 checks passed; 8/8 false mutations rejected | [independent_oracle.json](receipts/independent_oracle.json) |
| Production research probe | 837 exact checks passed | [production_probe.json](receipts/production_probe.json) |
| Optional phase observations | 9 finite cases executed | same production receipt; these are high-precision observations, not interval certificates |
| Inherited Oily module tests | 26 passed after declared dependencies were provided | [oily_baseline.log](receipts/oily_baseline.log) |
| Inherited path-field and Pólya tests | 19 and 10 passed | [initial_environment_checks.json](receipts/initial_environment_checks.json) |

The oracle does not import the production triangle module. It reconstructs
quadratic-field arithmetic, source transforms, raw moments, cumulants,
factorial differences and full-word probabilities separately. Its quadratic
arithmetic is calibrated against SymPy. This is implementation and method
separation, **not independent source provenance**: both implementations are
required to use the same authenticated original BBP source. The root researcher
executed the oracle and inspected its actual output rather than accepting an
agent's success report as a proof.

The finite mutation receipts reject an altered signed pole, an omitted
posterior normalizer, resetting the carrier between segments, resetting the
source tilt, pairwise-only log truncation, false flatness, an incorrect mixed
difference exponent, and an invented cross-forcing term. Universal statements
instead rely on the analytic derivations in the three linked proof dossiers.

## Required repository gates

| Gate | Result | Receipt |
|---|---|---|
| `python scripts/verify_provenance.py` | PASS | [provenance.log](receipts/provenance.log) |
| `python scripts/observer_foundations_probe.py` | PASS | [foundations.log](receipts/foundations.log) |
| `python scripts/ordinal_succ_report_probe.py` | PASS | [ordinal.log](receipts/ordinal.log) |
| `python -m unittest discover -s tests -p 'test_*.py'` | 9,808 tests; 0 assertion failures, 1 reproduced environment error; exit 1 | [full_suite.log](receipts/full_suite.log), [full_suite.json](receipts/full_suite.json) |

Exact commands, exits and durations for the completed short gates are in
[required_gates.json](receipts/required_gates.json).

The full suite's test runner reported 956.156 seconds (962.947 seconds for
the complete command). Its only error was the inherited subprocess import
case diagnosed below. The other 9,807 cases completed successfully, and all
11 cases in the affected module passed in the corrected replay. The full
command itself is retained as **exit 1**; no second complete green run is
claimed. The `STALE/MISSING` message referring to a temporary catalog in the
raw log is an intentional negative fixture inside the catalog tests, not
another reported suite failure.

### Environment history and the full-suite import error

The runtime initially lacked the repository's declared `mpmath` and `sympy`
test dependencies. The initial missing-dependency results are retained in
`initial_environment_checks.json`; they are not counted as passing runs.
After installing `mpmath 1.3.0` and `sympy 1.14.0` into an isolated dependency
directory, the Oily and ordinal checks passed.

The full suite used that dependency directory on `PYTHONPATH`, without an
editable package installation or the checkout root on the child-process path.
One inherited test launches `scripts/meta_choice_descent_probe.py` directly.
That child sees `scripts/` as its first import directory and cannot import
`observational_succ` under this incomplete environment.

The [baseline reproduction](receipts/baseline_environment_reproduction.json)
records a separate clean detached worktree at the exact pinned main commit:

1. The same target test fails on unchanged main with vendor-only `PYTHONPATH`.
2. Its direct child fails with `ModuleNotFoundError: observational_succ`.
3. Adding the baseline checkout root makes the target test pass.
4. Adding the current checkout root makes the entire affected test module
   pass: **11 tests**. No source modification was needed.

The raw [baseline failure](receipts/baseline_missing_root_targeted.log),
[direct-child failure](receipts/baseline_missing_root_direct_probe.log),
[baseline correction](receipts/baseline_corrected_targeted.log), and
[current corrected replay](receipts/current_corrected_test_file.log) are
preserved. This supports an environment diagnosis, rather than concealing the
initial nonzero exit or treating it as a new research regression.

For normal reproduction, install the checkout as the repository's CI does:

```sh
python -m pip install -e '.[test]'
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_recursive_carrier_triangle.py'
python scripts/recursive_carrier_triangle_probe.py --numerical --output /tmp/triangle-probe.json
python scripts/recursive_carrier_triangle_oracle.py --output /tmp/triangle-oracle.json
```

An isolated dependency installation also works when `PYTHONPATH` includes both
that dependency directory and the exact checkout root. The finite checks and
their command-line scopes do not establish the paper theorems by themselves.

## Source binding and integration

[SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) pins the starting commit and tree,
the inherited source Git blobs and SHA-256 hashes, and all four executed Python
files. Historical source files, the original recurrence and its zero seed,
import archives, claim namespaces and CI policy are unchanged. PR #359 was
read at its exact head as sibling context; none of its unmerged files is
imported as a premise.

The mathematics discovery catalog is regenerated from the final documents.
This changes discovery metadata only; it does not assign proof authority or
promote historical claims. The local claim ledger has 23 scoped entries.

Final structural checks verify the 13 pinned source/code hashes, all local
Markdown links in this package, Python compilation, `git diff --check`, and
`python scripts/build_math_memory.py --check`. The catalog's pre-existing
warnings, if any, are discovery diagnostics rather than proof promotions.

Publication is a draft research PR with one consolidated commit. Hosted CI is
a separate execution: this local report makes no claim that it has completed
or passed. The PR's live checks are the authority for that state.
