# Executed validation and precise scope

## Completed checks

| Gate | Observed result |
|---|---|
| New module focused tests | **32/32 pass**, exact rational/cyclotomic arithmetic |
| Full repository test suite | **12,210/12,210 pass** in 978.827 seconds, process exit 0 |
| Independent frame/local-inverse oracle | **11,975 checks pass**; five wrong inverse formulas rejected |
| Independent lock-in oracle | **783 source words / 66,960 source-reference pairs**, exact mean and variance; seven rejected mutants |
| Independent scan oracle | **582 checks pass**, including nine fresh source scan and transport enclosures; three rejected mutants |
| Fresh source protocol | **12 readouts** on A=19,37,73,137 and m=8,12,16 reconstruct exactly |
| Source recurrence in fresh protocol | **528 transitions**, including repeated prefixes, match the four signed fractions |
| Separate source implementation cross-check | **155/155 states**, U0 through U154, exact agreement |
| Provenance gate | SOURCE_PROVENANCE_VERIFIED |
| Foundation and ordinal probes | Exit 0 |
| Explanatory figure | Rendered and visually inspected; display-only floating arithmetic |

Root executed every program in this table. The standalone oracle files import
no SUCC module. Their arithmetic uses rational polynomial quotients, Gaussian
rationals, and sound Machin/Taylor intervals. Counts are finite scope, not
independent academic witnesses or proof of universal claims.

The source protocol rejects nine malformed/substituted cases and separately
checks three non-Gaussian constant gains. The varying-phase source substitution
was discovered during the adversarial pass; it is labelled as a derived control
rather than a predeclared holdout. No source trend or asymptotic rate is inferred.

## Required full repository suite

Command, from the new worktree root:

```sh
PYTHONPATH="$PWD" python -m unittest discover -s tests -p 'test_*.py'
```

The full suite completed successfully: **12,210 tests in 978.827 seconds, OK,
process exit 0**, using Python 3.12.14. [The raw log](FULL_TEST_LOG.txt) and
[hashed receipt](FULL_TEST_RECEIPT.json) preserve the observed result. The
implementation at published checkpoint `774dd2f91a8f91c58281fefb10d4fe36d290d59c`
has the same code inputs used throughout this run. The module and 32-test file
were frozen before it began and still match the bounded implementation audit:

- Module SHA256: `4d47c84a9a7797e1522539bcaea1f51abb78e0fd51231c7a34baeae93dbc75d4`.
- Tests SHA256: `8f0470154f1829278498febc8722040e5838568a31674c550a624e78072e2257`.

Putting the root on PYTHONPATH uses the already diagnosed uninstalled-checkout
import setup from PR541. No historical source or test is changed.

## Receipts

FOCUSED_TEST_LOG.txt, FINITE_RECEIPT.json, INDEPENDENT_FRAME_RECEIPT.json,
INDEPENDENT_LOCKIN_RECEIPT.json, INDEPENDENT_SCAN_RECEIPT.json,
SOURCE_CROSSCHECK_RECEIPT.json, PROVENANCE_RECEIPT.json,
FOUNDATIONS_RECEIPT.json, ORDINAL_RECEIPT.json, FULL_TEST_LOG.txt and
FULL_TEST_RECEIPT.json preserve the corresponding raw outputs, exact values,
scopes and hashes.

No physical instrument run or Lean certificate for the new mathematics is
claimed. Hosted CI is separate; inspect the draft PR at its exact current head.
**Original-source all-epoch decay and pi base-16 normality remain OPEN.**
