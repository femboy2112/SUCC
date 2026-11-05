# Validation record

Pinned starting head: c9dfcdf057c4870f113e898464e4821c2ff5fedf.
Preregistration was committed and pushed first as e17eef43. The signed
instrument and AH theorem checkpoint was committed and pushed as
29ed93c733cfb2587d37e6f59a0509a9d7971e40.

The isolated `.venv` uses CPython3.13.13, mpmath1.3.0, numpy2.5.4,
scipy1.18.1 and sympy1.14.0, with this checkout installed editable.
The initial native source bridge also passed under system CPython3.12.3.
The parent staging-directory missing-package limitation is resolved here.

## Completed focused verification

- 18 native critical-chirp tests PASS: the inherited11, including the genuine
  native source bridge, plus7 new signed-certificate guards.
- 6 derivative tests PASS;18 exact derivative holdouts; dropped-pole mutation
  rejected; deterministic derivative receipt replays.
- 7 normal-counterseed component tests PASS;373 good-position rational phase
  certificates; all373 sign-reversed certificates rejected; receipt replays.
- 4 arithmetic/radial tests PASS;540 exact state-denominator and LCM checks;
  8,128 unordered pair checks;7,519 protected pairs all match. Twenty-five
  unprotected denominator changes are retained in the receipt.
- All12 preregistered original/coherent signed cases replay exactly. The
  instrument enumerates1,379,840 interval chords across both models and all
  cases, certifies each critical depth rationally, and retains exact M/R bounds.
- Parent CC finite receipt replays. All72 historical provenance entries verify;
  observer foundations and ordinal report probes exit0.

Raw focused logs and required probe JSONs are under [validation](validation/).
Front-specific receipts, commands and negative-control failures remain in each
front directory. The instrument review additionally ran six rational phase
checks and nine small source maxima at100 decimal digits; those are numerical
diagnostics, not the certificate's authority.

## Whole native suite and exact-head CI

One complete native run was launched at implementation checkpoint29ed93c7:

```
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 \
  .venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
```

It is tracked separately from the focused results; a partial stream is not a
pass. The final outcome, tested commit, input preservation and log hashes are
recorded in the integration receipt/PR when the process exits. No green parent
run is attributed to this child. The final pushed SHA's hosted workflows are
queried independently, and their observed state is reported explicitly.

No new Lean theorem or kernel build is claimed. Proof cross-reviews are
recorded in `front_ah/INSTRUMENT_REVIEW.md`, `front_ah/REVIEW_BDE.md`, and
`front_cfg/REVIEW_AH.md`. They are same-model reviews, not external refereeing.
