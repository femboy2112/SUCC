# Tenacious D handoff: the Second Forge, prepared for cross-examination

**Second Forge (Claude Fable principal, Claude Opus delegated), 2026-11-14.** This is a
self-contained briefing for a future interface audit between this constructive, carrier-upward
programme and the independent axiomatic programme ("Astra"). It is written so that the two
systems can be connected through explicit maps, theorem by theorem, without sharing prose or
metaphors. Nothing from the Astra campaign was read, used or coordinated with in producing this
package (see [PROVENANCE_AND_INDEPENDENCE.md](PROVENANCE_AND_INDEPENDENCE.md)).

Identifiers: `QG/RG/HQ` → [CAUSAL_GEOMETRY.md](CAUSAL_GEOMETRY.md); `FO` →
[agents/OPUS_I_FINITE_OBSERVER.md](agents/OPUS_I_FINITE_OBSERVER.md); `FH` →
[FINITE_HORIZONS.md](FINITE_HORIZONS.md); `CA` → [THEOREM_FORGE.md](THEOREM_FORGE.md) §F;
"Geometer CG" → [agents/OPUS_II_CAUSAL_GEOMETER.md](agents/OPUS_II_CAUSAL_GEOMETER.md).

## 1. Primitive definitions and "axioms"

We assume **no axioms about observers**. The primitives are data; everything else is derived or
is an explicitly named premise.

**Primitive data** ([FOUNDATIONAL_KERNEL.md](FOUNDATIONAL_KERNEL.md) §1):

- **K0** a finite carrier `(X, A, (o_a, t_a)_{a∈A})`: states, operations, per-operation readout
  and (possibly partial) transition;
- **K1** a nonempty set `S ⊆ X` of possible source states;
- **K2** (when knowledge is at issue) a target `P : S → Y`;
- **K3** (when cost, time or distance is at issue) a value structure `V` and weights
  `R : X×X → V`.

**The value structure** is the only algebraic axiom set in the package. It is the list of
inequalities in `LaxQuantale` (`formal/ObservatorisQuantale.lean`): a preorder with arbitrary
suprema, a monotone multiplication distributing over suprema on both sides, associativity and
unit laws. Commutativity, antisymmetry and idempotence of the multiplication are not assumed.

**Named premises** (never derived from records; each is indispensable for the theorems that cite
it — KERNEL §5): source adequacy; source selection; a complexity bound; a modulus of
convergence; observability of refusal; calibration transport; completeness of the model's
wiring.

## 2. Strongest proved theorem

**The observation–dynamics commutation theorem** (QG-3, QG-7, QG-10, with QG-4 and QG-6).
For any set `X`, any observation `q : X → Y`, any `V`-weighted relation `R` over any value
structure, the following are equivalent:

1. no quotient endpoint value is invented, from any start: `Q∃*(q(x),b) = ⋁_{q(z)=b} R*(x,z)`;
2. pushed-forward closures are constant on observation fibres;
3. direct image preserves potentials; 4. saturation preserves potentials;
5. every source edge is realised from every representative of its start report
   (`Q∃(R) ≤ Q∀(R*)`);
6. "evolve, then blur" (`Sat_q ∘ Cl_R`) is idempotent.

In all cases `Q∀* ≤ q_!R*(x,·) ≤ Q∃*`; `Cl_Q∘q_!` is left adjoint to `q^*` and carries the source
closure from `x` to the quotient closure from `q(x)`; and exactness transports along strict
homomorphisms of value structures.

*Authority:* Lean 4.14 core, no imports, **no axioms**, 18 exported declarations, two rejected
mutations; independently proved on paper by a different agent with exhaustive finite models over
six value structures (one noncommutative), reproducing SUCC's 2,594-model Boolean census.
*Scope:* idempotent values only. *Not established:* any signed, probabilistic or physical
statement; source adequacy.

## 3. Strongest no-go results

1. **Limit-identifiable, never certified (FH-5).** On linear-recurrent sequences of unknown
   order, a learner is exactly right from time `2·ord(x)` on, and **no sound stopping rule halts
   on any member**. A declared order bound `n` restores a certificate at exactly `2n` terms.
