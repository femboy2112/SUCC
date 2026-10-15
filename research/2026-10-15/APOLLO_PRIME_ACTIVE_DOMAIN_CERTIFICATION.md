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


## 7. S7 — A true source-positive Hilbert contraction on each activated domain

The parent APOLLO K2 constructs *independent* authentic Hilbert feature spaces H_plus and H_minus with true original point kernel
\[
K_g(x,y)=\langle\Phi_+(x),\Phi_+(y)\rangle
-\langle\Phi_-(x),\Phi_-(y)\rangle
\]
for every x,y in a fixed bounded source window. This exact signed decomposition retains true Gamma OU modes, true prime-powers with their log/sqrt weights, one contact, and both pole signs. Neither feature family was synthesized by assuming RH.

For any one FIXED admissible small-support E above, define for f∈C_c^\infty(E)
\[
A_\pm(f)=\int_{-a}^a f'(x)\Phi_\pm(x)\,dx.
\]
The Bochner integrals are well-defined since each source feature is continuous and bounded on the compact test window, and f' has compact support. Source identification plus two integrations by parts gives
\[
\|A_+f\|^2-\|A_-f\|^2=Q_\zeta(f)\ge c_E\|f\|_2^2.
\]
Consequently the map \(T_E^0(A_+f)=A_-f\) is WELL-DEFINED and contractive on the positive-feature image: if A_+f=0 then A_-f=0, and \(\|T_E^0z\|\le\|z\|\). It extends to the closed source-positive feature span. The Hilbert feature
\[
\Psi_E(f)=(I-T_E^*T_E)^{1/2}A_+(f)
\]
therefore obeys the **authentic source** polarized identity
\[
\boxed{\langle\Psi_E(f),\Psi_E(h)\rangle=Q_\zeta(f,h)
\quad\forall f,h\in C_c^\infty(E).}\tag{S7}
\]

This is NOT a positive feature factor for K_g at all points in [-a,a]. It is a proof-earned contraction **on each certified fixed linear test domain**; the quadratic sign was obtained independently by Gamma/sparsity and original Euler bounds. S7 is genuine progress through nontrivial prime-active Hilbert domains, but does not produce RH or the global all-a T_a. Naively gluing independently constructed positive/negative point features across prime births is not legitimate: APOLLO K5 proves those births can be signed-neutral while altering both Hilbert feature carriers.

## 8. S8 — Exact domain connection to PR #107's Suzuki low/high Neumann shorting

The parallel TATE×SUZUKI PR #107 (head 44d7f699dc2e3e29225d2aad0557bfb1360c97e1 at audit) proves an authentic first-prime a=1/2 cross-range theorem conditional on the pinned AMW-06B high-sector source inequality. Its **low Schur sign remains UNVERIFIED**. No code from this concurrent branch is cherry-picked or rewritten here.

On H=L²_0(-1/2,1/2), let G_{1/2} be the exact signed Suzuki compact operator, V the mean-zero Neumann primitive, and K=V*V=(-Δ_N)^-1. For every f∈C_c^\infty(E_2) set u=i f'. Then u∈H, V u=i f, and Suzuki's true source pairing yields
\[
\boxed{
\langle G_{1/2}u,u\rangle
=Q_\zeta(f)>\frac35\|f\|_2^2
=\frac35\langle Ku,u\rangle .
}\tag{S8}
\]
This is **Neumann-relative** (K), not a false constant L² gap for compact G. Its test vectors generally have BOTH low and high 30-Legendre components. Restriction to the sparse packet domain does not survive arbitrary orthogonal P_low / P_high projection, so this is NOT evidence that the full low Schur A-R_0≥0.

