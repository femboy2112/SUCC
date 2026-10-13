# Contextual Heuristic SUCC: Structural Priors, Lawful Likelihoods, and Target-Relative Experiment Design

**Date:** 2026-10-12/13 (UTC). **Research branch:** `research/contextual-heuristic-inference-2026-10-12`, stacked on categorical-repair PR #41 at `a5462ea4ef655bba7dd67fbc16ec048acfb994d1`. **Maintainer's hypothesis:** observers should acquire a mathematical notion of *getting a vibe*: seeing an incomplete mathematical shape in its environmental context, preferentially exploring analogical hypotheses, revising those preferences from outcomes, and protecting formal proof from probabilistic guesswork.

**Verdict:** finite probabilistic model hypotheses, Bayesian experimental design, quadratic proper scoring, categorical quotient/sufficiency, latent-variable conditioning, hyper-Bayesian learning and likelihood-ratio martingales are classical. The exact, context-/source-tagged integration and hostile SUCC controls are new to this repository. **No academic novelty is established.** Nothing authenticates laboratory observations, makes a prior objective, supplies missing analytic Weil positivity, proves RH, or warrants interpreting subjective probability as a proof of arithmetic truth.

## HS0 — The separate epistemic types (DEFINITION)

A source-relative heuristic record is:

\[
H=(\mathcal M,\mathcal A,\pi,\{K_a\}_{a\in\mathcal A},C,E,\rho).
\]

- `\mathcal M`: explicitly enumerated *candidate models*, each bearing a context, feature signature, description-length budget and target-label **hypothesis**.
- `\mathcal A`: lawful declared experimental generators; `K_a(y|m,h)` are **normalized predictive kernels conditional on public history** `h`, including repeated-noise conditions if necessary.
- `\pi`: prior weights assigned **before** counting the source observations used by that update.
- `C`: interface/context and allowable carrier interventions; `E`: source-tagged, epoch-/basis-checked record of observations; `\rho`: cost/resource model.

Crucially **`HEURISTIC` is a different type from `PROOF`**. A probability of 99.999% is a model-relative betting confidence, NOT a proof that a formal theorem holds in the intended structure. A mathematically valid proof needs independently verified assumptions, domain/semantics, lawful derivation and source correspondence; the observer neither promotes a guessed proof nor treats a simulation-event tag as physical-origin attestation. The model class may be incomplete even when its posterior weights sum to one.

## HS1 — Structural shape produces a PRIOR, not new evidence (PROVED LOCAL/DECLARED HEURISTIC)

For model `m`, structural tags `\sigma(m)`, pre-evidence context tags `\sigma(C)`, and declared encoding cost `L(m)\ge1`, choose:

\[
w_C(m)=2^{|\sigma(m)\cap\sigma(C)|-L(m)},\quad
\pi_C(m)=\frac{w_C(m)}{\sum_{m'}w_C(m')}.
\]

This is only one finite MDL-/Bayesian-inspired proposal. A different admissible code changes the prior, and similar morphology need not imply similar causal laws. **No probability-calibration guarantee follows from the formula.** We use this visible, independently replaceable scoring rule so E's heuristic assumptions can be falsified instead of buried inside a black-box guess. Every weight is `fractions.Fraction`, with no floating probability comparisons.

**Proof obligations:** the scored tags must precede the evidence update; the coding scheme must be documented; the context must match; competing models must belong to the same declared experiment language (or pass an independently checked adapter). Reusing the same measured fact as both a shape prior and a likelihood observation silently double-counts evidence, and is not licensed.

## HS2 — Exact posterior and source-consistency gates (CLASSICAL/PROVED LOCAL)

If a report is a lawful observation `y` from declared action `a`, the posterior is

\[
\pi_{+}(m)=\frac{\pi(m)K_a(y\mid m,h)}{\sum_j\pi(j)K_a(y\mid j,h)}.
\]

Every model kernel is normalized and nonnegative. Reports must carry a unique immutable event ID, fixed source ID, epoch, basis, observer and declared probe/outcome. Replaying an event, using another epoch or an unavailable outcome raises a typed error. If the denominator is zero, the **right repair is to expand/revise the model class**, not to divide by zero or declare a theorem by contradiction from arbitrary observations.

