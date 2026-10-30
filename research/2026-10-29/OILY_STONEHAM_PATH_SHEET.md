# Oily–Macaroni × Stoneham × SUCC path-sheet gluing (2026-10-29)

**Baseline:** \`main@ec2fbe321a29a220f3d67ff5fbd749e64d4d3efc\` (Main XIV). **Research only.** This additive dossier makes no change to BBP forcing, the zero seed, original archives, formal proof IDs, workflows, or main. The mathematical identities below have paper derivations and targeted *locally executed* independent Fraction/SymPy probes; exact-head CI and Lean have **NOT** run. Known Stoneham normality is not a new discovery; pi base-16 normality and RH remain **OPEN**.

## 1. Source passports and central question

The exact signed source is
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad U_0=0,\quad U_{n+1}=16U_n+r(n+1).
\]
The positive Oily packet source has \(u(x)=x-x^2/2\), \(v(x)=x^2/2\), endpoint grade \(w_j=(j+1)/2^{j+2}\), and PGF \(G(q)=(2-q)^{-2}\). That auxiliary packet is NOT the selected real-circle BBP orbit.

**Hypothesis under examination:** a full path is a *glued* object, not merely a sum of independent micro paths. A realized path may update a posterior over micro histories; a physical/material change additionally needs a specified transition law. We ask what gluing constraints, golden/Gamma corrections and finite-to-global normality witnesses can be **proved**, and which still fail to distinguish the authentic seed.

## 2. OM-1: a two-loop-dependent golden fixed point

\[
G(q)-q=-\frac{(q-1)(q^2-3q+1)}{(2-q)^2}.
\]
The attracting fixed point \(q_*=(3-\sqrt5)/2=\varphi^{-2}\) is selected by \(q_0=0,\ q_{m+1}=G(q_m)\). The other fixed point is \(1\). Because \(G'(q)=2/(2-q)^3\), the mean-value theorem on \([0,q_*]\) yields
\[
0<q_*-q_m\le q_*\rho^m,\quad \rho=2\varphi^{-3}<1/2.
\]
**Hostile one-channel deletion:** for one rather than two geometric channels the PGF is \(G_1(q)=1/(2-q)\). Its fixed point equation is \((q-1)^2=0\), so the nontrivial attracting golden point disappears. The original *two-channel grading* is load-bearing for this exact chosen coordinate. Existing source-preserving regradings still change the fixed point, so it is not a canonical invariant of the ungraded BBP source.

## 3. OM-2: logarithmic fiber entropy and a one-sided finite constant certificate

Conditioned on endpoint grade \(j\), the packet has \(j+1\) equally weighted two-channel splits, so \(S_j=\log(j+1)\). The exact entropy increment is \(\log(1+1/j)\). Its **declared first-order harmonic comparison** is \(1/j\); accumulating the mismatch gives
\[
E_m=\sum_{j=1}^m[1/j-\log(1+1/j)]=H_m-\log(m+1)\uparrow\gamma.
\]
Define the finite contrast
\[
\Xi_m=(1-q_m)-E_m,\qquad \Omega_{\rm OM}=\varphi^{-1}-\gamma.
\]
Since \(1-q_*=\varphi^{-1}\) and \(0<\gamma-E_m<1/(2m)\), we obtain
\[
\boxed{0<\Xi_m-\Omega_{\rm OM}<q_*\rho^m+\frac1{2m}.}
\]
All finite inputs are rational except \(\log(m+1)\), which admits an exact rational interval via the artanh series. At \(m=12\), a local exact rational arithmetic certificate gave
\(0.0380869345959<\Omega_{\rm OM}<0.0798004642121\), without using a decimal value of \(\gamma\) as input. The clock synchronization and harmonic reference are *chosen*, not uniquely compelled by the physical carrier.

Independent **inherited**, source-graded Oily Mellin covariance (read \`research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md\`):
\[
\lim_{n\to\infty}8n\,\mathrm{Cov}_{\mu_n}(\mathbf1_{\{J\ {\rm odd}\}},(\log Y_n-\varphi^{-2})^2)
=-\frac8{27}\Omega_{\rm OM},\quad Y_n=8n(1-X).
\]
Its \(-4/27\) primitive-grade endpoint response was reproduced in a separate symbolic oracle. The result is **center dependent**, not a canonical third cumulant nor a statement about Weyl phases. Changing the center to \(1-\gamma\) erases the leading coefficient.

## 4. PS-1: actual gluing is not multiplicative after observation

For an isometry \(J:H\to K\), put \(P=JJ^*\), \(C(A)=J^*AJ\), and
\[
\Delta(A,B)=C(AB)-C(A)C(B)=J^*A(I-P)BJ.
\]
This has an exact *three-operation coherence law*:
\[
\boxed{\Delta(AB,C)+\Delta(A,B)C(C)
=\Delta(A,BC)+C(A)\Delta(B,C).}
\]
Proof: both sides simplify to \(C(ABC)-C(A)C(B)C(C)\). Moreover
\[
\Delta(A^*,A)=((I-P)AJ)^*((I-P)AJ)\succeq0.
\]
This is a rigorous mathematical model of triangular path sheets: the triangle face holds microstate information discarded by intermediate compression, and tetrahedral regrouping constrains its faces. SUCC WCG-08 already has the source-specific nonzero witness \(\|\Delta(S_A,A_2)|1\rangle\|^2=5/24\). This is NOT a derived physical Yang–Mills field.

## 5. ST-1: exact Stoneham conductor births and full-cycle signed sums

The distinct source \(\alpha_{2,3}=\sum_{p\ge1}1/(3^p2^{3^p})\) has the rational control
\[
z_0=0,\quad z_n=\{2z_{n-1}+\mathbf1_{n=3^p}/n\}.
\]
On the circle, \(D_b\circ T_r=T_{br}\circ D_b\), so \((D_bT_r)-(T_rD_b)\) is the translation by \((b-1)r\) in additive circle coordinates. Stoneham's active pulses have \(b=2,\ r=3^{-p}\); the ordering defect is exactly \(3^{-p}\).

At stage \(3^p\le n<3^{p+1}\), the rational orbit lies in \((\mathbb Z/3^p)^\times/3^p\). Its first numerator is \(1\bmod3\), and \(\mathrm{ord}_{3^p}(2)=2\cdot3^{p-1}\), as follows from \(v_3(2^{2\cdot3^k}-1)=k+1\). Stage length \(2\cdot3^p=3\varphi(3^p)\) is exactly three complete sweeps. For the \(p\)-th **complete** rational stage,
\[
\sum_{n=3^p}^{3^{p+1}-1}e(hz_n)=3c_{3^p}(h),\quad
c_{3^p}(h)=\begin{cases}
2\cdot3^{p-1}&3^p\mid h,\\
-3^{p-1}&3^{p-1}\mid h,\ 3^p\nmid h,\\
0&3^{p-1}\nmid h.
\end{cases}
\]
For each fixed \(h\ne0\), sufficiently late complete stages cancel **exactly**. Crucially, this does not control an *arbitrary partial stage*, so it is not a standalone normality proof.

## 6. ST-2: direct all-horizon weak hot-spot estimate

Bailey–Misiurewicz establish the genuine source approximation \(|\{2^n\alpha_{2,3}\}-z_n|<1/(2n)\) (their \`A Strong Hot Spot Theorem\`, §4).

For any interval \(I\subset[0,1)\) of length \(\ell\), \(N\ge4\), and \(P=\lfloor\log_3(N-1)\rfloor\), the following **paper derivation** yields:
\[
\boxed{A_N(I):=\#\{0\le n<N:\{2^n\alpha_{2,3}\}\in I\}
\le \tfrac92 N\ell+6P+3.}
\]
At each complete or partial stage \(p\), a unit residue appears at most three times. Every true hit must correspond to a rational grid point within \(1/(2\cdot3^p)\) of \(I\); this expanded arc has length at most \(\ell+1/3^p\) and contains at most \(3^p\ell+2\) grid points. This stage therefore contributes at most \(3^{p+1}\ell+6\) hits. Add the initial three indices, sum \(p\le P\), and use \(\sum_{p=1}^P3^p<(3/2)N\). Divide by \(N\): \(\limsup A_N(I)/N\le(9/2)\ell\) for every interval. The **already published** weak hot-spot criterion implies base-2 normality of the Stoneham constant. This is a reproof of a known theorem with an explicit counting constant, not a novel Stoneham normality claim.

## 7. PS-2: a universal no-go for *central* Oily–Macaroni weights

The authentic positive Oily source gives a logarithmic correction \(0<\eta_n\le c/n,\ c=7/16\) in \`OILY_MACARONI_SOURCE_BRIDGE.md\`. For any bounded complex source phases \(|f_n|\le1\), let
\[
W_n=\exp[t(\Omega_{\rm OM}-\eta_n)],\quad
M_N^W=\frac{\sum W_nf_n}{\sum W_n},\qquad t\in\mathbb R\ {\rm fixed}.
\]
The common \(e^{t\Omega_{\rm OM}}\) cancels *identically* from numerator and denominator. Writing \(\widetilde W_n=e^{-t\eta_n}\), one has \(|\widetilde W_n-1|\le |t|ce^{|t|c}/n\) and \(\sum\widetilde W_n\ge Ne^{-|t|c}\). Therefore
\[
\boxed{\left|M_N^W-\frac1N\sum_{n=1}^N f_n\right|
\le2|t|ce^{2|t|c}\frac{H_N}{N}=O_t(\log N/N).}
\]
This holds for **every sequence**, including both the authentic four-pole seed and its known coherent nonnormal counterseed \(-\pi/16\). A scalar center or an \(O(1/n)\) positive weight cannot *cause* Weyl cancellation. To become load-bearing for π, Oily must enter a **noncentral, signed, seed-sensitive cross-path interaction**, not just a normalization.

## 8. Exact source-specific 15 alignment, and the boundary

\(Q(x)=4-2e^{-3x}-e^{-4x}-e^{-5x}\) has \(Q'(0)=15=16-1\). Therefore \(r(n)\sim15/(64n^2)\), and the authentic future tail \(T_n=\sum_{j\ge1}16^{-j}r(n+j)\sim1/(64n^2)\), because \(\sum16^{-j}=1/15\). The same \(16-1\) is the coefficient in the affine path-ordering commutator. This exact source/base alignment is worth probing with mutations but does not imply signed cancellation, and \(\Omega_{\rm OM}\) does not appear in it.

## 9. Provenance, validation, and next verdict-changing probe

Local independent work: 13 standard-library Python unit tests passed after a corrected one-loop mutant, using exact \`Fraction\` for five primitive sweeps, Ramanujan stage integers, 3×3 compression associator, interval upper bounds, the original forcing, rational \(\Omega\) bounds and source mutations. Separate SymPy checks recovered both fixed-point polynomials, \(-4/27\) and \(Q'(0)=15\). **Exact GitHub tree execution, repository-wide suite, Lean, and hosted CI remain UNRUN.**

Sources:
- SUCC \`research/2026-10-26/OILY_TOTIENT_THIRD_SHADOW.md\`, \`FOUR_POLE_ATOMIC_SUBSTRATE.md\`, \`OILY_MACARONI_SOURCE_BRIDGE.md\`.
- SUCC \`research/2026-10-28/OILY_ZETA_CAUSAL_GROWTH_AND_SOURCE_DEFECT.md\`.
- Bailey–Misiurewicz, *A Strong Hot Spot Theorem*, §4: https://www.davidhbailey.com/dhbpapers/dhb-mm-hotspot.pdf .
- NIST DLMF Euler constant and asymptotics: https://dlmf.nist.gov/5.2 , https://dlmf.nist.gov/2.10 .

**Required next discriminator:** define a source-faithful signed gluing observable that preserves the zero initialization and makes a mathematically different prediction for \(U_0=0\) versus the same-forcing coherent seed \(-\pi/16\). Require an unbounded-horizon \(o(N)\) improvement, or a weaker independently proved estimate that feeds it; do not substitute an equivalent Weyl assumption. No physical coupling, RH, or π-normality status promotion.
