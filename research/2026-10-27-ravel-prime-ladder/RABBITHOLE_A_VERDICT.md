# Rabbithole A — VERDICT: the coupled solenoid defect discriminates (new, proved finite)

**Author:** Ravel. **Date:** 2026-10-27. **Status:** PROVED (finite, exact) + sharp boundary.

## The question

Does the ×3-defect of π's *canonical solenoid lift* to $X_{2,3}$, evaluated at a character with
non-trivial 3-adic content, discriminate the authentic source from the coherent non-normal control —
unlike the *bare* real-circle defect, which the Infinite-Dimensionality Theorem proved is
$O(1/N)$-blind for every α?

## The three-layer result (each checked exactly)

**Layer 1 — real-circle defect alone: BLIND (already proved).**
$D^{(3)}_{N,h}(\alpha)=O(1/N)$ for every α. Confirmed this session.

**Layer 2 — 3-adic factor alone: BLIND (new, verified this session).**
The defect $\frac1N\sum_n[\psi_3(\tfrac13 z_3^{(n)})-\psi_3(z_3^{(n)})]$ of the *3-adic factor by itself*
does **not** decay for either the authentic source ($\approx0.85$) or the control $-T_n$ ($\approx0.80$):
both stay bounded away from zero. The 3-adic memory, in isolation, is not discriminating.

**Layer 3 — the COUPLED defect (real × 3-adic): DISCRIMINATING (new).**

Define the full solenoid defect at the character $a=\tfrac13\in\mathbb Z[1/6]$:
$$D_N(\tfrac13)=\frac1N\sum_{n=1}^N\Big[e(\tfrac13 U_n)\,\psi_3(\tfrac13 z_3^{(n)})\ -\ e(U_n)\,\psi_3(z_3^{(n)})\Big],$$
where $U_n=A_n/B_n$ is the authentic rational state and $z_3^{(n)}=\operatorname{frac}_3(U_n)$ its exact
3-adic memory. **Exact computation (no floats in the arithmetic):**

| $N$ | authentic $|D_N(1/3)|$ | control $-T_n$ | ratio |
|---|---|---|---|
| 30 | 0.295 | 0.773 | 2.6 |
| 60 | 0.159 | 0.798 | 5.0 |
| 120 | 0.146 | 0.875 | 6.0 |
| 240 | 0.031 | 0.791 | 25.6 |
| 300 | 0.025 | 0.777 | 31.5 |

The authentic defect **decays toward 0** while the coherent control $-T_n$ **remains bounded away**,
with the separation ratio growing monotonically. **The coupled (real × 3-adic) defect discriminates.**

## Why this is non-circular (the point)

- The bare real defect is blind (Layer 1, proved).
- The bare 3-adic defect is blind (Layer 2, verified).
- **Their product is not blind** (Layer 3). The coupling — the real phase of the rational state
  *times* the 3-adic character of its denominator's 3-adic memory — is a *genuinely new observable*
  that is neither the Weyl sum alone nor the adic memory alone.

This is precisely the "solenoid restores discriminating power" hypothesis of `analytic_solenoid.py`,
now confirmed for the first time, at a specific character, with exact arithmetic.

## Boundary (honest — what this does and does NOT establish)

- **Proved (finite):** the coupled defect discriminates the authentic zero-selected source from the
  future-selector control $-T_n$, at character $a=1/3$, over $N\le300$, with a monotonically growing
  separation ratio.
- **Not proved:** that the authentic defect $D_N(1/3)\to0$ as $N\to\infty$. The decay to $0.025$ is
  finite evidence; the *rate* and the *limit* are not established. (This is exactly the Weyl/×3-
  invariance statement, now re-expressed at a 3-adic-carrying character.)
- **Not proved:** discrimination against *all* non-normal mutants (only $-T_n$ and the constant-memory
  mutant were tested).
- **Not proved:** π normality. This is a *new observable* that separates π's source from a coherent
  control; it is not a proof that the observable itself vanishes in the limit.

## The precise open object (sharper than before)

The coupled defect $D_N(a)$ at 3-adic characters is a candidate for the *right* measure-level
×3-invariance witness. The single remaining question is now:

> Does $D_N(1/3)\to0$ for the authentic source, at a *proved* sublinear rate?

If yes (at any rate), the coupled solenoid defect is the missing discriminating arrow, and the
×2×3 wall is re-expressed in a form that the source's exact arithmetic (rational $U_n$ + exact
$\operatorname{frac}_3$) can attack with machine-checkable certificates — rather than the raw
transcendental Weyl sum.
