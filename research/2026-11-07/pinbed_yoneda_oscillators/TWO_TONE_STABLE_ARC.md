# Two-tone stable aperture × exact BBP source transport

**2026-11-07 · Research-only local theorem dossier · additive continuation of SUCC PR #542.**

Parent branch: research/pinbed-yoneda-fourier-relative-truth-2026-11-07, originally pinned to main d32342d375f44ddf62221ad6aff2f534abdc0a03. Read-only sibling connections: #541 (continuous Bernoulli-B2 Yoneda pin surface and its sharp dynamical weight criterion), #540 (golden single-aperture spatial Fejér triangle), #539 (circle aperture and Pisot controls), #538 (epoch critical Fejér transport), #527 (2-adic source graph no-go), #518 (observational Yoneda and ×16-invariant empirical limits), #525 (source-fixed observer gauge). Original BBP four signed poles, literal zero seed, carries and provenance are unchanged.

**All theorems below are mathematical derivations in declared source/observer models, not new academic priority or Lean-certified statements. No physical oscillator was operated. The one selected infinite signed Weyl estimate, π base-16 normality, and RH remain OPEN.**

## STP-1. Raw finite two-tone frame has an unconditional lower bound — PROVED LOCAL

Let m≥2, 1≤L<m, \(\zeta=e^{2\pi i/m}\), and let \(v\in\mathbb C^m\). At every translated pin position y, collect the two complex phase-calibrated responses

\[
R_kv(y)=\sum_{j=0}^{L-1}v(y+j)\zeta^{-kj},\qquad k=0,1.
\]

With \(\widehat v(q)=\sum_y v(y)\zeta^{-qy}\), the DFT of the observed surface is \(\widehat{R_kv}(q)=H_L(q-k)\widehat v(q)\), \(H_L(r)=\sum_{j=0}^{L-1}\zeta^{rj}\). Parseval gives

\[
\sum_{k=0}^1\|R_k v\|_{\ell^2}^2
=\frac1m\sum_{q=0}^{m-1}w_q|\widehat v(q)|^2,\qquad
w_q=|H_L(q)|^2+|H_L(q-1)|^2.
\]

For every integer r, \(|H_L(r)|\ge|\sin(\pi Lr/m)|\): for r≢0 mod m this follows from the geometric-sum denominator \(|\sin(\pi r/m)|\le1\); for r≡0 it follows from H=L and the zero sine. Put \(\theta=\pi L/m,\ x=\pi Lq/m\). Then

\[
w_q\ge\sin^2x+\sin^2(x-\theta)
=1-\cos\theta\cos(2x-\theta)
\ge c_{m,L}:=1-|\cos\theta|>0.
\]

Hence **the unnormalized two-channel frame lower bound** is

\[
\boxed{\ \|R_0v\|_2^2+\|R_1v\|_2^2
\ge (1-|\cos(\pi L/m)|)\|v\|_2^2.\ }
\]

This quantitatively strengthens the two-tone injectivity of #542; it does not rely on gcd(m,L)=1. For consecutive Fibonacci grids (m,L)=(F_(k+1),F_k), k≥2, the ratio lies in [1/2,2/3], so \(|\cos(\pi L/m)|\le1/2\) and the uniform **rational** certificate is \(w_q\ge1/2\). In the golden limit L/m→a=φ^-1, the lower constant tends to \(1-|\cos(\pi a)|≈0.6376251099\) (decimal diagnostic).

**STP-1N — normalization/noise obstruction (PROVED).** If the device outputs window **averages** \(R_k/L\) instead of raw coherent sums, the certified lower bound becomes c_(m,L)/L². This loss is not merely an artifact of the estimate: for even m≥4 at q=m/2, \(|H_L(q)|≤1\) and \(|H_L(q-1)|≤1/\cos(\pi/m)≤\sqrt2\), so \(w_{m/2}≤3\). Therefore the least singular value of the *averaged* two-channel surface operator is ≤√3/L along these grids. In particular it tends to zero for growing Fibonacci windows with even m. No unqualified uniform signal-to-noise or continuum inverse estimate follows from raw-frame stability.

