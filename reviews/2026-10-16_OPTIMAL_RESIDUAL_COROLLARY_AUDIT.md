# Optimal continuum residual corollary: independent paper audit

2026-10-16. **SURVIVES — CONDITIONAL PAPER PROOF.**
For the fixed actual source, exact columnwise continuum residual minimization
on nested high Legendre spans gives Schur brackets converging in low
operator norm to \(S_0\), with residual Grams decreasing to zero.
**No monotonicity of \(H_{U_N}\), degree-dependent convergence rate, actual
source sign, or RH conclusion is asserted.** This is a late principal
corollary of existing premises, not a claimed novel literature theorem or
independent arithmetic source construction.

Scope: one new review only; no code, existing dossier/receipt, or git
mutation. No numerical, Lean, or full-suite tests were run. The repository
AGENTS.md, docs/METHOD.md, the Aletheia method and its provenance-interferometry
instructions were read. No callable independent worker tool was available:
the proof and adversarial passes share one reasoner and are not independent
agent votes.

## 1. Exact dependencies

Use \(I=(-1/2,1/2)\), \(H=L^2_0(I;\mathbb C)\),
\(l_j(t)=P_j(2t)\), \(PH=\operatorname{span}(l_1,\ldots,l_4)\),
\(QH=\mathcal P_4^\perp\), \(M=\mathcal P_3^\perp\).
Write \(J:PH\hookrightarrow H\) for inclusion. Set
\[
X_N=\operatorname{span}(l_5,\ldots,l_N),\quad
R=R_Q=\Pi_M(G\,\cdot\,)'|_{QH},\quad Y=R_P=\Pi_M(G\,\cdot\,)'|_{PH}.
\]
All residual norms are actual continuum \(L^2(I)\) norms. Inner products
are linear in the first argument. The inherited premises are:

1. FRACTIONAL_SOURCE_RANGE_AUDIT.md, fixed domains and SR-01–04:
   \(R,Y\) are bounded, \(R\) is compact, and
   \(\overline{\operatorname{Ran}R}=M\). Source-specific density depends on
   the genuine Gamma/domain argument and the inherited whole-high bound
   \[
   D=QGQ\geq\kappa K_Q,\quad K_Q=V_Q^*V_Q,\quad
   V_Q u(t)=\int_{-1/2}^t u(s)\,ds,\quad \kappa=20699/10^6>0. \tag{1}
   \]
   This audit accepts, rather than re-proves, those analytic premises.
2. AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md, definitions/E-03, and its
   explicit dependency OBSERVER_SCHUR_SOURCE.md, OS-SOURCE-04:
   \(b=QGP\) has columns in \(\operatorname{Ran}D^{1/2}\);
   \(t=D^{-1/2}b\), \(S_0=A-t^*t\); every finite-column high trial obeys
   \[
   H_U-\kappa^{-1}C_U\leq S_0\leq H_U,\quad
   H_U=(J-U)^*G(J-U),\quad C_U=(Y-RU)^*(Y-RU). \tag{2}
   \]
3. Legendre completeness: the nested \(X_N\) have dense union in \(QH\).
   Boundedness of \(R\) transfers that approximation to its images.

The new convergence implication uses boundedness, density, finite low
dimension and (2). Compactness is needed only for the range/stability
statements below. No fractional-range exponent above \(1/2\), bounded
inverse of \(D\), or upper comparison \(D\leq CK_Q\) is required.

## 2. Finite minimizers: existence, and actual-source uniqueness

For \(j=1,\ldots,4\), define
\[
u_{N,j}\in\arg\min_{u\in X_N}\|Yl_j-Ru\|_2^2,\qquad U_Nl_j=u_{N,j}.
\tag{3}
\]
The image \(Z_N=RX_N\) is finite-dimensional and closed, so its orthogonal
projection \(\Pi_N\) exists. The minimum is attained and every minimizer
satisfies \(Ru_{N,j}=\Pi_NYl_j\). For a general bounded map, minimizers
can differ by \(X_N\cap\ker R\); their residual is nevertheless unique.
Dense range alone does not imply uniqueness.

