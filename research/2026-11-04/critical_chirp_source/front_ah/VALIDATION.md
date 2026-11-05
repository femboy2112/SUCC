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

## Additional paper review: AH-05

The coordinator's explicit finite F4 constant was independently checked and
appended as AH-05 in PROOFS.md. The audit checked `j=0`, `j>=A`, `A=1`, empty
and singleton retained intervals, negative h, all shifted source indices, and
the geometric coefficient. It proves the seed-uniform finite retrieval bound
with explicit sufficient constant `pi/32` and no upper frequency cap. This is
**quantified inherited retrieval, not new cancellation**. It is a paper-proof
review; no additional test execution or formal-kernel authority is claimed.
No shared code or native tests were changed for this addition.
