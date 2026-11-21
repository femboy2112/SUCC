# The causal origami seam: final coalgebras, source journals, BBP analytic transport, and prime-square spectral complexity

**2026-11-20 | SUCC isolated, stacked research.** Parent: observer-headed Yoneda GPS PR #676 (`c910be34f935be7b3c1c4c6344648a5b5ca9d34a`), behind constructive Fourier atoms #675, prime wavefront #674, and the earlier analytic/pinbed/Gaussian fronts. Main XXVI (`81be6b897ae980b801a3b9de9e22ef81e8360bfb`) is untouched. No historical, formal, production, CI, or source imports changed. **R0, π base-16 normality, RH, quantum/carrier energy, and statistical independence of primes remain OPEN.** Classical antecedents are identified; no academic priority claimed.

## Steelman and notation

**User conjecture:** a finite causal observer's chronological bookkeeping is not merely an arbitrary coordinate system. At a properly typed seam, the carrier's execution and the observer journal's next-index operation can become equivalent **dynamical presentations**, and the retained journal can be folded into the carrier as a memory/policy subsystem. On an additive journal, Fourier modes are characters of the actual successor composition. Dense observer-heads may preserve the full carrier category, while restricted heads preserve only a quotient. Gaussian smoothing is a declared further operation, not automatic physical probability.

The terms *0★J seam*, *causal origami*, and *subjective/objective* motivate this framework; we do **not** silently identify them with an independently uninspected legacy formal `0★J` object. All mathematical arrows below have explicit domains. In particular, an intrinsic timestamp is not the same thing as a calibrated timestamp accessible to a physical observer.

Write `e(t)=exp(2πit)`; `r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2)` for `n≥1`, **literally** `U_0=0`, `U_n=16U_(n−1)+r(n)`, `c_n=16^(−n)r(n)`, `P_n=Σ_(j≤n)c_j`, `x=Σ_(j≥1)c_j=π/16` by the classical BBP identity, `T_n=Σ_(k≥1)16^(−k)r(n+k)`. `Q(t)=4−2t³−t⁴−t⁵=(1−t)H(t)`, `H(t)=4+4t+4t²+2t³+t⁴`. The model controls with other seeds and `Q*(t)=Q(t)+(1−t)²` never replace this source.

## COS-01 — Complete causal journals form a final coalgebra (CLASSICAL; EXACT)

Let `X,Y` be sets, `T:X→X`, `o:X→Y` total. Define `γ(x)=(o(x),Tx)` and the complete journal

`J(x)=(o(x),o(Tx),o(T²x),...) ∈Y^N`.

On `Y^N` let `head` and `tail` be standard. The map `Y^N→Y×Y^N`, `a↦(a_0,tail a)`, is a bijection; `(Y^N,head/tail)` is the **final F-coalgebra** for `F(Z)=Y×Z` in Set. The map `J` is the unique coalgebra morphism; in particular

`head(Jx)=o(x)` and **`J(Tx)=tail(Jx)`**.

*Proof:* recursively define `J(x)_n=o(T^nx)`. Any coalgebra morphism `g` has the same head and, inductively, `n`th entry, establishing uniqueness. This is not a state fixed point `Tx=x`: it is a self-similar **head/tail structural fixed point**. The global infinite stream is a mathematical completion, not a physically elapsed infinite record.

## COS-02 — When the graph and bookkeeping graph are *actually equivalent* (CLASSICAL; EXACT / CONDITIONAL)

Let `S=J(X)⊆Y^N`; it is closed under `tail` (not necessarily closed topologically). Put `x~x'` iff `J(x)=J(x')`. Then `x~x'` implies `Tx~Tx'`, so `T` descends to `X/~`. The map `[x]↦J(x)` is a **bijection** from the quotient to `S`, and it conjugates the successor: `\bar J\bar T=tail \bar J`. Thus the **observational quotient action graph** is isomorphic to the realizable-journal action graph, with forward clock labels preserved.

If `J` is injective, this is an isomorphism of **the full carrier action graph** and journal graph. More categorically, define the action category `Act(X,T)` with objects `x∈X` and arrows `(x,n):x→T^nx` labeled by `n∈N`; composition is addition. Then `Act(X/~,\bar T)≅Act(S,tail)`; if `J` injective, `Act(X,T)≅Act(S,tail)`. No reverse-time arrows have been admitted. The ordinary Yoneda embedding of either small action category in its representable presheaves is fully faithful. An **additional restricted-Yoneda claim** on a smaller probe category needs a supplied dense probe functor; arbitrary scalar observations are not automatically Hom-sets.

