# Principia Observatoris — Gamma Genesis: a pointed successor grows a Mellin-weighted volume

**2026-11-14.** Research-only proposed child of [SUCC PR #632](https://github.com/femboy2112/SUCC/pull/632), itself following the gauge-anchored π/RH work #631. **Origin:** Leah's hypothesis that Gamma *emerges* when a value is distributed over an infinitesimal basis, the resulting field is twisted/evolved by an exponential, and an integral realizes a new volume attached to the carrier. We reconstruct that idea through the multiplicative Haar/Mellin transform, an origin-pointed convolution semigroup, and an exact source-relative Green/Mellin bridge. The original four signed BBP poles, literal U0=0, source archives, historical theorem statuses and production remain unchanged.

**Scope/claim ledger:** Classical standard results are called CLASSICAL; exact elementary algebra derived here is PROVED PAPER within its stated model and independently tested separately; **new-to-SUCC** means implementation/synthesis only, not scholarly priority. An abstract Gamma semigroup and a physically operating BBP/Weil sensor are different types. Base-16 π normality, R0, completed signed Weil positivity, RH, gravitational physics and universal observer optimality remain **OPEN/UNVERIFIED**.

## GG-01 — The multiplicative carrier and the two transported modes (CLASSICAL)

The multiplicative group \(\mathbb R_{>0}\) has invariant Haar measure \(dt/t\); its continuous characters include \(\chi_s(t)=t^s\), for complex \(s\) when the output is allowed to be non-unitary. The additive attenuation semigroup \(E_t(1)=e^{-t}\) solves \(\partial_tE=-E\) with \(E_0=1\). Their Mellin pairing is

\[
\boxed{Z(s)=\langle \chi_s,E\rangle_{dt/t}=\int_0^\infty t^se^{-t}\frac{dt}{t}=\Gamma(s),\quad \Re s>0.}\tag{G1}
\]

Writing \(t=e^u\), \(dt/t=du\), gives the *logarithmic carrier* formulation
\[
\boxed{Z(s)=\int_{-\infty}^{\infty}\exp(su-e^u)\,du.}\tag{G2}
\]

For a positive real \(s\), the normalized log-coordinate density \(\exp(su-e^u)/\Gamma(s)\) has a unique mode at \(u=\log s\) (log-density derivative \(s-e^u\), second derivative \(-e^u\)). Its physical time-coordinate pushforward is \(\operatorname{Gamma}(s,1)\), whose mean is \(s\) and variance is \(s\). In the **t** density, the mode is instead \(s-1\) when \(s>1\); modes change under coordinate transformations. This makes the author's "a volume shifted to s" precise as a **shape- and chart-dependent centering**, not literal Euclidean translation.

**Spectral interpretation (the precise complex "twist").** For every real \(\sigma>0\), \(s=\sigma+i\omega\) is a Fourier character in log coordinates:
\[
\boxed{\frac{\Gamma(\sigma+i\omega)}{\Gamma(\sigma)}
=\mathbb E_{T\sim\operatorname{Gamma}(\sigma,1)}[e^{i\omega\log T}].}\tag{G2a}
\]
The normalized Gamma volume therefore has a genuine, *signed complex Mellin–Fourier spectrum*. For any \(\omega\ne0\) its modulus is strictly below 1: equality in the complex triangle inequality would require \(e^{i\omega\log T}\) to be a.s. constant, impossible for a continuous positive density on \(0<T<\infty\). Riemann–Lebesgue further gives decay as \(|\omega|\to\infty\). At \(\sigma=2\), the classical identity \(|\Gamma(2+i\omega)|^2=(1+\omega^2)\pi|\omega|/\sinh(\pi|\omega|)\) for \(\omega\ne0\) makes the phase attenuation explicit. This is **signed spectral cancellation in the log-Gamma coordinate**, *not* a claim about the chronology of BBP fractional phases.

The point evaluations \(\delta_t\) provide a useful distributional decomposition for an integral, but an uncountable family of point masses is **not** a Hilbert orthonormal basis or a family of independent random variables. One should not assert quantum amplitudes, a physical continuum or stochastic independence merely from an integral sign.

**Where the two weights come from:** if a nonzero continuous scalar \(\chi\) respects multiplicative composition \(\chi(ab)=\chi(a)\chi(b)\), then \(\chi(t)=t^s\) for some complex exponent \(s\) (write \(t=e^u\) and solve the additive Cauchy equation). If a continuous, strictly positive one-stage **survival function** obeys stationary memorylessness \(S(t+v)=S(t)S(v)\), \(S(0)=1\) and is nontrivial, then \(S(t)=e^{-\lambda t}\) for some \(\lambda>0\). Choosing the rate-one clock is a unit convention. Thus both the **power-law twist** and the **exponential attenuation** follow from compositional character laws—**if** those laws are source-authenticated. Merely saying "start at zero" does not establish memorylessness or multiplicative scale invariance.

The choice of **character**, **Haar measure**, and **attenuation kernel** is the actual structural content. Different attenuation produces a different Mellin transform: the Gamma functional is not forced by `SUCC(0)` alone. With this source choice, integration by parts yields \(\Gamma(s+1)=s\Gamma(s)\), \(\Gamma(1)=1\) and integer \(\Gamma(n)=(n-1)!\). Bohr–Mollerup supplies the uniqueness of a positive **log-convex** real function satisfying both \(f(1)=1\) and \(f(s+1)=sf(s)\) (classical). Analytic continuation beyond \(\Re s>0\) is an additional meromorphic construction, not a positive probability density.

**Relational clock gauge.** Under a unit change \(t'=ct\) and accompanying source rate \(\lambda'=\lambda/c\), the dimensionless \(\lambda t\) is invariant. The partition function \(Z(s,\lambda)=\int t^{s-1}e^{-\lambda t}dt=\Gamma(s)\lambda^{-s}\) obeys \(\lambda^s Z(s,\lambda)=\Gamma(s)\), invariant under this compensated change. Holding \(\lambda\) fixed while rescaling \(t\) is **not** the same source clock. This is a genuine elementary gauge-compatible relational reference within the declared exponential-clock family.

## GG-02 — Construct Gamma from zero, one independent waiting step at a time (CLASSICAL / PROVED)

The distinguished origin is the Dirac probability measure \(g_0=\delta_0\), and one allowed waiting step has density \(g_1(t)=e^{-t}\mathbf1_{t>0}\). Assume **independent stationary nonnegative step waiting times**, and define the next generated volume by convolution: \(g_{n+1}=g_n*g_1\). Its exact density for \(n\ge1\) is
\[
\boxed{g_n(t)=\frac{t^{n-1}e^{-t}}{(n-1)!}\mathbf1_{t>0}.}\tag{G3}
\]

**Direct SUCC-volume proof:** The independent joint density of \((t_1,\ldots,t_n)\ge0\) is \(\exp[-\sum_jt_j]\). On the hyperplane of fixed sum \(t\), integrate out \(n-1\) coordinates constrained by \(\sum_{j<n}t_j\le t\); their simplex has Lebesgue volume \(t^{n-1}/(n-1)!\), so the total arrival time has density (G3). At step n a higher-dimensional simplex of independently generated histories has been pushed down to one aggregate carrier coordinate. The origin is not reselected at each step.

For positive real \(\alpha\), define \(g_\alpha(t)=t^{\alpha-1}e^{-t}/\Gamma(\alpha)\). The beta integral proves
\[
\boxed{g_\alpha*g_\beta=g_{\alpha+\beta},\qquad g_0=\delta_0\text{ weakly}.}\tag{G4}
\]

**Uniqueness contract:** If \((\mu_\alpha)_{\alpha\ge0}\) is a *weakly continuous* convolution semigroup of probability measures on \([0,\infty)\), with \(\mu_0=\delta_0\) and \(\mu_1(dt)=e^{-t}dt\), then it must be the Gamma family. For every Laplace parameter \(q\ge0\), \(L_\alpha(q)=\int e^{-qt}d\mu_\alpha\) is positive, multiplicative under parameter addition and continuous, and \(L_1(q)=1/(1+q)\). Therefore \(L_\alpha(q)=(1+q)^{-\alpha}\); uniqueness of Laplace transforms fixes \(\mu_\alpha\). **Without** independent convolution, weak continuity and the exponential one-stage clock, SUCC successor alone does not force this interpolant.

**Hostile control:** Two perfectly correlated Exp(1) waits each have the correct marginal, yet their sum is \(2T\sim\operatorname{Exp}(1/2)\), not Gamma(2,1). The source coupling/independence premise is load-bearing.

## GG-03 — Gamma as an analytic observer update (CLASSICAL / PROVED)

For \(s>0\) let \(\nu_s(dt)=t^{s-1}e^{-t}dt/\Gamma(s)\). For any \(a>-s\) the positive reweighting operator
\[
\mathsf U_a(\nu_s)(dt)=\frac{t^a\nu_s(dt)}{\mathbb E_{\nu_s}[T^a]}
\]
produces exactly \(\nu_{s+a}\) because \(\mathbb E_{\nu_s}[T^a]=\Gamma(s+a)/\Gamma(s)\). Therefore
\[
\boxed{\mathsf U_b\mathsf U_a\nu_s=\mathsf U_{a+b}\nu_s,\qquad\mathsf U_0=\operatorname{id}.}\tag{G5}
\]

This is an **exact normalized measure tilt**, a rigorous interpretation of "twist, realize, retwist". Unless one has a sensor with genuine likelihood proportional to \(t^a\) (bounded/normalized on the relevant source), it is not automatically a physically realizable Bayesian observation. For integer \(s=n\), \(\mathbb E[\log T]=\psi(n)=H_{n-1}-\gamma\); the classical Euler–Mascheroni depth finite part arises from differentiating this source partition function, not by calling every observer defect \(\gamma\).

## GG-04 — The volume becomes a discrete SUCC wave: an exact Poisson/Gamma square (CLASSICAL / PROVED)

Define a *separately declared* Poisson observation channel \(P(j\mid t)=e^{-t}t^j/j!\). Applied to a \(\operatorname{Gamma}(\alpha,1)\) intensity, it gives
\[
\boxed{w_j^{(\alpha)}=\int_0^\infty P(j\mid t)g_\alpha(t)dt
=\frac{\Gamma(j+\alpha)}{\Gamma(\alpha)j!\,2^{j+\alpha}},\quad j\ge0.}\tag{G6}
\]

The generating function is \(G_\alpha(z)=(2-z)^{-\alpha}\), so
\[
\boxed{w^{(\alpha)}*w^{(\beta)}=w^{(\alpha+\beta)},\qquad w^{(0)}=\delta_0.}\tag{G7}
\]

**Commuting observational square:** taking the sum of two *independent* Gamma latent intensities and then sampling a Poisson count has the same outcome law as sampling independent Poisson counts first and adding those counts. Both paths deliver \(w^{(\alpha+\beta)}\). Thus the **positive** source-volume construction and its **discrete** observer projection commute, subject to the explicit independence and Poisson-channel contracts.

For the authentically source-derived critical two-stage Oily waiting law, \(\alpha=2\) gives
\[
\boxed{w_j^{(2)}=(j+1)/2^{j+2}.}\tag{G8}
\]

This is an exact equality of **probability laws**, not evidence that the original BBP physical mechanism contains a Gamma-distributed latent intensity or a Poisson sensor. The Oily source already constructs the same coefficients via two geometric waiting loops, providing a second realization of the law without selecting the latent semantics. Arbitrary \(\alpha\) is a *mathematical* continuous-depth extension; the original positive Oily source authenticates two stages, not fractional physical observers.

## GG-05 — The original zero-seeded BBP Green tail is a source-specific Mellin moment (PROVED SOURCE ALGEBRA)

**Do not alter the source.** Take the original signed four-pole forcing
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,
\]
with the exact positive integral \(r(n)=\int_0^1 x^{8n-8}Q(x)dx\), where
\[
Q(x)=4-2x^3-x^4-x^5=(1-x)(x^2+2)(x^2+2x+2).
\]

