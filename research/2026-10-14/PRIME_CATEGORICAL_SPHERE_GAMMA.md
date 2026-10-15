# PRIME CATEGORICAL SPHERE — source-faithful Pascal / Gamma chiral gluing

**Date:** 2026-10-14 (New York); maintainer hypothesis: a common origin, a family of prime-correlated SUCC ladders of different unit lengths and path geometries, and a lawful global/Archimedean boundary with genuine dynamics *between* the ladders. **Branch:** `research/prime-categorical-sphere-gamma-sieve-2026-10-14`. **Exact parent:** `femboy2112/SUCC@5a3f5cf4d415266b3c647e1eab3326acb04d3cbd`, Pascal-quarter-turn PR #66. Parent also descends from Suzuki Wavefront PR #64 (`a10d994`), zero-centered SUCC PR #59, and the main SUCC carrier/no-ghost theory. **RH PROVED: no.** The novel-to-project assembly is not a claim of scholarly priority, independent external physical authentication, an actual adelic sphere, or Weil positivity.

**Author's conjectural picture** is a *categorical sphere* whose paths share an origin and a global endpoint, with finite prime-correlated ladders forming patches and with a lawful process for gluing local observations. **Our mathematically repaired model** has: (a) an actual integer Pascal carrier with place-valued source observables; (b) an actual Suzuki spectral-mode set and derived prime-indexed transports; (c) a four-phase simplicial S² *toy nerve* and a degree character; (d) a genuine positive signed chiral Gamma operator and source-derived Euler character. These are separate explicitly typed objects. No equivalence between them is silently assumed.

**Primary external mathematical source:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, [arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), especially eqs (1.3), (2.5), (8.2)/(8.7). Classical Kummer carry theorem, Euler product for Dirichlet L-functions, reflection formula for Gamma, Fourier transform of sech, and Fourier positivity of OU resolvent kernels are imports. See the parent [Pascal-quarter-turn dossier](PASCAL_QUARTER_TURN_GAMMA.md) and [Suzuki source dossier](../2026-10-13/SUZUKI_SOURCE_WAVEFRONT_ROUND_001.md). No nontrivial zeros supplied to any construction.

## PS-01 — prime-local Pascal vertices are authentic and determine their real magnitude (CLASSICAL, PROVED LOCAL)

Put `c(n,k)=binom(n,k)>0`, `0<=k<=n`. A Pascal edge merges two predecessors by *integer addition*, not multiplication. For every actual prime `p`, Kummer's theorem says

\[
 v_p(c(n,k))=\operatorname{Carr}_p(k,n-k).
\]

Because all prime factors of `c(n,k)` are at most `n`, the source-typed value can be reconstructed from the **finite** local observations at the real mathematical Pascal vertex:

\[
 \boxed{c(n,k)=\prod_{p\le n}p^{\operatorname{Carr}_p(k,n-k)},\qquad
 \log c(n,k)=\sum_{p\le n}\operatorname{Carr}_p(k,n-k)\log p.}\tag{PS1}
\]

For the probability-normalized binomial source `w(n,k)=2^-n c(n,k)`, the prime valuations are **not** unchanged:

\[
 \boxed{v_p(w(n,k))=\operatorname{Carr}_p(k,n-k)-n\mathbf1_{p=2},\qquad
 \log w(n,k)=\sum_p v_p(w(n,k))\log p.}\tag{PS1b}
\]

These are exact, source-dependent product-formula statements, NOT an infinite simultaneous observation or a uniquely defined physical carrier. Example `c(6,3)=20`, `v2=2`, `v5=1`; normalized probability `20/64=5/16` has `v2=-4`, `v5=1`, illustrating the **dyadic normalization defect**. Compare PG-05's real Gaussian weak limit; the normalization `2^-n` has 2-adic norm `2^n`, so the Gaussian weak limit cannot be transported to all finite places for free.

**Proof:** Legendre's factorial-valuation formula gives Kummer's carry identity. Unique factorization gives the product and logarithmic equality. Subtracting `n*v_p(2)` gives PS1b. All are finite integer equalities at each `(n,k)`. Implementation factorizes binomial integers through actual primes and independently counts carries, checking every row up to 33 and middle `binom(256,128)`.

