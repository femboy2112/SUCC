import PiSource
import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Data.Nat.Choose.Sum
import Mathlib.Analysis.Calculus.MeanValue
import Mathlib.Analysis.Complex.RealDeriv
import Mathlib.Analysis.Complex.Basic

/-!
# Finite source algebra and two-time BBP transport

These declarations preserve the exact four-pole BBP source and its actual
`Real.pi` identification from PR #232. The pole moments are forcing-index
moments, not circle states. All inequalities state their real domains.

No declaration asserts Fourier cancellation, equidistribution, or normality.
The pointwise kernel bounds are finite algebra; their integration and the
all-order Hausdorff/Hankel statements remain separate analytic obligations.
-/

noncomputable section
open scoped BigOperators
open ObservationalSUCC.BaileyCrandall

namespace ObservationalSUCC.PiSourceGenesis

def poleMoment (k : ℕ) : ℝ :=
  (1/2)*(7/8)^k - (1/4)*(1/2)^k - (1/8)*(3/8)^k - (1/8)*(1/4)^k

theorem pole_moment_zero : poleMoment 0 = 0 := by norm_num [poleMoment]
theorem pole_moment_one : poleMoment 1 = 15/64 := by norm_num [poleMoment]
theorem pole_moment_two : poleMoment 2 = 151/512 := by norm_num [poleMoment]
theorem pole_moment_three : poleMoment 3 = 1209/4096 := by norm_num [poleMoment]
theorem pole_moment_four : poleMoment 4 = 8995/32768 := by norm_num [poleMoment]

def kernelH (t : ℝ) : ℝ := 4 + 4*t + 4*t^2 + 2*t^3 + t^4
def kernelMultiplier (t : ℝ) : ℝ := kernelH t / (16-t^8)

theorem kernel_factorization (t : ℝ) :
    DuckPiIntegral.numerator t = (1-t)*kernelH t := by
  unfold DuckPiIntegral.numerator kernelH
  ring

/-- Source-specific cancellation of the degree-eight denominator. -/
theorem kernel_reciprocal_certificate (t : ℝ) :
    kernelH t * (4-4*t+2*t^3-t^4) = 16-t^8 := by
  unfold kernelH
  ring

theorem kernel_endpoint_certificate (s : ℝ) :
    4-4*(1+s)+2*(1+s)^3-(1+s)^4 = 1-2*s-2*s^3-s^4 := by
  ring

theorem kernelH_pos {t : ℝ} (ht : 0 ≤ t) : 0 < kernelH t := by
  unfold kernelH
  positivity

theorem kernel_positive {t : ℝ} (ht : 0 ≤ t) (ht1 : t < 1) :
    0 < DuckPiIntegral.numerator t := by
  rw [kernel_factorization]
  exact mul_pos (by linarith) (kernelH_pos ht)

theorem kernel_denominator_pos {t : ℝ} (ht : 0 ≤ t) (ht1 : t ≤ 1) :
    0 < 16-t^8 := by
  have := pow_le_one₀ ht ht1 (n := 8)
  linarith

theorem kernel_multiplier_lower {t : ℝ} (ht : 0 < t) (ht1 : t ≤ 1) :
    1/4 < kernelMultiplier t := by
  have hd := kernel_denominator_pos ht.le ht1
  rw [kernelMultiplier, lt_div_iff₀ hd]
  have h2 := sq_nonneg t
  have h3 := pow_nonneg ht.le 3
  have h4 := pow_nonneg ht.le 4
  have h8 := pow_nonneg ht.le 8
  unfold kernelH
  nlinarith

theorem kernel_multiplier_upper {t : ℝ} (ht : 0 ≤ t) (ht1 : t < 1) :
    kernelMultiplier t < 1 := by
  have hd := kernel_denominator_pos ht ht1.le
  have h2 := pow_le_one₀ ht ht1.le (n := 2)
  have h3 := pow_le_one₀ ht ht1.le (n := 3)
  have h4 := pow_le_one₀ ht ht1.le (n := 4)
  have h8 := pow_le_one₀ ht ht1.le (n := 8)
  rw [kernelMultiplier, div_lt_iff₀ hd]
  unfold kernelH
  nlinarith

