# Original-source BBP edge measure, exact seed tomography, and a 73-point cyclic plane

**2026-10-31. Research only.** This paper is additive to SUCC Main XVII `e8598cfa5d32fd1de8e94a3e458a366a0850d59e` and CRPM draft PR #431 (`cf23b8cfc39f56935c432ed764adf0a33efb0d7e`). No claim that π is normal, that a positive measure creates signed cancellation, or that the statements have been Lean-kernel checked. Most mathematical ingredients are classical; the original-source typed synthesis and finite receipts are new to this branch, not claimed as academic priority.

## 0. Exact objects, quantifiers, and observer firewall

Use **only the original** four signed BBP poles:

\[
 r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
 U_0(s)=s,\quad U_{n+1}(s)=16U_n(s)+r(n+1).
\]

The **authentic** orbit has `s=0`; all changed-seed experiments are labeled **counterfactual**, not alternative readings of π. Write `e(t)=exp(2πit)` and let `x_n={U_n(0)}`. The selected Fourier gate is `S_N(h)=sum_(1<=n<=N) e(h U_n(0))=o(N)` for each **fixed** nonzero integer `h`. This is equivalent to base-16 normality of π by SUCC's existing O_h(1) genuine Green-tail comparison; equivalence is not a proof of either.

Declare three separately typed constructions:

* **Realized edge observable:** `d_n=U_(n+1)(0)-U_n(0)`, and its empirical circle measure `ν_N=N^-1 sum δ_{ {d_n} }`.
* **Counterfactual seed response:** `F_(N,h)(s)=sum_(n=1)^N z_n e(h 16^n s)` with source-authenticated `z_n=e(h U_n(0))`. This is a virtual family of *different initial conditions*, not a probability law on the actual π orbit.
* **Finite sample instrument:** for prime `p`, evaluate `I_(N,h)(j/p)=|F_(N,h)(j/p)|²`, `j∈Z/p`. Phase ratios are represented exactly by rational classes `h(U_n-U_m) mod 1`, never by an invented q-Pascal phase. A finite prime sampling modulus is **not** an arithmetic p-adic place.

## ESM-01. Exact successor-edge phase transport (PROVED LOCAL)

For every `n>=1` and every seed `s`, subtract the recurrence:

\[
\boxed{U_{n+1}(s)-U_n(s)=15U_n(s)+r(n+1).}\tag{E1}
\]

The source forcing admits the positive archimedean representation

\[
 r(n)=\int_0^1 t^{8n-8}P(t)\,dt,\quad
 P(t)=4-2t^3-t^4-t^5=(1-t)(t^2+2)(t^2+2t+2).
\]

`0<P(t)<=15(1-t)` for `0<t<1`, hence for `n>=1`,

\[
0<r(n+1)<\frac{15}{(8n+1)(8n+2)}<\frac{15}{64n²}.
\]

Therefore `sum_(n>=1) r(n+1)<(15/64)ζ(2)<15/32`, using elementary `sum 1/n²<2`. Let `E_N(h)=sum_(n=1)^N e(h d_n)` and `S_N(15h)=sum e(15h U_n(0))`. The pointwise inequality `|e(t+v)-e(t)|<=2π dist(v,Z)<=2π|v|` proves the **all-N** estimate

\[
\boxed{|E_N(h)-S_N(15h)|\le 2π\sum_{n=1}^N\operatorname{dist}(h r(n+1),\mathbb Z)
\le 2π|h|\sum_{n=1}^N r(n+1)<\frac{15π}{16}|h|.}\tag{E2}
\]

The tighter rational sum of circle distances is computed by the module. This source estimate is uniform in horizon but **does not bound** either signed sum on the right at sublinear scale.

## ESM-02. An invariant non-injective cover reflects Haar (CLASSICAL, complete elementary proof)

Let `b>=2`, `k>=1` be integers. Write `T_b(x)=b x mod1`, `M_k(x)=k x mod1`, and λ for Haar/Lebesgue measure on the circle. **For every T_b-invariant Borel probability μ:**

\[
\boxed{(M_k)_*\mu=\lambda \quad\Longleftrightarrow\quad \mu=\lambda.}\tag{E3}
\]

The reverse implication is immediate. For the forward direction, let `K` be any compact set. Since `K⊆M_k^{-1}(M_k K)`,

`μ(K)<= (M_k)_*μ(M_k K)=λ(M_k K)<=k λ(K)`.

