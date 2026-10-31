# SUCC: the arithmetic energy–momentum mass shell of the Lorentz clock triangle

**2026-10-30 — RESEARCH ONLY.** Exact proposed parent: draft [PR #393](https://github.com/femboy2112/SUCC/pull/393) at `903fdb77ba92f14c620d7c0ab50229a2823b2ac9`; ancestral #392 and merged Main XVI `e18ba565ca540adb7edf3292f5593929e76d91c5`. **Do not** alter imported BBP sources, `U_0=0`, main, historical claims, or CI. The present work distinguishes a classical indefinite lattice norm, a **declared** Poisson-clock observation model, and the still-deterministic signed BBP circle orbit. No physical energy, physical mass, stress-energy conservation, π normality or RH is proved.

## 0. Steelman / acceptance criterion

The user's question follows an exact two-panel SUCC result: one retained positive source, two time-horizontal observation triangles, a conserved native observation budget, a Lorentz-like *projective* reallocation, and an integer golden matrix preserving a quadratic form. A useful energy–momentum relation should:

1. derive its rest parameter from the **original four-pole BBP positive source**, with no fitted mass;
2. express energy and momentum in terms of **operational readouts** of the two triangles;
3. have an authentic Lorentzian invariant under **un-normalized** light-cone clock boosts;
4. make a prediction about shared source covariance, failing under a posterior-reset control;
5. recover both SUCC's native Gamma(2)/Oily golden limit and the first finite four-pole fingerprint;
6. disclose precisely why the original π-selected carry/phase process has not acquired the same symmetry.

All six are addressed below, with separate statuses.

## 1. Integer arithmetic supplies a genuine Lorentzian norm (AR-EM-01)

Let `φ=(1+sqrt(5))/2` and `φ'=(1-sqrt(5))/2=-φ^(-1)`. For integers `u,v`, put the algebraic integer

`ξ=v-uφ`, `ξ'=v-uφ'`.

The norm, energy, and momentum of that lattice label are

\[
\begin{aligned}
N(\xi)&=\xi\xi'=v^2-uv-u^2,\\
E_{\rm ar}(u,v)&=(\xi+\xi')/2=v-u/2,\\
P_{\rm ar}(u,v)&=(\xi'-\xi)/2=\sqrt5\,u/2.
\end{aligned}
\]

Hence **identically**

\[
\boxed{E_{\rm ar}^2-P_{\rm ar}^2=N(\xi)=v^2-uv-u^2.}\tag{EM-1}
\]

The inherited SUCC golden matrix `B=[[1,1],[1,2]]` acts by `(u,v) -> (u+v,u+2v)`. It sends `ξ -> φ^(-2) ξ` and `ξ' -> φ^2 ξ'`. Accordingly the associated `(E_ar,P_ar)` transform is the usual proper 1+1 Lorentz boost with `η_B=2 log φ`; `cosh η_B=3/2` and `sinh η_B=sqrt5/2`. Integer coefficient matrix `B` preserves the norm exactly; its determinant is one. Starting from the inertial lattice point `(u,v)=(0,1)`, every integer iterate `B^k` lies on the **unit** mass shell

\[
E_{\rm ar}^2-P_{\rm ar}^2=1.
\]

The contracting embedding eigenvalue `φ^(-2)` happens to equal the separately marked Oily endpoint fixed point. This is an exact arithmetic equality; the chosen embedding in `Q(sqrt5)` is not a BBP digit-generating dynamics, and it does not establish a physical Lorentz symmetry.

## 2. Native positive source fixes an operational running rest mass (AR-EM-02)

Original authenticated four poles, for every real source tilt `a>0`:

\[
\begin{aligned}
Q(x)&=4-2e^{-3x}-e^{-4x}-e^{-5x}>0,\\
R(a)&=\int_0^\infty e^{-ax}Q(x)dx
 =\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}\\
&=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)},\\
\mu_a(dx)&=e^{-ax}Q(x)dx/R(a).
\end{aligned}
\]

Native BBP forcing is `r(n)=R(8n-7)`, and the selected arithmetic orbit is the deterministic recurrence `U_0=0, U_n=16U_(n-1)+r(n)`. The **positive** source law `μ_a` contains no information about which initial circle seed was actualized.

Scale the microscopic coordinate to `Y=aX`. Define a *dimensionless* positive source mass by its mean:

\[
\boxed{M(a):=\mathbb E_{\mu_a}Y=-a\frac{d}{da}\log R(a).}\tag{EM-2}
\]

Its explicit original-four-pole rational value is

\[
M(a)=\frac{30a^5+543a^4+3864a^3+13427a^2+22560a+14400}
{15a^5+301a^4+2397a^3+9467a^2+18540a+14400}.
\]

