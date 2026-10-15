# ONE OBJECT — Tate/Connes contact ↔ Suzuki Neumann metric; zero-shift residual-Schur theorem

**2026-10-15 research draft. RH OPEN.** Branch research/one-object-residual-schur-2026-10-15, exact parent PR #104 research/hilbert-prime-weil-operator-atlas-2026-10-14 @ 88eca261bae1381b83d018163d0945c3434a3385; original consolidated main @ 03db44203147a7b28d445bb9f970fa71360e78c4. Independent, READ-ONLY sibling source contexts: Tate conductor-sensitive PR #103 @ 940f0a47, ONE OBJECT Weil–Suzuki–Connes PR #106 @ 65e46f29, Hilbert fully integrated finite-J cell block PR #105 @ 2da47bd8. Those PRs are not imported or merged. This branch derives an additional RELATIVE NEUMANN/GALERKIN residual theorem and identity-contact source transport, without assuming RH.

## 0. What is established by literature versus this branch

**Primary literature, not new priority**:
- Suzuki, Weil's quadratic form via the screw function, arXiv:2606.09096v3, equations (1.3) Weil screw, (1.5) compact meanzero G_a, (1.8) Q_W(v)=<G_a(i v'),i v'>, and §8.2 eq. (8.2) Neumann inverse K_a=(-Delta_N)^(-1): https://arxiv.org/html/2606.09096v3 .
- Tate (1950), Fourier analysis in number fields: self-dual additive Haar/Fourier and compatible adelic characters, multiplicative Mellin, conductor/root/Gamma; for accessible exposition see https://math.uchicago.edu/~may/REU2016/REUPapers/Mine.pdf . Requires explicit Schwartz–Bruhat tests and source-normalization, not invented local clocks.
- Connes, Trace formula in noncommutative geometry and zeros of zeta, 1998/1999, arXiv:math/9811068, local Theorem 3: a trace has 2h(1)log' Lambda, local |1-u|_v^-1 off identity, and a uniquely prescribed Fourier-normalized principal-value distribution. It is not uniquely recovered from off-identity fixed-point counts: https://arxiv.org/html/math/9811068 .
- Classical Douglas factorization/range theorem; variational characterization of shorted positive forms; Galerkin and residual a posteriori bounds. Their assembly below is a proved statement under explicit assumptions, not a claimed new published theorem.

**Imported source-dependent ancestor**: PR #104 claims, for TRUE zeta on a=1/2, H=L0²(-1/2,1/2), P=Legendre modes 1..30 and Q=I-P, genuine original Suzuki G_a has QGQ=D >= kappa QK_aQ with kappa=369/10000, and B=QGP maps the 30-low into H1 ∩ QH. This branch calls the ancestor's SHA-pinned source gate, including the actual original source module blob. The ancestor's analytic inequality is not reproduced by a finite test suite alone; all conclusions relying upon it are explicitly **conditional on its complete mathematical proof**. No unwarranted D >= kappa I or globally invertible D is assumed.

## 1. A precise unexpected Tate–Connes–Suzuki contact identity — ORS-01 (CLASSICAL/PROVED SOURCE TRANSPORT)

Let W be the WHOLE original completed Weil distribution, including true arithmetic Lambda(p^r)/sqrt(p^r), only one real Gamma, polar terms and self-dual Tate convention; Suzuki's anchored continuous even screw g obeys -g''=W as distributions (ancestor ONE OBJECT #106 establishes a contact-matched finite stage; this source identification is imported).

For ANY scalar contact perturbation c, set W_c=W+c delta_0. Then
  g_c(t)=g(t)-c|t|/2
is the unique even anchored primitive satisfying -g_c''=W_c: d²|t|/dt²=2 delta_0. On mean-zero H=L0²(-a,a),
  G_{a,c}=G_a+c K_a,  K_a=(-Delta_N)^(-1).
The key is Suzuki's actual kernel
  N(x,y)=(x²+y²)/(4a)-|x-y|/2+a/6.
The x²,y²,const terms vanish after BOTH input/output mean-zero compression, so P[-|x-y|/2]P=K_a **as operators**, not just finite samples.

For v in H0¹(-a,a), u=i v', Suzuki's exact identity gives
  Q_{W_c}(v)=Q_W(v)+c||v||²
             =<G_a u,u>+c<K_a u,u>.
