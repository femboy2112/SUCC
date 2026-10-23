# Secondary Circle Reconstruction: complete-prime coherence, chord geometry, and finite defect certificates

**Date:** 2026-10-23. **Research-only.** Parent: SUCC draft PR #247, head `5a2922986719c03dfd4e20d23d3b266b8b775c8e` (stacked on Reality Pin #244), not `main`. Neither source archives nor installed formal theorem authority are modified. Sibling drafts #229, #231, #232, #245 and #246 are compared and **not** silently incorporated. Academic novelty of this synthesis and finite quantitative bound is **UNVERIFIED**. None of the claims below proves π-normality or RH.

## 0. Steelman and type of the reconstruction

The original Euclidean circle and its exact quotient `circumference / diameter = π` remain geometrically valid. The *secondary circle* is the measured compact dynamical system reconstructed from source-indexed arithmetic observations: a fixed metric circle `T=R/Z`, its multiplier maps `T_n(x)=nx mod 1`, and the empirical **measure** `ν_N=(1/N)Σ_{j<N}δ_{T_b^j α}`. A nonuniform reconstructed measure is a measured-geometry defect, **not** a proof that the source metric ceases to be Euclidean.

The user's strongest noncircular proposal is: π's independently authenticated geometric source forces a sufficiently complete, *time-indexed* family of joint prime-action coherences **and** a geometric chord calibration; then the induced arithmetic observation measures cannot have non-Haar limits. We must not define lawful transport to mean Haar equidistribution. The conditions below are explicit analytic obligations and receive no authority merely from existence of the maps or the original circle's Haar ensemble.

Notation: `e(t)=exp(2πit)`, `q(x)=|1-e(x)|²=2−2cos(2πx)`, and `F_m(q(x))=q(mx)` for the integer chord/Chebyshev polynomials already implemented in PR #247. For a Borel probability μ on T, `c_h(μ)=∫cos(2πhx)dμ`, `a_h(μ)=∫e(hx)dμ`. Thus `∫F_h(q(x))dμ=2−2c_h(μ)`.

## SCR-01. Classification of complete-prime invariant circle measures (CLASSICAL / PAPER)

**Theorem.** If `T_p* μ=μ` for **every genuine prime** `p`, then

`μ=c δ_0+(1−c)λ` for `c=μ({0})∈[0,1]`, where `λ` is normalized circle Haar measure.

**Proof.** By unique factorization, all integer multipliers preserve μ. For each integer `h>=1`, `a_h(μ)=a_{hn}(μ)` for every `n>=1`. Average over n. The bounded Dirichlet averages `M⁻¹Σ_(n=1)^M e(hnx)` converge pointwise to `1` precisely when `hx=0 mod 1`, otherwise `0`. Dominated convergence gives `a_h(μ)=μ(T_h^-1{0})`. Invariance under `T_h` makes the latter `μ({0})=c`. All nonzero positive Fourier coefficients equal `c`; negative coefficients are their conjugates, also `c`. The measure `cδ_0+(1-c)λ` has exactly these Fourier coefficients. Uniqueness of finite Borel measures from all their trigonometric moments proves equality. QED.

**Corollary (single-chord selection).** Under complete-prime invariance, `∫q dμ>=2` forces `c=0` because `∫q dμ=2(1-c)`. Therefore μ=λ. The inequality is one-sided: oversampling the opposite arc can give `∫q>2` without invariance; one chord measurement alone is insufficient.

**Sharp controls:** δ_0 has all-prime invariance but chord mean 0. The uniform **5-gon** `μ_5=(1/5)Σ_(j=0)^4δ_(j/5)` has chord mean **exactly 2**, and is invariant under every prime `p≠5` (permutation of vertices); `T_5*μ_5=δ_0`. Thus omitting just **one** prime from the action language invalidates the all-prime theorem, even with perfect first-chord calibration. Finite-subset invariance is not complete-prime invariance.

**Comparison with Furstenberg:** the class of measures invariant only under `T_2` and `T_3` is not completely classified in general; we do not claim to solve the Furstenberg ×2×3 measure rigidity conjecture. The all-prime hypothesis is materially stronger and makes the present classification elementary. See Furstenberg (1967), Rudolph (1990), Einsiedler–Fish (2009) [below].

## SCR-02. Failure of normality forces a singular measured-circle defect (CLASSICAL / PAPER)

