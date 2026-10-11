# Absorbing models, Hard SUCC, constructive information, and finite completion channels

**Date:** 2026-10-10/11. **Status:** originating hypothesis faithfully formalized; classical fixed-point and computability results; new-to-repository exact finite constructions and countermodels; general physical ontology **UNVERIFIED**.

**Originating proposal (maintainer):** The local working model is **absorbing**, not merely the currently favorite candidate. It assimilates all justified local phenomena; ideal SUCC progresses as hard as technically available, with a mathematical \(\omega\)-limit standing in for an infinite path no human can physically traverse. Probe access is initially epistemic in simple spaces and may encounter genuine physical barriers in FuckedSpaces. Incompatibility between a probe and a model motivates model repair (described informally as where excluded middle fails). A proposed completion must be communicable to a second observer via an optimized finite-time channel, at least at the relevant local scale.

This proposal replaces the *preferred-model* assumption in the earlier finite observer-trap note. The old trap theorem remains correct **for observers that select a single preferred model**; it does not establish trapping of the maximally absorbing observer proposed here. The present file deliberately uses the *full compatible source fiber* and strong local closure. The old countermodel survives as a regression/control for insufficient semantic uptake, not as an axiomatic description of every observer.

**Implementation:** observational_succ/absorbing_frames.py and constructive_frontier.py; tests/test_absorbing_frames.py and test_constructive_frontier.py. **Source files from FuckingRH remain unchanged.**

## 1. The absorbing frame as a mathematical object

Fix a declared source class \(X\), actual source \(x_*\in X\), an interpreted family of probes \(\{p:X\to Y_p\}_{p\in P}\), a sound rule system \(R\), and a shared target/report \(T:X\to Z\).

An observer frame must separate:

\[
F_n=(H_n,K_n,\mathrm{Th}_P(K_n),C_n,E_n,\Phi_n).
\]

- \(H_n\): immutable, *actualized* causally ordered observations \((p,p(x_*))\), not hypothetical outcomes or predictions.
- \(K_n=\{x\in X:x\text{ matches }H_n\}\): the full compatible source class. No arbitrary favorite model is promoted to truth.
- \(\mathrm{Th}_P(K_n)=\{(p,y):\forall x\in K_n,\ p(x)=y\}\): every probe prediction shared by **all** compatible candidates, tagged as prediction rather than physical observation.
- \(C_n=\operatorname{Cl}_{R}(H_n,\mathrm{Th}_P(K_n))\): the least sound inference closure of all premises at this frame.
- \(E_n\): probe descriptions discovered from \(C_n\) (epistemic feasibility).
- \(\Phi_n\): actually executable probes in the carrier and its resource context (physical feasibility).

The **absorbing model** is the canonical knowledge object \(M_n=(K_n,\mathrm{Th}_P(K_n),C_n)\), not one selected element of \(K_n\). A fixed point of the semantic inference operator is not yet a proof that \(K_n\) is a singleton or that its target values have become constant.

**Axiom firewall:** Rules \(R\) are declared and must be sound relative to their intended interpretation. The current finite program validates their syntax and checks causal outcomes against its *declared* source table; it does **not** infer the truth of arbitrary real-world semantic or physical rules. If \(K_n=\emptyset\), the model class, prior premises or observation provenance must be investigated. Classical explosion is not a valid repair strategy.

The maximal available probe set is \(P_n^{\mathrm{live}}=E_n\cap\Phi_n\). An ideal local successor evaluates *all* as-yet-unmeasured live probes and instantly computes the new absorbing closure. Hard SUCC iterates this update (mathematically, with a declared limit operation where legitimate).

### Monotone source-faithful invariant

If observations are genuine and \(x_*\in X\), then \(x_*\in K_{n+1}\subseteq K_n\). Proof: append actual equations; each one holds for \(x_*\), so the compatible fiber shrinks but never excludes it.

If \(K_{n+1}\subseteq K_n\), then \(\mathrm{Th}_P(K_n)\subseteq\mathrm{Th}_P(K_{n+1})\): universally agreed probe predictions can only accumulate. This monotonicity depends on retaining a valid source class, genuine evidence and a fixed probe semantics; revision of *assumptions* is separately typed and may be nonmonotone.

## 2. Finite closure, Hard SUCC and the legitimate infinite limit

For a finite Horn-rule vocabulary, use the monotone operator

\[
U_H(S)=S\cup H\cup\{b:(a_1\wedge\cdots\wedge a_k\Rightarrow b)\in R,\
a_i\in S\text{ for all }i\}.
\]

