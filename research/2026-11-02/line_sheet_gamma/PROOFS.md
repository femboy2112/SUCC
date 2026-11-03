# OPERATION CIRCLE LINE × SHEET — Gamma convolution, sublog collision, simultaneous BBP primes

**2026-11-02 · RESEARCH-ONLY · paper proofs + exact/rational and exploratory numerical oracles.**
Exact parent is draft SUCC #473 SHA 80dc4d8b54574e03843f198ff833e2add469422a, ancestor #471 global Fejér and #470 Pisot/Gamma, #468 Gamma Seam, #461 original Laurent clocks and merged Main XIX. Sibling #472 oily×ħ was inspected separately; it is NOT automatically imported. Preserve the authentic ORIGINAL four signed BBP poles, literal U₀=0, frozen archives, formal/Lean, canonical source, workflows and main. Base-16 π normality, RH and the genuine original-source signed/collision saving remain OPEN.

## LS-01. The continuous Γ defect is a line; its square is literally a positive sheet

For **every real s>0**, put \(\gamma=\) Euler–Mascheroni, \(\psi=\Gamma'/\Gamma\), and

\[
D(s)=\psi(s+1)-\log s,\qquad
\kappa(t)=\frac1t-\frac1{e^t-1}>0\quad(t>0).
\]

The classical digamma integral (NIST DLMF §5.9.13, https://dlmf.nist.gov/5.9.E13), plus \(\psi(s+1)=\psi(s)+1/s\), gives the exact universal one-dimensional Laplace representation

\[
\boxed{D(s)=\int_0^\infty e^{-st}\kappa(t)\,dt.}\tag{LS-01}
\]

For integers n≥1, \(D(n)=H_n-\log n-\gamma\). Square the integral and apply Tonelli (positive integrands); change variables \(t=u+v\) on the two-dimensional first quadrant:

\[
\boxed{\frac{D(s)^2}{16}
=\int_{u,v\ge0}\frac{e^{-s(u+v)}}{16}\kappa(u)\kappa(v)\,du\,dv
=\int_0^\infty e^{-st}\,Q_{\rm sheet}(t)\,dt,}
\quad Q_{\rm sheet}(t)=\frac1{16}\int_0^t\kappa(u)\kappa(t-u)\,du.\tag{LS-02}
\]

The “line→sheet” language now has an OPERATIONAL meaning: two separately regulated finite-to-continuum lines are convolved over a genuine \((u,v)\) sheet; the \(u+v=t\) diagonal fibers project that positive sheet back to a one-dimensional Laplace kernel. This is classical convolution geometry, not a topology proof or a quantum speedup.

For the ORIGINAL signed BBP source and literal \(U_0=0\),

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
P(x)=(1-x)(x^2+2)(x^2+2x+2),
\]

the inherited exact positive Beta/Gamma tail has the **real-continuation**

\[
T(s)=\int_0^1\frac{x^{8s}P(x)}{16-x^8}\,dx
=\int_0^\infty e^{-st}\,Q_{\rm BBP}(t)\,dt,\quad
\boxed{Q_{\rm BBP}(t)=\frac{e^{-t/8}P(e^{-t/8})}{8(16-e^{-t})}.}\tag{LS-03}
\]

For integer n, this is exactly the original Green tail \(T_n=16^n(\pi/16)-U_n\); it is NOT an altered source or an assumed stochastic average.

## LS-02. NEW STRONG POINTWISE KERNEL DOMINATION — every positive real scale

**Theorem (proved analytically).** For **every t>0**,

\[
\boxed{0<Q_{\rm BBP}(t)<Q_{\rm sheet}(t).}\tag{LS-04}
\]

Detailed constructive proof, with NO numerical interval assumptions:

**Lower bounds on κ.** The classical Bernoulli inequality

\[
\frac1{e^t-1}\le\frac1t-\frac12+\frac t{12}
\]

follows by expanding \((e^t-1)(1-t/2+t^2/12)-t\): all coefficients through \(t^4\) vanish, and for each \(m\ge5\) the coefficient is \((m-3)(m-4)/(12m!)>0\). Thus \(\kappa(t)\ge1/2-t/12\). Separately, \(e^t-1\ge t+t^2/2\) gives \(\kappa(t)\ge1/(t+2)\). For \(0<t\le6\), both factors of the first lower bound are nonnegative inside the convolution, so

\[
\boxed{Q_{\rm sheet}(t)\ge L(t):=\frac t{64}-\frac{t^2}{384}+\frac{t^3}{13824}
\quad(0<t\le6).}\tag{LS-05}
\]

For every \(t>0\), the second bound yields

\[
\boxed{Q_{\rm sheet}(t)\ge\frac{\log(1+t/2)}{8(t+4)}.}\tag{LS-06}
\]

**Case 0<t≤4.** Write \(x=e^{-t/8}\ge e^{-1/2}>1/2\), and \(R(x)=x^4-x^3-x^2+3x-1\). The exact polynomial identity is

\[
x(16-x^8)-(x^2+2)(x^2+2x+2)
=(1-x)(x^2+2)(x^2+2x+2)R(x).
\]

Here \(R(1/2)=3/16>0\) and
\(R'(x)=(1-x)(x+3)+2x^2(2x-1)\ge0\) on \([1/2,1]\). Therefore

\[
Q_{\rm BBP}(t)
\le\frac{x^2(1-x)}8
\le\frac{-x^2\log x}{8}
=\frac{t e^{-t/4}}{64}.
\]

For \(0\le z=t/4\le1\), the function
\(g(z)=1-2z/3+2z^2/27-e^{-z}\) is concave since
\(g''(z)=4/27-e^{-z}<0\), and \(g(0)=0,\ g(1)=11/27-1/e>0\). By its chord, \(g(z)\ge0\). Hence
\(e^{-t/4}\le1-t/6+t^2/216\), so \(Q_{\rm BBP}(t)\le L(t)\).

**Case 4≤t≤5.** Since \(0<x<1\),
\(Q_{\rm BBP}\le(4x-2x^4)/(8\cdot15)\le
3\,2^{-1/3}/120<1/48\).
The polynomial \(L(t)\) decreases on [4,6], and
\(L(5)=305/13824>1/48\). Thus \(Q_{\rm BBP}<L\).

**Case 5≤t≤6.** The bound
\(e^{5/8}>1+5/8+(5/8)^2/2>20/11\) gives \(x<11/20\). The rational function \(xP(x)/(8(16-x^8))\) is strictly increasing for \(0<x≤11/20\): its derivative numerator is \(16(P+xP')+x^8(7P-xP')>0\), because \(P+xP'=4-8x^3-5x^4-6x^5>0\) and \(P>0>P'\). Consequently

\[
Q_{\rm BBP}(t)\le Q_{\rm BBP}(x=11/20)
=\frac{4950}{326599}<\frac1{64}=L(6)\le L(t).
\]

**Case t≥6.** Since \(P(x)\le4\) and \(16-x^8\ge15\),
\(Q_{\rm BBP}(t)\le e^{-t/8}/30\). Equation LS-06 dominates this for t≥6 because
\((t+4)e^{-t/8}\) decreases for t≥4, while \((15/4)\log(1+t/2)\) increases; at t=6 the former is \(10e^{-3/4}<5\), the latter is \((15/4)\log4>5\). These strict elementary inequalities follow from \(e^{3/4}>1+3/4+9/32>2\) and \(\log2>2/3\) (the positive artanh series). This finishes every t>0.

**Consequences (stronger than inherited PGC-06):**

\[
\boxed{0<T(s)<D(s)^2/16\quad\text{FOR EVERY REAL }s>0.}\tag{LS-07}
\]

The defect \(W(s)=D(s)^2/16-T(s)=\int_0^\infty e^{-st}(Q_{\rm sheet}-Q_{\rm BBP})\,dt\) is the Laplace transform of a strictly positive measure, hence is **STRICTLY COMPLETELY MONOTONE**:

\[
\boxed{(-1)^m W^{(m)}(s)=\int_0^\infty t^m e^{-st}(Q_{\rm sheet}-Q_{\rm BBP})dt>0
\quad\forall m\in\mathbb N_0,\ s>0.}\tag{LS-08}
\]

Taylor expansions at the continuum boundary t=0 (exact algebra):
\[
\kappa(t)=\tfrac12-\tfrac t{12}+\tfrac{t^3}{720}+O(t^5),
\quad Q_{\rm sheet}(t)=\tfrac t{64}-\tfrac{t^2}{384}+\tfrac{t^3}{13824}+O(t^4),
\]
\[
Q_{\rm BBP}(t)=\tfrac t{64}-\tfrac{7t^2}{1024}+\tfrac{55t^3}{24576}+O(t^4),
\quad Q_{\rm sheet}-Q_{\rm BBP}
=\boxed{\frac{13}{3072}t^2-\frac{479}{221184}t^3+O(t^4).}
\]

Watson's lemma or dominated elementary Laplace asymptotics recover the sharp previously derived cubic gap
\[
\boxed{\lim_{s\to\infty}s^3W(s)=13/1536.}\tag{LS-09}
\]

These are genuine analytic/global source constraints with a positive geometric sheet, but they are NOT a signed bound on temporal real-circle correlations. The same ORIGINAL four-pole forcing with the nonnormal changed real seed \(-\pi/16+1/5\) has the same T(s), Q kernels, and W(s).

## LS-03. WEAKER π-normality route: sublogarithmic self-resolution collision, not bounded

Let \(A=2^j\) and \(U_n\) be the original rational zero-seeded BBP states. Define the exact self-scale occupancy and energy from parent PGC-10:

\[
v_i(A)=\#\{A\le n<2A:\lfloor A\{U_n\}\rfloor=i\},\qquad
\mathscr C_A=\frac1A\sum_{i=0}^{A-1}v_i(A)^2.
\]

Parent #473 proved **bounded** \(\mathscr C_A\) is sufficient. We can weaken it to an unbounded log-saving:

\[
\boxed{\mathscr C_A=o(\log A)\quad (A=2^j\to\infty)
\Longrightarrow \pi\text{ normal base }16.}\tag{LS-10}
\]

**Full proof with quantified moving scales.** Put \(N=L^2,M=L+1\), \(A_0=2^{\lceil\log_2 M\rceil}\in[M,2M)\), and
\(C_*(L)=\max\{\mathscr C_A:A\text{ dyadic},A_0\le A<N\}\).
For an original source epoch \([A,2A)\), the parent fine→coarse lemma gives
\(\sum_j u_j(A,M)^2\le(A^2/M+2A)\mathscr C_A\).
The exact original Γ tail transports the rational completion \(\{16^n\alpha_N\}\) by fewer than one M-bin for each \(n\ge A_0\), so its (possibly partial) epoch histogram has ℓ² norm ≤3 times the FULL original source-epoch norm. The first <\(A_0\) times contribute at most \(A_0<2M\). Minkowski, \(\sum A<2N\), and \(\sum\sqrt A\le\sqrt N/(1-2^{-1/2})\) give the exact finite bound

\[
\boxed{
\sqrt{\mathscr B_L}\le
\frac{2M^{3/2}}N
+6\sqrt{C_*(L)}
+\frac{3\sqrt2}{1-2^{-1/2}}\sqrt{\frac{MC_*(L)}N},
\quad
\mathscr B_L=\frac{M}{N^2}\sum_jc_j^2,
}\tag{LS-11}
\]

where \(c_j\) is the ONE exact \(M\)-bin histogram of the original rational \(\alpha_N\) completion. If \(\mathscr C_A=o(\log A)\), then \(C_*(L)=o(\log L)\) uniformly over epochs \(A_0\le A<N\). With \(M\asymp L,N=L^2\), LS-11 gives \(\mathscr B_L=o(\log L)\). The universal positive Fejér bound from PGC-05 yields
\(\mathscr Q_L\le(3+\pi^2/12)\mathscr B_L=o(\log L)\).
Parent #471's exact Gamma transport is O(L⁻⁴), hence its completed π-orbit Fejér energy is likewise \(o(\log L)\).
For each FIXED nonzero harmonic h, choose \(K_L=\lfloor\log_{16}(L/(2|h|))\rfloor+1\sim\log_{16}L\). The exact radix Ward ladder gives
\[
|c_{L^2}(h)|\le\sqrt{(\mathscr Q_L+O(L^{-4})-1)/K_L}+(K_L-1)/L^2=o(1).
\]
Arbitrary prefixes follow because consecutive squares differ by O(L) steps. Weyl proves base-16 π normality **CONDITIONALLY**.

If the source can be shown to satisfy the quantitative but still OPEN
\(\mathscr C_A=O((\log A)^{1-\delta})\) for some \(0<\delta\le1\), then the same proof yields a conditional effective harmonic rate \(c_N(h)=O_{h,\delta}((\log N)^{-\delta/2})\) (with constants depending on the assumed source bound).

**Sharp firewall — sufficient, not necessary.** A base-16 normal number may FAIL LS-10: begin with a known normal digit sequence and replace digits with zero in disjoint intervals beginning at \(A_j=2^{j^2}\), of length \(\lfloor A_j^{3/4}\rfloor\). The modified-digit set has zero density, so normality is unchanged, but \(\gg A_j^{3/4}\) successive circle shifts in the epoch land in the same first \(1/A_j\) bin, and \(\mathscr C_{A_j}\gg A_j^{1/2}\). Thus LS-10 is an extra arithmetic regularity condition, not disguised necessity for normality. The same-original-four-pole real coherent counterseed violates it even more sharply (\(\mathscr C_A\asymp A\)).

## LS-04. Simultaneous ORIGINAL newborn primes: a prime-clock tensor sheet

For dyadic \(A=2^j\), let \(\mathcal P_A=\{p=8k+1\text{ prime}: A/2\le k<A\}\). Classical PNT in the fixed progression p≡1 (mod 8) gives
\(|\mathcal P_A|\sim A/(2\log A)\). EVERY \(p\in\mathcal P_A\), simultaneously, has an exact original-source clean interval covering ALL \(n\in[A,2A)\).

For any such n, put \(b_p=(p+7)/8=k+1\) and
\(a_{p,n}=4\,16^{n-b_p}\bmod p\in\{0,\ldots,p-1\}\). The original exact rational state has p-valuation −1. Consequently, with \(\mathbb Z_{(\mathcal P_A)}\) denoting rationals whose reduced denominator is coprime to every p in the set,

\[
\boxed{U_n=\sum_{p\in\mathcal P_A}\frac{a_{p,n}}p+C_n,\qquad
C_n\in\mathbb Z_{(\mathcal P_A)}.}\tag{LS-12}
\]

This is exact simultaneous prime-plus-complementary-real embedding at the ORIGINAL zero seed, not a source substitution. It gives \(e(hU_n)=e(hC_n)\prod_p\zeta_p^{h a_{p,n}}\).

For any finite epoch subset and fixed nonzero integer h with \(p\nmid h\) for all p in the family, the exact joint Galois average (Ramanujan sums, no randomness) is

\[
\boxed{
\frac1{\prod_p(p-1)}\sum_{u_p\in\mathbb F_p^\times}
\left|\sum_n e(hC_n)\prod_p\zeta_p^{h u_pa_{p,n}}\right|^2
=\sum_{n,m}e(h(C_n-C_m))
\prod_{p\in\mathcal P_A}
\begin{cases}
1,&p\mid 16^{n-m}-1,\\
-1/(p-1),&\text{otherwise.}
\end{cases}
}\tag{LS-13}
\]

The product over p is an EXACT pairwise Galois kernel. It is **NOT** the selected u_p=1 embedding.

**New quantitative short-lag Galois firewall.** By PNT-AP, for all sufficiently large A, \(|\mathcal P_A|\ge A/(3\log A)\). For any \(1\le d=|n-m|\le A/(12\log16)\), an alias prime must divide \(16^d-1\); since each p≥4A, at most \(d\log16/\log(4A)\le A/(12\log A)\) such primes exist. Therefore at least \(A/(4\log A)\) primes are NONALIAS, and the exact pairwise Galois product obeys

\[
\boxed{\left|\prod_{p\in\mathcal P_A}c_p(16^d-1)\right|
\le(4A)^{-A/(4\log A)}\le e^{-A/4}.}\tag{LS-14}
\]

So simultaneous prime clocks produce **exponentially** small Galois-averaged short-lag coherence for original source epochs, despite possible small order at an individual p (p=257 has order four). This is a genuine arithmetic enhancement over one-prime average; still not an Archimedean selected saving.

**Hostile source-map obstruction:** for ANY finite such clock chart, choose an integer Q coprime to all its primes, and set \(C_n^*=-\mathrm{round}(Q\sum_p a_{p,n}/p)/Q\). Then all complementary denominators remain prime-free, but every SELECTED phase \(\sum_p a_{p,n}/p+C_n^*\) lies within \(1/(2Q)\) of an integer, giving \(|A^{-1}\sum_ne(hU_n^*)|\ge1-\pi|h|/Q\). This counterfeit does NOT obey the original BBP forcing and zero seed; it decisively refutes any inference from multi-prime clocks, exact Galois average or p-free denominator types ALONE to π normality.

## LS-05. What the circle/line/sheet connection does and does not buy

There are TWO type-correct positive sheets:

1. **Gamma source sheet:** the genuine 2D Laplace convolution \(\kappa(u)\kappa(v)\) and the original-source strictly dominated real-continuum kernel \(Q_{\rm BBP}\). This yields positive, completely monotone analytic defects and exact phase-transport costs, for all real scales.
2. **Real-circle Fourier sheet:** the Fejér kernel is \((H+1)^{-1}|\sum_{j=0}^He(j(x-y))|^2\). It is the square of a one-dimensional Fourier line, measuring a 2-time phase-coherence sheet. Its energy has the same exact positive Gram/purity identity already found by SUCC #296.

The missing mathematical arrow between those two sheets is **not** positivity or a visual identification of their dimensions: it is the original selected real cofactor/carry estimate LS-10, or an alternative original source-specific signed dyadic loss. Neither pointwise Gamma kernel domination nor exponentially small Galois AVERAGE proves the selected real-circle cancellation.

**Ledger:** LS-01/02 positive convolution and strict all-real kernel dominance = **paper PROVED**, with classical Laplace/coth/Bernoulli ingredients attributed; LS-03 sublogarithmic conditional normality and its normal-but-failing counterexample = **paper PROVED as implication**, source premise **OPEN**; LS-04 simultaneous original CRT and exponential short-lag Galois-average bound = **paper PROVED**, selected real saving **OPEN**. No Lean proof compilation, independent mathematical referee or all-horizon numerical extrapolation is claimed. A false assertion of π normality is explicitly excluded.
