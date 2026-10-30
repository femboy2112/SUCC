# Operation MAX / ROOT — exact observer-conditioned Pólya transport in SUCC

**2026-10-28; research-only child of draft PR #356, pinned to b89fac9aff8bc0ef20dc0f1beda0020d0141701f.** All results below concern the original OLZF-04 / PCR-02 prime-power source probability model. RH, pi normality, empirical human preference, and physical Maxwell-demon work remain **OPEN / UNVERIFIED**. No zero location is used as input. Literature priority is unverified.

## 1. Source and random-variable typing

For a genuine prime p, exponent j >= 0, and path coordinate k=0,...,j, SUCC's uniform marked vector on H_(p^j) has source coordinate law u_j(k)=1/(j+1). Its native Pólya transition is

\[
P_j(k,k+1)=(k+1)/(j+2),\qquad P_j(k,k)=(j+1-k)/(j+2).
\]

The equivalent de Finetti representation samples U uniformly on [0,1], then samples conditional Bernoulli(U) increments; K_j counts successes. Thus K_j/j approaches U almost surely. This is the classical two-color Pólya process, not a zeta-zero eigenstate.

For independent U_1,...,U_m uniform on [0,1], m an integer >= 1, their maximum has CDF x^m. The transformed variable U^(1/m) has the **same distribution**, Beta(m,1), with density m u^(m-1). Neither pathwise equality nor equality of joint laws follows. m is an *observer sample count*, not the arithmetic prime 2 or a physical charge.

## 2. Exact source-preserving observer construction (OST-01 and OST-02)

Retain the original latent U, introduce m-1 independent ancillary uniforms V_2,...,V_m and record the single global event A_m that U exceeds every V. Then

\[
P(A_m\mid U=u)=u^{m-1},\quad P(A_m)=1/m,\quad U\mid A_m\sim\mathrm{Beta}(m,1).
\]

The unconditional arithmetic source remains Uniform[0,1]; conditioning selects a different observer law. Given K_j=k in the original source, Bayes gives U|K_j=k ~ Beta(k+1,j-k+1). With the rising factorial (a)_r=a(a+1)...(a+r-1),

\[
w_j^{(m)}(k):=P(A_m\mid K_j=k)
=\frac{(k+1)_{m-1}}{(j+2)_{m-1}}.
\]

Consequently the exact selected grade marginal and likelihood ratio are

\[
q_j^{(m)}(k)=\frac{m(k+1)_{m-1}}{(j+1)_m},\qquad
h_j^{(m)}(k)=\frac{q_j^{(m)}(k)}{u_j(k)}
=\frac{m(k+1)_{m-1}}{(j+2)_{m-1}}.
\]

The first is BetaBinomial(j;m,1). Importantly 0 < h_j <= m uniformly in both j and k; its expectation under P is 1. The native conditional-mean identity gives the exact positive martingale

\[
P_j(k,k)\,h_{j+1}(k)+P_j(k,k+1)\,h_{j+1}(k+1)=h_j(k).
\]

The Doob transform of the *original* transition is therefore

\[
P_j^{(m)}(k,k+1)=P_j(k,k+1)\frac{h_{j+1}(k+1)}{h_j(k)}
=\frac{k+m}{j+m+1},
\]
\[
P_j^{(m)}(k,k)=\frac{j+1-k}{j+m+1}.
\]

The identity holds at every finite grade, and on every full binary prefix \omega of depth j,

\[
Q_m(\omega)/P(\omega)=h_j(K_j(\omega)).
\]

Hence the observer-selected infinite-history law Q_m has dQ_m/dP=m U^(m-1), which is positive P-almost surely and bounded by m. **Q_m and P are mutually absolutely continuous, not singular.** The global selection event has probability 1/m independent of history depth.

## 3. Full source reconstruction and its coherent boundary (OST-03)

For m=2, select the event A={U>=V}; the rejected complement is equally likely. Their exact finite marginals are

\[
q_j^+(k)=\frac{2(k+1)}{(j+1)(j+2)},\quad
q_j^-(k)=\frac{2(j+1-k)}{(j+1)(j+2)}.
\]

For all k and j, the original source is recovered *probabilistically*:

\[
\frac12 q_j^+(k)+\frac12 q_j^-(k)=\frac1{j+1}.
\]

Likewise the weighted sum of both Fourier characters equals the unconditioned source character at each grade. This is **not** automatic preservation of the *pure* marked vector after discarding observer information.

Indeed, with w_j(k)=(k+1)/(j+2), the tagged map

\[
W_j|k\rangle=\sqrt{w_j(k)}\,|k,+\rangle+
\sqrt{1-w_j(k)}\,|k,-\rangle
\]

is an isometry (the observer record can be retained coherently). But tracing out its tag multiplies the off-diagonal k,l coherence by
\(\sqrt{w_k w_l}+\sqrt{(1-w_k)(1-w_l)}\), less than 1 when the two weights differ. At grade j=1 that factor is 2 sqrt(2)/3. The source *classical marginal* survives; the discarded-tag quantum-style density matrix generally changes.

## 4. Bounded information and persistent source overlap (OST-04)

Because every full-prefix likelihood h_j <= m,

\[
D_{\rm KL}(Q_m^{(0:j)}\Vert P^{(0:j)})\le\log m.
\]

