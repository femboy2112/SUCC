# Three more angles, all closed honestly (monotone-spiral, tail-integral, Stieltjes)

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel. **Scope:** keep blasting — push genuinely-new angles past the fixed point and
record their honest outcomes.

## Angle 1 — monotone-spiral / ordered-winding equidistribution (CLOSED, inert)

Steelman: the orbit `U_n = 16^{n-1}π − T_n` is *monotone increasing* on the universal cover; maybe
monotone + geometric + irrational-limit forces equidistribution of the projection.

Crucify: **counterexample** `a_n = 16^{n-1}·(1/5)` — monotone, geometric (`a_{n+1}/a_n → 16`),
irrational-looking, but `{a_n} = 0.2` **periodic** (since `16 ≡ 1 mod 5`). Monotone+geometric+
irrational-limit is **not** sufficient; the seed's arithmetic matters. Ordered winding gives no
new handle.

## Angle 2 — exact integral form of the tail (CONFIRMED, but π-free)

`T_n = ∫₀¹ x^{8n} P(x)/(16−x⁸) dx`, `P(x) = (1−x)(x²+2)(x²+2x+2) > 0`. Verified exactly
(`n=1,3`: integral = exact `T_n`). This is the maintainer's LS-03, re-derived. It gives `T_n` a
**positive-measure moment representation** — but it is a functional of the *poles* only, π-free
(proved earlier), so it cannot constrain the digit equidistribution.

## Angle 3 — Stieltjes / complete monotonicity of T_n (CLOSED, inert for the product)

`T_n` is a **Stieltjes moment sequence** (completely monotone): `(−1)^k Δ^k T_n ≥ 0`, decreasing
and convex. Consequence: the tail phase `φ_n = −h(16^k−1)T_n` is **monotone** in `n`, so its own
partial sums are controlled by monotone-phase lemmas.

Crucify: `W_{k,N}(h) = Σ e(iθ_n)·e(iφ_n)` where `θ_n = h(16^k−1)16^{n-1}π` is the **wild fast
rotation** and `φ_n` is the **slow monotone tail**. The product phase `θ_n + φ_n` is still wild —
the monotone tail phase does **not** tame the rotation (which is the same Diophantine object as
always). Complete monotonicity of the tail gives no new cancellation.

## The running tally

Every angle — now ~12 distinct steelmen across the campaign — converges to the same fixed point:
`π normal ⟺ {16^{n-1}π} T_16-generic for Lebesgue`, with every decomposition a re-encoding. The
new angles this round (monotone-spiral, tail-integral, Stieltjes) each add one more *proved*
reason the wall is symmetric and self-similar.

**π base-16 normality and RH remain OPEN.** No false victory; durable negative map keeps growing.