Fix b>=2 and `ν_N^α=N⁻¹Σ_(j<N)δ_{T_b^jα}`. For every continuous φ, the endpoint telescope gives

`|∫φ d(T_b*ν_N^α)−∫φ dν_N^α|<=2||φ||∞/N`.

Consequently every weak subsequential limit μ is `T_b`-invariant. If α is nonnormal to base b, the full sequence does not converge to λ, hence compactness provides **some** subsequence with invariant limit μ≠λ.

Any `T_b`-invariant probability has a Lebesgue decomposition `μ=fλ+μ_s`, and the two components are individually invariant: the Lipschitz covering `T_b` sends Haar-null sets to null sets and preserves absolute continuity. Invariance of the full measure and uniqueness of the decomposition imply invariance of each component. For h≠0,

`widehat f(h)=widehat f(b^j h)→0` as j→∞ by the Riemann–Lebesgue lemma. Therefore `f` is a constant almost everywhere, i.e. μ=cλ+μ_s. If μ≠λ, then `μ_s` is nonzero.

**Correct interpretation:** the secondary measured circle has a singular statistical component, not necessarily a singular Euclidean metric. The original geometric circle has no defect.

## SCR-03. Some chord harmonic detects the defect at every dilation scale (PAPER)

Let `R(x)=−x`, and let `q:T→[0,4]` be the chord quotient. If `q_*μ=q_*λ`, every R-even continuous test has the same integrals under μ and λ. Hence `(μ+R_*μ)/2=λ`. Positivity implies `μ<=2λ`, so μ is absolutely continuous. If μ is also `T_b`-invariant, SCR-02 forces μ=λ.

**Contrapositive:** any non-Haar `T_b`-invariant μ has `q_*μ≠q_*λ`. Since polynomials are dense in `C([0,4])`, at least one positive integer k has

`∫q(x)^k dμ != binom(2k,k)`,

or, equivalently, there is a positive integer `h` with `c_h(μ) != 0` (because `F_h(X)=2−2cos(2πh x)` and Chebyshev polynomials span the polynomial observables).

For that h, `T_b`-invariance gives **all-lag persistent discrepancy**

`∫F_(h*b^j)(q(x)) dμ = 2−2c_h(μ) != 2` for every j≥0.

A finite selected orbit subsequence that converges to μ has its corresponding harmonic moments tending to this non-Haar value. Do not confuse fixed-h subsequential convergence with a uniform-in-h or uniform-in-j numerical bound.

**Exact control:** the full multiplicative unit orbit of 1/9 under T_2 has `c_1=0` and `∫q=2`, yet `c_(3*2^j)=−1/2` and `∫F_(3*2^j)=3` for every j. This follows from Ramanujan sums `c_9(1)=0`, `c_9(3)=−3` normalized by φ(9)=6. A perfect first-chord reading does **not** certify the secondary circle.

## SCR-04. FINITE quantitative complete-prime cosine rigidity (PROVED PAPER / EXACT MODEL)

This is the central new-to-project proof instrument, independent of asymptotic compactness.

Let μ be **any actual probability measure** on T (no invariance assumed), M>=2, and define

`ε_M= max_{p prime, k>=1, pk<=M}|c_(pk)(μ)−c_k(μ)|`,
`L_M=floor(log_2 M)`, `d_M=L_M ε_M`,
`η_M=max(0, 2−∫q dμ)=max(0,2c_1(μ))`.

**Theorem (explicit finite error budget).** For every 1<=h<=M,

`|c_h(μ)| <= min(1, max(η_M/2+d_M, 1/(M−1)+2d_M))`

and the looser additive certificate is

`|c_h(μ)| <= η_M/2 + 1/(M−1) + 2 L_M ε_M`.

**Proof.** Factor each positive integer h<=M into its canonical prime word. Every multiplication step relates `c_k` to `c_(pk)` with `pk<=M`. Triangle inequality along at most `Ω(h)<=L_M` steps gives `|c_h−c_1|<=d_M`. Now use the classical nonnegative Fejér kernel

`K_M(x)=M^-1 |Σ_(j=0)^(M-1) e(jx)|²=1+2Σ_(h=1)^(M-1)(1−h/M)cos(2π h x)`.

Integrating gives `0<=∫K_M dμ`. The weights sum to `(M−1)/2`, hence

`0<=1+(M−1)c_1+E`, `|E|<=(M−1)d_M`.

