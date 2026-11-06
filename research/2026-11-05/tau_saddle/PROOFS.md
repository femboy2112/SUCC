# TAU SADDLE: optimal truncation of the authentic radial BBP observer

**Research-only paper mathematics, 2026-11-05.** Strict additive child of PR #508 pinned at commit 61cdf240d0c2e75afe934dde6c98ce71a783a832; parent #507 derives the positive source-jet coefficients and original/radial Mellin identities. This continuation investigates the **observer-order/source-time dynamics** of that exact reconstruction, not π-digit normality. Discovery preceded preregistration and is labelled developmental; held-out rational checks were specified before being run. No independent academic referee or global priority is claimed.

## Source contract and fourfold crossing

Let \(E f(n)=f(n+1)\), \(e(x)=\exp(2\pi i x)\), and let the ORIGINAL four-pole forcing \(r_o\) and the genuine zero-seeded radial state \(Z_n\) be exactly as in PRs #499, #504 and #507. The radial taps are

\[
w_r=(2,-2,-1,-2,-1/2,-1/2,1/4,0),\quad
P_r(t)=\sum_{j=1}^8 w_{r,j}t^{j-1},\quad
\rho(t)=-\frac{P_r(t)}{16-t^8}.
\]

For integers \(n\ge1,k\ge0\), the source-derived radial moment is

\[
I_k(n)=(1-E)^kZ_n=\int_0^1 t^{8n}\rho(t)(1-t^8)^k\,dt. \tag{TS1}
\]

The unique interior radial zero is

\[
\tau=2-\sqrt2,\qquad
u_0=\tau^8=9232-6528\sqrt2,\qquad
\sigma=1-u_0.
\]

Exactly at \(\tau\): (i) \(K_{\rm rad}(\tau)=0\); (ii) the signed potential \(G(t)=2\log((2-t^2)/(t^2-2t+2))\) has maximum \(G(\tau)=\log2\); (iii) the Gaussian angular coordinate is \(\theta_0(\tau)=\pi/8\); (iv) the generating function for the **unique** canonical radial source-jet coefficients has its nearest real singularity at \(s=\sigma\). These are related algebraic features, not evidence for a physical quantum field.

The rational source densities have the strict signs

\[
\rho(t)<0\ (0<t<\tau),\quad
\rho(\tau)=0,\quad
\rho(t)>0\ (\tau<t\le1),\qquad \rho(1)=1/4.
\]

In particular \(I_0(n)=Z_n>0\), with literal zero initial condition.

## TS-01: one and only one signed observer-order transition, for EVERY n

For fixed integer n, extend \(I_k(n)\) to real \(k\ge0\) through the integral (TS1). Decompose

\[
I_k(n)=B_k(n)-A_k(n)
\]
where
\[
A_k=\int_0^\tau t^{8n}|\rho(t)|(1-t^8)^kdt>0,\quad
B_k=\int_\tau^1 t^{8n}\rho(t)(1-t^8)^kdt>0.
\]

On the negative side \(s(t)=1-t^8>\sigma\); on the positive side \(s(t)<\sigma\). For every real \(k\ge0\) and every fixed \(\delta>0\),

\[
A_{k+\delta}/A_k>\sigma^\delta>B_{k+\delta}/B_k.
\]

Therefore \(A_k/B_k\) is STRICTLY INCREASING in k. Because a compact subinterval of \((0,\tau)\) has \(s>\sigma+\eta\), while the entire positive side has \(s<\sigma\), we have \(A_k/B_k\to\infty\) as \(k\to\infty\). Since \(I_0(n)=Z_n>0\), there is exactly one real \(k_c(n)>0\) with

\[
\boxed{I_k(n)>0\ (k<k_c),\quad I_{k_c}(n)=0,\quad I_k(n)<0\ (k>k_c).} \tag{TS2}
\]

Codex #507 already established EVERY canonical coefficient \(b_k>0\) and
\(P_m(E)=-\sum_{k=1}^m b_k(1-E)^k\). For \(\varepsilon_m(n)=r_o(n)+P_m(E)Z_n\), define \(\varepsilon_0=r_o(n)\). Then

\[
\boxed{\varepsilon_m(n)-\varepsilon_{m-1}(n)=-b_m I_m(n).} \tag{TS3}
\]

Hence residuals STRICTLY DECREASE for integers \(m<k_c\), STRICTLY INCREASE for \(m>k_c\), with at most one zero-increment/adjacent minimum when \(k_c\) is an integer. There is a unique optimal integer truncation except for this possible adjacent tie. This is an **all-source-times** statement; it does not infer a Weyl orbit distribution.

## TS-02: exact algebraic critical ratio and first-order refinement

Put \(\widetilde\rho(u)=\rho(u^{1/8})\), \(a_0=1/8\), and
\(U_{n,k}\sim\mathrm{Beta}(n+a_0,k+1)\), a mathematically auxiliary beta distribution, NOT π digit sampling. The change \(u=t^8\) in (TS1) gives