## PS-02 — local valuation is NOT a sufficient Pascal-addition observer (PROVED LOCAL, classical p-adic cancellation)

The Pascal recursion is `c(n,k)=c(n-1,k-1)+c(n-1,k)`. For any `p`,

\[
 v_p(x+y)\ge\min(v_p(x),v_p(y)),
\]

with equality if the parent valuations differ, but strict inequality may occur when they agree. In row 2: `1+1=2`; at p=2 both parents have valuation zero, but the child valuation is one. **An observer retaining only p-adic valuations loses the residue phases necessary to propagate SUCC's intrinsic addition.**

The failure persists at arbitrary fixed precision: for every actual prime `p` and integer `r>=1`, the pairs `(1,p^r-1)` and `(1,p^(r+1)-1)` give **identical parent values modulo `p^r`**, but their sums have valuations `r` and `r+1`. Thus no fixed finite truncation can certify all future addition-cancellation orders without either more source data or a justified global arithmetic recurrence. This is not a statement that the original source's exact labels, if independently available, are unknowable. It is an instrument-relative no-go on truncated local data.

## PS-03 — the **actual Suzuki Gamma ladder** forces prime-dependent chart transitions (PROVED LOCAL)

The parent branch proves that the **positive OU bath** in Suzuki's completed real-place kernel is

\[
 B_{+,a}=\sum_{j\ge0}\alpha_j^{-2}P_aR_{\alpha_j}P_a,\quad
 \alpha_j=2j+\tfrac12=\tfrac{4j+1}{2},\quad
 R_\alpha(x,y)=e^{-\alpha|x-y|},
\]

where `P_a` is the mean-zero projection on `(-a,a)`. We distinguish the original source chart (`n=4j+1`), its derived companion chart (`n=4j+3`), and dyadic conductor levels. Every positive integer mode label has unique coordinates

\[
 \boxed{n=2^e(4j+r),\quad e\ge0,\ r\in\{1,3\},\ j\ge0,\qquad \alpha=\frac n2.}\tag{PS3}
\]

For any *authentic prime* p, multiplication sends this chart to

\[
 (e,r,j)\stackrel{p}{\longmapsto}
 \begin{cases}
 (e+1,r,j),&p=2,\\
 (e,pr\bmod4,\;pj+(pr-(pr\bmod4))/4),&p\text{ odd}.
 \end{cases}\tag{PS3b}
\]

The integer in the third coordinate is exact. Multiplication by 5 preserves the original chart, by 3 sends it to the 3-mod-4 companion, and by 2 moves to the next conductor. The original Gamma ladder by itself is therefore **not an all-prime invariant SUCC carrier**.

**Minimal-semigroup-closure theorem.** The smallest set of positive spectral labels containing Suzuki's `alpha_0=1/2` and closed under multiplication by every genuine prime is **the entire half-integer lattice** `{n/2:n>=1}`: closure contains `(1/2)*n` for every positive integer n by its prime factorization; the half-lattice is already closed. This **does not license inserting all added modes into Suzuki's original Weil operator**. It specifies the minimal mathematical host of all these possible chart transports; source projections remain mandatory.

**Causal note:** These maps are *mathematical scalar-dilation transport of a derived spectral index*. Nothing yet proves that changing a prime's FUCC action *physically* or *arithmetically* acts on the Gamma test state by these maps; the proposed genuine operator intertwiner is still missing.

### PS-03b — a genuine affine arithmetic **label** functor, but not yet a Hilbert operator functor (PROVED LOCAL)

There is a canonical exact injection from the **positive integer address** carrier into the minimal half-integer spectral host:

\[
 \boxed{J:\mathbb N_{\ge1}\to\{n/2:n\ge1\},\quad J(n)=n/2.}
\]

It intertwines the actual additive and prime-multiplicative source operations with the corresponding half-unit and scalar-dilation operations:

\[
 J(n+1)=J(n)+1/2,\quad J(pn)=pJ(n),\quad
 J(p(n+1))=J(pn+p).
\]