/-- A polynomial certificate for the sharp first-order deficit majorant. -/
theorem kernel_deficit_certificate (t : ℝ) :
    2*(1-t)*(16-t^8) - ((16-t^8)-kernelH t) =
      (1-t)^2*(20+12*t+8*t^2+6*t^3+5*t^4+4*t^5+3*t^6+2*t^7) := by
  unfold kernelH
  ring

theorem kernel_deficit_upper {t : ℝ} (ht : 0 ≤ t) (ht1 : t ≤ 1) :
    1-kernelMultiplier t ≤ 2*(1-t) := by
  have hd := kernel_denominator_pos ht ht1
  have hc := kernel_deficit_certificate t
  have hp : 0 ≤ (1-t)^2*(20+12*t+8*t^2+6*t^3+5*t^4+4*t^5+3*t^6+2*t^7) :=
    by positivity
  have hcross : (1-2*(1-t))*(16-t^8) ≤ kernelH t := by nlinarith
  have hdiv : 1-2*(1-t) ≤ kernelMultiplier t :=
    (le_div_iff₀ hd).2 hcross
  linarith

/-- Readout matrix at the four authenticated, fixed forcing-index poles. -/
def sourceCauchy : Matrix (Fin 4) (Fin 4) ℝ :=
  !![8, 2, 8/5, 4/3;
     8/9, 2/3, 8/13, 4/7;
     8/17, 2/5, 8/21, 4/11;
     8/25, 2/7, 8/29, 4/15]

def sourcePole : Fin 4 → ℝ := ![7/8, 1/2, 3/8, 1/4]

theorem source_cauchy_entry (i j : Fin 4) :
    sourceCauchy i j = 1/((i : ℝ)+1-sourcePole j) := by
  fin_cases i <;> fin_cases j <;> norm_num [sourceCauchy, sourcePole]

theorem forcing_first_four_readouts :
    forcing 1 = 47/15 ∧ forcing 2 = 106/819 ∧
      forcing 3 = 829/19635 ∧ forcing 4 = 316/15225 := by
  norm_num [forcing, numerator, denominator]

theorem source_cauchy_determinant :
    sourceCauchy.det = 8388608/1224171073125 := by
  rw [Matrix.det_succ_row_zero]
  norm_num [sourceCauchy, Fin.sum_univ_succ, Matrix.det_fin_three,
    Matrix.submatrix, Fin.succAbove, Fin.lt_def, Fin.le_def, Fin.ext_iff,
    Fin.castSucc, Fin.castAdd, Fin.castLE, Fin.reduceFinMk]

theorem source_cauchy_determinant_ne_zero : sourceCauchy.det ≠ 0 := by
  rw [source_cauchy_determinant]
  norm_num

/-- Identification is restricted to residues at the specified four poles. -/
theorem source_residues_identified (a b c d : ℝ)
    (h1 : 8*a + 2*b + (8/5)*c + (4/3)*d = 47/15)
    (h2 : (8/9)*a + (2/3)*b + (8/13)*c + (4/7)*d = 106/819)
    (h3 : (8/17)*a + (2/5)*b + (8/21)*c + (4/11)*d = 829/19635)
    (h4 : (8/25)*a + (2/7)*b + (8/29)*c + (4/15)*d = 316/15225) :
    a = 1/2 ∧ b = -1/4 ∧ c = -1/8 ∧ d = -1/8 := by
  constructor
  · linarith
  constructor
  · linarith
  constructor <;> linarith

def liftedFrom (s : ℝ) (n : ℕ) : ℝ := liftedOrbit n + 16^n*s

theorem liftedFrom_initial (s : ℝ) : liftedFrom s 0 = s := by
  simp [liftedFrom, liftedOrbit]

theorem liftedFrom_recursion (s : ℝ) (n : ℕ) :
    liftedFrom s (n+1) = 16*liftedFrom s n + forcing ((n : ℝ)+1) := by
  simp only [liftedFrom, liftedOrbit, pow_succ]
  ring

theorem liftedFrom_source_selection (s : ℝ) (n : ℕ) :
    liftedFrom s n + tail n = 16^n*(s+tail 0) := by
  have h := lifted_orbit_tail_identity n
  unfold liftedFrom
  nlinarith

