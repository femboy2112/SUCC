# Principia Observatoris — A Target-Relative Gauge Pin for Source Authentication

**2026-11-14 · research-only · source ancestry: SUCC PR #629, head `83ade09a46fefa88fbbddfb5bcc483d8f689586f`.** This is a correction to the instrument-first reading of source authentication, motivated by the author's statement: *pin yourself to something gauge in your carrier with respect to your problem; otherwise you incur additional mathematical transport obligations.* No new physical gauge symmetry or empirical experiment is claimed.

## 0. Interpret the proposal faithfully

A *gauge symmetry* means a transformation of **representation** that leaves the specified physical/mathematical target and source laws unchanged. It is not automatically a physical operation, an elapsed-time transition, or a free instrument. A *gauge pin* may mean either:

1. **Gauge fixing:** choose a representative of each gauge orbit via a section of the orbit quotient. This section is usually *not itself equivariant* and may not exist globally as a continuous section.
2. **Relational/internal reference:** construct a source-attached covariant reference `r(x)` and evaluate a diagonal-gauge-invariant comparison `F(x,r(x))`. The comparison is invariant without selecting any global point representative.

The author's operational shortcut is most faithfully expressed by **(2)**. The internal anchor must be given a declared, actually sourced transformation law; simply naming a parameter "gauge" does not make it so. External instruments may still be needed to attest physical costs and validity of the proposed symmetry.

Work in a finite *declared* group action `G ↷ X`, reference space `G ↷ R`, time/action law `T:X→X`, target `P:X→V`, and lawful source joint kernel `J(x,x',o)` when stochastic interactions are used. Require the correct current/source state, causal frame and source label. Gauge orbits `X/G` are equivalence classes of *descriptions*; a pair of gauge-related states need not be two physically distinct sources.

## GA-01 — Relational gauge pinning, exact descent (CLASSICAL / PROVED PAPER)

**Theorem.** Let `r:X→R` be equivariant: `r(gx)=g r(x)`. Let `F:X×R→V` be invariant under simultaneous transformations: `F(gx,ga)=F(x,a)`. Then

\[
P(x)=F(x,r(x))\quad\Longrightarrow\quad P(gx)=P(x).
\]

Proof: `P(gx)=F(gx,r(gx))=F(gx,g r(x))=F(x,r(x))`. Thus there is a unique `\bar P:X/G→V` with `P=\bar P\circ\pi`. This is *target-relative*: not every question factors through `X/G`; a gauge-variant question is not a physical invariant of this action.

**Exact two-bit witness.** `X={(s,r):s,r∈{0,1}}`; the declared descriptive gauge flip is `g(s,r)=(1-s,1-r)`. Choose source-attached reference `a(s,r)=r` with reference transformation `g_R(a)=1-a`, and relational comparison `F((s,r),a)=s XOR a`. Hence `P=s XOR r` is gauge invariant and separates the two genuine gauge orbits. This is a **mathematical binary gauge toy**, not a claim that physical spacetime consists of two bits.

**Negative control:** the fixed *absolute* reference `a_0(s,r)=0` is not equivariant, producing the raw report `s`; gauge-related descriptions disagree. **Second negative control:** reference `a=s` is gauge-covariant but gives `F((s,r),s)=0` identically. Covariance of a reference is **not sufficiency for the target**. It merely removes one representation/transport obstruction.

## GA-02 — Dynamics on gauge orbits (CLASSICAL / PROVED)

If a lawful source update `T:X→X` respects the declared gauge action, `T(gx)=gT(x)`, then

\[
\bar T([x])=[Tx]
\]

is well-defined. Conversely, if a given `T` is not equivariant, an apparent gauge orbit reduction may be illegitimate or require an explicitly transformed action label and connection. A gauge transformation `g` itself is a change of representation, not a paid physical transition.

