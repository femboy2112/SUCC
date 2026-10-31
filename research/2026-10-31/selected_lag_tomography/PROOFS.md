# Operation SIGNED LAG FORGE — true BBP phase, logarithmic conductor sieve, and finite tomography

**Research-only, 2026-10-31.** Parent: PR #433 exact SHA 5721c048b54430b3d2195d63ba4d1a9ec0794f99; sibling PR #432 SHA d3907a7937b10dbf51f3926e0dd3460d5ff12353 imported via all 11 identical Git blobs. PR #431 is inherited by both. Main XVII e8598cfa5d32fd1de8e94a3e458a366a0850d59e, original four signed BBP poles, literal U0=0, source archives, formal, production and CI workflows unchanged. **π normality and RH remain OPEN.**

## LAG-01 — original signed recurrence admits an EXACT lag reduction

Preserve the authentic source:
\[
r(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2),\quad
U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
For any integer h≠0 write e(x)=exp(2πix), z_n=e(hU_n), and S_N=Σ_(n=1)^N z_n. For 1≤k<N,
\[
\boxed{U_{n+k}-U_n=(16^k-1)U_n+F_{n,k},\quad
F_{n,k}=\sum_{j=1}^{k}16^{k-j}r(n+j)>0.}
\tag{L1}
\]
Let actual lag C_(h,k)(N)=Σ_(n=1)^(N-k) e(h(U_(n+k)-U_n)), and source-reduced lag D_(h,k)(N)=Σ_(n=1)^(N-k)e(h(16^k-1)U_n). The ORIGINAL full offdiagonal Gram has the exact partition
\[
\boxed{|S_N(h)|^2=N+2\sum_{k=1}^{N-1}\operatorname{Re}C_{h,k}(N).}\tag{L2}
\]
The corresponding virtual-seed tomography labels in PR #432 are the distinct integer frequencies h(16^(n+k)-16^n)=h16^n(16^k-1), with the actual source pair phase retained. Phase reconstruction is not a bound on the reconstructed sum. Scalar edge phases are gradient-flat by PR #431, not artificial physical holonomy.

## LAG-02 — all-horizon source error for the four ORIGINAL poles

The original source's positive regrouping gives r(n+1)<15/(64n²) for n≥1, and r is decreasing. As Σ_(n≥1)n^-2<2, Σ_(n≥1)r(n+1)<15/32. Hence
\[
\sum_{n\ge1}F_{n,k}
\le\frac{16^k-1}{15}\sum_{n\ge1}r(n+1)
<\frac{16^k-1}{32}.
\tag{L3}
\]
The elementary |e(x+y)-e(x)|≤2π|y| and π<22/7 give the **uniform, rational, source-authenticated error**
\[
\boxed{|C_{h,k}(N)-D_{h,k}(N)|
<\frac{\pi|h|}{16}(16^k-1)
<\frac{11|h|}{56}(16^k-1).}\tag{L4}
\]
Valid for every original seed label if counterfactuals are explicitly marked, but in the proof target U0 is LITERALLY zero. This is source transport, not signed cancellation.

## LAG-03 — finite van der Corput plus a SIGNED lag source certificate

For 1≤K≤N extend z_n by zero outside the observed window. For time t=1,...,N+K-1 set V_t=Σ_(j=0)^(K-1)z_(t-j). Then Σ_tV_t=KS_N and Cauchy–Schwarz gives K²|S_N|²≤(N+K-1)Σ_t|V_t|². Expanding the latter exactly,
\[
\sum_t|V_t|^2
=KN+2\sum_{k=1}^{K-1}(K-k)\operatorname{Re}C_{h,k}(N).
\]
Define the ONE source-selected signed observable
\[
\boxed{\mathcal L_{N,K}(h)=\frac2{KN}
\sum_{k=1}^{K-1}(1-k/K)\operatorname{Re}D_{h,k}(N).}\tag{L5}
\]
This permits genuine destructive inter-lag cancellation; a condition on the absolute sizes of every D is unnecessarily strong. The quantitative all-horizon bridge is
\[
\boxed{
|S_N(h)/N|^2
\le (1+(K-1)/N)\,[1/K+\mathcal L_{N,K}(h)+E_{N,K}(h)].
}\tag{L6}
\]
The source forcing is paid by an explicit positive RATIONAL error:
\[
\boxed{E_{N,K}(h)=
\frac{11|h|}{28KN}\sum_{k=1}^{K-1}(1-k/K)(16^k-1)
\le\frac{11|h|(16^K-16)}{420KN}.}\tag{L7}
\]
For K=1 both error sums are zero; no division-by-zero or fictitious phase law. The exact Gaussian-integer Cauchy/Gram expansion is checked by an independent sliding-window oracle.

## LAG-04 — usable FULL logarithmic lag window, not a π proof

Take K_N=floor(log_16 N), N≥256. Then 16^K≤N and
\[
0\le E_{N,K_N}(h)\le11|h|/(420K_N)\to0
\]
for each FIXED nonzero h. Furthermore K_N/N→0 and 1/K_N→0. Thus the following is a valid conditional **sufficient** theorem:
\[
\boxed{
\forall h\in\mathbb Z\setminus\{0\},\
\limsup_{N\to\infty}\mathcal L_{N,\lfloor\log_{16}N\rfloor}(h)\le0
\ \Longrightarrow\
\pi\text{ is base-16 normal}.
}\tag{L8}
\]
The entire source-error budget is O_h(1/log N), even though its largest individual lag correction can be O(N). This is a genuinely narrowed *route*: at each horizon the signed all-pair Gram is replaced by a weighted bundle of only O(log N) arithmetic frequencies h(16^k-1), with a proved forcing/coverage bridge. **The required upper bound for the actual zero-seeded source has not been proved.** This fixed critical-clock sufficient condition may be stronger than normality in general; do NOT label it necessary without proof. Existing selected-logarithmic absolute-loss results N−c log N are still insufficient.

## LAG-05 — prime 3/5 conductor and local character firewall

Classical LTE yields for every k≥1
\[
v_2(16^k-1)=0,\quad
\boxed{v_3(16^k-1)=1+v_3(k),\quad v_5(16^k-1)=1+v_5(k).}
\tag{L9}
\]
The first lag frequencies are 15h, 255h (3·5·17), 4095h (3²·5·7·13). This is a natural arithmetic sieve coupling SUCC's dyadic carrier and its 3/5 exceptional poles. It does NOT prove real Weyl cancellation. The inherited authentic dyadic source isometry implies perfect local character cancellation for h not divisible by 2^a on complete 2^a source windows, even after multiplication by odd 16^k−1; this local Haar cannot be equated with real-circle characters (explicit (0,1) counterexample). The 3-adic pole-depth refinement in PR #430 deletes rare deep poles for bounded complex phases only, not for unbounded p3 norms.

## LAG-06 — calibrated, finite, RIGOROUS signed selection evidence

The exact source interval oracle constructs π bounds from Machin's 16 arctan(1/5)−4 arctan(1/239) identity and rational alternating remainders. It converts each exact rational phase into a bounded-denominator rational cell, pays the cosine Lipschitz error, evaluates an exact rational Taylor polynomial with a global remainder bound, and outward-rounds each cosine to 10^−12. There are no external π digits or float-only numerical sign claims.

For h=1,K=4, direct finite source computation gives (displays abbreviated; exact fractions in CERTIFIED_LAG_RECEIPTS.md):

| N | selected signed L | coherent nonnormal seed signed L LOWER bound | selected normalized squared Weyl UPPER bound |
|---:|---:|---:|---:|
| 512, calibration | −0.003785708291 | 0.524562290736 | 0.471959875551 |
| 1024, fresh horizon | −0.009154820708 | 0.637281145368 | 0.353375586652 |
| 1536, fresh horizon | −0.007533026406 | 0.674854096912 | 0.317417822792 |

These are real finite inequalities using the original rational zero seed and a genuine same-forcing nonnormal control. They are **NOT asymptotic information**; there is no proof they continue at later N. The intervals derive from rational arithmetic, not from Monte Carlo or auxiliary seed Haar.

## LAG-07 — precise hostile controls

- For the fixed coherent same-forcing seed s*=−π/16, U_n(s*)=−T_n, so
\[
\boxed{\mathcal L^{s_*}_{N,K}(h)
\ge\frac{K-1}{K}\left(1-\frac{K+1}{3N}\right)-E_{N,K}(h).}\tag{L10}
\]
At K_N=floor(log16 N) and fixed h, this lower bound tends to one. The proposed sufficient criterion L8 **definitively FAILS** for this nonnormal seed, despite identical forcing and perfect auxiliary seed-Haar moments.
- The irrational near-zero nonnormal shadows of PR #433 have source seeds s_L=q_L−π/16 with |s_L|<16^-L/[(8L+1)(8L+2)] and exactly rational completed orbits. For every finite N≤L, their lag score differs from the selected zero-seed score by an explicit rational nearzero_nonnormal_shadow_lag_error_bound in the module. Hence ANY finite source measurement can be spoofed arbitrarily closely by some *fixed* nonnormal infinite orbit. Finite calibration is not proof.
- Wall's rational-addition theorem means ordinary FIXED rational seed changes preserve base-16 normality status; do not impose false mandatory-failure tests on s=1/7. The exact literal zero seed remains essential to the claimed SOURCE.
- The measure μ=(δ_0+δ_(1/3)+δ_(2/3))/3 is invariant under ×16, non-Haar, and μhat(1)=0 but μhat(3)=1. A single h or finite arbitrary modes cannot establish normality.
- Positive path resistance, gauge-trivial phases, q-Pascal model root-of-unity cancellation, and finite 73-channel tomography alone give NO asymptotic selected saving. The latter only reconstructs genuine finite phase ratios.

## Verdict / source-map debt

**PROVED LOCAL / CLASSICAL:** LAG01–05 and LAG07, with exact proof, assumptions and honest source dependencies. **OBSERVED FINITE:** LAG06 rational outward certificates and 28 focused locally executed exact tests, including independent Gaussian window energy and original source recurrence oracle. **OPEN:** prove the signed LAG04 upper bound (or a weaker truly sufficient variant) from authentic four signed poles and exact U0=0 with all-horizon coverage; π normality and RH remain OPEN.

The next external execution is specified in ASTRA_ULTRA_HANDOFF.md. Its objective is to achieve an **unconditional original-source all-horizon signed estimate**, not merely restate Weyl or re-run the finite intervals.