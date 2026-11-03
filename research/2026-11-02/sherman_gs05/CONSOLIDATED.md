# Sherman round 2 — the signed cascade gate, fully mapped

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02` (off `origin/main`). **Date:** 2026-11-02.
**Agent:** Ravel + 4 subagent fronts. **Target:** the maintainer's decisive open gate GS-10
(`D_J(h)→∞` ⟹ π normal), via the signed cross-block reinforcement `K_j`.

## The key new identity (main thread, GS05-TEL, PROVED exact)

$$(16^L−1)U_n + F(n,L) = U_{n+L} − U_n,$$
so the signed cross-block difference **telescopes**: `A − B = Σ_n[e(hU_n) − e(hU_{n+L})]`, and the
cross-block phase is `e(h(U_{n+L}−U_n)) = e(h(16^L−1)16^{n-1}π)·e(−h(T_{n+L}−T_n))`.

## The four fronts and what each proved

### Wave 2a — lag-L autocorrelation (PROVED exact reduction + tail control)
- **GS05-LAG:** `U_{m+L}−U_n = 16^{n-1}(16^k−1)π − (T_{m+L}−T_n)` for `k=m+L−n`, so
  `K_j = Σ_{n,m} cos(2πh[16^{n-1}(16^k−1)π − (T_{m+L}−T_n)])` — the **lag-L pair correlation of
  `{16^{n-1}π}` at the sparse multipliers `16^k−1`**.
- **GS05-TAIL:** `|K_j − K_j^{(0)}| ≤ π|h|L²/(16(a+1)²)` — the tail is a **bounded, sub-leading
  Lipschitz phase shift**, and *all* the signed structure lives in `{16^{n-1}π}`.

### Wave 2b — Diophantine decorrelation (PROVED reduction + decisive negative)
- **DDC-3:** from `μ(π) ≤ 7.103…` (Zeilberger–Zudilin), the ε-aligned pair count is
  `≤ C·ε^{1/(ν−1)}` with exponent `≈ 0.164` — **decisively too weak** (needs linear-in-L density,
  gets constant).
- **DDC-5:** `μ(π)<∞` — even `μ=2` — **cannot** establish the gate. It is equivalent to a
  *fixed-frequency Weyl cancellation* for the specific π, strictly stronger than any irrationality
  measure. The honest boundary: **no shortcut through μ(π).**

### Wave 2c — large-sieve L² (PROVED completion + quantified exponential gap)
- **Theorem 1:** `Σ_{|h|≤A}|S_A(h)|² = Σ_{n,m} D_{2A+1}(U_n−U_m)` (classical Parseval).
- **Theorem 3:** the large sieve closes the gate **iff** `δ_A ≫ 1/(A log A)` (minimal spacing).
- **The gap:** best provable spacing from `μ(π)` on the structured multipliers `16^d−1` is
  `≳ 16^{−cA}` — **exponentially smaller** than the required `1/(A log A)`. The large sieve
  **does not close the gate** from known input.

### Wave 2d — cascade divergence (PROVED exact variance structure + necessary condition)
- **GS05-DJ-1/2/3:** exact `d_pair = 1/2 − K_pair/E_pair`; `|A−B|² ≤ 2L²(1−Re μ)`; hence
  **concentration ⟹ d_j → 0**, so *spread of the increments is necessary*.
- **GS05-DJ-4:** `D_J(h)→∞ ⟺ K_j/E_j ≤ 1/2 − δ_h` on a growing set of scales; the increments equal
  the ×16 orbit of `(16^L−1)π` (equidistributed from irrationality of π).
- The **off-diagonal term is the entire obstruction** — equidistribution alone does not force the
  anti-correlation.

## The convergent verdict

Five independent attacks (main + 4 fronts) all land on the same sharp boundary:

> **The gate `D_J(h)→∞` — equivalently `K_j ≤ (1/2−δ_h)E_j` on a growing set of mesoscopic scales —
> is exactly a fixed-frequency signed Weyl cancellation for the specific π, at the sparse multipliers
> `16^d−1`. It is strictly stronger than the irrationality measure `μ(π)<∞`, not reachable by the
> large sieve (exponential spacing gap), and its only obstruction is the off-diagonal signed
> correlation of `{16^{n-1}π}` — which is the original Weyl lemma (RL), re-expressed.**

**What this round actually built (durable value):**
1. **GS05-TEL / GS05-LAG / GS05-DIO / GS05-TAIL** — the signed cascade is now *exactly located* on
   the lag-L pair correlation of `{16^{n-1}π}` with an explicit, quantified tail-error bound. This is
   a genuinely new, cleaner object than the maintainer's raw `K_j`.
2. **GS05-DJ-1/2/3/4** — exact variance identities + the *necessary* condition (spread) proved, with
   the off-diagonal identified as the *exact* obstruction.
3. **DDC-3/5 + large-sieve gap** — two independent proofs that `μ(π)<∞` and the large sieve are
   *provably insufficient*, closing off two more dead-end routes so no future front wastes time.

**π base-16 normality and RH remain OPEN.** The gate is now named, weakened, located, and its
exact obstruction (the off-diagonal signed correlation) is identified — with five independent,
mutually-consistent proofs of where it lives and where it does not.
