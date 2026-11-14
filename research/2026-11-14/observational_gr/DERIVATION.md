# Principia Observatoris — Operational Lorentz Geometry and Stress–Energy

**Research round:** 2026-11-14 · **Scope:** conditional reconstruction and a finite observer-tomography theorem, not derivation of gravitational physics from observer agreement alone. **Status:** CLASSICAL/PAPER PROVED where specifically marked, EXACT FINITE TESTS for the toy carrier, physical source-map adequacy UNVERIFIED. No RH/π-normality/quantum-gravity result.

## 0. The proposed bridge, with the missing implications shown

The author's “observer = triangle; two agreeing observers = a quadrilateral made of two triangles” is interpreted as a source-relative commutative diagram. If two observers report `q_A(s),q_B(s)` from a source `s`, and comparison maps `c_A,c_B` target a common chart `C`, **agreement** is

\[c_A\circ q_A=c_B\circ q_B\quad\text{on the declared source class}.\]

This is a well-typed, checkable agreement condition. It does **not** imply a spacetime dimension, metric, signature, light cone, affine connection, curvature, or energy–momentum tensor. A commuting square is not spacetime curvature. To construct GR one needs additional declarations and checks:

1. A sufficiently rich space of events with an observation atlas and lawful overlaps (smooth manifold when invoking ordinary differential GR).
2. Oriented causal/null structure, physically calibrated by propagation and clocks; no uncontrolled identification of correlation with signaling.
3. A conformal factor from proper time/length or independently calibrated volume; timelike free-fall trajectories if reconstructing the affine/projective structure from operations.
4. A compatible Lorentzian metric, tetrads and connection (usually Levi–Civita: metric-compatible, torsion-free).
5. A constitutive matter law/action, and an independent gravitational dynamics postulate; ordinary Einstein equations follow from Einstein–Hilbert + matter action, **not** from agreement alone.

This roadmap is an **operational formulation** in contact with established Ehlers–Pirani–Schild and causal reconstruction results, not an assertion of new scholarly priority.

## 1. Conditional lightcone-and-clock reconstruction in 1+1 dimensions — OGR-01

Work in one tangent plane with coordinates `(t,x)`, units `c=1`. Let a *declared* symmetric bilinear form be

\[g=\begin{pmatrix}a&b\\b&d\end{pmatrix}.\]

Suppose a calibrated observer has two independent, oppositely oriented null tangents `n_+=(1,1)` and `n_-=(1,-1)` and a normalized timelike clock `e_0=(1,0)` obeying `g(e_0,e_0)=-1`. Then

\[a+2b+d=0,\quad a-2b+d=0,\quad a=-1.\]

Subtracting fixes `b=0`; adding gives `d=-a=1`. Therefore:

\[\boxed{g=\operatorname{diag}(-1,1).}\]

**Proof scope:** uniqueness is for symmetric bilinear forms on this fixed tangent plane, with exactly these calibrated directions and clock. Without the clock, every `Ω²g`, `Ω>0`, has the same null rays. With only one null direction and the clock there is a one-parameter family `g_b=[[-1,b],[b,1-2b]]`, Lorentzian for `b≠1`, matching those two measurements. Therefore both null directions and the clock carry independent identification work. This recovers the spirit of SUCC's earlier GL4 result in PR #39, not a new theorem of relativity.

For a smooth Lorentzian manifold of dimension `d≥3`, under the appropriate distinguishing and regularity hypotheses, the causal order determines the conformal metric rather than its scale (Malament/HKMM). Given a **positive calibrated volume density** `ν`, a representative `g_0` of that conformal class determines

\[g=Ω^2g_0,\qquad Ω=\left(\frac{ν}{\sqrt{|\det g_0|}\,|dx^0\wedge\cdots\wedge dx^{d-1}|}\right)^{1/d}.\]

This is an elementary conditional *volume-fixing lemma*: `vol_(Ω²g₀)=Ω^d vol_g₀`. The operation assumes `ν` and `g₀` are on one manifold with a calibrated source correspondence. **Neither is produced by a four-corner diagram.**

### Exact Lorentz boost — OGR-02

Let `u=t−x` and `v=t+x`, so `ds²=−du dv`. A linear, time-oriented map respecting the two null directions has `u'=αu`, `v'=βv` with `α,β>0` (up to exchanging rays). It preserves null cones for arbitrary `αβ>0`; it preserves **the calibrated interval** only when `αβ=1`. Write `α=e^θ`, `β=e^(−θ)`:

\[\begin{pmatrix}t'\\x'\end{pmatrix}=\underbrace{\begin{pmatrix}\cosh θ&−\sinh θ\\−\sinh θ&\cosh θ\end{pmatrix}}_{Λ(θ)}\begin{pmatrix}t\\x\end{pmatrix},\qquad Λ^TηΛ=η.\]

Then `v_rel=tanh θ` in units `c=1`. For `tanh(θ/2)=1/2`, the exact rational Lorentz matrix is `[[5/3,−4/3],[−4/3,5/3]]`. **The invariant speed and clock normalization are independent inputs.**

## 2. Four real components and the spinor/Lorentz bridge — OGR-03

A particularly clean **declared** 3+1-dimensional carrier is the real vector space `Herm₂(C)`, of dimension four. Encode an event-vector in units `c=1` as

\[X=tσ_0+xσ_1+yσ_2+zσ_3=\begin{pmatrix}t+z&x−iy\\x+iy&t−z\end{pmatrix}.\]

Direct determinant expansion gives

\[\boxed{\det X=t^2−x^2−y^2−z^2.}\]

For `A∈SL₂(C)`, `X↦AXA†` preserves Hermiticity, future-timelike orientation, and this determinant, hence induces a proper orthochronous Lorentz transformation. The kernel on the connected group is `{±I}`: this is the classical spin double cover. **Four real components do not mean this is the quaternion division algebra.** The extra operation and determinant are required.

This exact bridge already appears as a separately scoped mathematical object in SUCC PR #604. It is not a derivation of physical 3+1 spacetime from a four-point square. The exact rational diagnostic here tests the diagonal `A=diag(r,r⁻¹)` subgroup for 99 independent rational event-vectors.

## 3. Observer gluing versus genuine curvature — OGR-04

Suppose overlapping observer charts `x_A,x_B` exist on a smooth event manifold. Their Jacobians `J_BA=∂x_B/∂x_A` must transport metric components by

\[g_A=J_{BA}^Tg_BJ_{BA}.\]

On triple overlaps, transition functions satisfy the **exact Čech cocycle law** `f_CA=f_CB∘f_BA`. A failure is inconsistent atlas gluing, not physical Riemann curvature.

At a point choose a tetrad `e^a{}_{μ}` and Minkowski form `η_ab=diag(−1,1,1,1)`:

\[\boxed{g_{μν}=η_{ab}e^a{}_{μ}e^b{}_{ν}.}\]

Local Lorentz changes `e'{}^a{}_μ=Λ^a{}_b e^b{}_μ`, `Λ^TηΛ=η`, preserve `g`. For metric-compatible torsion-free geometry, the Levi–Civita connection `Γ[g]` is determined by `g`; the spin connection `ω^a{}_{bμ}` follows from `∇_μe^a{}_{ν}=0`. Its curvature two-form is

\[F_{μν}=∂_μω_ν−∂_νω_μ+[ω_μ,ω_ν],\qquad [∇_μ,∇_ν]V^ρ=R^ρ{}_{σμν}V^σ.\]

A small loop of area `Δx^μΔx^ν` transports a frame by `I+F_{μν}Δx^μΔx^ν+O(Δ^3)` for a declared loop orientation/sign convention. This is the mathematically appropriate observer-square curvature instrument. It requires a *connection*, not only agreement of descriptions.

### Two-dimensional gravitational no-go — OGR-05

In dimension two the Riemann tensor of a Levi–Civita metric has only one independent algebraic curvature component, so `R_{μν}=(R/2)g_{μν}`. Therefore

\[\boxed{G_{μν}=R_{μν}−\tfrac12Rg_{μν}\equiv0\quad\text{in 1+1 dimensions}.}\]

Curvature need **not** vanish: for `ds²=−dt²+a(t)²dx²`, direct Christoffel calculation gives `R=2a''/a`; the Einstein tensor still vanishes. In ordinary Einstein gravity, nontrivial local metric dynamics require more structure and suitable spacetime dimension. This is a precise reason why two triangles/one square alone cannot yield the physical 3+1 Einstein equations.

## 4. Causal cones alone cannot determine Einstein curvature — OGR-06

Use conformal time `η<0` in 3+1 dimensions. Compare

\[g_0=−dη²+dx²+dy²+dz²,\qquad g_1=\frac{1}{H²η²}g_0\quad(H>0).\]

Since `g_1(v,v)=(H²η²)^{-1}g_0(v,v)`, the two geometries have **identical causal cones** on their common patch. Nevertheless, direct Levi–Civita computation gives