**No-go:** a model assigned prior mass zero cannot recover under ordinary Bayes conditioning, even if it is true. Therefore a broad admissible `OTHER` class or explicit candidate-growth operation is needed for robust real applications. This implementation flags missing support and does not falsely claim an exhaustive hypothesis catalog.

## HS3 — Target-relative heuristic value (CLASSICAL/EXACT PROOF)

Let `T:\mathcal M\to\mathcal Y` be the research question, and write `p(t)` for the current target-marginal posterior. Define the quadratic uncertainty

\[
G(p)=1-\sum_t p(t)^2.
\]

For proposed probe `a` with outcomes `y` and predictive weights `q_y`, its target-specific expected gain is

\[
\boxed{\Delta_a(T)=G(p)-\sum_yq_yG(p(\cdot\mid y))
=\sum_yq_y\,\|p(\cdot\mid y)-p\|_2^2\ge0.}
\]

**Proof:** expand the squared norms, use `\sum_yq_yp(t\mid y)=p(t)`, cancel mixed terms. Equality holds iff each positive-probability outcome leaves the target posterior unchanged. The exact program independently verifies both sides. Rank lawful probes by `\Delta_a(T)/cost(a)` (a specified utility, not a unique rational-choice principle).

**Unexpected gain:** E may rationally IGNORE an observation that sharply identifies which model is present if it leaves the desired *target property* unchanged. Conversely, an extremely weak measurement that distinguishes a load-bearing target deserves attention even if it exposes few other structural details. This is a mathematical version of focusing a research intuition on the *claim*, not on arbitrary internal descriptions.

### HS3a — An exact Bernoulli two-model discrimination formula

For opposite target models `m1,m2`, `p=P(m1)`, Bernoulli yes-likelihoods `u,v`, and `q=pu+(1-p)v\in(0,1)`, direct substitution gives

\[
\boxed{\Delta_a(T)=\frac{2p^2(1-p)^2(u-v)^2}{q(1-q)}.}
\]

Thus the expected evidence value vanishes **quadratically** with the difference in lawful predictions. This directly quantifies why an apparently excellent intuitive hypothesis sometimes has no practical discriminating probe. Checked by 400 exact independent parametrizations against explicit outcome-tree calculation.

## HS4 — Correlated observations: a duplicated event is not a fresh experiment (CLASSICAL/PROVED LOCAL)

Independent likelihood products require source-justified **conditional independence**. Two separate event IDs do not establish independence, and neither does an agent reading the same underlying noisy sensor twice. Define an exact finite latent source `Z` with weights `p(z|m)` and deterministic public probe outcomes `y_a(z)`. For a history `h`, the actual conditional law is

\[
K_a(y\mid m,h)=\frac{\sum_{z:y_a(z)=y,\,z\models h}p(z\mid m)}{\sum_{z:z\models h}p(z\mid m)}.
\]

The source verifier constructs this law from the joint state and compares it with every claimed conditional kernel. **Counterexample:** two reads of the SAME one-bit latent state report the same outcome; after the first `yes`, the next `yes` has probability one under BOTH hypotheses. A naive replay of the first noisy likelihood inflates Bayes odds; the correct conditional updates them by a factor of one. With two genuinely independent noise coordinates, the same second-stage Bernoulli law can remain valid. Both controls have exact source tables.

This protects a generalized E tower against apparent confirmation from correlated model agents trained on the same datum, copied benchmarks, and repeated experiments sharing the same physical latent variable. Source provenance is an essential *mathematical contract*, not a guarantee that the outside world obeys the given table.

## HS5 — Contextual capsule / quotient sufficiency (CLASSICAL/PROVED LOCAL)

Fix a lawful probe menu `A`. Call `m\equiv_A n` when `K_a(\cdot|m)=K_a(\cdot|n)` for **every** `a\in A` (including history-conditional laws if applicable). For every adaptive observation policy using this menu, the likelihood ratio of two equivalent models is identically one at every step. Their posterior odds remain the same as their prior odds.

**Proof:** condition on any common public history. The policy selects the same next action; the two outcome kernels coincide, so their one-step likelihood ratio is one. Induct. A black-box observer may therefore reason on the induced model quotient `\mathcal M/\!\equiv_A`, provided the target claim is constant on each observational equivalence class. If target labels disagree within a class, **the target is observationally dark**, regardless of posterior magnitude or duplicated towers.

