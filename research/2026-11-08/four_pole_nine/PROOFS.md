# FOUR-POLE NINE — the 3–4–5 source triangle, three-channel correlation and genuine signed debt

**2026-11-08. Research-only; original SUCC base is `main@43a607818907120d4cdab73d240f5b4d7700b63f`.** All statements below are scoped to declared mathematical structures and their given time/source/observer domains. There is **no proof of base-16 normality of π**, no RH proof, no independent academic priority claim, no physical quantization claim. Formal Lean work in the frozen repository is neither altered nor claimed to certify the present results. New claims are paper derivations, accompanied by exact rational local code, a separately implemented SymPy oracle and hostile controls.

## 0. Recover the original source and distinguish the three different "nines"

The historical Bailey–Borwein–Plouffe source (unchanged) is, for each integer `n>=1`,

\[
r(n)=\frac4{8n-7}-\frac2{8n-4}-\frac1{8n-3}-\frac1{8n-2},
\quad U_0=0,\quad U_n=16U_{n-1}+r(n).
\]

Use the **specific source anchor** `a=8n−7`, pole offsets `d=(0,3,4,5)` and signed weights `c=(4,−2,−1,−1)`. They have `Σc=0`. The authentic positive source density is `Q(x)=4−2e^{-3x}−e^{-4x}−e^{-5x}` and Laplace transform

\[
R(a)=\frac4a-\frac2{a+3}-\frac1{a+4}-\frac1{a+5}
=\frac{15a^2+121a+240}{a(a+3)(a+4)(a+5)},\qquad r(n)=R(8n-7).
\]

The user's proposed `4 poles → 3 relative channels → 3²=9` has an **exact mathematical realization** as a three-dimensional zero-sum source coefficient space and its nine-dimensional operator algebra. However, the **Poisson scalar** `1/9` in `G(z)=(2−z)^{-2}` is a separate universal Gamma(2) boundary fact. A two-pole source also has that scalar. The nine complex entries of a matrix are NOT nine independent arithmetic phase measurements, and a three-channel **product** additionally requires third-order joint data.

## FN-01. The original source is uniquely a three-positive-difference system at its pole anchor — PROVED LOCAL

The true forcing splits into **three positive channels**:

\[
\boxed{r(n)=r_3(n)+r_4(n)+r_5(n)},\qquad
r_d(n)=\frac{m_dd}{a(a+d)},\quad (d,m_d)=(3,2),(4,1),(5,1).
\]

Indeed `r_3=2(1/a−1/(a+3))`, `r_4=1/a−1/(a+4)`, `r_5=1/a−1/(a+5)`. The three basis functions `1/a−1/(a+d)` are linearly independent as rational functions because they have distinct simple poles at `−3,−4,−5`, so their coefficients in this anchored basis are **unique**, provided the pole offsets are fixed. All three are positive for `a>0`.

The pole differences **actually form a 3–4–5 Pythagorean triangle**:

\[
3^2+4^2=5^2,\qquad
\prod_{i<j}(d_j-d_i)=120=2^3\cdot3\cdot5.
\]

The nonzero Vandermonde means all four offsets remain distinct modulo every prime `p>5`; primes `2,3,5` are precisely the collision-support exceptions. This is a separate view of the old SUCC exceptional-prime support, not an independent discovery of those prime exceptions.

The source endpoint jets are `Q'(0)=15`, `−Q''(0)=59`, `Q'''(0)=243` from

\[
Q(x)=\sum_{d=3,4,5}m_d(1-e^{-dx}),\qquad
\sum m_dd=15,\ \sum m_dd^2=59,\ \sum m_dd^3=243.
\]

### FN-01b. Two-jet **integer template rigidity** — PROVED LOCAL, sharp hypotheses

**Theorem.** If `x,y,z` are strictly positive integers, `y<=z`, and the *declared source template* has multiplicities `(2,1,1)` with `2x+y+z=15`, `2x²+y²+z²=59`, then **the only** possibility is `(x,y,z)=(3,4,5)`.

**Proof.** Set `s=y+z=15−2x`. Then `y²+z²=59−2x²`, and the discriminant of the quadratic with roots `y,z` is

\[
(y-z)^2=2(59-2x^2)-(15-2x)^2=-107+60x-8x^2.
\]

