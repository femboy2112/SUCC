# GTQ6-15: universal Cesaro cancellation of the **unconditioned** signed seam

**Addendum to the source-specific q6 Gamma seam theorem, 2026-10-29.** This is a negative control, not evidence of pi normality.

Let `z_m` be ANY bounded complex sequence, `|z_m|<=1`. The exact source-derived finite Pascal grade law is `q_n(j)` from PR #370. Let

\[
 \chi(j)=1_{\gcd(j,6)=1},\quad d_j=\chi(j+2)-\chi(j),\quad
 A_j=\frac1{j+2}+\frac1{j+3}+\lambda^{j+3},\quad
 \theta_j=e^{i\pi(j+2)/8},\quad \lambda=\varphi^{-1}.
\]

The **carry-summed** (or unmarked) seam is

\[
 G_n(z)=\sum_{j=0}^{n} q_n(j)d_j A_j\theta_j(z_{n+j}-z_{n+1}).
\]

## Theorem: a universal source-independent time-mean bound

For each `L>=3,N>=1`,

\[
 \boxed{\left|\frac1N\sum_{n=L}^{L+N-1}G_n(z)\right|
 \le\frac4N+\frac{88}N\sum_{n=L}^{L+N-1}\frac1n.}
\]

**Proof.** First replace the exact finite law q_n by the limiting source `w_j=(j+1)/2^(j+2)`. The pointwise error is <=88/n, since the inherited total-variation estimate `TV(q_n,w)<=22/n` implies `sum_j |q_n(j)-w_j|<=44/n` and the bounded summand has magnitude <=2. (The nonzero selector grades are >=1, so A_j<1.)

Now, for the stationary Oily filter and any j>=1,

\[
 \left|\sum_{n=L}^{L+N-1}(z_{n+j}-z_{n+1})\right|\le2(j-1),
\]

because the overlapping interior terms cancel, leaving only boundary indices. Hence

\[
 \left|\sum_n\sum_jw_jd_jA_j\theta_j(z_{n+j}-z_{n+1})\right|
 \le2\sum_jw_j|d_j|A_j(j-1)
 \le2\sum_j j w_j=4.
\]

Here `sum j*w_j=2` is exact from the Oily probability-generating function `(2-z)^(-2)`. Divide by N and add the accumulated <=88/n source variation. QED.

### Why this is important

The previous theorem proved a positive lower **limsup of instantaneous norm** for the authentic zero seed and O(n^-2) decay for the coherent changed seed. This addendum proves that the signed **unconditioned time mean** is nevertheless asymptotically zero for **every** bounded phase sequence, even a constant sequence, a periodic sequence, or a nonnormal one.

Therefore: claiming `G_n` has vanishing Cesaro mean is mathematically true but logically **useless** for pi normality. The only potentially informative next objects are the **individual literal-carry-conditioned components** `A_(n,h,c)` or nonlinear cross-bin interactions, for which the carry labels obstruct this generic telescoping. Their positive-density or signed mean estimates remain completely open.

The Gamma Abel twist is constant per grade and is included in the universal bound; it does not rescue a carry-summed Weyl criterion.