*Crucible:* with `X={0,1}²`, `o(a,b)=a`, `T(a,b)=(b,a)`, the first two reports reconstruct `(a,b)` and `J` is injective. With `T(a,b)=(a,1−b)`, the entire journal is `(a,a,...)` and loses `b`, despite its real dynamics. Even all future scalar probes of that type yield only the proper quotient.

## COS-03 — Analytic journal intertwines causal successor with Hardy backward shift (CLASSICAL; EXACT)

For a complex sequence `a_0,a_1,...` with `Σ|a_n|R^n<∞` for some `R>1`, define `G_n(z)=Σ_(k≥0) a_(n+k) z^k`, `|z|<R`. Then

`G_n(0)=a_n`, `G_(n+1)(z)=B G_n(z)`, with **`B f(z)=(f(z)−f(0))/z`** (holomorphic at zero). Its boundary character `G_0(e^{iω})` is the temporal Fourier series of the source journal. If `a∈ℓ²`, the Hardy H² identity is `||G_0||_(H²)^2=Σ|a_n|²` (Parseval). A finite journal `a_0,...,a_(M−1)` gives a polynomial with a certified uniform tail whenever a source tail bound is available.

This is the literal mathematical **finite ↔ analytic seam**: one step of acquiring the next head is the analytic backward-shift operation. It is not an inverse causal action. In particular, the existence of the shift does not imply a uniform lower bound on temporal Fourier modes.

## COS-04 — Exact original-BBP Mellin–Hardy seam and signed completion (SOURCE-SPECIFIC, PROVED PAPER)

Take `a_k=c_(k+1)` in COS-03. The original four-pole source integral is

`r(j)=∫_0^1 t^(8j−8) Q(t) dt`.

For every `n≥0` and `|z|<16`, absolute convergence and geometric summation give

`G_n(z)=Σ_(k≥0) c_(n+k+1)z^k = 16^(−n)∫_0^1 t^(8n)Q(t)/(16−zt^8) dt`.

Thus `G_(n+1)=B G_n`, and at `z=1`,

**`P_n+G_n(1)=x=π/16`, `U_n=16^nP_n`, `T_n=16^nG_n(1)`**.

In particular, the exact compensating tail is

**`T_n=∫_0^1 t^(8n)Q(t)/(16−t^8)dt`.**

*Proof:* `Σ_(k≥0)16^(−n−k−1)t^(8n+8k)z^k = 16^(−n)t^(8n)/(16−zt^8)`. Integrate against `Q`; sums are uniformly absolutely convergent for `|z|<16`. At `z=1`, `G_n(1)=Σ_(j>n)c_j`; multiplying by `16^n` gives the BBP tail. The **finite observer's past** and the **analytic observer's future** are now source-attested, not an independently generated matched waveform.

**Sharp two-term asymptotic.** Write `Q(t)=(1−t)H(t)` and `f(t)=H(t)/(16−t^8)`, smooth on `[0,1]`, with `f(1)=1`, `f'(1)=2`. Taylor at `1` gives `f(t)=1−2(1−t)+O((1−t)^2)` uniformly. Using beta integrals,

`T_n=1/[(8n+1)(8n+2)] − 4/[(8n+1)(8n+2)(8n+3)] + O(n^(−4))`

and therefore **`T_n = 1/(64n²) − 7/(512n³) + O(n^(−4))`**. The implied constant is finite because `f''` is bounded on `[0,1]`. This asymptotic is derived from original `Q`, not from digit fits.

**Finite transport:** for `M≥n`, `G_n^[M](z)=Σ_(j=n+1)^M c_j z^(j−n−1)` satisfies `P_n+G_n^[M](1)=P_M` exactly. Since the original `r` is strictly decreasing and positive,

`0 < x−P_M ≤16^(−M)r(M+1)/15`, and hence the original terminal real-phase error is at most `16^n(x−P_M)`. Taking `M=2B` for `B≤n<2B` recovers the rigorous O(B^(−2)) source-tail transport, **not** a signed Weyl estimate. See existing #672 for stronger calibration and #675 for the original F(z) transform.

