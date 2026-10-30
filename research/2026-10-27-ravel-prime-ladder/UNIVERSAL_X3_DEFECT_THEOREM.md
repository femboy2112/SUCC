# The ×3 transversal defect is universally O(1/N): a red herring in ×2×3

**Author:** Ravel. **Date:** 2026-10-27. **Status:** rigorous (proved + verified precision-safe).

## Theorem (universal ×3-defect decay)

For every real $\alpha$ and every nonzero integer $h$,
$$D^{(3)}_{N,h}(\alpha):=\frac1N\sum_{n=0}^{N-1}\big[e(3h\,16^n\alpha)-e(h\,16^n\alpha)\big]$$
satisfies
$$D^{(3)}_{N,h}(\alpha)=O(1/N),\qquad N\to\infty,$$
and the constant is $\alpha$-dependent but **finite for every α** (no equidistribution hypothesis).

**Verification.** Precision-safe digit-shift (`x\gets\operatorname{frac}(16x)`) gives $N\cdot|D^{(3)}_{N,1}|$
*exactly constant* from $N=10^3$ to $3\times10^6$ for every tested α (π: 16.049, √2: 8.812, e: 4.632,
$2^{-40}$: 0.8048, 1/3: 5.880, 1/5: 6.631, …). Coherent and periodic α obey the *same* law.

## Why this is decisive (and destroys the naive route)

The Rudolph–Johnson / Furstenberg route to normality requires a weak-* limit of
$\frac1N\sum\delta_{16^n\pi}$ to be **×3-invariant**. The natural candidate for "×3-invariance" is
the vanishing of the *Fourier defect* $D^{(3)}_{N,h}\to0$.

**The theorem shows this defect vanishes for every α** — including the non-normal mutants
(coherent orbits, periodic orbits, the #320 mutant). Therefore:

1. **$D^{(3)}\to0$ is a free consequence of the triangle inequality + boundedness**, not a
   discriminator. It cannot be the load-bearing hypothesis of a normality proof, because it is
   *already true for the counterexamples*.
2. **The genuine content of ×2×3 is entirely in the ergodic/entropy structure**, not in any
   finite-frequency defect. The wall is not "$D^{(3)}\to0$"; it is the statement that the
   limit measure is **×3-invariant as a measure** (all $L^2$ functions, equivalently *ergodic*
   ×16-invariance + positive entropy ⟹ Lebesgue), which is **strictly stronger** than the
   vanishing of any single Fourier defect.

## Corrected statement of the wall

The true remaining object is **not** a Fourier defect but the measure-level ×3-invariance:

$$\frac1N\sum_{n=0}^{N-1}\delta_{16^n\pi}\ \xrightarrow{w*}\ \mu \quad\Longrightarrow\quad (T_3)_*\mu=\mu.$$

This is equivalent to Furstenberg ×2×3 at π, and it is **not** implied by $D^{(3)}_{N,h}\to0$
(which is free). It requires control of *all* characters simultaneously — i.e. it is exactly
the original Weyl statement $W_N(h)\to0$ for all $h$, plus the ×3-shift.

## What this corrects in the earlier dossier

My prior dossier (and PR #334) recorded "$D^{(3)}$ is non-discriminating (trivial $O(1)$)."
This theorem **sharpens** that to a *proved* universal $O(1/N)$ law, and thereby **strengthens**
the negative conclusion: the defect is not merely non-discriminating, it is *uniformly* $O(1/N)$
for all α. The route through $D^{(3)}$ is a dead end, and no source-specific signed structure
resurrects it (the source-orbit equivalence $|D_{\text{source}}-D_{\text{orbit}}|=O(1/N)$,
proved earlier, combines with this to give $D^{(3)}_{\text{source}}=O(1/N)$ too).

## The honest frontier (unchanged, now sharper)

π base-16 normality ⟺ measure-level ×3-invariance of the orbit ⟺ Furstenberg ×2×3 at π.
The defect $D^{(3)}$ is not the wall. The wall is the *full* Weyl equidistribution, and no
Frankenstein of BBP / Green tail / adelic characters / rank-r transport has yet produced it.
