# Selected prime-phase carrier: exact source births, Galois-trace blindness, and the remaining signed cofactor

**Research date:** 2026-11-01. **Starting authority:** canonical Main XIX head `81045770234a114247e43eb08ae5c6d446e9514a`; post-integration negative draft #458 is read-only context. Source is the literal original BBP four-pole recurrence, **not** a surrogate. These are classical/paper exact results with local independent finite oracles. No new Lean declaration, external referee, π-normality, RH, physical quantum, or asymptotic signed cancellation claim. Do not change source archives or promote canonical claims.

## SPP-01. A new prime creates a persistent signed phase clock (PROVED LOCAL, integer arithmetic)

Write

\[
 r(j)=\frac4{8j-7}-\frac2{8j-4}-\frac1{8j-3}-\frac1{8j-2},\quad
 U_0=0,\quad U_N=\sum_{j=1}^N 16^{N-j}r(j). \tag{1}
\]

For any **prime `p>5`, `p≡1 or 5 mod 8`**, define

\[
 (n_p,c_p)=\begin{cases}((p+7)/8,4)&p\equiv1\pmod8,\\
 ((p+3)/8,-1)&p\equiv5\pmod8,\end{cases}
 \qquad J_p=(p+1)/2.\tag{2}
\]

The four raw pole denominators have residue classes `1,4,5,6 (mod 8)` and positive sizes `8j-7,8j-4,8j-3,8j-2` respectively. At time `j=n_p`, exactly one denominator equals `p`, with signed coefficient `c_p/p`. All earlier raw denominators are less than `p`. For any `n_p<j<J_p`, none of the raw denominators is divisible by `p`: `2p≡2 (mod8)`, `3p≡3 or 7 (mod8)` are forbidden pole residues, and the earliest admissible later multiple is `4p=8J_p-4`. Consequently, for every integer `n_p<=j<J_p`,

\[
 U_j=\frac{c_p16^{j-n_p}}p+V_{p,j},\qquad
 V_{p,j}\in\mathbb Z_{(p)},\quad
 v_p(U_j)=-1,\quad
 pU_j\equiv c_p16^{j-n_p}\pmod p.\tag{3}
\]

Here `Z_(p)` is the localization of Z at the prime `p` (rationals with p-free reduced denominator). A proof by source convolution or induction works. Between birth and first reuse, `V_(p,j+1)=16 V_(p,j)+r(j+1)` with p-integral initial cofactor. **Phase factorization is exact** at the distinguished real embedding:

\[
 e(hU_j)=e(hc_p16^{j-n_p}/p)\,e(hV_{p,j}),\quad e(x)=\exp(2\pi ix).\tag{4}
\]

The persistence length `J_p-n_p` is `(3p-3)/8` for `p≡1 mod8` and `(3p+1)/8` for `p≡5 mod8`. The coefficient and *all* intermediate residues were checked by exact Fraction arithmetic for every eligible prime below 250, including a separate combined rational-source implementation.

**Boundary:** the same p-clock appears for every rational changed seed `s` whose denominator is p-free; the zero boundary authenticates the actual trajectory but the clock by itself does **not** select normality. The coherent altered real seed `-π/16` is *not* a p-free rational-seed comparison and must not be smuggled into (3).

## SPP-02. Exponentially growing original-state denominator (PROVED LOCAL + classical PNT-AP)

For an integer horizon `N>=1`, define the finite squarefree product

\[
 P_N=\prod_{\substack{2N<p<8N\\p>5,\ p\equiv1\pmod4}}p.\tag{5}
\]

**Exact all-N theorem:** every prime in this product occurs with valuation **exactly -1** in `U_N`. Indeed `p>2N` implies `4p>8N`, so the only possible multiple of `p` among the `4N` raw source pole denominators is the original `p` itself: `2p,3p` have forbidden residues modulo 8. It appears precisely once at `n_p<=N` and carries coefficient `4` or `-1` times a power of 16, which is a p-adic unit. Thus

