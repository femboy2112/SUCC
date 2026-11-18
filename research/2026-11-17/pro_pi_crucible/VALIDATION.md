# Validation receipt and proof authority

## Source and work isolation

- Repository: femboy2112/SUCC.
- Base: 81be6b897ae980b801a3b9de9e22ef81e8360bfb.
- Branch: research/pro-pi-normality-full-source-offensive-2026-11-17.
- This is an isolated checkout; only additive dossier and test files are
  proposed. No original forcing, frozen source archive, main branch or
  donor branch was edited.
- All remote heads were fetched; relevant open PRs #657--#663 were pinned
  as recorded in SOURCE_SNAPSHOT.json. The named Gemini branch was initially
  absent, then read-only audited at 97c7433371feca631991a1b8227b656e92e4abcb
  once it appeared. No unpushed work was assumed.

## Completed baseline and focused runs

The evidence directory contains actual command arrays, elapsed wrapper
times, exit codes and raw stdout/stderr. Times are observations, not estimates.

| Run | Result | Receipt |
|---|---|---|
| Baseline provenance | PASS; 72 manifest items | baseline_0.json |
| Baseline observer foundations | PASS | baseline_1.json |
| Baseline ordinal report | PASS | baseline_2.json |
| Baseline integer BBP carrier | PASS; 15 tests | baseline_3.json |
| New focused modules | PASS; 27 tests, 1.194 s unittest time | focused_final.json |
| Standalone separate prime audit | PASS; 128 principal-part and 17 LCM cases | prime_independent_final.json |
| Original prime probe | PASS; 1,665 comparisons, 988 cutoff cases, 1,662 rejected mutations | prime_survival.json |
| #657 Borwein replay | PASS; 9 tests | parent_borwein.json |
| #662 wall/cofactor replay | PASS; 13 tests | parent_walls.json |
| #657 pole/history replay | PASS; 10 tests | parent_poles.json |
| #657 two-form locked replay | PASS; 8 tests | parent_locked.json |
| Exact swept cross-implementation comparison | PASS; 10 configurations | sweep_comparison_script.json |
| Final provenance | PASS; 72 manifest items | provenance_final.json |
| Final observer foundations | PASS | observer_final.json |
| Final ordinal report | PASS | ordinal_final.json |
| Targeted baseline import diagnosis, configured | PASS; 11 tests | baseline_import_configured.json |

The universal paper results do not derive their quantifiers from these
finite counts. The source-tail and exact algebraic proof arguments are
separately displayed in the theorem manuscripts.

## Required full-suite gate: initial failure retained

The first attempt was exactly

~~~sh
timeout 600s python -m unittest discover -s tests -p 'test_*.py'
~~~

with BLAS/OpenMP/MKL thread counts limited to one. It returned **124 after
600.061 seconds**. Its log contains one error marker before the timeout;
it did not reach a suite summary. It is **not a pass**, and the number of
completed cases is not inferred from a string of dots.

The error was isolated to
TestMetaChoiceDescent.test_exact_probe_receipt_and_independent_count.
Its unchanged subprocess script failed with:

~~~text
ModuleNotFoundError: No module named 'observational_succ'
~~~

The test, script and imported module were each verified byte-identical to
pinned main. The unconfigured error is preserved in
baseline_import_unconfigured.json. Supplying the repository root in
PYTHONPATH resolves the environment cause: the complete targeted 11-test
module then passes. No baseline implementation was edited.

The STALE/MISSING mathematics-catalog text in the initial log comes from
an intentional temporary-fixture mutation in test_math_memory.py. That
fixture expects the stale check to return 1; the text alone is not another
failure.

### Configured full-suite replay

A single configured replay was started with:

~~~sh
PYTHONPATH="$PWD" OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
timeout 1800s python -m unittest discover -s tests -p 'test_*.py'
~~~

**PASS: 14,503 tests run in 1,222.448 seconds; OK (skipped=2).**
The bounded wrapper exited 0 after 1,227.983 seconds. The two skipped cases
are the R26 and R27 methods in LeanEncodingReceipts, whose shared reason is
"pinned Lean 4.14.0 not available". Their full identifiers and identification
method are in evidence/full_suite_skips.json. The raw complete stdout, stderr
and environment/command receipt are evidence/full_suite_configured.*.

