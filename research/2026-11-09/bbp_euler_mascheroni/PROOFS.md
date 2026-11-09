# BBP Euler–Mascheroni finite part × Gamma16 Mellin jet × q-divisor spectrum

**Date:** 2026-11-09. Research child of Γ16 draft #568 at `c0e5681762d0c13b38fb14a76937db17a9658e95`. **Original zero-selected BBP base-16 normality OPEN.** All new results are paper/exact rational derivations, checked locally, without global scholarly-priority claims. The source, archive, and formal contracts remain unchanged. Constants defined here are *observer- and clock-normalization dependent*: there is no claim of a uniquely canonical “BBP Euler constant” independent of that choice.

## BGEM-01 — Unchanged four-pole source and the Gamma16 block

The source is

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

The inherited positive Laplace realization (Oily Macaroni III, Γ16 #568) is

\[
Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}>0\ (x>0),\qquad
r(n)=\int_0^\infty e^{-(8n-7)x}Q(x)\,dx,
\]

with $Q(0)=0$, $Q'(0)=15$, $Q''(0)=-59$, and $Q'''(0)=243=3^5=2\cdot3^3+4^3+5^3$.

For every positive integer block size $g$ define

\[
R_g(k)=\sum_{j=1}^g16^{g-j}r(g(k-1)+j).
\]

From #565/#568, the genuine zero-origin radix-$16^g$ path obeys $U_{gk}=16^gU_{g(k-1)}+R_g(k)$. Exactly

\[
R_g(k)=\int_0^\infty e^{-a_g(k)x}Q_g(x)\,dx,\quad
 a_g(k)=8g(k-1)+1,\quad
Q_g(x)=Q(x)\sum_{j=0}^{g-1}16^{g-1-j}e^{-8jx}.
\]

