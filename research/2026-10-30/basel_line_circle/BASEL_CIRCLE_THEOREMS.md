# Operation Basel × Line–Circle Carrier: finite topology, Gamma completion and the original BBP 59-jet

**2026-10-30 — DRAFT RESEARCH ONLY.** Based on pinned Universal N PR #416 head \`725377a64748ab0c442d16a61509b99687412505\`, itself stacked on the existing SUCC work from merged Main XVI. Read-only related branches: PR #390 (time extrusion/Green tail), #397 (line/circle holonomy), #402 (three-atom rank and curvature qualification), #404 (Noether/pure scalar coboundary), #416 (universal N, BBP rational multiplicative potential), #418 (Pisot ramification), #419 (Pisot lattice holonomy). This dossier introduces **only declared finite observer operators**: no changes to original four signed BBP poles, original U0=0, historical proof contracts, workflows, production, archives, or main. The base-16 normality of π, RH, and a canonical physical BBP spacetime remain OPEN.

## 0. Steelman / object / truth-reference

The author wants to know what **an observer embedded in N or Z** can infer about the circular curvature/closure of the continuum when the actual finite counting realization is compared with its analytic completion, and why Basel, Bernoulli, Gamma, Euler–Mascheroni, the harmonic/golden triangle and Oily–Macaroni keep appearing. The strong, testable version is **not** that an intrinsically one-dimensional circle has nonzero Riemann curvature (it does not), but that the observer can measure global closure and source-dependent transport through a declared local response law, while keeping separate (i) combinatorial finite counting, (ii) source-specific arithmetic, (iii) global topology/holonomy, (iv) renormalization and (v) the selected BBP signed orbit. A meaningful theorem must distinguish the closed carrier from the open line with finite measurements and honest source- versus model-adequacy controls.

For N≥3 let \(C_N=\mathbb Z/N\mathbb Z\) be the N-cycle with vertices 0,...,N−1. Fix a counterclockwise edge ordering. An edge with positive conductance \(w_j\) has electrical resistance \(r_j=1/w_j\). The symmetric graph Laplacian \(L_{N,\mathbf w}\) has a one-dimensional constant kernel. Its Moore–Penrose pseudoinverse \(G_{N,\mathbf w}=L_{N,\mathbf w}^+\) is the **zero-mean** Green response. This is a mathematical finite observer instrument, not something the original π digits have been shown to implement physically.

### External/classical provenance

- NIST DLMF §24.8, Bernoulli polynomial Fourier series https://dlmf.nist.gov/24.8 .
- NIST DLMF §5.5 Gamma reflection https://dlmf.nist.gov/5.5 , §5.7 Gamma Taylor/zeta expansion https://dlmf.nist.gov/5.7 , §5.15 polygamma https://dlmf.nist.gov/5.15 .
- Jorgenson, Karlsson and Smajlović (2023), *The resolvent kernel on the discrete circle and twisted cosecant sums*, https://arxiv.org/abs/2305.00202 . Its abstract explicitly obtains the discrete-circle resolvent both through Fourier/spectral methods and as a quotient of Z; the local source-weighted observations below are SUCC specializations, not a claim of academic priority.
- Standard Kirchhoff effective resistance, weighted cycle series/parallel reduction, rank-one inverse update and the finite matrix determinant lemma are used with derivations here rather than assumed as new mathematics.

## BL-01. Universal finite line/circle closure: explicit resistance, Green and Basel (EXACT)

With all \(w_j=1\), the nonzero eigenvalues are
\[
\lambda_k=4\sin^2(\pi k/N),\quad k=1,\ldots,N-1.
\]
The zero-mean graph Green function and trace are
\[
\boxed{g_N(j)=\frac{N^2-1}{12N}-\frac{j(N-j)}{2N},\quad
\operatorname{Tr}L_N^+=\frac{N^2-1}{12}.}
\]
To verify, \(L_Ng_N=\delta_0-\frac1N\), \(\sum_jg_N(j)=0\); uniqueness on \(1^\perp\) gives the Green formula. The effective resistance between vertices at graph separation \(k\), 0<k<N, is
\[
R_{C_N}(0,k)=g_N(0)+g_N(0)-2g_N(k)=\frac{k(N-k)}N.
\]
On the open line, the resistance is \(k\), so the **exact closure defect** is \(k^2/N\). A finite-range observer cannot see this if it samples only local adjacency, but can detect it with a global response or paths wrapping around the loop.

