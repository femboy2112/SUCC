# Operation WHOLE RESIDUAL — the genuine original four-mode Suzuki Schur has a rigorously observable continuum action

**Date:** 2026-10-18. **Source:** stacked on GKR draft PR #174 at exact 6fb1dba87ed273350a636b14b248fccacfb88934, with IGC #171 and TBF #170 in ancestry. **Immutable ORIGINAL signed Suzuki/Git source blob** 0cc8510b71d178fc79e8d410a86d8b6014cf9178. Source includes true \(\Lambda(2)=\log2\), weight \(\log2/\sqrt2\), exactly one real Gamma completion, original contact, and **BOTH completed polar signs**. No nontrivial zeta-zero coordinates used. **First-window S4 SIGN OPEN. RH PROVED: NO.**

## 1. Recovered mathematical obstruction

On I=(-1/2,1/2), let H=L²_0(I) and u_k(x)=P_k(2x) for k=1..4. Let H_high=(span(u1,..,u4))^perp, K=V*V, (Vu)(x)=integral_(-1/2)^x u(t)dt. The exact original Suzuki signed derivative form G has blocks \(\begin{bmatrix}A_4 & B^*\\B&D_4\end{bmatrix}\). The inherited *source-conditional all-high* theorem asserts, on the proper high FORM domain, D_4>=κ_pi K with κ_odd=63/500, κ_even=153/500 (parity of DERIVATIVE). It does not assert D_4>=κI on ordinary derivative L².

The K-completion V H_high has primitive representation E=(poly_degree<=3)^perp in L²(I). On the appropriate positive closed source-form domain the high operator D has gap D>=κI. In this Hilbert space the true low/high source dual vector is \(g_i=Q_E H_\infty F_i\), \(F_i=V u_i\), with actual completed primitive operator H, and the **original** Schur expression is

    S4(c) = inf_{x in E} q(F_c-x)
          = q(F_c-x_trial) - <r_c,D^{-1}r_c>,
    r_c = Q_E H_inf (F_c-x_trial).

Therefore for any operator-domain trial and actual residual observation,

    S4(c) >= q_inf(h_c) - ||r_c||²/kappa_pi,
    h_c=F_c-x_trial.                                            (1)

This is classical shorting/Riesz algebra, but the Riesz norm must come from the TRUE continuum source. An apparently positive 4x4 Galerkin block or a finite list of action samples is not a substitute. The earlier H¹ derivative bound cannot be silently rewritten as a K=L² primitive bound.

## 2. The source-faithful boundary-matched family (OCR-01)

For each low i=1..4, choose m_i=(5,6,5,6)_i, the smallest same-derivative-parity high Legendre mode. Define the actual HIGH trial

    x_i=V u_(m_i) + sum_(r=0)^(N-1) t_(i,r) U_(m_i+2r),
    U_m=V(u_m-u_(m+2)), m>=5,

and its low-minus-high difference

    h_i=V(u_i-u_(m_i)) - sum_r t_(i,r)U_(m_i+2r).                (2)

The exact Legendre boundary values u_k(+1/2)=1 and u_k(-1/2)=(-1)^k imply **h_i=0 and h_i'=0 at both physical endpoints**. Every U_m and x_i is lawful original Q4 high data because only genuine Legendre derivatives k>=5 appear. Thus \(h_i\in H²_0(I)\); its zero extension to R is H². For every real low coefficient vector c, h_c=sum_i c_i h_i remains in H²_0(I), while x_c lies in the original K-high completion.

