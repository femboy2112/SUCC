# Noncommuting observational proof transport: causal source shadows, path refinement and GF(2) holonomy

**Date:** 2026-10-11. **Branch:** research/noncommuting-source-proof-transport-2026-10-11, based on draft source/backaction PR #20 at 3c350bee700c804b4177d483f2896107a0f1e5d4. **User objective:** continue proof-support transport under genuinely state-changing observations, distinguishing irreversible source-data loss, path-dependent mathematical frames, bounded evidence, and finite/omega debt. **Status:** classical finite machine/fiber results and elementary GF(2) algebra, PROVED LOCAL plus independently checked finite models. Nothing is asserted about academic priority, human observers, physical supertasks, Galois cohomology, gauge curvature in spacetime, novel zeta/Gamma transport or RH.

## 0. The precise object and independent gates

A **deterministic source observation/intervention** on a finite state carrier S is a partial map with explicit executable domain:

\[
a:S\rightharpoonup O_a\times S,\qquad a(s)=(o_a(s),h_a(s)).
\]

An immutable causal report includes action name, observed outcome, carrier epoch, declared source-id and basis-id. It does NOT expose the original hidden state or the post-action hidden state to the decoding observer. The simulator independently retains both for adversarial truth labels and mathematical audits. A publicly visible enabled-action menu is assumed for the future-behavior comparison, not smuggled into earlier action outcomes.

For an admissible finite action word \(\pi=a_1\cdots a_n\), let
\[
F_\pi:S\rightharpoonup O_{a_1}\times\cdots\times O_{a_n},
\qquad H_\pi:S\rightharpoonup S
\]
be respectively its complete *observable* history and post-carrier state. All theorems involving an initial compatible source class \(X\subseteq S\) require each chosen action in the fixed path to be executable for **every** source of X. An action unavailable to some source is not silently replaced by a conveniently narrowed source class. Dynamic feasible menus for distinct states are admitted separately and are publicly observable in the future-bisimulation model.

There are FOUR distinct proposed transports and failure surfaces:

1. **Evidence / source distinguishability:** does the original target \(t:X\to Y\) factor through \(F_\pi\)?
2. **Source semantics:** does a claimed post-carrier predicate \(t':S\to Y\) satisfy \(t=t'\circ H_\pi\) on X?
3. **Future operational behavior:** can the poststates yield different outputs or enabled menus under any admissible future action word?
4. **Mathematical reference frame:** if invertible frame paths have identical endpoints, does a claim depend on the choice of path, measured by explicitly oriented holonomy?

No successful gate implies the others without further hypotheses. In particular a retained report can remain valid as past evidence even when the current physical carrier no longer contains all source distinctions.

## 1. Causal history concatenation and monotonic retained information

For composable action paths \(\pi,\sigma\), where \(\sigma\) is executable on every poststate arising from X,

\[
\boxed{
H_{\pi\sigma}=H_\sigma\circ H_\pi,\qquad
F_{\pi\sigma}(s)=
   \big(F_\pi(s),F_\sigma(H_\pi(s))\big).
}\tag{N1}
\]

Proof: direct induction on action word length. The second expression is an ordered concatenation of epoch-labeled reports, never a commutative set of unordered probe names. It follows immediately that

\[
\ker(F_{\pi\sigma}|_X)\subseteq \ker(F_\pi|_X).\tag{N2}
\]

This is a **full-history** statement. Recorded, original-source evidence is never erased by later deterministic carrier modifications. The new carrier can nevertheless lose *future access*. N2 corrects the unsupported inference that a destructive later probe retracts a previously legitimate historical proof.

For a fixed target \(t\), a decoder \(g\) with \(t=g\circ F_\pi\) exists iff

\[
\boxed{F_\pi(x)=F_\pi(y)\Rightarrow t(x)=t(y)
\quad\forall x,y\in X.}\tag{N3}
\]

This is exact finite fiber factorization; the executable checker constructs g or a concrete conflicting pair. It does not manufacture independent support for the declared t or X.

For two paths \(\pi,\sigma\) on the same source class, **every** claim decodable from \(\sigma\) is also decodable from \(\pi\) precisely when

\[
\boxed{\ker(F_\pi|_X)\subseteq\ker(F_\sigma|_X).}\tag{N4}
\]

