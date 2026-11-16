# Fuckedfield / idealhard as instrument-relative boundary obstructions

**2026-11-12 · research continuation of draft PR #606 · parent commit `2206fbc085ffa2986adae83e39300316013b57dd` · Main XXV base `db9fb4b84672050efa79b13377f1e73364598a14`.** New additive operational models. Frozen original four-pole BBP recurrence, literal zero source, provenance contracts, completed Weil and π frontier are untouched. **π normality, R0, Goldbach, completed Weil positivity, RH and any physical ER=EPR interpretation remain OPEN.** No claims of novel priority.

## 0. Recover the conjecture; distinguish three obstructions, not an exhaustive metaphysical dichotomy

The author's tentative labels **fuckedfield** and **idealhard** name two possible failure modes of boundary reconstruction:

- **FF / coupling absent relative to the declared instrument closure:** distinct candidate internal states have identical observable response *for all admissible instruments and their lawful adaptive histories*. What is invisible is an equivalence class, not a declaration that a proposition is false, logically undecidable, or objectively nonexistent. An independent formal proof may still establish a theorem about the same mathematical object.
- **IH / distinction available only through source-affecting coupling:** a separating instrument exists but alters the state/histories being reconstructed, so transporting the response back to the intended unprobed source requires a **specified** map, calibration, undo, counterfactual, or corrected likelihood. This is an operational access/transport burden, not a theorem that all measurements must deposit positive physical energy.
- **QND / protected-observable control:** a separating observation exists which preserves the relevant source *on the declared state alphabet* (or measured eigenobservable), albeit not necessarily every quantum superposition. This refutes an exhaustive FF-or-IH ontology. Other live cases include limited precision, finite computational resources, missing source authentication and model nonidentifiability.

The classification is **relative to a state class, source, filter family, allowed controls, fidelity criterion, and output semantics**. It does not define an absolute order of proof difficulty or a truth probability. In TLICA language, a route/probe absence (φ/μ) and a source-map defect (σ) are distinct; a model can be highly coherent but wrong about the true carrier.

## 1. BI-01 — exact active instrument closure (classical Mealy-machine theorem)

A finite **declared** carrier has state set `S` and admissible probes `P`. Each probe changes the state and emits a record:

`I : S × P → O × S`, `I(s,p)=(o(s,p),T_p(s))`.

A probe word `w=p1...pk` produces both a finite output history and a final state. Define `s ≡_P t` iff **every** finite word has identical output histories from both starts. The same equivalence holds against arbitrary deterministic adaptive choice of the next probe using only the previously observed outputs (proof: equal initial outputs force identical next choices, and induction applies).

Define initially one block and refine by the signatures

`signature_d(s) = ((o(s,p), class_(d−1)(T_p(s))))_(p∈P)`.

The stabilized partition is exactly `≡_P`: this follows by induction because depth-d equality means equality of current output under every first action plus depth-(d−1) equality of successors. For a finite `|S|=N`, every proper refinement increases the number of blocks, so stabilization takes at most N iterations from the trivial initial partition. An independent shortest separating word is found by breadth-first search in the pair-product graph `S×S`: for each action, compare immediate outputs and otherwise advance to both next states. The search is finite and returns a shortest witness if one exists; its first mismatch occurs no later than N² probed transitions. This is classical automata/bisimulation theory, not novel quantum research.

**Exact hostile table:** choose states `s0`, `s1`, `reset`. A passive sensor always emits `null` and leaves the hidden states unchanged. An invasive `interrogate` emits `0` or `1` and maps either source to `reset`. Under passive probes, `s0 ≡ s1`; under the larger instrument closure, they separate in one step but the measured carrier changes. Replacing `interrogate` with a nondisturbing state-label read keeps the source state intact and still separates it. The third case shows that distinguishability does not intrinsically demand alteration for every source class.

This is a **full instrument** equivalence: the update map participates in the definition. Static Cx measurements alone can miss distinctions revealed by active transitions. Conversely a detector whose output is blind to the input and whose update is fixed gives no information no matter how often it is used.

**Execution:** `finite_active_observer.py`; tests include 256 exhaustively enumerated two-state/two-action binary instruments checked against two independent algorithms (partition refinement and pair-product BFS), plus wrong-action, two-step, invisible, invasive and nondemolition cases.

## 2. BI-02 — the no-information-without-disturbance graph theorem (quantum)

Fix a **declared** finite alphabet of normalized pure states `{|ψ_i>}` in the same finite-dimensional Hilbert space. Let the apparatus start in a *fixed* pure blank `|e*>`. A zero-disturbance record-making isometry must take

`V (|ψ_i>⊗|e*>) = |ψ_i>⊗|e_i>`

for every listed i, up to physically irrelevant pure-state phases. Assume the system rays are preserved, not just the ensemble-averaged density matrix. Unitarity/isometry preserves all inner products:

`<ψ_i|ψ_j> = <ψ_i|ψ_j><e_i|e_j>`.

