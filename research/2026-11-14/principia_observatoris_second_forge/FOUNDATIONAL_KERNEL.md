# Foundational kernel: the finite observer, constructed from below

**Second Forge, 2026-11-14.** This is the smallest constructive definition of a finite observer
interacting with a carrier that the campaign's theorems actually use. It was obtained by starting
from explicit finite systems and deleting every component whose removal changed no theorem. It is
a definition plus consequences, not a metaphysics: every statement is about a *declared finite
model*, and whether a declared model describes a real source is a separate obligation that
nothing here discharges.

Proof pointers: `FO-*` = [agents/OPUS_I_FINITE_OBSERVER.md](agents/OPUS_I_FINITE_OBSERVER.md);
`QG-*`, `RG-*`, `HQ-*` = [CAUSAL_GEOMETRY.md](CAUSAL_GEOMETRY.md);
`FH-*` = [FINITE_HORIZONS.md](FINITE_HORIZONS.md); Lean = `formal/ObservatorisQuantale.lean`.

## 1. Primitive data

**K0 (carrier).** A finite set `X` of source states; a finite set `A` of lawful operations; for
each `a ∈ A` a readout `o_a : X → V_a` in its own chart and a transition `t_a : X ⇀ X`.

**K1 (source selection).** A nonempty set `S ⊆ X` of states the source may be in (a single
`x₀` when the start is known). `S` is the observer's uncertainty fibre.

**K2 (target, optional).** A function `P : S → Y`.

**K3 (value structure, optional).** A quantale-like structure `V` and a weight `R : X × X → V`
on transitions (truth, cost, elapsed steps, best-path relevance, action words).

That is the whole kernel: **`(X, A, (o_a, t_a), S)`**, plus a target when knowledge of something
is in question, plus weights when cost, time or distance is in question. SUCC's existing
`Carrier`/`Instrument` and `Machine`/`Edge` contracts are instances; no new container was needed.

## 2. What was deleted, and why it could be

The commissioning sketch was `Observer = (Carrier, Instruments, Actions, Records, Resources, Target)`.
Testing each component (FO-1, PROVED):

