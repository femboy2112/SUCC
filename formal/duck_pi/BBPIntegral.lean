import Mathlib.Analysis.SpecialFunctions.Integrals
import Mathlib.Analysis.SpecialFunctions.Trigonometric.ArctanDeriv
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.MeasureTheory.Integral.DominatedConvergence
import Mathlib.Tactic

/-!
The classical BBP identity from an elementary integral.  There is no premise
asserting the BBP identity, nor any normality assertion.  The infinite exchange
uses a summable majorant on the entire interval, not finite numerical agreement.
-/

noncomputable section
open MeasureTheory Set Filter
open scoped Topology BigOperators

namespace DuckPiIntegral

def numerator (x : ℝ) : ℝ := 4 - 2*x^3 - x^4 - x^5
def integrand (x : ℝ) : ℝ := numerator x / (1 - x^8/16)
def primitive (x : ℝ) : ℝ :=
  2*Real.log (2-x^2) - 2*Real.log (x^2-2*x+2) + 4*Real.arctan (x-1)
def term (n : ℕ) (x : ℝ) : ℝ := numerator x * (x^8/16)^n
def coefficient (n : ℕ) : ℝ :=
  4/(8*(n:ℝ)+1) - 2/(8*(n:ℝ)+4) - 1/(8*(n:ℝ)+5) - 1/(8*(n:ℝ)+6)

