# Infinite genuine Gamma tower: Carleman boundary and test-form convergence

**Date:** 2026-10-18. **Base:** first-prime Gamma boundary PR #170 at d479e5007cb253facf77b6926547b2d490f21fd4. **Immutable signed Suzuki source blob:** 0cc8510b71d178fc79e8d410a86d8b6014cf9178. No nontrivial zero data, fake composite impulses or altered source coefficients. **S4 OPEN, RH PROVED: NO.**

## 1. Actual source and operator-domain distinction

Take I=(-1/2,1/2), b=log(2) in (5/8,3/4), the genuine prime-two compressed symmetric shift A=P(T_b+T_-b)P on L2(I), where T_b f(x)=f(x-b). The original real-Gamma rungs are G_j=4/(4j+1)I-E_j, where E_j has restricted OU kernel exp(-alpha_j |x-y|), alpha_j=(4j+1)/2. Each G_j is nonnegative in the original primitive quadratic form. For finite J let Gamma_J=sum_(j<J) G_j, and D_J=[A,Gamma_J]=-sum_(j<J)[A,E_j]. From PR #170 every summand is skew, of rank exactly four, and splits into even/odd rank-two wedges.

The *complete* Gamma operator is unbounded and defined via monotone forms. This paper DOES NOT assume A preserves its operator domain. We define the infinite boundary anomaly as the STRONG limit of these already lawful finite bounded commutators. It is not automatically identified with an unrestricted composition [A,Gamma_infinity] of unbounded operators.

## 2. Exact infinite sum and corner geometry (IGC-01)

The source shell spacing is exactly alpha_(j+1)-alpha_j=2, hence for s>0

    K_J(s)=e^(-s/2)*(1-e^(-2Js))/(1-e^(-2s))
    K_inf(s)=e^(-s/2)/(1-e^(-2s))
    K_tail,J(s)=e^(-alpha_J*s)/(1-e^(-2s)).

By exp(-s/2)>=1-s/2, 1-e^(-2s)<=2s, and 1/(e^(2s)-1)<=1/(2s),

    1/(2s)-1/4 <= K_inf(s) <= 1/(2s)+1.         (A)

In fact K_inf(s)=1/(2s)+1/4+O(s) as s tends to zero. The 1/2 is not a free parameter: it is the reciprocal of the true rung step TWO. A mutant step four has coefficient 1/4 and fails source calibration.

Let L=(-1/2,1/2-b), C=(1/2-b,b-1/2), R=(b-1/2,1/2); put ell=1-b>1/4 and c=2b-1>1/4. The complete boundary commutator kernel is the negative of the parent one-rung commutator kernel with exp(-alpha_j s) replaced by K_inf(s). On R x C use coordinates u=1/2-x and v=y-(1/2-b), giving K_inf(u+v). The three other singular blocks C x R, L x C, C x L are signed/adjoint reflected copies. The displaced-diagonal source singularities cancel in the ORIGINAL coefficient difference; do not assign a value at the cancelled point. Remaining L x L and R x R terms have positive argument at least c and bounded, smooth kernels; L x R and C x C have no contribution.

## 3. Bounded strong limit (IGC-02)

Consider the classical Carleman integral H f(u)=integral_0^infinity f(v)/(u+v) dv on L2(R+). Under the unitary logarithmic change f(e^t) -> e^(t/2) f(e^t), H becomes convolution with h(t)=1/[2 cosh(t/2)] whose L1 norm is pi. Hence H is bounded with norm pi; long normalized logarithmic plateaus show sharpness.

By (A), each actual edge-center kernel K_inf(u+v) equals 1/[2(u+v)] plus a uniformly bounded Hilbert-Schmidt kernel on a finite rectangle. Therefore each is bounded; other edge-edge pieces are Hilbert-Schmidt. Thus the whole D_inf is a bounded skew-adjoint L2 operator.

Since 0<=K_J<=K_inf pointwise for the genuine positive kernel, every finite boundary block is uniformly operator bounded by its complete positive-kernel block. On input functions supported away from the singular corner the kernels converge in L2 by dominated convergence. Density plus uniform boundedness gives

    D_J -> D_inf STRONGLY on L2(I).             (B)

The infinite Gamma operator itself is NOT thereby shown bounded.

## 4. Sharp Carleman obstruction, each reflection sector (IGC-03)

For a small fixed delta less than both ell and c/3, isolate the two singular corner squares (0,delta)x(0,delta) in the edge-center blocks. Outside them 1/(u+v) is bounded on finite rectangles; those contributions are compact Hilbert-Schmidt operators. The two corner squares attach to DISJOINT center endpoints and DISJOINT edge endpoints, hence modulo compact operators the boundary anomaly is the direct sum of two skew Carleman cross-channel operators.

Each channel has norm at most pi/2, by the Carleman L2 bound. To attain the essential norm, use weakly null normalized logarithmic plateaus, supported nearer and nearer the corner, with plateau lengths tending to infinity. Their transformed Carleman convolution norm tends to its L1 mass pi/2. Any compact perturbation vanishes on weakly null packets. The reflected even/odd combinations provide the same sharp lower in each parity sector. Therefore

    ||D_inf||_essential = pi/2,
    ||D_inf|even||_essential = pi/2,
    ||D_inf|odd||_essential = pi/2.              (C)

These are ESSENTIAL norms: compact smooth remainders can increase the ordinary operator norm.

Every finite D_J has rank at most 4J, hence compact, so (C) implies the decisive NO-GO

    ||D_inf - D_J||_(L2 -> L2) >= pi/2
    for every finite J.                       (D)

