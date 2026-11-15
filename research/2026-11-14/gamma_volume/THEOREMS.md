# Gamma volumes: exact operators, source memory, and observer descent

**Status:** classical identities and locally proved source-specific interfaces, with exact finite instruments. Proofs below are mathematical derivations, not Lean kernel certificates or consequences of finite testing. The original signed four-pole recurrence and `U₀=0` are unchanged. Historical and scholarly antecedents are recorded in `PROVENANCE.md`.

## 0. Coordinate contract

| Symbol | Role |
|---|---|
| `s` | complex Mellin index / Gamma argument |
| `t` | positive integration coordinate or elapsed lag |
| `α,β` | positive real composition depth |
| `a` | causal basepoint in the fractional-integral construction |
| `λ` | real nonnegative exponential tempering rate |
| `x∈[0,1]` | original Oily source coordinate; never an interchangeable dummy source |
| `z` | generating-function coordinate, not an observed source time |
| `K` | specified linear source-step or delay operator, with its interpretation declared |
| `P` | a linear observer report map in the finite-dimensional descent theorems |

The scalar Gamma function, its normalized convolution kernel, and an operator obtained by integrating source evolution are three related objects. Each equality below declares which one is being used.

## GV-01. What the Euler integral spreads, and where phase actually lives

For `Re s>0`,

\[
\Gamma(s)=\int_0^\infty t^{s-1}e^{-t}\,dt.
\]

Thus `Γ(t+1)=∫₀∞ r^t e^{-r}dr` if the exponent is named `t`. The integration variable `r` is not the output location. Under `t=e^u`, and `s=c+iω` with `c>0`,

\[
\Gamma(c+i\omega)=\int_{\mathbb R}
 e^{cu-e^u}e^{i\omega u}\,du.
\]

**Proof.** Substitute `dt=e^u du` in the Euler integral. The amplitude is integrable: it decays exponentially as `u→−∞` and faster than exponentially as `u→∞`. The factor `e^{iωu}` is a Fourier character on the logarithmic coordinate. Varying `c` changes the real weight; varying `ω` changes phase.

The real powers are linearly independent in finite families on an interval, but they are not automatically orthogonal or statistically independent. For example, the Gram matrix of `1,t` in `L²(e^{-t}dt)` is `[[1,1],[1,2]]`. A continuum of Dirac distributions can express a distributional resolution of a carrier; it is not a collection of unit vectors in ordinary `L²`, and its independence is not a consequence of the Gamma integral. These corrections specify a carrier rather than refute the proposed geometric intuition.

**The author's centering at s.** For real `s>0`, normalize the carrier as `g_s(t)=t^(s−1)e^(-t)/Γ(s)`. The Gamma successor identity gives `E[T]=s` and `Var(T)=s`. Its density in log coordinates is `q_s(u)=e^(su−e^u)/Γ(s)`; differentiating its log gives `s−e^u`, so its unique mode is `u=log s`, corresponding to `t=s`. The density with respect to `dt` instead peaks at `t=s−1` when `s>1`. Thus the volume is centered at `s` in two precise senses (mean in the original coordinate, mode in the logarithmic chart), while its shape and width change with `s`. It is not a rigid translate of one fixed profile. This classical centering was also developed in concurrent draft #634, GG-01, inspected after this round's initial publication; see the pinned cross-reference in `PROVENANCE.md`.

**Provenance:** Euler integral and Mellin/Fourier change of variables are classical, DLMF 5.2.1 and 1.14(iv). **Next discriminator:** a proposed alternate measure or basis must reproduce the Jacobian, domain, and transform convention.

## GV-02. Ordered causal volumes force the Gamma normalization

For an integer `m≥1`, the volume of

\[
 a<t_1<\cdots<t_m<b
\]

is `(b−a)^m/m!`. Its boundary-density kernel is

\[
 k_m(t)=\mathbf1_{t>0}\frac{t^{m-1}}{(m-1)!}.
\]

