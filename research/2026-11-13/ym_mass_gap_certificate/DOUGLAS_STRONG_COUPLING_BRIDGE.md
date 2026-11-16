# External Lean strong-coupling lattice theorem and SUCC's UV-to-IR bridge

**Date:** 2026-11-13. **Status:** audited source statement + conditional synthesis. **No continuum Yang–Mills mass-gap claim.**

## Pinned primary source

Michael R. Douglas / Fred Rajasekaran, [mrdouglasny/lgt](https://github.com/mrdouglasny/lgt), read-only main commit **b8793ccf6a51e00e9e2b1685ba191b8626e37137** (2026-07-22).

- [StrongCoupling.lean](https://github.com/mrdouglasny/lgt/blob/b8793ccf6a51e00e9e2b1685ba191b8626e37137/LGT/MassGap/StrongCoupling.lean): declarations ym_mass_gap_exponential_decay and ym_mass_gap_rate_exists.
- [DobrushinVerification.lean](https://github.com/mrdouglasny/lgt/blob/b8793ccf6a51e00e9e2b1685ba191b8626e37137/LGT/MassGap/DobrushinVerification.lean): influenceBound and dobrushinAlpha.
- [ScaleTransfer.lean](https://github.com/mrdouglasny/lgt/blob/b8793ccf6a51e00e9e2b1685ba191b8626e37137/LGT/Bridge/ScaleTransfer.lean): conditional abstract coarse-to-fine covariance decay transfer assuming RG blocking data, distance compression and covariance comparison. This does not construct a 4D continuum Wilson RG.
- The README reports a zero-project-axiom Lean/kernel replay for the strong-coupling theorems. This SUCC round inspected published code but did **not** independently rebuild Lean or run the Comparator.
- **Version-skew caution:** the external README still mentions v4.29.0, but the actual main lean-toolchain and pinned Mathlib manifest inspected today use v4.30.0. For reproduction the checked-in toolchain and manifest supersede README prose.

## Exact external theorem: a finite-lattice plaquette correlation bound

For periodic d-dimensional U(n) Wilson lattice theory, n≥1, d≥2, side length N>2, and coefficient β satisfying

\[
0<\beta<1/(4n\operatorname{maxNeighbors}(d)),
\quad\operatorname{maxNeighbors}(d)=8(d-1),
\]

the connected two-point function for **plaquette ReTr observables** obeys

\[
|\operatorname{Cov}_{\beta}(\mathrm{ReTr}\,U_p,\mathrm{ReTr}\,U_q)|
\le \frac{32n^2}{\alpha(1-\alpha)}e^{-m_\mathrm{lat}\,d_{\mathrm{plaq}}(p,q)}, 
\]

where

\[
\alpha=8(d-1)(1-e^{-4n\beta})\in(0,1),\qquad
m_\mathrm{lat}=-\frac12\log\alpha>0.
\]

The companion algebraic theorem has a sharper truncated-power expression. Distance here is *in lattice units*. The formal theorem controls one chosen class of plaquette observables, not a dense bank spanning the OS physical vacuum-orthogonal Hilbert space. A finite periodic lattice with uniform-size estimates is not itself a positive physical continuum Hamiltonian gap.

### Example: an explicit rigorous lattice rate (not the physical glueball mass)

For d=4, n=2, β=1/512 in the external action convention, maxNeighbors=24 and 4nβ=1/64. By 1−e^(−x)≤x for x≥0,

\[
\alpha=24(1-e^{-1/64})\le 24/64=3/8<1,
\]
\[
\boxed{m_{\mathrm{plaquette,lattice}}\ge\tfrac12\log(8/3)>0.}
\]

**Scope:** this is a lower bound for the strong-coupling *lattice plaquette correlation decay exponent*, obtained by elementary substitution into the external theorem. It is **not** an estimate of the MeV mass of a continuum glueball, is not a proof that this exponent is the infimum of the entire Hamiltonian spectrum, and includes no physical scale setting.

## What blocks transfer to the Clay regime

1. **UV coupling mismatch.** This result needs small β; the standard 4D asymptotically free Wilson continuum trajectory has bare g(a)→0, hence β(a)→∞ in the convention β∝1/g(a)^2. The small-β Dobrushin theorem cannot simply be applied along that trajectory.
2. **RG changes the source action.** Coarse-graining an authentic Wilson measure typically generates extended multi-loop/spin interactions, not only the original plaquette term. The strong-coupling instance theorem therefore does not automatically apply to the effective law. One needs a *new* influence bound including all generated interactions or a rigorously controlled source comparison.
3. **Scaling and phase selection.** The selected continuum phase in the OpenAI October construction is not proved identical to a Douglas-model lattice source/phase. A legitimate bridge must share the same Wilson action convention, limit extraction, renormalized physical clock and complete observable correspondence.
4. **Observer completeness.** Decay of ReTr plaquette covariances alone can miss a slower gauge-invariant sector. SUCC MG1 requires a dense OS bank, including gauge-invariant mixed-word, spin-network, Haar detail and global/topological channels.
5. **Missing uniformity.** A q<1 at finitely many cutoffs, or a rate positive in lattice units, need not imply a positive infimum in fixed physical units. One source-selected same-phase estimate must survive all small a and large volume.

## Five concrete research rungs, each falsifiable

**A — source matching:** Compare SU(2), U(2) action normalizations in the two external Lean repos and SUCC #613's one-plaquette state, prove a coefficient/observable map, and reject wrong-coupling and wrong-Haar mutations.

**B — physical 4D Wilson slabs:** Use SUCC #614's complete nonabelian simultaneous-conjugacy quotient and noncontractible holonomy controls. Build positive-time mixed Wilson words and source-derived reflected Gram matrices for small actual 4D compact simple-group slabs.

**C — actual RG data:** Construct a gauge-equivariant and law-preserving coarse map for *the full generated effective action*, retaining source-weighted Haar details. Prove the covariance transfer and long-range tail bounds assumed in the Douglas ScaleTransfer theorem, not only a commuting gauge-subdivision square.

**D — effective Dobrushin/semigroup contraction:** Prove for a physically fixed coarse slab, uniformly over all fine UV lattice spacings and volumes, either (i) an effective generalized conditional influence contraction α★<1 with controlled nonlocal tails, upgraded to all OS channels, or (ii) directly SUCC MG3's coarse/detail semigroup margins α,β,γ with γ²<(1−α)(1−β). The same q must work for an increasing dense bank.

**E — limit and mass:** Prove two-time OS Gram convergence in the same OpenAI-selected Wightman phase with physical t★ fixed. Apply MG2/MG1, obtaining an actual physical Hamiltonian Δ>0; if quantitative, specify the renormalization scale needed to translate it to energy units. A sharp numerical 0++ glueball mass is a further calculation, distinct from demonstrating a nonzero lowest excitation.

## Hostile control suite

- Bare β(a)→∞ violates the external small-β hypothesis; forbid applying it directly.
- A coarse law containing omitted multi-loop terms fails source matching.
- Twisted flat torus holonomy defeats plaquette-only observers (#614).
- Coherent cross-channel coupling can leave a zero mode despite diagonally contracting coarse/detail blocks (MG3).
- Two spectral families can share any fixed finite set of cutoff measurements yet have respectively positive/gapless limits (MG5 and #614).
- A single scalar connected correlator cannot certify unseen physical excitations (MG1 completeness).
- Source-normalization, physical time n a, and field contact terms must be explicitly transported.

**Ledger:** external Lean strong-coupling *lattice* theorem = **EXTERNAL REVIEWED, not locally rebuilt**. Strong-coupling numeric example = **DISCLOSED conditional on inspected theorem**. Source-selected 4D Wilson RG into an effective contracting basin = **UNVERIFIED**. Dense-bank all-channel physical spectral mass = **OPEN**. Clay mass gap = **OPEN**.

Read with [SUCC MG1–MG5](README.md), [preexisting SUCC #614](https://github.com/femboy2112/SUCC/pull/614), and [preexisting SUCC #613](https://github.com/femboy2112/SUCC/pull/613). No external source copied.