For this actual source, **\(R\) is injective**. If \(u\in QH\), then
\(Vu\in H^1_0(I)\cap M\). The endpoint values vanish by the mean-zero
condition; its moments through degree three vanish by integration by parts
and the moments of \(u\) through degree four. Since \(Gu\in H^1(I)\),
Sobolev integration by parts gives
\[
\langle Du,u\rangle=\langle Gu,u\rangle
=-\langle(Gu)',Vu\rangle=-\langle Ru,Vu\rangle. \tag{4}
\]
There is no derivative of a high projection and no omitted endpoint term.
If \(Ru=0\), (1) and (4) force \(Vu=0\), hence \(u=(Vu)'=0\).
Thus each finite minimizer in (3) is unique. Its finite Gram is positive
definite; this gives no uniform bound on the inverse Gram.

The exact normal equation is
\(\langle Yl_j-Ru_{N,j},Rv\rangle=0\) for every \(v\in X_N\).
It concerns the full continuum source, not a sampled or truncated objective.

## 3. Projection proof and bracket convergence

The union of the \(Z_N\) is dense in \(M\): approximate any target by
\(Ru\), using range density, and then approximate \(u\) by high Legendre
polynomials, using boundedness of \(R\). Consequently \(\Pi_N\to I_M\)
strongly. The column identities extend linearly to every low input:
\[
F_N:=Y-RU_N=(I-\Pi_N)Y,\qquad
C_N=F_N^*F_N=Y^*(I-\Pi_N)Y. \tag{5}
\]
Nesting gives \(0\leq C_{N+1}\leq C_N\). For an orthonormal low basis
\(e_1,\ldots,e_4\),
\[
\|F_N\|_{\rm op}^2
\leq\sum_{j=1}^4\|(I-\Pi_N)Ye_j\|_2^2\longrightarrow0,\qquad
\|C_N\|_{\rm op}=\|F_N\|_{\rm op}^2\longrightarrow0. \tag{6}
\]
Finite low dimension supplies uniformity on the low unit sphere;
pointwise convergence alone would not suffice on an arbitrary infinite
low space.

Put \(H_N=H_{U_N}\), \(B_N^-=H_N-\kappa^{-1}C_N\), \(B_N^+=H_N\).
Equation (2) implies
\[
0\leq H_N-S_0\leq\kappa^{-1}C_N,\qquad
0\leq S_0-B_N^-\leq\kappa^{-1}C_N.
\]
Taking norms of positive operators proves
\[
\boxed{\ \|B_N^\pm-S_0\|_{\rm op}
\leq\kappa^{-1}\|C_N\|_{\rm op}\longrightarrow0.\ } \tag{7}
\]
Only \(C_N\)'s monotonicity is asserted. Neither \(H_N\) nor \(B_N^-\)
needs to be monotone. This is an a posteriori residual bound, not a rate
in degree \(N\). No attainment of an infinite-dimensional minimum or
boundedness of \(U_N\) entered the proof.

## 4. Coordinate metric and the different Galerkin objective

In the unnormalized basis \(l_1,\ldots,l_4\),
\[
W=\operatorname{diag}(1/3,1/5,1/7,1/9),\qquad e_j=\sqrt{2j+1}\,l_j.
\]
For the form matrix \((C_N^{\rm f})_{ij}=\langle F_Nl_j,F_Nl_i\rangle\),
\[
\|C_N\|_{\rm op}=\|W^{-1/2}C_N^{\rm f}W^{-1/2}\|_2
\leq\operatorname{tr}(W^{-1}C_N^{\rm f})
=\sum_{j=1}^4(2j+1)\|F_Nl_j\|_2^2. \tag{8}
\]
The same congruence applies to Schur form errors. A bound \(C_N\leq cI\)
means \(C_N^{\rm f}\leq cW\), not \(cI_4\). Normalizing the low columns
does not change their least-squares minimizers.

Energy Galerkin imposes \(\langle bl_j-Du,v\rangle=0\) on \(X_N\).
It minimizes \(\|tl_j-D^{1/2}u\|^2\), not \(\|Yl_j-Ru\|^2\).
The completion identity
\[
H_U-S_0=(t-D^{1/2}U)^*(t-D^{1/2}U)
\]
and (2) show that residual convergence implies energy convergence; the
reverse implication is unavailable.

For an exact adverse receipt, COMPACT_SOURCE_GALERKIN.md, CG-07, uses
\(s_j=2^{-j}\) and
\[
D_j=\begin{pmatrix}s_j^8&s_j^7/2\\s_j^7/2&s_j^6\end{pmatrix},
\quad K_j=(s_j^8/2)I_2,\quad b_j=(s_j^5,0).
\]
Here \(D\geq K\), \(K^{-1/2}D\) is compact with dense range, and coordinate
Galerkin at \(N=2j-1\) has energy error \((7/9)s_j^2\to0\) but squared
relative residual \(1/2+(2/3)s_j^2\to1/2\); at \(N=2j\) that residual
is \((2/3)s_j^2\to0\). Thus the full residual sequence fails to converge.
This inherited synthetic counterexample distinguishes objectives; it
refutes neither (3) nor a source sign.

## 5. Compact+dense: nonclosed range, not onto, possible norm blowup

The compact+dense conclusion is correct on infinite-dimensional
\(M=\mathcal P_3^\perp\). If \(\operatorname{Ran}R\) were closed it would
equal \(M\). Then \(R:(\ker R)^\perp\to M\) would be a bounded bijection
with bounded inverse. Composition with compact \(R\) would make the
identity on \(M\) compact, contradicting an infinite orthonormal sequence.
Thus the range is nonclosed and not onto, even without assuming
injectivity. In the actual injective case its inverse on its dense proper
range is unbounded.

This does not decide whether any of the four particular columns of \(Y\)
is in the range. If a target \(y\notin\operatorname{Ran}R\) and \(Ru_N\to y\),
then \(\|u_N\|\to\infty\): otherwise a bounded subsequence has a weakly
convergent subsequence, and compactness makes its images converge strongly
to the image of its weak limit, producing a preimage of \(y\).

A complete synthetic control is \(R=\operatorname{diag}(1/n)\) on
\(\ell^2\), \(y=(1/n)_{n\geq1}\), \(D=K=R^*R\), \(b=R^*y\), with one
low dimension and \(A=\|y\|^2+a\). Here \(S_0=a\). On the first \(N\)
coordinates the unique minimizer is \(u_{N,n}=1\) for \(n\leq N\) and
zero otherwise. Therefore
\[
\|u_N\|=\sqrt N,\quad C_N=\sum_{n>N}n^{-2}=:q_N\to0,\quad H_N=a+q_N.
\tag{9}
\]
There is no infinite \(\ell^2\) preimage of \(y\). This compact block
source satisfies the short/range premises and (2) for any \(0<\kappa\leq1\);
it embeds into four low dimensions by direct sum. Response blowup and
bracket convergence coexist. This is not the arithmetic source.

## 6. Inexact optimization and effective certification

Exact minimization is sufficient, not necessary. If admissible approximate
columns obey the actual continuum inequality
\[
\|Yl_j-R\widetilde u_{N,j}\|^2
\leq\min_{u\in X_N}\|Yl_j-Ru\|^2+\epsilon_{N,j},
\quad \epsilon_{N,j}\geq0,\quad\epsilon_{N,j}\to0,
\tag{10}
\]
then (6)–(7) still follow. Their residual Grams need not be monotone.
Direct certification that the actual residual tends to zero also suffices.

Vanishing operator approximation error alone is insufficient. In (9),
replace just the \(N\)-th diagonal entry of \(R\) by \(N^{-3}\), obtaining
\(\widetilde R_N\). It is injective and
\(\|\widetilde R_N-R\|=N^{-1}-N^{-3}\to0\). Its unique exact minimizer on
the first \(N\) coordinates has entries \(1\) before \(N\), and \(N^2\)
at \(N\). Its approximate squared residual is \(q_N\to0\), but its true
residual has \(N\)-th coordinate \(N^{-1}-N\). Even unique exact
minimizers of converging inexact objectives can therefore fail.

For approximating maps into a common residual Hilbert space the issue is
\[
\|Y-R\widetilde U_N\|
\leq\|\widetilde Y_N-\widetilde R_N\widetilde U_N\|
 +\|Y-\widetilde Y_N\|
 +\|R-\widetilde R_N\|\,\|\widetilde U_N\|. \tag{11}
\]
Sampled least squares additionally requires a justified comparison with
the continuum norm; fit/holdout agreement alone does not supply it.

Effective certification needs explicit admissible coefficients and
rigorous full-source enclosures for \(H_U,C_U\), covering projection,
spatial integration, the entire Gamma remainder, rounding and the metric
\(W\). Given \(H^-\leq H_U\leq H^+\), \(C_U\leq C^+\), the certified
bracket is \(H^- -\kappa^{-1}C^+\leq S_0\leq H^+\).
Errors must become sufficiently small in absolute low operator norm.
For example the inherited differentiated Gamma bound is
\(\|F_U-F_{U,J}\|\leq\eta_J\|J-U\|\), where
\(\eta_J=2/(4J+1)+8/(4J+1)^2\); source-form tail errors scale with
\(\|J-U\|^2\). Fixed truncation/precision is unjustified when responses grow.

No stronger fractional-range theorem or a priori rate is logically
necessary for eventual certification with a strict margin: **if**
arbitrarily accurate rigorous evaluations for rational polynomial trials
are available, enumerate those trials and dovetail evaluation precision.
Rational coefficient approximation and boundedness preserve arbitrarily
small residuals. This supplies a conditional semidecision route, not an
implemented algorithm or a resource bound. A prescribed degree/runtime
would need further effective approximation or stability estimates. The
two inherited analytic facts alone do not establish that computational
interface; no existing sampled experiment is promoted here.

## 7. Strict versus singular sign

If \(S_0\geq\delta I\), \(\delta>0\), (7) makes \(B_N^->0\) eventually.
If some low \(x\) has \(\langle S_0x,x\rangle<0\), then
\(\langle H_Nx,x\rangle<0\) eventually. If \(S_0\) is nonsingular,
sufficiently close brackets have its inertia. These are conditional
eventual statements, with no actual sign or degree supplied.

Singular semidefiniteness has no automatic finite stopping conclusion.
In (9), choose \(a=0\), with the valid bound \(\kappa=1/2\).
Every bracket is then \(-q_N\leq S_0=0\leq q_N\), with \(q_N>0\).
It shrinks to zero but never certifies nonnegativity from its lower
endpoint. Some singular cases admit exact structural certificates;
convergence alone guarantees none. A negative lower bound is never
evidence of a negative short.

## 8. Claim ledger and freeze

| Claim | Verdict and boundary |
|---|---|
| Finite exact minimizers exist | PROVED by finite image projection |
| Actual-source minimizers are unique | PROVED CONDITIONAL on (1), regularity and (4) |
| \(C_N\downarrow0\) in low operator norm | PROVED CONDITIONAL on source range density |
| Both Schur brackets converge to \(S_0\) | PROVED CONDITIONAL by squeezing; no rate or endpoint monotonicity |
| Energy convergence implies this residual convergence | REFUTED in general by inherited CG-07 |
| Compact dense range in infinite \(M\) is nonclosed/not onto | PROVED; specified target attainment remains unresolved |
| Bounded responses or stable inexact optimization follow | REFUTED in general by Sections 5–6 |
| Convergence always decides singular nonnegativity | REFUTED by Section 7 |
| Actual low sign, effective implementation, or RH | NOT ESTABLISHED by this audit |

Aletheia separation: direct contact is local dossier access and the
displayed derivations; truth status concerns the conditional implication,
while source correctness remains inherited. The two source dossiers share
the same arithmetic lineage and coercivity premise: one source family,
not independent arithmetic bearings. Synthetic controls test overclaims,
not that source. Publication pressure adds no evidence. Without density,
the projection proof leaves the residual onto the complement of
\(\overline{\operatorname{Ran}R}\); without (2), it supplies no Schur
squeeze. No statistical score, factorial experiment or phasor is asserted.
The next useful practical discriminator is a rigorously enclosed continuum
residual for an explicit useful trial; this qualitative corollary itself
needs no new numerical experiment.

Intake metadata, read as files without invoking git: branch
research/arithmetic-wavefront-spectral-response-2026-10-16,
HEAD 6e179c6204360c17b39cbdec0599acf01e7213a9. This is an intake snapshot,
not a statement about the principal's subsequent publication head.
The new review target was absent. The following SHA256 values were read:

| File | SHA256 |
|---|---|
| research/2026-10-16/FRACTIONAL_SOURCE_RANGE_AUDIT.md | 30b689a3ceb109d97ce93ddbf28e4adb39e8a76ceab3c3f8964c8b05379c6d9d |
| research/2026-10-16/AUTHENTIC_SCHUR_RESPONSE_CERTIFICATE.md | 78c113e4c1cbe09ff361e49ca51f4e0a57e4fb1af3ebd69673565aaa17222875 |
| research/2026-10-16/OBSERVER_SCHUR_SOURCE.md | 0a269b8bc9b0840e132e3a31ab88fc3c1330c7a38b6013afdc426e0333f03dab |
| research/2026-10-16/COMPACT_SOURCE_GALERKIN.md | 6e44d42fedd72274d8732272315bd05a43564c13bc423338a4711c0746b3986e |
| reviews/2026-10-16_ARITHMETIC_RESONANCE_HOSTILE_AUDIT.md | df29cf2cd36b009fff130f82fc3fff24643cc629114ff71c9dd75519ce596b6a |
| observational_succ/source_weil_hierarchy.py | 183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b |

The source-byte match is provenance contact, not independent proof of its
arithmetic identity. This review is frozen at the stated conditional paper
verdict. Principal full-suite receipts and publication remain outside
this review's execution and claims.