The precise moment-map distinction is instructive. On ANY nonempty open packet U, the map \(f\mapsto(\int x^jf(x)dx)_{j<30}\) from C_c^\infinity(U) is SURJECTIVE. If a nonzero linear combination of these moments vanished on all f, its representing polynomial would vanish as a distribution on U and hence be identically zero, contradiction. A rational Vandermonde of 30 distinct points inside the original p2 packet is independently checked with exact Fraction arithmetic. For u=i f', integration by parts gives pairings with Legendre modes 1..30 through polynomials P_k' of degrees 0..29. Their leading coefficients are nonzero, so the low Legendre projection map is also SURJECTIVE.

**Critical missing quantitative ingredient:** such a low moment realization can carry arbitrarily large high-sector or derivative norm as U becomes narrow. Surjectivity gives no uniformly bounded inverse and no sign of the authentic low Schur. The S7 local contraction on one sparse E is not invariant under the full Suzuki low/high decomposition. The missing actual 30×30 source pairings M_Z,E_Z and their sign, as highlighted by PR #107, remain the correct next computation.

The two positive-sector programs do have a nontrivial INTERSECTION: if f=φ^(30) for smooth compact φ supported in an admissible E, then moments ∫x^jf=0 for 0≤j≤29. Thus u=i f' has zero pairings with low Legendre 1..30. Such f satisfy both the sparse-domain bound and the PR #107 high-sector estimate (given that independent theorem's hypotheses). Shared provenance is NOT an independent confirmation of that theorem, and neither program settles the low sign.

## 9. Domain-sensible gluing and negative controls

For E_1,E_2 each correctly source-certified, \(|E_1\cup E_2|\le |E_1|+|E_2|\). The source-aware union acceptance rule is:
- at a=1/2: accept the combined domain ONLY if the sum of exact upper measures is <=1/32;
- for a<=1: accept the combined domain under the five-prime 4096-mode theorem ONLY if the sum is <=1/16384.

A union that fails the budget is **UNVERIFIED**, not a negative witness, even when both individual domains are known positive. This distinction is load bearing: positivity of Q(f_1) and Q(f_2) alone says nothing about the sign of \(Q(f_1+f_2)\) unless the cross pairing is controlled. The exact synthetic Gram [[1,-2],[-2,1]] has positive coordinate diagonals but negative determinant.

Other falsification controls:
- Fake primitive 6, n>=8 in a<=1, wrong prime p for n=4, unsorted/nonprimitive source and untyped support budgets are refused; original sha is checked.
- Doubling the original p2 weight to a synthetic w=1 ruins the J=16 first sparse sign budget, but this is a failed method on a FAKE source, not a certified negative original-zeta direction.
- Dropping the sixteenth positive real Gamma mode makes the displayed rational 1/10 certificate fail; no genuine negative witness follows from that.
- Exact original log comparisons (log2, log3, log8, and pairwise gaps among log2, log3, log4, log5, log7) determine every source activation/separation, without trusting floating point near thresholds.
- Source-matched controls for wrong half-density, conductor, parity, Gamma scale, and pole/contact were implemented in inherited Tate and ONE OBJECT PRs. They are not silently rewritten here.
- An arbitrary declared E's length is an assumed domain constraint. The specially constructed E_2 and E_n are themselves mathematical witnesses with certified exact lengths and strict placement.

## 10. Claim-status ledger and roadmap

