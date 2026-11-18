# The BBP Wavelet–Pascal–Gamma Crucible: Finite Noise Floor, Exact Observer-Energy Budget, and a Source-Time Impulse Tower

**SUCC π-normality research offensive, 2026-11-17.**
**Branch:** research/bbp-borwein-kernel-discrepancy-crucible-2026-11-17, stacked on draft PR #657 as draft PR #663.
**Originating challenge (Leah):** repeatedly lift the SUCC observer through its knowledge volume; treat Dirac and Borwein impulses as source-typed convolution instruments; use the Gamma function as a real analytic continuation/normalization law; ultimately prove π's base-16 normality from the literal zero-seeded BBP history.

**Status:** WPG-01–09 are **CLASSICAL / PROVED PAPER** algebra, source-integral asymptotics and exact rational certificate constructions. WPG-10 is a **REFUTED general normality inference** with an explicit locked source. The joint scalar limit, all-shell R0 inequality, and all-mode π normality remain **OPEN** for authentic π. The assembled observer calculus is a research synthesis, not a claim of priority over Fejér kernels, Hilbert-space ANOVA, Hausdorff moments, Bernstein approximation or Laplace asymptotics.

## 1. Source passport and faithful observable

Keep the source unchanged:
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\qquad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
Let \(x=\pi/16\). The original completion is \(U_N+T_N=16^Nx\) with positive tail \(T_N=\sum_{j\ge1}16^{-j}r(N+j)\), and \(0<T_N<r(N+1)/15\).

The inherited two-pulse Borwein circle filter [BSI](BORWEIN_SWEPT_IMPULSE_BBP.md) is
\[
L(\theta)=\frac{162}{289}\left(\|\theta\|_{\mathbb T}-\frac1{18}\right)_+^2,\qquad
\ell_0=\int_{\mathbb T}L=\frac{256}{7803}.
\]
Every nonzero Fourier coefficient obeys
\[
\boxed{|\widehat L(h)|\ge \frac{c_\star}{h^2},\quad
c_\star=\frac{2205}{139876},\quad h\in\mathbb Z\setminus\{0\}.}\tag{WPG0}
\]

Write \(\Phi(\theta)(\alpha)=L(\theta-\alpha)-\ell_0\in H=L^2(\mathbb T,d\alpha)\). For any \(N\) phases \(\theta_0,\ldots,\theta_{N-1}\) set \(F_N=N^{-1}\sum_n\Phi(\theta_n)\) and \(\mathcal V_N=\|F_N\|_2^2\). For authentic π choose \(\theta_n=16^nx\bmod1\). Rational shadows at a shared terminal \(U_M\) produce exactly rational finite counterparts, with source-tail certificates.

## 2. Finite observers cannot be exactly Haar: a sharp-order universal floor

**WPG-01 (PROVED; finite atomic observer floor):** for *every* finite phase list of length \(N\ge1\), including repeated points and all original-BBP shadows,
\[
\boxed{
\mathcal V_N\ge\frac{c_\star^2}{16N^4}
=\frac{4862025}{313044726016\,N^4}>0.
}\tag{WPG1}
\]

**Proof.** Let \(M_h=N^{-1}\sum_{j=0}^{N-1}e(h\theta_j)\). The nonnegative Fejér kernel
\[
F_{2N}(t)=\frac1{2N}\left|\sum_{j=0}^{2N-1}e(jt)\right|^2
=\sum_{|h|<2N}\left(1-\frac{|h|}{2N}\right)e(ht)
\]
has \(F_{2N}(0)=2N\). Its empirical pair average is at least the diagonal contribution \(2\), while Fourier expansion equals \(1+2\sum_{h=1}^{2N-1}(1-h/(2N))|M_h|^2\). Therefore \(\sum_{h=1}^{2N-1}|M_h|^2\ge1/2\). Parseval and WPG0 give
\[
\mathcal V_N=2\sum_{h\ge1}|\widehat L(h)|^2|M_h|^2
\ge\frac{2c_\star^2}{(2N)^4}\cdot\frac12
=\frac{c_\star^2}{16N^4}.
\quad\square
\]

