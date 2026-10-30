# Operation Interaction Curvature × Arithmetic Waves

2026-10-30. **DRAFT RESEARCH ONLY**, additive continuation of PR #397 (base merged Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5). The author's hypothesis: the geometry relevant to finite observers should be reconstructed from supported interactions of an object, a place, a carrier and a target property of a larger connected object. An accelerating frame could change that interaction geometry, and an intrinsically dynamical carrier could then propagate sine/Fourier/periodic arithmetic modes.

Read-only provenance: PR #390 (time-extruded Pascal source; signed carry), #392 (shared Gamma source and harmonic/golden tile; commuting positive-source updates), #393 (declared projective Lorentz observer), #394 (authentic four-pole running information mass), #397 (no-discard/inertial contact/Oily response). Original signed BBP poles, U_0=0, frozen source, production, claim namespaces, legacy contracts and main are unchanged.

## 1. Type the four-layer reconstruction before calling it spacetime

Let P be places, O objects, C the physical or mathematical carrier, and E admissible object–carrier interaction edges. A realized object path γ:p→q consists of interactions with typed maps T_e on retained object/observer/source fibers. Its existence defines a reachability relation and possibly a causal preorder if the edges include an oriented time. It does NOT by itself uniquely determine a metric, curvature, or dynamics.

A separately declared edge cost c(e)>0 yields a path metric d(p,q)=inf_γ sum_e c(e) under suitable reversibility/connectedness assumptions. A transition probability kernel P_p and a metric d give Ollivier curvature κ(p,q)=1−W_1(P_p,P_q)/d(p,q). This is an established kind of **coarse Riemannian/discrete** curvature, not a Lorentzian spacetime Riemann tensor.

**Exact same-support counterexample:** three-site path 0−1−2, unit edge distance, lazy kernel P_0=(1−p,p,0), P_1=(q,1−2q,q), P_2=(0,p,1−p), with p∈(0,1), q∈(0,1/2). For p+q≤1, the one-Wasserstein distance W_1(P_0,P_1)=|1−p−q|+q=1−p, hence κ(0,1)=p. The support stays unchanged while changing p changes curvature. Thus support alone cannot uniquely select curvature; the original source law/observer transport has to constrain the weights and distances.

For invertible transport operators U_e in a declared common fiber and endpoint frame, a holonomy round a closed plaquette measures failure of path independence. If transports are noninvertible posteriors/filters, compare the two composites in a common target with a norm/coupling rather than inventing an inverse. PR #392's positive shared-source Pascal likelihood updates commute even though the grades are correlated: that flat diamond is a mandatory null control. A nonzero information-memory covariance does not equal curvature.

## 2. Exact discrete frame-versus-carrier loop discriminator

Let t∈Z be observation clock and x∈Z a spatial interaction-place label. An additive U(1) connection is specified by lifted link values A_x(t,x), A_t(t,x), with the U(1) holonomy obtained only after reducing the lifted loop integral modulo integers:
\[
F_{tx}^{\rm lift}=A_x(t+1,x)-A_x(t,x)-A_t(t,x+1)+A_t(t,x).
\]
The holonomy is exp(2πi F_lift). Keep **both** F_lift and its circle reduction; modulo-one phase loses integer windings, violating a literal no-discard carrier ledger unless the integer label is stored.

Use the ORIGINAL four-pole source:
\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5},\quad
M(a)=-a\,R'(a)/R(a),\quad \kappa_a=M(a)/2.
\]
PR #394 proves 1<M(a)<2 and M(a)=2−59/(15a)+O(a^−2); hence κ_a=1−59/(30a)+O(a^−2). The declared Gamma-matched tangent has κ_fake=1.

For observer rapidity η_t, *both* assignments below use the same spatial link A_x(t,x)=κ_a η_t.

(a) **Pure moving frame:** A_t(t,x)=κ_a x(η_(t+1)−η_t). Then F_lift=0 for every acceleration schedule. This is a discrete exact gradient A=d(κ_a x η_t), i.e. pure gauge.

(b) **Independent spatial-carrier response:** A_t(t,x)=0 while A_x(t,x)=κ_aη_t. Then F_lift=κ_a α_t with α_t=η_(t+1)−η_t. In a discrete local gauge rechart χ(t,x), A_e→A_e+χ(source)−χ(target), F_lift is invariant. This nonzero holonomy is a legitimate **declared** interacting connection, NOT a theorem that an accelerating coordinate frame must curve spacetime. The acceleration-to-edge-coupling is an additional dynamical assumption.