Its **actual** source-coupled Green tail is
\[
T_n=\sum_{j\ge1}16^{-j}r(n+j)=\int_0^1x^{8n}\frac{Q(x)}{16-x^8}dx.
\]

Exactly canceling the polynomial factors of the *same* original source (not a new source law) yields
\[
\boxed{T_n=\int_0^1x^{8n}R(x)dx,\quad R(x)=\frac{1-x}{(2-x^2)(x^2-2x+2)}.}\tag{G9}
\]

For \(m=8n\) write \(I_m=\int x^m R(x)dx\). Put \(\delta=1-x\); the source denominator is
\[
D(\delta)=1+2\delta+2\delta^3-\delta^4\ge1,
\quad R(1-\delta)=\frac{\delta}{D(\delta)}.
\]

Two algebraic residual factorizations, valid throughout \(0\le\delta\le1\), are
\[
0\le \frac1{D(\delta)}-(1-2\delta)\le4\delta^2,
\quad -20\delta^3\le \frac1{D(\delta)}-(1-2\delta+4\delta^2)\le0.
\]

Let \(B_k(m)=\int_0^1x^m(1-x)^k dx=k!/\prod_{j=1}^{k+1}(m+j)\). Integrating the source-pointwise bounds yields the **new all-depth rational enclosure**
\[
\boxed{B_1-2B_2+4B_3-20B_4\ \le I_m\le\ B_1-2B_2+4B_3.}\tag{G10}
\]

