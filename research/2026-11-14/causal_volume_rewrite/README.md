# SUCC Causal-Volume Rewrite Algebra (BBP × Oily × Gamma)

Research-only, additive child of [draft PR #634](https://github.com/femboy2112/SUCC/pull/634). The user's question is whether expanding every BBP variable into its source-attached causal volume and cancelling common factors yields reusable inference rules. **Yes: a typed Mellin-polynomial/radix normal form with exact zero origin and explicit observer nonlinearity boundaries.**

Start at [THEOREMS.md](THEOREMS.md) (CV-01..CV-07), then [VALIDATION.md](VALIDATION.md). Executable oracle: `observational_succ/causal_volume_rewrite.py`, new exact tests: `tests/test_causal_volume_rewrite.py`, independent SymPy/mpmath check: `independent_sympy_oracle.py`.

Most useful consequences: original four signed BBP poles cancel pointwise to the **same** positive Oily kernel **and** original two-register Oily resolvent (already in GG-05, now normalized systematically); all finite original U_n arise as Mellin-volume finite differences with no altered seed; complete positivity of Green moments yields a Gamma(k+2) causal-difference ladder; an explicit source-specific moving-Mellin complex-frequency bound reaches `(1+iλ)^−2` with rigorous O((1+|λ|)/m) certificate; one zero-seeded, positive Gamma(2) **different** source completes to rational 1/2, so positivity isn't a normality mechanism; a source-perturbed family retains the *same* π completion and finitely many source moments but changes later forcing.

The unproved gate remains the exact zero-seeded chronological signed Weyl estimate. The module is not a proof of pi normality, RH, genuine physical Gamma wave propagation or stochastic independence. Historical canonical BBP/origin and archived source contracts remain untouched.
