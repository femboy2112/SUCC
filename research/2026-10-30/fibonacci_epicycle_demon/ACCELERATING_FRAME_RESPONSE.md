# Operation Accelerating Frame — virtual-field response, information saturation and four-pole coupled detector

Research date 2026-10-30. Additive **DRAFT RESEARCH ONLY** from PR #397 based on Main XVI e18ba565ca540adb7edf3292f5593929e76d91c5. Read-only source passes: PR #392 (shared Gamma source), #393 (projective Lorentz clock), #394 (original-source information mass), #396 (human T-action), #397 (Oily and inertial-contact). No original signed BBP poles, U_0=0, frozen sources, claim namespaces, production code, main, or CI changed. π base-16/base-3 normality and RH remain OPEN; no physics equivalence is asserted.

## ARC-01. Three distinct meanings of a frame-induced "field perturbation"

1. **Pure coordinate transport** changes components, not the intrinsic carrier. For the unprojected Poisson clock extension of #394, the original-source running mass M(a)=−a R'(a)/R(a), and information-energy / momentum E=M(a)cosh η, P=M(a)sinh η satisfy E²−P²=M(a)². For constant a and η=η(τ), the apparent mixing obeys E-dot=η-dot P and P-dot=η-dot E. A co-moving covariant derivative D_τ=∂_τ−η-dot [[0,1],[1,0]] annihilates the vector. The connection A=K dη is pure gauge; one-dimensional frame transport cannot by itself produce intrinsic curvature. When a varies, D_τ(E,P)=(dM/dτ)(cosh η,sinh η), detecting actual source-clock change.
2. **Observer/channel redistribution** changes the joint law of observed marks, even with unchanged carrier. Its time-dependent response is measurable but is not a physical field disturbance.
3. **Source-sensitive measurement or backaction** changes the conditional posterior on X, or an independently specified dynamical carrier state. The former is Bayesian; only an actual coupling/action with its balance laws justifies physical backreaction.

Physical analogy and boundary: Rindler acceleration has a horizon in a region of flat Minkowski spacetime, with no nonzero Minkowski Riemann curvature. The Unruh response concerns a coupled quantum detector and requires its QFT assumptions. A classical SUCC probability field is not a quantum vacuum, nor does acceleration alone create heat. Sources: https://iqi.rwth-aachen.de/wp-content/uploads/lecture_notes/SRT_EN.pdf ; https://doi.org/10.1088/0264-9381/23/22/026 ; https://journals.aps.org/prd/abstract/10.1103/PhysRevD.76.064008 .

## ARC-02. Exact normalized-clock susceptibility and the corrected Oily normalizer

Take shared latent Y~Gamma(2,1). Conditional on Y, two marked Poisson observation panels have independent counts J|Y~Poisson(pY), K|Y~Poisson((1−p)Y), with **fixed total budget one** and
\[
p=p_\eta=\frac{e^\eta}{2\cosh\eta}=\frac{1+\tanh\eta}2.
\]
Then
\[
H_\eta(z,w)=\mathbb E[z^Jw^K]=[2-p_\eta z-(1-p_\eta)w]^{-2},\quad
H_\eta(z,z)=(2-z)^{-2}.
\]
The total S=J+K has P(S=s)=(s+1)/2^(s+2), invariant under η. Conditional J|S=s~Binomial(s,p_\eta). Thus observer motion redistributes directional labels, not the total source grade or underlying Gamma latent.

Use the same harmonic/golden tile readout as #392/#397:
\[
D_s=H_{s+1}-\gamma-\lambda^{s+2},\quad\lambda=\varphi^{-1}.
\]
Under **fixed total budget one**, its normalized Oily tilt has
\[
Z_{OM,1}=\sum_s \frac{s+1}{2^{s+2}}D_s
=1-\gamma+\log2-\frac1{(1+2\lambda)^2}
=\frac45+\log2-\gamma,
\]
\[
\bar s_{OM,1}=
\frac{3-2\gamma+2\log2-2/(5\sqrt5)}
{\frac45+\log2-\gamma}
=3.3331941754643366\ldots.
\]
**Mandatory clock passport:** 5.658041726438... from existing #397 refers to **two FULL depth-n panels** with theta_1+theta_2=2, H(z,z)=(3−2z)^−2; it is NOT the conserved-budget observer mean. Earlier intermediate trial erroneously mixed these clocks and failed one test; corrected before commit. The underlying conditional tile D_s stays the same, but its marginal normalization and mean change.

