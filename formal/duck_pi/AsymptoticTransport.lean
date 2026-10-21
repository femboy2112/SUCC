import HaarIntervals
import PiSource
import Mathlib.Analysis.Asymptotics.SpecificAsymptotics
import Mathlib.Topology.UniformSpace.HeineCantor

/-!
# The actual Bailey–Crandall conditional normality bridge

Asymptotically close circle sequences have the same continuous-test limits.
The proof uses compact uniform continuity and Cesaro convergence, not finite
matching or an asserted source identity. The BBP integral proof identifies pi;
the exact tail bound supplies the vanishing distance. Equidistribution of the
specific forced orbit remains an explicit, unproved hypothesis.
-/

noncomputable section
open scoped BigOperators Topology
open Filter MeasureTheory

namespace ObservationalSUCC.DuckPi

theorem continuous_observation_difference_tendsto_zero
    (u v : ℕ → AddCircle (1 : ℝ))
    (hd : Tendsto (fun n => dist (u n) (v n)) atTop (𝓝 0))
    (F : AddCircle (1 : ℝ) → ℝ) (hF : Continuous F) :
    Tendsto (fun n => F (u n) - F (v n)) atTop (𝓝 0) := by
  apply Metric.tendsto_nhds.mpr
  intro ε hε
  obtain ⟨δ, hδ, hstep⟩ := Metric.uniformContinuous_iff.mp
    (CompactSpace.uniformContinuous_of_continuous hF) ε hε
  have hnear : ∀ᶠ n in atTop, dist (u n) (v n) < δ :=
    hd.eventually (gt_mem_nhds hδ)
  filter_upwards [hnear] with n hn
  simpa only [Real.dist_eq, sub_zero] using hstep hn

theorem haarUniform_of_dist_tendsto_zero
    (u v : ℕ → AddCircle (1 : ℝ))
    (hd : Tendsto (fun n => dist (u n) (v n)) atTop (𝓝 0))
    (hu : HaarUniformDistribution u) : HaarUniformDistribution v := by
  intro F hF
  have hdiff := (continuous_observation_difference_tendsto_zero u v hd F hF).cesaro
  have hdiff' : Tendsto (fun N : ℕ =>
      (∑ n ∈ Finset.range N, F (u n)) / (N : ℝ) -
        (∑ n ∈ Finset.range N, F (v n)) / (N : ℝ)) atTop (𝓝 0) := by
    simpa only [Finset.sum_sub_distrib, mul_sub, div_eq_mul_inv, mul_comm] using hdiff
  have htarget := (hu F hF).sub hdiff'
  simpa only [sub_sub_cancel, sub_zero] using htarget

theorem pi_forced_orbit_distance_tendsto_zero :
    Tendsto (fun n : ℕ => dist
      (ObservationalSUCC.BaileyCrandall.circleOrbit (n+1))
      ((16^n * Real.pi : ℝ) : AddCircle (1 : ℝ))) atTop (𝓝 0) := by
  apply tendsto_of_tendsto_of_tendsto_of_le_of_le tendsto_const_nhds
    tendsto_one_div_add_atTop_nhds_zero_nat
  · intro n
    exact dist_nonneg
  · intro n
    apply (Source.pi_circle_transport_shifted n).trans
    apply one_div_le_one_div_of_le (by positivity)
    have hn : (0 : ℝ) ≤ n := by positivity
    nlinarith [sq_nonneg (8*(n : ℝ)+9)]

/-- The actual forced orbit, starting with its first forcing step, carries the
same Haar limit as the hexadecimal pi digit orbit. This assumes the former
limit; no new equidistribution or normality axiom is introduced. -/
theorem baileyCrandall_haar_implies_pi_haar
    (hu : HaarUniformDistribution
      (fun n => ObservationalSUCC.BaileyCrandall.circleOrbit (n+1))) :
    HaarUniformDistribution (circleOrbit 16 Real.pi) := by
  have h := haarUniform_of_dist_tendsto_zero _ _ pi_forced_orbit_distance_tendsto_zero hu
  simpa only [circleOrbit, digitOrbit, Nat.cast_ofNat] using h

theorem baileyCrandall_haar_implies_pi_normal16
    (hu : HaarUniformDistribution
      (fun n => ObservationalSUCC.BaileyCrandall.circleOrbit (n+1))) : PiNormal16 := by
  apply pi_interval_equidistribution_implies_normal16
  exact haarUniform_implies_uniformDistribution _ (baileyCrandall_haar_implies_pi_haar hu)

end ObservationalSUCC.DuckPi