## STP-2. Two modulated continuous arcs remove golden small divisors — PROVED LOCAL

For any aperture fraction \(0<a<1\) on \(\mathbb T=\mathbb R/\mathbb Z\), define **two actual probe kernels**

\[
g_{a,k}(t)=\frac{1_{[0,a)}(\{t\})}{a}\,e^{2\pi i kt},
\qquad k=0,1,
\]

and centered complex surfaces \(F_{a,k}(\mu)=g_{a,k}*(\mu-\lambda)\), with normalized Haar λ. Every probability law is admitted; no stochastic sampling, physically available actuator, or four-pole source is assumed. For two laws define the phase-sensitive observation discrepancy

\[
D_{a,2}(\mu,\nu)^2
=\sum_{k=0}^1\|g_{a,k}*(\mu-\nu)\|^2_{L^2(\mathbb T)}
=\sum_{h\ne0}w_h|\widehat\mu(h)-\widehat\nu(h)|^2,
\]

where \(\operatorname{sinc}(t)=\sin t/t\), with \(\operatorname{sinc}(0)=1\), and

\[
w_h=\operatorname{sinc}^2(\pi ah)+\operatorname{sinc}^2(\pi a(h-1)).
\]

For h∉{0,1}, the same two-sine identity yields

\[
w_h\ge\frac{c_a}{\pi^2a^2(1+|h|)^2},
\qquad c_a=1-|\cos(\pi a)|>0.
\]

For h=0,1 one sinc term is exactly 1 and this lower bound also holds (since \(c_a≤(\pi a)^2/2\)). Conversely, for h∉{0,1}, \(|\operatorname{sinc}(\pi a(h-k))|\le1/(\pi a|h-k|)\), and \((1+|h|)/|h-k|≤3\) for |h|≥2, k=0,1. At h=0,1, w_h≤2. Therefore

\[
\boxed{
\frac{\alpha_a}{(1+|h|)^2}\le w_h\le
\frac{\beta_a}{(1+|h|)^2},
\quad \alpha_a=\frac{c_a}{\pi^2a^2},\quad
\beta_a=\max\left(8,\frac{18}{\pi^2a^2}\right),\quad h\ne0.}
\]

Consequences (all proved): every w_h>0, all w_h are summable, so D is a **metric** on circle probability laws, induces weak convergence on this compact law space, and controls the signed complex mode \(|\widehat\mu(h)-\widehat\nu(h)|≤(1+|h|)D_{a,2}(\mu,\nu)/\sqrt{\alpha_a}\). This is an H^(-1)-type spectral bound. The *single* golden aperture from #540 is characteristic, but its modal weights have arbitrarily severe Diophantine small-divisor conditioning; our second coherent channel removes these extra near-zeros. The gain is one Sobolev power relative to #541's B2 weight (h^-4), not a bound on the true arithmetic Weyl coefficients.

**STP-3. Bounded ×16 law dynamics (PROVED LOCAL).** For any integer b≥2 and circle rotation t, \(T(x)=bx+t\bmod1\) obeys \(\widehat{T_*\mu}(h)=e^{-2\pi iht}\widehat\mu(bh)\). By the two-sided weights,

\[
\boxed{
D_{a,2}(T_*\mu,T_*\nu)
\le b\sqrt{\beta_a/\alpha_a}\,D_{a,2}(\mu,\nu).
}
\]

Proof: \(w_h/w_{bh}≤(\beta_a/\alpha_a)((b|h|+1)/(|h|+1))^2≤b^2\beta_a/\alpha_a\). Sum only over b-multiple output modes, a subset of all modes. The constant is independent of translation t, the laws, and the epoch. At a=φ^-1, α≈0.1691379, β=8 and b=16 give the conservative bound ≈110.04. This **repairs the unbounded one-step Lipschitz ratio of the single irrational arc aperture diagnosed in #541**, without installing its infinite discounted future-pin completion. It is an observer-geometry theorem, not exponential mixing or contraction (the upper constant exceeds one).

## STP-4. Explicit nonnegative pair kernel, and original-source O(A^-2) energy transport — PROVED LOCAL