**Proof.** Up to the measure-zero collision hyperplanes, the cube `(a,b)^m` splits into `m!` congruent ordering regions. Integrating the last coordinate, or differentiating the volume with respect to `b`, gives the kernel. Concatenation of ordered histories is convolution.

For every real `α>0`, define

\[
 k_\alpha(t)=\mathbf1_{t>0}\frac{t^{\alpha-1}}{\Gamma(\alpha)}.
\]

For `α,β>0` and `t>0`,

\[
 (k_\alpha*k_\beta)(t)
 =\frac{t^{\alpha+\beta-1}}{\Gamma(\alpha)\Gamma(\beta)}
   \int_0^1 v^{\alpha-1}(1-v)^{\beta-1}dv
 =k_{\alpha+\beta}(t).
\]

This is the Beta identity, not an appeal to fractional physical dimensions. It explains exactly why Gamma appears when a family of ordered-volume kernels must compose at noninteger depth.

**Conditional uniqueness.** Suppose kernels have the homogeneous form `c(α)t^(α−1)`, `c(α)>0` continuous, their convolutions add depths, and `c(1)=1`. The Beta identity implies `d(α+β)=d(α)d(β)` for `d(α)=c(α)Γ(α)`. Positive continuous solutions are `d(α)=e^(Cα)`; `d(1)=1` gives `C=0`. Hence the displayed normalization is forced within this declared homogeneous class. Without those hypotheses, composition alone does not select this kernel.

**Provenance:** classical simplex/Beta/fractional integration; inherited PG-03 and PB15. **Next discriminator:** changing the unit kernel, measure, or scaling class must be tracked as a different family.

## GV-03. The exact twist → evolve → untwist, rooted at any a

On a finite interval `[a,b]`, let `f∈L¹[a,b]`, `α>0`, and `λ≥0`. Define, almost everywhere,

\[
 (J_{a+}^{\alpha,\lambda}f)(y)
 =\frac1{\Gamma(\alpha)}\int_a^y
  (y-v)^{\alpha-1}e^{-\lambda(y-v)}f(v)\,dv.
\]

Write `I_{a+}^α=J_{a+}^{α,0}` and `(C_λf)(y)=e^{λ(y−a)}f(y)`. Then

\[
 \boxed{J_{a+}^{\alpha,\lambda}
       =C_\lambda^{-1}I_{a+}^{\alpha}C_\lambda.}
\]

**Proof.** In the conjugated integral, the two exponential factors multiply to `e^{-λ(y−v)}`. The multipliers are bounded with bounded inverse on the finite interval; the kernels are locally integrable, so this is an operator identity on `L¹[a,b]`. Fubini/Tonelli and GV-02 yield

\[
 J_{a+}^{\alpha,\lambda}J_{a+}^{\beta,\lambda}
 =J_{a+}^{\alpha+\beta,\lambda}.
\]

For `λ>0`, the whole-lag kernel `g_α(t)=λ^α e^{-λt}k_α(t)` has mass one, satisfies `g_α*g_β=g_(α+β)`, and has mean `α/λ`. It extends to the measure-valued identity `g₀=δ₀`: for every `ε>0`, its mass on `[ε,∞)` is at most `α/(λε)`, so `g_α` converges weakly to `δ₀` as `α↓0`. This supplies an exact zero-origin pulse and continuous composition depth. On a finite causal window the kernel has incomplete mass; dividing each truncated output by a position-dependent mass is a different operator and is not licensed by the semigroup proof.

At `λ=0`, `I_{a+}^α1(y)=(y−a)^α/Γ(α+1)`: the volume is literally translated to a new basepoint. An impulse at `a` produces the translated kernel in the distributional sense. On the half-line, the Laplace multiplier is `(p+λ)^(-α)` for `Re p≥0`, `λ>0`; this is a spectral shift by `λ`. Translating the origin and shifting the spectral variable are different operations.

