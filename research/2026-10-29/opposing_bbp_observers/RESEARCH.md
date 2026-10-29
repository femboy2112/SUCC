# SUCC — Two opposing BBP observers: source-relative semantic disagreement and the Oily gap

**Research-only, October 29, 2026.** Exact parent SUCC [draft #379](https://github.com/femboy2112/SUCC/pull/379) at `171c445e6dd8aa32a60d653263924b9f3b0e800e`; this branch must remain unmerged and the original four-pole BBP forcing and seed `U_0=0` must remain byte-identical. Prior sources: #367 source convolution and source variance, #368/#370 Oily/Pascal, #372 totient-selected Pascal–Gamma conditional ranks, #373 inertial zero boundary, #379 Kepler normal form. No physical/cognitive equivalence, academic priority, π-normality, or RH claim is made.

## Steelman: two distinct meanings of the author's observer proposal

The author asks for two observers independent except for a common base carrier, realizing the BBP system in opposing information directions and comparing their disagreement. There are two different mathematical mechanisms: (A) **independent microstate draws with opposing beliefs** from the same authenticated positive BBP source; (B) **independent evidence updates to one shared latent microstate**, for which source-relative likelihoods can cancel. They are not interchangeable. Neither model is automatically a sampler of π digits. There is also an exact deterministic forward-prefix/backward-tail split of the selected BBP recurrence, treated separately below.

## Original four-pole passport

For `a>0`, let

\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)},
\]
\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0,\qquad
\mu_a(dx)=\frac{e^{-ax}Q(x)}{R(a)}dx.
\]

Original arithmetic time is `a_n=8n-7`, `r(n)=R(a_n)`, `U_0=0`, `U_n=16 U_(n-1)+r(n)`. The scalar source uses the *same* `Q`, not positive replacement coefficients. Put `F(a)=log R(a)`, so `F''(a)=Var_mu_a(X)>0`.

## Theorem 1 — exact opposition, shared semantic barycenter

Fix `0<=t<a`. Define positive and negative observer laws

\[
\mu_+=\mu_{a+t},\qquad\mu_-=\mu_{a-t}.
\]

Their likelihood ratios relative to their shared base are `L_+(x)=e^{-tx}R(a)/R(a+t)` and `L_-(x)=e^{tx}R(a)/R(a-t)`. The pointwise product `L_+L_-` is constant:

\[
L_+(x)L_-(x)=\frac{R(a)^2}{R(a+t)R(a-t)}=H_a(t)^2,
\]
\[
\boxed{H_a(t)=\int\sqrt{d\mu_+d\mu_-}=\frac{R(a)}{\sqrt{R(a+t)R(a-t)}}.}
\]

Thus the normalized geometric mean of the two observer laws is **exactly the original carrier** `mu_a`. If we instead interpret the likelihoods as two conditionally independent pieces of evidence on a **single** unknown `X`, pooling their likelihood factors restores `mu_a` exactly. This does not mean two independent posteriors have the same sampled realization. The even disagreement cost is the Bhattacharyya/Jensen gap

\[
J_a(t)=-\log H_a(t)=\tfrac12[F(a+t)+F(a-t)]-F(a)>0\quad(t>0).
\]

The source's exact variance bounds from #367 imply, for `rho=t/a` and `0<t<a`,

\[
\boxed{1-\rho^2<H_a(t)<\sqrt{(1-\rho^2)\left(1-\frac{t^2}{(a+5)^2}\right)}.}
\]

Proof: integrate strict `1/u²+1/(u+5)²<F''(u)<2/u²` over the centered second-difference triangular kernel on `[a-t,a+t]`. All steps retain positive `u` because `t<a`.

## Theorem 2 — the exact two-observer disagreement density

For independent `X_+~mu_+`, `X_-~mu_-`, let `Delta=X_+-X_-`. Define `c_0=4,c_3=-2,c_4=c_5=-1` and

\[
G_a(z)=e^{-az}\int_0^\infty e^{-2ay}Q(y+z)Q(y)dy
=\sum_{j\in\{0,3,4,5\}}c_jR(2a+j)e^{-(a+j)z}>0.
\]

The exact all-real, all-parameter probability density is

\[
\boxed{p_{a,t}(d)=\frac{e^{-td}G_a(|d|)}{R(a+t)R(a-t)}.}
\]

Proof: for `d>=0` substitute `X_-=y`, `X_+=y+d` in the product density; for negative `d`, exchange `+` and `-`. This directly gives the positive integral above. The four-pole formula follows by expanding only `Q(y+d)` and integrating `Q(y)`. Thus for `d>0`,