Nonnegativity forces the integer `x` to be `3` or `4`: the quadratic is strictly negative for all positive integers `x<=2` and `x>=5`. At `x=4`, the discriminant is `5`, not a square. At `x=3`, it is `1` and `y+z=9`, hence `y=4,z=5`. QED.

**Boundary:** arbitrary extra poles, real offsets, changed multiplicities or a kernel perturbation `Q+εe^{-6x}(1−e^{-x})³` can preserve low jets without preserving this exact rational source. Two jets are rigid **only inside the stated three-integer-offset template**. This does not assert that π's digits depend on the 3–4–5 right-triangle equation.

### FN-01c. Three scalar clock samples determine three source amplitudes — PROVED LOCAL

Fix three distinct positive clock parameters `a_i`. In an unknown-amplitude family `r(a)=Σ_{d=3,4,5}t_d d/[a(a+d)]`, three exact measurements form a `3×3` Cauchy system `r(a_i)=Σ_j K_{ij} t_j`, `K_{ij}=d_j/[a_i(a_i+d_j)]`. Its determinant is

\[
\boxed{\det K=\frac{\left(\prod_j d_j\right)
\left(\prod_{i<k}(a_k-a_i)\right)
\left(\prod_{j<l}(d_l-d_j)\right)}
{\left(\prod_i a_i\right)\left(\prod_{i,j}(a_i+d_j)\right)}\ne0.}
\]

Thus exact Gaussian elimination recovers `(t_3,t_4,t_5)=(2,1,1)` from the original source values. Distinct clock times are essential. This authenticates amplitude **in a known pole-offset family**, not arbitrary rational sources.

## FN-02. Three original zero-seeded arithmetic phases, their carry seam and third cumulant — PROVED LOCAL

Let `V_{d,0}=0` and `V_{d,n}=16V_{d,n−1}+r_d(n)`. Linearity gives the unwrapped identity

\[
\boxed{U_n=V_{3,n}+V_{4,n}+V_{5,n}},\qquad
\boxed{e(hU_n)=\prod_{d=3,4,5}e(hV_{d,n})},\quad e(t)=e^{2\pi it}.
\]

Every component has its own exact positive Green tail `T_{d,n}=Σ_{j>=1}16^{-j}r_d(n+j)` and completed point `α_d=Σ_{j>=1}16^{-j}r_d(j)`, so `V_{d,n}+T_{d,n}=16^nα_d` and `Σ_dα_d=π/16`. For an arbitrary other initial seed `s`, the original phase receives an extra `16^ns` contribution; the three **zero-seeded** channels alone must not be substituted for the wrong-seed orbit.

At the real circle level put `x_{d,n}={V_{d,n}}` and `m_n=⌊x_{3,n}+x_{4,n}+x_{5,n}⌋∈{0,1,2}`. Then exactly

\[
\{U_n\}=\left\{\sum_d x_{d,n}\right\},\qquad
\lfloor U_n\rfloor=\sum_d\lfloor V_{d,n}\rfloor+m_n.
\]

For `κ_{d,n}=⌊16x_{d,n-1}+r_d(n)⌋` and original `κ_n=⌊16{U_{n-1}}+r(n)⌋`, the **integer carry seam** is

\[
\boxed{\kappa_n=\sum_d\kappa_{d,n}+m_n-16m_{n-1}}.
\]

This explicitly accounts for what the sum-of-phases quotient forgets. It is a genuine historical three-channel constraint, not a stochastic independence claim.

**π-normality as a three-channel diagonal character.** The empirical law `ν_A` of `(V_{3,n},V_{4,n},V_{5,n}) mod1` over `[A,2A)` pushes forward under circle addition to the actual BBP empirical phase measure. Thus

\[
c_A(h)=\widehat\nu_A(h,h,h)
=\mathbb E_A[Z_3Z_4Z_5],\quad Z_d=e(hV_{d,n}).
\]

Its centered third cumulant is

\[
\kappa_3=E[Z_3Z_4Z_5]-\sum_{i=3,4,5}\mu_i E[Z_jZ_k]
+2\mu_3\mu_4\mu_5,
\]

where `{j,k}={3,4,5}\setminus{i}`, `μ_d=E[Z_d]`, and **no complex conjugation** enters this algebraic cumulant. Replacing pair moments by covariances yields

