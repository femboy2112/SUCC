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

## Borwein ratchet and triadic transport continuation

This continuation starts from published commit
`e855200a9a447933ef93b3ee0947d14d00ef42de`. New mathematical executables,
tests, proofs, audits and a figure remain isolated in the dossier. The exact
general convolution queries reuse the October Borwein CDF without changing
that dependency. Existing factorial-hologram results are attributed rather
than presented as new discoveries.

| Check | Actual result | Receipt |
|---|---|---|
| Main exact Borwein probe | 4,285 assertions, zero failures | `receipts/BORWEIN_REPORT.json`, `receipts/borwein-probe-check.json` |
| Separate geometric audit | 382 assertions, zero failures | `receipts/BORWEIN_INDEPENDENT_AUDIT.json` |
| Complete dossier suite | 74 methods PASS in 13.380s, including 13 new Borwein methods | `receipts/borwein-focused-suite.log`, `receipts/borwein-focused-check.json` |
| Required full native suite | 13,047 tests PASS in 1348.871s; wrapper exit0, 1356.879s | `receipts/borwein-native-suite.log`, `receipts/borwein-native-check.json` |
| Provenance | PASS: 72 imported items | `receipts/borwein-provenance.log` |
| Observer foundations and ordinal probes | Both PASS | `receipts/borwein-checks.json` and named logs |
| Earlier executable preservation | All 13 earlier dossier Python hashes unchanged; native source/tests/provenance/dependencies unchanged | `receipts/borwein-source-preservation.json` |
| Explanatory figure | Regenerated and visually inspected after layout adjustment | `figures/borwein_ratchet.svg`, `plot_borwein_ratchet.py` |

The Borwein probe uses exact rational geometry to check shifted and scaled
window queries, sign-quadrant geometry for the positive-part CDF, independent
prime-power marking for degrees at labels 1..1000, and exact source-braid
checks. It records the first three odd-width releases at 7,56,418 and retains
exact formula parameters even when the resulting rational has very large
numerator and denominator. Decimal logarithms are explicitly approximate
display diagnostics; none decides an equality, release or sign.

The constant-half-width observer visits every label 2..90 in its recorded
180-stage prefix and reports precisely the source primes. This checks the
same controller on a different width schedule. It is a Python arithmetic
run, not a new measured beta-reduction trace. Infinite productive traversal
and the stochastic rectification theorem are supported by written proofs.

The independent audit calibrates rational polygon clipping against full,
empty, half and quarter boxes. Its geometric oracle does not call the
inherited inclusion-exclusion CDF; that routine is a comparator. The tests
still share the classical uniform-convolution model, so they are not
independent evidence for a source-specific number-theory conjecture.

### Repairs and retained history

The proof review corrected a unit-projector coefficient and made the full
carrier explicit in the multiplier-independence argument. The code review
found public summaries with impossible width products that could produce
purported probabilities 50 and 25/12. Exact necessary product bounds,
singleton consistency and a probability guard now reject these cases. The
regressions also retain valid extremal summaries. Reviews contain the
original witnesses and their successful replays. The 74-method suite above
was run after these changes.

An integration helper initially used a nonexistent manifest key `artifacts`
instead of `artifact_sha256`. It failed before producing a preservation
receipt; the schema was then read and the comparison rerun successfully.
This nonmathematical helper failure is recorded in
`receipts/borwein-integration-history.json`.

Finalization also repaired a metadata parser that initially selected a nested
four-test fixture summary instead of the final 13,047-test native summary,
and removed one trailing blank line reported by the formatting gate. Both
receipts are preserved in that integration history. The full native log was
unchanged and passed; these were reporting and formatting repairs.

The native suite was run once in this continuation, with the checkout root
explicitly available through `PYTHONPATH`. Its full output and final summary
were observed before publication. All earlier full-run records, including
the historical import-path failure and incomplete retry, remain intact.
Hosted CI results are separate from these local receipts.

### Triadic source and phase replay

The root executed the finalized `triadic_probe.py` from `/tmp`, confirming
its explicit repository-root import bootstrap. The run passed and is
preserved in `receipts/TRIADIC_REPORT.json` and `receipts/triadic-check.json`.
It includes symbolic determinant and gauge identities, all 64 fourth-root
phase triples (16 flat and 48 nonflat), all 64 pure-gauge configurations,
16 composed-chord controls, and exact agreement between the boundary and
vertex transport conventions. The edge Gram determinant is checked as the
squared holonomy defect.

The source portion checks 587 prime edges through label 500, 12,000 exact
anchor-word/formula cases, both orders of A2/A3 composition on 500 labels,
and 24 explicit norm-error-one witnesses. It reproduces the preserved local
unit loops of the transposition (5 7), its 14/10 braid discrepancy, and its
19/13 mixed-composition discrepancy. The unique global fixed spaces and
strong limits are proved in the note; finite basis checks alone would not
establish them. These distinct case counts are not combined into a purported
number of independent witnesses.