Thus SUCC's affine braid `V_p S=S^p V_p` **really does commute** on the expanded Gamma **index carrier**. This is the exact source-level coupling that was previously only speculative. But the operation `n->n/2` does not preserve original Suzuki's **selected** mode subset, its weights `alpha^-2`, the differential domain, or the full Weil form. Its source base starts at n=1 / alpha=1/2: forcing a spectral alpha=0 would make the resolvent term singular. The outstanding RH-relevant theorem is now specifically the *source-preserving analytic-operator lift* of this correct discrete label functor, with original-source projections and all signed completion terms—not the existence of a label map.

## PS-04 — EXACT half-density intertwining, compatible positive Gamma-branch sieve (PROVED LOCAL)

On `L²(R)` define the genuinely unitary geometric dilation `D_p f(x)=sqrt(p) f(px)`. A change of variables proves

\[
 \boxed{D_pR_\alpha D_p^{-1}=p R_{p\alpha},\qquad
 p^{-3}D_p(\alpha^{-2}R_\alpha)D_p^{-1}=(p\alpha)^{-2}R_{p\alpha}.}\tag{PS4}
\]

This is *not* the sampled integer FUCC pullback, which has a different operator norm. The factor `p^-3` comes from exactly one integral Jacobian and two powers of inverse spectral scale. For the interval kernel, `D_p:L²(-a,a)->L²(-a/p,a/p)` also maps mean-zero to mean-zero, so (PS4) survives projection when the target radius is changed accordingly.

For `p≡1 mod4`, `p*{4j+1}` is a subset of `{4j+1}`; consequently

\[
 \boxed{B_{+,a/p}-p^{-3}D_pB_{+,a}D_p^{-1}
 =\sum_{\substack{n\equiv1\ (4)\\p\nmid n}}
 (n/2)^{-2}R_{n/2,a/p}\ \succeq 0.}\tag{PS4a}
\]

Here all resolvents are mean-zero compressed on the **target** interval. For `p≡3 mod4`, the same positive **remainder** requires the companion chart `B_-`, not `B_+`:

\[
 \boxed{B_{-,a/p}-p^{-3}D_pB_{+,a}D_p^{-1}
 =\sum_{\substack{n\equiv3\ (4)\\p\nmid n}}(n/2)^{-2}R_{n/2,a/p}\succeq0.}\tag{PS4b}
\]

For p=2 the correct comparison is the **next dyadic conductor** chart, with an exact equality of full mode sums and **no forced remainder**. All sums converge as bounded positive operators: `||alpha^-2 R_alpha||<=2/alpha^3`, summable.

This is an authentic and nontrivial **operator-order transfer across prime-indexed Gamma charts**. It is not yet an action of the genuine arithmetic prime-jet Hilbert representation on Suzuki's complete Weil form. The transported source really is the original Gamma mode ladder plus its explicitly recorded companion, not an arbitrary positive kernel.

## PS-05 — finite Euler-sieve algebra on the minimal Gamma host (PROVED LOCAL; source-label caveat)

On the full half-integer host define `B_all=sum_(n>=1)(n/2)^-2 R_(n/2)` and let `T_q(B)=q^-3 D_q B D_q^-1`. Then

\[
 \boxed{T_q(B_{\rm all})=\sum_{q\mid n}(n/2)^{-2}R_{n/2}.}\tag{PS5}
\]

For **distinct authentic primes** `P`, inclusion-exclusion gives

\[
 \boxed{\prod_{p\in P}(I-T_p)B_{\rm all}
 =\sum_{\gcd(n,\prod P)=1}(n/2)^{-2}R_{n/2}\succeq0.}\tag{PS5b}
\]

The products mean the commuting **linear dilation superoperators** acting on this special bath, not an Euler-product identity for the Riemann zeta function. Independent exact controls:

- `P={2,3}` yields coefficient 1 iff gcd(n,6)=1.
- `P={2,6}` yields coefficient **−1 at mode n=6**: overlapping/composite factors invalidate the coprime inclusion-exclusion inference.
- `P={2,2}` yields coefficient **−1 at n=2**: repeated primes are not an allowed Euler source set.
- `P={4,9}` still yields coefficients 0 or 1 because coprimality, but the factors are **composite**, so the primality gate rejects them as a primitive Euler-place family.

Our exact OU sample matrix uses actual kernel distances `x_i=2i log2`. Since `alpha=n/2`, **every entry is rational**:

\[
 K_{ij}=\sum_{n\in S}\frac4{n^2}2^{-n|i-j|}.
\]

Cholesky-free exact rational `LDL^T` certifies finite positive matrices; infinite operator positivity follows from the Fourier transforms of the genuine resolvents and nonnegative source coefficients, not finite test counts.

## PS-06 — Gamma **chiral positivity**, an exact signed interaction (PROVED LOCAL; classical Fourier identities)

Now form the *auxiliary* companion bath `B_-` on the whole line with `alpha=(4j+3)/2`, and let `C=B_+-B_-`. Although this is a **signed subtraction**, `C` is positive! Under angular Fourier transform its multiplier is

\[
 \sigma(\xi)=\sum_{j\ge0}\left[\frac4{(4j+1)((4j+1)^2/4+\xi^2)}
 -\frac4{(4j+3)((4j+3)^2/4+\xi^2)}\right]>0.\tag{PS6a}
\]

Each pair is positive because the scalar multiplier is strictly decreasing as `n` grows. Summability follows from `O(n^-3)`; zero mean or any Suzuki interval compression preserves PSD. Every finite paired truncation is **also positive**, since each pair has nonnegative Fourier multiplier.

The stronger **closed formula** is

\[
 \boxed{\sigma(\xi)=\frac{\pi[1-\operatorname{sech}(\pi\xi)]}{\xi^2}
 =\frac{\pi-|\Gamma(1/2+i\xi)|^2}{\xi^2},\quad\xi\ne0,\qquad
 \sigma(0)=\pi^3/2.}\tag{PS6b}
\]

**Independent proof:** With `x=|t|>0` the source difference kernel is

\[
 k_C(t)=\sum_{j\ge0}\left[\frac4{(4j+1)^2}e^{-(4j+1)x/2}
 -\frac4{(4j+3)^2}e^{-(4j+3)x/2}\right].
\]

For `t≠0`, its second derivative is the absolutely convergent geometric series

\[
 k_C''(t)=\sum_{j\ge0}\big(e^{-(4j+1)x/2}-e^{-(4j+3)x/2}\big)
 =\frac1{2\cosh(t/2)}.
\]

Each exponential has distributional second derivative `alpha² e^-alpha|t| - 2alpha delta_0`; hence pairing the modes and using the convergent Leibniz sum `sum_(j>=0)(1/(4j+1)-1/(4j+3))=beta(1)=pi/4` gives the **complete distributional identity**

\[
 \boxed{k_C''=\tfrac12\operatorname{sech}(t/2)-\pi\delta_0.}\tag{PS6c}
\]

Fourier of `sech(t/2)/2` is `pi sech(pi xi)`. Since Fourier of a second derivative is `-xi²` times Fourier, (PS6b) follows, including the removable value at zero. The Gamma-modulus expression is Euler's reflection identity `Gamma(1/2+i xi)Gamma(1/2-i xi)=pi/cosh(pi xi)`.

**Precise arithmetic content:** Let `chi4(n)` be 0 if even, +1 for n=1 mod4, and −1 for n=3 mod4. Then the difference kernel really sums over source modes with coefficient `chi4(n)`; the standard *actual-prime* Euler product

\[
 \boxed{\beta(s)=L(s,\chi_4)=\sum_{n\ge1}\frac{\chi_4(n)}{n^s}
 =\prod_{p\text{ odd prime}}(1-\chi_4(p)p^{-s})^{-1},\quad \Re s>1}
\]

identifies the sector character with genuine multiplicative prime arithmetic. In particular

\[
 \boxed{k_C(0)=4\beta(2)=4G_{\rm Catalan},\quad
 \sigma(0)=16\beta(3)=\pi^3/2.}\tag{PS6d}
\]

This is a bona fide arithmetic-to-analytic compatibility example. It is **NOT an identification of `C` with the completed Weil form for zeta**, and adding `B_-` to Suzuki's authentic operator without accounting for its source would violate the repository's no-ghost/source-authenticity rules.

## PS-07 — chiral H^{-1} rigidity with explicit constants (PROVED LOCAL)

Define the inhomogeneous norm `||f||_{H^-1}²=(2pi)^-1 int |fhat(xi)|²/(1+xi²) dxi`. Then on all `L²(R)`,