Starting at \(\varnothing\), iterate \(S_{n+1}=U_H(S_n)\). Because there are only finitely many named atoms, every strict update adds a new atom and the least fixed point is attained after finitely many steps. The executable program does this exactly: it returns the resulting saturated atom set and finite derivation rounds, never pretending a loop executed infinitely many frames.

More generally, if \(U\) is \(\omega\)-continuous on a pointed \(\omega\)-complete partial order, Kleene's fixed-point theorem yields:

\[
\boxed{\ \mu U=\bigvee_{n<\omega}U^n(\bot).\ }
\]

This mathematically **realizes the closure at a limit** without asserting a human observer has walked infinitely many stages. For finitary positive Horn rules over an infinite vocabulary, \(\omega\)-continuity follows because any rule has *finitely many premises*: when those premises occur somewhere in an increasing union, all occur by some finite common stage. This is the strongest rigorous reading of the user's "hard SUCC realizes an infinite path as a limit."

**But monotonicity alone is not enough.** On \(\mathcal P(\mathbb N\cup\{\star\})\) define

\[
U(S)= S\cup\{0\}\cup\{n+1:n\in S\cap\mathbb N\}
  \cup\begin{cases}\{\star\},&\mathbb N\subseteq S,\\
                   \varnothing,&\text{otherwise}.\end{cases}
\]

Every finite iterate is \(U^n(\emptyset)=\{0,\dots,n-1\}\). At the ideal limit \(S_\omega=\mathbb N\), the rule requiring **all natural numbers** is newly enabled: \(U(S_\omega)=\mathbb N\cup\{\star\}\). Hence \(U(S_\omega)\ne S_\omega\). The map is monotone but not \(\omega\)-continuous, and the fixed point needs **\(\omega+1\)**.

This explicitly answers a crucial research boundary: **Hard SUCC may take a legitimate limit, but cannot automatically declare that limit saturated unless a continuity/fixed-point theorem supplies the certificate.** The infinitary rule producing \(\star\) is a *separately declared axiom*, not a finite observational inference or a new physical capability. The code's \`SymbolicOmegaStage\` only represents the mathematical assertion; it never executes infinity.

**Prior work:** Cousot & Cousot, *Constructive Versions of Tarski's Fixed Point Theorems*, Pacific J. Math. 82 (1979), 43–57, https://cs.nyu.edu/~pcousot/COUSOTpapers/Tarski-79.shtml . The fixed-point result and transfinite qualifications are classical, not original physical results.

## 3. Two independent probe obstructions

The author's proposed epistemic-to-physical transition should be represented **as two separately testable predicates**, not as a mandatory metaphysical phase transition:

\[
p\in E_n\quad\text{(the observer knows how to formulate the probe)},\qquad
p\in\Phi(x_*,r_n)\quad\text{(the carrier/resources permit it)}.
\]

A missing \(p\) from \(E_n\) is an **epistemic pathway gap**. A known \(p\in E_n\) with \(p\notin\Phi\) is a **physical access constraint** under the declared device model. Both may coexist; FuckedSpace cannot be equated to "necessarily physically obstructed" without a physical theory and evidence. If feasibility depends on \(x_*\), the act of trying and failing to execute \(p\) might itself convey information and must be modeled as an observation; the finite implementation uses a single public source-independent feasibility list.

**Positive experiment (no contradictions):** sources \(A,B\); initial accessible probe coarse gives the same outcome for both. A sound declared rule

\[
\mathrm{observed}(\mathrm{coarse}=\mathrm{same})
\ \Longrightarrow\ \mathrm{can}(\mathrm{fine})
\]

makes the fine probe epistemically available. The coarse evidence does not eliminate either candidate and contradicts nothing. Yet the absorbing model **generates a new experiment**. If physically feasible, the second successor performs fine and distinguishes A from B. If fine is physically blocked, the observer knows *which experiment would matter* but remains unable to execute it.

**Consequence:** model/probe growth does not require a contradiction. Contradictory evidence may demand revision; positive or previously unexploited consistent evidence can also enlarge the probe language.

## 4. Correct logical treatment of the law of excluded middle

There are three distinct claims that must not be conflated:

1. **Classical truth:** \(P\vee\neg P\) is a classical tautology regardless of whether the observer knows which side. Discovering that a working model makes a false prediction refutes a premise/model class, **not classical LEM**.
2. **Constructive justification:** intuitionistic logic does not prove \(P\vee\neg P\) in general. A Kripke root may force neither \(P\) nor \(\neg P\), hence not their disjunction. The test model has a root with two extensions: one forces \(P\), the other (as a terminal leaf) forces \(\neg P\). Both leaves force \(P\vee\neg P\), but the root does not.
3. **Bad local dichotomy:** a model that only admits two phenomenological categories can receive evidence incompatible with both. This signals a **defective classification or inconsistent premises**, not a counterexample to classical LEM.

