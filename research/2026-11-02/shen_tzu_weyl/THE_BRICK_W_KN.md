# The actual bridge brick: W_{k,N}(h) — HMS-15's sufficient object

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** the *specific, concrete* lemma whose proof closes
π-normality via the maintainer's harmonic-mirror bridge — not a description of a wall, but a
named, well-posed, sufficient object.

## The brick (HMS-15, PROVED CONDITIONAL)

The maintainer's harmonic-mirror forge (`weyl-mirror-slowmesh`, `PI_HARMONIC_MIRROR_SUCC_FORGE.md`)
proves the **positive van der Corput bridge** (HM-vdC) with explicit constants, reducing π
base-16 normality to the single open statement **HM-open**:

$$\frac1N \sum_{k=1}^{K_N-1} w_{K_N,k}\,\big|W_{k,N}(h)\big| \to 0, \qquad
W_{k,N}(h) = \sum_{n=1}^{N-k} e\big(h(16^k-1)\,U_n\big),$$

with `K_N = \lfloor\log_{16}N\rfloor + 3\lfloor\log_{16}\log_{16}N\rfloor`, harmonic weights
`w_{K,k}`, and `U_n = 16^{n-1}π - T_n` the four-pole BBP orbit.

**Every other term in HM-vdC is exact/proved**: the diagonal `H_K^{(2)}/H_K → 0`, the forcing-error
budget `88|h|/1575 · 16^K/(N H_K K^3) → 0`, and the positive Fejér mixture. The *only* unknown is
the harmonic-weighted average of `|W_{k,N}(h)|`.

## Why this is the right brick (not a wall)

`W_{k,N}(h)` is the Weyl sum at frequency `h(16^k−1)`. It is:
- **concrete** (exact rational orbit, computable),
- **sufficient** (HMS-15 already proves `HM-open ⟹ π normal`),
- **alive** (empirically `|W_{k,N}(h)|/N ≈ 0.02–0.07`, oscillating, no clean decay yet — but NOT
  provably stuck, unlike the five dead routes),
- **arithmetically structured** — the multiplier `16^k−1 = 15·(16^{k-1}+…+1)` is highly composite,
  which is a handle the bare `16^{n-1}π` rotation lacks.

## The concrete attack

`W_{k,N}(h) = Σ_n e(h(16^k−1)(16^{n-1}π − T_n))`. The phase is
`h(16^k−1)16^{n-1}π − h(16^k−1)T_n`. Two parts:
1. The **rotation** `e(h(16^k−1)16^{n-1}π)` — the Diophantine object at multiplier `16^k−1`.
2. The **tail** `e(−h(16^k−1)T_n)` — but now the multiplier `16^k−1` *amplifies* the tail by
   `16^k`, which is a **different** regime from the fixed-`h` tail (the tail is no longer
   `O(1/n²)`-negligible; it's `O(16^k/n²)`).

This is the genuinely new feature: the harmonic mirror *trades* the fixed-frequency Weyl gate for
a **k-weighted family** of Weyl sums at the composite multipliers `16^k−1`, where the tail is
amplified. Whether this helps or hurts is exactly the open question — and it is *not* settled by
any of the five dead routes.

## What this means

The bridge is not "a wall to describe." It is a **named, sufficient, open object** `W_{k,N}(h)`
with a proved conditional theorem (HMS-15) already in place. Proving `HM-open` — the harmonic-
weighted average of `|W_{k,N}(h)|` vanishes — is the single brick that closes π-normality.

**π base-16 normality and RH remain OPEN.**
