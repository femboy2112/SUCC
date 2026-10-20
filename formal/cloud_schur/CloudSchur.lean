import Mathlib.LinearAlgebra.Matrix.SchurComplement
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
Classical finite Schur theory, pinned to Lean/mathlib 4.14.0.
This wrapper invokes an actual mathlib theorem, not caller-supplied metadata.
The rational elimination algorithm is separately paper-proved and executable;
this file does not claim a full formal refinement proof of its Python code.
-/

set_option autoImplicit false

namespace ObservationalSUCC.CloudSchur

open Matrix

/-- Finite real Schur equivalence. Positive definiteness of D supplies its inverse. -/
theorem finite_schur_psd_iff {m n : Nat}
    (A : Matrix (Fin m) (Fin m) ℝ) (B : Matrix (Fin m) (Fin n) ℝ)
    (D : Matrix (Fin n) (Fin n) ℝ) (hD : D.PosDef) :
    (Matrix.fromBlocks A B B.conjTranspose D).PosSemidef ↔
      (A - B * D⁻¹ * B.conjTranspose).PosSemidef := by
  letI := hD.isUnit.invertible
  exact Matrix.PosSemidef.fromBlocks₂₂ A B hD

/-- A Hermitian real matrix failing PSD has an actual negative direction. -/
theorem finite_negative_direction {n : Nat}
    (M : Matrix (Fin n) (Fin n) ℝ) (hM : M.IsHermitian)
    (hn : ¬ M.PosSemidef) :
    ∃ x : Fin n → ℝ, star x ⬝ᵥ (M *ᵥ x) < 0 := by
  by_contra h
  apply hn
  refine ⟨hM, ?_⟩
  intro x
  exact le_of_not_gt (fun hx => h ⟨x, hx⟩)

/-- Exact rational square completion, with an explicit nonzero denominator. -/
theorem scalar_schur_identity (a b d x y : ℚ) (hd : d ≠ 0) :
    a*x*x + 2*b*x*y + d*y*y =
      d*(y + b*x/d)^2 + (a - b*b/d)*x*x := by
  field_simp [hd]
  <;> ring

/-- A negative rational Schur direction lifts without approximation. -/
theorem scalar_negative_lift (a b d x : ℚ) (hd : d ≠ 0)
    (h : (a - b*b/d)*x*x < 0) :
    a*x*x + 2*b*x*(-(b*x/d)) + d*(-(b*x/d))*(-(b*x/d)) < 0 := by
  rw [scalar_schur_identity a b d x (-(b*x/d)) hd]
  simpa using h

/-- A zero diagonal with a nonzero coupling gives q(v) = -1 exactly. -/
theorem zero_diagonal_negative (b c : ℚ) (hb : b ≠ 0) :
    2*b*(-((c+1)/(2*b))) + c = -1 := by
  field_simp [hb]
  <;> ring

#print axioms finite_schur_psd_iff
#print axioms finite_negative_direction
#print axioms scalar_schur_identity
#print axioms scalar_negative_lift
#print axioms zero_diagonal_negative

end ObservationalSUCC.CloudSchur