Consequently, with the original source and no fitted constants,
\[
\boxed{I_m=m^{-2}-7m^{-3}+55m^{-4}+O(m^{-5}),\quad m\to\infty.}\tag{G11}
\]

The coefficients are certified by exact rational bounds and symbolic expansion, not a finite numerical fit. In particular \(T_n\sim\Gamma(2)/(8n)^2=1/(64n^2)\), recovering the existing SUCC/Oily Gamma2 endpoint with a stronger explicit next-order error certificate. The exact \(I_m\) also has independently certified positive rational *series* enclosures from original four-pole forcing, checked without numerical approximation of π.

**Critical type:** the signed rational orbit \(U_n(0)\) and the positive Green **tail** \(T_n\) have different observables. This theorem is a source-specific statement about the positive moment, not about the distribution of \(\{U_n(0)\}\) modulo one. The literal pointed zero and original source are retained throughout.

## GG-06 — A quantitative source → Gamma → discrete-volume bridge (NEW-TO-SUCC BOUND; PROVED PAPER)

Fix positive integer \(m\). **Declare** a conditional observer law with posterior density on the source interval
\[
\mu_m(dx)=\frac{x^mR(x)}{I_m}\,dx,
\quad X_m\sim\mu_m,
\quad Y_m=m(1-X_m).
\]

