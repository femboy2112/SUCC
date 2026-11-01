# Original four-pole BBP on a punctured Riemann sphere: source, Pascal sampling, residues and path history

**2026-10-31; research-only.** Source is the literal original four signed poles
\(r(z)=4/(8z-7)-2/(8z-4)-1/(8z-3)-1/(8z-2)\) and \(U_0=0,\ U_n=16U_{n-1}+r(n)\). Main XVIII and PRs #437–#441 are precedents, not independently re-proved here. The core results below are elementary/classical specializations and **paper proofs**, with exact local finite checks. No Lean proof and no claim of π normality or RH.

## RSP-01. Four source punctures on the sphere, a rational logarithmic differential (PROVED PAPER)

Set \(P=(7/8,1/2,3/8,1/4)\), \(w=(4,-2,-1,-1)\), \(\rho=w/8=(1/2,-1/4,-1/8,-1/8)\). The meromorphic one-form

\[\omega=r(z)dz=\frac18d\log R(z),\qquad R(z)=\frac{(8z-7)^4}{(8z-4)^2(8z-3)(8z-2)}\]

is globally defined on \(\mathbb P^1\) as a **meromorphic differential** (the logarithm itself is multivalued). Differentiating gives the original four poles, so \(\operatorname{Res}_{p_i}\omega=\rho_i\). The sum \(\sum_i\rho_i=0\); equivalently \(r(z)=15/(64z^2)+O(z^{-3})\). In local coordinate \(u=1/z\), \(\omega=-15\,du/64+O(u)du\), regular at infinity. This is the exact four-pole zero-mass condition, not an unverified curvature analogy.

For a closed path \(\gamma\) missing the punctures, the residue theorem gives
\[\oint_\gamma\omega=\frac{2\pi i}{8}(4w_1(\gamma)-2w_2(\gamma)-w_3(\gamma)-w_4(\gamma)),\]
where \(w_i(\gamma)\in\mathbb Z\) are winding indices. Thus puncture periods need not vanish even for coincident endpoints. Their exponentiated scalar periods have order dividing 8; **these do NOT encode base 16 by themselves**.

The ordered cross-ratio \(\lambda=((p_1-p_3)(p_2-p_4))/((p_1-p_4)(p_2-p_3))=8/5\). The two-sheeted cover \(y^2=\prod_i(z-p_i)\) has genus one by Riemann–Hurwitz and Legendre invariant \(j=256(1-\lambda+\lambda^2)^3/(\lambda^2(1-\lambda)^2)=470596/225\). This is a **legitimate elliptic cover of the pole geometry**; however, the pullback of \(\omega\) remains a logarithmic differential with residue-determined periods. A new elliptic holomorphic differential such as \(dz/y\) would require a **separate source-authenticated** transport to matter for π.

## RSP-02. Exact Pascal–residue contour for EVERY finite BBP partial sum (PROVED PAPER)

Let \(N\ge1\) be an integer and let