\[
E[Z_3Z_4Z_5]=\kappa_3+\mu_3\operatorname{Cov}(Z_4,Z_5)
+\mu_4\operatorname{Cov}(Z_3,Z_5)
+\mu_5\operatorname{Cov}(Z_3,Z_4)+\mu_3\mu_4\mu_5.
\]

**Refuted shortcut: nine second-order data entries determine the phase product.** Let `X,Y` be independent uniform `m`th roots of unity, `m>=3`, and `Z=(XY)^{-1}`. All three marginals and all three pair laws are uniform independent, but `XYZ=1` identically. If `Z` is instead an independent uniform root, its complete first- and pairwise laws are identical while `E[XYZ]=0`. This kills unrestricted pairwise-only proof strategies. It is a finite countermodel, **not** a counterexample to any purportedly sourced bound about actual `U_n`.

### FN-02b. A strict *2-adic source gluing* condition — PROVED LOCAL

Because `a=8n−7` is odd and `a+3=4(2n−1)`, `a+5=2(4n−1)`, the individual channels are

\[
r_3(n)=\frac{3}{2a(2n-1)},\quad v_2(r_3(n))=-1;\qquad
r_4(n)=\frac4{a(a+4)},\quad v_2(r_4(n))=2;
\]
\[
r_5(n)=\frac5{2a(4n-1)},\quad v_2(r_5(n))=-1.
\]

Yet the two half-integral classes agree in `Q_2/Z_2` and cancel:

\[
\boxed{r_3(n)+r_5(n)=\frac{11n-4}{a(2n-1)(4n-1)}\in\mathbb Z_2.}
\]

Since the radix multiplier is `16=2⁴`, induction from all three **zero seeds** yields for every `n>=1`

\[
v_2(V_{3,n})=v_2(V_{5,n})=-1,\quad v_2(V_{4,n})=2,
\quad V_{3,n}+V_{5,n}\in\mathbb Z_2,
\quad U_n\in\mathbb Z_2.
\]

One can therefore lose the original denominator/carry passport by projecting the three channels independently. Changing the first multiplicity `2→1` leaves an unpaired valuation `−2` and fails this gluing test. Source-specific, exact, and **still not a theorem transporting 2-adic integrality into real-circle Haar mixing**.

## FN-03. Three relative pole coefficients give a genuine nine-dimensional algebra — PROVED ALGEBRAIC

The balanced coefficient space is `E={v∈R⁴:Σ_iv_i=0}` of dimension three. The original coefficient vector `c=(4,−2,−1,−1)∈E`. Hence `End_R(E)` is nine-dimensional. After choosing the **declared standard Euclidean pole-label metric**, every real endomorphism decomposes uniquely as

\[
\boxed{A=\frac{\operatorname{tr}A}{3}I
+\frac{A-A^T}{2}
+\left(\frac{A+A^T}{2}-\frac{\operatorname{tr}A}{3}I\right),\quad
9=1+3+5.}
\]

These are scalar, skew-adjoint, and symmetric-traceless sectors (formally the `spin 0/1/2` pieces under an **added** orthogonal action). They are not three independent physics particles, and the source's distinct pole shifts and fixed coefficients break full O(3) symmetry. A source's nine pairwise operator entries are **not** automatically nine independent phase constraints. The normalized **positive channel mixture** itself lies in a two-dimensional probability simplex, a different counting problem.

### FN-03b. Chronological projection produces a strictly noncommuting skew sector

Define four rational pole states `v_a=(1/(a+d_i))_i`, projector `P=I_4−11^T/4` and one-step diagonal clock

\[
D_a=\operatorname{diag}\frac{a+d_i}{a+d_i+8},\qquad
v_{a+8}=D_av_a,\quad M_a=P D_aP\big|_E.
\]

The relative state `x_a=Pv_a` **does not evolve autonomously**:

\[
\boxed{x_{a+8}=M_ax_a+\bar v_a P D_a\mathbf1,\qquad
\bar v_a=\tfrac14\sum_i(v_a)_i.}
\]

The second summand is the common-mode injection lost by prematurely quotienting. The historical source scalar is `r(a)=c^T x_a`. These are exact source-labelled rational linear maps, not physical oscillator assumptions.