This is SUCC's first-order model-capsule principle made Bayesian. New probes, changed sources or hidden interventions may split a class; equivalence is not global without a scope-complete instrument description.

## HS6 — Syntax-cloning destroys naive shape priors; categorical quotient repairs it (CLASSICAL NEGATIVE/NEW-TO-PROJECT REPAIR)

Consider candidates A and B with equal prior descriptions, and an observation that differentiates A and B. Initially the probability of A is `1/2`. Add *a second name for the exact same A law* with the same description. Naive counting changes the aggregate A probability to `2/3`, although no real possibility or evidence was added.

**Repair:** first quotient by equal kernels for the declared menu; give each behavioral class the weight of its highest-scoring representative (minimal available description), then divide its probability among syntactic names. In this explicit rule the total probability of A remains exactly `1/2` regardless of copied presentations. Theorem: duplicating an existing representation without improving its score leaves the entire **behavioral-class distribution** invariant. Proved directly because neither the class set nor any class maximum changes.

**Limit:** the equivalence is relative to a finite admitted probe menu. An additional observation may split copied names if they represent genuinely different future dynamics. Also, there is no semantics-free unique canonical complexity prior; different encodings and model universes change the weights.

## HS7 — Structural intuition can learn which analogies are fruitful (CLASSICAL HIERARCHICAL BAYES)

Instead of fixing a single feature score, let `\Theta` be a finite set of candidate scoring rules `\theta`, and let independently solved past tasks `D=(C_j, m_j^*)` contain source-identified **verified** winning models. Then

\[
P(\theta\mid D)\propto P(\theta)\prod_j\pi_\theta(m_j^*\mid C_j),\quad
P(m\mid C,D)=\sum_\theta P(\theta\mid D)\pi_\theta(m\mid C).
\]

This is exact hyper-Bayesian updating. One independently verified `storage`-type success changes the meta-prior over `storage`-sensitive versus feature-blind rules from `1/2 : 1/2` to `8/13 : 5/13`. The next model prior changes from `13/20` to `8/13*(4/5)+5/13*(1/2)` for a model with that feature. A failure of that analogy instead lowers its weight. A repeated task or a second task sharing the same original source is rejected unless a joint sampling law is declared.

**Scope:** the finite hypermodel is NOT empirical calibration without exchangeability, correctly specified task-generation mechanisms, independently confirmed winners and actual physical source attestation. Success on biased, repeatedly copied or nonrepresentative tasks can still create a terrible prior. Learning the *heuristic's reliability* is part of the intended SUCC observer program, not an axiom.

## HS8 — Exact all-frequency passive alias obstructs naive heuristic certainty (NEW-TO-PROJECT APPLICATION OF CR3)

Use the independently established positive Stieltjes aliases from PR #41: two passive rational responses of **minimal modes 2 versus 3** that coincide exactly at `s=0,1,2,3` and differ at `s=4` by `|\Delta h|=1/283500` (under the predecessor's normalization). Before any new observation, a shape prior favoring shorter description gives `P(two)=2/3`, `P(three)=1/3`.

Even after four **separately declared independent** Bernoulli sensor observations from those four frequencies, posterior odds remain exactly `2:1`, because the two models predict precisely the same outcome laws at those frequencies. For a declared synthetic sensor with

\[
P(\text{yes}|m,s)=\frac{1+2h_m(s)}{2(1+h_m(s))},
\]

the first discriminating frequency `s=4` yields target Gini gain

\[
\boxed{\Delta_{s=4}=\frac{2}{1946711832863}>0.}
\]

It is **strictly positive and exceptionally tiny**; this is why a mathematical difference does not necessarily make a practically useful experiment. A hypothetical *perfect exact* `h(4)` readout would distinguish the two models at one observation, but it is a more powerful instrument that must be separately justified.

The generator and the full 2-versus-3-mode alias are classical positive-real/Stieltjes countermodels, not physical sensor measurements or a completed RH analogue. The demonstration automatically discovers which of the declared frequency probes is informative, rather than hard-coding it by name.