**WPG-02 (PROVED sharp exponent):** for the equally spaced grid \(\{0,1/N,\ldots,(N-1)/N\}\), \(M_h=1\) iff \(N\mid h\), else zero. Directly from the exact Borwein coefficient and \(3<\pi\), \(|\widehat L(h)|<11/(289h^2)\). Consequently
\[
\boxed{
0<\mathcal V_N^{\rm grid}
=2\sum_{j\ge1}|\widehat L(jN)|^2
<\frac{968}{250563\,N^4}.
}\tag{WPG2}
\]
The upper bound uses \(\sum_{j\ge1}j^{-4}<4/3\). Thus the universal \(N^{-4}\) floor has the **correct order** for this filter.

**Interpretation:** a finite atomic observer cannot report Haar precisely; it may still converge to Haar as \(N\to\infty\). This does **not** prove a universal noise process, random π digits, R0, or normality. The floor is *source-independent* and cannot certify that the original-source energy decays.

## 3. The exact signed interference defect between consecutive orbit blocks

For two equal-length consecutive blocks \(A=[a,a+N)\), \(B=[a+N,a+2N)\), put \(F_A=N^{-1}\sum_{n\in A}\Phi(\theta_n)\), \(F_B\) analogously. Define
\[
E_A=\|F_A\|_2^2,\quad E_B=\|F_B\|_2^2,\quad
\boxed{\mathfrak D_{a,N}:=\tfrac14\|F_A-F_B\|_2^2\ge0.}\tag{WPG3}
\]

**WPG-03 (PROVED exact Hilbert/Parseval source-chronology interface):**
\[
\boxed{
E_{A\cup B}=\frac{E_A+E_B}{2}-\mathfrak D_{a,N}.
}\tag{WPG4}
\]
For \(\theta_n=16^nx\pmod1\), its actual source radix evolution yields
\[
\boxed{
\mathfrak D_{a,N}=
\frac14\sum_{h\ne0}
|\widehat L(h)|^2
\left|W_{a,N}(h)-W_{a,N}(16^Nh)\right|^2,
}\tag{WPG5}
\]
where \(W_{a,N}(h)=N^{-1}\sum_{n=a}^{a+N-1}e(h16^nx)\). Indeed \(W_{a+N,N}(h)=W_{a,N}(16^Nh)\) **exactly**. The source zero section is retained; no independent randomization of digits or phases occurs.

This is the desired *two-window source-respecting interference* observable. It compares harmonics related by the **actual clock power** \(16^N\), rather than asserting that the auxiliary Mellin lag and chronological shifts are identical.

For one original rational terminal at \(M=a+2N\), replace both blocks by \(\hat\theta_n=U_M/16^{M-n}\pmod1\). All displayed energies and \(\hat{\mathfrak D}_{a,N}\) are exact Fractions. The original source tail and \(\operatorname{Lip}L=144/289\) provide the uniform one-block feature error
\[
\epsilon_{a,N}:=\frac{16r(M+1)}{7225N};
\]
therefore
\[
\boxed{
\left|\sqrt{\mathfrak D_{a,N}}-
\sqrt{\hat{\mathfrak D}_{a,N}}\right|\le\epsilon_{a,N}.
}\tag{WPG6}
\]
The difference in each centered \(L^2\) feature average is ≤\(\epsilon_{a,N}\), and the half-difference obeys the triangle inequality. The rational \(\hat{\mathfrak D}\) can be computed **independently** by pairwise autocorrelation
\[
\boxed{
\hat{\mathfrak D}_{a,N}
=\frac{1}{4N^2}
\left(\sum_{i,j\in A}K(q_i-q_j)
+\sum_{i,j\in B}K(q_i-q_j)
-2\sum_{i\in A,j\in B}K(q_i-q_j)\right),}\tag{WPG7}
\]
where \(K(t)=\int_{\mathbb T}L(\alpha)L(\alpha-t)\,d\alpha\) is rational at rational shifts.

**Hostile checks.** A fixed rational circle orbit (0 or 1/15) has \(E_A=E_B=E_{A\cup B}=C_{\rm atom}>0\) but \(\mathfrak D=0\). Conversely even the authentic finite BBP shadow **does not have monotone merged energy**: for \(a=N=4\), \(E_{A\cup B}>E_A\), an exact Fraction result. Thus the tempting blanket claim that every merger lowers the energy is **REFUTED**. No positive source-derived mixing-rate bound has been established.