Put `u_a=P D_a1`. For any `a,b>0`,

\[
\boxed{[M_a,M_b]=-	frac14(u_au_b^T-u_bu_a^T)\big|_E.}\tag{FN-03}
\]

**Nonzero and sharp norm, for every `a≠b`.** For pole offsets `d=(0,3,4,5)` let `\Delta_{ijk}=(d_j-d_i)(d_k-d_i)(d_k-d_j)`. Then

\[
\boxed{\|[M_a,M_b]\|_{\rm op}^2
=64(a-b)^2\sum_{i<j<k}
\frac{\Delta_{ijk}^2}
{\prod_{t\in\{i,j,k\}}(a+8+d_t)^2(b+8+d_t)^2}>0.}\tag{FN-04}
\]

**Proof.** The commuting diagonals cancel from `P D_aP D_bP−P D_bP D_aP`, leaving the displayed antisymmetric wedge. Its two nonzero singular values are each `\sqrt{\|u_a\|²\|u_b\|²−(u_a\cdot u_b)²}/4`. Cauchy–Binet for the `4×3` matrix `[1/2·1,u_a,u_b]` reduces the Gram determinant to one quarter the sum of squared `3×3` determinants of `[1,D_a1,D_b1]`. Each determinant has absolute value

\[
\frac{64|a-b|\,|\Delta_{ijk}|}{\prod_{t\in\{i,j,k\}}(a+8+d_t)(b+8+d_t)}.
\]

This proves FN-04. Its numerator is strictly positive since `a≠b` and every triple of distinct pole shifts has `Δ≠0`. Exact antisymmetric rank is two. QED.

For actual consecutive clock parameters `b=a+8`, let `p=P(0,3,4,5)^T`, `q=P(0,9,16,25)^T`. Taylor expansion at `a=∞` gives

\[
\boxed{a^6[M_a,M_{a+8}]\longrightarrow-128(pq^T-qp^T),\quad
\lim_{a\to\infty}a^6\|[M_a,M_{a+8}]\|_{\rm op}=128\sqrt{362}.}\tag{FN-05}
\]

Here `\|p\|²=14,\|q\|²=337,p\cdot q=66`, so `14·337−66²=362`. The four squared Vandermonde minors are `144,900,400,4`, totaling `1448=4·362`. The independent symbolic oracle verifies **all sixteen** exact commutator entries, all sixteen asymptotic entries, and the closed norm formula; strict nonvanishing has the analytic proof above.

**What this is NOT.** Swapping the projectors `M_a,M_b` compares **counterfactual orders** of source-clock operators after a chosen Euclidean quotient; real arithmetic time still advances in its fixed order with the missing common scalar injected. This is a valid *observer ordering defect*, not automatic physical/connection curvature. The matrices depend on pole **positions**, not the original signed **multiplicities**: mutating weights while keeping shifts preserves the commutator. Also `c^T[M_a,M_b]c=0` by antisymmetry. No source-selective signed Weyl decay follows from a `O(a^-6)` summable defect.

## FN-04. The universal 1/9 Poisson kernel is *not* the source's nine-dimensional invariant — PROVED NEGATIVE

The Gamma(2) endpoint and unit source observation clock give

\[
G_\infty(z)=(2-z)^{-2},\quad
|G_\infty(e^{i\theta})|=\frac1{5-4\cos\theta}\in[1/9,1].
\]

The `5=4+1` arises from `|2-z|²`; the `9` comes from `z=−1`, where `|2-z|²=3²`. By contrast, **a two-pole** positive Laplace source `Q_{\rm fake}(x)=1-e^{-x}` has `R_{\rm fake}(a)=1/[a(a+1)]`, also a simple endpoint zero, also Gamma(2), and therefore **the same** observer `G_\infty` and sharp `1/9`. Its pole-balance coefficient space has dimension one and `End` has dimension one, not nine.

Hence the numerical coincidences `3²=9`, Pythagorean offset `5`, and disk-kernel `5,9` are authentic algebraic observations **but not a proved shared source invariant**. A proof must transport a specific source-dependent component, not just match integers.

## FN-05. Source-specific finite golden fixed-point drift — PROVED LOCAL

This is where the **authentic** `15,59` jets do enter golden observation quantitatively. Define the exact continuous-clock **mixed-Poisson observation law** from the original positive BBP source:

