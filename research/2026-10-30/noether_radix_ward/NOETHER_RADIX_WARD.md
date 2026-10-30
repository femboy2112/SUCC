# SUCC — Discrete Noether, radix-16 Ward resonances, and the selected-seed obstruction

**Research date:** 2026-10-30. **Authority:** DRAFT RESEARCH ONLY, proposed stacked child of draft PR #402 at exact SHA `384fe179250a172c2e667c387fdb55bf9589e7a0`, itself stacked on #397 and rooted in Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. All source equations below retain the authentic original signed four poles and `U_0=0` as a *marked* selected boundary. No production modules, original source, archives, Lean contracts, historical claims, main, or workflow modifications. π base-16/base-3 normality and RH remain **OPEN**.

## 0. Steelman: Noether as the missing source–observer–carrier constraint

The author's proposal is not simply that geometry and waves *resemble* GR: an observer starts with an object in a place and attempts to move it through the carrier to prove something about a larger connected object. Possible interactions support an operational geometry; acceleration may redistribute access and, under a genuine coupling, change the field. An admissible action, its symmetries, its fluxes and its observer/carrier exchange should then constrain the realized path. The proposed no-discard and finite-inertial-capacity axioms require every claimed source-to-output identification to preserve its actual observed branch/carry data, with declared external records.

**Object/outcome:** derive actual discrete Noether invariants and local source/boundary work terms; use them to discriminate the authentic zero-seed signed BBP orbit from coherent changed-seed controls; reject vacuous symmetry-averaging routes rather than manufacture a Weyl saving.

**Prior source passports:** #390–#394 (BBP forcing, retained latent triangle, golden mass and Lorentz clocks), #397 (epicycle/no-discard/inertial-contact/3D graph interaction), #402 (three-channel source marks/Fisher H³/three-dimensional wave probes). Read-only arithmetic siblings #399–#401: prime CRT and real-circle selected signed barriers; no sibling ancestry silently imported. Classical outside input: Marsden–West (2001), *Discrete mechanics and variational integrators*, DOI `10.1017/S096249290100006X`; Marsden–Patrick–Shkoller (1998), *Multisymplectic Geometry, Variational Integrators, and Nonlinear PDEs*; gauge-invariant Maxwell–Klein–Gordon lattice schemes, DOI `10.1093/imanum/drp007`. These are methodological foundations, not proof that BBP has a physical action.

## NWR-01. Exact source-constrained *variational* lift and its bulk Noether charge

Keep
\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},\quad
r_n=R(8n-7),\quad U_{n+1}=16U_n+r_{n+1}.
\]
For a finite horizon `N`, introduce real Lagrange multipliers `p_1,...,p_N` and the constrained discrete action
\[
\boxed{\mathcal A_N[U,p]=\sum_{n=0}^{N-1}p_{n+1}(U_{n+1}-16U_n-r_{n+1}).}
\]
Variations with respect to `p_(n+1)` give exactly the authentic forced recurrence. Interior variations with respect to `U_n` (for `1<=n<N`) give the adjoint equation
\[
p_n-16p_{n+1}=0.
\]
The bulk action is **exactly invariant even off shell** under the continuous affine seed-shift variation
\[
\delta_\epsilon U_n=16^n\epsilon,\qquad\delta_\epsilon p_n=0.
\]
Indeed every recurrence residual is unchanged. The corresponding discrete momentum map (up to overall sign convention) is
\[
\boxed{\mathcal Q_n=16^np_n,\qquad \mathcal Q_{n+1}=\mathcal Q_n\quad(1<=n<N).}
\]
This is a genuine discrete-Noether-type charge **for the declared first-order constrained action**, not an observed BBP energy or source momentum. It is independent of the selected seed when the same multiplier solution is used, and is equally available to source mutants whose forcing is merely substituted into the same constraint.

**Boundary crucible:** The authentic selection fixes `U_0=0`. The bulk symmetry has `delta U_0=epsilon`, so **nonzero seed shifts are NOT admissible variations of the fixed-boundary problem**. It is invalid to infer a physical or probabilistic selection rule for the marked zero seed from this unpointed bulk symmetry. This is exactly the observer/carrier identity-coupling issue: symmetry of the family of all solutions is not invariance of one selected member.