In the Kripke model the root not forcing \(P\vee\neg P\) also does **not** mean it forces \(\neg(P\vee\neg P)\). In fact intuitionistic logic proves \(\neg\neg(P\vee\neg P)\). The program tests the distinction.

The strongest charitable version of the initiating LEM idea is: *an absorbing observer may not be able to constructively inhabit either branch of a model-local dichotomy until new probe capabilities appear*. That is a meaningful constructive knowledge frontier. It does **not** license translating empirical model error into a new logical law.

**Reference:** Stanford Encyclopedia of Philosophy, *Intuitionistic Logic*, https://plato.stanford.edu/entries/logic-intuitionistic/ . This is standard Kripke semantics, not an original LEM refutation.

## 5. Completion as finite, inter-observer transmission

Let \(T:X\to Z\) be a precisely declared report (full source, selected invariant, theorem, valid action, or the **entire observation-closed theory**). Suppose observers share an interpreter/protocol \(I\), agreed background source models, and a finite-alphabet channel \(\Sigma^*\).

A **finite report** for a particular completed source must have a finite message \(m\in\Sigma^*\) with an effective decoder \(D\) satisfying

\[
D(I,m)=T(x_*)\quad\text{under the declared shared semantics}.
\]

If the receiver knows only a genuine finite observation history \(H\) and shared \(I\), then a report \(T\) is **identified** exactly when

\[
\boxed{|T(K_H)|=1.}
\]

This is **necessary**: if \(x,y\in K_H\) have distinct \(T\)-values, they supply identical evidence and a history-only decoder must return the same thing for both, hence must err on at least one. It is **sufficient for a finite target report** if the common \(T\)-value has a finite encodable name, the observations themselves have finite encodings, the receiver shares the source semantics and computation rule, and the measurement provenance is trusted. It is NOT sufficient for a general exact global model when the target has uncountably many non-finitely-encodable values.

### Finite bit channel no-go

The set \(\Sigma^*\) of all finite strings over a finite alphabet is countable. An uncountable set of distinguishable exact targets cannot inject into it. In particular, even **constant functions** \(f_a(x)=a\) for arbitrary \(a\in\mathbb R\) are degree-zero polynomials, perfectly identified by one infinite-precision real-valued observation, yet cannot all be transmitted exactly in finite binary strings.

So under this channel assumption:

\[
\boxed{\text{finite mathematical identification}\not\Rightarrow
\text{exact finite digital transmissibility}.}
\]

This is a theorem of cardinal arithmetic; it is **not** a claim about unconstrained infinite-precision analog communication. Even if a particular analytic object has a finite formula (e.g. \(e^x\)), an observer may lack finite evidence sufficient to certify that formula is the true source.

Conversely, the infinite set \(\mathbb N\) can be communicated by the finite rule "0 is in the set and successor preserves membership", **provided the receiver already knows the standard intended natural-number semantics and accepts a mathematical proof of the relevant closure**. A program describing an infinite mathematical object is not the physical execution of an infinite enumeration.

### Optimized channels have at least two incompatible objectives

The finite executable model now supports:

- **Source/history-faithful full frame:** send the actual outcome evidence and reconstruct the same absorbing closure, including a reproducible *lawful access path*. A measurement cannot justify the existence of the probe by retroactively citing that same measurement as the probe's unlocking premise.
- **Target-sufficient minimal witness:** find the smallest *number of observed probes* that guarantees a selected target value against all compatible sources, using exact exhaustive finite subset search. This can omit observations necessary to reconstruct causal provenance, so its decoder explicitly advertises **target-only; no proof of access**.

"Smallest number of observations" is **not necessarily** "fewest transmitted bits". An actual channel-optimization theorem must specify what must be preserved (target, source, historical provenance, a proof certificate), a coding language, side information, physical bandwidth, allowed error and the cost objective.

**Authentication boundary:** In the finite example the sender's reported outcomes are trusted *by assumption*. The decoder checks consistency against the source table and replayable endogenous access—but an adversary may fabricate a transcript compatible with some other source. No authentication of a real physical observer is claimed.

## 6. A productive self-reference counterexample: causal bootstrap

Suppose a purported observation is "fine returned B", and the only rule unlocking the fine probe is

\[
\mathrm{observed}(\mathrm{fine}=\mathrm{B})
\ \Longrightarrow\ \mathrm{can}(\mathrm{fine}).
\]

