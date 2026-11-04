# Causal Echo Tomography: exact finite-history blind spots and source-qualified reconstruction

**2026-11-02. RESEARCH-ONLY PAPER DERIVATIONS; NOT a π-normality or RH proof.** Exact stacked parent #466 at c71b18dba200c2d227d9c084bbb9d8399f81ede3, over #464/#463/#462/#460/#459 and Main XIX 81045770234a114247e43eb08ae5c6d446e9514a. Original signed four poles, U0=0, frozen historical proofs, production, formal/Lean and main remain UNMODIFIED. Classical moments/convexity/normal-number facts are not academic priority claims.

## Source and the causal observer: original exact four poles

Let b=16, e(t)=exp(2πit), and
\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},\quad
U_0=0,\quad U_n=16U_{n-1}+r(n).
\]
As inherited from the original source and PR #440,
\[
r(n)=\int_0^1 x^{n-1}f(x)dx,\quad
f(x)=\frac18x^{-7/8}P(x^{1/8}),\
P(v)=4-2v^3-v^4-v^5=(1-v)(v^2+2)(v^2+2v+2)>0.
\tag{0}
\]
Its completed boundary is
\[
\alpha=\sum_{n\ge1}16^{-n}r(n)
=\int_0^1\frac{f(x)}{16-x}dx=\pi/16.
\tag{1}
\]
Write \(T_n=\sum_{j\ge1}16^{-j}r(n+j)>0\); then \(U_n=16^n\alpha-T_n\) and \(\sum_n T_n<\infty\), inherited source-tail estimates. Consequently the selected fixed-h Weyl sums \(S_N(h)=\sum_{n=1}^Ne(hU_n)\) differ by O_h(1) from \(\sum_{n=1}^Ne(h16^n\alpha)\). Any normality assertion needs a NEW signed estimate for the exact original source.

Finite causal observations through horizon M are the vector \(q_M(\mu)=(r(1),...,r(M))\) and its zero-seeded state path \((U_0,...,U_M)\), each derived from the SAME positive source measure \(\mu=f(x)dx\). Our controls change the source AFTER this observational cut, not the authentic source.

## CE-01. Source-complete, 95%-matched, **entire** echo-null perturbation for EVERY finite horizon (PROVED PAPER)

Fix any integer M>=1 and rational endpoints \(a=1/4\), \(c=1/2\). Let
\[
g_M(x)=
\begin{cases}
(x-a)^{M+1}(c-x)^{M+1},&a\le x\le c,\\
0,&\text{elsewhere},
\end{cases}
\qquad \psi_M=g_M^{(M)}.
\tag{2}
\]
The piecewise polynomial is \(C^M\) because its derivatives through order M vanish at each endpoint; g_M and its first M−1 derivatives vanish there. The signed density ψ_M has compact support [a,c], and repeated **finite** integration by parts gives
\[
\boxed{\int_a^c x^{n-1}\psi_M(x)dx=0\quad(1\le n\le M).}\tag{3}
\]
For EVERY integer n>M the *same* integration-by-parts proof yields
\[
\boxed{
\int_a^c x^{n-1}\psi_M(x)dx
=(-1)^M\frac{(n-1)!}{(n-1-M)!}
\int_a^c x^{n-1-M}g_M(x)dx\ne0.
}\tag{4}
\]
Thus the subsequent forcing difference has a definite sign for fixed sign ε, not an assumed random perturbation.

Let B_M be the positive rational \(\sum_{k\ge0}|[x^k]\psi_M|\) in the polynomial representation of ψ_M on [a,c]. Since 0<=x<=1, \(\sup|\psi_M|\le B_M\). For x∈[1/4,1/2], \(u=x^{1/8}<15/16\) because \(2\cdot15^8>16^8\); hence \(P(u)>(1/16)\cdot2\cdot2=1/4\), and \(f(x)>1/32\).

For ANY real ε with \(|\epsilon|B_M\le1/1000\), define
\[
\boxed{
f_{\epsilon,M}(x)=f(x)+\epsilon\psi_M(x),\quad
r_{\epsilon,M}(n)=\int_0^1x^{n-1}f_{\epsilon,M}(x)dx.
}\tag{5}
\]
Then **pointwise for all x∈(0,1)**,
\[
\boxed{\frac{19}{20}f(x)\le f_{\epsilon,M}(x)\le\frac{21}{20}f(x).}\tag{6}
\]
(Actually the explicit relative deviation is <32/1000, not merely 5%; outside [a,c] the measures agree.)

