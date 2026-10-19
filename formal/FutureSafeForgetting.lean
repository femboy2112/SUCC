/-!+# Future-safe forgetting for partial deterministic systems with exact costs

Standalone Lean 4.14.0; no domain-library imports.
The state may explicitly include source identity, complete history and budget.
Those data are not automatically supplied by this theorem.  Report may bundle
source tags, observations and declared mathematical task results.  This does
not prove that the task results are true or physically observable.

`blocked` is a mathematical lawfulness marker.  Interpreting it as an observed
outcome requires an extra menu/rejection instrument, absent from this theorem.
Cost is an arbitrary exact label; its order, addition and budget are not needed.
The supplied section makes quotient construction constructive and avoids choice.
-/

set_option autoImplicit false
namespace ObservationalSUCC.FutureSafeForgetting
universe u v w z q

structure System (State : Type u) (Action : Type v)
    (Report : Type w) (Cost : Type z) where
  observe : State → Report
  step : Action → State → Option (State × Cost)

def mapStep {State : Type u} {Small : Type q} {Cost : Type z}
    (forget : State → Small) : Option (State × Cost) → Option (Small × Cost)
  | none => none
  | some (next, cost) => some (forget next, cost)

def FiberSafe {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost) (forget : State → Small) : Prop :=
  ∀ s t, forget s = forget t →
    source.observe s = source.observe t ∧
      ∀ a, mapStep forget (source.step a s) = mapStep forget (source.step a t)

def Descends {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost)
    (target : System Small Action Report Cost) (forget : State → Small) : Prop :=
  (∀ s, source.observe s = target.observe (forget s)) ∧
    ∀ a s, mapStep forget (source.step a s) = target.step a (forget s)

/-- Necessary and sufficient local laws for an exact quotient, given a section.
This asks for congruence of the actual forgetting fibers, not merely containment
in a coarser future-observational equivalence. -/
theorem fiber_safe_iff_descent
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost) (forget : State → Small)
    (representative : Small → State) (section_law : ∀ b, forget (representative b) = b) :
    FiberSafe source forget ↔ ∃ target, Descends source target forget := by
  constructor
  · intro safe
    let target : System Small Action Report Cost := {
      observe := fun b => source.observe (representative b)
      step := fun a b => mapStep forget (source.step a (representative b)) }
    refine ⟨target, ?_, ?_⟩
    · intro s
      exact (safe s (representative (forget s)) (section_law (forget s)).symm).1
    · intro a s
      exact (safe s (representative (forget s)) (section_law (forget s)).symm).2 a
  · intro h s t same
    obtain ⟨target, observes, steps⟩ := h
    constructor
    · rw [observes s, observes t, same]
    · intro a
      rw [steps a s, steps a t, same]

/-- An exact quotient has uniquely determined reports and partial transitions.
The conclusion is pointwise, so no function-extensionality axiom is required. -/
theorem descended_structure_unique
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost) (forget : State → Small)
    (representative : Small → State) (section_law : ∀ b, forget (representative b) = b)
    (left right : System Small Action Report Cost)
    (hl : Descends source left forget) (hr : Descends source right forget) :
    (∀ b, left.observe b = right.observe b) ∧
    ∀ a b, left.step a b = right.step a b := by
  constructor
  · intro b
    have h := (hl.1 (representative b)).symm.trans (hr.1 (representative b))
    simpa only [section_law b] using h
  · intro a b
    have h := (hl.2 a (representative b)).symm.trans (hr.2 a (representative b))
    simpa only [section_law b] using h

inductive Trace (Report : Type w) (Cost : Type z) where
  | stop : Report → Trace Report Cost
  | blocked : Report → Trace Report Cost
  | step : Report → Cost → Trace Report Cost → Trace Report Cost

def trace {State : Type u} {Action : Type v} {Report : Type w} {Cost : Type z}
    (system : System State Action Report Cost) : List Action → State → Trace Report Cost
  | [], s => .stop (system.observe s)
  | a :: rest, s => match system.step a s with
    | none => .blocked (system.observe s)
    | some (next, cost) => .step (system.observe s) cost (trace system rest next)

/-- Every finite structural trace, including every intermediate report and cost,
is preserved by exact partial-action descent. -/
theorem finite_trace_preserved
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost)
    (target : System Small Action Report Cost) (forget : State → Small)
    (law : Descends source target forget) (word : List Action) (s : State) :
    trace source word s = trace target word (forget s) := by
  induction word generalizing s with
  | nil => exact congrArg Trace.stop (law.1 s)
  | cons a rest ih =>
    have square := law.2 a s
    cases h : source.step a s with
    | none =>
      have target_none : target.step a (forget s) = none := by
        simpa only [h, mapStep] using square.symm
      simp only [trace, h, target_none, law.1 s]
    | some pair =>
      obtain ⟨next, cost⟩ := pair
      have target_some : target.step a (forget s) = some (forget next, cost) := by
        simpa only [h, mapStep] using square.symm
      simp only [trace, h, target_some, law.1 s, ih next]

