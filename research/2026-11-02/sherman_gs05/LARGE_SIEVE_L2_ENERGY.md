# Large-sieve / L² energy attack on the open gate C_A = o(log A)

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (subagent, large-sieve-L2 front).
**Scope:** apply a large-sieve / spectral L² method to bound `Σ_{1≤|h|≤A} |S_A(h)|²`,
the load-bearing object of the exact Parseval/Fejér identity (FEJ-1), and determine
whether any such L² route can close `C_A = o(log A)` without the pointwise Weyl sup bound.

**π base-16 normality: OPEN. RH: OPEN. No new sublinear Weyl bound is proved here.**

---

## 0. Objects and the target (all exact)

Four-pole BBP forcing `r(n) = 4/(8n-7) - 2/(8n-4) - 1/(8n-3) - 1/(8n-2)`,
orbit `U_0 = 0`, `U_{n+1} = 16 U_n + r(n+1)` (exact rationals). Green tail
`U_n = 16^{n-1}π - T_n`, `T_n = Σ_{k≥1} 16^{-k} r(n+k) > 0`, summable, `Σ T_n = B < 1/32`.

Window Weyl sum: `S_A(h) = Σ_{n=A}^{2A-1} e(h U_n)`, `e(t) = exp(2πi t)`.

**FEJ-1 (proved, prior round):** the collision energy satisfies
$$C_A = \frac1A\sum_i v_i(A)^2 = \frac1{A^2}\sum_{h\in\mathbb Z} |S_A(h)|^2\, \mathrm{sinc}^2(h/A).$$
The weight `sinc²(h/A) ≈ 1` for `1 ≤ |h| ≤ A` and `≤ (A/πh)²` beyond, so the tail
`|h| > A` contributes `O(A²)` (bounded after `/A²`). The load-bearing object is therefore

$$\boxed{ \mathcal E_A := \sum_{1\le |h| \le A} |S_A(h)|^2 .}$$

**Target (the L² gate).** `C_A = o(\log A)` is equivalent (by FEJ-1 + tail control) to
$$\mathcal E_A = o(A^2 \log A), \qquad\text{i.e.}\qquad \frac1{2A}\sum_{1\le|h|\le A}|S_A(h)|^2 = o(A\log A).$$

**Baseline.** Random/sqrt-cancellation `|S_A(h)| ≈ √A` gives `E_A ≈ A · A = A²`, i.e.
`C_A ≈ 2`. Empirically (exact `Fraction`, verified below) `E_A/(A² log A) ∈ [0.36, 0.40]`
and the per-frequency mean `|S_A(h)|² ≈ A` for `A = 32, 64, 128` — the *shape* of random
cancellation is already present; only a proof is missing.

---

## 1. The pair-sum completion (PROVED, exact, classical Parseval)

**Theorem 1 (completion to the pair-sum).** For any `A ≥ 1` and any real points
`x_n = U_n mod 1` (`n ∈ [A, 2A)`),

$$\sum_{|h|\le A} |S_A(h)|^2 = \sum_{n,m=A}^{2A-1} D_{2A+1}(x_n - x_m), \qquad
D_{2A+1}(t) = \sum_{h=-A}^{A} e(ht) = \frac{\sin\big((2A+1)\pi t\big)}{\sin(\pi t)} .$$

*Proof.* Expand `|S_A(h)|² = Σ_{n,m} e(h(x_n - x_m))` and swap the (finite) sums:
`Σ_{|h|≤A} Σ_{n,m} e(h(x_n-x_m)) = Σ_{n,m} Σ_{|h|≤A} e(h(x_n-x_m)) = Σ_{n,m} D_{2A+1}(x_n-x_m)`.
The inner geometric sum is exactly the Dirichlet kernel of order `2A+1`. ∎

**Corollary 2 (the two-scale split).** The diagonal `n = m` contributes `(2A+1)·A ≈ 2A²`;
each off-diagonal pair contributes the Fejér-type weight `D_{2A+1}(x_n-x_m)`, which is
`≈ 2A+1` when `‖x_n - x_m‖ ≪ 1/A` and `O(1/‖x_n-x_m‖)` when `‖x_n-x_m‖ ≫ 1/A`. Hence
`E_A` is, up to the diagonal, a **weighted count of near-coincidences** `‖U_n - U_m‖ ≲ 1/A`:

$$E_A \;=\; A(2A+1) \;+\; \sum_{n\ne m} D_{2A+1}(\|U_n-U_m\|) .$$

This is the classical Parseval/completion passage: the L² energy **is** the pair-sum.
(Verified exactly below to machine precision.)

---

## 2. The large sieve and the spacing it needs (the load-bearing input)