For real `λ>0`, the twists change amplitudes and are not unitary. An imaginary parameter `λ=iω` yields phase multipliers on a finite interval; it does not give a positive probability density. On the whole half-line `C_λ` is unbounded for positive `λ`, so the finite-interval conjugation must not be asserted as an everywhere bounded similarity there.

**Provenance:** classical tempered fractional calculus, Sabzikar–Meerschaert–Chen §3, especially (19), (23). **Next discriminator:** a sign mutation in either exponential must fail a nonconstant-input integral test.

## GV-04. A Gamma integral can carry an entire source operator

Let `K` be a bounded operator on a complex Banach space (or the complexification of a real Banach space) with `||K||≤1`. For `α>0`, set

\[
 F_\alpha(K)=\frac1{\Gamma(\alpha)}
  \int_0^\infty t^{\alpha-1}e^{-t}
            e^{t(K-I)}\,dt.
\]

The integral converges in operator norm. Expanding the Poissonized source evolution gives

\[
 \boxed{F_\alpha(K)=(2I-K)^{-\alpha}
    =\sum_{n\ge0}w_n^{(\alpha)}K^n,\qquad
 w_n^{(\alpha)}=
 \frac{\Gamma(n+\alpha)}{\Gamma(\alpha)\Gamma(n+1)}2^{-n-\alpha}.}
\]

The branch is the principal holomorphic one, available because `2I−K` has spectrum in the right half-plane. The weights are positive, sum to one, and satisfy

\[
 \sum_{n\ge0}w_n^{(\alpha)}z^n=(2-z)^{-\alpha},\qquad
 F_\alpha F_\beta=F_{\alpha+\beta},\qquad F_0=I.
\]

**Proof.** `||e^{t(K−I)}||≤1`; absolute norm convergence justifies termwise integration of `e^{-2t}e^{tK}`. Each coefficient is the Euler integral at `n+α`, scaled by 2. The binomial generating function proves both normalization and convolution. This also gives norm continuity at zero and `F_α=e^{-α log(2I−K)}`.

There is a quantitative finite-prefix certificate. For `1<r<2`,

\[
 \left\|F_\alpha-\sum_{n=0}^Nw_n^{(\alpha)}K^n\right\|
 \le r^{-N-1}(2-r)^{-\alpha}.
\]

Indeed, multiply each omitted weight by `r^n≥r^(N+1)` and sum the positive generating function. No infinite number of executed automata is required to approximate this operator to a certified tolerance.

**Interpretation boundary.** If `K` advances a source, this is a weighted future observable, requiring the source law and an appropriate initial state/report. If `K=L` is the backward time delay, it is a retarded filter. An equation in `K` does not identify these interpretations. The original Oily physical-stage model separately includes its two compulsory delays `L²`.

**Provenance:** classical Gamma subordination / negative binomial law; prior conversation and PG-03/PB15 already contain the coefficient semigroup. **Next discriminator:** preserve the operator, normalization, and direction of time when transporting between carriers.

## GV-05. The original Oily unit law has a source-preserving depth lift

For `0≤x≤1`, put

\[
 u=x-x^2/2,\quad v=x^2/2,\quad
 a_x=(1-u)(1-v)=1-x+x^3/2-x^4/4.
\]

The subscript distinguishes `a_x` from the causal basepoint in GV-03. From the unchanged four-pole source,

\[
 R(x)=\frac{4-2x^3-x^4-x^5}{16-x^8}
 =\frac{1-x}{(2-x^2)(x^2-2x+2)}
 =\frac{1-x}{4a_x},\qquad
 \int_0^1R(x)dx=\pi/16.
\]

The existing raw packets are `p_j(x)=(1−x)Σ_{k=0}^j u^kv^(j−k)/4`. Their conditional grade PGF, with its continuous endpoint limit, is

\[
 G_x(z)=\frac{(1-u)(1-v)}{(1-uz)(1-vz)}.
\]