Therefore for ALL integers n>=1, d>=0, the complete Hausdorff source jets obey
\[
\boxed{
\frac{19}{20}(-1)^d\Delta^dr(n)\le
(-1)^d\Delta^dr_{\epsilon,M}(n)\le
\frac{21}{20}(-1)^d\Delta^dr(n),
}\tag{7}
\]
and every term is strictly positive. The same inequality holds for all mixed analytic time derivatives \((-1)^{j+d}\partial_z^j\Delta^d r_{\epsilon,M}(z+1)\) at EVERY real z>−1/8, j,d>=0, since the integral kernel \(x^z(-\log x)^j(1-x)^d\) is nonnegative. Thus all unit×differential positivity and relative-order data from #440/#463 are retained globally.

Source equality through M is EXACT by (3). Consequently the zero-seeded selected state U_n and **all** its exact rational values / circle characters / causal response fields for n<=M are the same on original and counterfeit trajectories. For fixed rational ε, every new source value is rational because ψ_M is rational polynomial on a rational interval, despite the positive measure containing the original non-polynomial density.

**Meromorphic-source/pole firewall:** the complex-time difference
\[
\delta r(z)=r_{\epsilon,M}(z)-r(z)
=\epsilon\int_a^c x^{z-1}\psi_M(x)dx
\tag{8}
\]
is **ENTIRE** in z (compact support away from zero). Its integer values satisfy
\[
|\delta r(n)|\le |\epsilon|B_M(c-a)c^{n-1}
\le\frac{1}{2000}\,2^{-n}.
\tag{9}
\]
Every fixed complex-time derivative along n>=1 satisfies a similar exponentially decaying bound, with an additional constant \((\log4)^j\). The original rational meromorphic source and r_ε thus have the SAME poles, principal parts, and full inverse-power asymptotic expansions, despite not being the same global meromorphic function. It is invalid to call the counterfeit the exact four-pole rational law.

## CE-02. The completed constant can be chosen NORMAL or NONNORMAL without changing ANY observed finite source history (PROVED PAPER)

The completion functional on a finite positive measure is
\[
A(\mu)=\int_0^1\frac{d\mu(x)}{16-x}.
\]
For ψ_M above,
\[
\boxed{
\beta_M=\int_a^c\frac{\psi_M(x)}{16-x}dx
=(-1)^M M!\int_a^c\frac{g_M(x)}{(16-x)^{M+1}}dx\ne0.
}\tag{10}
\]
(The M-th derivative of \((16-x)^{-1}\) is \(M!(16-x)^{-M-1}\), positive.) Hence
\[
\boxed{A(f_{\epsilon,M}dx)=\pi/16+\epsilon\beta_M.}\tag{11}
\]
Because \(\beta_M\ne0\), the allowable open ε-interval maps to a nonempty open interval around π/16.

