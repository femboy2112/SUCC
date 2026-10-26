import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity

/-!
Finite odd-carrier obstruction core. Pinned Lean 4.14/mathlib.

Kernel scope: odd-residue units, inverse-branch uniqueness, affine injection,
permutation norm preservation, and the exact deterministic branch defect.
The BBP odd-denominator induction, rational-resolution threshold and analytic
non-normality/normality statements are NOT formalized in this file.
-/

open scoped BigOperators

namespace ObservationalSUCC.SelectedBranch

theorem odd_unit_mod_sixteen (q : ℕ) (hq : Odd q) : IsUnit (q : ZMod 16) := by
  apply (ZMod.isUnit_iff_coprime q 16).mpr
  have h := hq.coprime_two_right.pow_right 4
  norm_num at h
  exact h

theorem sixteen_unit_mod_odd (q : ℕ) (hq : Odd q) : IsUnit (16 : ZMod q) := by
  apply (ZMod.isUnit_iff_coprime 16 q).mpr
  have h := hq.coprime_two_left.pow_left 4
  norm_num at h
  exact h

theorem odd_inverse_digit_unique (q : ℕ) (hq : Odd q) (a j k : ZMod 16)
    (hj : (q : ZMod 16)*j+a=0) (hk : (q : ZMod 16)*k+a=0) : j=k := by
  apply (odd_unit_mod_sixteen q hq).mul_left_cancel
  exact add_right_cancel (hj.trans hk.symm)

theorem odd_affine_step_injective (q : ℕ) (hq : Odd q) (r : ZMod q) :
    Function.Injective (fun x : ZMod q => 16*x+r) := by
  intro x y h
  apply (sixteen_unit_mod_odd q hq).mul_left_cancel
  exact add_right_cancel h

theorem permutation_squared_norm {ι : Type*} [Fintype ι]
    (p : Equiv.Perm ι) (f : ι → ℝ) :
    (∑ x, (f (p x))^2) = ∑ x, (f x)^2 := by
  exact Equiv.sum_comp p (fun x => (f x)^2)

theorem deterministic_row_defect (j : Fin 16) :
    (16:ℝ)*(∑ k : Fin 16, (if k=j then (1:ℝ) else 0)^2)-1=15 := by
  simp
  norm_num

theorem deterministic_mixture_defect {ι : Type*} [Fintype ι]
    (weight : ι → ℝ) (mass : ∑ b, weight b=1) :
    (∑ b, weight b*15)=15 := by
  rw [← Finset.sum_mul, mass]
  ring

theorem unit_mod_sixteen_is_necessary_control :
    ((2:ZMod 16)*0+0=(2:ZMod 16)*8+0) ∧ (0:ZMod 16) ≠ 8 := by
  decide

theorem parity_perspective_lipschitz (s t n : ℝ) (hn : 0 < n)
    (hs : |s| ≤ n) (ht : |t| ≤ n) :
    |s^2/n-t^2/n| ≤ 2*|s-t| := by
  have hsum : |s+t| ≤ 2*n := by
    calc
      |s+t| ≤ |s|+|t| := abs_add s t
      _ ≤ 2*n := by linarith
  have factor : s^2/n-t^2/n = (s-t)*(s+t)/n := by ring
  rw [factor, abs_div, abs_mul, abs_of_pos hn]
  apply (div_le_iff₀ hn).mpr
  calc
    |s-t| * |s+t| ≤ |s-t| * (2*n) :=
      mul_le_mul_of_nonneg_left hsum (abs_nonneg _)
    _ = 2 * |s-t| * n := by ring

theorem critical_scale_polynomial_positive (m : ℝ) (hm : 0 ≤ m) :
    0 < 448*m^4+1976*m^3+2904*m^2+1478*m+87 := by
  positivity

end ObservationalSUCC.SelectedBranch

#print axioms ObservationalSUCC.SelectedBranch.odd_unit_mod_sixteen
#print axioms ObservationalSUCC.SelectedBranch.sixteen_unit_mod_odd
#print axioms ObservationalSUCC.SelectedBranch.odd_inverse_digit_unique
#print axioms ObservationalSUCC.SelectedBranch.odd_affine_step_injective
#print axioms ObservationalSUCC.SelectedBranch.permutation_squared_norm
#print axioms ObservationalSUCC.SelectedBranch.deterministic_row_defect
#print axioms ObservationalSUCC.SelectedBranch.deterministic_mixture_defect
#print axioms ObservationalSUCC.SelectedBranch.unit_mod_sixteen_is_necessary_control
#print axioms ObservationalSUCC.SelectedBranch.parity_perspective_lipschitz
#print axioms ObservationalSUCC.SelectedBranch.critical_scale_polynomial_positive
