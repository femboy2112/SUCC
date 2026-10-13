# EODCS: Evolutionary Obstruction-Driven Categorical Synthesis

**Research checkpoint:** 2026-10-13. **Stack:** PR #44 onto GF PR #43, initial parent 1cb30a3d92420f1197fc1615a68fb4309c0e036d. **Scope:** exact mathematics of finite posets, relations, permutation group actions, finite voltage covers, and rational probability laws, each with explicit **declared-source** assumptions. **NOT:** empirical source authentication, calibration, scholarly mathematical priority, unrestricted category invention, RH/Weil positivity or an unrestricted Lean formalization of EODCS.

The maintainer's original goal is not to pick from a fixed library forever: E should use failed explanations and crossed model contexts to propose better *representation types* while refusing to edit their source evidence.

## Six requests and the moonshot: completed scope

1. **Generalize the alphabet:** implemented finite-poset functors including noninjective maps, pointwise natural transformations, a sufficient order-quotient criterion, Galois adjunctions, permutation-valued connections and minimal covering-space representations.
2. **Counterexample-driven evolution:** exact source probes reject specific model predictions and preserve no-good clauses. Failed bijections enable a functor grammar; nonflat scalar constraints enable a covering-space grammar. Seeded monotone-map genetic mutation/crossover remains independent of the exhaustive certification oracle.
3. **Dependent source probability:** sharp posterior intervals over unknown conditional Frechet couplings, plus explicit conditional second receipts. No arbitrary multiplication of marginals.
4. **Partial/noisy/delayed state-changing sources:** incomplete source tables retain rival models; blind held-back source rows test honest prediction sets; delayed event receipts retain their original epoch. A real state-changing causal transport square is *still open*.
5. **Formal verification:** a self-contained Lean 4.14.0 proof now **passes kernel checking** for monotone composition, adjunction unit/counit, and right-adjoint uniqueness ([push run 38346981020](https://github.com/femboy2112/SUCC/actions/runs/38346981020), pinned commit `bab34a1158054da3130e44b8086f9bd156ae7af5`). The other categorical and covering-space theorems are **not yet kernel-formalized**. Independent brute-force oracles are executable in Python.
6. **Unknown-target invariant:** an independent seeded 8-to-4 chain source (165 admissible monotone maps) fixes a mapping unknown to the genetic proposal generator. Its fibers, right adjoint and sealed suffix prediction set are reconstructed. This is a source-relative finite unknown *value*, not a newly invented general theorem.
7. **Moonshot (bounded):** an obstruction changes the admissible kind of object, not just its coefficients. Poset quotient/adjunction and minimal holonomy covers are certified representation births. The grammar families themselves are programmer-supplied, so completely automatic new-mathematics invention is UNVERIFIED.

## EC1. Functors and law-preserving order transports

A finite poset P is a thin category, with an arrow x→y iff x≤y. A functor F:P→Q is a monotone map. For monotone functors F,G:P→Q, a natural transformation F⇒G exists exactly when F(x)≤G(x) for every x. Necessity follows from components; sufficiency follows because each naturality square has at most one morphism with the prescribed endpoints. This is a classical categorical theorem, now checked using exact finite source types and negative maps.

**Source-obstruction experiment.** P is the chain a<b<c, Q the chain cold<warm. The complete declared paired source reports (a,cold), (b,cold), (c,warm). There is NO bijection due to 3≠2. Instead of forcing one, E expands to finite monotone functors and identifies uniquely

F(a)=F(b)=cold, F(c)=warm.

The source table is not independently authenticated. Total input coverage is checked; a false completeness flag with a missing input is rejected. A source pair demanding nonmonotonicity cannot be rescued by mutating the evidence.

## EC2. An adjunction E did not receive in its grammar input

An adjunction F⊣G is the equivalence, for all x∈P,y∈Q,

F(x)≤y **iff** x≤G(y).

The program exhaustively enumerates all monotone right-adjoint candidates, then checks all ordered pairs; this is independent of the source-map generator. For EC1 it constructs G(cold)=b and G(warm)=c.

**Proof of uniqueness:** for two possible right adjoints G1,G2, reflexivity makes F(G1(y))≤y, which implies G1(y)≤G2(y), and conversely; antisymmetry forces equality. Unit x≤GF(x) and counit FG(y)≤y follow from the same hom-set equivalence. Thin-category triangle identities then hold by uniqueness.

**A sound quotient property:** if F:P→Q is surjective AND each order y≤z in Q has comparable lifts x≤x' with F(x)=y,F(x')=z, every monotone map from P constant on F-fibers factors *uniquely and monotonically* through Q. Surjectivity defines the factor, fiber constancy makes it well-defined, and the comparable lifts prove monotonicity. The two-point discrete-to-two-point-chain surjection is a counterexample to assuming that every surjective monotone map has this property. A top-constant functor that misses the bottom can fail to have a right adjoint. Both negative controls are executable.

## EC3. CEGIS, source exclusions and genuinely failed stochastic proposals

The exact synthesis first attempts isomorphisms. If cardinality prohibits one, it emits an exact obstruction. If observed values eliminate them, it emits the falsifying predictions, including the source input and the actual output. At each query E selects an unqueried symbol that separates its current live proposals maximally (deterministic ties). The accumulated no-good constraints prevent future genetic proposals from contradicting previously queried source outcomes.

An independent genetic sampler evolves finite *chain* functors. Every crossover output must remain monotone; children contradicting source observations are rejected rather than promoted. A bounded exact enumerator acts as a different instrument: it may rescue failed genetic searches but CANNOT rewrite the reported genetic success bit. The finite source class can be conditionally identified with at most n input queries where n is its declared number of input labels. No minimax-optimality or unrestricted computational completeness claim is made.

**Blind source:** a separate seeded source stream selects monotone 8-to-4 chain values (0,0,1,1,2,2,2,2). There are C(11,8)=165 possible maps. With only five training reports (0,0,1,1,2), exactly four admissible suffixes remain: 222, 223, 233, 333. The sealed actual suffix 222 is inside the frozen prediction set; it cannot be inferred uniquely from the five examples. Under full declared coverage the map has adjoint G(0)=x1,G(1)=x3,G(2)=x7,G(3)=x7. Its image misses output 3, so this new adjunction is NOT surjective and is NOT certified as an order quotient. These held-back simulator states are not external empirical validation.

## EC4. Source contradiction -> minimal trivializing holonomy cover

Let Γ be a finite connected graph with additive edge laws b_e∈Z/m. A single-valued scalar q obeys q(v)-q(u)=b_e for each oriented e:u→v iff all closed-walk voltages vanish. Necessity telescopes; sufficiency propagates q along a spanning tree and checks each off-tree edge.

For a tree-propagated h, define each residual r_e=h(u)+b_e-h(v) modulo m. The subgroup H generated by residuals is the image of the holonomy homomorphism ρ:π1(Γ)→Z/m. Put d=gcd(m,r_1,...,r_k) and k=m/d=|H|.

**Minimal covering theorem (classical):** a connected cover trivializing the pulled-back edge connection corresponds to a subgroup K contained in kerρ. Its degree satisfies

[π1:K]≥[π1:kerρ]=|H|.

The cover associated with kerρ achieves equality. This uses standard graph-covering-space classification. The implementation goes further and constructs its vertices (v,s) for s∈Z/k, and for each e the lifted transition (u,s)→(v,s+r_e/d modulo k). On the lifted vertices,

q_tilde(v,s)=h(v)+d*s modulo m

is a globally well-defined scalar satisfying every lifted copy of the ORIGINAL edge law. It generally does not descend to a globally single-valued scalar on Γ. The larger canonical m-sheet cover consists of m/k connected copies of this minimal cover.

**Controls:** the odd parity triangle has a three-edge contradiction on the base but an exact six-vertex, six-edge minimal double cover. One loop of voltage 2 mod 6 gives H={0,2,4}, hence minimal cover degree three, not six. Flat graphs need just one sheet. Parallel-edge mutations, nonzero loops and disconnected graphs are explicitly checked. 200 seeded graphs are compared against a separate exhaustive base-vertex assignment oracle and an independent BFS monodromy oracle.

## EC5. Nontrivial holonomy need not kill all parallel sections

The GF theorem for free Z/2 translations must NOT be generalized to an arbitrary permutation action. Let each directed edge transport a finite fiber X bijectively. Choose a root and spanning tree. Every root value x determines all vertex values by tree transport; it satisfies off-tree edges iff x is fixed by all fundamental-loop permutations. Thus there is a canonical bijection

Sections(Γ,X) ≅ X^(image ρ).

For a one-vertex loop with transposition (01) acting on X={0,1,2}, holonomy is nonidentity yet 2 is fixed: exactly ONE global parallel section survives. Add a second loop (12); the common fixed-point set becomes empty. The algorithm checks both cases, tests noncommuting permutation compositions and compares 180 randomized action graphs to a separately exhaustive vertex assignment oracle.

**Correction:** zero holonomy is necessary for a scalar potential under the *free regular translation* action, not under all group actions. The right general obstruction is the absence of common fixed points. Neither example constructs a real physical gauge field.

## EC6. Source-dependent superposition yields a sharp posterior SET

Let exclusive exhaustive hypotheses H,K have prior π=P(H). Under each hypothesis i, two reported binary yes-events have known marginal likelihoods p_i,q_i but an *unknown* joint coupling t_i=P(A∩B|i). Nonnegativity of the exact 2×2 table forces

max(0,p_i+q_i−1) ≤ t_i ≤ min(p_i,q_i).

For both reports yes, posterior(H)=π t_H/(π t_H+(1−π)t_K), provided the observed event has positive probability. This expression is increasing in t_H and decreasing in t_K. Hence endpoint couplings provide the sharp posterior bounds over the declared class of hypothesis-specific couplings. If all couples make the event impossible, no posterior is returned.

**Exact example:** p_H=q_H=3/4, p_K=q_K=1/4 and π=1/2. Then t_H∈[1/2,3/4] and t_K∈[0,1/4], giving posterior(H)∈[2/3,1]. Multiplying marginals would pick 9/10, which is only one valid coupling. Across 625 exact rational marginal quadruples the computed interval is tested against midpoint/endpoint realizations. This is not a probability that an unobserved mathematical theorem is true.

**Correlation control:** if B is a duplicate of A, the correct conditional source likelihood is P(B=1|A=1,i)=1; the prior 1/2 with first likelihoods 3/4 vs 1/4 then yields posterior 3/4, not 9/10. A legitimately independent conditional second report can produce 9/10.

**Time control:** evidence reports carry source ID, basis, event epoch and arrival epoch. A delayed epoch-zero event reported during epoch one updates epoch zero; without a specified causal transition, epoch-one posterior must not inherit it. Two reports for the same epoch cannot be multiplied without an explicit joint-history kernel. Physical source transitions, calibration and measurement backaction remain open.

## Formalization and evidence ledger

The standalone `formal/EODCS_OrderAdjunction.lean` was compiled and checked by the **Lean 4.14.0 kernel** in [successful CI run 38346981020](https://github.com/femboy2112/SUCC/actions/runs/38346981020) at `bab34a1158054da3130e44b8086f9bd156ae7af5`, with explicit relation hypotheses and no `sorry`/`admit`. The four formal statements are monotone composition, adjunction unit, adjunction counit and uniqueness of right adjoints. **This does not kernel-verify the covering-space or CEGIS correctness theorems**; those retain their pen-and-paper general proofs and finite computational checks. `scripts/eodcs_probe.py` itself makes no dynamic claim to have invoked Lean.

Python reproducibility:
- python -m unittest discover -s tests -p 'test_eodcs_*.py' -v
- python scripts/eodcs_probe.py
- python scripts/verify_provenance.py
- full AGENTS.md mandatory suite and GitHub Actions after final SHA

The experiment preserves immutable historical imports, old defaults, and source IDs. No previous counterexample or genetic miss is deleted.

| Result | Claim status | Key limitations |
|---|---|---|
| Functors, natural transformations, Galois adjunctions | CLASSICAL / finite proof + exact oracle | Lean-kernel checked on composition, unit/counit, right-adjoint uniqueness only |
| Source-complete nonbijective bridge | PROVED LOCAL / declared full table | Not authenticated physical source |
| Witness-guided grammar expansion and genetic proposals | OBSERVED finite algorithm | Incomplete open-world mathematics |
| Sealed blind source suffix | TESTED mathematical holdout | No independent real-world source |
| Minimal holonomy-kernel cover | CLASSICAL general theorem / constructed finite instances | No nonabelian minimal-cover compiler yet |
| General permutation section fixed-point criterion | CLASSICAL general theorem / independent finite oracles | Only invertible finite actions |
| Posterior ambiguity and conditional noise | CLASSICAL sharp rational result | No empirical likelihood calibration |
| Delayed epoch-local evidence | VERIFIED restricted state bookkeeping | No state-changing proof-transport theorem |
| Universal invention of new categories, arbitary experimental instruments | UNVERIFIED | Predefined family of representation constructors |
| RH or completed Weil/Suzuki positivity | UNVERIFIED / NOT CLAIMED | Authentic Euler/Gamma/test-function positivity identification absent |

**Next verdict-changing probes:** extend the pinned Lean formalization to graph-cover minimality and source functor naturality; allow source-changing arrows with actual commutative causal squares and interventions; construct categories not previously in the grammar; use independent stochastic or physical source producers; add learned properly-scored model-misspecification/OTHER options. A truly unknown mathematical invariant must survive fresh generators that were not selected to match its original grammar.

**Established prior art (no novelty claim):** category theory of Galois connections and posets; C. L. Ezell (1979), Observations on the construction of covers using permutation voltage assignments (DOI 10.1016/0012-365X(79)90181-X); Gross & Tucker (1979), Fast Computations in Voltage Graph Theory (DOI 10.1111/j.1749-6632.1979.tb32796.x). Earlier GF and HS dossiers cover categorical ontology bridges, genetic search and source-aware Bayesian reasoning.
