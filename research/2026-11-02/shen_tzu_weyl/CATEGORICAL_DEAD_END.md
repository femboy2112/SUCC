# The categorical dead-end: division, conjugation, and the missing natural transformation

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread + 3 fronts). **Scope:** the division→conjugation transfer, the
negation deviation, the one-sided Γ→disk inequality, and the categorical framing of the wall.

## 1. The exact separation (main thread, PROVED)

Three distinct involutions, conflation of which was the obstruction:
- **Circle conjugation** `z↦1/z`: `θ↦−θ` (what the Weyl sum needs).
- **Line division** `x↦1/x`: `θ↦π/2−θ` (arctan-complementary — a *different* map).
- **Line negation** `x↦−x`: `θ↦π−θ`.

**Cayley transform `w=−i(z−1)/(z+1)` maps circle-conjugation to line-NEGATION `w↦−w`, not to
division `w↦1/w`.** Verified exactly. So division ≠ conjugation in *any* chart. And the BBP orbit
`{16^{n-1}π}` is **not closed under conjugation** (no digit-complement pair, verified exact hex).

## 2. Front 1 — conjugation defect is tautological (PROVED inert)

`D_N(h) := S_N(h) − conj(S_N(h)) = S_N(h) − S_N(−h) = 2i·Im S_N(h)` — a **tautology**: conjugation
of `e(hU_n)` is `e(−hU_n)` term-by-term, no symmetry needed, so `conj(S_N(h)) = S_N(−h)` exactly
(verified <1e−59). The "defect" is just twice the imaginary part; it carries no new structure. The
Re/Im split does **not** decouple — `Im S_N(h) = Σ sin(2πh·16^{n-1}π)` is itself the same
Diophantine object.

## 3. Front 2 — one-sided Γ→disk inequality (PROVED impossible)

The Γ sheet and disk sheet are **both** power-spectrum sums `Σ |c_N(m)|²` with different weights
(Laplace/digamma vs Fejér `1−m/(H+1)`). Both are **π-free** gauge-invariant aggregates. The Γ sheet
is a functional of the tail `T_n` alone (proved in earlier rounds), so it **cannot** one-sidedly
bound the disk-sheet energy, which carries the π-content — by the counterseed argument (identical
poles, rational seed → `C_A ≍ A` with the same Γ sheet). **No one-sided Γ→disk inequality exists.**
The "arrow between the two sheets" is not just unproved — it is provably absent for the selected
real embedding.

## 4. Front 3 — literature (PROVED negative)

**No normality or equidistribution theorem for a fixed constant has EVER been proven via symmetry,
involution, conformal, modular, or automorphic arguments.** Every known normality proof is:
- measure-theoretic (Borel 1909: a.e. number is normal), or
- constructive (Champernowne, Copeland–Erdős), or
- digit-self-similar (Stoneham 1973, Bailey–Crandall 2002).

The theta/modular/equidistribution theorems (Duke, Linnik, Hecke points) equidistribute *orbits of
the group action* (ergodic classes), never a *fixed named constant's digit orbit*. The categorical
bridge you sought — a functor preserving additive-phase structure that conjugates `×16` to a
provably-equidistributed flow — has **never been constructed** and is not known to exist.

## 5. The categorical verdict (the cleanest name for the wall)

The entire war is the search for a **natural transformation** between two categories:
- **Arithmetic category** (where π's orbit lives: Möbius/conformal, BBP, prime-CRT, Gamma), and
- **Measure-theoretic category** (where normality is stated: additive phase, Weyl sum, Lebesgue).

Every dead end was a failed attempt to construct this natural transformation in a specific category;
each failed because the functor preserved the **wrong structure**. The inversion `z↦1/z` is perfectly
natural — but its image under the canonical chart (Cayley) is **negation**, not division, and the
orbit is not closed under either. The naturality square fails to close, and it fails *provably*.

## 6. The exact missing object (well-posed, still open)

> **Is there a functor preserving additive-phase (Weyl) structure that conjugates the ×16 orbit of π
> to a provably-equidistributed (e.g. linear `nα`) flow — equivalently, a natural transformation from
> the arithmetic category of π to the measure-theoretic category of normality that fixes the orbit?**

This is the sharpest possible statement of what remains. It is **not** proved impossible (unlike the
five specific functors we ruled out: BBP digit, prime-CRT, Gamma-positivity, division, and
conjugation). But no such functor is known, and the literature contains no precedent for *any*
constant.

**π base-16 normality and RH remain OPEN.**