theorem forced_first_zero : Int.fract (16*(0 : ℝ)+forcing 1) = 2/15 := by
  norm_num [forcing_at_one, Int.fract]

theorem forced_first_third : Int.fract (16*(1/3 : ℝ)+forcing 1) = 7/15 := by
  norm_num [forcing_at_one, Int.fract]

theorem forcing_changed_initial_not_unforced_fixed :
    Int.fract (16*(1/3 : ℝ)+forcing 1) ≠ 1/3 := by
  rw [forced_first_third]
  norm_num

/-- Each individual summand is strictly decreasing; positivity is not circle mixing. -/
theorem tail_succ_le (n : ℕ) : tail (n+1) ≤ tail n := by
  apply tsum_le_tsum _ (tail_summable (n+1)) (tail_summable n)
  intro k
  have hn : (0 : ℝ) ≤ n := by positivity
  have hk : (0 : ℝ) ≤ k := by positivity
  have hf := (forcing_succ_lt (x := (n : ℝ)+k+1) (by linarith)).le
  unfold tailTerm
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  convert hf using 1 <;> push_cast <;> ring

theorem tail_add_le (n d : ℕ) : tail (n+d) ≤ tail n := by
  induction d with
  | zero => simp
  | succ d ih =>
    exact (tail_succ_le (n+d)).trans ih

/-- Authentic two-time identity; the small correction is a tail difference,
not the exponentially amplified `(16^d-1)*tail (j+1)`. -/
theorem pi_lag_lift_identity (j d : ℕ) :
    (16^d-1)*16^j*Real.pi =
      liftedOrbit (j+d+1)-liftedOrbit (j+1) + tail (j+d+1)-tail (j+1) := by
  have h0 := ObservationalSUCC.DuckPi.Source.pi_orbit_identity j
  have h1 := ObservationalSUCC.DuckPi.Source.pi_orbit_identity (j+d)
  rw [pow_add] at h1
  nlinarith

theorem pi_lag_correction_abs (j d : ℕ) :
    |tail (j+d+1)-tail (j+1)| = tail (j+1)-tail (j+d+1) := by
  have ht : tail (j+d+1) ≤ tail (j+1) := by
    simpa [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm] using tail_add_le (j+1) d
  rw [abs_of_nonpos (by linarith)]
  ring

theorem pi_lag_correction_uniform (j d : ℕ) :
    |tail (j+d+1)-tail (j+1)| ≤ 1/(8*(j : ℝ)+9)^2 := by
  rw [pi_lag_correction_abs]
  have hpos := (tail_pos (j+d+1)).le
  have hb := tail_le_shifted (j+1)
  have heq : 8*((j+1 : ℕ) : ℝ)+1 = 8*(j : ℝ)+9 := by push_cast; ring
  rw [heq] at hb
  linarith

/-- An algebraic telescope valid even when the two windows overlap. -/
theorem lag_window_telescope (a : ℕ → ℝ) (J L d : ℕ) :
    (∑ j ∈ Finset.range L, (a (J+j)-a (J+j+d))) =
      (∑ j ∈ Finset.range d, a (J+j)) -
      (∑ j ∈ Finset.range d, a (J+L+j)) := by
  have hp (m n : ℕ) :
      (∑ j ∈ Finset.range (m+n), a (J+j)) =
        (∑ j ∈ Finset.range m, a (J+j)) +
        (∑ j ∈ Finset.range n, a (J+m+j)) := by
    rw [Finset.sum_range_add]
    congr 1
    apply Finset.sum_congr rfl
    intro j hj
    congr 1
    omega
  have h1 := hp L d
  have h2 := hp d L
  rw [Nat.add_comm d L] at h2
  rw [Finset.sum_sub_distrib]
  have heq : (∑ j ∈ Finset.range L, a (J+j+d)) =
      ∑ j ∈ Finset.range L, a (J+d+j) := by
    apply Finset.sum_congr rfl
    intro j hj
    congr 1
    omega
  rw [heq]
  linarith

/-- Complex phases retain their signs; `a = 2*pi*h` gives Fourier mode `h`. -/
def phase (a t : ℝ) : ℂ := Complex.exp (((a*t : ℝ) : ℂ)*Complex.I)