**Theorem (all positive a):** `1<M(a)<2` and `M'(a)>0`. The positive coefficient certificate is:

- `M(a)-1` has numerator `15a^5+242a^4+1467a^3+3960a^2+4020a` over the common positive denominator;
- `2-M(a)` has numerator `59a^4+930a^3+5507a^2+14520a+14400`;
- `M'(a)` has numerator `885a^8+27900a^7+386322a^6+3069308a^5+15305949a^4+49063680a^3+98735460a^2+114048000a+57888000`, divided by the square of the displayed positive degree-five denominator.

These are exact polynomial identities, independently rederived by the oracle. Their coefficients prove the claims *for all real* `a>0`, not only sampled native clocks. The limits and finite source fingerprint are

\[
\boxed{\lim_{a\downarrow0}M(a)=1,\qquad
\lim_{a\to\infty}M(a)=2,\qquad
M(a)=2-\frac{59}{15a}+O(a^{-2}).}\tag{EM-3}
\]

This is a source-specific interpolation from Gamma-shape-one to Gamma-shape-two local behavior. Its **name** “mass” is operationally declared: the rest clock expects `M(a)` path-count units. These units are not joules, kilograms, physical rest mass, or a derived thermodynamic cost. The original four poles (not a generic shape-two endpoint) determine the exact finite law.

## 3. Two genuinely shared triangles produce energy–momentum (AR-EM-03)

Define a **declared continuous-clock extension** of SUCC's finite Pascal observation. Draw `X~μ_a` *once*. Conditionally on this same X, draw two independent counts

\[
J_+\mid X\sim\operatorname{Poisson}(\theta_+ aX),\quad
J_-\mid X\sim\operatorname{Poisson}(\theta_- aX),\qquad\theta_\pm\ge0.
\]

Conditional independence is *not* unconditional independence: both panels retain the same source and posterior. Define the operational total and directional mean-count currents

\[
\boxed{\mathcal E=\mathbb E(J_++J_-),\qquad
\mathcal P=\mathbb E(J_+-J_-).}\tag{EM-4}
\]

Their exact values for any positive a are

\[
\boxed{\mathcal E=M(a)(\theta_++\theta_-),\qquad
\mathcal P=M(a)(\theta_+-\theta_-).}\tag{EM-5}
\]

The corresponding joint PGF for `|z|,|w|<=1` is the *original-source rational function*

\[
\boxed{\mathcal H_{a,\theta}(z,w)=\frac{R\big(a[1+\theta_+(1-z)+\theta_-(1-w)]\big)}{R(a)}.}\tag{EM-6}
\]

This holds at **every finite a**, not just in the Gamma limit. For `a->infty`, it tends to `[1+θ_+(1-z)+θ_-(1-w)]^(-2)`, the inherited Gamma(2) two-panel symbol.

Choose proper reference intensities `θ_+=θ_-=1/2`. Apply a continuous *unprojected* rapidity boost:

\[
\theta_+(\eta)=\tfrac12e^\eta,\qquad
\theta_-(\eta)=\tfrac12e^{-\eta}.
\]

Then

\[
\boxed{\mathcal E=M(a)\cosh\eta,\quad
\mathcal P=M(a)\sinh\eta,\quad
\mathcal E^2-\mathcal P^2=M(a)^2.}\tag{EM-7}
\]

More generally the invariant is `4M(a)^2 θ_+θ_-`. The *source mass* `M(a)` is unchanged by changing observer-clock orientation; source time a is held fixed. Applied to the first golden integer boost, the rest currents `(M(a),0)` become `(3M(a)/2,sqrt5 M(a)/2)` and retain the same mass shell. Along native a=8n-7 the shell tends to `E²-P²=4` as n→infty.

### Source-defined covariance form of the mass shell

The shared latent gives exactly

\[
\operatorname{Cov}(J_+,J_-)=\theta_+\theta_- a^2\operatorname{Var}_{\mu_a}(X).
\]

Define the **effective source shape**

\[
\rho(a):=\frac{(\mathbb E_{\mu_a}X)^2}{\operatorname{Var}_{\mu_a}(X)}
=\frac{[\partial_a\log R(a)]^2}{\partial_a^2\log R(a)}.
\]

For positive θ±, this yields a second, entirely operational expression of the same exact invariant:

\[
\boxed{\mathcal E^2-\mathcal P^2=4\rho(a)\operatorname{Cov}(J_+,J_-).}\tag{EM-8}
\]

**Theorem:** For the original four poles, `1<ρ(a)<2`, `ρ'(a)>0`, and

\[
\boxed{\rho(a)=2-\frac{1379}{150a^2}+O(a^{-3}).}\tag{EM-9}
\]

**All-a algebraic certificate.** Let `C=15a²+121a+240`, `D=a(a+3)(a+4)(a+5)`, `U=D'C-DC'` and

