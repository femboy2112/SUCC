import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite quadratic and rational core of the Oily branch-coercivity argument.
Pinned Lean/mathlib 4.14.0. These declarations check the coefficient norms,
the sharp quadratic inequalities, and the numerical contradiction margin.

The complex chord inequality, integer-branch construction, BBP source,
irrationality measure input, infinite block count and normality are NOT
formalized here. In particular the energy and gap premises below must be
proved by the paper argument; a source label does not discharge them.
-/

namespace ObservationalSUCC.OilyBranchCoercivity

theorem coefficient_norms :
    (16 : ℝ)^2 + 17^2 + 1^2 = 546 ∧
    16^2 + 1^2 + 16^2 + (1 : ℝ)^2 = 514 := by
  norm_num

theorem adjacent_branch_quadratic (a b c : ℝ) :
    (16*a - 17*b + c)^2 ≤ 546*(a^2+b^2+c^2) := by
  nlinarith [sq_nonneg (17*a+16*b), sq_nonneg (a-16*c),
    sq_nonneg (b+17*c)]

theorem separated_branch_quadratic (a b c d : ℝ) :
    (16*a-b-16*c+d)^2 ≤ 514*(a^2+b^2+c^2+d^2) := by
  nlinarith [sq_nonneg (a+16*b), sq_nonneg (16*a+16*c),
    sq_nonneg (a-16*d), sq_nonneg (16*b-c),
    sq_nonneg (b+d), sq_nonneg (c+16*d)]

theorem loss_implies_small_phase (q loss : ℝ)
    (budget : 8*q^2 ≤ loss) (small : loss ≤ 1/29) :
    q^2 < (1/15 : ℝ)^2 := by
  nlinarith

theorem trigonometric_rational_margin :
    2*(25/8 : ℝ)^2 - (2/3)*(22/7)^4/225 = 997929491/51861600 ∧
    (19 : ℝ) < 997929491/51861600 := by
  norm_num

theorem branch_rational_margin :
    (19 : ℝ)*(4081/4096)^2/546 - 1/29 = 2329025/37950062592 ∧
    (0 : ℝ) < 2329025/37950062592 := by
  norm_num

theorem gap_energy_forces_loss (energy loss : ℝ)
    (gap : (4081/4096 : ℝ)^2 ≤ 546*energy)
    (cost : 19*energy ≤ loss) :
    (1/29 : ℝ) < loss := by
  have margin : (546 : ℝ)/29 < 19*(4081/4096)^2 := by norm_num
  nlinarith

theorem adjacent_gap_forces_loss (a b c loss : ℝ)
    (gap : (4081/4096 : ℝ)^2 ≤ (16*a-17*b+c)^2)
    (cost : 19*(a^2+b^2+c^2) ≤ loss) :
    (1/29 : ℝ) < loss := by
  apply gap_energy_forces_loss (a^2+b^2+c^2) loss
  · exact le_trans gap (adjacent_branch_quadratic a b c)
  · exact cost

theorem separated_gap_forces_loss (a b c d loss : ℝ)
    (gap : (4081/4096 : ℝ)^2 ≤ (16*a-b-16*c+d)^2)
    (cost : 19*(a^2+b^2+c^2+d^2) ≤ loss) :
    (1/29 : ℝ) < loss := by
  apply gap_energy_forces_loss (a^2+b^2+c^2+d^2) loss
  · have quad := separated_branch_quadratic a b c d
    nlinarith [sq_nonneg a, sq_nonneg b, sq_nonneg c, sq_nonneg d]
  · exact cost

end ObservationalSUCC.OilyBranchCoercivity