| ID | Status | Proven mathematical scope | Unpaid truth debt |
|---|---|---|---|
| S1 | CLASSICAL/PROVED ANALYTIC | TRUE Gamma Schur support-measure lower and original all-term signed Weil inequality for every Cc∞(E) | none in stated domain |
| S1b | PROVED ANALYTIC | every fixed finite a admits some positive sparse support measure m_a with true Weil sign | m_a does NOT cover general tests |
| S2 | PROVED ORIGINAL-SOURCE LOCAL | at a=1/2, source p2 active; all E of measure<=1/32, Q>||f||²/10 | broad-support tests |
| S3 | PROVED SOURCE-ACTIVE LINEAR DOMAIN | E=U∪(U+log2), nonzero genuine p2 transfer, Q>3||f||²/5 | full ambient sign |
| S4 | PROVED ORIGINAL-SOURCE LOCAL | every 0<a<=1, any E measure<=1/16384, all five authentic source jets budgeted, Q>||f||²/2 | broad-support tests |
| S5 | PROVED SOURCE-ACTIVE LINEAR DOMAINS | five separate E_n with actual prime transfer, only 16 Gamma rungs, Q>||f||²/2 | contraction gluing over sums |
| S6 | CLASSICAL/PROVED DOMAIN EXTENSION | source signed Q and inequalities extend from Cc∞(E) to H0¹(E) by translation difference estimate | not bounded L² on all test functions |
| S7 | PROVED CONDITIONAL ON SOURCE FORMULA (LOCAL) | genuinely positive Hilbert factor of original signed Weil form on each E | global point-kernel feature equality |
| S8 | CLASSICAL/PROVED DOMAIN RELATION | u=i f' transports S3 into exact PR107 G/K relative inequality; low moments reachable but no norm-controlled inverse | authentic low Schur 30×30 sign |
| RH | UNVERIFIED | no all-a/all-test positivity or original global contraction is established | true global Weil-positive proof remains open |

**Next verdict-changing instrument:** construct true analytic Gamma/contact/prime cross pairings between the 30 source-Legendre low modes and the S3/S5 prime-coupled packet Hilbert features, with a rigorous operator norm in the Neumann K geometry. Compare them against PR #107's source residual Schur \(M_Z-\kappa^{-1}E_Z\) without importing its unmerged files or treating an arbitrary positive surrogate as completed Weil. Calibrate cross-pairing source controls, a large-support negative model, and exact original 30-mode matrix residual. Proving all positive packet domains **is not** the same as proving that the union of their spans is positive.

**Reproduction:** observational_succ/apollo_prime_domain.py; tests/test_apollo_prime_domain.py; scripts/apollo_prime_domain_probe.py; .github/workflows/apollo-prime-domain.yml; claim supplement and RH handoff on this draft branch. All full-suite GitHub workflow results must be checked separately from the targeted 3.10/3.13 gates. No physical-observer authentication or original mathematical priority is claimed.

**External primary reference:** Masatoshi Suzuki, *Weil's quadratic form via the screw function* (arXiv:2606.09096v3, https://arxiv.org/html/2606.09096v3); R. G. Douglas (1966), DOI https://doi.org/10.1090/S0002-9939-1966-0203464-1. Source internal dependencies: research/2026-10-14/ARITHMETIC_META_WEIL_BOUNDARY.md, research/2026-10-14/SUZUKI_CANONICAL_MOMENT_SCHUR.md and APOLLO parent K2/K6/K7 source dossier.

**RH PROVED: NO.**


## 8a. An exact genuine prime-active HIGH-sector witness (new independent certificate)

The S8 moment-surjectivity fact has a complementary **kernel intersection** with PR #107's actual high sector that we can exhibit without zeros or an abstract density argument.

Let δ=1/64 and choose integer q>=34. On the source packet U, let φ_q be the affine translate of \(t^q(\delta-t)^q\), 0<t<δ, zero elsewhere. Set \(f_0=\phi_q^{(30)}\), and let \(f_1(x)=f_0(x-\log2)\) on the second genuine packet U+log2. Then f=f0+f1 is supported in E2 and is C³ or better after zero extension (its endpoint vanishing order is q−30>=4), hence is in H_0¹(E2). It is not falsely asserted Cc-infinity; smooth H_0¹ approximations are available for the form identity.

For every integer 0<=k<=29, integration by parts 30 times gives
\[
\int_U x^k f_0(x)dx=0.
\]
The translated packet f1 also has these vanishing polynomial moments by expanding \((t+\log2)^k\) using the binomial theorem; therefore **the actual two-packet f has all 30 zero moments**. For u=i f', integration by parts against normalized Legendre low basis e_j (1<=j<=30), whose derivatives e_j' are polynomials of degree j−1<=29, yields \(\langle u,e_j\rangle=0\). Thus u lies in the **authentic high subspace** of PR #107.