**Conditional, not achieved:** if an actual prefix block and its next half satisfy \(E_B\le(1+\kappa)E_A\) and \(\mathfrak D_{0,N}\ge\eta E_A\), then \(E_{[0,2N)}\le(1+\kappa/2-\eta)E_{[0,N)}\). When \(1+\kappa/2-\eta<1\), repeated applicable conditions yield geometric convergence along *that doubling subsequence*. Convergence only on dyadic endpoints does **not** automatically establish normality at every intermediate horizon.

## 4. The observer volume has an exact finite wavelet energy budget

For an *arbitrary* prefix of length \(N\), recursively bisect its index interval into nonempty children, including unequal splits. Every leaf is the centered source-circle feature \(\Phi(\theta_n)\), whose squared norm is **independent of n and phase**:
\[
\boxed{
C_{\rm atom}=\|\Phi(\theta)\|_2^2
=\int_{\mathbb T}(L-\ell_0)^2
=\frac{335872}{304434045}.
}\tag{WPG8}
\]

For any tree node \(I\) with children \(I_L,I_R\), define their means \(F_{I_L},F_{I_R}\), sizes \(p,q\), and total \(m=p+q=|I|\). Its **nonnegative source-rational detail** is
\[
\boxed{
d_I=\frac{pq}{Nm}\|F_{I_L}-F_{I_R}\|_2^2.
}\tag{WPG9}
\]
Here \(N\) is the *global* prefix length, not m.

**WPG-04 (PROVED exact multiresolution ANOVA/Parseval identity):**
\[
\boxed{
C_{\rm atom}
=
\underbrace{\mathcal V_N}_{\text{unresolved Haar-distance energy}}
+
\underbrace{\sum_{I\ {\rm internal}}d_I}_{\text{certified accumulated observer distinctions}}.
}\tag{WPG10}
\]
Proof: for any weighted split of a finite list, the within-node squared deviation satisfies the classical two-population ANOVA identity, and all within-child terms telescope when multiplied by node mass \(m/N\). Leaves have zero within-node variance; every individual feature norm is \(C_{\rm atom}\). The remaining top mean-square is \(\mathcal V_N\).

**The exact knowledge-volume interpretation:** the previous observer's average discards distinctions among its phases; each successor exposes an independent block contrast. At every *finite* N, the total available contrast budget remains short of \(C_{\rm atom}\) by at least WPG1. For the true original BBP orbit,
\[
\boxed{
\pi\text{ normal to base 16}
\iff
\lim_{N\to\infty}
\sum_{I\ {\rm internal}}d_I=C_{\rm atom}.
}\tag{WPG11 — EQUIVALENCE/OPEN}
\]

A finite source-rational prefix from the single endpoint \(U_N\) computes **every** \(d_I\) and the complete budget exactly. Its mean feature differs from the true π prefix by
\[
\epsilon_N=\frac{16r(N+1)}{7225N}=O(N^{-3}).
\]
Therefore \(\left|\sqrt{\mathcal V_N^{\rm true}}-\sqrt{\mathcal V_N^{\rm rational}}\right|\le\epsilon_N\), and the source-rational wavelet budget approximates the true one with a known vanishing error. This is a **source-certified finite artifact**, not a proof that the budget saturates.

**WPG-05 (dense-horizon interpolation, PROVED):** for any bounded feature sequence \(v_n=\Phi(\theta_n)\), if \(M\le N\) then
\[
\boxed{\|F_N-F_M\|_2\le
2\|L\|_\infty\frac{N-M}{N}
=\frac{64}{289}\frac{N-M}{N}.}\tag{WPG12}
\]
Consequently, decay \(\mathcal V_{N_j}\to0\) on a sequence \(N_j\to\infty\) with \(N_{j+1}/N_j\to1\) **does** imply decay at all N. Decay on a merely dyadically spaced subsequence does not follow from this estimate. A prospective proof should use horizons such as \(N_j=j^2\) or supply an independent interpolation theorem.

## 5. The original BBP tail has its own **chronological** impulse/Gamma hierarchy

From the original source's exact impulse/Mellin integral [IMF](BBP_IMPULSE_MELLIN_FILTER.md),
\[
K(t)=\frac{1-t}{(2-t^2)(t^2-2t+2)}>0,\quad
r(n)=\int_0^1t^{8n-8}Q(t)\,dt,\quad Q(t)=(16-t^8)K(t),
\]
the **actual future tail** is an exact source moment:
\[
\boxed{
T_N=\sum_{j\ge1}16^{-j}r(N+j)
=\int_0^1 t^{8N}K(t)\,dt.
}\tag{WPG13}
\]
No new seed, forcing or probabilistic assumption is introduced.

