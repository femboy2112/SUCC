# OPERATION FOUR-SOURCE SCHUR: completed arithmetic center residual Gram and full signed S₄ enclosure

**Date:** 2026-10-17. **Research branch:** \`research/full-four-prime-residual-schur-2026-10-17\`, child of SOURCE-EDGE PR #161 at \`eb62620300add80f8b38ebf0f7cd54c2a3c5ae36\`. **Independently imported exact blobs** from analytic-Suzuki PR #155 at \`1a84799575ca38a33ed552cf94a0850b5632525e\`, without changing the original source or main. The signed Weil/Suzuki source is frozen at Git blob \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\`. **Original S₄ SIGN OPEN; RH PROVED: NO.**

## 1. Scope and correct source domains (FS-01)

On \(I=(-1/2,1/2)\), let \(H=L^2_0(I)\), \(u_k=P_k(2x)\), \(F_4=\operatorname{span}\{u_1,\ldots,u_4\}\), \(Q_4=I-P_{F_4}\), \(K=V^*V\) with \(Vw(x)=\int_{-1/2}^x w(t)\,dt\). The **unmodified original source** is \(G\), including prime2, one completed real Gamma, contact, and BOTH signed poles. The four low-to-high source residuals are
\[
r_k=Q_4G u_k,\quad
g_k=-Q_{\mathcal P_{\le3}}(G u_k)'\in E:=\mathcal P_{\le3}^{\perp}\subset L^2(I).
\]
The source dual identity identifies \(r_k\) on the correct high-form domain with \(g_k\). The original positive high source obeys, by the inherited Bessel plus true prime-2 surplus theorem (PR #161),
\[
D_{4,\pi}\succeq \kappa_\pi K_\pi+
w_2 V^*(I-A_{\log2}) V,
\quad
(\kappa_{\rm odd},\kappa_{\rm even})=(63/500,153/500),
\quad w_2=\log2/\sqrt2>12/25.
\]
Parity label \(\pi\) refers to the derivative-coordinate carrier: \(g_1,g_3\) are even; \(g_2,g_4\) odd. No finite sampled PSD matrix substitutes for this **source-conditional all-high form**.

PR #155 established a grid-free original-source analytic finite-J derivative Gram and a rigorous omitted-Gamma tail plus a verified first-window \(4\times4\) low signed source trial. This campaign integrates that already independently tested mathematics via **exact Git blobs**, not by inventing an alternative source; all imported code is checked against the frozen original source point oracle.

## 2. Four authentic center source observations (FS-02)

True \(b=\log2>5/8\) means **the entire** \(C_0=[-1/8,1/8]\) is outside the finite first-prime activation support of the ORIGINAL derivative responses. For each \(k=1,\ldots,4\), and source Gamma truncation \(J\), the actual finite derivative \((G_J u_k)'(x)\) on \(C_0\) is the sum of the following ORIGINAL completed source channels:

- pole: \(-2I_k^-e^{x/2}+2I_k^+e^{-x/2}\), with \(I_k^\pm=\int_I e^{\pm y/2}u_k(y)\,dy\) and both signs preserved;
- contact: \(C_\infty\, Vu_k(x)\) from the original \(-C_\infty K\) source;
- Gamma: \(-\sum_{j<J}2/d_j\,[F_{j,+}(x)+F_{j,-}(x)-e^{-\alpha_j(x+a)}F_{j,+}(-a)-e^{-\alpha_j(a-x)}F_{j,-}(a)]\), \(d_j=4j+1,\alpha_j=d_j/2\);
- genuine prime: **zero identically on C₀** because \(x\pm\log2\notin I\) there, *not* because the prime term was deleted from the full signed source.

The first two components and each Gamma rung admit EXACT rational-polynomial/exponential antiderivatives of \(x^t\), \(t=0,1\). No spatial quadrature, made-up contact independence, fitted high response, or nontrivial zero is used. For \(J=64\), the inherited rigorous original B3 derivative tail \(\eta_{k,J}\) gives the true weighted omitted-Gamma error
\[
\left|\int_{C_0}x^t((G-G_J)u_k)'dx\right|
\le\eta_{k,J}\,\|x^t\|_{L^2(C_0)},\qquad
\|1\|^2=1/4,\quad\|x\|^2=1/768.
\]

The **independent original** completed mixed derivative rows \(L_{qk}=\langle P_q(2x),(Gu_k)'\rangle\), \(q=0,\ldots,3\), are taken from the SHA-pinned \`CertifiedTrial\` source (not from this new integrator). Writing \(z_k=Q_{\mathcal P_{\le3}}(Gu_k)'\), the exact source center observations are
\[
\boxed{
m_k^{(t)}=\int_{C_0}x^t z_k\,dx
=\int_{C_0}x^t(Gu_k)'dx-
\sum_{q=0}^3(2q+1)L_{qk}\int_{C_0}x^tP_q(2x)\,dx.}
\]
By reflection, only four entries are nonzero:
\[
\mu_{\rm even}=(m_1^{(0)},m_3^{(0)}),\qquad
\mu_{\rm odd}=(m_2^{(1)},m_4^{(1)}).
\]
The 4-channel source interval vector includes the authentic contact/pole/Gamma errors, full derivative projection and true half density. It also must INTERSECT the independently certified P1 original-source interval from PR #161; distinct outward interval certificates need not be nested.

## 3. Genuine full \(4\times4\) source center Gram and off-diagonal correlations (FS-03)

Let \(g_x=\sum_{k=1}^4x_kg_k\), with \(x\in\mathbb R^4\), and let \(m_k\) mean its source-attested center-moment vector (the common negative sign of all \(g_k\) is irrelevant to Gram and squares). Original prime parity and exact Bessel on C₀ give
\[
\boxed{
\|g_x|_{C_0}\|_2^2\ge
4|x_1m_1+x_3m_3|^2+
768|x_2m_2+x_4m_4|^2.}
\]
Consequently the genuinely positive center Gram of the original four-column response has source-derived rank-one *off-diagonal* entries
\[
4m_1m_3,\quad 768m_2m_4,
\]
and exactly zero cross reflection parity entries. These are **not** copied from diagonals; they encode correlated original arithmetic response amplitudes, including their relative signs.

**Critical interval trap (FS-04):** if source values are only enclosed as \(m_i\in[\bar m_i-\epsilon_i,\bar m_i+\epsilon_i]\), the unknown rank-one direction rotates inside its interval cone. In general no nonzero fixed PSD matrix lies below every possible \(mm^*\). Therefore **do not** place \(\bar m\bar m^*\) into a signed Schur lower as if it were a certified true positive matrix.

Two valid alternatives are implemented:

1. **Exact all-directions nonlinear lower:**
\[
\begin{aligned}
E_C(x)\ge{}&
4\bigl(|x_1\bar m_1+x_3\bar m_3|-|x_1|\epsilon_1-|x_3|\epsilon_3\bigr)_+^2\\
&+768\bigl(|x_2\bar m_2+x_4\bar m_4|-|x_2|\epsilon_2-|x_4|\epsilon_4\bigr)_+^2,
\end{aligned}
\]
where \((y)_+=\max(0,y)\). This is an **authenticated directional form lower**, preserving both off-diagonals without inventing fixed matrix rank.

2. **True fixed rational Loewner lower** for any \(0<\eta\le1\):
\[
\boxed{
mm^*\succeq
(1-\eta)\bar m\bar m^*-
(\eta^{-1}-1)\operatorname{diag}
   \left(\epsilon_i\sum_j\epsilon_j\right).}
\]
Proof: expanding \(m=\bar m+\delta\), matrix Young bounds \(2\Re\,\bar m\delta^*\succeq-\eta\bar m\bar m^*-\eta^{-1}\delta\delta^*\); \(\delta\delta^*\preceq\operatorname{diag}(\epsilon_i\sum_j\epsilon_j)\) by weighted Cauchy. Perform this **within each parity block only**, multiplied by weights \(4\) or \(768\). The lower may have a negative direction: it is still a valid LOWER on a positive source Gram, and must not be projected/clamped to PSD. Hostile corner checks exercise all 16 interval signs.

## 4. Fully signed low-sector and arithmetic high-inverse comparison (FS-05)

Let \(A_{4,\rm lower}\) be the authentic signed lower source matrix from the inherited original finite \(G_{J_G}\), with TRUE omitted Gamma tail positive and both source poles. Let \(T_{\rm upper}\) be the **separately verified** PR #155 source-exp-polynomial derivative quotient upper with the inherited B3 Gamma \(H^1\) tail, computed before any interval approximation. Source \(S_4=A_4-R_4\), and the genuine arithmetic comparator \(B_\pi=\kappa_\pi I+(12/25)(I-A_{\log2})\) has on the ambient primitive Hilbert carrier the exact inverse gain
\[
c_\pi=\frac{12/25}{\kappa_\pi(\kappa_\pi+12/25)}
\]
on center energy, plus a separately **nonnegative** edge-phase saving. Discard the latter to remain source-conservative, and retain the authenticated four-column center Gram:
\[
\boxed{
S_4\succeq
S_{\rm scalar,lower}
+c_{\rm odd}L_{\rm even\ center}
+c_{\rm even}L_{\rm odd\ center},}
\]
where \(S_{\rm scalar,lower}=A_{4,\rm lower}-\operatorname{diag}(\kappa_\pi^{-1})T_{\rm upper}\), with inherited exact source/rounding conventions, and \(L_{\cdot}\) are the two source-interval Young Loewner floors from FS-04. This is a **complete original-source \(4\times4\) rational Loewner lower**, not a synthetic finite S4. Exact PSD on this lower would certify source S4 for the **first window only**; a negative lower means AMBIGUOUS, not that the genuine source form has a negative vector.

For any requested rational real low direction \(x\), a potentially stronger lower is
\[
\boxed{
\langle x,S_4x\rangle\ge
\langle x,S_{\rm scalar,lower}x\rangle+
c_{\rm odd}E_{C,\rm even}(x)+
c_{\rm even}E_{C,\rm odd}(x),}
\]
with *nonlinear* robust bounds from §3. The signed source low energy is never swapped for a generic positive covariance.

## 5. Hostile contracts, research authority and next routes

The authentic source derivative center formula is tested against the previous independent original \(P_1\) source interval. The true Gamma tail is error-propagated as an L² bound before integrating center test weights; source even/odd parity is **enforced algebraically**, not sampled. Both genuine pole signs and true \(p=2\) activation are retained. Additional controls: four Legendre projection weights, full source SHA, non-integral indices, source Γ truncation, coefficient-uncertainty rank-one error cone, fake cross-parity coupling, fake uniform surplus scalar from PR #161's infinite phase-locked nullspace, and no zeta-zero reading.

**Claim ledger**

| ID | Status | What would falsify it |
|---|---|---|
| FS-01 original four-mode source center analytic formula | PAPER SOURCE-CONDITIONAL + hosted exact original interval replay | wrong pole, contact, gamma rung, log2 hinge, source normalization |
| FS-02 full four completed mixed-moment source intervals | ORIGINAL SHA-PINNED SOURCE; host checks | no reflection parity or mismatch with previous independent P1 |
| FS-03 rank-two genuine four-column center Gram / cross terms | PROVED SOURCE-CONDITIONAL FROM Bessel in real center | wrong true center support/weights, wrong parity |
| FS-04 nonlinear robust and fixed Young Loewner floors | PROVED EXACT MATRIX LAW | some legal interval-vector corner violates Loewner bound |
| FS-05 signed original first-window S4 lower | SOURCE-CONDITIONAL, exact-head CI pending | false derivative Q contraction, invalid Γ tail, wrong high source comparator |
| Positive original S4 | OPEN unless source lower actually PSD | need decisive sign of authenticated full 4x4 |
| Weil all-radius source positivity / RH | OPEN | no finite first-window result alone suffices |

**Next:** source-certify the true *edge mismatch residual* on all four columns (not merely the center), potentially using PR #155's source-true piecewise exp-polynomial derivatives and original completed low moment source. Its exact two-edge flip inverse is source-derived. Optimize signed four-column \(U\) only if true \(G\)-source completed trial energy, Gamma tails, and exact test domains are transported together. Preserve the source-positive Gamma/FUCC and pole channels; no made-up physical observer or RH proof.

No source code archives or main modifications, release, tag, merge or academic priority claims are authorized. This research is a reviewable draft contribution, not a completed RH proof.


## 6. Whole true p=2 edge-mismatch residual Gram (FS-06)

The inherited original source is more structured than a generic high-sector operator. At b=log2 with b>1/2, the two actual prime-connected edge strips are L=(-1/2,1/2-b), R=(b-1/2,1/2). On R, reflect the original source derivative residual h'_k=(GP_k)' with parity (-1)^(k+1), and define z_k=Q_poly<=3 h'_k. Then for x in R the true shifted difference is

D_k(x)=z_k(x)-z_k(x-b)=
 z_k(x)+z_k(b-x) if k even derivative parity,
 z_k(x)-z_k(b-x) if k odd derivative parity,

with the actual signs set by P_k reflection: k=1,3 gives z_k(x)-z_k(b-x) and k=2,4 gives z_k(x)+z_k(b-x). The first difference is odd around midpoint x=b/2; the second is even. Hence their cross-parity inner products on R vanish EXACTLY, and two independent source edge test-functionals suffice for a nontrivial lower on the entire true four-column **edge mismatch Gram**:

- For k=1,3, set m_k^edge = 2 integral_R (x-b/2) z_k(x) dx. Then ||x-b/2||²_R=(1-b)^3/12.
- For k=2,4, set m_k^edge = 2 integral_R z_k(x) dx. Then ||1||²_R=1-b.

Using Bessel in each reflection sector,
\[
\boxed{
\|D_x\|_{L^2(R)}^2\ge
\frac{12}{(1-b)^3}|x_1m_1^{edge}+x_3m_3^{edge}|^2
+\frac{1}{1-b}|x_2m_2^{edge}+x_4m_4^{edge}|^2.}
\tag{FS-06}
\]
This is a TRUE prime-phase source observation, not a generic PSD covariance. It includes off-diagonal source correlations m1*m3 and m2*m4, with phase/derivative parity proved rather than sampled.

The \`source_four_edge_gram.py\` adapter imports the SOURCE-TRUE analytic exp-polynomial positive-edge expression from the byte-pinned PR #155, including original real Gamma J modes, true prime2 hinge, BOTH original pole terms and shared contact midpoint. It integrates that function over the true source b-dependent right edge analytically (no spatial quadrature), **subtracts all FOUR completed independent source mixed derivative moments**, then adds the actual omitted Gamma H1 derivative bound with L2 Cauchy on the edge observation test, plus the single SOURCE contact uncertainty bound. Every original source interval is carried outward. The exact source record for b and half-density is cross-checked against the frozen original code SHA.

Let ell_hi be the authenticated upper interval bound for ell=1-log2. In any source rank-one Gram lower, replacing 12/ell³ by 12/ell_hi³ and 1/ell by 1/ell_hi is safe. The same exact nonlinear interval-direction and rational Young/Gershgorin error controls from FS-04 apply. Their outputs may be ZERO or INDEFINITE when source error dominates; no fabricated positive edge observation is allowed. Independent rational source edge-mismatch polynomial controls, all interval corners, wrong parity, invalid J and SOURCE provenance are executable regressions.

## 7. Complete original signed FOUR-MODE center+edge Schur lower (FS-07)

The exact original first-prime source dual on the primitive Hilbert space has for each derivative parity sector
\[
\langle g,B^{-1}g\rangle =
\kappa^{-1}\|g\|^2 -
\frac{w}{\kappa(\kappa+w)}\|g_C\|^2 -
\frac{w}{\kappa(\kappa+2w)}\|g_R-T_bg_L\|^2,
\quad B=\kappa I+w(I-A_b),
\]
with w the SOURCE-CERTIFIED positive floor 12/25<=true w2. The source high moment-null space E is not invariant under the edge flip, hence the ambient B inverse remains a true **UPPER** for the high Schur correction. Both positive subtractions from the same source operator can be retained simultaneously; their signs must not be changed or the center/edge costs counted twice.

Using independent true-Suzuki source enclosures for all four g_k, the new signed rational lower is
\[
\boxed{ S_4\succeq
S_{\rm signed,scalar}^{\rm original\ lower}
+ c_C L_{\rm center}^{\rm true\ source}
+ c_E L_{\rm edge}^{\rm true\ source}.}
\tag{FS-07}
\]
The two source Gram lower matrices preserve all allowed cross-parity and same-parity entries. Both are conservative: a negative eigenvalue of either lower or of the signed 4x4 sum CANNOT certify negativity of the true signed Weil source. The nonlinear all-low-direction bound is also emitted; for any rational x, it retains guaranteed positive center/edge savings and may be quantitatively sharper than the fixed Loewner lower.

**Boundary of rigor:** this is a coherent assembly of paper-proved first-prime all-high arithmetic coercivity, actually SHA-verified Suzuki source intervals, true omitted Gamma derivative norm estimates and original signed low A4 source. It has not solved the complete original S4 sign, which remains an exact-head CI-determined question; no finite first-prime sign would by itself imply RH.


## 8. The interval-rank-one NO-GO and source-optimal zero comparator (FS-08)

The first true original J_edge=8 edge certificate had ALL FOUR outward source-moment intervals straddling zero. This is NOT an analytic statement that the original edge response is zero: it is a measured proof-information deficit from the inherited differentiated Γ tail. For a single reflection-parity rank-one moment Gram m*m^T where the declared possible interval vector contains m=0, any fixed PSD matrix L universally satisfying L<=m*m^T for all interval-admissible m must satisfy L<=0 (choose m=0), hence L=0. Therefore **zero is the strongest certifiable PSD Loewner lower from ONLY these interval observations**. A Young/Gershgorin lower with negative diagonals is still mathematically valid but *can worsen* the combined signed S4 lower; the implementation chooses the exact ZERO PSD floor whenever all four edge intervals contain 0. This cannot fabricate a positive edge gain, and a new J_edge=20 source interval is independently computed to test whether deeper original Gamma information resolves any edge direction.

## 9. Entire-continuum exact 2D source-sign gate (FS-09)

Even when the fixed Young 4x4 Loewner floor is indefinite, the **all-low-direction nonlinear** source inequality from §§3 and 7 retains additional information. Reflection reduces the source problem to two 2×2 real symmetric blocks. For any block and each independent center/edge row with authentic rational nominal (m1,m2), errors (e1,e2), positive weight λ, the guaranteed directional lower is
\[
q(x,y)=a x^2+2b xy+c y^2+
\sum_j\lambda_j
\left(|m_{j1}x+m_{j2}y|-e_{j1}|x|-e_{j2}|y|\right)_+^2.
\]
For x≠0 set x=1,y=t, and check x=0 separately. On each semiaxis t≥0 and t≤0 the positive part is exactly the maximum of three affine functions with rational coefficients. Partition the semiaxes at their finitely many *exact rational intersections*. On each resulting interval q(1,t) is a **rational quadratic polynomial**, so positivity for ALL real t is decided by exact endpoint/vertex checks, including both unbounded tails, with no angular grids, unsourced floating eigenvalues, dense finite matrices or guessed zero ordinates. A successful exact test certifies nonnegative signed first-window S4 under inherited source hypotheses. A failed test witnesses negativity ONLY of the conservative computed LOWER, not of genuine S4. The proof-producing routine is \`observational_succ/exact_source_two_dim_cone.py\` and its exact synthetic/source controls.

This exact interval-aware sign calculus also strengthens SUCC's general observational semantics: information carried as per-coordinate bounds is not the same as a fixed global rank-one direction, and its loss must be charged explicitly instead of repaired by a made-up PSD covariance.


## 10. True original-Gamma refinement under fixed arithmetic source (FS-10)

The source-exact exp-polynomial differentiated-convolution engine imported from PR #155 is instantiated at genuine real Gamma truncations **J=2 and J=6** (not fabricated positive auxiliary rungs). Original low signed A4, source high parity coercivity, C∞, both completed poles, the genuine p=2 half-density and the four completed mixed derivative moment packets are held fixed. The source analytic engine encloses the omitted genuine Gamma derivative energy by a provable H1/B3 estimate at both truncations; it cannot claim that a larger J necessarily improves each interval computation unless a **separate exact Loewner comparison** verifies that fact.

The executable scripts/source_four_schur_gamma_sweep.py computes the actual signed 4x4 source lower matrices for J_deriv=2 and J_deriv=6 with exact rational arithmetic, emits each diagonal lower bound, and tests whether S_lower,J6 - S_lower,J2 is genuinely PSD using the exact all-principal-minors criterion. A tighter signed **lower** remains only an improved enclosure, not an original S4 proof; a strictly negative bound is AMBIGUOUS and a first-window positive sign still would not prove RH. The probe is source-pinned and must pass hosted Python3.10/3.13 checks before its measured improvement is reported.


## 11. A strict authentic P2–P4 source cross-channel sign (FS-11)

There is a nontrivial **off-diagonal** theorem in the original four-observation source packet, not just four individual positive diagonal savings. The parity-odd *source derivative* center moment intervals at J_center=64/J_G=64 obey
\[
m_2^{(1)}\in[-0.000193219322,-0.000152731306],\quad
m_4^{(1)}\in[-0.000195002165,-0.000143728653].
\]
Both entries are strictly negative by separate original-source analytic Gamma/polar and completed-mixed-row enclosures; their PRODUCT is therefore strictly positive. The Bessel-projected two-dimensional original center observable has measured rank-one cross entry
\[
\boxed{768\,m_2^{(1)}m_4^{(1)}>0,}
\]
with its full exact rational interval generated by the four endpoint products. This certifies **source-coherent constructive coupling of the P2 and P4 center observations**. The P1–P3 measured center cross remains sign-ambiguous at J=64 because the P3 interval contains zero. Cross-reflection-parity contributions vanish identically. The UNKNOWN orthogonal portion of the entire true center L2 Gram can contribute an additional off-diagonal term of either sign; this result does NOT claim that its full off-diagonal is positive or that S4 is positive. An exact new regression explicitly distinguishes 'measured projected rank-one cross sign' from 'whole unknown Gram cross sign', and tests the true source P2P4 strict sign.
