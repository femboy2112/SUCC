# Launchpad execution and proof authority

**Verified research baseline:** draft parent SUCC PR407, exact head `5f05181339ea97a56999ca8b8ab10a2009c6c84d`, stacked over PR405. Main baseline at preparation: `e18ba565ca540adb7edf3292f5593929e76d91c5`. All added files are research-only. Original source coefficients and U0=0 untouched.

## Executed locally

- Inherited cylinder_collision exact regression suite: **18/18 PASS**, independently executed against the locally present parent source snapshot.
- New moving_certificate focused regression suite: **9/9 PASS** with the parent cylinder_probe present on PYTHONPATH.
- Standalone six-case finite certificate calibration: **6/6 PASS**. Controls: base-16 de Bruijn order2 and order3, constant-zero path, deterministic seeded pseudo-uniform digits, biased digits, periodic small-support digit cycle.
- Exact counts and Q_m are Python Fraction; the displayed logarithm/Pinsker upper bound uses floating point and is *not* an interval-certified transcendental computation.
- The new finite-horizon MS-01 and one-depth MS-02 have a complete local mathematical derivation; numerical passes are independent calibration, not proof authority.
- The source-directed MS-03 estimate is still **OPEN**; no signed CRT saving, normality proof, RH proof or external scholarly novelty is claimed.

## Replay after checkout

```bash
export PYTHONPATH=research/2026-10-30/deepseek_cylinder_fanout:research/2026-10-30/cylinder_tiling_collision
python -m unittest discover -s research/2026-10-30/deepseek_cylinder_fanout -p 'test_*.py' -v
python research/2026-10-30/deepseek_cylinder_fanout/moving_certificate.py
python -m unittest discover -s research/2026-10-30/cylinder_tiling_collision -p 'test_*.py' -v
```

**Not executed at launch:** whole SUCC 10,008-test root suite on this child head, new Lean formalization, project-wide provenance/observer/ordinal gates on this child, hosted exact-head CI, or external blind mathematical review. DeepSeek must run and distinguish these gates; inherited parent passing is not an equivalent result.

A failed comparison, missing Python dependency or unaudited baseline must be retained in raw receipts, not silently relabeled as a theorem defect or success.