The last bound is the Lipschitz image-length inequality for the k-fold covering (on finitely many arcs); regularity then yields `μ<=k λ`. Therefore `dμ=f dλ` for a bounded `0<=f<=k`. Since μ is `T_b` invariant, `hat μ(m)=hat μ(b^j m)` for all integers `m` and `j>=0`. For every `m!=0`, the Riemann–Lebesgue lemma applied to `f∈L¹` gives `hat μ(b^j m)->0`, hence `hat μ(m)=0`. The only probability with all nonzero Fourier coefficients zero is λ. **No injectivity of M_k was assumed.**

**Sharp scope:** the invariance hypothesis is essential. The non-Haar probability with positive density `f(x)=1+cos(2πx)` satisfies `(M_15)_*(f λ)=λ`, because its only nonzero Fourier frequencies are `±1`, not multiples of 15. But it is not `T_16` invariant. This is a calibrated false positive against a static covering-map shortcut.

**Strengthening (CLASSICAL):** every `T_b`-invariant probability has the unique Lebesgue decomposition `μ=t λ+(1-t)σ`, where `σ` is singular and T_b-invariant. Finite integer multiplication maps λ-null sets to λ-null sets and preserves λ. Thus for the convention `TV(μ,λ)=sup_A|μ(A)-λ(A)|`,

\[
\boxed{\operatorname{TV}(\mu,\lambda)=\operatorname{TV}((M_k)_*\mu,\lambda)=1-t.}\tag{E4}
\]

Proof of decomposition: `T_b` pushes an absolutely continuous measure to another absolutely continuous measure, and pushes a singular measure to a singular measure because `T_b` is piecewise Lipschitz; uniqueness of Lebesgue decomposition makes both parts invariant. Invariance and the Fourier proof above (or standard uniqueness of the acim) make the AC component `tλ`. `M_k` preserves these types. This is an **invariant-measure-only TV identity**. Every finite empirical atomic measure is TV-distance one from λ; do not misuse E4 as a finite discrepancy estimate.

## ESM-03. Selected edge increment normality is equivalent to π base-16 normality (PROVED LOCAL + classical Weyl/Wall)

Let `μ_N=N^-1 sum_(n=1)^N δ_(x_n)`, `ν_N=N^-1 sum δ_({U_(n+1)-U_n})`. The circle recurrence is `x_(n+1)=T_16 x_n + r(n+1) mod1`. For every Lipschitz circle test `f`,

\[
\left|\int f\,d\mu_N-\int f\circ T_{16}\,d\mu_N\right|
\le\frac{2\|f\|_\infty+\mathrm{Lip}(f)\sum_{n=1}^N r(n+1)}{N},\tag{E5}
\]

and

\[
\left|\int f\,d\nu_N-\int f\circ M_{15}\,d\mu_N\right|
\le\frac{\mathrm{Lip}(f)\sum_{n=1}^N r(n+1)}{N}.\tag{E6}
\]

Both follow by telescoping and E1, respectively. Their errors tend to zero (uniformly O_f(1/N)), so every weak-* limit μ of `μ_N` is `T_16` invariant, and along the same subsequence `ν_N` converges to `(M_15)_*μ`. Compactness of circle probability measures + E3 now implies

\[
\boxed{\mu_N\Rightarrow\lambda\quad\Longleftrightarrow\quad\nu_N\Rightarrow\lambda.}\tag{E7}
\]

If the edge sequence were not Haar, an orbit limit would witness the failure; if it were Haar, each orbit limit has Haar pushforward and must itself be Haar. Weyl's criterion and the established exact π source-tail bridge give the alternative **necessary and sufficient** target

\[
\boxed{\pi\text{ is base-16 normal}\quad\Longleftrightarrow\quad
 \forall h\in\mathbb Z\setminus\{0\}:\ E_N(h)=o(N).}\tag{E8}
\]

This is an authentic **edge-/difference-measure realization** of the author's path measure intuition. It is not a signed estimate on E_N. The fact that rational multiplication preserves base-b normality is classical (Wall); E3-E8 give an independent measure proof, and E1-E2 pay the exact original-source forcing cost. The factor 15=3·5 suggests a well-typed interface with SUCC's independent 3-adic pole-depth and prime-clock studies, but p-adic Haar must not be silently promoted to real-circle Haar.

## ESM-04. Source-phase tomography from the *full* counterfactual intensity (CLASSICAL / PROVED LOCAL)

Fix `h!=0`, `N>=2`, and `z_n=e(hU_n(0))`. For a virtual seed `s`,