## HS9 — Learning from repeated noise: a Bayesian analogue of the SUCC field trichotomy (CLASSICAL)

For a two-model i.i.d. Bernoulli source, let `P_true(yes)=p>1/2`, `P_false(yes)=1-p`, both with nonzero equal priors.

- **Simple/disjoint predictions:** one perfectly separating authorized deterministic outcome can establish a conditional model-class conclusion after finitely many observations.
- **Ideal-hard/statistical:** both noisy laws have full support, so no finite observation string rules out the false model completely. Yet the posterior converges to the true model almost surely when the conditional sampling law is correct and repeatedly accessible.
- **Observationally dark:** if all available model likelihoods coincide, posterior odds never change, however many observations E receives.

**Quantified statistical proof:** set `B=2\sqrt{p(1-p)}<1`. Under the true model, the wrong-vs-true likelihood ratio `R_n` satisfies `E_true[\sqrt{R_n}]=B^n`. Markov's inequality gives

\[
P_{\mathrm{true}}(P_n(\mathrm{wrong})\ge1/2)\le B^n.
\]

For **even** `n`, the upper bound is the exact rational `\big(4p(1-p)\big)^{n/2}`, implemented without evaluating square roots. Summability and Borel–Cantelli yield almost-sure posterior consistency. This **statistical trichotomy is not equivalent** to the previous deterministic simple/ideal-hard/fucked trichotomy; a posterior approaching one is not proof of a universal mathematical theorem.

## HS10 — Adaptive stopping requires a separate error-control certificate (CLASSICAL)

Let `P_0` be a **specified, source-justified null** for public histories and `P_1` a specified alternative. At each checkpoint, E predictably chooses action `a_n` from previous public outcomes. Let

\[
L_n=\prod_{j\le n}\frac{P_1(Y_j\mid a_j,H_{j-1})}{P_0(Y_j\mid a_j,H_{j-1})}.
\]

If the null's conditional laws are correct and have full support, then

\[
E_0[L_{n+1}\mid H_n]=L_n
\]

so `L_n` is a nonnegative mean-one martingale. **Ville's inequality** gives

\[
\boxed{P_0\left(\sup_{n\ge0}L_n\ge 1/\alpha\right)\le\alpha.}
\]

This is genuine time-uniform *statistical* error control under the specified null, even if E adaptively chooses when to stop. It is not a deductive proof, a posterior, or null correctness authentication. The implementation exhaustively sums exact null probabilities over adaptive binary trees (tested over multiple thresholds and horizons); the infinite-horizon theorem is proved classically, **not** by finite simulation.

## HS11 — Verified law-preserving bridges transport Bayes updates (CLASSICAL FINITE NATURALITY)

Let `F:\mathcal M\to\mathcal M'` be a bijection on candidate models, with matching priors `\pi'(Fm)=\pi(m)` and matching outcome kernels `K'_{F(a)}(y|Fm)=K_a(y|m)` under a certified outcome-coordinate translation. Then Bayes commutes with this translation:

\[
\boxed{F_*\,\mathrm{Bayes}_a(\pi,y)
=\mathrm{Bayes}_{F(a)}(F_*\pi,y).}
\]

**Proof:** substitute the identities in numerator and common denominator. The code checks each generator's full law, all model labels, bijectivity, and transported priors; a false adapter is rejected with a concrete mismatch. A graph Laplacian/RC model may carry this *mathematical* kernel to a heat-model representation; **source IDs remain distinct**, and the electrical observation was not thereby a thermal measurement.

## HS12 — What cannot be inferred, even in the limit (CLASSICAL NO-GO)

1. **Identical likelihoods:** if `m\equiv_A n`, no adaptive strategy using the fixed menu changes their posterior ratio. Model ontology remains underdetermined.
2. **Misspecified model class:** a source producing an outcome impossible under every model makes the candidate catalog inadequate; high posterior in a closed, wrong catalog is not physical truth.
3. **Unjustified priors:** description-length values depend on encoding, available hypotheses and choice of context. A shape match alone is neither an independent source observation nor a causal mechanism.
4. **False independence:** without true conditional likelihoods, posterior updates and Ville-style guarantees may be wrong.
5. **No quantum magic or RH:** the procedure does not construct a source-derived completed Weil form or prove its positivity. It can rank conjectural repair searches; it cannot turn high credence into proof.