The following is a **declared fractional continuation of this authenticated unit law**, not a newly measured source process:

\[
 G_{x,\alpha}(z)=G_x(z)^\alpha,\qquad \alpha>0.
\]

It has nonnegative coefficients summing to one, since it is a product of two negative binomial PGFs. At fixed `x`, `G_{x,α}G_{x,β}=G_{x,α+β}`. For a contraction `K`, the corresponding operator is

\[
 Q_{x,\alpha}(K)
 =a_x^\alpha(I-uK)^{-\alpha}(I-vK)^{-\alpha}.
\]

The entire retained carrier therefore has an autonomous depth law. On essentially bounded, strongly measurable fields `f(x)` with values in the source Banach space and the essential-supremum norm, act pointwise by `Q_{x,α}`; the resulting operators compose in depth and have norm at most one. Uniform bounds `u,v≤1/2` control the power series and continuity. These fields admit the probability-weighted Bochner average used in GV-06.

Its generator is explicit:

\[
 \mathcal L_x(K)
 =\sum_{k\ge1}\frac{u^k+v^k}{k}(K^k-I),\qquad
 Q_{x,\alpha}=e^{\alpha\mathcal L_x}.
\]

The series converges absolutely in norm. If `K` is Markov, this is a compound-Poisson generator with total rate `−log a_x`, and jump weights proportional to `(u^k+v^k)/k` when `x>0`. This is a mathematical realization of the declared depth extension. At `x=0` it is the zero generator. At `x=1`, `R(1)=p_j(1)=0`; `G_1` denotes the continuous conditional endpoint limit. At that endpoint,

\[
 Q_{1,\alpha}(K)=(2I-K)^{-2\alpha}=F_{2\alpha}(K).
\]

The factor **2** retains the original two loops. A single Gamma shape at this endpoint must not silently replace the original shape two.

**Proof of source identity.** Factor the numerator as `(1−x)(x²+2)(x²+2x+2)` and the denominator as `(2−x²)(x²+2)(x²−2x+2)(x²+2x+2)`. The integral normalization is the inherited original BBP identity, independently recoverable from partial fractions. Expand each `(1−uz)^(-α)` with the positive rising-factorial coefficients; taking logarithms gives the generator.

**Next discriminator:** changing one loop or treating a composite arithmetic multiplier as an authenticated new prime is a source mutation, not this lift.

## GV-06. Integrating out the shared source breaks depth composition

Use the authenticated marginal source measure

\[
 \mu(dx)=\frac{16}{\pi}R(x)dx,
 \qquad A_\alpha(z)=\int_0^1G_x(z)^\alpha\,\mu(dx).
\]

For `α,β>0`, and real `0≤z<1`,

\[
 \boxed{A_{\alpha+\beta}(z)-A_\alpha(z)A_\beta(z)
 =\operatorname{Cov}_\mu(G_X(z)^\alpha,G_X(z)^\beta)>0.}
\]

At `z=1` the difference is zero. At any fixed known `x`, it is zero as well.

**Proof of strictness.** For fixed `z<1`, `(1-q)/(1-qz)` has derivative `(z−1)/(1−qz)²<0` in `q`. Both source rates are nondecreasing and at least one increases on every nonempty subinterval. Hence `G_x(z)` is strictly decreasing. For independent copies `X,Y`,

\[
 2\operatorname{Cov}(f(X),g(X))
 =\mathbb E[(f(X)-f(Y))(g(X)-g(Y))].
\]

With the two positive powers of `G`, the integrand is positive whenever `X≠Y`. The source has positive density in the open interval, so the covariance is strictly positive.

The left side uses the **same source coordinate through both layers**. The product on the right averages each layer separately and therefore describes **independent redraws of the source coordinate**. Its failure is not failure of the conditional Gamma semigroup. It is a precisely located loss at the report map.