Proof: if the inclusion holds, define the quotient decoder \(F_\pi(x)\mapsto F_\sigma(x)\), then compose any claimed \(\sigma\)-decoder. Conversely, if inclusion fails, there are x,y with the same \(\pi\)-report and unequal \(\sigma\)-reports; choose as target the entire \(\sigma\)-report (or a Boolean predicate separating those reports) to refute universal transport. This means information profiles form a **partial order of source partitions**, not a universally adequate scalar 'debt score'.

## 2. Concrete noncommuting destructive carrier and irrecoverable shadows

Set \(S=\{(a,b):a,b\in\{0,1\}\}\). Two source-changing actions are

\[
A(a,b)=(\hbox{observe }a,\ (a,0)),\qquad
B(a,b)=(\hbox{observe }b,\ (0,b)).
\]

Let the original-source goal be \(t(a,b)=a\oplus b\).

**Path A then B:** reported values (a,0), final state (0,0).
**Path B then A:** reported values (b,0), final state (0,0).
For every initial source both paths end in the SAME physical state. However their preserved public evidence differs and their source partitions are incomparable under N4: one learns original a; the other learns original b. Neither history suffices to determine original parity for all four sources. This is a concrete NONCOMMUTING EVIDENCE diagram, despite a confluent final payload.

**Irrecoverable source-shadow theorem:** If \(x,y\in X\) obey

\[
\boxed{
F_\pi(x)=F_\pi(y),\quad H_\pi(x)=H_\pi(y),
\quad t(x)\ne t(y),
}\tag{N5}
\]

then no deterministic **future adaptive instrument policy** whose allowed actions, menus, reports and transitions depend only on the poststate and visible history can ever soundly decide original t on both worlds.

**Proof:** Both worlds enter the same poststate with the same public transcript. Every next policy choice is identical. The enabled-action menus and instrument outputs are functions of the common poststate, giving the same next record and successor state. By induction the two complete future reports remain indistinguishable for all finite continuation lengths; a deterministic decoder of their common transcript cannot equal both unequal original targets. Such a pair is a **decisive impossibility witness for the declared single-carrier protocol**. It is NOT mathematical unprovability when additional independent copies, true source laws or different instruments exist.

- A-first shadow: original 00 versus 01; both report a=0 and collapse to (0,0) but original XOR differs.
- B-first shadow: original 00 versus 10; both report b=0 and collapse to (0,0) but original XOR differs.
- Before ANY observation, a deterministic policy must either stop (which cannot know parity on all sources) or choose A or B. Either first choice creates a shadow. Hence even adaptive future decisions cannot repair the restricted one-carrier protocol.

**Nuance with real mathematical value:** every pair of distinct INITIAL sources has *some* first probe that distinguishes them (A if their a bits differ; otherwise B). Therefore all initial states are pairwise finitely separable in the classic automata sense, but THERE IS NO SINGLE UNIVERSALLY SUCCESSFUL ADAPTIVE EXPERIMENT for original parity with one carrier. Pairwise distinguishability is not equivalent to uniform single-run identification under destructive backaction.

**Independent repairs:** a non-destructive A followed by non-destructive B, or one admissible joint source-preserving A+B probe, can certify original parity. Two genuinely identically prepared source carriers also suffice (previous proof_coherence.py); a fresh independent source cannot simply be *asserted* available. The supplied source IDs and ideal transition tables are declared mathematical assumptions, not cryptographically authenticated evidence or physically verified measurements.

### 2a. Second hostile control: physically NONCOMMUTING, reversible source updates

The destructive A/B experiment has noncommuting **causal observations**, but its two payload update maps happen to commute: either two-step order resets the source payload to zero. To avoid falsely labeling source-payload changes themselves noncommuting, we also constructed a separate genuinely noncommuting pair of invertible physical-state transformations:

\[
\widetilde A(a,b)=
  (\text{observe old }a,\ (a,a\oplus b)),\qquad
\widetilde B(a,b)=
  (\text{observe old }b,\ (a\oplus b,b)).
\]

Both are involutions of the same four-state carrier. Their **state-update maps do not commute**. For source (1,0), A then B ends at (0,1), whereas B then A ends at (1,1). This is an exact source-state difference, not merely different observer-language descriptions.