\[
 \boxed{\frac83||f||_{H^{-1}}^2\le\langle f,Cf\rangle
 \le22||f||_{H^{-1}}^2.}\tag{PS7}
\]

**Lower proof:** The first positive pair in (PS6a) is `4/(1/4+xi²)-4/[3(9/4+xi²)]`, which is >= `(8/3)/(1+xi²)`. All later pairs are positive.

**Upper proof:** Each pair in (PS6a) decreases with |xi|, so `sigma(xi)<=sigma(0)=pi³/2`. For `x=|xi|>0`, writing `f_x(n)=1/[n(1+n²/(4x²))]`, one calculates

\[
 -f_x'(n)=\frac{1+3u}{n²(1+u)^2}\le\frac2{n²},\qquad u=\frac{n²}{4x²}.
\]

Thus `x² sigma(x)<=8 sum_(j>=0)(1/(4j+1)-1/(4j+3))=2pi`. Therefore `(1+x²)sigma(x)<=pi³/2+2pi<22` (using the classical rational bound pi<22/7). Plancherel completes the proof.

These inequalities identify the chiral positive operator with an honest **negative Sobolev-order metric**, not a uniform coercive `L²` gap. In particular `sigma(xi)~pi/xi²` for large |xi|, and `<f,Cf>` can be arbitrarily small for normalized high-frequency states. It has strictly positive Fourier symbol but zero lower `L²` spectral bound. It is a mathematically useful auxiliary metric for comparing dual SUCC observations, not automatically the metric of the true Weil operator.

**Further source-coupling obstruction (PROVED LOCAL; qualified by the carrier metric).** If the auxiliary C is applied *directly to v*, rather than the correct Suzuki derivative variable u=i v', in Suzuki's first prime interaction interval `log2/2<a<log2`, choose a nonzero smooth left-strip profile and translate it right by log2. High-frequency modulation by `e^(i 2pi m x/log2)` leaves the negative prime-overlap pairing bounded away from zero (phase wraps to 1), while the auxiliary chiral norm tends to zero by `sigma(xi)->0` and dominated convergence. Hence **no uniform constant C** can bound the absolute first-prime overlap by `C*<v,Cv>` on all L² endpoint states. This does **not** say the real Suzuki form is negative: its full, high-frequency Gamma bath and remaining pole terms are absent from this auxiliary comparison. It kills a tempting shortcut that would use the positive chiral sector on **bare v** to dominate authentic signed prime transport. **This does NOT refute the correct differentiated pairing `<i v', C i v'>`; indeed that pairing yields the genuinely promising bounded Markov energy in PS-10.**

## PS-08 — a literal FINITE categorical sphere, and its source-authentication barrier (PROVED FINITE MODEL)

Let equator be the four-cycle with vertices `0,1,2,3 (mod 4)`. Glue **two cones** over this cycle (south/origin and north/formal-global apex). The resulting eight triangles and twelve edges on six vertices form an octahedral boundary complex, homeomorphic to `S²`. Direct rational boundary-matrix calculations give

\[
 \partial_1\partial_2=0,\quad(V,E,F)=(6,12,8),\quad
 \chi=2,\quad(b_0,b_1,b_2)=(1,0,1).
\]

For every odd actual prime `p`, **multiply equator phase labels by p mod4**, fixing the two apex vertices. This is a simplicial automorphism. It acts on the top integral homology class by

\[
 \boxed{\deg(p\cdot -\!\!\mod4)=\chi_4(p)\in\{+1,-1\}.}\tag{PS8}
\]

If p=1 mod4 the equator map is identity; if p=3 mod4 it is reflection and reverses the top cycle. This is checked against an explicit signed integral fundamental 2-cycle, not inferred from Euler characteristic alone. At p=2, multiplication mod4 sends a 4-cycle edge to a diagonal, **not a simplicial automorphism**: it forces a conductor-changing enlargement (matching PS-03).

