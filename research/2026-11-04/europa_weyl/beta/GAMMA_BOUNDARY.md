# The Catalan and angular-period remainders recover Euler's constant

Use the chronological finite source polynomial \(B_N\) of BETA_WEIL.md, with \(m=8N\), \(G=\beta(2)\) (Catalan's constant), and \(R_N(s)=\beta(s)-B_N(s)\). For every N≥1,
\[
 0<\frac{G-B_N(2)}{\pi/4-B_N(1)}-H_{m+1}
   <\frac{3}{(m+2)(m+3)-2}.                                      \tag{1}
\]
The difference is \(3/m^2+O(m^{-3})\), so the leading constant in this bound is sharp. In particular,
\[
 \gamma=\lim_{N\to\infty}
 \left[\frac{G-B_N(2)}{\pi/4-16^{1-N}Y_N/4}-\log(8N+1)\right].
\]
This is an identity for the lifted zero-seed endpoint and a separate s=2 source evaluation. It uses Catalan's constant and π as target period values. It supplies no digit oracle to the recurrence.

**Proof.** With the probability density \((m+1)(1-x)^m\,dx\) on (0,1) let \(U=-\log x\) and \(W=(1+x^2)^{-1}\). The Mellin remainder formula gives
\[
 (m+1)16^N R_N(1)=E W,\qquad (m+1)16^N R_N(2)=E[UW].
\]
This integral measure is defined by the analytic remainder. It does not average over real-orbit starting points. Beta integration and differentiation in k give, for nonnegative integers k,
\[
 E[x^k]=\binom{m+k+1}{k}^{-1},\qquad
 E[Ux^k]=E[x^k](H_{m+k+1}-H_k).
\]
Indeed the beta integral with a real exponent k is \((m+1)!/\prod_{j=1}^{m+1}(k+j)\). Thus \(EU=H_{m+1}\). U and W are strictly decreasing in x, so \(\operatorname{Cov}(U,W)>0\), by the independent-copy covariance formula. Write \(W=1-x^2+S\), \(S=x^4/(1+x^2)\). S increases, so
\[
 \operatorname{Cov}(U,W)\le-\operatorname{Cov}(U,x^2)
 = \frac2{(m+2)(m+3)}
        \left(\frac32-\frac1{m+2}-\frac1{m+3}\right).
\]
Divide by \(EW\ge 1-E[x^2]>0\) to get (1). Also \(x^4-S\) increases, so \(0\le-\operatorname{Cov}(U,S)\le-\operatorname{Cov}(U,x^4)\le H_4 E[x^4]=O(m^{-4})\). Combining with \(EW=1+O(m^{-2})\) gives the asserted sharp coefficient.

**The transverse complex Mellin boundary.** Uniformly on every compact \(K\subset\{\Re s>0\}\), with \(L=\log m\),
\[
 \frac{m16^N\Gamma(s)R_N(s)}{L^{s-1}}
 =1+\frac{(s-1)\gamma}{L}+O_K(L^{-2}).                         \tag{2}
\]
To see this set v=mx in the remainder. The resulting integral on (0,m) has weight \(w_m(v)=(1-v/m)^m/(1+(v/m)^2)\) times \((1-\log v/L)^{s-1}\), with positive real bases. The total mass is \(mEW/(m+1)=1+O(m^{-1})\). Its normalized expectation of \(-\log v\) equals \(E[UW]/EW-\log m=\gamma+O(m^{-1})\) by (1) and elementary harmonic-number bounds. Its second unnormalized log moment is bounded by \(\int_0^\infty e^{-v}(\log v)^2dv\). For \(m^{-1/2}\le v\le m^{1/2}\), use the uniform Taylor remainder \(O_K((\log v/L)^2)\). Below this range logarithmic powers are integrable and give \(O_K(m^{-1/2}\operatorname{poly}_K(L))\). Above it \(w_m\le e^{-v}\); if \(\Re s<1\), use \(-\log(v/m)\ge1-v/m\) and absorb the one resulting inverse power into \((1-v/m)^m\), still bounded there by \(e^{-\sqrt m/2}\) for large m. These tails, including their first two log moments, give \(o_K(L^{-2})\). Integrating the Taylor expansion gives (2).

At s=1 the gamma coefficient in (2) vanishes identically. The ratio in (1) extracts it at s=2 with much better accuracy. A seed shift by a sends the observed rescaled endpoint to \(16^{1-N}Y_N^{(a)}/4=B_N(1)+4a\), while the source polynomial B_N and its value B_N(2) remain fixed. If that shifted lift is *substituted for* B_N(1), the denominator tends to −4a, so the ratio tends to zero for a≠0. This distinguishes lifted seed choices. The ratio uses a second Mellin moment, and neither estimate controls the signed Weyl sum of the selected real phases. In particular no uniform bound over rational cofactors or circle near-pairs follows.

**Scope and prior work.** The probability identity \(EU=H_{m+1}\) is also the classical expected maximum of m+1 independent unit exponentials; the angular kernel supplies the specific rational tilt W. Rényi's order-statistic calculations and the elementary beta/gamma identities give antecedents for this mechanism. The finite polynomial is an instance of the complex Euler series transformation; annihilation of polynomial sequences by high finite differences explains its exact negative-integer termination. No priority is claimed. [Rényi (1953)](https://doi.org/10.1007/BF02127580).

Run `python3 gamma_boundary_probe.py` to regenerate `gamma_receipt.json`. The verifier uses alternating Taylor envelopes for W, independent of the covariance proof. It confirms the strict bounds with rational intervals at four preregistered N. The finite holdouts are regression checks. The all-N inequalities rely on the proof.
