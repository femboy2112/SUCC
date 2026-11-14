# Principia Observatoris — Source-Coupled Recursive Observer and Predictive Fixed Point

**2026-11-14.** Research branch stacked exclusively on [SUCC #627](https://github.com/femboy2112/SUCC/pull/627), at `a459d531050bda54856d01c2c0ec3e4be7ce07cb`. **Draft mathematics**, no main changes. Author's proposal: source dynamics supply the coupling underlying likelihood and probe costs; an observer recursively models its own observations and interventions; retrospective conditioning yields a predictive reference that may be transported toward a lawful future causal boundary.

**Interpretation kept:** The source is not created by observation. A pre-activated carrier already has source-marked distinctions (PI-0 in [#624](https://github.com/femboy2112/SUCC/pull/624)). An observer's changing computation is an observable process. A self-consistent model can provide a useful reference, *provided its source map and prediction instruments are adequately calibrated*. A computational recursion does not imply a unique state fixed point, true source identification, reverse causation or objective access to all histories.

**Status vocabulary:** CLASSICAL/PROVED PAPER means an algebraic theorem under explicit hypotheses (academic novelty not claimed); EXACT FINITE TEST means a run on declared rational tables; CONJECTURED means extra physical adequacy or a mathematical implication not yet proved; UNVERIFIED means a required source probe has not run. Cross-model numerical agreement and shared research provenance are not blind independent validation.

## RFO-01 — Source-first coupling, not stitched likelihood (CLASSICAL / PROVED)

Let `X` be a finite source state set, `A` an **actually permitted** action set and `O_a` finite typed outcome alphabets. The primitive, if a stochastic source is independently supplied, is a joint conditional transition/readout law

\[
J_a(x,x',o)=\Pr(X_{t+1}=x',O_{t+1}=o\mid X_t=x,\operatorname{do}(a)),\quad J_a\ge0,\quad\sum_{x',o}J_a(x,x',o)=1.
\]

This is one source-indexed interaction, with source transition `P_a(x,x')=sum_o J_a(x,x',o)` and conditional emission `L_a(o|x,x')=J_a/P_a` when `P_a>0`. `J=P(x,x') L(o|x')` **iff** for each fixed `x'`, `J(x,x',o)/P(x,x')` is independent of all predecessors `x` for which `P(x,x')>0`. The proof divides the required equality by positive transition masses; conversely use the common ratio as `L`. On unreachable `x'` any normalized `L` works because all factors vanish.

**Smallest hostile construction:** `X={0,1}`, action resets both states to `0` but returns the **pre-reset** source bit. `J(0,0,0)=1`, `J(1,0,1)=1`, all else zero. Both source rows have identical next-state distribution, yet different outcome laws. No likelihood depending *only* on `x'=0` reproduces both. A guessed post-state sensor rewrites the source and loses its past-information channel.

The action cost is a separate calibrated resource primitive. A path-dependent meter `C_a(x,x',o)≥0` and a fixed charge `c_a>0` are permitted, with expected total one-step charge at current belief `b` equal to
\[
c_a+\sum_{x,x',o} b(x)J_a(x,x',o)C_a(x,x',o).
\]
Costs in physical units (e.g. joules) need an **independently authenticated calibration**. Two distinct cost tables can accompany the same `J`; source-transition probabilities do not mathematically force a unique action price. If a *realized meter value is observed* and carries information, it belongs in the observable alphabet `(o,cost_reading)` of the joint kernel, not in an unacknowledged side channel. Resource cost is not automatically entropy production or thermodynamic work.

## RFO-02 — Exact retrospective/current joint Bayesian update (CLASSICAL)

For a single initial source `X_0`, current source `X_t`, and all lawful reports and actions actually delivered, store a normalized joint belief
\[
b_t(u,x)=\Pr(X_0=u,X_t=x\mid H_t).
\]
After action `a` and observed `o`, set
\[
\widetilde b_{t+1}(u,x')=\sum_x b_t(u,x)J_a(x,x',o),\qquad
z_{t+1}=\sum_{u,x'}\widetilde b_{t+1}(u,x').
\]
For `z>0`, `b_{t+1}=\widetilde b/z`; for `z=0` the record is **incoherent with the declared source model** and no posterior is constructed. Base `b_0(u,x)=\mu_0(u) 1_{u=x}`. By conditional probability, induction on the actual action/output transcript proves this equals the full source-conditional posterior on initial and present states. For the full **path** posterior, one must retain paths or adequate history statistics; the `(initial,current)` joint does not reconstruct intermediate visits.

In the reset/read-old countermodel, a uniform initial prior and observed outcome `1` yield
\[
\Pr(X_0=1\mid O=1)=1,\qquad\Pr(X_1=0\mid O=1)=1.
\]
The posterior has *reconstructed a past source fact* while the source has been destructively reset. No physical signal traveled backwards in time; later conditioning changed the observer's beliefs about an earlier state.

**Limits:** No independent source prior / stochastic law means a compatible **set of histories**, not a normalized posterior. A same-source actual observed event different from any modeled positive-likelihood output is a source-map defect, not a license to fabricate posterior mass.

## RFO-03 — Exact belief-memory repair of a missing static stochastic section (PROVED)

[SUCC #626](https://github.com/femboy2112/SUCC/pull/626) proves that the deterministic three-state source `a→b→c→c` with quotient reports `q(a)=u`, `q(b)=q(c)=w` has **no** fixed stochastic equivariant section `K(w)` satisfying `T_*K_u=K_w=T_*K_w`: the first equality forces `K_w=δ_b`, the second `K_w=δ_c`.

Yet with an authenticated start `δ_a`, and a clock/history record, the exact dynamic Bayesian source reconstruction is
\[
b_{t=1}(X_t\mid w,\text{clock})=\delta_b,\qquad b_{t=2}(X_t\mid w,\text{clock})=\delta_c.
\]
Both are valid beliefs conditioned on *different histories*, and are not required to be one time-independent `K(w)`. Thus **exact dynamical posterior inference is compatible with static backward-section nonexistence**. This changes the observer representation (to include a time-labelled history), not the underlying source transition and not the original static theorem.

A fixed current-state identity probe after irreversible merging of two unknown origins need not recover which origin occurred. Hidden history is identified only when some source-faithful evidence retains or separates it. Identity on the source alone is no omniscience theorem.

## RFO-04 — Bayesian finite-horizon lawful policy theorem (CLASSICAL)

For finite actions with actual `J_a`, positive fixed charges `c_a` and optional calibrated nonnegative meters, define the 0–1 posterior Bayes error on a declared **original-source target** `Q:X_0→V` as
\[
R(b)=1-\max_{v\in V}\sum_{u:Q(u)=v}\sum_x b(u,x).
\]
At horizon `h`, the minimum expected sum of action costs plus terminal classification error is
\[
V_0(b)=R(b),\qquad
V_h(b)=\min\left\{R(b),\min_a\left[c_a+\mathbb E_b C_a+\sum_o z_a(o\mid b)V_{h-1}(b_{a,o})\right]\right\}.
\]
Here zero-likelihood outcomes are omitted; all actual action costs are paid before the next report, and `z_a` comes from the full `J`. Backward induction on a finite policy tree proves optimality: the root either stops and incurs `R`, or chooses one of finitely many actions and then optimal policies on each realized outcome. A policy for initial-source target cannot silently replace it by current-source target after a destructive action.

**Exact probes:** uniform two-state prior with read-and-reset sensor cost `1/8` gives policy value `1/8` and complete original-target identification. The **identical source law** with action cost `3/4` gives optimal **stop** and Bayes error `1/2`. A noisy `3/4`-accurate read-only sensor with cost `1/16` beats a perfect but costlier `1/3` instrument at one-step horizon (`5/16` versus `1/3`). Metered versions use `J·C` and change the decision without changing the source likelihood; source-dependent-meter calculations are exact rational.

This is *expected Bayes risk under a supplied prior*, not the worst-case guaranteed source identification problem of SUCC #627. If policy choice is a deterministic function of the observer's existing record, the observer must not multiply in an extra likelihood for observing its own predictable action; if action selection had a hidden source-dependent side channel, that is a different declared joint law. Model self-reference does not create independent evidence out of already known decisions.

## RFO-05 — Uniform filter contraction and a conditional analytic reference (CLASSICAL)

Suppose one fixed action has Markov transition `P` and **valid** post-state likelihood factorization `J_a(x,x',o)=P(x,x')L_o(x')`. Assume for each outcome considered a uniform bound `0<m≤L_o(x')≤M`. Let
\[
\delta(P)=\max_{x,z}\frac12\sum_{x'}|P(x,x')-P(z,x')|,
\qquad r=2\frac{M}{m}\delta(P).
\]
For each realized outcome `o`, its normalized filtering map `F_o(b)=\mathrm{Normalize}((bP)\cdot L_o)` satisfies
\[
\|F_o(b)-F_o(c)\|_{TV}\le r\|b-c\|_{TV}.
\]
**Proof:** Dobrushin contraction gives `TV(bP,cP)≤δ(P)TV(b,c)`. For probability vectors `p,q`, normalize weighted masses by `Z_p,Z_q≥m`. Expanding
`(p_iL_i)/Z_p-(q_iL_i)/Z_q` and applying `|Z_p-Z_q|≤M||p-q||₁` yields the conservative weighted-TV estimate `TV(B_L(p),B_L(q))≤(2M/m)TV(p,q)`. Compose. The two-to-one constant is deliberately conservative and not asserted sharp.

If `r<1`, every **fixed** repeated-outcome map `F_o` is a Banach contraction on the complete finite simplex and has a unique attracting fixed belief `b_o*`. If the same observation sequence and the same fixed action are fed to two starting beliefs, their distance decays at most `r^t` despite arbitrary variation of the observed outcomes. **A variable outcome stream need not make either posterior trajectory converge to a single point.** No contraction is asserted if a belief-dependent policy changes the action between the two comparisons; a discontinuous adaptive policy may destroy it.

For any subsequently declared **same** future lawful action/decision protocol and target report event `A`, data processing gives
\[
|\Pr_b(A)-\Pr_c(A)|\le\|b-c\|_{TV}.
\]
Therefore an explicitly bounded posterior discrepancy supplies a quantitative future-prediction error bound under that *same* protocol, even for events defined on an entire infinite future output stream, when a lawful path-space measure has been constructed. It is **not** a physical passage through a cosmological horizon and cannot authenticate a misspecified transition law.

**Exact two-state model:**
\[
P=\begin{pmatrix}3/5&2/5\\2/5&3/5\end{pmatrix},\qquad
L_0=(2/3,1/3),\quad L_1=(1/3,2/3).
\]
The uniform contraction certificate is `r=4/5`. Let `p=Pr(X_t=0)`. Then
\[
F_0(p)=\frac{4+2p}{7+p},\qquad F_1(p)=\frac{2+p}{8-p}.
\]
The repeated-0 fixed point is exactly
\[
\boxed{p^*_0=(\sqrt{41}-5)/2\simeq0.7015621187.}
\]
Since `F_0'(p)=10/(7+p)^2≤10/49<1`, this also has a direct sharp local/global derivative certificate. Strict positivity permits the classical Perron–Frobenius projective eigenvector interpretation for the outcome-conditioned positive operator. This is a fixed point of **the observer's conditional belief map**, not an objective state of reality.

## RFO-06 — Fixed-point failure even with contracting recursion (EXACT COUNTERMODEL)

For the *same* positive P and likelihoods as RFO-05, alternate outcomes `0,1,0,1,…`. The resulting even-time state-0 probability converges to the unique admissible solution of
\[
F_1(F_0(p))=p\quad\Longleftrightarrow\quad p^2+8p-3=0,
\]
namely
\[
\boxed{p_{even}^*=\sqrt{19}-4\simeq0.3588989435,\quad
p_{odd}^*=1-p_{even}^*.}
\]
The posterior alternates forever between two distinct values, despite exponential forgetting of its initial prior. Thus the statement “self-observation recursively updates ⇒ posterior converges to a fixed point” is **REFUTED as a general implication**. What exists is a stable *periodic orbit* (or, under more general stochastic observation, an invariant distribution over beliefs with extra assumptions).

A simpler source-permutation example has a deterministic swap `T(0)=1,T(1)=0`; the observer's Dirac state alternates without convergence, while the uniform mixture is an invariant distribution. Neither constitutes knowledge of a selected actual source without prior/source attestation.

## RFO-07 — Predictive-span fixed point, exact finite source-model equivalence (PROVED)

A *different*, more structurally useful fixed point exists even when posterior beliefs never settle. Define `M_(a,o)` by `M_(a,o)[x,x']=J_a(x,x',o)`. For a word `w=(a₁,o₁)…(a_k,o_k)`, the column vector
\[
f_w=M_{a_1,o_1}\cdots M_{a_k,o_k}{\bf1},\qquad f_w(x)=\Pr(w\mid X_0=x,\text{fixed action word}),
\]
is the exact future transcript probability from each source state. Set
\[
V_0=\operatorname{span}_{\mathbb Q}\{{\bf1}\},\qquad
V_{k+1}=V_k+\sum_{a,o} M_{a,o}V_k.
\]
With `n=|X|<∞`, this **ascending** sequence stabilizes by stage `n−1`: `V_{n-1}=V_n=V_∞`. Proof: if any stage has no enlargement it is invariant and remains so; otherwise the dimension strictly increases at least once per step, starting at 1 and bounded by n. By induction `V_k=span{f_w: |w|≤k}`. Hence `V_∞` contains exactly the linear span of *all* finite future transcript probability functions.

**Exact behavioral equivalence theorem:** two source states `x,z` are indistinguishable by *every permitted finite future transcript* iff `v(x)=v(z)` for every vector in one basis of `V∞`. This is a finite rank test. It also implies equality under all finite adaptive policies defined from previous public reports, because a policy leaf is a fixed action–outcome word chosen by earlier outputs. A source state may be behaviorally indistinguishable from another despite a distinct actual causal history.

**Cross-model theorem:** given two different source models with identical permitted action labels, output alphabets and nominal action charges, form their **disjoint union** with block diagonal joint kernels. For priors `µ` and `ν`, the two sources predict the same law for every finite future action/outcome word **iff**
\[
\sum_{x\in X_1}\mu(x)v(x)=\sum_{z\in X_2}\nu(z)v(z)
\quad\text{for each basis vector }v\in V_\infty(X_1\sqcup X_2).
\]
This gives a finite, exact operational reference by which an observer can compare a proposed equivalent predictive model. An assumption that cost is an observable requires comparing the **full cost-augmented outcome laws**, not just nominal charges. Predictive equivalence alone gives neither physical identity of latent sources nor agreement on unavailable interventions.

**Two exact controls:** a one-state source emitting a fair bit and a two-state source that swaps its hidden state while also emitting an independent fair bit have identical laws for every finite output word; their disjoint predictive span has dimension 1. Conversely two candidate models with the **same posterior fixed point** `b=(1/2,1/2)` but different fair/biased outcome probabilities are **not** predictively equivalent. Equality of a fixed belief vector is not a source-model equivalence certificate.

**Sharp-depth witness:** on three states `a,b,c`, let `a→c` emit 0, `b→b` emit 0, and `c→c` emit 1. `a` and `b` have identical first output, but the word `(0,1)` occurs from `a` and not from `b`. Predictive rank grows from 1 to 2 at depth 1, then to 3 at depth 2, saturating the `n−1` bound.

This is a known classical finite linear-realization/observability method organized here as the recursive observer's operational fixed-point instrument. **It is not evidence of a final coalgebra or a universal quantum eigenvector.** Source equivalence and physical source authentication remain distinct.

## RFO-08 — Retrospective information is monotone in expectation, not on every observation (CLASSICAL)

For a fixed original source target `Z=P(X_0)` and history filtration `\mathcal H_t` generated by the actual allowed action/observation records, if the action policy uses only that record and known randomness, then
\[
\mathbb E[H(Z\mid\mathcal H_{t+1})\mid\mathcal H_t]
\le H(Z\mid\mathcal H_t)
\]
by concavity of entropy (equivalently conditional mutual information nonnegativity). Here `H(Z|H_t)` denotes the entropy of the *random posterior* conditional on the particular realized transcript. This concerns information about a **fixed original target**; a changing current state may acquire fresh uncertainty from source dynamics. An individual surprising outcome may increase posterior entropy: for prior `(9/10,1/10)` and an outcome with likelihoods `(1/9,1)`, the posterior on that outcome is `(1/2,1/2)`, raising entropy from `H₂(1/10)<1` to 1 bit. The outcome occurs with probability `1/5`, and the complementary outcome pins the initial state `0` with certainty; the expectation still obeys the entropy theorem.

Action selection that is already measurable from the observer's current information is not itself a fresh likelihood witness: conditioning on an action that follows with probability 1 from the known record cannot change its own posterior. If an action reveals an inaccessible internal state to a **different** observer, that second observer has a different evidence sigma-field. Explicitly name the observer/reference frame before transporting this claim.

## RFO-09 — TLICA, personal reflection and source-map boundaries (CONJECTURED interface)

- `κ/contact`: an executed source-labelled probe and its actual report count as a distinct contact record; imagined probes do not.
- `ρ/identity coupling`: an observer's model of its own policy, recorded actions and original/current source coupling requires an explicit data channel and may change with history.
- `φ/toolkit-relative indistinguishability`: the finite predictive-span quotient characterizes *model-relative* future transcript indistinguishability; no scalar Bayesian posterior is automatically TLICA φ.
- `σ/source-map adequacy`: even a mathematically attracting posterior, source-cost optimal policy, or exact predictive span can be false as a model of physical reality.
- `µ/probe availability`: only authenticated lawful instruments enter the Bellman recursion and the predictive closure.

**Reflexive meta-model:** to let the observer model its own learning algorithm, the augmented state must include at least `(source state, belief, observer memory, policy/configuration, source-model parameter)` or a carefully declared quotient. A policy such as “choose action 0 if posterior > 1/2 else action 1” can be discontinuous. Any claim that this full feedback map has an attracting fixed point needs its own compactness, continuity, contraction or other operational hypotheses. A self-consistency equation can have no solution, multiple solutions, or a periodic orbit in a chosen state space. The source-model and action-cost laws cannot be inferred from self-consistency alone.

**Causal boundary:** the legitimate "analytic swing" is **predictive continuation under an authenticated lawful kernel**, controlled by finite exact transcript functions and/or quantitative filter error bounds. It is not temporal foreknowledge, physics beyond an event horizon, or a proof of a physical Big Bang/gravitational entropy. The first barrier is always the source-to-model map.

## RFO-10 — Strictly proper source-model holdout scoring (CLASSICAL)

Given a *predeclared* probabilistic prediction `q` on a finite outcome alphabet, and an **independently authenticated** future outcome `y`, the Brier score is
\[
S(q,y)=\sum_i(q_i-\mathbf1_{i=y})^2.
\]
For actual conditional source outcome law `p`, direct expansion gives the exact proper-scoring identity
\[
\boxed{\mathbb E_{Y\sim p}S(q,Y)-\mathbb E_{Y\sim p}S(p,Y)
=\sum_i(q_i-p_i)^2\ge0,}
\]
with equality precisely at `q=p`. This is a *testable source-to-model discriminator in expectation* under a declared source law. Finite stochastic receipts do not logically certify equality of two unknown entire source laws; they can falsify a strong prediction or provide bounded evidence only with independently specified statistical controls.

**Exact hostile example:** two source models both keep posterior belief `b=(1/2,1/2)` unchanged, yet predict outcome-0 probabilities `1/2` versus `3/4`. If the second outcome law is authenticated as true, the fair forecast pays a strictly positive excess Brier risk of `1/8`. This prevents the observer from mistaking internal self-consistency or an attractive fixed point for truth. The exact standard-library tests verify both scoring identities and invalid unnormalized forecast rejection. A source-generated score becomes informative only on a **fresh holdout**: using a forecast to tune its own source model and then evaluating it on the same data is not independent evidence.


## Evidence, source family and falsification

The executable evidence consists of a standard-library exact `Fraction` module, finite model tests, an independent path-enumeration and unnormalized-policy oracle, and a separate SymPy oracle for the two-state algebraic fixed point and two-cycle. The independent oracle derives trajectory probabilities by enumerating **entire hidden paths**, not by invoking the production update. It independently reproduces budget values from unnormalized raw masses and cross-model predictive indistinguishability from all action/outcome words up to the sharp finite depth. These are separate algorithms on the same **declared synthetic source**, not independent empirical source maps. Numerical root approximations are presentations of exact symbolic roots, not fitted evidence.

**Hostile suite:** guessed `L(o|x')` on a reset/read-old action; zero-likelihood outcome; prior mutation; positive-cost mutation; source-dependent cost-meter hidden observation; destructive reset; history merge; insufficient future toolkit; alternating reports; wrong source with stable fixed posterior; shared fixed posterior but differing next-outcome predictions; incomplete conditional/probe closure; delayed length-two distinguishability. Prior #626 stochastic-section obstruction remains intact.

**Next verdict-changing experiment:** Find an *authenticated* SUCC source where one and the same contact protocol supplies (a) source evolution, (b) joint outcome likelihood, (c) calibrated resource cost, and (d) a real history-sensitive holdout. Then predeclare a prospective transcript whose probability differs between the newly fixed predictive reference model and a matched source-mispecified rival. Treat source-model agreement on fitted histories as training, not a fresh holdout. For additional foundations, independently formalize RFO-07's predictive-span closure and verify the effect of enabled destructive actions on the equivalence quotient.

**Prior/source anchors:** [#619](https://github.com/femboy2112/SUCC/pull/619) predictive action descent and minimal invariant refinements; [#620](https://github.com/femboy2112/SUCC/pull/620) finite observers and timed causal quotients; [#626](https://github.com/femboy2112/SUCC/pull/626) equivariant choice; [#627](https://github.com/femboy2112/SUCC/pull/627) lawful worst-case probe budgets; [#47](https://github.com/femboy2112/SUCC/pull/47) possibility-vs-probability firewall; [SUCC source-relative targets](../../../docs/CARRIER_RELATIVE_TARGETS.md). Literature antecedents: K. Cho & B. Jacobs (2019) *Disintegration and Bayesian Inversion, Both Abstractly and Concretely*; classical POMDP belief-state dynamic programming; Perron–Frobenius positive matrix theorem; finite weighted automata/linear observability. Bibliographic academic-priority verification is a separate research task, not completed here.

**Verdict:** Within the declared finite source class, RFO-01–08 and RFO-10 survive the exact mathematical checks. The attractive universal claim "recursion implies an objective truthful fixed point" is REFUTED by the explicit two-cycle and wrong-model controls. Source adequacy, universal physical observer self-knowledge, computational closure over all possible future world interventions, and any new GR/π/RH theorem remain UNVERIFIED.
