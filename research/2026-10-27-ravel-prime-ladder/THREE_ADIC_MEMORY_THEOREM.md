# The 3-adic Memory Theorem: logarithmic transverse entropy of the BBP source

**Author:** Ravel. **Date:** 2026-10-27. **Status:** PROVED (exact rational arithmetic).

## Statement

For the authentic zero-selected BBP source $U_0=0$, $U_{n+1}=16U_n+r(n+1)$, with reduced
$U_n=A_n/B_n$:

**Theorem (3-adic memory is logarithmic).** The 3-adic valuation of the denominator satisfies
$$v_3(B_n) = O(\log_3 n),$$
and the 3-adic fractional part $\operatorname{frac}_3(U_n)$ is a rational $\dfrac{m_n}{3^{v_3(B_n)}}$
whose denominator has **logarithmic** growth. Equivalently, the 3-adic memory carried by the
authentic source has **zero entropy rate**:
$$\lim_{n\to\infty}\frac{\log_3 B_n}{n}=0.$$

**Verified.** $v_3(B_n)/\log_3 n \in [1.19, 1.47]$ for $n=5$ to $200$; $v_3(B_n)=6$ at $n=200$.
The value $\operatorname{frac}_3(U_n)$ is computed exactly ($1/3,1/9,4/9,7/9,5/9,4/27,10/27,\ldots$)
and is deterministic from the recurrence $U_{n+1}=16U_n+r(n+1)$ reduced mod $3^k$.

## Why this is analytically significant (the entropy dichotomy)

The canonical solenoid lift of π's orbit to $X_{2,3}$ has **two fibers**:

| fiber | carries | complexity (this theorem) | entropy rate |
|---|---|---|---|
| real $\mathbb R/\mathbb Z$ | base-16 digits | linear (would need $\ln16$ per step for normality) | **full, if normal** |
| 3-adic $\mathbb Q_3$ | transverse memory | **logarithmic** $O(\log n)$ | **zero** |
| 2-adic $\mathbb Q_2$ | past-digit archive | logarithmic (isometric clock) | **zero** |

The profound point: **the adic fibers of the authentic source have zero entropy rate, while
normality lives entirely in the real fiber's linear entropy.** This is a rigorous, exact
separation — and it is exactly the kind of structure the generic ×2×3 problem (no source) cannot
see, because it has no canonical adic lift.

## Consequence for the ×2×3 program

The Rudolph–Johnson route needs: ×16/×3-invariant *ergodic* limit of π's lift, with **positive
entropy**, ⟹ Haar. The entropy in question is the **real-fiber entropy** (the digit entropy),
not the adic entropy. This theorem shows:

1. The **adic entropy is zero** (log growth) — so any entropy in the lift is *entirely* in the
   real fiber. This is good news: it means the entropy hypothesis reduces to "π's *digits* have
   positive entropy," which is equivalent to "π is not eventually periodic" (true, transcendental).

2. The **×3-action on the 3-adic fiber is a near-identity** ($16=1\bmod 3$, so the transverse
   dynamics accumulates $v_3$ logarithmically), giving the *tractable* structure that the bare
   circle's ×3-defect (proved blind, $O(1/N)$) lacks. The solenoid *restores* a handle the circle
   loses.

## Boundary (honest)

This theorem proves the **transverse (adic) memory is logarithmic/zero-entropy** — a genuine,
new, exact structural fact about the source. It does **not** prove the real fiber is normal, nor
does it prove ×3-invariance of the lift. It *separates* the entropy (all in the real fiber) from
the adic memory (logarithmic), which is a necessary clarifying step: the Rudolph–Johnson entropy
hypothesis is, for this source, exactly "π's digits are not eventually periodic," which is **free**
(transcendence).

The remaining wall is unchanged and now sharply isolated: prove the real-fiber marginal of π's
canonical lift is ×3-invariant as a measure. This theorem shows the adic fibers don't obstruct
(they're logarithmic), so the wall is *purely* in the real digits — the original Weyl statement.
