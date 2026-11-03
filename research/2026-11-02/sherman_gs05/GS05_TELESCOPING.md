# The GS-05 telescoping identity: the signed cross-block phase is a lag-L autocorrelation

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** exact simplification of the maintainer's decisive open
gate GS-05 (the signed cross-block reinforcement `K_j`).

## 1. The clean identity (PROVED, exact)

The maintainer's GS-05 cross-block difference is:
$$A − B = \sum_{n=a+1}^{a+L} e(hU_n)\left[1 − e\!\left(h((16^L−1)U_n + F(n,L))\right)\right],$$
where `F(n,L)` is the four-pole Gamma lag satisfying `U_{n+L} = 16^L U_n + F(n,L)` (GS-01).

**Claim (GS05-TEL, PROVED).** `(16^L−1)U_n + F(n,L) = U_{n+L} − U_n` exactly.

*Proof.* `F(n,L) = U_{n+L} − 16^L U_n` (definition of the lag). Then
`(16^L−1)U_n + F(n,L) = (16^L−1)U_n + U_{n+L} − 16^L U_n = U_{n+L} − U_n`. ∎

**Consequence.** The GS-05 signed difference **telescopes** to a lag-L first difference:

$$\boxed{A − B = \sum_{n=a+1}^{a+L}\left[e(hU_n) − e(hU_{n+L})\right].}$$

Hence the signed cross-block reinforcement is an **autocorrelation at lag L**:
$$K_j = \operatorname{Re}\sum_{\text{pairs}} A\overline B
= \sum_{n,m=a+1}^{a+L}\cos\left(2\pi h(U_n − U_{m+L})\right).$$

## 2. The phase is the Diophantine rotation at multiplier `16^L−1`

Using the Green tail `U_j = 16^{j-1}π − T_j` (summable, `T_j = O(1/j²)`):
$$h(U_{n+L} − U_n) = h(16^L−1)16^{n-1}π \;-\; h(T_{n+L} − T_n).$$

The **dominant term** is `h(16^L−1)16^{n-1}π`, the Diophantine rotation of π at the sparse
multiplier `16^L−1`; the tail correction `h(T_{n+L}−T_n) = O(h/L²)` is sub-leading.

## 3. What this means for GS-05

- `d_j = W_j/(2E_j) = 1/2 − K_j/E_j`. Empirically (exact rational, N=1024, h=1):
  `d_j ∈ [0.46, 0.65]`, i.e. `K_j/E_j` is small (near 0, sign-oscillating) — the cross-term does
  **not** reinforce, so the Haar cascade loses `≈ 1/2` of energy per mesoscopic level.
- The target `K_j ≤ (1/2 − δ_h)E_j` (δ_h > 0) is equivalent to `d_j ≥ δ_h`, i.e. the *phase
  decorrelation* `e(hU_{n+L}) ≈ −e(hU_n)` on average — a **signed anti-correlation** statement.
- The exact phase structure shows this anti-correlation is governed by the Diophantine rotation
  `‖(16^L−1)16^{n-1}π‖`, the *same* object located by the previous round (`army-sub-log-collision`).

## 4. The sharpened gate

GS-10 (`D_J(h)→∞`) reduces to: prove the lag-L autocorrelation `K_j` is `≤ (1/2−δ_h)E_j` on a
growing number of mesoscopic scales `L = 2^j`. Via GS05-TEL this is a statement about the **pair
correlation of `{16^{n-1}π}` at lags `L` with the multiplier `16^L−1`** — a Diophantine
decorrelation estimate, not a source-only or positive-kernel fact.

**π base-16 normality and RH remain OPEN.**
