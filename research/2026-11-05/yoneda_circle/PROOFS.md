# Operation OBSERVATIONAL YONEDA × HEX-CELL PAULI PRESSURE — source-faithful theorems

**Research-only, 2026-11-05.** Strict add-only child of SUCC #514 at pinned SHA \`4243b6c5dda90d49969c62f99b3f3aae73300ebe\`. Original signed four-pole rational forcing, literal U0=0, complete carries, formal/historical source and proof contracts, production/workflows/main unchanged. This is classical category theory, harmonic analysis, probability measures and arithmetic dynamics applied to SUCC's source. **No base-16 normality of π, physical quantum field, novel priority, or unproved statistical claim is asserted.**

## 0. The corrected logical object: SOURCE hypothesis ≠ NORMALITY hypothesis

An observational/Yoneda account must keep these different typed obligations:
1. **Hypothesis/source contract:** \(r_o(n)=4/(8n-7)-2/(8n-4)-1/(8n-3)-1/(8n-2)\), exactly the authentic four-pole BBP rational function. The standard BBP series identity verifies \(\sum_{n\ge1}16^{-n}r_o(n)=\alpha=\pi/16\). This is already known, not a normality premise.
2. **Pointing:** \(U_0=0\), and the exact unwrapped rational recurrence \(U_{n+1}=16U_n+r_o(n+1)\).
3. **Representation:** the hidden common-unit paired fiber and its source-compatible circle character observations.
4. **Distribution target:** the empirical measures of the single selected orbit converge to Haar (Weyl equidistribution). This remains UNKNOWN.