\[
\boxed{G_a(z)=\mathbb E_{\mu_a}\exp[-a(1-z)X]
=\frac{R(a(2-z))}{R(a)},\qquad 0\le z\le1.}
\]

This is a genuine probability generating function: conditional on `Y=aX`, choose a Poisson(`Y`) count. **This auxiliary count is not a hexadecimal digit of π**, nor is it asserted equal to the repository's finite-depth Bernoulli/Pascal count (though both have the same Gamma(2) scaling limit).

Write

\[
F(a)=a^2R(a)/15=\sum_{d=3,4,5}\frac{m_dd}{15}\frac a{a+d}.
\]

Every summand increases strictly to its mass, so `0<F(a)<1`, `F'(a)>0`, `F(a)→1`. Moreover `aF'(a)/F(a)` is a convex combination of `d/(a+d)∈(0,1)`, hence

\[
1<G_a'(1)=2-aF'(a)/F(a)<2.
\]

Strict convexity of the mixed-Poisson PGF ensures a **unique interior fixed point** `q_a∈(0,1)`. Since `F(a(2-z))>F(a)` for every `0≤z<1`,

\[
G_a(z)>(2-z)^{-2},\qquad
\boxed{q_a>q_\star:=\varphi^{-2}=\frac{3-\sqrt5}{2}}.
\]

The source expansion `R(a)=15a^{-2}−59a^{-3}+243a^{-4}+O(a^{-5})` is uniform under `a→a(2-z)` near `z=q_*`. Therefore

\[
G_a(z)=(2-z)^{-2}
\left[1+\frac{59}{15a}\left(1-\frac1{2-z}\right)+O(a^{-2})\right].
\]

At `q_*`, `2−q_*=φ`, the limiting derivative is `2φ^{-3}=2λ³<1`, and the analytic implicit-function expansion proves the **unconditional original-positive-source theorem**

\[
\boxed{q_a=\varphi^{-2}+\frac{59(5-\sqrt5)}{150a}+O(a^{-2}).}\tag{FN-06}
\]

This rate is a source fingerprint: the two-pole fake `Q_fake(x)=1−e^{-x}` has the **same** Gamma(2), golden limit and `1/9` disk kernel, but `m_2/m_1=1`, so its `1/a` golden drift coefficient is `(5−√5)/10`, not `59(5−√5)/150`. It demonstrates an actual source-dependent golden **observer correction**. It does **not** show that this scalar correction controls the selected real signed covariance.

At the Gamma rank-two limit, the log moment is `ψ(2)=1−γ`, and the declared golden contrast is `λ−γ` (Oily–Macaroni). The present `q_a` drift contains the genuine four-pole `59/15`; the absolute `γ` term does not appear in the signed orbit's cross-time phase without a proved coupling. Do not insert it into a complex character by hand.

## FN-06. A deliberately complete nine-component observer still has a scalar Weyl bottleneck — PROVED NEGATIVE

Define **positive channel probabilities** `w_d(a)=r_d(a)/R(a)` and their real Hilbert amplitudes `\eta_d(a)=\sqrt{w_d(a)}`. The normalized first-jets imply

\[
w_\infty=(6,4,5)/15,\quad
\eta_\infty=(\sqrt{6/15},\sqrt{4/15},\sqrt{5/15}).
\]

The exact ratios satisfy `1/(1+5/a)≤w_d(a)/w_d(∞)≤1+5/a`, because the source clocks `a/(a+d)` lie between `a/(a+5)` and `1`. Taking square roots and summing gives the **uniform genuine-source bound**

\[
\boxed{\|\eta(a)-\eta_\infty\|_2\le\frac5{2a}.}
\]

For **any** unit-phase sequence `z_n` (in particular `z_n=e(hU_n(s))` for any seed) and every integer epoch `[A,2A)`, set

\[
\mathbf W_{A,h}=A^{-1}\sum_{n=A}^{2A-1}z_n\eta(8n-7),\quad
W_A=A^{-1}\sum_{n=A}^{2A-1}z_n.
\]

Then **independently of any genuine phase-cancellation estimate**

\[
\boxed{\|\mathbf W_{A,h}-\eta_\infty W_A\|_2
\le\frac5{2(8A-7)}.}\tag{FN-07}
\]

