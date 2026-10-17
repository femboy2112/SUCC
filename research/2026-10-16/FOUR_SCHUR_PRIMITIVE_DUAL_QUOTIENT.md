# SUCC original Weil four-mode Schur: primitive-dual quotient, authentic trial bounds and falsifiers

**Date:** 2026-10-16. **Branch:** `research/dual-variational-schur-source-gates-2026-10-16`. **Parent:** PR #149 head `8a65f0bb5babb6be625059b81d63824c4526234b`; previous Academic Main II main `07806f307ae6e2f62f9c0faa90377bf79cee1cc0`. **Status:** PROVED PAPER / exact rational model for structural theorems; source-dependent application conditional on WB4 and original source cancellation certificates. **RH PROVED: NO.**

## Problem and steelman

Prior CertifiedTrial correctly refused to assert the false contraction
`||(Q_4 h)'|| <= ||h'||` for an L2-Legendre projection Q4. Consequently its rigorous lower Schur bracket was independent of trial response U. We reconstruct the strongest valid statement by using the actual variational dual pairing against **high w**, not differentiating Qh. This creates an exact finite source-independent mathematical map suitable for a source-specific certified bracket. We do not invent or move a zeta zero, replace signed Weil by a positive covariance, or assume a bounded inverse of the compact high block.

## PDQ-01. The primitive image of the genuine high subspace (PROVED, classical density machinery)

Fix a>0, I=(-a,a), H=L²₀(I), V:H→H¹₀(I), `Vw(t)=int_{-a}^t w(s) ds`. Let F4 be the span of the first four nonconstant Legendre modes and Q4 the L² orthogonal projection to H_high=F4^⊥ in H. Let P3 be the L² orthogonal projector onto ordinary polynomials of degree <=3 on I. Then

\[
\boxed{\overline{V(H_{high})}^{L²(I)}=\ker P_3.}\tag{PDQ1}
\]

For w∈H_high and j=0,1,2,3, integration by parts and Vw(±a)=0 give
`int t^j Vw = -int t^{j+1}w/(j+1)=0`, because w has vanishing moments of degrees 0..4. Conversely, for every compact smooth φ whose moments degrees 0..3 vanish, w=φ′ lies in H and is orthogonal to Legendre modes 1..4, because `int φ′ P_k= -int φ P_k′=0`; Vw=φ. Such φ are dense in ker P3: approximate any polynomial-orthogonal L² function by smooth compact functions, then correct its four moments using four fixed compact smooth bumps whose moment matrix is invertible. Existence of those bumps follows from nondegeneracy of the four polynomial functionals on C_c∞ (e.g. disjoint small supports centered at four distinct points, close to Vandermonde).

## PDQ-02. Exact inverse-Neumann high residual dual energy (PROVED)

If h∈H¹(I), r=Q4 h and K=V*V, then