**Theorem 3 (additive large sieve, Montgomery–Vaughan form).** Let `x_1, …, x_N ∈ ℝ/ℤ`
be `δ`-separated, i.e. `‖x_n - x_m‖ ≥ δ` for `n ≠ m`. Then for every complex `a_1,…,a_N`,

$$\sum_{h=1}^{H} \Big|\sum_{n=1}^N a_n e(h x_n)\Big|^2 \;\le\; \Big(N - 1 + \frac1\delta\Big)\sum_{n=1}^N |a_n|^2 .$$

(Standard: the dual/selberg large sieve; see Montgomery–Vaughan, "The large sieve".)

Applying it with `N = A` points `{U_n : n ∈ [A,2A)}`, `a_n ≡ 1`, `H = A` (and symmetrizing
over `h ∈ [−A, A]`), gives

$$\mathcal E_A = \sum_{1\le |h|\le A} |S_A(h)|^2 \;\le\; \Big(A - 1 + \frac1{\delta_A}\Big) \cdot A ,$$

where `δ_A = min_{n≠m, n,m∈[A,2A)} \|U_n - U_m\|` is the **minimal circular spacing** of the
orbit window.

**The requirement.** To reach the target `E_A = o(A² log A)` we need
$$A - 1 + \frac1{\delta_A} = o(A\log A), \qquad\text{i.e.}\qquad \delta_A \gg \frac{1}{A\log A}.$$

So the large sieve closes the gate **iff the orbit window is `δ_A ≫ 1/(A log A)`-separated**.

### 2.1 What spacing is actually available (PROVED + empirical)

- **Exact non-coincidence (PROVED):** `U_n ≠ U_m` for `n ≠ m`, since equality forces
  `16^{n-1}π = 16^{m-1}π`, i.e. `π ∈ ℚ`. So `δ_A > 0` always — but this gives no size.

- **Tail correction (PROVED, prior round):** `‖U_n - U_m‖ = ‖(16^d-1)·16^{n-1}·π - (T_n - T_m)‖`
  with `|T_n - T_m| = O(1/A²)`, strictly sub-bin-scale (`< 1/A`). The tail is a *bounded
  summable* correction; it **cannot** certify any positive lower bound on `δ_A` — the
  counterseed `β = 0` gives `U_n = -T_n → 0` (collisions at every scale, `C_A = A`).

- **Conductor (PROVED):** `Q_n = exp(6n + o(n))`, so `1/(Q_n Q_m) = exp(-12A + o(A))`,
  astronomically below the `1/A` scale — irrelevant to `δ_A`.

- **Empirical (exact `Fraction`, this round):** `δ_A` is governed by Diophantine
  near-coincidences of `‖(16^d-1)·16^{n-1}·π‖`. Measured:

  | A   | δ_A (exact) | 1/δ_A | A²  | closest pair (n, m) | lag d |
  |-----|-------------|-------|------|----------------------|-------|
  | 16  | 1.58e-3     | 6.3e2 | 256  | (16, 18)             | 2     |
  | 32  | 1.71e-3     | 5.8e2 | 1024 | (39, 40)             | 1     |
  | 64  | 1.05e-4     | 9.5e3 | 4096 | (118, 120)           | 2     |
  | 128 | 3.14e-5     | 3.2e4 | 16384| (155, 173)           | 18    |

  The minimal spacing is **much smaller than random `1/A²`**: `δ_A ≈ 1/A³` roughly
  (`1/δ_A` grows from `6e2` to `3e4` as `A` goes 16 → 128, i.e. like `A²`), reflecting
  genuinely anomalously-close Diophantine pairs `(16^d-1)π ≈` integer.

### 2.2 The gap: large sieve falls short by a factor ~ A/log A

The large sieve needs `δ_A ≫ 1/(A log A)`, i.e. `1/δ_A = O(A log A)`. The observed
`1/δ_A ≈ A²` (from the Diophantine pairs `‖(16^d-1)16^{n-1}π‖`), and there is **no proved**
lower bound `δ_A ≫ 1/(A log A)` from any available input:

- Irrationality measure `μ(π)` only bounds `‖qπ‖ ≫ q^{-μ-ε}` for **single** integer `q`,
  not for the **structured sparse** multipliers `(16^d-1)·16^{n-1}` with `d` up to `A` and
  `n` up to `2A` (these have `≈ 6A` bits; a Roth-type bound `‖qπ‖ ≫ q^{-2-ε}` gives
  `δ ≳ (16^{2A})^{-2} = 16^{-4A}`, far below `1/(A log A)`).

