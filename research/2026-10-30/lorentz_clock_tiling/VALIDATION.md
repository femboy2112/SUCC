# Validation and provenance — Lorentz-clock tiling

- Research parent: SUCC PR #392 at `00b073fb9adedcda91cc499540add10dfcfabc66`, ultimately Main XVI at `e18ba565ca540adb7edf3292f5593929e76d91c5`.
- Source: exactly original four-pole rational `R(a)`; no source edits; zero-seed is kept as an external arithmetic mark and is **not** randomized by this observer.
- Locally executed standalone standard-library source probe: **12/12 tests PASS**, including exact finite original-source probabilities, hypergeometric/Vandermonde, normalized boost group, golden quadratic invariant, q2 parity non-invariance, original source first jet and tail-inclusive finite TV. Initial too-strict finite-jet test threshold `1/(20n²)` failed; changed to the observational `1/(8n²)` after examining exact `n²` residuals (approx 0.078, hence not less than 0.05). That finite threshold is **not claimed as a proved uniform analytic bound**.
- Independently authored SymPy oracle: PASS; checks golden matrix arithmetic, twenty-five full coefficient identities, parity covariance exact rational at balanced and golden frames, Fourier non-invariance, finite-original polynomial transform independently of word summation, and 59-jet algebra.
- Proven mathematical inequalities are derived in `LORENTZ_CLOCK_TILING.md`, not inferred from finite tests.
- Not executed: full 9k+ SUCC suite, native AGENTS required provenance/observer/ordinal gates, hosted exact-head CI, Lean, independent mathematical peer review. Branch should remain DRAFT.
- No physical Lorentz covariance or selected signed o(N) estimate is claimed. Historical proof statuses remain unchanged.
