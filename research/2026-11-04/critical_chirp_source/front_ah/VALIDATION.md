# Front A/H validation and authority

Executed in the isolated child worktree of
`c9dfcdf057c4870f113e898464e4821c2ff5fedf`:

```
python -m unittest discover -s research/2026-11-04/critical_chirp_source/front_ah -p 'test_*.py' -v
```

Result: **6 tests PASS**, 0 failures/errors; 18 preregistered exact rational
`(n,k)` holdout rows, two distinct formulas for derivatives of the four-pole
forcing, strict infinite-tail interval containment, and a dropped-pole
changed-forcing negative control detected.

```
python research/2026-11-04/critical_chirp_source/front_ah/derivative_probe.py --write research/2026-11-04/critical_chirp_source/front_ah/DERIVATIVE_RECEIPT.json
python research/2026-11-04/critical_chirp_source/front_ah/derivative_probe.py --verify research/2026-11-04/critical_chirp_source/front_ah/DERIVATIVE_RECEIPT.json
```

Result: `TAIL_DERIVATIVE_RECEIPT_VERIFIED`, exit 0. The JSON retains exact
Fraction interval endpoints and an SHA-256 of all raw row records. The
holdout set was declared in PREREGISTRATION.md before these executions.

The quantified derivative theorem and uniform discrete coherent asymptotic
are **paper derivations** in PROOFS.md. Finite checks do not prove either
universal statement. No new Lean/kernel proof or external independent
mathematical referee is claimed. The two derivative implementations share
BBP source provenance. Full native suite and hosted CI are owned by the
coordinator and are not certified by this front's focused results.
