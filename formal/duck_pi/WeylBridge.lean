import Normality
import Mathlib.Analysis.Fourier.AddCircle
import Mathlib.MeasureTheory.Integral.BoundedContinuousFunction
import Mathlib.Topology.MetricSpace.Equicontinuity

/-!
# From actual Fourier cancellation to continuous-test Haar equidistribution

The missing cancellation remains an explicit premise. The extension from
characters to all continuous tests uses the genuine Stone-Weierstrass density
result in pinned mathlib, uniform norm bounds, and closedness of convergence.
This is not an interval approximation theorem and does not assert pi normality.
-/

noncomputable section

open scoped BigOperators Topology
open Filter MeasureTheory

namespace ObservationalSUCC.DuckPi

abbrev CircleTest := C(AddCircle (1 : ℝ), ℂ)

instance circleHaar_isProbabilityMeasure : IsProbabilityMeasure circleHaar :=
  ⟨circleHaar_total_mass⟩

def empiricalMean (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ) (F : CircleTest) : ℂ :=
  (∑ n ∈ Finset.range N, F (u n)) / (N : ℂ)

def haarMean (F : CircleTest) : ℂ := ∫ z, F z ∂circleHaar

def ComplexHaarUniformDistribution (u : ℕ → AddCircle (1 : ℝ)) : Prop :=
  ∀ F : CircleTest, Tendsto (fun N => empiricalMean u N F) atTop (𝓝 (haarMean F))

theorem circleTest_integrable (F : CircleTest) : Integrable F circleHaar :=
  (BoundedContinuousFunction.mkOfCompact F).integrable circleHaar

theorem empiricalMean_add (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ) (F G : CircleTest) :
    empiricalMean u N (F + G) = empiricalMean u N F + empiricalMean u N G := by
  simp [empiricalMean, Finset.sum_add_distrib, add_div]

theorem empiricalMean_smul (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ)
    (c : ℂ) (F : CircleTest) :
    empiricalMean u N (c • F) = c • empiricalMean u N F := by
  simp only [empiricalMean, ContinuousMap.smul_apply, smul_eq_mul]
  rw [← Finset.mul_sum]
  ring

theorem empiricalMean_sub (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ) (F G : CircleTest) :
    empiricalMean u N (F - G) = empiricalMean u N F - empiricalMean u N G := by
  simp [empiricalMean, Finset.sum_sub_distrib, sub_div]

theorem haarMean_add (F G : CircleTest) : haarMean (F + G) = haarMean F + haarMean G := by
  exact integral_add (circleTest_integrable F) (circleTest_integrable G)

theorem haarMean_smul (c : ℂ) (F : CircleTest) : haarMean (c • F) = c • haarMean F := by
  exact integral_smul c F

theorem haarMean_sub (F G : CircleTest) : haarMean (F - G) = haarMean F - haarMean G := by
  exact integral_sub (circleTest_integrable F) (circleTest_integrable G)

theorem norm_empiricalMean_le (u : ℕ → AddCircle (1 : ℝ)) (N : ℕ) (F : CircleTest) :
    ‖empiricalMean u N F‖ ≤ ‖F‖ := by
  by_cases hN : N = 0
  · simp [empiricalMean, hN]
  have hpos : (0 : ℝ) < N := by exact_mod_cast (Nat.pos_of_ne_zero hN)
  rw [empiricalMean, norm_div, Complex.norm_natCast, div_le_iff₀ hpos]
  calc
    ‖∑ n ∈ Finset.range N, F (u n)‖ ≤ ∑ n ∈ Finset.range N, ‖F (u n)‖ :=
      norm_sum_le _ _
    _ ≤ ∑ _n ∈ Finset.range N, ‖F‖ := Finset.sum_le_sum (fun n _ => F.norm_coe_le_norm (u n))
    _ = ‖F‖ * (N : ℝ) := by simp [mul_comm]