There is an operator form of the same statement. Let `S_α` be the retained-source semigroup from GV-05, `Π` average over `x`, and `J` embed a source-independent report as a constant field. Then `ΠJ=I`, and the compressed operators `S̄_α=ΠS_αJ` obey

\[
 \boxed{\overline S_{\alpha+\beta}-\overline S_\alpha\overline S_\beta
 =\Pi S_\alpha(I-J\Pi)S_\beta J.}
\]

Expand the right side and use `S_αS_β=S_(α+β)`. The middle projection `I−JΠ` retains source-dependent contrasts with zero average. It identifies precisely the part that the first integration discards and the next layer can still use. The scalar positivity above is not a claim that this operator difference is positive for arbitrary source operators.

At the simplest probe `z=0`, `α=β=1`, `G_x(0)=a_x`. Since `a_xR=(1−x)/4`,

\[
 A_1(0)=\frac2\pi,\qquad
 A_2(0)=\frac7{5\pi},\qquad
 \boxed{A_2(0)-A_1(0)^2=\frac{7\pi-20}{5\pi^2}>0.}
\]

The two elementary integrals are `∫a_xR dx=1/8` and `∫a_x²R dx=7/80`. The inequality follows already from `π>3`. No fitted source or rounded determinant is used.

**Provenance:** shared-source covariance and retained/redrawn controls are inherited WPI-03 and Oily cross-time grammar. The exact fractional-depth specialization and constants are the new interface computed here. **Next discriminator:** compare the joint two-layer grade law, not only its one-layer marginals.

## GV-07. Every source-depth Hankel matrix has full rank

Let `m_n=A_n(0)=∫a_x^n μ(dx)` for integers `n≥0`, including `m₀=1`. For every integer size `N≥1` and shift `r≥0`,

\[
 H_N^{(r)}=(m_{r+i+j})_{0\le i,j<N}
\]

is strictly positive definite.

**Proof.** `a_x` is strictly decreasing from 1 to `1/4`. For example `a'_x=−(1−x)(1−v)−x(1−u)<0` on `[0,1]`. For any nonzero real vector `c`,

\[
 c^TH_N^{(r)}c
 =\int_0^1 a_x^r\left(\sum_{i=0}^{N-1}c_i a_x^i\right)^2\mu(dx)>0.
\]

A nonzero polynomial has only finitely many roots; the pushforward source measure has support throughout `[1/4,1]`. This proves the universal rank assertion, independently of the finite certificates.

It follows that the sequence has no finite-dimensional autonomous linear realization `m_n=C B^n b`, and no eventual constant-coefficient linear recurrence. Such a realization bounds all Hankel ranks by its state dimension; a recurrence would similarly bound a sufficiently shifted Hankel matrix.

This is a statement about **linear state realization in the depth index**. It is consistent with the existing two-register grade realization at fixed `x`, and says nothing against a finite nonlinear or programmable description. Infinite Hankel rank after integration was already proved for another original-source sequence in PI_SOURCE_GENESIS_GREEN G2; the present theorem specializes that mechanism to the Gamma-depth observable.

**Next discriminator:** a claimed finite autonomous linear closure must fail at a Hankel order above its proposed dimension, unless it changes the observable or source.

## GV-08. A finite source-bound program predicts every integer depth

For every integer `n≥1`, define the rational number

\[
 c_n=4\int_0^1(1-x)a_x^{n-1}dx\in\mathbb Q.
\]

Then

\[
 \boxed{m_n=\frac{c_n}{\pi}=\frac{c_n}{2}m_1.}
\]

The first coefficients are

\[
 c_1=2,\quad c_2=7/5,\quad
 c_3=2657/2520,\quad c_4=100679/120120.
\]

**Proof and algorithm.** Cancel `a_x` against the denominator of `R`, expand the rational polynomial `a_x^(n−1)`, and integrate its monomials. If its coefficient at `x^k` is `b_k`, then `c_n=4Σ_k b_k/[(k+1)(k+2)]`. This is a terminating exact rational computation, not a limiting fit. It yields a nonautonomous scalar recurrence `m_(n+1)=(c_(n+1)/c_n)m_n` as well.