\[
I_k(n)=\frac18 \mathrm B(n+1/8,k+1)\,
        \mathbb E[\widetilde\rho(U_{n,k})].             \tag{TS4}
\]

If \(k/n\to\alpha\in(0,\infty)\), beta concentration gives \(U_{n,k}\to(1+\alpha)^{-1}\) in probability. Since \(\widetilde\rho\) changes sign only at \(u_0=\tau^8\), the sign of \(I_k(n)\) eventually agrees with \(\mathrm{sign}((1+\alpha)^{-1}-u_0)\) when \(\alpha\ne \alpha_*\). Together with TS-01 this proves

\[
\boxed{\frac{k_c(n)}n\to\alpha_*:=\frac{1-u_0}{u_0}
      =\tau^{-8}-1
      =\frac{561}{16}+\frac{51\sqrt2}{2}
      \approx71.12494584051392.} \tag{TS5}
\]

A sharper analysis expands the beta mean and variance uniformly for \(k=\alpha_*n+c\), bounded c:

\[
\begin{aligned}
\mathbb E(U_{n,k}-u_0)
 &=\frac{u_0^2}{n}\left(\frac{\alpha_*}{8}-c-1\right)+O(n^{-2}),\\
\operatorname{Var}(U_{n,k})
 &=\frac{u_0^2\sigma}{n}+O(n^{-2}).
\end{aligned}
\]

The third *central signed* moment and Taylor remainder are \(O(n^{-2})\) for smooth \(\widetilde\rho\), with its density evaluated away from \(u=0\) at exponentially small beta-tail cost. Therefore

