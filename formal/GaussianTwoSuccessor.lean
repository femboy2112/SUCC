import Std.Tactic

/-!
Verified narrow SUCC/Gaussian exact facts in Lean 4.14, no Mathlib.
No assertion that S^2 equals Gaussian multiplication, and no
formalization of Weil half-density or the infinite Suzuki Schur problem.
-/
namespace ObservationalSUCC.GaussianTwoSuccessor

/-- Peano 2 is the second iterate after the zero source. -/
theorem two_successor_from_zero :
    Nat.succ (Nat.succ 0) = 2 := by rfl

/-- Multiplying x+iy by 1+i on the Gaussian lattice. -/
def gaussianStep (x y : Int) : Int × Int :=
  (x-y,x+y)

/-- Two Gaussian multiplicative steps rotate by a quarter turn and scale 2. -/
theorem gaussian_step_twice (x y : Int) :
    gaussianStep (gaussianStep x y).1 (gaussianStep x y).2 =
      (-2*y,2*x) := by
  simp only [gaussianStep]
  apply Prod.ext <;> omega

/-- The Gaussian prime 1+i has norm 2. -/
theorem first_gaussian_norm_two :
    (1:Int)*(1:Int)+(1:Int)*(1:Int)=2 := by decide

/-- No identificaton of additive SUCC^2 with (1+i)^2 is allowed. -/
theorem different_two_step_targets :
    gaussianStep (gaussianStep 1 0).1 (gaussianStep 1 0).2
      ≠ (2,0) := by
  decide

end ObservationalSUCC.GaussianTwoSuccessor
