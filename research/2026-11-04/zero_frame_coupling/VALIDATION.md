# Validation and exact authority

This is a research-only addition to #506 at
`bc2d7b01b6b0a37cb79994e180758e98681aa68e`. No inherited source, theorem
contract or test is edited. Paper proofs, executable checks and hosted CI
are distinct authorities. There is no new Lean theorem or external referee.

## Local executable checks

**77 focused tests passed**: 46 inherited tests and 31 new tests (12 native
instrument tests and 19 front-specific checks). Commands, counts and exit
codes are in [FOCUSED_RECEIPT.json](validation/FOCUSED_RECEIPT.json), with the
ten raw logs beside it. These counts overlap the native suite; they are not
77 additional native tests.

The exact finite instrument was generated and replayed successfully. Its
receipt binds the executable hashes, all 3,075 reconciled unwrapped states,
80 factorial cells, 20 controls and 4,272,640 sharp prefix chords. Raw phase
grids are retained in `RAW_GRID.json.gz`. The three independent front receipts
also replayed successfully; see
[REPLAY_RECEIPT.json](validation/REPLAY_RECEIPT.json). A separate LCM plus
convex-hull implementation agrees with four fresh original-source means,
maxima and maximizing intervals at both 80 and 110 digits; see
[NUMERIC_REVIEW.md](front_cf/NUMERIC_REVIEW.md). Numerical agreement is not
the authority for the rational character enclosures or an asymptotic proof.

The single complete native run finished successfully:

- Started at implementation commit
  `8755bc7bade06d6a0893d0b7ece080e79a05072b`.
- Command: `.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v`.
- **11,795 tests, OK**, 1,016.587 seconds reported by unittest.
- Outer process exit 0; elapsed 1,024.274 seconds.
- All **1,512** snapshotted native package/test Python files were unchanged
  throughout the run. The integration commit adds proofs, research probes
  checked above and receipts; it does not change these native suite inputs.
- [Receipt](validation/NATIVE_RECEIPT.json),
  [input manifest](validation/NATIVE_INPUTS.json),
  [complete compressed log](validation/NATIVE_SUITE.log.gz).
- Uncompressed log SHA256:
  `87b23190c425d431fccce09b75aa13883b80cf268f4b70a5f6b7a146a07b0ff2`.

Environment: CPython 3.13.13 in this checkout's `.venv`, editable local
package, mpmath 1.3.0, numpy 2.5.4, scipy 1.18.1 and sympy 1.14.0.
Heavy numerical thread pools were capped with `OPENBLAS_NUM_THREADS=1`,
`OMP_NUM_THREADS=1` and `MKL_NUM_THREADS=1`. No repeated full run was used.

The historical provenance check passes all 72 entries (17 byte-identical
archives and 55 namespace entries); observer and ordinal checks exit zero.
Their complete logs are in [validation/](validation/). The 27 immutable
source-file pins in [SOURCE_HASHES.json](SOURCE_HASHES.json) were verified
against the specified Git blobs. `git diff --check` is clean.

## Reproduction

From an environment installed with the repository's declared dependencies:

```sh
python research/2026-11-04/zero_frame_coupling/coupling_probe.py --verify research/2026-11-04/zero_frame_coupling/FINITE_RECEIPT.json
python -m unittest discover -s tests -p 'test_zero_frame_coupling.py' -v
python -m unittest discover -s research/2026-11-04/zero_frame_coupling/front_ad -p 'test_*.py' -v
python research/2026-11-04/zero_frame_coupling/front_be/probe.py --verify research/2026-11-04/zero_frame_coupling/front_be/FINITE_RECEIPT.json
python research/2026-11-04/zero_frame_coupling/front_cf/probe.py --verify
```

The complete native command is recorded above and need not be repeated after
every mathematical prose edit. Research front tests live outside native
discovery and are covered by the focused receipt.

The final formatting pass removed one trailing blank line from
`certified_phase.py`. Its parsed Python AST is identical to the version used
in the native run. The receipt's helper hash was refreshed, then all 12 native
instrument tests and the complete deterministic finite receipt were replayed
successfully. Raw observations and their hashes did not change. See
[FINAL_FOCUSED.log](validation/FINAL_FOCUSED.log) and
[FINAL_AUDIT.json](validation/FINAL_AUDIT.json). All 1,512 native package/test
inputs still match the completed suite. No full-suite result is claimed for
a later commit merely by inheritance.

## Hosted validation

Hosted workflows are associated with exact commit SHAs. At the time this
integration record was written, implementation SHA `8755bc7b...` had three
successful workflows (institute/core Lean, One Object II, collective
observer), while its Observational SUCC workflow remained in progress.
Those are not results for the subsequent integration SHA. The final exact
head and its current workflow status are reported in draft
[PR #507](https://github.com/femboy2112/SUCC/pull/507); no pending job is
reported as passing and no CI run certifies the new paper mathematics.

## Mathematical review scope

Distinct Mellin/beta, endpoint integration, integer-LCM, symbolic polynomial,
Gram/Bessel and rational interval routes were cross-checked. Workers shared
model and context, so these are method and implementation rotations, not
independent external testimony. Front review files bind the reviewed proof
hashes. The inherited radial-lag statement needs the natural domain
restriction `A+ell>=1` for negative lags; no parent file was rewritten.
All selected original-source normality gates remain OPEN.