Nevertheless, if the causal order is REPORTED:
- \(\widetilde A\widetilde B\) has observable outcomes \((a,a\oplus b)\).
- \(\widetilde B\widetilde A\) has observable outcomes \((b,a\oplus b)\).

Each route therefore has a bijection from all four initial sources to its own four ordered reports. **Every** original-source predicate is recoverable with the route recorded, including old a, b and parity. Invertible state change is not necessarily proof destruction.

Suppose instead a faulty packet forwards only the two outcome bits and **forgets the names/order** of the two interventions. Then the same local report can arise from different original sources along the two routes:

\[
\boxed{
\exists (x,\pi)\ne(y,\sigma):
F_\pi(x)=F_\sigma(y),\quad
t(x)\ne t(y).
}\tag{N5a}
\]

A path-blind decoder exists exactly when t is constant on this JOINT route-forgotten observation partition. For t(x)=old a, the same report (1,1) occurs from x=(1,0) on AB and y=(0,1) on BA, and the claim values disagree. Conversely, the original XOR is always the SECOND output under either route, so **original parity survives route forgetting**. This control sharply separates an information-losing compression of otherwise source-faithful evidence from an irreversible physical source shadow: preserving the original path names suffices to repair the former, whereas the latter requires new source access.

The code's causal packet always records the path. Route forgetting is an explicitly MUTATED observer/decoder contract, not secretly attributed to honest full-history observation. The generalized route-blind factorization helper computes a source collision pair or a decoder, with all 16 binary targets independently checked on the four source states. This source-changing control offers an operational interpretation of the separate oriented GL(2,F2) frame calibration in §5 without asserting they are literally the same physical mechanism.

## 3. Source-truth commuting square is separate from information sufficiency

For any original predicate t and post-intervention predicate t', the mathematically necessary and sufficient source-meaning condition is