Under this exact tilt, for a fixed-budget observation experiment,
\[
\mathbb E_{OM,\eta}[J-K]=\bar s_{OM,1}\tanh\eta,\quad
\frac{d}{d\tau}\mathbb E[J-K]
=\bar s_{OM,1}\operatorname{sech}^2\eta\,\dot\eta.
\]
The last derivative is a **family-of-experiments response**, not necessarily the physical time-rate of an accumulating point process. In the unnormalized clock model of #394, total mean M(a)coshη grows, and no fixed-budget saturation can be inferred.

The exact Oily KL between directional experiments and rest is
\[
D_{KL}(W_\eta\Vert W_0)
=\bar s_{OM,1}\,[\eta\tanh\eta-\log\cosh\eta].
\]
Its Fisher metric follows directly from the score
\(\partial_\eta\log W_\eta(j,k)=(j-k)-(j+k)\tanh\eta\):
\[
g_{\eta\eta}=\bar s_{OM,1}\operatorname{sech}^2\eta,\quad
\ell_F(\eta)=\sqrt{\bar s_{OM,1}}\,\arcsin(\tanh\eta).
\]
**Saturation:** \(\ell_F(+\infty)=\frac\pi2\sqrt{\bar s_{OM,1}}=2.867808741\ldots\). This is a finite information-statistical boundary from normalization (p→1), NOT a physical event horizon, curvature singularity, or universal cap on an observer's contact with the carrier. At golden η_F=2logφ, \(\tanh\eta_F=\sqrt5/3\) and the directional mean is \(\bar s_{OM,1}\sqrt5/3\).

## ARC-03. Temporal response without source backreaction; an exact no-go

In a declared marked Poisson process with constant total event intensity Y and source-independent mark allocation p_\eta(t), the joint likelihood of S time-stamped events with marks σ_i=±1 is, conditional on Y, proportional to
\[
Y^S e^{-TY}\prod_i p_{\eta(t_i)}^{1_{\sigma_i=+}}
(1-p_{\eta(t_i)})^{1_{\sigma_i=-}}.
\]
The mark factors do **not** depend on Y, so the retained posterior is always
\[
d\mu_{a|history}(x)\propto (ax)^S e^{-Tax}\,\mu_a(dx),
\]
independent of the η(t) schedule. This is true of the authentic four-pole source and any common source mutant. A moving frame alone changes **marked observation statistics**, not the latent posterior, under this source-blind instrument.

The exact history log-likelihood ratio against the at-rest p=1/2 instrument is
\[
\log \frac{P_\eta(history)}{P_0(history)}
=\sum_i[\sigma_i\eta(t_i)-\log\cosh\eta(t_i)].
\]
The full time protocol matters even if integrated endpoints coincide. Example: Bernoulli mark probabilities (p1,p2)=(3/4,1/4) versus their temporal reversal give the same total grade law, but probability of the marked history (+,-) is respectively 9/16 and 1/16, an **exact ninefold chronological evidence ratio**. Oily grade-only weighting preserves this ratio. This is a protocol-history information defect, NOT geometrical curvature or a noncommuting latent-source likelihood.

## ARC-04. Minimal declared acceleration-sensitive source coupling (new-to-program, exact)

Let f(x)=e^(−8x), b(x)=f(x)(1−f(x))∈[0,1/4], and use an explicitly specified acceleration-protocol label α_i∈{−1,+1}. Modify the conditional mark response to
\[
P(+\mid x,\alpha_i)=\frac12+\epsilon\,\alpha_i b(x),
\quad P(-\mid x,\alpha_i)=\frac12-\epsilon\,\alpha_i b(x),
\quad|\epsilon|\le1.
\]
This is a valid conditional probability law. It is a **new declared detector coupling**, NOT forced by relativity, BBP, or observer motion. The original positive source \(\mu_a(dx)=e^{-ax}Q(x)dx/R(a)\), with
\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x},\quad
R(a)=4/a-2/(a+3)-1/(a+4)-1/(a+5),
\]
is kept fixed.

