# Validation, actual runs, and retained limitations

Base: `071ce1e0ee6ab8f8c07113e901131aa646d6b95d`. Runtime: Python3.12.14,
SymPy1.14.0, NumPy2.3.5, SciPy1.17.0, mpmath1.3.0. No new dependency or
production-module modification is required for the mathematical implementation.
Regenerating the optional wave figure uses Matplotlib, available in this
execution environment; it is not needed for the exact tests. Native source/test bytes are
unchanged from the base; new executables/tests are isolated in this dossier.

## Initial observer/cylinder code and exact probes

| Check | Actual result | Receipt |
|---|---|---|
| Dossier unittest discovery, final executable/test bytes | 47 tests PASS | `receipts/final-focused-suite.log` |
| Preregistered arithmetic / spectral / Haar probe | 74,229 checks,0 failures | `receipts/FINITE_REPORT.json`, `receipts/probe.log` |
| Arithmetic labels | Every integer2..10000, independent divisor-multiple table and marking sieve | Finite report |
| Even sum targets | Every even N4..2048, plus2458,4096,8192,16384 | Finite report |
| Actual beta/delta observer | First30 primes through113;3,181 beta and44,018 delta contractions | Finite report `beta_prefix` |
| Zero budget | UNKNOWN, empty observed prefix | Finite report `zero_budget_control` |
| Source/spectrum mutations | Six JSON field mutations rejected; additional unit/type/forgery mutations in tests | Finite report and test suite |
| Cylinder phase cancellation | Exact cyclotomic polynomial remainder checks; no floating tolerance | `test_cylinder.py`, cylinder test log |
| Cylinder source controls | Exact phase-clock, aliases, opposite twist, unit contamination, sparse two-kick paths, histogram transport | `receipts/CYLINDER_REPORT.json` |
| Fejér result | Exact rational bound9/1024 for X10000,K256, plus exact weight and integer Diophantine checks | Cylinder report; this is an analytic bound, not a sampled irrational-phase norm |

The74,229 count is the explicit number of assertions in `probe.py`; it does
not include assertions inside the47 unittest methods or any subagent's
separate diagnostic campaigns. Do not combine these into an invented count of
independent mathematical witnesses. Code SHA256 digests are part of the
finite report and final validation manifest.

## Initial required repository gates (historical record)

| Command / gate | Actual result |
|---|---|
| `python scripts/verify_provenance.py` | PASS:72 imported items verified; `receipts/provenance.log` |
| `python scripts/observer_foundations_probe.py` | PASS, exit0; `receipts/observer-foundations.log` |
| `python scripts/ordinal_succ_report_probe.py` | PASS, exit0; `receipts/ordinal-succ.log` |
| `python -m unittest discover -s tests -p 'test_*.py'` | Completed13,047 tests in1055.659s:13,046 passed,1 subprocess import-path error; `receipts/native-suite.log` |
| Untouched-base reproduction | Same script fails with `ModuleNotFoundError: observational_succ`; `receipts/untouched-base-import-replay.log` |
| Corrected targeted replay with `PYTHONPATH=.` | All11 tests in the affected module PASS; `receipts/native-failure-corrected.log` |
| Full retry with corrected environment | INCOMPLETE / UNVERIFIED; execution handle was no longer available, and the retained log has no final summary. Not counted as a pass |
| Mathematics catalog and graph | Final regeneration/check results recorded in `receipts/catalog.log` and `receipts/math-memory-graph.log` |

The single completed native failure is in
`test_eodcs_meta_choice_descent.TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count`.
It invokes `scripts/meta_choice_descent_probe.py` as a subprocess. This
uninstalled checkout does not put the repository root on that subprocess's
import path. The same failure was reproduced in the untouched base checkout;
adding the root via `PYTHONPATH=.` fixes the affected module without modifying
code. The initial failure and incomplete retry are retained, not erased or
reported as successful full-suite runs.

At that stage every native test case had a passing result across the completed
run and corrected targeted replay, but a single all-green native full-suite
run was not certified. The incomplete retry remains unverified. New full
runs are recorded separately below; hosted checks have separate authority.

## Proof and provenance scope

### Shared-carrier follow-up

The carrier addendum starts from published commit
`836d03806183c1f73488dca1d37e149a9826eb53`. It adds research prose and an
isolated exact probe. The original seven executable/test hashes in
`FINITE_REPORT.json` were rechecked and remain unchanged. Existing native
source and test files also retain their original bytes.

The new `carrier_probe.py` completed **691 explicit checks with zero
failures**, recorded in `receipts/CARRIER_REPORT.json` and
`receipts/carrier-probe.log`. These cover exact rational entropy controls,
the full carrier-cost identity, equal-information/opposite-overlap sources,
bivariate coefficients versus an independent marking sieve for every integer
target 4 through 512, finite horizons and shuffled computation orders,
transported source controls, anchor failures, and a quarter-turn scalar-phase
calibration of the approximate braid estimate. The last calibration is not a
general numerical operator-bound campaign. The entropy routine intentionally
supports probabilities that are powers of two, rather than all probabilities.

