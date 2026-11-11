# Validation and publication checkpoints

## Publication history

Base: SUCC Main XXII at `43886e830cee5ff6d6b37719e18d809819673bd9`.
Branch: `aletheia/cursed-categories-dedekind-yoneda-2026-11-10`.

The first requested push is commit
`3f68a7d6be38c811591f8f85f2e8cdb47673a58c`: Rounds I and II, their exact probe,
local claim ledger, provenance and generated discovery catalog. Its remote
Git tree exactly matched the locally staged tree
`5be2c11eed9226384f8c687c38ed366bf8ee37d4`.

The second requested push contains Round III, the expanded ledger and sources,
all four standalone probe receipts, this validation record, and the regenerated
catalog. A single draft PR is opened at that final head. Workflow files are
unchanged; the ordinary PR gates then run on the completed result.

## Required repository gates

The full existing unittest suite ran once while the checkout remained frozen at
the first checkpoint. No core implementation, existing test, dependency file,
or workflow differs from the pinned base in the final patch. The additional
Round III research scripts were tested separately at their final source hashes,
and the final discovery catalog received its own freshness check.

Runtime: Python 3.12.14. The hosted Python-version matrix is a separate gate.

The initial full run did **not** finish green. Its sole error was
`test_exact_probe_receipt_and_independent_count`: the subprocess entrypoint
`scripts/meta_choice_descent_probe.py` could not import `observational_succ`,
because this fresh checkout had not yet been installed as an editable package.
The error was reproduced directly as `ModuleNotFoundError`. The repair was
`python -m pip install --no-deps --no-build-isolation -e .`, with the declared
test dependencies already present. No source code was changed. The entire
11-test affected module then passed, including its real subprocess invocation.
The original failure log and successful retest are both preserved.

The 18-minute full suite was not repeated after this isolated environment
repair. Thus the record is a full run with one diagnosed setup error plus a
successful targeted module retest, not a claimed clean second full run. The
hosted workflow performs its own editable install and full matrix run.

| Command | Actual result |
|---|---|
| `python -m unittest discover -s tests -p 'test_*.py'` | 12,806 tests in 1,062.048 s: 12,805 passed; one missing-package subprocess error, repaired and retested as below. |
| `python scripts/verify_provenance.py` | PASS at the final working tree. |
| `python scripts/observer_foundations_probe.py` | PASS at the final working tree. |
| `python scripts/ordinal_succ_report_probe.py` | PASS at the final working tree. |
| `python scripts/build_math_memory.py --check` | Checked after final document assembly; see repository_validation.json. |
| `git diff --check` | Checked on the complete staged patch; see repository_validation.json. |

The raw unittest output and execution metadata are in `receipts/`. The provenance
receipt verifies 72 imports: 17 byte-identical research archives and 55 documented
namespace migrations, against original source commit
`ba075348b7bcc66d938b3e0ca96c26e95bba340a`. The regenerated catalog retains the
base's 170 existing warnings; it introduces no new warning or global claim
status promotion.

## Exact research probes

Each command below completed successfully with `python -W error`. The saved
JSON receipts bind the actual script SHA-256; `probe_manifest.json` provides a
compact cross-reference. The rational compiler receipt also hashes its shared
BBP implementation dependency. Counts are executed cases, not independent
witness counts or universal theorem proofs.

| Probe | Representative finite scope |
|---|---|
| `round_ii_probe.py` | 27,000 affine associativity triples; 348 typed Karoubi arrows; 15,768 composable pairs; 1,640 affine Möbius grid points with two-sided and recursive inverses; 1,296 matrix-unit products; 256 span pairs; exact oscillator Laurent coefficient. |
| `round_iii_dedekind/dedekind_order_probe.py` | 4,416 Galois pairs; 77 completed-lattice pairs; 1,187 rational-code roundtrips; 2,209 order comparisons; 128 dyadic enclosures; two 80-step locator schedules; three rejected mutations. |
| `round_iii_dedekind/computation_probe.py` | 270 source recurrences and refinements; 11 independent Machin tail comparisons; 36 pi digits through exponent 255; 35 sqrt(2) floor certificates; two 128-step Stern–Brocot paths; 15 character rectangles; eight recovered authentic prime-defect phase cells; floor and phase mutations. |
| `round_iii_dedekind/rational_compiler_probe.py` | 10,000 quadratic matrix-product instances; 1,944 rational-function evaluations; seven exact signs; seven floors; seven actual naturality/composition diagrams including zero dimensions; malformed and information-loss controls. |

Core acceptance arithmetic is integer or `fractions.Fraction`. The proofs of
all infinite statements are in the notes. The table is not a claim of formal
kernel verification, PIGAME execution, or an all-epoch statistical bound.

## Proof audit and provenance limits

Constructor, computation, and adversarial-review bearings checked the exact
maps, variance, composition, endpoints, source normalization and failure modes.
These were same-model research agents, not external mathematical referees.
The root reran every standalone probe and inspected the critical proofs.

Separate derivations and implementations included Pell recurrence versus a
binomial expansion and integer-square floor tests, BBP intervals versus Machin
intervals, direct matrix products versus quadratic-field multiplication, and
coefficientwise versus recursive affine inversion. The character routes share
their Taylor evaluator; that dependence is disclosed and its remainder bounds
are proved separately. The Q(pi) compiler explicitly inherits classical pi
transcendence and the certified source name; neither is inferred from samples.

The audit repaired the at-least-two-prime scope of the mixed separability
contrast, specified the interval versus circle Wasserstein metric, retained
the open/closed rational endpoint distinction, specified the Yoneda transpose,
and separated rectangular corner maps from square algebras. It also records
that canonical symbolic Q(pi) expressions cannot generally be recovered from
arbitrary Cauchy names, even when the represented values are rational.

## Hosted CI and remaining mathematical scope

This file records local verification. Hosted CI starts from the draft PR opened
after the final push and has its own status on GitHub; no hosted success is
asserted by a local receipt. No merge, tag, release, or historical-default change
is part of this round.

The authenticated source and original-zero seed are preserved. The completed
constant uses pi=sum(16^(1-n)r(n)); the alternate P-infinity is pi/16. The new
finite source-sign recovery does not establish the required all-epoch signed
estimate. Pi normality, original-zero parity balance, and RH receive no proof
or status promotion from this dossier.