theorem phase_lipschitz (a x y : ℝ) :
    ‖phase a y-phase a x‖ ≤ |a| * |y-x| := by
  let df := fun t : ℝ => phase a t * ((a : ℂ)*Complex.I)
  have hf (t : ℝ) : HasDerivAt (phase a) (df t) t := by
    convert ((((hasDerivAt_id t).const_mul a).ofReal_comp).mul_const Complex.I).cexp using 1
    simp [phase, df]
  have hb (t : ℝ) : ‖df t‖ ≤ |a| := by
    have hp : ‖phase a t‖ = 1 := Complex.norm_exp_ofReal_mul_I (a*t)
    dsimp only [df]
    rw [norm_mul, hp]
    simp [norm_mul]
  have h := (convex_univ : Convex ℝ (Set.univ : Set ℝ)).norm_image_sub_le_of_norm_hasDerivWithin_le
    (fun t _ => (hf t).hasDerivWithinAt) (fun t _ => hb t) (Set.mem_univ x) (Set.mem_univ y)
  simpa [Real.norm_eq_abs] using h

theorem pi_lag_character_transport (a : ℝ) (j d : ℕ) :
    ‖phase a ((16^d-1)*16^j*Real.pi) -
        phase a (liftedOrbit (j+d+1)-liftedOrbit (j+1))‖ ≤
      |a| * (tail (j+1)-tail (j+d+1)) := by
  have h := phase_lipschitz a (liftedOrbit (j+d+1)-liftedOrbit (j+1))
    ((16^d-1)*16^j*Real.pi)
  have heq : (16^d-1)*16^j*Real.pi -
      (liftedOrbit (j+d+1)-liftedOrbit (j+1)) = tail (j+d+1)-tail (j+1) := by
    rw [pi_lag_lift_identity]
    ring
  rw [heq, pi_lag_correction_abs] at h
  exact h

def piLagSum (a : ℝ) (J L d : ℕ) : ℂ :=
  ∑ j ∈ Finset.range L, phase a ((16^d-1)*16^(J+j)*Real.pi)

def forcedLagSum (a : ℝ) (J L d : ℕ) : ℂ :=
  ∑ j ∈ Finset.range L, phase a (liftedOrbit (J+j+d+1)-liftedOrbit (J+j+1))

/-- The exact window-tail correction controls the ORIGINAL complex lag sums. -/
theorem pi_lag_sum_transport (a : ℝ) (J L d : ℕ) :
    ‖piLagSum a J L d - forcedLagSum a J L d‖ ≤ |a| *
      ((∑ j ∈ Finset.range d, tail (J+1+j)) -
       (∑ j ∈ Finset.range d, tail (J+L+1+j))) := by
  unfold piLagSum forcedLagSum
  rw [← Finset.sum_sub_distrib]
  calc
    _ ≤ ∑ j ∈ Finset.range L, ‖phase a ((16^d-1)*16^(J+j)*Real.pi) -
        phase a (liftedOrbit (J+j+d+1)-liftedOrbit (J+j+1))‖ := norm_sum_le _ _
    _ ≤ ∑ j ∈ Finset.range L, |a| * (tail (J+j+1)-tail (J+j+d+1)) := by
      apply Finset.sum_le_sum
      intro j hj
      exact pi_lag_character_transport a (J+j) d
    _ = |a| * ∑ j ∈ Finset.range L, (tail (J+1+j)-tail (J+1+j+d)) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro j hj
      simp only [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]
    _ = _ := by
      rw [lag_window_telescope]
      simp only [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]

theorem pi_lag_sum_transport_le_initial_block (a : ℝ) (J L d : ℕ) :
    ‖piLagSum a J L d - forcedLagSum a J L d‖ ≤
      |a| * ∑ j ∈ Finset.range d, tail (J+1+j) := by
  apply (pi_lag_sum_transport a J L d).trans
  apply mul_le_mul_of_nonneg_left _ (abs_nonneg a)
  have hp : 0 ≤ ∑ j ∈ Finset.range d, tail (J+L+1+j) :=
    Finset.sum_nonneg (fun j hj => (tail_pos _).le)
  linarith

