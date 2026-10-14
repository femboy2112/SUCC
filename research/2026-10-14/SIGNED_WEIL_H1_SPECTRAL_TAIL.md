# SIGNED WEIL / H¹ — Source-Gaussian Jensen zero density and an all-test signed spectral tail

**Source pin:** SUCC `research/xi-complex-contour-weil-residue-2026-10-14`, commit `bb5b6f96f78df0d9472a60441501024e0e2b904e`, draft PR #82. Its ancestors include the source-faithful theta-completion and finite rational jet proof. This checkpoint is a *sibling* of contour PR #83, which is independently read and not merged. 

**Claims:** classical Jensen/Fourier/Weil ingredients with a new-to-project source-specific quantitative combination and an all-`H₀¹` domain repair. **RH PROVED: NO.** No nontrivial zeta zero *positions* enter a construction. Spectral zeros in the classical Weil equality are summation indices, **not oracle inputs**. Physical-carrier authenticity and independent scholarly novelty not claimed. Main and source archives untouched.

## 0. Steelman, acceptance, and the signed/no-ghost boundary

The user's requested result is *not* another positive finite Gram matrix and not merely a stronger first-zero contour. We seek a uniform operator/form-norm upper bound for the signed Weil spectral contribution from **all unknown nontrivial zeros at heights `|Im ρ|>T`**, with the genuine arithmetic completed Weil distribution fixed, off-critical zeros permitted, and precise Suzuki test domain. Passing the test means `sup_(||v||H¹=||w||H¹=1)|R_>T(v,w)|→0` with a **proved, computable** modulus, and a separate honest finite-height decomposition.

The established Weil spectral/source identity is an **external classical theorem**: on `C_c^∞(R)`, for `h=v*\widetilde w`,

    Q_W(v,w) = W(h) = Σ_(ξ(ρ)=0) A_v(ρ) * conjugate(A_w(1-conjugate(ρ))),
    A_v(s) = ∫_R v(x) exp((s-1/2)x) dx.                           (ST-0)

All zeros are counted with multiplicity. Critical zeros contribute nonnegative `|A_v(ρ)|²` on the diagonal; off-line paired zeros can contribute negative signs. This equality has the **original** prime powers Λ(n)/√n, full real-place Gamma/contact, pole distribution, conductor/half-density normalization. It is NOT inferred from a Gaussian covariance or positive moment Gram. Primary: Masatoshi Suzuki (2026 v3), arXiv:2606.09096, introduction (Weil functional, (1.1)–(1.8)); earlier classical Weil explicit formula. We never substitute an auxiliary χ₄ or Markov form.

Fix a>0, `v,w∈C_c^∞(-a,a)` (real or complex). The localized Suzuki compact-kernel representation `Q_W^a(v)=<G_a i v',i v'>` is an established equality on `H₀¹(-a,a)`; `G_a` is bounded on the derivative variable because its continuous kernel is restricted to a compact square. The classical zero-side identity is initially asserted only on the smooth core, with extension to `H₀¹` proved below. This does *not* identify the full (larger) closed form domain with H¹.

## 1. ST-01: source-only order-one growth and absolute zero count (PROVED LOCAL; Jensen classical)

Let `F(z)=ξ(1/2+z)` with the classical normalization `ξ(s)=s(s-1)π^(-s/2)Γ(s/2)ζ(s)/2`. SUCC PR #73/74 reconstructs this exact source from the integer Gaussian theta:

    F(z)=1/2 + (z²-1/4)B(z),
    B(z)=∫_1^∞ ψ(t)t^(-3/4)cosh((z/2)log t)dt,
    ψ(t)=Σ_(n>=1)e^(-πn²t).

The authentic source gives for t≥1: `0<ψ(t)<2e^(-3t)` (as π>3). Also `F(0)=ξ(1/2)>59/120`; this is a *source-derived lower bound*, not a lookup of zeros. For `R=|z|≥1`:

    |B(z)| <= 2∫_1∞e^(-3t)t^(R/2)dt.

