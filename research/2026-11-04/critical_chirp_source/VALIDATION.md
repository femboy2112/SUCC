# Validation record

Pinned starting head: c9dfcdf057c4870f113e898464e4821c2ff5fedf.
Preregistration was committed and pushed first as e17eef43. The signed
instrument and AH theorem checkpoint was committed and pushed as
29ed93c733cfb2587d37e6f59a0509a9d7971e40.

The isolated `.venv` uses CPython 3.13.13, mpmath 1.3.0, numpy 2.5.4,
scipy 1.18.1 and sympy 1.14.0, with this checkout installed editable.
The initial native source bridge also passed under system CPython 3.12.3.
The parent staging-directory missing-package limitation is resolved here.

## Completed focused verification

- 18 native critical-chirp tests PASS: the inherited 11, including the genuine
  native source bridge, plus 7 new signed-certificate guards.
- 6 derivative tests PASS; 18 exact derivative holdouts; dropped-pole mutation
  rejected; deterministic derivative receipt replays.
- 7 normal-counterseed component tests PASS; 373 good-position rational phase
  certificates; all 373 sign-reversed certificates rejected; receipt replays.
- 4 arithmetic/radial tests PASS; 540 exact state-denominator and LCM checks;
  8,128 unordered pair checks; 7,519 protected pairs all match. Twenty-five
  unprotected denominator changes are retained in the receipt.
- All 12 preregistered original/coherent signed cases replay exactly. The
  instrument enumerates 1,379,840 interval chords across both models and all
  cases, certifies each critical depth rationally, and retains exact M/R bounds.
- Parent CC finite receipt and all 19 Gamma Prybar receipts replay. All 72 historical provenance entries verify;
  observer foundations and ordinal report probes exit 0.

Raw focused logs and required probe JSONs are under [validation](validation/).
Front-specific receipts, commands and negative-control failures remain in each
front directory. The instrument review additionally ran six rational phase
checks and nine small source maxima at 100 decimal digits; those are numerical
diagnostics, not the certificate's authority.

## Whole native suite and exact-head CI

One complete native run was launched at implementation checkpoint 29ed93c7:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  .venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

**PASS: 11,634 tests in 1,038.630 seconds, exit 0; no failures, errors or
skips.** All 11,634 verbose test labels are distinct. The 1,502 snapshotted
native test/package files remained byte-identical through the run. Additive
research-only dossiers were integrated while it ran and their probes were
validated separately. This is execution on the new implementation checkpoint,
not inherited parent validation or a claim that the later receipt commit had
already been executed.

The [native receipt](validation/NATIVE_RECEIPT.json) records exact commits,
counts and hashes; the [complete compressed log](validation/native-suite.log.gz)
is retained. The final pushed SHA's hosted workflows are queried independently;
their final observed state is reported on PR #505. No green parent run is
attributed to this child, and a queued/running hosted job is not a pass.

No new Lean theorem or kernel build is claimed. Proof cross-reviews are
recorded in `front_ah/INSTRUMENT_REVIEW.md`, `front_ah/REVIEW_BDE.md`, and
`front_cfg/REVIEW_AH.md`. They are same-model reviews, not external refereeing.