## HS13 — Proposed rigorous next leaps

**A. Learn a genuinely calibrated structure prior:** compare held-out independently sourced research problems using proper scoring rules (Brier/log scoring); include a robust `OTHER` hypothesis and causal mechanism of generating tasks. Derive sensitivity/error bounds if the task distribution changes.

**B. Instrument semantics and belief-state dynamics:** connect the current finite exact kernels to original-source/current-carrier belief states, authorized action menus, intervention backaction, error budgets, and actual (not syntactic) source provenance. Prove generalized conditionalization across source-changing lenses and Beck–Chevalley squares.

**C. Bayesian categorical model search:** discover candidate functors/adjunctions by a grammar over model signatures, use prior mass to rank candidates, prove naturality on generators/relations, and expand the grammar on source-derived obstruction witnesses. Compare a fixed abstract bridge with a failed law-preserving adapter and give E independent holdouts.

**D. Repair-aware model growth:** synthesize new hypothesis classes when every predictive kernel assigns zero to a verified observation. Do not silently renormalize the remaining wrong models. Encode minimum observable model complexity and unknown hidden structure separately.

**E. Beyond expected gain:** cost-aware sequential experimental design under model misspecification, robust/minimax alternatives, Bayesian stopping vs e-process control, and correct conditioning on correlated shared sources.

**F. Riemann-zeta stress test:** all priors on candidate Gamma/Weil mechanisms must be based on genuine Euler local factors and source-completed test-function data, not unknown nontrivial zeros. Heuristic search may suggest a polarization; a real proof must independently verify the **full** Weil/Suzuki kernel, domain, and global sign, with mutation controls. None is yet constructed here.

## Verification and prior art

`observational_succ/contextual_heuristics.py` — pre-evidence structural weights, exact Bayesian source-gated posterior, Gini target-relative value, observational model capsules, quotient-based cloning resistance, generator-level bridge naturality and binary value formula.

`observational_succ/heuristic_joint_noise.py` — exact finite shared-latent source conditionalization and independence forgery witness.

`observational_succ/heuristic_evidence_martingales.py` — exact null likelihood-ratio step, adaptive finite-horizon false-alarm audit, and rational statistical limit bounds.

`observational_succ/heuristic_shape_learning.py` — finite verified-task hyperprior learning and duplicated-source refusal.

`observational_succ/heuristic_bridge_discovery.py` — independent two-vs-three positive Stieltjes source, discriminating holdout, and RC/heat analogical kernel translation.

Tests include independent exact 300-case quadratic-risk checks, 400-case closed-form binary information gains, model-source mutations, source-epoch forgery, duplicate event, wrong repeated-noise law, finite random passive aliases, learned analogy failures and many exact adaptive optional stopping trees. Code-level exact checks are finite; proofs of limiting concentration and Ville's inequality use the established mathematical theorems under written assumptions.

Classical references:
- Bayesian active experimental design and model selection: [Scientific Reports (2024)](https://www.nature.com/articles/s41598-024-54329-w), [Foster (2022)](https://ae-foster.github.io/posts/2022/04/14/bed-model-selection.html).
- MDL and Bayesian induction: [Royal Society (2026)](https://doi.org/10.1098/rsta.2024.0584), [Li and Vitányi (1999)](https://arxiv.org/abs/cs/9901014).
- Predictable sequential sampling and time-uniform tests: [JRSSB (2026)](https://academic.oup.com/jrsssb/article/88/4/1366/8493290), classical Ville inequality.
- Conditional sampling and proper scoring: standard Brier score / Bayesian decision theory.
- Source-relative categorical law transport: predecessor [CR/MB](CATEGORICAL_MODEL_BRIDGES_AND_REPAIR_SYNTHESIS.md), earlier [DB](SOURCE_DRIVEN_DYNAMIC_BOUNDARY_REPAIR.md).

**Priority conclusion:** SUCC's mathematical contribution here is an auditable *discovery workflow* in which structural recognition steers experiment/proof selection but cannot silently promote intuition to truth. The theory's source-realization, calibration and general category-synthesis foundations remain open.
