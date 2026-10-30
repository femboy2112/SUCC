# Operation Third Dimension — Source-Native Three-Channel Geometry and 3+1 Wave Crucible

**Date:** 2026-10-30. **Authority:** DRAFT RESEARCH ONLY; new auxiliary observer construction on the unchanged original four-pole BBP source. Parent: exact PR #397 head 992b3f9d77f1016300f1daf7db3c88da7392269b, itself from merged Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5. Read-only adjacent research: PR #390 (time-extruded source), #391 (zero-spine), #392 (two-panel Oily Mellin/Fourier), #393 (projective Lorentz clocks), #394 (source mass), #396 (human T-action), #399 (signed CRT arithmetic). No changes to original BBP four signed poles, original U_0=0 boundary, source archives, historical proof contracts, production, workflows, main, or other research PRs. π base-16 normality and RH remain OPEN.

## 0. Author's hypothesis and its rank obstruction

The author proposes that the natural effective spacetime geometry is made of interaction-path degrees supported by object–carrier couplings, and an observer's acceleration might perturb this geometry and generate propagating arithmetic waves. Explore a **third spatial direction** without relabeling a time coordinate, an exact real carrier residual, or a categorical mark as if it were already physical distance.

Distinguish four different ranks:
- At fixed original source a and **independently adjustable three observer gains** θ_1,θ_2,θ_3>0, the statistical model has parameter rank 3: a genuine 3-dimensional Fisher-Riemannian manifold.
- Under total-clock conservation θ_1+θ_2+θ_3=Θ_0 it has rank 2, not 3. This is a decisive negative control.
- If gains are locked to the source atom proportions and only (a, Θ) vary, the accessible subset has rank at most 2.
- If Θ and gains are locked while only native a_n changes, the actual family traces at most a curve, even though the **model space of possible interventions** is 3-dimensional.

No direct proof identifies the observer's 3D Fisher coordinates with independent physical spacelike directions. Independent controllable interaction channels are a proposed instrument, not a fact about actual BBP digit dynamics.

## T3-01. Exact original-four-pole positive source with THREE authenticated marks

The unchanged source is
\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}
=2(1-e^{-3x})+(1-e^{-4x})+(1-e^{-5x})>0.
\]
Let d∈{3,4,5} with authentic coefficients c_3=2,c_4=c_5=1. Then
\[
R_d(a)=\int_0^\infty e^{-ax}c_d(1-e^{-d x})\,dx
=\frac{c_d d}{a(a+d)},\qquad
R(a)=\sum_dR_d(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}.
\]
All R_d(a)>0, so a source-native marked extension with
\[
p_d^*(a)=R_d(a)/R(a)
\]
is a genuine rational probability law for every a>0. Its boundary reference point is
\[
(\beta_3,\beta_4,\beta_5)=\lim_{a\to\infty}p^*(a)
=(6,4,5)/15.
\]
These channels are tied to the **given signed-pole representation**, not three unobserved independent scalar fields. A positive analytic source can admit other positive decompositions, so canonical physical meaning is NOT established by decomposition alone.

The first three weighted atom power sums are exact:
\[
A_1=\sum c_d d=15,\quad A_2=\sum c_d d^2=59,\quad A_3=\sum c_d d^3=243.
\]
In particular Q'(0)=15, Q''(0)=-59 and Q'''(0)=243. Source mark asymptotics are
\[
p_d^*(a)=\beta_d\left[1+\frac{59/15-d}{a}+O(a^{-2})\right].
\]
The weighted angular mean shift is 59/15, and its exact source-induced variance is
\[
\boxed{\sum_d\beta_d(d-59/15)^2=\frac{243}{15}-\left(\frac{59}{15}\right)^2=\frac{164}{225}.}
\]
The number 164 is **new-to-program source angular information** assembled from the authentic first three power sums; it is not a curvature tensor or a physical force.

## T3-02. Exact finite native THREE-panel posterior, with the one shared X retained