/-- A deliberately simple rational telescoping majorant. The paper theorem
uses the sharper integrated beta-kernel bound and improves this constant. -/
theorem tail_succ_telescoping_majorant (n : ℕ) :
    tail (n+1) ≤ (1/32 : ℝ)*(1/((n : ℝ)+1)-1/((n : ℝ)+2)) := by
  have hn : (0 : ℝ) ≤ n := by positivity
  have h1 : (n : ℝ)+1 ≠ 0 := by positivity
  have h2 : (n : ℝ)+2 ≠ 0 := by positivity
  have hb := tail_le_shifted (n+1)
  have heq : 8*((n+1 : ℕ) : ℝ)+1 = 8*(n : ℝ)+9 := by push_cast; ring
  rw [heq] at hb
  apply hb.trans
  have hr : 1/(8*(n : ℝ)+9)^2 ≤ 1/(32*((n : ℝ)+1)*((n : ℝ)+2)) := by
    apply (div_le_div_iff₀ (by positivity) (by positivity)).2
    nlinarith [sq_nonneg (n : ℝ)]
  have hid : 1/(32*((n : ℝ)+1)*((n : ℝ)+2)) =
      (1/32 : ℝ)*(1/((n : ℝ)+1)-1/((n : ℝ)+2)) := by
    field_simp
    ring
  rwa [hid] at hr

theorem tail_block_sum_bound (J d : ℕ) :
    (∑ j ∈ Finset.range d, tail (J+1+j)) ≤
      (1/32 : ℝ)*(1/((J : ℝ)+1)-1/((J : ℝ)+d+1)) := by
  induction d with
  | zero => simp
  | succ d ih =>
    rw [Finset.sum_range_succ]
    have hb := tail_succ_telescoping_majorant (J+d)
    have heq : J+d+1 = J+1+d := by omega
    rw [heq] at hb
    push_cast at hb ⊢
    rw [show (J : ℝ)+((d : ℝ)+1)+1 = (J : ℝ)+d+2 by ring]
    linarith

/-- An unconditional all-start/all-length/all-lag transport budget for the
actual pi-selected source. It bounds a difference of sums, not cancellation. -/
theorem pi_lag_sum_transport_uniform (a : ℝ) (J L d : ℕ) :
    ‖piLagSum a J L d - forcedLagSum a J L d‖ ≤
      |a|/(32*((J : ℝ)+1)) := by
  apply (pi_lag_sum_transport_le_initial_block a J L d).trans
  have hp : 0 ≤ 1/((J : ℝ)+d+1) := by positivity
  have hb := mul_le_mul_of_nonneg_left (tail_block_sum_bound J d) (abs_nonneg a)
  have hr : |a| * ((1/32 : ℝ)*(1/((J : ℝ)+1)-1/((J : ℝ)+d+1))) ≤
      |a| * ((1/32 : ℝ)*(1/((J : ℝ)+1))) := by
    apply mul_le_mul_of_nonneg_left _ (abs_nonneg a)
    apply mul_le_mul_of_nonneg_left _ (by norm_num)
    linarith
  apply hb.trans
  convert hr using 1 <;> simp only [div_eq_mul_inv, mul_inv_rev] <;> ring

/-- Weighted invariant of the alternating binomial pole residues. -/
theorem weighted_binomial_invariant (K : ℕ) :
    (∑ j ∈ Finset.range (K+1), (-1 : ℝ)^j * (K.choose j : ℝ) * 16^j) =
      (-15 : ℝ)^K := by
  have h := add_pow (-16 : ℝ) 1 K
  norm_num only [neg_add_cancel_left, one_pow, mul_one] at h
  calc
    _ = ∑ j ∈ Finset.range (K+1), (-16 : ℝ)^j * (K.choose j : ℝ) := by
      apply Finset.sum_congr rfl
      intro j hj
      rw [show (-16 : ℝ) = (-1)*16 by norm_num, mul_pow]
      ring
    _ = (-15 : ℝ)^K := by simpa only [show (-16 : ℝ)+1 = -15 by norm_num] using h.symm

theorem weighted_binomial_invariant_ne_zero (K : ℕ) :
    (∑ j ∈ Finset.range (K+1), (-1 : ℝ)^j * (K.choose j : ℝ) * 16^j) ≠ 0 := by
  rw [weighted_binomial_invariant]
  exact pow_ne_zero K (by norm_num)

end ObservationalSUCC.PiSourceGenesis
