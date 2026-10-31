# COUNT-OUT validation / exact-source integrity

**Date:** 2026-10-30. Stacked research on Noether/radix PR #404 exact head `419cf7c280e7be11542ecbd6edef6c70fa7050e5` (Main XVI root `e18ba565ca540adb7edf3292f5593929e76d91c5`). All files additive; no original source or seed, production, archives, legacy theorem contracts, workflows or main modified.

## Executed local checks (real bytes)

- `python counting_quotient_probe.py` — **15/15 PASS**; exact Fraction tests for original four signed poles, unique bounded future correction, finite-vs-infinite boundary trilemma, integer carry cocycle and the artificial terminal-seam counterexample, 3-panel full-word grade/count quotient, original-selected intermediate carries, radix-16 collision enumerator through k=17, 34th-moment group algebra against full O(N²) pair formula, independent O(N) fast identity, h=1 source asymptotic, and selected coherent-orbit transfer-operator no-go.
- `python independent_oracle.py` — **PASS**, independent SymPy source polynomial simplification, exact Green conjugacy over finite horizons, separately implemented integer-frequency class enumeration at 34th moment (N=5), a high-precision mpmath original four-pole digamma source sum, source memory identity `(Σr_n−π)/15`, h=1 source dephasing A/S/B, and the complete next constant C with 60 dps. The independent implementations share the same model and are not external referees.
- `python -m compileall -q counting_quotient_probe.py independent_oracle.py` — **PASS**.
- Local source SHA-1 from `git hash-object`:
  - `counting_quotient_probe.py`: `011fec3ae724606e0ce852807e561fe5b8c51af5`
  - `independent_oracle.py`: `6bd91bd9424805c9e239922de94579cfc110ea6f`
  These are the expected blob SHA-1 values to independently compare with exact remote GitHub fetches after posting; do **not** claim byte identity until the remote check runs.

**Independent numerical results:** original source unweighted pole sum `S_R=3.38604761959719172193641883143841286...`; counting-subtracted source values `A_1≈0.3623667635505392644`, `S_1≈1.4975538144415172488`, `B_1≈0.1574172312886052698`, and limiting constant `C_1≈−981.1623446123234361`. The h=1 A_1 truncation at p≤20000 has a source-derived mathematical tail bound <`4.52e-14`; the sine-minus-linear tail is <`3.33e-23`. Numerical rounding cannot become a proof of the all-N formula.

## Repaired negative controls and source caveats

Read [RAW_TEST_LOGS.md](RAW_TEST_LOGS.md) for the initial failed numerical cancellation and terminal carry expectation and the repairs. The finite artificial future tail T_M=0 is **not** the infinite original future tail; its terminal carry is 16 rather than 15. The exact sign and factor in the 34th moment were tested by independent group-algebra, not guessed by fitting an asymptotic. The source-coherent control shares exactly the same Haar Ward residual but has nonnormal selected radix orbit.

**Not run:** full SUCC root provenance, complete repository unit tests, observer foundations, ordinal report probe, hosted exact-head GitHub CI, Lean, external mathematical review or independent check of SUCC historical source contract changes (none are changed here). Base-16 normality of π and RH remain OPEN. No physical gravitational/spacetime or entropy law inferred.

**Next verdict gate:** a non-fitted, bounded/marked counting quotient *preserving actual selected carry/phase chronology* and proving a genuinely source-and-zero-boundary-sensitive long-range signed bound. The new source-only Haar dephasing coefficient is not such a bound.
