# OPERATION HANNIBAL — Phase 0 hostile audit + load-bearing attack state

**Branch:** `research/hannibal-weyl-encirclement-2026-11-02` (off `1478b51c`).
**Date:** 2026-11-02. **Agent:** Ravel.

## Phase 0 — hostile audit of WM-01..WM-08: NO DEFECTS FOUND (all correct)

1. **WM-01 (reciprocal≠conjugation):** CONFIRMED. `1/z=conj(z)` on the circle is anti-
   holomorphic; on the projective line `C(1/t)=−1/C(t)` (reciprocal ↦ `x↦1/2−x`); conjugate
   pairs sum to `2cos`, not 0. Matches my `DIVISION_CONJUGATION.md` (Cayley maps conjugation
   to negation, not division). **Correct.**
2. **WM-02 (Möbius centralizer = 15 rotations only):** CONFIRMED. `M=c·z` or `c/z` with
   `c^15=1`; common reflection needs `2(r(2)−r(3))∈ℤ`, but `=133558/765765∈(0,1)`. Only
   identity fixes marked seed `U_0=0`. **Correct** — and correctly scoped: rules out *fixed*
   source-preserving mirrors, not approximate/statistical/time-reindexed ones.
3. **WM-03 (odd denominators forbid exact antiphase):** CONFIRMED. All `U_n` odd reduced
   denominator ⇒ `h(U_n−U_m)≠1/2 mod 1`, no exact two-term cancellation; three odd roots still
   sum to 0 (multiway polygons possible). Matches my CRT/SIGNED_CRT round. **Correct.**
4. **WM-04 (`T_*μ=μ` + `J_*μ=μ` ⇒ Haar, `J(x)=1/16−x`):** CONFIRMED (elementary: `TJ=J_0T`,
   `J_0=−x`, `JJ_0=R_{1/16}`, then radix frequency reduction kills all nonconstant Fourier
   coefficients). **Correct sufficient condition; does NOT claim J-invariance of the orbit.**
5. **WM-05 (uniform determinant bound only for `16∤h`; Ward for `h=16^v g`):** CONFIRMED.
   `|sin(πh/16)|≥1/8` for nonzero residue; never divides by zero. `B_N(h)→0 ∀h ⟺ π normal`.
   **Correct conditioned criterion, premise OPEN.**
6. **WM-06 (hereditary Fejér needs POINTWISE nonnegativity, not just PSD):** CONFIRMED. The
   rank-one `e(h(x−y))` is PSD but a subset can have positive quadratic sum while the full sum
   vanishes — tested explicitly. **Correct.**
7. **WM-07 (arbitrarily slow mesh ⇒ `E=o(log m)`, not `o(log A)`; explicit log-schedule):**
   CONFIRMED. `E_(A,m_A)=o(log log A)` for `m_A=2^⌊log2 j⌋` is the sufficient premise; the
   all-prefix passage is handled by WM-06's uniform partial-epoch bound (no power-scale
   gluing). **Correct; premise OPEN.**
8. **WM-08 (permutation certificate `|mean e(hU)| ≤ π·c_h(τ)`):** CONFIRMED. Valid for any
   permutation; feasible half-rank cyclic match is not claimed optimal; exact parity forces
   positive finite costs but they may tend 0. **Correct.**

**Audit verdict:** all eight WM lemmas are mathematically sound and correctly scoped. No defect
to repair. The single load-bearing OPEN premise is `E_(A,m_A) = o(log log A)`.

## Load-bearing attack: E_(A,m_A) structure

- `E_A = (m/A²)Σv_i² = m/A + 2m/A²·#(same-bin pairs)`.
- Collision at mesh `m~log A` ⟺ `‖U_n−U_t‖ < 1/m = 1/log A`; the tail `T_n−T_t = O(1/A²) ≪ 1/log A`
  is **negligible**, so the collision is purely `‖16^{t-1}(16^d−1)π‖ < 1/log A`.
- Irrationality measure `μ(π)≤7.1` gives `‖Mπ‖ ≥ 16^{−14A} ≪ 1/log A` — **no control** (as in
  every prior round).
- **Empirical:** `E_A → 1` exactly (1.007 at A=1024, 1.003 at A=2048) — the **Poisson/uniform**
  signature, no anomalous clustering at the coarse mesh.

## The precise discriminator (the only live question)

`E_A = o(log log A)` is a **second-moment (collision-energy)** statement at a *logarithmic* mesh,
genuinely weaker than the pointwise Weyl sup (this is the Parseval/weakness insight from the
`shen-tzu` rounds: L² ≠ ℓ∞). The proof would be: **the phases `{16^{t-1}(16^d−1)π}` do not
cluster worse than Poisson at mesh `1/log A`** — i.e. their collision energy is `O(1)`.

This is the **same Diophantine non-clustering** as every prior round, but now stated at the
*coarsest* scale (log-mesh) where it is a *weakest* (second-moment) form. It remains governed by
`‖(16^d−1)16^{t-1}π‖`, for which no known theorem gives a polynomial bound.

## Verdict (honest, per handoff acceptance)

**No new theorem proved.** The strongest established deliverable is: (a) the full Phase-0
confirmation that WM-01..WM-08 are correct and correctly scoped; (b) the exact reduction of the
open premise `E_(A,m_A)=o(log log A)` to a second-moment Diophantine non-clustering at the
logarithmic mesh; (c) the empirical `E_A→1` (Poisson) receipt.

**Next discriminator (precise):** does any *L²/energy* method (large sieve at the structured
moduli, second-moment orthogonality, collision-energy via the exact CRT decomposition) bound
`E_(A,m_A)=o(log log A)` at the logarithmic mesh — *without* the pointwise sup? This is the one
place the campaign found genuine weakness (L² weaker than ℓ∞), and it is the exact target the
maintainer's WM-07 sufficient theorem isolates.

**π base-16 normality and RH remain OPEN.**