Choose a physical circumference L>0, mesh \(h=L/N\), and continuum coordinate \(x=kh\). The continuum mean-zero Green kernel of \(-\partial_x^2\) on a circle is
\[
\boxed{G_L(x)=\frac L{12}-\frac x2+\frac{x^2}{2L}
=\frac L2 B_2(x/L),\quad 0\le x\le L,}
\]
periodically extended, satisfying \(-G_L''=\delta_0-L^{-1}\). **At every finite grid vertex**, with no asymptotics,
\[
\boxed{G_L(kh)-h g_N(k)=\frac{L}{12N^2}.}
\]
The dimensionally scaled Laplacian is \(L_{N,h}=h^{-2}L_N\); its pseudoinverse trace is
\[
\operatorname{Tr}L_{N,h}^+=h^2\frac{N^2-1}{12}
=\frac{L^2}{12}(1-N^{-2}).
\]
The continuum Fourier spectrum \((2\pi n/L)^2\), \(n\ne0\), gives
\[
\frac{L^2}{12}=\frac{L^2}{4\pi^2}\sum_{n\ne0}n^{-2}
=\frac{L^2}{2\pi^2}\zeta(2)
\quad\Rightarrow\quad\boxed{\zeta(2)=\frac{\pi^2}{6}.}
\]
This is the finite arithmetic-to-Basel comparison. The same Bernoulli polynomial \(B_2(x)=x^2-x+1/6\) accounts for the 1/12; via the **separate** analytic-continuation prescription, \(\zeta(-1)=-1/12\). Never interpret \(-1/12\) as the ordinary convergent sum \(\sum n\). A one-dimensional smooth circle is intrinsically Riemann-flat; the closure/zero-mode and possible extrinsic curvature are separately typed.

## BL-02. Finite global U(1) holonomy: EXACT weighted magnetic determinant

Give each oriented edge \(j\to j+1\) a unit complex transport with product \(e^{i\theta}\). By gauge rechart all but the closing edge can be made 1, while the closing edge has \(e^{i\theta}\). The N×N twisted incidence \(D_\theta\) has determinant \(1-e^{i\theta}\) up to phase and the Hermitian magnetic Laplacian is \(L^\theta=D_\theta^*\,\operatorname{diag}(w_j)\,D_\theta\). Therefore for EVERY N≥3 and EVERY positive edge-weight vector:
\[
\boxed{\det L_{N,\mathbf w}^{(\theta)}
=(2-2\cos\theta)\prod_{j=0}^{N-1}w_j.}
\]
The source-dependent amplitude \(\prod w_j\) and the gauge-invariant loop phase **factor exactly**. This determinant remains zero at \(\theta=0\) because the constant mode survives.

**Original arithmetic scalar-phase null:** if the proposed edge link is only \(A_{uv}=h(U_v-U_u)\) for a single global state function U and a fixed harmonic h, every closed loop has lifted sum 0 and U(1) product 1. Nonzero fractional-branch winding without independent transport is a chart/carry record, not automatically gauge curvature. Thus neither the original BBP source nor the zero seed creates a nontrivial \(\theta\) by this scalar construction. Any \(\theta\ne0\) here is a DECLARED independent interaction/contact observable.