\[
F_{N,h}(s)=\sum_{n=1}^N z_n e(h16^n s),\quad
I_{N,h}(s)=|F_{N,h}(s)|^2.
\]

Expanding the full off-diagonal interference gives

\[
\boxed{I_{N,h}(s)=N+\sum_{n\ne m}z_n\bar z_m\,e\big(h(16^n-16^m)s\big).}\tag{E9}
\]

If `n>m`, `16^n-16^m=16^m(16^(n-m)-1)`, and the second factor is `-1 mod 16`. Thus the maximal power of 16 dividing the difference is exactly `16^m`, which determines m; division then determines n. The negative sign determines orientation. Therefore the `N(N-1)` nonzero integer frequencies are **pairwise distinct**. In the continuous Fourier transform of I, each such spectral coefficient is exactly `z_n bar z_m`. All phase ratios can be reconstructed up to the unavoidable single global phase. The **mean alone** `int_0^1 I(s) ds=N` erases every off-diagonal; the complete response retains them.

The map `z -> I` is a known mathematical counterfactual response, NOT a physical measurement instrument performed on the actual source. Moreover reconstructing phases does not prove that the sum at the distinguished real seed `s=0` cancels.

## ESM-05. A minimal 73-channel alias-free radix-16 projective plane (CLASSICAL difference-set theory; exact independent finite proof)

For `N=9, h=1`, take sampling prime `p=73` and

\[
D=\{16^n\bmod73:1\le n\le9\}=\{1,2,4,8,16,32,37,55,64\}.
\]

An exact exhaustive residue certificate independently verifies

\[
\boxed{\{(d_i-d_j)\bmod73:i\ne j\}=\{1,2,\ldots,72\}\quad\text{with multiplicity one}.}\tag{E10}
\]

Here `73=8²+8+1=Φ₃(8)=(2^9−1)/(2^3−1)`, while `2^9=512≡1 (mod 73)` and `16=2^4` has the same order-nine subgroup as 2 because `gcd(4,9)=1`. This explains the radix-2/radix-16 compatibility of the nine-point orbit. Thus D is a cyclic `(73,9,1)` planar difference set. The 73 translates `a+D` are 73 lines, each of size 9, and each pair of distinct points belongs to exactly one line: for `x-y ≠ 0`, the unique ordered difference `d_i-d_j=x-y` determines the unique translation `a=x-d_i`. Symmetrically any two lines meet once. This constructs a finite projective plane of order 8. **This finite design is known classically** (the octic residues modulo 73); we claim only the exact SUCC radix16 spectral identification and independent implementation receipt, not discovery of a new finite geometry.

Let `I(j/73)` for `0<=j<73` denote the 73 virtual-seed intensities. Finite Fourier orthogonality implies

\[
\boxed{\frac1{73}\sum_{j=0}^{72}I(j/73)e\left(-\frac{qj}{73}\right)
=\begin{cases}
9,&q=0,\\z_n\bar z_m,&q\equiv16^n-16^m\pmod{73},\quad n\ne m.
\end{cases}}\tag{E11}
\]

**Exact fourth-order cubature (additional classical consequence).** Any finite modulus p for which the off-diagonal differences and 0 are pairwise distinct automatically has no nontrivial collision of two-sums `16^a+16^b ≡ 16^c+16^d (mod p)` other than equality of the two multisets. Otherwise rearranging the two-sum equality would give a collision of off-diagonal difference labels or a forbidden zero label. Thus for *every* choice of unit-modulus source phases `z_n`, the **finite** p-grid reproduces the exact continuum second and fourth moments:

\[
\boxed{\frac1p\sum_{j=0}^{p-1}|F_{N,h}(j/p)|^2=N,\qquad
\frac1p\sum_{j=0}^{p-1}|F_{N,h}(j/p)|^4=2N^2-N.}\tag{E11a}
\]

At N=9,p=73 the values are 9 and 153, independently of z. This is exact **restricted degree-four Fourier cubature**, not a universal quadrature rule for arbitrary functions and not selected-seed cancellation. The independent integer group-ring oracle checks the finite two-sum counts against direct integer quartic counts; an aliased p=17 fails.

All 73 Fourier channels are used, with **no aliasing**. Seventy-three is minimal **for a completely alias-free uniform DFT of all 9×8 off-diagonal plus one diagonal Fourier labels** because fewer than 73 residues cannot hold 73 distinct labels. It is **not** a theorem about minimal nonlinear phase retrieval or the cost of an actual π normality proof. When `73|h`, the particular modulus 73 aliases frequencies and must be rejected.