## NWR-02. A different, exact *first integral* preserves the lost integer carry

The unwrapped source-corrected invariant is
\[
\boxed{C_n=16^{-n}U_n-\sum_{j=1}^n16^{-j}r_j=U_0=s.}
\]
This is an algebraic first integral, **not identified with the Noether charge** `Q_n=16^np_n` above.

Set `x_n={U_n}` and retain the literal integer carry
\[
\kappa_n=\lfloor16x_{n-1}+r_n\rfloor,\qquad
x_n=16x_{n-1}+r_n-\kappa_n.
\]
Then the *lossless circle-lifted* counterpart is
\[
\boxed{C_n^\circ=16^{-n}x_n+\sum_{j=1}^n16^{-j}(\kappa_j-r_j)=\{s\}.}
\]
For the original zero seed, its right side is precisely zero. Integer carries are not optional decoration; dropping them destroys an exact reconstructible balance. If an observer reports a 'charge violation' only because the quotient lost those integers, it has found an **observation defect**, not physical symmetry breaking. Fixed finite carry prefixes do not certify global π digit statistics.

## NWR-03. The honest connection no-go: a single scalar phase is pure gauge

For any fixed integer harmonic h, on a graph of sampled arithmetic times let the **lifted** edge connection be
\[
A_{uv}=h(U_v-U_u),\qquad G_{uv}=e(A_{uv}),\quad e(x)=e^{2\pi i x}.
\]
For EVERY closed oriented loop `u_0->...->u_m=u_0`, without using any statistical assumption,
\[
\boxed{\sum_{j=0}^{m-1}A_{u_j u_{j+1}}=0,\quad \prod_{j=0}^{m-1}G_{u_j u_{j+1}}=1.}
\]
Consequently **scalar relative BBP phases alone cannot give nonzero U(1) holonomy or a nonflat intrinsic connection**, regardless of how many time-extruded triangles are tiled. Reducing each edge difference separately to its fractional representative can create a nonzero **integer** lifted cycle sum, but its circle holonomy remains 1: a choice-of-branch artifact unless independently transported carry evidence yields something else. Keeping the integer winding is required for no-discard, but integer winding is not a new physical curvature.

Using *different* harmonic labels on different edges (`h1` and `h2`) may give nontrivial path comparisons, but those labels define different observation protocols; an operationally derived common-basis transport is necessary before calling the mismatch intrinsic curvature. The positive retained-X Pascal posterior diamonds from #392 commute, so memory/covariance alone is also an exact flatness control.

## NWR-04. A genuine discrete U(1) Noether current in the 3D interaction carrier

Let `V` be a finite spatial graph, `w_(xy,t)=w_(yx,t)>0` real symmetric, and oriented unit-modulus spatial links `g_(yx,t)=conj(g_(xy,t))`. Define the Hermitian weighted covariant Laplacian
\[
(L_t\psi)_x=\sum_{y\sim x}w_{xy,t}(\psi_x-g_{xy,t}\psi_y).
\]
For a complex field `psi_(t,x)`, a **declared** discrete action using time step 1 is
\[
\mathcal S=\sum_t\left\{\frac12\|\psi_{t+1}-\psi_t\|^2-\frac{c^2}{4}\big[\langle\psi_t,L_t\psi_t\rangle+\langle\psi_{t+1},L_{t+1}\psi_{t+1}\rangle\big]\right\}.
\]
Its discrete Euler–Lagrange equation (including an externally specified source `J_t`, when present) is
\[
\boxed{\psi_{t+1}-2\psi_t+\psi_{t-1}+c^2L_t\psi_t=J_t.}
\]
The action has an EXACT **continuous global U(1)** symmetry `psi -> exp(i alpha) psi`, even when the real Hermitian interaction weights change with time. The corresponding time-link charge, up to sign convention, is
\[
\boxed{q_{t+1/2,x}=\Im(\overline{\psi_{t,x}}\psi_{t+1,x}),\quad
Q_{t+1/2}=\sum_xq_{t+1/2,x}.}
\]
Define the antisymmetric edge current
\[
j_{t,x\to y}=-c^2w_{xy,t}\Im(\overline{\psi_{t,x}}g_{xy,t}\psi_{t,y}),\quad j_{x\to y}=-j_{y\to x}.
\]
Direct multiplication of the equation by `conj(psi_t,x)` and taking imaginary parts yields the **exact local Ward/Noether continuity law**:
\[
\boxed{q_{t+1/2,x}-q_{t-1/2,x}+\sum_{y\sim x}j_{t,x\to y}
=\Im(\overline{\psi_{t,x}}J_{t,x}).}
\]
Thus when `J=0`, the total `Q` is conserved for ANY time-dependent collection of Hermitian edge weights: geometrical pumping/wave generation need not alter the phase charge. On a subregion, edge currents quantify actual boundary export. A spatially varying, **time-independent** gauge rechart `psi_x -> g_x psi_x`, `g_xy -> g_x g_xy conj(g_y)` preserves the discrete action and currents. For *fully spacetime-local* gauge symmetry one must include covariant temporal links and, for Noether's second theorem/Gauss constraints, an appropriate dynamical gauge action; we have not derived those for the native BBP carrier.

