# Constant Registry: the oily-macaroni constant (canonical record)

**Author:** Ravel. **Date:** 2026-10-27. **Purpose:** a single findable record of a named constant
and its geometric identification, to counter the "too much math to track" problem. This is a
*registry entry*, not a new theorem.

## The constant

$$\boxed{\ \delta = \varphi^{-1} - \gamma = \frac{\sqrt5-1}{2} - \gamma = 0.04081832384836198759\ldots\ }$$

where $\varphi=(1+\sqrt5)/2$ is the golden ratio and $\gamma=0.5772156649\ldots$ is Euler–Mascheroni.

## Provenance (exact source)

- **Name:** "oily-macaroni constant" (author's chosen name), the candidate offset
  $\delta=\lambda-\gamma$ with $\lambda=(\sqrt5-1)/2=\varphi^{-1}$.
- **Source dossier:** `SUCC-carry-defect/research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md`
  (PR #306, commit `7989be5753341c5e74d570e8fea51e00129d2d0a`), lines 30–31.
- **Exact source moments:** $E[B]=7/2$, $E[B^2]=55/3$, $\eta_n\sim7/(16n)$.

## Geometric identification (exact, verified this session)

Both terms of $\delta$ are **circle quantities**:

1. **$\varphi^{-1}$ is a chord of the unit circle.** $\varphi=2\cos(\pi/5)$ is the *long* chord
   (subtending $72°$), the regular pentagon's diagonal-to-side ratio; $\varphi^{-1}=\varphi-1=2\cos(2\pi/5)$
   is the *short* chord (subtending $144°$), the pentagon's side-to-diagonal ratio. So
   $$\varphi^{-1}=2\cos(2\pi/5),\qquad \varphi=2\cos(\pi/5).$$
   Verified to 40 digits: $2\cos(2\pi/5)=0.61803398874989484820\ldots=\varphi^{-1}$.

2. **$\gamma$ is the harmonic-circle discrepancy.** $\gamma=\lim_{n}(H_n-\log n)$ is the gap between
   the discrete harmonic sum and the continuous log — the "discrete lattice vs continuous circle"
   discrepancy.

Hence **$\delta = (\text{short pentagon chord}) - (\text{harmonic discrepancy})$**: one geometric/rigid
circle quantity minus one analytic/limiting circle quantity.

## Forced vs. chosen (the honest boundary, from the source dossier)

- **$\gamma$ is structural:** the Euler error $\epsilon_m=H_m-\log m-\gamma\to0$ holds for *any* real
  reference constant in place of $\lambda$. (Source dossier §4, line 188.)
- **$\varphi^{-1}$ is a chosen reference:** it is the golden fixed point $L(\lambda)=\lambda$ of the
  Laplace map, a convenient fixed point, not forced by the four-pole BBP source.

So the *combination* $\varphi^{-1}-\gamma$ is aesthetically coherent (two circle quantities), but the
specific pairing of $\varphi^{-1}$ (rather than another chord/constant) is a **convention**, not a
theorem. This does not reduce the constant's value or its usefulness as a reference; it marks what is
forced vs. chosen.

## Relationship to the proof program

The constant enters via the proved auxiliary cancellation $8n\,\Theta_n(k)\to-\frac72+\frac{i}{2\pi k}$
($\Theta_n=O(1/n)$, full-source, rejects the matched-moment control $\mu_*$). The remaining named
obstruction is the log→inverse-square transport. See `OILY_MACARONI_VERDICT.md`.

## Cross-references (so this is findable)

- `SUCC-carry-defect/handoffs/OILY_MACARONI_RELATIVE_PHASE_NEXT_2026-10-26.md`
- `SUCC-carry-defect/research/2026-10-26/OILY_MACARONI_SOURCE_BRIDGE.md`
- `SUCC-carry-defect/tests/test_oily_macaroni_totient.py`
- This branch: `research/2026-10-27-ravel-prime-ladder/OILY_MACARONI_VERDICT.md`