2. **Executable knowledge is not closed under conjunction (FO-10d).** A four-state carrier in
   which each of the eight Boolean targets is accessible to a single copy and the conjunction
   (the class) is not.
3. **Structure is not response (RG-1c, FO-8).** A carrier in which every edge is live and the
   composite response vanishes at every lag; a second, distinct mechanism (gating) in
   cancellation-free networks. Hidden wiring is not an invariant of accessible response data.
4. **Readout-only decidability = continuity (FH-1).** At a discontinuity point every terminating
   protocol errs; the founding two-regime label is discontinuous at the limit-only member.

## 4. Dependencies

```
PAP-01..05 (SUCC, inherited) ──► QG-1 ─► QG-2 ─► QG-3 ─► QG-7, QG-8, QG-10
                                  │        │       └────► QG-6 (adjunction, ghost defect)
                                  └────────┴────► QG-4 (sandwich) ─► QG-5, HQ-4
Cayley–Hamilton (classical) ─► RG-2 ;  Harary balance (classical) ─► RG-4 ─► RG-3, HQ-2
finite propagation ─► HQ-1 ─► HQ-2, HQ-3
Moore/Nerode (classical) ─► FO-2 ─► FO-3, FO-10 ;  Möbius inversion ─► FO-4 ─► FO-5, FO-6
kernel dimension + lcm ─► FH-3 ─► FH-4, FH-5, FH-6 ;  Cauchy determinant ─► FH-6
SUCC target descent (inherited) ─► FH-10 ;  finite-information topology (classical) ─► FH-1, FH-11
```

## 5. Assumptions that appear indispensable (each with the receipt that shows it)

| Assumption | Needed by | Receipt when dropped |
|---|---|---|
| a selected start / fibre | QG-3 | unpointed closure diagram commutes, selected-start claim false (PAP-04 ghost) |
| idempotent values | QG-2, QG-3 | signed quotient both invents and deletes (Geometer CG-13) |
| distribution of `⊗` over joins | QG-1…3 | non-distributive lattice-monoid mutation fails (Geometer tests) |
| strictness of a change of base | QG-8 for a selected start | oplax `⌊a/2⌋` receipt; lax `[0∈A]` receipt |
| balance (up to a global sign) | "response = structure" | signed diamond |
| a declared complexity bound | every finite-horizon theorem | FH-5 |
| monic recurrence | FH-3 | `0·x = 0` |
| a declared modulus | FH-10 | limit set of every prefix is ℝ |
| joint clamping of all parents | FO-9 | constant-table pair with one altered unrealised context |
| free observation or injectivity | single-copy access | destructive A,B,C carrier |
| transported calibration | one-way magnitude comparisons | unit change reverses an order |

## 6. Results that need a different source map or a new instrument

- **Signed diamond / cancellation:** invisible to every experiment on `(x, z)`; exposed by an
  intervention on one branch.
- **Hidden wire (HQ-3):** no invariant of the model reveals it; a finite contrast violating the
  model cone does.
- **Interaction order (FO-4):** a dependency at order `h` needs `h` simultaneous interventions.
- **Gating (FO-8):** needs a context outside the realised range.
- **Unknown dimension (FH-5):** needs a premise about the source, not an instrument.
- **Limit claims (FH-10):** need a proved modulus.
- **π-normality, RH:** need the authenticated source and its signed cancellation estimate; this
  package supplies neither and says so.

## 7. Where a rival foundational construction is most likely to collide with ours

We do not know Astra's axioms. These are the commitments an axiomatic route might naturally make
that our receipts contradict; each is a test to run at the interface.