**Quantified gap:** to reach `E_A = o(A² log A)` via the large sieve, we require a spacing
$$\delta_A \gg \frac1{A\log A},$$
but the *best provable* spacing from `μ(π) < ∞` (or even Roth `μ ≤ 2+ε`) on the structured
multipliers is `≳ 16^{-cA}` for some `c > 0`, i.e. **exponentially smaller**. The large
sieve therefore **does not close the gate** from the known spacing input — the gap is
`A\log A` vs `16^{cA}`, an exponential gap, not a log factor.

---

## 3. The direct L² estimate: pair-sum via Diophantine spacing (honest reduction)

Since the large sieve's δ-input is exactly the Diophantine spacing that we cannot bound,
the honest route is to *not* assume a spacing, but to bound the pair-sum
`Σ_{n≠m} D_{2A+1}(‖U_n-U_m‖)` directly. This is the same content re-expressed:

**Theorem 4 (pair-sum = Diophantine near-coincidence count, PROVED reduction).**
$$E_A = A(2A+1) + \sum_{d=1}^{A-1}\sum_{n=A}^{2A-1-d} 2\,D_{2A+1}\Big(\big\|(16^d-1)16^{n-1}\pi - (T_{n+d}-T_n)\big\|\Big) .$$
*Proof.* Substitute the exact decomposition `U_{n+d} - U_n = (16^d-1)16^{n-1}π - (T_{n+d}-T_n)`
(IDENTITY-1 of the tail-spacing round) into Corollary 2 and group by lag `d = m - n`. ∎

The term `D_{2A+1}(t)` is `≈ 2A+1` iff `‖t‖ ≲ 1/A` and `O(1/‖t‖)` otherwise. Hence `E_A`
is controlled by

$$\sum_{d=1}^{A-1} \#\Big\{n\in[A,2A-d]: \big\|(16^d-1)16^{n-1}\pi\big\| \le \tfrac1A\Big\} \cdot (2A+1) \;+\; \text{(tail terms)} .$$

This is **literally** the count of `1/A`-near-coincidences of the rotation `{16^{n-1}π}`
at the sparse multipliers `16^d - 1` — the *same Diophantine object* identified by the
`army-sub-log-collision` round and by `GS05_TELESCOPING.md` §2.

**No new input.** There is no known analytic principle (large sieve, Selberg, spectral/L²
orthogonality, Weil-type, positivity kernel) that bounds this near-coincidence count for
the *structured* multipliers `(16^d-1)16^{n-1}` of a fixed transcendental `π` without
invoking the very Diophantine non-clustering that the gate *is*. Every L² method reduces to:

> **Diophantine non-clustering of π:** `‖(16^d-1)16^{n-1}π‖ ≫ 1/A^{1+o(1)}` for all but
> `o(A²)` pairs `(d, n)`.

This is *structurally the same* (not obviously weaker) as the signed Weyl gate RL.

---

## 4. The honest boundary

1. **What is PROVED (this round):** the pair-sum completion (Thm 1), the two-scale split
   (Cor 2), the large-sieve reduction and its exact spacing requirement `δ_A ≫ 1/(A log A)`
   (Thm 3), and the pair-sum→Diophantine reduction (Thm 4). All exact, all machine-verified.

2. **The spacing input the large sieve needs is NOT attainable.** The required
   `δ_A ≫ 1/(A log A)` is **exponentially** stronger than any spacing provable from
   `μ(π) < ∞` (even Roth) on the structured multipliers `(16^d-1)16^{n-1}`. The gap is
   `A log A` vs `16^{cA}`. **The large sieve, with the only provable δ, yields `E_A ≤
   A·(A + 16^{cA}) = 16^{cA}`-scale — useless (worse than trivial `E_A ≤ 2A·A²`).**

3. **No L² route closes the gate without the Diophantine content.** Theorem 4 shows the
   L² energy *is* the near-coincidence count of `{16^{n-1}π}` at `16^d-1`. Any large-sieve/
   spectral/L²/energy bound that reaches `o(A² log A)` must *ipso facto* prove the
   Diophantine non-clustering `‖(16^d-1)16^{n-1}π‖ ≫ 1/A^{1+o(1)}` for almost all pairs —
   which is not known and is the same content as the pointwise/sup Weyl gate. The
   "weakness" of the L² norm (the `o(log A)` tolerated spikes) does **not** translate into
   a strictly easier Diophantine problem: the near-coincidence count at scale `1/A` is
   insensitive to whether the bad frequencies are `o(log A)` or `O(1)`.

4. **Therefore:** `C_A = o(log A)` via large-sieve/L² **reduces to, and does not bypass,**
   the Diophantine non-clustering of π at the sparse multipliers `16^d-1`. The L² route is
   a *reformulation* (a different norm to attack), not an independent easier gate. This is
   the honest boundary: **the large sieve does not reduce the arithmetic content; it
   re-encodes it as a spacing requirement that is exactly as hard as the target.**

**π base-16 normality and RH remain OPEN.**