\[
\boxed{\frac{p_{a,t}(d)}{p_{a,t}(-d)}=e^{-2td}.}
\]

This is the precise **semantic direction versus carrier shape** decomposition: the odd log-density component `-td` depends on observer orientation and the even component `log G_a(|d|)` on the authenticated base source. It is an exact instance of classical exponential tilting, not a new generic probability phenomenon. At `t=0` the disagreement density is symmetric.

The full mgf is

\[
E e^{s\Delta}=\frac{R(a+t-s)R(a-t+s)}{R(a+t)R(a-t)},
\quad -(a-t)<s<a+t.
\]

All moments exist and are obtained by differentiating this rational transform. In particular `E Delta = -F'(a+t)+F'(a-t)<0`, and the KL divergence between the opposite *joint-orientation* laws equals

\[
D(P_t\Vert P_{-t})=-2t E_t\Delta
=2t[F'(a+t)-F'(a-t)]>0.
\]

## Theorem 3 — Gamma-difference limit and golden calibration

Let `t=rho*a`, `0<=rho<1`, and use the common carrier scale `Z_a=a Delta`. The authentic `Q(x)=15x-59x²/2+O(x³)` implies that `a X_+` and `a X_-` converge independently to Gamma(shape 2, rates `1+rho` and `1-rho`). Hence `Z_a` has the limiting bilateral Gamma density

\[
\boxed{g_\rho(z)=\frac{(1-\rho^2)^2}{4}(1+|z|)e^{-|z|-\rho z},\quad z\in\mathbb R.}
\]

This is a known gamma-difference family (Forrester 2024; Küchler and Tappe 2008), specialized to the authentic source endpoint. It has `g_rho(z)/g_rho(-z)=e^(-2rho*z)` and

\[
E Z=-\frac{4\rho}{1-\rho^2},\qquad
H_a(\rho a)\longrightarrow1-\rho^2,
\qquad J_a(\rho a)\longrightarrow-\log(1-\rho^2).
\]

**Optional golden choice, declared rather than forced:** the two-stage Oily packet fixed point selects `lambda=(sqrt5-1)/2` and `lambda²=1-lambda`. Setting `rho=lambda` gives

\[
\boxed{E Z=-4,\quad P(Z>0)=\lambda^2/4,\quad H_\infty=\lambda,\quad J_\infty=\log\varphi.}
\]

The exact finite-source overlap obeys `lambda<H_a(lambda*a)<sqrt(lambda*(1-(lambda*a/(a+5))²))`; source expansion gives

\[
J_a(\lambda a)=\log\varphi-\frac{59\lambda}{15a}+O(a^{-2}).
\]

The integer `-4` is a consequence of the chosen rank-two Gamma comparison and golden equation. Its square matching base 16 is **not** a derivation of the BBP base or a digit-frequency proof. A Gamma-matched fake positive kernel `Q_fake(x)=15x` gives the same limiting golden values but not the authentic `59` correction.

### Opposing Pascal grade observers

Keep the actual declared BBP–Pascal sensor from #370: for each observer source `c=a(1±rho)` at native time `a=8n-7`, sample `X~mu_c` and then `J|X~Binomial(n,1-e^(-8X))`. At each finite n,

\[
q_{n,c}(j)=\frac{\binom nj}{R(c)}\sum_{k=0}^j(-1)^k\binom jk R(c+8(n-j+k)).
\]

The exact mean is `n[1-R(c+8)/R(c)]`. Its probability generating function converges to

\[
G_\kappa(z)=\left[\frac{\kappa}{\kappa+1-z}\right]^2,\quad\kappa=1\pm\rho,
\]

and `E J_+ - E J_- -> 2/(1+rho)-2/(1-rho)`. At the declared golden `rho=lambda`, **the mean grade disagreement also tends to -4**. This is a consequence of the authentic source's asymptotic Gamma endpoint and the chosen clock-matched sensor; neither digit sampling nor the finite n=-4 equality is claimed.

## Theorem 4 — Oily-Macaroni is the shared finite part; the disagreement gap eliminates gamma

At the neutral midpoint `t=0`, draw `X,Y` independently from the original `mu_a`, and put `V_a=a|X-Y|`. Use the **same golden Laplace readout** on a single carrier and on the absolute inter-observer disagreement:

