# FINITE-SOURCE WEIL: canonical hierarchy, negative-depth obstruction and effective observer bounds

**2026-10-14, research draft.** Branch \`research/finite-source-weil-negative-depth-2026-10-14\`, based *exactly* on \`femboy2112/SUCC@3270d4b9d992042c7c2bebbe784916f544ac565c\` (Gaussian-Weil draft PR #76, itself a source-indexed child of PR #73 and genuine Weil PR #71). Read-only siblings: recursive Meta-SUCC PR #80, meta-contour PR #81, original theta zero PR #82, certified contour PR #83 and Black Sun #79. **Main is untouched. RH PROVED: NO.** No zero positions, arbitrary positive covariance, ghost Euler place or unspecified physical sensor is an input.

**PRIMARY MATHEMATICAL IMPORT:** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3, 23 September 2026, equations (1.3), (1.5), (1.8), (8.2), and the introduction Weil criterion:
https://arxiv.org/html/2606.09096v3. Classical functional analysis: compact operator approximations, spectral variational principle, positive cone closedness, spectral/convex-distance estimates; elementary computability: halting undecidability; classical Euler-Maclaurin sign-remainder for the Euler constant. Source-specific completed Gamma/contact/norm corrections are inherited from existing SUCC #71/#76 and checked against the original Suzuki formula. Do not present a classical import as independently new priority.

## 0. Steelman of the author's moonshot and its answer

The question:

> Does there exist a **finite-description, source-preserving** hierarchy of models of arithmetic-source interactions whose operators tend to the **actual completed Weil form**, and whose negative parts vanish **uniformly on every fixed compact test domain**?

**Decompose into distinct propositions:**

1. **HIERARCHY EXISTS:** For every rational \(a>0\) there is a source-derived sequence of finite signed operators whose operator-norm error tends to zero on the mean-zero Hilbert space \(L_0^2(-a,a)\). **YES, UNCONDITIONALLY**, by Suzuki's continuous original-source kernel, finite prime support on each compact interval, and quantified Gamma + spatial approximation. For general real \(a\), the same mathematical construction exists (the pure rational evaluator in code is currently restricted to \(a\le1\)).
2. **NEGATIVE DEPTH VANISHES:** \(d_-(G_{a,N})\to0\) as \(N\to\infty\), for every \(a>0\). **Exactly EQUIVALENT to RH**, by the Weil criterion and norm continuity of the negative spectral depth. This is not a solved second theorem.
3. **AUTONOMOUS CERTIFICATION:** Construct from actual source laws a finite proof rule establishing the entire infinite family of nonnegative limits, or an independent source-identified positive factorization. **UNVERIFIED, RH-HARD**. A report of many finite positive eigenvalues is not the rule.
4. **GENERIC CARRIER HARDNESS:** No algorithm uniformly decides exact positivity from arbitrary effective compact self-adjoint kernels and explicit norm convergence moduli. **PROVED relative to that general input class** by a halting reduction, with smooth rank-one kernels. This does **not** establish a FuckedSpace for the single fixed arithmetic source zeta.

The principal outcome is a sharper task reduction: **a finite signed source representation already exists; it is the asymptotic absence of negative spectrum—an exact source-specific assertion—that still needs proving**.

## I. Authentic source identity and domain — FSW-01 (CLASSICAL SUZUKI + PROVED LOCAL SOURCE TRUNCATION)

Suzuki fixes
\[
Q_W(v)=W(v*\widetilde v),\qquad v\in C_c^\infty(\mathbb R),
\]
where \(W\) contains **genuine prime powers** \(\Lambda(p^k)/\sqrt{p^k}=\log(p)/\sqrt{p^k}\), **one** completed real Gamma factor with digamma \(\psi(1/4)\), the completed poles and real half density. His authentic continuous even kernel is
\[
\boxed{\begin{aligned}
g(r)&=-4(e^{r/2}+e^{-r/2}-2)
 +\sum_{n=p^k\le e^r}\frac{\log p}{\sqrt n}(r-\log n)\\
 &\phantom{=}-\frac r2(\psi(1/4)-\log\pi)
 -4\sum_{j\ge0}\frac{1-e^{-(4j+1)r/2}}{(4j+1)^2},
\qquad r\ge0.
\end{aligned}}\tag{FS1}
\]
The full completed arithmetic source is fixed, not fitted. The digamma contact identity \(\psi(1/4)=-\gamma-\pi/2-3\log2\) is classical. This is exactly Suzuki Eq. (1.3) rewritten from the Hurwitz–Lerch expression. For each \(a>0\), let \(H_a=L_0^2(-a,a)\) and \(G_a=P_a[g(x-y)]P_a\), a compact bounded self-adjoint operator (continuous kernel). For \(v\in H_0^1(-a,a)\), the bijection \(D=i\,d/dx:H_0^1\to H_a\) satisfies the CLASSICAL identity
\[
\boxed{Q_W(v)=\langle G_a Dv,Dv\rangle_{L^2}.}\tag{FS2}
\]
Do not confuse \(G_a\) with Suzuki's *unbounded* Friedrichs extension \(A_a\): the operator norm in this dossier applies to \(G_a\), while the quadratic form is transported through \(D\), and its natural normalization is \(\|v'\|_2\), not \(\|v\|_2\).

At fixed \(a\), only \(p^k\le e^{2a}\) can enter the kernel differences. The infinite Gamma ladder is summable and has a source-derived uniform tail. Consequently, for any rational \(a>0\) and any positive integers \(J,N\), the exact mathematical construction is finite: J authentic Gamma rungs, the true prime tape through \(\lfloor e^{2a}\rfloor\), completed pole/contact and N cell reports. No RH, positive-kernel substitute or nontrivial zero-input is used.

## II. A source-preserving quantitative hierarchy — FSW-02 (PROVED LOCAL using Suzuki source formula)

Retain the first J Gamma terms and write the finite source kernel \(g_J\). Partition \((-a,a)\) into N equal cells of width \(h=2a/N\), center locations \(c_i=-a+(i+1/2)h\). The finite step kernel is \(K_{J,N}(x,y)=g_J(c_i-c_j)\) on the cell \(i\times j\), compressed to mean-zero functions. On normalized cell indicators its matrix is
\[
\boxed{M_{ij}=h\,g_J\big(h|i-j|\big).}\tag{FS3}
\]
A literal rational approximation \(\widetilde M\) is obtained by **outward rational intervals** of genuine \(g_J\) values, never by unbounded floating-point roundoff.

Let
\[
\tau_J:=\frac1{4J+1}+\frac4{(4J+1)^2},\quad
L_J(a):=2(e^a-e^{-a})+\frac{|\psi(1/4)-\log\pi|}{2}
+\sum_{p^k\le e^{2a}}\frac{\log p}{\sqrt{p^k}}
+2\sum_{j=0}^{J-1}\frac1{4j+1}.
\]
Then
\[
\|g-g_J\|_{\infty}\le\tau_J,\qquad
|g_J(x)-g_J(y)|\le L_J(a)|x-y|
\]
for \(x,y\in[-2a,2a]\). If each computed interval for \(g_J(hk)\) has midpoint error \(\le\eta\), then Schur's integral norm inequality yields
\[
\boxed{
\left\|G_a-\widetilde G_{a,J,N}\right\|
\le E_{a,J,N}:=2a\left(\tau_J+hL_J(a)+\eta\right).
}\tag{FS4}
\]
Every normalization is explicitly retained: each normalized cell has matrix coefficient \(h\,g_J\); the mean-zero compression is a projection of norm one, and the row-sum matrix error is at most \(Nh\eta=2a\eta\). On a fixed a, take \(J\to\infty\), \(N=J^2\), and a source-certified interval evaluator with \(\eta\to0\). Since \(L_J(a)=O_a(\log J)\), \(E_{a,J,J^2}\to0\). This is **unconditional** source-faithful signed convergence, not an RH proof.

**Entirely rational coarse Lipschitz certificates for code's first windows.** For \(0<a\le1/2\), the true prime list contains only \(n=2\), so
\[
L_J(a)<9+2\sum_{j<J}\frac1{4j+1}.
\]
For \(1/2<a\le1\), \(e^{2a}\le e^2<8\); bounding every authentic prime power by the integers \(2,\dots,8\) gives
\[
L_J(a)<45+2\sum_{j<J}\frac1{4j+1}.
\]
Use \(e<11/4\), \(\gamma<1\), \(\pi<4\), \(\log2<1\), \(\log\pi<2\) and \(\log p/\sqrt{p^k}\le p^k\). Thus the **analytic norm remainder is certified by rational arithmetic**, without trusting numerical calculations of exponentials or digamma.

## III. Negative spectral depth is a 1-Lipschitz source invariant — FSW-03 (CLASSICAL, sharp)

For any bounded self-adjoint operator \(A\) on a Hilbert space, define
\[
d_-(A):=\max(0,-\inf_{\|u\|=1}\langle Au,u\rangle)
=\|(-A)_+\|=\operatorname{dist}_{\|\cdot\|}(A,\mathrm{PSD}).
\]
Here \((-A)_+\) denotes the positive spectral part of \(-A\), and PSD is the closed cone of bounded positive semidefinite operators. For any two self-adjoint \(A,B\), Rayleigh variational inequalities yield
\[
\boxed{|d_-(A)-d_-(B)|\le\|A-B\|.}\tag{FS5}
\]
The distance formula is exact: \(A+(-A)_+\) is PSD and within \(d_-(A)\), while a unit approximate minimizing Rayleigh vector forces every PSD operator to lie at least \(d_-(A)\) away.

Apply (FS5) to the **actual source** (FS4):
\[
\boxed{\max(0,d_-(\widetilde G_{a,J,N})-E_{a,J,N})
\le d_-(G_a)
\le d_-(\widetilde G_{a,J,N})+E_{a,J,N}.}\tag{FS6}
\]
This is a two-sided **mathematical** error bracket on an infinite-dimensional truth. It does not itself decide whether the true value is exactly zero. It also gives a sharp falsifier: a finite certified negative Rayleigh vector satisfying \(-R_{\widetilde G}(u)>E_{a,J,N}\) implies \(Q_W(v)<0\) for the source-faithful antiderivative \(Dv=u\). Smooth compact approximants retain strict negativity.

**WEIL EQUIVALENCE** (CLASSICAL + reduction): RH iff \(d_-(G_a)=0\) for every \(a>0\), iff the negative depth in *any* genuine source-faithful norm-convergent hierarchy tends to zero for every \(a\). Rational positive \(a\) suffice by nested-interval exhaustion and density. This resolves the **existence of a hierarchy** in the user's question: existence is not the obstacle. Proving its negative-depth limit equals zero would be the missing RH proof.

## IV. Canonical Galerkin negative debt is MONOTONE — FSW-04 (CLASSICAL, new-to-SUCC formulation)

Fix a>0 and choose nested finite-dimensional mean-zero step spaces \(V_1\subset V_2\subset\cdots\subset H_a\) with dense union (dyadic refinements, for example). Let \(P_N\) be orthogonal projections onto them, and \(K_N=P_NG_aP_N\), extended by zero to \(H_a\). Since \(G_a\) is compact, \(K_N\to G_a\) **in operator norm**.

Define the exact compression debt \(b_N=d_-(K_N)\). Then
\[
\boxed{0\le b_N\le b_{N+1},\qquad
\lim_N b_N=d_-(G_a).}\tag{FS7}
\]
Proof: the Rayleigh infimum over a growing unit-sphere subspace cannot increase; zero on the complement ensures the negative-depth interpretation. Compactness and strong density imply norm convergence; apply (FS5). In particular, **any authentically negative direction discovered at one exact level persists in all later exact Galerkin levels**. Finite source/Gamma truncations \(\widetilde G_{a,J,N}\) do *not* automatically preserve this monotonicity: their numerical and analytic errors change, so monotonicity assertions must specify the exact nested projections rather than whatever approximate matrices happen to have been printed.

This is a useful obstruction/repair discriminator: repeated late-stage “negative eigenvalues disappearing” must be reconciled with approximation error or changing source/basis, not promoted to a source theorem.

## V. Fully rational interval evaluation of the AUTHENTIC source — FSW-05 (PROVED LOCAL + classical constants)

\`observational_succ/source_weil_hierarchy.py\` builds exactly the original g_J on rational \(|r|\le2\) with 32-decimal-place **directed rational floors/ceilings at every interval operation**. Its source tape is exactly \((n,p)=(2,2),(3,3),(4,2),(5,5),(7,7),(8,2)\) with the correct true-prime power test; \(n=6\) has no independent prime-place coefficient and source mutations are rejected.

- \(\pi\): rational alternating Machin formula \(16\arctan(1/5)-4\arctan(1/239)\).
- \(\log x\): dyadic range reduction and \(\log x=2\sum_{k\ge0}t^{2k+1}/(2k+1)\), \(t=(x-1)/(x+1)\), positive geometric remainder.
- \(e^{\pm x}\): positive Taylor polynomial with explicit geometric tail, dyadic scaling and reciprocal/squaring, with interval outward rounding.
- \(1/\sqrt n\): integer isqrt enclosures on a scaled rational grid.
- \(\gamma\): Euler–Maclaurin at n=16, with the first neglected term as a rigorously bounding alternating remainder:
\[
 H_{16}-\log16-\frac1{32}+\frac1{12\cdot16^2}
-\frac1{120\cdot16^4}+\frac1{252\cdot16^6}
-\frac1{240\cdot16^8}
\;\le\gamma\le\;
 H_{16}-\log16-\frac1{32}+\frac1{12\cdot16^2}
-\frac1{120\cdot16^4}+\frac1{252\cdot16^6}.
\]
This is a **classical analytic inequality**, not inferred from the numerical tests.

The code computes source intervals \([g_{J,k}^-,g_{J,k}^+]\), exact midpoint matrix \(M\) and a theorem-backed bound \(E_{a,J,N}\). The scalar entry radius \(\eta=\max_k(g_{J,k}^+-g_{J,k}^-)/2\) accounts for finite-transcendental evaluation. The code is explicitly a **budgeted first-window instrument** (\(a\in\mathbb Q\cap(0,1]\), stage \(J\le36,N\le24\)); the mathematical theorem is not restricted to these implementation ceilings.

The mean-zero condition matters: the \(N\) normalized cell states have constraint \(\sum_i u_i=0\). In the rational contrast basis \(B=[e_0-e_{N-1},\ldots,e_{N-2}-e_{N-1}]\), the Rayleigh denominator is \(B^TB=I+\mathbf1\mathbf1^T\), NOT \(I\). For any rational \(\delta\ge0\), the exact shifted test
\[
 B^T(M+\delta I)B\succ0
\]
is verified by exact rational positive LDL pivots. It produces a finite **all-vector** lower bound \(M|_{\mathrm{meanzero}}\succeq-\delta I\); together with (FS4) this yields \(d_-(G_a)\le\delta+E\). The code explicitly **replays and compares the entire stage source**, refusing forged matrices or forged smaller errors before returning a source certificate. The source is mathematical, not cryptographically/physically authenticated.

A contrast witness \(u=e_i-e_j\) gives the complementary source lower bound \(d_-(G_a)\ge\max(0,-u^TMu/\|u\|^2-E)\). If ever strictly positive under genuine arithmetic and fully audited error, this would be a legitimate RH counterexample. No such witness is reported.

## VI. An exact FuckedSpace-like boundary for GENERIC source kits — FSW-06 (PROVED LOCAL theorem schema, NOT a theorem about zeta)

Fix one Hilbert space \(H=L_0^2(-1,1)\) and the normalized odd vector \(\phi(x)=\sqrt{3/2}\,x\). For any Turing machine/program \(e\), define a signed rank-one operator
\[
A_e=
\begin{cases}
-2^{-T_e}|\phi\rangle\langle\phi|,&e\text{ halts at first step }T_e,\\
0,&e\text{ never halts.}
\end{cases}
\]
Its real polynomial kernel is \(-2^{-T_e}(3/2)xy\) or zero, so all these kernels are continuous, smooth and finite rank. At SUCC stage \(N\), simulate e for N steps and output \(A_{e,N}\) with coefficient \(-2^{-T_e}\) if halt detected, else 0. Then **for every e and N**
\[
\boxed{\|A_{e,N}-A_e\|\le2^{-N}.}\tag{FS8}
\]
Proof: if a halt was detected, stage is exact; if no halt by N, any eventual first halt has \(T_e>N\) and coefficient \(\le2^{-N}\). These are effective rational stages with a computable, rapidly converging norm modulus. But \(A_e\succeq0\iff e\) never halts. An algorithm deciding **all** such operator-positive questions from any such executable finite representation would solve the halting problem, impossible.

**Interpretation:** an exact effective global norm-convergence certificate does **not** supply a general finite-time *positive answer* to whether the limit is PSD. Negative answers are semidecidable (a strict certified negative witness eventually appears), and equality at the boundary may remain undecidable. This is a **uniform-source-class toolkit barrier**, a legitimate operational “FuckedSpace” example. It does not show that the specific **unique original Euler/Poisson zeta source** is undecidable, physically unreachable, or RH true/false. Proving such a source-specific barrier would require an additional reduction respecting every authentic arithmetic constraint; no such reduction is known.

## VII. The most severe source-identification and proof-debt tests

- **Composites/incorrect multiplicativity:** inserting n=6 as an independent Euler place, omitting prime 3, changing p-label on 8 must be rejected.
- **Gamma source and contact:** the genuine 1-mod-4 half-index rungs, \(\psi(1/4)\), pi/log2 and Euler gamma intervals must pass independent high-precision *diagnostic* comparisons and exact interval endpoint inequalities.
- **Pole/half-density:** deleting a pole, changing \(\sqrt n\) to \(n^\alpha\), replacing the actual signed source with a positive Gaussian covariance invalidates the source manifest. A generic operator norm theorem remains valid for those mutants only as a mathematical toy, **not as the Weil criterion**.
- **No spectral repair by magic:** all finite matrices can be positive while a later exact nested compression reveals a negative direction. Positive approximations from a different source prove nothing. An approximation with a declared error can only prove sign if its **rigorously certified** margin excludes negative alternatives.
- **Holonomy bridge:** PR #80's two separately noncoercive unitary loop models produce a positive joint gram and exact \(1/23\) bound, but there is no domain-correct, source-identified operator map from that finite transport energy to the *actual* Suzuki \(G_a\). That is precisely the missing IdealHard source interaction inequality.
- **Contour bridge:** PRs #82/#83 establish genuinely bounded analytic zero information under their own source contracts. No finite sum of local positive zero projectors controls the complementary full signed Weil form; the high-zero tail generally requires regularity stronger than the uniform \(H^1\) norm available in FS2. Distinguish norm topology before attempting gluing.

## VIII. What actually has to be proved next

One particularly sharp **verdict-changing** possibility: find a **finite-description, source-first form factorization** \(G_a=T_a^*T_a-R_a\) on \(H_a\) for each rational a, where *every* \(T_a,R_a\) is built from real Euler/Gamma/pole/half-density source data, with a fully justified common basis/domain, and prove \(\|R_a^-\|\) or other **negative domination certificate** is zero (or tends to zero under authenticated refinement). It is NOT valid to simply define \(T_a=(G_a)_+^{1/2}\): that presupposes knowledge of the sign decomposition and says nothing source-first. Alternatively, discover a source-identified joint holonomy/Schur inequality that bounds the actual prime-pole negative contribution by the real Gamma-positive bath plus the correct contact. That inequality **must** survive fake composite 6, true primitive odd \(\chi_4\), conductor, pole and full compact-test-domain probes.

Proof graph (minimal cut):
1. Original source g + completion, compact domain **done** (classical Suzuki; project implementation).
2. Source-authenticated rational signed finite stages **done** within declared implementation domain, conditional on classical EM and Suzuki imports.
3. Norm convergence and two-sided negative-depth error **done** (classical and exact formulas).
4. **New source-specific all-stage positivity/limiting zero-negative-depth theorem** **UNVERIFIED (RH-equivalent)**.
5. A source-independent *general* decision procedure for positivity with effective norm modulus **REFUTED** by (FS8).
6. Classification of RH itself as FuckedSpace **UNVERIFIED**; IdealHard features are established, generic observer limitations are rigorous.

**No finality claim**: success on the mathematical hierarchy and exact source enclosure only advances the probe/toolkit and strengthens falsifiability. It cannot turn a finite certificate covering a bounded interval or a fast numeric zero scan into RH. Review all theorem normalization constants and hostile cases on this branch before merge. No physical source or academic priority authenticated.


## IX. Genuine higher-order sign obstruction: pairwise positivity is not enough — FSW-07 (PROVED LOCAL, finite toy; NO authentic RH conclusion)

Our first exact finite signed test searched only pairwise mean-zero contrasts \(e_i-e_j\). A three-model source test refutes their completeness. Take
\[
 u=(1,1,-2),\quad M=I-\tfrac15 uu^T
 =\begin{pmatrix}4/5&-1/5&2/5\\-1/5&4/5&2/5\\2/5&2/5&1/5\end{pmatrix}.
\]
On every pairwise contrast \(e_i-e_j\), the Rayleigh value is either \(1\) or \(1/10\), **strictly positive**. Yet \(Mu=-u/5\), hence the genuinely three-coordinate direction has Rayleigh quotient \(-1/5\). A model-of-pairwise-positive-models can therefore be **false about the whole signed interaction**. This is the elementary \(3\times3\) principal-minor/Schur phenomenon, not new operator theory or a source-lawful zeta mutation. The rational proof is independently executable, not numerical.

\`finite_multiway_search\` now enumerates bounded integer mean-zero vectors, including \(u\), and finds a negative rational joint direction that all pairwise controls miss. \`authenticated_multiway_witness\` runs the SAME search on an original-source replayed Suzuki stage and only promotes a negative mathematical conclusion if its actual upper Rayleigh bound plus *every* analytic/interval error is strictly negative. No positive statement is inferred from the failure to find a witness. The finite source replay and source label remain required. This provides SUCC's recursive interaction calculus a **real test of probe completeness**, not an unconstrained “interesting vibe.”

## X. Prime-wavefront and radial negative-debt monotonicity — FSW-08 (PROVED LOCAL + classical Suzuki continuity)

**Original-source radius inclusion.** For \(0<a<b\), zero extension embeds \(H_a=L_0^2(-a,a)\) isometrically into \(H_b\). The quadratic form of the *same original* convolution kernel is preserved on embedded functions:
\[
\langle G_b\,\iota u,\iota u\rangle=\langle G_a u,u\rangle.
\]
Therefore
\[
 \boxed{d_-(G_a)\le d_-(G_b)\qquad(0<a<b).}\tag{FS9}
\]
Moreover \(a\mapsto d_-(G_a)\) is **continuous**: rescale \(H_a\to H_1\) unitarily by \(f\mapsto\sqrt a\,f(a\cdot)\); the rescaled continuous kernel is \(a\,g(a(x-y))\). Uniform continuity of g on bounded differences implies norm-continuity on every compact radius interval, and (FS5) transfers this to d. Near \(a=0\), \(\|G_a\|\le2a\sup_{|r|\le2a}|g(r)|\to0\), so \(d_-(G_a)\to0\).

**Operational meaning:** if a negative source direction ever appears at radius \(a_0\), it persists at every larger radius and can never be “repaired” by a *larger exact source window*. Conversely, for RH it is necessary and sufficient that the debt vanish on any unbounded sequence of test radii, such as integer \(a=1,2,3,\ldots\). Earlier finite numerical stage output need not itself respect this monotonicity because its source truncation and interval budgets differ; its **rigorously bounded** error must account for apparent counter-trends. This is the radial companion to nested Galerkin monotonicity (FS7).

**Authentic arithmetic wavefront:** a prime-power n first enters compact kernel differences when \(2a=\log n\), i.e. \(a=(\log n)/2\), since the source term is \((|x-y|-\log n)_+\). The source wavefront finder computes the actual n=p^k activation set for rational \(a\le1\) using outward logarithm intervals, refusing precision-ambiguous boundaries. At a=1/4: no prime atoms; at a=1/2: only n=2; at a=1: n=2,3,4,5,7. Composite 6 is not a new independent place. The **overall sign depth remains continuous across these activation thresholds**, since \((r-\log n)_+\) is continuous. There is no discontinuous “new zero created by opening a prime port” theorem.

If RH is false, \(\{a:d_-(G_a)>0\}\) is a nonempty upper interval and the first obstruction radius \(a_*=\inf\{a:d_-(G_a)>0\}\) is mathematically well-defined. Suzuki/Yoshida's imported small-support positivity results suggest \(a_*>0\), but no numerical value or finite construction of \(a_*\) follows from this theorem. If RH is true, the set is empty. The classification is conditional, not a claim about the actual sign.

## XI. A sharp certified resource tradeoff — FSW-09 (PROVED LOCAL)

A subtle IdealHard-like phenomenon emerges directly from the true source's finite-Gamma/spatial approximation errors. More authentic Gamma modes always improve the **kernel's infinite-rung truncation**, but at a **fixed spatial observer resolution** they make the finite-truncated kernel more oscillatory / less cheaply Lipschitz. Our stated analytic error
\[
E_{a,J,N}^{\rm an}=2a\bigl(\tau_J+(2a/N)L_J^{\rm safe}(a)\bigr)
\]
uses \(\tau_J=(4J+1)^{-1}+4(4J+1)^{-2}\), and the rational safe Lipschitz ladder increments by exactly \(2/(4J+1)\). Consequently the **exact rational change in the proved error bound** on adding one Gamma rung is
\[
\boxed{
E_{a,J+1,N}^{\rm an}-E_{a,J,N}^{\rm an}
=2a\left[\tau_{J+1}-\tau_J+
\frac{4a}{N(4J+1)}\right].}\tag{FS10}
\]
The error certificate improves **if and only if**
\[
\boxed{N>\frac{4a}{(4J+1)(\tau_J-\tau_{J+1})}.}\tag{FS11}
\]
For \(a=1/2,J=12\), the threshold is exactly \(137641/6010\simeq22.902\), so increasing J improves the bound at N=23 but **worsens it at N=22**. For J=16,N=24 it also worsens; at N=64 it improves. The source Gamma rung itself is genuine; the nonmonotonicity is in this *particular observer's quantitative approximation guarantee*, **not in d_-(G_a)**. This is an explicit two-resolution SUCC law: advancing one certified model coordinate requires enough capacity in the other coordinate to preserve overall approximation quality.

At \(a=1/2\), the existing modest N=24 stage has an analytic norm error around 0.5 even when J is optimized; true first-window lowest spectral margins reported in sibling Black Sun #79 are \(\sim10^{-4}\) diagnostics. Thus a small finite Gram pass with this coarse certificate is nowhere near a definitive whole-test positivity proof. Demanding such a proof from this insufficient resource geometry would confuse an *instrument calibration wall* with a mathematical impossibility. To reach RH-relevant spectral scales the program needs better Galerkin/interpolation, adaptive wavefront meshing, stronger source-specific bounds or a structural positivity theorem—not merely more numerically sampled zeros.

## XII. Source-map cache alias incident (OBSERVED AND REPAIRED)

An adversarial type test discovered that Python's default \`functools.lru_cache\` can reuse a \`Fraction(1,2)\` result for a float \`0.5\` because their hashes and equality coincide, bypassing the **function-body** exact-type rejection if a certified rational key was already cached. Thus source validity is not protected by a post-cache argument validator. The dedicated CI failed this test on head \`7d565c2\`, preserving the actual failure receipt; the repair uses \`@lru_cache(..., typed=True)\` on **every** exact-source cache (\`stage\`, \`screw_interval\`, \`log_iv\`, \`exp_pos\`, etc.) with explicit warmed-cache float-alias regression. GitHub CI after the typed-cache patch passed both Python versions, confirming the particular alias no longer bypasses these source gates. This is a real implementation-level \(\sigma\)/source-map correctness issue, not a new theorem about Weil positivity. A Python cache key is not a physical source certificate.