\[B_N(z)=\frac1{16}\sum_{k=0}^{N-1}\binom{z-1}{k}\left(-\frac{15}{16}\right)^k,\quad D_N(z)=\prod_{j=1}^{N}(z-j),\quad K_N(z)=\frac{D_N'(z)}{D_N(z)}=\sum_{j=1}^{N}\frac1{z-j}.\]

This \(B_N\) is a genuine degree-\((N-1)\) polynomial, hence rational on the entire Riemann sphere. For every integer \(1\le j\le N\), all terms with \(k\ge j\) vanish, and the **finite** binomial theorem proves
\[B_N(j)=\tfrac1{16}(1-\tfrac{15}{16})^{j-1}=16^{-j}.\]

Define the fully **rational meromorphic one-form**
\[\boxed{\Omega_N=B_N(z)r(z)K_N(z)dz.}\]

Its finite poles consist only of the four source punctures and the integers \(1,\ldots,N\), with an additional possible pole at infinity. The integer poles have EXACT residues
\[\operatorname{Res}_{z=j}\Omega_N=B_N(j)r(j)=16^{-j}r(j).\]

Choose a positively oriented contour \(\Gamma_N\) that encloses exactly \(1,\ldots,N\) (not the source punctures). The residue theorem gives
\[\boxed{\mathcal A_N:=\frac1{2\pi i}\oint_{\Gamma_N}\Omega_N=\sum_{j=1}^N16^{-j}r(j)=16^{-N}U_N=x_Np_N,}\]
where the last equality uses the **already established** original symplectic lift with \((x_0,p_0)=(0,1)\), \((x_{n+1},p_{n+1})=(16x_n+r(n+1),p_n/16)\). Finally
\[\boxed{e^{2\pi i hU_N}=\exp\!\left(h16^N\oint_{\Gamma_N}\Omega_N\right),\qquad h\in\mathbb Z.}\]

Thus **finite source accumulation, canonical action pairing, and the real-circle phase arise as three different readouts of one source-labelled contour**. The last expression is an *Abelian holonomy/character of a contour period*, not a Feynman integral over arbitrary paths. The full Weyl sum \(\sum_{n\le N}e^{2\pi i hU_n}\) is still a signed sum over MANY such finite contour phases. No bound for it is asserted.

The first two exact receipts: \(\mathcal A_1=47/240\), \(\mathcal A_2=102913/524160\); these match the native original rational recurrence. Independent Lagrange and Newton implementations agree for \(1\le N\le8\).

## RSP-03. Global residue mirror and the infinity/prime-source boundary (PROVED PAPER)

Let \(p_i,\rho_i\) be the source poles/residues. At the source punctures,
\[\mathcal R_{\mathrm{src}}(N)=\sum_{i=1}^4\rho_iB_N(p_i)K_N(p_i).\]

The global residue theorem **on the sphere**, including infinity, yields an EXACT second reading of the SAME contour action:
\[\boxed{\mathcal A_N=-\mathcal R_{\mathrm{src}}(N)-\operatorname{Res}_\infty\Omega_N.}\tag{RSP-3}\]

This is not obtained by illegally deforming a contour through poles without accounting for their residues. The source punctures and the infinity residue are the complete complement of the sampled unit punctures.

There is an independent, finite, **pure rational** formula for the infinity residue. Write \(B_N(z)=\sum_{k=0}^{N-1}b_{N,k}z^k\), let \(m_j=\sum_iw_ic_i^j\) with \(c=(7,4,3,2)\), and \(s_t(N)=\sum_{a=1}^Na^t\). Since \(m_0=0\), expansion at \(u=1/z\) gives
\[\boxed{\operatorname{Res}_\infty\Omega_N=-\sum_{k=2}^{N-1}b_{N,k}\sum_{j=1}^{k-1}\frac{m_j}{8^{j+1}}s_{k-j-1}(N).}\tag{RSP-4}\]

The proof uses \(r(1/u)=\sum_{j\ge1}m_j u^{j+1}/8^{j+1}\) and \(K_N(1/u)=\sum_{t\ge0}s_t(N)u^{t+1}\), then extracts the coefficient of \(u^{-1}\) in \(-u^{-2}B_N(1/u)r(1/u)K_N(1/u)du\). This is finite coefficient extraction, not an infinity-limit assertion. The first infinity residue occurs at \(N=3\), and is \(-10125/524288\). Exact unit tests compared RSP-4 and the independently computed finite source/sampling residues for \(N=1,\ldots,10\).

## RSP-04. Unit-SUCC time enlargement is a NEW PUNCTURE and an exact residue seam (PROVED PAPER)

Pass \(N\mapsto N+1\). The polynomials satisfy
\[B_{N+1}(z)=B_N(z)+\frac1{16}\binom{z-1}{N}(-\tfrac{15}{16})^N,\quad K_{N+1}(z)=K_N(z)+\frac1{z-N-1}.\]

All old integer residues are preserved, because \(B_{N+1}(j)=B_N(j)=16^{-j}\) for \(j\le N\). The **only new sampled residue** is \(16^{-(N+1)}r(N+1)\) at \(z=N+1\). Thus
\[\boxed{\mathcal A_{N+1}-\mathcal A_N=16^{-(N+1)}r(N+1),}\]
\[\boxed{\Delta_N\left(\mathcal R_{\mathrm{src}}+\operatorname{Res}_\infty\Omega\right)=-16^{-(N+1)}r(N+1).}\]

**Geometric interpretation:** the successor-to-successor move adds one universal sampling puncture, retaining old arithmetic residues while the source/infinity dual repartitions by the opposite signed amount. Distinguish a geometrically selected path from an arbitrary path across punctures; the period is determined by winding data.

## RSP-05. SOURCE-SPECIFIC logarithmic divergence, Euler–Mascheroni finite part (PROVED PAPER, classical digamma input)

For any fixed \(p\in(0,1)\), the binomial series at \(-15/16\) yields \(B_N(p)\to16^{-p}\) with exponentially decaying error \(O_p((15/16)^N N^{-p})\). Moreover
\[K_N(p)=\sum_{j=1}^N\frac1{p-j}=\psi(1-p)-\psi(N+1-p)=-\log N+\psi(1-p)+O_p(N^{-1}),\]
where \(\psi\) is the digamma function. Therefore
\[\mathcal R_{\mathrm{src}}(N)=-\log N\sum_i\rho_i16^{-p_i}+C_0+o(1),\quad C_0:=\sum_i\rho_i16^{-p_i}\psi(1-p_i).\]

**The original source gives a remarkably exact weighted residue identity**:
\[\sum_i\rho_i16^{-p_i}=\frac{\sqrt2}{32}-\frac1{16}-\frac{\sqrt2}{32}-\frac1{16}=\boxed{-\frac18}.\]

Consequently the four source punctures contribute **+one eighth of a harmonic divergence**:
\[\boxed{\mathcal R_{\mathrm{src}}(N)=\tfrac18\log N+C_0+o(1).}\]

Using the standard rational digamma values (Gauss, reflection and multiplication),
\[\boxed{C_0=\frac\gamma8+\frac5{16}\log2-\frac{3\pi}{32}-\frac18\log(1+\sqrt2).}\]

The finite-part identity was independently checked symbolically using the digamma special values and to >50 decimal places; those computations do not replace the paper derivation. References for imported formulas: NIST DLMF §§5.4.19 and 5.5.4 (https://dlmf.nist.gov/5.4 and https://dlmf.nist.gov/5.5). An **exact finite** alternative, requiring no special functions, is to write \(H_N=\sum_{j\le N}1/j\), \(D_N(p)=\sum_{j\le N}(1/(j-p)-1/j)\):
\[\mathcal R_{\mathrm{src}}(N)=-H_N\sum_i\rho_iB_N(p_i)-\sum_i\rho_iB_N(p_i)D_N(p_i).\]
The exact rational finite-sum identity is checked independently for \(N=1,\ldots,9\).

Because the original BBP identity supplies \(\mathcal A_N\to\pi/16\), the global residue equation RSP-3 now forces
\[\boxed{\operatorname{Res}_\infty\Omega_N=-\tfrac18\log N-\frac\pi{16}-C_0+o(1).}\]

**This is a rigorously typed source/infinity cancellation**: a +log divergence on the finite source-pole side and its opposite at the infinity boundary cancel to give the finite BBP constant. Neither individual side is a convergent infinity limit. It aligns structurally with SUCC's Euler–Mascheroni boundary themes but gives no selected signed digit equidistribution.

## RSP-06. Scalar periods necessarily erase NONCOMMUTING source history (PROVED PAPER / counterexample)

The affine original-source step has a faithful endpoint matrix
\[F_j=\begin{pmatrix}16&r(j)\\0&1\end{pmatrix}.\]
The actual ordered product is \(F_N\cdots F_1=\begin{psmallmatrix}16^N&U_N\\0&1\end{psmallmatrix}\). But the two original first source steps already fail to commute:
\[\boxed{(F_2F_1)_{12}-(F_1F_2)_{12}=15(r(1)-r(2))=\frac{12301}{273}\ne0.}\]

In contrast, **any scalar one-form integral is additive** under path concatenation and kills all path commutators. Thus the above Abelian sphere-contour action can preserve the authentic cumulative value but cannot represent ALL original noncommuting word histories. To meet the complete user proposal, retain the source-labelled ordered word groupoid, or add a separately defined NONABELIAN flat local system / path-ordered parallel transport whose based-loop generators are authenticated by the original affine steps. Such a lift is a possible mathematical construction, **not** a result derived for free from the logarithmic source differential. Existing SUCC `operational_yoneda_descent.ObservationPathCategory` is the approved spine; do not mint a rival core.

## RSP-07. Precise boundary to π normality (OPEN)

The full selected Weyl sum is
\[S_M(h)=\sum_{N=1}^M\exp\!\left(h16^N\oint_{\Gamma_N}\Omega_N\right).\]
This equation is **exact but does not bound its own signed sum**. The form \(\Omega_N\) and its sphere punctures also **depend on N**; a finite rational meromorphic form does not imply one fixed meromorphic form on the compact sphere in the infinite limit. A source seed \(s\ne0\) changes the initial action \(\mathcal A_0=s\) while leaving every original forcing pole unchanged, so source-pole geometry alone is seed-BLIND. The selected `U0=0`, full four signed poles, Archimedean phase and all-horizon covariance must stay coupled. The proven source/infinity log divergence is NOT a Weyl saving.

**Verdict:** exact source-faithful finite contour and residue-boundary machinery with a nonabelian-history obstruction; π base16 normality and RH OPEN. Next probe is a new source-selected signed estimate, tested against q=1/5 coherent same-forcing altered seed, near-zero shadows, positive moment-matched fake, joint-phase triple-lock and changing sampling windows. Historical `formal/`, source and claim registries remain untouched.