\[
\mathbb E[\widetilde\rho(U_{n,k})]
 =\frac{u_0^2\widetilde\rho'(u_0)}n
 \left[\frac{\alpha_*}{8}-c-1+
       \frac{\sigma\widetilde\rho''(u_0)}{2\widetilde\rho'(u_0)}\right]
 +O(n^{-2}).
\]

The derivative \(\widetilde\rho'(u_0)>0\). Applying the monotonic one-crossing theorem and the implicit zero with a uniform \(O(n^{-2})\) expansion yields

\[
\boxed{k_c(n)=\alpha_*n+c_*+O(n^{-1}),\quad
c_*=\frac{\alpha_*}{8}-1+
    \frac{\sigma}{2}
       \frac{\widetilde\rho''(u_0)}{\widetilde\rho'(u_0)}
    \approx-17.7026236019995.}                       \tag{TS6}
\]

For the integer minimizer, take the integer just below the real crossing (or one of two tied choices if it is integral). In particular \(m_{\rm opt}(n)=\alpha_*n+O(1)\).

## TS-03: sharper exponential optimal residual — an interior saddle

#507 proves the meromorphic decomposition

\[
\mathcal A(1-s)=\frac{K}{\sigma-s}+R(s),\quad
K=8(16-u_0)>0,
\]
where \(R(s)\) is analytic on \(|s|<1\) and the original radial jet polynomial is \(S_m(s)=\sum_{j=1}^m b_j s^j\). Subtracting its Taylor polynomial gives the EXACT pole remainder

\[
\frac{K}{\sigma-s}
-\sum_{j=0}^m\frac{K}{\sigma^{j+1}}s^j
=\frac{K\sigma^{-m-1}s^{m+1}}{\sigma-s}.
\]

Set \(g(u)=\widetilde\rho(u)/(u-u_0)\). It extends continuously and positively across the radial zero, with \(g(u_0)=\widetilde\rho'(u_0)>0\). The pole part of the authentic \(\varepsilon_m(n)\) therefore is

\[
\boxed{
E_m^{\rm pole}(n)=
\frac{K\sigma^{-m-1}}8
\int_0^1u^{n-7/8}(1-u)^{m+1}g(u)\,du>0.} \tag{TS7}
\]

The analytic R remainder is negligible compared with TS7 when \(m=\alpha_*n+O(1)\). **Explicit error route:** split at \(t=1/2\). On \(t\ge1/2\) choose Cauchy radius \(R_0=511/512\) larger than \(\sigma\) and \(1-(1/2)^8=255/256\); the regular Taylor remainder is \(O(R_0^{-m}s^{m+1})\), smaller than the pole contribution by \((\sigma/R_0)^m\) after beta normalization. On \(t<1/2\), use the unexpanded original Mellin density and \(\sum_{j\le m} b_j=O(\sigma^{-m})\). Its total is \(O(\sigma^{-m}256^{-n})\). At \(m=\alpha_*n+O(1)\) its exponential rate \(-\log256+\alpha_*\log(1/\sigma)\approx-4.552\) is strictly smaller than the saddle's \(\log u_0\approx-4.2784\). Thus it is negligible. No uniform-in-m fixed-time identity is asserted.

For \(m=\alpha_*n+O(1)\), the beta integrand in TS7 concentrates at \(u=u_0\); Laplace's method with
\[
f(u)=\log u+\alpha_*\log(1-u),\quad
f'(u_0)=0,\quad -f''(u_0)=1/(u_0^2\sigma)
\]
gives, uniformly over bounded \(m-\alpha_*n\),

\[
\boxed{
\varepsilon_m(n)\sim
C_*\,\frac{u_0^n}{\sqrt n}
=C_*\,\frac{\tau^{8n}}{\sqrt n},\quad
C_*=-\frac{P_r'(\tau)}{8\tau^6}\sqrt{2\pi\sigma}
\approx44.844291342999.}                            \tag{TS8}
\]

Here \(P_r'(\tau)=96-72\sqrt2<0\). In particular the optimal residual has this sharp asymptotic, improving #507's legitimate but nonoptimal \(\varepsilon_n(n)\le C(4\sigma)^{-n}\).

**Ill conditioning is not paid by the small residual.** The #507 delay coefficients satisfy
\[
\sum_{\ell=1}^m|a_\ell^{(m)}|
=\sum_{k=1}^m b_k(2^k-1)=\Theta((2/\sigma)^m).
\]
At \(m\sim\alpha_*n\), its norm grows as \(\exp((\alpha_*\log(2/\sigma)+o(1))n)\approx\exp(50.2931n)\). Thus observer precision/perturbation sensitivity becomes much worse even as the exact rational residual improves.

## TS-04: where Lambert W legitimately appears

Define the *pole/Beta exponential envelope* for a fixed order ratio \(m/n\to\alpha>0\),

\[
\Phi(\alpha)=\alpha\log(\alpha/\sigma)
             -(1+\alpha)\log(1+\alpha).
\]

This is the exponential rate of the explicitly defined positive **pole term** TS7, with a slowly varying positive multiplier. It is not a rate proved for the entire residual for arbitrary \(\alpha\). Differentiation gives

\[
\Phi'(\alpha)=\log\frac{\alpha}{\sigma(1+\alpha)},\quad
\Phi''(\alpha)=1/[\alpha(1+\alpha)]>0.
\]

Therefore its unique minimum is at the ALGEBRAIC \(\alpha_*\), with \(\Phi(\alpha_*)=\log u_0<0\). The envelope crosses zero again at a unique \(\alpha_{\rm env}\approx519.5540956674056\). Setting \(\delta=-\log\sigma>0\) and expanding at large \(\alpha\) gives

\[
\Phi(\alpha)=\delta\alpha-\log\alpha-1+O(1/\alpha).
\]

Solving the leading equation \(\delta\alpha=\log\alpha+1\) gives the genuine *secondary asymptotic inversion*

\[
\boxed{
\alpha_{\rm W}=-\frac{W_{-1}(-\delta/e)}{\delta}
\approx519.47419623610,\quad
\alpha_{\rm env}-\alpha_{\rm W}\approx0.07989943.} \tag{TS9}
\]

The nonprincipal negative real branch \(W_{-1}\) is required by the large root. This W formula is an approximation to the envelope crossover; **it is not** the exact equation for \(\tau\), nor evidence of a Lambert-W dynamics in the actual π-digit time orbit. See NIST DLMF §4.13 on W and its two real branches.

## Relation to the selected π-normality obstruction

The source-dependent zero \(t=\tau\) simultaneously marks: maximum radial potential, angular midpoint, sign reversal of \(\rho\), singular inverse jet multiplier, and the optimal beta-observer saddle. **This is a structural localization mechanism for reconstructing the forcing.** It is not a distribution theorem for the selected real circle phases.

Neither TS-01 through TS-09 nor the nonlinear bispectrum from #508 controls the authenticated original maximal-subinterval Weyl sum at \(H_A(h)\). The same-four-pole coherent wrong seed shares the forcing and radial source and consequently the entire observer-order optimization, but fails the critical Weyl rate. The unresolved obligation remains a new signed inequality binding **the original literal zero-seeded angular/carry phase** to its radial observer corrections. At present the best scope is a strong new mathematical characterization of the source-jet information bottleneck, not a π-normality proof.

## Validation and authority

- Independent SymPy algebra of the four-pole/radial rational sources, \(P_r(\tau)=0\), \(\alpha_*\), \(P_r'(\tau)\), and first four \(b_k\) passed.
- Exact Fraction + rational tail enclosures independently certified DEVELOPMENT moment crossings \(n=1,2,3,5\).
- NEW n=7,11,13 source-moment crossings were specified before testing in PREREGISTRATION.md; exact Fraction enclosures verified the first-negative k as **481, 765, 908** respectively, with no ambiguous enclosures.
- High-precision n=10,20,40,80 moment diagnostics were development checks, not external validation.
- The TS-08 saddle asymptotic is a paper derivation from the explicit pole decomposition with displayed exponentially small regular contributions, not an inference from these finite cases.
- No new Lean theorem, independent external peer review, global scholarly novelty, full native SUCC CI or π normality theorem claimed.

**NEXT:** seek a nonlinear, source-labelled angular/radial/carry test whose good observer-order moments are provably incompatible with the original selected coherent phase at the true critical Weyl depth. A scalar optimal truncation cannot distinguish original zero seed from a changed homogeneous seed.