Compare time-ordered acceleration labels (α1,α2)=(+1,−1) and two marked histories h+=(+,-), h−=(-,+), which have identical total grade. Their source likelihoods are
\[
L_\pm(x)=[\tfrac12\pm\epsilon b(x)]^2.
\]
With m_k(a)=E_{\mu_a}[b(X)^k], their exact evidence normalization is Z_\pm=1/4±ε m_1+ε² m_2 and conditional b expectation
\[
E[b\mid h_\pm]=
\frac{m_1/4\pm\epsilon m_2+\epsilon²m_3}
{1/4\pm\epsilon m_1+\epsilon²m_2}.
\]
Therefore
\[
\boxed{\Delta_b(a,\epsilon)=
E[b\mid h_+]-E[b\mid h_-]
=8\epsilon\,{\rm Var}_{\mu_a}(b(X))+O_a(\epsilon^3).}
\]
Variance strictly positive for all a>0, giving a true difference in the **conditional virtual field**. It remains Bayesian state update, not physical substrate backreaction.

Crucially the original four signed BBP poles control every b-moment exactly:
\[
m_k(a)=\frac1{R(a)}
\sum_{j=0}^k(-1)^j\binom kj R(a+8(k+j)),\qquad k=1,2,3.
\]
Compare Q against the Gamma-matched fake Q_fake(x)=15x, R_fake(a)=15/a². The original source expansion Q(x)=15x−59x²/2+... implies, for the finite-source **variance difference**,
\[
\boxed{
{\rm Var}_{BBP}(b)-{\rm Var}_{fake}(b)
=-\frac{128\cdot59}{15a^3}+O(a^{-4}).
}
\]
Thus the leading acceleration-sensitive history contrast has a source-specific 59-jet at order ε/a³ when \epsilon is small. The same leading rank-two term Var(b)~128/a² appears for both sources and is not uniquely identifying. A higher-jet-matched fake remains a required hostile control. The finite model permits an exact rational Fraction verification.

The response remains sensitive to observer protocol and total clock; assigning α_i=η-dot(t_i) requires a time unit and a physical acceleration-to-detector-response law, neither supplied by current SUCC. The marker α_i here is **not** assumed to be a physical acceleration measurement.

## ARC-05. What's missing for genuine curvature/selected arithmetic

- Boost-induced component motion is canceled by correct co-moving transport. Only an operationally nonzero curvature/holonomy after removing pure-gauge effects could justify geometric backreaction.
- Source-dependent posterior response is not the same as physical field reaction C_{t+1}≠C_t; that requires a declared dynamical coupling and its independent energy/information ledger.
- Even the exact 59-jet uses the **positive auxiliary source** and a new detector law. It does not yield a signed π digit Weyl saving. The actual four-pole selected U_0=0 circle/carry process is deterministic and remains uncoupled to the auxiliary Poisson marks by the repo's existing axioms.
- A proof-target observer must record chronological marks, source posterior, intermediate literal carries, full four-bit Walsh modes, and selected signed phase. Use same-forcing coherent seed s*=-π/16, fake Q=15x, matched jets, reset-posterior and normal Stoneham/non-normal de Bruijn controls. Demand a genuinely new zero-seed-sensitive all-horizon arithmetic inequality rather than a normality-equivalent filter.

**Claim statuses:** ARC-01 classical boost transport + declared source mass; ARC-02 exact normalized-clock classical Gamma/Oily calculations, corrected clock passport; ARC-03 proved source-blind posterior no-go and chronological history ratio; ARC-04 proved positive exact-rational declared interaction and first source jet; ARC-05 selected and physical bridges OPEN/UNVERIFIED. Root tests, hosted CI, Lean, external referee not run for this research addition. Run the standalone probe as a reproducibility check; finite checks do not prove the asymptotic statements.
