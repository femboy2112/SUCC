# Operation Selected Boundary: real/adic cross-character saturation and a testable π gate

**2026-10-27 · research-only child of [#323](https://github.com/femboy2112/SUCC/pull/323).** Parents #319→#320→#321→#322→#323 are preserved. All source originals, U0=0, archives and main are immutable. **π normality and RH OPEN.** Paper-proved claims below are not external novelty or Lean-kernel claims.

## Authentic source and missing assertion

Let r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2), U0=0, U_n=16U_(n−1)+r(n). Inherited from #323, with T_n=Σ_(j≥1)16^(−j)r(n+j)>0 and T_n<1/[15(n+1)^2] for n≥1,

$$
U_n=16^{n-1}\pi-T_n,\quad B=\sum_{n\ge1}T_n=(R-\pi)/15=0.0162969977338265\ldots
$$

where R=Σ_(n≥1)r(n)=π/4+5√2π/16+5log(2)/8+5√2log(1+√2)/8. The exact original-source Weyl requirement remains

$$
\forall h\in\mathbb Z\setminus\{0\}:\quad S_N(h)=\sum_{n=1}^N e(hU_n)=o(N),\quad e(x)=\exp(2\pi ix).
$$

The inherited #319 result is only |S_N(h)|≤N−(log_8 N)/14+O_h(1), not normality.

## SB-1. Nonlinear cylinder transfer (PAPER-PROVED)

For any N, any finite possibly moving list of nonnegative delays ell_j, define real-circle coordinates X_(n,j)={U_(n+ell_j)} and Y_(n,j)={16^(n+ell_j−1)π}. Let f_(n,N) be coordinatewise Lipschitz for geodesic circle metric with constants L_(j,N), uniformly in n, and |w_(n,N)|≤1. The f's may depend on n, fixed adic/CRT labels, and the experiment; the **same f** must be used on X and Y. Then

$$
\boxed{\left|\sum_{n=1}^{N}w_{n,N}\left[f_{n,N}(X_n)-f_{n,N}(Y_n)\right]\right|\le B\sum_jL_{j,N}.}
$$

Proof: circle distance of the jth coordinates ≤T_(n+ell_j); apply the coordinatewise Lipschitz bound and sum over n, with Σ_(n≥1)T_(n+ell_j)≤B. This permits any nonlinear/smooth observable, arbitrary sparse large lags, moving packet sizes, and time-label selection. If total Lipschitz budget=o(N), normalized observables have the same limits on U and completed π, **not automatically Haar**. Real digit/carry cut indicators are discontinuous and excluded; growing budgets must be kept.

For character f=e(Σ_j h_jx_j) get 2πBΣ|h_j|, reproducing #323 by a different circle-metric argument. Under normality, the fixed-lag Haar target is the pushforward x↦({16^ell_1 x},...), **not product Haar**. In particular

$$
\int_0^1 e\left(x\sum_jh_j16^{\ell_j}\right)\,dx
=\begin{cases}1,&\sum_jh_j16^{\ell_j}=0,\\0,&\text{otherwise}.\end{cases}
$$

The annihilator E−16 has Haar target **one**: e(U_(n+1)−16U_n)=e(r(n+1))→1. It must NOT be tested against independent uniform coordinates.

## SB-2. Exact real digit seam and authentic generic expectation (PAPER-PROVED)

For n≥1, define y_n(α)={16^(n−1)α} and x_n(α)={16^(n−1)α−T_n}; D(x)=floor(16{x}). Since 0<T_n<1/16,

$$
\boxed{D(x_n(\alpha))\ne D(y_n(\alpha))\iff
y_n(\alpha)\in\bigcup_{a=0}^{15}[a/16,a/16+T_n)\pmod1.}
$$

This is a **selected π carry criterion** when α=π. For uniform Haar α, every y_n is individually Haar, without time independence. By Tonelli,

$$
\boxed{\mathbb E_\alpha\,\#\{n\ge1:D(x_n(\alpha))\ne D(y_n(\alpha))\}
=16B\approx0.2607519637412.}
$$

Therefore the digit mismatches are almost surely finite, and P(no mismatch ever)≥1−16B≈0.739248. **This is generic-in-seed, NOT a bound for the fixed seed α=π.** The hostile changed-seed α=0 gives y_n=0 and x_n=1−T_n, hence a mismatch at every n despite ΣT_n<∞. Never promote phase L¹ transport to a selected discontinuous digit/carry count.

## SB-3. Original finite CRT Plancherel identity (PAPER-PROVED conditional on inherited #321–#322)