/-- Structural enabledness is both preserved and reflected. -/
theorem availability_reflected
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost)
    (target : System Small Action Report Cost) (forget : State → Small)
    (law : Descends source target forget) (a : Action) (s : State) :
    source.step a s = none ↔ target.step a (forget s) = none := by
  have square := law.2 a s
  cases h : source.step a s with
  | none =>
    have target_none : target.step a (forget s) = none := by
      simpa only [h, mapStep] using square.symm
    simp only [target_none, iff_self]
  | some pair =>
    obtain ⟨next, cost⟩ := pair
    have target_some : target.step a (forget s) = some (forget next, cost) := by
      simpa only [h, mapStep] using square.symm
    simp only [target_some, Option.some_ne_none, iff_self]

/-- Any actual quotient transition lifts from EVERY representative, with the
same cost.  Existential lifting from only one representative would be weaker. -/
theorem quotient_step_lifts_from_each_representative
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost)
    (target : System Small Action Report Cost) (forget : State → Small)
    (law : Descends source target forget) (a : Action) (s : State)
    (b : Small) (cost : Cost) (edge : target.step a (forget s) = some (b, cost)) :
    ∃ next, source.step a s = some (next, cost) ∧ forget next = b := by
  have square := (law.2 a s).trans edge
  cases h : source.step a s with
  | none => simp only [h, mapStep] at square; cases square
  | some pair =>
    obtain ⟨next, actualCost⟩ := pair
    have pair_eq : (forget next, actualCost) = (b, cost) := by
      exact Option.some.inj (by simpa only [h, mapStep] using square)
    have cost_eq : actualCost = cost := congrArg Prod.snd pair_eq
    have state_eq := congrArg Prod.fst pair_eq
    exact ⟨next, by rw [cost_eq], state_eq⟩

/-- Finite executable paths retain both final states and every charged cost. -/
def execute {State : Type u} {Action : Type v} {Report : Type w} {Cost : Type z}
    (system : System State Action Report Cost) : List Action → State → Option (State × List Cost)
  | [], s => some (s, [])
  | a :: rest, s => match system.step a s with
    | none => none
    | some (next, cost) => match execute system rest next with
      | none => none
      | some (last, costs) => some (last, cost :: costs)

/-- Whole quotient paths lift from every source representative, not just edges. -/
theorem quotient_path_lifts_from_each_representative
    {State : Type u} {Small : Type q} {Action : Type v}
    {Report : Type w} {Cost : Type z}
    (source : System State Action Report Cost)
    (target : System Small Action Report Cost) (forget : State → Small)
    (law : Descends source target forget) (word : List Action) (s : State)
    (b : Small) (costs : List Cost)
    (path : execute target word (forget s) = some (b, costs)) :
    ∃ last, execute source word s = some (last, costs) ∧ forget last = b := by
  induction word generalizing s b costs with
  | nil =>
    have pair_eq : (forget s, []) = (b, costs) := Option.some.inj path
    have state_eq := congrArg Prod.fst pair_eq
    have costs_eq : [] = costs := congrArg Prod.snd pair_eq
    exact ⟨s, by simp only [execute, ← costs_eq], state_eq⟩
  | cons a rest ih =>
    cases he : target.step a (forget s) with
    | none => simp only [execute, he] at path; cases path
    | some pair =>
      obtain ⟨next, cost⟩ := pair
      obtain ⟨lifted, lifted_edge, lifted_state⟩ :=
        quotient_step_lifts_from_each_representative source target forget law a s next cost he
      cases ht : execute target rest next with
      | none => simp only [execute, he, ht] at path; cases path
      | some tailPair =>
        obtain ⟨last, tailCosts⟩ := tailPair
        have tail_path : execute target rest (forget lifted) = some (last, tailCosts) := by
          simpa only [lifted_state] using ht
        obtain ⟨lifted_last, source_tail, final_state⟩ := ih lifted last tailCosts tail_path
        have pair_eq : (last, cost :: tailCosts) = (b, costs) := by
          exact Option.some.inj (by simpa only [execute, he, ht] using path)
        have last_eq := congrArg Prod.fst pair_eq
        have costs_eq : cost :: tailCosts = costs := congrArg Prod.snd pair_eq
        refine ⟨lifted_last, ?_, final_state.trans last_eq⟩
        simp only [execute, lifted_edge, source_tail, costs_eq]

#print axioms fiber_safe_iff_descent
#print axioms descended_structure_unique
#print axioms finite_trace_preserved
#print axioms availability_reflected
#print axioms quotient_step_lifts_from_each_representative
#print axioms quotient_path_lifts_from_each_representative

end ObservationalSUCC.FutureSafeForgetting
