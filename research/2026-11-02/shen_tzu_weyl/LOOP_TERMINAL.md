# The loop terminal: all three brick vectors settled

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel. **Scope:** fold the three brick-front results into the steelman→crucify→improve
loop, and state the terminal.

## The three brick vectors, final verdicts

### Brick 1 — composite multiplier `16^k−1` (CRUCIFIED, inert)
`16^k−1 = 15·Σ16^i = (4^k−1)(4^k+1) = ∏_{d|k}Φ_d(16)` is a rich divisibility tower, always odd,
`gcd(16^{n-1},16^k−1)=1`. But π is transcendental, so **no integer factor can rationalize the
phase** — the tower is a re-parametrization, not a constraint. The only exact identity
`(16^k−1)16^{n-1}=16^{n+k-1}−16^{n-1}` reproduces the self-similar covariance (inert).

### Brick 2 — amplified-tail regime (PARTIAL — one positive bound)
`W_{k,N}(h) = R + (amplified-tail term)`, with the **uniform bound**
`|W − R| = O(|h|·16^k·Σ_T)` where `R = Σ e(h(16^k−1)16^{n-1}π)` is the pure rotation. This
*separates* the tail from the rotation with an explicit `16^k` amplification factor. It is a
**genuine, if coarse, bound** — the amplified tail is `O(|h|·16^k)` in total, which is *large*
(not `o(N)`) and confirms the tail is **less** controlled (amplified), not a saving. **The
bound is honest but does not close HM-open** (the `16^k` factor is the wrong size).

### Brick 3 — k-weighted second moment (CRUCIFIED, same wall)
`W_{k,N}(h) = S_{N−k}(h(16^k−1))` — literally the same Weyl sum re-indexed. **No Parseval
identity over `k`** exists, so the second moment is a convex combination of squares of the same
sum, reducing to the same pointwise wall. The harmonic `1/k` weight renormalizes; it doesn't cancel.

## The loop terminal (honest)

All three brick vectors are settled. Two are **provably inert** (composite multiplier, k-second
moment). One produced a **positive but insufficient** bound (amplified-tail separation, with the
wrong-size `16^k` factor). The bridge brick `W_{k,N}(h)` is, structurally, **the same Weyl sum**
at the ladder frequency `h(16^k−1)` — self-similar under the ×16 dynamics, exactly as the
van-der-Corput / Ward rounds proved.

## The campaign's cleanest terminal statement

The loop has converged. The problem, in its final canonical form, is:

$$\pi \text{ base-16 normal} \iff \{16^{n-1}\pi\}\text{ is }T_{16}\text{-generic for Lebesgue}$$

equivalently the Birkhoff averages of `e(hx)` along the ×16 orbit converge to 0 for the specific
point `{π}`. This is the *definition* of normality, reached via every route:

- **Birkhoff/ergodic** (path geometry),
- **Weyl** (signed cancellation `S_N(h)=o(N)`),
- **collision/entropy** (`C_A = o(log A)`, the weaker L² gate),
- **rigidity** (×16×3, needs (A)+(B)),
- **harmonic-mirror** (HMS-15's `W_{k,N}(h)`).

All five are **equivalent** (proved across the campaign), and all five reduce to the same
specific-point genericity. Every decomposition (BBP digit, prime-CRT, Gamma, van der Corput,
large sieve, division/conjugation, composite multiplier, k-second moment) is a **re-encoding or
symmetry** of that one object, now proved.

## What is NOT concluded

- π is **not** proven normal.
- π is **not** proven non-normal.
- π-normality is **not** proven independent of ZFC (no such result, and none claimed).

The loop's honest terminal is: **the problem is a specific-point Birkhoff-genericity statement,
equivalent to normality by definition, with a complete map of every known route (all re-encodings),
and no known technique reaches a specific named point's genericity under an expanding map.**

**π base-16 normality and RH remain OPEN.**