\[
 \boxed{P_N\mid\operatorname{den}(U_N),\qquad
 v_p(U_N)=-1\quad(p\mid P_N).}\tag{6}
\]

For fixed nonzero harmonic h, all large N also have these prime factors in the reduced denominator of `hU_N`. Applying the **classical prime number theorem in the fixed arithmetic progression** `p≡1 (mod4)` to the Chebyshev theta function,

\[
 \sum_{\substack{2N<p<8N\\p\equiv1\pmod4}}\log p
 =\vartheta(8N;4,1)-\vartheta(2N;4,1)
 =3N+o(N).\tag{7}
\]

Therefore

\[
 \boxed{\log\operatorname{den}(U_N)\ge3N+o(N).}\tag{8}
\]

The arithmetic-progression prime-distribution theorem is classical input, not reproved here; the source-specific *exact valuation* is obtained directly from the four poles. No new conjectural distribution of primes is assumed. Even huge cyclotomic conductor **does not imply** chronological phase cancellation.

## SPP-03. Exponentially strong Galois-average false positive (PROVED LOCAL)

For each N, let `P=P_N` and split the actual rational `U_N` uniquely into

\[
 U_N=V_N+\sum_{p\mid P}\frac{a_p}p,\qquad
 \gcd(\operatorname{den}V_N,P)=1,\quad
 a_p\equiv pU_N\pmod p,\quad 1\le a_p<p.\tag{9}
\]

The `a_p` are the authenticated source residues `c_p16^(N-n_p) mod p`. Put `q=den(V_N)`, so `(P,q)=1`, and `K=Q(ζ_q)`, `L=Q(ζ_{Pq})`. The Chinese remainder theorem identifies the relative Galois group as the product of the primitive p-sector groups. For every **fixed nonzero h** and all N sufficiently large that `2N>|h|`, each p-sector is primitive and

\[
 \frac1{[L:K]}\operatorname{Tr}_{L/K}e(hU_N)
 =e(hV_N)\prod_{p\mid P}\frac1{p-1}\sum_{a=1}^{p-1}\zeta_p^{ha_pa}
 =e(hV_N)\prod_{p\mid P}\left(-\frac1{p-1}\right).\tag{10}
\]

Thus the trace magnitude is exactly `1/φ(P_N)`, and the classical theta asymptotic in (7) gives

\[
 \boxed{\left|\operatorname{normalized\ relative\ trace}\right|
 =\exp(-3N+o(N)),\quad |e(hU_N)|=1.}\tag{11}
\]

**This is NOT temporal cancellation**: the averaged observation appears to vanish exponentially at a *single time* while the designated complex embedding still has full unit magnitude. It is an exact warning against discarding the p-primary contribution as observational noise. For `N=3`, `U_3=615863723/765765`, `P_3=13·17`, the exact split is

`U_3=2783233/3465 + 10/13 + 4/17`;

its normalized relative trace equals `e(2783233/3465)/192`, even though the original phase is unit length. This follows from cyclotomic trace; not any assumption about normality.

**Universal no-go control:** for each N choose the entirely DIFFERENT rational sequence `w_N=1/P_N` (when P_N>1). Then `|e(w_N)-1|<=2π/P_N->0`, so the selected phases become perfectly coherent, but their normalized Galois traces still tend to zero like `1/φ(P_N)`. This fake does **not** satisfy the original forcing. It proves that conductor growth and Galois averaging cannot, on their own, establish normality.

## SPP-04. Galois-observer information budget (CLASSICAL, source-specialized)

At a newborn prime p, regard the function `f(a)=ζ_p^(c a)` on the multiplicative Galois group `G=F_p^×`, `c≠0`. Expand it into *multiplicative* characters χ of G using the normalized Fourier coefficient `fhat(χ)=(1/(p-1))Σ_{a in G}f(a)conj(χ(a))`. The trivial coefficient is `-1/(p-1)`. For every nontrivial χ, the elementary Gauss-sum calculation gives