Define the nonnegative scalar energy \(E_{a,2}(\mu)=D_{a,2}(\mu,\lambda)^2\). For \(d\in[0,1)\), the exact overlap length of two arcs of fractional length a separated by d is

\[
O_a(d)=(a-d)_+ + (a-1+d)_+,
\]

which is periodic and 1-Lipschitz under circular distance. The two channel autocorrelations are \(R_k(d)=O_a(d)e^{2\pi ikd}/a^2\) (up to choice of correlation orientation). Their real symmetric sum gives the elementary **pair kernel**

\[
K_a(d)=\frac{O_a(d)}{a^2}(1+\cos 2\pi d).
\]

The zero-Haar-centered energy for any probability μ is thus

\[
\boxed{
E_{a,2}(\mu)=\iint K_a(x-y)\,d\mu(x)d\mu(y)
-\left[1+\operatorname{sinc}^2(\pi a)\right].
}
\]

This equals the nonnegative Fourier series \(\sum_{h\ne0}w_h|\widehat\mu(h)|^2\), but K_a itself is not the literal positivity certificate; the two underlying L² norms are. The kernel is Lipschitz with respect to circular distance, with the explicit valid constant

\[
\operatorname{Lip}(K_a)\le L_a:=\frac2{a^2}+\frac{2\pi}a,
\]

since \(O_a≤a\), \(\operatorname{Lip}(O_a)≤1\), \(|1+\cos|\le2\), and \(\operatorname{Lip}(\cos2\pi d)≤2\pi\). The constant term in E has no influence on this estimate.

Now retain the **literal original BBP source**

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1),
\quad x_n=\{U_n\}.
\]

Its authenticated future tail \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\) satisfies \(0<T_n<1/[15(n+1)^2]\) for n≥1, and \(z_n=\{U_n+T_n\}=\{16^n\pi/16\}\). Over every epoch [A,2A) let μ_A^x and μ_A^z be empirical laws. For every ordered pair, circular distance between differences \(z_n-z_t\) and \(x_n-x_t\) is ≤T_n+T_t. By the kernel Lipschitz estimate,

\[
|E_{a,2}(\mu_A^z)-E_{a,2}(\mu_A^x)|
\le\frac{2L_a}{A}\sum_{n=A}^{2A-1}T_n
\le\frac{L_a}{15A^2},
\]

because \(\sum_{n=A}^{2A-1}(n+1)^{-2}≤1/(2A)\). Thus

\[
\boxed{
|E_{a,2}(\mu_A^\pi)-E_{a,2}(\mu_A^{U_0=0})|
\le\frac{2/a^2+2\pi/a}{15A^2}.
}
\]

This is an unconditional **source-specific error** in the **UNSQUARED positive energy**, valid all A≥1. It is not an estimate on \(E_{a,2}(\mu_A^x)\) itself. Numerically the bound at golden a is approximately 1.0268/A². The source-to-π transfer is distinct from #540 GA-04's one-channel coefficient and #541's Bernoulli B2 L²-norm transport.

**STP-5. Source-selected normality gate (EQUIVALENT-REFORMULATION, PREMISE OPEN).**
All w_h are strictly positive and summable; hence \(E_{a,2}(\mu_j)\to0\iff\mu_j\Rightarrow\lambda\). By the already established original-source Weyl/Green-tail bridge and dyadic epoch-to-prefix decomposition (main π frontier), we obtain

\[
\boxed{
\pi \text{ normal in base 16}\ \iff\
E_{a,2}(\mu_A^{U_0=0})\longrightarrow0
\quad\text{for all large integer epochs }A.
}
\]

This is a new, better-conditioned **testing representation**, not a proved decay theorem.

**STP-6. Hostile coherent wrong seed (PROVED negative control).**
The same original forcing with \(s_*=-\pi/16\) has completed orbit \(z_n=0\) and rational-source orbit \(U_n(s_*)=-T_n\), so its empirical energy obeys the very same transport estimate but tends to

\[
E_{a,2}(\delta_0)
=\frac2a-1-\operatorname{sinc}^2(\pi a)
\ge 2/a-2>0.
\]