## ESM-06. Prime sampling instrument exists for *every finite* N and h (CLASSICAL, exact construction)

Let `A={0} ∪ {h(16^n−16^m):1<=n,m<=N,n!=m}`. ESM-04 proves these are distinct integers. The finite list `B={a−a':a,a'∈A,a!=a'}` contains no zero. Any prime p that divides none of the finitely many integers in B makes reduction `A -> Z/p` injective. Such primes exist by Euclid's infinitude of primes (only finitely many primes divide the product of B). Therefore there is an algorithm—enumerate primes and reject collisions—which **terminates for every specified finite N and h**. The module supplies a finite search cap and raises instead of falsely claiming non-existence when that cap is exhausted.

Examples for `h=1`: N=2→p=7; 3→7; 4→19; 5→31; 6→53; 7→73; 8→73; 9→73; 10→283; 11→337; 12→503; 13→643; 14→761. This is not an asymptotic polynomial-cost theorem. The object indexed by p is a **finite Fourier-sampling carrier**, not a genuine independent arithmetic prime place or the original 2-adic clock.

## ESM-07. Universal exact second/fourth moments and a.e. counterfactual normality (CLASSICAL lacunary orthogonality)

For every source twist sequence `|z_n|=1`, every integer `h!=0`, and `N>=1`:

\[
\boxed{\int_0^1 |F_{N,h}(s)|^2 ds=N,\qquad
\int_0^1 |F_{N,h}(s)|^4 ds=2N^2-N.}\tag{E12}
\]

The second moment uses distinct integer frequencies. The fourth moment counts solutions `16^a+16^b=16^c+16^d`. In base16 the digits of the sum cannot carry (there are only two summands), so the multisets `{a,b}` and `{c,d}` must coincide. There are `2N²−N` ordered solutions; each contributing complex coefficient equals 1 since `|z_n|=1`.

Markov's inequality gives

\[
\lambda\{s:|F_{N,h}(s)|\ge\varepsilon N\}
\le\frac{2N^2-N}{\varepsilon^4N^4}=O_{\varepsilon}(N^{-2}).\tag{E13}
\]

Summing over N and applying Borel–Cantelli, then taking the countable intersection over `ε=1/j` and all nonzero integer h, proves `F_(N,h)(s)/N->0` for Lebesgue-a.e. seed `s`, **regardless of the deterministic forcing sequence**. This is a generic-seed theorem, NOT an estimate for the single authentic zero seed `s=0`.

## ESM-08. Exact radix-cylinder conditional fourth moments (CLASSICAL)

Condition the virtual seed on an arbitrary aligned radix-16 cylinder `I_(j,k)=[j/16^k,(j+1)/16^k)`. Put `t=16^k s-j`. For all `n>=max(1,k)`,

`e(h16^n s)=e(h16^(n-k) t)`

with **no j-dependence**. Let `M=N-max(1,k)+1` be the number of tail modes, provided `0<=k<=N`. In the conditional uniform measure on any such cylinder, the tail intensity fourth moment is exactly `2M²−M`, independent of j or original source phases. At most `k-1` early terms remain when k>=1. Thus for `εN>k-1`,

\[
\boxed{\Pr_{s\in I_{j,k}}(|F_{N,h}(s)|\ge\varepsilon N)
\le\frac{2M^2-M}{(\varepsilon N-(k-1))^4}.}\tag{E14}
\]

This is a calibrated **finite-observer precision bound**: for any `k_N=o(N)` the conditional bad-seed mass is `O_ε(N^-2)`, uniformly across the selected cylinder label. It does NOT say the particular selected seed contained in the cylinder is typical, and does not turn changing conditional measures into a false almost-sure result.

## ESM-09. Finite rational coherent counterfeit from original source (PROVED LOCAL)

Let `c=π/16=Σ_(k>=1)16^-k r(k)` and its exact rational prefix `c_K=Σ_(k=1)^K16^-k r(k)`. Let

`T_n=Σ_(j>=1)16^-j r(n+j)`.

Positivity, source bounds and the geometric series yield

\[
0<c-c_K=16^{-K}T_K\le\frac{16^{-K}}{(8K+1)(8K+2)},\qquad
0<T_n<\frac1{(8n+1)(8n+2)}.\tag{E15}
\]

For every `0<=n<=K`, the exact **rational** seed `s_K=-c_K` (not the authentic `s=0`) satisfies

\[
\boxed{U_n(s_K)=-T_n+16^n(c-c_K),\qquad
|U_n(s_K)+T_n|\le\frac{16^{n-K}}{(8K+1)(8K+2)}.}\tag{E16}
\]