If `<ψ_i|ψ_j> != 0`, the two normalized marker vectors must coincide (up to phase if the system outputs were only preserved as rays). Form the **nonorthogonality graph** with an edge precisely when the two input states overlap nontrivially. By transitivity, any perfectly nondisturbing classical label extracted from a pure apparatus must be **constant on each connected component**.

**Sharp converse (finite alphabet):** different graph components span mutually orthogonal subspaces, because every cross-component pairwise inner product vanishes. Projecting onto the direct sum of those subspaces nondestructively records a component label while preserving every listed state. Thus a label is perfectly recordable with zero disturbance **iff** it is constant on each nonorthogonality component. This is a classical finite-alphabet no-information-without-disturbance structure theorem, presented as SUCC's candidate instrument discriminator, not a novel quantum no-go.

**Adversarial witness:** `|0>=(1,0)`, `|1>=(0,1)`, `|b>=(3/5,4/5)`. Although `|0>` and `|1>` are orthogonal, both overlap with `|b>`, so the graph is connected. There is no perfect probe that assigns **all three** different labels while leaving every listed state unchanged. If the allowed alphabet excludes `|b>`, computational-basis measurement is QND for `|0>` and `|1>`. The answer depends on the carrier state class—not merely whether its algebra is quantum.

**Exact rational certificate:** the Gram residual for an attempted environment marker family is

`R_(ij) = <ψ_i|ψ_j>(1−<e_i|e_j>)`.

Vanishing of all residuals is necessary and sufficient for an isometry on the span of the listed inputs to realize the requested product outputs, after extending to a unitary on the finite composite system. The code computes these residuals over real rational vectors; the proof above applies to complex Hilbert spaces. A zero residual is a *mathematical compatibility certificate* conditional on the chosen tensorization, not experimental source calibration.

**Quantum caveat:** this is stronger and better typed than the idea that every observation pumps energy into its system. A QND measurement can preserve specified eigenstates/eigenobservable while disturbing incompatible superpositions, and may exchange no net energy with the measured subsystem. It is still a nontrivial instrument coupling. Hence the user's Higgs analogy illustrates **indirectly calibrated transduction**, but is not a universal quantum energy law.

## 3. BI-03 — calibrated quantitative overlap debt (not a universal physical energy bound)

Suppose a physical isometry applied to two candidate signals has outputs `|Φ_i>`, each satisfying

`|| |Φ_i> − |ψ_i>⊗|e_i> || ≤ δ` for i=0,1,

where all listed target vectors are normalized and the same blank instrument is used. Expand their inner product and use Cauchy–Schwarz. Writing `s=<ψ_0|ψ_1>` and `t=<e_0|e_1>` gives

`|s| |1−t| ≤ 2δ + δ²`.

**Derivation:** set `Φ_i=ψ_i⊗e_i+r_i`. Isometry gives `<Φ_0|Φ_1>=s`, whereas product target overlap is `s t`. The difference consists of two cross terms, each of norm at most δ, and one residual inner product of magnitude at most δ². Triangle inequality finishes. We use a common error radius; unequal radii yield δ0+δ1+δ0δ1.

This is a **necessary** uniform fidelity/record-overlap constraint. It is **not sufficient** to implement a given operation and makes no statement about a Hamiltonian or energy. In an exact rational witness with `s=3/5`, orthogonal markers `t=0`, any attempt has `2δ+δ²≥3/5`; a claimed δ=1/4 is impossible, whereas δ=3/10 passes this necessary bound but is not thereby constructible.

## 4. BI-04 — explicit CNOT and norm-preserving active transduction controls

With a qubit `|ψ>=(3|0>+4|1>)/5` and pure environmental blank `|0>`, apply `CNOT` with the qubit as control:

`|ψ>|0> → (3|00>+4|11>)/5`.

The reduced system and probe both become `diag(9/25,16/25)`. The probability that the environment records `1` is `16/25`, and the original system ray's survival fidelity is `(3/5)^4+(4/5)^4=337/625`, an exact disturbance of `288/625`. The total bipartite state remains **pure**. In contrast, for basis eigenstates `|0>` and `|1>`, CNOT can write the bit label while leaving the system state unchanged. Neither of these cases establishes an energy cost.

To model transduction independently of quantum measurement, take a **classical real two-coordinate** state `(a,b)` with visible boundary `a` and hidden interior `b`. Apply the rational orthogonal rotation

`R = [[3/5,4/5],[-4/5,3/5]]`.

The new boundary report `a'=(3a+4b)/5` together with the pre-interaction report `a` reconstructs `b=(5a'−3a)/4`. The inverse `R^T` restores the full two-coordinate state, and `a²+b²` is conserved exactly. This is a calibrated reversible **classical** transduction and cannot be identified with direct measurement of an unknown quantum amplitude. It disproves any *formal universal* assertion that a distinguishing intervention must inject strictly positive quadratic energy.

