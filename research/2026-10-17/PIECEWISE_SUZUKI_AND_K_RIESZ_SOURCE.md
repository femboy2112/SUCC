# Operation SUZUKI-EXACT × K-RIESZ: first-window analytic source energy and source-relative operator coercivity

**2026-10-17 · stacked research-only branch.** Parent: PR #153 @ \`c8ed4929cb4659de5dfbd8c8c11475e723ec2c2d\`. Original completed signed Weil source blob \`0cc8510b71d178fc79e8d410a86d8b6014cf9178\` is pinned and unchanged. No merger, publication, analytic continuation substitution, zero coordinate oracle or RH proof authorized.

## 1. Recovered actual mathematical problem

At the first prime-active window \(\,I=(-a,a),a=1/2\), on \(H=L^2_0(I)\), the original Suzuki derivative-carrier form is \(G=\begin{psmallmatrix}A_4&B^*\\B&D_4\end{psmallmatrix}\) relative to \(F_4\oplus H_{\rm high}\), with \(K=(-\Delta_N)^{-1}=V^*V\). The genuine first-window Schur form is
\[
S_4=A_4-B^*D_4^{-1}B.
\]
Inverses in this expression are understood as variational form inverses on the appropriate energy-dual domains, not unrestricted bounded Hilbert inverses. Our inherited source-conditional theorem is \(D_{4,\rm odd}\succeq(63/500)K_{\rm odd}\), \(D_{4,\rm even}\succeq(153/500)K_{\rm even}\). It is not equivalent to \(D_4\ge\kappa I\).

The inherited PDQ identity is
\[
\sup_{w\in Q_4 H\setminus0}\frac{|\langle Q_4 Gv,w\rangle|^2}{\langle Kw,w\rangle}
=\|(I-\Pi_{\mathcal P_{\le3}})(Gv)'\|_{L^2(I)}^2.
\]
This identity holds in the correct dense form domain. It expressly **does not** say \(\|(Q_4 Gv)'\|\le\|(Gv)'\|\), which is false in general.

PR #153 correctly established a projector-first upper but source midpoint/Lipschitz errors dominated. The exact \(\Theta(N^{-2})\) squared-energy ambiguity on the unrestricted Lipschitz class was proved and preserved. This campaign changes the **probe family**, not just the resolution.

## 2. Piecewise exponential-polynomial source theorem (PEX-01)

Let \(u_k(x)=P_k(2x)\), \(v_k(x)=\int_{-a}^{x}u_k(y)\,dy\), and \(b=\log 2\) with \(1/2<b<1\). For the *actual* \(J\)-rung truncation of the original completed signed Suzuki source on the positive half \(0\le x\le a\), write \(h'_{k,J}=(G_J u_k)'\).