\[R[g_0]=0,\qquad R[g_1]=12H²,\qquad G_{μν}[g_1]=−3H²(g_1)_{μν}.\]

This is flat Minkowski versus a conformal chart of de Sitter spacetime. The missing conformal scale changes curvature and any stress tensor inferred using Einstein equations. **Therefore:** observer causal agreement by itself does not identify curvature, matter, or Λ. A separately justified scale probe is essential. Independent SymPy calculation checked the full 1+1 and 3+1 Ricci contractions, not only scalar substitutions.

## 5. Operational reconstruction of symmetric stress–energy — OGR-07

A symmetric covariant stress–energy tensor `T_{μν}` at a *single* event has 10 real components in 3+1 dimensions. With metric `η=diag(−1,1,1,1)`, an observer of known future unit-timelike four-velocity `u` measures **energy density**

\[ρ(u)=T_{μν}u^μu^ν.\]

Fix a rational velocity `s` with `0<s<1/√2`. Let `e_i` denote the spatial axes, and let

\[u_0=(1,0,0,0),\quad u_i^±=\frac{(1,±se_i)}{\sqrt{1−s²}},\quad u_{ij}=\frac{(1,se_i+se_j)}{\sqrt{1−2s²}}\quad(i<j).\]

There are `1+6+3=10` distinct timelike directions. Write their densities `ρ₀,ρ_i^±,ρ_ij`. Define `q_i^±=(1−s²)ρ_i^±` and `q_ij=(1−2s²)ρ_ij`. Direct quadratic expansion gives the explicit inverse:

\[\begin{aligned}
T_{00}&=ρ_0,\\
T_{0i}&=\frac{q_i^+−q_i^-}{4s},\\
T_{ii}&=\frac{\tfrac12(q_i^++q_i^-)−ρ_0}{s²},\\
T_{ij}&=\frac{q_{ij}−ρ_0−2s(T_{0i}+T_{0j})−s²(T_{ii}+T_{jj})}{2s²}\quad(i<j).
\end{aligned}\]

These formulae prove that ten chosen scalar readouts determine `T` uniquely. Fewer than ten arbitrary **independent scalar** density readouts cannot determine a generic 10-dimensional symmetric tensor without additional constraints (linear-rank obstruction). “Ten observers” is shorthand: a physically repeatable setup can use multiple preparations and velocities, but all readouts must refer to the same source tensor/event or a rigorously transported stationary configuration. **A four-corner square is insufficient for unrestricted 3+1 tensor tomography.**

This is the finite-dimensional polarization identity made into a concrete operational measurement schedule. It is classical mathematics, a useful new-to-SUCC interface, not a claim of new physics. The exact script verifies the rank is 10 (every one-reading ablation rank 9), recovers 80 seeded rational symmetric tensors and checks covariance under rational Lorentz boosts.

### What the tensor components actually mean

For `u^μu_μ=−1`, let `h_{μν}=g_{μν}+u_μu_ν`. Define measured rest energy `ρ=T_{μν}u^μu^ν`, momentum/heat flux `q_μ=−h_μ{}^αT_{αβ}u^β`, and spatial stress `S_{μν}=h_μ{}^αh_ν{}^βT_{αβ}`. Then algebraically

\[\boxed{T_{μν}=ρu_μu_ν+u_μq_ν+q_μu_ν+S_{μν}.}\]

This is an exact observer-relative decomposition; the underlying tensor is independent of the frame if the Lorentz transformations and source alignment are correct. A dust source has `T^{μν}=ρ_rest U^μU^ν`; a perfect fluid has `T^{μν}=(ρ+p)U^μU^ν+p g^{μν}`. These material constitutive models are not implied by the observer-square diagram.

## 6. Derive matter stress–energy by metric variation — OGR-08

To identify the tomographically reconstructed symmetric tensor with **physical matter stress–energy**, supply a diffeomorphism-invariant matter action. Set `c=1`, signature `(−+++)`, and consider one real scalar field:

\[S_m[g,φ]=-\int_Md^4x\,\sqrt{-g}\left(\frac12g^{μν}\partial_μφ\partial_νφ+V(φ)\right).\]

By definition, varying with respect to the inverse metric (holding `φ` fixed),

\[\boxed{T_{μν}:=-\frac2{\sqrt{-g}}\frac{\delta S_m}{\delta g^{μν}}.}\]

Use `δ√−g=−(1/2)√−g g_{μν}δg^{μν}`. Since `φ` is a scalar, `∂_μφ` needs no metric variation. Thus