If the receiver simply takes the final dataset and computes its Horn closure, the result appears saturated: the outcome implies the probe is available. This would falsely **bootstrap its own causal legitimacy**.

The implementation therefore requires a second certificate: there must be an actual source-compatible endogenous sequence from the empty frame that *could have acquired the measurements with the declared probes and rules*. It explicitly rejects the circular example. Logical consistency of a final explanation **does not** by itself demonstrate causal constructibility of that explanation.

This is an instructive distinction between **coherent completion** and **lawfully obtained completion**; analogous circularity warnings apply in proof certificates and self-referential logical systems, though this toy observation is not Gödel's theorem.

## 7. Experiments, controls and the claim ledger

| Claim / rival | Control or falsifier | Result and scope |
| --- | --- | --- |
| New probes need contradictory observations | Same coarse result on A/B unlocks fine | **Refuted as necessity** in exact finite model |
| Absorption is a preferred model | Retain full \(K=\{A,B\}\) and shared predictions, no arbitrary favorite | **Implementation decision / typed model** |
| Hard SUCC always ends at its first \(\omega\)-limit | Monotone non-\(\omega\)-continuous operator enables \(\star\) at \(\omega+1\) | **Refuted**, proved mathematical counterexample |
| Finite Horn absorption is a genuine least closure | Idempotence, order monotonicity, derived facts and bounded rounds | **Proved local**, exact implementation |
| Model permits every conceivable probe | Epistemic fine known but physically blocked | **Refuted as universal assumption** in typed control |
| Contradictions disprove classical LEM | Classical Boolean truth table and proper Kripke semantics | **Refuted / classical** |
| Constructive \(P\vee\neg P\) can remain unforced | Kripke root with P extension and not-P extension | **Classical logic-model theorem + finite test** |
| Finite identification implies finite digital exact transmission | Arbitrary real constants / countability of finite strings | **Classical counterexample** |
| All reported evidence is legally acquired just because a final explanation is internally closed | Observation-unlocks-itself cycle | **Refuted by source-faithful replay control** |
| Full causal history and minimal target witness carry identical certification authority | Fine-only target witness versus coarse→fine access record | **Refuted in exact finite model** |
| Arbitrary infinitely completed mathematical knowledge transfers in finite physical time | Missing effective interpreter, code, physical throughput, proof authority | **UNVERIFIED** |

Source code checks never purport to enumerate actual \(\omega\)-steps. The all-order statements above carry explicit proofs or classical references. Proof-theoretic claims remain separated from numerical success, and neither RH nor a universal theory of human cognition follows.

## 8. Six next verdict-changing research questions

1. **What exactly is the absorbing codomain?** A canonical set of compatible sources and their invariant reports, a dependent type of all justified proofs, or a maximal physical representation? Does its closure include all definable probes or only resource-bounded, effectively constructible ones? A maximal semantic closure can be noncomputable.
2. **Does the ideal limit have a finite certificate?** For which \(\omega\)-continuous and non-\(\omega\)-continuous domains can a finite second observer verify that the transmitted finite rule denotes the claimed limit? Separate finite *definition*, finite *proof* of uniqueness/existence, and effective approximation.
3. **Where is the epistemic/physical seam?** Does the permitted physical probe set depend on the actual source? Is an unavailable probe's failure itself informative? Can we prove a noncircular transition theorem from model-generated access to physically constrained measurements, rather than assuming every FuckedSpace undergoes it?
4. **What notion of completion is required?** Exact full source, shared theory of all accessible observations, target-relative invariant, or ability to construct the same future probe paths? These have different finite coding and minimal witness requirements.
5. **What is the optimized inter-observer channel?** Bit-minimal, time-minimal, proof-minimal, provenance-complete, robust under noise, or bounded-error? Which context/decoder may be assumed shared? A short program is useless if the receiving observer cannot check its commitment.
6. **How do we import intuitionistic logic without misclassifying physical contradiction?** Design a typed forcing/proof-state semantics distinguishing "not yet forced", "forced negation", "theory inconsistent" and "probe physically impossible". Seek a predictive distinction that cannot be simulated equally well by a simpler classical partial-information model.

**Verdict:** the absorbing-model correction eliminates an unearned preferred-hypothesis assumption. A fully specified finite closure can generate previously unavailable probes without contradictory observations, and can be transmitted exactly under a shared protocol when its target and causal evidence are finitely expressible. The existence of a mathematically complete transfinite closure, its physical feasibility, and its finite transmissibility are three independent constraints. The core physical and categorical generalization remains **UNVERIFIED**.