Subtract the Gamma-tangent reference lift, not its circle projection:
\[
\boxed{F^{\rm rel}_{tx}=(\kappa_a-1)\alpha_t
=-\frac{59\,\alpha_t}{30a}+O(\alpha_t/a²).}
\]
For α_t=1, the fake reference has zero relative defect, while the authentic original source has a nonzero rational lift for all a>0. However the original and coherent same-forcing nonnormal BBP seed share the positive source and this defect. It does not select π normality.

## 3. A genuine hyperbolic carrier equation with Fourier modes

For a finite graph with vertices V, symmetric positive weights w_e(t)>0, and field ψ_t∈R^V, define the positive weighted Laplacian
\[
(L_t\psi)_x=\sum_{y\sim x}w_{xy}(t)(\psi_x-\psi_y).
\]
**Declare an evolution law**:
\[
\boxed{\psi_{t+1}-2\psi_t+\psi_{t-1}+c²L_t\psi_t=J_t.}
\]
This is a discrete hyperbolic wave equation, not forced by the existence of graph paths or by the Lorentz boost matrix. Locality implies finite propagation in integer steps. For a static 1D uniform ring, let k=2πm/N and ψ_(t,x)=exp(i(kx−ωt)); the exact dispersion relation is sin²(ω/2)=c² sin²(k/2). Choosing c²=1/4 gives stable oscillatory modes on every nonzero spatial Fourier sector. They are mathematical cyclic characters independently of selected π digits. Flat carriers **already** support waves; curvature is not required for Fourier modes.

The exact discrete static-graph energy (for symmetric L and J=0) is
\[
\mathcal E_{t+1/2}=\tfrac12\|\psi_{t+1}-\psi_t\|²
+\frac{c²}{2}\langle\psi_t,L_t\psi_{t+1}\rangle.
\]
When L_t=L is constant this energy is conserved. It is nonnegative if c² λ_max(L)≤4 (with zero-mode degeneracy on a periodic graph). For varying L_t and arbitrary forcing J_t, direct use of the recursion gives the **exact balance law**
\[
\boxed{\mathcal E_{t+1/2}-\mathcal E_{t-1/2}
=\tfrac12\langle\psi_{t+1}-\psi_{t-1},J_t\rangle
+\tfrac{c²}{2}\langle\psi_{t-1},(L_t-L_{t-1})\psi_t\rangle.}
\]
The second term is work due to a changed interaction geometry. Conservation of total physical energy would require an independently modeled actuator/carrier budget; this field equation does not supply one for free.

## 4. Source-specific accelerated bond: a transparent constructive witness

For the probe below, choose c²=1/4, ε=1/4 and one spatial bond e*=(m,m+1). We are free to declare a gauge-invariant **reference-relative conductance response**:
\[
\boxed{w_{e*}(t)=1+\epsilon\,[F^{\rm rel}_{tx}(t)]²,\qquad w_e(t)=1\ (e\ne e*).}
\]
This uses the unwrapped relative defect. It is positive and measures a source-sensitive, nonnegative local perturbation. **The square is a chosen coupling, not a unique or source-derived Einstein equation.** If α_t=0, the original and fake have identical unperturbed bonds. If κ_a=1, the reference fake has no perturbation for any α_t. If the field is constant in x, L_tψ=0 for every edge weight, so even a changed geometry generates no wave without field gradients or a separate source.

Let initial ψ_{-1,x}=ψ_{0,x}=x locally near the affected bond, so the unperturbed Laplacian vanishes near e*. Turn on a one-step rapidity increment α_0=1. Relative to the same initial conditions on unperturbed bonds, the exact first-step wave pulse is
\[
\boxed{\delta\psi_{1,m}=c²\epsilon(\kappa_a-1)^2,\qquad
\delta\psi_{1,m+1}=-c²\epsilon(\kappa_a-1)^2.}
\]
All other first-step sites are unchanged. Subsequent steps with unperturbed weights propagate this equal-and-opposite pulse outward, one nearest-neighbor site per tick. This is a deterministic arithmetic witness of a **conditional** acceleration-to-carrier-to-wave mechanism. The shape is a dipole-like lattice disturbance, not a gravitational quadrupole wave.

