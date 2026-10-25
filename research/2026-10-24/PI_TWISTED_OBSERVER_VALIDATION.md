# Twisted observer round: validation and provenance

**Date:** 2026-10-24. **Parent:**
`e648df3e4fca73ab6b942232b5ca4b310e9cac08`.
**Branch:** `research/pi-twisted-observer-agreement-2026-10-24`.

The [mathematical dossier](PI_TWISTED_OBSERVER_AGREEMENT.md) distinguishes
paper proofs, equivalent criteria, exact finite experiments and open arithmetic
claims. These checks validate that distinction and the executable instruments;
they do not establish an infinite normality assertion.

## Tested revision boundary

All three new production modules and all four new test modules were frozen
before the final complete discovery run. Later edits clarified documentation,
registered the claim namespace, and added the separately executed coprime-gain
measurement and inverse-branch oracle scripts. No existing production module, historical claim record,
imported archive, Lean declaration, or provenance manifest was changed.

The parent is the coherent-main #267 merge. PR #266 was inspected at
`e821a90d615aa5f78a61ad08c9d7a44709ad6189` and was not merged into this branch.
Its 27 hosted checks were independently observed completed and successful.
This is an upstream status snapshot, not a claim about hosted checks on this
new branch. The p=2081 count was independently replayed here; the p=1048601
count remains a cited donor result, not a rerun.

The final [machine receipt](PI_TWISTED_VALIDATION_RECEIPT.json) records SHA-256
hashes for the code, tests, report, preregistration, finite receipts and retained
validation outputs. It excludes its own bytes to avoid a self-referential hash.

## Repository gates

| Gate | Result |
|---|---|
| Initial focused inherited source/clock/entropy tests | 42 passed before this round's additions |
| New focused tests | 52 passed in 1.218 seconds |
| Claim namespace guards after final 15-claim registration | 15 passed in 0.057 seconds |
| Complete unittest discovery | 7,653 passed in 723.941 seconds; exit 0 |
| `scripts/verify_provenance.py` | `SOURCE_PROVENANCE_VERIFIED`: 72 items, 17 byte-identical research archives, 55 documented mechanical namespace migrations |
| `scripts/observer_foundations_probe.py` | Exit 0; retained output preserves its own unresolved source/analytic/semantic premises |
| `scripts/ordinal_succ_report_probe.py` | Exit 0; finite probe only; no RH or universal positivity conclusion |
| New Python compilation, relative documentation links and receipt hashes | PASS: 13 new Python files compiled; local links resolved; all 16 explicit receipt file hashes verified |
| `git diff --check` | PASS |

The complete discovery transcript is retained in
[PI_TWISTED_FULL_SUITE.txt](PI_TWISTED_FULL_SUITE.txt). Shorter gate outputs
are included in the machine receipt.

### Runtime and reproducibility

The successful final environment uses Python 3.12.14 with mpmath 1.3.0,
NumPy 2.5.4, SciPy 1.18.1 and SymPy 1.14.0, all within the repository's
declared `test` extra. The checkout was made importable to child scripts with
`PYTHONPATH` and the same virtual environment was first on `PATH`.

From a fresh checkout, install the repository and its declared test extra, or
install those dependencies and make the checkout importable. Then run:

```sh
python scripts/verify_provenance.py
python -m unittest discover -s tests -p 'test_*.py'
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py

python -m unittest tests.test_twisted_observer_probe tests.test_twisted_pair_transport tests.test_twisted_observer_joining tests.test_twisted_source_energy
python -m unittest tests.test_claim_namespace_collisions

python scripts/twisted_pair_transport_oracle.py
python scripts/twisted_observer_joining_oracle.py
python scripts/twisted_observer_common_shift_probe.py
python scripts/twisted_source_energy_probe.py
python scripts/twisted_coprime_gain_probe.py
python scripts/twisted_inverse_branch_oracle.py
```