Thus unbounded autonomous linear realization rank coexists with a finite source-bound predictor. The known law, not the number of sampled moments, licenses the shortcut. `m₁` alone would not select this source among arbitrary probability laws, and knowing a numeric value exactly is distinct from receiving a finite-precision observation. No constant bit-cost or constant-time evaluation is asserted.

The shortcut is uniformly stable with respect to that one measured scalar. Since `1/4≤a_x≤1`,

\[
 4^{1-n}\le c_n/2=2\int_0^1(1-x)a_x^{n-1}dx\le1.
\]

If `|m̂₁−m₁|≤ε` and the exact coefficient is used, then `|m̂_n−m_n|≤ε` for every `n≥1`. This bound concerns input error in the scalar under the authenticated source law; an incorrect source class is a different error. The finite implementation caps indices explicitly; the polynomial algorithm and the proof extend to every finite integer `n`.

For certification, `det H_N^(0)=(b_N π+d_N)/π^N` with rational `b_N,d_N`, because after multiplying every entry by `π` only the `(0,0)` entry contains `π`. Exact determinants plus original-BBP rational enclosures certify finite signs without floating eigenvalues. This finite instrument supports, but does not replace, GV-07.

**Next discriminator:** source-matched finite-moment counterfeits must remain distinct from the authenticated polynomial rule; error and bit costs must accompany an operational observer claim.

## GV-09. Coherent Gamma descent has an exact report condition

Let `K∈M_d(C)` have spectrum in the closed unit disk, let `P:C^d→C^r` be a linear report, and write `N=ker P`. A linear operator `T` descends to the report image exactly when

\[
 TN\subseteq N
 \quad\Longleftrightarrow\quad
 \exists Q:\operatorname{im}P\to\operatorname{im}P,\ PT=QP.
\]

This is the same fiber/quotient condition used in the earlier observer work, specialized to linear reports.

For the Gamma family `F_α=(2I−K)^(-α)`, the following are equivalent:

1. `K` descends.
2. `F₁` descends.
3. Every `F_α`, `α≥0`, descends.

**Proof.** If `K` preserves `N`, all analytic functions used in the family preserve it (in finite dimension, use polynomial functional calculus). Conversely `F₁` is invertible; if it preserves the finite-dimensional `N`, it maps `N` onto `N`, so its inverse preserves `N`. Then `K=2I−F₁^{-1}` preserves `N`. The all-family assertion includes order one.

The implementation supplies either an exact rational `Q` with `PT=QP`, or a rational collision witness `v` with `Pv=0` and `PTv≠0`. Mere invertibility of `2I−K` suffices for its integer matrix calculations; the program does **not** infer the unit-disk or positive-kernel interpretation from that algebra alone.

**Next discriminator:** replay the kernel witness against the actual report, including dependent report rows, instead of treating a visually commuting diagram as evidence.

## GV-10. Sharp alias threshold at Gamma order six

Under the finite-dimensional hypotheses of GV-09, for every real `0<α<6`,

\[
 F_\alpha\text{ descends}\quad\Longleftrightarrow\quad
 K\text{ descends}.
\]

**Proof.** On the closed unit disk, `2−z` lies in the disk centered at 2 with radius 1, so its argument is in `[-π/6,π/6]`. If `(2−z₁)^(-α)=(2−z₂)^(-α)`, then `Log(2−z₁)−Log(2−z₂)=2πik/α` for some integer `k`. Their argument difference has magnitude at most `π/3`; `α<6` forces `k=0`, hence `z₁=z₂`. Also `f'_α(z)=α(2−z)^(-α−1)` is nonzero. At the finitely many source eigenvalues, local analytic inverse functions and Hermite polynomial interpolation, including all Jordan orders, give a polynomial `p` with `K=p(F_α)`. Therefore invariance under `F_α` implies invariance under `K`. The other direction is immediate.

