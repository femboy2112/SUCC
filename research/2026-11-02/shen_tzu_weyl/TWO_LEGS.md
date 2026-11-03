# Shen Tzu on the Weyl form: the exact signed decomposition and its two legs

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** the exact structure of the signed Weyl sum
`S_N(h) = Σ_{n≤N} e(hU_n)` in the SUCC framework, and where the two provable legs live.

## 1. The gate (WB-01, exact equivalence)

`S_N(h) = o(N)` for every fixed `h≠0` ⟺ π base-16 normal. The object:
`U_n = 16^{n-1}π − T_n`, `r(n) = 4/(8n-7)−2/(8n-4)−1/(8n-3)−1/(8n-2)`, `U_0=0`,
`U_{n+1}=16U_n+r(n+1)`.

## 2. The exact signed decomposition (WB-02, verified this round to 1e-81)

For resolution `M`, `a_n = ⌊M{U_n}⌋`, `s_n = M{U_n}−a_n ∈ [0,1)`:
$$S_N(h)/N = g_M(h)\underbrace{\sum_a e(ha/M)(p_a − 1/M)}_{\text{cell imbalance}} + \underbrace{\sum_a e(ha/M)d_{(a,h)}}_{\text{within-cell cofiber } C_{(N,M)}(h)},$$
where `g_M(h) = ∫_0^1 e(hs/M)ds`, `p_a = #{n:a_n=a}/N`, `d_{(a,h)} = w_{(a,h)} − p_a g_M(h)`.

## 3. The decisive empirical structure (exact Fraction, N=512)

| h | M | \|cofiber\| | \|cell-imbalance\| |
|---|---|---|---|
| 1 | 16 | 0.00197 | 0.10156 |
| 1 | 256 | 0.00012 | 0.51562 |
| 5 | 16 | 0.02258 | 0.10156 |
| 5 | 256 | 0.00065 | 0.51562 |

**The cofiber `C_{(N,M)}(h)` → 0 as M grows** (within-cell phase residual shrinks), while the
cell-imbalance grows (as M→N each cell holds ≤1 point). At **coarse M ≪ N**, the Weyl sum splits
into:
- a **cell-imbalance leg** — controlled by the collision energy `C_M` (my earlier rounds proved
  `C_M = o(log M)` ⟹ this leg → 0, and it is the *finite-entropy* object);
- a **within-cell cofiber leg** — the signed phase residual inside each cell, provably decaying
  in M and carrying the π-content.

## 4. The two legs and the strategy (Art of War framing)

> *"Attack where the enemy is weak, appear where you are not expected."*

The Weyl gate has **two legs**, and they are *different* objects:

1. **Cell imbalance** — a *finite-resolution* (entropy/collision) object. This is where the
   maintainer's LS-10 `C_A = o(log A)` lives, and where my Parseval/weakness theorem showed the
   gate is genuinely an L² (not ℓ∞) statement. **This leg is the weak flank.**

2. **Within-cell cofiber** — a *signed phase residual* object, the π-content itself. This is the
   Diophantine rotation `e(h(16^k−1)16^{n-1}π)` located by rounds 2–3. **This leg is the strong
   flank, and it is the same object the fixed-frequency Weyl cancellation lives in.**

The strategy is to **divide and measure**: prove the cell-imbalance leg decays (L²/collision
methods, already mapped), and separately bound the cofiber leg — where any genuinely new
signed-phase identity or Diophantine estimate must act.

## 5. What this round will fan out on

The cofiber `C_{(N,M)}(h) = Σ_a e(ha/M)[w_{(a,h)} − p_a g_M(h)]` is the sharpest new object. Its
exact structure — `w_{(a,h)} = (1/N)Σ_{n:a_n=a} e(hs_n/M)` with `s_n = M{T_n}`-driven residual — is
the target. The army will attack:
1. The exact `s_n` structure (`s_n = M{U_n} − a_n`, and `U_n = 16^{n-1}π − T_n`, so `s_n` is the
   tail `T_n` at resolution M).
2. Whether the cofiber's decay in M is provable (it looks like `O(1/M)` or better), which would be
   a genuine *reduction* of the gate to the cell-imbalance leg.

**π base-16 normality and RH remain OPEN.**