At the same time the original p=2 translation overlap is NOT zero:
\[
\langle T_{\log2}f,f\rangle=\|f_0\|_2^2>0,\quad
\|f\|_2^2=2\|f_0\|_2^2.
\]
So the high subspace and the APOLLO **genuinely prime-active** packet Hilbert domain intersect in nonzero vectors. This is a source-specific independent test of the domain interface, not merely a formal statement of dense subspace compatibility. Our full packet inequality gives Qζ(f)>=3||f||²/5, while the independent PR #107 moment-high theorem supplies its separately sourced κ=369/10000 statement under its own assumptions.

**Executable exact Fraction receipt:** expand \(\phi=t^q(\delta-t)^q\) in the polynomial basis, differentiate 30 times exactly, verify 30 vanishing rational integrals and a strictly positive exact polynomial L² norm. The translation overlap equals this same exact L² norm by support geometry, without evaluating log2 numerically. This finite C³ control does not replace the analytic Cc-infinity theorem, and neither bound determines PR #107's low Schur matrix.

**Verdict:** PROVED LOCAL high-sector / prime-coupling intersection, with an exact rational polynomial calibration; original low 30 Schur positivity remains UNVERIFIED.


## 8b. A genuinely source-identified LOW-to-activated-prime cross term (exact rational lower)

To go beyond declaring that low moments are reachable, choose the first normalized Legendre mode at a=1/2:
\[
u_1(x)=2\sqrt3\,x\quad (-1/2<x<1/2),\qquad
v_1(x)=\int_{-1/2}^x u_1(t)dt=\sqrt3(x^2-1/4).
\]
This is exactly PR #107's low Neumann primitive (up to its harmless i-phase). Let U=(-7/16,-7/16+1/64), b=log2 (genuine), and for any integer q>=4 let f=f0+f1 with \(f_0(t)=s^q(\delta-s)^q\) for s=t−left(U), 0<s<δ, and \(f_1(t)=f_0(t-b)\) in U+b. This zero-extended polynomial is at least C³ and in H0¹(E2); the source-signed form extends to this domain. There are also smooth positive test approximants.

The **PRIME-ONLY** original source cross term is, by polarization of the negative true n=2 translation,
\[
Q_2(v_1,f)=-w_2\{\langle T_b v_1,f\rangle+
                 \langle v_1,T_b f\rangle\}
=-w_2\sqrt3\int_U
\big[(t+b)^2+t^2-\tfrac12\big]f_0(t)dt.
\tag{S8-prime-cross}
\]
No other original prime is active at a=1/2. Exact original log intervals prove \(0<t+b<3/10\) on U, and \(|t|<7/16\). Hence the square bracket is strictly smaller than
\[
-c_*=-\left(\frac12-\frac{49}{256}-\frac9{100}\right)<0.
\]
Since the original half-density weight \(w_2=\log2/\sqrt2\) has a strictly positive source-certified Fraction lower \(\underline w_2\), and \(\sqrt3>1\), we obtain the exact **strict rational lower**
\[
\boxed{Q_2(v_1,f)>
\underline w_2 c_*
\delta^{2q+1}\frac{(q!)^2}{(2q+1)!}>0.}
\tag{S8-cross-cert}
\]
The original-source coefficient interval is authenticated by the same pinned source as the previous theorem; no zeta zeros, source-blind Gram fitting or numerical quadrature is used.

This is a real source-specific LOW-to-prime-coupled cross **COMPONENT**, exactly of the type PR #107's complete 30-low residual will need. It **does not certify the total completed signed Weil bilinear** Q_zeta(v1,f): the genuine Gamma/contact/pole pieces may offset the prime term. It does not certify any eigenvalue, sign of A, or low shorting. The true remainder is now a concrete cross-integral target, not an abstract plea for more positivity.