Let \(S\) denote the **chronological one-clock shift** \(S f(N)=f(N+1)\). This is no longer an auxiliary Mellin-exponent shift. Define the k-fold signed impulse response
\[
\boxed{
S_{N,k}=(1-S)^k T_N
=\sum_{j=0}^k(-1)^j\binom kj T_{N+j}
=\int_0^1t^{8N}(1-t^8)^kK(t)\,dt>0.
}\tag{WPG14}
\]

**WPG-06 (PROVED complete monotonicity and Pascal transport):**
\[
\boxed{
S_{N,k}=S_{N+1,k}+S_{N,k+1},\quad
\sum_{N=0}^m\binom mN S_{N,m-N}=T_0=\pi/16
\quad(m\ge0).
}\tag{WPG15}
\]
The first identity is \(t^8+(1-t^8)=1\) inside WPG14. The second is its binomial expansion. Every entry is **strictly positive**.

A finite rational version is obtained by truncating the tail sum to M source terms:
\[
S_{N,k}^{[M]}=\sum_{\ell=1}^M16^{-\ell}
\sum_{j=0}^{k}(-1)^j\binom kj r(N+\ell+j)\in\mathbb Q_{>0}.
\]
It satisfies the **same Pascal identities exactly**, and conserves
\[
\boxed{
\sum_{N=0}^m\binom mN S_{N,m-N}^{[M]}
=P_M=\sum_{\ell=1}^M16^{-\ell}r(\ell).
}\tag{WPG16}
\]
Moreover \(S_{N,k}^{[M]}<S_{N,k}<S_{N,k}^{[M]}+16^{-M}d_kr(N+M+1)/15\), where \(d_kr(n)=\sum_{j=0}^k(-1)^j\binom kj r(n+j)>0\) is strictly decreasing in n. Thus **every finite Pascal channel admits an exact rational interval certificate**.

### Two opposite Gamma axes, and the joint scaling

**WPG-07 (PROVED analytic asymptotics).** At \(t\to1\), \(K(t)/(1-t)\to1\). At \(t\to0\), \(K(t)\to1/4\). Endpoint Laplace/Beta asymptotics yield
\[
\boxed{
S_{N,k}\sim\frac{\Gamma(k+2)}{64 N^{k+2}}
\quad(N\to\infty,\ k\text{ fixed}),
}\tag{WPG17}
\]
\[
\boxed{
S_{N,k}\sim\frac{\Gamma(N+1/8)}{32 k^{N+1/8}}
\quad(k\to\infty,\ N\text{ fixed}).
}\tag{WPG18}
\]

For WPG17 set \(t=1-v/(8N)\), apply \(t^{8N}\to e^{-v}\), \(1-t^8\sim v/N\), \(K(t)\sim v/(8N)\), and dominate by an exponential-polynomial majorant; integrate \(\int_0^\infty e^{-v}v^{k+1}dv=\Gamma(k+2)\). For WPG18 substitute \(y=t^8\), write the integrand as \((1/8)y^{N-7/8}(1-y)^k K(y^{1/8})dy\) and compare to the Beta function \(B(N+1/8,k+1)\) with \(K(0)=1/4\).

For every fixed \(\lambda>0\), the *joint regime* \(k=\lfloor\lambda N\rfloor\) has the further **Laplace-principle rate**
\[
\boxed{
\lim_{N\to\infty}\frac1N\log S_{N,\lfloor\lambda N\rfloor}
=\lambda\log\lambda-(1+\lambda)\log(1+\lambda)<0.
}\tag{WPG19}
\]
Indeed in \(y=t^8\), the exponent \(\log y+\lambda\log(1-y)\) has a unique maximum at \(y=(1+\lambda)^{-1}\), where the positive K remains finite. This is a real two-axis source-convolution asymptotic, not a Fourier cancellation estimate.

## 6. Certified convergence of the Pascal observer **to the source carrier**

Let \(\nu(dt)=K(t)dt\), total mass \(x=\pi/16\). Let \(\rho\) be its normalized pushforward under \(y=t^8\in[0,1]\). At truncation M, \(\nu_M(dt)=Q(t)\sum_{\ell=1}^M16^{-\ell}t^{8\ell-8}dt\) is a *positive* measure of rational total mass \(P_M\).

