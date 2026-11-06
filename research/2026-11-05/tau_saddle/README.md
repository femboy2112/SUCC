# Operation TAU SADDLE × OPTIMAL VIRTUAL OBSERVER

**Research-only, additive child of [PR #508](https://github.com/femboy2112/SUCC/pull/508) at pinned exact parent 61cdf240d0c2e75afe934dde6c98ce71a783a832.** Source-normality OPEN. No original four signed BBP poles, seed U0=0, production, frozen contracts, formal/Lean, workflows, license or main altered.

The original radial source's interior sign zero \(\tau=2-\sqrt2\) has **four exact roles**: (1) \(G(t)=2\log((2-t^2)/(t^2-2t+2))\) attains its maximum \(\log2\) there; (2) the Gaussian angular observation reaches \(\pi/8\), half its quarter arc; (3) the radial Mellin density \(\rho(t)\) changes sign there; (4) the source-jet coefficient generating function has its singularity at \(s=\sigma=1-\tau^8\).

**New paper results:** For every n, the signed radial observer moment \((1-E)^kZ_n\) has exactly one sign crossing in real observer order k. Since the source-jet coefficients b_k are strictly positive, the unique finite-order reconstruction residual strictly decreases, then increases. Its minimizing order obeys

\[
m_{\rm opt}(n)=\left(\tau^{-8}-1\right)n+O(1)\approx71.12494584n+O(1).
\]

At this source-derived saddle the residual has the sharper asymptotic

\[
\varepsilon_{m_{\rm opt}(n)}(n)\sim
C_*\,\tau^{8n}/\sqrt n,\qquad
C_*\approx44.844291342999,
\]

where the coefficient L1 norm grows as \(\exp((50.29309+o(1))n)\). **Very accurate, but extremely ill-conditioned.** This refines #507's m=n exponential source reconstruction without implying any improvement in π's signed Weyl/current estimate.

**Lambert W:** the primary threshold is ALGEBRAIC. A separate pole/Beta asymptotic envelope \(\Phi(\alpha)=\alpha\log(\alpha/\sigma)-(1+\alpha)\log(1+\alpha)\) has a large positive zero near 519.5541; approximating its large-root equation gives \(-W_{-1}(-\delta/e)/\delta\approx519.4742\) with \(\delta=-\log\sigma\). This is a **secondary asymptotic inversion**, not an asserted Lambert W law for the actual π orbit.

[Mathematical proofs](PROOFS.md) · [Chronological preregistration](PREREGISTRATION.md) · [Claim ledger](CLAIM_LEDGER.md) · [Next discriminating probe](NEXT.md).

**Validation:** 13/13 focused local tests pass. The exact tested source Git blob SHA is \`372bb3661041f55b681c167f7d920169f1eb5cbc\`, verified against the remote committed Git blob. Development exact moment crossings: n=1,2,3,5. New prospectively declared exact Fraction+tail certified crossings: n=7→481, n=11→765, n=13→908. All tests use original radial taps, not π digits. Source-dependent infinite results rest on displayed mathematics, not these finite cases. No full native/hosted suite, new Lean kernel, external referee or worldwide novelty claim.

**Next:** A source-authenticated *signed angular–radial–carry* inequality. The same-forcing coherent wrong seed shares this entire radial saddle/optimal-truncation theorem, so this discovery is NOT evidence of equidistribution by itself.

## New post-preregistration signed angular response (AR-01/02)

[ANGULAR_RESPONSE.md](ANGULAR_RESPONSE.md) proves an additional **source-only mixed observation**. At the unique real radial moment zero \(k_c(n)\), the scalar \(I_{k_c(n)}(n)=0\), but the Gaussian-half-arc transported response
\[
\mathcal M_{n,k}(q)=\int_0^1t^{8n}\rho(t)(1-t^8)^k
   e^{i q[\theta_0(t)-\pi/8]}dt
\]
has **strictly positive imaginary part for every n>=1, real k>=0 and integer q=1,...,8**. Its exact saddle behavior is
\[
\lim_{n\to\infty}
n\,\mathcal M_{n,k_c(n)}(q)/
  \left[\mathrm B(n+1/8,k_c(n)+1)/8\right]
=i q\,\frac{3825\sqrt2-5406}{2048}.
\]
This is a strictly oriented analytic angular–radial response despite scalar radial cancellation. It does not bound the original chronological \(\pi\)-orbit's Weyl sums. [Four new focused tests](../../../tests/test_tau_angular_response.py) passed locally, making 17/17 total. Their executed Git blob SHA is \`1f7e0b42453882998233526dcd9c2bfce255e152\`, verified against GitHub.