For \(\theta=2\pi t\ne0\), divide out the source amplitude and the small-twist quadratic zero. Gamma reflection gives, EXACTLY AT FINITE N,
\[
\boxed{\frac{\det L_{N,\mathbf w}^{(2\pi t)}}{(2\pi t)^2\,\prod_jw_j}
=\left(\frac{\sin\pi t}{\pi t}\right)^2
=\frac1{\Gamma(1+t)^2\Gamma(1-t)^2}.}
\]
Extend analytically at t=0 with value 1. The logarithmic second derivative there is \(-4\zeta(2)=-2\pi^2/3\). The first derivative cancels by orientation symmetry; this provides a rigorous Gamma/Basel **second-order response** of finite loop holonomy, not proof of intrinsic Gaussian curvature or actual BBP gauge flux.

**Spectrum versus source order firewall:** \(\prod_jw_j\) and hence twisted determinant is blind to source order along the loop. A weighted Green trace is not. Exact counterexample on C4: weights (1,2,3,4) versus (1,3,2,4) both have determinant \(24(2-2\cos\theta)\), but \(\mathrm{Tr}\,G=29/50\) versus \(119/200\). Two observations are required if arrangement, not just aggregate amplitude, is part of the carrier question.

## BL-03. General source-marked *single edge*: exact rank-one Green transport

Let \(L_{N,w}=L_N+\tau bb^\top\), \(\tau=w-1>-1\), and \(b=e_0-e_1\). On the mean-zero subspace the Sherman–Morrison identity holds:
\[
G_{N,w}=G_N-\frac{\tau\,G_Nbb^\top G_N}{1+\tau\,b^\top G_Nb}.
\]
The universal cycle has
\[
b^\top G_Nb=\frac{N-1}{N},\qquad
b^\top G_N^2b=\frac{N^2-1}{12N}.
\]
The second follows by discrete Fourier transform or direct polynomial Green differences. Therefore
\[
\boxed{\mathrm{Tr}G_{N,w}-\mathrm{Tr}G_N
=-\frac{(w-1)(N^2-1)}{12[N+(w-1)(N-1)]}.}
\]
The pseudo-determinant is \(\prod_{\lambda>0}\lambda=N[1+(N-1)w]\), while the nontrivially twisted determinant is \(w(2-2\cos\theta)\); zero-mode normalization and twist are different operations.

### A declared native source/contact map, including a hostile matched-rank mutant

Use the exact ORIGINAL BBP forcing
\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)}.
\]
A natural but **DECLARED** sensor-reference conductance is \(w(a)=R(a)/(15/a^2)=a^2R(a)/15\), comparing the original Laplace source against its Gamma-rank-two leading reference \(Q_*(x)=15x\). For a>0,
\[
\boxed{w(a)=\frac{a(15a^2+121a+240)}{15(a+3)(a+4)(a+5)},\quad
w(a)-1=-\frac{59a^2+465a+900}{15(a+3)(a+4)(a+5)}.}
\]
It is positive and <1. Setting a=a_N=8N−7 in the exact single-bond formula gives
\[
\boxed{\Delta_N^{(1)}
=\frac{(N^2-1)(59a^2+465a+900)}
{12(15Na^3+121Na^2+240Na+59a^2+465a+900)}
=\frac{59}{1440}+\frac{6031}{172800N}+O(N^{-2}).}
\]
The first coefficient uses precisely the authentic source's \(-59\) second jet; no selected arithmetic orbit or unknown digit is needed.

Hostile positive mutant with the SAME leading rank-two/Gamma/Pascal/golden law:
\[
Q_{\rm mut}(x)=5(1-e^{-3x}),\quad R_{\rm mut}(a)=15/[a(a+3)],\quad
w_{\rm mut}(a)=a/(a+3).
\]
It yields \(\Delta_N^{(1,\rm mut)}\to1/32\), not 59/1440. Thus the observer sees source-specific higher-jet arithmetic even though the universal limiting Gamma rank agrees. **Neither sensor response distinguishes the SAME-forcing coherent counterseed \(s_*=-\pi/16\) from authentic \(U_0=0\).**

