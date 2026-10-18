import Std.Tactic

/-!
Infinite genuine Gamma boundary program — narrow verified finite algebra.

Lean 4.14, no mathlib, no axioms. This file proves a finite geometric
telescoping law and the authentic Gamma rung spacing. It does NOT prove
Carleman boundedness, essential norm, H01 traces, original S4 or RH.
-/

namespace ObservationalSUCC.InfiniteGammaGeometric

def partialGeom (r : Rat) : Nat → Rat
  | 0 => 0
  | n+1 => partialGeom r n + r ^ n

/-- Finite geometric source kernel telescoping, not an infinite limit. -/
theorem finite_geometric_telescope (r : Rat) (n : Nat) :
    (1-r) * partialGeom r n = 1-r^n := by
  induction n with
  | zero => simp [partialGeom]
  | succ n ih =>
      simp only [partialGeom, pow_succ]
      calc
        (1-r) * (partialGeom r n + r^n) =
            (1-r) * partialGeom r n + (1-r) * r^n := by ring
        _ = (1-r^n) + (1-r) * r^n := by rw [ih]
        _ = 1-r^n*r := by ring

/-- Actual real-Gamma scalar shell spacing alpha_(j+1)-alpha_j=2. -/
def realGammaAlpha (j : Nat) : Rat := (4*j+1 : Nat)/2

theorem real_gamma_rung_spacing (j : Nat) :
    realGammaAlpha (j+1) - realGammaAlpha j = 2 := by
  unfold realGammaAlpha
  push_cast
  ring

end ObservationalSUCC.InfiniteGammaGeometric