\[
S_a=E_{\mu_a}[\log(aX)-e^{-\lambda aX}],\quad
W_a=E[\log V_a-e^{-\lambda V_a}].
\]

The authentic source provides exact finite formulas. Write `B_j(a)=log(1+j/a)/(a+j)` and let the sums range over `j=0,3,4,5`. Then

\[
\boxed{S_a=-\gamma-\frac{\sum_jc_jB_j(a)}{R(a)}-\frac{R(a(1+\lambda))}{R(a)}},
\]
\[
\boxed{W_a=-\gamma-\frac{2}{R(a)^2}\sum_jc_jR(2a+j)
\left[B_j(a)+\frac1{a(1+\lambda)+j}\right].}
\]

Proof: integrate each (possibly signed) elementary exponential in the **total positive** source density, using

\[
\int_0^\infty e^{-pz}\log(az)dz=\frac{\log(a/p)-\gamma}{p};
\]

for the pair, use Theorem 2 at `t=0`. Normalization gives the `-gamma` coefficient *exactly one* in both observables. Therefore, for **every finite a>0**, `S_a-W_a` has **no uncanceled Euler–Mascheroni term**. It is not just asymptotic cancellation.

As `a->infty`, `aX~Gamma(2,1)` and `V_a` has density `(1+v)e^(-v)/2` on `v>0`. Hence

\[
\begin{aligned}
\lim S_a&=1-\gamma-\lambda^2=\lambda-\gamma=\Omega_{OM},\\
\lim W_a&=\tfrac12-\gamma-\tfrac12=-\gamma,\\
\boxed{\lim(S_a-W_a)&=\lambda.}
\end{aligned}
\]

The pair's `E log V=1/2-gamma`, while `E exp(-lambda V)=[lambda+lambda²]/2=1/2`.

**Original-source first corrections (paper derivation, independently checked numerically):** let `c=59/30` from `Q''(0)=-59`. Since the scaled one-body density is `y e^-y[1-(c/a)(y-2)+O(a^-2)]`, a two-body observable incurs `-(c/a) Cov(g(|Y_1-Y_2|),Y_1+Y_2)`. For `g(v)=log v-e^-lambda*v` and two independent Gamma(2,1) variables,

\[
\operatorname{Cov}(\log|Y_1-Y_2|,Y_1+Y_2)=1,
\quad \operatorname{Cov}(e^{-\lambda|Y_1-Y_2|},Y_1+Y_2)=\lambda^3-\frac12.
\]

The latter follow by integrating the conditional first moment `E[Y_1+Y_2||Y_1-Y_2|=v]=(v²+3v+3)/(v+1)` against the exact bilateral Gamma density. Polynomial/exponential domination controls the `O(a^-2)` remainder despite the integrable logarithmic diagonal. Therefore

\[
\boxed{S_a=\lambda-\gamma-\frac{59}{30a}(1+2\lambda^4)+O(a^{-2})},
\]
\[
\boxed{W_a=-\gamma-\frac{59}{30a}\left(\frac32-\lambda^3\right)+O(a^{-2})},
\]
\[
\boxed{S_a-W_a=\lambda+\frac{59}{30a}\left(4\lambda-\frac52\right)+O(a^{-2})}.
\]

This is an **authentic original-source correction** beyond the generic Gamma law. The common `-gamma` is a reference finite part, not a signed π-normality mechanism; the residual gap is a measurable change of observation. The 59 is source-specific, the λ calibration is declared by the older two-stage source, and the selected BBP phase is not identified with either stochastic sample.

## Theorem 5 — actual selected-phase witness and the no-go

For `n>=1`, original exact rational states `U_(n+j)(s)` and integer nonzero `h`, form

\[
\Theta_{n,\pm}(h;s)=\sum_{j=0}^{n}q_{n,a_n\pm t}(j)e^{2\pi i h U_{n+j}(s)},
\quad D_{n,h}(s)=\Theta_{n,+}(h;s)-\Theta_{n,-}(h;s).
\]

These are **finite genuine BBP-phase-tied** readouts, not independent random digit generation. Weights are rational for rational `a_n,t`. They preserve the entire authentic recurrence, initial seed and exact integer-frequency phase. For `n=1,t=1/3`, `q_{+,0}-q_{-,0}=835944211343/29626769851315` and the genuine source has phase residues `U_1 mod1=2/15`, `U_2 mod1=1076/4095`, so the contrast is not identically zero.

