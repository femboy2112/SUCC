# A native uniform-correlation estimate: the actual import boundary

**Date:** 2026-11-13. **Status:** bounded source-code audit of an upstream
analytic theorem and its immediate proof inputs. **Local reproduction:** none
of the Lean declarations below was compiled or kernel-replayed in this round.
The elementary finite Wilson calculation in `WILSON_REFLECTION_SLICE.md` does
not reproduce this estimate.

## 1. The selected theorem

The exact native endpoint is

`YM.FullVolume.genuine`

in [`YM/FullVolume/Literal.lean`][literal]. Its type states that for an actual
`YM.PhysicalNext.Repeat.Legato.Run G` and a proof of `G.Simple`, the constructed
family satisfies `YM.FullVolume.FixedBounds`.

The definition of `FixedBounds` in
[`YM/FullVolume/Discrete.lean`][discrete] expands to a significant uniform
analytic assertion. Fix:

- a finite number \(n\) of insertions;
- a list \(v\) of \(n\) field tokens in the construction's common dictionary;
- any finite list \(l\) of insertion-slot/coordinate directions;
- a positive physical separation \(r\).

There exist \(B\ge0\) and a cutoff threshold \(N_0\) such that, for every
\(N\ge N_0\), every admitted volume index \(p\), and every lattice
configuration of insertion positions \(x\) with pairwise physical torus
separation at least \(r\),

\[
\left|
 \Delta^{\,l}_{a_N}
 \mathbb E_{\mu_{N,p}}
 \left[\prod_{i=1}^{n}O_{N,p}(v_i,x_i)\right]
\right|\le B.
\]

Each coordinate difference is normalized by the actual mesh:

\[
\Delta_{a,u}f(x)=a^{-1}\bigl(f(x+u)-f(x)\bigr).
\]

`gKernel` is this iterated difference of the periodically lifted numeric
correlation. `spaceout` uses the torus max-distance multiplied by \(a_N\).
The bound and cutoff threshold may depend on the run, the complete field list,
the direction list, and \(r\). They are uniform in \(N\) beyond that threshold
and in **all** the family's volume indices. No uniformity as \(r\downarrow0\),
as field degree increases, or as the number of differences increases is asserted.

This is stronger than continuity or boundedness of a fixed finite-dimensional
integral. The observables are renormalized, and the difference operators divide
by powers of a mesh that tends to zero. A naive finite-cutoff supremum estimate
can diverge with that cutoff. The theorem bounds the specified correlations and
their fixed finite derivatives uniformly across those cutoffs.

## 2. The source is the Wilson law, not an arbitrary positive state

The following definitions were read to bind the statement to its actual source:

| Native file | Definitions or declarations | Role |
|---|---|---|
| `YM/Wilson/Law.lean` | `prior`, `bare`, `partition`, `law`, `moment` | Product Haar prior and normalized plaquette Boltzmann density; moments are integrals against that law |
| `YM/Source/Construction.lean` | `Family`, `Family.O`, `Family.Makes` | Local field dictionary, transferred insertions, and calibrated source certificates |
| `YM/Extraction/LatticeFamily.lean` | `Family.numeric`, `Family.num`, `Family.integrableR` | Correlations are actual products of those insertions under one Wilson measure, with integrability |
| `YM/Extraction/Integrate.lean` | `lifted` | Lift positions to the cover and then wrap them to the periodic lattice |
| `YM/FullVolume/Skein.lean` | `delta`, `deltas` | Actual mesh-normalized finite differences |
| `YM/FullVolume/Discrete.lean` | `gKernel`, `FixedBounds` | The kernel and uniform estimate above |

`Family.Makes` includes a selected RG history, sound local sections, support and
size conditions, and renormalization calibration. The selected-history fields
in [`YM/RG/History.lean`][history] assert that the ultraviolet endpoint equals
the actual bare Wilson density, record exact successive blocking of the density,
control the coupling drift, and fix a common reference coupling. Thus a
positive matrix with similarly named fields would not instantiate this interface.

The physical construction supplies the run: `Run.ramp` in
[`YM/FullVolume/Cross.lean`][cross] proves existence of a `Run G` for every
positive requested blocking penalty, assuming `G.Simple`. Its proof invokes
the earlier `dagger`, `rod`, and `squad` construction producers. Those large
upstream producers were **not** audited here. The inspected `Run` structure
retains the same Wilson family, transfer data, gauge-door steps, and calibration
certificates needed by `genuine`.

