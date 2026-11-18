# Validation receipt and proof authority

## Source and work isolation

- Repository: femboy2112/SUCC.
- Base: 81be6b897ae980b801a3b9de9e22ef81e8360bfb.
- Branch: research/pro-pi-normality-full-source-offensive-2026-11-17.
- This is an isolated checkout; only additive dossier and test files are
  proposed. No original forcing, frozen source archive, main branch or
  donor branch was edited.
- All remote heads were fetched; relevant open PRs #657--#663 were pinned
  as recorded in SOURCE_SNAPSHOT.json. No unpushed Gemini work was assumed.

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

**IN PROGRESS at the first dossier commit.** No pass is claimed for it here.
The final operation will append its actual completion/timeout receipt.
Discovery found 14,503 outer test cases in this additive checkout; discovery
alone is not an execution result.

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
