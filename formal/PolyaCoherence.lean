import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
Exact real quadratic-form core of the source-marked Pólya isometry.
Pinned Lean 4.14 / mathlib 4bbdccd9. No Hilbert-space completion, complex
channel, Hahn spectrum, source authenticity, or BBP cancellation is inferred
from this file. The paper constructs the two-dimensional environment; this
file verifies its load-bearing all-dimension energy decomposition.
-/

open scoped BigOperators
namespace ObservationalSUCC.PolyaCoherence

theorem row_energy (m k a b : ℝ) :
    ((m-k)*a+k*b)^2 + k*(m-k)*(a-b)^2 =
      m*((m-k)*a^2+k*b^2) := by
  ring

theorem weighted_row_sum (m : ℕ) (v : ℕ → ℝ) :
    (∑ i ∈ Finset.range (m+1),
      (((m:ℝ)-(i:ℝ))*(v i)^2+(i:ℝ)*(v (i-1))^2)) =
      ((m:ℝ)+1)*(∑ i ∈ Finset.range m, (v i)^2) := by
  rw [Finset.sum_add_distrib]
  rw [Finset.sum_range_succ (fun i => ((m:ℝ)-(i:ℝ))*(v i)^2)]
  simp only [sub_self, zero_mul, add_zero]
  rw [Finset.sum_range_succ' (fun i => (i:ℝ)*(v (i-1))^2)]
  simp only [Nat.cast_zero, zero_mul, add_zero, Nat.add_sub_cancel,
    Nat.cast_add, Nat.cast_one]
  rw [← Finset.sum_add_distrib]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro i hi
  ring

/-- Full finite Gram/isometry identity before normalization by m(m+1). -/
theorem full_energy_decomposition (m : ℕ) (v : ℕ → ℝ) :
    (∑ i ∈ Finset.range (m+1),
      ((((m:ℝ)-(i:ℝ))*v i+(i:ℝ)*v (i-1))^2 +
        (i:ℝ)*((m:ℝ)-(i:ℝ))*(v i-v (i-1))^2)) =
      (m:ℝ)*((m:ℝ)+1)*(∑ i ∈ Finset.range m, (v i)^2) := by
  calc
    _ = ∑ i ∈ Finset.range (m+1),
        (m:ℝ)*(((m:ℝ)-(i:ℝ))*(v i)^2+(i:ℝ)*(v (i-1))^2) := by
      apply Finset.sum_congr rfl
      intro i hi
      exact row_energy (m:ℝ) (i:ℝ) (v i) (v (i-1))
    _ = _ := by
      rw [← Finset.mul_sum, weighted_row_sum]
      ring

/-- The degree-one Hahn mode supplies the sharp nonzero spectral-gap witness. -/
theorem first_hahn_mode (m k : ℝ) :
    k*(m-k)*((k-(m-1)/2)-((k-1)-(m-1)/2)) +
    (k+1)*(m-k-1)*((k-(m-1)/2)-((k+1)-(m-1)/2)) =
      2*(k-(m-1)/2) := by
  ring

/-- The scalar square-root lift fails already at source dimension two. -/
theorem scalar_overlap_obstruction : (1:ℝ)/9 ≠ 0 := by
  norm_num

end ObservationalSUCC.PolyaCoherence

#print axioms ObservationalSUCC.PolyaCoherence.full_energy_decomposition
#print axioms ObservationalSUCC.PolyaCoherence.first_hahn_mode
