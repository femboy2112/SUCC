# Operation SOURCE-EDGE — genuine prime-2 surplus of the completed Weil high operator

Research checkpoint: October 17, 2026. **Source branch:** research/hidden-memory-schur-telescope-2026-10-17 at 6c3f768de3cca5c494ec46681f8997b28e482608 (PR #159, stacked #158/#156/#154). Separate original-source analytic integration PR #155 is a sibling and has NOT been silently merged. Frozen original Suzuki source blob: 0cc8510b71d178fc79e8d410a86d8b6014cf9178. One real Gamma, both completed poles, contact, genuine n=2 and half-density are unchanged. **RH PROVED: NO. Original S4 sign OPEN.**

## 1. The source observation missed by scalar coercivity (ES-01)

At a=1/2 let I=(-a,a), b=log(2) and w=log(2)/sqrt(2). The genuine first-window source has a<b<2a. Partition
- L=(-a,a-b)
- C=(a-b,b-a)
- R=(b-a,a).

The zero-extended primitive F=Vu is a legitimate Hilbert form input. Translation T_b maps L onto R and no other part of I back into I. The compressed symmetric genuine FUCC operator A_b=P_I(T_b+T_-b)P_I acts as a left/right flip, plus zero on the central interval C. Thus ||A_b||=1 (the special first-prime norm, NOT the full-line norm 2), and

\[
\boxed{\mathcal M_b(F):=\|F\|^2-\langle F,A_bF\rangle
=\|F_C\|^2+\|F_R-T_bF_L\|^2\ge0.}
\tag{ES-01}
\]

The original signed prime contribution is EXACTLY
\[
-w\langle F,A_bF\rangle=-w\|F\|^2+w\mathcal M_b(F).
\tag{ES-02}
\]
The Bessel coercivity route used only the source-correct uniform bound -w||F||² and discarded the second, genuine arithmetic, nonnegative term. This is the central new-to-project insight. It cannot be obtained by redistributing an assumed scalar kappa; it depends on the actual prime source geometry.

## 2. All-high source-conditional non-scalar Loewner inequality (ES-02)

The inherited WB4/PDQ proof on the ORIGINAL high derivative carrier Q4 L2_0(I) proves:
\[
D_{4,\mathrm{odd}}\succeq(63/500)K_{\mathrm{odd}},\quad
D_{4,\mathrm{even}}\succeq(153/500)K_{\mathrm{even}},\quad K=V^*V .
\]

Its Gamma multiplier uses the first 256 genuine positive Gamma rungs with a weighted Bessel/Legendre low-frequency loss, bounds the original contact and true prime norm budget, and bounds the negative sinh pole in the even derivative sector. The omitted true Gamma tower is PSD, and the original positive cosh pole was discarded in the odd derivative/even primitive sector. Redo ONLY the prime lower step by retaining (ES-02), with the exact same signed source and quantifiers, to obtain for EVERY legal high w:

\[
\boxed{
\langle w,D_4w\rangle\ \ge\
\kappa_\pi\|Vw\|_2^2+w\mathcal M_b(Vw)
+{\bf1}_{\pi=\mathrm{odd}}\ 2|\langle Vw,\cosh(x/2)\rangle|^2 .
}
\tag{ES-03}
\]

Here pi labels DERIVATIVE reflection parity; the primitive has opposite parity. The odd high primitive is even, hence the negative sinh pole is exactly zero. The even high primitive is odd, hence the positive cosh channel is absent and the inherited negative sinh estimate remains unchanged. The unused positive real Gamma tail is also available, not twice counted here.

**Status:** Classical edge-translation identity PROVED. ES-03 is PROVED PAPER CONDITIONAL ON THE SHA-PINNED ORIGINAL Bessel source theorem. It is not inferred from finite matrices, not an all-a theorem, and does not imply S4 positivity or RH.

## 3. Two source-derived surplus square-root-range channels (ES-03)

Because true log2>5/8, the fixed rational interval C0=[-1/8,1/8] lies inside genuine C. The two functions 1_C0 and x*1_C0 are orthogonal in L2(I), with exact norms squared 1/4 and 1/768. By Cauchy/Bessel:
\[
\mathcal M_b(F)\ge\|F_{C0}\|_2^2
\ge 4|\int_{C0}F|^2+768|\int_{C0}xF|^2.
\]
The original source interval gives true w>12/25, so for every high w:
\[
\boxed{D_4\succeq \kappa_\pi K+
(12/25)(4\,\ell_0^*\ell_0+768\,\ell_1^*\ell_1),}
\quad
\ell_0(w)=\int_{C0}Vw,\quad
\ell_1(w)=\int_{C0}xVw.
\tag{ES-04}
\]
This is an explicit ALL-HIGH source-derived rank-two non-scalar lower comparator; reflection places ell0 in odd derivative sector and ell1 in even derivative sector.

Equivalently, letting A_*=D_4-kappa_parity*K, the two displayed functionals are bounded in the A_* quadratic-form energy with known constants. By the classical Douglas/Riesz form-range criterion, these two very specific source functionals DO belong to the square-root range of this genuine surplus form (in the appropriate energy-dual completion). This is real partial discharge of the previous surplus-range obligation. The ORIGINAL four-low/high response functional has NOT been shown to align with either range direction.

Projection to E=P_poly<=3^\perp gives source-independent exact feature norms
\[
\|Q1_{C0}\|^2=1947/16384,\qquad
\|Q(x1_{C0})\|^2=19929/16777216 .
\]

## 4. An entire true-prime finite Ritz matrix, not just rank-two sampled positivity (ES-04)

For modes k>=5 use the actual Legendre derivative u_k=P_k(2x) and original primitive F_k=Vu_k. The exact rational original source K norm and center features are:
\[
K_{55}=1/2574,\quad K_{66}=1/4290,\quad
\ell_0(P_5)=-2925/524288,\quad
\ell_1(P_6)=-5175/16777216.
\]

The rank-two source comparator already gives STRICTLY more than 2 times the old scalar lower on P5 and more than 1.4 times it on P6. Stronger: for ANY finite polynomial primitives P,Q, the true mismatch pairing on a<b<2a is a polynomial in b with EXACT rational coefficients:
\[
\mathcal M_{P,Q}(b)=\langle P,Q\rangle
-\int_{b-a}^{a}[P(x)Q(x-b)+Q(x)P(x-b)]dx .
\]
Our independently implemented polynomial expansion, not a sampled Fourier Gram, gives for P5
\[
\mathcal M_b(F_5)=
-\frac1{2574}+\frac{b^2}{11}-\frac{b^3}{3}
+b^5-2b^7+\frac{20b^9}{9}
-\frac{14b^{11}}{11}+\frac{42b^{13}}{143},
\]
and for P6
\[
\mathcal M_b(F_6)=
-\frac1{4290}+\frac{b^2}{13}-\frac{b^3}{3}
+\frac75b^5-4b^7+\frac{20}{3}b^9
-\frac{70}{11}b^{11}+\frac{42}{13}b^{13}
-\frac{44}{65}b^{15}.
\]

Evaluate these polynomials on the **genuine independently sourced** interval enclosing log2, without rounding b to a preferred fitted value. Outward rational source estimates confirm
\(\mathcal M_b(F_5)>1/2000\) and \(\mathcal M_b(F_6)>3/10000\). Therefore
\[
\boxed{\langle P_5,D_4P_5\rangle>5(63/500)K_{55},\qquad
\langle P_6,D_4P_6\rangle>3(153/500)K_{66}.}
\tag{ES-05}
\]
These are quantitative TRUE-SOURCE Legendre high-vector inequalities conditional on WB4, not a proof for arbitrary low/high coupling. The complete positive cosh pole also contributes strictly in the odd derivative sector: Rodrigues + positive Taylor coefficients show <P5(2x),sinh(x/2)> > 1/10644480, giving another positive 8/(10644480²).

**Independent cross-oracle:** The already installed Suzuki primitive derivative-source polynomial prime_hinge_integral_polynomial(i,j,a) must equal our new arithmetic edge Gram polynomial \(\mathcal M_{ij}(b)-\langle F_i,F_j\rangle\), by two integrations by parts. Tests compare distinct implementations including P5/P6, cross parities and low modes. A fake independent n=6 coefficient or a wrong factor of two must be rejected.

## 5. Exact source high-residual inverse is algebraically available (ES-06)

Let E=P_poly<=3^\perp be the closure of VQ4H in the primitive L2 Hilbert metric, and suppose a genuine source low/high residual has K-dual representative g=-Q(Gv)' in E. ES-03 gives the high comparator
\[
B_\pi=\kappa_\pi I+w(I-A_b)\quad\text{on primitive }L^2(I).
\]
By the variational definition, the actual source high Schur correction is no larger than the ambient inverse quadratic \(\langle g,B_\pi^{-1}g\rangle\) (the actual test space E is smaller).

The source b two-edge flip diagonalizes B exactly: eigenvalues kappa on symmetric edges, kappa+2w on antisymmetric edges, and kappa+w on the center. Hence
\[
\boxed{
\langle g,B_\pi^{-1}g\rangle
=\frac1{\kappa_\pi}\|g\|^2
-\frac{w}{\kappa_\pi(\kappa_\pi+w)}\|g_C\|^2
-\frac{w}{\kappa_\pi(\kappa_\pi+2w)}
\|g_R-T_bg_L\|^2.
}
\tag{ES-06}
\]
This is an **explicit operator-valued saving** over the scalar kappa inverse, sourced by prime phase and actual center support, not by a hypothetical positive covariance. The true source lower w>12/25 can be substituted for a weaker certified upper inverse, since inversion reverses Loewner order.

CAUTION: E does NOT generally reduce the compressed shift. The displayed ambient inverse is a valid UPPER on the original correction, not automatically the *exact* inverse of the high-space compressed comparator. On finite models, an additional rigorously positive polynomial-observation correction is
\[
\langle g,B^{-1}g\rangle
-(P^*B^{-1}g)^*(P^*B^{-1}P)^{-1}(P^*B^{-1}g).
\]
The source \(g\) must still be computed from the ORIGINAL Suzuki low/high response. The current code does NOT claim that its mathematical test g represents that source, and does NOT certify S4 or RH. The original source-exact analytic derivative integrator in separate PR #155 is a possible next cross-repository/branch interface, but must be imported with exact dependency pins and independently revalidated.

## 6. Falsifiers, provenance, statuses, next verdict-changing probe

| Claim | Status | Decisive guard |
|---|---|---|
| ES-01 true two-edge norm-1 flip | DISCLOSED CLASSICAL | Correct a<b<2a; flipped factor-two or fake prime source dies |
| ES-02 whole-high original arithmetic surplus | PROVED PAPER / SOURCE CONDITIONAL | SHA-pinned Bessel, real Gamma, both poles, true prime2 |
| ES-03 two source high surplus range probes | PROVED SOURCE CONDITIONAL | Rational inner center, exact 4/768, actual w2>12/25 |
| ES-04 P5/P6 source 5x/3x diagonal lower gains | EXACT SOURCE-INTERVAL CERTIFICATE, hosted replay pending | Independent true log2 source, fake Γ/pole/phase mutations |
| ES-05 prime source cross-oral | EXACT FINITE POLYNOMIAL | Different integration formulas must agree coefficient by coefficient |
| ES-06 edge phase dual correction | PROVED SOURCE-CONDITIONAL + exact finite inverse models | Correct high E domain, wrong sign on off-diagonal, false attainability |
| Signed first-window S4 sign | **UNVERIFIED** | Need source-attested g center/mismatch or full low/high inversion |
| All-radius completed Weil positivity and RH | **OPEN** | First window not enough, zero location reading prohibited |

Source files: observational_succ/authentic_prime_surplus.py and prime_surplus_dual.py; exact and authenticated tests; scripts/prime_two_surplus_probe.py. The true positive Gamma tail can supply still further source-positive spectral surplus; this campaign does NOT double count it.

**Highest leverage next actual original-source probe:** use the source-exact piecewise derivative representation from PR #155 to derive a rigorous, outward-interval lower bound on either the center energy \(\|g_C\|^2\) or phase mismatch \(\|g_R-T_bg_L\|^2\) for the TRUE low residual g, then insert the positive savings from ES-06 into the four-low Schur lower. A finite matched sample, a hypothetical Hilbert g, a rank-only source projector, or a generic scalar κ shift cannot discharge this remaining source-interface obligation. Main and archived originals must remain unchanged.


## 7. A genuine arithmetic no-uniform-gap theorem (ES-07)

The positivity in ES-03 is directional. It **cannot** be promoted to a strictly positive scalar lower bound for the prime mismatch operator on the full moment-null high space. In fact the original first-prime source has an **infinite-dimensional smooth nullspace** for the isolated prime mismatch, even after all four polynomial moment constraints.

**Theorem (PROVED PAPER, genuine source b=log2).** Let b in (a,2a), F any C_c^infty(I) primitive, and E the subspace orthogonal to polynomial moments 0..3. Choose any smooth compactly supported function phi in the left edge L and extend
  F=phi+T_b phi.
The supports are disjoint, entirely inside L union R; the center is zero and F_R=T_b F_L exactly. Hence M_b(F)=0 and ||F||>0 for phi not identically zero. The four global moments reduce to four linear functionals
  int_L [x^j+(x+b)^j] phi(x) dx=0 for j=0..3.
Choose **five** linearly independent smooth bumps phi_i in L. The homogeneous 4x5 linear system has a nonzero combination phi, hence a nonzero F with all four moments zero and exactly M_b(F)=0. Choosing arbitrarily many linearly independent bumps shows an infinite-dimensional kernel in E. Then u=F' is a genuine mean-zero original high derivative-carrier test, since <u,P_k(2x)>=-<F,P'_k(2x)>=0 for k=1..4.

The original true b=log2 lies in (a,2a), so this proof applies to the **actual first-prime geometry** without synthesizing any new Euler source. It refutes the tempting statement \(\mathcal M_b(F)\ge\epsilon\|F\|^2\) for some uniform epsilon>0 on the four-moment high space; the true Gamma/coercive and completed polar terms remain present in the whole signed Weil source and are NOT refuted.

The new test model constructs an exact rational 4x5 moment matrix on FIVE pairs of perfectly shift-correlated left/right cells with b=7/10, solves an exact nonzero rational null vector, and verifies all moments vanish while the modeled edge mismatch and center energy are exactly zero. The piecewise-constant model is NOT mislabeled smooth; the smooth theorem comes from the independent finite-codimension argument.

**Implication for RH:** strengthening the original high sector by retaining prime2 energy is legitimate, and its diagonal P5/P6 gains are large, but the operator's nullspace forces any universal Schur proof to use actual coupling alignment, the positive Gamma source, completed polar contacts, or a nontrivial interaction theorem. One cannot close S4 merely by asserting a new uniform prime-induced spectral gap.


## 8. Actual original P1 low/high residual overlap with arithmetic surplus (ES-08; pending hosted exact-head source verification)

The previous ES-06 inequality required a **genuine source-derived**, not synthetic, low/high K-dual residual \(g_1=-Q_{\mathcal P_{\le3}}(G P_1(2x))'\). A new independent source adapter evaluates its center moment on a certified fixed C0=[-1/8,1/8] included in the actual prime-2 central strip. Exact symbolic integration of the original (unmodified) finite-J signed Suzuki derivative through C0 retains BOTH completed poles, the original contact scalar, and J REAL Gamma rungs; the genuine prime2 convolution term is exactly absent on C0 (since true log2>5/8). It does NOT fit a free g. Its analytic pole orientation is copied from and checked against the frozen original SHA-pinned source rather than guessed.

The source center derivative integral interval is extended to full Gamma by an independently stated original polynomial B3 differentiated OU tail estimate. For \(d=4J+1\) and genuine Legendre polynomial \(u=P_1(2x)\),
\[
\|(G-G_J)u)'\|_2\le 2\|u'\|_2(d^{-2}+8d^{-3})+
(|u(1/2)|+|u(-1/2)|)\left(\frac{2}{3d^{3/2}}+\frac4{d^{5/2}}\right).
\]
Center integration costs only \(\|1_{C0}\|_2=1/2\). Original independently authenticated *completed* degree-0 and degree-2 derivative-Legendre moments \(L_0,L_2\) are obtained via \`certified_four_schur_trial.CertifiedTrial\` — NOT the new analytic center integrator. Since \(\int_{C0}P_0=1/4\) and \(\int_{C0}P_2=-15/128\), the exact projected residual moment is
\[
m_1=\int_{C0}(GP_1)'\,dx-\frac14L_0+\frac{75}{128}L_2 .
\]
A source interval \([m_-,m_+]\) excluding zero would prove
\[
\|g_1|_{C0}\|_2^2\ge 4\min(|m_-|,|m_+|)^2>0
\]
and therefore the **genuine** first-window low-mode P1 original-source Schur upper correction is STRICTLY smaller than the old scalar \(\kappa_{\rm odd}^{-1}\|g_1\|_2^2\), by a certified amount
\[
\boxed{\Delta_1\ge\frac{12/25}{(63/500)(63/500+12/25)}
             4\min(|m_-|,|m_+|)^2.}
\]
This would be a source-attested arithmetic **off-diagonal low/high overlap** and a real step toward the original four-mode Schur residual. However, **a strict positive P1 dual saving does not imply S4 positive**: the complete 4×4 residual coupling and trial-energy lower remain necessary. The proof/test status will only be promoted if the exact-head hosted Python 3.10+3.13 source CI confirms the strict interval sign, true source and Gamma tail. Any zero-overlapping interval stays AMBIGUOUS, never an invented strict result.

Important analytic scope: the stated B3 Gamma tail estimate is an analytic series bound for any integer J≥1, although earlier source-point derivative evaluators were capped at J≤20 for computational reasons. This adapter evaluates J=64 with rational exponential integrals for the finite prefix (not the earlier sampled point oracle). It must validate the series-tail derivation on its own terms; finite success is not an RH proof.