All original signed poles are retained. The multiplier is $\mathcal B_g(t)=\sum_{j<g}16^{g-1-j}t^j=16^{g-1}[g]_{t/16}=16^{g-1}\Gamma_{t/16}(g+1)/\Gamma_{t/16}(g)$ by the **classical** $q$-Gamma recurrence [NIST DLMF 5.18.7](https://dlmf.nist.gov/5.18.E7). That factor is universal for any source grouped in radix 16, not BBP-specific.

## BGEM-02 — Exact BBP-modified harmonic-log finite part (PROVED)

For each fixed $g$, positivity and the simple endpoint zero give, as $k\to\infty$,

\[
R_g(k)=\frac{Q_g'(0)}{a_g(k)^2}+O_g(a_g(k)^{-3})
\sim\frac{16^g-1}{64g^2k^2}.
\]

Therefore the genuine positive source's telescoping logarithmic free energy has an absolutely convergent harmonic-renormalized finite part:

\[
\mathcal F_g:=\lim_{N\to\infty}\left[
 \sum_{k=1}^{N-1}\log\frac{R_g(k)}{R_g(k+1)}-2H_{N-1}
\right]
=\log\frac{64g^2R_g(1)}{16^g-1}-2\gamma.
\tag{BGEM2}
\]

Absolute convergence of the stepwise difference follows from the full $k^{-2}(1+O_g(k^{-1}))$ expansion, which makes each subtracted summand $O_g(k^{-2})$. The expression does **not** depend on any π digit sequence or on frequency averages. The ungrouped $g=1$ case reduces exactly to the prior Oily Macaroni III formula $\log(3008/225)-2\gamma$; it is **not** a newly discovered finite-part mechanism.

To use the **original source-time clock** $gN$ rather than the grouped clock $N$, remove the explicit $2\log g$:

\[
\boxed{\gamma_g^{\rm BBP}:=\lim_{N\to\infty}\left[H_{N-1}+\log g-\tfrac12\log\frac{R_g(1)}{R_g(N)}\right]
=\gamma-\frac12\log C_g},\qquad
C_g=\frac{64R_g(1)}{16^g-1}\in\mathbb Q_{>0}.
\tag{BGEM3}
\]

**Type and status:** $C_g$ is an exact positive rational source invariant at the declared block clock; $\gamma_g^{\rm BBP}$ is a **defined** finite-part observable equal to the classical $\gamma$ plus the logarithm of a rational. Neither is generally an algebraic number. A changed clock/normalization changes this constant. “BBP–Euler–Mascheroni” is a mathematical name for this declared observable, not a separate established classical universal constant.

## BGEM-03 — Exact π at the large-block boundary, with finite error (PROVED, classical BBP input)

Set $\alpha=\sum_{n\ge1}16^{-n}r(n)=\pi/16$ by the **classical BBP formula**, and $\alpha_g=\sum_{n=1}^g16^{-n}r(n)$. Then

\[
R_g(1)=16^g\alpha_g,\quad
C_g=\frac{64\alpha_g}{1-16^{-g}},\quad
\boxed{\lim_{g\to\infty}C_g=64\alpha=4\pi}.
\tag{BGEM4}
\]

Thus $\gamma_g^{\rm BBP}\to\boxed{\gamma-\frac12\log(4\pi)}\approx-0.68829645858311253588$. **This uses the already-known period identity; it is not an independent derivation of π or its normality.**

In fact, with the inherited positive Green tail $T_g=\sum_{j\ge1}16^{-j}r(g+j)$, the *exact* error formula is

\[
\boxed{C_g-4\pi=\frac{64\cdot16^{-g}}{1-16^{-g}}(\alpha-T_g).}
\tag{BGEM5}
\]

Since $0<T_g\le r(g+1)/15\le r(2)/15=106/12285<r(1)/16\le\alpha$ for all $g\ge1$, the difference is **strictly positive**. Hence every finite $\gamma_g^{\rm BBP}$ is strictly *below* its $\gamma-\frac12\log(4\pi)$ limit. The positive source $r(n)$ is strictly decreasing, so $C_g=(64/15)$ times the positive-$16^{-j}$ weighted mean of $r(1),\ldots,r(g)$ strictly **decreases** with $g$. Thus $\gamma_g^{\rm BBP}$ strictly **increases** to its limit. The upper error follows from $\alpha\le r(1)/15=47/225$:

\[
0<C_g-4\pi<\frac{64\cdot16^{-g}}{1-16^{-g}}\frac{47}{225}.
\tag{BGEM6}
\]

The limits are *iterated*: first $N\to\infty$ at fixed $g$ in BGEM3; then $g\to\infty$. The endpoint $g=\infty$ is not one physical infinite-step macrotransition.

## BGEM-04 — A distinct local Mellin/Euler deformation, sensitive to the four poles (PROVED)

For $a>0$ and fixed $g$, let

\[
Z_g(a)=\int_0^\infty e^{-ax}Q_g(x)\,dx
=\sum_{j=0}^{g-1}\sum_{(d,w)\in\{(0,4),(3,-2),(4,-1),(5,-1)\}}
\frac{16^{g-1-j}w}{a+8j+d}>0,
\]

and $d\mu_{a,g}=e^{-ax}Q_g(x)dx/Z_g(a)$. Its exactly defined Mellin transform (for $\Re s>-1$, with cancellation allowing further continuation) is

\[
M_{a,g}(s)=\mathbb E_{\mu_{a,g}}[(aX)^s]
=\frac{a^s\Gamma(1+s)}{Z_g(a)}
\sum_{j,d}\frac{16^{g-1-j}w_d}{(a+8j+d)^{1+s}}.
\]

The standardized Gamma(2) limit has $\mathbb E\log Y=\psi(2)=1-\gamma$ [DLMF §5.4](https://dlmf.nist.gov/5.4). Define the **local** Euler deviation

\[
\gamma^{\rm Mellin}_{a,g}:=1-\mathbb E_{\mu_{a,g}}\log(aX).
\]

Then **exactly**, not asymptotically,

\[
\boxed{\gamma^{\rm Mellin}_{a,g}=\gamma+1+
\frac1{Z_g(a)}\sum_{j,d}\frac{16^{g-1-j}w_d}{a+8j+d}
\log\frac{a+8j+d}{a}.}
\tag{BGEM7}
\]

For positive integer $a$, this is $\gamma+1$ plus a *finite rational-linear combination of $\log p$ over the ordinary prime factors of $a$ and $a+8j+d$*. For example at $g=a=1$:

\[
\gamma^{\rm Mellin}_{1,1}=\gamma+1-\frac{35}{94}\log2-\frac5{94}\log3-\frac3{47}\log5.
\]

As $a\to\infty$ for fixed $g$, $aX\Rightarrow\mathrm{Gamma}(2,1)$. The precise source endpoint jets are

\[
Q_g'(0)=16^g-1,\quad
Q_g''(0)=-59\frac{16^g-1}{15}
-240\frac{16^g-16g+g-1}{225}.
\]

Taylor/Laplace expansion with a dominated logarithmic moment and $\mathrm{Cov}_{\Gamma(2)}(Y,\log Y)=1$ yields

\[
\boxed{\gamma^{\rm Mellin}_{a,g}
=\gamma+\left(\frac52-\frac{8g}{16^g-1}\right)\frac1a+O_g(a^{-2}).}
\tag{BGEM8}
\]

At $g=1$ the $1/a$ coefficient is $59/30$. At $g=2$ it is $1243/510$. It tends to $5/2$ as $g\to\infty$. **This coefficient is source-specific:** a two-pole positive source $Q_*(x)=1-e^{-x}$ has the *same* universal q-Gamma blocking factor and the same Gamma(2) limit, but has coefficient $(1/2)+8\sum_jj16^{g-1-j}/\sum_j16^{g-1-j}$, smaller by exactly $22/15$. Hence the q-Gamma factor alone cannot determine the BBP Mellin Euler correction.

**Do not identify BGEM3 and BGEM7.** They are different declared observables (harmonic-time finite part vs. normalized *one-time* Mellin log moment). They share $\gamma$ and the original source, but are not the same invariant.

## BGEM-05 — Genuine source prime support: 27 and 31 survive (PROVED finite exact arithmetic)

The original *reduced* rationals are

\[
r(7)=\frac{5273}{911547},\quad 911547=3^3\cdot 7^2\cdot13\cdot53;
\qquad r(8)=\frac{776}{179645},\quad179645=5\cdot19\cdot31\cdot61.
\]

Thus $v_3(r(7))=-3$ and $v_{31}(r(8))=-1$. The first six terms have $v_3(r(j))\ge-2$, and the first seven have $v_{31}(r(j))\ge0$. Because multiplying by powers of 16 does not change these odd-prime valuations, the unique **new most singular** source term at the indicated birth forces

\[
\boxed{v_3(R_8(1))=-3,\qquad v_{31}(R_8(1))=-1.}
\]

For the chosen harmonic-clock renormalization $C_8=64R_8(1)/(16^8-1)$, $v_3(16^8-1)=1$ and $31\nmid(16^8-1)$ (the multiplicative order of 16 mod31 is 5). Therefore

\[
\boxed{v_3(C_8)=-4,\qquad v_{31}(C_8)=-1.}
\]

Explicitly the reduced rational is

\[
C_8=\frac{8361553080369561496666886470144}{665391252178290169344635447625}.
\]

The denominator also contains many other odd primes, including 257 and 65537. **“Prime support” here means factorization of the rational argument inside the chosen logarithm**, or factorization of individual Mellin-log arguments. It does *not* define p-adic valuations of $\gamma$ or $\log\pi$, and does not assert that 3 and 31 uniquely select the BBP source. The power 27 is **not itself a prime**; it is the third power of the exceptional prime 3.

In BGEM7 for $a=1,g=8$, $\log31$ also has the *exact nonzero* coefficient $-1/(62R_8(1))$: it comes uniquely from the original $-1/(8n-2)$ pole at $n=8$. No analytic continuation or fitted prime list was used to find it. This is a second, independent type of prime support of the finite logarithmic jet.

## BGEM-06 — Canonical q-Euler constant, Lambert series and nonselective prime support (CLASSICAL / PROVED FORMULA)

The $q$-Gamma ratio of BGEM1 by itself does **not** specify the logarithmic derivative of a Gamma function at 1. Choose **the canonical DLMF q-Gamma product** $\Gamma_q(z)=(q;q)_\infty(1-q)^{1-z}/(q^z;q)_\infty$ for $0<q<1$ and define $\gamma_q=-\psi_q(1)$. Direct logarithmic differentiation gives

\[
\boxed{\gamma_q=\log(1-q)-(\log q)\sum_{n=1}^\infty\frac{q^n}{1-q^n}}.
\tag{BGEM9}
\]

At the Gamma16 source endpoint $x=0$, $q_x=e^{-8x}/16\to1/16$. Thus

\[
\boxed{\gamma_{1/16}=\log(15/16)+\log16\sum_{n\ge1}\frac1{16^n-1}}
\approx0.1318958182223980194674209652162561372746504.
\]

The series is rigorously tail-bounded, for any finite $m\ge0$, by

\[
0<\sum_{n>m}\frac1{16^n-1}
<\frac{16^{-m}}{15(1-16^{-(m+1)})}.
\]

Its Lambert/Dirichlet divisor identity is

\[
\sum_{n\ge1}\frac{q^n}{1-q^n}=\sum_{t\ge1}\tau(t)q^t,
\quad\tau(t)=\prod_{p^a\parallel t}(a+1).
\]

Here $\tau(27)=4$ and $\tau(31)=2$. In the *different* denominator-event clock $1/(16^n-1)$, the first multiple of 31 appears at $n=5$ ($\operatorname{ord}_{31}(16)=5$), while $3^3\mid 16^n-1$ first occurs at $n=9$ ($\operatorname{ord}_{27}(16)=9$). **All odd primes** divide one of the denominators $16^n-1$, since 16 has finite multiplicative order modulo each odd prime. Consequently the universal q-Euler constant has broad termwise prime support; it does **not** by itself explain selected π, despite containing the queried factors at identifiable arithmetic orders. This avoids mistaking the q-Gamma factor's universal arithmetic for source-specific prime births at original times 7 and 8.

A critical uniqueness trap: replacing $\Gamma_q(z)$ by $e^{t\sin(2\pi z)}\Gamma_q(z)$ for a real $t$ preserves its ratio $\Gamma_q(z+1)/\Gamma_q(z)$ **and the integer normalizations** $\Gamma_q(1)=\Gamma_q(2)=1$, but shifts $-\psi_q(1)$ by $-2\pi t$. The DLMF product/log-convexity is indispensable for the particular q-Euler constant. Therefore the finite blocking polynomial (which samples only integer ratios) does not itself select $\gamma_q$ or $\gamma_g^{\rm BBP}$.

## BGEM-07 — Non-normality firewall and what could change the verdict

All of BGEM1–06, including $C_g\to4\pi$, depend on **the forcing and its completed period**, not on original-zero digit frequencies. A coherent wrong seed $s=-\pi/16$ has the *same source forcing, every $R_g(k)$, every $Q_g$, the same two Gamma deformations, and the same $C_g\to4\pi$*, but its completed radix-16 orbit is the fixed point zero and nonnormal. Even the **same leading Gamma(2) rank and q-Gamma blocker** are shared by two-pole sources with different periods. These provide exact counterexamples to any claim that BBP–Euler finite-part values, the numbers 27/31, or Gamma blocking alone imply normality.

The **additional** condition that would matter is an authenticated, original-zero **signed real-phase/carry correlation estimate** surviving the full Yoneda/future-tail matrix of #568 and rejecting coherent seeds. The Gamma deformations can serve as *source-identification priors or normalization controls* but are not statistically discriminating probes for normality unless coupled to time-dependent real phases. A theorem must pay the old #544 signed prime/complement covariance or #565 conditional first-digit Haar defect, including source-moving boundary costs. No such estimate is proved here.

**Claim ledger:** source q-Mellin first jets and block-clock constants PROVED PAPER; π-normality OPEN; independence of competing mathematical derivations is partial (same source, different algorithms), not external peer review; numerical checks OBSERVED FINITE; claims of new global mathematical priority UNVERIFIED.