The tower is strongly complete but NEVER finite-rank operator-norm convergent.

An entirely rational alternative gives an independent weaker but strict bound, with no pi, Mellin transform or numerical spectrum. Set delta_J=1/[32(J+1)] and take normalized indicators 1_[delta_J,2delta_J]/sqrt(delta_J) in a genuine edge-center corner. Since K_inf(s)>=1/(2s)-1/4 and K_J(s)<=J, on the source-licensed delta-square, s<=4delta_J, and

    <f,(K_inf-K_J)f> >= 1/8 - delta_J*(J+1/4)
                     >= 3/32.                 (E)

This exact rational analytic certificate refutes the norm-convergence shortcut independently of the sharp Carleman analysis.

## 5. H1_0 source-test-domain RESCUE with rate (IGC-04)

The real source primitive test space contains F=Vu in H1_0(I). If F,G belong to H1_0(I), source endpoint zero traces make the four singular corners better behaved in bilinear form topology.

Set t=alpha_J=(4J+1)/2. The omitted genuine kernel obeys

    K_tail,J(s) <= e^(-ts) * [1+1/(2s)].

On each edge-center corner, one test (say F) is evaluated at distance u from a PHYSICAL endpoint, where |F(u)|<=sqrt(u)*||F'||_2, while the other center test satisfies |G(v)|<=||G'||_2 (interval length one). Extend both integrations to the positive quadrant. Exactly,

    integral_du_dv sqrt(u)e^(-t(u+v))*(1+1/[2(u+v)])
       = sqrt(pi)/(2*t^(5/2))+sqrt(pi)/(6*t^(3/2)).

Sum the FOUR source corners. The FOUR bounded same-edge terms have shift argument s>=c=2b-1, area <=ell^2 each, and contribute at most 4ell^2 e^(-tc)(1+1/(2c)). Thus

    |<F,(D_inf-D_J)G>|
      <= B_J ||F'||_2 ||G'||_2, where
    B_J = (2sqrt(pi)/3)*t^(-3/2)
          + 2sqrt(pi)*t^(-5/2)
          + 4ell^2*e^(-tc)*(1+1/(2c)).         (F)

In particular this original-source interface converges as O(J^(-3/2)) in H1_0 x H1_0 dual bilinear-form norm, even though it does not converge in L2 operator norm.

A fully RATIONAL, deliberately conservative CI-checkable bound uses sqrt(pi)<2, ell<3/8, c>1/4, e^(-t/4)<=8!*4^8/t^8, and a certified rational lower r_t<=sqrt(t):

    B_J <= (4/3)/(t*r_t) + 4/(t^2*r_t)
           + (27/16)*8!*4^8/t^8.               (G)

The code checks rational t, integer-square-root enclosure, and strictly decreasing budgets at independent J. No numerical zero ordinates or artificial Gamma normalizations are used.

## 6. Limitations: still not a signed-S4 certificate

1. D_inf is skew-adjoint, so its real quadratic diagonal is identically zero. It measures mode transport mismatch, not source-positive energy.
2. Formula (F) depends on ||F'|| and ||G'||, which are NOT uniformly controlled by the K-relative high-sector norm ||F|| alone. The original full signed S4 high-resolvent requires a separate genuine source-domain transport theorem.
3. The sharp indicator witnesses for noncompactness are L2, not lawful H1_0 eigenmodes. The H1 estimate is a separate result, not an escape from (D).
4. A nonzero commutator limit of bounded truncations is NOT automatically the operator commutator with unbounded Gamma_infinity; common operator domains are unpaid.
5. The original prime shift, half-density, C_infinity contact, and BOTH completed poles are unchanged. This paper proves an authentic Gamma boundary interface, NOT full signed Weil positivity or the Riemann hypothesis.

## 7. Claim ledger and verification

| Claim | Status | Evidence / falsifier |
|---|---|---|
| IGC-01 exact genuine infinite Gamma kernel, leading coefficient 1/2 | Classical algebra + rational interval independent oracle; fake rung spacing control |
| IGC-02 bounded skew strong L2 limit | PAPER PROVED using Carleman, dominated convergence, source-specific corner geometry |
| IGC-03 essential norm exactly pi/2 in both parity sectors | PAPER PROVED with Mellin + compact cutoffs; independent rational >=3/32 no-go |
| IGC-04 H1_0 x H1_0 tail O(J^-3/2) | PAPER PROVED with endpoint traces; exact rational majorant regression |
| IGC-05 authentic source-index spacing and finite recursive prefix | Lean 4.14 FINITE KERNEL only; exact rational Python checks the closed geometric ratio; Carleman NOT formalized |
| Entire unbounded operator commutator identity | UNVERIFIED; not assumed |
| Authentic source S4 positivity / all-radius Weil / RH | OPEN; RH PROVED: NO |

Hostile controls: wrong SHA, fake composite n=6, altered alpha step 4, invalid rounding/floats, non-H1 vectors passed to H1 estimate, any claim of norm convergence, full-tower finite rank, Gram positivity from a skew commutator, or use of zero positions.

**Next verdict-changing task:** transfer the H1 boundary control through the actual high-response Douglas/Riesz domain and quantify a source-signed S4 change, or produce a counterexample showing the derivative-space bound is insufficient. Full source Gamma/prime/pole/contact inputs remain mandatory.

**Prior art:** Carleman norm and spectral Mellin representation are classical (Pushnitski/Yafaev 2015, https://doi.org/10.1016/j.jfa.2014.12.005; https://link.springer.com/article/10.1007/s13373-013-0044-0). A separate originality literature audit is required before any academic priority claim for the SUCC-specific source embedding.