Final catalog, graph and formatting results are retained in the named
`borwein-integration-checks.json` receipts and the validation manifest.

## Return families, common roots, and typed channels

This continuation starts from published commit
`3b2a3058ac6973da43554cbeeaaeee806a891d67`. The initial triadic witness was
replayed before building on it. New source implementations remain isolated
in this research dossier; earlier dossier Python files and native sources
are preserved byte for byte. The new proofs are in `RETURN_PATHS.md`,
`COMMON_ROOT_AND_LIMITS.md`, `TYPED_CHANNELS.md`, and
`MOTION_AND_COHERENCE.md`.

| Check | Actual result | Receipt |
| --- | --- | --- |
| Main return-family probe | 107,806 exact checks, zero failures | `RETURN_PATH_REPORT.json`, `return-probe.log` |
| Separate literal-word/category audit | 353,330 exact checks, zero failures | `RETURN_PATH_INDEPENDENT_AUDIT.json`, `return-independent.log` |
| Source-swap control | 788 exact checks, zero failures | `RETURN_SOURCE_REPORT.json`, `return-source.log` |
| Quaternion/coherence probe | 1,559 exact checks, zero failures | `MOTION_REPORT.json`, `return-motion.log` |
| Centered-root and analytic-boundary probe | 28,076 exact checks, zero failures | `ROOT_LIMIT_REPORT.json`, `return-root-limit.log` |
| Typed-channel probe | 354 exact checks, zero failures; 3,575 literal histories through cost9 | `TYPED_CHANNEL_REPORT.json`, `return-typed-channels.log` |
| Complete dossier suite | 86 methods PASS in12.905s, including12 new return-family methods | `return-focused-suite.log`, `return-checks.json` |
| Required native suite | 13,047 tests PASS in1517.658s; wrapper exit0 in1523.964s | `return-native-suite.log`, `return-native-check.json` |
| Provenance, observer foundations, ordinal report | All PASS | `return-checks.json` and named logs |

All receipt filenames in this section are relative to `receipts/`. The root
actually replayed every listed probe. The final root/typed reports were
compared to the recorded deterministic reports, with exact agreement; their
separate wrapper is `return-extension-checks.json`. The 86-method suite
preceded the two final standalone probes, whose files are not imported by
that suite. The new tests use literal word execution, correct partial
domains and sparse states without artificial finite-matrix truncation.

The main arithmetic holdouts include137,169,221,257,289,331,437,509,667,1009.
The separate audit also enumerates seven literal histories to5 and their
five affine equivalence classes. The universal common-domain criterion,
prime projection equivalence, fixed-space and strong-limit results rest on
written proofs, not a finite range of these holdouts.

The centered-root probe retains the d-1 affine offset, the strict q^j>M
finite-window threshold, a noncoprime iteration mutation, norm-one moving
inputs, exact moment bounds, and the r=1 analytic exception. Its coefficient
conditioning test compares overlapping worst-case measurement balls at
epsilon=rho^N/2 with separated balls at rho^N/3. This is a declared
observation-interface bound, not a proof-hardness certificate.

The typed probe checks formal coefficients against literal paths, both
inverse identities, noncancelling resource counts under cancelling
amplitudes, the zero-cost loop, cost3/4 equivalent implementations, and
flat/twisted compatible-root conditions. Positive-cost formal series are
not silently promoted to numerically convergent analytic functions. The
unit and map types are tested separately from their amplitudes.

The implementation accepts real rational amplitudes. Complex coefficient
and phase statements in the notes have analytic proofs; the finite return
API does not implement arbitrary complex phases. The motion probe uses
exact rational quaternion arithmetic. Counts across these related probes
are not summed as independent evidence for a universal conjecture.

### Integration history and proof-review boundaries

The root/category review distinguished the unique common fixed line from
all common eigenspaces: epsilon1 is a common eigenvalue-zero vector for
the strict returns. The forward category and its added partial-operator
returns remain different typed settings. The proper-lower-presheaf gluing
obstruction and37/50 versus13/50 phase counterfeit are preserved.

Three nonmathematical integration repairs are retained in
`return-integration-history.json`: an added-file patch was rejected before
writing because one line lacked its prefix, and a wrapper initially compared
the typed probe's short stdout summary to its full saved report. Both probes
in that wrapper had exited zero. Correct schema-aware comparisons then
passed without changing their mathematical implementations. A local-link
regular expression also mistook an unchanged displayed coefficient-extraction
formula for a Markdown link; excluding mathematics and code repaired that
checker. No earlier proof or actual link was changed.

The full native suite completed once in this continuation, with its final
13,047-test summary selected after the nested fixture summaries. Its result
is PASS, not inferred from progress dots. The native source/test tree was
unchanged; new isolated executables were checked by the separate probes.