\[
\boxed{
 \sup_{w\in H_{high}\setminus0}\frac{|\langle r,w\rangle|²}{\langle Kw,w\rangle}
 =\|(I-P_3)h'\|_{L²(I)}².}\tag{PDQ2}
\]

Here K is restricted only as a quadratic form to H_high; no inverse operator is asserted on the whole L². Integrating by parts gives `⟨Qh,w⟩=⟨h,w⟩=−⟨h′,Vw⟩` with `⟨Kw,w⟩=||Vw||²`. PDQ1 and Hilbert projection give the exact supremum.

**Crucial distinction**: this is **NOT** the generally false identity `||(Qh)'||²=...` and does not require `Qh∈H¹` as its route to the estimate. The quotient derivative is `((I-P3) h')`, not `(Qh)'`.

### Rational countermodel to derivative contraction

On (-1/2,1/2), take `h=P5(2t)-P3(2t)`. Then `Q4 h=P5(2t)`, while Legendre differentiation gives `h′=18P4(2t)`. Since `||P4(2t)||²=1/9`, the full derivative energy is 36. But `||(Q4 h)'||²=60`, factor 5/3 larger. The correct high K-dual energy of Qh is `||(I-P3)h′||²=36`. This explicitly refutes the `H¹` contraction shortcut while validating PDQ2 by a different route. Independent symbolic Legendre integration is a useful second check; the exact rational constants are also pinned in standard-library-only tests.

## PDQ-03. Source-specific U-dependent low Schur bound without projected-derivative tails (PROVED CONDITIONAL)

Let G be the **original** even anchored Suzuki convolution operator on meanzero H, and assume the authentic upstream first-window source `||g′||_{L¹(-1,1)} < c=11/40`. Let `D=Q4 G Q4 ⪰ κ Q4 K Q4` with κ=1/50 (WB4). For **any** finite rational parity-preserving response U:F4→H_high, set

`v_x=x−Ux`, `r_U x=Q4 G v_x`, `L_U=U*B+B*U−U*DU`, `M_U(x)=⟨G v_x,v_x⟩`, `N_U(x)=||v_x||²`.

For w∈H_high, `⟨r_U x,w⟩=⟨Gv_x,w⟩=−⟨(Gv_x)′,Vw⟩`. In the original source, derivative of the meanzero-projected convolution is convolution with g′; Young therefore gives `||(Gv_x)′|| ≤ c||v_x||`. The duality, `D>=κK`, and completing the square yield

\[
\boxed{M_U-\frac{c²}{κ}N_U \preceq S_4 \preceq M_U,
\quad\frac{c²}{κ}=\frac{121}{32}.}\tag{PDQ3}
\]

No derivative norm of Qh appears, and no high Legendre tail is silently dropped. Because v_x is low-minus-high, `N_U=W_low+U*U` in the correct L² mass metric. The full `M_U=A4−L_U`. For U=0 this reproduces exactly the inherited low floor `A4−121/32 W_low`; for nonzero U it is a rigorously U-dependent lower bracket.

**Honest limitation / no free gain:** relative to the U=0 Young floor, the improvement operator is

\[
\boxed{(M_U-c²N_U/κ)-(A_4-c²W_{low}/κ)
      =-L_U-(c²/κ)U^*U.}\tag{PDQ4}
\]

Thus if `L_U ⪰ 0`—as for an effective trial approximating the positive high response—the new source-only Young floor cannot improve the original U=0 lower bound; it becomes weaker. **This is a theorem-based limitation**, not a failure of numerical precision. The new bound is useful as a typed baseline, sanity check and a gateway to the quotient-moment refinement below, not a proof of first-window positivity.

At Gamma depth J, the parent original-source interval block and positive omitted true Gamma tail give `M_{U,J} ⪯ M_U ⪯ M_{U,J}+τ_J N_U`. If the symmetric interval entries of M_{U,J} have exact rational mid and a Gershgorin row-sum radius e, then the explicitly certifiable Loewner pair is

\[
\boxed{
  (mid-eI)-(121/32)N_U\preceq S_4
  \preceq(mid+eI)+\tau_J N_U.}\tag{PDQ5}
\]

The upper is already present in `certified_four_schur_trial`. The lower is the additional **source-verified U-dependent** alternative. It may be weaker than the inherited U=0 floor, so preserve BOTH, never manufacture a matrix maximum, and use either only if it separately certifies the desired sign. Convex rational combinations of two certified lower forms are also valid but cannot establish a sign unless the combination is rigorously checked.

## PDQ-04. The EXACT derivative polynomial-quotient improvement (PROVED; FULL FOUR SOURCE MOMENTS NOT YET ATTESTED)

Define h_i=G(e_i−Ue_i) in H¹(I) for i=1..4 and let `E_{ji}=int_{−a}^a t^j h_i′(t)dt` (j=0..3), a `4×4` derivative-moment matrix. Let `P_{jk}=int_I t^{j+k}dt`, the **positive definite exact rational polynomial Gram**.

From PDQ2, the residual dual Gram is exactly

\[
\boxed{R^{dual}=H' - E^*P^{-1}E,\qquad
H'_{ij}=\langle h_i',h_j'\rangle.}\tag{PDQ6}
\]

Thus a certified upper bound `H'⪯c²N_U` and a **separately authenticated** derivative-moment matrix E give

\[
\boxed{S_4\succeq M_U-κ^{-1}(c²N_U-E^*P^{-1}E).}\tag{PDQ7}
\]

This **does** potentially improve the U=0 floor, depending on exact source moments. No tail in the high *Legendre derivative coefficients* is required to state or prove this quotient formula. The remaining full-moment work shifts to certifying all four rows of E, while PDQ-04b below source-certifies two endpoint-vanishing polynomial combinations and, ideally, improving `H'` beyond its global Young upper. For polynomials the exact moments obey, with a=1/2:

- E_0=h(a)−h(−a),
- E_1=a[h(a)+h(−a)]−int h,
- E_2=a²[h(a)−h(−a)]−2 int t h,
- E_3=a³[h(a)+h(−a)]−3 int t² h.

Since Gv is in the meanzero carrier, `int h=0`. The other interior integrals can be read from authentic low Galerkin source entries; the **remaining full source endpoint values still require a new certified source evaluation**, for example exact polynomial-exponential integrals of g_J(a−s)v(s), with certified g−g_J tails. Arbitrary numeric E data must NOT be used in a signed Weil certificate. Future `CertifiedTrial` should consume source-attested E, not a caller's Boolean claim of authenticity.

The source-neutral module `four_schur_dual_quotient.py` implements P, exact inverse, exact projection Gram and source-consistency rejection `c²N−E*P⁻¹E ⪰ 0`. It explicitly says a supplied moment matrix is **not** source-authenticated. Fast exact tests exercise counterfeits, projections, parity and a strictly smaller quotient bound on synthetic models.


## PDQ-04b. Two real source-CERTIFIED derivative-moment channels without endpoint data

At a=1/2, choose the even/odd polynomials

\[
\phi_e(t)=t^2-\tfrac14,\qquad \phi_o(t)=t(t^2-\tfrac14).
\]

Both vanish at the endpoints, are mutually orthogonal and have EXACT rational norms

\[
\|\phi_e\|_2^2=\tfrac1{30},\qquad \|\phi_o\|_2^2=\tfrac1{840}.
\]

For h_i=G(e_i-Ue_i), integration by parts gives

\[
\langle h_i',\phi_e\rangle=-\langle P_1(2t),h_i\rangle=-c_{1i},
\quad
\langle h_i',\phi_o\rangle=-\tfrac12\langle P_2(2t),h_i\rangle=-\tfrac12c_{2i}.
\]

Therefore the degree<=3 polynomial projection energy dominates

\[
\boxed{\quad \|\Pi_{\le3}h_x'\|^2\ge x^T(30c_1^Tc_1+210c_2^Tc_2)x.\quad}\tag{PDQ8}
\]

These c1,c2 rows are genuine completed signed Suzuki **low Galerkin rows already authenticated** in the parent source. They preserve true prime2, Gamma parity, half-density, contact and both poles. No unknown endpoint values are needed for this two-dimensional subprojection.

For the finite-J original Gamma stage, c_ji(J) is a sum of authenticated G_J matrix intervals. The omitted authentic Gamma operator has \|G-G_J\|_op <= tau_J, and for every trial input vector v_i one has

\[
|c_{ji}-c_{ji}^{(J)}|
\le\tau_J\|P_j\|_2\|v_i\|_2
\le\tau_J\sum_m|V_{mi}|.\tag{PDQ9}
\]

Use this exact rational error plus the finite-J source interval radius. If a row c belongs to the componentwise box m±e, then for 0<eta<1,

\[
cc^T\succeq(1-\eta)mm^T-(\eta^{-1}-1)\|e\|_2^2 I.\tag{PDQ10}
\]

The proof is the exact scalar square identity (A+B)^2 >= (1-eta)A^2 -(eta^-1-1)B^2, plus |delta·x|^2 <= \|e\|^2 \|x\|^2. Weight the first row by 30 and the second by 210; call the resulting Loewner lower P_van,lo. This matrix can be indefinite: do not clamp its negative part or treat it as a positive source substitute.

Combining the primitive-dual variational theorem and the source moment projection yields an actual source-certified third lower:

\[
\boxed{\quad S_4\succeq (M_{U,J}^{mid}-r_JI)-
(121/32)N_U+50P_{\mathrm{van,lo}}.\quad}\tag{PDQ11}
\]

The authenticated CertifiedTrial implementation now reports its source rows, rational error bounds, moment Loewner correction and third lower matrix, and uses that lower to issue a POSITIVE verdict only if both parity blocks are rigorously PD.

**Open:** source authenticity of the remaining two polynomial derivative moments requiring endpoint evaluations; a sharper source-specific upper bound on the full differentiated convolution energy H'; and the sign of the original S4. The addition is a real original-source-information correction, NOT a claim of global Weil positivity. Independent SymPy polynomial integration confirmed the exact norms 1/30 and 1/840 and the low-channel pairings.


## PDQ-05. Correctness constraints and remaining gate

- Strict positive source `D>=K/50` is NOT an ordinary L² spectral gap and K⁻¹ is not asserted bounded.
- The full signed Weil distribution is **already classically identified** (CTW-08); its positive factorization remains OPEN.
- The exact source supports only the prime 2 in the first window; the original Γ_R parity, both poles, contact and half-density are preserved by parent source entry routines.
- The stronger thirty-mode κ_30 cannot simply be inserted into κ_4 (the middle 26 signed modes survive); the nested short is lawful only with its genuine middle response and error.
- **No a priori sign of S4 is obtained from PDQ3–7.** In particular PDQ4 explains why global L1 Young constants cannot by themselves extract the cancellation of a near-optimal response U.
- Precision gates should distinguish a request from an actual certified radius: a reported `precision` without an achieved bound is not a fulfilled request.

### Next falsification and execution

1. Replay source gate and U0 under #149: old and new lower must be identical for U=0. For nonzero U, new lower must be exactly mid−eI−(121/32)N_U, and both bounds independently source-certified.
2. Build a second source interval endpoint evaluator for `h_i(a),h_i(-a)` and verify it against direct, independent high-precision diagnostics (diagnostics never certificates). Then construct E and PDQ7, classify whether actual moment subtraction improves the old lower bound.
3. Challenge every claimed improvement on the Legendre `P5−P3` countermodel and on fake prime6/wrong Γ/contact controls; refuse a forged E matrix even if its algebraic PSD checks pass.
4. If moment subtraction is inadequate, target the full differentiated convolution energy `H'`: compute exact finite-J exponential-polynomial integrals and a rigorous L1 gamma derivative tail, or a source-adapted energy inequality. A certified per-U residual Gram needs these source-derived inputs.

**No academic priority claimed for classical Hilbert orthogonal-projection, Schur/Douglas, or Sobolev duality. The source-indexed composition and countermodel are new-to-repository. RH PROVED: NO.**

## PDQ-06. An exact gate for 30→4 nested Schur transport (PROVED FINITE / original S30 NOT built here)

Suppose H=F₄ ⊕ M₂₆ ⊕ H_{≥31} and a separately source-certified **finite** 30-mode selfadjoint effective packet obeys `L30 ⪯ S30 ⪯ U30` in Loewner order on F₄ ⊕ M₂₆. If the compression of **L30** to M₂₆ is **strictly PD**, then its two-stage Schur forms satisfy

`Short_F4(L30) ⪯ Short_F4(S30) ⪯ Short_F4(U30)`.

Proof: the middle compression of S30 and U30 is also strictly PD. For each fixed x∈F4, the Schur quadratic `Short_F4(M)(x)` is the **infimum** over y∈M₂₆ of the quadratic form `⟨M(x+y),x+y⟩`. Infimum preserves ordered forms. Classical Haynsworth transitivity then identifies `Short_F4(S30)` with the original S4 **when** the correct variational domains and source identification are separately proved. This gate is not a routine inversion of the original infinite high block.

**Failure of indiscriminate monotone shorting:** `L=[[0,1],[1,-1]]`, `U=[[0,1],[1,1]]` obey `L⪯U` (difference diag(0,2) PSD), yet the scalar shorts are `Short(L)=+1 > -1=Short(U)`. The discarded block switches from negative to positive, so one is a supremum and the other an infimum; Loewner order does not survive this invalid operation. Source packets whose *lower* discarded compression is not PD must refuse the claimed nested bound, rather than invert an indefinite matrix and forge a sign.

`nested_schur_envelopes.py` and its seven independent Fraction tests implement the finite conditional gate and the reversal control. The pure module carries `original_source_identified=False` because no 30-mode original source interval packet was constructed here. The genuine modes 5..30 are within the four-mode high subspace, where source relative coercivity is inherited, **but one must still certify the finite effective middle response after shorting modes ≥31**; κ30 alone gives no quantitative protection of the intermediate correction.

**Next task:** construct and authenticate original-source 30×30 effective intervals `L30,U30`, including the high-response and positive discarded-compression margin, before trying to transport them to S4. A finite exact toy matrix is neither such a source packet nor RH evidence.