The density of \(Y_m\), zero outside \([0,m]\), is \(h_m(y)/Z_m\), where
\[
h_m(y)= y\left(1-\frac ym\right)^m\frac{1}{D(y/m)}\mathbf1_{0\le y\le m},\quad Z_m=m^2I_m.
\]

Since \((1-y/m)^m\le e^{-y}\) and \(D\ge1\), **pointwise** \(0\le h_m(y)\le ye^{-y}=h(y)\). The latter density has total mass one, so \(Z_m\le1\). The Gamma2 law decomposes as \(h\,dy=Z_m\operatorname{Law}(Y_m)+(1-Z_m)\rho_m\) for a residual probability measure \(\rho_m\). Hence
\[
\|\operatorname{Law}(Y_m)-\operatorname{Gamma}(2,1)\|_{\rm TV}
\le1-Z_m=1-m^2I_m.
\]

Using the weaker \(I_m\ge B_1-2B_2=(m-1)/[(m+1)(m+2)(m+3)]\), obtain the fully rational source-specific rate
\[
\boxed{\operatorname{TV}(Y_m,\Gamma_2)\le1-m^2I_m
\le\frac{7m^2+11m+6}{(m+1)(m+2)(m+3)}\le\frac7m.}\tag{G12}
\]

For the genuine Oily Green index \(m=8n\), this gives \(\operatorname{TV}\le7/(8n)\). This is stronger than weak convergence and has a **quantified finite-source-to-analytic error bound**. The positive source \(R\) is authentic; the \(x^m\) observation likelihood is the declared earlier WPI model, not a law inferred from actual BBP digits.

