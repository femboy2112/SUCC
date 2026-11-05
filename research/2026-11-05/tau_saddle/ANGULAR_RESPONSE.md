# Angular response at the radial observer's exact zero: a signed cross-channel theorem

**Research-only post-preregistration extension of draft #509.** This result was derived after the original tau-saddle preregistration, so no test below is claimed to be an independently preregistered discovery. Original signed four BBP poles, literal source U0=0, original carry, frozen proofs, historical Lean, production, workflows and main remain untouched. This is an *analytic Mellin-carrier observation*, not a signed exponential-sum estimate for the chronological orbit of π.

## AR-01: the radial scalar zero is NOT an angular-observer zero

Use exactly the genuine #507 radial signed density \(\rho(t)=-P_r(t)/(16-t^8)\), \(t\in[0,1]\), with unique zero \(\tau=2-\sqrt2\). For every original source index \(n\ge1\) and *real* observer order \(k\ge0\), let
\[
I_k(n)=\int_0^1 t^{8n}\rho(t)(1-t^8)^k\,dt.
\]

#509 TS-01 proves \(I_k(n)\) has a unique real root \(k=k_c(n)>0\). The scalar signed source observer therefore sees \(I_{k_c(n)}(n)=0\).

The authentic Gaussian angular coordinate from #499 is
\[
\theta_0(t)=\arctan(t-1)+\pi/4,\quad
\theta_0'(t)=\frac1{(t-1)^2+1}>0,\quad
\theta_0(0)=0,\quad \theta_0(1)=\pi/4,\quad
\theta_0(\tau)=\pi/8.
\]

**Declare the shared frame transport** to be rotation by the *same* reference angle \(\theta_0(\tau)=\pi/8\); do not average over unrelated frames. For every integer \(1\le q\le8\), define the exact cross-channel response
\[
\mathcal M_{n,k}(q)
 =\int_0^1 t^{8n}\rho(t)(1-t^8)^k
   \exp\!\left(iq[\theta_0(t)-\pi/8]\right)\,dt.
\]

For every \(t\ne\tau\) in the interior, the sign of \(\rho(t)\) equals the sign of \(t-\tau\). The sign of \(\theta_0(t)-\pi/8\) also equals the sign of \(t-\tau\). Since \(|q(\theta_0(t)-\pi/8)|<\pi\) for \(q\le8\) on \(0<t<1\), the sine has the same sign. Therefore the product is strictly positive:
\[
\boxed{\operatorname{Im}\mathcal M_{n,k}(q)
=\int_0^1t^{8n}\rho(t)(1-t^8)^k
  \sin(q[\theta_0(t)-\pi/8])dt>0.}    \tag{AR1}
\]
This holds for EVERY n>=1, real k>=0 and integer q=1,...,8. In particular
\[
\boxed{I_{k_c(n)}(n)=0,\quad
       \operatorname{Im}\mathcal M_{n,k_c(n)}(q)>0.}     \tag{AR2}
\]
The scalar radial cancellation still leaves a rigorously oriented nonzero angular response, with a declared common phase basis. **This is not a sign-free “zero” and not an independent physical energy field.**

## AR-02: sharp leading angular response at the beta saddle

Set
\[
u_0=\tau^8,\ \sigma=1-u_0,\ \widetilde\rho(u)=\rho(u^{1/8}),
\ \widetilde\theta(u)=\theta_0(u^{1/8}),\
B_{n,k}=\frac18\mathrm B(n+1/8,k+1).
\]
Under the auxiliary \(\mathrm{Beta}(n+1/8,k+1)\) law, write \(U\) for the beta variable. Then \(\mathcal M_{n,k}/B_{n,k}\) is the expectation of \(\widetilde\rho(U)\exp(iq[\widetilde\theta(U)-\pi/8])\), and \(I_k(n)/B_{n,k}=\mathbb E[\widetilde\rho(U)]\).

At the exact real root \(k=k_c(n)\), the latter expectation is identically zero. Its location satisfies \(k_c(n)=\alpha_*n+O(1)\), \(\alpha_*=\sigma/u_0\), as proven in TS-02. The beta law concentrates at \(u_0\), with \(\mathbb E(U-u_0)=O(1/n)\), \(\mathbb E[(U-u_0)^2]=u_0^2\sigma/n+O(n^{-2})\), and third centered signed moments \(O(n^{-2})\).

Subtracting the ZERO scalar expectation from the complex response and expanding near \(u_0\):
\[
\widetilde\rho(U)\left(\exp(iq[\widetilde\theta(U)-\pi/8])-1\right)
=iq\,\widetilde\rho'(u_0)\widetilde\theta'(u_0)(U-u_0)^2
+O((U-u_0)^3).
\]
The beta concentration/tail estimates justify termwise expectation (the absolute third centered moment is \(O(n^{-3/2})=o(n^{-1})\)). Consequently
\[
\boxed{
\lim_{n\to\infty}
  n\,\frac{\mathcal M_{n,k_c(n)}(q)}{B_{n,k_c(n)}}
= i q\,u_0^2\sigma\,
\widetilde\rho'(u_0)\widetilde\theta'(u_0).
}                                                   \tag{AR3}
\]

This limit is PURELY imaginary and has strictly positive orientation. The exact constant reduces using \(P_r'(\tau)=96-72\sqrt2<0\), \(\theta'_0(\tau)=1/(2\tau)\), to
\[
\boxed{
u_0^2\sigma\widetilde\rho'(u_0)\widetilde\theta'(u_0)
=\frac{\sigma\tau[-P_r'(\tau)]}{128(16-u_0)}
=\frac{3825\sqrt2-5406}{2048}
=0.00164398245951589925\ldots>0.
}                                                   \tag{AR4}
\]
No π digits enter the source or this constant: π/8 is a classical arctangent angle of the declared Gaussian carrier.

## Independent finite diagnostics and limitations

An independently written 65-digit mpmath implementation used the actual rational radial taps, a **separate 60-term future geometric/beta source tail**, and direct quadrature of the angular-weighted integral after solving the real scalar root. This is numerical development, NOT rigorous interval certification nor a full new blind holdout. Results for q=1:

| n | scalar-zero root k_c (numerical) | n * Im(M)/B | ratio to AR4 |
|---:|---:|---:|---:|
| 2 | 125.971962449401 | 0.00176018813477 | 1.070685 |
| 5 | 338.467082240367 | 0.00169613153961 | 1.031721 |
| 10 | 693.813760447889 | 0.00167089409788 | 1.016370 |
| 20 | 1404.92825237689 | 0.00165763226453 | 1.008303 |

The reported ratios approach the analytic value 1 from above; this is calibration, not the reason the limit is claimed. Separate exact symbolic and numeric tests are in \`tests/test_tau_angular_response.py\` and were run locally.

**Strict boundary:** \(\mathcal M_{n,k}\) is an integrated analytic Mellin-observer response over source parameter \(t\), whereas normality asks for chronological time averages \(\sum_{n\in I}e(H(Y_n+Z_n))\). We HAVE NOT transferred AR1–AR4 to that empirical selected trajectory. The same-four-pole wrong seed leaves the analytic source densities and these results unchanged. Thus neither a Weyl bound nor π normality follows.

**Next verdict-changing obligation:** construct and verify a source-authenticated transport from this **declared positive mixed angular current** to a nontrivial bound on the original selected integer-carry-conditioned sharp-window Weyl correlation. Pay the observer Jacobian, chronology, and original zero-seed. If that transport is only a renamed Weyl criterion or assumes sampling according to the auxiliary beta distribution, reject it.
