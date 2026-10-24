import HaarBoundary

/-!
# The canonical half-open cylinders are Haar continuity sets

The measurable representative comes from mathlib's actual quotient-circle
isomorphism. The only extra boundary point is the cut at zero. Its Haar
mass, and those of the two cylinder endpoints, are proved zero. This supplies
the geometric step from continuous-test equidistribution to canonical blocks.
-/

noncomputable section

open scoped Topology ENNReal
open Filter MeasureTheory Set

namespace ObservationalSUCC.DuckPi

def circleRepresentative (z : AddCircle (1 : ℝ)) : ℝ :=
  AddCircle.equivIco (1 : ℝ) 0 z

def circleCylinder (a c : ℝ) : Set (AddCircle (1 : ℝ)) :=
  circleRepresentative ⁻¹' Set.Ico a c

theorem circleRepresentative_measurable : Measurable circleRepresentative :=
  measurable_subtype_coe.comp (AddCircle.measurableEquivIco (1 : ℝ) 0).measurable

theorem circleCylinder_measurable (a c : ℝ) : MeasurableSet (circleCylinder a c) :=
  measurableSet_Ico.preimage circleRepresentative_measurable

theorem circleRepresentative_coe (x : ℝ) :
    circleRepresentative (x : AddCircle (1 : ℝ)) = Int.fract x := by
  simpa [circleRepresentative] using AddCircle.coe_equivIco_mk_apply (1 : ℝ) x

theorem coe_circleRepresentative (z : AddCircle (1 : ℝ)) :
    (circleRepresentative z : AddCircle (1 : ℝ)) = z :=
  (AddCircle.equivIco (1 : ℝ) 0).symm_apply_apply z

theorem circleHaar_singleton (z : AddCircle (1 : ℝ)) : circleHaar {z} = 0 := by
  simpa [circleHaar] using (AddCircle.volume_closedBall (T := (1 : ℝ)) (x := z) 0)

instance circleHaar_noAtoms : NoAtoms circleHaar := ⟨circleHaar_singleton⟩

theorem circleCylinder_frontier_subset {a c : ℝ} (hac : a < c) :
    frontier (circleCylinder a c) ⊆
      {0, (a : AddCircle (1 : ℝ)), (c : AddCircle (1 : ℝ))} := by
  intro z hz
  by_cases hz0 : z = 0
  · simp [hz0]
  let e := (AddCircle.partialHomeomorphCoe (1 : ℝ) 0).symm
  have hzsource : z ∈ e.source := by
    change z ∉ {((0 : ℝ) : AddCircle (1 : ℝ))}
    simpa using hz0
  have hp : z ∈ e.source ∩ e ⁻¹' frontier (Set.Ico a c) := by
    rw [e.preimage_frontier]
    exact ⟨hzsource, hz⟩
  have hr : circleRepresentative z ∈ frontier (Set.Ico a c) := hp.2
  rw [frontier_Ico hac] at hr
  simp only [mem_insert_iff, mem_singleton_iff] at hr ⊢
  rcases hr with h | h
  · exact Or.inr (Or.inl (by rw [← coe_circleRepresentative z, h]))
  · exact Or.inr (Or.inr (by rw [← coe_circleRepresentative z, h]))

theorem circleCylinder_nullBoundary {a c : ℝ} (hac : a ≤ c) :
    circleHaar (frontier (circleCylinder a c)) = 0 := by
  rcases lt_or_eq_of_le hac with hlt | rfl
  · have hfinite : ({0, (a : AddCircle (1 : ℝ)),
        (c : AddCircle (1 : ℝ))} : Set (AddCircle (1 : ℝ))).Finite :=
      ((Set.finite_singleton (c : AddCircle (1 : ℝ))).insert _).insert _
    exact measure_mono_null (circleCylinder_frontier_subset hlt)
      (hfinite.measure_zero circleHaar)
  · simp [circleCylinder]

theorem circleCylinder_measure {a c : ℝ} (ha : 0 ≤ a) (hc : c ≤ 1) :
    circleHaar (circleCylinder a c) = ENNReal.ofReal (c - a) := by
  have hset : ((fun x : ℝ => (x : AddCircle (1 : ℝ))) ⁻¹' circleCylinder a c) ∩
      Set.Ico (0 : ℝ) 1 = Set.Ico a c := by
    ext x
    simp only [mem_inter_iff, mem_preimage, circleCylinder, circleRepresentative_coe]
    constructor
    · rintro ⟨h, hx⟩
      rwa [Int.fract_eq_self.mpr hx] at h
    · intro hx
      have hx01 : x ∈ Set.Ico (0 : ℝ) 1 := ⟨le_trans ha hx.1, lt_of_lt_of_le hx.2 hc⟩
      exact ⟨by simpa only [Int.fract_eq_self.mpr hx01] using hx, hx01⟩
  change volume (circleCylinder a c) = _
  rw [AddCircle.add_projection_respects_measure (1 : ℝ) 0 (circleCylinder_measurable a c)]
  simp only [zero_add]
  calc
    volume ((QuotientAddGroup.mk ⁻¹' circleCylinder a c) ∩ Set.Ioc (0 : ℝ) 1) =
        volume ((QuotientAddGroup.mk ⁻¹' circleCylinder a c) ∩ Set.Ico (0 : ℝ) 1) :=
      measure_congr ((Filter.EventuallyEq.refl _ _).inter Ico_ae_eq_Ioc.symm)
    _ = volume (Set.Ico a c) := by rw [hset]
    _ = ENNReal.ofReal (c - a) := Real.volume_Ico

theorem observationFrequency_circleCylinder (u : ℕ → ℝ) (a c : ℝ) (N : ℕ) :
    observationFrequency (fun n => (u n : AddCircle (1 : ℝ))) (circleCylinder a c) N =
      intervalFrequency u a c N := by
  simp [observationFrequency, intervalFrequency, circleCylinder, circleRepresentative_coe]

/-- Full classical Haar-to-interval implication, with canonical endpoints. -/
theorem haarUniform_implies_uniformDistribution (u : ℕ → ℝ)
    (hu : HaarUniformDistribution (fun n => (u n : AddCircle (1 : ℝ)))) :
    UniformDistributionModOne u := by
  intro a c ha hac hc
  have h := haarUniform_nullBoundary_frequency (fun n => (u n : AddCircle (1 : ℝ))) hu
    (circleCylinder a c) (circleCylinder_measurable a c) (circleCylinder_nullBoundary hac)
  have hfreq : observationFrequency (fun n => (u n : AddCircle (1 : ℝ)))
      (circleCylinder a c) = intervalFrequency u a c :=
    funext (observationFrequency_circleCylinder u a c)
  rw [hfreq] at h
  simpa only [circleCylinder_measure ha hc,
    ENNReal.toReal_ofReal (sub_nonneg.mpr hac)] using h

/-- Conditional normality from actual global Fourier cancellation, not a
redefinition of normality. Its cancellation premise remains unproved for pi. -/
theorem fourierCancellation_digitOrbit_implies_normal {b : ℕ} (hb : 2 ≤ b) (x : ℝ)
    (hu : FourierCancellation (digitOrbit b x)) : NormalTo b x :=
  uniformDistribution_digitOrbit_implies_normal hb x
    (haarUniform_implies_uniformDistribution _ (fourierCancellation_implies_haarUniform _ hu))

theorem pi_fourierCancellation_implies_normal16 (hu : PiFourierCancellation16) : PiNormal16 :=
  fourierCancellation_digitOrbit_implies_normal (by norm_num) Real.pi hu

end ObservationalSUCC.DuckPi