Now introduce the **separately declared** Poisson readout \(J_m\mid Y_m=y\sim\operatorname{Poisson}(y)\). Because stochastic channels contract total variation, and the Poisson image of \(\Gamma(2,1)\) is the native Oily \(w^{(2)}\),
\[
\boxed{\operatorname{TV}(\operatorname{Law}(J_m),w^{(2)})\le 7/m.}\tag{G13}
\]

This is an exact *source-positive-to-analytic-to-discrete observer* commuting-limit theorem, with explicit but not physically authenticated choice of both observation channels. It is not a theorem that the original independent Oily geometric waits are the same random variable coupling as this Gamma–Poisson realization.

**Uniform signed log-Mellin phase transport (NEW).** Total variation controls **every bounded complex character**, not just positive moments. For each real \(\omega\), the conditional source-defined variable \(Y_m\) from above satisfies
\[
\boxed{\left|\mathbb E[e^{i\omega\log Y_m}]
 -\frac{\Gamma(2+i\omega)}{\Gamma(2)}\right|\le\frac{14}{m},\qquad \forall\omega\in\mathbb R,\quad m\ge1.}\tag{G13a}
\]
This follows from \(|e^{i\omega\log y}|=1\) for \(y>0\) and the \(2\operatorname{TV}\) dual bound. The estimate is **uniform in the phase frequency** \(\omega\), including frequencies varying with \(m\). For any fixed nonzero \(\omega\), the exact strict attenuation in (G2a) gives a positive signed modulus margin for sufficiently large \(m\). This is a real source-specific *Mellin* spectral estimate; the source law and the declared conditioning are explicit. It still does **not** estimate the selected real-circle Weyl characters \(e^{2\pi i hU_n(0)}\). Producing a legitimate cross-coordinate intertwiner is the next arithmetic gate.

**Hostile nonuniqueness:** For every \(c\ge0\), the different positive source \(R_c(x)=(1-x)(1+c(1-x))\) has the same leading Gamma2 endpoint after scaling, since its boundary coefficient is also one, while its exact moment is \(B_1+c B_2\). Thus the Gamma2 *shape alone* does not authenticate the original four-pole source. These are explicit other sources, **not counterexamples to a theorem whose premises fix the original source**.

## GG-07 — Signed wavefront transport: Gamma can preserve a phase mean, but cannot create its cancellation (PROVED)

For every bounded complex sequence \(f_0,f_1,\ldots\), extend it by zero for negative indices. Define the causal discrete Gamma observer, with integer processing delay \(d\ge0\), by
\[
y_n=\sum_{j\ge0}w_j^{(\alpha)}f_{n-d-j},\quad n\ge0.
\]

For positive integer \(\alpha\) (and indeed any real \(\alpha\ge0\) for the genuine NB law), the weights are nonnegative and sum one with mean \(\alpha\). Interchanging sums and comparing prefix lengths gives
\[
\boxed{\left|\sum_{n=0}^{N-1}y_n-\sum_{n=0}^{N-1}f_n\right|
\le (\alpha+d)\|f\|_\infty.}\tag{G14}
\]