## NWR-05. Energy can change even while the phase charge remains constant

The same linear Hermitian wave equation has the exact quadratic half-step energy
\[
\mathcal E_{t+1/2}=\frac12\|\psi_{t+1}-\psi_t\|^2
+\frac{c^2}{2}\Re\langle\psi_t,L_t\psi_{t+1}\rangle.
\]
Its explicit work-source identity is
\[
\boxed{\mathcal E_{t+1/2}-\mathcal E_{t-1/2}
=\frac12\Re\langle\psi_{t+1}-\psi_{t-1},J_t\rangle
+\frac{c^2}{2}\Re\langle\psi_{t-1},(L_t-L_{t-1})\psi_t\rangle.}
\]
With fixed `L` and `J=0`, this special quadratic leapfrog scheme conserves `E` exactly. A changing observer/coupling can do work on the field while `Q` stays conserved. **Do not overgeneralize:** fixed-step discrete variational mechanics does not automatically conserve energy merely because it preserves a discrete Noether momentum; the displayed energy identity is a special algebraic property of this quadratic scheme. Calibrate against Marsden–West (2001) and the time-adaptive energy–momentum literature.

A physical closed-system ledger requires giving the actuator/observer its own dynamics. One optional **continuous-time declared** completion is
\[
L=\frac I2\dot\eta^2+\frac12\sum_x|\dot\psi_x|^2
-\frac{c^2}{2}\sum_{e=(x,y)}w_e(\eta,a)|\psi_x-\psi_y|^2.
\]
Let one edge carry the explicitly chosen source-sensitive strength
\[
w_e(\eta,a)=1+\varepsilon[\kappa(a)-1]^2\eta^2,\quad
\kappa(a)=\tfrac12[-a\partial_a\log R(a)].
\]
If both eta and psi satisfy the action's Euler–Lagrange equations and `a` is fixed, total energy
\[
E_{\rm total}=\frac I2\dot\eta^2+\frac12\sum_x|\dot\psi_x|^2
+\frac{c^2}{2}\sum_ew_e(\eta,a)|\psi_x-\psi_y|^2
\]
is conserved, with exact equal-and-opposite observer and field exchange. The source coefficient is
\[
\kappa(a)-1=-\frac{59}{30a}+O(a^{-2}),\qquad [\kappa(a)-1]^2=\frac{3481}{900a^2}+O(a^{-3}).
\]
This `59^2` is inherited from the **declared source-to-edge coupling**, not independent evidence for gravity, physical acceleration or selected digit wave dynamics. External prescribed eta(t) instead supplies work that cannot be counted as internally conserved.

## NWR-06. Exact arithmetic *finite symmetry* and seed-averaged moment selection