Therefore `c_1>=−1/(M−1)−d_M`. From the chord premise, `c_1<=η_M/2`. Together these imply `|c_1|<=max(η_M/2,1/(M−1)+d_M)`, and the prime-word triangle proves the stated bound for all h<=M. The trivial |c_h|<=1 supplies the cap. QED.

**Inverse/defect certificate:** if a source-authenticated real harmonic has `|c_h|>=ρ` at some h<=M but the chord deficit is at most η, then necessarily

`ε_M >= max(0, ρ−η/2−1/(M−1))/(2 L_M)`.

This is a concrete either-chord-or-prime-coherence defect witness, not an appeal to generic mixing. For M=2 the denominator `L_M` is already 1. A missing prime at band edge can be detected automatically.

**Authority boundary:** the Python module accepts exact rational moment arrays and checks elementary necessary positivity, but arbitrary supplied arrays are NOT authenticated observations. The theorem is valid only when these are moments of an actual probability source. Genuine rational-orbit sources, complete uniform polygon sources and independently enclosed polygon-π moments have dedicated adapters.

## SCR-05. Finite orbit covariance amplifies real chord bounds to complex Fourier control (PROVED PAPER)

For the **actual base-b orbit** `ν_N^α` and nonzero integer h, set

`A_(h,N)=∫e(hx)dν_N^α`,
`Z_R(x)=R^-1 Σ_(r=0)^(R−1)e(h b^r x)`.

The endpoint shift gives `|A_(h b^r,N)−A_(h,N)|<=2r/N`, so

`|A_(h,N)−∫Z_R dν_N|<=(R−1)/N`.

By Cauchy–Schwarz and the exact pair-correlation expansion,

`|∫Z_R dν_N|² <= ∫|Z_R|² dν_N`
`=1/R+(2/R²)Σ_(0<=s<r<R)c_(h(b^r−b^s))(ν_N)`.

If M>=|h|(b^(R−1)−1), all these frequency indices lie between 1 and M. Apply SCR-04's uniform real bound `B_M` to obtain

**`|A_(h,N)| <= (R−1)/N + sqrt( 1/R+(1−1/R) B_M )`.**

Every displayed error is explicit. There is no assumed spatial-to-temporal mixing, random independence, spectral positivity transfer to Weil, or hidden π-digit oracle. This estimate is new-to-SUCC synthesis of elementary positive-definite harmonics; scholarly priority is UNVERIFIED.

The stdlib checker returns a dyadic rational **upper** square-root bound, not a floating approximation. It enforces the lag/frequency budget `M>=|h|(b^(R−1)−1)` and rejects malformed sources. The bound may legitimately be 1 for a short finite π sample; this is **not** evidence of normality.

## SCR-06. Conditional normality criterion and the exact remaining wall (PROVED IMPLICATION, OPEN HYPOTHESES)

For any fixed b>=2 let the actual π orbit measures have chord deficit η_N and joint genuine-prime cosine defect ε_(M,N) as in SCR-04. Suppose some integer band M_N satisfies:

1. `M_N→∞` and `log M_N=o(N)`;
2. `η_N→0`;
3. `floor(log_2 M_N)*ε_(M_N,N)→0`.

Then **π is normal in base b**.

Indeed choose `R_N=floor((1/2)log_b M_N)` for every fixed frequency h. Eventually `R_N→∞`, `R_N/N→0`, and `|h|(b^(R_N−1)−1)<=M_N`. SCR-04 makes `B_(M_N,N)→0`, and SCR-05 makes each `A_(h,N)→0`. Weyl's criterion finishes the proof.

**The conditions are NOT proved for π.** Commutativity of `T_p` with `T_b` gives no uniform bound on the selected π orbit's prime defect ε. The geometric `C/D=π` source fixes the starting number, but does not by itself bound a time-average. The task is to derive (2) and (3) from π's authentic circle/polygon/Wallis/BBP/lattice-shell source; success must survive the following hostile controls.

## SCR-07. Adversarial countermodels (REFUTED inferences, exact sources)

