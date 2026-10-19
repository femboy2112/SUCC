import Std.Tactic

/-!
Infinite real-Gamma source: narrow proof-kernel algebra (Lean 4.14, no Mathlib).
Only the original rung-index arithmetic and recursive finite geometric prefix
are formalized. Closed geometric ratio, Carleman, H01 and essential norm are
PAPER/EXACT Fraction claims, NOT Lean formalizations. No axioms/sorry.
-/
namespace ObservationalSUCC.InfiniteGammaGeometric

/-- Frozen real Gamma has denominator d_j=4*j+1. -/
def originalGammaDenominator (j : Nat) : Nat := 4*j+1

theorem original_gamma_spacing (j : Nat) :
    originalGammaDenominator (j+1) =
      originalGammaDenominator j + 4 := by
  unfold originalGammaDenominator
  omega

theorem original_gamma_strict_order (i j : Nat) (h : i < j) :
    originalGammaDenominator i < originalGammaDenominator j := by
  unfold originalGammaDenominator
  omega

theorem original_gamma_no_level_collision (i j : Nat)
    (h : originalGammaDenominator i = originalGammaDenominator j) :
    i = j := by
  unfold originalGammaDenominator at h
  omega

/-- Finite geometric prefix recursion, a small exact proof-kernel check. -/
def partialGeom (r : Nat) : Nat → Nat
  | 0 => 0
  | n+1 => partialGeom r n + r^n

theorem finite_geometric_successor (r n : Nat) :
    partialGeom r (n+1) = partialGeom r n + r^n := by
  rfl

end ObservationalSUCC.InfiniteGammaGeometric