Define the unnormalized signed Weyl sum over the original source family
\[
W_N(s;h)=\sum_{n=1}^N e(hU_n(s)),\qquad h\in\mathbb Z\setminus\{0\}.
\]
The affine seed law is exact: `U_n(s)=U_n(0)+16^n s`. Hence
\[
W_N(s+1/15;h)=e(h/15)W_N(s;h).
\]
This is a `Z_15` character (a **finite group symmetry**, not Noether's continuous first theorem). A stronger exact arithmetic selection rule comes from `16^n ≡ 1 (mod 15)`: for nonnegative integers p,q, the Haar seed moment
\[
\int_0^1 W_N(s;h)^p\overline{W_N(s;h)}^q ds
\]
vanishes unless `p-q` is divisible by `15`. The arithmetic frequency condition is exact even if `h` shares factors with 15. **Every** Haar seed-averaged moment is independent of the initial seed `s0` because its shift is a change of integration variable; no such moment identifies the selected `U_0=0` realization.

For all integers `1<=k<=16`, sums of exactly `k` positive powers of 16 have a unique representation of fixed length `k`. Therefore the first sixteen balanced moments are **independent of the actual signed source phases**:
\[
\boxed{\int_0^1|W_N(s;h)|^{2k}ds
=\sum_{m_1+\cdots+m_N=k}\left(\frac{k!}{m_1!\cdots m_N!}\right)^2,\quad1\le k\le16.}
\]
In particular `∫|W|²=N`, `∫|W|⁴=2N²−N`. Proof of the threshold: with at most 16 summands, canonical radix carrying either does not occur (all multiplicities <=15) or occurs once when all 16 terms have the SAME exponent; the canonical result uniquely identifies the multiset. At 17 summands the first nonunique representations appear.

## NWR-07. FIRST unbalanced radix-carry resonance is an exact original-source forcing sum

For every `N>=2` and integer nonzero h,
\[
\boxed{\int_0^1W_N(s;h)^{16}\overline{W_N(s;h)}\,ds
=\sum_{n=1}^{N-1}e(-h r_{n+1}).}
\]
**Proof:** Expand the 16+1 factors as characters of `s`. Orthogonality forces `sum_{j=1}^{16}16^{n_j}=16^m`. As every summand is positive, equality is possible iff all `n_j=m-1`, for `m=2,...,N`. Their source phase is `16U_{m-1}(0)-U_m(0)=-r_m`. Every surviving term has multiplicity 1. The proof works for ANY forced radix-b affine map with `b` copies on the left; this specialization is the authentic four-pole source.

Since `0<r_n<=15/(8n-7)^2` and the sum converges,
\[
\boxed{\int W_N^{16}\overline{W_N}\,ds=N-1+O_h(1).}
\]
This is a **source-visible but maximally coherent** asymptotic, not selected Weyl cancellation. The original and a Gamma-matched fake have different `r_n`, but both obey the identity and neither obtains a seed-sensitive estimate. The coherent same-forcing nonnormal counterseed also obeys it.

## NWR-08. FIRST balanced 34th moment has an exact all-pairs four-pole source formula

The first nontrivial equal-degree additive collision occurs for `k=17`:
\[
16\cdot16^{p-1}+16^q=16\cdot16^{q-1}+16^p,
\qquad 2\le p<q\le N.
\]
For the original BBP phases the signed difference equals
\[
16U_{p-1}+U_q-16U_{q-1}-U_p=r_q-r_p.
\]
Every nontrivial collision at exactly 17 summands has this form. Let
\[
D_{N,17}=\sum_{m_1+\cdots+m_N=17}\left(\frac{17!}{m_1!\cdots m_N!}\right)^2.
\]
A complete exact group-algebra expansion gives
\[
\boxed{\int_0^1|W_N(s;h)|^{34}ds
=D_{N,17}+2\sum_{2\le p<q\le N} a_{pq}\cos(2\pi h(r_q-r_p)),}
\]
where `a_(pq)=17` when `q=p+1` and `a_(pq)=289` when `q>=p+2`. The coefficient is the product of the multinomial weights of the two collision representations (17 versus 1 for adjacent indices; 17 versus 17 otherwise). A separate 90-digit group-algebra oracle independently checks this exact formula against the original rational source.

This is **source-specific arithmetic appearing at the first possible balanced mixed term**, but it is still **seed-blind** by the Haar integration. It is not a mechanism identifying actual base-16 π digits.

## NWR-09. An exponentially shrinking seed-cylinder is the missing scale

The triangle inequality and `|e(t)-1|<=2π|t|` yield, for any `0<=s<=16^{-N}`,
\[
|W_N(s;h)-W_N(0;h)|
\le2\pi|h|s\sum_{n=1}^N16^n<\frac{32\pi|h|}{15}.
\]
Therefore if `I_N=[0,16^{-N}]` and `\mathcal L_N=16^N\int_{I_N}W_N(s;h)ds`, then
\[
\boxed{|\mathcal L_N-W_N(0;h)|<\frac{32\pi|h|}{15}.}
\]
Hence `mathcal L_N=o(N)` iff the authentic `W_N(0;h)=o(N)`: an exact source-independent representation transfer, **not a new saving**. Its significance is diagnostic: global Haar seed moments operate on an interval of length 1, whereas selecting the authentic seed requires arithmetic discrimination in a cylinder of exponentially shrinking length `16^{-N}`. Existing universal source-only Haar moment identities do not control such shrinking neighborhoods. A genuinely new source- and zero-boundary-sensitive local estimate must not merely repackage the original Weyl criterion.

## NWR-10. The Ward tautology and a decisive counterexample

On a one-site complex field take *any* unit-modulus sequence `z_t`, and **fit** a source afterwards:
\[
J_t=z_{t+1}-2z_t+z_{t-1}.
\]
The putative Noether source is automatically
\[
\Im(\overline z_tJ_t)
=\Im(\overline z_tz_{t+1})-\Im(\overline z_{t-1}z_t).
\]
Thus its N-step sum has absolute value at most 2 **for EVERY such sequence**, including one with Cesàro mean 1. Defining the Ward source from the already known trajectory only proves a tautological telescoping identity. This is the precise Noether analogue of the old normalized-Weyl `o(N)` vacuity problem.

Even for a SOURCE-FREE Hermitian wave equation, global charge `Q` cannot force mean cancellation: a constant real mode and a real six-period standing mode on the SAME four-site ring with `c²=1/4` both have `Q=0`, but the first has nonzero temporal mean and the latter zero temporal mean. An independently sourced current or a coercive mixing/observability estimate is required.

## Claim verdicts, probes and next lamp

- **PROVED LOCAL (paper + exact Fraction controls):** BBP constrained action seed-shift symmetry, adjoint charge, fixed-mark incompatibility; unwrapped/carry first integrals; pure scalar phase holonomy no-go; Hermitian local phase continuity and exact quadratic work balance; finite `Z_15` selection; first 16 balanced moments; 17-factor forcing identity; full 34th-moment first collision; seed-cylinder inequality; fitted-Ward vacuity. These are either classical constructions or new-to-this-repository specializations, **not** claims of academic priority.
- **CLASSICAL / DECLARED:** general discrete variational Noether theory; complex wave action with arbitrary real positive graph weights/observer coupling; continuous total-energy exchange for the chosen action.
- **REFUTED as implications:** seed-family symmetry forces normality of its marked member; phase differences alone yield curvature; conserved U(1) charge or 17-factor moment forces Weyl cancellation; Haar-averaged phase moments identify the zero seed; acceleration alone causes a nonzero charge source; a source chosen post hoc from the phase path supplies independent dynamics.
- **UNVERIFIED / OPEN:** physical 3+1 observer/carrier action; a genuine noncommuting BBP source/carry phase transport and locally sourced gauge field; a novel selected `U_0=0` signed all-horizon bound; π base-16/base-3 normality; RH.

**Next falsifier:** Construct a *predeclared*, lossless, original-source four-pole and zero-seed-dependent current on the full three-time carry/phase tensor. Keep all integer lifts, q6 primitive labels, original source atom and Oily clock passports, and the actual selected real-circle/prime-power CRT embeddings. Require a source term not definable by fitting `J=Dψ` after seeing the path, a gauge-covariant two-path comparison with nonzero **intrinsic** holonomy, and an actual new bound controlling a shrinking seed cylinder or Weyl harmonic. Test coherent same-forcing seed `s*=-π/16`, finite exact `Z[1/16]` aliases, high-jet-matched fake source, source reset, distinct normal Stoneham c=3/5 and nonnormal periodic/de Bruijn controls; never use unknown π digits as theoretical inputs. Preserve raw and transported views; demonstrate a uniform signed saving against a nontrivial bound, not another restatement.

**Validation boundary:** standalone exact stdlib tests, two independent mathematical/combinatorial oracles, and exact Git blob identities (see VALIDATION.md). Full SUCC root AGENTS gates, hosted exact-head CI, Lean and blind external referees were not run in this new branch. Do not merge blindly.