`V=((D')²-D''D)C²+(C''C-(C')²)D²`.

Then `ρ=U²/V`. The denominator `V` is positive for a>0 (it is `(DC)² Var X`). Direct polynomial expansion gives:

- `U²-V` has **nonnegative** coefficients and is positive for a>0;
- `2V-U²` is the **strictly positive** polynomial `4137 a^8+125532 a^7+1672998 a^6+12801660 a^5+61570009 a^4+190760640 a^3+372124800 a²+418176000 a+207360000`;
- `(U²)'V-U²V'` has nonnegative coefficients and a strictly positive constant term.

These exact coefficient conditions certify both bounds and monotonicity. The independently written SymPy oracle reconstructs all polynomials, both asymptotic coefficients and the characteristic response.

**Crucible — posterior resetting:** If each panel samples an *independent* new `X`, their expected J± remain unchanged, but `Cov(J_+,J_-)=0`. Then the covariance expression (EM-8) does not hold whenever θ+θ->0. Consequently this version of the mass shell sees **retained field memory**, whereas a representation using the mean clock currents alone does not.

## 4. Exact source Lorentz-covariant dual observation (AR-EM-04)

For any nonnegative dual probes `t_+,t_-`, consider the original-source Laplace observable

\[
\mathcal Z_a(\theta,t)=\frac{R(a[1+\theta_+ t_++\theta_- t_-])}{R(a)}.
\]

A paired boost

\[
\theta_\pm\mapsto e^{\pm\eta}\theta_\pm,\qquad
 t_\pm\mapsto e^{\mp\eta}t_\pm
\]

leaves `Z_a` **exactly unchanged for every a>0**. Define dual coordinates `t_+=q_0-q_1`, `t_-=q_0+q_1`; then

\[
\boxed{\mathcal Z_a=\frac{R\big(a[1+(\mathcal E q_0-\mathcal P q_1)/M(a)]\big)}{R(a)}.}\tag{EM-10}
\]

Both `(E,P)` and `(q0,q1)` transform as Lorentz vectors under this paired action. The bilinear scalar `E q0-P q1` is invariant. Indeed the operational currents are first logarithmic derivatives at the origin,

`E=-(partial_(q0) log Z)|_(q=0)`, `P=(partial_(q1) log Z)|_(q=0)`.

**Authentic first jet.** For fixed `d=1+θ_+t_++θ_-t_->=1`,

\[
\boxed{\frac{R(ad)}{R(a)}=
\frac1{d^2}+\frac{59}{15a}\frac{d-1}{d^3}+O_d(a^{-2}).}\tag{EM-11}
\]

The Gamma-matched fake `R_fake(a)=15/a²` is **exactly** `d^-2` and has no finite 59 correction. This extra finite coefficient is invariant under paired boosts because d itself is invariant. It is positive-source discrimination, not selected π-phase cancellation.

The Poisson-clock extension is deliberately **different** at finite n from the original integer-depth Bernoulli/Pascal sensor. The local frequency torus `z_+=exp(iω_+)`, `z_-=exp(iω_-)` is not preserved by the real dual transformation `1-z -> e^{±η}(1-z)`. Hence **the full selected arithmetic Fourier/carry dynamics is not Lorentz-covariant by this theorem**.

## 5. Exact native finite Pascal mass-shell analogue (AR-EM-05)

For the inherited original-source Bernoulli sensor `p(X)=1-e^{-8X}`, fix integer panel budgets `m_+,m_-`. Let

`u_a=E p(X)=1-R(a+8)/R(a)`,
`v_a=Var p(X)=R(a+16)/R(a)-[R(a+8)/R(a)]²>0`.

For the shared retained latent,

\[
\begin{aligned}
\mathcal E_m&=(m_++m_-)u_a,\\
\mathcal P_m&=(m_+-m_-)u_a,\\
C_m&=\operatorname{Cov}(J_+,J_-)=m_+m_- v_a.
\end{aligned}
\]

Thus the **native exact-rational shell** is

\[
\boxed{\mathcal E_m^2-\mathcal P_m^2=4\rho_{\rm Pascal}(a)C_m,
\quad \rho_{\rm Pascal}(a)=u_a^2/v_a.}\tag{EM-12}
\]

A fully independent finite-difference series oracle shows

\[
\begin{aligned}
\rho_{\rm Pascal}^{BBP}(a)
&=2+\frac{48}{a}+\frac{18061}{150a^2}+O(a^{-3}),\\
\rho_{\rm Pascal}^{fake}(a)
&=2+\frac{48}{a}+\frac{224}{a^2}+O(a^{-3}),\\
\rho_{\rm Pascal}^{BBP}(a)-\rho_{\rm Pascal}^{fake}(a)
&=-\frac{15539}{150a^2}+O(a^{-3}).
\end{aligned}\tag{EM-13}
\]