This run covers the first published implementation tree
bcad7b2bafd996696a84087e2c14f4dc2a076f52, including the 27 new tests.
The later additions are proof/audit documents, archived receipts and two
standalone probes; those probes were executed separately as recorded below.
No existing runtime module or either integrated test module changed after
this full run. The full suite was not repeated for documentation additions.

## Other verification boundaries

- Local Lean executable: not found on PATH. No Lean formalization of the
  new arithmetic or observer theorems was attempted or claimed.
- Same-model hostile audits: prime height/cutoff, Borwein inverse, sharp
  energy theorem and counterfeits; their reports are retained in audits.
  They are not external peer review or statistically independent witnesses.
- The prime audit's denominator-exponent wording and effective-threshold
  details were incorporated. The final dossier audit also corrected a
  prose sentence to say that BI5 bounds squared word-frequency error.
- No new code depends on the donor #663 implementation. Its head was read
  and audited; its stated 24-test receipt is an inspected donor receipt,
  not a local replay of those tests.
- The refreshed #663 receipt of 53 tests was inspected, not replayed.
  The later adelic branch's 15-test suite was replayed in scratch; its exact
  denominator failure is preserved despite its native tests passing.
- Hosted check states for donor heads are snapshots only. At observation
  #657 included two cancelled checks; #663 included one in-progress check.
  No cancelled or in-progress check was represented as successful.
- No merge, force-push, tag, release, frozen-history edit or main modification.

## Reproducibility and code identity

See TESTS.md for commands and source extraction. IMPLEMENTATION_SHA256.json
records final implementation files and primary proof documents by SHA-256,
independent of later receipt-only edits. Commit identifiers and remote
publication are recorded by the draft PR and final operation report.

Original-source terminal coercivity, R0, swept convergence and full
base-16 pi normality remain **OPEN** regardless of software test outcomes.

## Final late-frontier probes and publication

The portable root audit of pinned 97c7433 exited 0 in 0.550 s. It verifies
three precise algebraic errors and the surviving matrix/sign repair using
SymPy and Fraction, without importing donor modules. The finite CRT signature
probe exited 0 in 0.048 s: four cases, three direct reverse enumerations,
including the q>K noninjectivity control and 240 admissible U_6 words.
See evidence/audit_adelic_pinned.json and evidence/crt_signature_probe.json.
The exact B=3 repaired witness and native 15-test replay are separately
archived with their actual commands; no repeated execution is invented.

Draft PR: https://github.com/femboy2112/SUCC/pull/664 .
The first local content commit was 41ded6ab6952290f67b5791e159ec349861f3618.
Direct git push failed because the CLI had no GitHub credentials. The
authorized GitHub connector published commit
1d33174c39625b39b54d49533b2aac028952d3ec with the identical tree
bcad7b2bafd996696a84087e2c14f4dc2a076f52; the original local commit was
preserved on the local-evidence branch. The publication receipt is
evidence/publication_initial.json. Later receipt/audit additions are
published as an ordinary descendant on the same draft branch; no history
is rewritten. Hosted checks are stated only for the exact observed head.

Closing source cutoff: evidence/frontier_closing_snapshot.json pins #663
at 74b9f48 and the adelic branch at 9ff8544c. The latter25-test receipt and
#663's new method were not replayed. One additional bounded exact prime-path
probe checked the printed normalization/valuation failures and B=1,...,32
modular-wrap identities; evidence/fqr_minimal_arithmetic.json records it.
No absence of a wrap witness in that finite range was made into an all-B
claim. The H-05 backward-seed correction and M-04/finite lane refinements
are paper proofs, not newly claimed test suites.

A later hosted query completed the first published head's record: all 19
checks succeeded at 1d33174c. Exact names, head, timestamps and URLs are
in evidence/first_published_head_ci_complete.json. This is not a claim
that the final receipt commit's newly scheduled checks have completed.