The Friedrichs realization A_a of the localized form changes by the rigid scalar shift A_{a,c}=A_a+cI on the SAME form domain, and the generalized Rayleigh quotient relative to K changes by EXACTLY c.

**Interpretation:** any wrong Tate/Connes identity normalization, even with every off-origin Euler prime and Gamma trace agreeing, can shift the localized Weil sign by a predetermined amount. This explains why the principal-value/contact term is directly load-bearing for the **same K metric** in the 30-moment high inequality. Connes off-identity |1-u|^-1 cannot fix c; his Fourier normalization is a separate actual premise. Therefore neither the Connes finite local p-clock nor arbitrary h(0)-blind probes authenticate the full signed distribution.

**Exact independent finite calibration:** for step-constant meanzero u on N equal cells of width h=2a/N,
  <K_a u,u> = int_-a^a [int_-a^x u(t) dt]^2 dx
             = -1/2 int int |x-y|u(x)u(y)dxdy.
The first integral is an exact finite sum of squared piecewise-linear antiderivatives; the second is an independent exact double sum using h³/3 (same cell) and h³|i-j| (different cells). Both agree for every tested rational meanzero source and show c times the same energy. At a=1/2, source low raw Legendre K has exact diagonal 1/30,1/210 on modes P1/P2, replayed from the integrated module; those are the authentic inverse-Neumann low metric, NOT the signed original G.

## 2. The SOURCE RELATIVE NEUMANN RESIDUAL-SCHUR THEOREM — ORS-02 (PROVED MATHEMATICALLY, conditional on correct source high lemma)

Let real or complex H=F ⊕ H_h, with F finite dimension m, G=G* bounded, blocks
  G=[A B*; B D].
Let K_a be the genuine positive injective inverse-Neumann Laplacian of the full mean-zero H (not the identity). Assume:
  (H1) D >= kappa QK_aQ on H_h, with kappa>0;
  (H2) B:F→H_h maps into H1(-a,a) ∩ H_h;
  (H3) Y:F→H_h is ANY bounded finite-rank, known, source-compatible response, with DY:F→H1 and r:=B-DY:F→H1 ∩ H_h.
The last inclusion holds if original source G:L²→H1 is bounded, P/Q are bounded on H1, and Y finite rank in H_h; those analytic claims must be proved for the true arithmetic source before issue of a source certificate.

Define the variational **zero-shift response** (without unbounded D^-1):
  <R0 x,x> = sup_{z∈H_h} (2 Re<Bx,z>-<Dz,z>).
It is finite: for r∈H1 ∩ H_h, Suzuki K_a=(-Delta_N)^-1 gives the classical estimate
  |<r,z>| ≤ ||r'||_2 <K_a z,z>^1/2
  ≤ kappa^-1/2 ||r'||_2 <Dz,z>^1/2.
By elementary quadratic completion, the response is finite, hence defines a positive finite-dimensional m×m Hermitian R0.

Define
  L_Y=Y*B+B*Y-Y*DY,   r=B-DY,
  T_r(i,j)=<r_i',r_j'>_L² where r_i=r(e_i).
For any x, write z=Yx+w; the variational functional becomes
  <L_Y x,x>+2 Re<rx,w>-<Dw,w>.
The term at w=0 gives LOWER, the dual K-Neumann bound gives UPPER. Thus as finite-matrix Loewner inequalities,
  **L_Y <= R0 <= L_Y+kappa^-1 T_r.**                    (ORS2)
The source shorted low matrix S0=A-R0 is sandwiched
  **A-L_Y-kappa^-1 T_r <= S0 <= A-L_Y.**                (ORS3)

**Two-sided verdicts with NO global inverse:**
(a) A-L_Y-kappa^-1 T_r >=0 -> G>=0 (the high block is >=0 and the variational infimum is nonnegative) for THIS FIXED a, once every piece of original source data is really certified.
(b) If x*(A-L_Y)x<0 for a verified rational x, the actual vector x ⊕ (-Yx) has strictly NEGATIVE G form (falsifies the corresponding original Weil positivity claim). To promote (b) the actual source entries, not only matrix arithmetic, must be rigorously enclosed.
(c) If neither holds, record AMBIGUOUS. Calling it "RH undecidable" is unsupported.

