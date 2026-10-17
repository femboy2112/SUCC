# Operation EDGE-DIODE — an exact two-port chiral prime-wavefront theorem

**Research checkpoint:** 2026-10-17. **Base:** `femboy2112/SUCC` post-Academic-Main-III merge `610efacf02556e1c5922bc5d4e87d0087f19b446` (PR #152). **Source:** preserved genuine Suzuki completed Q-zeta screw kernel (`observational_succ/source_weil_hierarchy.py`, Git blob `0cc8510b71d178fc79e8d410a86d8b6014cf9178`; SHA256 `183863dc722230331cdbe7ba1ba4d781ad3ab4d6e58aa39552a8af4cc6c9174b`), the original source's `authenticated_prime_wavefront`, and the classical Weil distribution. The imported analytic source includes the real Gamma tower, both poles, contact, and genuine prime powers; only the **isolated n=2 prime hinge** is analyzed here. **No nontrivial zeta-zero location is used. RH OPEN; S4 SIGN OPEN.**

**Status:** The pure hinge geometry, sharp relative-energy bounds, finite polynomial resource formula and failure of uniform relative-radius continuity are **PAPER-PROVED** below and have exact rational synthetic holdouts. A hosted SUCC source gate verifies that the actual single active first-window term has `b=log(2)`, `w=log(2)/sqrt(2)` with `a=1/2`; the authenticator checks exact interval source data, not a numerical fit. There is no inference that this isolated indefinite channel makes the **complete** Weil form negative. Claimed academic priority: **UNVERIFIED** (the elementary mathematical ingredients are classical).

## 1. Two fundamentally different operator topologies

Let `I=(-a,a)`, `a>0`, and `a<b<2a` (this includes the actual prime-2 first-window `a=1/2`, `b=log 2`). Let `delta=2a-b in (0,a)` and let `w` be any nonzero real coefficient. On the mean-zero Hilbert space `H=L2_0(I)`, define

\[
(H_{b,w}u)(x)=w\int_I (|x-y|-b)_+u(y)\,dy,\qquad
(Vu)(x)=\int_{-a}^{x}u(y)\,dy,\qquad K=V^*V.
\]

`Vu=F` belongs to `H^1_0(I)`; conversely every `F in H^1_0(I)` is the primitive of the mean-zero `u=F'`. The source coefficient at the genuine first-prime hinge is `w=log2/sqrt2`, and the full original `G_a` is the **sum** of this channel with the genuine Gamma, contact and pole channels. Do NOT identify any isolated term with the completed source.

**Theorem ED-01 [CLASSICAL/PAPER-PROVED].** The isolated source kernel is small in ordinary Hilbert–Schmidt norm:

\[
\boxed{\|H_{b,w}\|_{\mathrm{HS}}^2=\frac{w^2\delta^4}{6}.}\tag{1}
\]

Indeed the difference-coordinate count on `I^2` is `2(2a-r)dr`; integrate `w^2(r-b)^2` over `r in [b,2a]`. Hence `H_{b,w}` tends to zero in L2 operator norm as `delta downarrow 0`.

The source-relevant **K-relative quadratic-form topology**, however, behaves dramatically differently.

## 2. Exact chiral two-edge factorization

For `F=Vu`, define the **left and right primitive edge charts** on `0<=t<=delta`:

\[
L_F(t)=F(-a+t),\qquad R_F(t)=F(b-a+t).
\]

The supporting edge strips `[-a,a-b]` and `[b-a,a]` are disjoint because `b>a`. Note that a two-*port* description means **two infinite-dimensional L2 chart spaces**, not a rank-two operator.

**Theorem ED-02 [PAPER-PROVED, SOURCE-SCOPED].** The exact signed quadratic form of the isolated prime hinge is

\[
\boxed{
\langle H_{b,w}u,u\rangle
=-2w\operatorname{Re}\int_0^\delta L_F(t)\overline{R_F(t)}dt.}
\tag{2}
\]

The derivative itself is supported on the two separated boundary strips:

\[
(H_{b,w}u)'(x)=w\begin{cases}
F(x+b),&-a<x<a-b,\\
0,&a-b<x<b-a,\\
F(x-b),&b-a<x<a.
\end{cases}
\tag{3}
\]

For proof: the derivative of the even hinge kernel is the odd step `w sgn(r) 1_(|r|>b)`. Integrate the step against `u=F'`, using `F(-a)=F(a)=0` and then integrate the pairing against `u=F'` by parts. The two edge contributions transform into identical cross correlations and produce (2). The source uses genuine `w=log2/sqrt2`; no zero or fake-composite impulse is consulted.

Equivalently, for `f_+=(L_F+R_F)/sqrt(2)` and `f_-=(L_F-R_F)/sqrt(2)`, the prime form is

\[
\langle H_{b,w}u,u\rangle
=-w\|f_+\|_{L^2(0,\delta)}^2+w\|f_-\|_{L^2(0,\delta)}^2.\tag{4}
\]

Thus the genuine isolated prime source creates a **Krein/chiral interaction** with opposite signs on symmetric/antisymmetric boundary correlations. It is invisible to independent reports that reveal only each edge's energy but not their cross phase. A true mixed test requires a lawful common-source superposition/measurement interface.

The differentiated prime-only Gram for any mean-zero polynomial inputs `p,q` is also exact:

\[
\langle (H_{b,w}p)',(H_{b,w}q)'\rangle
=w^2\left(\int_{-a}^{a-b}F_p(t)\overline{F_q(t)}dt+
\int_{b-a}^a F_p(t)\overline{F_q(t)}dt\right).\tag{5}
\]

For true source Legendre `p=P_j(2t)` and `a=1/2`, the entries are explicit rational polynomials in `b=log2`, times `w^2`. For instance

\[
\| (H_{b,w}P_1(2\cdot))'\|^2
=w^2\frac{(1-b)^3(6b^2+3b+1)}{15}.\tag{6}
\]

**Independent exact controls:** for the synthetic rational `a=1/2`, `b=3/4`, `w=1`, `p(t)=2t`:

- Direct triangular double integral gives `\langle H_{b,w}p,p\rangle=-61/15360`.
- The two-edge primitive identity gives the **same** `-61/15360`.
- The derivative Gram is `53/7680`.

These are **synthetic calibrations** of a theorem applied to the true log2 channel, not substituted parameters in the authentic completed kernel.

## 3. The K-relative shock survives every finite low-mode cut

Put

\[
Q_mH=\left\{u\in L^2(I):\int_I x^ku(x)dx=0\ \text{for }k=0,1,\dots,m\right\}.
\]

For the SUCC first-window four-low decomposition, `Q_4 H` is precisely this space at `m=4` (invariant under change from monomials to Legendre polynomials).

**Theorem ED-03 [PAPER-PROVED / EXACT FINITE CALIBRATION].** For EVERY fixed nonnegative integer `m` and EVERY `delta in (0,a)`:

\[
\boxed{\inf_{0\ne u\in Q_mH}
\frac{\langle H_{b,w}u,u\rangle}{\langle Ku,u\rangle}
=-|w|,\qquad
\sup_{0\ne u\in Q_mH}
\frac{\langle H_{b,w}u,u\rangle}{\langle Ku,u\rangle}
=+|w|.}\tag{7}
\]

The upper absolute bound follows immediately from (2), Cauchy–Schwarz, `2ab<=a^2+b^2`, and the fact the left/right windows are disjoint:

\[
|\langle H_{b,w}u,u\rangle|
\le |w|(\|L_F\|^2+\|R_F\|^2)
\le |w|\|F\|^2=|w|\langle Ku,u\rangle.
\]

**Explicit sharp construction:** Let `d=delta`, and on `0<=t<=d` put

\[
\varphi_m(t)=\frac{d^m}{dt^m}\left[t^{m+1}(d-t)^{m+1}\right].\tag{8}
\]

Both endpoints of `phi_m` vanish. Integrating by parts `m` times, with all boundary terms zero, proves `\int_0^d t^j phi_m(t)dt=0` for `0<=j<m`. Build a primitive F that is zero away from the edge windows, equals `phi_m(t)` on the left, and equals `+phi_m(t)` (respectively `-phi_m(t)`) on the right. This F is in `H^1_0(I)`, and `u=F'` has all moment constraints through degree m. Equation (2) gives ratio `-w` (respectively `+w`), so both extrema are **actually attained by smooth-on-each-window polynomial profiles**, not merely approached.

**Important consequence.** As the prime hinge is just born (`a downarrow b/2`), `delta downarrow0`, equation (1) gives `||H_{b,w}||HS ->0` but (7) retains exactly `|w|>0` in the K-relative high-energy metric — including after killing the first four SUCC low modes. Hence **small ordinary operator norm does not imply small K-relative Schur influence**. This is a theorem for the actual isolated true prime-power channel. It does NOT imply the full source high block changes sign or that its total coercivity degenerates: the complete Gamma/contact/pole terms can dominate these high-frequency witnesses.

## 4. The price of finite observer bandwidth — a quantitative SUCC resolution law

The extremal functions in ED-03 get increasingly localized and expensive in ordinary L2 derivative energy. Since `u=F'`, their `||u||² / ||Vu||²` ratio is the pure edge Sobolev quotient.

**Theorem ED-04 [PAPER-PROVED].** For the concrete order-m witness above,

\[
\boxed{
\frac{\|u\|_{L^2(I)}^2}{\|Vu\|_{L^2(I)}^2}
=\frac{2(2m+1)(2m+5)}{\delta^2}.}
\tag{9}
\]

*Derivation.* Under `z=2t/d-1`, `phi_m` is a nonzero multiple of `(1-z²) P'_{m+1}(z)`. By Legendre's differential equation, `[(1-z²)P'_{m+1}]'=-(m+1)(m+2)P_{m+1}`. Orthogonality and the three-term recurrence express `(1-z²)P'_{m+1}` as `(m+1)(m+2)/(2m+3)·(P_m-P_{m+2})`. The ratios of their exact L2 norms then give `∫|phi'_m|² / ∫|phi_m|²=2(2m+1)(2m+5)/d²` after applying the coordinate Jacobian. Both edge copies scale identically.