The numerical proximity of 59/1440≈0.0409722222 to Oily–Macaroni \(\varphi^{-1}-\gamma≈0.04081832385\) is *not an identity*. An explicit exact-rational certificate uses 1000 harmonic summands, rigorous bounds \(H_N-\log N-\frac1{2N}<\gamma<H_N-\log N-\frac1{2(N+1)}\), the alternating-free positive atanh expansion for \(\log10\) at \(u=9/11\), and integer-square-root bounds for \(\sqrt5\). It proves \(\varphi^{-1}-\gamma<0.040818408<59/1440\), using no unbounded numerical-probe extrapolation. The reproducible oracle retains the rational certificate.

## BL-04. All-edge *native* BBP clock: exact Gamma determinant, harmonic divergence and digamma renormalization

For every \(N\ge3\), label edge \(n-1\to n\bmod N\) with the SOURCE-DEFINED conductance \(w_n=w(a_n)\), \(a_n=8n-7\), with the original R(a) above. This choice is a declared observer wiring, not a consequence of π's signed digits. Put
\[
\lambda_\pm=\frac{121\pm\sqrt{241}}{30},\qquad
q_0=\frac18,\quad q_\pm=\frac{151\pm\sqrt{241}}{240},\quad
r_1=\frac12,\ r_2=\frac58,\ r_3=\frac34.
\]
The original source conductance factorizes exactly:
\[
w(a)=\frac{a(a+\lambda_+)(a+\lambda_-)}{(a+3)(a+4)(a+5)}.
\]
Therefore its N-fold native-clock product is a SIX-factor Gamma quotient:
\[
\boxed{\mathscr W_N=\prod_{n=1}^{N}w_n
=\frac{\prod_{q\in\{q_0,q_+,q_-\}}\Gamma(N+q)/\Gamma(q)}
{\prod_{r\in\{r_1,r_2,r_3\}}\Gamma(N+r)/\Gamma(r)}.}
\]
As \(\sum_q q-\sum_r r=-59/120\), Stirling/Gamma ratio asymptotics prove
\[
\boxed{\mathscr W_N=C_w N^{-59/120}(1+O(N^{-1})),\qquad
C_w=\frac{\Gamma(1/2)\Gamma(5/8)\Gamma(3/4)}
{\Gamma(1/8)\Gamma(q_+)\Gamma(q_-)}
=0.200550308149309758\ldots .}
\]
Combining with BL-02:
\[
\boxed{\det L_{N,\mathbf w}^{(\theta)}
=(2-2\cos\theta)\mathscr W_N.}
\]
This is a **finite arithmetic → Gamma → global loop-determinant** theorem. For fixed \(\theta\notin2\pi\mathbb Z\), \(\log\det=-\frac{59}{120}\log N+\log C_w+\log(2-2\cos\theta)+O(N^{-1})\).

A particularly clean completed response is
\[
\boxed{\lim_{N\to\infty}N^{59/120}
\frac{\det L_{N,\mathbf w}^{(2\pi t)}}{(2\pi t)^2}
=\frac{C_w}{\Gamma(1+t)^2\Gamma(1-t)^2}.}
\]
The \(\Gamma(q)\) factors on the RHS's overall amplitude authenticate the source; \(\Gamma(1\pm t)\) encodes the universal geometric twist. The second derivative in t is the Basel response, independently of source selection.