Thus source tail precision, phase-pinned kernel positivity, the dynamical norm estimate, or formal compatibility alone **cannot** prove the zero-seed decay. At golden a this locked-point energy is ≈2.005638743 (display only). Other hostile controls: periodic completed beta, single-channel irrational small divisor, normalized-window noise, intensity-only phase loss, and observer rotations without declared source-fixed origin.

## STP-7. Coherent intensities recover complex responses; local BBP plaquettes remain seed-uniform

Suppose a physical or simulated observer can **actually realize phase-coherent superposition with known references** 1 and i, and read only nonnegative squared amplitudes. For \(z=x+iy\), the triple

\[
I_0=|z|^2,\quad I_1=|z+1|^2,\quad I_i=|z+i|^2
\]

determines \(x=(I_1-I_0-1)/2\), \(y=(I_i-I_0-1)/2\). This is exact polarization, valid over Q(i) for rational quadratures and over C generally. It is *not* a free capability of a generic mechanical height sensor: the coherent reference, phase origin and quadratic-intensity coupling are explicit instrument assumptions. The phase-blind homometric eight-point models of #542 remain genuine counterexamples without this reference.

For the actual BBP phase characters \(\chi_h(x_n)=e^{2\pi ihx_n}\), the source update gives the exact local phase-transport/plaquette identity

\[
\chi_h(x_{n+1})\,
\overline{\chi_{16h}(x_n)}\,e^{-2\pi ihr(n+1)}=1,
\qquad\forall h\in\mathbb Z,\ n\ge0.
\]

**Negative theorem:** this relation holds for **every initial seed**, including nonnormal completed orbits; repeated flatness of source-labelled local oscillator holonomy cannot imply π normality. A candidate breaking this relation is not compatible with the declared source; a candidate satisfying it is only source-evolution-compatible, not necessarily Haar-generic. The true zero selector must enter a **new all-epoch signed cancellation argument**, not be inferred from phase-cocycle consistency.

## Claim ledger / precise next discriminator

- **PROVED LOCAL (paper algebra):** STP-1 finite raw frame; STP-1N normalized-window no-go; STP-2 H^-1 equivalence/target modulus; STP-3 finite ×16 stability; STP-4 pair kernel and original-source energy transfer; STP-6 coherent wrong-seed countermodel; STP-7 polarization and local flatness no-go.
- **EQUIVALENT-REFORMULATION; OPEN premise:** STP-5 vanishing two-tone energy for the unique zero-seeded original BBP history.
- **UNVERIFIED:** a physical phase-calibrated superposition/intervention; a Yoneda-full/faithful functor from actual carrier actions to the proposed instrument; any genuinely source-selected signed Weyl/energy inequality; scholarly priority.
- **Next hostile theorem test:** an original-source, zero-seed-specific inequality on the joint driven pin responses across *all* large epochs that forces a nontrivial contraction of the signed h-mode or of E, while failing for s_*. Use #527 2-adic residue isometry, #534/#540 time-geometry, #541 actual dynamic law/surface naturality and main's selected-orbit carry history as **separately typed** inputs. Any seed-uniform phase-plaquette, formal inverse, or observer-gauge rotation is disqualified in advance.

### Validation boundary

The companion isolated stdlib module was exercised on exact rational BBP recurrence and calibrated Q(i) intensity inversion, all translated finite windows on grids up to 37, independent DFT-root sums and sine-form weights, continuous weights for |h|≤2000 and source epochs A=16,32,64,128. The new focused tests passed locally; no claim of a full SUCC suite, native Lean, exact-head hosted CI, independently authenticated physical apparatus or independent scholarly referee is made. Numerical scalar energies are **OBSERVED FINITE**, not all-A estimates.

**Source links:** [PR #541](https://github.com/femboy2112/SUCC/pull/541), [PR #540](https://github.com/femboy2112/SUCC/pull/540), [main π frontier](https://github.com/femboy2112/SUCC/blob/main/docs/PI_NORMALITY_FRONTIER.md), [existing categorical observer atlas](https://github.com/femboy2112/SUCC/blob/main/docs/CATEGORICAL_OBSERVER_ATLAS.md).
