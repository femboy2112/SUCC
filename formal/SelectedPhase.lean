import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Algebra.Order.BigOperators.Group.Finset
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring
import Std.Tactic

/-!
Selected-phase finite core. Pinned Lean/mathlib 4.14.0.

Formalized: integer-branch separation, the inhomogeneous backward telescope,
its endpoint error transport, summation of explicit block deficits, and the
two rational margins used by the paper inverse-coherence proof.

NOT formalized: complex chord geometry, the BBP integral/source theorem,
the irrationality measure of pi, the logarithmic block count, or normality.
The scalar block theorem explicitly assumes the triangle estimate and every
block deficit. It does not infer them from a source label.
-/

open scoped BigOperators

namespace ObservationalSUCC.SelectedPhase

theorem integer_gap_unique (a b : ℤ) (h : |((a-b : ℤ):ℝ)| < 1) : a=b := by
  have hl := (abs_lt.mp h).1
  have hu := (abs_lt.mp h).2
  have il : (-1:ℤ) < a-b := by exact_mod_cast hl
  have iu : a-b < (1:ℤ) := by exact_mod_cast hu
  omega

theorem translated_integer_branches_unique (a b : ℤ) (theta x y : ℝ)
    (hx : x=theta+(a:ℝ)) (hy : y=theta+(b:ℝ))
    (spread : |x-y| < 1) : a=b := by
  apply integer_gap_unique
  have eq : ((a-b : ℤ):ℝ)=x-y := by rw [hx, hy]; push_cast; ring
  rw [eq]
  exact spread

theorem backward_forcing_telescope (b : ℝ) (hb : b ≠ 0)
    (z force : ℕ → ℝ) (step : ∀ n, z (n+1)=b*z n+force n)
    (T : ℕ) :
    z 0 + (∑ j ∈ Finset.range T, force j / b^(j+1)) = z T/b^T := by
  induction T with
  | zero => simp
  | succ T ih =>
      rw [Finset.sum_range_succ, ← add_assoc, ih, step T, pow_succ]
      have hp : b^T ≠ 0 := pow_ne_zero T hb
      field_simp
      ring

theorem backward_endpoint_bound (b : ℝ) (hb : b ≠ 0)
    (z force : ℕ → ℝ) (step : ∀ n, z (n+1)=b*z n+force n)
    (T : ℕ) (R : ℝ) (endpoint : |z T| ≤ R) :
    |z 0 + (∑ j ∈ Finset.range T, force j / b^(j+1))| ≤ R/|b^T| := by
  rw [backward_forcing_telescope b hb z force step T, abs_div]
  exact div_le_div_of_nonneg_right endpoint (abs_nonneg _)

theorem finite_block_deficit_sum {ι : Type*} (blocks : Finset ι)
    (length magnitude : ι → ℝ) (loss : ℝ)
    (each : ∀ i ∈ blocks, magnitude i ≤ length i-loss) :
    (∑ i ∈ blocks, magnitude i) ≤
      (∑ i ∈ blocks, length i)-loss*(blocks.card:ℝ) := by
  calc
    (∑ i ∈ blocks, magnitude i) ≤ ∑ i ∈ blocks, (length i-loss) :=
      Finset.sum_le_sum each
    _ = (∑ i ∈ blocks, length i)-loss*(blocks.card:ℝ) := by
      rw [Finset.sum_sub_distrib]
      simp
      ring

theorem selected_total_deficit {ι : Type*} (blocks : Finset ι)
    (length magnitude : ι → ℝ) (loss remainder total bound : ℝ)
    (each : ∀ i ∈ blocks, magnitude i ≤ length i-loss)
    (cover : total=remainder+(∑ i ∈ blocks, length i))
    (triangle : bound ≤ remainder+(∑ i ∈ blocks, magnitude i)) :
    bound ≤ total-loss*(blocks.card:ℝ) := by
  have summed := finite_block_deficit_sum blocks length magnitude loss each
  linarith

theorem inverse_coherence_variation_margin :
    (34:ℝ)/100+15/64=919/1600 ∧ (919:ℝ)/1600 < 1 := by
  norm_num

theorem inverse_coherence_endpoint_margin :
    (16:ℝ)*((32/100)/15+1/(64*7^2)+1/(64*8^2))=1648007/4704000 ∧
    (1648007:ℝ)/4704000 < 1 := by
  norm_num

end ObservationalSUCC.SelectedPhase

#print axioms ObservationalSUCC.SelectedPhase.integer_gap_unique
#print axioms ObservationalSUCC.SelectedPhase.translated_integer_branches_unique
#print axioms ObservationalSUCC.SelectedPhase.backward_forcing_telescope
#print axioms ObservationalSUCC.SelectedPhase.backward_endpoint_bound
#print axioms ObservationalSUCC.SelectedPhase.finite_block_deficit_sum
#print axioms ObservationalSUCC.SelectedPhase.selected_total_deficit
#print axioms ObservationalSUCC.SelectedPhase.inverse_coherence_variation_margin
#print axioms ObservationalSUCC.SelectedPhase.inverse_coherence_endpoint_margin