Consequently the Hermitian nine-entry matrix `\mathbf W\mathbf W^*` is rank one, and asymptotically differs from `|W_A|²\eta_\infty\eta_\infty^T` by at most `2ε_A+ε_A²` in operator norm (`ε_A=5/[2(8A−7)]`). Thus the obvious **three-channel second-order positive lift** does not supply a new cancellation estimate; it asymptotically carries the same scalar Weyl problem. The coherent same-forcing nonnormal seed `s_*=-π/16` has `z_n=e(-hT_n)→1`, and the lifted norm likewise tends to one.

**Verdict:** `3×3=9` is a legitimate representation capacity; it is not a free guarantee of nine independent signed constraints. The joint *third-order* character, integer carry seam and source-specific chronology remain the prospects worth attacking.

## FN-07. Claim-status summary and the remaining arithmetic gate

**PROVED LOCAL (paper + exact algebra):** all-source signed/positive decomposition; restricted two-jet rigidity; three-clock Cauchy identification; three-torus phase/carry seam; odd-denominator 2-adic gluing; `1+3+5` operator decomposition; nonzero clock-projector commutator with closed norm and asymptotic; source-dependent golden fixed-point drift; nine-entry rank-one collapse.

**REFUTED with explicit countermodels:** universal `4 poles ⇒ 1/9` (two-pole Gamma(2) source); nine pairwise entries determine a general three-phase product (finite roots-of-unity triple); source-only skew commutator automatically gives real selected cancellation (same-seed/source-only / `c^T[C]c=0`); any larger positive source-vector measurement forces normality (coherent wrong seed). These are refutations of the **specified implications**, not π normality.

**OPEN:** the authentic zero-seed signed character `c_A(h)=\widehat\nu_A(h,h,h)→0` for every fixed `h≠0` and all integer `A→∞`, equivalent to base-16 π normality. The triple cumulant decomposition is exact but no termwise or total asymptotic decay has been shown. Connecting the genuine 2-adic half-integral carry-gluing condition, the rank-three time-ordered observer and the literal zero boundary to a *signed* all-epoch estimate remains a pathway/probe gap. The coherent same-forcing seed and terminal-denominator/carry shadows from PR #544 must be hostile controls.

**Next falsifiable experiment:** study a declared *source-and-carry-conditioned* third-order mixed Fourier statistic on the three zero-seeded component histories. Predict different behavior on authentic zero versus original-forcing wrong seeds and a source-mutant with same Gamma rank. Require the full joint phase/historical labels; no phase-free `a^-6` commutator or scalar golden drift can count as cancellation. Use exact rational/interval finite oracles with fresh holdouts; then seek an actual universal inequality. If no discriminator survives those controls, the `3×3` construction is an observer representation, not a proof engine.

## Provenance and independent checks

- Original BBP: Bailey–Borwein–Plouffe (1997), Theorem 1, four signed rational poles, and SUCC `provenance/IMPORT_MANIFEST.json` (original unchanged).
- Inherited source geometry: `research/2026-10-29/recursive_carrier_triangle/ATOMIC_SOURCE_AND_INTERACTIONS.md`, `docs/OPERATIONAL_TRIANGLE.md` (Gamma/Poisson and golden fixed point), `research/2026-10-26/OILY_MACARONI_SOURCE_MELLIN_HILBERT.md`, `research/2026-11-08/fibonacci_circle_triangle/` (draft PR #549), and `research/2026-11-08/signed_covariance_round2/` (draft PR #544). The last two are **read-only**; no merge/rebase assumed.
- Exact Python/stdlib: `observational_succ/four_pole_nine.py`; new root-discoverable `tests/test_four_pole_nine.py` (34 focused tests in isolated replay).
- Independent symbolic oracle (SymPy, separately constructs the source/operator): `research/2026-11-08/four_pole_nine/independent_sympy_oracle.py` + `INDEPENDENT_EXACT_RECEIPT.json`.
- Prospective finite signed diagnostics: `finite_signed_probe.py` and `FINITE_SIGNED_DIAGNOSTIC.json`; these use ordinary floating complex phases and provide **NO infinite authority**.
- Full repository suite, hosted CI and new Lean kernel proofs are not asserted by local paper/test runs; see `VALIDATION.md` and exact-head checks when available.