| Component | Verdict | Reason |
|---|---|---|
| Instruments vs Actions | **one notion** | an action is an operation with constant readout; a pure observation is one with identity transition. Splitting each operation into "measure" + "act" leaves the behavioural partition and the reachable set unchanged. |
| …but the *pairing* is not redundant | **keep it** | the split changes what a single unresettable copy can learn: the destructive A,B,C carrier becomes freely observable once measurement is separated from its disturbance. Counterfactual knowledge ignores the pairing; executable knowledge does not. |
| Records | **derived** | a record is the transcript of a word: `(o_{a₁}(x), o_{a₂}(t_{a₁}x), …)`, each readout taken before its operation acts. |
| Resources | **not part of observation** | costs never change the core; they matter for bounded or single-copy execution, and then they are a `V`-weight (K3). |
| Target | **indispensable for knowledge, irrelevant for observation** | without a target the only canonical question is the full behavioural class. |
| Source selection | **indispensable** | unpointed diagrams can commute while the selected-start claim is false (SUCC's three-state ghost, inherited; weighted form QG-3). |
| Partial transitions | **reducible only under a premise** | refusal may be totalised to an observable `⊥` *only if refusal is observable*; that is an assumption about the source, not a theorem. |

## 3. Derived notions

- **Experiment / history:** a word `w ∈ A*`; **record:** its transcript; **policy:** a rule from
  records to the next operation (a finite decision tree).
- **Behavioural equivalence** `x ∼ y`: equal transcripts for all words. (Classical: Moore, Nerode;
  SUCC's `behavioral_partition`.)
- **Core:** `Reach(x₀)/∼` with induced readouts and transitions.
- **Structural reachability / distance:** the closure `R*` over the chosen `V` (QG-1).
- **Two closure operators on `V`-valued predicates over `X`:**
  the **dynamical closure** `Cl_R` (close under what the carrier can do) and the
  **observational closure** `Sat_q = q^* q_!` for an observation `q` (close under what the
  observer cannot separate).

## 4. The kernel theorems

Each line is a theorem with a proof elsewhere in this package; together they are the working
"axioms" a user of the kernel may rely on. None is assumed.

**KT-1 Identification (FO-2; CLASSICAL Moore/Nerode, sharpness PROVED).** Two pointed carriers
with cores of sizes `n`, `m` have equal responses on all words of length `≤ n+m−1` iff their
cores are isomorphic, by a unique isomorphism; the bound is sharp. Complete response data
determine the core **and nothing more**: unreachable states and behaviourally merged states are
unidentifiable in principle.

**KT-2 Toolkit monotonicity (FO-3, PROVED).** For toolkits `A ⊆ A∪B`:
`core_A(M) ≅ core(core_{A∪B}(M)|_A)`. A new *readout* can expose a hidden distinction in a
2-state carrier; a new *pure intervention* needs exactly 3 states. Correction to the PI's first
formulation: a new instrument does not only refine — an intervention can also make new states
reachable; the exact map is a surjection from a sub-carrier of the new core onto the old core.

**KT-3 Target descent (inherited SUCC, `docs/CARRIER_RELATIVE_TARGETS.md`).** `P` is determined by
observations `E` iff `P` is constant on the fibres of `E`; an empty fibre is *incoherent*, not
vacuously true.

**KT-4 Executable versus counterfactual knowledge (FO-10, PROVED; independently CA-1).**
Whether a single unresettable copy can reveal its behavioural class is decided exactly, for all
horizons, by a least fixed point on beliefs. If no operation changes the behaviour class
("free observation"), reading every instrument once suffices and behaviour is the joint one-shot
readout; class-injective dynamics also suffices. Neither is necessary, "commuting and idempotent"
is **not** sufficient, and **executable knowledge is not closed under conjunction**: there is a
4-state carrier in which every Boolean target is separately accessible and the class is not.

**KT-5 Geometry under observation (QG-2, QG-3, QG-4; Lean, axiom-free).** For every value
structure: the may-quotient never under-reports (`R* ≤ Q∃*`); the must-quotient never
over-reports (`Q∀* ≤ q_!R*`); and selected-start exactness has an exact criterion.

**KT-6 Exactness is commutation (Lean `satClosed_iff_sat_closure_idempotent`,
`closure_push_adjunction`).** `L = Cl_Q ∘ q_!` is left adjoint to pullback `q^*`; it sends the
source closure from `x` to the quotient closure from `q(x)`; and all-start exactness holds iff
`Sat_q ∘ Cl_R` is idempotent. In words: *the observer's effective world is the join of the
dynamical and observational closures; the source seen through the observer is their composite;
the ghosts are the difference; exactness is the statement that "evolve, then blur" is already
closed.*

**KT-7 Structure versus response (RG-1, RG-4, FO-8, FO-9).** Net response is supported inside
structural dependency; equality holds for balanced linear carriers and fails through signed
cancellation or through gating in an unrealised context. Hidden wiring is **not** a response
invariant; the essential graph of an unrestricted network class is identifiable iff every node's
potential parents can be clamped jointly over all contexts while the node is read.

**KT-8 Order of intervention (FO-4…FO-6, PROVED; Möbius inversion CLASSICAL).** From a baseline,
a dependency on input `j` is detected at simultaneous-intervention order exactly
`h_j = min{|S| : j ∈ S, Δ_S f ≠ 0}` and is invisible to every lower order; certifying *absence*
within degree `d` costs exactly `2·Σ_{i<d} C(k−1, i)` evaluations.

**KT-9 Finite horizons (FH-3…FH-12).** Inside a class with a declared complexity bound, a
finite record determines all future records, with exact sharp constants. Without the bound the
observer identifies the truth in the limit and can never certify having done so.

## 5. What the kernel treats as premises (never as observations)

These are the places where a finite record cannot substitute for knowledge of the source. Each
was found by a theorem failing when the premise was removed.

1. **Source adequacy.** That the declared table describes the intended source.
2. **Source selection.** Which state, or which fibre, the source is actually in.
3. **A complexity bound** (state count, dimension, degree). It is not observable (FH-5), and
   physical size is an exponentially weaker bound than state count (FH-7).
4. **A modulus of convergence.** Without it a prefix says nothing about a limit (FH-10).
5. **Observability of refusal** for partial operations.
6. **Calibration transport.** One-way magnitude comparisons are not unit-free (RG-5).
7. **Completeness of the model's wiring.** A geometry has no unseen ancestor exactly when it
   covers every source edge (QG-5); whether it does is not readable from the geometry itself.
8. **The observer's own causal role.** Once it acts on its record the observer is a channel from
   sensors to actuators that is not an edge of the carrier (HQ-1, HQ-3).

## 6. What an observer can distinguish, compute, know — in the kernel's terms

| Question | Kernel answer |
|---|---|
| What can be distinguished? | `∼`-classes: the core (KT-1). |
| What can be reached / how far? | `R*` over the chosen value structure (QG-1). |
| What does the observer's geometry assert? | `Q∃*` (possible) and `Q∀*` (guaranteed) (KT-5). |
| What can be known about a target? | whether `P` is constant on the surviving fibre (KT-3). |
| What can one copy actually find out? | the belief fixed point (KT-4). |
| What cannot yet be known, and why? | one of the eight premises in §5 is missing, or the target is discontinuous at the source (FH-1). |
| When does finite evidence justify an exact conclusion? | when the conclusion is constant on the fibre of sources compatible with the evidence **and** the premises; the theorems of FINITE_HORIZONS give the exact horizons. |

## 7. Boundary

The kernel is finite, deterministic and synchronous. Stochastic carriers appear only through
weighted automata (FH-9) and one exact declared Hilbert model
(`observatoris_classical_appearance`). It does not model continuous time, noise, or an observer
with bounded memory, and it does not claim that any brain, device or physical field performs
these computations.
