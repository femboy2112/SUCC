import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite real forcing-defect transport core. Pinned Lean 4.14/mathlib.

The norm quantities and their recurrence comparison are explicit hypotheses.
This file proves the weighted square estimate, its exact endpoint budget,
finite summation, and a scalar modulus-loss consequence. It does NOT prove
the complex Fourier comparison, any BBP forcing estimate, an oscillatory
integral limit, a growing-frequency schedule, or pi normality.
-/

open scoped BigOperators

namespace ObservationalSUCC.GlobalSigned

theorem weighted_square_gap (a b : ℝ) :
    17*a^2+272*b^2-(a+16*b)^2 = 16*(a-b)^2 := by
  ring

theorem weighted_square_upper (a b : ℝ) :
    (a+16*b)^2 ≤ 17*a^2+272*b^2 := by
  nlinarith [sq_nonneg (a-b), weighted_square_gap a b]

theorem forcing_defect_square_upper (a b w : ℝ)
    (ha : 0 ≤ a) (hb : 0 ≤ b) (hw : 0 ≤ w) (h : w ≤ a+16*b) :
    w^2 ≤ 17*a^2+272*b^2 := by
  have hs : 0 ≤ a+16*b+w := by linarith
  have hp := mul_nonneg (sub_nonneg.mpr h) hs
  have hsq := weighted_square_upper a b
  nlinarith

theorem adjacent_weighted_energy_identity (u : ℕ → ℝ) (T : ℕ) :
    (∑ i ∈ Finset.range T, (17*(u (i+1))^2+272*(u i)^2)) =
      289*(∑ i ∈ Finset.range (T+1), (u i)^2)
        -17*(u 0)^2-272*(u T)^2 := by
  induction T with
  | zero => simp; ring
  | succ T ih =>
      rw [Finset.sum_range_succ, ih]
      rw [Finset.sum_range_succ (fun i => (u i)^2) (T+1)]
      ring

theorem finite_forcing_defect_transport_with_endpoints
    (u w : ℕ → ℝ) (T : ℕ)
    (hu : ∀ i, i ≤ T → 0 ≤ u i)
    (hw : ∀ i, i < T → 0 ≤ w i)
    (step : ∀ i, i < T → w i ≤ u (i+1)+16*u i) :
    (∑ i ∈ Finset.range T, (w i)^2) ≤
      289*(∑ i ∈ Finset.range (T+1), (u i)^2)
        -17*(u 0)^2-272*(u T)^2 := by
  rw [← adjacent_weighted_energy_identity u T]
  apply Finset.sum_le_sum
  intro i hi
  have hit : i < T := Finset.mem_range.mp hi
  exact forcing_defect_square_upper (u (i+1)) (u i) (w i)
    (hu (i+1) (by omega)) (hu i (by omega)) (hw i hit) (step i hit)

theorem finite_forcing_defect_transport
    (u w : ℕ → ℝ) (T : ℕ)
    (hu : ∀ i, i ≤ T → 0 ≤ u i)
    (hw : ∀ i, i < T → 0 ≤ w i)
    (step : ∀ i, i < T → w i ≤ u (i+1)+16*u i) :
    (∑ i ∈ Finset.range T, (w i)^2) ≤
      289*(∑ i ∈ Finset.range (T+1), (u i)^2) := by
  have h := finite_forcing_defect_transport_with_endpoints u w T hu hw step
  nlinarith [sq_nonneg (u 0), sq_nonneg (u T)]

theorem phase_modulus_from_forcing_loss (length magnitude forceLoss : ℝ)
    (transport : forceLoss ≤ 289*(length-magnitude)) :
    magnitude ≤ length-forceLoss/289 := by
  linarith

theorem coefficient_288_fails_constant_control :
    (289:ℝ)*289 > 288*(289+1) := by
  norm_num

theorem quiet_transition_scale_bound (T : ℝ) (hT : 20000 ≤ T) :
    2 ≤ (1/100:ℝ)^2*T := by
  nlinarith

theorem local_cosine_rational_coefficient :
    (2:ℝ)*(157/50)^2-(2/3)*(22/7)^4/112 = 1206224729/63026250 ∧
    (1206224729:ℝ)/63026250 > 19 := by
  norm_num

theorem quiet_branch_loss_lower (Q D R u : ℝ) (hu : 0 ≤ u)
    (energy : 19*Q ≤ D)
    (gap : (1-R)^2 ≤ 257*Q*(1+u)^2) :
    19*(1-R)^2/(257*(1+u)^2) ≤ D := by
  have hd : 0 < 257*(1+u)^2 := by positivity
  apply (div_le_iff₀ hd).mpr
  calc
    19*(1-R)^2 ≤ 19*(257*Q*(1+u)^2) :=
      mul_le_mul_of_nonneg_left gap (by norm_num)
    _ = (19*Q)*(257*(1+u)^2) := by ring
    _ ≤ D*(257*(1+u)^2) := mul_le_mul_of_nonneg_right energy (le_of_lt hd)

theorem quiet_branch_exact_margin :
    (19:ℝ)*(4081/4096)^2/(257*(101/100)^2)-1/14 =
      9907077909/19243046273024 ∧
    (9907077909:ℝ)/19243046273024 > 0 := by
  norm_num

theorem quiet_branch_scalar_contradiction (Q D R : ℝ)
    (range : R ≤ 15/4096) (loss : D ≤ 1/14)
    (energy : 19*Q ≤ D)
    (gap : (1-R)^2 ≤ 257*Q*(101/100)^2) : False := by
  have hlow : 0 ≤ (1-R)-(4081/4096:ℝ) := by linarith
  have hsum : 0 ≤ (1-R)+(4081/4096:ℝ) := by linarith
  have hprod := mul_nonneg hlow hsum
  have hmargin := quiet_branch_exact_margin
  have hlower := quiet_branch_loss_lower Q D R (1/100) (by norm_num) energy
    (by convert gap using 1 <;> norm_num)
  norm_num at hlower hmargin
  nlinarith

end ObservationalSUCC.GlobalSigned

#print axioms ObservationalSUCC.GlobalSigned.weighted_square_gap
#print axioms ObservationalSUCC.GlobalSigned.weighted_square_upper
#print axioms ObservationalSUCC.GlobalSigned.forcing_defect_square_upper
#print axioms ObservationalSUCC.GlobalSigned.adjacent_weighted_energy_identity
#print axioms ObservationalSUCC.GlobalSigned.finite_forcing_defect_transport_with_endpoints
#print axioms ObservationalSUCC.GlobalSigned.finite_forcing_defect_transport
#print axioms ObservationalSUCC.GlobalSigned.phase_modulus_from_forcing_loss
#print axioms ObservationalSUCC.GlobalSigned.coefficient_288_fails_constant_control
#print axioms ObservationalSUCC.GlobalSigned.quiet_transition_scale_bound
#print axioms ObservationalSUCC.GlobalSigned.local_cosine_rational_coefficient
#print axioms ObservationalSUCC.GlobalSigned.quiet_branch_loss_lower
#print axioms ObservationalSUCC.GlobalSigned.quiet_branch_exact_margin
#print axioms ObservationalSUCC.GlobalSigned.quiet_branch_scalar_contradiction