\[
 |\widehat f(\chi)|^2=\frac{p}{(p-1)^2}.\tag{12}
\]

Proof: in the unnormalized square, write `a=ub` and sum `ζ_p^((u-1)b)` over nonzero b; the sum is `p-1` when u=1 and `-1` otherwise. Orthogonality `Σ_{u∈G}χ(u)=0` yields `|Gauss(χ)|²=p`. Parseval checks the exact energy identity

\[
 \frac1{(p-1)^2}+(p-2)\frac{p}{(p-1)^2}=1.\tag{13}
\]

A projection retaining only the trivial Galois character plus m nontrivial modes retains at most `(1+mp)/(p-1)^2` of this **normalized Galois-orbit L² energy**. If `m=o(p)`, this tends to zero. This is not a lower bound on all algorithms for computing a selected complex phase, nor a statement about physical quantum information. It specifies why **this particular averaging/Fourier compression** erases the observation that needs to survive.

## SPP-05. A prime clock can itself remain coherent (PROVED LOCAL exact negative witness)

The authentic prime `p=257` has `16²≡-1`, `16⁴≡1 (mod 257)`. It first enters at `n_p=33` with `c_p=4`, and persists to first reuse `J_p=129`. At `N=128`, the 96-step window `j=33,...,128` is a whole multiple of the order-four prime clock. Its **primary-only** mean is exactly

\[
 \frac14(\zeta_{257}^{4}+\zeta_{257}^{64}+\zeta_{257}^{-4}+\zeta_{257}^{-64})
 =\frac12\big(\cos(8\pi/257)+\cos(128\pi/257)\big)>\frac{49}{100}.\tag{14}
\]

Indeed both cosines are positive, and `cos x>=1-x²/2`, `π<22/7` give the stated strict rational lower bound. This kills any proposed **universal, all-p primary-clock cancellation theorem**. It says nothing about the full original source+cofactor sum; finite signed values of that genuine joint sum remain an unproved diagnostic.

## SPP-06. Rational source seeds are a common normality class (CLASSICAL)

Let `α=Σ 16^-n r(n)=π/16` and `T_n=Σ_(j>=1)16^-j r(n+j)`. For any real seed `s`, `U_n(s)=16^n(α+s)-T_n`; the summable tail transfers base-16 normality between the completed point `α+s` and the orbit. **Normality is invariant under addition of a rational number**: after finitely many radix steps `16^n s` is periodic in n, and the normality of x in base16 entails equidistribution along every fixed residue class of that period, by normality in base `16^L`. Applying `-s` proves the reverse. Therefore *all rational initial seeds* share the same normality answer as the exact zero seed. In particular, for `s=a/15`,

\[
 e(hU_n(a/15))=e(ha/15)e(hU_n(0))\quad\text{for EVERY }n,h.\tag{15}
\]

This is a source/seed firewall: the original *literal* zero seed is required to identify the original π orbit, but rationality of the seed alone cannot discriminate it from its rational translates. The coherent `s=-π/16` or `s=1/5-π/16` is irrational and lies outside this rational-seed cohort. **Do not infer normality from the cohort's algebraic existence.**

## SPP-07. Fully conditioned quarter-turn observer and improved exact error budget (PROVED LOCAL, classical)

Let `A_N(h)=N^-1 Σ_{n=1}^N e(hU_n)` and define one real observation for each *positive* harmonic h:

\[
 b_N(h)=\begin{cases}\Im A_N(h),&v_{16}(h)\text{ even},\\
 -\Re A_N(h),&v_{16}(h)\text{ odd}.\end{cases}\tag{16}
\]

The ×16 source recurrence and telescoping sums yield

\[
 |A_N(16h)-A_N(h)|
 \le\frac{2+2\pi h\sum_{n=2}^{N+1}r(n)}N
 <\frac{2+(715/448)h}{N}.\tag{17}
\]