**Proof:** For a fixed lag \(j+d\), the N-term prefix sum of the lagged signal omits at most \(\min(N,j+d)\) terms of the original prefix. Average over the probability kernel and use \(\mathbb E(J+d)=\alpha+d\). This controls **boundary loss**, not the unbounded temporal correlations of the source.

For fixed \(\alpha,d\), or even \(\alpha_N+d_N=o(N)\), the original and filtered **normalized** signed sums differ by \(o(1)\). In particular, if \(f_n=e^{2\pi i hU_n(0)}\) with the authentic zero-seeded BBP rational orbit, then
\[
\boxed{\left|\overline y_N-\frac1N\sum_{n<N}e^{2\pi ihU_n(0)}\right|\le(\alpha_N+d_N)/N.}\tag{G15}
\]

The Gamma-wavefront observer is therefore an *exact transport of the still-open Weyl cancellation target* in this admissible growth regime. It **does not** prove the limit is zero: the constant coherent control \(f_n\equiv1\) survives any fixed-depth normalized filter with mean approaching one.

**Oversmoothing falsifier:** If \(\alpha_N=N^2\), \(d=0\) and \(f_n\equiv1\), then the causal output on the first N indices obeys \(y_n=\Pr(J\le n)\), \(J\sim w^{(N^2)}\). As \(\mathbb E[2^{-J}]=(2-1/2)^{-N^2}=(2/3)^{N^2}\), Markov's inequality on \(2^{-J}\) gives
\[
\boxed{0\le\frac1N\sum_{n<N}y_n\le2^N(2/3)^{N^2}\to0,}
\]

**even though the original source f is maximally noncancelling.** A moving observer-depth limit can erase signs without proving any source arithmetic. This is a decisive control against using Gamma smoothing as an unlicensed normality proof.

The original Oily WEO has **two compulsory ticks** and \(\alpha=2\), so (G14) specializes to signed-sum boundary cost at most \(4\|f\|_\infty\). It is an observer transfer theorem **if** the actual desired phase sequence is lawfully supplied as W input, not a proof that the original source naturally emits these phases to that specific physical filter.

## GG-08 — RH: Gamma is the authentic Archimedean leg, not the Weil sign (CLASSICAL / PROVED FOR Re(s)>1)

The genuine theta heat source is \(\theta(t)=\sum_{n\in\mathbb Z}e^{-\pi n^2t}\). For \(\Re s>1\), termwise positive/Mellin integration, with the zero-mode subtracted, yields
\[
\boxed{
\frac12\int_0^\infty(\theta(t)-1)t^{s/2}\frac{dt}{t}
=\pi^{-s/2}\Gamma(s/2)\zeta(s).}\tag{G16}
\]

Each integer source mode \(n\ge1\) propagates as \(e^{-\pi n^2t}\); the Mellin character \(t^{s/2}\) and source-scale \(\pi n^2\) produce the Gamma factor and integer Dirichlet weight \(n^{-s}\). Theta duality \(\theta(t)=t^{-1/2}\theta(1/t)\) gives the **completed functional equation** after analytic continuation and the appropriate pole terms. The intrinsic critical coordinate arises from this source reflection, not from an arbitrary external gauge pin.

But the raw integral (G16) is not convergent at critical strip points without continuation/subtractions. Evenness/functional equation and the positivity of heat kernels do **not** imply all nontrivial zeros lie on the critical line or that the signed completed Weil quadratic form is nonnegative. The full real Gamma factor, prime powers, conductor/half-density, poles and phases must remain correctly sourced; this note does **not** modify the RH proof gate or use any nontrivial zero ordinate as an input.

**Type separation:** the BBP/Oily Gamma2 endpoint and zeta's Gamma(s/2) local completion share the **Gamma integral mechanism** but have different authentic arithmetic sources. A shared integral kernel is not an authenticated morphism from selected π Weyl phases to the genuine completed zeta Weil form.

