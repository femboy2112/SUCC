# Validation — original BBP Gamma-prime pigeonhole

**Source base:** merged main a673ec95dfac4ef6a61c60222be8b615fd08535d. No imported source modules or historical contracts modified. Local interpreter is Python 3 (Fraction exact, no Monte Carlo/π digits). Full native GitHub Actions status checked only at the exact posted commit; do not infer CI success from isolated instruments.

## Actually executed

- Local research test: \`python -m unittest -v test_gamma_pigeonhole\` => **11/11 PASS**, 0 errors/skips, ~0.05s. Development probes p=17,41,73,89,97,113,137 and extra p=233,313 for formula stress. 
- \`python receipt_probe.py --write FINITE_RECEIPT.json\` then \`--verify\` => **GAMMA_PIGEONHOLE_SOURCE_PIN_RECEIPT_VERIFIED**. Each recorded SHA256 covers an exact-Fraction tuple of real Gamma rational enclosures, full source cofactor, original integer state and candidate identity. Decimal widths are display only, never proof.
- **Preregistered holdouts:** \`PREREGISTRATION.md\` was committed at \`25cd0262c1bc102b644b4e2fb218f21c3c735882\` *before executing* p=193,241,257,281,337,353. Independent holdout evaluator \`heldout_probe.py\` used the rational polynomial source expression, independent four-term Euler bounds, newborn prime-state address, and the neighboring mutated source. **6/6 PASSED**. SHA256 of canonical exact rational case array: \`845730b09ea18e4eaa30645aa948d98f9e753be2428fa8e587f36da9acbeaf29\`.
- Full finite proof certificate for p>=41 comes from one-dimensional rational inequalities in PROOFS.md, not a finite test grid. Exact p=41 bound \(C_pW_p=110229570/115856201<1\), plus a globally monotone p-dependent expression.
- Distinct computational pathways: original four separate source rational terms vs independently simplified polynomial formula; integer LCM original orbit vs independent canonical SUCC original source implementation (the latter checked **only when** \`test_gamma_pigeonhole_repo_bridge.py\` runs in a native checkout). All numerical calculations use one deterministic exact-rational arithmetic model, not independent human review.

**Not yet run locally:** repository-native \`tests/test_gamma_pigeonhole_repo_bridge.py\` (requires the full SUCC Python package and checkout), full \`unittest discover\` 11k+ suite, source provenance/observer/ordinal probes, hosted CI and new Lean proofs. Do not claim those results until independently observed. Frozen source unchanged. **π base-16 normality, source-selected J=o(K), signed Weyl and RH remain OPEN.**
