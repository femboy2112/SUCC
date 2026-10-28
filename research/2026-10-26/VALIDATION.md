# Validation and provenance: source bridge and atomic BBP continuation

Date: 2026-10-26. This record distinguishes executable checks from the universal
paper proofs in [the source-bridge dossier](OILY_MACARONI_SOURCE_BRIDGE.md) and
[the atomic continuation](FOUR_POLE_ATOMIC_SUBSTRATE.md).
No new Lean theorem, normality theorem, RH theorem, or academic priority is claimed.

## Exact research baseline

- Repository: `femboy2112/SUCC`.
- Baseline: draft PR [#306](https://github.com/femboy2112/SUCC/pull/306), head
  `7989be5753341c5e74d570e8fea51e00129d2d0a`.
- Baseline tree: `7be31e3213fd4ddcbc9dea9e4b468097ef8a0d56`.
- Main XI: `6dd80730c3575d91f746546a25da5aedbd2e2737`.
- Research branch: `research/oily-macaroni-laplace-mellin-2026-10-26`.
- Preserved imported source commit: `ba075348b7bcc66d938b3e0ca96c26e95bba340a`.

The baseline PR head was re-read before publication and remained unchanged. The four
observed hosted workflows at that baseline had succeeded; these are baseline results,
not results for the new commit. No merge, release, tag, or historical default is changed.

## Environment and commands

Python 3.12.14 in an isolated virtual environment, with the repository's `.[test]`
dependencies: mpmath 1.3.0, NumPy 2.5.4, SciPy 1.18.1, and SymPy 1.14.0.
All commands below run from the repository root with its absolute path in `PYTHONPATH`.

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py

python -m unittest tests.test_bbp_log_mixture tests.test_cyclic_carry_extension \
  tests.test_exponential_gamma_bridge tests.test_ladder_shift_audit -v
python -m unittest tests.test_ladder_contraction_probe \
  tests.test_claim_namespace_collisions -v

python scripts/oily_macaroni_probe.py \
  --verify research/2026-10-26/OILY_MACARONI_RECEIPT.json
python research/2026-10-26/independent_mixture_oracle.py
python research/2026-10-26/normalized_frequency_independent.py
python -m unittest tests.test_bbp_atomic_substrate -v
python research/2026-10-26/bbp_mirror_polynomial_independent.py
python scripts/bbp_substrate_probe.py \
  --verify research/2026-10-26/BBP_ATOMIC_SUBSTRATE_RECEIPT.json
git fetch origin f8f74e0eccb12e0d8aa127b3b5fa091f00367414
python -m unittest tests.test_round2_registry -v
git diff --check
```

The first four commands are the required `AGENTS.md` gates. The first discovery run
found 8,785 tests: the baseline's 8,742 plus 43 new tests. The user's subsequent
four-pole request added a fifth production/test module with 9 tests, bringing the
expanded tree to 8,794 tests and motivating a second complete discovery run.

## Observed results

| Check | Result |
|---|---|
| Final expanded required unittest discovery | **8,794 tests passed in 1,121.891 seconds, exit 0, no failures, errors or skips** |
| First required unittest discovery | 8,785 tests executed in 1,429.491 seconds: 8,784 passed, one environment/provenance-object error; resolved by the targeted rerun below |
| Historical registry after fetching its pinned blob | All 6 tests passed in 2.114 seconds; the previously errored test passed |
| Four new test modules | 43 tests passed in 5.635 seconds |
| Atomic substrate test module | 9 focused tests passed; exact transfer, coefficient minimality, clock, source holdouts and mutation controls |
| Existing ladder instrument and namespace gate | 19 tests passed in 0.325 seconds |
| Imported source provenance | `SOURCE_PROVENANCE_VERIFIED`: 72 entries, 17 byte-identical archives, 55 mechanical namespace migrations |
| Observer foundations probe | Exit 0; its mathematical nonclaims remain explicit |
| Ordinal SUCC report probe | Exit 0; its mathematical nonclaims remain explicit |
| Exact receipt regeneration and replay | `OILY_MACARONI_RECEIPT_VERIFIED` |
| Receipt mutation calibration | Altering the claimed first mixing moment to zero was rejected with `RECEIPT_MISMATCH` and nonzero exit |
| Atomic substrate receipt replay | `BBP_ATOMIC_SUBSTRATE_RECEIPT_VERIFIED`; changing the paired-layer fixed point from one to zero was rejected with `SUBSTRATE_RECEIPT_MISMATCH`, exit 1 |
| Atomic and graded certificates | 8 authentic-forcing holdouts through n=65521, 13 packet/endpoint identities, 9 finite rational fixed-point brackets, exact scalar clock and Hankel witness |
| Independent source and carry oracle | 83 exact source identities, all 256 `C16` additions, and all 92 bit marginals of orders one through three checked |
| Exact even-frequency control | Both digit marginals uniform; nonzero remainder modulo `X^64+1` at `h=2` |
| Independent numerical oracle | Standard-library Decimal, 70 digits, tail depth 64, through `n=16384`; diagnostic values agree |
| Moving-frequency independent oracle | mpmath at 80 digits, depth 24, 12 `(n,k)` cases through `n=1048576`; authentic, two-atom and uniform-cell laws checked; separate quadrature agrees with endpoint integration to about `1.08e-81` |
| Independent mirror/polynomial oracle | 9 exact symbolic identities, 505 pointwise rational checks, 24 moment enclosures, and 5 deliberately too-small tail bounds rejected; root rerun matches saved JSON byte for byte |
| Syntax and whitespace | New modules/scripts compile; `git diff --check` passed |

Raw output from the required gates is preserved in the adjacent `validation/` directory.
The [exact receipt](OILY_MACARONI_RECEIPT.json) includes source hashes, exact controls,
parameters, outward decimal enclosures, and explicit nonclaims. The separate
[oracle output](INDEPENDENT_MIXTURE_ORACLE.json) is reproduced by
[independent_mixture_oracle.py](independent_mixture_oracle.py), which does not import
the new production modules. Its floating/Decimal outputs are not proof certificates.

## Problems actually encountered and resolved

The initial focused baseline run used a bare Python environment without mpmath. It
reported 10 dependency errors and one skip among 59 tests. Installing the declared
test dependencies in the isolated environment resolved that environmental obstacle.

A combined focused run then exposed a numerical-oracle precision problem in a new
test. At `n=73`, the exact rational enclosure can be approximately `2e-154` wide;
50-digit quadrature cannot reliably resolve membership in that enclosure. The
oracle was increased to 220 digits and independently checked at that precision.
The exact interval algorithm and its bounds were unchanged. The subsequent four-module
run passed all 43 tests. This was a test-instrument correction, not a proof by adjusting
an expected numerical value.

Inherited invalid-escape `SyntaxWarning` messages may appear in full discovery. No
unrelated source file was edited to silence them.

The full discovery run completed with one error in
`test_round2_registry.ActualGraphControls.test_real_graph_retains_history_and_checks_new_sources`.
The partial-clone checkout lacked the pinned historical Git **blob**
`f8f74e0eccb12e0d8aa127b3b5fa091f00367414`; the test correctly refused to authenticate
an absent source object. Fetching that exact object from the existing origin restored it.
The complete six-test registry module then passed, including the originally errored
case. No registry, test expectation, or provenance guard was weakened.

The first full run's original error log is retained. At that stage the failure was
confined to a missing immutable object, and the complete affected module passed after
its restoration. The paper-only moving-frequency extension did not change those four
production modules or their tests. The later atomic continuation did add a production
module and nine tests, so a second full discovery run was started on the expanded tree.
Its result is recorded separately below; the first invocation is not rewritten as a pass.

The provenance, observer-foundations and ordinal probes were also rerun after the atomic
module was added. All three exited zero, and their outputs were byte-identical to the
first run. The original outputs in `validation/` therefore also represent these reruns.

The local Markdown-link checker initially misread the inline code `1_[0,d](u)` as a
link. Excluding code spans corrected that checking instrument; the actual relative
links in the changed Markdown documents resolve. No document link was changed to mask
the false positive.

## Final expanded discovery run

After the atomic implementation and its nine tests were added, the complete required
discovery command finished successfully: **8,794 tests in 1,121.891 seconds, OK**.
The log contains 8,794 passing test markers and no skip, error or failure markers;
the process exited zero. Its unchanged raw output is
[`validation/full_unittest_final.log`](validation/full_unittest_final.log).
This is the baseline's 8,742 plus 52 new tests in five new modules. The original
first-run error log and its successful targeted recovery are also retained for an
accurate chronology. No test, registry guard or imported source was weakened.

## What the checks do and do not establish

The all-n inequalities, Mellin identities, asymptotic coefficients, nonnormal rational
control, carry-extension obstruction, and late infinite-product bound have derivations
in the dossier. The finite executable checks corroborate those derivations and exercise
the rational certificate implementations; a finite sample does not supply their
universal quantifiers.

The normalized-frequency diagnostic was independently rerun after copying it into
the repository; its output matched the saved JSON byte for byte. Its exact source-cell
factorization, rational modulus bounds using pi below 22/7, and uniform-cell hostile
control are also included in the regenerated source-hashed receipt. The augmented
receipt passed replay and the same deliberately corrupted-moment rejection check.

Three delegated agents reviewed separate aspects and then audited the assembled
dossiers. The final atomic audit checked the two atoms, signed scalar return, mirror,
sharp polynomial defect, growing-depth quantifiers, graded fixed point, both grading
controls and the natural joint-law distinction. It corrected an angle description
from a quarter turn to pi/4, explicitly restricted scalar rescaling to nonzero values,
and stated n at least one and fixed nonzero integer k where required. These were
scope/prose corrections; no symbolic formula or production algorithm changed.
The agents share a model family and the source context; this is not external
peer review. Distinct check routes included exact Fraction algebra, a separate
standard-library Decimal implementation, high-precision quadrature, an independent
SymPy polynomial expansion, changed-source controls, and exhaustive finite carry algebra.

The authentic four-pole forcing and zero-initialized recurrence were reused without
editing their original implementations. Selected signed Weyl cancellation remains
open. The existing `N - O(log N)` modulus frontier is unchanged.

Hosted checks for the new commit must be read from its PR after publication. This
committed record does not pre-claim a hosted result.