Two incomplete setup attempts are not counted as passing tests. The first
used a runtime lacking the declared numerical extras and was interrupted.
The second had the extras but an inherited subprocess could not import the
uninstalled checkout; it was interrupted after that environment error. The
identified subprocess test passed once `PYTHONPATH` was supplied. The final
complete discovery was started from scratch with both requirements resolved.
That first completed 7,653-test run then reported one inherited provenance
error because a historical Git blob was absent from the partial-object
checkout. The six exact source credentials were hydrated and verified; the
entire six-test registry module passed on replay. The final full run was then
started afresh and passed all 7,653 tests. No unrelated test was modified to
bypass an environment or provenance failure.

## Independent arrangements and deliberate failure controls

The three exploratory agents share model and repository provenance. Their
agreement is not independent external refereeing. The retained checks instead
use different exact arrangements and explicit falsifiers:

| Instrument | Retained checks and scope |
|---|---|
| [Wire transport](PI_TWISTED_TRANSPORT_RECEIPT.json) | 12,288 signed transport identities, 4,096 quadratic identities, 8,064 detected omitted-transport mutations, 13,000 rational antiphase inequalities, 24 independently arranged BBP forcing/carry steps, 3 odd-radix controls and 2 rejected source/path mutations |
| [Joining controls](PI_TWISTED_JOINING_RECEIPT.json) | Exact finite probability laws at modulus 31, seven-step marginal and differential histories, all 49 prescribed character pairs, source pairs with equal differential and different common signal; a distinct modulus-17 holdout is in the tests |
| [Common initial shifts](PI_TWISTED_COMMON_SHIFT_RECEIPT.json) | Independent exact p=2081 count 76,544 versus 608,400 for each changed-source variant; both wire carry prefixes of length 28 and 1,043 differential samples checked; three independent pair-counter calibrations; a one-wire mutation is detected |
| Sharp coprime-gain theorem | Exact algebraic equality case and smaller-constant mutations; authentic odd-source witnesses at p=41 and p=73; independent audit of 728 finite gain triples |
| [Source energy](PI_TWISTED_SOURCE_ENERGY_RECEIPT.json) | All preregistered p=41,97,257,1009; h=1,3; H=2,4,8,16 within domain; exact source states, outward phase boxes, exact signed-lag versus block-energy identities, constant/alternating controls, independent Machin shadow and Green-tail budget |
| [Fresh gain holdout](PI_TWISTED_COPRIME_GAIN_RECEIPT.json) | Every prescribed p=193,353,577 at h=1; all three certify that the absolute-error bound is vacuous there, and none is omitted |
| [Adaptive inverse-branch oracle](PI_TWISTED_BRANCH_RECURSION_RECEIPT.json) | 10,446 pair recurrence checks, 838 zero-centered-carry checks, all nine source/radius rows and an enlarged-branch mutation; the branch-loss premise is explicitly unproved |

The source-energy receipt was replayed after appending the prospective gain
holdout to the preregistration: all energy intervals and the p=2081 count were
identical, and the receipt now hashes the completed preregistration. Display
intervals have width exactly one 10^-10 tick; the underlying rational bounds
are retained separately in the same receipt.

The final hostile proof read corrected a prime-window index, made the forcing
half-turn condition explicit at character frequency h, declared the Fourier
sign convention, and restricted the diagonal-freedom statement to the
constructed joining family. A final packaging read also made explicit that
the energy criterion must hold for every nonzero integer frequency, rather
than any one frequency alone. None of those edits changes executable outputs.
The inverse-branch addendum was independently checked for its centered carry,
radius, endpoint and exponent constants; its open branch-loss premise remains
explicit. Its standalone oracle and the final namespace guard were executed
after addition; the frozen production and test modules did not change.

## Earned conclusion

The round establishes the stated elementary observation and obstruction
theorems, implements their exact finite controls, and measures selected finite
BBP windows with outward bounds. The temporal-energy criterion is explicitly
equivalent to normality under the inherited window-coverage theorem. No
uniform selected-source cancellation estimate, asymptotic collision bound,
pi-specific independence theorem or proof of pi normality is claimed.