| Tempting shortcut | Source-faithful witness | Exact defect |
| --- | --- | --- |
| All-prime coherence alone forces Haar | α=0; ν_N=δ_0 | ε_M=0, ∫q=0, η=2 |
| Correct first chord moment alone forces Haar | α=1/9 under b=2; full unit orbit | c_1=0, c_(3*2^j)=−1/2 for every j |
| All but one prime suffice | uniform 5-gon | ∫q=2, invariant under all primes except p=5; c_5−c_1=1 |
| Arbitrarily large finite moment band proves infinite Haar | uniform q-gon with q>M and gcd(q,b)=1 | c_h=0 for 1<=h<=M, yet atomic non-Haar |
| Uncontrolled first moment proves normality even without time-orbit law | μ(dx)=(1+sin(2πx))dx | c_h=0 for all h, but a_1=i/2; T_b-invariance fails |
| Finite π interval or moment certificate proves limit | Any fixed-degree rational π approximation | eventual periodic orbit; limit-order error cannot be interchanged |
| An irrational source excludes δ_0 limiting observations | α=Σ_(k>=1)2^(−k²) | irrational, binary ones density 0, ν_N→δ_0 |

**Proof of the last row:** outside the at-most `K(√(N+K)+2)` starting indices lying within K places of a square digit, the next K binary digits are all zero, so the fractional orbit coordinate is at most `2^-K`. First let N→∞ at fixed K, then K→∞. Every empirical weak limit is δ_0. The digit string is not eventually periodic because the gaps between square positions diverge, so α is irrational. All prime semigroup laws remain perfectly valid at the source level. Therefore selection specificity—not irrationality, dimensional completeness or symmetry—must carry the proof.

## SCR-08. π-source exact finite observation and source-closure discipline

This stacked branch REUSES the authenticated PR #247 `pi_interval()` Archimedean brackets and its exact rational `_cos_enclosure()`; there is no π digits input. Each h-step phase interval `[h b^j L,h b^j U]` is reduced in exact turns and pays its own source phase error plus π-in-the-radian-map uncertainty. This yields rational enclosures of each c_h(ν_N^π), including interval upper budgets η and ε. All were intentionally evaluated at finite `(N,M)`—no infinite limit claim. An independent Machin rational source and independent Taylor oracle are proposed holdouts, not a source fed into the production computation.

**Important:** the squared chord angle uses the *number* π as the base-b phase, not simply a geometric half-turn at angle π radians, which has normalized phase 1/2 and is periodic. These are different source-to-angle maps. Likewise the arithmetic lattice needed for circle lattice-shell counting is an extra declared source; it does not arise from a bare unmarked Euclidean circle.

## SCR-09. Research verdict and falsification contract

**Established**: exact reconstruction defect topology (singular non-Haar invariant limit), persistent chord-harmonic witness, complete-prime Haar/Dirac classification, universal finite Fejér–prime–chord bound, and finite amplification into full Fourier control for an honest orbit. Existing PR #247 provides separate finite Fejér *collision energy*; this new instrument measures single-orbit chord harmonics and explicit prime coherence defects. Neither theorem subsumes the other as a useful source probe.

**Not established**: any growing-band estimate of η_N or ε_(M_N,N) for the π-selected orbit; absolute normality, RH, signed Weil positivity, or academic novelty. A bound for finitely many N cannot validate its infinite-horizon continuation. No paper theorem here has been newly Lean-kernel checked.

**Decisive next attempt:** use the *specific* π-generating recurrence (nested chord source, BBP forcing, Wallis/Kummer and Gaussian-shell source) to prove η_N→0 and `ε_(M_N,N)=o(1/log M_N)` for a diverging, subexponential M_N. Predict contrary signatures on α=0, 1/9, finite 5-gons, sparse-square irrational and degree-bounded fake π sources before testing the actual pi interval oracle. If neither estimate survives, preserve the negative mutant and try a distinct source/observable basis rather than redefining “lawful” as “normal.”