## COS-05 — Exact finite Fourier alias and exponentially precise source tomography (SOURCE-SPECIFIC; PROVED PAPER)

Let `F(z)=Σ_(n≥1)c_n z^n=z G_0(z)`, holomorphic for `|z|<16`. For any integer `M≥1`, roots of unity `ζ_M=e(1/M)` and `1≤j≤M` give

**`A_(j,M)=(1/M)Σ_(ℓ=0)^(M−1) F(ζ_M^ℓ) ζ_M^(−jℓ) = Σ_(k≥0)c_(j+kM)`**.

This is the exact cyclic Fourier orthogonality relation. Since `r(j)` is positive decreasing,

**`0 < A_(j,M)−c_j ≤ r(j+M) 16^(−j−M)/(1−16^(−M))`**.

So finitely many *exact analytic spectral values* reconstruct the first M chronological BBP atoms within explicit one-sided errors. Those spectral values themselves encode infinitely many source terms; this is not an assertion that finite causal measurements have infinite-precision access to them. A finite `P_K` replaces `F` with a certified additional source-tail budget. Wrong-seed variants have the **same** `A_(j,M)`, so this instrument alone does not authenticate `U0=0` or force normality.

## COS-06 — Source-marked prime-square seams (EXACT ORIGINAL SOURCE, WITH MUTANT CONTROL)

For primes `p≥7`, the first BBP pole is a square at exactly

`j_p=(p²+7)/8`, because `8j_p−7=p²`. At `j_p`, the other three original denominators are `p²+3,p²+4,p²+5`, all `p`-adic units. Hence the **canonical p-primary fractional part** of `r(j_p)` is exactly **`4/p²`**. This is the specific `4/(8j−7)` source pole, not every prime event in the four-pole process. Define the signed-source-authenticated marker

`a_n=4/p²` if `n=j_p` for a prime `p≥7`, and `a_n=0` otherwise; `b_n=16^(−n)a_n`. A clock-indexed, p²-amplified representation is `m_n=p² a_n=4` at a seam and zero elsewhere. Recovering `p` from the absolute index uses `p=√(8n−7)`; a mere binary local flash without a timestamp does not furnish this label.

The declared matched-first-jet mutant `Q*=Q+(1−t)²` adds `2/[(8n−7)(8n−6)(8n−5)]`, changing the canonical p-primary fraction at every such seam to `5/p²`. The mark `4→5` is a source discriminator, but both sources have the same seam *timestamps*. Both are deterministic; no random prime-arrival process is asserted.

## COS-07 — Exact growing Hankel minors; no finite stationary Fourier/linear carrier (NEW-TO-SUCC EXPLICIT SOURCE RECEIPT, ELEMENTARY PROOF)

Let `p<q` be **consecutive** primes at least 7. Put `L=j_q−j_p=(q²−p²)/8`, `t=j_p+1`, and, for any source-mark sequence `v_n` supported at prime-square seam clocks with `v_(j_q)=w_q≠0`, define the `L×L` Hankel matrix `H_(a,b)=v_(t+a+b)`, `0≤a,b<L`. There are no seam events between `j_p` and `j_q`, so entries with `a+b<L−1` vanish and every entry at `a+b=L−1` is `w_q`. Reverse column order: the matrix becomes lower triangular with diagonal `w_q`. Therefore

**`det H = (−1)^(L(L−1)/2) (w_q)^L`**,

**independently of every later seam value** below the anti-diagonal. In particular:

- Binary seam marker `w_q=1`: `det H=±1`, a *unimodular* arbitrarily large Hankel minor.
- Amplified original BBP first-pole mark `w_q=4`: `det H=±4^L`; mutant `5`: `det H*=±5^L`.
- Actual p-primary mark `w_q=4/q²`: `det H=±(4/q²)^L` (mutant `5/q²`).
- Native radix-weighted p-primary mark `w_q=4/(q²16^(j_q))`: `det H=±[4/(q²16^(j_q))]^L`.

Since `q≥p+2`, `L≥(p+1)/2→∞`. The prime-square seam stream has **infinite Hankel rank over Q, R, and C**, hence no finite-dimensional stationary constant-coefficient linear realization and no finite sum of stationary exponential Fourier characters can produce the entire *seam indicator chronology*. This is an obstruction to a **finite stationary spectral model**, not to a short arithmetic program, nonlinear model, external clock oracle, or BBP's nonautonomous rational rule. The minor requires source reports through clock `t+2L−2=2j_q−j_p−1`, not merely to the next seam.