Source preservation, local links, catalog, graph, formatting and artifact
hashes are recorded in the final integration receipts and validation
manifest. These same-model audits are not external peer review. Hosted CI
is distinct from the completed local checks.

## Twin observers, present frames, and retained branches

This continuation starts from published commit
`7622063945ab06c72b092371747a1a5bbbf35e3a`. The root replayed the existing
centered-root and typed-channel canonical probes before building on them.
`twin-baseline-replay.json` binds the unchanged sources and prior reports.
The October twin-frame and dual-boundary notes were inspected and preserved.

The user refined the protocol while work was active: only present outputs
at one meeting event may be compared. Earlier observations require their
event/frame transport and a separate evolution or prediction rule. That
refinement entered the contract, proofs and controls before final testing.

| Check | Actual completed result | Receipt |
| --- | --- | --- |
| Typed transport and arithmetic extension | 122,975 exact checks PASS | `TWIN_TRANSPORT_REPORT.json`, `twin-transport.log` |
| Present outputs, frame/metric transport and seam | 1,219 exact checks PASS | `TWIN_SEAM_REPORT.json`, `twin-seam.log` |
| Separate gluing and naturality implementation | 7,315 exact checks PASS | `TWIN_GLUING_REPORT.json`, `twin-gluing.log` |
| Gaussian-rational tensor/readout implementation | 396 exact checks PASS | `TWIN_CORRELATION_REPORT.json`, `twin-correlation.log` |
| Complete dossier suite | 99 methods PASS in12.785s, including13 new methods | `twin-focused-suite.log`, `twin-checks.json` |
| Required native suite | 13,047 tests PASS in1404.833s; wrapper exit0 in1411.864s | `twin-native-suite.log`, `twin-native-check.json` |
| Provenance, observer foundations, ordinal report | All PASS | Named twin logs and `twin-checks.json` |

Receipt filenames in this section are relative to `receipts/`. The root
actually ran every listed check. Related check counts are kept separate;
they are not independent votes for a universal theorem. The native suite
ran once for this continuation and its final summary, after nested fixture
summaries, was used. Earlier native sources/tests were unchanged throughout.
New research code is isolated and checked by the separate dossier suite
and probes. Hosted CI is distinct from these local completed runs.

The transport oracle covers96 rational typed chains,99 reduced return pairs,
134 basis labels including104729, and four fresh-flag schedules. Sparse
infinite-operator actions have no artificial finite-matrix boundary. Its
controls distinguish adjoints from inverses, unitary from nonsurjective
isometric transport, principal compression from a unitary extension, and
fresh records from reusing one environment.

The frame probe compares only two declared present outputs. It rejects
mismatched events, frames, units and dimensions, and a raw history list.
It checks gauge-covariant current output, transported nonunitary metrics,
path holonomy, coarse-output blindspots, typed defect telescoping, and the
weighted finite-prefix bound. Rational frame fixtures use denominators7,
11 and13 and finite paths through length6; unitary paths extend through8.
Universal frame and norm statements rest on the written algebraic proofs.

The gluing oracle exhausts all255 nonempty restrictions of a three-bit
source and all4,096 binary-report/target triples on a four-state source.
Exactly99 restrictions glue every compatible pair;1,880 target triples
factor through the present joint output. Its naturality controls cover
2,040 paths through length7. It retains global parity, hidden-coordinate,
shared-invalid-relation and source-interpretation countermodels.

The tensor probe uses exact Gaussian rationals, including holdout dimensions
7 and9. It distinguishes transpose, adjoint and conjugate transport; computes
Bell readout probabilities, deferred readout identities, environment overlap,
the17/25 acceptance counterexample, and finite/infinite weighted boundaries.
The full physical-collapse claim remains UNVERIFIED; this is a mathematical
protocol, not a reported quantum experiment.

### Integration history and proof scope

`twin-integration-history.json` preserves the metadata repair: the wrapper
initially left the correlation count null because that report uses the key
`checks`. The actual full396-check report and process had passed. The count
was extracted from the saved report without changing its source or rerunning
mathematics. Patch delivery/context retries occurred before the corresponding
document edits were applied and are recorded separately from mathematical
validation. Redundant non-discriminating development checks were removed
before the final396 count. No failed mathematical check was concealed.

The independent decompositions are same-model audits, not external review.
They sharpened the square-map/common-orthonormal-basis domain, the D>=1
prefix condition, existence for a certified actual source pair versus
surjectivity for all pairs, and the nonfunctoriality of individual dilations.
The written proofs establish the universal statements within those domains.
No finite count supplies an infinite meeting or an arithmetic remainder bound.

The final integration receipt records source preservation, local links,
catalog, typed graph and staged formatting. The updated manifest hashes
all retained artifacts except itself. All27 preceding dossier Python files
and the native source/test/provenance/dependency paths remain unchanged.
