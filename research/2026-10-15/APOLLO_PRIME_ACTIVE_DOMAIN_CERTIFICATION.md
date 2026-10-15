# OPERATION APOLLO PRIME-ACTIVE — Source-domain certification and authentic Suzuki shorting interface

**Date:** 2026-10-15. **Branch:** research/apollo-prime-active-domain-2026-10-15. **Parent:** research/apollo-suzuki-second-third-jet-2026-10-15 at cb7b804d8624dcf5247eac34cf59e969577c6ccb (draft PR #110). Its ancestry includes ONE OBJECT PR #106, Tate PR #103 and Phoenix II main 03db44203147a7b28d445bb9f970fa71360e78c4. **Independent PR #107:** research/tate-suzuki-zero-shift-source-range-2026-10-15 at 44d7f699dc2e3e29225d2aad0557bfb1360c97e1 was studied, NOT merged. Original SHA-pinned mathematical source was not changed. No independent RH repo, main branch, historical source or nontrivial zeros are inputs. Scholarly priority UNVERIFIED. **RH PROVED: NO.**

## 0. Exact original arithmetic source and test domain

For fixed a>0, let I_a=(-a,a), E be a fixed open subset of I_a, and f a complex smooth compact function supported in E. Write
\[
C_G=-\psi(1/4)+\log\pi=\gamma+\pi/2+3\log 2+\log\pi,\quad
b_n=\log n,\quad w_{p^k}=\frac{\log p}{\sqrt{p^k}},\quad
P_a=\{n=p^k:b_n<2a\}.
\]
The authentic completed signed Weil quadratic form, using the same imported Suzuki normalization as the parent APOLLO and SUCC AMW source, is
\[
\boxed{
Q_\zeta(f)=\mathcal E_G(f)-C_G\|f\|_2^2
+2|\langle f,\cosh(x/2)\rangle|^2
-2|\langle f,\sinh(x/2)\rangle|^2
-2\sum_{n\in P_a}w_n\operatorname{Re}\langle T_{b_n}f,f\rangle .
}\tag{S0}
\]
Here T_bf(x)=f(x+b) on the full additive log carrier, followed by the ordinary support-sensitive pairing. It is NOT a unitary compressed shift. Authentic gamma has the actual positive OU spectral decomposition
\[
\mathcal E_G(f)=\sum_{j\ge0}\beta_j
\langle f,(I-R_{\alpha_j})f\rangle,\quad
\alpha_j=(4j+1)/2,\quad\beta_j=4/(4j+1),
\quad R_\alpha(x-y)=(\alpha/2)e^{-\alpha|x-y|}.
\tag{S0-Gamma}
\]
This follows from the parent source-positive Gamma increment features by Fourier transform and distributional integration by parts, not by fitting a numerical Gram. Every Gamma summand is PSD, since the Fourier symbol of R_alpha is alpha²/(alpha²+frequency²) between 0 and 1. The original finite Euler source keeps all true p^k, completed contact, one Gamma, polar pole terms, half density and its genuine support. The original source adapter verifies Git blob SHA through suzuki_legendre_source._pinned_source; no code alterations to the source dossier.

## 1. S1 — General support-measure source coercivity theorem

Take an arbitrary FIXED open E⊂I_a of Lebesgue measure at most m, and f∈C_c^\infty(E). The nonnegative convolution kernel of R_alpha satisfies on E
\[
\sup_{x\in E}\int_E R_\alpha(x-y)\,dy\le\frac{\alpha m}{2},
\]
with the same column estimate. Schur's lemma therefore yields
\[
0\le\langle f,R_{\alpha_j}f\rangle
\le\frac{\alpha_jm}{2}\|f\|_2^2.
\]
Since beta_j alpha_j/2=1, the first J TRUE Gamma rungs give
\[
\boxed{\mathcal E_G(f)\ge (S_J-Jm)\|f\|_2^2,\quad
S_J=\sum_{j=0}^{J-1}\frac4{4j+1}.}\tag{S1-G}
\]
The omitted infinite Gamma tail is PSD and is NOT charged as negative uncertainty. The positive cosh-pole term may be dropped, the negative sinh-pole costs at most \(2m\sinh^2(a/2)\|f\|^2\), and each authentic p^k shift has absolute overlap at most \(\|f\|^2\). Therefore, with \(W_a=\sum_{n\in P_a}w_n\),
\[
\boxed{Q_\zeta(f)\ge
\big[S_J-Jm-C_G-2W_a-2m\sinh^2(a/2)\big]\|f\|_2^2.}\tag{S1}
\]
**Status:** PROVED ANALYTIC given the original signed Weil source formula. The quantifier is ALL smooth compact tests in each FIXED admissible E. Entering a rational m in software does not itself authenticate that an arbitrary E has that measure: this is an explicit mathematical domain precondition.

**Every compact interval admits sparse coercivity (S1b).** For any fixed finite a>0, P_a is finite, while S_J diverges like log J. Choose J with \(S_J>C_G+2W_a+2\), then any \(0<m_a\le1/(J+2\sinh^2(a/2))\) yields
\[
Q_\zeta(f)>\|f\|_2^2
\quad\forall f\in C_c^\infty(E),\quad E\subset I_a,\ |E|\le m_a.
\tag{S1b}
\]
This proves *conditional source-positive sparsity for every finite a*, not unrestricted Weil positivity. The m_a may shrink rapidly, and two functions on separately admissible sets can have a union outside the admissible budget. A negative Weil test in a fixed interval, if one exists, must have support larger than that interval's certified threshold. This is not a location-of-zeros theorem.

## 2. S2 — Original n=2 active at a=1/2

The SHA-checked exact rational log/source intervals establish log2<1<log3, so at a=1/2 the sole genuine original impulse is n=2 with w_2=log2/sqrt2<1/2. The original contact has C_G<43/8. The elementary bounds sinh(1/4)<1/3 and \(2m\sinh^2(1/4)<m/4\) hold on this real interval (from sinh t<=t e^t, e^(1/4)<=4/3).

Let m=1/32, J=16. The exact rational source margin
\[
\boxed{S_{16}-16/32-43/8-1-1/128>1/10}
\tag{S2-rational}
\]
is checked using fractions and strict inequality, not eigenvalues. Consequently
\[
\boxed{Q_\zeta(f)> \frac1{10}\|f\|_2^2}
\tag{S2}
\]
for EVERY complex smooth compact f supported in ANY fixed open E⊂(-1/2,1/2) with |E|<=1/32. This includes tests with nonzero true p=2 transfer; no positivity of G_{1/2} on all L²_0 is claimed.

## 3. S3 — Actual p=2 coupled two-packet LINEAR domain

The exact source certifies \(2/3<\log2<7/10\). Define
\[
U=(-7/16,-7/16+1/64),\qquad
E_2=U\cup(U+\log2)\subset(-1/2,1/2).
\]
This domain has **exact total measure** 1/32 and two genuinely disjoint packets. For any f=f_0+f_1∈C_c^\infty(E_2),
\[
|\langle T_{\log2}f,f\rangle|
\le\|f_0\|_2\|f_1\|_2
\le\frac12\|f\|_2^2.
\]
It is nontrivial: setting f_1(x)=f_0(x-log2) for any nonzero smooth f_0∈C_c^\infty(U) gives exactly \(\langle T_{\log2}f,f\rangle=\|f_0\|_2^2>0\). With this source-geometric factor 1/2 and the original w2<1/2,
\[
\boxed{Q_\zeta(f)>
\big[S_{16}-1/2-43/8-1/2-1/128\big]\|f\|_2^2
>\frac35\|f\|_2^2,\quad f\in C_c^\infty(E_2).}\tag{S3}
\]
The source-active packet is a nontrivial infinite-dimensional **linear** domain; its gamma/pole/contact and the live original p=2 shift all appear.

A separate rational polynomial calibration on the two packets uses f_0(t)=t^q(\delta-t)^q, 0<t<delta, q>=4, and its exact translate. The one-packet L² energy is delta^(4q+1)(2q)!²/(4q+1)!, and the shifted overlap is exactly that energy; hence the overlap-to-total-norm ratio is 1/2. This finite polynomial is only finitely smooth; it does NOT stand in for the universal Cc-infinity proof, which uses arbitrary smooth identical translated bumps.

## 4. S4 — FIVE genuine source impulses for every a<=1

For 0<a<=1, source.log_iv(8).lo>2 and exact original prime-power enumeration show
\[
P_a\subseteq\{2,3,4,5,7\}.
\]
n=6 is not a von Mangoldt source; n=4 is a power of the genuine prime 2. The exact SHA-pinned half-density bounds are
\[
w_2<1/2,\quad w_3<2/3,\quad w_4<3/8,\quad
w_5<3/4,\quad w_7<3/4,\quad W_a<73/24.
\]
For J=4096, use eight dyadic blocks of the genuine Gamma mass:
\[
S_{4096}=S_{16}+\sum_{k=4}^{11}\sum_{j=2^k}^{2^{k+1}-1}\frac1{j+1/4}.
\]
Each decreasing-harmonic block exceeds
\[
\log\frac{2^{k+1}+1/4}{2^k+1/4}
>\log2-\frac{1}{4\cdot2^k}
>\frac23-\frac{1}{4\cdot2^k}.
\]
Thus the rational
\[
L_{4096}=S_{16}+16/3-\sum_{k=4}^{11}\frac1{4\cdot2^k}
\]
is a **rigorous lower** for the 4096 true Gamma masses without numeric partial summation. For a<=1, \(\sinh(a/2)<1\). At m=1/16384, exact integer cross-multiplication establishes
\[
\boxed{L_{4096}-4096m-43/8-2(73/24)-2m>1/2.}\tag{S4-cert}
\]
Hence for ALL 0<a<=1 and ALL complex smooth f on every fixed open E⊂(-a,a) of |E|<=1/16384,
\[
\boxed{Q_\zeta(f)>\frac12\|f\|_2^2.}\tag{S4}
\]
The general bound permits several original prime couplings simultaneously (they were all budgeted), but still does not cover arbitrary support. All exact bounds originate in the declared original zeta source.

## 5. S5 — Isolate each of five active jets with only 16 Gamma modes

Take a=1, n∈{2,3,4,5,7}, and δ=1/128. Define
\[
U=(-1+\delta,-1+2\delta),\qquad E_n=U\cup(U+\log n).
\]
The original rigorous log-source enclosures certify both packets lie inside (-1,1), and every other active prime log m differs by strictly MORE than δ. Therefore all other original shift overlaps vanish *exactly*. The selected overlap obeys the same sharp 1/2 source geometry as S3 and is nonzero on positive translated smooth bumps. The selected original weight is strictly <3/4. With |E_n|=2δ=1/64 and J=16, the *true* source inequality is
\[
\boxed{Q_\zeta(f)>
\big[S_{16}-16/64-43/8-3/4-2/64\big]\|f\|_2^2
>\frac12\|f\|_2^2,\quad f\in C_c^\infty(E_n).}\tag{S5}
\]
This establishes five separate **source-active infinite-dimensional linear domains** with actual certified positive Hilbert contractions, including the prime power n=4 (weight log2/2). A smaller δ=1/32768 and 4096 modes also certifies a stronger coefficient >5, at the expense of much narrower support. These are different budget regimes, not a global all-test sign.

## 6. S6 — Legitimate functional-analytic domain closure

For fixed admissible E, the original Cc-infinity domain extends by continuity to H_0¹(E). In the actual Gamma jump form, its kernel behaves like 1/(2t) near t=0 and decays exponentially at infinity. The elementary estimates
\[
\|T_tf-f\|_2\le |t|\|f'\|_2,\qquad
\|T_tf-f\|_2\le 2\|f\|_2
\]
give a finite H¹ continuity modulus since \(\int_0^1t²k_G(t)dt<\infty\) and \(\int_1^\infty k_G(t)dt<\infty\). The finitely many authentic prime translations, contact and rank-two pole terms are H¹-continuous as well. S2–S5 therefore pass to H_0¹(E) by density. This does NOT assert an everywhere bounded operator on bare L²(E), nor a positive form on the whole ambient Sobolev space H_0¹(-a,a).

**Source acceptance:** the software checks strict SHA, prime-power labels, original rational contact/log/sqrt bounds, exact rational measure BUDGETS and explicit translated packet endpoints. An arbitrary claimed bound for a user-supplied E is a conditional hypothesis, not an observed or measured event. Fixed packet E_2 and E_n are source-constructed mathematical objects with certified measure and placement.
