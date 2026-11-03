# The steelman→crucify→improve loop on W_{k,N}(h): current state

**Branch:** `research/shen-tzu-weyl-form-2026-11-02`. **Date:** 2026-11-02.
**Agent:** Ravel. **Scope:** run the loop on the concrete bridge brick `W_{k,N}(h)` until it is
solved, resolved, or precisely located.

## The brick (recap)

`W_{k,N}(h) = Σ_{n=1}^{N-k} e(h(16^k−1)U_n)`. HMS-15 (proved): its harmonic-weighted average
`(1/N)Σ_k w_{K,k}|W_{k,N}(h)| → 0` ⟹ π base-16 normal.

## Cycle 1 — steelman: "the composite multiplier 16^k−1 gives new arithmetic cancellation"

**Steelman (Brick 1):** `16^k−1 = 15·Σ16^i = (4^k−1)(4^k+1) = ∏_{d|k}Φ_d(16)` is a rich
divisibility tower, always odd, `gcd(16^{n-1}, 16^k−1)=1` — maybe the composite structure
constrains the rotation phases.

**Crucify (against reality):** π is transcendental, so `{h·M·16^{n-1}π}` is irrational for every
integer multiplier M — **no divisibility of `16^k−1` can make the phase rational.** The tower
structure is a *re-parametrization*, not a constraint. The only exact identity is
`(16^k−1)16^{n-1} = 16^{n+k-1} − 16^{n-1}`, which reproduces the self-similar covariance
(already proved inert). **VERDICT: dead.**

**Improve:** the amplified tail `(16^k−1)T_n ≈ 16^k/(64n²)` is *less* controlled (not more) —
it's a genuine obstacle, not a handle. Partial summation on `e(−h(16^k−1)T_n)` converts it to
`T_n′ ≈ −1/(32n³)` but *reintroduces* the rotation partial sums — faithfully reproducing the
gate's self-similarity. **No gain.**

## Cycle 2 — steelman: "the k-weighted second moment is an L² object, genuinely weaker"

**Steelman (Brick 3):** `Σ_k w_{K,k}|W_{k,N}(h)|²` is a second moment; maybe it's a weaker L²
object (like the collision gate was) and closes HM-open via Cauchy–Schwarz.

**Crucify (against reality):** `W_{k,N}(h) = S_{N−k}(h(16^k−1))` — it is **literally the same
Weyl sum** re-indexed to frequency `h(16^k−1)`. There is **no Parseval identity over `k`**
(the multiplier index is an integer re-parameterization, not a frequency). The second moment is a
*convex combination of squares of the same sum*, reducing to the **same pointwise wall** — not a
weaker L² statement. **VERDICT: dead.**

**Improve:** the collision-gate case was different: there, Parseval summed over *frequency `h`*
(giving a genuine L² energy). Here, summing over the *multiplier `k`* gives no new spectral
object. The harmonic `1/k` weight only suppresses short-`N−k` tails; it renormalizes, doesn't
cancel.

## Cycle 3 — (in progress): the amplified-tail regime split

The remaining brick is the **amplified-tail regime**: split `W_{k,N}(h)` into
`|h(16^k−1)T_n| ≪ 1` (tail ≈ 1, controllable) vs `n` small (tail amplified, wild). Whether the
amplified tail is a *controlled* perturbation or a *wild* Diophantine object is the live question
(Front 2, still running).

## The loop's honest convergence

Two cycles have **crucified** the two most promising steelmen: the composite multiplier is inert
(π transcendental), and the k-second-moment is the same pointwise wall (no Parseval over k). The
object `W_{k,N}(h)` is, structurally, **the same Weyl sum** `S(h·16^k)` — the frequency `h(16^k−1)`
is just a *ladder point*, and the ladder is self-similar (proved in the van der Corput / Ward
rounds).

**The honest state:** the bridge brick `W_{k,N}(h)` has not yet yielded a proof, and two of its
three attack vectors are now provably inert. The remaining vector (amplified-tail regime split)
is the last live angle. If it too is inert, then HMS-15's object is the **same Diophantine wall**
as everything else — and the loop's terminal output will be: *π normality is equivalent to the
signed Weyl cancellation, every decomposition is a re-encoding, and no known or new route closes
it.*

**π base-16 normality and RH remain OPEN.**