| A rival commitment of this form… | …contradicts | Receipt |
|---|---|---|
| closeness is a single symmetric metric fixed by relevance | RG-5, RG-1c | one-way order reversed by units; signed diamond breaks the triangle inequality |
| causal relevance ⇔ nonzero derivative or first-order response | FO-4, RG-1c | AND gate invisible below order `k`; cancelled path |
| a coarse-grained observer sees a sub-geometry (distances preserved or lost) | QG-2 | quotient distances only shrink; ghosts are invented, never hidden |
| knowledge is closed under conjunction | FO-10d | four-state carrier |
| measurement and action are separable without loss | FO-1(6) | splitting changes single-copy access |
| more instruments only refine | FO-3 | an intervention enlarges the reachable set |
| "classical" is a predicate of a system | CA-3 | witness table |
| sufficiently long agreement justifies a universal or limit claim | FH-5, FH-10 | no certifier; unconstrained limit |
| the observer's geometry determines what the source can do | C-9 | two sources, same four quotient closures, different futures |
| exactness is stable under any reasonable change of scale | QG-8 limits | lax and oplax receipts |
| hidden causes are those outside a coarse view | QG-5 | a coarse view cannot hide an ancestor; an omitted edge can |

If Astra's axioms *imply* any left-hand statement, one of the two systems is wrong and the
receipt decides. If they are merely compatible with it, the receipt is a required countermodel.

## 8. Questions an independent researcher should use to attack this package

1. Is `LaxQuantale` really weaker than a unital quantale in every field, including for the
   reversed-order cost structure? Exhibit a quantale failing a field, or a pathological
   `LaxQuantale` instance in which a theorem is vacuous.
2. QG-5 says a may-quotient geometry has no unseen ancestors. Is that a theorem about observers
   or a tautology of defining the geometry from the unseen source? What is the strongest version
   for an observer who only has a quotient of a *subgraph*?
3. RG-3 claims `−log` of the response is derived for balanced carriers. Is the object obtained a
   Lawvere metric (sign, diagonal, dependence on horizon and discount), or only a graded family?
4. Break HQ-1 with a policy that has memory, randomisation, or sensors that are actuators.
5. FH-5: is "no sound certifier halts" robust to certifiers allowed a bounded error probability?
6. FO-10d: does a *resettable* copy or a second copy restore conjunction-closure, and at what
   exact cost?
7. Do the finite-horizon constants survive noise? Give the exact precision–horizon trade-off
   beyond FH-6(e).
8. Is there a nonlinear analogue of balance excluding both cancellation and gating?
9. Which of our "premises" (KERNEL §5) can Astra's axioms *derive*? Any such derivation is a
   theorem we could not prove from below.
10. Find a carrier where our kernel's totalisation of refusal over-reports what can be known.

## 9. Promising but unproved

- A canonical coarsest refinement for *selected-start* exactness on `Reach(x)` (conjectured to
  exist there; refuted globally).
- The open-map reading of condition 5 (`Q∃(R) ≤ Q∀(R*)`).
- Whether oplax is the optimal class of maps transporting all-start exactness.
- A may/must bracket for hitting probabilities; non-idempotent analogues of resolvent
  lumpability.
- Sharpness of `2d` mind changes for every `d`.
- An intercept theorem (detect *and* act before the target is affected).
- A sign-pattern criterion for possible cancellation at a given lag.

## 10. Theorem interoperability contract

Each row: the **input structure** a theorem accepts and the **output invariant** it guarantees.
To transport a theorem into another system, supply a map from that system's structures to the
input type preserving the listed data; the output then holds there verbatim.