A further quantum no-go remains: if an environmental record has irreversibly discarded the phase of two Bell inputs at the accessible boundary, no **boundary-only** recovery CPTP map can restore both, because their reduced outputs are identical. Recovery requires access to the environment, a protected code, independent records or additional trusted source information. See draft PR #604 twin-rendezvous controls.

## 5. BI-05 — source-selected arithmetic firewall

Retain SUCC's immutable original four-pole source:

`r(n)=4/(8n−7)−2/(8n−4)−1/(8n−3)−1/(8n−2); U_0=0; U_n=16U_(n−1)+r(n)`.

For another initial seed s, `U_n(s)=U_n(0)+16^n s`. Two rational seeds s,t have identical **circle phases** from clock N onward iff `16^N(s−t)` is an integer. Hence the actual zero seed and the wrong seed `s=1/16` are indistinguishable by all later *bare phase* probes starting at N≥1, although their source-anchored histories differ. This is an FF-style **relative observational equivalence**, immediately repaired by the permitted unwrapped zero-origin pin. It does **not** prove that the actual π orbit equidistributes: both source authentication and a new signed all-epoch R0/Haar estimate are needed.

One can freely encode source labels into orthogonal qubits and measure them nondestructively, or encode the same labels into nonorthogonal qubits and invoke BI-02. Neither is a **source-derived** qubit interface. Until SUCC constructs a lawful arithmetic-to-quantum instrument map and validates its output, the quantum information–disturbance theorem supplies no π or RH inequality. A positive general Gram matrix likewise does not identify the signed completed Weil distribution.

## 6. Higgs analogy: the useful part and its boundary

The collider does not use a direct 'create Higgs' button. In proton collisions, quantum interaction channels include gluon fusion via heavy-quark loops, vector-boson fusion and associated production; decay products provide reconstructed evidence. However, **not every channel is a direct quark-field-only interaction**, and uncertainty of a finite physical measurement is not equivalent to formal mathematical undecidability. ATLAS/CMS establish the Higgs through convergent high-significance evidence, whereas a formal mathematical proof establishes a statement relative to axioms and verified inference, without requiring a physical collider experiment for the abstract proposition.

There are real quantum tradeoffs for discriminating **nonorthogonal states** (e.g. Fuchs–Peres 1996), and genuine QND measurements (e.g. trapped-ion many-body Hamiltonian readouts). Those are different instrument contracts, not a universal 'any knowledge costs energy' axiom.

Primary/external references checked during this round:

- Fuchs and Peres, *Quantum-state disturbance versus information gain*, Phys. Rev. A 53, 2038 (1996): https://doi.org/10.1103/PhysRevA.53.2038
- D'Ariano, Perinotti and Tosini, *Information and disturbance in operational probabilistic theories*, Quantum 4, 363 (2020): https://quantum-journal.org/papers/q-2020-11-16-363/
- ATLAS, *Adding more pieces to the Higgs boson puzzle*: https://www.atlas.cern/updates/briefing/adding-more-pieces-higgs-boson-puzzle
- Yang et al., *Quantum non-demolition measurement of a many-body Hamiltonian* (2020): https://www.nature.com/articles/s41467-020-14489-5

## 7. Next verdict-changing probe: source-calibrated coupling, not source-agnostic positive geometry

1. Build the **actual** admissible action/observation category for original zero-seeded BBP and for the completed prime–Γ Weil carrier. Preserve literal source labels, chronology, phases, test-function domains, all prime powers and genuine spectral half-densities.
2. Compute source-map adequacy σ separately from probe rank μ and interaction/contact κ. Find two source-world candidates with identical passive shadows but distinct responses to a *physically/mathematically available* active instrument; prove the required correction from the intervention to the original source state.
3. Use a **held-out** channel to distinguish a truly source-derived response from fitted probes. Include the same-forcing wrong seed `1/16`, coherent seed `−π/16`, periodic nonnormal completions, fake-composite 6, wrong Gamma and pole/contact, and correlated-observer errors. Observe that good finite Gram rank alone is irrelevant to R0/RH.
4. Attempt a source-calibrated quantitative lower bound on the boundary discrimination modulus or a signed all-epoch estimate. Reconstructible at every finite depth without uniform stability is not the required asymptotic theorem.
5. Distinguish true source-preserving QND instruments, source-disturbing interventions with a verified recovery protocol, and impossible boundary-instrument closure under the declared category. Never silently reclassify a missing instrument as a logical no-go.

### Reproducibility / authority

`observational_succ/active_boundary_coupling.py` and `observational_succ/finite_active_observer.py` are exact stdlib implementations. Focused tests: `tests/test_active_boundary_coupling.py`, `tests/test_finite_active_observer.py` (**27 passed on isolated Python 3.13.5 overlay**), including cross-oracle enumeration of **all 256** two-state/two-action binary-output deterministic instruments. The unconditional finite-structure statements are provided with elementary paper proofs. The code is not a quantum hardware simulation, a physical energy budget, an independently reviewed priority claim or a theorem prover.
