# Validation, provenance and authority

Parent at execution: `1a1524de28b155139d8fe84ea90fc2f117fbb9f3`.
Worktree: `/media/leah/SPANKBANK/SUCCYBOI/SUCC-arithmetic-barrier`.
Branch: `research/bbp-arithmetic-barrier-2026-10-30`.
All new deliverables are in this directory. Commands executed before the
delivery commit record the parent as HEAD while the added files were present;
the source manifest pins their final bytes. This is not a claim that the
new tests already existed in the parent commit.

## Required repository checks

| Check | Result | Raw receipt |
|---|---|---|
| Full `unittest discover -s tests -p 'test_*.py'` | **10,008 tests PASS**,1068.855s test runtime;1079.479s command elapsed | [full-suite.log](receipts/full-suite.log), [metadata](receipts/full-suite.json) |
| `scripts/verify_provenance.py` | PASS:72 items,17 byte-identical archives,55 namespace migrations | [provenance.log](receipts/provenance.log) |
| `scripts/observer_foundations_probe.py` | PASS, with its explicit unproved-foundations fields retained | [foundations.log](receipts/foundations.log) |
| `scripts/ordinal_succ_report_probe.py` | PASS, with its explicit RH/Weil/ordinal limits retained | [ordinal.log](receipts/ordinal.log) |
| `scripts/verify_math_memory_graph.py` | PASS:51 typed nodes,60 edges; not independent proof checking | [math-graph.log](receipts/math-graph.log) |
| `scripts/build_math_memory.py --check` | **FAIL: baseline stale/missing catalog**, not promoted to PASS | [child](receipts/math-catalog.log), [clean parent](receipts/baseline-math-catalog.log) |

The clean-parent catalog replay used a separate detached worktree at the exact
parent, with the same interpreter. Both report stale/missing
`docs/math_memory/CLAIM_CATALOG.json`; no broad catalog regeneration or
historical contract change was performed. The required full test suite has
no failures. Hosted Actions are a separate delivery check; local success
does not establish hosted CI. Consult the draft PR's exact-head checks for
their later state.

The system Python3.12.3 had mpmath1.2.1, below the declared >=1.3 requirement.
An isolated ignored `.venv` was installed with `.[test]`; it uses Python3.13.13,
mpmath1.3.0, numpy2.5.4, sympy1.14.0 and scipy1.18.1. Required suite execution
used one numerical thread and a1024MiB address-space cap. The full run began
2026-10-30T15:45:05Z and ended16:03:04Z. Agent standard-library probes used
Python3.12.3 as recorded in their own receipts. No repository dependency
specification changed.

## Focused and independent checks

| Scope | Result | Evidence |
|---|---|---|
| Parent prime stroboscope |15 tests PASS;138 oracle equalities across46 authentic cases | [parent-focused](receipts/parent-focused.log), [parent-oracle](receipts/parent-oracle.log) |
| Arithmetic |14 tests PASS;275 exact shadow/lift cases across five coefficient families,23 authentic births,19 null-source births | [scoped validation](arithmetic/VALIDATION.md), [independent receipt](arithmetic/independent_receipt.json) |
| Signed CRT |12 tests PASS;36 certified period/frequency rows;206 independent phases and144 numerical interval cross-checks | [test log](signed_crt/focused_tests.log), [command receipts](signed_crt/command_receipts.json), [probe](signed_crt/probe_receipt.json) |
| Stoneham/triangle |19 tests PASS; integer-LCM oracle and alternate exact arc-radius minimization | [scoped validation](transfer/VALIDATION.md), [commands](transfer/validation_commands.json) |
| Root finite circle |8 tests PASS;64 full complex-sum rectangles and three occupancy tables through1024 | [tests](receipts/finite-circle-tests.log), [exact interval run](receipts/finite-circle.log) |
| Independent real-pi calibration |1400-digit pi phases,100-digit character calculations agree with all64 rectangles and all three count tables | [independent-circle](receipts/independent-circle.log); numerical cross-check, not interval authority |
| Root arithmetic implementation |45 clock/lift cases plus births and explicit conductor-grid controls PASS | [domain-repaired oracle](receipts/independent-arithmetic-domain-repaired.log) |
| Partial-packet survival |512 exact nonzero rationals;2268 comparable-prime checks at seven fresh times | [packet-survival](receipts/packet-survival.log) |
| Fixed filters |28 exact cases from seven filters;4055 retained-prime valuation checks | [fixed-filter](receipts/fixed-filter.log) |
| Null source small depths |Exact E1=-8/105 supplies the separate Q3/5 cases | [null-small-depths](receipts/null-small-depths.log) |
| Independent proof review |AT/TR/root interval derivations and sharp6n proof reviewed; CG-03 independently expanded | [review](signed_crt/INDEPENDENT_REVIEW.md), [hashed proof receipt](signed_crt/conductor_growth_review_receipt.json) |