For knowledge level \(m\ge0\), define the explicit **rational finite observer** on \(\{0,1/m,\ldots,1\}\):
\[
\boxed{
p^{[M]}_{m,N}=
\frac{\binom mN S_{N,m-N}^{[M]}}{P_M}>0,
\quad 0\le N\le m,\quad \sum_Np_{m,N}^{[M]}=1.
}\tag{WPG20}
\]
(At \(m=0\), treat its only point as zero.)

**WPG-08 (PROVED source-observer convergence with an explicit rate).** For \(m\ge1\), let \(\rho_{m,M}=\sum_N p_{m,N}^{[M]}\delta_{N/m}\). Then
\[
\boxed{
W_1(\rho_{m,M},\rho)
\le\frac1{2\sqrt m}+
\frac{16^{-M}r(M+1)}{15P_M}.
}\tag{WPG21}
\]

Proof: conditionally on a source parameter \(Y=y\), the binomial probabilities in WPG20 give \(Z_m\sim\operatorname{Bin}(m,y)\), so
\(\mathbb E|Z_m/m-y|\le\sqrt{y(1-y)/m}\le1/(2\sqrt m)\). Coupling \(Z_m/m\) with \(Y\) gives the first W1 bound for the finite normalized source \(\nu_M/P_M\). Since \(\nu-\nu_M\) is positive with mass \(x-P_M=16^{-M}T_M<16^{-M}r(M+1)/15\), the normalized full source is a mixture of the finite source and a tail source. Coupling their pushforwards on [0,1] costs at most \((x-P_M)/x<16^{-M}r(M+1)/(15P_M)\). Add the costs.

Thus the tower built from *actual source impulses* converges to its analytic carrier, with a source-authenticated finite-error certificate. It does not claim that the source variable \(Y=t^8\) is the **π digit phase** \(16^n x\bmod1\).

Two exact finite Bernstein controls:
\[
\sum_N p^{[M]}_{m,N}\frac Nm
=\frac{S_{1,0}^{[M]}}{P_M},\quad
\sum_N p^{[M]}_{m,N}\left(\frac Nm\right)^2
=\frac{S_{2,0}^{[M]}}{P_M}
+\frac{S_{1,0}^{[M]}-S_{2,0}^{[M]}}{mP_M}.
\]
Both are checked by Fraction arithmetic.

## 7. Hostile division: the source-to-orbit bridge remains OPEN

Take the *different*, strictly positive Mellin kernel already constructed in SUCC's [ordinal observer crucible](ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md),
\[
K_{\rm lock}(t)=(1-t)(1+\tfrac32(1-t)),\qquad\int_0^1K_{\rm lock}(t)dt=1.
\]
Its source-zero forcing \(\tilde r(n)=\int_0^1t^{8n-8}(16-t^8)K_{\rm lock}(t)dt\) is positive, strictly decreasing, and matches the original leading \(15/(64n^2)\) profile. Its completed radix-16 orbit is **exactly locked**, so every orbit wavelet detail is zero and its Haar energy remains \(C_{\rm atom}\).

Yet \(K_{\rm lock}\) also gives positive S_{N,k}, **the identical Pascal conservation law**, convergence of its binomial observer tower, and the same fixed-k time-axis Gamma coefficient WPG17 because \(K_{\rm lock}(t)/(1-t)\to1\).

The high-filter-order axis *does* resolve the sources: \(K_{\rm lock}(0)=5/2\), while \(K(0)=1/4\); hence the analogue of WPG18 for the locked source has coefficient \(5\Gamma(N+1/8)/16\), **ten times** the original source's coefficient. That is a genuine source-discriminating observable in the higher knowledge plane, but a known difference of analytic source profiles is **not yet an inequality about original integer winding**.

A second no-go is exact for EVERY orbit under \(T(\theta)=16\theta\): its N-clock empirical measure is nearly invariant under one T step because
\[
T_*\mu_{a,N}-\mu_{a,N}
=\frac1N(\delta_{\theta_{a+N}}-\delta_{\theta_a}).
\]
Filtered through L, the difference has \(L^\infty\) norm at most
\[
\boxed{\frac{2\|L\|_\infty}{N}=\frac{64}{289N}.}\tag{WPG22}
\]
This tends to zero for a **locked orbit as well**. Approximate T-invariance, positive source-tail impulses and repeated finite knowledge-volume lifts do not select Haar among the many T-invariant measures.