Keep the original positive latent
\[
\mu_{a_n}(dx)=e^{-a_nx}Q(x)\,dx/R(a_n),\quad a_n=8n-7.
\]
Three conditionally independent *declared* Bernoulli sensor panels, each of n trials, share this SAME latent X, with success probability 1−e^{-8X}. For grade (j,k,l) with s=j+k+l,
\[
\boxed{P_n(j,k,l)=\binom nj\binom nk\binom nl
\frac{\sum_{h=0}^s(-1)^h\binom sh R(a_n+8(3n-s+h))}{R(a_n)}.}
\]
This is a strictly positive **rational** law at every n, and the conditional posterior on X after any ordered history is retained. Conditional on S=s the split is
\[
\boxed{P(J_1=j,J_2=k,J_3=l\mid S=s)
=\binom nj\binom nk\binom nl/\binom{3n}{s}.}
\]
This is a multivariate hypergeometric identity from Vandermonde; it preserves source-relative posterior information while explicitly distinguishing intermediate chronology/carries. Posterior resetting creates a different model.

At n→∞, Y=a_nX⇒Gamma(2,1) and J_i|Y⇒independent Poisson(Y), so
\[
\boxed{H(z_1,z_2,z_3)=(4-z_1-z_2-z_3)^{-2}.}
\]
Its coefficient at (j,k,l) is \((s+1)s!/(j!k!l!\,4^{s+2})\). For three full channels E[J_i]=2, Cov(J_i,J_j)=2 (i≠j) and the mixed three-way cumulant κ(J_1,J_2,J_3)=4. These are **one latent Gamma source's** shared correlations, not independent carrier spatial directions or actual π-digit laws.

At fixed real z_i∈[0,1] define C=Σ_i(1−z_i), d=1+C. Relative to the same clock and Bernoulli channels applied to the Gamma-matched fake Q_fake(x)=15x,
\[
\boxed{H_n^{BBP}(\boldsymbol z)-H_n^{fake}(\boldsymbol z)
=\frac{59\,C}{120\,n\,d^3}+O_{\boldsymbol z}(n^{-2}).}
\]
Proof: normalize Y=a_nX. The authentic-minus-fake density first jet is
\[
\frac{59}{240n}\;y e^{-y}(2-y)+O(n^{-2})
\]
with the stated integrable remainder; the common three-panel likelihood tends to e^{-Cy}; the weighted integral is \(2C/d^3\). The original four signed poles survive unmodified. At the same native diagonal, the source-specific mixed three-channel cumulant correction is
\[
\boxed{\kappa_{3}^{BBP}(J_1,J_2,J_3)-\kappa_{3}^{fake}
=-\frac{59}{20n}+O(n^{-2}).}
\]
This uses n³κ_3(1−e^{-8X}) and the same first source density jet. Validity is fixed observer channels/clock; do not extend uniformity to moving growing-grade windows without further estimates.

### T3-02a. Literal selected zero-seed arithmetic history is already three-way order-sensitive

Use the **separate actual** signed original recurrence \(U_0=0\), \(U_n=16U_{n-1}+R(8n-7)\) over exact rationals, and literal carry \(\kappa_n=\lfloor16\{U_{n-1}\}+R(8n-7)\rfloor\). Direct exact evaluation yields \(\kappa_3=4\), \(\kappa_4=3\). For native three-panel \(n=3\), each of the positive-probability virtual grade triples (1,0,0), (0,1,0), (0,0,1) has **the same total grade S=1**, but their **marked original arithmetic intermediate histories** at the three clock points \(n+j,n+j+k,n+j+k+l\) have respectively carry triples
\[
(3,3,3),\qquad(4,3,3),\qquad(4,4,3).
\]
Thus three-step signed carry/phase annotation strictly refines positive total-grade sufficiency, even for the authentic zero boundary. The test uses exact source rationals, not fitted digits. This is an **observation/representation separation**, not a cancellation or normality proof: an arbitrary selected path could also show differing intermediate carries. Preserve all three carry lifts and time indices under the no-discard axiom.

**Exact original-source third cumulant mechanism.** Put \(b(X)=1-e^{-8X}\) and
\[
\mu_k(a)=E_{\mu_a}b(X)^k
=\frac{\sum_{j=0}^k(-1)^j\binom kj R(a+8j)}{R(a)}.
\]
For three conditionally independent n-trial panels, the mixed joint third cumulant is **exactly**
\[
\kappa(J_1,J_2,J_3)=n^3[\mu_3-3\mu_2\mu_1+2\mu_1^3].
\]
Thus the leading mixed cumulant 4 and its authentic-minus-fake \(-59/(20n)\) jet can both be checked directly from the original rational four-pole source, without fitting a stochastic π-digit law.

## T3-03. The exact 3D Fisher hyperboloid, and the fixed-budget rank drop