When all high coordinates are finite and K invertible, T_r is exactly r* K^-1 r and the theorem can be checked by independent rational inversion of D. The infinite theorem relies on Sobolev duality and the source-relative K gap, NOT a formal Moore–Penrose inverse with unproved domain. It remains valid when no H-valued solution Dy=Bx exists.

## 3. Genuine Gamma finite-stage bridge with NO λ^-1 explosion — ORS-03 (PROVED CONDITIONAL SOURCE MAJORIZATION)

Take exactly PR #104's true contact-fixed Gamma truncation G_J: the genuine pole, prime and infinite contact are **unchanged** while the omitted positive OU Gamma tail is T_J=G-G_J. This is not the separate contact-MATCHED W_J scheme in sibling PR #106; do not identify the schemes at finite J without its own explicit correction.

Ancestor source bound at a=1/2:
  || [Q(G-G_J) f]' ||_2 <= delta_J ||f||_2,
  delta_J=963 tau_J,
  tau_J=1/(4J+1)+4/(4J+1)^2.
On low x and high Yx, let r_J(x)=QG_J(x-Yx), r(x)=QG(x-Yx). Low and high are L²-orthogonal, so ||x-Yx||²=||x||²+||Yx||². For arbitrary rational eta>0, Young's square inequality gives
  T_r <= (1+eta) T_{r_J}
          +(1+eta^-1) delta_J²(I+Y*Y).                (ORS4)
Consequently, for the **original completed source**, if authentic independently checked matrices A,L_Y,T_{r_J},Y satisfy
  A-L_Y-kappa^-1[(1+eta)T_{r_J}
       +(1+eta^-1)delta_J²(I+Y*Y)] >=0              (ORS5)
then G_{a=1/2}>=0. This is a **FINITE-DIMENSIONAL sufficient sign certificate** that does not pay a 1/lambda resolvent blow-up. It is not itself a proof that original arithmetic satisfies ORS5.

The module original-source source gate replays PR #104 original SHA, prime tape, kappa=369/10000 and 30-mode range. The Gamma-tail delta is source-derived. However A, Y and T_{r_J} are currently UNCOMPUTED as rigorously authenticated complete original source matrices; user-provided rational matrices cannot be stamped with genuine arithmetic provenance merely because they satisfy PSD algebra. The implemented ORS4 API visibly says actual_T_J_verified=False, actual_Y_verified=False, RH_proved=False.

**Advantage over previous approach**: the previous global estimate R0 <= kappa^-1 T_B was source-correct but ignores finite high responses, while Galerkin Y subtracts those interactions and makes the bound depend only on a RESIDUAL. It can be significantly sharper in the right basis. **No theorem says the residual H1 norm must shrink for an arbitrary sequence of Galerkin subspaces**. The source's analyticity, high operator range structure, or an independently justified approximation theorem is still required.

## 4. Falsifiers, compactness, and effective Zeno regimes — ORS-04 (PROVED exact toy controls)

**Toy I: compact D with no H-valued inverse, yet finite zero-shift short response.** On ell²(N), D=K=diag(n^-2) and b_n=n^-2. b is in Range(D^1/2) but not Range D: formal D^-1 b=(1,1,...) not in ell². Nevertheless the response R0=sum_n 1/n² is finite. Finite responses using the first N states yield sum_{n<=N}1/n², with true residual H1²=sum_{n>N}1/n² <=1/N. Therefore the zero-shift scalar short can be certified to arbitrary accuracy by FINITE SUCC with a source-derived modulus, despite impossibility of a bounded inverse operator. This is the exact useful Zeno shape.

**Toy II: L² is insufficient.** D=K=diag(n^-2), b_n=n^-1 is in ell² but not Range D^1/2, and finite responses equal N, so no finite zero-shift scalar response. It is impossible to derive ORS2 from just "bounded original B" without its Sobolev/range source law.

**Toy III: real high residual improves a margin.** Finite rational K=diag(1,1/4,1/9), D=diag(2,1/4,1/9) >=K, b=(1,1/4,1/9), true response R0=31/36. For A=9/10, Y=0 gives upper 49/36 and cannot certify positivity; selecting only first high response y1=1/2 gives L=1/2, residual penalty 13/36, U=31/36, and A-U=7/180>0. This is an **independent exact-rational proof** that a lawful first Galerkin response can turn an inconclusive one-sided global derivative budget into a positive source-specific toy verdict. For A=4/5, full high response supplies an explicit negative low source test. Neither toy is the original Weil operator.