Choose from that interval (i) a RATIONAL q, and (ii) an explicitly known base16 NORMAL number q' (e.g. a base-16 Champernowne constant plus an appropriate rational translation; such translates are dense and normal by the classical base-b normality theorem). Set ε=(q−π/16)/β_M or ε'=(q'−π/16)/β_M. Both positive Hausdorff source measures satisfy (3)–(9) and BOTH have literal U0=0.

Their future tails stay positive and summable because f_ε is between 0.95f and 1.05f:
\[
U_n^{\epsilon}=16^nq-T_n^{\epsilon},
\quad \sum_nT_n^{\epsilon}<\infty.
\]
The **NORMAL** candidate then has \(S_N^{\epsilon'}(h)=o_h(N)\) for every h!=0; the rational-q candidate is **NONNORMAL** and, at the fixed nonzero harmonic h=den(q), satisfies \(S_N^\epsilon(h)=N+O_h(1)\).

This is **unconditional** about the two changed-source controls. No premise about whether the original π is normal is needed. The perturbation ε or ε' may be irrational; original *rational-valued* source metadata is NOT preserved in these specifically normal-versus-rational controls. For rational ε, all modified source values remain rational, and the finite effect is still real, but the completed normality is not classified by this proof.

**Category conclusion:** on the signed vector space of moment measures, the prefix observation q_M has ψ_M dx in its kernel, whereas completion A has A(ψ_Mdx)=β_M≠0. Consequently the linear functional A does **not** factor through q_M. The failure persists if the observer adds every source pole/principal part (the correction is entire), all inverse-power asymptotic coefficients, and positivity/5%-comparison constraints. This is the exact ker(q_A) ⊆ ker(q_B) obstruction from SUCC #423 applied to an original-source neighborhood.

## CE-03. Even an EXACT-RATIONAL and completely monotone source counterfeit exists for EVERY finite M (PROVED PAPER, rational moment convexity)

This is a **separate** stronger arithmetic alternative without a pointwise 95% density guarantee.

Let \(\mu=f(x)dx\) be the authentic positive source measure on [0,1]. For every integer M>=1 there exist finitely many **rational** nodes \(x_i\in(0,1)\) and **strictly positive rational** weights \(w_i\) with
\[
\boxed{\sum_iw_i x_i^{j}=r(j+1),\qquad0\le j<M.}\tag{12}
\]

**Proof of existence with rationality:** Normalize μ by its rational mass \(r(1)=47/15\), and map \(x\mapsto(x,x^2,...,x^{M-1})\). Its moment vector has RATIONAL coordinates. Because f(x)>0 for all x in (0,1), the moment vector lies in the interior of the convex hull of the moment curve: any nonzero supporting affine polynomial nonnegative on [0,1] has strictly positive integral. Rational nodes are dense; the interior point therefore lies in a polytope with RATIONAL moment-curve vertices (take sufficiently close rational approximants to a finite set of enclosing real vertices). A rational point in that rational polytope admits a convex decomposition with RATIONAL nonnegative barycentric weights by elementary rational linear algebra; discard any zero coefficients. Multiply by rational total mass 47/15. For M=1 choose any one rational interior node with weight 47/15.

Set
\[
\boxed{
r_{\mathrm{atom}}(n)=\sum_iw_ix_i^{n-1}\in\mathbb Q_{>0},\
\alpha_{\mathrm{atom}}=\sum_i\frac{w_i}{16-x_i}\in\mathbb Q.
}\tag{13}
\]
For EVERY n>=1,d>=0, \((-1)^d\Delta^d r_{\mathrm{atom}}(n)=\sum_iw_ix_i^{n-1}(1-x_i)^d>0\). The exact first M forcing values and zero-seeded states coincide with authentic BBP. But \(\alpha_{\rm atom}\) is RATIONAL, hence at h=den(\alpha_atom), the new selected orbit has \(S_N(h)=N+O_h(1)\), so is certainly NONNORMAL. Its tail is exponentially summable since max_i x_i<1.

**One fully exact 4-observation certificate:** choose positive rational atomic data
\[
\begin{array}{c|c}
x_i&w_i\\
1/80&93606744115/32218183998\\
5/16&992400341/7594857270\\
1/2&1011071983/11951906967\\
63/80&23100710/1823277183
\end{array}
\]
Then the first FOUR source values and zero-seeded states agree EXACTLY with the original; the completed rational value is
\[
\boxed{\alpha_{\mathrm{atom}}=
4062342947075618/20689342837729335.}\tag{14}
\]
A separate exact SymPy matrix-inverse oracle independently rederived all weights, four moment constraints, positivity and (14). The fifth source value differs, providing the first finite discriminator.

**Important non-identifications:** This rational atomic model does NOT retain the exact four rational poles/meromorphic source class, nor the 95% pointwise-density comparability of CE-01. Finite atomic measures cannot generally satisfy uniform all-(n,d) moment-ratio domination against a strictly positive continuous density. CE-01 and CE-03 are independent hostile controls with different invariants.

## CE-04. Quantified causal horizon and completion aperture (PROVED, finite deterministic)

For any positive finite measures μ,ν with identical first M source moments and total mass R0=r(1), use
\[
\frac1{16-x}=\sum_{j=0}^{M-1}\frac{x^j}{16^{j+1}}
+\frac{x^M}{16^M(16-x)}.
\]
The moments cancel in the difference, giving the exact expression and bound
\[
\boxed{
A(\mu)-A(\nu)=\frac1{16^M}\int_0^1\frac{x^M}{16-x}\,d(\mu-\nu),\
|A(\mu)-A(\nu)|\le\frac{\|\mu-\nu\|_{\rm TV}}{15\cdot16^M}
\le\frac{2R_0}{15\cdot16^M}.
}\tag{15}
\]
For the CE-01 perturbation supported in [1/4,1/2] and already null to order M, improve to
\[
\boxed{|A(\mu_\epsilon)-A(\mu)|\le
\frac{2\|\mu_\epsilon-\mu\|_{\rm TV}}{31\cdot32^M}.}\tag{16}
\]
This is an exact exponential *source-observer completion resolution* law. It agrees in kind with #465's still sharper, ORIGINAL-FOUR-POLE-specific positive Gamma-tail brackets, but does not replace them.

If |\(\delta r(j)|\le\eta r(j)\) for all j, with identical source prefix through M, finite causal Green propagation yields
\[
\boxed{
|\widetilde U_n-U_n|=0\ (n\le M),\quad
|\widetilde U_n-U_n|
\le\eta R_0\,\frac{16^{n-M}-1}{15}\ (n>M).
}\tag{17}
\]
Thus even small source discrepancies can be amplified at late times, while any prescribed finite observation horizon is identical or can be made arbitrarily close. This is an affine response theorem, not a new digit distribution theorem.

**Fully exact finite echo:** CE-01's rational ε=1/(1000 B_4) with M=4 preserves all four authentic values. At n=18 the TRUE versus positive altered source's circle-state distance is EXACTLY
\[
\boxed{
\|U_{18}^{\epsilon}-U_{18}\|_{\mathbb R/\mathbb Z}
=\frac{260840294718179115804391693}
{837084962009298606489600000}
\in(1/4,\,2/5).
}\tag{18}
\]
Separate independent SymPy and Fraction calculations agree, with no π digits or float signs involved. The perturbed forcing values are all rational for this selected rational ε. This proves finite strong causal amplification of an extremely small, all-jet-controlled source echo, NOT asymptotic nonnormality of this particular ε.

## CE-05. Causal/astronomical interferometry and Yoneda observer descend are exact only within their source fiber (PROVED; prior work credited)

The source-to-state finite Green map from SUCC #443/#464 is
\(U_n=\sum_{j=1}^n16^{n-j}r(j)\). For any source in the CE-01/03 fiber, all \(U_n\) through M, and therefore ALL of the following measurements built from those times, are literally identical:
- the source/finite-state causal path, every rational phase \(e(hU_n)\) for every integer h;
- the calibrated causal field \(\Phi_M(s)=\sum_{n\le M}e(hU_n)e(h16^n s)\), its entire nonnegative intensity and every Fourier coefficient;
- cosmic reference measurements / phase stepping / matched-filter scores of #466, for any **fixed source-independent reference**;
- Pascal/Newton finite source jets supported within the first M source values, and their reconstructed original finite history.

Therefore no finite causal observation at that horizon can distinguish the future NORMAL versus NONNORMAL modified-source continuations in CE-02; in the rational CE-03 class no such observation can rule out an eventual coherent rational-completed path.

This is the *mathematical* equivalent of an unresolved astrophysical reverberation-map inverse problem: different source histories have identical finite-response data under a declared response operator. It is NOT an assertion that the real CMB is a SUCC foreground, nor evidence that an actual observer chooses a quantum collapse.

**Important restoration:** Prior SUCC #437/#448/#421 already proves finite source authentication in a much NARROWER four-simple-pole rational class via Prony/Hankel/source rigidity. CE-01 adds an entire correction; CE-03 replaces the rational poles with exponential atoms. Both EXIT that restricted class. When the exact global four-pole model is independently established and literal U0=0 is retained, the entire causal path is uniquely specified. Source identifiability then is no longer the obstruction; the selected signed Fourier saving remains.

## CE-05B. General finite-observer *weight-span theorem*: the exact lamp for categorical descent (PROVED, classical functional linear algebra)

The preceding witness is not special to observing the first M raw moments. It extends to **any finite list of genuine LINEAR source observations**. Work with signed finite Borel measures on the closed compact interval \(I=[a,c]\subset(0,1)\), or with smooth density perturbations supported inside I. Let
\[
L_i(\nu)=\int_I\phi_i(x)\,d\nu(x),\qquad i=1,\dots,k,
\quad A_I(\nu)=\int_I K(x)\,d\nu(x),\quad K(x)=\frac1{16-x},
\tag{19}
\]
where each specified real observer weight \(\phi_i\) is continuous on I. Reduce to a linearly independent list of observer weights. Then the following are EQUIVALENT:

1. \(A_I\) factors through the combined finite linear observation \(L=(L_1,\ldots,L_k)\) on **all signed measures** supported in I.
2. \(\ker L\subseteq\ker A_I\).
3. \(K\in\operatorname{span}_{\mathbb R}\{\phi_1,\ldots,\phi_k\}\) as a continuous function on I.

Proof: 3→1 is direct, with A_I a fixed linear combination of the L_i. 1→2 is the #423 quotient criterion. If 3 fails, the continuous functions \((\phi_1,\ldots,\phi_k,K)\) are independent, hence there exist k+1 distinct interior evaluation nodes x_j for which their evaluation matrix is invertible. Choose k+1 disjoint nonnegative C_c^∞ bumps β_j narrowly concentrated at those nodes, each with integral 1. The matrix \(B_{ij}=\int\phi_i\beta_j\), extended with final row \(\int K\beta_j\), tends to the invertible evaluation matrix, so it is itself invertible for sufficiently narrow bumps. Solve \(Bc=(0,\ldots,0,1)^{\top}\) and put \(\psi=\sum c_j\beta_j\). This **constructs** a smooth compactly supported signed density with
\[
\boxed{L_i(\psi dx)=0\ \forall i,\qquad A_I(\psi dx)=1.}\tag{20}
\]
Thus ker inclusion fails, refuting 2. This also establishes the contrapositive 2→3.

Because the authentic BBP source density f has a positive lower bound on I, \(f+\epsilon\psi\) is strictly positive and between (1−η)f and (1+η)f for ANY predeclared η>0 when |\epsilon| is sufficiently small. It therefore retains ALL source unit/analytic mixed Hausdorff moment positivity and multiplicative proximity bounds, exactly as CE-01. Moreover \(\delta r(z)=\epsilon\int_Ix^{z-1}\psi(x)dx\) is entire and exponentially small at positive integer z, preserving every original meromorphic pole and inverse-power asymptotic coefficient. Completion changes by exactly ε; by density of rational and base-16-normal constants, arbitrarily nearby changed-source normal and nonnormal completions exist, with identical finite specified L_i observations.

**Applications and limits:** finite Pascal/Newton source moments have polynomial weights, and finite analytic source-time derivatives have weights \(x^{z}(\log x)^a(1-x)^d\) on I. Any FINITE collection of those weights is analytic away from x=0 and lacks the pole at x=16, hence cannot express \(K(x)=1/(16-x)\) on an open I; the real-analytic identity theorem would extend such an equality toward 16 and contradict the pole. Therefore **no finite bundle of those pure source-jet observations** determines the complete boundary on the full Hausdorff source class. This statement is restricted to these explicitly linear source observables: it does NOT automatically apply to nonlinear observables such as log Γ, conditional Bayesian likelihoods or an arbitrary real-circle interference intensity. For the specific nonlinear finite causal intensity in #466, prefix equality of all U_n directly establishes equality separately (CE-05).

This is a mathematical diagnosis of the observer \(\sigma\)/source-map and \(\phi\)/pathway gap, NOT a theorem forbidding finite mathematical PROOFS that exploit a known global four-pole formula. On the restricted at-most-four-pole rational model class, the admissible perturbations ψ are excluded and previous Prony source identification may restore the arrow. Normality remains another, genuinely signed and all-horizon proposition.

## CE-05C. The circle/line relative-period defect: absolutely exact is NOT endpoint-relative exact (PROVED)

SUCC #452's original BBP angular decomposition is precise about its **endpoint-vanishing coboundary**, which preserves the completed source's relative period. Our causal echo produces the complementary boundary-sensitive case.

The completed source in the positive Hausdorff x-coordinate has one-form \(\omega=f(x)/(16-x)\,dx\). Its CE-01 perturbation is
\[
\boxed{
\delta\omega_\epsilon=
\frac{\epsilon\psi_M(x)}{16-x}dx=dF_\epsilon(x),\qquad
F_\epsilon(x)=\epsilon\int_0^x\frac{\psi_M(t)}{16-t}dt.
}\tag{21}
\]
This is an **ordinary exact one-form** on [0,1], with primitive zero on the left endpoint. But
\[
\boxed{
F_\epsilon(0)=0,\qquad F_\epsilon(1)=\epsilon\beta_M\ne0,\qquad
\int_0^1\delta\omega_\epsilon=\epsilon\beta_M.
}\tag{22}
\]
It is therefore NOT exact in the **relative** de Rham complex with primitives vanishing on BOTH boundary endpoints. Its relative cohomology class in \(H^1([0,1],\{0,1\};\mathbb R)\cong\mathbb R\) is nonzero and detected by the endpoint period.

Thus a completely local-looking, pole-invisible source correction can shift the global circumference/diameter-type period **without** contradicting #452 AC-13: that earlier original-source coboundary was independently shown to vanish at BOTH endpoints and hence did NOT alter the period. Our perturbation deliberately changes the full source; it is not a second derivation or modification of π, nor curvature of a 1D circle.

This is the geometric transport of the same categorical observation-gap theorem CE-05B: retaining only local differential/pole data does not certify the boundary class. The appropriate extra datum is an endpoint-relative period passport (or the complete global rational four-pole source law). **Neither passport proves digit-normality; it only fixes WHICH completed constant the signed Fourier orbit concerns.**

## CE-06. The precise next original-source π-normality probe (UNVERIFIED)

This dossier does NOT establish a new original-source \(o(N)\) Weyl bound, any all-prime cofactor cancellation, or RH. It proves a source-map separation and finite-time instrument limitations.

The proof-producing next step is not another generic positive Hausdorff moment statistic: CE-02 shows that ALL such statistics, even to uniform 5% precision and with any finite prefix, allow a normal-versus-coherent source ambiguity. It must instead use the FULL exact four-pole source as a rigid analytic input, the selected zero boundary, the signed real phase, and the joint p-primary/p-free cofactor in #459/#460.

A concrete proposed discriminating experiment: combine #437/#448 finite Prony source fingerprint, #465 original-source Gamma-tail certified phase intervals, #466 calibrated reference cross-intensity and the #460 exact prime birth windows; prove a new quantitative weighted source-cofactor inequality for unbounded p. The experiment must REJECT both the CE-03 positive rational quadrature and the CE-02 smooth entire-shadow controls, plus the same-exact-four-pole altered irrational seed \(-\pi/16\). Merely rephrasing \(|S_N|=o(N)\) as a matched intensity limit is equivalence, not a proof.

### Classical and internal provenance

- SUCC #440: original positive Hausdorff BBP moment source and all Newton/Pascal unit differences; #463: coherent positive full tower and differential; #421: all-order entire-source shadow and fixed-prefix countermodels; #437: original four-pole Prony and source/phase Fourier nonconspiracy; #448: seven-sample four-pole rigidity; #423: criterion for factoring observational quotient arrows; #443/#464: exact causal Green/path selection; #465: authentic Gamma source-tail interval; #466: cosmic calibrated cross-intensity.
- Curto–Fialkow, *A Duality Proof of Tchakaloff's Theorem* (2002), https://arxiv.org/abs/math/0207065 : classical positive atomic quadrature, here refined with rational moment coordinates and rational nodes by an explicit convex interior argument.
- Peterson–Horne, *Reverberation Mapping of Active Galactic Nuclei*, NASA/IPAC NED https://ned.ipac.caltech.edu/level5/March10/Peterson/paper.pdf : line-of-sight velocity/delay response as a causal Green inverse problem; methodological analogy ONLY.
- Planck Collaboration, *2018 results IV: Diffuse component separation*, A&A (2020), https://doi.org/10.1051/0004-6361/201833881 : explicit source/foreground model comparisons, methodological analogy ONLY.