We separately certify the old two Jacobi-clamped directions, and the new many-mode U_m basis, by exact Fraction polynomial primitives, exact \(\int h_i' P_k(2x)=0\) for k=1..4 on each high correction, endpoint trace identities, and independent Legendre-derivative coefficient expansions. No boundary traces are fitted or assumed; they are identities of the actual original P_k.

## 3. Entire frozen signed finite primitive action, not a sampled Gram (OCR-02)

For h a polynomial primitive, the genuine first-prime source's finite real-Gamma operator is exactly

    H_J h = (c_J-C_inf)h
            -sum_(j<J) E_(alpha_j)h
            -w A_b h
            +2<c,h>c-2<s,h>s,                                  (3)

where \(d_j=4j+1\), \(\alpha_j=d_j/2\), \(c_J=\sum_{j<J}4/d_j\), \(A_b=P_I(T_b+T_{-b})P_I\), \(b=\log2\), \(w=b/\sqrt2\), \(C_inf=\gamma+\pi/2+3\log2+\log\pi\), \(c(x)=\cosh(x/2)\), \(s(x)=\sinh(x/2)\), and E_alpha has the authentic exponential OU kernel \(e^{-\alpha|x-y|}\). BOTH completed polar terms have their original opposite signs.

We independently constructed a global exact-Fraction polynomial approximation to the **actual continuum action**, rather than fitting a finite grid. Define the source-independent absolute moment functions

    K_k[h](x)=integral_I |x-y|^k h(y)dy.

They are exact rational polynomials obeying

    K_0[h]=integral_I h,
    K_1[h]''=2h,
    K_k[h]''=k(k-1)K_(k-2)[h]    (k>=2),                       (4)

with exact left-endpoint value and derivative

    K_k[h](-a)=integral_I(y+a)^k h(y)dy,
    K_k[h]'(-a)=-k integral_I(y+a)^(k-1)h(y)dy.

These equations determine each entire rational polynomial uniquely. Hence

    sum_(j<J) E_(alpha_j) h
       = sum_(k=0)^M [sum_(j<J)(-alpha_j)^k/k!] K_k[h] + error. (5)

On |x-y|<=1 the Taylor–Lagrange remainder of \(e^{-\alpha|x-y|}\) is <=alpha^(M+1)/(M+1)!; since I length1, this gives the TRUE continuum L² action error

    ||error_OU||_2 <= [sum_(j<J)alpha_j^(M+1)/(M+1)!] ||h||_2.  (6)

Polar cosh/sinh are separately replaced by rational even/odd polynomials from exp Taylor degree P, with rigorous sup error epsilon<=2(1/4)^(P+1)/(P+1)! since |x/2|<=1/4 and exp(1/4)<2. The entire two-pole rank-one operator error is <=4 epsilon (4+epsilon)||h||_2, preserving signs.

The ORIGINAL source interval b, w and C_inf is read only through source_weil_hierarchy.py after a frozen Git SHA and genuine n=2 wavefront check. Its rational center is snapped at a declared 10^-12 grid with **all** source widths added to separate db,dw,dC. The shifted-prime source variation is bounded by

    ||w A_b h -w0 A_b0 h||_2
       <=dw||h||_2 +2|w0|db||h'||_2,                         (7)

using actual ||A_b||<=1 and the H¹ zero-extension translation estimate. The contact uncertainty is <=dC||h||. Combining (6),(7) and polar estimates yields a single exact rational upper \(e_{J,M,P}(h)\) on the WHOLE source action \(\|H_J h-P_{J,M,P}h\|_2\).

The approximant P is exactly piecewise rational POLYNOMIAL on three TRUE source-supported intervals L=(-a,a-b0), C=(a-b0,b0-a), R=(b0-a,a). All its continuum polynomial products are integrated by exact primitives, including the true active shifted polynomial on L/R, not a source-blind Hermitian surrogate.

## 4. Exact full continuum projection and archived independent source replay (OCR-03)

The original high-space primitive moment projector is \(\Pi_{\le3}\), not the derivative low P1..P4 projector. Since \(\|P_k(2x)\|²=1/(2k+1)\),

    <Q_E f,Q_E g> =
      <f,g> - sum_(k=0)^3 (2k+1)
        <f,P_k(2x)> <g,P_k(2x)>.                            (8)

All terms on the right are integrated EXACTLY on the three rational intervals of P, for the source's true four low modes and high candidate combinations; no spatial samples, floating eigenvalues or fit-to-original Gram.

The original SUCC exponential-antiderivative integrator \`suzuki_legendre_source.authentic_full_low_entry\`, using the frozen Git blob and source Gamma/contact/poles/prime, is a second implementation with materially DIFFERENT analytical decomposition. For J=2 it agrees within the new fully paid action error on P1-P1, P1-P5, P5-P5, P2-P2, P2-P6, P1-P3. Independent J=8 holdouts additionally test original P3-P7 and P4-P8, which were not part of the first six source checks. Every comparison checks intersection of two outward rational enclosures and fails closed on disagreement.

Hostile source mutations: shift C_inf by +1 or set prime half-density w=0 while pretending the original source remains unchanged. BOTH mutants produce SOURCE-DISJOINT signed pairings on a genuine low P1 trial and are rejected by focused CI. Fake n=6 is rejected by original source stage before any signed operator is constructed. The source analytic method has no nontrivial-zero input.

## 5. Infinite Gamma source-domain closure and two-sided tail (OCR-04)

The exact original real-Gamma primitive Fourier multiplier is

    m_j(xi)=16 xi²/[d_j(d_j²+4xi²)] >=0.

The elementary inequality \(d_j²+4\xi²>=4d_j|\xi|\) gives

    m_j(xi)<=4|xi|/d_j².

Since \(\sum_{j>=0}4/(4j+1)²<=4+\int_0^\infty4/(4t+1)²dt=5\), we obtain the genuine ALL-RUNG DOMAIN theorem

    ||Gamma_inf h||_2 <= 5||h'||_2  for every h in H¹_0(I). (9)

Thus the original zero-extended H¹_0 primitive space sits in the unbounded Gamma operator domain, and the source-signed H_inf h is a legitimate L² vector when the bounded prime/contact/polar channels are added. This is NOT a universal bound on H_inf in L² and does not assert the unrestricted operator commutator [A,Gamma_inf] is defined.

For J>=1, d=4J+1, sum over j>=J yields two independent upper bounds:

    ||Gamma_tail,J h||_2 <= (1/d+4/d²)||h'||_2
      for h in H¹_0(I),

    ||Gamma_tail,J h||_2 <= (2/d²+16/d³)||h''||_2
      for h in H²_0(I).                                    (10)

The second is a genuine O(J^-2) action estimate for our boundary-matched h_i. The code takes the **minimum of these two valid source upper bounds**, not an inferred inverse estimate.

The *other* side of the same true positive Gamma tower can also be retained. From 1/(1+t)>=1-t in the original multiplier and exact integral comparison, for h in H²_0

    q_Gamma,tail,J(h)
      >=a_J||h'||²-b_J||h''||²,
    a_J=2/d², b_J=4/d⁴+64/d⁵.                              (11)

This holds as a QUADRATIC FORM on every finite span of our genuine h_i. The source Gamma tail is independently PSD, hence both the signed matrix from (11) and the zero matrix are legitimate Loewner lowers. If the WHOLE signed (11) matrix is PSD, choose it; otherwise safely choose ZERO. **Do not project the indefinite matrix to its positive part**: positive-part clamping is not automatically a Loewner lower of the original tail. This repairs an early overconservative implementation that could worsen the signed source lower at small J.

## 6. Completed all-low Schur certificate (OCR-05)

Let h_i be the actual H²_0 low-minus-high trials (2), p_i the exact source-rational continuum approximant to H_J h_i, and error \(\epsilon_i=e_{J,M,P}(h_i)+\Gamma_{\mathrm{tail},J}^{\mathrm{action}}(h_i)\). Then the true projected primitive residual has the **all-test** bound

    ||r_c||_2 <= sqrt(c^T M c) + sum_i |c_i| epsilon_i,
    M_ij=<Q_E p_i,Q_E p_j>.                                (12)

All entries of M are exact rational FULL CONTINUUM integrals, not a finite compression. Reflection parity from the ORIGINAL source splits into two independent 2×2 blocks \((i=1,3)\), \((i=2,4)\). Within a block and for any eta>0, Young/Cauchy gives

    ||r_c||² <= (1+eta)c^T M c
          +(1+1/eta)(epsilon_i²+epsilon_j²)||c||².         (13)

The archived source exponential integrator independently evaluates the genuine signed finite-Gamma two-by-two Gram A_J(h_i,h_j) as outward rational intervals from ORIGINAL \`authentic_full_low_entry\` matrix entries, including BOTH polar signs, real Gamma, contact, true prime2 and its half-density. The diagonal matrix of row-summed entrywise interval radii is a valid Loewner uncertainty floor (by 2|x_i x_j|<=x_i²+x_j²).

Combining the true positive Gamma tail (11), inherited high \(\kappa_\pi\), and (1),(13), the source-licensed ENTIRE 2×2 Schur lower is

    S4|parity >= A_J,mid −diag(row_radii)
                   +T_J,selected
                   −(1+eta)/kappa M
                   −(1+1/eta)/kappa (sum epsilon_i²)I.     (14)

All ingredients on the right are EXACT rationals and apply to EVERY real c in the correct parity block. A strict 2×2 matrix PSD test therefore certifies the source S4 for this FIRST window, if it passes. A negative eigenvalue of this conservative lower is **AMBIGUOUS** and does not provide a negative Weil test. The code retains source SHA, fitted coefficients, original signed A_J intervals, actual continuum M, parameter/Gamma errors, valid tail route, and full rational Schur Loewner lower. A 4×4 lower is the direct sum of the two 2×2 parity blocks, not a fabricated off-identity covariance.

## 7. Finite source results, ablations and falsifiers (OCR-06)

Hosted exact SHA-pinned source CI passed on Python 3.10/3.13. The first mathematical instrument produced source J8 block conservative diagonals around -0.0348 to -0.0325. An independent exact source depth ablation at J=4,8,12,16,24 showed the worst diagonal of the valid conservative lower shrinking towards zero; at J24 on the initial one-correction response the worst was about -0.00126. These are valid LOWER bounds, not the actual values of S4.

The all-source CI also ran the first multimode response ablation (one/two/three lawful clamped corrections per low mode). Some extra high packets reduced \(\langle Q_E p,Q_E p\rangle\), but increased the true H² Gamma-tail action norm and could WORSEN the certified signed lower. This **refutes** the shortcut "more high modes or a lower fitted finite residual necessarily improve the genuine signed S4 certificate". The independent Gamma-tail quadratic lower and H¹/H² action selector are now retained to measure this tradeoff accurately rather than double-counting nominal and error norm.

The multilevel response solver minimizes the ACTUAL CONTINUUM rational surrogate residual with explicit genuine Gamma H²-tail regularization; it is not fitted to presumed zeta zero coordinates. Coefficients are rounded to exact denominator 4096 and re-evaluated on the original signed matrix separately; this is model selection, not independent empirical proof. Negative controls include non-SPD fitted Gram, malformed source period/basis, missing or changed source parameter, bad H² endpoint trace, incorrect Gamma shell, bogus no-Gamma-tail claims, fake composite6 and missing half-density/contact. Positive controls include original Legendre mixed source moment holdouts and finite exact variational identities.

**HARD BOUNDARY:** The sign of the TRUE completed original S4 at a=1/2 remains OPEN in all current exact tested source instruments. No claim of an RH proof, Weil global PSD, complete zero-free spectrum or a completed Suzuki operator diagonalization is made. The source-level original completed Weil distribution exists by the imported Tate/Weil theory; positivity is its unsolved condition.

## 8. Verdict-changing next probes

1. **Source-specific high-response inverse:** compute or bound a larger original continuum projected residual on true low/high columns using analytically separated exp-polynomial OU boundary layers to allow far deeper J without huge Taylor degree; audit exact original source comparisons on fresh high modes and withheld J.
2. **Sharp non-scalar high coercivity:** replace global scalar 1/kappa with a true original-source spectral/directional Douglas/Riesz inverse bound on the *actual residual*, retaining the prime-2 edge mismatch and completed polar/contact response. A nice finite PSD does NOT imply such an all-high form inequality.
3. **Adaptive source tail form:** use true Gamma \(m_J(\xi)\), exact low/high frequency-decomposition and rigorously calibrated polynomial source-frequency moments to bound action more sharply than a universal τ_J||h''|| in trial families that push weight to high Legendre indices.
4. **Optimal Schur-direction selection:** search among source-valid boundary-matching trials to maximize authenticated S4 lower, rather than minimize only the finite approximation residual; keep fitted selection and independent holdout/source test disjoint.
5. **Domain/formal audit:** independently reproduce (3)–(14), the m_\Gamma<=5|xi| domain closure, source pin and signed polar orientations with a separate mathematical implementation. Current tests have multiple arithmetic decompositions but no formal Lean proof of the continuous spectral statements.

### Provenance and claim ledger

| Claim | Status | Boundary |
|---|---|---|
| OCR-01 original Legendre boundary-matched H²_0 affine high trial | PROVED EXACT POLYNOMIAL | All low index 1..4, high moment source Q4, endpoints verified |
| OCR-02 Taylor absolute moments and entire signed primitive action with controlled error | PROVED PAPER/EXACT RATIONAL + SOURCE-AUTHENTICATED | Bounded J,M; no spatial quadrature |
| OCR-03 six + two high unfitted original Suzuki exp-source interval holdouts | VERIFIED ORIGINAL SOURCE, two independent implementations | May share SOURCE frozen SHA; method diversity not independent input source |
| OCR-04 original Gamma∞ domain m<=5|xi|, dual action tail and positive-tail quadratic lower | PAPER PROVED, exact source arithmetic | Needs original single real Γ and endpoint trace hypotheses |
| OCR-05 entire 4-low/2-parity source Schur Loewner lower on full high test carrier | PAPER FORM/EXACT RATIONAL SOURCE-CONDITIONAL | Uses inherited WB4 high coercivity; lower negativity AMBIGUOUS |
| OCR-06 multi-corrector ablation falsifying naive "more fitted modes always better" | OBSERVED IN EXACT SOURCE CERTIFICATES | Not general no-go for better nonlocal trial spaces |
| Certified completed original S4>=0 or RH | UNVERIFIED/OPEN | No source-valid positivity achieved |

The authoring branch is review-only. No original source blob, main, merge, publication or release changed.

**Canonical external primary reference** Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (2026-09-23), https://arxiv.org/abs/2606.09096 . Source comparison and competing normalization claims are never treated as proof of the original Weil sign.