Using the inherited source formula from \`certified_four_schur_trial.authentic_suzuki_mode_derivative_point\` and the frozen original Gamma/contact/poles, one obtains
\[
h'_{k,J}(x)=R_{k,J}(x)
+\frac{b}{\sqrt2}v_k(x-b)\,\mathbf1_{\{x\ge b-a\}},
\]
where
\[
R_{k,J}(x)=C_\infty v_k(x)-2I^-_k e^{x/2}
+2I^+_k e^{-x/2}
+\sum_{j=0}^{J-1}\left[
-\frac2{4j+1}\bigl(F_{j,+}(x)+F_{j,-}(x)\bigr)
+\frac{2e^{-\alpha_j a}}{4j+1}
\bigl(F_{j,+}(-a)e^{-\alpha_j x}+F_{j,-}(a)e^{\alpha_j x}\bigr)\right],
\quad \alpha_j=(4j+1)/2.
\]
Here \(d(e^{\pm\alpha_j x}F_{j,\pm}(x))/dx=e^{\pm\alpha_j x}u_k(x)\), and \(I^\pm_k=\int_I e^{\pm y/2}u_k(y)\,dy\). All coefficients are polynomials in \(x\) with rational coefficients, except genuine source-interval factors \(C_\infty,b,1/\sqrt2,e^{-\alpha_j a},e^{\pm a/2}\). The **single** source activation boundary on \(x\ge0\) is \(b-a\in(0,a)\). Negative-side values are fixed by the original reflection parity.

**Proof.** Substitute source oracle's exact polynomial antiderivatives into its pole, contact and finite-Gamma derivative formulas. For the true prime-2 shifted term, on \(x\ge0\) the shift \(x+b>a\) cannot contribute; \(x-b\) enters the source interval only when \(x>b-a\). The source's \(\Lambda(2)=\log2\) and half-density supply \(b/\sqrt2\). All expressions are finite exponential-polynomials on the two regions. This is an identity of the actual truncated source; it introduces no synthetic kernel. The imported full signed source, its authentic gamma tail and the signs remain separate.


**Hostile source-orientation correction (observed and repaired).** An initial analytic reconstruction assigned \(e^{-x/2}\) to the negative pole coefficient and \(e^{+x/2}\) to the positive coefficient. The independently exercised original derivative oracle decisively rejected it (for \(P_2\) at \(x=1/8\), the result differed by \(0.002094012759\ldots\)). The original implementation uses \(\mathrm{exp\_minus}(-x/2)=e^{+x/2}\) in the negative term and \(\mathrm{exp\_minus}(x/2)=e^{-x/2}\) in the positive term. The formula above is corrected; the regression oracle makes wrong pole orientation a killed route, not an editable convention.

## 3. Exact analytic projected Gram enclosure (PEX-02)

For the same-parity pairs \(i,j\), reflection yields
\[
H^{(J)}_{ij}=2\left(\int_0^{b-a}R_iR_j\,dx+
                    \int_{b-a}^{a}(R_i+\mathrm{prime}_i)
                                     (R_j+\mathrm{prime}_j)\,dx\right);
\]
the opposite-parity entries vanish **exactly**. Similarly let
\[
M_{mi}^{(J)}=2\left(
\int_0^{b-a}P_m(2x)R_i(x)\,dx+
\int_{b-a}^{a}P_m(2x)(R_i(x)+\mathrm{prime}_i(x))\,dx
\right)
\]
for the matching reflection parity; otherwise \(M_{mi}^{(J)}=0\), \(m=0,\ldots,3\).
The directly projected Gram is
\[
\boxed{T_{\rm quot}^{(J)}=
H^{(J)}-\sum_{m=0}^3(2m+1)M_m^{(J)*}M_m^{(J)}.}
\]
Each integral reduces by the exact antiderivative
\[
\int p(x)e^{\lambda x}\,dx
=\begin{cases}
\sum_k p_k x^{k+1}/(k+1),&\lambda=0,\\
e^{\lambda x}\sum_{k=0}^{d}p_k
 \sum_{j=0}^{k}\frac{(-1)^j k!}{(k-j)!}
                    \frac{x^{k-j}}{\lambda^{j+1}},&\lambda\ne0.
\end{cases}
\]
The implementation uses exact Fraction polynomial coefficients and strict rational intervals for \(b\), original contact, \(1/\sqrt2\), and rational exponentials at the endpoints. It is **not numerical quadrature**; its intervals enclose all original finite-\(J\) terms at source-pinned normalization.

The main available independent validation routes are: (a) inherited pointwise original-source derivative intervals on both sides of \(x=b-a\), including both parity sectors; (b) exact anti-derivative algebra on arbitrary synthetic exponential-polynomials; (c) direct check of the H/projection/Q identity and Gram symmetry with correctly zeroed parity blocks; and (d) regression against PR #153's midpoint upper. Reusing the inherited source interval oracle is not an independent physical source witness; the standalone polynomial/exponential integrator is a differently implemented analytic route.

## 4. Finite-to-infinite Schur transport (PEX-03, SOURCE CONDITIONAL)

For \(v_x=x-Ux\), set \(f_J=(G_Jv_x)'\), \(Q=I-\Pi_{\le3}\). The previous B3 lemma gives per-column genuine omitted-Gamma derivative bounds \(\| (G-G_J)v_i)'\|_2\le\epsilon_i\) using polynomial integration by parts. On each reflection sector the associated Gram error obeys the exact Loewner comparison
\[
E^*E\preceq\operatorname{diag}\left(\epsilon_i\sum_{j\in{\rm sector}}\epsilon_j\right).
\]
Then for any rational \(\eta>0\):
\[
Q_{\rm true}^*Q_{\rm true}\preceq
(1+\eta)\,\bigl[T_{\rm quot}^{(J)}\bigr]_{\rm rational-upper}
+(1+\eta^{-1})E_{\rm diag}.
\]
The rational upper is constructed by taking each source interval midpoint matrix and adding a per-parity maximum absolute radius-row-sum to its diagonal. It is a genuine Loewner majorant: no interval midpoint is treated as exact.

The inherited original \(\langle v_x,Gv_x\rangle\) interval lower and parity coercivity yield
\[
\boxed{
S_4\succeq M_U^{\rm source-lower}
-\operatorname{diag}_{\rm parity}
\left(\kappa_{\rm odd}^{-1},\kappa_{\rm even}^{-1}\right)
\bigl[T_{\rm quot}^{\rm source-upper}\bigr].
}
\]
The source-gated code only promotes the **first-window** lower to positive if its exact rational 4×4 PSD test passes. Even success there would not prove RH (which requires global all-radius Weil positivity). Failure/negative lower remains AMBIGUOUS, not a negative-source witness.

## 5. Infinite-dimensional source-relative non-scalar form (RZ-01)

The Bessel-4 source theorem also supplies a rational **strictly better** lower bound \(\kappa_*>\kappa_0\) in each high parity sector. Let \(K\) be the positive injective inverse-Neumann form on \(H_{\rm high}\), and \(z\) a fixed nonzero high vector with \(\langle Kz,z\rangle>0\). Define
\[
P_z^K[w]=\frac{|\langle Kw,z\rangle|^2}{\langle Kz,z\rangle}.
\]
Hilbert-space Cauchy–Schwarz in the \(K\)-form metric gives \(0\preceq P_z^K\preceq K\) for **all** high vectors, not just a finite compression. Consequently
\[
\boxed{
D_4\succeq\kappa_*K\succeq
C_z:=\kappa_0K+(\kappa_*-\kappa_0)P_z^K\succ0
}
\]
as forms on the declared sector and domain. The result is source-certified **provided** the actual SHA-pinned all-high Bessel certificate is used; \`source_riesz_high_comparison.py\` insists on that source and genuine parity-high modes, and separately checks exact finite Legendre \(K\) charts.

On the appropriate energy-dual domain the rank-one Woodbury quadratic identity is
\[
\langle r,C_z^{-1}r\rangle
=\frac1{\kappa_0}\langle r,K^{-1}r\rangle
-\frac{\kappa_*-\kappa_0}{\kappa_0\kappa_*}
\frac{|\langle r,z\rangle|^2}{\langle Kz,z\rangle}.
\]
This is a mathematically genuine, infinite-form, non-scalar source comparison. **It does not produce a stronger bound than \(\kappa_*K\)**, as next shown.

## 6. A sharp no-free-positivity theorem (RZ-02)

Suppose all source information about the high operator is \(D\succeq\kappa_*K\). Any proposed *universal* comparator \(C\preceq D\) valid for every admissible \(D\) necessarily satisfies \(C\preceq\kappa_*K\): choose the admissible source \(D=\kappa_*K\). Hence no non-scalar elaboration relying **solely on the same scalar source certificate** can outperform the strongest scalar \(\kappa_*K\) in Loewner order. To strengthen positivity genuinely requires new independent source information about \(D-\kappa_*K\) (frequency-localized multiplier, rank-one source remainder with controlled cross-terms, or genuine coercivity on a target response subspace).

Moreover, a positive finite-direction compression is not sufficient. The exact symmetric \(M=\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\succeq0\) has \(M_{11}=1>0\), yet \(M-\frac12 e_1e_1^T\) is indefinite. A candidate positive “directional surplus” inferred solely from the \(11\) diagonal is a **ghost source lower bound**.

This obstruction closes the route “take a nice positive finite high matrix, treat it as a new infinite coercivity theorem.” It is independent of RH.

## 7. Status and next discriminators

| Claim | Status | Critical instrument / failure mode |
|---|---|---|
| PEX-01 actual finite \(G_J\) exp-polynomial decomposition | PROVED CONDITIONALLY ON PINNED SOURCE; tested independent numerical source identity | Prime activation moved / pole sign flipped mutants |
| PEX-02 exact analytic \(H_J\) and polynomial quotient Gram | PROVED FINITE with rigorous intervals | Outward exponential/log evaluations, hinge endpoint interval, parity tests |
| PEX-03 authentic first-window source Schur lower | SOURCE-CONDITIONAL / exact-head CI pending | Original B3 gamma tail, parity D>=κK, no nontrivial zero inputs |
| RZ-01 source-certified non-scalar \(K\)-Riesz comparator | PROVED FORM CONDITIONAL ON Bessel-4 SOURCE; finite exact oracle | Source SHA, genuine high parity, \(D-\kappa_*K\) not sampled |
| RZ-02 no-new-coercivity-from-scalar and block compression | PROVED GENERAL / exact finite counterexample | Attempts to transport finite PSD as global surplus REFUTED |
| \(S_4\succeq0\) at \(a=1/2\) | OPEN pending a decisive source sign check | An indefinite lower proves neither sign |
| Completed all-support Weil positivity and RH | OPEN | Genuine source positivity across all test radii and complete signed form |

**Next verdict-changing work:** run real source \(U,J\) analytic packet, compare its Loewner upper against previous B1+B3 and PR #153, establish exact margin/error budget. If analytic precision ceases to be limiting yet \(S_4\) lower remains negative, abandon purely numerical refinement; find *new* high-sector source information controlling the positive spectral remainder \(D-\kappa_*K\) or direct source-constrained residual alignment. An all-radius RH result does not follow from a successful first-window result.


## 8. Exact sparse contact-gauge projector (PEX-04)

For the authentic source carrier \(u_k(x)=P_k(2x)\), the classical Legendre primitive identity is
\[
Vu_k=(u_{k+1}-u_{k-1})/(2(2k+1)).
\]
For \(Q=I-\Pi_{\mathcal P_{\le3}}\), define
\[
B_{jk}=\frac{\mathbf1_{j=k+1}-\mathbf1_{j=k-1}}{2(2k+1)},\qquad j\ge4.
\]
Since \(\langle u_j,u_l\rangle=\delta_{jl}/(2j+1)\),
\[
\boxed{V^*QV=B^*\operatorname{diag}_{j\ge4}((2j+1)^{-1})B.}
\]
For pure low modes \(1,\ldots,4\) the exact diagonal is
\(\boxed{(0,0,1/1764,1/3564)}\).
Thus the genuine contact uncertainty does not enter the polynomial-orthogonal differentiated response for the first two low modes. On arbitrary source-identified trial columns \(v_i\), it contributes at most
\(|C-C_0|\sqrt{\langle v_i,V^*QVv_i\rangle}\) in \(L^2\).
The source adapter now uses this sparse **exact** Legendre Gram; independent tests derive the same result using direct polynomial integration and inversion of the four-moment Gram.

## 9. Monotone source-contact Schur comparison (PEX-05, theorem / next probe)

The original signed derivative-carrier contact is \(-C K\), since \((Ku)'=-Vu\) and the point-derivative source contact is \(+C Vu\). Hence for \(C_2\ge C_1\),
\(G_{C_2}\preceq G_{C_1}\).
If both high compressions remain coercive on the correct common form domain, then by the infimum characterization of the Schur shorting,
\[
\boxed{S_4(G_{C_2})\preceq S_4(G_{C_1}).}
\]
This gives a potential contact-*endpoint* source certification that avoids perturbative contact-tail estimates. The whole \(A,B,D\) source packet and inherited high-sector bound must be changed coherently; changing only the derivative contact in the residual and leaving a trial-energy lower from a different source would be a **no-ghost violation**. This alternative source envelope is a future test, not silently implemented as an RH sign.


## 10. Rational finite-source response selection and recertification (PEX-06)

The existing source \`CertifiedTrial\` verifies \(G_J\) and provides exact outward intervals for the authentic low/high Galerkin block. The new \`source_schur_response_search.py\` uses only the exact rational midpoint matrix on original modes \(1,\ldots,m\), \(5\le m\le8\), to form a **candidate** high response \(U\approx (D_{\rm mid}+\lambda I)^{-1}B_{\rm mid}\). If a finite midpoint block is not SPD, a declared positive rational ridge \(\lambda\) is used; no property of that auxiliary matrix is promoted to the original infinite \(D_4\). The response is rounded to fixed-denominator rationals with strict parity zeros. It is then separately re-evaluated by the *complete original-source* analytic first-window Schur lower (pinned source + true Gamma remainder + source parity coercivity). It is not a Hilbert-matrix positivity shortcut.

**Important methodological boundary:** Numerically optimizing a finite or uncertified surrogate and reporting its eigenvalues as original source evidence is disallowed. The candidate is only a search heuristic; the fully signed source and form-domain certificate are the arbiter. A report remaining AMBIGUOUS is an honest failed sign search, not a hidden RH theorem.