On the infinite history space, U has Beta(m,1) density under Q_m and uniform density under P. Direct integration gives finite distances in natural units:

\[
D_{\rm KL}(Q_m\Vert P)=\log m-1+1/m,\qquad
D_{\rm KL}(P\Vert Q_m)=m-1-\log m.
\]

For m=2 these are log 2 -1/2 ~=0.193147 and 1-log 2 ~=0.306853. There is no growing selection-event rarity or forced physical work per grade.

For the canonical positive-amplitude source and selected vectors, the squared Hellinger overlap is

\[
F_j^{(m)}=\Big(\sum_{k=0}^j\sqrt{u_j(k)q_j^{(m)}(k)}\Big)^2.
\]

Riemann-sum convergence and the Beta density imply

\[
\lim_{j\to\infty}F_j^{(m)}
=\left(\int_0^1\sqrt{m u^{m-1}}\,du\right)^2
=\frac{4m}{(m+1)^2}.
\]

For m=2 this equals **8/9**, unlike the fixed geometric a^k selection of PR #355/#354, whose overlap tends to zero. These are source-relative mathematical overlaps, not physical measurement statistics.

## 5. A decisive off-unit-circle root control (OST-05)

For m=2 let L=log p, and z be SUCC's *local phase-character parameter*, not the argument of zeta(s). The selected local character equals

\[
\chi_j^+(z)=\frac{2e^{-ijzL}}{(j+1)(j+2)}
P_j(e^{2izL}),\qquad P_j(w)=\sum_{k=0}^j (k+1)w^k.
\]

**Exact polynomial theorem:** every root of P_j for j>=1 has modulus <1. Proof: define the reverse polynomial
\(R_j(v)=v^jP_j(1/v)=\sum_{k=0}^j(j+1-k)v^k\).
Then

\[
(1-v)R_j(v)=(j+1)-\sum_{k=1}^{j+1}v^k.
\]

If |v|<1, the sum has modulus strictly <j+1; if |v|=1, equality to j+1 requires v=1, where R_j(1)=(j+1)(j+2)/2>0. Thus R_j has no zeros on |v|<=1, so P_j has no roots on |w|>=1.

Since |exp(2izL)|=exp(-2L Im z), every selected-character root has Im z>0. The rejected polynomial is reciprocal, giving Im z<0, while the **unselected** uniform source polynomial has its nontrivial roots exactly on |w|=1 (real phase axis). Their weighted characters nonetheless reconstruct the original source identically.

At j=1, P_1(w)=1+2w, so its zero w=-1/2 yields
\[
z=\frac{(2n+1)\pi}{2\log p}
+i\frac{\log 2}{2\log p}.
\]

This is a **source-compatible off-real local-character zero** with a bounded full-history likelihood ratio and finite KL. It refutes the generic shortcut

> off-axis local Fourier zero => singular virtual-history law => energetic Maxwell demon.

It does not refute RH: these characters are **not** the completed zeta function or a proven spectral encoding of its nontrivial zeros. Any RH argument must discriminate this source-legal control from the authentic completed Weil pairing, rather than assuming the false shortcut.

## 6. Selection and coarse observation do not commute (OST-06)

The max/root identity applies at the **latent continuous** level. Taking a maximum of m already-discretized uniform grade observations is not equivalent to changing the latent prior and then sampling the grade.

At j=1 and m=2,

\[
P(\max(K_1^{(1)},K_1^{(2)})=1)=3/4
\quad\ne\quad
P(K_1=1\mid A_2)=2/3.
\]

In general the discrete-maximum mass is
\(((k+1)^m-k^m)/(j+1)^m\), not BetaBinomial(j;m,1).
A deterministic map U -> U^(1/m) also has the same one-point law but does not automatically preserve its coupling to the original source or its history. This is the precise order-of-operations defect.

## 7. Verdict and proof debt

**PAPER-PROVED in the stated probability model:** a complete all-grade observer-selected urn family, bounded Doob transport, source restoration after retaining the outcome tag, finite full-history KL, positive asymptotic amplitude overlap, and selected/rejected off-axis local-character roots.

**CLASSICAL:** order statistics, beta-binomial/Pólya, Bayesian conditioning, Doob transforms, entropy, polynomial manipulations.

**REFUTED SHORTCUT:** generic off-axis local character zeros must be produced by singular infinite-history selection. The countermodel is genuine SUCC Pólya source probability with an observer tag.

**UNVERIFIED:** any transport from these local phase characters to actual nontrivial zeros of completed zeta; a source-authenticated positive Weil pairing; actual human N-first observer preferences; physical energy cost; any arithmetic prime-2 significance of sample count 2. RH and pi normality remain OPEN.

The next decisive probe must reconstruct genuine prime-power coefficients, gamma/pole, operator/test-function domains, all-prime charge labels, and a new positive spectral invariant rejecting the source-compatible observer controls, fake primitive 4, non-Pisot clocks, 11/29 Pisot collision, and positive-Fourier off-line functions. No zeta-zero locations may be inserted as data. All current source/ancestor folders remain untouched.

**Evidence:** 13 local exact/unit tests, 1323 separate SymPy symbolic checks, six false-model controls, plus the displayed analytic proofs; one reasoner, no blind peer-review or Lean proof. Sources and limitations are catalogued separately.
