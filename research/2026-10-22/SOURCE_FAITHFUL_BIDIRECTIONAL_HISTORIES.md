# SUCC ↔ FUCC: source-faithful bidirectional histories and stopped prime-Pascal geometry

**2026-10-22 · Research draft, stacked on [HISTORY-DTN PR #237](https://github.com/femboy2112/SUCC/pull/237) at 391c304e768d073ae747459d279e14d5357092e5.** Cross-reading: reciprocal prime/Gibbs [PR #236](https://github.com/femboy2112/SUCC/pull/236), coherent arithmetic code [#235](https://github.com/femboy2112/SUCC/pull/235), observation-pinned geometry [#238](https://github.com/femboy2112/SUCC/pull/238). Classical mathematical components are credited as such. No RH/Weil positivity, gravitational ER=EPR, retrocausal signal, or physically derived prime law is claimed.

### Steelman and typed source

The motivating requirement is “SUCC looking backward while advancing forward has to agree with FUCC looking forward while advancing backward, within the same system.” Here *agree* means compatible predictions on complete, ordered **source-labelled histories** and a common probability measure—not merely coincident endpoints. Physical growing-graph events, arithmetic sampling clocks, Hilbert adjoints, and Bayesian retrodiction are distinct types. The first two can be related through a declared observation interface, but identifying arithmetic FUCC with an intrinsic material process remains UNVERIFIED.

### SBH-01 — exact history composition; the affine square is a common refinement

Let finite chronological layers X_0,...,X_T have rational nonnegative labelled kernel K_t(x,label,y), with row sum one even across parallel labelled channels. A full source history γ=(x_0,label_0,x_1,...,label_(T−1),x_T) has probability μ_0(x_0) times the product of its transition weights. For s≤r≤t, splitting at r is a bijection between complete histories over [s,t] and composable histories over [s,r] and [r,t]. Its inverse is concatenation and weights multiply, so the source-history kernel composes associatively. Proof: ordered paths have exactly one state and label at each tick; splitting/concatenating partitions/reconstructs that data and its product measure exactly. This is classical marked-path probability, not a new form of physics.

For genuine prime p and n≥1 the arithmetic identity V_p S=S^p V_p gives two *observation-clock itineraries* from n to p(n+1): (n,n+1,p(n+1)) and (n,pn,pn+1,...,p(n+1)). Each is a differently bracketed observation of the **same source microhistory**. Upon *retaining all intervening source events* and forgetting only artificial grouping delimiters, the induced full-path laws are equal, even if stochastic and branching. But the checkpoint receipts themselves can differ; equality on full source paths DOES NOT identify two distinct measurement schedules. The executable affine_history_square reports these two different results separately. This is a source-faithful *common-refinement span*, not an assertion of teleportation or physical prime multiplication.

### SBH-02 — complete forward/Doob and backward/Bayes path identity

Define forward α_(t+1)(y)=Σ_(x,label)α_t(x)K_t(x,label,y), and backward h_t(x)=Σ_(label,y)K_t(x,label,y)h_(t+1)(y), with terminal h_T=1_A. The overlap Z=Σ_x α_t(x)h_t(x)=Pr(A) is identical at every cut. For α_(t+1)(y)>0 set

    R_(t+1)(y;x,label)=α_t(x)K_t(x,label,y)/α_(t+1)(y).

For h_t(x)>0 the success-conditioned forward kernel is

    K_t^A(x;label,y)=K_t(x,label,y)h_(t+1)(y)/h_t(x).

For every positive-probability complete path, when Z>0,

    P(γ|A)= μ_0(x_0) [∏_t K_t(x_t,label_t,x_(t+1))] 1_A(x_T)/Z
           = [α_T(x_T)1_A(x_T)/Z] ∏_(t=T−1...0)R_(t+1)(x_(t+1);x_t,label_t).

Proof: substitute the reverse formula and telescope α-ratios along the history. This holds on EACH labelled history, not merely on terminal states. Values off support require separate conventions; Z=0 makes conditional probability undefined. Our exact-rational hostile example has Z=23/60, two surviving selected histories, and complete forward/backward agreement. A future-conditioned Bayesian reverse is neither physical reverse causation nor a prime Hilbert adjoint.

### SBH-03 — endpoint-only reverse is obstructed

Two distinct labelled sources a,b both deterministically reach z. Priors (1/4,3/4) and (3/4,1/4) give identical terminal observation z but different Bayesian predecessor probabilities. Hence no prior-independent reverse kernel from z alone can reconstruct both source histories. If labels are discarded, source multiplicity is lost as well. This is a decisive counterexample against any unconditional endpoint-only inverse; it does not obstruct posterior reconstruction when the full source law is retained. HISTORY-DTN independently supplies the geometrically meaningful hidden-edge witness: identical present boundary response, later intervention producing 7/6 versus 49/41.

### SBH-04 — a genuinely projective stopped prime-word history source

Let P be a finite set of *genuine primes*, β>1, and t_p=p^(−β). Independently sample geometric prime-power counts A_p≥0 with Pr(A_p=a)=(1−t_p)t_p^a. Given occupation multiset α, let k=Σ_p α_p, uniformly order its k occurrences among the k!/∏_p α_p! distinct words, and append an absorbing **STOP** marker. A specific completed word w has probability

    q_P(w)= [∏_(p in P)(1−t_p)t_p^(α_p)] · [∏_p α_p!]/k!.

Normalization: sum over all permutations of α cancels the second bracket, then sum over all independent geometric occupations gives one. For any P'⊂P, delete every symbol whose prime lies outside P'; **the entire stopped-word law**, not just the terminal product, projects EXACTLY to q_(P'). Proof: independent geometric counts on P' have their original marginal law, and the relative order of the selected letters from a uniformly random multiset permutation is itself uniform. The finite executable uses per-prime caps A_p≤M normalized *independently*, so this deletion law holds exactly at every finite cap. Globally conditioning on total rank and separately normalizing each rank does NOT give that result.

For ALL genuine primes and β>1, Σ_p p^(−β)<∞. Borel–Cantelli implies only finitely many positive counts almost surely, and every count is itself finite. This determines an almost surely finite prime word. Unique factorization and the absolutely convergent Euler product yield terminal

    Pr(N=n)=[∏_p(1−p^(−β))]n^(−β)=n^(−β)/ζ(β).

This is a classical infinite probability theorem with an explicit proof outline; no computational finite-range test is promoted to that universal claim.

### SBH-05 — stopped forward rule and exact backwards Pascal cotransition

Let m(α) be the probability of one particular ordered prefix with occupation α, and q(α) the probability it is the entire completed word. By exchangeability m depends only on the counts, not order. Every continuation either immediately stops or chooses prime p:

    m(α)=q(α)+Σ_p m(α+e_p).

Thus Pr(STOP|α)=q(α)/m(α) and Pr(next=p|α)=m(α+e_p)/m(α) on positive support, with total one. Successive prefix-mass ratios telescope: the probability of any completed ordered word is exactly q(α). Conditional on having observed rank k>0 with occupation α, the last-prime cotransition is α_p/k, because the complete word order was uniform.

The correctly aggregated rank-k **survival** mass is u_k(α)=k!m(α)/∏α_p!, and it obeys the killed/backward identity

    u_k(α) = stop_k(α)
           + Σ_p u_(k+1)(α+e_p)·(α_p+1)/(k+1),

where stop_k(α)=k!q(α)/∏α_p!. This is *subprobability* compatibility with an absorption term, not strict projectivity of separately normalized rank distributions. Preserve the hostile corpse from PR #236: for primes 2,3 and β=2, naive normalized rank-1 gives 9/13 for prime 2, but separately normalized rank-2 pushed back by α_2/2 gives 99/133. These are unequal. The common *stopped* law repairs the missing source, it does not make the dead rank-normalization claim true.

Finite exact receipt: primes (2,3,5), β=2, per-prime cap 2: 271 completed ordered words, 27 killed-Pascal recursions, 66 projected words checked independently, empty-word mass 90000/138229. These are exact model computations, not material experiments.

### SBH-06 — high-carry source-locality obstruction

Use authentic prime occupation v(n)=(v_p(n))_p with ℓ1 edit distance. At n=2^k, v_2(n)=k whereas n+1 is odd, so v_2(n+1)=0. Hence ||v(n+1)−v(n)||_1≥k for every k≥1. For any proposed uniform finite prime-occupation edit budget C choose k>C; a single additive SUCC n→n+1 cannot be implemented by that bounded-edit rule on every state. Prime FUCC n→pn adds one occupation unit. This is a decisive no-go in the **declared prime-occupation locality metric only**: unboundedly deep composed local steps or other physical/geometric localities are not excluded. It aligns with the finite-prefix boundary/channel and geometric noncanonicity caveats of PRs #235 and #238.

### Verdict, receipts and next physical discriminator

SURVIVES: a shared, *fully labelled* stochastic history law with exact forward/backward reconstruction, a source-faithful arithmetic rebracketing of microhistories, and an independently genuinely projective **stopped prime-word source**. REFUTED as general inferences: prior-free endpoint inverse; equality of distinct checkpoint receipts; naive per-rank-normalized Pascal projectivity; uniform bounded prime-edit SUCC; an optical Cherenkov signal from a quasistatic DtN solution. UNVERIFIED: any intrinsic material source functor that maps real discharge-event morphology and conditional statistics to **genuine prime multiplication**. Its next decisive instrument is a calibrated physical source map and a held-out observation that discriminates an alternative mapping. No physical high-voltage experiments are proposed. Academic novelty, source-derived Weil positivity, RH, and ER=EPR gravity are not claimed.

Reproduce with 16 tests, scripts/bidirectional_source_histories_probe.py --check, pinned source Git blob SHA-1 values, and focused GitHub CI on Python 3.10 and 3.13. Lean and full-repo validation are separate.