For three independently adjustable positive *observation intensities* θ_i, declare the shared-Y Gamma/Poisson model
\[
J_i\mid Y\sim Pois(\theta_iY),\quad Y\sim Gamma(2,1),\qquad
H_\theta(\mathbf z)=[1+\sum_i\theta_i(1-z_i)]^{-2}.
\]
**Original-source finite-a passport:** before the Gamma limit, the declared three-panel *Poisson* extension can retain the original \(\mu_a\) exactly:
\[
\boxed{H_{a,\boldsymbol\theta}(\boldsymbol z)
=\frac{R(a[1+\sum_i\theta_i(1-z_i)])}{R(a)}.}
\]
For \(d=1+\sum_i\theta_i(1-z_i)>0\), comparing with the Gamma-matched fake \(R_f(a)=15/a²\) gives
\[
H_{a,\theta}^{BBP}-H_{a,\theta}^{fake}
=\frac{59(d-1)}{15\,a\,d^3}+O(a^{-2}).
\]
Its three cross cumulants are source-derived through the derivatives of \(\log R\); in particular \(\kappa(J_1,J_2,J_3)=\theta_1\theta_2\theta_3[-a^3(\log R)'''(a)]\), with \(-a^3(\log R)'''(a)=4-118/(5a)+O(a^{-2})\). The **finite-a Fisher metric is not asserted to be constant-curvature H³**; exact H³ describes the limiting Gamma rank-two model. This use of independent Poisson observation gains is a declared instrument, not the finite native Bernoulli grammar.

In its 3-dimensional mean-coordinate statistical family m_i=2θ_i, the covariance (an exponential-family Hessian) is
\[
\Sigma_{ij}=m_i\delta_{ij}+m_i m_j/2,
\quad
\boxed{g_{ij}=\Sigma^{-1}_{ij}=\delta_{ij}/m_i-\frac1{2+\sum_km_k}.}
\]
Set X_i=2√m_i and T=2√(2+Σm_i). Then
\[
T^2-\sum_iX_i^2=8,\quad
\boxed{ds_F^2=\sum_i dX_i^2-dT^2.}
\]
This is **isometric to the positive-octant sector** of 3-dimensional hyperbolic space H³ of radius √8, with constant sectional curvature −1/8 and scalar curvature −3/4. It is an intrinsic **Riemannian** statistical space embedded in ambient (3+1) Minkowski space; the ambient T is NOT the observer's elapsed physical proper time. The positive-octant restriction is not the full geodesically complete H³.

Let Θ=Σθ_i, p_i=θ_i/Θ, n_i=√p_i, Σn_i²=1, and ρ=arsinh√Θ. The exact metric is
\[
\boxed{ds_F²=8[dρ²+\sinh²ρ\,dΩ²_{S²}]}
\]
on the positive spherical octant. A genuine **third radial coordinate** exists only if total Θ is allowed to vary independently of the two angular allocations p_i. For fixed Θ=1, T is fixed and ΣX_i²=8, so the allowed 2D slice is a positive-octant portion of a round sphere radius √8 with Gaussian curvature **+1/8**, not a 3D hyperbolic space. A fixed clock removes the third information direction. This is the clock/rank firewall missing from naive "three channels => three spatial dimensions" assertions.

The original positive source may naturally anchor a reference angular ray p=p*(a), but it does not independently generate all possible p. A clear **candidate instrument** for 3D rank is to allow independently adjustable positive detector gains g_d>0 on the THREE authentic source marks, while keeping the carrier Q itself unchanged:
\[
\theta_d=\Theta\,\frac{g_dp_d^*(a)}{\sum_eg_ep_e^*(a)}.
\]
After quotienting the irrelevant overall gain scale, the three controls (logΘ, log(g_4/g_3), log(g_5/g_3)) have Jacobian determinant θ_3 θ_4 θ_5>0 with respect to θ=(θ_3,θ_4,θ_5). Thus they locally span the entire three-parameter family **if those gain interventions are admissible**. This is a model of observer–carrier coupling, NOT evidence an actual BBP physical apparatus has these three independently measurable channels.

## T3-04. Source-authenticated angular drift; new exact 164/225 metric jet

For fixed total Θ and reference angular allocation p*(a), the Fisher angular line element is
\[
ds_{\rm ang}²=2\Theta\sum_{d=3,4,5}\frac{dp_d^2}{p_d}.
\]
Differentiate the exact rational p_d^*(a)=R_d(a)/R(a). Using the power sums above gives
\[
\boxed{g_{aa}^{\rm angular}
=2\Theta\sum_d\frac{(p_d^{*\prime}(a))^2}{p_d^*(a)}
=\frac{328\,\Theta}{225a^4}+O(a^{-5}).}
\]
At conserved original native clock Θ=1, the source ray's angular Fisher speed is
\[
\frac{d\ell_{\rm ang}}{da}\sim\frac{2\sqrt{82}}{15a²},
\quad
\ell_{\rm ang}(a,\infty)\sim\frac{2\sqrt{82}}{15a}.
\]
This is exact derived asymptotics of a chosen *source-anchored observer allocation*, not automatically observer acceleration, spacetime holonomy, or physical gravitational curvature. Matched-jet source mutants and alternative positive decompositions are mandatory negative controls.

## T3-05. Third channel and Oily–Macaroni: clock passports matter

At total Θ, the total grade S has PGF (1+Θ(1−z))^−2 and rank-two Gamma/posterior readout
\[
D_s=H_{s+1}-\gamma-\lambda^{s+2},\quad\lambda=\varphi^{-1}.
\]
Let c=1+Θ, and normalize the positive Oily tilt of this total grade. Its **exact** normalizer and mean are
\[
Z_{\rm OM}(\Theta)=1-\gamma+\log c-(1+c\lambda)^{-2},
\]
\[
\bar s_{\rm OM}(\Theta)=\frac{\Theta[3-2\gamma+2\log c-2(1+c\lambda)^{-3}]}{Z_{\rm OM}(\Theta)}.
\]
At Θ=1 the source's original golden fixed point q=φ^-2 survives even when *three* panels share the one conserved budget; the model still has only 2 independent angular directions. At three full unit panels Θ=3, H(z,z,z)=(4−3z)^−2 has a different nontrivial fixed point \(q_3=(5-\sqrt{21})/6\), and the Oily normalizer and mean differ from the Θ=1 values. Never transfer clock=1, clock=2, clock=3 numerical coefficients without a passport.

### T3-05a. The three-axis static Fourier surface is **not yet a wave**

For three **full** unit observer channels, the joint limit is \(H(z_1,z_2,z_3)=(4-z_1-z_2-z_3)^{-2}\), a static grade generating function. On the unit three-torus, \(|4-\sum_i e^{i\omega_i}|\ge1\), so its Fourier symbol has no zeros or propagation pole. The exact formal local inverse is
\[
(4-X-Y-Z)^2=16-8(X+Y+Z)+(X^2+Y^2+Z^2)+2(XY+XZ+YZ).
\]
This is an invertible **spatial observation kernel**, not a Lorentzian hyperbolic propagator. The existence of three grade-frequency directions does NOT supply physical spatial coordinates or a causal wave equation. The required new ingredient is independently constrained second-order dynamics in a separate time coordinate, as tested below. A finite cyclic arithmetic grade Fourier mode is not evidence of π's selected-digit Weyl cancellation.

## T3-06. From statistical H³ to a **conditional** 3+1 spacetime and wave operator

To give H³ spatial slices a **physical-like** time coordinate τ, we must **add and declare** a separate temporal metric:
\[
ds_{\rm trial}²=-dτ²+A(τ)^2h_{H³},
\]
where h_H³ is the Riemannian Fisher metric above, with sectional curvature −1/8. This is an intrinsic 3+1-dimensional Lorentzian metric (not the same as merely using the ambient embedding variable T). For a homogeneous scale factor A, its 3-curvature is \(R^{(3)}=-3/(4A²)\). The 3+1 Hamiltonian vacuum combination is
\[
R^{(3)}+K²-K_{ij}K^{ij}=-\frac{3}{4A²}+6(\dot A/A)^2.
\]
The choice A(τ)=τ/√8 makes it zero and yields **flat Minkowski spacetime in Milne slicing**, despite negatively curved H³ spatial slices. Hence intrinsic statistical/spatial curvature is not itself evidence of gravitational spacetime curvature, observer acceleration backreaction, or a black hole horizon.

A declared minimally coupled massless scalar ψ obeys the covariant wave equation
\[
\ddot\psi+3\frac{\dot A}{A}\dot\psi-\frac1{A²}\Delta_{h_{H³}}\psi=J,
\]
with \( \Delta_{h_{H³}}=\frac18[\partial_\rho²+2\coth\rho\partial_\rho+\sinh^{-2}\rho\,\Delta_{S²}]\) on the positive-octant patch and appropriate boundary conditions. It supports wave/spectral modes once dynamics and initial data are supplied. Wave modes also exist on flat backgrounds; they cannot establish that acceleration physically deforms the geometry.

For a discrete three-dimensional cubic interaction carrier with spatial nearest-neighbor Laplacian L_3 and second-order update
\[
\psi_{t+1}-2\psi_t+\psi_{t-1}+c²L_3\psi_t=J_t,
\]
the Fourier eigenvalue is \(\lambda(\mathbf k)=4\sum_{i=1}^3\sin²(k_i/2)\), and exact dispersion is
\[
\boxed{\sin²(\omega/2)=c²\sum_{i=1}^3\sin²(k_i/2).}
\]
The uniform 3D periodic grid has λ_max≤12, so the ordinary leapfrog scheme is stably oscillatory for nonzero spatial modes when 0<c²<1/3 (at equality the highest-frequency double root can exhibit linearly growing solutions; the zero mode needs its separate constant/linear treatment). This already supports sinusoidal arithmetic lattice modes without claiming physical spin-2 gravity or π digit normality.

A key **3+1 capability absent in 2+1 vacuum GR** is the existence of two linearly independent transverse-traceless tensor wave polarizations. For a wave along the z-direction, the ansatz
\[
h_{ij}=\begin{pmatrix}
h_+&h_\times&0\\h_\times&-h_+&0\\0&0&0
\end{pmatrix}
\]
is exactly trace-free and transverse when h_+,h_× depend only on z,t; both independent profiles may satisfy the same discrete wave evolution. This proves existence of **two TT tensor-mode slots in a declared 3D lattice**, not that SUCC has derived the linearized Einstein equations or any quadrupole radiation. Primary GR/physics calibration: PDG gravitational tests review (https://pdg.lbl.gov/2023/reviews/rpp2023-rev-gravity-tests.pdf), Milne spacetime (https://link.springer.com/article/10.1007/s10701-020-00335-7).

## T3-07. Falsification / boundary

- **DISCLOSED within model:** exact original source three-positive-atom passport (15,59,243), new angular variance 164/225, exact native three-panel rational probability and source-specific 59-jet, rank-two Gamma three-channel H³ and independent-control rank condition, fixed-budget rank-two sphere, Oily clock-specific normalization, 3D lattice Fourier dispersion, two TT slots and vacuum Milne null constraint.
- **DECLARED:** independently variable gain channels on source atoms; Poisson observation law; promotion of observer-information H³ to physical spatial geometry; temporal scale factor and hyperbolic wave dynamics.
- **REFUTED:** three source atoms by themselves prove three physical dimensions; the one source variable X is a three-dimensional latent; the fixed total clock yields a third independent Fisher direction; a 3+1 Minkowski embedding is a physical observer clock; waves imply nonzero curvature; TT slots automatically satisfy Einstein evolution; source-only positivity or a filtered Weyl sum proves π normality.
- **UNVERIFIED:** operational native three-gain sensor; genuine source-selected and zero-seed-sensitive gauge holonomy; Einstein-style action and energy-momentum identity; base-16 π normality and RH.

**Next discrimination:** use a *lossless source-atom-marked* three-panel experiment with independently testable gains. Verify Jacobian rank 3 in the declared instrument, then either construct a truly source- and U_0=0-sensitive intertime carry/phase transport (including every literal integer seam and modulo-16 Walsh sector) with nonzero gauge-invariant loop defect, or record the failed bridge. Re-run same-source coherent seed s*=−π/16, matched Q_fake=15x, higher-jet-matched source, altered poles, source reset, fixed-clock ablation, and normal Stoneham 3/5 vs nonnormal de Bruijn controls. A signed o(N) estimate must be a new theorem, not restated normality.

**References:** Li, Sun & Li (2020), "A Geometric Approach to Average Problems on Multinomial and Negative Multinomial Models", Entropy 22(3) 306, DOI 10.3390/e22030306, classical hyperboloid Fisher geometry. PDG 2023 review of gravitational theory, linearized Einstein TT equations. Milne coordinate curvature control (Foundations of Physics 2020, DOI 10.1007/s10701-020-00335-7). These establish the *general classical structures*, not SUCC-specific physical significance.

**Validation authority:** source-level exact-Fraction stdlib tests and separately authored symbolic/quadrature oracle for this branch, with separate receipts. Complete root AGENTS tests, hosted CI and Lean NOT RUN. No mainstream physics or π/RH status promotion. Do not merge blindly.
