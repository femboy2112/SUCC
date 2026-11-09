# Evidence and validation for Gamma-matrix source perturbation

**Baseline:** draft #567 pinned at `40f2fca0d6101c3391fea9174399b0bf63c55e72`; full original SUCC source, U0=0, all prime CRT residue and real carry archive frozen.

- The `observational_succ` module uses the production import `from observational_succ.duck_bbp import forcing`. In the isolated local workspace this was provided by a small test-only exact polynomial API-compatible fixture matching the unchanged canonical main module. It is **not uploaded** and must never replace `duck_bbp.py`.
- All 15 focused Python unittest methods pass after one explicit test assertion repair: an excessively sharp **estimate of the intentionally loose analytical series remainder** initially failed at 10 terms; test now correctly uses 24 terms. The mathematical series and coefficients were not modified. A separate q-Euler input test revealed an mp conversion issue for exact Fraction inputs; the API was repaired to preserve the fraction exactly before numeric evaluation and the source identities were unchanged.
- Independent SymPy expansion of `-Σ w_i ψ(a_i)` reproduces the elementary `(15/64)γ+π/log` form; 70-digit MP digamma and explicit forms agree, and a finite N=10,000 four-pole rational sum differs by approximately -1.7773634e-5, consistent with the sharp asymptotic `−91/(512N)`.
- Exact source partial fractions `n r(n)=Σ w_i/(n−1+a_i)` verified for independent n. γ-coordinate recursion tested against exact rational `n r(n)` at six timestamps; matched-leading mutation shift checked independently against finite exact rational terms.
- Exact nilpotent model `P*=H+uvᵀ/64`: matrix identity P²=H, X²=0 and Γ-response `γ_BBP I−c₁X` hold algebraically. Numerical matrix implementation validated at that known exact oracle.
- Previously certified 131,072 π hexadecimal digits were reused as **CALIBRATION**, with first/second/full matrix-Gamma norm diagnostics and the certified source SHA checked. No new π digit calculation or blind future holdout is claimed.
- mpmath precision is scoped with workdps and no ambient precision mutation; matrix computations use NumPy double and **do not constitute interval certified values**. The analytic tail bound is proved for exact series coefficients and ideal input X, not rounded implementation error.

**Not claimed:** full native 12k+ suite, global root provenance/observer/ordinal, new Lean kernel certificate, exact-head hosted CI success before inspection, peer review, π base-16 one-/two-/all-digit normality or a source-selected signed 225-mode estimate.