**Finite-state lower bound:** for a deterministic autonomous Moore machine emitting the binary seam stream, states at clocks `j_p+1,...,j_q` have distinct forward waiting times to the next 1, so the machine needs **at least L distinct states** even to generate the prefix through `j_q`. By Euclid there are arbitrarily large consecutive prime pairs; no fixed finite-state autonomous Moore generator exists. Stronger: by classical Bertrand's postulate, for every `N≥100`, choose `X=√(8N−7)`, an integer `m=⌊X/4⌋`, a prime `m<p<2m`, and its next prime `p<q<2p<X`. Then `j_q≤N` and `L≥(p+1)/2>X/8`. Thus an autonomous Moore machine matching the seam output **through clock N** requires **more than `√(8N−7)/8` states**. This is a *representation-size lower bound*, not an information-theoretic bit count or a physical space complexity lower bound for algorithms with a growing external clock.

## COS-08 — Prime-square seam analytic natural boundary (CLASSICAL FABRY + EXPLICIT SOURCE SPECIALIZATION)

For nonzero fixed mark `c∈C`, define `M_c(z)=Σ_(p≥7) c z^(j_p)`. The coefficients are constant magnitude at infinitely many exponents, so its radius is exactly 1. If the qualifying primes in order are `p_k`, then `p_k≥k+6`, hence `j_(p_k)/k≥((k+6)²+7)/(8k)→∞`. Fabry's gap theorem states that for radius-one power series supported at exponents whose `j_k/k→∞`, the unit circle is a **natural boundary**: there is no analytic continuation through any boundary point. Thus `M_4` and `M_5` have natural boundary `|z|=1`.

For the *actual positive source-selected p-primary weights*,