\[\boxed{T_{μν}=\partial_μφ\partial_νφ-g_{μν}\left(\frac12g^{αβ}\partial_αφ\partial_βφ+V(φ)\right).}\]

With flat metric, `∂φ=(2,1,0,0)`, `V=1/4`, one gets `T_00=11/4`, `T_11=9/4`, `T_01=2`, exactly checked by rational arithmetic. Different matter actions produce different stress tensors. In particular, observational agreement alone does not specify `V(φ)`, material density, particle content, or the quantum state.

On matter equations of motion, diffeomorphism invariance gives `∇_μT^{μν}=0` (total matter stress–energy for the declared system; interacting subsystems can exchange energy). This covariant conservation is not an independent identity for arbitrary off-shell matter fields.

**There is generally no unique local, covariant stress–energy tensor for the gravitational field itself.** Do not label a generic observer-gluing mismatch “gravitational energy density.”

## 7. Derive Einstein's field equation from an additional dynamical postulate — OGR-09

Choose the Einstein–Hilbert plus matter action (compactly supported metric variations, or the appropriate Gibbons–Hawking–York boundary term):

\[S[g,φ]=\frac{1}{16πG}\int_Md^4x\sqrt{-g}(R−2Λ)+S_m[g,φ].\]

Under inverse-metric variation, the Palatini identity and integration by parts give

\[\delta S=\int_Md^4x\sqrt{-g}\left[\frac{1}{16πG}(R_{μν}−\tfrac12Rg_{μν}+Λg_{μν})−\tfrac12T_{μν}\right]\delta g^{μν}.\]

Requiring stationary action for arbitrary compactly supported metric variations gives

\[\boxed{G_{μν}+Λg_{μν}=8πG T_{μν}\qquad(c=1).}\]

Restoring physical units yields `G_{μν}+Λg_{μν}=(8πG/c⁴)T_{μν}`. This is the established Einstein equation. The contracted Bianchi identity `∇^μG_{μν}=0` is consistent with matter conservation. Its gravitational coupling is fixed by the normalization and Newtonian limit, not by four observer corners. Alternate gravitational actions (e.g. higher-curvature terms), torsionful connections or extra fields can share some operational causal data while producing different field equations.

**Geometric inverse only with the action specified:** defining `T_eff=(G+Λg)/(8πG)` computes a tensor from `g`, but identifying it with a physical *matter* tensor uses the field equation. The split between `Λ` and vacuum-energy stress is additionally conventional: changing `Λ` shifts the assigned matter tensor by a multiple of `g` at fixed geometry.

**Alternative conditional route:** Jacobson (1995) derives Einstein's equation from Clausius `δQ=T dS` on *all* local Rindler horizons, Unruh temperature, a universal area entropy density, and local equilibrium via Raychaudhuri focusing. This is particularly consonant with observer boundaries, but these thermodynamic assumptions are **additional physical premises**; the result does not follow merely from finite observer gluing.

## 8. Discrete observer fabrics and Regge curvature — OGR-10, research pathway

If the observer diagram is made into an actual piecewise-flat **4D Lorentzian simplicial complex** with admissible timelike/spacelike edge data and consistent simplex gluings, curvature may be concentrated on codimension-two triangular *hinges*. The classical Regge action is proportional to

\[S_{\mathrm{Regge}}=\frac{1}{8πG}\sum_{h}A_h\,\delta_h + S_{Λ,\mathrm{discrete}}+S_{m,\mathrm{discrete}}+S_{\mathrm{boundary}},\]

with orientation/sign convention adapted to Lorentzian dihedral angles. Variation with respect to edge-length variables gives discrete gravitational equations only after metric admissibility and matter coupling have been specified. The square of two triangles is **not** itself a 4-simplex or a full Regge triangulation. Convergence to continuum Einstein dynamics is a separate demanding problem. This route is suggested by Regge calculus; it has **not** been constructed in the present SUCC research package.

## 9. SUCC integration, no-go boundaries and the next discriminator

### Existing exact antecedents (do not double count)