**Exact rational source mass budget:** `Σ_(n=2)^16 r(n)+1/64 <65/256`, from `r(n)<15/[64(n-1)^2]` and monotone integral tail `Σ_(m>=16)m^-2<1/15`; use the classical `2π<44/7`. The new h-coefficient `715/448≈1.596` replaces the earlier `165/56≈2.946`. This is a transport constant improvement, not a new signed mean bound.

The two perpendicular observations `b_N(h)` and `b_N(16h)` recover `A_N(h)` with error smaller than the right-hand side of (17). In particular

\[
 \boxed{|A_N(h)|<\sqrt{b_N(h)^2+b_N(16h)^2}
 +\frac{2+(715/448)h}{N}.}\tag{18}
\]

Proof: when `v_16(h)` is even reconstruct `-b_N(16h)+i b_N(h)`, otherwise reconstruct `-b_N(h)+i b_N(16h)`; only one Cartesian component incurs the ×16-ladder error. This improves the earlier adaptive arctan *factor 8* conditioning in this coordinate choice, but relies on **two orthogonal real observations at adjacent harmonics**, not a physical 75% reduction in Shannon information. It remains a well-conditioned equivalence, not a theorem `b_N(h)->0`.

## SPP-08. Source-born prime suffix: a local-to-global signed criterion (CLASSICAL equivalence, not proof)

By the classical PNT in arithmetic progressions, for every sufficiently large N choose a prime `p_N≡1 (mod4)` in `(2N,3N)`. Its birth index `n_(p_N)` satisfies

\[
 N/4<n_{p_N}<3N/8+1,\qquad n_{p_N}\le N<J_{p_N}.\tag{19}
\]

For any fixed h, define the source-authenticated **joint cofactor/prime sum**

\[
 R_N(h;p_N)=\sum_{j=n_{p_N}}^N
 e(hV_{p_N,j})e(hc_{p_N}16^{j-n_{p_N}}/p_N).\tag{20}
\]

It is **exactly the suffix** `S_N(h)-S_(n_p-1)(h)`. If `R_N(h;p_N)=o_h(N)` for one such choice at every sufficiently large horizon, then `S_N(h)=o_h(N)`: writing `L=limsup_N |S_N(h)|/N<=1`, the exact split and `n_p/N<=3/8+o(1)` imply `L<= (3/8)L`, hence L=0. Conversely a vanishing global Weyl mean makes this suffix vanish because `n_p→∞` and `n_p=Θ(N)`. This is an **equivalent but localized gate**, not a newly proved cancellation estimate. It identifies a concrete positive-density window where a prime-clock and a source-constrained p-free cofactor must jointly cancel.

**The remaining open signed obligation (SPP-09):** show the joint sum (20) is `o_h(N)` for every fixed nonzero h on the genuine original source/zero seed. Merely bounding the isolated primary clock, applying a Galois trace, or averaging over rational seeds cannot settle it. The p=257 period-four witness, the coherent sequence `1/P_N`, the p-free cofactor spoof, and same-source irrational counterseeds are required falsifiers.

## Provenance and claim boundaries

- Original source and selected signed-lag gate: Main XIX and the Main XVIII `signed_lag_fireworks/BOUNDARY.md`.
- Finite three-channel source factorization and cofactor non-conspiracy: Main XIX `four_pole_path_interference/PROOFS.md`, source-qualified rather than assumed independent.
- Prime number theorem in fixed arithmetic progressions: classical theorem, for example `https://www.math.purdue.edu/~sahay5/imsc.pdf`, §1 and `https://www.math.tau.ac.il/~rudnick/courses/sieves2015/BrunTitchmarsh.pdf`. It is an INPUT to the asymptotic shell coverage, not a theorem implemented by the tests.
- Elementary Gauss sum, CRT, cyclotomic relative trace, and Weyl normality criterion: classical.
- All exact arithmetic code and tests included in this additive dossier; finite floating complex diagnostics are **not** certified asymptotics. No new unconditional selected signed cancellation or π-normality proof is claimed.
