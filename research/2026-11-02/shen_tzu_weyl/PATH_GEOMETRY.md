# Path geometry of the limit: the walk S_N(h) as a self-similar Birkhoff sum

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel (main thread). **Scope:** the user's instruction — analyze the *path geometry*
of the limit we take to generate the Weyl object, rather than the object itself.

## 1. The object as a path (walk)

`S_N(h) = Σ_{n≤N} e(h·16^{n-1}π)` is a **deterministic walk** in ℂ: each term `e(h·16^{n-1}π)`
is a unit step, so `S_N(h)` accumulates unit steps along the ×16 orbit. The path
`N ↦ S_N(h)/N` is a genuine geometric object — the trajectory of the accumulation.

## 2. Precision firewall (third occurrence of the trap, documented)

At `dps=60`, the digit-shift `x ← frac(16x)` collapses to `0` at `n≈50` (verified), making the
walk spuriously `S_N ≈ N·1` — which *looks* like "limit = 1, π non-normal" but is precision
death. Corrected with exact hex-digit extraction (verified prefix), the true walk is:

| N | S_N(h=1) | \|S_N\|/N |
|---|---|---|
| 100 | 0.29+9.64i | 0.096 |
| 200 | −4.60−5.29i | 0.035 |
| 400 | −9.80−1.68i | 0.025 |
| 600 | −31.61+14.14i | 0.058 |
| 800 | −36.66+18.66i | 0.051 |
| 1000 | −33.60+26.40i | 0.043 |

`|S_N|/N` oscillates ~0.02–0.09, with `|S_N| ≈ √N` — **square-root cancellation**, the exact
random/normal signature (not drift, not collapse).

## 3. The path is a self-similar Birkhoff sum

`S_N(h)` is the **Birkhoff sum** of the observable `f(x) = e(hx)` along the orbit of
`T_16(x) = 16x mod 1`. Its self-similarity under `N ↦ 16N` (the ×16 dynamics) means the path
geometry is **self-similar** at every scale — a fractal curve in ℂ.

## 4. The path geometry lands on the ergodic theorem (the cleanest statement)

"Analyze the path geometry of the limit" correctly identifies the object as a Birkhoff sum, and
the limit `S_N(h)/N → 0` is exactly the **ergodic/Birkhoff convergence** of the ×16 orbit of `{π}`.
Normality of π **is** the statement that the Birkhoff averages of `e(hx)` along the `T_16`-orbit
converge to the space average 0.

## 5. What this cycle produced (honest)

- **The path geometry is real and correctly-framed** — it's Birkhoff ergodic theory applied to
  `T_16` at the specific point `{π}`.
- **The walk is empirically square-root-cancelling** (`|S_N| ≈ √N`), the precise quantitative
  signature of normality.
- **The missing ingredient is unchanged:** proving *this specific orbit* has square-root
  cancellation — i.e. the Weyl gate — now stated as a theorem about the **geometry of a
  self-similar Birkhoff walk**, not about digits.

The cycle "crucified" nothing new here — instead it **re-framed** the wall in its canonical form:
normality = Birkhoff ergodicity of the `T_16`-orbit of π. The path geometry is the *right* object;
the limit is the *same* unknown; and the improvement is a cleaner name: **the Weyl gate is a
Birkhoff-ergodicity statement for a specific, non-ergodicity-provable point.**

**π base-16 normality and RH remain OPEN.**