At the four-mode cut `m=4`, the construction costs **`234/delta²`** in squared L2-to-K energy. The exact tests verify the formula for m=0..8 and multiple rational widths.

This is a rigorous version of the user's finite observer intuition: **there is no uniform shallow/high-bandwidth certificate merely because an emerging prime kernel looks small in L2.** At a fixed finite observer bandwidth `||u||<=M||Vu||`, however, the HS norm gives

\[
\frac{|\langle H_{b,w}u,u\rangle|}{\langle Ku,u\rangle}
\le \frac{|w|M^2\delta^2}{\sqrt6},\tag{10}
\]

so the same prime effect **does vanish** with the wavefront width within a fixed finite-resolution class. The two limits (observer bandwidth to infinity, prime activation width to zero) do not commute. This is an observer-relative, exact mathematical statement—not a physical clock-energy law, a proof of RH independence, or a source-derived positive Weil factorization.

## 5. Consequences for the actual RH program

1. **The missing all-radius transport has a specific obstruction.** The support radius can change continuously and the newly active prime hinge can go to zero in Hilbert–Schmidt norm, while its signed coupling remains order-one in exactly the `K=V*V` geometry used in SUCC's high coercivity/Schur estimates. Therefore a proposed transfer of first-window coercivity across prime thresholds needs **source-specific Gamma-versus-boundary-current compensation** and a controlled observer bandwidth, not continuity of the undifferentiated kernel alone.
2. **Two-port observability gives a source-faithful mixed probe grammar.** The right mathematical E-program reads matched primitive edge profiles (source-correlated), their cross pairing, and the normalization to the original K metric; independent E votes or two isolated edge energies are insufficient. No physical sensor is built here.
3. **An exact analytic route around coarse midpoint-Lipschitz derivative bounds is visible.** For finite Gamma truncation J and polynomial response v, `h_J'=(G_Jv)'` is a finite **piecewise exponential polynomial** on the intervals cut by `x=±(a-b)` and source endpoints. Each term (Gamma exponentials, two pole exponentials, contact primitive, and hinge primitive) has exact rational-polynomial antiderivatives with computable source transcendental intervals. Its whole derivative Gram and the `P_≤3` correction can in principle be enclosed by certified interval evaluation of these finite expressions, paying the proven O(J^-3/2) **differentiated** Gamma tail. This is a concrete method to remove the ~18×-energy B1 grid radius that dominates the current `CertifiedDerivativeEnergyTrial`; it is **NOT IMPLEMENTED HERE** and does not by itself make the S4 sign positive. Reproduce #149–#152 packets before any new sign claim.
4. **A useful new quantitative experimental target** is a relative inequality comparing the complete Gamma/contact/pole positive energy on the moment-constrained edge modes against the explicit negative chiral eigenchannel (7), preferably as an operator-valued frequency/edge weight rather than the existing global scalar coercivity κ. The isolated negative channel cannot be suppressed by simply increasing the number of low polynomial moments: ED-03 constructs it for every finite cut.