theorem norm_haarMean_le (F : CircleTest) : ‖haarMean F‖ ≤ ‖F‖ := by
  have h := norm_integral_le_of_norm_le_const (μ := circleHaar)
    (Filter.Eventually.of_forall (fun z => F.norm_coe_le_norm z))
  simpa [haarMean, circleHaar_total_mass] using h

theorem empiricalMean_equicontinuous (u : ℕ → AddCircle (1 : ℝ)) :
    Equicontinuous (empiricalMean u) := by
  apply Metric.equicontinuous_of_continuity_modulus (fun x : ℝ => x) tendsto_id
  intro F G N
  simpa only [dist_eq_norm, ← empiricalMean_sub] using norm_empiricalMean_le u N (F - G)

theorem haarMean_continuous : Continuous haarMean := by
  have h : LipschitzWith 1 haarMean := by
    apply LipschitzWith.of_dist_le_mul
    intro F G
    simpa only [dist_eq_norm, ← haarMean_sub, NNReal.coe_one, one_mul]
      using norm_haarMean_le (F - G)
  exact h.continuous

/-- Continuous tests whose empirical means already converge to their Haar mean. -/
def convergentTests (u : ℕ → AddCircle (1 : ℝ)) : Submodule ℂ CircleTest where
  carrier := {F | Tendsto (fun N => empiricalMean u N F) atTop (𝓝 (haarMean F))}
  zero_mem' := by simpa [empiricalMean, haarMean] using
    (tendsto_const_nhds : Tendsto (fun _ : ℕ => (0 : ℂ)) atTop (𝓝 0))
  add_mem' := by
    intro F G hF hG
    change Tendsto (fun N => empiricalMean u N (F + G)) atTop (𝓝 (haarMean (F + G)))
    simpa only [empiricalMean_add, haarMean_add] using hF.add hG
  smul_mem' := by
    intro c F hF
    change Tendsto (fun N => empiricalMean u N (c • F)) atTop (𝓝 (haarMean (c • F)))
    simpa only [empiricalMean_smul, haarMean_smul] using hF.const_smul c

theorem convergentTests_isClosed (u : ℕ → AddCircle (1 : ℝ)) :
    IsClosed (convergentTests u : Set CircleTest) :=
  (empiricalMean_equicontinuous u).isClosed_setOf_tendsto haarMean_continuous

theorem circleHaar_eq_normalizedHaar : circleHaar = @AddCircle.haarAddCircle (1 : ℝ) _ := by
  simp [circleHaar, AddCircle.volume_eq_smul_haarAddCircle]

theorem haarMean_fourier_zero : haarMean (@fourier (1 : ℝ) 0) = 1 := by
  simp [haarMean, fourier_zero, circleHaar_total_mass]

theorem haarMean_fourier_ne_zero {h : ℤ} (hh : h ≠ 0) :
    haarMean (@fourier (1 : ℝ) h) = 0 := by
  unfold haarMean
  rw [circleHaar_eq_normalizedHaar]
  exact integral_eq_zero_of_add_right_eq_neg (μ := AddCircle.haarAddCircle)
    (fourier_add_half_inv_index hh (by norm_num))

theorem empiricalMean_fourier_zero_tendsto (u : ℕ → AddCircle (1 : ℝ)) :
    Tendsto (fun N => empiricalMean u N (@fourier (1 : ℝ) 0)) atTop (𝓝 1) := by
  apply (tendsto_congr' (show (fun N => empiricalMean u N (@fourier (1 : ℝ) 0)) =ᶠ[atTop]
      (fun _ : ℕ => (1 : ℂ)) from ?_)).mpr tendsto_const_nhds
  filter_upwards [eventually_ge_atTop 1] with N hN
  have hne : (N : ℂ) ≠ 0 := by exact_mod_cast (show N ≠ 0 by omega)
  simp [empiricalMean, fourier_zero, hne]