## 3. Immediate proof inputs: derivative costs and chessboard estimates

The proof of `genuine` invokes `funding` in the same file. This assembles two
different inputs; confusing their roles would hide the hard work.

### 3.1 Controlling each differentiated insertion

`YM.PhysicalNext.Repeat.Legato.Run.financed` proves

`Funded (hops (Bid.upper R.family w) l)`

for any fixed degree, any coefficient row \(w\) eventually bounded uniformly
in cutoff and volume, and any finite coordinate-direction list \(l\).
`hops` applies normalized differences to the **literal insertion**. In the final
`genuine` application the coefficient rows are constant, so their boundedness is
immediate; boundedness of the resulting differentiated field costs is not.

The predicates in [`YM/FullVolume/Rent.lean`][rent] specify what this buys:

- `Affords F u` requires a fixed finite stencil and, at every sufficiently fine
  fixed centered scale \(m\), eventual control at finer cutoffs under all volumes.
- `Funded F` provides a cost function \(u(m)\) independent of the finer cutoff
  and volume, bounding the centered replication-root test of \(F\).
- Interior support and measurability are retained with the estimate.

Here the replication-root test is not an arbitrary norm. For a tiling \(T\),
[`YM/Cells/Tiling.lean`][tiling] defines it as

\[
\mathcal R_{T,\beta}(F)=
 \left|
  \mathbb E_{\mu_\beta}
  \prod_{c\in T}\operatorname{copy}_{c}(F)
 \right|^{1/|T|},
\]

where the copies carry the specified translations, reflections, and conjugations.
The observable, the reflected copies, and the expectation all use the same law.

One input retained by `Run.again` is `Extraction.Wcmain`. Its precise definition
in [`YM/Extraction/Center.lean`][center] bounds primary centered root tests by
\(A a_m^{-d-\varepsilon}\), for each fixed degree \(d\), coefficient ball and
\(\varepsilon>0\), with \(A\) chosen before \(m\), and an eventual cutoff
threshold uniform in volume. `Funded.primaries` uses that estimate. Derivative
control additionally uses `YM.FullVolume.cap` and `YM.FullVolume.improved` in
[`YM/FullVolume/Moneys.lean`][moneys].

Those proofs compare a differentiated insertion to a primary representative,
control a projected coefficient vector using field/rank detectors, and use
source-derived equation terms whose replication costs vanish. The file's
`cap` proof obtains an eventual bound of the form \(2Zc+1\) for the projected
coefficient norm. Its assumptions include the actual source calibration,
detector estimates, and a vanishing root-cost error. This is not deduced merely
from the existence of a projection or a quotient.

**Dependency caution:** `Run.financed` calls `Run.again`, selects a preliminary
extracted table, and obtains the associated field/rank detectors before applying
these estimates. Therefore this uniform-bound result strengthens an existing
subsequential construction. It is not the entire first-principles existence
proof reduced to one freestanding inequality. The source dependencies inspected
here do not justify removing that preliminary construction.

### 3.2 Turning per-insertion costs into a correlation bound

`YM.FullVolume.cohort` and `YM.FullVolume.financed` in
[`YM/FullVolume/Cohort.lean`][cohort] place separated insertions into distinct
cells and bound their joint Wilson expectation by the product of their
replication-root costs. The centered scale is fixed after the separation and
the finite insertion list; its cost is then independent of the finer cutoff and
volume. `funding` distributes the requested coordinate differences among the
insertion slots and applies this bound.

The product inequality comes from the actual Wilson reflection/chessboard
interface: `Cells.Seam`, `Cells.laws`, and `Cells.Tiling.planted` in
[`Certificate.lean`][certificate] and [`Embedded.lean`][embedded].
`Cells.seamless` obtains that interface from `Family.Makes` and the positive
coupling band. This is where source-derived reflection positivity enters.
Ordinary Gram positivity or independent one-plaquette averages cannot replace it.

The filter definition also matters. In
[`YM/FullVolume/Sluggish.lean`][sluggish], `mesh` is the pullback of the cutoff
tail filter, and `late` proves that eventual truth in this filter means an
eventual cutoff threshold valid for **every** volume index. No silent
large-volume exception is present.

## 4. What this estimate does and does not close

