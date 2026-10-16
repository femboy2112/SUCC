# SUCC-λ × MATRYOSHKA × E consensus: lawful finite joint discrimination

**Research checkpoint:** October 16, 2026.  **Parent:** `research/succ-lambda-observation-calculus-2026-10-16@f4f3d83f4cd38722a49ff9605b3667db0816bfad` (draft PR #139). **Destination:** `research/e-ladder-consensus-lambda-2026-10-16` (isolated child draft). **Status:** classical elementary finite theorems + new-to-project source-indexed software integration; models/test witnesses only; academic priority unverified. **RH PROVED: NO.**

## 0. What the maintainer proposed (steelman)

Combine the existing **E** substrate/finite observer, **E successor ladders**, nested miniature automata, and observational spheres with the new typed SUCC lambda calculus. Let multiple Es and observers share a mathematical frame, perform *different lawful* probes, exchange knowledge, and detect facts unavailable to any one finite view. The objective is **source-preserving consensus that improves discrimination**, potentially eventually furnishing a finite detector for globally forced arithmetic resonance. The proposal does NOT license majority voting as proof, manufacture missing sensors, infer physical authentication from a model identifier, or merge Hilbert covariance with the original signed Weil form.

The named existing constructions are more precise than an invented generic E:

- `observational_succ/knowledge_ladder.py` and `research/2026-10-10/KNOWLEDGE_AIDED_SUCC_LADDER.md`: source-indexed testimony, physical versus semantic placement, strict relay versus snapshot equivalence and cross-enabled finite ladders.
- `observational_succ/miniature_carrier.py`, `miniature_stochastic.py` and `research/2026-10-13/MATRYOSHKA_MINIATURE_SUCC_CARRIERS.md`: certified invariant and quotient miniatures; nested parent action macros, future observational minimization, noninterfering product gluing, no free sensor.
- `observational_succ/noncommuting_proof_transport.py`, `adaptive_proof_policy.py`, `operational_yoneda_descent.py`: changing current state versus original source, Mealy words, public outcomes, finite winning belief policies and bisimulation. These are essential when actions can change the common source.
- `observational_succ/prime_categorical_sphere.py`: a *finite decorated double-cone homological toy sphere*, not proof that arithmetic itself is an S².
- `observational_succ/wild_embedding_succ.py` and `research/2026-10-14/ALEXANDER_WILD_SOURCE_GLUING.md`: the *intrinsic versus ambient* sphere obstruction; nontrivial perfect exterior group with abelian shadows zero, sharp high-depth nilpotent stage detectors.
- `observational_succ/interobserver_channels.py`: existing exact chromatic/minimum-zero-error receiver-side-information theorem (Witsenhausen); communication compression is distinct from new source information.
- `observational_succ/source_lambda.py`: de Bruijn simply typed lambda terms; source/epoch/basis passports; `Gamma |- term : type ! finite-read-set` (this file does not change its semantics).

### Two radically different meanings of “sphere”

**E accessibility sphere** `B_E(r)` in *this* extension is the finite set of E control states reachable by an action word of length at most `r`. It records feasible modeled **potential** program menus and shortest words. It is not a Euclidean ball, physical field, or S². **Source/topological sphere** in WILD-SUCC is an embedded topological object whose complement can carry nonabelian information missed by intrinsic homology. We use that established construction as a hostile observational example and **do not identify the two spheres**.

## 1. Formal objects and evaluation boundary

A world is `W=(s,X,T)` where `s=(source_id,epoch,basis)` is a declared common source passport, `X` is a *finite, explicit* source-candidate set, and `T:X->Labels` is an original-source target. A candidate includes an integer label so source_lambda can predict modular outputs, but *two different source candidates may have exactly the same integer label and different targets*. This deliberately prevents equating arithmetic address with hidden state identity.

A finite E device `D=(name,s,Q,q0,A,delta,M,P)` has a finite internal control carrier `Q`, an initial prepared state `q0`, partial deterministic control transitions `delta`, a set of named ports `P`, and each state's admitted port menu `M(q)`. Each lambda port is a closed **ground** SUCC-λ term. Its static `may_read` set propagates latent closure effects. A MATRYOSHKA mini port is admitted only when the actual `compile_factor` validates every parent state/action/report square, and its public output factors through the **declared parent public report**. The mini's hidden decoder state is **not** a newly measured observable. A `certify_dual_ports` call invokes the existing source-product/noninterference checker; separately compiled factors alone do not suffice.

An E frame stores one finite action word (the *declared model's* realized control history). A lambda record replays a supplied `Atlas` that already contains the actual claimed modular rows; absent rows are an `AccessGap`. A mini record replays a supplied parent public report and its justified translation. A source passport checks identity, epoch, and basis. The received evidence retains source E attribution; a relay is testimony, not a recipient-local measurement. Runtime replays evidence and refuses forged values, provenance and paths.

**Critical frozen-source hypothesis:** The static portfolio and consensus theorems suppose the original tested source does not change during the finite control/program observations. If an intervention changes the carrier, the proper space is a belief over `(original_source,current_carrier)` with actual ordered action/outcome kernels (already implemented separately by `adaptive_proof_policy`). Declared `EDevice.non_destructive_source=True` is a hypothesis, NOT empirical evidence or a proof of hardware noninterference. Destructive devices are rejected here.

The observational signature of a ground lambda program comes from the interpreter's typed output, with a source-typed modular report represented by `(passport,modulus,residue)` and not by its accidental lineage. A child's output is its translated public parent reading. The model evaluates every candidate to form a full **finite** observation table. No such evaluation constructs an all-integer, all-adelic, or all-Suzuki oracle.

## 2. ECλ-01: source-target consensus is exactly a common-refinement theorem

Given (modeled lawful) observable maps `o_i:X->Y_i` and a target `T:X->Z`, write

`ker(o)={(x,y):o(x)=o(y)}` and `K_y=intersection_i o_i^{-1}(y_i)`.

**Theorem [ELEMENTARY/PAPER, EXACT FINITE TESTS].** The target is determined by the whole observer tuple for **all x in X** iff

`intersection_i ker(o_i) subset ker(T)`.

*Proof.* If two sources have the same joint report, target factorization through the joint report exists exactly when they have the same target. Define the decoder on each attained fiber using that common target. Conversely any decoder forces equality for source pairs with identical joint observations. Unattained report tuples are **not** assigned ghost sources or target values. QED.

An actual report tuple has compatible set `K_y`. Outcomes have separate scopes:

- `SOURCE_IDENTIFIED_IN_DECLARED_MODEL`: one remaining model state.
- `TARGET_CERTIFIED_IN_DECLARED_MODEL`: several remaining states, but one target value.
- `TARGET_UNRESOLVED`: at least two different target labels survive.
- `NO_GLOBAL_SOURCE_IN_DECLARED_MODEL`: empty model fiber; a minimal inconsistent event subset is computed by exact enumeration. This is a **model inconsistency**, not a theorem that no physical/global source exists.

Adding a genuine source-coherent observation only shrinks `K_y` and cannot remove the actual source if the declared source model is correct. Pairwise nonempty intersections DO NOT imply common nonempty intersection: the three sets `{0,2}`, `{0,1}`, `{1,2}` are pairwise compatible, jointly empty. The tests construct these with honest source_lambda Boolean predicates read at three distinct source candidate examples; the inconsistent combined transcript is not falsely labeled a performed single-source trajectory. The generalized CRT exception is explicit: a pure family of integer congruences has a special pairwise gcd sufficiency theorem; the counterexample instead concerns arbitrary typed predicates over a restricted source class.

## 3. ECλ-02: consensus gains distinguishing dimensions, not voters

Let `D_T={(x,y) in X²: x<y and T(x)!=T(y)}`. A port covers the pairs on which its two predictions disagree. The joint target factors iff the **union of pair-coverage sets** equals `D_T`.

The `exact_portfolio` routine computes the smallest number of admissible ports covering these target-disagreeing pairs, by exhaustive subset enumeration with explicit source and budget caps. It is an exact finite set-cover computation, not an optimal scalable solver. Its result is a certificate of **model-specific sufficiency**. Ten observers measuring the same quotient have the same coverage as one observer; no amount of uncorroborated agreement raises their algebraic rank. Even two distinct candidate sources with identical arithmetic labels remain indistinguishable to *every* term of this lambda fragment, whatever their targets.

**Positive calibration:** candidates 0,1,2,3; E1 reads mod 2, E2 mod 3. Each E alone confounds two candidates, but the joint pair identifies all four. One E must unlock its sensor with an explicit modeled control action first. The initial E sphere does not include that sensor; at radius 1 it does. A finite executed pair of source-matched reports identifies candidate 3 in the declared model. This is analogous to the existing complementary-observer/XOR demonstration, **not** a claim that physical probes exist.

**Negative calibration:** repeated mod-2 Es cannot distinguish original candidates labeled integers 0 and 2 with different target values. Their consensus remains `TARGET_UNRESOLVED`. Copying testimony changes an observer's available knowledge, not the source-to-report partition.

## 4. ECλ-03: action spheres require a JOINT realization contract

For E device `i`, `B_i(r)` is the reachable control-state set at path length `<=r`. Let `M_i(q)` be programs enabled at that state. For a tuple of reachable states `q=(q_i)`, the jointly admitted port family is

`P(q)=union_i { (i,p) : p in M_i(q_i) }`.

**Crucial repair [PROVED LOCAL].** We must select **one final configuration** `q_i` per E before treating its enabled ports as jointly available. Merely unioning everything seen anywhere in `B_i(r)` creates a phantom collection of mutually exclusive instruments. `exact_portfolio` enumerates admissible tuples of terminal states and then exact portfolios within each. The separate union-of-all-sphere coverage is retained only as a diagnostic upper bound.

The model's *one-state forcing depth* for target `T` is

`R_T = min { r : exists q_i in B_i(r), intersection_{p in P(q)} ker(p) subset ker(T) }`.

This minimum is computed under bounded finite state/program enumeration. If successful, it is an exact earliest radius **under this protocol**, with a certificate that no smaller radius supports a separating portfolio. If unknown due to budget, it returns `DEPTH_BUDGET_GAP` or `RESOURCE_BUDGET_GAP`, never falsehood. Every reachable state of a finite deterministic control graph has a simple path of length at most `|Q_i|-1`. Thus after all those horizons are considered, the **one-terminal-state protocol** is exhausted, not the global toolkit of possible protocols.

**Hostile branch control:** E from initial `root` may reach `left` (mod2) or `right` (mod3), but cannot go from one terminal state to the other. The naive union of sphere menus would identify the 0..3 source. The lawful one-state planner returns `UNJOINTLY_REALIZABLE_PORT_FAMILY`; the forcing verdict is `ONE_STATE_PROTOCOL_SATURATED`. Forging an actually executed transcript from mutually exclusive same-E paths is refused.

**Important distinct positive control:** another E has a real modeled chronological path `root -> middle -> end`. It records mod2 *at middle* and mod3 *at end*. Those prefix-compatible, nondestructive **actually declared** observations can be fused to identify the source. The conservative **one-terminal-state planner** still says it cannot optimize that sequential strategy. This is a named planning restriction, not darkness of the source. Extending the planner to ordered-action strategies is the next implementation priority.

The operational sphere is **not** the E's intrinsic/topological S² and does not suggest a smooth source manifold.

## 5. ECλ-04: no-free-sensing theorem for nested Es

Suppose every constructed mini E report is a legitimate factor of an existing common parent report `h:X->Y`: `o_i=g_i∘h`. Then their joint observation is `(g_1,...,g_m)∘h`, hence

`ker(h) subset intersection_i ker(o_i)`.

**Proof.** If `h(x)=h(y)`, every `g_i` must return the same value on those inputs. QED.

This is the elementary mathematical core of MATRYOSHKA's no-free-hidden-source boundary. Better computation and more nested layers may compress, synchronize and communicate known evidence, but cannot create a distinction absent from the parent readout/action closure. Actual source interventions, additional physical sensors, or a structurally justified theorem are needed to change that closure.

`MiniPort` validates a true MATRYOSHKA `compile_factor` receipt, preserves public translations, and exposes no hidden decoder state. `certify_dual_ports` additionally checks the source-derived joint product. Two individually lawful factors of the three-state parent `{00,01,10}` do **not** imply the fourth product state `11` exists: `compile_dual_product` must reject the ghost. Two bit miniatures above a genuine four-state parent with noninterfering toggles do pass their exact conditional finite source squares. None is authenticated physical apparatus.

## 6. ECλ-05: communication consensus and source-faithful relay

The prior knowledge ladder proved that transmitting trusted evidence can put a receiver into the same *epistemic placement* in fewer macro-updates while retaining distinct physical access and causal history. Here an `ERelay` preserves the source observation object and the origin E; its receipt counts no new primitive read. Retelling one observation cannot increase the common-refinement rank, even if many recipients display unanimous agreement.

`minimum_consensus_channel` compiles two admitted E output functions with the original target into the existing `InterobserverWorld`, then invokes `exact_minimum_channel`. This is the classical graph-coloring theorem for one-shot, zero-error coding with receiver side information. The candidate model at addresses 0..3 has a mod-3 sender (three distinct views) and mod-2 receiver; four distinct targets are jointly recoverable. The sender needs **two codewords/one fixed bit**, instead of the naive two bits for three uncompressed sender symbols, because the receiver's side information disambiguates the relevant conflicts. This is exact **conditional information compression**, not an added observer or source oracle.

The calculation is valid only for a common finite source family and correctly produced readouts. Distinct E names and a good code do NOT prove physical independence, instrument calibration, or source authenticity.

## 7. ECλ-06: intrinsic sphere consensus can miss ambient nonabelian truth

The prior **WILD-SUCC** dossier reproduces (with classical topology imported) Hatcher's Alexander horned-sphere complement tower `F_1 -> F_2 -> F_4 -> ...`, each meridian mapped to a commutator. The direct-limit group `G` is **nontrivial and perfect**. Thus its abelianization and every one-dimensional `U(1)` character vanish on the nontrivial meridian. More strongly any map from `G` to a solvable group is trivial, because a perfect solvable group is trivial.

For the stage-`k` iterated meridian, word length is `4^k` and lower-central depth is `2^k`. Every nilpotent stage observer whose class is strictly less than `2^k` must miss it. A sharp stage-specific integer unitriangular detector `UT_(2^k+1)(Z)` exists at that stage, but those detectors **do not form a compatible nontrivial representation of the perfect direct-limit group**. The `horned_sphere_consensus_control` wrapper calls the *actual existing* WILD-SUCC functions rather than fabricating a second topological source.

**Consequence [CLASSICAL + FINITE CALIBRATION].** More Es, more votes and even unbounded many **same-typed abelian shadows** need not expose the defect. To reveal it one needs a lawful probe whose algebraic functor does not kill that distinction; lowering a finite resource cost is insufficient. This is an exactly scoped counterexample to consensus-as-truth, not evidence that the Riemann zeta completed Weil operator has Alexander wildness.

## 8. ECλ-07: two positive local chart energies are NOT a global Weil sign

For an arbitrary exact real symmetric two-chart model,

`G=[[a,c],[c,b]]`, with `a,b>0`,

both isolated diagonal readings are positive. Yet `det G=ab-c²` may be negative; then the exact vector `v=(c,-a)` has energy

`vᵀ G v = a(ab-c²) < 0`.

The module's `two_chart_cross_energy` invokes the inherited exact rational `signed_witness` for this calculation. It reproduces `(a,b,c)=(1,1,2)` giving negative energy `-3` for `v=(2,-1)`. **The missing information is the cross-chart coupling**, not more repetitions of either positive diagonal observation. This toy form is explicitly **not the authentic Suzuki/Weil source**.

This supplies a concrete target for future SUCC-λ analytic effects: `CrossEnergy(source, f, g, radius, interval, tail, conductor, phase)`. The source must be the original completed signed Weil distribution, including genuine `Lambda(p^k)/sqrt(p^k)` impulses, the sole real Gamma tower, pole contributions, half-density and valid test-function domain. Only a source-authenticated *strict negative upper interval* for `W_zeta(f*tilde(f))`, or an independently proved all-function sign theorem, could carry RH-critical authority. A majority of positive auxiliary Gram results cannot.

## 9. Claim ledger and tools/probe calibration

| Claim | Verdict / scope | Required next independent check |
|---|---|---|
| ECL-01 common-source target factorization | ELEMENTARY PAPER PROVED, exact finite tests | Formalize finite kernel intersection and source-typed report signature in YEAN |
| ECL-02 minimal separation portfolio | EXACT FINITE CHECK (bounded exhaustive set cover), direct modular holdouts | Extend to certified dynamic action schedules without ghost branch unions |
| ECL-03 finite access sphere and saturated one-state protocol | ELEMENTARY PAPER PROVED + test; no all-protocol impossibility | Replay exact step-cost and original/current belief semantics |
| ECL-04 nested mini cannot invent distinctions | ELEMENTARY FACTORIZATION, actual MATRYOSHKA API replay required | Independent dual-product/interference controls on exact hosted branch |
| ECL-05 receiver-side minimum channel | CLASSICAL Witsenhausen + existing exact finite solver | Hosted replay of imported interobserver code; no simulated sender authorization |
| ECL-06 perfect wild exterior invisible to solvable observers | CLASSICAL IMPORT + WILD stage exact control | Verify stage-to-limit incompatibility, do NOT infer RH |
| ECL-07 cross-term may destroy local positive consensus | EXACT FINITE RATIONAL negative witness | Real completed Weil cross-form signed interval and analytic tail |
| ECL-08 earliest TRUE RH resonance detection bound | **UNVERIFIED / OPEN** | Construct explicit source-identified analytic port and uniform forcing theorem |

**Hostile controls:** source/epoch/basis mismatch; repeated identical E source; hypothetical E spheres counted as observations; mutually exclusive port menus; pairwise-consistent but globally impossible reports; illicit hidden mini state exposed as sensor; separate mini factors with ghost joint product; wrong/changed report; unexecuted lambda closure; finite mod2/3 indistinguishability; repeated uninformative E relays; wrong float-signed Gram; no global nilpotent character; model candidate outside parent carrier. Exact numeric tests cannot certify physical source or the all-support signed Weil form.

**Baseline local worktree:** Python focused tests and deterministic probe run with `PYTHONPATH` pointing at the package containing the new file and #139's `source_lambda`. Existing MATRYOSHKA, WILD and communication imports are present on full `main`, but **not copied into the isolated local module harness**; those integration cases were skipped locally, and must run unskipped under full SUCC CI. Frozen source archives and existing code are untouched. A source-text SHA or successful CI proves neither mathematical novelty nor physical access.

## 10. Next round that can actually change the mathematical frontier

1. **Build dynamic consensus as AND/OR belief SUCC.** Use the already existing `FiniteCarrier`, `adaptive_proof_policy`, `operational_yoneda_descent` and `no_ghost_policy`. Replace the conservative one-terminal E state protocol with source- and current-state pairs and actual jointly admissible action histories. Solve a finite minimum worst-case observer-coordination policy; verify against hidden-path and changing-source mutants.
2. **Attach a truly source-preserving signed arithmetic port.** Its *effect* is not merely `Read(n)`: require exact source ID, hash, conductor/parity, `Gamma_R`, poles, half-density, prime powers, bounded-radius autocorrelation, certified approximation and separate true-source-to-Weil identification. Cross terms between observer modes are indispensable.
3. **Proof-mine effective forcing depth.** With the port above, seek a certified `R_T(epsilon)` for a fixed authentic radius/support and low/high Schur response. Cross-family resonance must survive chi4, fake composite, altered Gamma and auxiliary self-dual Gaussian controls. Until then there is **no** RH counterexample resonance amplifier, just exact finite source-relative discrimination machinery.
4. **YEAN formalization.** Import ECL-01, ECL-03 finite machine state reachability, ECL-04 kernel inclusion and witness audit; retain all source/analytic hypotheses and trust boundaries. Neither model-space exhaustive enumeration nor Lean Boolean reflection is an analytic RH proof.

**Final scoped verdict:** Consensual Es can genuinely improve *target-specific finite discrimination and communication efficiency*. They cannot overcome a common probe kernel, fabricate a jointly executable experiment, or make the completed Weil positivity sign appear from unrelated positive auxiliary observations. RH remains OPEN.
