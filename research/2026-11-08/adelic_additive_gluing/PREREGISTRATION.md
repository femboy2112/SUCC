# Preregistered exact prime-real phase gluing holdouts — 2026-11-08

**Parent:** SUCC draft PR #556 head `f999bdd8ebd90c80e06a1484e128d1dda31d2fb6`.
**Frozen authentic source:** `r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)`, `U_0=0`.

This file is committed **before evaluating the new held-out epochs**. Earlier epochs A=32,80,100 are pre-seen in #556 and serve as calibration only.

## Held-out cases

1. `A=192, p=457`, h in {1,3}; p is 1 mod8 and the four prime births are at 58,229,286,343, so all later births are inside [192,384).
2. `A=320, p=769`, h in {1,3}; p is 1 mod8 and the four births are at 97,385,481,577, so later births are inside [320,640).

All calculations must use exact frozen BBP rational states and p-primary residues. Float/MP complex phase diagnostics are explicitly **not** proof certificates.

## Predeclared measurements

- Exact verification of `e(h U_n)=e_p(h C_p(n)) e(h(U_n-C_p(n)/p))` and complete original finite-place CRT phase equality.
- Compute `W_A(h)`, p-marginal mean, true complementary mean, complementary total variation, and the signed contribution of the real/prime product. Preserve all complex signs, chronological ordering and four genuine birth positions.
- Compare each real mean with a no-pi-oracle rational epoch-dependent coherent seed constructed from exact four-pole finite terms. This control retains p-primary source labels. It is **not** a fixed rational seed and is not a counterexample to pi normality.
- Compute critical source-only holonomy `Theta_(A,k)`, k=ceil(log_16 A), and same-pi coboundary contrast using exact Fractions and proved rational enclosures. No heat kernel or independently sampled Haar source.

## Acceptance criteria and interpretation

- **PASS** means exact p-history and CRT equalities hold with no exceptions; the recorded complex numbers are computed with independently reduced exact rational arguments and replay under declared MP precision.
- **FAIL** is any disagreement, source mutation, unaccounted p² pole, or an unrecorded precision/algorithm dependency; preserve it.
- **AMBIGUOUS** is a float discrepancy without interval certification; do not promote.
- A small observed `W_A` or measured signed covariance at these two finite epochs is not evidence of an all-A saving. The missing theorem remains `W_A(h)->0` for every fixed h !=0, equivalently the #554 signed prime/complement lag gate.
