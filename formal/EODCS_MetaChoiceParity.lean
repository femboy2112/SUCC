/-!
# EODCS Meta Choice and Parity Obstruction (Lean 4.14.0, no mathlib)

Tiny kernel-level calibrations, independent of any imported theorem:
1. When dependent witness *data* are given, choice is projection, not an axiom.
2. Every vertex of a parity-flip relation has an admissible local choice.
3. An odd triangle of three flips has NO global assignment.
4. The even triangle (two flips and an identity edge) is inhabited.

These theorems are NOT full topos choice or non-Boolean internal logic, not
an arbitrary-graph cohomology formalization, and not an empirical claim.
-/

namespace ObservationalSUCC
namespace MetaChoice

universe u v

/-- Witnessed dependent choice: the selector is literally the first field
of supplied dependent witness data. No `Classical.choose` is used. -/
theorem witnessed_dependent_choice
    {X : Type u} {Y : X → Type v}
    (R : (x : X) → Y x → Prop)
    (witness : (x : X) → {y : Y x // R x y}) :
    {f : (x : X) → Y x // ∀ x, R x (f x)} := by
  refine ⟨(fun x => (witness x).1), ?_⟩
  intro x
  exact (witness x).2

/-- A single flip can always be chosen locally. -/
theorem flip_local_witness : ∀ a : Bool, ∃ b : Bool, b = !a := by
  intro a
  exact ⟨!a, rfl⟩

/-- All three edge laws are individually solvable. This is NOT a
compatible triple of choices. -/
theorem every_triangle_edge_is_locally_solvable :
    (∀ a : Bool, ∃ b : Bool, b = !a) ∧
    (∀ b : Bool, ∃ c : Bool, c = !b) ∧
    (∀ c : Bool, ∃ a : Bool, a = !c) := by
  exact ⟨flip_local_witness, flip_local_witness, flip_local_witness⟩

/-- An odd cycle with three flips cannot support a global section.
This is an eight-case finite theorem, not an inference from simulations. -/
theorem odd_triangle_has_no_global_section :
    ¬ (∃ a b c : Bool,
      b = !a ∧ c = !b ∧ a = !c) := by
  rintro ⟨a, b, c, hab, hbc, hca⟩
  cases a <;> cases b <;> cases c <;> simp_all

/-- The parity-even control has an explicit global section. -/
theorem even_triangle_has_global_section :
    ∃ a b c : Bool, b = !a ∧ c = !b ∧ a = c := by
  exact ⟨false, true, false, rfl, rfl, rfl⟩

end MetaChoice
end ObservationalSUCC
