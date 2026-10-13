/-!
Independent RA audit of deterministic all-word repair.
Lean 4.14 core only; no mathlib, axioms, sorry or finite-state assumption.
Action is a COMMON alphabet; step maps are TOTAL and f intertwines EVERY action.
The base-change result assumes neither surjectivity nor injectivity of f,
and does not require reports at all. Repair is defined for arbitrary relations.
-/
namespace IndependentRepairAudit

universe u v w

def Run {X : Type u} {A : Type w} (T : A → X → X) : List A → X → X
  | [], x => x
  | a :: rest, x => Run T rest (T a x)

def Repair {X : Type u} {A : Type w} (T : A → X → X)
    (R : X → X → Prop) (x y : X) : Prop :=
  ∀ word : List A, R (Run T word x) (Run T word y)

def Pullback {X : Type u} {Y : Type v} (f : X → Y)
    (R : Y → Y → Prop) (x y : X) : Prop := R (f x) (f y)

def Stable {X : Type u} {A : Type w} (T : A → X → X)
    (R : X → X → Prop) : Prop :=
  ∀ a x y, R x y → R (T a x) (T a y)

def Subrelation {X : Type u} (R S : X → X → Prop) : Prop :=
  ∀ x y, R x y → S x y

theorem run_intertwines {X : Type u} {Y : Type v} {A : Type w}
    (TX : A → X → X) (TY : A → Y → Y) (f : X → Y)
    (strict : ∀ a x, f (TX a x) = TY a (f x)) :
    ∀ word x, f (Run TX word x) = Run TY word (f x) := by
  intro word
  induction word with
  | nil => intro x; rfl
  | cons a rest ih =>
      intro x
      change f (Run TX rest (TX a x)) = Run TY rest (TY a (f x))
      rw [ih (TX a x), strict a x]

/-- Pointwise equality of the two reindexed relations, for ALL finite words. -/
theorem repair_base_change {X : Type u} {Y : Type v} {A : Type w}
    (TX : A → X → X) (TY : A → Y → Y) (f : X → Y)
    (strict : ∀ a x, f (TX a x) = TY a (f x))
    (R : Y → Y → Prop) (x y : X) :
    Repair TX (Pullback f R) x y ↔ Pullback f (Repair TY R) x y := by
  change (∀ word, R (f (Run TX word x)) (f (Run TX word y))) ↔
    (∀ word, R (Run TY word (f x)) (Run TY word (f y)))
  constructor
  · intro h word
    simpa only [run_intertwines TX TY f strict] using h word
  · intro h word
    simpa only [run_intertwines TX TY f strict] using h word

theorem repair_deflationary {X : Type u} {A : Type w}
    (T : A → X → X) (R : X → X → Prop) :
    Subrelation (Repair T R) R := by
  intro x y h
  exact h []

theorem repair_stable {X : Type u} {A : Type w}
    (T : A → X → X) (R : X → X → Prop) : Stable T (Repair T R) := by
  intro a x y h word
  exact h (a :: word)

theorem stable_under_words {X : Type u} {A : Type w}
    (T : A → X → X) (E : X → X → Prop) (stable : Stable T E)
    (x y : X) (related : E x y) :
    ∀ word, E (Run T word x) (Run T word y) := by
  intro word
  induction word generalizing x y with
  | nil => exact related
  | cons a rest ih => exact ih (T a x) (T a y) (stable a x y related)

/-- Right-adjoint law on relation inclusion; restrict to equivalences for Eq(X). -/
theorem repair_coreflection {X : Type u} {A : Type w}
    (T : A → X → X) (E R : X → X → Prop) (stable : Stable T E) :
    Subrelation E R ↔ Subrelation E (Repair T R) := by
  constructor
  · intro inclusion x y related word
    exact inclusion _ _ (stable_under_words T E stable x y related word)
  · intro inclusion x y related
    exact repair_deflationary T R x y (inclusion x y related)

theorem repair_preserves_equivalence {X : Type u} {A : Type w}
    (T : A → X → X) (R : X → X → Prop) (eqv : Equivalence R) :
    Equivalence (Repair T R) := by
  constructor
  · intro x word
    exact eqv.refl (Run T word x)
  · intro x y h word
    exact eqv.symm (h word)
  · intro x y z hxy hyz word
    exact eqv.trans (hxy word) (hyz word)

theorem repair_idempotent {X : Type u} {A : Type w}
    (T : A → X → X) (R : X → X → Prop) (x y : X) :
    Repair T (Repair T R) x y ↔ Repair T R x y := by
  constructor
  · exact repair_deflationary T (Repair T R) x y
  · intro h
    exact (repair_coreflection T (Repair T R) (Repair T R) (repair_stable T R)).mp
      (fun _ _ same => same) x y h

end IndependentRepairAudit

#print axioms IndependentRepairAudit.repair_base_change
#print axioms IndependentRepairAudit.repair_coreflection
#print axioms IndependentRepairAudit.repair_preserves_equivalence
