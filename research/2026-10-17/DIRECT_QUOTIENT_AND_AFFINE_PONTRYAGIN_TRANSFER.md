# Operation DQ × APT: projector-first Suzuki Schur and affine Pontryagin transfer

**2026-10-17. Branch-only research; parent main 610efacf02556e1c5922bc5d4e87d0087f19b446.**

This dossier records two independent mathematical instruments. One is a new source-conditional *first-window* Suzuki/Weil lower enclosure; the other is an exact realization of the classical arithmetic Bost–Connes root-average. **RH OPEN. No zero coordinates, fake prime-power inputs, physical source-authentication claims, C*-completion, or global Weil sign claims.**

## A. Projector-first differentiated-convolution Gram

Let \(I=(-a,a)\) and \(Q=1-\Pi_{\mathcal P_{\le3}}\) in \(L^2(I)\). If \(f_i=(Gv_i)'\) are source-response derivatives, the already-established PDQ dual identity identifies their full high-sector \(K\)-dual energy with

\[
T_{\rm quot}=[\langle Qf_i,Qf_j\rangle]_{i,j=1}^4.
\]

An earlier certified route bounded \(\langle f_i,f_j\rangle\) and separately subtracted polynomial moments. This does not exploit cancellations within the same computed source packet. We propose an exact projection *before* interval error propagation.

**DQ-01 (PROVED CONDITIONAL).** Partition \(I\) into equal cells \(C_k\) of width \(h\), midpoint \(c_k\). Assume \(f_{J,i}(c_k)\) lies in a rational interval of midpoint \(m_{ki}\) and radius \(r_{ki}\). Assume a *proved, global* Lipschitz bound \(L_i\) on \(f_{J,i}\), a source-derived omitted-tail norm \(\|f_i-f_{J,i}\|_2\le t_i\), and parity \(f_i(-x)=(-1)^{i-1}f_i(x)\). Let \(s_i(x)=m_{ki}\) on \(C_k\). Then

\[
b_i=\sum_k\left(h r_{ki}^2+\tfrac12h^2r_{ki}L_i+
                       \tfrac1{12}h^3L_i^2\right),\qquad
\epsilon_i=\sqrt{b_i}+t_i
\]

bounds \(\|f_i-s_i\|_2\). For parity blocks \(\{1,3\}\), \(\{2,4\}\), define the diagonal error matrix

\[
D_{ii}=\epsilon_i\sum_{j\text{ in same parity block}}\epsilon_j.
\]

Then for every \(\eta>0\),

\[
\boxed{0\preceq T_{\rm quot}\preceq
 (1+\eta)T_{\rm step}^{*}QT_{\rm step}+
 (1+\eta^{-1})D.}
\]

**Proof:** The cellwise estimate \(|f_{J,i}(x)-m_{ki}|\le r_{ki}+L_i|x-c_k|\) integrates to the displayed \(b_i\). Projection \(Q\) is a contraction in \(L^2\), with no differentiation of \(Qh\). In each parity block Cauchy–Schwarz gives \((\sum_i \epsilon_i|x_i|)^2\le(\sum_i\epsilon_i)(\sum_i\epsilon_i x_i^2)\); opposite parities remain orthogonal. Apply weighted Young to \(QT_{\rm step}+Q(f-T_{\rm step})\). The step Gram is **exactly** \(S^*S-M^*P^{-1}M\), with rational cell integrals; only *after* this subtraction is the error added. All Loewner orders are valid. A large constant added to a step column cancels exactly in \(QT_{\rm step}\); this is tested with \(10^{12}\), not inferred from an unstable numerical difference.

**Original-source adapter (IMPLEMENTED; exact-head CI required).** The new source wrapper calls inherited pinned \(\operatorname{CertifiedTrial}\), true \(p=2\) wavefront, \(\operatorname{authentic\_suzuki\_mode\_derivative\_point}\), source BV/Lipschitz bound, and the previously justified \(O(J^{-3/2})\) Gamma derivative-tail lemma. With inherited \(D_{4,\rm odd}\succeq(63/500)K_{\rm odd}\) and \(D_{4,\rm even}\succeq(153/500)K_{\rm even}\), it subtracts the corresponding parity-scaled certified upper quotient from the original \(U\)-dependent trial-energy lower bound \(M_U\). The output can only be POSITIVE_CERTIFIED if the **original-source rational four-by-four lower** is PSD. Otherwise the tool says AMBIGUOUS; a negative lower *does not* refute positivity. This first-window trial alone cannot prove RH.

**Adversarial residual witness:** For \(h=P_5(2t)-P_7(2t)\) on \((-1/2,1/2)\), direct exact integration gives \(h(\pm1/2)=0\), four vanishing derivative polynomial moments, \(h\perp\{P_1,\ldots,P_4\}\), but \(\|h'\|_2^2=52\). Thus endpoint and polynomial measurements do not determine the general Sobolev residual. This is *not* claimed to lie in the true range \(h=Gv\); source restrictions are load-bearing.

## B. Operator-valued Schur comparison instead of a scalar \(\kappa\)

**DQ-02 (PROVED FINITE; SOURCE-TRANSFER CONDITIONAL).** In an exact real finite block
\[
G=\begin{pmatrix}A&B^*\\B&D\end{pmatrix}
\]
assume \(D\succeq C\succ0\), where \(C\) can be a matrix-valued comparison rather than \(\kappa K\). For an arbitrary high response \(U\), set \(L_U=U^*B+B^*U-U^*DU\) and \(r_U=B-DU\). Then completing the square and using inversion order yields
\[
\boxed{ A-L_U-r_U^*C^{-1}r_U
\preceq A-B^*D^{-1}B\preceq A-L_U.}
\]
The module uses exact Fraction inversion and all-principal-minor PSD tests, and rejects a comparator for which \(D-C\) fails PSD. **The finite matrices are not the genuine infinite Suzuki operator.**

**DQ-03 (PROVED FINITE).** For \(K\succ0,\kappa>0,\delta\ge0\), and \(z\),
\[
C=\kappa K+\delta zz^*,\quad
(\kappa K)^{-1}-C^{-1}
=\frac{\delta}{\kappa(\kappa+\delta z^*K^{-1}z)}
K^{-1}zz^*K^{-1}\succeq0.
\]
This is an explicit *direction-dependent* reduction in residual energy. The honest unsolved gate is a source- and domain-certified infinite quadratic-form inequality \(D_4\succeq C\); a finite PSD matrix or generic Hilbert covariance is not sufficient.

## C. SUCC–FUCC–Pontryagin → classical Bost–Connes

**TR-01 (CLASSICAL, EXACT MODEL).** On the finite-support rational group ring \(\mathbb Q[\mathbb Q/\mathbb Z]\) write \(e(r)e(s)=e(r+s)\). Define \(\sigma_n e(r)=e(nr)\) and

\[
\rho_n e(r)=\frac1n\sum_{ns=r\ ({\rm mod}\ 1)} e(s).
\]

Precisely \(n\) roots exist; finite preimage counting proves
\[
\rho_m\rho_n=\rho_{mn},\quad\sigma_m\sigma_n=\sigma_{mn},\quad
\rho_n(fg)=\rho_n(f)\rho_n(g),\quad
\sigma_n\rho_n=\mathrm{id},\quad
\rho_n\sigma_n(f)=e_nf,\quad e_n=\rho_n(1),\quad e_n^2=e_n\ne1\ (n>1).
\]

The normalized **additive Haar** functional \(\tau(e(r))=\mathbf1_{r=0}\) satisfies
\[
\boxed{\tau(\rho_n(f)g)=\tfrac1n\tau(f\sigma_n(g)),\qquad\tau(e_n)=1/n.}
\]
On Fourier dual \(\widehat{\mathbb Z}\), \(e_n\) is exactly the indicator of \(n\widehat{\mathbb Z}\). This gives a precise nonunital partial backward transport, **not** a magical inverse original source event.

**TR-02 (CLASSICAL AFFINE, NEW SOURCE-INDEXED INSTANTIATION).** Chronological SUCC \(S(x)=x+1\) and genuine prime FUCC \(V_p(x)=px\) generate maps \(x\mapsto ax+b\). The exact character pullback is \(\chi_r(ax+b)=e^{2\pi i br}\chi_{ar}(x)\), with the phase kept as a rational class modulo \(1\). The distinct words \((S,V_p)\) and \((V_p,S,\ldots,S)\) with \(p\) successor steps both give \((a,b)=(p,p)\). Event count differs (\(2\) versus \(p+1\)). By the coimage factorization criterion, event count cannot be decoded from their shared affine endpoint representation. Mathematical action equivalence is not source-history faithfulness.

**Mutation firewall:** A composite root average \(\rho_6\) is valid as a semigroup operation; a letter \(V_6\) cannot masquerade as a *prime* FUCC generator. Wrong-source/epoch compositions, bool/float exactness forgeries, missing \(1/n\) factor, treating \(\rho_n\) as unital, and confusing exponent phase sign are separate hostile controls. No C*-completion, KMS-state classification, gamma factor, completed signed Weil identity or RH positivity is imported from Bost–Connes.

**Primary mathematical source:** J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Math. 1 (1995), 411–457, DOI 10.1007/BF01589495; IHES M/95/38. SUCC parents: the Pontryagin finite-adèles atlas, finite affine presentation, original signed Suzuki source, and YEAN coimage handoff.

## D. Claim ledger and next discriminators

| Claim | Status | Test / dependency |
|---|---|---|
| DQ-01 projector-first interval inequality | PROVED CONDITIONAL; EXACT MODEL | Needs source-certified midpoint/Lipschitz and omitted Gamma tails |
| DQ-02 arbitrary matrix coercive comparison | PROVED FINITE | Exact Schur enclosure, wrong-comparator rejection |
| DQ-03 rank-one Woodbury saving | PROVED FINITE | Rational PSD identity; genuine source comparison OPEN |
| TR-01 classical nonunital transfer and Haar identity | CLASSICAL; EXACT FINITE TESTED | Root counting, \(\rho_2\rho_3\), source mismatch, nonunital test |
| TR-02 affine dual transport/history obstruction | CLASSICAL ACTION + NEW-TO-PROJECT SOURCE TEST | Exact word-normalization collision and phase naturality |
| Genuine \(S_4\succeq0\) at \(a=1/2\) | **UNVERIFIED / OPEN** | Source adapter's exact lower must clear |
| Weil full support/RH | **UNVERIFIED / OPEN** | No all-radius positive factorization |

**Highest-value next discriminator:** Evaluate the *authentic* first-window direct-quotient trial on source-valid \(U,J,\mathrm{grid},\eta\) and report exactly which error term dominates, with the inherited independently certified \(H'-E^*P^{-1}E\) result as a hostile baseline. If the lower is indefinite, do not increase precision blindly: seek source-derived spectral/anisotropic \(C\) and a sound \(D_4\succeq C\) proof. Independently lift the arithmetic transfer to the appropriate Hecke/C*-completion with external reference matching, while guarding event-history loss and the absence of any positivity transport to completed Weil.

**RH PROVED: NO.**