**Important scope:** when a *readout* `E:X→O` is invariant but coarser than the orbit quotient, equivariance of `T` does **not** imply an observed update `\bar T_O` exists. The exact extra condition is `E(x)=E(y) ⇒ E(Tx)=E(Ty)` (SUCC's preexisting target/descent condition).

**Hostile example.** Add a hidden bit `h` unaffected by the gauge flip, and set `E(s,r,h)=s XOR r`, `T(s,r,h)=(s XOR h,r,h)`. `T` is gauge equivariant and `E` invariant, but sources with the same `E` and different `h` have different next reports. Thus a perfectly lawful relational gauge pin can remain **predictively insufficient**. This is a real missing source variable, not a gauge artefact.

## GA-03 — Joint source law, likelihood and posterior descend to gauge orbits (CLASSICAL / PROVED)

Let a finite joint source kernel satisfy normalization, and let the output `o` be gauge invariant. Assume

\[
J(gx,gx',o)=J(x,x',o)\qquad \text{for all }g,x,x',o.
\]

For gauge-orbit classes `B=[x], C=[x']`, define

\[
\bar J(B,C,o)=\sum_{z\in C}J(x,z,o).
\]

The right-hand side is independent of which representative `x∈B` is used: replacing `x` with `gx` and substituting `z=gw` leaves the sum unchanged. The reduced `\bar J` is a normalized joint kernel; source laws and observation likelihoods are preserved on the quotient.

For a prior `b` on `X`, define `\pi_*b(B)=\sum_{x\in B}b(x)`. When an outcome `o` has positive evidence likelihood, Bayesian update commutes **exactly** with gauge reduction:

\[
\boxed{\pi_*\operatorname{Bayes}_{J,o}(b)=
\operatorname{Bayes}_{\bar J,o}(\pi_*b).}
\]

Proof: multiply both sides by the common positive observation normalization and expand both sides as `\sum_{x∈B}b(x)\sum_{z∈C}J(x,z,o)`. Gauge covariance makes the inner sum depend only on `B`. Divide by the common normalization. If the denominator is zero, **no posterior is defined**, as in RFO-02. **No gauge-invariance assumption on the prior is needed** to predict *gauge-invariant* future outcomes under the source law. The full prior's within-orbit content need not be recovered.

Actions and observed outcomes with nontrivial gauge representations require their appropriately transformed indices. Omitting those indices is not a theorem; this package deliberately tests only trivial output action and one fixed physical intervention. A conditional cost expectation also descends if the cost is invariant on the relevant joint source/outcome gauge orbits. It does not descend merely because a cost table exists.

**Executable positive control:** source `(s,r)` physically flips `s`, and emits old relational parity correctly with probability `3/4`. A gauge-related pair has the same transformed source likelihood; the 2-orbit joint model filters exactly as the 4-source model. The independent closed-form implementation checks 1,248 exact rational prior/outcome comparisons; the primary tests use another 150 seeded priors plus point masses.

**Negative control:** reading the *absolute* pre-intervention `s` with `3/4` accuracy breaks gauge covariance. The correct verdict is **not** to marginalize it as an invariant physical source instrument; its orientation calibration/refinement must be supplied or the gauge claim withdrawn. Changing an action to an absolute reset can similarly violate covariance. The model should fail closed.

## GA-04 — Choice sections and the reference are different objects (CLASSICAL / STRICT)

Previous SUCC [PR #626](https://github.com/femboy2112/SUCC/pull/626) shows no equivariant point section of the orbit quotient for a nontrivial free group orbit. This does **not** obstruct a *source-attached covariant reference* `r:X→R`. In our two-bit model, the orbit quotient has no equivariant section because no source point is fixed by the flip, but `r(s,r)=r` is an equivariant map into the two-point reference space and `s XOR r` remains invariant.

The correct distinction is:

- `σ:X/G→X` chooses an orbit representative and need not be equivariant; global continuous choice can fail on nontrivial bundles.
- `r:X→R` travels with the carrier and need not select a unique global representative.
- `P=F(x,r(x))` is the *invariant* problem-target readout.

An internal reference does not magically remove genuine bundle holonomy, gauge-patch transitions or source-map mismatch; it changes the proof burden to explicit, typed equivariance/transition checks. In nontrivial continuous gauge geometries, patchwise reference fields and coherent overlap maps can be necessary (classical gauge theory; see the primary and lecture sources below).

## GA-05 — Gauge-physical distinction changes FuckedField diagnostics (CLASSICAL SUCC SYNTHESIS)

Given lawful evidence `E` and a target `P`, the original SUCC target-nonidentifiability condition remains:

\[
\exists x,y:\quad E(x)=E(y),\quad P(x)\ne P(y).
\]

But if `G` is a *genuine physical gauge redundancy*, a target of **physical source identity** must be well-defined on the gauge quotient, i.e. `P(gx)=P(x)`. Calling an unobservable **gauge-variant coordinate** a physical `FuckedField` target would misclassify a mere convention as missing physics.

On the two-bit model `E=P=s XOR r` exactly resolves the physical gauge orbits; the raw coordinate `s` remains unknown because it is gauge variant. That is **not** a failure of physical source identification. Add the gauge-invariant hidden bit `h` and let the permitted observer see only `s XOR r`; then `P_h=h` differs on genuinely inequivalent source orbits while every current report is identical. If permitted future probes also ignore `h`, this is a genuine toolkit-relative nonidentifiability obstruction. In the action `T(s,r,h)=(s XOR h,r,h)`, however, later observations can reveal `h` if the observer can apply `T` and retain time-indexed reports: the present-time gap is **not** a proof of all-future nonidentifiability.

Thus the honest classification is still `FieldClass(Source, Target, Tools)`, but before classifying physical targets test whether the proposed gauge transformations are actual source-law symmetries and whether the target is gauge invariant. SimpleField for invariant prediction can coexist with nonidentifiability of **another gauge-invariant physical variable**; IdealHard and the other Fucked modes retain their preexisting proof obligations.

## GA-06 — Pinning as minimization of mathematical transport debt (CONJECTURED as optimization slogan)

A source-attached covariant reference reduces the need to track arbitrary absolute-frame shifts in gauge-invariant predictions. That is a **proved algebraic saving** in GA-01/03; it is not a universal theorem that all gauge pins are cheaper, easier to measure, or better conditioned.

An anchor that is not covariant needs an explicitly supported comparison/compensation map. One can measure the mismatch **only after declaring a common target space**, e.g. the predicate `r(gx)\neq g r(x)`. If a numerical defect is desired, also specify a norm, signs, units, or transported basis. A source-derived gauge pin may itself be inaccessible, ambiguous, unstable under noise, or globally obstructed. Avoid assigning a fake scalar `gauge quality` score.

**Operational research contract:** declare `(Source, Target, Tools, G, source joint J, reference r, readout F, cost C, future action/policy)`. Check `G` preserves actual source laws and intended target; check reference equivariance and diagonal readout invariance; test whether observed dynamics/likelihood/cost descend; then conduct source-authenticated holdouts. An unmeasured future source is not authenticated just because a group-theoretic diagram commutes.

## Evidence and next verdict-changing probe

- **PROVED PAPER / classical finite group algebra:** GA-01, GA-02, GA-03, and section-versus-reference distinction GA-04.
- **OBSERVED exact finite computation:** 17/17 standard-library tests; 150 seeded-prior quotient checks plus four point-mass controls; 1,248 independent closed-form outcome/posterior comparisons; compileall passes. These are model tests, not empirical source calibration.
- **REFUTED general claims by explicit countermodels:** arbitrary absolute pin is physical gauge-invariant evidence; gauge-equivariant reference always identifies the desired target; gauge-equivariant source update automatically descends through any coarser invariant readout; orbit gauge freedom creates a genuine FuckedField physical defect.
- **UNVERIFIED:** that the declared two-bit flip symmetry (or any proposed SUCC physical symmetry) corresponds to an actual external carrier; any measured joule/timing meter; physical clock/G orbits; historical source identity; RH/π normality/GR implications.

**Next test:** run the source-authentication experiment from PR #629 using a *predeclared relational output channel*, compare against an absolute-orientation hostile mutant, and include a separate source-marked reference readout. Ensure the observation channel, intervention, and paid clock/energy meter are all calibrated on the *same source frame*. On actual hardware, report unavailable instrument access or missing calibration as **ACCESS GAP**, not as a theorem that the source has no gauge. Keep a fresh holdout in which an undetected variable alters gauge-invariant future predictions.

**SUCC source-context references:** [PR #629 source authentication](https://github.com/femboy2112/SUCC/pull/629), [PR #628 recursive observer](https://github.com/femboy2112/SUCC/pull/628), [PR #626 equivariant choice](https://github.com/femboy2112/SUCC/pull/626), [covariant observer frames on main](https://github.com/femboy2112/SUCC/blob/main/observational_succ/covariant_observer_frames.py), and [target-relative field taxonomy on main](https://github.com/femboy2112/SUCC/blob/main/docs/OBSERVER_PROOF_ACCESS.md).

**External classical context:** Leonardo Chataignier (2021), *Relational observables, reference frames, and conditional probabilities*, Phys. Rev. D 103, 026013, DOI 10.1103/PhysRevD.103.026013; I. M. Singer (1978), *Some Remarks on the Gribov Ambiguity*, Commun. Math. Phys. 60, 7–12; V. P. Nair, *The topology and geometry of C*, lecture notes (2023) on local versus global gauge sections. No academic-priority claim is made.
