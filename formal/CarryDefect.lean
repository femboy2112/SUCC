import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
Finite signed endpoint, modal-count, and periodic-terminal algebra only.
No circle lifts, BBP source bound, Green inverse, complex norm, irrationality
measure, selected count growth, or analytic limit is formalized here.
-/

open scoped BigOperators
namespace ObservationalSUCC.CarryDefect

theorem signed_endpoint_identity (q : ℕ → ℝ) (T : ℕ) :
    289*(∑ i ∈ Finset.range (T+1), (q i)^2)
      -17*(q 0)^2-272*(q T)^2
      -(∑ i ∈ Finset.range T, (q (i+1)-16*q i)^2) =
    16*(∑ i ∈ Finset.range T, (q (i+1)+q i)^2) := by
  induction T with
  | zero => simp; ring
  | succ T ih =>
      rw [Finset.sum_range_succ (fun i => (q i)^2) (T+1)]
      rw [Finset.sum_range_succ (fun i => (q (i+1)-16*q i)^2)]
      rw [Finset.sum_range_succ (fun i => (q (i+1)+q i)^2)]
      nlinarith [ih]

theorem modal_pair_budget (counts : ℕ → ℝ) (labels : ℕ) (T M : ℝ)
    (nonnegative : ∀ i ∈ Finset.range labels, 0 ≤ counts i)
    (modal : ∀ i ∈ Finset.range labels, counts i ≤ M)
    (total : ∑ i ∈ Finset.range labels, counts i = T) :
    T*(T-M) ≤ T^2-(∑ i ∈ Finset.range labels, (counts i)^2) := by
  have hsum : (∑ i ∈ Finset.range labels, (counts i)^2) ≤
      ∑ i ∈ Finset.range labels, M*counts i := by
    apply Finset.sum_le_sum
    intro i hi
    have hprod := mul_nonneg (nonnegative i hi) (sub_nonneg.mpr (modal i hi))
    nlinarith
  rw [← Finset.mul_sum, total] at hsum
  nlinarith

theorem modal_loss_lower (T Q D R C K : ℝ) (hT : 0 < T)
    (pairs : T*K ≤ 2*C)
    (separation : (1-R)^2*C ≤ 289*T*Q)
    (chord : 8*Q ≤ D) :
    (4/289:ℝ)*(1-R)^2*K ≤ D := by
  have hp := mul_le_mul_of_nonneg_left pairs (sq_nonneg (1-R))
  have hcancel : (1-R)^2*K ≤ 578*Q := by
    apply (mul_le_mul_left hT).mp
    nlinarith [hp, separation]
  linarith

theorem periodic_terminal_identity (B z0 zT q0 qT forcing : ℝ)
    (recurrence : zT = B*z0+forcing)
    (difference : zT-z0 = qT-q0) :
    (B-1)*zT = B*(qT-q0)-forcing := by
  rw [← difference]
  nlinarith [recurrence]

end ObservationalSUCC.CarryDefect