Split `e^(-3t)=e^(-3t/2)e^(-3t/2)`. Elementary one-variable calculus proves `sup_(t≥1)[t^(R/2)e^(-3t/2)]≤(1+R)^(R/2)` (the unrestricted maximum is at t=R/3 if R≥3, and the t=1 boundary applies otherwise). Thus

    |B(z)| <= (4/3)e^(-3/2)(1+R)^(R/2)
             < (4/3)(1+R)^(R/2).

Hence the entire authentic function satisfies

    |F(z)| <= 3(1+R)^(R/2+2), R≥1.                          (ST-1a)

This improves the previous Gaussian-Fock `exp(R²/8)` growth envelope to an **order-one** `exp(O(R log R))` bound, using only the same original source. Nothing about RH is assumed.

Apply Jensen's formula at center z=0, radius `2r`, to the entire function F with F(0)≠0. For r≥1, with radial zero count `n_F(r)` (multiplicities):

    n_F(r)log2 <= log max_(|z|=2r)|F(z)| - log|F(0)|
                <= log 3 + (r+2)log(1+2r) + log(120/59).

Use exact inequalities `log2>2/3`, `log(360/59)<2`, and `(r+2)log(1+2r)>2` for r≥1 to get

    n_F(r) < 3(r+2)log(1+2r).                             (ST-1b)

Every zero of ξ lies in the **closed critical strip** `0≤Reρ≤1`; this is classical and does not require RH. Thus a zero with `|Imρ|≤t` has shifted radius `|ρ-1/2|≤t+1/2`. For t≥2, `r=t+1/2`, and `r+2≤9t/4`, `1+2r≤4t`. Therefore the **total** count at both positive and negative heights obeys

    N_abs(t) := #{ρ : |Imρ|≤t} < 7t log(4t), t≥2.           (ST-1c)

This count includes multiplicities. It is deliberately weaker than classical Riemann–von Mangoldt/Rosser estimates, but is **proved from source-Gaussian theta + elementary Jensen** rather than taking zero-density input or zero coordinates from an external oracle. It is a finished finite-to-global source interaction bound, not a statement inferred from numeric samples.

## 2. ST-02: unconditional dyadic absolute spectral mass (PROVED LOCAL)

For any real T≥2 and integer m≥1, put `q=2^(1-2m)`. Partition the unknown zeros into dyadic shells `2^jT<|Imρ|≤2^(j+1)T` and use (ST-1c) *at the upper endpoint* of each shell. Since the total count in a shell is no greater than the count up to that upper endpoint,

    Σ_(|Imρ|>T) |Imρ|^(-2m)
    ≤ 14 T^(1-2m) [log(8T)/(1-q) + (q log2)/(1-q)^2].     (ST-2a)

In particular for m=1 this simplifies EXACTLY to

    Σ_(|Imρ|>T) |Imρ|^(-2) ≤ 28 log(16T)/T.               (ST-2b)

Every term is nonnegative in this *absolute* majorant; the genuine Weil terms being bounded may be negative. Note: no enumeration of the rho is performed by code. This is an all-height bound conditional only on the **classical identity of the rho as zeros of the original completed source**, not on the truth of RH.

## 3. ST-03: the signed ALL-H¹ spectral-tail theorem (PROVED LOCAL; essential result)