The **exact infinitesimal opposition score** is stronger than merely a
new probability representation. Let `M_n(x;h,s)=E[e(hU_(n+J)(s))|X=x]`, with the
same source-authenticated conditional Pascal law. Differentiating the
exponential-family carrier at the neutral midpoint gives

\[
\boxed{\left.\frac{d}{dt}(\Theta_{n,+}-\Theta_{n,-})\right|_{t=0}
= -2\operatorname{Cov}_{\mu_{a_n}}(X,M_n(X;h,s))
=2\sum_{j=0}^n q'_{n,a_n}(j)e(hU_{n+j}(s)).}
\]

The finite weights `q'` are exact rationals, and `sum_j q'=0`. This is a
source-connected **signed** covariance with genuine selected-phase labels,
but covariance existence or finite nonzero value gives no uniform time bound.
The exact derivative instrument and no-go are tested independently. 

But `sum_j(q_{n,+}(j)-q_{n,-}(j))=0`, and the contrast vanishes **identically for every constant phase sequence**. A theorem merely bounding the opposition contrast cannot imply π normality. Integer seed offsets have identical phase readouts, as in #373; the same-source coherent counterseed `s=-pi/16` has `e(hU_k(s))->1`, so its opposing contrast tends to zero too. An actual original-zero-seed signed estimate still has to control a common-mode observable.

## Forward time vs reverse time: exact BBP prefix/tail disagreement

This is a distinct deterministic pair. Put `p_n=16^-n U_n(0)` (known-prefix accumulator) and `t_n=16^-n T_n` (future-tail accumulator), where `T_n=sum_(j>=1)16^-j r(n+j)` as in #379. Then

\[
\boxed{p_n+t_n=\pi/16,\quad
p_{n+1}-p_n=16^{-(n+1)}r(n+1)=-(t_{n+1}-t_n).}
\]

These increments are perfectly anticorrelated (indeed deterministically opposite) once the shared forcing is fixed. They are NOT two uncorrelated actual histories; their boundary data and information directions are complementary. The bare orbit disagreement between zero and advanced seed is `U_n(0)-U_n(-pi/16)=16^(n-1)pi`, exactly the original still-open Weyl orbit.

## Verdict and next falsifier

**PROVED LOCAL, source-conditional:** exact density, odd/even orientation factor, midpoint information geometry, source-dependent all-a overlap bounds, Gamma/golden limit, exact finite Oily constants and gamma cancellation, and finite original phase-tied observer readout. **CLASSICAL ingredients:** exponential tilting, Gamma differences, KL/Hellinger identities, harmonic/digamma and Gamma–Poisson mixing. **INTERPRETATION:** calling the odd log term *semantic* records an observer-frame distinction; it is not evidence of human cognition or physical gauge forces. **OPEN:** a unique physical observation rule and any original-zero-seed `o(N)` signed Fourier bound for π normality or RH.

The first actual breakthrough target is a source-authenticated conditional signed carry **common-mode** inequality that distinguishes selected `U_0=0` from the same-forcing counterseed, survives mutant `Q=15x`, wrong-pole clocks and wrong Pascal/Gamma joints, and yields a sublinear Weyl sum rather than a trivially vanishing difference of normalized observers. Keep full residue/carry history; early primitive/cototient projection loses state (q=6 witness in #372/#379).

## Execution and provenance

`python test_opposing_observers.py` exercises 10 exact standard-library tests, including literal BBP phase aliases and 20-step exact opposing Pascal likelihoods. `python independent_oracle.py` independently rederives all moment identities in SymPy without importing the production code. `python numerical_oracle.py` independently compares the real Laplace integral, finite Oily closed forms, asymptotic coefficients, and 105-digit direct discrepancy integral. Results and limitations are in `VALIDATION.md` and `numerical_receipt.json`. This is **isolated research-package validation**; no native SUCC full-suite/Lean/hosted exact-head pass is claimed for this new child until actually observed.

External classical context: Peter J. Forrester, *On the gamma difference distribution*, Statistics & Probability Letters 211 (2024), DOI 10.1016/j.spl.2024.110136; Uwe Küchler & Stefan Tappe, *On the shapes of bilateral Gamma densities*, Statistics & Probability Letters 78 (2008), DOI 10.1016/j.spl.2008.02.039; [NIST DLMF Gamma](https://dlmf.nist.gov/5.2) and [digamma](https://dlmf.nist.gov/5.4); BBP source Bailey–Borwein–Plouffe 1997 original http://www.davidhbailey.com/dhbpapers/digits.pdf. Mathematical novelty beyond SUCC's new-to-program specializations has not been established.