Now take reciprocal resistances \(\rho_n=1/w_n=1+\delta_n\). The EXACT original-source rational formula is
\[
\boxed{\delta_n=\frac{472n^2-361n+67}{(8n-7)(120n^2-89n+16)}
=\frac{59}{120n}+f_n,\quad
f_n=\frac{48248n^2-36269n+6608}{120n(8n-7)(120n^2-89n+16)}.}
\]
For every n≥1, \(0<f_n\le4/n^2\) (n=1 direct, n≥2 via crude polynomial bounds). Let \(D_N=\sum_{n=1}^{N}\delta_n\), \(c=59/120\). Then
\[
D_N=c H_N+\sum_{n\le N}f_n,\quad
\left|\sum_{n>N}f_n\right|<4/N,\quad
D_N=c\log N+\mathcal C_{\rm res}+O(N^{-1}).
\]
Here is a **source-specific digamma realization** of the constant:
\[
\alpha_0=\frac{15}{32},\quad
\alpha_\pm=\frac{2651\mp19\sqrt{241}}{231360},\qquad
\sum\alpha=\frac{59}{120},
\]
\[
\delta_n=\sum_{q\in\{q_0,q_+,q_-\}}\frac{\alpha_q}{n-1+q},
\quad
\boxed{\mathcal C_{\rm res}=-\alpha_0\psi(q_0)-\alpha_+\psi(q_+)-\alpha_-\psi(q_-)
=3.9660550275954530133\ldots .}
\]
Equivalently \(\mathcal C_{\rm res}=c\gamma+\sum_{n\ge1}f_n\). So the Euler–Mascheroni constant appears explicitly as the finite-N harmonic/logarithmic discrepancy, whereas the remaining finite-source correction is an independently convergent series. This is **genuine** Gamma/harmonic source threading, not the assertion that Oily–Macaroni is a topological invariant.

## BL-05. Arbitrary weighted-cycle Green response from finite prefix counting (EXACT O(N) formula)

For arbitrary positive resistances \(\rho_j\), j=0,...,N−1, put \(S=\sum_j\rho_j\), \(P_j=\sum_{e<j}\rho_e\), \(P_0=0\), j=0,...,N−1. The resistance between vertices i<j is the parallel combination of the two oriented arcs:
\[
R_{ij}^{eff}=\frac{(P_j-P_i)(S-P_j+P_i)}S.
\]
The Kirchhoff trace identity is \(\mathrm{Tr}L^+=(1/N)\sum_{i<j}R_{ij}^{eff}\). Collect all pairs using \(\sum_{i<j}(P_j-P_i)^2=N\sum_jP_j^2-(\sum_jP_j)^2\); this gives the completely finite O(N)-arithmetic formula:
\[
\boxed{\mathrm{Tr}L_{\rho}^{+}
=\frac{S\sum_{j=0}^{N-1}(2j-N+1)P_j
-N\sum_{j=0}^{N-1}P_j^2+(\sum_{j=0}^{N-1}P_j)^2}{NS}.}
\]
The observer needs no continuum coordinate and no eigenvector computation; all inputs can be exact positive rationals. Independent Fraction pseudoinverses, pairwise resistances and prefix-statistic evaluations agree for all tested N.

For the ORIGINAL native \(\rho_n=1+\delta_n\), let \(F_N=\mathrm{Tr}L_{N,\mathbf w}^{+}\), \(F_N^0=(N^2-1)/12\), \(D_N=\sum_n\delta_n\). A uniform, rigorous perturbation bound is
\[
\boxed{\left|F_N-F_N^0-\frac{N^2-1}{12N}D_N\right|
\le\frac58 D_N^2.}
\]
**Proof sketch with full quantifiers.** For any i<j, let k=j−i and E be the excess resistance along that arc (0≤E≤D). The weighted resistance is \((k+E)(N-k+D-E)/(N+D)\). Its linearization at D=0 is \(k(N-k)/N+L_{ij}\), where \(L_{ij}=[(N-k)^2E+k^2(D-E)]/N^2\in[0,D]\). The exact residual is \(-DL_{ij}/(N+D)+E(D-E)/(N+D)\), whose absolute value ≤\(5D^2/(4N)\). Sum over N(N−1)/2 unordered vertex pairs and divide by N. By cyclic symmetry the sum of the linear terms equals \((N^2-1)/(12N)D\). This proves the displayed bound.

Since \(D_N=c\log N+\mathcal C_{\rm res}+O(N^{-1})\), the original-source Green correction has a **two-term renormalized asymptotic**:
\[
\boxed{
F_N-F_N^0
=\frac{59}{1440}N\log N
+\frac{\mathcal C_{\rm res}}{12}N
+O((\log N)^2).
}
\]
Thus there is an exact *paired spectral signature*:
\[
\boxed{
-\lim_{N\to\infty}\frac{\log[\det L_{N,\mathbf w}^{(\theta)}/(2-2\cos\theta)]}{\log N}
=\frac{59}{120},\quad
\lim_{N\to\infty}\frac{F_N-F_N^0}{N\log N}
=\frac{59}{1440}.}
\]
The second is precisely 1/12 of the first. The agreement does NOT imply that one spectral instrument reconstructs the complete source's ordered arrows; the edge-order counterexample in BL-02 refutes that stronger inference.