Put A2=16^k, A3=3^L, M=A2*A3. Under the upstream all-time source isometry and CRT theorem, the labels a_n=[U_n]_(A2), b_n=(120n²−89n+16) mod A3 identify n modulo M bijectively, for n≥0. The b-label is the *cleared 3-adic numerator*, not a 3-adic U-state. For arbitrary complex z_n and

$$
W_N(u,v)=\sum_{n=0}^{N-1}z_n e(ua_n/A2+vb_n/A3),
$$

finite character orthogonality (expand the square; equal labels iff n≡m mod M) yields

$$
\boxed{\sum_{u<A2}\sum_{v<A3}|W_N(u,v)|^2
=M\sum_{t=0}^{M-1}\left|\sum_{\substack{0\le n<N\\n\equiv t\pmod M}}z_n\right|^2.}
$$

Set z_n=e(hU_n) only after this exact identity. Define the **UNPROVED sufficient criterion**

$$
\mathcal E_{N,M}(h):=\frac M{N^2}\sum_{t<M}\left|\sum_{\substack{0\le n<N\\n\equiv t\pmod M}}e(hU_n)\right|^2\longrightarrow0
$$

for every fixed h≠0, along an admissible M=M(N)=16^k3^L=o(N), including any fixed M. By Cauchy–Schwarz |Σ_(0≤n<N)e(hU_n)|²/N²≤mathcal E, hence it would prove π normality. **No estimate of this type is proved here.** For coherent z_n=1 and N multiple M, mathcal E=1 and only the trivial CRT character survives: finite arithmetic character orthogonality does not imply real Weyl cancellation.

## SB-4. Every finite real Fourier band has an explicit nonnormal counterfeit (PAPER-PROVED)

Given any H≥1, take an odd q>H. Let D_k(j/q) be the first k hexadecimal digits of the rational j/q by ordinary long division. Form an explicit real α_q whose hexadecimal digits concatenate, for k=1,2,..., the q blocks

D_k(0/q), D_k(1/q), ..., D_k((q−1)/q).

This α_q is generic for μ_q=(1/q)Σ_(j=0)^(q−1)δ_(j/q), because multiplication by 16^t permutes j modulo q for every t (gcd(16,q)=1). Every complete stage has exactly the average μ_q(f) under the corresponding ideal rational orbits; excluding the last w digits of each block makes orbit error ≤16^(−w), and the excluded proportion through stage K is at most 2w/(K+1). An incomplete stage is O(1/K) of the preceding total. Uniform continuity proves weak convergence to μ_q.

By the exact qth-root sum,

$$
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}e(h16^n\alpha_q)
=\frac1q\sum_{j=0}^{q-1}e(hj/q)=
\begin{cases}1,&q\mid h,\\0,&q\nmid h.\end{cases}
$$

Thus **all modes 1≤|h|≤H vanish in the limit**, but mode q is maximally non-Haar. The q=17 control fools modes 1,...,16 and fails mode 17. This is an arithmetic/dynamical countermodel, **NOT the original BBP forcing**; it refutes a finite-frequency-to-normality shortcut unless a separate source-rigidity theorem is established.

## Actual frontier / scope / handoffs

**PROVED on paper:** SB-1, SB-2, SB-3 under the inherited #321–#322 CRT theorem, SB-4. **Locally corroborated independently:** seven exact-focused stdlib tests against the original four signed poles, rational Green identities, nonlinear character bound, CRT 16×3 orthogonality, real-cut crossing, and q=17 mutation; separate local scripts exist, not a native/hosted SUCC validation claim. **OPEN:** a source-specific signed arithmetic estimate proving S_N(h)=o(N), or the above conditional CRT energy criterion. **REFUTED:** the inference from smooth echo observables, real phase L¹ transport, 2-adic CRT orthogonality, generic a.e. digit counts, or any finite character band to selected π normality.

Next discriminate the true four-pole/U0=0 source against #320's strongly 2-adic-isometric **nonnormal** mutant, changed-seed −T_n, and the new q-grid Fourier counterfeit. Quantify h,k,L,N, time windows, seam errors and all moving coefficients. No merge, source rewrite, claim promotion or Lean authority is authorized.

Related: [#319](https://github.com/femboy2112/SUCC/pull/319), [#320](https://github.com/femboy2112/SUCC/pull/320), [#321](https://github.com/femboy2112/SUCC/pull/321), [#322](https://github.com/femboy2112/SUCC/pull/322), [#323](https://github.com/femboy2112/SUCC/pull/323); Bailey–Crandall (2001) https://doi.org/10.1080/10586458.2001.10504441; Lagarias (2001) https://arxiv.org/abs/math/0101055.
