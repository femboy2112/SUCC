# The ×3-rigidity frontier (WB-10): a genuinely different route to π normality

**Branch:** `research/x3-rigidity-frontier-2026-11-02` (off `origin/main`). **Date:** 2026-11-02.

This attacks the **Hochman–Shmerkin ×16–×3 rigidity route** (WB-10 in the maintainer's
`weyl_borg_fusion` dossier), which is a *genuinely different* route from the stuck signed-Weyl
gate: instead of `S_N(h)=o(N)`, it needs (A) `T_3`-invariance and (B) positive lower dimension,
each attackable by different tools.

## 0. The clean reduction (PROVED, this round)

The completed orbit `x_n = {16^{n-1}π}` is **exactly** the ×16 trajectory of the single point
`x_1 = {π}`:
$$ x_{n+1} = \{16 x_n\} = T_{16}(x_n), \qquad x_1 = \{\pi\}. $$
Consequently the empirical measures `μ_N = N^{-1}Σ δ_{x_n}` are the orbit measures of one point
under `T_{16}`, and (since `T_n → 0` is a summable perturbation, `Σ T_n = B < 1/32`) the rational
orbit `{U_n}` has the *same* weak-* accumulation. **`T_{16}`-invariance of every limit is free**
(exact, via `r(n+1)→0` and Cesàro, as WB-10 shows).

So the entire rigidity route reduces to **two obligations for the ×16 orbit of the single point
`{π}`**:
- **(A) real ×3 defect** `D_N(h) = N^{-1}Σ[e(3hU_n) − e(hU_n)] → 0` for every fixed `h` — equivalently
  `T_3`-invariance of every limit;
- **(B) positive lower dimension** `dim_* μ > 0` for every limit.

Hochman–Shmerkin (Ann. Math. 175 (2012), Thm 10.4) then forces every limit = Haar ⟹ π base-16 normal.
**(A)+(B) is another equivalent criterion, not a free lunch** — but it is attackable by *different*
tools (rigidity/dimension vs. Fourier cancellation).

## 1. What is genuinely different here (and hence worth attacking)

- **(A)** is a *difference* `S_N(3h) − S_N(h)`, strictly weaker than `S_N(h)→0`: it asks that the
  `3h` and `h` modes *agree in the limit*, not that either vanishes.
- **(B)** is a *geometric* statement (Frostman/non-concentration) about the orbit of `{π}` under
  `×16`, which is *not* a Fourier statement at all.

## 2. Empirical signature (finite, correct precision)

`|D_N(h)|` is small and decaying: h=1: 0.057→0.022; h=3: 0.038→0.005 (N=500→2000), consistent with
`T_3`-invariance. (Finite; not a proof.)

## 3. The key question for (B): does finite irrationality measure of π force positive ×16-orbit dimension?

`π` has `μ(π) < 15/2` (Zeilberger–Zudilin), finite, so `π` is not Liouville. The natural hope:
finite irrationality measure ⟹ the `×16` orbit is non-concentrated. **This is NOT implied for
free** — positive Hausdorff dimension of a `×m` orbit is stronger than non-Liouville, and needs a
Furstenberg/Hochman–Shmerkin-type input. The honest sub-targets, in increasing strength:
1. **Spacing lower bound** (provable?): `min_{n<m≤N} ‖x_n − x_m‖` grows polynomially in `1/N` —
   i.e. the orbit has no exponentially-close pairs. This is a *strictly weaker* statement than
   `dim_* > 0`, and might be provable from the explicit rational structure of `U_n`.
2. **Frostman bound** `μ_N(I) ≤ C |I|^s` for some `s>0` (implies `dim_* ≥ s`).
3. **Full `dim_* = 1`** (equivalent to normality — the summit, not attacked directly).

## 4. Status

`T_{16}`-invariance is free; the route is *equivalent* (not easier) in the sense that normality ⟺
(A)+(B). The genuinely-new leverage is that (A) and (B) are each *weaker* and *different* objects
than the stuck `S_N(h)=o(N)`, so a proof of either — even partial — is progress. π normality and RH
remain **OPEN**.

## 5. Literature reconnaissance (this round)

- **Hochman–Shmerkin, Ann. Math. 175 (2012), Thm 10.4** is the load-bearing rigidity theorem:
  `T_m × T_n`-invariant + `dim_* > 0` ⟹ Lebesgue (for `m,n` multiplicatively independent).
- **Hochman, "On the dimension of αβ-sets" (arXiv:2410.19640, 2024)** is directly adjacent
  (dimension of `{α^n β^m}` digit-type sets), confirming this is active, deep territory.
- **Key honest finding:** positive lower dimension of the `×16` orbit of a *specific* irrational
  `{π}` is NOT implied by finite irrationality measure `μ(π)<15/2` alone — it is a deep statement,
  and (B) is therefore NOT a shortcut. The rigidity route (A)+(B) is *equivalent* to normality,
  but its two obligations are *different* (rigidity/dimension vs. Fourier) and the spacing bound is
  the most concrete provable sub-result.

**Conclusion: the ×3 rigidity route is worth pursuing for its genuinely different methods, but its
two obligations are each as hard as normality in their own way. The cleanest provable contribution
is a spacing/non-concentration lower bound (a strictly weaker, source-derived statement), which the
spacing front attacks.**