/-- Weyl's character-to-continuous-test implication on the actual unit circle.
No source-specific cancellation is manufactured by this theorem. -/
theorem character_cancellation_implies_complexHaar
    (u : ℕ → AddCircle (1 : ℝ))
    (hu : ∀ h : ℤ, h ≠ 0 →
      Tendsto (fun N => empiricalMean u N (@fourier (1 : ℝ) h)) atTop (𝓝 0)) :
    ComplexHaarUniformDistribution u := by
  have hchars : Set.range (@fourier (1 : ℝ)) ⊆ (convergentTests u : Set CircleTest) := by
    rintro F ⟨h, rfl⟩
    change Tendsto (fun N => empiricalMean u N (@fourier (1 : ℝ) h)) atTop
      (𝓝 (haarMean (@fourier (1 : ℝ) h)))
    by_cases hh : h = 0
    · subst h
      rw [haarMean_fourier_zero]
      exact empiricalMean_fourier_zero_tendsto u
    · rw [haarMean_fourier_ne_zero hh]
      exact hu h hh
  have hspan : Submodule.span ℂ (Set.range (@fourier (1 : ℝ))) ≤ convergentTests u :=
    Submodule.span_le.mpr hchars
  have hclosed := (Submodule.span ℂ (Set.range (@fourier (1 : ℝ)))).topologicalClosure_minimal
    hspan (convergentTests_isClosed u)
  rw [span_fourier_closure_eq_top] at hclosed
  intro F
  exact hclosed (Submodule.mem_top : F ∈ (⊤ : Submodule ℂ CircleTest))

/-- The exponential sum used in `Normality.lean` is precisely the Haar character
average; the period is one and the pi constant is mathlib's genuine Real.pi. -/
theorem weylMean_eq_characterMean (u : ℕ → ℝ) (h : ℤ) (N : ℕ) :
    weylMean u h N = empiricalMean (fun n => (u n : AddCircle (1 : ℝ))) N
      (@fourier (1 : ℝ) h) := by
  simp [weylMean, empiricalMean, fourier_coe_apply]

theorem fourierCancellation_implies_complexHaar (u : ℕ → ℝ)
    (hu : FourierCancellation u) :
    ComplexHaarUniformDistribution (fun n => (u n : AddCircle (1 : ℝ))) := by
  apply character_cancellation_implies_complexHaar
  intro h hh
  simpa only [← weylMean_eq_characterMean] using hu h hh

/-- Complex continuous-test convergence includes the real-test Haar predicate
already defined independently in Normality.lean. -/
theorem complexHaar_implies_haarUniform (u : ℕ → AddCircle (1 : ℝ))
    (hu : ComplexHaarUniformDistribution u) : HaarUniformDistribution u := by
  intro F hF
  let Fc : CircleTest := ⟨fun z => (F z : ℂ), Complex.continuous_ofReal.comp hF⟩
  have havg (N : ℕ) : empiricalMean u N Fc =
      (((∑ n ∈ Finset.range N, F (u n)) / (N : ℝ) : ℝ) : ℂ) := by
    simp [empiricalMean, Fc, Complex.ofReal_div, Complex.ofReal_sum]
  have hint : haarMean Fc = ((∫ z, F z ∂circleHaar : ℝ) : ℂ) := by
    exact integral_ofReal
  have hc := hu Fc
  simp_rw [havg] at hc
  rw [hint] at hc
  have hr := (Complex.continuous_re.tendsto _).comp hc
  simpa only [Function.comp_apply, Complex.ofReal_re] using hr

theorem fourierCancellation_implies_haarUniform (u : ℕ → ℝ)
    (hu : FourierCancellation u) :
    HaarUniformDistribution (fun n => (u n : AddCircle (1 : ℝ))) :=
  complexHaar_implies_haarUniform _ (fourierCancellation_implies_complexHaar u hu)

end ObservationalSUCC.DuckPi
