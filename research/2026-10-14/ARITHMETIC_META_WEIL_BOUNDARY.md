# ARITHMETIC META-SUCC — Source-realized prime/Gamma interactions, boundary commutator, and a certified Weil moment-subspace theorem

**Research checkpoint:** October 14, 2026. **Source:** `femboy2112/SUCC`, exact parent `research/recursive-meta-interaction-coercivity-2026-10-14@cc0d50bb2585db254cf865c66522b9a356eb9d4d` (PR #80), itself descending from the source-completed Weil line via PR #77. **Branch:** `research/arithmetic-meta-weil-boundary-2026-10-14`. **RH PROVED: NO.** The author seeks a genuinely arithmetic realization of the meta-interaction machine, not a fitted positive operator. The results below are explicitly **source-conditional mathematical theorems**; none authenticates physical observations or supplies RH's full all-test sign. Classic source facts and earlier SUCC work are credited. **Academic priority: UNVERIFIED.**

## 0. Intake, acceptance criteria and mathematical status

Existing exact ancestry: PR #80 provides conditional source-labeled unitary connection Laplacians and `1/23` coercivity for two specially chosen noncommuting-reflection holonomies. PR #71 gives the completed signed Weil distribution from the authentic Euler/Gamma source; PR #70 identifies the complete real-place Gamma Markov/Carleman ladder and prime dilations; PR #76 studies a signed Fourier decomposition and derives a high-frequency multiplier moat; Suzuki's 2026 v3 paper provides the classical full Weil/Suzuki formulas, including its correct analytic domains. **No** part of that ancestry gives an independent proof that genuine prime and real-place actions instantiate PR #80's incompatible holonomies.

Acceptance before experimenting:

1. Every arithmetic edge is a genuine prime-power Euler/FUCC action, not a freely invented matrix. All source weights must be `w_{p^k}=log(p)/sqrt(p^k)` in the half-density chart; `6` is not a primitive jet.
2. The Gamma edge is taken from the **original one-Gamma real place**, not a separate independently supplied positive bath, with the contact normalization unchanged.
3. Derive an actual common-carrier operator identity for the **whole signed** compact Weil form: Gamma, prime powers, scalar contact, and positive/negative pole terms. Never infer the latter from an unrelated Gram.
4. The parent joint-holonomy positive gap may be used only if the arithmetic transports actually have its nonflat unitary holonomies. If the authentic arithmetic transports commute, record the no-go, not a substitute model.
5. Produce at least one whole-test-space **nontrivial** rigorous inequality with explicit constants, and retain exact source/analytic/numerical controls, the provenance and the missing RH arrow.

Results: AMW-01 to AMW-08 below. AMW-04 yields a **strict source-realized operator commutator** from window boundary leakage; AMW-06 yields **genuine completed Weil positivity on a codimension-101 infinite-dimensional subspace of the first-prime window**, with an entirely rational certificate of explicit constants. A further independent hostile refinement **AMW-06B strengthens this to codimension 30**, retaining the same complete source and an exact positive rational margin. AMW-07 is a source-first sufficient *conditional* finite-Schur validation instrument. The full form on the original unrestricted test class remains RH-hard.

## 1. AMW-01. Arithmetic prime sources and one real-place chart (CLASSICAL / PROVED LOCAL)

Set the continuous radial carrier `H_r=L²(R_+,dr)` and logarithmic carrier `H_x=L²(R,dx)`. The half-density chart

\[
(Uf)(x)=e^{x/2}f(e^x)
\]

is unitary: substituting `r=e^x`,

\[
\int_\mathbb R |Uf(x)|^2 dx=\int_0^\infty|f(r)|^2dr.
\]

The exponent `1/2` is forced for this fixed choice of measures: for `U_αf(x)=e^{αx}f(e^x)`, the norm is `∫r^{2α-1}|f(r)|²dr`, so it equals the original norm for all `f` iff `α=1/2`. The `f=1_[1,2]` exact control has squared transformed norms `1` at `1/2` and `3/2` at exponent `1`.

For a genuine prime `p`, define the **continuous pullback**

\[
(V_pf)(r)=\sqrt p\,f(pr).
\]

It is unitary on `H_r`, and `UV_pU^{-1}=T_{\log p}` with `(T_bv)(x)=v(x+b)`. This continuous Hilbert dilation is a model of the multiplicative arithmetic action; it does **not** identify `\ell²(N)` point masses with `L²(R_+)` vectors. The discrete arithmetic `n→pn` on `\ell²(N)` is an isometry, not surjective; that distinction is retained.

Authentic Euler data are separate: the Dirichlet-log source has atoms at `n=p^k` with source weight `Λ(n)=log p`; after half-density this gives `w_n=Λ(n)/√n>0`. Exact unique factorization is the source validation. A dilation at `6` exists as an analytic operator but `Λ(6)=0`: it cannot be installed as an independent primitive Euler source. The implemented `prime_power_jet` rejects it. Real primitive Dirichlet character `χ₄` already changes sign at `3` and changes its conductor and Gamma parity; it is an intentionally mismatched control, **not** a positive-zeta source.

The **actual real-place** first Gamma/Carleman layer on `H_x` is convolution

\[
(C_0v)(x)=\int_\mathbb R\nu_0(x-y)v(y)dy,
\qquad \nu_0(t)=\frac1{2\cosh(t/2)}.
\]

This is exactly `UC U⁻¹`, where `(Cf)(r)=∫f(s)/(r+s)ds`, the classical positive Carleman operator. It is a genuine component of the completed one-Gamma ladder, **not** a new independent Gamma assigned to each prime. For `k≥0`, set

\[
\nu_k(t)=\frac{e^{-k|t|}}{2\cosh(t/2)},\quad
k_G(t)=\frac{e^{-|t|/2}}{1-e^{-2|t|}}=\sum_{k\ge0}\nu_k(t),\quad t\ne0.
\]

The identity is geometric summation. Thus the positive Gamma jump form (on its natural form domain) is

\[
\mathcal E_G(v)=\frac12\int_{\mathbb R^2} k_G(x-y)|v(x)-v(y)|^2dxdy
=\int_0^\infty k_G(t)\|T_tv-v\|_2^2dt\ge0.
\tag{AMW-1}
\]

Each summand `ν_k` is a positive Markov jump kernel; the full `k_G` has infinite total jump rate, so do not replace it by one finite-rate compound Poisson process. For `v∈C_c^∞`, (AMW-1) is finite: near zero the numerator is `O(t²)` and `k_G(t)~1/(2t)`; at infinity `k_G` decays exponentially.

## 2. AMW-02. Exact identification of the positive interaction model *inside* completed Weil (CLASSICAL identity, source-preserving new-to-SUCC meta interface)

Let `a>0`, `v∈C_c^∞(-a,a)` zero-extended to `R`, and let

\[
P_a=\{n=p^k:n<e^{2a}\},\quad b_n=\log n,\quad w_n=\frac{\log p}{\sqrt{p^k}},\quad C_G=\gamma+\frac\pi2+3\log2+\log\pi.
\]

The source-identified Suzuki/Weil identity (the *signed* expression, imported and re-derived in previous SUCC PRs) is

\[
\boxed{\begin{aligned}
Q_\zeta(v)={}&\mathcal E_G(v)-C_G\|v\|_2^2
+2|\langle v,c\rangle|^2-2|\langle v,s\rangle|^2\\
&-2\sum_{n\in P_a}w_n\operatorname{Re}\langle T_{b_n}v,v\rangle,
\qquad c(x)=\cosh(x/2),\;s(x)=\sinh(x/2)
\end{aligned}}
\tag{AMW-2}
\]

where `c,s` are paired only against the supported `v`. Compact support makes the true prime sum finite; `n=e^{2a}` lies on the vanishing endpoint and contributes zero. The original completed **pole**, scalar **contact**, prime source, and **Gamma** are present; no zero locations are inputs. The existing signed Weil equality itself is CLASSICAL, not our new theorem.

For any unitary `T_b` on full `H_x`, the exact polarization identity is

\[
\|T_bv-v\|_2^2=2\|v\|_2^2-2\Re\langle T_bv,v\rangle.
\]

Define the source-identified *positive* meta-interaction energy

\[
\mathscr D_a(v)=\mathcal E_G(v)+\sum_{n\in P_a}w_n\|T_{b_n}v-v\|_2^2\ge0.
\]

Then the **complete exact relation** is

\[
\boxed{
Q_\zeta(v)=\mathscr D_a(v)
-\underbrace{\left(C_G+2\sum_{n\in P_a}w_n\right)}_{D_a}\|v\|_2^2
+2|\langle v,c\rangle|^2-2|\langle v,s\rangle|^2.
}
\tag{AMW-3}
\]

The term `D_a` is **negative** in `Q`, and `c,s` have opposite polar signs. One cannot call `Q=||Bv||²` by forgetting them. (AMW-3) gives an actual source-identified positive **sub-form plus a signed deficit**, a useful input to recursive Meta-SUCC. It does *not* prove its deficit absorbed.

**Exact finite calibration.** For any finite rational vector indexed on an integer log clock and zero-extended, the identity `||T_mv-v||²-2||v||²=-2<T_mv,v>` holds as a Fraction identity. The Python suite exhaustively checks lengths 1–5 with entries in `{-2,-1,0,1,2}` and shifts 1,2,3,8; source weights remain separately tagged and no floating equality is used. This is a calibration of the algebra, **not** an identification of discrete samples with the continuum Weil operator.

## 3. AMW-03. Flat genuine prime/Gamma holonomy: an exact no-go (CLASSICAL/PROVED LOCAL)

The primal `T_{\log p}` are translations on the same `H_x`; hence

\[
T_{\log p}T_{\log q}=T_{\log q}T_{\log p},\quad
T_b C_0=C_0T_b,
\quad T_b\mathcal E_G T_b^{-1}=\mathcal E_G.
\]

The second follows by convolution/Fubini on a core, then bounded extension; the last by translation invariance of the closed quadratic form. At the integer source, `V_p V_q=V_q V_p` and `ν(pq)=ν(p)+ν(q)`. Every genuinely **closed source-prime word** has trivial product on every valuation coordinate, hence translation holonomy `I` after the half-density transport.

Therefore **there is no nontrivial unitary holonomy manufactured by simply looping genuine prime dilations against the translation-invariant original Gamma ladder**. In particular the chosen incompatible-reflection holonomies `diag(1,-1)` and `diag(-1,1)` of PR #80 do not descend automatically from these actions. Transplanting PR #80's `1/23` gap would be an unlicensed source substitution. The `χ₄` twist has a completely multiplicative scalar factor and also commutes on genuine prime squares; it is not a license for such reflections.

This is the first substantial *negative verdict*: the obvious connection-Laplacian moonshot is **refuted within the declared authentic translation representation**, not RH. A repair must identify a different genuine source structure (e.g. boundary interfaces, noncommuting lawful additive operations, or an independently justified nonabelian arithmetic representation) and prove the required domain/gap laws.

## 4. AMW-04. **The boundary creates a true source-derived noncommuting square** (PROVED LOCAL, quantified)

Let `W=(0,L)`, `P` the multiplication projection onto `W`, `T_bf(x)=f(x+b)` for `b=log2>0` the genuine prime-2 continuous dilation, and `C_0` the actual Carleman/Gamma convolution above. Define the bounded compressed operators

\[
S_{W,b}=P T_bP|_{L²(W)},\qquad K_W=P C_0P|_{L²(W)}.
\]

`T_b` and `C_0` commute on the full logarithmic carrier, but **not after source-preserving compression to a proper finite observational window**. For any projection P and bounded commuting U,K, direct operator algebra gives the *exact* boundary leakage square:

\[
\boxed{[PUP,PKP]= -PU(I-P)KP+PK(I-P)UP.}
\tag{AMW-4}
\]

The right side retains two separately sourced outside-window interfaces. It is not an arbitrary holonomy phase. Reintroducing the boundary carrier restores global commutation and makes the apparent noncommutation a precisely localized projection/backaction effect.

**Explicit theorem:** for `L=1` (the centered Suzuki window `a=1/2`, translated), with `b=log2`,

\[
\boxed{\|[S_{W,b},K_W]\|_{L²(W)\to L²(W)}>\frac3{22}.}
\tag{AMW-5}
\]

**Proof.** As `2/3<log2<7/10<1`, put `δ=(1-b)/2`, so `0<δ<min(b,1-b)`. Let `f=δ^{-1/2}1_{(1-δ,1)}` (`||f||₂=1`). For every `x∈(1-b,1)`, `(S_{W,b}K_W f)(x)=0` because `x+b>1`; whereas `S_{W,b}f=δ^{-1/2}1_{(1-b-δ,1-b)}`. Consequently

\[
(K_WS_{W,b}f)(x)=δ^{-1/2}\int_{1-b-δ}^{1-b}\nu_0(x-y)dy
\ge\sqrt δ\,\nu_0(b+δ),
\]

since `ν₀` is positive and decreasing on positive arguments, and `0≤x-y≤b+δ`. Integrating over a set of measure `b`,

\[
\|[S_{W,b},K_W]f\|_2\ge\sqrt{bδ}\,\nu_0(b+δ).
\tag{AMW-6}
\]

For a **fully rational** strict lower bound: `b>2/3` and `δ>3/20` imply `bδ>1/10` and `sqrt(bδ)>3/10`. Furthermore `t=(b+δ)/2=(1+b)/4<17/40`, and, for `0<t<17/40`,

\[
\cosh t\le (1-t²/2)^{-1}
<\left(1-(17/40)^2/2\right)^{-1}
=\frac{3200}{2911}<\frac{11}{10}.
\]

Thus `ν₀(b+δ)>5/11` and the product in (AMW-6) is strictly greater than `(3/10)(5/11)=3/22`. The elementary bound `log2>2/3` comes from the first term of `log2=2 atanh(1/3)`; its tail bounded by replacing `1/(2j+1)` by `1/3` gives `log2<25/36<7/10`. This proves (AMW-5) without spectral sampling, unknown zeros, or numerical intervals. The indicator `f` lies in L² where both bounded compressed operators are defined; by density, smooth compact witnesses also have a nonzero commutator. QED.

**Exact dyadic rational shadow:** at grid sites `x_j=2j log2`, a genuine prime-square (`p²=4`) shift takes adjacent sites to one another. The true first Carleman kernel **evaluated** at those sites is

\[
\nu_0(2m\log2)=\frac{2^{|m|}}{4^{|m|}+1}\in\mathbb Q.
\]

For a three-site projection, the sampled Toeplitz kernel has rows `(1/2,2/5,4/17)`, `(2/5,1/2,2/5)`, `(4/17,2/5,1/2)`, while the truncated one-step shift is nilpotent. Their commutator has `(0,0)` entry exactly `2/5`. This is an independent **finite rational calibration** of boundary noncommutation; bare kernel samples are NOT exact Galerkin coefficients and are not the proof of (AMW-5).

**Critical distinction:** `S_{W,b}` is a **contraction, not unitary**. Its nonzero commutator is genuine boundary leakage, not a nontrivial unitary holonomy. The PR #80 theorem about positive gaps from incompatible *unitary* holonomies cannot be invoked here. Doing so would silently cross an operator-domain boundary. The quantified commutator is nonetheless an authentic example of the author's requested second-order “models of model interactions” producing a new observable law absent from either isolated model.

## 5. AMW-05. Global multi-model dispersion has NO whole-carrier spectral gap (PROVED obstruction)

For any finite authentic prime-power set `P` with `w_n>0`, define on full `L²(R)`

\[
\mathscr D_P(v)=\mathcal E_G(v)+\sum_{n\in P}w_n\|T_{\log n}v-v\|_2^2.
\]

This form is nonnegative, with trivial L² kernel. Indeed, `E_G(v)=0` implies that `T_t v=v` for almost every `t>0`; a nonzero L² function cannot be translation invariant, so `v=0`.

**But** there is no `κ>0` such that `D_P(v)≥κ||v||²` for all supported smooth v on the whole real line. Fix nonzero `φ∈C_c^∞(R)` with unit L² norm and set `v_L(x)=L^{-1/2}φ(x/L)`. Then `||v_L||=1`, while

\[
\|T_tv_L-v_L\|²\le t²L^{-2}\|φ'\|².
\]

Because `∫₀^∞t²k_G(t)dt<∞` and `P` is finite,

\[
0\le\mathscr D_P(v_L)
\le\frac{\|φ'\|²}{L²}
\left(\int_0^\infty t²k_G(t)dt
+\sum_{n\in P}w_n(\log n)²\right)\xrightarrow[L\to\infty]{}0.
\]

Hence **trivial kernel does not imply uniform coercivity** on this infinite-dimensional carrier. This is the authentic arithmetic/Archimedean counterpart to PR #80's bilateral-shift countermodel. The fixed observation window changes the situation by adding a boundary barrier, but it cannot be replaced by a fabricated frustration gap.

## 6. AMW-06. **Exact infinite-dimensional first-prime Weil positivity with 101 moment constraints** (PROVED LOCAL, rational certificate)

Let `a>0` be fixed, and let

\[
\mathcal V_{a,N}=\bigl\{v\in C_c^∞(-a,a):\int_{-a}^a x^jv(x)dx=0\ \forall 0\le j\le N\bigr\}.
\]

This is an infinite-dimensional subspace: if `φ∈C_c^∞(-a,a)`, then `v=φ^{(N+1)}` lies in it by repeated integration by parts; varying φ gives infinitely many independent examples.

Let `α_j=2j+1/2` and define the genuine Gamma symbol

\[
M_G(ξ)=\sum_{j=0}^{∞}\frac{2ξ²}{α_j(α_j²+ξ²)}\ge0,
\qquad
E_G(v)=\frac1{2π}\int_\mathbb R M_G(ξ)|\hat v(ξ)|²dξ.
\tag{AMW-7}
\]

Every term is nonnegative and increases with `|ξ|`; the sum diverges only logarithmically at high frequency. For integer `J≥1`, `T>0`, define the finite exact lower bound

\[
L_J(T)=\sum_{j=0}^{J-1}\frac{2T²}{α_j(α_j²+T²)}\le M_G(T).
\]

For `v∈V_{a,N}`, Fourier moment annihilation allows one to subtract the degree-N Taylor polynomial from `e^{-iξx}` inside the Fourier integral. On `|ξ|≤T`, Taylor's remainder and Cauchy–Schwarz give

\[
|\hat v(ξ)|\le\sqrt{2a}\|v\|_2\frac{e^{aT}(aT)^{N+1}}{(N+1)!}.
\]

By integrating this over the bounded frequency band and dividing by `2π`,

\[
\frac1{2π}\int_{-T}^{T}|\hat v(ξ)|²dξ
\le\epsilon_N(a,T)\|v\|²,
\quad
\epsilon_N(a,T)=\frac{2aT}{π}\frac{e^{2aT}(aT)^{2N+2}}{((N+1)!)²}.
\tag{AMW-8}
\]

For `ε_N<1`, Plancherel and monotonicity now yield the **uniform all-test** inequality

\[
\boxed{E_G(v)\ge L_J(T)(1-\epsilon_N(a,T))\|v\|²
\quad\forall v\in\mathcal V_{a,N}.}
\tag{AMW-9}
\]

The full completed Weil formula (AMW-2), using `|Re⟨T_bv,v⟩|≤||v||²`, discarding only the **positive** pole term, and bounding the negative pole by Cauchy–Schwarz with `||s||²=\sinh a-a`, gives

\[
\boxed{
Q_\zeta(v)\ge
\left[L_J(T)(1-\epsilon_N(a,T))
-C_G-2\sum_{n\in P_a}w_n-2(\sinh a-a)\right]\|v\|²,
\quad v\in\mathcal V_{a,N}.}
\tag{AMW-10}
\]

This is a **constructive finite-codimensional positivity principle** for every fixed `a`: by the logarithmic unboundedness of `M_G(T)` (elementarily, take `T=2J`, then `L_J(2J)≥∑_{j<J}1/α_j→∞`) and the factorial decrease of `ε_N` for fixed `a,T`, some explicit sufficiently large `J,T,N` make the bracket positive. This general qualitative phenomenon has classical precedents in Yoshida and Suzuki; **the fully exact worked first-prime instance below is the project's new certified instrument.**

### An explicit fully rational prime-2 certificate (new-to-SUCC quantified instance)

Set `a=1/2`; then `2<e^{2a}=e<3`, so the **only** genuine prime-power source is `n=2` with `w_2=log2/sqrt2`. Choose exactly

\[
T=40,\quad J=75,\quad N=100.
\]

The first comparison is a **finite rational sum** with `α_j=(4j+1)/2`:

\[
\boxed{L_{75}(40)>\frac{359}{50}.}
\tag{AMW-11}
\]

The second comparison is proved by a rational majorant using `π>3`, `e<4` and `2aT=40`:

\[
\boxed{\epsilon_{100}(1/2,40)
<\frac{40}{3}\frac{4^{40}20^{202}}{(101!)²}
<\frac1{100}.}
\tag{AMW-12}
\]

Both inequalities are independently recomputed by `fractions.Fraction` exact integer cross-multiplication in the focused suite and deterministic receipt. They do **not** rely on mpmath eigenvalues or floating-point spectra.

For the complete **signed** remainder, elementary classical inequalities suffice:

\[
C_G<6,\qquad 2w_2<1,
\qquad 2\|\sinh(x/2)\|_{L²(-1/2,1/2)}²
=2(\sinh(1/2)-1/2)<1/20.
\]

Details: `γ<1`, `π<16/5`, `log2<7/10`, and `logπ<6/5` (from the fourth positive Taylor partial sum of `exp(6/5)>16/5`) give `C_G<1+8/5+21/10+6/5=59/10<6`. The bound `w_2<1/2` follows from `log2<7/10` and `sqrt2>7/5`. For the hyperbolic remainder use its positive power series: after the term `1/48`, the remaining terms form a series bounded by `2/3840=1/1920`, so `sinh(1/2)-1/2<41/1920<1/40`. Hence the source-defined negative budget in (AMW-10) is strictly less than `141/20`.

Putting the exact inequalities into (AMW-10), for **every** nonzero `v∈V_{1/2,100}`,

\[
\boxed{\begin{aligned}
Q_\zeta(v)
&>\left(\frac{359}{50}\frac{99}{100}-\frac{141}{20}\right)\|v\|_2²\\
&=\boxed{\frac{291}{5000}\|v\|_2²>0.}
\end{aligned}}
\tag{AMW-13}
\]

**This theorem is for an infinite-dimensional space of smooth compactly supported functions, not a finite Gram experiment**. It includes the genuine prime-2 contribution and every real-place/pole/contact term. It is a genuine, explicit, source-first positivity statement *inside the authentic completed Weil form*. It does not establish positivity of the remaining 101-dimensional low-moment sector nor of its cross-couplings with the complement, and hence it does **not** prove RH or even full positivity at this one radius.

### A safety-critical sign note

AMW-13 used `Q_W=E_G - C_G ||v||² + (positive polar) - (negative polar) - 2 real prime correlations`, **not** `Q_W=E_G+ positive prime graph energy`. The latter omits `-2w_2||v||²` and is wrong. The signed deficit remains in all theorem bounds. A fake primitive composite or a wrong half-density invalidates the theorem's declared arithmetic/source contract even if it accidentally preserves a similar numerical inequality.


### AMW-06B. Stronger **30-moment** all-test certificate (PROVED LOCAL / exact rationals)

The preceding use of `e^{aT}` in the Taylor remainder is valid but wasteful. For real `y`, the **integral remainder formula** gives

\[
 e^{iy}-\sum_{j=0}^{N}\frac{(iy)^j}{j!}
 =\frac{(iy)^{N+1}}{N!}\int_0^1(1-t)^Ne^{ity}dt,
 \qquad
 \left|e^{iy}-\sum_{j=0}^{N}\frac{(iy)^j}{j!}\right|
 \le \frac{|y|^{N+1}}{(N+1)!}.
\]

The reason is mathematical, not numerical: the intervening phase has modulus **exactly one**. Thus no exponential growth factor is needed on the bounded real Fourier interval. The sharper uniform concentration theorem is

\[
\frac{1}{2\pi}\int_{-T}^T|\hat v(\xi)|^2d\xi
\le \widehat\epsilon_N(a,T)\|v\|^2,
\qquad
\widehat\epsilon_N(a,T)
=\frac{2aT}{\pi}\frac{(aT)^{2N+2}}{((N+1)!)^2}.
\tag{AMW-15}
\]

This uses the **same** infinite-dimensional space `V_{a,N}` and source; all other parts of the proof of AMW-10 remain unchanged.

Set `a=1/2`, `T=21`, `J=75`, and `N=29`. The independent 75-term Fraction comparison and exact factorial comparison establish

\[
\boxed{L_{75}(21)>\frac{131}{20},\qquad
\widehat\epsilon_{29}(1/2,21)
<\frac{21}{3}\frac{(21/2)^{60}}{(30!)^2}
<\frac{1}{500}.}
\tag{AMW-16}
\]

We also strengthen the *negative* source budget without numerical estimates. The classical upper bound `γ<H_32−log32` is rationally certified to be `<3/5`: use `log32=5log2` and the three **positive** `atanh(1/3)` terms

\[
\log2 >2\left(\frac13+\frac1{81}+\frac1{1215}\right),
\quad
H_{32}-10\left(\frac13+\frac1{81}+\frac1{1215}\right)<\frac35.
\]

Also `π<22/7` and the sixth-term lower Taylor polynomial

\[
\sum_{k=0}^{5}\frac{(23/20)^k}{k!}>\frac{22}{7}>\pi
\]

prove `logπ<23/20`. Using `π/2<11/7` and the independently established `log2<25/36`,

\[
\boxed{C_G<\frac35+\frac{11}{7}+\frac{25}{12}+\frac{23}{20}
<\frac{109}{20}.}
\]

The old exact bounds `2w_2<1` and `2(sinh(1/2)-1/2)<1/20` remain valid. Hence the **complete signed** negative budget is strictly less than

\[
\frac{109}{20}+1+\frac1{20}=\frac{13}{2}.
\]

Now (AMW-9) and the correct signed Weil estimate (AMW-10) give, for **every nonzero** smooth compact `v` with only 30 vanishing moments (`0≤j≤29`),

\[
\boxed{\begin{aligned}
Q_\zeta(v,v)&>\left[\frac{131}{20}\frac{499}{500}-\frac{13}{2}\right]\|v\|_2^2\\
&=\boxed{\frac{369}{10000}\|v\|_2^2>0.}
\end{aligned}}
\tag{AMW-17}
\]

All displayed rational comparisons are regenerated in `improved_first_prime_moment_29_certificate` with `Fraction` and separately checked in the test suite. The theorem holds on an **infinite-dimensional subspace of codimension exactly 30 in the smooth compact test space**; it is not a 30-by-30 numerical eigenvalue claim. The earlier 101-moment theorem is retained as a different certificate with a stronger numerical margin on a narrower space.

**What remains:** at `a=1/2`, the unknown unrestricted sign is now concentrated in a **30-dimensional low-moment interface plus cross interactions**, rather than 101 dimensions. This does **not** mean a 30-by-30 matrix of selected tests is sufficient. The conditional Schur bridge below requires the actual source-identified cross-image Gram and certified infinite-dimensional complement bound.

## 7. AMW-07. Conditional finite Schur bridge: making the remaining obstruction checkable (PROVED elementary lemma; APPLICATION UNVERIFIED)

For a fixed radius let `Q` be the closed lower-bounded authentic form with associated self-adjoint `A`; Suzuki's operator construction supplies such a form. Let `V=V_{a,N}` be the high-moment subspace and suppose a source-derived bound `Q(u)≥κ||u||²` is proved for every `u∈V`, where `κ>0` (AMW-17 now supplies `κ=369/10000` on the codimension-30 complement at `a=1/2`; AMW-13 is an independent narrower-space certificate). Choose `N+1` **actual smooth source-domain** functions `f_0,…,f_N` with invertible moment matrix `(∫x^if_j)`; they generate a complementary subspace of the form domain, so every test decomposes uniquely as `v=∑t_jf_j+u`, `u∈V`. Assume these functions lie in the operator domain of `A` (true for sufficiently regular compact tests on this classical model; this is an explicit analytic domain obligation for any implementation).

Let `M_{ij}=Q(f_i,f_j)` and `R_{ij}=⟨Af_i,Af_j⟩`. Then for any coefficients `t`,

\[
Q(v)\ge κ\|u\|²+2\Re\langle u,\sum_jt_jAf_j\rangle +t^*Mt
\ge t^*\left(M-κ^{-1}R\right)t.
\]

Thus the **sufficient**, not necessary, certificate

\[
\boxed{M-κ^{-1}R\succeq0}
\tag{AMW-14}
\]

implies full positivity on that fixed window. The exact rational `exact_finite_schur_sufficiency` checks the abstract finite Hermitian-real matrix condition by **all principal minors** and rejects a negative matrix. It explicitly does NOT supply the genuine source-dependent numbers `M_{ij}` or `R_{ij}`, nor an error enclosure for their evaluation; doing so is the next mathematical/engineering gate. In particular, **no finite Gram scan** and no arbitrary choice of cross matrices is promoted to Weil positivity.

This gives the recursion its next step: the high-mode model certifies a uniform infinite-dimensional inequality; the low-mode source operator supplies a finite interacting model; the *model of their interactions*, through a rigorous cross-operator Schur matrix, can either certify the original global window sign or expose exactly which signed interaction still obstructs it.

## 8. AMW-08. Independent numerical source calibration (TESTED MODEL, no interval sign claim)

A separately implemented 40-digit oracle evaluates the original arithmetic Weil explicit distribution for the triangular test `v_a(x)=(1-|x|/a)_+`, with its exact cubic compact autocorrelation:

\[
h_a(t)=\begin{cases}
2a/3-t²/a+t³/(2a²),&0\le |t|\le a,\\
(2a-|t|)^3/(6a²),&a\le |t|\le2a,\\
0,&|t|>2a.
\end{cases}
\]

One evaluator computes the complete poles, true `Λ(n)/√n` atoms, and Gamma/contact integral over `[0,∞)`. A second evaluator independently computes (AMW-2) through `E_G`, the exact contact constant, and the rank-two pole. **The contact contribution beyond support `|t|=2a` is kept**, precisely as in BLACK SUN's earlier normalization control.

| `a` | authentic prime powers `n<e^{2a}` | `Q_W(v_a)` (numerical diagnostic only) | difference between independent implementations |
| --- | --- | --- | --- |
| 1/4 | none | 0.0129331914725101481 | <4×10^-39 |
| 1/2 | {2} | 0.0007283214179057340 | <4×10^-39 |
| 3/4 | {2,3,4} | 0.0010715954419843222 | <4×10^-39 |

All computed numbers are **NOT** rigorous interval sign certificates and do not enter the proof of AMW-13; their purpose is to catch a source/normalization implementation defect. The exact rational comparisons in AMW-11/12 and the continuum operator proof in AMW-5 do all load-bearing certification.

## 9. Mutation crucible and previous routes not resurrected

- **Fake 6:** `Λ(6)=0`, exact source check refuses a separate primitive-6 weight. The analytic dilation at 6 is still a valid operator: source truth, not unitary existence, distinguishes them.
- **Wrong half-density:** `U_1` sends `1_[1,2]` to squared norm `3/2` instead of `1`; reject the unitary claim.
- **Wrong χ4 parity/conductor:** `χ4(3)=-1` breaks nonnegative zeta-source weighting, and its real Gamma parity and conductor are different. This is a matched sign/normalization control, not a completed χ4 Weil proof.
- **Fake holonomy:** genuine `p,q` commute; attaching PR #80's 2x2 reflection holonomies without derivation fails the source-map gate.
- **Window-gauge mistake:** `P T_b P` is not unitary; `||[S,K]||>0` cannot itself be passed to the unitary connection Laplacian coercivity theorem.
- **Missing poles/contact:** changing the classical `C_G` or dropping either polar sign destroys the exact Weil identification. A generic positive covariance remains unrelated to `Q_W`.
- **Wrong norm/fitted Gram:** the rational dyadic kernel samples are a calibration, not an exact Galerkin compression of the continuous Carleman operator.
- **No finite-to-unrestricted leak:** AMW-13 does not assume that positivity on finite-codimension `V` is positivity on all tests; AMW-14 explicitly names the source-dependent missing low-mode certificate.

## 10. What was established and what is still RH-hard

**Disclosed within the stated source model:** the half-density unitary prime representation, real Gamma jump decomposition and signed Weil polarization, commutation on the full carrier, source-identified noncommutation after finite-window compression with universal strict rational norm lower bound `3/22`, and a genuinely infinite-dimensional, full signed completed-Weil coercivity estimate `291/5000` on `V_{1/2,100}`. Both finite numerical constants are certified by exact rational inequalities (plus paper proofs). The general high-moment Fourier certificate is stated with explicit hypotheses and the necessary source bounds. The Schur bridge is a correct **conditional** all-test sufficiency theorem, not an arithmetic result unless its input Gram/cross matrices are derived with certified errors.

**Still open:** source-derived positivity of the *unrestricted* compact-window Weil quadratic form for any first-prime interval, full all-radius positivity, a uniform all-test `Q_J≥-η_J||v||²` with `η_J→0`, a lawful physical joint-intervention source, or an independently positive factorization exactly equal to `Q_W`. No claimed RH proof or academic priority follows.

**Next decisive probe:** At `a=1/2`, construct **30 smooth dual-moment functions** and compute certified outward-error enclosures of the source-original `M_{ij}=Q_W(f_i,f_j)` and `R_{ij}=⟨A_af_i,A_af_j⟩`. Try AMW-14 for `κ=369/10000`, with a condition-number/residual audit and independent gamma/pole/prime evaluators. If this highly conservative 101-mode Schur certificate fails, retain its exact counterexample and improve the high-mode basis/tail rather than assuming the sign. The RH-hard all-window extension would still require an independent argument for arbitrary `a`.

## 11. Prior art and reproducibility

Mathematical ingredients include classical Mellin half-density and multiplicative Haar normalization; the Carleman operator and Laplace square `C=L*L`; Weil's explicit formula and positivity criterion; Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3 (23 Sep 2026), §§1–3; Yoshida/Bombieri finite-codimension positivity results; connection Laplacians (Bandeira–Singer–Spielman, 2013); finite rational linear algebra and standard moment/Fourier concentration. SUCC project antecedents: PR #70 CG1–CG9, PR #71 CW-01–20, PR #76 GWC-7, and parent PR #80 META-06–10. **Neither “a first mathematical holonomy” nor a new proof of localized finite-codimension positivity is asserted.** The derived quantitative boundary and moment-subspace results are specific new-to-project checkpoints; scholarly novelty is UNVERIFIED.

Reproduction on the branch (Python 3.10+, no mandatory numerical package; `mpmath` optional for the independent oracle):

```
PYTHONPATH=. python -m unittest tests.test_arithmetic_meta_weil -v
PYTHONPATH=. python scripts/arithmetic_meta_weil_probe.py --verify research/2026-10-14/ARITHMETIC_META_WEIL_RECEIPT.json
python scripts/verify_provenance.py
```

The finite Fraction checks prove the explicit rational inequalities from the paper. They do not formalize the continuum operator proof in Lean. The independent tent quadrature is diagnostic only; numbers are not certified signs. GitHub CI, whole repository regression results and kernel checking must be reported only when actually observed at the exact commit.