**Wrong metric:** D=diag(1,1/100) >=K=diag(1,1/100) but does NOT dominate I. A fake kappa I gap is immediately rejected; this is especially dangerous for compact high sectors.
**Near-zero band:** Nonnegative exact principal-minor tests include singular PSD controls; strict LDL requiring all pivots >0 cannot replace PSD.
**Contact normalization:** Off-identity Connes fixed-point data leave arbitrary c delta0; it manifests in this *same* relative-Neumann metric as cK and shifts generalized source margins by c. Test original source wrong-contact mutants; do not call any off-origin trace formula a normalization certificate.
**Character/conductor controls:** PR #103's primitive odd conductor3 chi(-3) gives different gamma parity/ramified source and no poles; a matched functional equation alone is not an original zeta positive source. Do not transplant original source kappa or contact to that test case without new proof.
**Hilbert data limits:** a finite dyadic stream or conditional L² martingale may approximate original source kernel, but it does not automatically provide derivative Gram T_{r_J}, norm H1 or an unshifted high inverse.

## 5. Faithful Tate–Suzuki–Connes ONE-OBJECT compatibility graph

SAME SOURCE gates:
(a) Genuine p^k source Λ=log p, half-density n^-1/2, full pole and one Gamma; additive self-dual Fourier Haar and multiplicative Mellin normalization, correct conductor and parity (Tate). Existing sibling PR #103 supplies a partial conductor3 calibration, not the FULL zeta Schwartz–Bruhat global coupling.
(b) Completed signed Weil distribution W as a test-functional, including the CONTACT at identity; PR #106 finite contact-matched W_J ↔ -g_J'' is a distinct, cited, partial gluing theorem.
(c) Suzuki g, compact meanzero G_a and inverse-Neumann K_a, with exact derivative transport (primary Suzuki). The explicit δ0↔K map above is now an additional exact source-shift compatibility test.
(d) A correctly normalized Connes adele-class distribution trace equal on a sufficiently rich common test space to W, including Fourier principal value, cutoff and nontrivial fixed-point/resonance contributions. PR #106 only proves a finite local p-clock/off-identity trace, not this global equality.
(e) The first-window zero-shift R0 and low S0 from ORIGINAL source; ORS2/ORS4 supply a **proof-shaped residual certificate**. Its source-evaluated low A, finite candidate Y and residual derivative T_J remain unpaid. A noncircular sign for all radii is still RH-hard.

Classification: SAME SOURCE normalized convergence via Tate/Suzuki is a necessary condition, not a sufficient sign theorem; Connes as a different realization is independent source identification, not a magical positivity guarantee. The mathematical final two layers are source identification plus source-derived **nonnegative signed form** for every admissible compact test. No zero lookup or circular feature map may be inserted into either step.

## 6. What to implement next (precise practical milestones)

1. **Actual original source finite-J derivative Gram**: use original g_J and exact low/high Legendre functions, calculate r_J(x)=QG_J(e_i−Y e_i) for i=1..30 and H1 derivative pairings on a=1/2 with outward rational bounds; preserve real Gamma/contact/prime/poles, true half-density. Compare against source-independent analytic/formula and direct main low matrix. Do NOT call a numerically computed T_J a proof.
2. **Galerkin optimization**: choose parity-respecting finite high Legendre modes >=31, compute original source block D_N and B_N with quantified errors, solve for Y from verified PSD regularization. Measure genuine residual derivative Gram decline against ancestor crude 11556²/κ bound; need explicit rigorous convergence or failure countermodel. Never presume D_N has a fixed gap.
3. **Substitute ORS4 into source low Schur**: issue one finite PSD certificate A−L−κ^-1 T_upper with actual interval matrix entries. A strict certified counterexample would negate current full Weil sign; a nonnegative certificate at a=1/2 does NOT prove RH at all a.
4. **Grow supports with proof budget**: prove source-dependent operators behave for all a>0 (not automatically from 30 moments at a=1/2), including higher primes and contact, using compact a-exhaustion and source-identified high gaps.
5. **Tate/Connes test-space unification**: explicitly fix Schwartz–Bruhat test data, Haar/character self-duality, completed gamma/conductor/root/poles and Fourier-normalized Connes identity principal value; prove equality with the same signed W on a dense test space, with rigorous domain continuity. Off-origin trace values are insufficient.
6. **Formal proof**: Lean4.14/mathlib finite-dimensional Schur residual identity, inverse Neumann dual pairing, source-typed proof capsules, fail forged source; no Lean claims until actual kernel CI.