Consequently for every `1<=N<=K` and fixed `h!=0`,

\[
\boxed{\left|\sum_{n=1}^N e(hU_n(s_K))-N\right|
\le 2π|h|\left(\frac1{32}+\frac{16}{15(8K+1)(8K+2)}\right).}\tag{E17}
\]

This produces rational hostile seeds with nearly maximal signed coherence at every inspected horizon `N<=K`; using `K=N` produces a **diagonal family**, not one fixed infinite source. The genuine infinite changed seed `s*=-π/16` from PR #431 instead satisfies `U_n(s*)=-T_n` and has `S_N(h;s*)/N->1` for each fixed h. Therefore any theorem built only from averaged seed measurements, source forcing or finite source-prefix coincidences is insufficient to certify the exact selected seed.

## ESM-10. Quantitative seed-localization weakness (CLASSICAL)

For any real seeds s,t and each fixed h,

\[
\boxed{|F_{N,h}(s)-F_{N,h}(t)|
\le 2π|h|\frac{16^{N+1}-16}{15}|s-t|.}\tag{E18}
\]

If `|F_N(0)|>=εN`, this Lipschitz inequality only forces comparable amplitude within a neighborhood of radius on the order of `N16^-N` around s=0. That neighborhood is exponentially small even though the a.e. exceptional-set bound in E13 is O(N^-2). **There is no contradiction.** This comparison shows why E12/E13 alone cannot select the authentic seed; it does not claim a universal exponential lower bound for every conceivable source-specific method.

## Verdict / the actual theorem gap ESM-11 (OPEN)

ESM-03 supplies a legitimate *difference-path* equivalent π gate: prove `E_N(h)=o(N)` for each fixed nonzero h, from **original** signed four-pole forcing and exact `U_0=0`. ESM-05/06 supply an exact finite instrument that preserves every source phase ratio, but each finite-N reconstruction leaves the global sum unconstrained. ESM-07/08 supply very strong counterfactual almost-everywhere laws, yet ESM-09 shows the authentic seed cannot be inferred from this ensemble. The **only missing mathematical claim** remains an all-horizon source-selected signed estimate. A new infinite theorem must survive `s*=-c` and the rational diagonal family `s_K=-c_K`, not merely a numerical holdout. No RH consequence is claimed.

### Provenance and comparison

- SUCC official source/frontier: `docs/PI_SELECTED_CATEGORICAL_FRONTIER.md` (Main XVII); original source, BBP tail and Fourier transport. Main's raw frequency ladder is already known to be a time shift; ESM-02/03 are an **alternative target formulation**, not an upgrade of the old ladder.
- Parent path measure: draft PR #431 `research/2026-10-31/carrier_path_measure/PROOFS.md`, particularly CRPM-05/06/07.
- Continuous triangle/selected Ward: PR #426 `research/2026-10-31/counterfactual_triangle/PROOF.md` (the source invariance estimate is adjacent to CT-05, not a wholly new phenomenon).
- Three-place pole depth: PR #430, `research/2026-10-31/multiplace_bbp_difference/NEXT.md`. Prime local estimates are not substitutes for original real-circle signed estimates.
- Wall's established rational-multiplication normality: Airey–Jackson–Mance, *Descriptive Complexity in Cantor Series*, Journal of Symbolic Logic, https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/descriptive-complexity-in-cantor-series/19EAD3B2B426D3826A6DA9405DFB7D81 (Theorems 1.2/1.3), and https://arxiv.org/abs/2609.24665 .
- Finite cyclic plane order eight / octic residues (73,9,1): https://www.static.imaginary.org/ko/node/1183 and https://personal.ntu.edu.sg/bernhard/Publications/pub/Singer.pdf . This design is **known classical mathematics**; our original-source phase instrument is the new SUCC use.
- Lacunary fourth-moment context: https://link.springer.com/article/10.1007/s00440-025-01405-5 . We provide the elementary exact b=16 proof and do not rely on an unverified general lacunary moment identity.

### Reproducibility and proof authority

The local package contains exact `Fraction` source states, modular integer Fourier labels, a brute-force independent collision oracle, an independent finite projective-plane incidence check, and root-discoverable regression tests. A float-based finite diagnostic is segregated as **FINITE_DIAGNOSTIC_ONLY** and cannot certify an asymptotic statement. No repo-wide CI, Lean kernel, independent referee, physical measurement, or π-normality proof is claimed by local tests.
