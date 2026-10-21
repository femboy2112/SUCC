import WeylBridge
import Mathlib.MeasureTheory.Measure.Portmanteau

/-!
# Empirical measures and null-boundary observations

The step from continuous tests to exact finite counts is proved using genuine
probability measures and Portmanteau. Nullity of the observed set's boundary
is an explicit geometric hypothesis, not a pi-specific equidistribution axiom.
The final identification of half-open circle arcs remains a separate lemma.
-/

noncomputable section

open scoped BigOperators Topology ENNReal
open Filter MeasureTheory

namespace ObservationalSUCC.DuckPi

/-- The empirical probability of the first N+1 observations. -/
def empiricalProbability (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ) :
    ProbabilityMeasure (AddCircle (1 : ℝ)) :=
  ⟨(((N + 1 : ℕ) : ℝ≥0∞)⁻¹) • ∑ n ∈ Finset.range (N + 1), Measure.dirac (u n),
    ⟨by
      simp only [Measure.smul_apply, Measure.finset_sum_apply, measure_univ,
        Finset.sum_const, Finset.card_range, nsmul_eq_mul, mul_one, smul_eq_mul]
      exact ENNReal.inv_mul_cancel (by simp) (by simp)⟩⟩

def haarProbability : ProbabilityMeasure (AddCircle (1 : ℝ)) :=
  ⟨circleHaar, ⟨circleHaar_total_mass⟩⟩

theorem empiricalProbability_integral (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ)
    (F : AddCircle (1 : ℝ) →ᵇ ℝ) :
    (∫ z, F z ∂(empiricalProbability u N : Measure (AddCircle (1 : ℝ)))) =
      (∑ n ∈ Finset.range (N + 1), F (u n)) / (N + 1 : ℝ) := by
  rw [empiricalProbability, ProbabilityMeasure.coe_mk, integral_smul_measure,
    integral_finset_sum_measure (fun n _ => F.integrable (Measure.dirac (u n)))]
  simp [div_eq_mul_inv, mul_comm]

theorem haarUniform_empiricalProbability_tendsto (u : ℕ → AddCircle (1 : ℝ))
    (hu : HaarUniformDistribution u) :
    Tendsto (empiricalProbability u) atTop (𝓝 haarProbability) := by
  apply ProbabilityMeasure.tendsto_iff_forall_integral_tendsto.mpr
  intro F
  have h := (hu F F.continuous).comp (tendsto_add_atTop_nat 1)
  simpa only [Function.comp_apply, empiricalProbability_integral,
    haarProbability, ProbabilityMeasure.coe_mk, Nat.cast_add, Nat.cast_one] using h

def observationFrequency (u : ℕ → AddCircle (1 : ℝ))
    (S : Set (AddCircle (1 : ℝ))) (N : ℕ) : ℝ :=
  ((Finset.range N).filter (fun n => u n ∈ S)).card / (N : ℝ)

theorem empiricalProbability_apply (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ)
    (S : Set (AddCircle (1 : ℝ))) (hS : MeasurableSet S) :
    (empiricalProbability u N : Measure (AddCircle (1 : ℝ))) S =
      (((Finset.range (N + 1)).filter (fun n => u n ∈ S)).card : ℝ≥0∞) /
        ((N + 1 : ℕ) : ℝ≥0∞) := by
  classical
  simp [empiricalProbability, Measure.finset_sum_apply,
    Measure.dirac_apply' _ hS, Set.indicator_apply, div_eq_mul_inv, mul_comm]

theorem empiricalProbability_toReal_apply (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ)
    (S : Set (AddCircle (1 : ℝ))) (hS : MeasurableSet S) :
    ((empiricalProbability u N : Measure (AddCircle (1 : ℝ))) S).toReal =
      observationFrequency u S (N + 1) := by
  simpa [observationFrequency] using
    congrArg ENNReal.toReal (empiricalProbability_apply u N S hS)

/-- Every measurable circle observation with Haar-null boundary has the correct
frequency under Haar continuous-test equidistribution. -/
theorem haarUniform_nullBoundary_frequency (u : ℕ → AddCircle (1 : ℝ))
    (hu : HaarUniformDistribution u) (S : Set (AddCircle (1 : ℝ)))
    (hS : MeasurableSet S) (hboundary : circleHaar (frontier S) = 0) :
    Tendsto (observationFrequency u S) atTop (𝓝 (circleHaar S).toReal) := by
  have hweak := haarUniform_empiricalProbability_tendsto u hu
  have hmeasure := ProbabilityMeasure.tendsto_measure_of_null_frontier_of_tendsto'
    hweak (show (haarProbability : Measure (AddCircle (1 : ℝ))) (frontier S) = 0 from hboundary)
  have hreal := (ENNReal.tendsto_toReal (measure_ne_top circleHaar S)).comp hmeasure
  apply (tendsto_add_atTop_iff_nat 1).mp
  simpa only [Function.comp_apply, empiricalProbability_toReal_apply u _ S hS,
    haarProbability, ProbabilityMeasure.coe_mk] using hreal

end ObservationalSUCC.DuckPi