**Next falsification:** independently derive the signed original `g_prime` coefficient and amplitude from the frozen source, reproduce the exact hinge double-integral and source-labeled K energy in two unrelated representations, then challenge the `K`-relative sharpness with a genuine Q4 moment-constrained F. Compare the analytically integrated finite-J complete derivative Gram against the current source-certified B1/B3 bounds. Preserve all Gamma, contact, poles, genuine prime powers, test domains and prior countermodels.

## 6. Executed receipts and limitations

`observational_succ/prime_hinge_chiral_edge.py` is a standalone exact-rational polynomial laboratory; `tests/test_prime_hinge_chiral_edge.py` tests the sharp witnesses, high moment constraints, 2x2 chiral signs, first-four derivative Gram, HS-vs-K nonuniformity, parameter mutants, and resource ratio. The **separate** `authentic_prime2_interval_gate()` imports the protected original source, checks the true wavefront `(2,2)` at `a=1/2`, and encloses `b=log2,w=log2/sqrt2`. The synthetic standalone checkout cannot run that integration test; it is skipped until the full repo is mounted, while the mathematical tests pass. No archived source or existing source implementation was edited.

Reproduction in a full SUCC checkout:

```sh
python -m unittest discover -s tests -p 'test_prime_hinge_chiral_edge.py' -v
python scripts/prime_hinge_chiral_edge_probe.py --verify
python scripts/verify_provenance.py
python scripts/observer_foundations_probe.py
python scripts/ordinal_succ_report_probe.py
python -m unittest discover -s tests -p 'test_*.py'
```

Claims ED-01–04 and equations (2)–(10) are an exact *single-channel* theorem, not a positivity theorem for complete original `G_a`; neither `S4` nor RH is decided. Independent academic literature comparison for this exact edge factorization is not complete. No 3D physical sphere or machine is inferred. **RH PROVED: NO.**
