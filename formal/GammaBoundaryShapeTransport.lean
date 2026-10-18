import Std.Tactic
/-!
Transported FORM does not imply unchanged VALUES. Lean 4.14 core+Std.
Only this finite algebraic kernel fact is formalized here.
This file does not claim a Lean proof of continuous OU operator rank,
original source provenance, first-window S4 or RH.
-/

namespace ObservationalSUCC.GammaBoundaryShapeTransport

universe u

def DifferenceForm {A : Type u} (profile : Int → A)
    (x y : Int) : A := profile (x-y)

/-- A difference kernel has EXACT form covariance under common transport. -/
theorem difference_form_covariant {A : Type u}
    (profile : Int → A) (x y displacement : Int) :
    DifferenceForm profile (x+displacement) (y+displacement) =
    DifferenceForm profile x y := by
  change profile ((x+displacement)-(y+displacement)) = profile (x-y)
  have h : (x+displacement)-(y+displacement)=x-y := by omega
  rw [h]

/-- Moving ONE argument can change a value without violating form transport. -/
theorem moving_one_coordinate_changes_value :
    DifferenceForm (fun z : Int => z) 0 0 ≠
    DifferenceForm (fun z : Int => z) 0 1 := by
  decide

end ObservationalSUCC.GammaBoundaryShapeTransport