The threshold is sharp. Set

\[
 K_2=\begin{pmatrix}0&-1\\1&1\end{pmatrix},\qquad P_2=(1,0).
\]

Then `K₂⁶=I`, `(2I−K₂)⁶=−27I`, and

\[
 F_6(K_2)=-I/27.
\]

The report therefore descends at order six, although `P₂K₂=(0,−1)` does not factor through `P₂`. The source is a contraction in the positive definite metric `H=[[2,1],[1,2]]`, since `K₂ᵀHK₂=H`; no Euclidean norm assumption is smuggled in.

There is also an actual positive finite-cycle realization. Let `K₆e_j=e_(j+1 mod6)` and

\[
 P_6=(1,1/2,-1/2,-1,-1/2,1/2).
\]

This `K₆` is a permutation/Markov contraction. Its first harmonic gives

\[
 P_6F_6(K_6)=-P_6/27,
\]

but states 1 and 5 have the same current report `1/2` and next reports `−1/2` and `1`. A predictable Gamma-weighted future report therefore does not imply a predictable next event. Positive evolution and positive averaging weights are fully compatible with this counterexample.

Here `P₆` records one signed observable or its expectation. Its descended mean is not a claim that the complete distribution of random future reports factors through this scalar report.

**Provenance:** local application of classical holomorphic matrix calculus; exact cycle specialization derived in this round. **Next discriminator:** test an order below six, or preserve enough phase information to separate the colliding harmonic components.

## GV-11. Continuous Gamma-order horizons are a closed-subgroup trace

Under GV-09, define

\[
 \mathcal A=\{\alpha\ge0:F_\alpha N\subseteq N\}.
\]

Exactly one of the following occurs:

\[
 \boxed{\mathcal A=\{0\},\quad
 \mathcal A=d\mathbb N_0\text{ for some }d>0,\quad
 \mathcal A=[0,\infty).}
\]

For this unit-disk Gamma family a nontrivial discrete period satisfies `d≥6`. The cycle in GV-10 has `A=6N₀`.

**Proof.** `F_α=e^{αB}`, `B=−log(2I−K)`, extends to all real `α` in finite dimension. Every `F_α` is invertible. If it preserves `N`, its restriction maps `N` onto itself, hence `F_(−α)` preserves `N` too. The real admitted set is therefore a subgroup. It is closed because the matrix family is continuous and subspace invariance is a closed condition. Closed subgroups of `R` are `{0}`, `dZ`, and `R`; intersect with the nonnegative half-line. GV-10 rules out a positive admitted order below six unless all orders are admitted. For the example, the two spectral phases are `±απ/6`; the real report is invariant precisely when their sine term vanishes.

This is a theorem about a finite-dimensional **linear Gamma-order report family**. It does not replace #633's additive monoids of actual integer source horizons. The two index sets refer to different observables and evolution laws.

**Next discriminator:** the finite-dimensional/invertibility hypothesis is load-bearing; an infinite-dimensional proper invariant subspace need not be onto and needs a separate theorem.

## GV-12. What has been established for the author's volume

Within the stated mathematical carriers, Gamma supplies the normalization that lets ordered-volume pieces concatenate coherently at real depth. A basepoint translation makes a rooted volume, and exponential conjugation gives the requested three-operation form. A specified source operator can be carried through the integral. The original Oily law admits such a source-preserving depth lift, while its integrated observer report has an explicit composition defect and an exact source-bound predictive compiler.

None of these statements identifies an unobserved physical communication channel, executes a continuum of automata, authenticates a source from a finite matching prefix, or proves signed BBP cancellation. The next source-specific task is to specify the actually received report and target and prove its intertwining, error, and cost contracts. The fresh discriminators here tell us exactly which identifications that task must preserve.
