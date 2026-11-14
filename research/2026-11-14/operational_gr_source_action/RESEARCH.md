# Principia Observatoris — The Source/Entropy/Action Gate to Einstein Dynamics

**Date:** 2026-11-14. **Status:** scoped classical mathematical deductions, exact finite tests, and explicit no-go countermodels. **Not** a derivation of physical GR solely from observer gluing. **No new physical measurements, source-map attestation, Lean certificate, RH or pi-normality result.**

**Parent:** [Operational Lorentz / tensor tomography, PR #623](https://github.com/femboy2112/SUCC/pull/623). The prior ten-timelike-observer tomography is used as a separate established finite observer instrument. The present note studies the additional **physical source and coupling** problem.

## 0. Prime question and the correct answer

Can one obtain **one** physically meaningful Lorentzian metric, matter energy law, horizon entropy, and gravitational dynamics from **one** authenticated observer carrier *without putting Einstein's equations in as an assumption*?

**Conclusion:** (i) from causal and massless coordinate-field records alone, no: two explicit smooth source completions have identical records but different curvature; (ii) from a sufficiently calibrated metric and a restricted local matter constitutive ansatz, one can derive a matter stress tensor, but its normalization is still independent; (iii) from a boundary entropy *postulate*, Unruh temperature, local equilibrium and Raychaudhuri focusing, one can derive Einstein's equation without inserting the Einstein-Hilbert field equation as an axiom (Jacobson 1995). **Those extra physical statements are not consequences of the SUCC observer axioms, and no source-faithful empirical calibration has been supplied.**

For the source, distinguish:

- **Observed carrier:** event labels, actual readout transcripts, permitted preparations/interventions, clock and energy calibration where available.
- **Candidate completion:** a metric, source probability law, field action, and horizon microphysics consistent with those records.
- **Physical authentication:** an independently tested claim that the candidate laws and scales really describe the intended world; not the same as exact computation with model labels.

The exact claim is **non-identifiability given a restricted toolkit**, not universal unknowability.

## 1. Exact continuous countermodel: same causal fabric, same massless field, different curvature (OGS-01)

Take the smooth patch \(M=\{(t,x):t<1\}\), time orientation increasing in \(t\), and the two declared Lorentz metrics

\[
 g_0=-dt^2+dx^2,\qquad g_1=\Omega(t)^2g_0,\quad \Omega(t)=(1-t)^{-1}.
\]

They have identical null cones, chronological/causal order, and all readouts that depend only on this causal ordering. Their curvatures, with \(R_{ab}=\partial_c\Gamma^c_{ab}-\partial_b\Gamma^c_{ac}+\cdots\), are

\[
R[g_0]=0,\qquad R[g_1]=2.
\]

The classical massless scalar action for a **fixed kinetic coefficient** \(Z>0\) is

\[
 S_Z[g,\phi]=-\frac Z2\int_M\sqrt{-g}\,g^{ab}\partial_a\phi\partial_b\phi\,dtdx.
\]

In **two** spacetime dimensions, \(\sqrt{-g_1}=\Omega^2\sqrt{-g_0}\) and \(g_1^{ab}=\Omega^{-2}g_0^{ab}\). Hence the entire coordinate action density is identical for all \(\phi\), and the field equation \(\Box_{g_1}\phi=\Omega^{-2}\Box_{g_0}\phi=0\) has exactly the same solution set, including all \(F(t-x)+G(t+x)\).

Even the covariant coordinate stress components agree:

\[
 T^{(Z)}_{ab}=Z\bigl[\partial_a\phi\partial_b\phi-\tfrac12g_{ab}g^{cd}\partial_c\phi\partial_d\phi\bigr],
\]

because \(g_{ab}g^{cd}\) is conformally invariant. Thus **causal order + arbitrary coordinate massless-scalar field solutions + their local coordinate action densities and covariant stress components** do not determine \(R\) for this toolkit. The two metrics are different candidate completions of the same accessible source data. The common scalar is not an authenticated physical particle model.

A calibrated clock breaks this particular ambiguity: a static observer measures \(d\tau/dt=\Omega(t)\). For example at \(t=1/2\), the rates are 1 and 2. The normalized energy \(T_{ab}u^au^b=T_{tt}/\Omega^2\) also differs if it is physically calibrated, even though \(T_{tt}\) as a coordinate component agrees.

**Boundary:** this is a property of the *classical massless scalar* in \(1+1\), not of arbitrary matter. In dimension \(d\), the corresponding massless density scales as \(\Omega^{d-2}\), so the direct scalar-action invariance fails in \(d=4\). The 4D Maxwell field provides a different conformally invariant example. The two-dimensional Einstein tensor is identically zero; the countermodel is an identifiability result, not a local 2D Einstein-dynamics model.

## 2. Finite probes cannot establish a smooth global conformal scale (OGS-02)

Fix finitely many observed times \(t_i\) and a maximum jet order \(m\ge0\). For \(\varepsilon\ne0\), let

\[
\sigma(t)=\varepsilon\prod_i(t-t_i)^{m+1},\qquad \widetilde g=e^{2\sigma(t)}g_0.
\]

Every derivative of \(\sigma\) through order \(m\) vanishes at every \(t_i\), so the metric and its derivatives through order \(m\) agree there with the flat reference. All null cones agree **everywhere**. Yet \(\sigma\) is nonconstant, and on open subsets \(R[\widetilde g]=2e^{-2\sigma}\sigma''\) is nonzero (choose \(m\ge2\) for curvature-jet equality at the sampled points). Thus a finite fixed-order probe bank, without a source restriction on \(\sigma\), cannot determine global curvature even if those measurements are exact. For \(t_i=0,1/2\), \(m=2\), \(\sigma=t^3(t-1/2)^3\), its 0/1/2 jets vanish at both points but \(\sigma''(1/4)=3/128\). This is a **constructible finite-horizon witness**, not a claim that analytic continuation from a full open set is impossible.

## 3. Causal order plus *uncalibrated* event density retains a scale gauge (OGS-03)

For a \(d\)-dimensional candidate continuum with Poisson event sprinkling of intensity \(\lambda\) per physical volume, the mean count in a region \(D\) is

\[
\mathbb E N(D)=\int_D\lambda(x)\sqrt{|g(x)|}\,d^dx.
\]

For any positive \(\Omega\), the joint transformation

\[
 g\mapsto\Omega^2g,\qquad \lambda\mapsto\Omega^{-d}\lambda
\]

preserves both causal order and the complete Poisson count law on each coordinate-defined measurable region. Hence count data do **not** determine the conformal scale if source event density is an unrestricted unknown field. If \(\lambda\) is promised *constant but unknown*, this argument directly leaves only a **global** scale ambiguity, not an arbitrary local Weyl ambiguity. If \(\lambda\) is independently known, continuum causal order plus volume is the classical reconstruction route (subject to manifold/causal assumptions), though one finite random realization is not exact volume tomography.

This is an operational calibration-gauge example, not proof that causal set quantum gravity recovers the continuum uniquely.

## 4. Matter energy from the same field dynamics: normalization debt (OGS-04)

Given a **calibrated** Lorentz metric and a minimally coupled Lorentz-invariant, shift-symmetric local scalar ansatz quadratic in first derivatives, **without curvature-dependent coefficients, higher derivatives or extra background tensors**, the nontrivial bulk kinetic term is, up to an overall coefficient \(Z>0\) and total divergences,

\[
S_Z=-\frac Z2\int\sqrt{-g}\,g^{ab}\nabla_a\phi\nabla_b\phi.
\]

Its Euler–Lagrange equation is \(Z\Box_g\phi=0\), so a complete noiseless record of field *solutions alone* does not identify \(Z\). Metric variation, however, gives the Hilbert matter tensor

\[
 T_{ab}^{(Z)}=Z\bigl(\nabla_a\phi\nabla_b\phi-\tfrac12g_{ab}\nabla_c\phi\nabla^c\phi\bigr).
\]

The physical null energy flux is \(T_{ab}k^ak^b=Z(k\cdot\nabla\phi)^2\). If one independently calibrated nonzero energy density/flux is available, it can fix \(Z\) for the declared action. That is an **additional instrument**, not an inference from the wave equation. More general interactions, fields, higher derivatives, or curvature couplings require their own constitutive laws.

## 5. Exact nine-null-direction rigidity and the cosmological ambiguity (OGS-05)

**Theorem (finite local algebra, proved here).** Let \(S\) be any real symmetric \(4\times4\) tensor in a known oriented Lorentz-orthonormal frame \(\eta=\operatorname{diag}(-1,1,1,1)\). Define nine null vectors:

- \(k_i^\pm=(1,\pm e_i)\) for \(i=1,2,3\), six vectors;
- \(k_{ij}=(1,\tfrac35e_i+\tfrac45e_j)\) for \(1\le i<j\le3\), three vectors.

Then

\[
\boxed{\forall k\text{ in these nine},\ S_{ab}k^ak^b=0\quad\Longleftrightarrow\quad S_{ab}=f\eta_{ab}\text{ for some }f.}
\]

The nine linear functionals are independent; **nine are necessary and sufficient among independent scalar null contractions** to identify the class of an arbitrary symmetric tensor modulo multiples of \(\eta\). This is a finite-algebraic statement, not a measurement of actual gravity.

**Proof.** The two axis signs imply \(S_{0i}=0\) and \(S_{ii}=-S_{00}\). Each mixed null vector then has zero contraction only if \((24/25)S_{ij}=0\), so all spatial off-diagonals vanish and \(S=-S_{00}\eta\). Conversely every multiple of \(\eta\) has zero null contraction. The kernel of the nine readout functionals on the 10-dimensional space of symmetric tensors is thus one-dimensional, so their rank is nine. Fewer than nine scalar equations cannot have such a kernel in general. Exact rational rank/ablation is checked independently in the native probe.

**Interpretation.** Let \(S_{ab}=R_{ab}-\kappa T_{ab}\), with \(\kappa\) an independently sourced coupling. If calibrated null-focusing and matter flux data establish \(S_{ab}k^ak^b=0\) for these nine directions *at an event*, then \(R_{ab}-\kappa T_{ab}=f g_{ab}\) **at that event**. If the relation is supplied throughout a connected smooth spacetime, the contracted Bianchi identity and \(\nabla^aT_{ab}=0\) give \(\nabla_b f=\tfrac12\nabla_b R\), hence \(f=R/2-\Lambda\) with constant \(\Lambda\). Therefore

\[
\boxed{G_{ab}+\Lambda g_{ab}=\kappa T_{ab}.}
\]

This is a **conditional derivation** of the tensor equation from null contraction data plus conservation, not an assumption of the Einstein field equation. It does not derive the null contraction relation, calibration, or conservation from observer gluing. A finite set of nine measurements at one event cannot establish a global field equation. The multiple-of-metric ambiguity explains why null observations do not directly determine a cosmological term or a scalar potential \(V(\phi)g_{ab}\).

## 6. An exact boundary-bit entropy law — and what it fails to determine (OGS-06)

Declare a finite boundary with \(N\) distinguishable **independent, equiprobable** two-state microvariables. Its microstate space has cardinality \(2^N\) and Shannon entropy (\(k_B=1\))

\[H_N=N\log 2.\]

If an *independent geometric calibration* assigns area \(A_N=Na_0\) for a fixed positive cell area \(a_0\), then at those discrete areas

\[\boxed{H_N=\alpha A_N,\qquad \alpha=\frac{\log 2}{a_0}.}\]

This is an exact combinatorial derivation **conditional on independence, equiprobability, a two-state boundary algebra, and calibrated cell area**. It is not a derivation of Bekenstein–Hawking entropy or of the physical horizon microstates. The differential law \(dS=\alpha dA\) used on arbitrary infinitesimal local horizons is an additional continuum/equilibrium extension of the discrete counting model.

**Countermodel:** use the same \(N\) hidden bits and the same causal/observer transition maps, but let the inaccessible microstate distribution be a point mass. The observable records remain identical when these bits are not probed, whereas entropy changes from \(N\log2\) to 0. Correlations or gauge constraints can also lower the entropy. Causal reachability alone cannot determine the source's microstate distribution, its entropy, or the physical area unit.

## 7. Conditional closure to Einstein dynamics without assuming the equation (OGS-07)

A controlled route, due to **Jacobson (1995)**, introduces the following *additional physical assumptions* at every event and for every local causal-horizon null direction:

1. A smooth Lorentzian metric and its Levi–Civita Raychaudhuri focusing law.
2. A local Rindler boost horizon, the Unruh temperature \(T_U=\hbar\kappa_H/(2\pi)\) (\(c=k_B=1\)), and a physically defined heat flux \(\delta Q\) from the **calibrated matter** stress tensor.
3. Local equilibrium at the reference event (the relevant expansion and shear vanish), and a universal *constant* horizon entropy density \(\delta S=\alpha\delta A\) (\(\alpha>0\)).
4. The Clausius identity \(\delta Q=T_U\delta S\) for **all** such local horizons, plus \(\nabla^aT_{ab}=0\).

Use the same affine parameter \(\lambda\) on the null generators (not the sprinkling rate of §3). At leading order near equilibrium, Raychaudhuri gives \(\delta A\propto\int(-\lambda)R_{ab}k^ak^b\,d\lambda\,dA\), and the boost energy flux divided by Unruh temperature gives \(\delta Q/T_U\propto(2\pi/\hbar)\int(-\lambda)T_{ab}k^ak^b\,d\lambda\,dA\). The Clausius identity for all null directions thus gives

\[
\boxed{R_{ab}k^ak^b=\frac{2\pi}{\hbar\alpha}T_{ab}k^ak^b\quad\text{for every null }k.}
\]

Applying OGS-05 or the standard null-tensor polarization lemma, then Bianchi and conservation, yields Einstein's equation with

\[
\boxed{G_{\mathrm{eff}}=\frac{1}{4\hbar\alpha}}\qquad (c=k_B=1).
\]

If the boundary-bit toy of §6 additionally supplies the *physical* horizon entropy in a justified scaling/equilibrium limit, it would imply \(G_{\mathrm{eff}}=a_0/(4\hbar\log2)\). **Neither physical horizon identification, local thermodynamic equilibrium, Unruh physics nor the cell-area calibration is derived here**. We have not proved that actual finite SUCC observer records meet these hypotheses. This reproduces an established conditional route, not a new derivation of gravity from information alone.

### The normalization-gauge residual

If the scalar kinetic action has coefficient \(Z\), then \(T_{ab}=Z\,\mathcal T_{ab}\) for the fixed coordinate field and calibrated metric. The gravitational response coefficient multiplies it as

\[\frac{2\pi}{\hbar\alpha}T_{ab}=\frac{2\pi Z}{\hbar\alpha}\mathcal T_{ab}.\]

Without an **absolute entropy/energy normalization instrument**, simultaneous rescaling \((Z,\alpha)\mapsto(cZ,c\alpha)\) with \(c>0\) leaves the classical scalar equation, metric equations from the above thermodynamic route, and calibrated dimensionless geometry intact, while changing the separate assigned energy and entropy scales. Quantum phases or independent energy/entropy calibration can distinguish those completions; no such invariance is claimed for all quantum readouts. This is an operational **normalization non-identifiability**, not a new gauge symmetry of physical GR.

## 8. A genuine dynamics non-identifiability countermodel (OGS-08)

Even if the metric is calibrated and the Einstein–Hilbert action is *one* working candidate, its uniqueness is not implied by observing only maximally symmetric backgrounds.

For any real \(\beta\), consider a 4D gravitational action differing by \(\beta\int\sqrt{-g}R^2\). The variation of the additional bulk term contributes (up to the common overall coefficient)

\[
H_{ab}=2R R_{ab}-\tfrac12R^2g_{ab}+2(g_{ab}\Box-\nabla_a\nabla_b)R.
\]

On any **four-dimensional Einstein metric**, \(R_{ab}=R g_{ab}/4\) with constant \(R\), so every term cancels: \(H_{ab}=0\). Minkowski and de Sitter vacuum-background observations therefore cannot by themselves distinguish \(\beta=0\) from \(\beta\ne0\) on the shared solution backgrounds. A source that probes non-Einstein curvature or off-shell variations can distinguish them. The physically justified horizon entropy in higher-curvature theories is generally a *Wald/Noether* entropy, not a universal constant \(\alpha A\); this is why the added thermodynamic postulate is load-bearing. See Lovelock for uniqueness under more restrictive assumptions.

Thus we **have not derived the physical gravitational action** from observer transport, and it would be circular to impose the second-order metric action and announce the Einstein action as source-generated.

## 9. Status and immediate next falsifier

| ID | Result | Authority | Unpaid debt |
| --- | --- | --- | --- |
| OGS-01 | Causal and classical 2D scalar-action/stress equivalence with different curvature | CLASSICAL / PAPER PROVED; symbolic + exact controls | Physical source adequacy |
| OGS-02 | Finite metric jets do not fix global conformal scale | PAPER PROVED / symbolic finite witness | Source complexity promise could repair |
| OGS-03 | Sprinkling-rate/volume calibration gauge | CLASSICAL / PAPER PROVED; exact rational controls | Density authentication |
| OGS-04 | Scalar action scale not identified by wave dynamics | CLASSICAL / PAPER PROVED | Independently measured energy normalization |
| OGS-05 | Nine-null readouts determine symmetric tensor modulo metric | PAPER PROVED; exact 9×10 rank and ablations | Physical null focusing/energy readouts and global law |
| OGS-06 | Binary independent boundary area law | CLASSICAL CONDITIONAL / EXACT COUNT | Microstates, area cells, continuum equilibrium |
| OGS-07 | Jacobson thermodynamic route plus OGS-05 ⇒ EFE | CLASSICAL CONDITIONAL, original-source assumptions NOT ESTABLISHED | Derive/source-calibrate physical entropy and heat law |
| OGS-08 | EH+βR² cannot be distinguished on 4D Einstein backgrounds | CLASSICAL / PAPER PROVED; symbolic control | Off-background source probes |

**Suggested next discriminating experiment:** construct one *source-selected* 3+1 observer carrier with independently calibrated timelike clocks, causal null directions, scalar field preparations, and energy-flux sensors. Predeclare nine null focusing/flux comparisons and one independent trace/scale probe. Test (a) Einstein plus scalar against (b) a \(R+\beta R^2\) rival on a *non-Einstein*, explicitly constructible background. Measure the residual of the Clausius/focusing identity before fitting \(\alpha, Z\), with a source-held-out metric and hostile calibration shifts. The absolute source/entropy calibration is the decisive missing instrument. Do not turn an assumed Einstein background into a validation of Einstein dynamics.

## 10. Primary mathematical/physical predecessors

- Ehlers, Pirani & Schild (1972), *The Geometry of Free Fall and Light Propagation*, https://bpfoundations.org/plans/ehlers2012.pdf — causal, projective and metric operational layers.
- Hawking–King–McCarthy/Malament causal reconstruction; modern mathematical review: https://link.springer.com/article/10.1007/s41114-019-0023-1 — causal order + calibrated volume.
- Jacobson (1995), *Thermodynamics of Spacetime: The Einstein Equation of State*, https://arxiv.org/abs/gr-qc/9504004 — local-horizon area entropy, Unruh temperature, Clausius and Raychaudhuri imply Einstein equation under assumptions.
- Eling, Guedens & Jacobson (2006), *Non-equilibrium Thermodynamics of Spacetime*, https://arxiv.org/abs/gr-qc/0602001 — curvature entropy corrections need non-equilibrium treatments.
- Wald (1993), *Black Hole Entropy is Noether Charge*, https://arxiv.org/abs/gr-qc/9307038 — gravity-action-dependent entropy.
- Lovelock (1971), *The Einstein Tensor and Its Generalizations*, DOI:10.1063/1.1665613 — 4D divergence-free natural tensor uniqueness under specific metric/derivative restrictions.
- Causal sets and an emerging continuum (2024), https://doi.org/10.1007/s10714-024-03281-1 — interval-counting and discrete action program (not directly imported as proof).

**SUCC provenance:** original founding/second-forge observer work #618–#620, historical Lorentz GL #39, twin Lorentz/energy #393/#394, 3+1 rank/waves #402, spinor #604, and parent observational GR #623. No original BBP source, zero seed, historical claim ledger, or frozen source data changed.