- [SUCC #39](https://github.com/femboy2112/SUCC/pull/39): two oriented light-null directions + normalized timelike clock generate a 1+1 Lorentzian form in an exact rational historical model.
- [SUCC #604](https://github.com/femboy2112/SUCC/pull/604): `SL₂(C)`/`Herm₂(C)` determinant yields Minkowski norm. Mathematical representation, not physical 3+1 curvature.
- [SUCC #393](https://github.com/femboy2112/SUCC/pull/393) and [#394](https://github.com/femboy2112/SUCC/pull/394): clock/allocation and arithmetic Lorentz-shaped mass shells; an arithmetic norm is not physical `T_{μν}`.
- [SUCC #483](https://github.com/femboy2112/SUCC/pull/483): a 2-adic precision cone and auxiliary split-signature form; its `c_precision` is not physical light speed.
- [SUCC #402](https://github.com/femboy2112/SUCC/pull/402): conditional 3+1 wave construction; not an Einstein action result.
- [Principia #618](https://github.com/femboy2112/SUCC/pull/618), [#619](https://github.com/femboy2112/SUCC/pull/619), [#620](https://github.com/femboy2112/SUCC/pull/620): finite observers, predictive descent, weighted causal quotients and finite detection horizons. Their *source-map adequacy* does not follow from internal exactness.

### Claim ledger / why there is no derived physical GR yet

- **PROVED PAPER / CLASSICAL:** conditional two-null-and-clock metric reconstruction; Lorentz boost; spinor determinant; tetrad and curvature formulas; dimension-two Einstein no-go; conformal causal ambiguity; finite ten-readout stress tomography; scalar-action stress variation; Einstein equation *conditional on Einstein–Hilbert action*.
- **OBSERVED, independently executed exact finite algebra:** seven rational test methods; 10×10 measurement rank, 10 single-reading ablations, eighty symmetric tensor reconstructions, Lorentz covariance and Hermitian determinant, null/clock controls, scalar tensor values, conformal-scale test.
- **INDEPENDENT SYMBOLIC CHECK:** 1+1 `R=2a''/a` and `G=0`; 3+1 conformal-de Sitter `R=12H²`, `G=−3H²g` from full Christoffel/Ricci contractions.
- **UNVERIFIED:** any physically validated causal event map from SUCC carriers to a smooth 3+1 spacetime, a measured clock/volume source, a derived matter action from SUCC computation, convergence of an observer-tiled fabric to Einstein–Hilbert dynamics, or a new theory of quantum gravity. No selected-π, RH or Yang–Mills proof is claimed.

### The next verdict-changing experiment

**T1 — Source-faithful metric tomography.** Declare a finite set of source-labelled observer operations whose readouts include two independent null directions and a timelike clock; independently recover the 1+1 form and prove or refute exact frame transport. Then generalize with sufficient null directions plus calibrated volume/proper-time information in 3+1, and test invariant metric reconstruction under a second observer's chart.

**T2 — Ten-reader matter stress tomography.** For an explicitly declared classical matter action or source distribution, predeclare the ten timelike readout protocols. Compute their outputs by a *different* implementation than the reconstruction code, recover `T`, and compare with the functional-variation tensor. Include gauge, missed component, calibration mutation, and context drift controls.

**T3 — Curvature/source separation.** Provide two source-faithful models with identical causal order and different conformal scales (Minkowski versus conformal de Sitter) and let a clock/volume or curvature/holonomy instrument break the ambiguity. Positive: calibrated scale detects the difference; negative: cone-only readout cannot; hostile: record-only square falsely reports curvature.

**T4 — Discrete-to-continuum debt.** Only after T1–T3 pass with an independently justified source map: construct a piecewise-Lorentzian multi-observer simplicial complex, a compatible discrete connection, a matter action and an honest continuum limit. Without those, stop at operational Lorentz geometry, **not** physical GR.

## Primary literature / source pointers

- Ehlers–Pirani–Schild (1972), *The geometry of free fall and light propagation*: https://doi.org/10.1007/s10714-012-1353-4 ; compatibility discussion https://link.springer.com/article/10.1007/s00220-013-1850-7
- Malament causal-conformal reconstruction: https://link.springer.com/article/10.1007/s41114-019-0019-x
- Causal order plus volume (causal-set perspective): https://link.springer.com/article/10.1007/s41114-019-0023-1
- Lorentz spinors via `Herm₂(C)`: https://member.ipmu.jp/yuji.tachikawa/lectures/2019-theory-of-elementary-particles/notes.pdf
- Einstein–Hilbert and stress–energy variation: https://www.damtp.cam.ac.uk/user/tong/gr/grhtml/S4.html
- Einstein as a local horizon equation of state (Jacobson 1995): https://arxiv.org/abs/gr-qc/9504004
- Classical Regge discretization: https://link.springer.com/article/10.12942/lrr-1998-13

**Provenance discipline:** Sources supply the historical mathematical antecedents. Their existence does not validate the SUCC-to-physical-source map. This research note is a new-to-project conditional synthesis with an elementary exact observer tomography schedule, not an academic-priority claim.
