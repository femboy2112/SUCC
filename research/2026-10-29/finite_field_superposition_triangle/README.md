# Finite-field → superposed-point triangle: source-authenticated BBP

**Research-only / DRAFT.** Parent SUCC [PR #383](https://github.com/femboy2112/SUCC/pull/383) at `e02933591e7b7486376acb9847e00fd01d9ae498`; siblings #368/#369/#370/#376/#382 are contextual references, not silently merged. The original four-pole source, `U_0=0`, claim registry, main and root workflows are unchanged.

## Structural correction

The proposed triangle is not the three constants `(harmonic numbers, inverse-golden, Euler–Mascheroni)` as unrelated vertices. It is a **three-operation diagram**:

1. Finite likelihood updates of the authentic positive four-pole source, retaining the conditional posterior field.
2. Coherent sum over all histories reaching one endpoint grade, producing a superposed finite point with a well-defined posterior.
3. Explicit observer/selection applied to that point (harmonic, Mellin–Gamma, golden fixed point, selected BBP circle character and literal integer carry).

Both update/endpoint orders have exact equalities. Nonlinear readouts and selected arithmetic must not be treated as automatically commuting with averaging. The positive triangle is a declared classical observation model, **not a physical quantum superposition or a stochastic model of π digits**.

## Hard results

- Original-source native clock `a_n=8n−7`, forcing `r(n)=R(a_n)`.
- Exact finite source-dependent path conservation, posterior update and cross-source triangle recursion.
- **Exact four-pole digamma bridge:** `A_(a,m)=R(a)^−1 Σ_d c_d/(a+d) [psi(m+1+(a+d)/8)−psi(1+(a+d)/8)]`; the Euler–Mascheroni reference cancels at finite depth. Native offsets are the original BBP 1/8, 4/8, 5/8, 6/8 with digamma dilation n→2n.
- Exact original-source harmonic sum: `A_n=H_n−Σ_(k=1)^n r(n+k)/(k r(n))`.
- Gamma–Poisson endpoint and Oily two-stage **marginal** fixed point `lambda²`, with the crucial joint-law distinction preserved.
- Derived `Omega_OM=lambda−gamma` at Gamma rank two, alongside a distinct mixed-grade constant `1+log 2−gamma−(1+2lambda)^−2`.
- **New calibrated BBP harmonic source first jet:** `A_n=1/2+log 2−49/(320n)+O(n^−2)`; Gamma-matched `Q_fake=15x` gives `+1/(32n)`. Their `−59/(320n)` difference comes from original `Q''(0)=−59`; a separate positive extra-pole mutant matches this first jet, so this is a discriminator, **not** full source identification.
- Exact deterministic two-step carry lift `kappa^(2)_n=16kappa_n+kappa_(n+1)` and grade-weight/selected-point/carry marks.

## Reproduce the focused receipts

```sh
cd research/2026-10-29/finite_field_superposition_triangle
python -m unittest -v test_finite_source_triangle.py
python independent_first_jet_oracle.py
python -m compileall -q finite_source_triangle.py test_finite_source_triangle.py independent_first_jet_oracle.py
```

Locally executed: 9/9 focused tests pass, independent exact SymPy oracle passes, compileall passes. Original source/test/oracle remote Git blob SHAs matched the executed files. **No full inherited SUCC root test/provenance/Lean suite, hosted exact-head CI or peer review was run here.**

Read [the exact derivation](RESEARCH.md), [claim statuses](CLAIMS.md), [validation receipts](VALIDATION.md) and [next proof task](NEXT.md).

**Boundary:** The coherent same-forcing seed `s=−π/16` shares the positive triangle and all source-only jets but has nonnormal selected phase. No signed `o(N)` estimate is established. **π base-16 normality and RH remain OPEN.**