The existing dossier suite was rerun: **47 tests PASS** in
`receipts/carrier-focused-suite.log`. Provenance, observer-foundation, and
ordinal probes also passed again; exact command exit codes are retained in
`receipts/carrier-checks.json`. New catalog and graph checks are retained in
the corresponding `carrier-catalog` and `carrier-math-memory-graph` receipts.

The original 74,229-check report is a separate retained run, not a number
augmented by the new controls. The native full-suite history above is also
retained without being rerun for this isolated follow-up. No new all-green
native-suite certification is asserted. Hosted validation remains separate.

The targeted executable audit is retained in
`reviews/carrier_code_audit.md`. It independently enumerated all coherently
transported sum-100 pairs, obtaining 12, while ordinary addition with the
transported multiplicative source retains the count 0. Mathematical identities
and infinite statements are supported by the explicit proofs in
`CARRIER_COUPLING.md`, not by the finite check count.

The universal local claims are supported by the written proofs in
`THEOREMS.md` and `CYLINDER.md`. Finite arithmetic can reject a false claim or
calibrate an implementation; it does not prove Goldbach or any universal
distribution estimate. The final claim ledger and hostile models remain part
of the deliverable.

Same-model construction, adversarial, and translation reviews caught concrete
errors and supplied separate calculation paths. These are recorded in
`AUDIT.md`; they are not external peer review, multi-model independence, or
Lean/kernel acceptance. No physical realization or speedup has been tested.

## Prime-wave continuation

The wave continuation starts from publication
`b3ddf81c4e893866aac04903f682fb5aa01830e2`. It adds the proved categorical
and phase identities in `PRIME_WAVES.md`, isolated rational arithmetic,
exact controls, and a reproducible explanatory SVG.

| Check | Actual result | Receipt |
|---|---|---|
| Main exact wave probe | 27,054 checks, zero failures | `receipts/WAVE_REPORT.json`, `receipts/waves-probe.log` |
| Independent Mobius/gcd replay | 10,424 checks, zero failures | `receipts/WAVE_INDEPENDENT_AUDIT.json`, `receipts/waves-independent.log` |
| Adversarial arithmetic appendix, root replay | 10,999 checks, zero failures | `receipts/waves-adversary-replay.log`, `receipts/waves-adversary-check.json` |
| Dossier unittest suite after repairs | 61 methods PASS, including 14 new wave methods | `receipts/waves-focused-suite.log` |
| Full native repository suite, corrected environment | 13,047 tests PASS in 1185.784s; wrapper exit0 | `receipts/waves-native-suite.log`, `receipts/waves-native-check.json` |
| Provenance, observer foundations, ordinal probes | All PASS | `receipts/waves-checks.json` and named logs |
| Scientific figure | Rendered and visually inspected; exact inputs, illustrative drawing | `figures/prime_wave_interference.svg`, `plot_prime_waves.py` |

The main probe checks every label 0..10000 against an independent marking
sieve, including the explicit 0/1 exclusion. It checks every integer target
4..512 and holdouts 514,582,997,1024,4096, local interference for primes
through47, complete CRT periods through210, and the homometric, modulo30,
endpoint, alias, and coherent-reference controls. The independent replay
uses a Mobius divisor formula rather than importing `prime_waves.py`.
The unittest suite also reduces roots of unity by exact cyclotomic
polynomials; no floating tolerance decides a mathematical equality.

The adversarial review found two input-interface gaps: a nonbinary mask
could enter `pair_count`, and an empty left spectrum skipped checking a bad
coefficient on the right. Both were repaired, regression cases were added,
and the complete 61-method dossier suite was rerun. The mathematical valid-
input formulas were unchanged. Reviews are retained in
`reviews/wave_adversary_audit.md` and `reviews/wave_resonance_audit.md`.
The latter also caught and repaired an overbroad singular-series quantifier:
the finite positive limit is stated for fixed even N>=4 and exhausting
prime sets, excluding N=0 and nonexhaustive sequences.

These execution counts have overlapping mathematical content and shared
provenance. They remain separate receipts, not a count of independent proof
witnesses. The code and proofs leave the universal prime-pair remainder
estimate open. The figure is an illustration, not numerical proof evidence.

### Reproduction commands

This continuation completed a single clean full native-suite run with the
checkout root explicitly set in `PYTHONPATH`. It resolves the local
full-run certification gap described in the historical record above; those
earlier failure and incomplete-retry logs remain preserved. The wrapper took
1190.924 seconds including startup and captured the full final summary.
Native source, tests, provenance files and dependency declarations were not
changed; their preservation and the eight earlier dossier executable/test
hashes are recorded in `receipts/waves-source-preservation.json`.

From the repository root, either install the declared test extras in the
chosen environment or expose the current checkout to subprocesses:

```bash
PYTHONPATH=. python -m unittest discover -s tests -p 'test_*.py'
PYTHONPATH=. python -m unittest discover \
  -s research/2026-11-12/prime_fixed_point_observer -p 'test_*.py' -v
```

Only the second, short command is the new dossier suite. The native suite is
much larger. The task publishes a draft research branch; no merge, tag, release,
main-branch modification, or solved-conjecture status is asserted.