**External primary literature / classical dependencies:** H. Furstenberg, *Disjointness in ergodic theory, minimal sets, and a problem in Diophantine approximation* (1967); D. Rudolph, [×2 and ×3 invariant measures and entropy](https://doi.org/10.1017/S0143385700005629) (1990); Einsiedler–Fish, [rigidity of measures for multiplicative semigroups of polynomial growth](https://people.math.ethz.ch/~einsiedl/manfred_sasha_entropy_2.pdf) (2009). Other ingredients: Fejér positivity, unique Fourier representation of measures, Lebesgue decomposition, Riemann–Lebesgue, Weyl, Chebyshev and CRT as credited classical results. No borrowed two-prime measure-rigidity conjecture is marked proved.

## SCR-10. No hidden geometric gauge can repair a defective secondary circle (PAPER)

**Centralizer theorem.** Let `h:T→T` be a circle **homeomorphism** satisfying `h∘T_2=T_2∘h`. Then **h is either identity or reflection** `R(x)=−x`. This is a sharp statement about homeomorphisms with original doubling dynamics, not about arbitrary continuous semiconjugacies, general finite-to-one maps, or other chosen transformation languages.

**Proof.** Since `T_2h(0)=hT_2(0)=h(0)`, `h(0)` is fixed by doubling; its only fixed point is 0. For every n, the exact preimage set `P_n=T_2^{-n}{0}={j/2^n:0<=j<2^n}` must be mapped bijectively onto itself by h. An orientation-preserving circle homeomorphism induces a cyclic-order-preserving permutation of P_n. The only such permutation fixing 0 is the identity on P_n. All dyadic grids are therefore fixed pointwise, and their union is dense; continuity forces `h=id`. If h is orientation-reversing, then `R∘h` is orientation-preserving and commutes with doubling, hence is identity; thus `h=R`. QED.

**Measured-geometry corollary.** If a non-Haar secondary circle `(T,d,μ)` is reparameterized by such a lawful h, then `h_*μ` cannot be Haar: if h is id or reflection and `h_*μ=λ`, reflection invariance of λ implies μ=λ, contradiction. This is the precise sense in which the nonuniform reconstruction cannot be 'made into a perfect measured circle' by a gauge that preserves doubling. The original Euclidean circle geometry remains completely intact.

**Scope necessity:** for b=3, a nonzero translation by 1/2 *does* commute with T_3 because `(b-1)c=0 mod 1`; the b=2 fixed-origin argument is special. Any global claim for all b needs the appropriate finite rotational centralizer. If one abandons equivariance altogether, an atomless full-support measure may be reparameterized to Haar by its distribution function; that operation changes the dynamics and is not a repair within the declared source/action contract.

## SCR-11. Min-plus source-aware prime-word transport, a strictly stronger finite estimate (PAPER / EXACT TESTED)

The uniform `L_M ε_M` term in SCR-04 throws away which prime-factor **path** is actually reliable. The full circle semigroup supplies multiple factorizations that reach the same geometric state. Their endpoints commute; their *measured error budgets* need not be equal. A source-faithful observer may choose the least-expensive admissible proof route, without changing any mathematical transformation.

For exact authentic cosine moments define `d_1=0` and recursively for `n>=2`,

`d_n = min_(p genuine prime | n) [d_(n/p)+|c_n−c_(n/p)|]`.

Each minimizing path is a chain of genuine prime coverings; every term is exact and nonnegative. By telescoping along that path, `|c_n−c_1|<=d_n`. For supplied **rational enclosures** of coefficients, replace each edge by the maximal absolute difference between the corresponding two intervals; the same inequality survives uniformly for every compatible source. A previous composite factor is never falsely promoted to a new independent prime generator.

Set

`W_M = [2/(M−1)]Σ_(n=1)^(M−1)(1−n/M)d_n`.

The Fejér proof of SCR-04 now gives the **sharper individual and uniform estimates**

**`|c_h|<=min(1,d_h+max(η/2,1/(M−1)+W_M))`, for every 1<=h<=M.**

Since `d_h<=Ω(h)ε_M<=L_M ε_M` and the Fejér weights sum to `(M−1)/2`, `W_M<=L_M ε_M`; this never gives a weaker bound than SCR-04's uniform estimate. A proposed empirical theorem may use `max_(h<=M_N)d_h→0` instead of the stronger `L_M ε_(M_N,N)→0`; the same SCR-05 amplification proves normality as long as the chord deficit and horizon hypotheses are also discharged.

**Proof** is only nonnegative Fejér integration plus a finite min-plus shortest-path recurrence on the canonical divisor directed acyclic graph, not a new multiplicative independence theorem. It composes with source-retained future histories and avoids assuming an arbitrary factor order is cheapest. The math is an exact realization of SUCC's 'same boundary, multiple lawful paths' ethos; independent academic novelty remains **UNVERIFIED**.

**Hostile controls:** the synthetic moment-like vector `c_1=0,c_2=1/4,c_3=1/2,c_6=1/3` has 1→2→6 path cost `1/3` versus 1→3→6 cost `2/3`, although both routes end at multiplier six. This synthetic vector is **not asserted to be a probability source**; it tests the combinatorial optimizer only. Genuine rational source families q=3,5,7,9 and their outward exact intervals verify that the min-plus bound encloses every actual harmonic and never exceeds the preceding uniform budget. The finite π sample remains at the honest trivial bound 1.
