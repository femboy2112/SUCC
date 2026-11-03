# Division, conjugation, and the Cayley transform: the exact obstruction

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** determine whether a Möbius/conformal automorphism
carries division `x↦1/x` to phase-conjugation `θ↦−θ` on the BBP orbit.

## 1. The three maps, made precise (PROVED, exact)

There are **three** distinct involutions floating in the discussion, and conflating them is the
obstruction:

| Chart | Involution | Formula | Effect on angle |
|---|---|---|---|
| **Circle** (unit circle `\|z\|=1`) | conjugation | `z ↦ 1/z = z̄` | `θ ↦ −θ` |
| **Line** (real axis `ℝ`) | division/inversion | `x ↦ 1/x` | `arctan`-complementary: `θ ↦ π/2 − θ` where `x=tan θ` |
| **Line** (real axis `ℝ`) | negation | `x ↦ −x` | `θ ↦ π − θ` (half-turn) |

## 2. The Cayley transform separates them (PROVED, verified exactly)

The Cayley map `w = −i(z−1)/(z+1)` carries the circle to the line. Computed exactly:

- Circle conjugation `z ↦ 1/z` (i.e. `θ ↦ −θ`) maps under Cayley to **line negation `w ↦ −w`**.
- Line division `x ↦ 1/x` is a **different** Möbius map (`w ↦ 1/w`), *not* the image of circle
  conjugation.

**Consequence:** "division `x↦1/x`" and "phase-conjugation `θ↦−θ`" are **not** the same map in
different charts — they are genuinely different involutions. The Cayley transform turns the former's
circle-avatar into **negation**, not into `1/x`. So there is **no chart** in which division is
conjugation.

## 3. What the BBP orbit actually needs (and why it fails)

The Weyl sum `S_N(h) = Σ e(h·16^{n-1}π)` needs **circle conjugation** `θ ↦ −θ` to pair terms into
conjugates (cancelling the imaginary part, leaving a real cos-sum). That is the map `z ↦ 1/z` on the
circle — equivalently, on the line (via Cayley), **negation** `w ↦ −w`.

For the orbit `{16^{n-1}π}` to be paired by conjugation, it would need to be **symmetric under
`θ ↦ −θ`**, i.e. closed under digitwise complement. Verified (exact hex digits): **no such
involution exists** — the digit-shift orbit of π contains no complementary pair.

## 4. The precise verdict on the "division" conjecture

- **Division `x↦1/x` is the wrong involution.** It pairs `θ ↦ π/2 − θ` (arctan-complementary),
  not `θ ↦ −θ` (conjugate). The Weyl sum needs the latter.
- **The correct involution (conjugation `θ↦−θ`) is line-negation, not line-division**, under the
  canonical circle↔line chart (Cayley).
- **The BBP orbit is not closed under conjugation** (no digit-complement pair exists). So no
  conformal automorphism — Möbius or otherwise — can carry "division" to a cancellation pairing,
  because the orbit is not symmetric under *any* of the three involutions.

## 5. The sharpened open question (what actually remains)

The obstruction is now **exact and provable**: the orbit `{16^{n-1}π}` is not invariant under
circle-conjugation, and division is not circle-conjugation in any chart. Therefore *pairing* cannot
produce the signed cancellation.

The only remaining route is **not** an involution of the orbit, but a **rigidity statement** that
forces the orbit to *approximate* conjugation-symmetry in the limit (the `o(N)` Weyl bound) —
which is exactly the Hochman–Shmerkin ×16×3 rigidity, or a genuinely new analytic transfer. The
"conformal automorphism carrying division to conjugation" does **not exist** for this orbit; that is
now proved.

**π base-16 normality and RH remain OPEN.**
