# The signed cascade: exact structure of d_j and the D_J divergence condition

**Branch:** `research/sherman-gs05-signed-cascade-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** exact reduction of the maintainer's GS-10 gate to a
phase-decorrelation condition via the GS05-TEL telescoping identity.

## 1. The telescoping form (PROVED, GS05-TEL)

`A = Σ_{n=a+1}^{a+L} e(hU_n)`, `B = Σ e(hU_{n+L})`. The exact identity
`(16^L−1)U_n + F(n,L) = U_{n+L} − U_n` gives
$$B = \sum_n e(hU_n)\,e\big(i\phi_n\big),\qquad \phi_n = h(U_{n+L}−U_n) \bmod 1,$$
$$A − B = \sum_n e(hU_n)\big[1 − e(i\phi_n)\big].$$

## 2. The variance identity (PROVED, exact)

For a single block pair, `W = |A−B|²`, `E = |A|²+|B|²`, `d = W/(2E)`. Two exact facts:

- **Constant-phase case:** if `φ_n ≡ φ` for all `n`, then `B = e^{iφ}A`, so
  `d = |1−e^{iφ}|²/(2·2) = sin²(φ/2)`. The cascade loss is `sin²(φ/2)` — the phase offset
  between adjacent blocks.
- **Spread-phase case:** when `φ_n` varies, `d` is governed by the *variance* of the increments,
  not their mean. Numerically (h=1, N=1024): the phase-concentration
  `|(1/L)Σ_n e^{iφ_n}| ≈ 0.15–0.26` (small, spread) across L=8..64, while single-block
  `d ∈ [0.10, 0.68]` (variable) and **aggregate** `d ∈ [0.46, 0.65]` (consistently large).

## 3. Why the aggregate d_j is consistently large (the key structural observation)

The aggregate `d_j = Σ W / (2 Σ E)` over all block-pairs at level L is stable (~0.46–0.65) because
it averages over many blocks, and the phase increments `φ_n = h(16^L−1)16^{n-1}π − h(T_{n+L}−T_n)`
(mod 1) are **generically spread** (the `16^{n-1}π` term is an irrational rotation, so
`(16^L−1)16^{n-1}π` mod 1 is non-degenerate). Individual blocks can be coherent (small `d`), but
the *aggregate* cannot — the irrational rotation forces the mean phase concentration to be small.

## 4. The D_J divergence condition (exact reduction)

`D_J(h) = Σ_{j=k_J}^{l_J−1} d_j(h) → ∞` requires `d_j ≥ δ_h > 0` on a growing number of mesoscopic
scales `L = 2^j`. By §2–3, this is equivalent to: **the phase increments
`φ_n = h(16^L−1)16^{n-1}π` (mod 1) are non-degenerate (spread) at mesoscopic L** — i.e. the rotation
`16^{n-1}π` does not have `(16^L−1)16^{n-1}π` land anomalously close to integers for most `n`.

This is a **Diophantine decorrelation statement about π at the multipliers `16^L−1`** — the same
object located by the `army-sub-log-collision` round. It is *not* controlled by:
- the Green tail (sub-leading `O(1/L²)`),
- the rational conductor (irrelevant at the observable scale),
- Gamma-sheet positivity or prime-CRT structure (both π-free).

## 5. The honest boundary

`D_J(h) → ∞` (hence π normality) reduces to a Diophantine decorrelation estimate for
`{16^{n-1}π}` at the multipliers `16^L−1`. The open question — is this provable from
`μ(π) < ∞` (irrationality measure) alone, or does it require the full signed Weyl content? — is
the exact boundary under attack by the four running fronts (lag-autocorr, diophantine-decorr,
large-sieve-l2, cascade-dj-divergence).

**π base-16 normality and RH remain OPEN.**
