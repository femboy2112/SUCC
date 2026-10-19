import FutureSafeForgetting
import InstituteCausal

/-!
Semantic adapter between the pinned PR179 and PR178 formal interfaces.
Compile using scripts/verify_forge_formal.py, which builds exact dependencies
in a temporary module directory. No historical source or toolchain is changed.
PR178 labelled runs omit current reports and collapse failed prefixes to none.
PR179 execute shares that failure policy; PR179 trace retains failed prefixes.
The adapter preserves the former and explicitly separates the latter.
-/
set_option autoImplicit false
namespace ObservationalSUCC.ForgeQuotientAdapters
universe u v w z q

def swap {X : Type u} {Y : Type v} : Option (X × Y) → Option (Y × X)
  | none => none
  | some (x, y) => some (y, x)

theorem swap_involutive {X : Type u} {Y : Type v} (p : Option (X × Y)) :
    swap (swap p) = p := by
  cases p with
  | none => rfl
  | some p => cases p; rfl

theorem swap_injective {X : Type u} {Y : Type v}
    {p r : Option (X × Y)} (same : swap p = swap r) : p = r := by
  have h := congrArg swap same
  rw [swap_involutive, swap_involutive] at h
  exact h

def adapt {S : Type u} {A : Type v} {O : Type w} {C : Type z}
    (system : FutureSafeForgetting.System S A O C) (s : S) (a : A) : Option (C × S) :=
  swap (system.step a s)

theorem project_adapt {S : Type u} {Q : Type q} {A : Type v}
    {O : Type w} {C : Type z}
    (system : FutureSafeForgetting.System S A O C) (forget : S → Q) (s : S) (a : A) :
    InstituteCausal.project forget (adapt system s a) = swap (FutureSafeForgetting.mapStep forget (system.step a s)) := by
  unfold adapt
  cases h : system.step a s with
  | none => rfl
  | some p => cases p; rfl

/-- Current report agreement is an essential additional condition. -/
theorem fiber_safe_iff_label_congruence {S : Type u} {Q : Type q}
    {A : Type v} {O : Type w} {C : Type z}
    (system : FutureSafeForgetting.System S A O C) (forget : S → Q) :
    FutureSafeForgetting.FiberSafe system forget ↔
      (∀ s t, forget s = forget t → system.observe s = system.observe t) ∧
      InstituteCausal.FiberCongruent forget (adapt system) := by
  constructor
  · intro safe
    constructor
    · intro s t same; exact (safe s t same).1
    · intro s t same a
      rw [project_adapt, project_adapt]
      exact congrArg swap ((safe s t same).2 a)
  · intro compatible s t same
    refine ⟨compatible.1 s t same, ?_⟩
    intro a
    apply swap_injective
    rw [← project_adapt, ← project_adapt]
    exact compatible.2 s t same a

/-- PR178 run agrees exactly with PR179 execute after swapping the pair order.
This makes no false claim of equality with the richer PR179 trace. -/
theorem successful_run_compatibility {S : Type u} {A : Type v}
    {O : Type w} {C : Type z}
    (system : FutureSafeForgetting.System S A O C) (word : List A) (s : S) :
    InstituteCausal.run (adapt system) word s = swap (FutureSafeForgetting.execute system word s) := by
  induction word generalizing s with
  | nil => rfl
  | cons a rest ih =>
    simp only [InstituteCausal.run, adapt, FutureSafeForgetting.execute]
    cases h : system.step a s with
    | none => rfl
    | some p =>
      obtain ⟨next, cost⟩ := p
      simp only [swap, ih]
      cases htail : FutureSafeForgetting.execute system rest next with
      | none => rfl
      | some p => cases p; rfl

def silent : FutureSafeForgetting.System Bool Unit Bool Nat := {
  observe := fun s => s
  step := fun _ _ => none }

/-- A report-free transition system cannot certify preservation of observations. -/
theorem label_congruence_does_not_preserve_current_report :
    InstituteCausal.FiberCongruent (fun _ : Bool => ()) (adapt silent) ∧
    ¬ FutureSafeForgetting.FiberSafe silent (fun _ : Bool => ()) := by
  constructor
  · intro s t same a; rfl
  · intro safe
    have impossible : false = true := (safe false true rfl).1
    cases impossible

def charged : FutureSafeForgetting.System Nat Unit Unit Nat := {
  observe := fun _ => ()
  step := fun _ s => match s with
    | 0 => some (2, 1)
    | 1 => some (2, 2)
    | _ => none }

/-- Equality of collapsed failures loses earlier cost receipts. -/
theorem failed_runs_can_hide_different_traces :
    InstituteCausal.run (adapt charged) [(), ()] 0 = InstituteCausal.run (adapt charged) [(), ()] 1 ∧
    FutureSafeForgetting.trace charged [(), ()] 0 ≠ FutureSafeForgetting.trace charged [(), ()] 1 := by
  constructor
  · rfl
  · intro same
    cases same

#print axioms swap_involutive
#print axioms swap_injective
#print axioms project_adapt
#print axioms fiber_safe_iff_label_congruence
#print axioms successful_run_compatibility
#print axioms label_congruence_does_not_preserve_current_report
#print axioms failed_runs_can_hide_different_traces
end ObservationalSUCC.ForgeQuotientAdapters