## GG-09 — What the analogy buys, and what it cannot prove (STEELMAN / CRUCIBLE)

**Survivors:**

1. The origin \(\delta_0\) and one exponential waiting step generate a continuous Gamma convolution-volume semigroup, uniquely under explicit independence/continuity premises (G3–G4).
2. The Mellin twist pairs the multiplicative character of the source's log-scale with the actual attenuation and constructs Gamma as a normalization (G1–G2).
3. A declared Poisson observer turns the continuous Gamma volume into the exact discrete negative-binomial Oily endpoint family, respecting observer-depth composition (G6–G8).
4. The *actual zero-seeded BBP source* has a Gamma2 boundary profile; explicit rational source bounds sharpen its asymptotics and yield a new source-conditional total-variation rate (G9–G13).
5. The same Gamma mechanism is genuinely the completed zeta's Archimedean factor (G16), but not its signed Weil sign.

**Boundaries/kill controls:**

- A complex analytic continuation of Gamma is not a positive probabilistic volume for \(\Re s\le0\).
- The analytic stage coordinate \(s\), the source carrier clock \(n\), a spatial dimension and the observer's delay are **different parameters**; conflate them only after a proved transport.
- Positive Gamma reconstruction and negative-binomial grade marginals cannot select genuine signed BBP characters or prove π normality (G14 plus coherent control).
- Independent waits, Poisson emission and Bernoulli \(x^m\) updating are additional **model** mechanisms, not automatic properties of original BBP carry sequences.
- The original signed Weil form is not a positive Gamma covariance and requires prime/Archimedean cancellations with source-correct signs.
- The correct pointed seed is the actual \(U_0=0\); replacing it with a mutated seed is not a gauge transformation. A mutant may refute an overbroad seed-blind claim, not the source-selected theorem.

**Next verdict-changing probe:** derive (or refute) a **source-attested joint phase/grade observation law**, indexed by the original four-pole clock and zero seed, whose Gamma/Poisson observer stage retains a *new* signed cross-time lower bound rather than the universal O(1) boundary transfer. Require the same source-labelled signed phase, carry and complete Weyl quantifiers on the input and output. On RH, build the fully completed signed Weil/prime/Gamma intertwiner, not merely the zeta functional equation. Test new conjectures on original-source histories and *premise-matched* controls without silently changing the source passport.

## Provenance / prior literature

- SUCC [PR #344 Wavefront Oscillator](https://github.com/femboy2112/SUCC/pull/344): exact two-stage Oily grade and delayed inverse; original BBP chiral source.
- SUCC [PR #345 Source-prior Wavefront](https://github.com/femboy2112/SUCC/pull/345): original \(R\), conditional posterior and Gamma2 endpoint; iid sensing is declared.
- SUCC [PR #346 Prior Field / Inflation](https://github.com/femboy2112/SUCC/pull/346): finite branching, declared channels and original-source anti-ensemble firewall.
- SUCC [PR #628 Predictive-span Source Observer](https://github.com/femboy2112/SUCC/pull/628): predictive algebra fixed points and source-law calibration.
- SUCC [PR #632 Pointed Zero Rigidity](https://github.com/femboy2112/SUCC/pull/632): immutable origin and source endomorphism meaning.
- [NIST DLMF 5.2](https://dlmf.nist.gov/5.2), [5.5](https://dlmf.nist.gov/5.5), [5.9](https://dlmf.nist.gov/5.9): Euler integrals, functional equation, log convexity, rate changes.
- [McGill number theory notes on Mellin theta and zeta](https://www.math.mcgill.ca/darmon/courses/11-12/nt/notes/lecture2.pdf); [DLMF theta integrals](https://dlmf.nist.gov/20.10).

No independent academic review or priority claim is made for the classical content. Exact finite checks and SymPy/mpmath oracles are not a new Lean formal proof or an authentic physical experiment.