**Matched-rank mutant:** \(w^{mut}(a)=a/(a+3)\) gives reciprocal excess \(3/a\), so its Gamma-product exponent is −3/8, and its native Green correction is \(+\frac1{32}N\log N+O(N)\). The original source is discriminated by the 59-jet despite identical leading Gamma rank.

## BL-06. The actual continuum seam threshold: fixed local source ≠ macroscopic curvature

The unscaled graph trace grows like N². Under fixed circumference L the physical trace is \((L/N)^2 F_N\). Therefore the ORIGINAL all-edge source mark satisfies
\[
\frac{L^2}{N^2}(F_N-F_N^0)=
\frac{59L^2}{1440}\frac{\log N}{N}+O(L^2/N)\longrightarrow0.
\]
Similarly the native single-edge source correction \(59/1440\) vanishes after physical scaling as \(L^2/N^2\). **The source 59-jet does NOT produce a finite nonzero continuum Riemann-curvature or topology defect in this declared scaling.** The finite arithmetic defect is real, but depends on operator normalization and the count/continuum transfer.

There is a separate, sharp macroscopic line/circle contact threshold. For a single closing edge conductance w_N>0,
\[
F_N(w_N)-F_N^0=
\frac{(1-w_N)(N^2-1)}{12[1+(N-1)w_N]}.
\]
If \(Nw_N\to c\in[0,\infty)\), then for physical circumference L:
\[
\boxed{
\lim_{N\to\infty}\frac{L^2}{N^2}(F_N(w_N)-F_N^0)
=\frac{L^2}{12(1+c)}.
}
\]
w_N=0 means open path, giving exactly \(F_N(0)=(N^2-1)/6\), twice the unweighted cycle trace. Conversely if \(Nw_N\to\infty\) with 0<w_N≤1, the scaled defect disappears. The genuine macroscopic seam strength is of order \(1/N\), while the ORIGINAL normalized source weight \(w(a_N)\to1\) stays far from this regime.

This is an operational topology/completion distinction, NOT intrinsic 1D Riemann curvature. Do not promote the numerical gamma/oily resemblance into physics.

## BL-07. SUCC Gamma/Oily first and second response: exact but typed cross-identifications

At the ORIGINAL rank-two Gamma boundary \(Y\sim\Gamma(2,1)\), its Mellin cumulant generator \(\log\mathbb E Y^t=\log\Gamma(2+t)-\log\Gamma(2)\) gives
\[
\mathbb E\log Y=\psi(2)=1-\gamma,\qquad
\operatorname{Var}(\log Y)=\psi_1(2)=\zeta(2)-1.
\]
For a circle of circumference 2π, half of the nonzero-mode inverse trace is \(\zeta(2)\), and deleting the two first modes ±1 from the full trace produces \(\zeta(2)-1\) after dividing by two. Hence the Gamma log variance equals a particular **spectrally truncated circle response**. This is an exact equality between independently defined objects, not a canonical isomorphism between the physical Gamma and circle carriers.

For \(\lambda=\varphi^{-1}\), SUCC's declared golden Laplace mark is \(\mathbb E e^{-\lambda Y}=\lambda^2\). The same rank-two source gives
\[
\boxed{(1-\gamma)-\lambda^2=\lambda-\gamma=\Omega_{\rm OM}.}
\]
The first cumulant / golden mark and the second cumulant / Basel remainder are **different observation orders of the same Gamma law**. Nothing shown makes \(\Omega_{\rm OM}\) itself a chart-invariant curvature.