theorem denominator_ne_zero {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    1-x^8/16 ≠ 0 := by
  have hpow : x^8 ≤ 1 := pow_le_one₀ hx.1 hx.2
  linarith

theorem rational_decomposition {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    integrand x = 4*x/(x^2-2) - 4*(x-2)/(x^2-2*x+2) := by
  have hpow : x^2 ≤ 1 := pow_le_one₀ hx.1 hx.2
  have hA : x^2-2 ≠ 0 := by linarith
  have hB : x^2-2*x+2 ≠ 0 := by nlinarith [sq_nonneg (x-1)]
  have hD := denominator_ne_zero hx
  have hE : 16-x^8 ≠ 0 := by
    have h8 : x^8 ≤ 1 := pow_le_one₀ hx.1 hx.2
    linarith
  unfold integrand numerator
  field_simp [hA, hB, hD, hE]
  <;> ring

theorem primitive_hasDerivAt {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    HasDerivAt primitive (integrand x) x := by
  have hpow : x^2 ≤ 1 := pow_le_one₀ hx.1 hx.2
  have hA : 2-x^2 ≠ 0 := by linarith
  have hB : x^2-2*x+2 ≠ 0 := by nlinarith [sq_nonneg (x-1)]
  have hC : 1+(x-1)^2 ≠ 0 := by positivity
  have hD : x^2-2 ≠ 0 := by linarith
  have hdA := ((hasDerivAt_pow 2 x).const_sub 2).log hA
  have hdB := (((hasDerivAt_pow 2 x).sub
    ((hasDerivAt_id x).const_mul 2)).add_const 2).log hB
  have hdC := ((hasDerivAt_id x).sub_const 1).arctan
  convert ((hdA.const_mul 2).sub (hdB.const_mul 2)).add (hdC.const_mul 4) using 1
  rw [rational_decomposition hx]
  norm_num
  field_simp [hA, hB, hC, hD]
  <;> ring

theorem integrand_intervalIntegrable : IntervalIntegrable integrand volume (0:ℝ) 1 := by
  apply ContinuousOn.intervalIntegrable_of_Icc (by norm_num)
  apply ContinuousOn.div
  · unfold numerator
    fun_prop
  · fun_prop
  · exact fun x hx => denominator_ne_zero hx

theorem integral_eq_pi : (∫ x in (0:ℝ)..1, integrand x) = Real.pi := by
  have hftc := intervalIntegral.integral_eq_sub_of_hasDerivAt
    (a := (0:ℝ)) (b := 1) (f := primitive) (f' := integrand)
    (fun x hx => primitive_hasDerivAt (by simpa using hx))
    integrand_intervalIntegrable
  rw [hftc]
  norm_num [primitive, Real.arctan_neg, Real.arctan_one]
  ring

theorem numerator_abs_le {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    |numerator x| ≤ 8 := by
  have h3 : 0 ≤ x^3 ∧ x^3 ≤ 1 := ⟨pow_nonneg hx.1 _, pow_le_one₀ hx.1 hx.2⟩
  have h4 : 0 ≤ x^4 ∧ x^4 ≤ 1 := ⟨pow_nonneg hx.1 _, pow_le_one₀ hx.1 hx.2⟩
  have h5 : 0 ≤ x^5 ∧ x^5 ≤ 1 := ⟨pow_nonneg hx.1 _, pow_le_one₀ hx.1 hx.2⟩
  unfold numerator
  rw [abs_le]
  constructor <;> linarith

theorem ratio_abs_le {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    |x^8/16| ≤ (1:ℝ)/16 := by
  rw [abs_of_nonneg (by positivity)]
  exact div_le_div_of_nonneg_right (pow_le_one₀ hx.1 hx.2) (by norm_num)

theorem term_norm_le (n : ℕ) {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    ‖term n x‖ ≤ 8*((1:ℝ)/16)^n := by
  rw [term, norm_mul, norm_pow, Real.norm_eq_abs, Real.norm_eq_abs]
  exact mul_le_mul (numerator_abs_le hx)
    (pow_le_pow_left₀ (abs_nonneg _) (ratio_abs_le hx) n)
    (pow_nonneg (abs_nonneg _) _) (by norm_num)

theorem term_hasSum {x : ℝ} (hx : x ∈ Icc (0:ℝ) 1) :
    HasSum (fun n => term n x) (integrand x) := by
  have hlt : |x^8/16| < 1 := lt_of_le_of_lt (ratio_abs_le hx) (by norm_num)
  simpa only [term, integrand, div_eq_mul_inv] using
    (hasSum_geometric_of_abs_lt_one hlt).mul_left (numerator x)

theorem term_polynomial (n : ℕ) (x : ℝ) :
    term n x = ((1:ℝ)/16)^n *
      (4*x^(8*n) - 2*x^(8*n+3) - x^(8*n+4) - x^(8*n+5)) := by
  unfold term numerator
  simp only [div_pow, one_pow, pow_add, pow_mul]
  ring

theorem integral_term (n : ℕ) :
    (∫ x in (0:ℝ)..1, term n x) = ((1:ℝ)/16)^n * coefficient n := by
  simp_rw [term_polynomial]
  rw [intervalIntegral.integral_const_mul]
  rw [intervalIntegral.integral_sub, intervalIntegral.integral_sub,
    intervalIntegral.integral_sub]
  · simp [intervalIntegral.integral_const_mul, integral_pow, coefficient]
    <;> ring
  all_goals apply Continuous.intervalIntegrable
  all_goals fun_prop

theorem hasSum_integral_terms :
    HasSum (fun n : ℕ => ∫ x in (0:ℝ)..1, term n x)
      (∫ x in (0:ℝ)..1, integrand x) := by
  have hgeo : |(1:ℝ)/16| < 1 := by
    rw [abs_of_nonneg (by positivity)]
    norm_num
  apply intervalIntegral.hasSum_integral_of_dominated_convergence
    (fun n (_ : ℝ) => 8*((1:ℝ)/16)^n)
  · intro n
    apply Continuous.aestronglyMeasurable
    unfold term numerator
    fun_prop
  · intro n
    exact ae_of_all _ fun x hx => term_norm_le n (by
      have hx' : 0 < x ∧ x ≤ 1 := by simpa using hx
      exact ⟨hx'.1.le, hx'.2⟩)
  · exact ae_of_all _ fun x hx =>
      (summable_geometric_of_abs_lt_one hgeo).mul_left 8
  · exact intervalIntegrable_const
  · exact ae_of_all _ fun x hx => term_hasSum (by
      have hx' : 0 < x ∧ x ≤ 1 := by simpa using hx
      exact ⟨hx'.1.le, hx'.2⟩)

/-- Classical BBP formula, with its source identity proved by an integral. -/
theorem bbp_hasSum_pi :
    HasSum (fun n : ℕ => ((1:ℝ)/16)^n *
      (4/(8*(n:ℝ)+1) - 2/(8*(n:ℝ)+4) -
        1/(8*(n:ℝ)+5) - 1/(8*(n:ℝ)+6))) Real.pi := by
  simpa only [integral_term, integral_eq_pi, coefficient] using hasSum_integral_terms

theorem bbp_tsum_eq_pi :
    (∑' n : ℕ, ((1:ℝ)/16)^n *
      (4/(8*(n:ℝ)+1) - 2/(8*(n:ℝ)+4) -
        1/(8*(n:ℝ)+5) - 1/(8*(n:ℝ)+6))) = Real.pi :=
  bbp_hasSum_pi.tsum_eq

#print axioms DuckPiIntegral.bbp_hasSum_pi
#print axioms DuckPiIntegral.bbp_tsum_eq_pi

end DuckPiIntegral
