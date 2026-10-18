import Std.Tactic

/-!
Finite source algebra for the infinite real-Gamma Carleman program.
Lean 4.14 core + Std, without Mathlib, sorry, axioms or ring tactic.
The continuous strong-limit and essential-norm theorem is PAPER PROVED,
NOT formalized by this file.
-/
namespace ObservationalSUCC.InfiniteGammaGeometric

def partialGeom (r : Int) : Nat → Int
  | 0 => 0
  | n+1 => partialGeom r n + r^n

/-- Exact finite geometric cancellation in Int, without infinite limits. -/
theorem finite_geometric_telescope (r : Int) (n : Nat) :
    (1-r) * partialGeom r n = 1-r^n := by
  induction n with
  | zero =>
      simp [partialGeom]
  | succ n ih =>
      change (1-r)*(partialGeom r n+r^n) = 1-r^(n+1)
      rw [mul_add, ih, pow_succ]
      rw [sub_mul, one_mul, mul_comm r (r^n)]
      omega

/-- Actual first-real-Gamma shells have d_j=4j+1, gap exactly four.
    Dividing these d_j by two yields real exponential alpha spacing two. -/
def originalGammaD (j : Nat) : Nat := 4*j+1

theorem original_gamma_d_gap (j : Nat) :
    originalGammaD (j+1) = originalGammaD j+4 := by
  unfold originalGammaD
  omega

end ObservationalSUCC.InfiniteGammaGeometric
