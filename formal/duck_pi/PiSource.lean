import BaileyCrandall
import BBPIntegral

/-!
The actual BBP source identity and circle transport. The imported integral
proof identifies the sum with mathlib's Real.pi; no source identity is assumed
in these declarations. This says nothing about equidistribution or normality.
-/
noncomputable section

namespace ObservationalSUCC.DuckPi.Source
open ObservationalSUCC.BaileyCrandall

theorem bbp_series_eq_pi : seriesValue = Real.pi :=
  seriesValue_eq_of_hasSum Real.pi DuckPiIntegral.bbp_hasSum_pi

theorem pi_orbit_identity (n : ℕ) :
    16^n * Real.pi = liftedOrbit (n+1) + tail (n+1) := by
  rw [← bbp_series_eq_pi]
  exact series_orbit_transport n

theorem pi_circle_distance_le_tail (n : ℕ) :
    dist (circleOrbit (n+1)) ((16^n * Real.pi : ℝ) : AddCircle (1 : ℝ)) ≤
      tail (n+1) := by
  rw [dist_comm, pi_orbit_identity, dist_eq_norm]
  simp only [circleOrbit, AddCircle.coe_add, add_sub_cancel_left]
  have hq : ‖(tail (n+1) : AddCircle (1 : ℝ))‖ ≤ |tail (n+1)| := by
    simpa only [Real.norm_eq_abs] using
      (quotient_norm_mk_le' (AddSubgroup.zmultiples (1 : ℝ)) (tail (n+1)))
  simpa only [abs_of_pos (tail_pos (n+1))] using hq

theorem pi_circle_transport_source_bound (n : ℕ) :
    dist (circleOrbit (n+1)) ((16^n * Real.pi : ℝ) : AddCircle (1 : ℝ)) ≤
      forcing ((n : ℝ)+2)/15 := by
  apply (pi_circle_distance_le_tail n).trans
  simpa only [Nat.cast_add, Nat.cast_one, add_assoc, one_add_one_eq_two] using
    tail_le_source (n+1)

theorem pi_circle_transport_shifted (n : ℕ) :
    dist (circleOrbit (n+1)) ((16^n * Real.pi : ℝ) : AddCircle (1 : ℝ)) ≤
      1/(8*(n : ℝ)+9)^2 := by
  apply (pi_circle_distance_le_tail n).trans
  convert tail_le_shifted (n+1) using 1 <;> push_cast <;> ring

end ObservationalSUCC.DuckPi.Source