| Theorem | Input structure | Must be preserved by an adapter | Output invariant / conclusion |
|---|---|---|---|
| QG-1 | `(X, R: X×X→V)`, start `x` | edge weights, unit | `R*(x,·)` = least potential with unit at `x`; potential certificates are sound lower/upper bounds |
| QG-2 / QG-4 | `(X, R, q: X→Y)` | fibres of `q`, edge weights | `Q∀*(q x,b) ≤ ⋁_{q z=b}R*(x,z) ≤ Q∃*(q x,b)` |
| QG-3 / QG-7 / QG-10 | same | same | six equivalent exactness conditions; a verdict plus a ghost witness when it fails |
| QG-6 | same, plus a quotient potential `ψ` | same | `Cl_Q q_!φ ≤ ψ ⇔ φ ≤ q^*ψ`; ghost defect of a start |
| QG-8 | an exactness certificate over `V`, a strict map `h: V→W` | joins, products, unit | exactness of `h∘R` over `W` at the same start |
| Geometer CG-10 | `(X, R, q)` | same | the unique coarsest exact refinement `q̂` and exact source values through it |
| RG-1 / RG-4 | a square matrix over an ordered field | zero pattern, signs | response support ⊆ structure; equality if balanced up to a global sign |
| RG-2 | same, dimension `n` | dimension | "no response for `n` lags" ⇒ "no response ever" |
| RG-5 | two matrices with equal patterns and signs | pattern, signs | unit-equivalence verdict with a certificate; `b₁` free magnitudes |
| HQ-1 / HQ-2 | a dependency digraph, sensor set, cause set, target | edges (parents), synchronous update, record-driven policy | no record depends on the cause before `d(H,S)`; lead time ≤ `d(H,y) − d(H,S)` |
| HQ-3 | a model graph and one finite contrast | node identification between model and source | a source edge absent from the model |
| FO-2 | two pointed finite carriers over the same operations | readouts, transitions, start | equal responses to length `n+m−1` ⇔ isomorphic cores |
| FO-4 / FO-6 | a function on `k` binary inputs, a baseline, an order budget | values on the Hamming ball | detected dependencies; exact cost of certifying absence within degree `d` |
| FO-9 | a potential-parent DAG and an experiment family | which nodes are clamped, free and read | identifiability verdict for the unrestricted class |
| FO-10 | a finite carrier and a start set | readouts, transitions | exact all-horizon verdict on single-copy access, with a policy or an obstruction |
| FH-3 / FH-4 | two exact prefixes and declared order bounds (or polynomial families) | exact values, the declared bounds | equality forever, or the extremal witness |
| FH-5 | a prefix stream | exact values | a conjecture trace; a refutation of any proposed stopping time |
| FH-10 | a prefix and a declared modulus | the modulus | the exact interval of compatible limits |
| FH-1 / FH-11 | a class of sequences and a target | the finite-information topology | decidable by finite readout ⇔ continuous at every point |
| CA-1 | a finite deterministic carrier | readouts, transitions | free observation ⇒ behaviour is the joint one-shot readout |

**Invariants we expect any correct rival system to agree on** (because a theorem forces them, not
because we prefer them): the core of a carrier (FO-2); the exactness verdict of an observation
(QG-3); the sandwich (QG-4); the finite-horizon constants inside the declared classes (FH-3,
FH-7); the unit-free content of a positive carrier (RG-5). **Things on which the systems need
not agree:** primitives, vocabulary, the choice of value structure, and which statements are
taken as premises.

## 11. Inherited versus independently derived

- **Inherited from SUCC (attributed, not rediscovered):** PAP-01…05 and their Lean file; target
  descent, the observer algebra, the destructive-instrument example and the target-oscillation
  radius; the `Machine`/`Carrier` contracts.
- **Inherited from PR #618 (shared input, not a validation witness):** the working principle
  "closer = more causally relevant"; the finite contrast and the impulse-response identity; the
  two-path cancellation and common-cause adversaries; the two-regime pair `a`, `b_H`; the unseen
  causal set `U`; the model-relative classical-appearance hypothesis.
- **Independently derived here:** everything registered in THEOREM_FORGE §A–§F, with classical
  ingredients named where used.

## 12. Receipts

- **Repository / branch:** `femboy2112/SUCC`, branch `ccr-db6a5bf5-l6g6wu` (the session's
  designated non-main branch; the suggested name `research/principia-observatoris-second-forge`
  was not used because this environment permits pushes only to the designated branch).
- **Base:** `db9fb4b84672050efa79b13377f1e73364598a14` (Main XXV).
- **Shared founding source read:** PR #618 at head `ab31057590a59b2bfbd5dbcd7126b2aefc7a2b55`
  (not modified).
- **Draft PR, head commit and validation results:** recorded in
  [PROVENANCE_AND_INDEPENDENCE.md](PROVENANCE_AND_INDEPENDENCE.md) §6 and in the PR description,
  which state exactly which commands were run and what they returned.
- **Kernel receipt:** [receipts/lean-kernel.json](receipts/lean-kernel.json).