The source-specific leading coefficient is
\[
\delta\psi_{1,m}
=c²\epsilon\,\frac{3481}{900a²}+O(a^{-3}).
\]
PR #397 proves independently for the authentic positive BBP source μ_a versus its Gamma-matched ν_a
\[
\chi²(\mu_a\Vert\nu_a)=\frac{3481}{450a²}+O(a^{-3}).
\]
Therefore the interaction-induced first pulse in this **chosen response law** has the nontrivial calibratable asymptotic
\[
\boxed{\delta\psi_{1,m}\big/\chi²(\mu_a\Vert\nu_a)\longrightarrow c²\epsilon/2=1/32.}
\]
The matching 59² is source-authenticated but not independent evidence for the coupling: the same source coefficient was explicitly used to define κ_a and hence the local bond response. A higher-jet-matched mutant can reproduce the leading term.

Alternative null: if instead one directly couples w_e=1+ε κ_a α_t, the Gamma fake ALSO produces a wave. This shows waves can be generated by a driven edge even without a source-relative curvature defect. Curvature and wave generation are logically separable.

## 5. Why no gravitational-wave or π-normality theorem follows

The toy field supports waves in a 1+1-dimensional spacetime, but in vacuum 2+1 Einstein gravity lacks local propagating gravitational degrees of freedom; actual 3+1 GR gravitational radiation is primarily governed by a time-varying quadrupole subject to energy-momentum constraints. Thus one must distinguish **a scalar/internal interaction-field wave** from a physical gravitational wave. See Deser–Jackiw–'t Hooft 1984 and LIGO source quadrupole discussion.

The signed BBP orbit still satisfies the original exact source relation U_n=16 U_(n−1)+R(8n−7), U_0=0. A formal source-driven wave response to e(hU_n) is only a linear filter of those phases; even an invertible filter or an oscillatory output cannot prove the original Weyl sums are o(N). Coherent same-forcing seed s*=−π/16 retains the positive source and yields nonnormal phases, refuting any positive-source-only implication. No selected zero-seed intertime cancellation, π normality or RH proof is obtained.

## 6. Claims and hostile gates

- **DISCLOSED:** same-support nonunique Ollivier curvature counterexample; exact pure-gauge vs source-linked lifted plaquette; exact rational BBP M(a) source fingerprint; stable Fourier dispersion; exact discrete energy/work balance; locality of pulse; source-defect 59² jet under chosen bond response.
- **DECLARED / CONJECTURED:** source-to-U(1) transport χ, relative bond-response square, matter wave dynamics, any identification with physical spacetime.
- **REFUTED:** mere support uniquely fixes curvature; acceleration-as-coordinate-change produces mandatory intrinsic curvature; Fourier modes imply curvature; one positive-source wave implies selected π normality; modulo-one holonomy is lossless without winding integer.
- **UNVERIFIED:** coupling derived *uniquely* from operational no-discard, source and object physics; full carry/phase holonomy, all-horizon signed arithmetic bound, RH, physical GR waves.

**Next discriminating probe:** Replace the freely declared bond response with a source- and zero-seed-sensitive interaction map derived from the original four signed BBP poles, full intermediate carry tensor and Oily-weighted retained posterior; require genuine path-ordered holonomy after gauge ablations and an independently sourced hyperbolic propagation law. Include coherent same-forcing seed, fake Q=15x, higher-jet-matched mutants, prior reset, clock1/clock2 passports, q6 and full four-bit Walsh holdouts, normal Stoneham 3/5 and nonnormal de Bruijn controls. A new signed o(N) saving must actually be derived, not assumed.

**Provenance and outside mathematics:** Ollivier (2009), https://arxiv.org/abs/math/0701886; Regge geometry, https://doi.org/10.1093/imanum/drad089 ; causal-set Lorentzian Ollivier curvature preprint Barton–Borza–Röhrig (2026), https://arxiv.org/abs/2606.04910; metric graph wave equation finite propagation, https://doi.org/10.1016/j.jfa.2012.06.005; 2+1 Einstein gravity Deser–Jackiw–'t Hooft (1984), https://doi.org/10.1016/0003-4916(84)90085-X; LIGO quadrupolar waves, https://dcc-llo.ligo.org/public/0172/P2000530/003/aLIGO_for_Contemporary_Physics_v3.pdf.

**Validation scope:** a standalone 11-method Python 3 stdlib exact Fraction + trigonometric probe was executed locally, using the same four-pole source rational function and negative controls. Full SUCC root tests, hosted CI, Lean and peer review not run. All new research files are additive; do not merge blindly.