For `v∈C_c^∞(-a,a)`, any zero `ρ=β+iγ`, `0≤β≤1`, and `|γ|>T≥2`, write `θ=β-1/2`, `|θ|≤1/2`. A single integration by parts gives

    A_v(ρ) = -(iγ)^(-1) ∫_(−a)^a e^(θx+iγx)[v'(x)+θv(x)]dx.

Thus Cauchy–Schwarz yields

    |A_v(ρ)| ≤ [e^(a/2)√(2a)/|γ|] (||v'||₂ + 1/2||v||₂)
             ≤ [e^(a/2)√(5a/2)/|γ|] ||v||H¹.

The same estimate applies to `A_w(1-\barρ)` because its real part is `1-β∈[0,1]`. Consequently every **signed** Weil term is absolutely bounded by

    |A_v(ρ) conjugate(A_w(1-\barρ))|
      ≤ (5a/2)e^a |γ|^(−2) ||v||H¹||w||H¹.

Combining with (ST-2b) gives the unconditional explicit bound

    |Q_>T(v,w)| ≤ δ_a(T) ||v||H¹ ||w||H¹,
    δ_a(T) = 70 a e^a log(16T)/T,  T≥2.                    (ST-3)

The sum is over **all** remaining nontrivial zeros, with multiplicity, whether their real parts are 1/2 or not. No sign is discarded, no positive covariance is invented, and no hidden spectral zero list is an input.

**Domain completion:** the estimate holds on `C_c^∞(-a,a)` and gives a bounded bilinear form on `H₀¹(-a,a)` by density. Every finite-height spectral sum is bounded on the same H¹ space. The authentic Suzuki localized Weil form is H¹-continuous by the bounded continuous-kernel `G_a` acting on `iv'` (Suzuki, 2026, Eqs. 1.5–1.8). Therefore the classical identity (ST-0) extends to H¹, and the finite zero-side truncations converge to it in **operator/form norm** `H₀¹→H^{-1}` with the rate (ST-3).

**THIS IS NOT** norm convergence of Suzuki's unbounded self-adjoint operators on L² or on the full closed-form domain, nor positive spectral approximation, nor a proof that any low-height zero is critical. It repairs the domain weakness of the separate PR #83 smooth-specific C⁷ estimate: a test family with huge or undefined sixth derivatives is still controlled because (ST-3) requires only one derivative.

For higher Sobolev orders `H₀^m`, m≥2, m integrations by parts yield a looser but faster bound using `||e^(θ·) v||^(m)_1 ≤ e^(a/2)√(2a)(3/2)^m||v||Hm`, giving a `T^(1-2m) log T` signed tail rate from (ST-2a). **Higher smoothness is optional**, never required for the principal H¹ theorem.

## 4. ST-04: true first pair + unknown finite middle + bounded signed high tail

Previous PR #82 source-certified a *simple genuine* pair at `ρ±=1/2±iγ`,

    γ∈(141327/10000,141367/10000),

via a rational theta contour, not a zero list. Its immutable original-source receipt Git SHA-1 is `8f5ae1135701a933ba4946cb0b584bba4a355a47`; the implementation validates the raw Git blob before using this pair. For any a>0 this pair contributes the genuinely positive rank≤2 kernel

    K_pair(x,y)=2cos(γ(x−y)), x,y∈(-a,a),

with source-midpoint phase γ₀=141347/10000 and certified operator error `≤8a²/500`. When a=1/2 this is `1/250`. This is the **authentic** pair residue from Weil's spectral side.

For T>141367/10000, the complete original source identity is precisely

    Q_W^a = Q_pair + Q_unknown_middle,≤T + Q_signed_high,>T.     (ST-4)

Only `Q_pair` is identified as nonnegative from the finite contour; `Q_unknown_middle` is finite-rank but its zeros **may be off the line** and its sign is not determined. The high remainder is bounded by (ST-3). The finite-source N_abs count gives an explicit crude bound `|Q_unknown_middle(v)|≤2a e^a(N_abs(T)-2)||v||²_2`, but that bound is far too large to conclude positivity. Do not replace the unknown middle by zero, silently count only critical zeros, or infer RH from a finite Taylor/winding result.

## 5. ST-05: hostile regimes and the source-identity firewall

- **High-frequency concentrated tests:** take the H¹ tent `v_ε(x)=√ε(1−|x|/ε)_+`. Its H¹ norm² equals `2 + (2/3)ε²`, uniformly bounded as ε→0; it does not even possess six classical integrable derivatives. ST-3 still holds by H¹ density. This directly refutes the *overbroad inference* that PR #83's six-derivative method shows H¹ signed-tail bounds impossible. The result does NOT refute PR #83's correctly scoped C⁷ theorem or its exhibited breakdown of that particular method.
- **Source mutation:** generic multiplication by six and an arbitrary Gaussian covariance are not original completed Weil sources; `source_count` is explicitly specialized to original theta, and the first-pair import verifies the precise prior receipt hash. A correct Poisson/theta analytic continuation with fake 6 has a different germ; no automatic transfer.
- **Unknown low sign:** `diag(1,1,1)` and `diag(1,−1,1)` have identical positive first-coordinate spectral observation and identical **zero** high tail, but opposite global positivity. This toy is not a source-faithful zeta mutation; it shows why ST-3 cannot finish RH.
- **Source growth versus assumed zeros:** the proof of (ST-1c) is about order-one growth of the authentic ξ, not a finite computation of the zeros. Replacing the source or using a meromorphic function with uncanceled Gamma poles invalidates the Jensen step.
- **Spectral counting:** an explicit `N_abs(T)` by itself gives no low-height zero *positions*, and no contour input may be trusted unless authenticated with its original source construction.
- **Topology:** a signed `H¹` form-tail certificate and its stronger-derivative variants are not the missing `L²` coercivity bound; lifting to the Friedrichs form domain needs separate proof.

## 6. Next quantified theorem and research verdict

Let `T_n→∞` be an unbounded sequence of heights. Suppose the original theta model constructs **source-justified complete low-height contour coverage** through each T_n and proves all enclosed zeros lie on the critical line (including multiplicities, without external zero coordinates). Then `Q_≤T_n≥0` for every test and ST-3 implies `Q_W^a(v)≥−δ_a(T_n)||v||H¹²`; taking n→∞ proves `Q_W^a≥0` on its H¹ core. The condition on all T_n is **exactly the missing RH-strength assertion**, not obtained here. The statement is a correct conditional transfer, not proof of its premise.

**Research status:** ST-1–ST-4 PROVED LOCAL (classical Jensen, one integration by parts, Gaussian-theta construction, Weil explicit formula) with exact rational constants and executable certificate; ST-5 hostile controls PROVED for toy models; ST-6 remains **UNVERIFIED** as an all-heights original-source sign theorem. Academic novelty unreviewed; the approach is a mathematically explicit improvement of the H¹ *tail-control instrument*, not a new unconditional RH lower bound.

**Next actionable adversarial problem:** exploit the *authentic* prime/Gamma/pole operator of PR #71/#70/#79 to prove that `Q_unknown_middle,≤T` is nonnegative on a test-localized subspace, or find source-derived finite-rank Schur certificates for a declared interval a. An arbitrary signed finite Gram or positive theta covariance does not establish the required identification. In the alternate **source-first** route, derive a lower bound for the actual signed Weil operator `G_a,J` uniform on its entire mean-zero L² domain (not just finite sampled states), and combine it with the positive Gamma tail; this remains the true Weil/Suzuki wall.

### Primary sources / review

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (Sept 23, 2026), §1 and §8.5. Classical domain equality `Q_W^a(v)=<G_a iv',iv'>` and Weil spectral/source formula.
- Original SUCC theta source/gaussian Fock bound and ξ(1/2) positive: PR #73/74; exact first contour and spectral pair: PR #82.
- Independent sibling PR #83: smooth C⁷ spectral tail and rational argument-principle observer; method strength differs, no duplicate claim of priority.
- Classical Jensen formula, compactly supported Fourier decay and Cauchy–Schwarz; explicit Rosser/Riemann–von Mangoldt **not needed** for the main theorem. Optional external comparison: Rosser (1941) / Hasanalizade–Shen–Wong (2021) zero count gives far sharper constants, but using it would no longer be a source-only proof of the count.

## 7. ST-08 — A finite arithmetic ↔ spectral gluing law with a quantified H¹ defect (PROVED LOCAL; two inherited source-equalities)

This is the natural operator-level completion of the user's request. **The arithmetic and spectral sides need not use the same finite representation or the same finite observation protocol.** They both map to the ONE authentic global source, with separately certified errors. The resulting diagram commutes to a rigorously bounded error, rather than asserting a diagrammatic equality by analogy.

The independent source-first Completed-Weil PR #71 (already an ancestor of PR #82 via the all-place branch) proves CW-11 for the **signed**, contact-corrected finite Gamma-rung arithmetic Weil form `Q̃_J^arith`: for all `v,w∈H₀¹(-a,a)`, with `A_J=2J+1/2`,

    |Q_W(v,w)-Q̃_J^arith(v,w)| ≤ ε_J ||v||H¹||w||H¹,
    ε_J=max(9/(8 A_J²)+1/(2 A_J³), 1/(2 A_J²)+2/A_J³).             (ST-8a)

CW-11 retains every *true* prime-power atom on the finite spatial interval, the Gamma contact correction, the pole terms and half-density. It is not an independent prime-cutoff and is **not positive by construction**. The analytic derivation and exact hypotheses are in `research/2026-10-14/COMPLETED_WEIL_SOURCE_TRANSPORT.md` §4, already published in the branch ancestry; its status is a mathematical source-theorem import, not re-proved by the new code.

Our ST-03 gives, independently in the zero-side chart,

    |Q_W(v,w)-Q_≤T^spec(v,w)| ≤ δ_a(T) ||v||H¹||w||H¹,
    δ_a(T)=70a exp(a) log(16T)/T.                                    (ST-8b)

Subtract and apply the triangle inequality **to one and the same original Weil form**:

    |Q̃_J^arith(v,w)-Q_≤T^spec(v,w)|
      ≤ [ε_J+δ_a(T)] ||v||H¹||w||H¹.                              (ST-08)

Both independent limits can be taken: `ε_J→0` as J→∞, and `δ_a(T)→0` as T→∞, so the two chart systems converge toward their authentic shared Weil source **in H¹ form/operator norm**, not in the L² spectral norm of the unbounded Suzuki realization. This is a mathematical proof of a quantified commutative diagram of representations, not an assumption that their finite objects are identical or individually positive.

For a=1/2, J=64, T=10⁶, `ε_J≈0.00006837`, `δ_a(T)≈0.00095722`, so the source-certified two-chart defect is `<11/10000` (0.0011). At J=512,T=10⁹, the bound drops below `3/10^6`. All official certificates are exact rational outward upper bounds for exp and logs, with source immutability constraints. These numbers are not eigenvalues or evidence that the finite spectral sum is nonnegative.

**Crucial execution debt:** Computing the *values* of `Q_≤T^spec` requires complete certified spectral data below T, and this branch currently has only the already authenticated first pair. An expression with an unknown finite spectral middle is still an exact mathematically defined form, but it is **not a finite algorithm output supplied by the source tapes**. Source-only ST-08 certifies an operator error contract, not the actual finite zero list. Completing that enumeration and proving the low signed piece positive for unbounded heights remains RH-equivalent. Similarly, a source-correct numerical matrix approximation of `Q̃_J^arith` cannot upgrade ST-08 into positivity without an **all-vector** lower sign bound.

Thus the diagram is

    source original arithmetic (prime/Gamma/pole) -- CW-11 / ε_J --> Q_W
                |                                           ↑
          finite signed Gamma J                               | ST-03 / δ(T)
                |                                           |
       Q̃_J^arith  ───── defect ≤ ε_J+δ(T) ────→  Q_≤T^spec

and every arrow has an explicit source/domain contract, rather than an invented terminal/global observation.