The projective marked-circle chart \(z=\tan(\theta/2)\) has pullback metric \(ds^2=4dz^2/(1+z^2)^2\), and the Möbius map \(D(z)=(z-1)/(z+1)\) is exactly a quarter-turn (a round-metric isometry). Finite integer line steps are compressed near infinity as \(2\arctan(n+1)-2\arctan n\sim 2/n^2\), but that series **telescopes exactly** and cannot be declared the Basel sum without an independent transport theorem.

## BL-08. Actual BBP signed orbit/seed firewall and decisive next test

The authenticated original recurrence remains
\[
U_0(0)=0,\qquad U_{n+1}(0)=16U_n(0)+R(8(n+1)-7),
\quad
\kappa_{n+1}=\lfloor16\{U_n\}+r_{n+1}\rfloor .
\]
The source-weighted circle instrument depends on the *forcing* R and the declared clock/edge embedding, not on the selected seed. Therefore every computed source-only conductance, Gamma determinant, digamma renormalization and Green trace is also valid for the coherent same-forcing seed \(s_*=-\pi/16\), which has a nonnormal phase orbit. This is a decisive countermodel to **source-only circle/Basel response ⇒ π normality**.

An additional tempting "phase-flux proof" sets \(\theta_n=2\pi hU_n(0)\) by fiat. Then
\[
\frac{\det L_{N,\mathbf w}^{(\theta_n)}}{\prod_j w_j}
=2-2\cos(2\pi hU_n(0)),
\]
which is **exactly** the original phase-slip observable in disguise. It provides no independently derived long-range bound. The gauge class must be derived from original four-pole / selected integer carries and operationally calibrated paths, not fitted to the desired Weyl cancellation. In contrast, if every edge phase is a difference of one globally defined scalar, the holonomy is exactly trivial, even at finite N.

### Ledger conclusions

- **DISCLOSED (classical exact and newly specialized):** finite cycle Green/Basel, Bernoulli pointwise error, magnetic determinant and Gamma reflection, arbitrary single-bond rank-one trace, original source \(w(a)\) and mutant, exact six-Gamma source determinant, exact digamma resistance constant, O(N) arbitrary weighted Green prefix statistic, rigorous 5/8 error bound, original 59/1440 N log N asymptotic and mutant 1/32, weak seam \(w_N\sim c/N\) continuum phase boundary, source-order blindness of magnetic determinant, source-only seed blindness.
- **DECLARED observer models:** selecting conductances as \(w(a)=a^2R(a)/15\), attaching them to C_N, choosing a nontrivial U(1) flux, promoting any finite graph response to physical space.
- **REFUTED (with receipts):** intrinsic nonzero 1D smooth circle Riemann curvature; Gamma/Oily equals 59/1440; source-weighted Green correction survives fixed-L continuum scaling; magnetic determinant reconstructs ordered source edges; scalar exact-phase differences generate nontrivial holonomy; original positive source circle trace alone proves normality.
- **UNVERIFIED / OPEN:** canonical original BBP-to-physical circle transport; independent source-and-U0=0-selected nonflat loop interaction; any positive-density selected signed cancellation, π normality, RH.
- **New verdict-changing probe:** obtain two path-composable, source-faithful, zero-seed-sensitive transport maps for the original signed four-pole trajectory, including literal integer lifts and an operational winding/holonomy condition. Require nonflatness to survive gauge ablation and to discriminate same-source coherent seed, Gamma-rank mutant and independent normal Stoneham controls. Then derive a **new** all-horizon signed or occupancy inequality; do not re-label an assumed phase-slip as a determinant.

**Validation:** Python stdlib 16/16 exact Fraction tests locally PASS; separately authored SymPy/mpmath oracle PASS, including a genuinely rigorous rational interval distinguishing Oily from 59/1440. Prior to final successful run, the oracle had a small SymPy Rational-construction error; repaired without changing source inputs. Full SUCC AGENTS provenance/full unit suite, hosted exact-head CI, Lean and outside referee were NOT RUN. A finite graph model is not an empirical gravitational-wave measurement or a theorem about digit normality.
