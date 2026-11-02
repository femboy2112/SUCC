# ×3 rigidity route — consolidated verdict

**Branch:** `research/x3-rigidity-frontier-2026-11-02`. **Date:** 2026-11-02.

Three independent fronts (×3 defect, dimension lower bound, spacing) plus main-thread analysis
attack the **Hochman–Shmerkin ×16–×3 rigidity route** (WB-10): prove `T_16 × T_3`-invariance with
positive lower dimension, hence Lebesgue, hence π base-16 normal. This is a genuinely *different*
route from the stuck `S_N(h)=o(N)` Weyl gate.

## The clean reduction (PROVED)

The completed orbit `x_n = {16^{n-1}π}` is **exactly** the ×16 trajectory of `x_1 = {π}`:
`x_{n+1} = {16 x_n}`. Hence:
- **`T_16`-invariance of every weak-* limit is FREE** (exact: `r(n+1)→0` + Cesàro).
- The rational orbit `{U_n} = {x_n − T_n}` has the same accumulation (`ΣT_n = B < 1/32` summable).

## Obligation (A) — ×3 defect (PROVED structure + firewall)

`D_N(h) = N^{-1}Σ[e(3hU_n) − e(hU_n)]` satisfies the **exact identity**
`D_N(h) = W_N(3h) − W_N(h) + O_h(1/N)` (explicit constant `≤ 2π(|3h|+|h|)B/N`), so
`D_N(h)→0 ⟺ ×3-invariance of every limit — **strictly weaker** than `S_N(h)=o(N)`.

**Firewall (PROVED, decisive):** the coherent counterseed (`U_n = −T_n`, all phases →1) also has
`D_N(h)→0`. So **(A) is necessary-but-NOT-sufficient** — it does not discriminate the non-normal
counterseed. This *confirms* Hochman–Shmerkin's requirement of **both** (A) and (B), and cleanly
identifies (B) as the leg that kills the counterseed.

**Proposed (not proved):** the Fejér-weighted form `D_N(h) = 2i·N^{-1}Σ e(2hU_n)sin(2πhU_n)` has
self-similarity under `h↦16h` that the bare sum lacks — a *different* handle, currently conjecture.

## Obligation (B) — positive lower dimension (PROVED negative / essentially open)

1. **`μ(x)<∞ ⟹ dim_*(×16-orbit) > 0` is FALSE** (explicit counterexample mechanism: finite
   irrationality measure does not control mutual orbit spacings in the Frostman sense).
2. **Spacing: only the exponential `e^{-12N}` bound is PROVED** (from the conductor `log Q_n=6n+o(n)`);
   the polynomial `N^{-2}` spacing is *empirical*, and spacing does **not** imply positive dimension
   (Liouville-type orbits can have polynomial spacing yet `dim_*=0`).
3. **(B) requires Furstenberg/Hochman–Shmerkin input not satisfied here** — it is deep, not a shortcut.

## Bottom line

The ×3 rigidity route is a **valid, genuinely-different, and *equivalent* (not easier) decomposition**
of π-normality into two obligations:
- **(A)** `T_3`-invariance — *strictly weaker* than Weyl, and now exactly characterized (and shown
  necessary-not-sufficient).
- **(B)** positive lower dimension — the *deep*, separating obligation (kills the counterseed), not
  reachable by conductor/irrationality-measure arithmetic.

The route's value is **conceptual and structural**: it names (A) and (B) as *independent, weaker*
sub-targets with *different* tools (rigidity/dimension vs. Fourier), even though (B) remains as deep
as normality itself. The cleanest *proved* contributions this round are (i) the exact defect identity
`D_N = W_N(3h) − W_N(h) + O_h(1/N)`, (ii) the counterseed firewall showing (A) is necessary-not-
sufficient, and (iii) the refutation of the hoped-for "finite irrationality measure ⟹ positive
dimension" implication.

π base-16 normality and RH remain **OPEN**.