[`YM/FullVolume/Profiles.lean`][profiles] uses `FixedBounds` together with a
**separate** `Purchased` hypothesis to prove `PositionsUV`. `Purchased`, defined
in [`YM/FullVolume/Tuned.lean`][tuned], supplies pointwise Cauchy behavior of
the authentic source correlations on generic separated positions. The bounds
support equicontinuity, derivative control, and passage to all suitable tests;
they do not independently establish that Cauchy hypothesis.

Consequently:

- `genuine` is a substantive source-bound analytic estimate, rather than a
  finite numerical observation.
- It supplies uniform control, not decay to zero, phase uniqueness, or a mass
  gap.
- The next convergence theorem still needs another nontrivial analytic input.
- This audit found a specific place where the earlier finite reproduction
  stops; it did not reconstruct the large RG library that proves the input.

## 5. Can SUCC or the BBP source instantiate it?

**No direct instantiation is presently supplied.** There are explicit type and
analytic mismatches, not simply missing terminology.

| Upstream requirement | SUCC/BBP counterpart needed | Present status in this round |
|---|---|---|
| Compact gauge group with nonabelian simple Lie algebra | A valid group and proof of simplicity tied to the arithmetic object | BBP phases lie on an abelian circle; that group fails the hypothesis |
| Product-Haar Wilson law on link configurations | A proved representation of the original zero-seeded arithmetic statistics under that law | No such source-identification map constructed |
| Shared RG history with actual blocking and calibration | Arithmetic coarse-graining maps with source preservation and common units | No adapter to `Family.Makes` constructed |
| Reflection/chessboard bounds on local replicated observables | The corresponding reflected arithmetic inequality, with the same source in every slot | Ordinary positive arithmetic Gram matrices do not supply this |
| Uniform primary root costs and derivative renormalization | Source-specific scale estimates and control of the required difference operators | No BBP version of `Wcmain` or `Run.financed` proved |
| Pointwise Cauchy behavior for the relevant hierarchy | A quantitative arithmetic convergence/cancellation theorem | Not supplied by this bound or by existence of subsequences |

Embedding the circle into diagonal matrices in SU(2) does not repair these
problems: the sampled subgroup remains abelian, and the deterministic BBP
sampling law does not become the nonabelian Wilson law.

Moreover, boundedness of a single arithmetic phase is already elementary:
\(|e^{2\pi i hU_n}|=1\). An analogue that merely bounds such moments would
not give the cancellation of their signed average. For a nontrivial transfer,
SUCC would have to identify the amplified, differentiated, or multiscale
observable whose uniform control closes a specified arithmetic dependency, and
then prove the required source estimates. That task cannot be discharged by
renaming the phase index as a gauge index.

## 6. The concrete next import test

The narrow transferable design is a hierarchy of **source-bound cost
certificates**, with volume/scale quantifiers declared before the estimates.
The next discriminating test is to construct an explicit arithmetic replicated
observable and reflection/transport operation, calculate both sides of its
proposed product bound on the authentic zero seed and hostile comparison seeds,
and determine whether the bound actually controls an unresolved cancellation
term. A successful finite check would remain a finite check until an all-scale
proof supplies the uniform constants and thresholds.

The present verdict is **OBSERVED UPSTREAM THEOREM AND DEPENDENCY MAP**. No
proof replay, new uniform arithmetic estimate, or direct use of `genuine` on
BBP data has occurred. The novelty contribution is locating and typing the
import boundary; the analytic theorem remains attributed to the upstream
construction.

## Pinned source location

All native paths above are relative to `submission/` inside the assessment
package at commit `55ba9fc36293b3f4d52c6b1f813169a0be76ee98`. The linked files
were read as source text. Their presence is covered by the already recorded
9,508-file integrity check, which does not certify their semantics or compilation.

[literal]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Literal.lean
[discrete]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Discrete.lean
[history]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/RG/History.lean
[cross]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Cross.lean
[rent]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Rent.lean
[tiling]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Cells/Tiling.lean
[center]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Extraction/Center.lean
[moneys]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Moneys.lean
[cohort]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Cohort.lean
[certificate]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Cells/Certificate.lean
[embedded]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/Cells/Embedded.lean
[sluggish]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Sluggish.lean
[profiles]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Profiles.lean
[tuned]: https://github.com/yang-mills-group/YM/blob/55ba9fc36293b3f4d52c6b1f813169a0be76ee98/submissions/openai-20261028/submission/YM/FullVolume/Tuned.lean