**Current verdict:** a rigorous, noncircular relative-Neumann residual shorting theorem and exact contact-shift transport identify a narrower, executable missing arithmetic matrix task. The true low Schur sign, rigorous original-source A/Y/T_J, global Connes trace, all radii and RH remain **UNVERIFIED**. This is material progress in the proof interface, not a complete proof of RH.

## Reproduction

- Code observational_succ/one_object_relative_residual.py; one_object_source_residual.py; one_object_contact_neumann.py.
- Tests tests/test_one_object_relative_residual.py, test_one_object_source_residual.py, test_one_object_contact_neumann.py.
- Receipt scripts/one_object_residual_probe.py and research/2026-10-15/ONE_OBJECT_RESIDUAL_RECEIPT.json.
- Full source baselines: ancestor original atlas PR #104, imported original signed source SHA 0cc8510b71d178fc79e8d410a86d8b6014cf9178, consolidated main SHA 03db4420.
- CI dedicated 3.10/3.13 plus original source provenance and existing atlas regression. Complete full-suite/Lean checks separately scoped.


## 1a. Two authentic contact boundary channels — ORS-01b (PROVED LOCAL / classical Legendre–Neumann algebra)

The source source difference cK_a is **NOT confined to the low 30-dimensional matrix block**. Decompose H=P_30 H⊕Q_30 H. In the same declared nonconstant Legendre basis \(L_i(x)=P_i(x/a)\), the actual inverse Neumann metric has exact matrix entries \(\langle L_i,K_aL_j\rangle=0\) unless \(|i-j|\in\{0,2\}\). This is the original integrated SUCC \`suzuki_moment_schur.inverse_neumann_entry\` classical identity. At a=1/2 the ONLY cross-cut pairs between low i≤30 and high j≥31 are:
\[
 \boxed{\langle L_{29},K_{1/2}L_{31}\rangle=-\frac1{906948},\qquad
 \langle L_{30},K_{1/2}L_{32}\rangle=-\frac1{999180}.}\tag{ORS1b}
\]
These are **unnormalized** Legendre coefficients; normalization by \(2a/(2i+1)\) must be applied if using an orthonormal basis. Consequently if c≠0 then \(\operatorname{rank}(QKP)=2\) in this split, and
\[
 \boxed{A_c=A+cPKP,\quad B_c=B+cQKP,\quad D_c=D+cQKQ.}\tag{ORS1c}
\]
Even a *single* contact-normalization error leaks into **two** authentic low/high parity channels in Suzuki's moment Schur problem. It is incorrect to adjust A only, omit B_c, and claim the Connes- or Tate-shifted model represents the same Weil object.

From the already-reported true high bound \(D\ge\kappa QKQ\), we have \(D_c\ge(\kappa+c)QKQ\). A negative shift \(c\le-\kappa\) destroys THIS derived positive-margin certificate (not necessarily the actual high positivity). An exact source gate verifies κ=369/10000, channels (-1/906948,-1/999180), original source blob, and refuses to call c≠0 the authentic Weil normalization. The quadratic contact shift still acts as \(A_a+cI\) in the *unbounded derivative-space Friedrichs realization*; both descriptions agree only when all low/high terms are transported, not if the cross boundary is dropped.

This makes the principal-value normalization a tangible **Schur coupling source** rather than a decorative scalar.

## 3a. Source-coupled Zeno schedule for arbitrarily expensive finite responses — ORS-03b (PROVED LOCAL; conditional on verified finite response norm)

An actual finite high-sector approximation Y_N may have rapidly increasing \(L^2\) operator norm, especially when attempting to approach the unbounded zero-shift inverse. A fixed synchronized Gamma cutoff J=N is therefore NOT automatically adequate. The genuine derivative tail bound lets SUCC select a **source-compatible diagonal schedule** without assuming a bounded high inverse:
\[
 \delta_J=963\Big(\frac1{4J+1}+\frac4{(4J+1)^2}\Big)
 < \frac{1926}{4J+1}\quad(J\ge1).
\]
Given an independently justified rational upper bound \(M\ge\|Y_N\|_{\rm op}\) and rational tolerance ε>0, choose
\[
\boxed{J=\max\bigl(1,\lfloor 1926(1+M)/(4\varepsilon)\rfloor+1\bigr).}\tag{ORS6}
\]
Then **the original source Γ tail**, including its derivative/Legendre projection effect, has
\[
 \boxed{\delta_J(1+\|Y_N\|)<\varepsilon.}\tag{ORS7}
\]
This is an exact rational finite Zeno resource law, proved by the monotone tail and the integer ceiling; no geometric, false Euler or zero-coordinate input. For each FINITE Y_N it gives a computable finite J, even if \(\|Y_N\|\to\infty\) along the sequence. It does **not** authenticate the input M, materialize the J×30 source Gamma integrals, or imply that the *uncorrected* residual \(\|(B-DY_N)'\|\) vanishes. Tests include enormous finite M and malicious non-exact coefficient inputs.

This cleanly splits two uncertainties:
1. SOURCE Γ truncation of the finite response can always be made negligible with sufficient finite source computation **once a bound M is known**.
2. Whether there exist effective finite Y_N for which the **original arithmetic** residual derivative Gram shrinks is the genuinely missing source-specific approximation theorem.

If the source independently provides \(\|(B-DY_N)'\|\to0\), choose ε_N→0 and J_N by ORS6; ORS2–ORS5 yield shrinking certified cross-response error. This conditional "diagonal completion" does not require a strong limit of the unbounded D^-1Y_N in \(L²\): the compact diagonal toy proves that such a strong inverse limit may not exist even when the scalar short converges.

## 7. Refined last-gate dependency graph

The exact source-checked chain at a=1/2 is now

    Tate normalization / Fourier Haar / Euler ↔ completed W  [full cross-source equality PENDING]
         ↓ source δ0 principal-value mismatch becomes cK exactly
    Suzuki original G, K=(-Δ_N)^−1, mean-zero D=i∂
         ↓ import AMW-06B D_high >= (369/10000) QKQ
    Douglas range B∈Range(D_high^1/2)  [import PR104; zero-shift scalar finite]
         ↓ this branch: finite Y residual ORS2 + true gamma budget ORS4/ORS6
    Source-authenticated A, Y, exact finite-J T_(B−DY)'   [MISSING]
         ↓ strict matrix inequality A−L_Y−κ^-1 Tupper >=0 at a=1/2
    Source extension to every a with appropriate high positive complement [MISSING]
         ↓ original signed Weil >=0 all H0¹ test functions
    RH

An independent Connes global realization must identify the SAME signed distribution **including its Fourier-normalized principal value**, not merely the same off-origin local clock traces. This is a separate missing representation arrow and does not supply sign by default.

**No complete proof of RH is claimed.** The newly demonstrated local theorem has removed the requirement of a bounded D^-1 at shift zero from the certificate architecture and exposed concrete source matrices/residuals to compute, but it has not established their required sign or a universal all-radius family.


## 1b. Connes/Tate contact gauge is exactly a translation of the original GENERALIZED Suzuki spectral pencil — ORS-01d (PROVED ALGEBRAICALLY; original source identity from ORS-01)

The correct signed Suzuki spectral question is naturally a relative pencil \(\mathcal P_G(\mu)=G-\mu K_a\), not an arbitrary finite matrix eigenproblem. Because a contact discrepancy \(c\delta_0\) gives \(G_c=G+cK_a\), there is an exact **all-domain** operator/form identity
\[
\boxed{\mathcal P_{G_c}(\mu)=G_c-\mu K_a
=G-(\mu-c)K_a=\mathcal P_G(\mu-c).}\tag{ORS1d}
\]
This is stronger than saying that isolated finite eigenvalues move by c: **the entire generalized spectral pencil is translated**, preserving every source-true low/high cross term and its two Neumann boundary channels. If a spectral-parameter domain permits taking the high shorted complement, its low Schur matrix must agree under this \(\mu\mapsto\mu-c\) translation. The identity is of quadratic forms, so it holds before attempting any potentially illegal high inverse at zero; it does not license one.

An exact 3×3 finite rational countercontrol uses SPD \(K=\begin{psmallmatrix}2&1&0\\1&2&0\\0&0&1\end{psmallmatrix}\), symmetric \(G=\begin{psmallmatrix}4&1&0\\1&3&0\\0&0&3\end{psmallmatrix}\), a one-mode low cut, \(c=1/2,\mu=1/4\). True Schur of \(G_c-\mu K\) equals true Schur of \(G-(\mu-c)K\) exactly. A **fake contact correction applied only to the low block** gives a different Schur (because K has a nonzero cross), demonstrating the omitted source-coupling error directly. The toy source is not the full arithmetic zeta, and its finite high block happens to be invertible; this is not a theorem that the actual infinite compact \(D^{-1}\) exists.

**How this constrains Connes:** the Fourier-normalized principal-value contact is not an arbitrary low-only renormalization. Any proposed Connes realization equal to authentic W must yield c=0, including the rank-two low/high K boundary contact channels. A finite off-identity local trace identity cannot establish c=0 by itself. This gives a falsifiable **normalization compatibility gate** in the same Hilbert space where the Suzuki sign problem lives, not a separate positivity theorem.


## 3b. FIRST ACTUAL authenticated finite-J derivative-response Gram, rank-one and rank-three — ORS-03c (PROVED LOCAL ORIGINAL SOURCE INTERVAL)

The missing source-dependent \(T_{(B-DY)'}\) is not discharged by the abstract theorem ORS-02. This round therefore also implements a **first real arithmetic low-to-high response laboratory**. On \(a=1/2\), take the genuine first unnormalized Legendre \(u_1(y)=P_1(y/a)=y/a\) and the signed true Suzuki finite-J kernel \(g_J\) from the **original infinite-contact source scheme**, retaining the only real Γ, actual p=2, both original polar terms and contact. For
\[
 F_J(x)=(G_{a,J}u_1)(x)=\int_{-a}^a g_J(x-y)u_1(y)\,dy,
\]
two exact finite integrations by parts (using continuity/Lipschitz of the original \(g_J\)) give
\[
 \boxed{F'_J(x)=\frac1a\int_{x-a}^{x+a}g_J(t)\,dt
                   -g_J(x-a)-g_J(x+a).}\tag{ORS8}
\]
The signed primitive \(H_J(R)=\int_0^R g_J(t)\,dt\), \(R\ge0\), has exact elementary source decomposition:
\[
\begin{aligned}
H_J(R)={}&-8(e^{R/2}-1)+8(e^{-R/2}-1)+8R
  +\frac{C_\infty R^2}{4}\\
 &+\sum_{n=p^k\le e^R}\frac{\log p}{2\sqrt n}(R-\log n)^2\\
 &-\sum_{j<J}\frac4{(4j+1)^2}
 \left[R-\frac{2}{4j+1}(1-e^{-(4j+1)R/2})\right].
\end{aligned}\tag{ORS9}
\]
Use the odd extension \(\operatorname{sgn}(x)H_J(|x|)\). At each R the original \(\log p,\sqrt n,\exp,\pi,\gamma\) values are enclosed by the immutable original-source rational interval functions. There is **NO interpolation across a prime hinge**, no fitted positive kernel, no input nontrivial zeros.

With source-proved \(\operatorname{Lip}(g_J)\le L_J(a)\), (ORS8) immediately yields
\[
 \boxed{\operatorname{Lip}(F'_J)\le4L_J(a).}\tag{ORS10}
\]
Thus rational \(x\)-grid intervals of width h and node bounds \([F'_J(x_i)]\) extend uniformly to each entire cell via \(\pm2L_Jh\); exact squaring and integral summation give a rigorous **whole-domain** rational enclosure of \(\int_{-a}^a |F'_J|^2\,dx\). Implemented by \`one_object_true_derivative.original_first_legendre_H1_energy\`. This is genuine original-source directional information, not a 30-mode bounded-inverse theorem.

For an additional SOURCE-IDENTIFIED projection, use the authentic direct original signed low block from integrated \`suzuki_legendre_source.authentic_full_low_entry(i,j,a,J)\`, which derives exact Legendre pair integrals of the same source g_J (not a numeric independent bath). On \(P_m=\operatorname{span}\{L_1,\ldots,L_m\}\), m=1 or 3 in the currently validated finite prototype, let
\[
 \beta_j=\frac{\langle L_j,G_J L_1\rangle}{\|L_j\|_2^2},
 \qquad r_{J,m}=(I-P_m)G_J L_1.
\]
Then
\[
 \boxed{r'_{J,m}(x)=F'_J(x)-\sum_{j=1}^m\beta_j L'_j(x),}
\tag{ORS11}
\]
and the original analytic Legendre coefficients are interval-certified source data. Exact polynomial derivatives and rational second-derivative bounds yield a whole-support rational enclosure \(0\le T_{J,m}\le M_{J,m}\) for the 1×1 **genuine directional** derivative Gram \(\|r'_{J,m}\|_2^2\). We intentionally DO NOT claim an orthogonal \(H^1\) projection or monotonic \(H^1\) error with increasing m; P is the L² Legendre projector.

**Status: partial authentic source milestone, NOT THE FINAL MATRIX.** The κ=369/10000 high gap is proved for the complement of the full **30** Legendre modes, not for m=1 or 3. The module refuses to mark \`original_30_mode_Q_projection_done\` or \`finite_high_response_DY_computed\`, and cannot feed its m=1/3 output directly into ORS5 as if it were the 30×30 authentic \(T_{r_J}\). Remaining tasks are scaling all 30 projected modes with controlled rational precision and real finite high Y, proving the source bounds are sharp enough for a genuine Schur sign. This is an arithmetic finite-to-global proof instrument, not a Weil-sign proof.

Independent controls: original \`signed_suzuki_g\` 70-digit integration at several J and R, true low Legendre projection from separately written polynomial/OU formula, exact parity-even derivative of odd input, decreasing x-grid enclosure widths, false source/float/extra prime rejection. All numerical comparisons are diagnostic only; source-rational interval arithmetic plus the analytic source identity is the proof basis.


### ORS-03d — first strict original-source derivative inequalities (PROVED LOCAL WITH EXACT OUTWARD FRACTIONS)

The completely source-aligned first-prime directional implementation now produces nontrivial **strict rational inequalities** for the genuine *finite* \(J=2\) signed original \(G_{a,J}\), at \(a=1/2\), with test \(u_1(x)=P_1(2x)=2x\) and genuine L² Legendre projections \(P_1\), \(P_3\):
\[
 \boxed{
 \|((I-P_1)G_{1/2,2}u_1)'\|_{L^2}^2 <\frac1{20},\qquad
 \|((I-P_3)G_{1/2,2}u_1)'\|_{L^2}^2 <\frac1{25}.
 }\tag{ORS12}
\]
The enclosure uses 128 rational x-cells, source analytic (ORS8)–(ORS9), original source signed low-Legendre coefficient intervals (to subtract the correct *L²* projection), and a proven \(L^2\) derivative variation bound; the test compares Fractions **exactly** to 1/20 and 1/25. Diagnostic CI prints the (non-proof) decimal upper approximations ~0.042600 and ~0.034168 respectively. The real theorem is the rational interval inequality, not the printout. No numerical zero data enters.

This is a genuine source-data milestone beyond symbolic source identification, but **its scope is sharply limited**. The high relative Neumann κ estimate is for the first 30 modes, not P1/P3; Γ is truncated at J=2, and the finite response candidate Y and actual \(m=30\) derivative Gram \(T_{(B-DY)'}\) are not computed. Moreover a source-positive omitted Gamma tail does **not** imply a small derivative norm at this J without the separate H¹ tail budget δ_J (large at J=2). Thus ORS12 is neither a sign certificate of the full original \(G_a\) nor a proof of even the first-window completed Weil positivity. It demonstrates that the source-first operator-to-derivative-Gram computation can produce **quantitative, exact, zero-independent inequalities** that future 30-mode attempts can generalize.

A hostile mathematical warning: L² projections \(P_1,P_3\) are **not orthogonal H¹ projections**, so the second upper estimate being smaller is an observed source-specific bound, not a general theorem that residual H¹ energies monotonically decrease with projection rank.
