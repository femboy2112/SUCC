# Source/observer map: realized paths, admissible futures and signed BBP phase

| Layer | Mathematical object | Data preserved | Explicit boundary / negative result |
|---|---|---|---|
| Original arithmetic | `(n,U_n,r(n),U0=0)` and ordered affine F_n | All four rational BBP poles, literal zero seed, full rational states | Exactly ONE true forward trajectory; no objective stochastic choice law derived |
| Full ordered path | Word γ and every source/history state, reference transition prior | Noncommuting affine matrix products; future support/branch identity | Costs/priors must be independently declared; time-reordering source r(n) is counterfactual |
| Observer `q` | Visible position only, `q(A)=q(B)=1` | Same current output state | Different future supports `{T,X}` vs `{T,X,Y}` and target odds 3/4 vs 1/4: no Markov descent or realization-faithful quotient |
| Virtual field | Probability measure on completed histories | Full path alternatives, conditional normalization | Observer inference, not necessarily physical realization |
| Actualization | Known positive-mass prefix η, event E | Bayes posterior; event information `−log Q(E)`; KL exact | Shannon entropy of remaining futures can increase; no automatic thermodynamic heat |
| Directional cost-to-go | Desirability H_t(s), V_t(s)=−β^-1 log H_t(s), tilted edge policy | Future viability and declared energy, zero-temperature shortest-cost limit | A geodesic is conditional on metric/cost/end; ties and sampling remain |
| Canonical BBP momentum | Real symplectic phase plane (x,p), source-labelled Hamiltonian H_n | p→p/16, time-one F_n, `A_n=x_np_n` exact source action | Different from the information costate V_t; no physical Lorentz/GR law derived |
| Unit-generator band | G_n²=G_n and G_iG_j=G_j; ordered products | Exact first-to-last original BBP history and combinatorial subset multiplicity | An algebraic subset expansion, NOT probability/quantum path measure |
| Source-pole sphere | PR442 four-punctured logarithmic differential | Abelian winding and source/infinity regulator | Pole residues alone DO NOT determine a time-indexed non-Abelian monodromy representation |
| Canonical scalar-action Gibbs time tilt | `A_n=U_n/16^n→π/16`, weights positive Lipschitz f(A_n) | All original source/action increments | Provably changes the N-term signed Weyl mean by at most `L/(512cN)` for L>0, so no normality upgrade |
| Signed phase | `exp(2πih U_n)` for each literal zero-seeded source index | Original π-normality Weyl gate, all complex cross terms | Positive path KL or endpoint action does NOT constrain signed asymptotic cancellations |

## Practical adequacy requirement

A mathematical target `P` descends through a proposed coarse observer map `q` **iff `P` is constant on every q-fiber**. A closed transition also descends only if future `q`-observable transitions are independent of the representative in each fiber (strong lumpability). Here, A and B have identical visible position and *different* next-step support/probabilities, so they cannot be quotient as a Markov state without retaining history.

### Source-faithful microhistory warning

Within a given original BBP step, `V16;T_r` and `T_(r/16);V16` both yield the same real affine function, but intermediate states and possible declared process cost differ. For authentic source-seed dynamics the genuine `exp(2πihU_n)` is the SAME on both. An imposed preference for one route would be external unless the source or a separately verified physical law provides it.

### Next genuine amplitude instrument

For a candidate path space carrying both positive weights and independently *source-attested* signed characters, define separately:

`Z_positive = Σ_γ R(γ)exp(−β C_γ)` and `A_signed = Σ_γ R(γ)exp(−β C_γ)χ_source(γ)`.

Require a verifiable character/holonomy map from actual time-indexed BBP to χ, **not** an arbitrary phase inserted for desired cancellation. A generic positive model does not define χ. Do not confuse source-only 2-adic character clocks with real-circle `exp(2πihU_n)`; PR441 has an explicit non-factorization counterexample.

The full original-source selected signed Weyl sum remains the necessary π-normality gate; PRs #437–#442 are inherited mathematical dependencies, not an independence certificate.