\[
\boxed{t|_X=t'\circ H_\pi|_X.}\tag{N6}
\]

We supply an explicit counterexample x and poststate whenever this square fails. In the destructive example, reading A preserves the truth of original a if the postpredicate still means the new a; reading B instead sets a=0, so it does not. Both double-path outcomes have postcarrier parity 0, whereas original parity can be 1. Even a perfect probe of the new carrier cannot make the poststate's predicate equal the lost original-source predicate.

Source truth and decodability are INDEPENDENT obligations: an observation may record a valid original source fact even when the poststate predicate differs; a poststate predicate may be true while the observed record fails to determine the original target. A target-transport diagram commutes only with declared source maps and actual checked truth tables.

## 4. Future continuation equivalence and closure of the tool universe

Let R be a binary relation on finite carrier states. For a deterministic instrument class with publicly reported enabled menus, define observational bisimulation:

\[
s\mathrel R t \ \Longrightarrow\
\begin{cases}
\text{enabled}_a(s)=\text{enabled}_a(t),\\
o_a(s)=o_a(t)\quad\text{if enabled},\\
h_a(s)\mathrel R h_a(t)\quad\text{if enabled},
\end{cases}
\quad\forall a.
\]

There is a greatest such relation \(R_\infty\), obtained by starting with all pairs and repeatedly deleting incompatible pairs. On an N-state system, this process stabilizes in finitely many removals. If (s,t) belongs to the greatest relation, no finite permitted word distinguishes them by public menu/outcome. Conversely, if they do not belong, finite-state determinism yields a finite separating word. The code independently obtains the shortest distinguishing word by BFS on ordered state pairs and compares with the greatest fixed point.

**Crucial distinction:** \(R_\infty\) is *future observational equivalence under the declared tool closure*; it is NOT equality of original sources, posteriors, state representations or semantic truth. Also, universal pairwise separators do not automatically form one safe adaptive strategy for a single destructive carrier, as §2 explicitly demonstrates.

Controls exhaust the 256 two-state/two-action machines with two Boolean output and transition functions, plus seeded partial-menu examples. The relation does not include hidden target truth labels as publicly observed signals; doing so would counterfeit observational access to the very fact being investigated.

## 5. Real path dependence: an explicitly oriented GF(2) square

To separate irreversible source loss from *reversible yet nonflat reference-frame transport*, let the original vector space be \(V=\mathbf F_2^2\). A 2x2 **invertible** matrix represents a local coordinate-frame transport. Define

\[
H=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\quad
V_0=\begin{pmatrix}1&0\\1&1\end{pmatrix}.
\]

These elements of GL(2,F_2) do not commute. Use the H map on both horizontal edges and V_0 on both vertical edges of an oriented square. With the convention that rightmost matrices act first:

\[
P_{\mathrm{RU}}=V_0H,\qquad
P_{\mathrm{UR}}=HV_0.
\]

Both start at the southwest node and end at the northeast node. Define the **source-basis transported relative holonomy**

\[
\boxed{W=P_{\mathrm{RU}}^{-1}P_{\mathrm{UR}}.}\tag{N7}
\]

It is a well-defined invertible source-vector transformation because both path maps are source-to-common-endpoint isomorphisms. In this instance W is nontrivial and \(W^3=I\), cycling the three nonzero vectors while fixing zero. This is a valid DISCRETE NONFLAT FRAME CONNECTION; the model does NOT generate a geometric metric, a complex transported phasor, a physical gauge field, or quantum speedup.

For a Boolean source claim \(t:V\to\{0,1\}\) and endpoint-only reading \(y=P_\pi x\) where the path label is **forgotten**, a path-independent decoder exists precisely when

\[
\boxed{t(x)=t(Wx)\quad\forall x\in V.}\tag{N8}
\]

**Proof:** For a common endpoint reading y, the inferred originals are \(P_{\mathrm{RU}}^{-1}y\) and \(P_{\mathrm{UR}}^{-1}y\). The two reported t-values agree for every y iff t is invariant under \(P_{\mathrm{UR}}^{-1}P_{\mathrm{RU}}=W^{-1}\). Invariance under W and W^{-1} are equivalent by bijectivity. Conversely define g(y)=t(P_{\mathrm{RU}}^{-1}y); the invariance makes g valid for either route.

Consequences:
- The first-coordinate source claim t(x_1,x_2)=x_1 is NOT path-blind decodable; exact same-local-output/different-original-claim witnesses exist.
- The claim "source vector equals zero" IS invariant, and hence is recoverable without knowing which path was taken.
- There are EXACTLY FOUR invariant Boolean predicates out of the 16 possible Boolean functions on four source vectors: the two W-orbits are {0} and the three nonzero vectors, so each orbit can be assigned true/false independently.
- With the PATH witness retained, P_RU and P_UR are individually invertible and EVERY one of the 16 predicates can be reconstructed. Thus here there is no physical information destruction; the obstruction is missing orientation/path metadata.
- In the flat control square both path matrices coincide; all 16 predicates are path-blind decodable.

The executable certificate checks the algebraic W-invariance condition INDEPENDENTLY against the source/output fiber grouping criterion. It enumerates all six elements of GL(2,F_2), all 216 three-factor associativity examples, 16 source predicates and 150 deterministic random oriented-square controls. No complex phases or Fourier gauge transport are declared.

This construction is an intentionally modest *discrete parallel-transport analogy* to the oriented link/plaquette holonomies used in classical lattice gauge theory (e.g. the [QCD on the Lattice chapter](https://link.springer.com/chapter/10.1007/978-3-030-38207-0_5)); source-origin, group, orientation and transformation laws are explicitly different from SU(3) and from physics.

## 6. The boundary exposed for Observational SUCC

These two transport obstructions cannot be fixed by the same operation.

1. **Irreversible single-carrier shadow** (N5): even retaining the entire causal history and source identity cannot recover the original lost predicate if every future experiment sees identical poststates. A real new source, a different instrument or an independent true source theorem is needed.
2. **Path-forgotten nonflat frame** (N8): all source information is invertibly preserved in each declared route, but omission of a route/basis witness makes certain claims ambiguous. Restoring correctly sourced path metadata is sufficient, even without additional physical observations.
3. **Partial-order evidence** (N4): two observation policies with the same number of outputs and the same terminal source carrier may support incomparable proof predicates. A scalar debt count is not a complete summary of knowledge.
4. **Genuine source-truth change** (N6): a later claim may refer to a different physical source predicate; an isomorphism of coordinate encodings does not license an original-to-new truth claim without a commuting law.
5. **Zeno moving objective from PR #20:** nonterminal positive certificates arise from ever-renewed support obligations. It is not equivalent to N5 irrecoverable lost original-source data, or N8 reversible lost metadata. A theorem claiming all are one phenomenon would be refuted by our different positive repairs.

## 6a. Finite adaptive proof policy: least fixed point, not a fixed-path guess

The original source-label target remains t(s), where s is the **original** physical carrier state. After actual interventions the observer must distinguish the changing state q from the preserved original-source referent s. A compatible possibility world is therefore a pair (s,q), and the observer's knowledge state is a finite nonempty belief set B of such pairs. The policy sees only the public outcomes and the declared lawful instrument menu, not the original s.

An action a may be chosen only if it is EXECUTABLE at every current q in B. This planner makes a deliberately conservative contract choice: menu variations are not exposed as free additional observations. The separate future-bisimulation routine explicitly DOES make menus visible and is therefore a different instrument model; the two must not be accidentally conflated.

After a result o, the belief updates as
\[
\boxed{ B_{a,o}=\{(s,h_a(q)):(s,q)\in B,\ o_a(q)=o\}. }\tag{N9}
\]

The target t is evaluable from the public history iff all initial-source coordinates s remaining in B have the SAME target value. For a fixed finite carrier and source class, enumerate reachable beliefs under admissible instruments; let

\[
\begin{aligned}
\mathcal W_0&=\{B:\ |\{t(s):(s,q)\in B\}|=1\},\\
\mathcal W_{n+1}&=\mathcal W_n\cup
\{ B:\exists a\ \text{executable on all }B,\
       \forall o\text{ with }B_{a,o}\ne\varnothing,\
       B_{a,o}\in\mathcal W_n\}.
\end{aligned}
\tag{N10}
\]

**Finite adaptive proof-planning theorem:** The initial belief \(B_0=\{(s,s):s\in X\}\) has a uniformly finite successful deterministic adaptive observation policy **iff** it lies in the least fixed point \(\mathcal W_*=\bigcup_n\mathcal W_n\). Its first appearance at rank r is the minimum achievable WORST-CASE number of observations to certify the original target on every compatible initial source.

**Proof:** \(B\in W_0\) can report the unique target directly. Inductively, an admissible a with every report branch in \(W_n\) permits a policy requiring at most n+1 steps. Conversely, take any strategy that terminates with a sound answer within at most n+1 steps for each source in B. Its first action is fixed before the next observation and must be executable in every still-possible state; each possible outcome branch must have a successful remaining policy of at most n steps. By induction B enters \(W_{n+1}\). For a fixed finite source X and a fixed deterministic policy which terminates after finite steps on EACH x∈X, the maximum of the finitely many termination lengths is finite. Thus all such policies have a uniform finite bound, and the fixed point is complete for this finite problem. This last statement fails as a universal principle once infinitely many possible sources and unbounded termination lengths are admitted.

**Mandatory negative control:** Destructive A/B original-parity carrier from §2 is NOT in W_*: the first action necessarily yields a source-shadow class with conflicting old parity and identical poststate, so no further adaptive probes can repair it.

**Positive controls:** Nondestructive A then B decides original parity in two observations; the permitted original-source joint probe decides it in one; a genuine independently proved compatible-source restriction can reduce the depth even further without new measurement. The finite game does not authorize the observer to counterfeit these alternative instruments/source premises.

### Outcome-conditioned policy is stronger than a fixed short sequence

Use a separately calibrated carrier with initial bits (a,b), and three TOTAL instruments:
- Q reports original a then updates the physical carrier invertibly to (a,a XOR b).
- R0 reads the **CURRENT** second bit only when current a=0; otherwise reports 0, without further state update.
- R1 reads the CURRENT second bit only when current a=1; otherwise reports 0, without further state update.

After Q, the current second bit is the original target a XOR b. The receiver uses the actual Q report to choose R0 if a=0 or R1 if a=1. This is a lawful adaptive two-event proof of **original parity**, with the source value never given directly to the policy.

Independently enumerate every one of the nine fixed two-action words over {Q,R0,R1}: NONE yields reports sufficient for original parity on all four source states. Consequently, the two-step adaptive policy has a **strict operational advantage at a stated finite depth**; it is not a computational complexity breakthrough, quantum parallelization, nor evidence of an impossible fixed-length proof in other languages. A three-step unconditional path may recover the same information, as it should.

The executable solver stores original/current possibilities separately, computes all reachable belief classes, iterates N10 to a fixed point, records an explicit action choice and rank for each winning belief, and replays the actual four initial sources as independent simulations. Hostile tests compare against a separately written minimax recursion for all 256 two-state two-action deterministic carriers and seeded multi-state targets, detecting bogus closure, forged menus, data leaks and incorrect minimum worst-case depth.

**Interpretation:** This is the first end-to-end SUCC mechanism that classifies *finite ability to actually complete a proof on a changing carrier* rather than merely identify a target as a mathematical function. It remains a classical finite AND/OR game, not an original new theorem of game theory. The interesting research direction is to transport its winning certificates through nonflat source-indexed frames and calibrated resource constraints, then ask which true arithmetical-source operators meet the interface.

## 7. Prior art, theorem status and next experiment

- **CLASSICAL/PROVED LOCAL**: N1–N8 with stated finite domains, fixed protocol class, source labels and orientation. These are direct elementary category-of-process, deterministic sufficiency/fiber, finite-automata bisimulation and finite group-action statements. New-to-repository organization is not scholarly novelty.
- **TESTED MODEL**: code modules with independent exhaustive and seeded mutation controls, a machine-readable JSON receipt, Python 3.10/3.13 matrix validation when run.
- **UNVERIFIED**: whether any physical or human carrier has the declared tables, source-certified independent preparations, a quantitative resource law, nonflat geometry of real observations, source-derived adelic/real Euler-Gamma compatibility or completed RH Weil positivity.
- **REFUTED**: endpoint equality implies evidence equality; noncommuting path necessarily destroys all source information; a later lower-quality observation erases retained valid history; pairwise separability entails a single successful adaptive destructive experiment; all proof predicates require zero holonomy; scalar debt completely characterizes source observability.

Related established frameworks are **dynamic epistemic logic with fact-changing updates** ([Stanford Encyclopedia of Philosophy, Dynamic Epistemic Logic](https://plato.stanford.edu/entries/dynamic-epistemic/)), **finite Mealy machines and separating sequences** ([Springer, State Matching and Multiple References in Adaptive Active Automata Learning](https://link.springer.com/chapter/10.1007/978-3-031-71162-6_14)), and **discrete link/plaquette holonomy** ([QCD on the Lattice](https://link.springer.com/chapter/10.1007/978-3-030-38207-0_5)). They supply known prior-art context, not independent proof of our particular program's implementation.

**Next verdict-changing probe:** build a source- and basis-indexed *functor of admissible instruments and evidence certificates* with an honest resource/physical feasibility relation. State a rigorous descent/gluing theorem for source-transformed observations that is stable under noncommuting path composition. Identify a genuine *source-attested* nonlinear connection or a mathematically interesting invariant beyond finite Boolean examples; test controls where identical endpoint states, transcripts and support resources diverge under further source modifications. If an RH thread emerges, preserve exact prime/Euler/FUCC data, real Gamma and conductor, declared analytic function space, original-source mutation controls and the no-zero-reading constraint before an outbound handoff.

## Reproducibility

- observational_succ/noncommuting_proof_transport.py — deterministic finite source interventions, audit-versus-public reports, actual causal histories, source-fiber proof factors, exact source-truth square, partition refinement, irreversible shadow, greatest observational bisimulation and BFS separator.
- observational_succ/holonomy_proof_transport.py — oriented GL(2,F2) square, explicit path and source transformations, relative holonomy, complete 16-predicate path-blind versus path-aware certificates, and flat/nonflat controls.
- tests/test_noncommuting_proof_transport.py — all 16 Boolean predicates and all short destructive paths, exact false-evidence source pairs, comprehensive two-state Mealy behavior tests, masked future menus and stale source/frame tags.
- tests/test_holonomy_proof_transport.py — all GL(2,F2) matrices, associative composition, 16 predicates, 150 randomized square connections, path-dependent collision witnesses, provenance and wrong/invertible frame controls.
- scripts/noncommuting_transport_probe.py — machine-readable proof-scope receipt, both mathematical models.
- observational_succ/adaptive_proof_policy.py, tests/test_adaptive_proof_policy.py, scripts/adaptive_proof_policy_probe.py — a finite source/current belief-pair AND/OR policy solver, rank certificates, destructive and noncommuting positive/negative controls; independent minimax tests.
- docs/CLAIM_LEDGER.md — O187 onward, classified theorem scopes and explicit source/physical firewall.