**`A_4(z)=Σ_(p≥7) (4/p²)(z/16)^(j_p)`**, and `A_5` analogously, have radius **16** because `(4/p²)^(1/j_p)→1`; their circle **`|z|=16` is a natural boundary** by the same Fabry theorem. This is about the *source-selected first-pole seam projection*, **NOT** the full BBP transform `F(z)` (which can have different analytic continuation). Fabry's theorem is imported, not reproved. References: [Encyclopedia of Mathematics, Fabry theorem](https://encyclopediaofmath.org/wiki/Fabry_theorem); [Puchta, On Fabry's Gap Theorem](https://www.bio.uni-rostock.de/storages/uni-rostock/Alle_MNF/Mathematik/Struktur/Lehrstuehle/Algebra/papers/Fabry.pdf).

## COS-09 — Gaussian origami: a natural boundary can disappear from the smoothed representation without source information vanishing (CLASSICAL, EXACT)

For fixed `λ>0`, apply a declared Gaussian Fourier multiplier to the **radix-weighted source projection**:

`A_(4,λ)(z)=Σ_(p≥7) [4/(p²16^(j_p))] exp(−λj_p²/2) z^(j_p)`.

Its radius of convergence is **infinite**: along nonzero coefficients, the `j_p`th root tends to `16^(−1)exp(−λj_p/2)→0`. The original `A_4` has a natural boundary at radius 16; its Gaussian-regularized image is entire. Nevertheless every multiplier is nonzero, so all **exact labelled coefficients** are in principle recoverable by division. The inverse on unrestricted ℓ² coefficients is unbounded because its cost at index n grows like `exp(λn²/2)` (and the same holds along seam indices `j_p`). **Analytic smoothness after an observer filter is not source erasure, a bounded reconstruction, or real-phase mixing.**

A legitimate Gaussian **probability** observer requires an additional normalized positive source measure, such as `μ_N=Σ_(p:j_p≤N) (4/p²)δ_(j_p/q mod1)/Σ_(p:j_p≤N)(4/p²)` (nonempty horizon and declared q), and then convolving with the positive periodized heat kernel. The Gaussian smoothed profile is a measure-level observation; no theorem says the actual prime arrivals are Gaussian-distributed, independent, or random. This distinction is inherited from Gaussian causal Yoneda #672 and wavefront #674.

## COS-10 — Fold the journal back into the carrier; preserve history iff it is actually retained (CLASSICAL, EXACT)

For a finite or infinite future atom stream `g=(c_1,c_2,...)` and a **retained** finite past journal `m=(c_{-k},...,c_0)`, define the *origami successor*

**`S(m,(c,g_tail))=(m||c,g_tail)`**.

On its image, `S` has the exact algebraic inverse that pops the final stored atom and prepends it to the future stream. The total sum `Σm+Σg` is invariant whenever it converges. On the original BBP trajectory, `Σm=P_n`, `Σg=G_n(1)` and the invariant is π/16. A physical embedded observer does not acquire the complete infinite g by executing one step; the inverse is a mathematical comparison of two representations of the same specified source.

If memory stores **only the scalar total P** rather than the actual transferred atom, then `(P,G)→(P+G(0),BG)` is generally many-to-one: for any `c`, `(P'−c,c+zG')` has the same image `(P',G')`. The equality `P+G(1)=constant` alone conserves a single scalar, **not every distinguishable global source history**. This is the exact receipt against interpreting an aggregate conservation equation as unrestricted information conservation. A controller with memory `m`, policy `π(m)` and lawful action `T_a` can be embedded into the augmented source `\tilde X=X×M` with `(x,m)→(T_(π(m))(x), δ(m,o(x)))`, retaining provenance and disturbance. This is causal feedback, not a spontaneous creation of new physical information.

## COS-11 — Honest source and spectral rejection controls (REFUTED SHORTCUTS; EXACT)

1. **Wrong seed:** the same `r(n)` with `s=−π/16` has identical source-time `F`, original p-square seam journals, and Fabry/Hankel receipts, while its completed real phase `16^n(x+s)` is identically zero. The authenticated root with `U0=0` rejects it, but no source/seed-blind spectral result implies R0.
2. **Wrapped alias:** `s=1/16` produces identical late circle phases at every `n≥1`, but distinct unwrapped seeds. Adding arbitrarily many phase-only heads cannot recover the lost root; source-history heads can.
3. **Matched first jet:** `Q*=Q+(1−t)²` keeps selected low-order source asymptotics but changes the original p-square mark `4→5`. The event times and gap complex structure stay identical; signed amplitude must be retained to identify the source.
4. **Finite model closure:** 2D swap vs hidden flipping bit show journal faithfulness depends on observer separation. A timestamped path category may be faithful **as a labelled trajectory** without revealing an unseen internal graph; source-map adequacy and lawful interventions are separate.
5. **Gaussian counterfeit:** all seam coefficients can be regularized to an entire function while the original seam series has a natural boundary. Smoothing does not prove source equidistribution, observer independence, or bounded inverse.
6. **Fourier type mismatch:** the integer event-time spectrum, p-adic odometer spectrum, auxiliary 11-adic Fibonacci eigenframe, and the circle Weyl sums of the π orbit are different typed representations. No conjugacy or normality follows from matching a particular frequency or generating a Fourier basis.

## COS-12 — The unrepaid π-normality theorem and prospective proof test (OPEN)

The original zero-seeded π phase remains `θ_n={16^nx}`. R0 demands `liminf_(B→∞) B^(−1)Σ_(n=B)^(2B−1)[1−cos(2πθ_n)]>0`. Full normality requires `W_B(h)→0` for all nonzero integer h. The present theorems prove structural equivalence, a new explicit source-tail integral/asymptotic, exact Fourier alias bounds, source-selected infinite-rank/minimum-memory inequalities, and a Fabry natural boundary for one arithmetic projection. **They do not prove R0 or full normality.**

Potential proof: define a **predeclared signed cross-observer witness** using original BBP zero seed, the source-marked prime-square seam time series (including 4/p² and full cofactor), independently conditioned moving/11-adic and 3/5-adic frames, the unwrapped carries, and the actual real-phase Gaussian observer. Define a same-source, correctly demodulated transfer that yields a nonzero signed all-shell lower bound and is falsified by seed/source/gauge controls. The new rank and boundary theorems **do not themselves** yield such an estimate: infinite source Fourier complexity can coexist with a locked real-phase observable.

**Verdict:** finite/analytic seam and prime-source infinite Fourier complexity are PROVED within declared domains; 'literal Yoneda' is exact on a faithful action-category presentation and conditional on dense probes for larger carrier categories; a Gaussian or randomly encountered prime model is **not automatic**; source-selected signed Archimedean normality saving remains **UNVERIFIED**.