The finite native Bernoulli readout carries a universal `48/a` first correction **not** present in Poisson's effective rank; prematurely identifying their finite shapes would be false. Its original-source difference first appears at second order. This is a concrete transport/calibration test, not a claim of source uniqueness against higher-jet-matched mutants.

## 6. A sharp budget-versus-mass obstruction, and the signed golden co-moving mark (AR-EM-06)

**No-go.** The projective clock action of inherited PR #393 fixes the panel budget `θ_++θ_-=1`. A genuine unprojected Lorentz boost on the rest shell fixes `4θ_+θ_-=1`. Both cannot hold nontrivially: by AM–GM, simultaneous sum 1 and product 1/4 force `θ_+=θ_-=1/2`. Therefore a real nonzero boost *changes the total coordinate observation clock*, and conserving that total clock by projective renormalization changes the mass-shell factor to `1-v²` where `v=θ_+−θ_-`. These are different observers, not a contradiction.

At the first arithmetic golden boost `η_B=2logφ`, the proper-clock values are

\[
\theta_+=\varphi^2/2,\quad\theta_-=\lambda^2/2,\quad
\theta_++\theta_-=3/2,\quad\lambda=\varphi^{-1}.
\]

The ordinary untransformed total-grade PGF at the Gamma(2) limit becomes

`[1+(3/2)(1-z)]^(-2)`;

its nontrivial fixed point is **not** `λ²`. If the **measurement probes also transform**, however, the original golden readout can be preserved. In the rest frame evaluate both panel marks at `z=λ²` so their common `t=1-z=λ`. The paired boost requires

\[
\boxed{z_+=1-\lambda^3,\qquad z_-=1-\varphi=-\lambda.}\tag{EM-14}
\]

The second mark is **negative**: it probes a genuinely *signed* analytic combination of the grade weights, not a positive probability conditioning. Yet

\[
\frac1{[1+\theta_+(1-z_+)+\theta_-(1-z_-)]^2}
=\frac1{(1+\lambda)^2}=\lambda^2.
\]

The finite **authentic** value is `R(aφ)/R(a)` rather than exactly `λ²`, with the inherited source correction `+59 λ^4/(15a)+O(a^-2)` from EM-11. The first golden boost crossing into a signed panel occurs because the dual probe changes its orientation; it does **not** establish a unit-modulus circle Fourier mode, new π-normality cancellation, or a physically forced Lorentz transformation.

## 7. Decisive scope / π normality firewall (AR-EM-07)

The new shell and paired covariance are entirely in the positive source / declared observation law. They hold unchanged for the same original four poles with *any* BBP initial seed `s`, including the coherent preparation `s*=-π/16` for which `U_n(s*)=-T_n->0`, the absolute signed phase `e(hU_n(s*)) ->1`, and π normality fails for that selected path. They cannot by themselves yield a bound on the authentic `T_N(h)=Σ_{n<=N}e(hU_n(0))` beyond the trivial `|T_N(h)|<=N`.

The source has its own rank-one-to-rank-two mass running, but neither a 1+1 Minkowski spacetime metric, a physical speed of light, an energy unit, energy conservation across actual time n, nor a Lorentz-covariant actual integer-carry map has been derived. The mass changes under `a` evolution while remaining invariant under an observer rapidity boost at fixed a; those are two **different operations**.

**Next verdict-changing probe:** attach original `U_0=0` intermediate literal carry `κ_(n+j)`, final `κ_(n+j+k)`, original phase and full q6/4-bit Walsh masks to the exact Poisson-clock/mass-shell operator. Ask whether any *source-derived* transport inequality controls a noncentral signed common-mode observable on a growing harmonic band; test the coherent counterseed, cubic-jet source mutant, independent reset, fixed-total projective observer, and nonnormal periodic digit controls. A positive-field Lorentz invariant alone is not a Weyl saving. `π` base-16 normality / RH remain **OPEN**.

## Validation and epistemic status

- **All-a source inequalities** have explicit positive-coefficient polynomial proofs; their exact source coefficients, Lorentz metric and asymptotic jets are independently reconstructed by SymPy.
- Standalone stdlib `Fraction` source tests exercise the original four signed poles, source mass/rank, both Poisson and native Pascal clocks, dual covariance, norm-1 golden integer orbits, posterior reset, fake source, budget no-go and seed blindness.
- All arithmetic and probabilistic identities are classical consequences of the stated model. Academic priority and a physical realization are **UNVERIFIED**. No Lean theorem or hosted CI completion claimed.
- Parent PR #393 remains a distinct *projective* clock family; no silently rewritten parent source, seed or accepted proof contract.