### What a winning π normality proof would have to establish

Use the original **literal four-pole BBP source, zero homogeneous seed, prime/cofactor chronology and actual integer carries** to prove that the wavelet detail budget in WPG10 **saturates C_atom across all large horizons**, not merely that all individual details are nonnegative.

A credible source-authenticated bridge could consist of a *new* signed cross-correlation between the **Pascal/Gamma source-time impulse channels** S_{N,k} (especially the joint \(k\asymp N\) regime where the probe is not a trivial constant weight) and the **actual integer winding/phase block contrast** \(\mathfrak D_{a,N}\), with a source-derived lower estimate across a dense enough sequence of horizons to invoke WPG12. It must falsify the matched locked-source, same-forcing tuned locked seed, sparse Kempner cold-shell and arbitrary source-blind seed controls. No such signed inequality has yet been derived.

A verified result \(\mathcal V_N\to0\) for the original zero-seeded π orbit would establish full base-16 π normality by the already-proved Borwein Fourier-completeness and Weyl criterion. **The exact positive Fejér floor, complete Pascal tower, entire Gamma completion and source-carrier W1 convergence do not imply this missing limit.**

## 8. Execution provenance, ledger and next falsifier

| Claim | Status | Scope |
|---|---|---|
| WPG-01/02 | **PROVED / CLASSICAL** | Universal finite atomic Borwein noise floor of sharp order N^-4 |
| WPG-03 | **PROVED / CLASSICAL** | Exact block interference/16^N harmonic transport, rational common-terminal certificate and source-tail stability |
| WPG-04/05 | **PROVED / CLASSICAL** | Exact finite Haar-wavelet variance budget and dense-horizon interpolation |
| WPG-06 | **PROVED / SOURCE-TYPED** | Complete monotonicity of the original tail and exact positive Pascal conservation at all observer depths |
| WPG-07 | **PROVED / CLASSICAL SOURCE ASYMPTOTICS** | Two Gamma axes and joint large-deviation rate |
| WPG-08 | **PROVED / CLASSICAL SOURCE CONVERGENCE** | Fully rational finite Pascal observers converge in W1 to authentic normalized BBP Mellin carrier with stated rate |
| WPG-09 | **OBSERVED EXACT FINITE** | Source rational block-variance/wavelet audits, source-tail interval bounds, independent autocorrelation equality, and Pascal/binomial mass and moment controls |
| WPG-10 | **REFUTED general implication** | Null seed + positive Gamma/Pascal hierarchy + complete analytic observer limit does NOT force circle equidistribution |
| BBP all-mode \(\mathcal V_N\to0\) | **UNVERIFIED / OPEN** | Requires a new signed source/carry/phase mixing inequality; RH also remains OPEN |

**Local execution:** [scale kernel module](../../../observational_succ/borwein_scale_renormalization.py), [tail/Gamma/Pascal module](../../../observational_succ/bbp_tail_impulse.py); [scale tests](../../../tests/test_borwein_scale_renormalization.py), [Pascal tests](../../../tests/test_bbp_tail_impulse.py); [validation dossier](BORWEIN_WAVELET_PASCAL_GAMMA_VALIDATION.md). The exact combined scoped local suite was 53/53 passes (29 new, 24 inherited) before committing. No full repository/Lean/hosted final-head gate is asserted.

**References/provenance:** SUCC original four-pole BBP source and null section, [impulse/Mellin identity](BBP_IMPULSE_MELLIN_FILTER.md), [ordinal Mellin/Gamma tower](ORDINAL_MELLIN_GAMMA_OBSERVER_ASCENT.md), [source-typed rational Borwein full-mode criterion](BORWEIN_SWEPT_IMPULSE_BBP.md), [quantitative kernel energy](BORWEIN_QUANTITATIVE_KERNEL_BRIDGE.md), [original terminal source norm](../../2026-11-16/defect_window_tomography/ENDPOINT_COERCIVITY_REPORT.md), and classical Fejér, Hilbert-ANOVA, Hausdorff moment/Bernstein approximation and Laplace principles. All source-dependent identities share the original BBP coefficients rather than independent origin witnesses.