The new focused count is14+12+19+8=**53** test methods. These tests are
separate from the10,008 repository tests because research directories are
not recursively discovered by the repository test command. Counts of
assertions, samples and numerical comparisons are not added to either test
count or called independent proofs.

The packet holdout retains cancellations `(n,p)=(127,37),(274,73),(761,569)`.
This is consistent with a finite exceptional-prime set for each bounded
packet range. The run does not prove the asymptotic rate; that authority is
the sign, finite-exception and PNT argument in the dossier.

The final artifact check verifies24 unchanged parent inputs,16 related-commit
source references, both scoped manifests, raw receipt hashes, Python syntax,
JSON parsing and local Markdown links. Its counts and exit code are retained
in [final-validation-complete.log](receipts/final-validation-complete.log) and
[metadata](receipts/final-validation-complete.json). This check does not certify a
mathematical theorem.

## Failed attempts and corrected fixtures

- The first root independent arithmetic run included `(p,a,k)=(7,3,1)`,
  violating its required p>L=7 domain and reaching a noninvertible modular
  denominator. The failed [raw output](receipts/independent-arithmetic.log)
  and exit1 metadata are preserved. The case was replaced with13,3,1 and
  an explicit domain assertion was added. The corrected45-case run passes.
  This was an oracle-case error, not an admissible counterexample to AT-01.
- The transfer Champernowne fixture compared21 expected characters with a
  20-character slice. Independent encodings already agreed. The corrected
  slice passes, and [failed fixture output](transfer/control_fixture_failure.log)
  remains preserved.
- Mathematical failures are never erased: naive p-squared lift, actual
  full<=primary+1, V<=4, native-period transplantation to p3/7, exact small
  grid transport, bounded posterior reset and primary-only selection are
  refuted or delimited in the theorem and route ledgers.
- The first final artifact check reached a link to its own metadata file
  before the runner had written that file. The failed
  [receipt](receipts/final-validation.log) is preserved. The runner now writes
  an explicitly RUNNING metadata record before launch and replaces it with
  the completed result afterward; the complete replay checks the real link.
  This was a receipt-ordering issue, not a theorem or test-suite failure.

## Replay and evidence boundaries

From the repository root, use a supported interpreter with the declared
test dependencies. Representative focused commands are:

```sh
python -m unittest discover -s research/2026-10-30/arithmetic_barrier/arithmetic -p 'test_*.py' -v
python -m unittest discover -s research/2026-10-30/arithmetic_barrier/signed_crt -p 'test_*.py' -v
python -m unittest discover -s research/2026-10-30/arithmetic_barrier/transfer -p 'test_*.py' -v
python -m unittest discover -s research/2026-10-30/arithmetic_barrier -p 'test_finite_circle.py' -v
python research/2026-10-30/arithmetic_barrier/independent_arithmetic_audit.py
python research/2026-10-30/arithmetic_barrier/packet_survival_audit.py
python research/2026-10-30/arithmetic_barrier/fixed_filter_audit.py
python research/2026-10-30/arithmetic_barrier/finite_circle.py
python research/2026-10-30/arithmetic_barrier/independent_circle_oracle.py
python research/2026-10-30/arithmetic_barrier/campaign_manifest.py --check
```

`run_receipt.py --name NEW_NAME -- COMMAND...` retains bounded raw output,
timestamps, exit code, command, interpreter, source HEAD and log SHA256;
it refuses to overwrite an existing receipt name. Package scripts that
write named receipts should be replayed in a disposable worktree if the
historical output must stay byte-identical.

The root manifest pins deliverable bytes, selected source inputs, and
scoped manifests; it excludes its own bytes and its final checking receipt
to avoid recursive hashes. Related-PR source references are checked at their
declared Git commits, not mistaken for files present on this child branch.
The reasoners share model family, prompt and source lineage; the oracle
implementations rotate arithmetic representation, not provenance. No new
Lean theorem, external referee certification, all-horizon normality proof,
RH proof or priority certification is claimed.