**Crucial type distinction:** This is an actual finite sphere with actual prime-typed simplicial maps, but we **chose** its equator as a phase cycle. We have **not** shown that this sphere is the adele class space, the global geometric carrier of zeta, Suzuki's infinite Hilbert space, or a legitimate physical E instrument. The first and last apex are labels of a model's cones; the north apex is NOT an actualized infinite computation or a quotient through which all original arithmetic claims factor. A literal singleton terminal apex would forget nonconstant original-source targets. The true arithmetic global object must be a structured compatible-section/completion carrier, not a forced identification of every prime history at one undifferentiated point.

## PS-09 — exact finite-to-continuum **heat-time** source certificate (PROVED LOCAL; rational bounds)

Parent PG-06 proved the genuine whole-line heat-resolvent representation for each OU mode:

\[
 e^{-\alpha|x|}=2\alpha\int_0^\infty e^{-\alpha^2u}h_u(x)du,
 \quad h_u(x)=(4\pi u)^{-1/2}e^{-x²/(4u)}.
\]

Consequently Suzuki's positive bath carries heat-weight

\[
 W_+(u)=\sum_{n\equiv1(4)}\frac4n e^{-n²u/4}.
\]

At the **source-typed dyadic time** `u=4r log2` (positive integer r), this becomes the convergent series of EXACT rationals

\[
 \boxed{W_+(4r\log2)=\sum_{n\equiv1(4)}\frac4n 2^{-r n²}.}\tag{PS9}
\]

For cutoff K, its finite prefix `L_K` and remainder obey

\[
 \boxed{L_K\le W_+(4r\log2)\le L_K+
 \frac4{K+1}\frac{t^{K+1}}{1-t},\qquad t=2^{-r(K+1)}.}\tag{PS9b}
\]

**Proof:** For n>K, `1/n<=1/(K+1)` and `n²>=(K+1)n`; bound the residual by the resulting geometric series. Exact `Fraction` code checks nested intervals and independent high-precision samples. This is a rigorous finite observation of a **positive** part of the authentic source at one special heat time, not a certified limit of the full signed Weil quadratic form.

## PS-10 — the CORRECT differentiated Gamma chiral coupling is a bounded MARKOV DIRICHLET FORM (PROVED LOCAL)

