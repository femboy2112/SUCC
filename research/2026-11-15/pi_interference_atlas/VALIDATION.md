# Executed validation and bounded proof review

## Final result

**13,535 full-discovery tests passed**, including all **71 new tests**.
The focused suite passed **208 tests**; its tests overlap the full suite.
The standalone arithmetic audit passed **5,416 exact assertions** and was
replayed by root without production imports. All three required repository
gates exited zero. The final 74-row catalogue passed the parent-blob audit.

These are finite validation results. The displayed mathematical proofs carry
the universal claims in IA-01–12; no new proof-assistant verification or
original-source normality/R0 estimate is asserted.

## Full production snapshot

The integrated run used Python 3.12.14 in an isolated copy at
`/tmp/succ_atlas_validation_8097d9e`. It contained parent
`8097d9e802da1d83a615d8812e74279820f5ae7e` plus all six frozen new
production/test files. The snapshot manifest is `receipts/full_snapshot.json`.
The final working-file hashes match that manifest exactly.

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
```

The runner reported **13,535 tests in 1031.218 seconds, OK**. The enclosing
command took 1039.575 seconds and exited 0. The raw log and execution metadata
are `receipts/full_suite.log` and `receipts/full_suite.json`; the parsed,
hash-checked result is `receipts/validation_summary.json`. Its parser uses the
final top-level summary because the log also contains nested four-test and seven-test
subprocess summaries; the initial first-match extraction was corrected.

The dossier prose was completed after the production snapshot and is checked
separately. No production or test code changed during the full run. This is
full current-code discovery, rather than a parent-only baseline plus an
unexamined extrapolation to new modules.

## Focused tests

| Module family | Executed tests |
|---|---:|
| New finite interference compiler | 25 |
| New gauges and hostile controls | 31 |
| New universal harmonic detector | 15 |
| Existing echo transport | 8 |
| Existing collision frame | 21 |
| Existing phase detection | 29 |
| Existing random probe frames | 10 |
| Existing carry/bin-window conjugacy | 16 |
| Existing source authentication | 27 |
| Existing collective spectral machinery | 26 |
| **Total** | **208** |

This final named-module run passed with no failures or errors in 2.242 seconds.
Its exact file hashes and module counts are in `receipts/focused.json`, with
full output in `receipts/focused.log`.

**Preserved harness failure.** The first focused command specified
`top_level_dir='.'` in unittest discovery. The namespace tests directory was
rejected as not importable before any tests ran. The correction loaded the
named modules directly; no production code or test namespace was changed.
`receipts/focused_attempt_1.json` and `.log` preserve that failed attempt.

## Independent arithmetic implementation

`independent_audit.py` reconstructs complex arithmetic from pairs of
Fractions, finite characters by integer polynomial remainders, the four-pole
source directly, actual periodic radix orbits, and finite product probability
laws. It imports no `observational_succ` module, production test, other-agent
note or production output. Its theorem formulas and the general research
context are shared premises; this is implementation separation, not an
independent source of arithmetic truth.

The **5,416 exact assertions** include normalized signed polarization,
geometric Gamma probabilities and moments, Poisson kernel/series identities,
ordered pair energies including diagonals, Laurent/Walsh character controls,
actual periodic coset Fourier coefficients, labelled versus unlabelled
chi-square, product-report censuses, original signed-source Green bounds,
and exact echo identities at source clocks 19–41. Development sizes 1–8 and
fresh fixture sizes 11, 13, 17 are retained in the receipts.

Optional Gamma quadrature at 65 decimal digits is explicitly
`NUMERIC_DIAGNOSTIC_ONLY`; those values do not enter the exact assertion
count. Exact rational circle fixtures are explicitly not BBP phases.

Root's final replay completed in 0.599 seconds, with all 5,416 assertions
passing, and is pinned to the final theorem, map and catalogue in
`receipts/independent_root.json`. The original agent run remains in
`receipts/independent.json`; a root replay before the final F60 provenance
correction is preserved in `receipts/independent_root_before_provenance_fix.json`.
These earlier receipts identify their historical catalogue snapshots.
Repeating the same script does not multiply the count of independent evidence.

## Required repository gates

All ran with `PYTHONPATH=.` and exited zero:

| Command | Elapsed seconds | Receipt stem |
|---|---:|---|
| `python scripts/verify_provenance.py` | 0.043 | `receipts/provenance` |
| `python scripts/observer_foundations_probe.py` | 0.093 | `receipts/foundations` |
| `python scripts/ordinal_succ_report_probe.py` | 1.877 | `receipts/ordinal` |

Each stem has both JSON metadata and a raw log. These gates preserve the
existing project contracts; they do not prove the new arithmetic targets.

## Catalogue, provenance and coverage checks

`catalogue_audit.py` verifies all 74 sequential IDs, all required target and
response fields, legal relation/representation labels, row presence in the
Markdown map, the map hash, every mapped source path and every frozen code
hash. **42 distinct mapped inputs**, plus two further core inputs, were
checked against their exact parent Git blobs: 44 pinned inherited paths in
total. The result and pin list are `receipts/catalogue.json` and
`receipts/inherited_blobs.json`.

The counts are representation and logical-role counts, not counts of newly
implemented algorithms or independent normality equivalences. For example,
F62's equivalence is explicitly to R0, and F73's sufficient thresholds are
explicitly to weaker rungs. F74's requested rate/window normalization remains
underspecified and is not promoted to a full-normality implication.

**Preserved provenance failure.** The first parent-blob audit caught F60's
source path pointing to the new map itself. That was a real source-accounting
defect: 42 existing paths were not yet 42 inherited inputs. F60 now points to
the inherited `research/2026-10-27/BBP_ECHO_DELAY_TRANSPORT.md`, while current
IA-02 receives credit for its full finite-polynomial synthesis. The final
audit passed. `receipts/catalogue_attempt_1.json` preserves the failed check.

## Paper and coverage review corrections

The reviewed theorem snapshot began at
`9d1b3008c32fa56d017993d8ac8c3a435fa948f182bf44228f9f3242390b5850`.
The final reviewed hash is
`00066c945a9e8896f09e08405ffb89172ac7542a7dc5c0f4fdf3453cd4f7ea5e`.

Review closed these substantive scope issues:

- IA-02 explicitly requires unit phases before using negative powers and
  conjugation as inversion; IA-01's optional disk domain is separate.
- IA-06 specifies independent fresh U-based trials, positive integer sample
  counts, positive epsilon tending to zero and confidence values between 0 and 1.
- IA-10 names the sampled cross product and keeps the valid inequality
  decoder-squared≤conditional energy. Decay implies decoder decay in that
  direction; the reverse fails because relative bin phases can cancel.
- The additional canonical comparison exposed the missing explicit defect
  thresholds and the distinct Route-C top-interaction request. F73 and F74
  now register them with their proper weaker/auxiliary scopes.

Constructor, adversary and translation notes retain both findings and their
bounded closing receipts. `receipts/proof_review.json` pins the final note
hashes and review scope. These are related-agent reviews with shared context,
not independent external peer review or a numerical truth probability.

The staged whitespace check then found extra terminal blank lines in the map
and translation notes. Those two EOFs were normalized, and the catalogue
map-hash field was refreshed. `receipts/proof_review.json` records the exact
before/after hashes and byte-equivalence scope; every target and mathematical
statement stayed identical. Final source and arithmetic receipts were refreshed
after this purely textual correction, without rerunning production tests.

## Final artifact checks

`receipts/artifact_check.json` records syntax compilation without executing
new tests, JSON parsing, local-link existence, final reviewed-hash alignment,
source/frozen-code integrity and whitespace checks. `FILE_HASHES.json` pins
the deliverable bytes, excluding itself to avoid a self-reference. Publication
additions are checked against the same local tree before a draft PR is opened.

The resulting boundary is precise: the observation algebra and controls are
validated, while the source-specific asymptotic inequalities in NEXT.md and
the catalogue remain unpaid.
