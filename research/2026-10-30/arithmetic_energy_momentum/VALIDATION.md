# Validation — Original source golden mass-shell research

**Source passport.** Parent draft #393 exact `903fdb77ba92f14c620d7c0ab50229a2823b2ac9`; Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. Historical BBP forcing and `U_0=0` untouched; additive research files only. Local tests do not certify full repo or physical validity.

**Executed local instruments**

- `python -m unittest -v energy_momentum_probe.py`: **11/11 PASS** with exact stdlib `Fraction`. One initial strict-positivity test mistakenly demanded that all trailing zero coefficients of a padded polynomial be strictly positive; corrected to nonnegative with at least one positive coefficient. Mathematical theorem and positive coefficients unchanged; the initial failure and repair are retained in this record.
- `python independent_symbolic_oracle.py`: **PASS**, independent factorized original-source `C/D` derivation using SymPy. Verified all-a strict positivity of rank-bounding and derivative polynomials; source mass endpoints and source-59 correction; native-vs-fake finite Pascal rank jets; exact arithmetic lattice metric; golden negative dual mark and boosted source jet.
- `python independent_numerical_oracle.py`: **PASS**, high-precision independent direct quadratures of `e^{-ax}Q(x)` and moments at `a=1,9,17,73,257`. Verified the analytic source mass, variance, covariance shell and golden marked Laplace evaluation at 65 dps. This is a numerical holdout, not a universal interval proof.

**Nonclaim:** Full SUCC root >9k+ unittest suite, provenance/observer/ordinal gates, hosted CI on this new branch, Lean kernel checking, independent blind mathematical review and any selected zero-seed signed asymptotic were **not** run or certified. They remain separate pre-integration requirements.

**Refutations and boundaries.** Independently reset panels have zero cross-covariance despite unchanged mean counts; projective fixed-total clock boosts alter the mass shell; the positive source symmetry survives coherent same-four-pole seed `−π/16`; and dual real Laplace probe covariance does not preserve unit-modulus Fourier characters. These are decisive negative tests for overbroad implications.