**This corrects an important metric issue in PS-07:** Suzuki's compact kernel operates on `u=i v'`, not on `v` directly. The auxiliary signed chiral operator `C=B_+-B_-` has multiplier `sigma(xi)=pi(1-sech(pi xi))/xi²`; therefore its differentiated form on `v` has the exact bounded nonnegative Fourier multiplier

\[
 \boxed{\widehat{D^*CD}(\xi)=\xi^2\sigma(\xi)
       =\pi(1-\operatorname{sech}(\pi\xi)),\qquad
       0\le D^*CD\le\pi I.}\tag{PS10a}
\]

This is not merely positivity in a weak Sobolev metric. It becomes a bounded positive order-zero operator on the **actual v-variable** after the correct differentiation. Let

\[
 \boxed{q(t)=\frac1{2\pi}\operatorname{sech}(t/2),\quad
 P f=q*f.}\tag{PS10b}
\]

The classical Fourier-sech identity gives `hat q(xi)=sech(pi xi)`, and direct substitution `t=2y` and `int_R sech(y)dy=pi` show that `q>=0`, `q(-t)=q(t)`, and `int q=1`. Thus `P` is a genuine self-adjoint positivity-preserving **Markov** convolution operator with `||P||=1`, and

\[
 \boxed{D^* C D=\pi(I-P),\qquad
 \langle v,D^*CDv\rangle
 =\frac{\pi}{2}\iint_{\mathbb R^2}q(x-y)|v(x)-v(y)|^2\,dx\,dy.}\tag{PS10c}
\]

For `v` in Schwartz, prove this with Plancherel plus expansion of the double integral; both sides extend as bounded quadratic forms to all L². This is a **source-derived nonlocal jump-energy law**, since `q` is forced by the paired Gamma OU ladder spectra (one authentic Suzuki chart plus one explicitly auxiliary companion), rather than a PSD covariance invented to fit RH. It has no L² lower spectral gap because multiplier vanishes at xi=0; for high frequencies the multiplier tends to pi, **countering the bare-variable no-go in PS-07**. It is not the genuine completed Weil form, and the auxiliary companion must not be inserted into Suzuki's original arithmetic source without additional identification.

**Finite-to-continuous SUCC of random jump units.** For time `t>=0`, the bounded Markov generator has the exact operator-norm convergent semigroup

\[
 \boxed{e^{-t\pi(I-P)}=e^{-\pi t}
   \sum_{k=0}^\infty \frac{(\pi t)^k}{k!}P^k.}\tag{PS10d}
\]

Each `P^k` is the lawful transition law of `k` independent jumps of the *actual mathematical density* q; the Poisson weights are nonnegative and normalized. For `t=1/pi`, truncating after K transitions yields a (sub-Markov) positive operator whose omitted **operator norm** is at most the Poisson tail, and therefore bounded by the purely rational envelope

\[
 \boxed{\left\|e^{-(I-P)}-e^{-1}\sum_{k=0}^K\frac{P^k}{k!}\right\|
 \le\sum_{j>K}\frac{e^{-1}}{j!}
 \le\frac{1/(K+1)!}{1-1/(K+2)}.}\tag{PS10e}
\]

This proves a **bounded finite-implementation error** for the mathematical Markov source when the exact transition P is available. It does not supply an actual physical source preparation or finite automaton implementing unbounded continuous jumps. A separate 4-state symmetric Markov *toy* with rational probabilities (stay 1/2, move ±1 with probability 1/4) is exactly certified by `sum_i(v_i-v_(i+1))²/4`; the code explicitly marks it as **not identical to q**.

## PS-11 — two independent finite SUCC hemispheres converge to ONE global Gaussian boundary, with a sharp Fourier sandwich (PROVED CLASSICAL ANALYTIC)

There is now a genuine two-sided **boundary-in-law** realization of the maintainer's sphere intuition.

1. **Pascal hemisphere:** let `eps_i` be independent symmetric ±1 increments and define `X_N=(sum_(i<=N) eps_i)/sqrt(2 pi N)`. The ordinary Pascal/binomial path law has cycles-Fourier characteristic
   `hat(mu_N)(xi)=cos(theta_N)^N`, with `theta_N=sqrt(2pi/N)*xi`.
2. **Gamma-chiral hemisphere:** let `J_i` be independent identically distributed jumps with **exact** positive source-derived density `q(t)=sech(t/2)/(2pi)`. Since `hat q(omega)=sech(pi omega)` in angular frequency, `Var(J_i)=pi²`. Set `Y_N=(sum J_i)/(pi sqrt(2pi N))`. Its cycles-Fourier characteristic is **exactly** `hat(nu_N)(xi)=sech(theta_N)^N`.

Both have the same fixed scale and for every real xi with `|theta_N|<pi/2` obey the **sharp order in the real Fourier-observation variable**

\[
 \boxed{\cos(\theta_N)^N\ \le\ e^{-\pi\xi^2}\ \le\
 \operatorname{sech}(\theta_N)^N.}\tag{PS11}
\]

**Proof:** for `0<=z<pi/2`, `tan z>=z` implies `log cos z<=-z²/2`; for all z>=0, `tanh z<=z` implies `log sech z>=-z²/2`. Both inequalities are even in z, exponentiation by positive N yields the sandwich. Taylor expansion provides opposite finite-depth defects:

\[
 \log\hat\mu_N(\xi)=-\pi\xi^2-\frac{\pi^2\xi^4}{3N}+O_\xi(N^{-2}),
 \qquad
 \log\hat\nu_N(\xi)=-\pi\xi^2+\frac{\pi^2\xi^4}{3N}+O_\xi(N^{-2}).
\]

The errors are uniform on any fixed compact Fourier-frequency interval for sufficiently large N. Both characteristic functions converge to `e^-pi xi²`, so Lévy's continuity theorem yields **weak convergence of both real probability laws to the same self-Fourier Gaussian** `g(x)=e^-pi x²`. This gives a precise meaning for a *common global/Archimedean boundary*: an identical **limiting observed probability law** approached from two distinct families of finite SUCC experiments, with one convergence from below and one from above in Fourier-observation value.

**No illicit identification:** the two finite source preparations are different; their original histories and finite-prime p-adic normalizations are not thereby equal, a Fourier-characteristic sandwich is NOT an ordering of the underlying probability measures, and neither source is a physically executed infinity. The Gamma-chiral hemisphere uses an *auxiliary* gamma companion; proving that this legal mathematical bath supplies the true completed ζ Weil geometry remains open. The same Gaussian marginal is **not** a categorical Yoneda equivalence of all possible observations of the two sources.

## Serious negative controls / scope boundary

1. Wrong Euler place: composite 6 has valid multiplication and source indices but is **not** a primitive prime. Coprime composites 4,9 produce positive sieve coefficients but still fail prime authentication.
2. Lost p-adic residue phase: valuations alone cannot propagate Pascal recursion; arbitrary fixed digit depth misses cancellation.
3. Wrong Gamma chart: original `1 mod4` is not stable under p=3, or p=2. Only honest companion/conductor changes preserve transported source labels.
4. Wrong half-density: forgetting the `p^-3` factor makes the spectral resolvent weights disagree exactly by p³.
5. Wrong sphere semantics: the finite S² homology is a theorem about a **declared four-cycle**; no actual adelic/Suzuki global-topology identification follows.
6. Wrong positive object: `C=B_+-B_-` and all its Fourier/Gamma identities are **auxiliary**; the complete Weil form includes signed prime powers, poles and the `-C K_a` term from the source and is not equal to `C`.
7. False domination: the auxiliary positive H^-1 chiral metric **on bare v** does not uniformly bound high-frequency negative prime cross-strip overlap. The **correct differentiated** auxiliary pairing on u=i v' instead yields the Markov form PS-10; this is not yet the authentic completed Weil form.
8. Wrong infinity: a positive infinite heat sum with a finite rational enclosure is an analytic theorem, not infinitely many physically realized measurements or completed RH.

**Tests and reproducibility:** `observational_succ/prime_categorical_sphere.py`, `tests/test_prime_categorical_sphere.py` (32 named exact/source tests, plus extensive finite grids), `scripts/prime_categorical_sphere_probe.py` and frozen `research/2026-10-14/PRIME_CATEGORICAL_SPHERE_RECEIPT.json`. Independent 70-digit calibration `scripts/prime_sphere_independent_oracle.py` uses direct alternating Dirichlet-mode sums, oscillatory Fourier cosine integration and Gamma reflection, with **no zeta zeros**, saved in `PRIME_CATEGORICAL_SPHERE_NUMERIC_HOLDOUT.json`. The mathematical proofs stand independently of finite test coverage or high-precision decimals. Lean/kernel formalization is **NOT claimed**.

## Frontier toward Suzuki / RH — *what would actually change the theorem status?*

- **F1 (arithmetic source transport):** realize a natural map from the genuine integer SUCC/FUCC prime-jet algebra—not just independently chosen scalar multiplication—to the expanded Gamma operator charts, preserving additive/multiplicative diamond defects, exact half-density, p-adic residue phases, and the real test-function state.
- **F2 (original source projection):** establish which chiral auxiliary terms, if any, can be transported back into the **true** Suzuki Gamma/pole/prime operator without adding ghost modes; a positive auxiliary `B_+-B_-` by itself cannot be substituted for the Weil form.
- **F3 (first-wavefront signed comparison):** source-identify a nonnegative remainder or closed-form boundary Schur complement that dominates the **actual** negative prime-2 coupling on the appropriate logarithmic-energy domain; this dossier's H^-1 metric alone provably cannot.
- **F4 (globality):** a justified all-a form inequality or the specific domain-correct, compact-uniform spectral limit of Suzuki's Corollary 1.6. No finite sphere or mode trace proves this.

**Verdict:** There is a rigorous, source-correlated algebraic/analytic **prototype** of the user's categorical sphere: Kummer's local Pascal arithmetic, a `chi4`-graded Gamma conductor fibration with true prime transport and positive source-sieve remainders, a genuine positive signed Gamma operator with an explicit sech/Gamma spectral formula, a source-derived **bounded Markov jump Dirichlet form**, two distinct finite SUCC hemispheres that sandwich the same Gaussian Fourier limit, and a literal topological S² toy complex carrying the same prime character as its degree. The unproved claim is that this *entire assembled picture* is one actual arithmetic/adelic/Suzuki carrier with a source-forced completed Weil positivity law. That is the correct next moonshot, not something this round assumes.