The classical Yoneda embedding is fully faithful for **all lawful morphism probes in a specified category**. A finite or restricted observer family need not be fully faithful (as already demonstrated by on-main \`observational_succ/yoneda.py\` / \`operational_yoneda_descent.py\`). Classical Yoneda does NOT assert that a represented circle orbit samples Haar. Below we distinguish categorical source-state reconstruction from measure reconstruction by a declared natural family of hexadecimal-cell probes.

## YO-01. The coupled unit pair is exactly isomorphic to the source real-line diagram AFTER fixing its common mode

For each \(n\ge0\) define the *affine common-mode fiber*
\[
\mathsf P_n:=\{(a,b)\in\mathbb R^2:\ a+b=2\cdot16^n\},
\quad \delta_n(a,b)=a-b,
\quad \sigma_n(x)=(16^n+x/2,\ 16^n-x/2).
\]
Thus \(\delta_n\circ\sigma_n=\mathrm{id}_\mathbb R\) and \(\sigma_n\circ\delta_n=\mathrm{id}_{\mathsf P_n}\). Define source arrows
\[
F_{n+1}(a,b)=\left(16a+\frac12r_o(n+1),\
                       16b-\frac12r_o(n+1)\right),
\qquad
R_{n+1}(x)=16x+r_o(n+1).
\]
The fiber law and both commuting source diagrams hold EXACTLY:
\[
\boxed{\delta_{n+1} F_{n+1}=R_{n+1}\delta_n,\qquad
       F_{n+1}\sigma_n=\sigma_{n+1}R_{n+1}.}\tag{YO1}
\]
These are genuine isomorphisms of the declared **time-indexed source diagrams**; the hidden pair is not inferred from an arbitrary unconstrained pair or an unspecified vacuum. The literal source-start is \(P_0=(1,1)\), \(\delta_0(P_0)=0\). The underlying \(\delta\) on unconstrained pairs has diagonal kernel, so fixing the common-mode law is indispensable.

Circle projection \(q:\mathbb R\to\mathbb T=\mathbb R/\mathbb Z\) commutes with the integer ×16 source dynamics. The observers \(\mathcal O_{h,n}(P)=e(h\delta_n(P))\), \(h\in\mathbb Z\), satisfy
\[
\boxed{\mathcal O_{h,n+1}(F_{n+1}P)
=\mathcal O_{h,n}(P)^{16}e(h r_o(n+1)).}\tag{YO2}
\]
All characters together reconstruct **the circle phase**, and h=1 already separates points on the circle. They do NOT recover the integer lift or literal carries of \(\delta_n(P)\), nor an arbitrary common-mode amplitude. The full source and carry observables must therefore be retained before claiming faithfulness of a larger hidden-state model. This is a Pontryagin-character instance of source-labelled observational reconstruction, not a formal identification of circle characters with a full Yoneda hom-functor.

## YO-02. The source enforces QUANTITATIVE approximate circle invariance, but cannot choose the invariant measure

The authentic rational forcing simplifies identically to
\[
r_o(n)=\frac{120n^2-89n+16}
{(2n-1)(4n-1)(8n-7)(8n-3)}>0.
\]
At n=1 it equals \(47/15\). For every n≥2,
\[
(2n-1)(4n-1)(8n-7)(8n-3)
\ge\frac{2457}{16}n^4,
\quad 120n^2-89n+16\le120n^2,
\]
so
\[
0<r_o(n)\le\frac{1920}{2457n^2},\qquad
\boxed{\sum_{n\ge1}r_o(n)
<\frac{47}{15}+\frac{1920}{2457}<4.}\tag{YO3}
\]

For ANY initial real seed s, define \(x_n(s)=q(U_n(s))\) and its initial-prefix empirical measure
\(\mu_N^s=N^{-1}\sum_{n=0}^{N-1}\delta_{x_n(s)}\). Let \(T(x)=16x\bmod1\), and f be complex-valued Lipschitz on the circle with geodesic Lipschitz constant L. The source recurrence, telescoping endpoints, and geodesic distance bound give
\[
\boxed{
|\mu_N^s(f)-\mu_N^s(f\circ T)|
\le\frac{2\|f\|_\infty+L\sum_{n=1}^N r_o(n)}N
<\frac{2\|f\|_\infty+4L}{N}.}\tag{YO4}
\]
This is a finite all-N, source-authentic error estimate. By compactness of probability measures on \(\mathbb T\), every subsequential weak-* limit \(\mu\) exists after extraction; taking limits for Lipschitz f and density in C(T) implies \(T_*\mu=\mu\).

**Sharp nonselection:** \(T\) is NOT uniquely ergodic. Its invariant probabilities include Haar \(\lambda\), Dirac \(\delta_0\), Dirac \(\delta_{1/15}\), and biased base-16 Bernoulli digit measures. Source compatibility/reconstruction can force the invariant-measure simplex but cannot force the Haar vertex. The same-source coherent wrong seed \(s_*=-\pi/16\) is asymptotic to phase0 and has limiting invariant measure \(\delta_0\).

## YO-03. Hexadecimal cell occupancy is a measure-complete "Pauli exclusion" PROBE

Partition the circle into \(M=16^m\) half-open hexadecimal cells \(I_{m,k}=[k/M,(k+1)/M)\) modulo1, m≥1, k=0,...,M-1. For any Borel probability µ set \(p_{m,k}=\mu(I_{m,k})\) and
\[
\boxed{\mathcal P_m(\mu):=M\sum_{k=0}^{M-1}p_{m,k}^2
=M\sum_k\mu(I_{m,k})^2\ge1.}\tag{YO5}
\]
This is an exact same-cell PAIR occupancy, not a physical fermionic energy. For the empirical µ_N write \(\mathcal P_{N,m}\). Refinement of one parent into 16 children and finite Cauchy–Schwarz prove
\[
\boxed{\mathcal P_{m+1}(\mu)\ge\mathcal P_m(\mu)\ge1.}\tag{YO6}
\]
Define the piecewise-constant *histogram density* \(f_m(x)=M p_{m,k}\) on the kth cell. Then
\[
\|f_m\|_{L^2(\lambda)}^2=\mathcal P_m(\mu),\quad
f_m=\mathbb E_{\lambda}[f_{m+1}\mid\mathcal F_m],
\]
and for every continuous test function \(\varphi\),
\(\int\varphi f_m\,d\lambda\to\int\varphi\,d\mu\)
because each cell diameter tends to zero.

**Exact measure-completeness theorem** (standard dyadic/radix martingale and L² duality):
\[
\boxed{
\sup_{m\ge1}\mathcal P_m(\mu)<\infty
\iff
\mu=f\,\lambda,\ f\in L^2(\lambda).
}\tag{YO7}
\]
Proof: if the left is finite, the histogram densities are uniformly bounded in L²; extract a weakly convergent L² subsequence \(f_{m_j}\rightharpoonup f\). Their continuous-test integrals converge to µ, so µ=fλ. Conversely for \(\mu=f\lambda\), \(f_m=\mathbb E[f|\mathcal F_m]\) and \(\|f_m\|_2≤\|f\|_2\); refinement and martingale convergence give \(\lim_m\mathcal P_m=\|f\|_2^2\). If \(\mu\) has a singular component OR an L¹ density not in L², monotonicity and contrapositive force \(\mathcal P_m\to\infty\).

**Invariant-measure dichotomy:** If \(T_*\mu=\mu\) AND \(\mu=f\lambda,\ f\in L^1\), then for every nonzero integer h,
\(\widehat\mu(h)=\widehat\mu(16h)=\widehat\mu(16^j h)\to0\)
as j→∞ by the classical Riemann–Lebesgue lemma. Fourier uniqueness forces \(\mu=\lambda\). Therefore
\[
\boxed{
T_*\mu=\mu\quad\Longrightarrow\quad
\left[
\mu=\lambda,\ \mathcal P_m(\mu)\equiv1
\right]
\quad\text{OR}\quad
\left[
\mu\ne\lambda,\ \mathcal P_m(\mu)\uparrow\infty
\right].
}\tag{YO8}
\]
The dichotomy holds at the level of *probability measures*, NOT for any finite sample under m→∞.

## YO-04. A SOURCE-SPECIFIC NORMALITY SUFFICIENCY THEOREM: bounded pressure at every fixed resolution

Let \(\mu_N=\mu_N^{s=0}\) be the original authentic zero-seeded empirical BBP orbit. Suppose there exists an absolute finite constant C such that
\[
\boxed{
\forall m\ge1:\qquad
\limsup_{N\to\infty}
\left(16^m\sum_{k=0}^{16^m-1}\mu_N(I_{m,k})^2\right)
\le C.
}\tag{YO9, OPEN PREMISE}
\]
Then every weak subsequential limit µ is L². To handle interval-boundary ambiguity, for continuous \(\varphi\) approximate it by cell constants \(\varphi_m\), taking one value per cell. Uniform continuity gives
\(|\mu_N(\varphi)-\mu_N(\varphi_m)|≤\omega_\varphi(16^{-m})\).
Cauchy–Schwarz gives
\[
|\mu_N(\varphi_m)|
\le\mathcal P_{N,m}^{1/2}
  \left(16^{-m}\sum_{k}|\varphi_{m,k}|^2\right)^{1/2}.
\]
Along any weakly convergent subsequence N_j, let N_j→∞ for fixed m, then m→∞. The premise implies
\[
|\mu(\varphi)|≤\sqrt C\,\|\varphi\|_{L^2(\lambda)}.
\]
By L² duality \(\mu=f\lambda\), \(\|f\|_2≤\sqrt C\). By YO4 µ is T-invariant, so YO8 forces \(\mu=\lambda\). Every subsequential empirical limit is Haar, hence the entire sequence \(\mu_N\to\lambda\).

Finally the original completed source satisfies
\[
U_n(0)=16^n\alpha-T_n,\qquad
\alpha=\sum_{k\ge1}16^{-k}r_o(k)=\pi/16,\quad
T_n=\sum_{j\ge1}16^{-j}r_o(n+j)\to0.
\]
Thus \(\mu_N\to\lambda\) is equivalent by uniform continuity to equidistribution of \(\{16^n\alpha\}\), hence to base-16 normality of π (a finite radix shift of \(\pi/16\)). Therefore
\[
\boxed{\text{YO9 for authentic zero-seeded BBP}\Longrightarrow
\pi\text{ is normal in base 16}.}\tag{YO10, CONDITIONAL}
\]

**This is a weaker KIND of arithmetic input than #513's global Fekete determinant lower bound:** no log singularity, no requirement for near-maximal determinant, no problem with sparse duplicated orbit points, and C may be any finite number (not 1). However given YO4, YO9 and normality are logically equivalent as limit assertions. We have REFORMULATED the missing selected-source obligation into a potentially more tractable UNSIGNED all-radix-cell upper pressure bound; no such bound has been proved here.

Equivalent observer statement, with the LIMIT ORDER DECLARED:
\[
\boxed{
\lim_{m\to\infty}\limsup_{N\to\infty}\mathcal P_{N,m}
=\begin{cases}1,&\text{original orbit is normal},\\+\infty,&\text{original orbit is nonnormal},\end{cases}
}\tag{YO11}
\]
because m↦limsup_N P_N,m is nondecreasing by YO6. The reversed order \(\lim_N\lim_m P_{N,m}\) diverges even for perfectly normal *sample trajectories*: any finite empirical measure is atomic and its histograms' L² norm diverges when m→∞. This is a real finite/infinite observer-scale noncommutation, not quantum energy.

**Natural pair-count version:** \(\mathcal P_{N,m}=(16^m/N^2)\#\{(i,j)<N:\lfloor16^m x_i\rfloor=\lfloor16^m x_j\rfloor\}\), including diagonal. It is a direct, signed-free source-selected pair-count task on the natural 16-adic observation partitions.

## YO-05. Source-faithful nearby NONNORMAL completions: finite observer probes cannot confer typicality

Let \(\alpha=\pi/16\) be defined via the authenticated original BBP series, and for each p≥1 put \(q_p=16^p-1\). Choose integer \(k_p\) nearest to \(q_p\alpha\), and set
\[
\beta_p=k_p/q_p,\qquad s_p=\beta_p-\alpha,\qquad
|s_p|\le[2(16^p-1)]^{-1}\longrightarrow0.
\]
This construction does **not** require π digits; it uses the already authenticated analytic value of the original four-pole series. Given any finite observation horizon K and tolerance ε>0, choose p large so \(|s_p|16^K<\varepsilon\). The exact same-four-pole source trajectories satisfy
\[
\boxed{|U_n(s_p)-U_n(0)|=16^n|s_p|<\varepsilon
\quad\forall 0\le n\le K.}\tag{YO12}
\]
Any predeclared finite set of continuous observer probes and finite time labels is therefore unable to robustly distinguish these seed completions at positive precision.

Yet \(U_n(s_p)=16^n\beta_p-T_n\), and \(16^{n+p}\beta_p-16^n\beta_p\in\mathbb Z\) EXACTLY. Since \(T_n\to0\), the empirical measure of \(\{U_n(s_p)\}\) converges to a finite periodic-orbit probability and is NOT Haar. They are truly altered seeds (since π is irrational), retain the complete original forcing and radial source, and can lie arbitrarily close to the selected source-zero seed. The literal exact U0=0 AUTHENTICATES the target; no finite approximate Yoneda probe certifies its infinite typicality.

A sharper Fekete falsifier follows. For any epoch A with A sampled source points, grouping indices modulo the period p gives \(D_A=A^2/p+O_p(A)\) **ordered** within-class distinct pairs. For such pairs,
\(\|U_i(s_p)-U_j(s_p)\|_{\mathbb T}\le T_A=O(A^{-2})\).
The remaining chords are at most 2. Hence the normalized log determinant of the same-forcing periodic completion obeys
\[
\boxed{\mathcal E_A(s_p)\le-(2/p)\log A+O_p(1)\to-\infty.}\tag{YO13}
\]
This is an exact all-A theorem using the source tail bound, not a finite plot. It shows that even very nearby source-compatible hypotheses can violate the proposed #513 logarithmic exclusion criterion drastically.

## YO-06. What the observer must genuinely prove next

A source-labelled natural isomorphism between paired fibers and circle **states** proves lawful structure and reconstruction. To identify the empirical source trajectory with Haar **as a measure**, one needs a quantitative observer-family inequality such as YO9 (all fixed hexadecimal cell pressures), #513's Fekete energy, or original signed fixed-h Weyl decay. Hypothesizing a circle or even π's normality does not prove any of these.

The #515 odd-cyclotomic deck injectivity and #516 source-coded sphere maps are additional geometry/provenance probes (read-only siblings); they do not supply YO9 since injective transport can carry concentrated non-Haar measures. The source must constrain the actual centered numerator/carries and time-resolved visit counts. A concrete next task is to derive **one source-specific constant C UNIFORM over hexadecimal depth m** in
\(\limsup_{N\to\infty}16^m\sum_k p_{N,m,k}^2\le C\).
Finite bounds with constants C_m growing in m, or #501's ultra-microscopic shrinking-scale pair estimates alone, do not satisfy this gate.

**Claim status:** YO1–YO8 and YO12–YO13 are paper derivations with scoped hypotheses; YO9 is explicitly UNVERIFIED; YO10/YO11 are conditional equivalences. Existing classical Yoneda, Riemann–Lebesgue, weak-* compactness and L² martingale facts are prior art. No global academic novelty certification, no physical quantum result, no original signed Weyl theorem, no π normality or RH proof.
