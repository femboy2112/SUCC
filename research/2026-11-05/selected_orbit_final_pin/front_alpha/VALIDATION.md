# Alpha validation

Executed in fresh worktree `SUCC-final-carry`, branch
`research/final-pin-carry-2026-11-05`, parent
`749931f0f357c60ef4e21879d96b0306999f428f`.

1. `python research/2026-11-05/selected_orbit_final_pin/front_alpha/carry_probe.py --write`
   completed exit 0. Exact Fraction states through n=1044; all independent
   forcing/circle paths, literal carries, direct macro carries, correction
   bounds, and rational interval controls passed. Receipt is finite evidence.
2. `python -m unittest discover -s research/2026-11-05/selected_orbit_final_pin/front_alpha -p 'test_*.py' -v`
   completed exit 0: 6 tests, 0 failures, 0.236 seconds. Includes deliberately
   chosen rational seeds forcing a correction and checking the reset/separation,
   so the zero corrections of the principal samples are not a vacuous check.
3. Receipt replay without `--write` is required before commit; see terminal
   receipt below. Full repository suite is coordinator-owned, not claimed here.

Original pressures at A=521 are `277968/271441`, `395520/271441`,
`2371584/271441` for m=1,2,3. All original correction counts in the registered
main epochs are zero. Coherent pressure is exactly 16,256,4096, also with zero
corrections. Period-11 pressure at A=521,m=3 is `101085184/271441`, again with
zero corrections. This is a successful falsifier of correction-only mixing,
not proof that the authentic orbit is normal.

The multiplier-2 source has one correction at A=125,m=3; every sign and cell
classification is exact. Coherent/periodic classifications use 24-term
rational Green-tail intervals; no floating point or pi oracle is involved.

Independent mathematical bearing: coordinator separately checked the reset
index, residue-class counting, and l-infinity pressure argument; this is an
independent agent derivation, not an external scholarly referee or Lean proof.
The periodic eventual-zero proof also follows directly from AC3: a correction
forces `x_(n+m)->0`, impossible for a finite nonintegral periodic completed
orbit bounded away from zero.

Final replay: `python research/2026-11-05/selected_orbit_final_pin/front_alpha/carry_probe.py`
completed exit 0 and exactly matched the saved JSON receipt. `py_compile` and
`git diff --check` completed exit 0. The predeclared A=37,m=3 calibration had
corrections at n=45 and n=73; the finite bound applies with L=1 and is correctly
weak. The two pressures remain equal (`4096/37`) because all sample labels are
distinct, illustrating why correction count and pressure change are different
observables.
