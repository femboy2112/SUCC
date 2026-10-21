import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Analysis.Normed.Group.AddCircle
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

/-!
# Exact Bailey–Crandall forcing and its analytic tail

The rational function below is the forcing in Bailey–Crandall's hexadecimal
pi iteration. No normality, BBP identity, or source-identification axiom is
assumed. Statements mentioning an infinite series concern this explicitly
defined rational sequence. The final identification with `Real.pi` is a
separate proof obligation unless a BBP theorem is supplied explicitly.
-/

namespace ObservationalSUCC.BaileyCrandall

noncomputable section

def numerator (x : ℝ) : ℝ := 120 * x ^ 2 - 89 * x + 16

def denominator (x : ℝ) : ℝ :=
  (2*x-1) * (4*x-1) * (8*x-7) * (8*x-3)

def forcing (x : ℝ) : ℝ := numerator x / denominator x

theorem denominator_expanded (x : ℝ) :
    denominator x = 512*x^4 - 1024*x^3 + 712*x^2 - 206*x + 21 := by
  unfold denominator
  ring

theorem denominator_pos {x : ℝ} (hx : 1 ≤ x) : 0 < denominator x := by
  unfold denominator
  have h1 : 0 < 2*x-1 := by linarith
  have h2 : 0 < 4*x-1 := by linarith
  have h3 : 0 < 8*x-7 := by linarith
  have h4 : 0 < 8*x-3 := by linarith
  positivity

theorem numerator_pos {x : ℝ} (hx : 1 ≤ x) : 0 < numerator x := by
  have hid : numerator x = 120*(x-1)^2 + 151*(x-1) + 47 := by
    unfold numerator
    ring
  rw [hid]
  have : 0 ≤ x-1 := by linarith
  positivity

theorem forcing_pos {x : ℝ} (hx : 1 ≤ x) : 0 < forcing x :=
  div_pos (numerator_pos hx) (denominator_pos hx)

/-- Exact cancellation of the four BBP fractions, with the correct shift. -/
theorem forcing_bbp_fractions {x : ℝ} (hx : 1 ≤ x) :
    forcing x = 4/(8*x-7) - 2/(8*x-4) - 1/(8*x-3) - 1/(8*x-2) := by
  have h1 : 2*x-1 ≠ 0 := by linarith
  have h2 : 4*x-1 ≠ 0 := by linarith
  have h3 : 8*x-7 ≠ 0 := by linarith
  have h4 : 8*x-3 ≠ 0 := by linarith
  have h5 : 8*x-4 ≠ 0 := by linarith
  have h6 : 8*x-2 ≠ 0 := by linarith
  unfold forcing numerator denominator
  field_simp
  <;> ring

/-- Sharp uniform constant: equality occurs at x=1. -/
theorem forcing_le_sharp {x : ℝ} (hx : 1 ≤ x) :
    forcing x ≤ (47/15) / x^2 := by
  have hden := denominator_pos hx
  have hxpos : 0 < x := by linarith
  have hu : 0 ≤ x-1 := by linarith
  have hpoly : 0 ≤ 22264*(x-1)^4 + 42263*(x-1)^3 +
      26429*(x-1)^2 + 5443*(x-1) := by positivity
  have hid : 47*denominator x - 15*x^2*numerator x =
      22264*(x-1)^4 + 42263*(x-1)^3 + 26429*(x-1)^2 + 5443*(x-1) := by
    unfold denominator numerator
    ring
  unfold forcing
  apply (div_le_div_iff₀ hden (sq_pos_of_pos hxpos)).2
  nlinarith [hpoly]

theorem forcing_le_eight {x : ℝ} (hx : 1 ≤ x) :
    forcing x ≤ 8 / x^2 := by
  apply (forcing_le_sharp hx).trans
  apply div_le_div_of_nonneg_right
  · norm_num
  · positivity

theorem forcing_at_one : forcing 1 = 47/15 := by
  norm_num [forcing, numerator, denominator]

/-- The sharp constant is necessary on the full x>=1 domain. -/
theorem sharp_constant_necessary (C : ℝ)
    (h : ∀ x : ℝ, 1 ≤ x → forcing x ≤ C/x^2) : 47/15 ≤ C := by
  simpa [forcing_at_one] using h 1 (by norm_num)

theorem forcing_lower {x : ℝ} (hx : 1 ≤ x) :
    (15/64) / x^2 ≤ forcing x := by
  have hden := denominator_pos hx
  have hxpos : 0 < x := by linarith
  have hu : 0 ≤ x-1 := by linarith
  have hpoly : 0 ≤ 9664*(x-1)^3 + 19336*(x-1)^2 + 12770*(x-1) + 2783 := by
    positivity
  have hid : 64*x^2*numerator x - 15*denominator x =
      9664*(x-1)^3 + 19336*(x-1)^2 + 12770*(x-1) + 2783 := by
    unfold denominator numerator
    ring
  unfold forcing
  apply (div_le_div_iff₀ (sq_pos_of_pos hxpos) hden).2
  nlinarith [hpoly]

theorem forcing_succ_lt {x : ℝ} (hx : 1 ≤ x) :
    forcing (x+1) < forcing x := by
  have hp := denominator_pos hx
  have hp' := denominator_pos (show 1 ≤ x+1 by linarith)
  have hu : 0 ≤ x-1 := by linarith
  have hpoly : 0 < 122880*(x-1)^5 + 662016*(x-1)^4 +
      1360896*(x-1)^3 + 1330440*(x-1)^2 + 620136*(x-1) + 110709 := by
    positivity
  have hid : numerator x * denominator (x+1) - numerator (x+1) * denominator x =
      122880*(x-1)^5 + 662016*(x-1)^4 + 1360896*(x-1)^3 +
      1330440*(x-1)^2 + 620136*(x-1) + 110709 := by
    unfold denominator numerator
    ring
  unfold forcing
  apply (div_lt_div_iff₀ hp' hp).2
  nlinarith [hpoly]

/-- A shifted bound with the correct leading asymptotic constant. -/
theorem forcing_le_shifted {x : ℝ} (hx : 1 ≤ x) :
    forcing x ≤ 15/(8*x-7)^2 := by
  have hden := denominator_pos hx
  have hxpos : 0 < 8*x-7 := by linarith
  have hu : 0 ≤ x-1 := by linarith
  have hpoly : 0 ≤ 3776*(x-1)^3 + 5136*(x-1)^2 + 2007*(x-1) + 178 := by
    positivity
  have hid : 15*denominator x - (8*x-7)^2*numerator x =
      3776*(x-1)^3 + 5136*(x-1)^2 + 2007*(x-1) + 178 := by
    unfold denominator numerator
    ring
  unfold forcing
  apply (div_le_div_iff₀ hden (sq_pos_of_pos hxpos)).2
  nlinarith [hpoly]

theorem forcing_nat_add_le (n k : ℕ) :
    forcing ((n : ℝ)+k+1) ≤ forcing ((n : ℝ)+1) := by
  induction k with
  | zero => simp
  | succ k ih =>
    have hn : (0:ℝ) ≤ n := by positivity
    have hk : (0:ℝ) ≤ k := by positivity
    have hs := forcing_succ_lt (x := (n:ℝ)+k+1) (by linarith)
    simpa only [Nat.cast_succ, add_assoc] using hs.le.trans ih

def tailTerm (n k : ℕ) : ℝ :=
  (1/16 : ℝ)^(k+1) * forcing ((n : ℝ) + k + 1)

def tail (n : ℕ) : ℝ := ∑' k : ℕ, tailTerm n k

theorem tailTerm_pos (n k : ℕ) : 0 < tailTerm n k := by
  unfold tailTerm
  have hn : (0:ℝ) ≤ n := by positivity
  have hk : (0:ℝ) ≤ k := by positivity
  have hf : 0 < forcing ((n : ℝ)+k+1) := forcing_pos (by linarith)
  positivity

theorem tailTerm_le (n k : ℕ) :
    tailTerm n k ≤ (1/16 : ℝ)^(k+1) * ((47/15)/((n : ℝ)+1)^2) := by
  unfold tailTerm
  apply mul_le_mul_of_nonneg_left _ (by positivity)
  have hk : (0:ℝ) ≤ k := by positivity
  have hn : (0:ℝ) ≤ n := by positivity
  apply (forcing_le_sharp (show (1:ℝ) ≤ (n:ℝ)+k+1 by linarith)).trans
  apply div_le_div_of_nonneg_left (by norm_num) (by positivity)
  nlinarith

theorem geometric_weight_hasSum :
    HasSum (fun k : ℕ => (1/16 : ℝ)^(k+1)) (1/15 : ℝ) := by
  convert (hasSum_geometric_of_lt_one (r := (1/16 : ℝ)) (by norm_num)
    (by norm_num)).mul_right (1/16 : ℝ) using 1 <;> norm_num [pow_succ]

theorem tail_summable (n : ℕ) : Summable (tailTerm n) := by
  exact Summable.of_nonneg_of_le (fun k => (tailTerm_pos n k).le)
    (tailTerm_le n) (geometric_weight_hasSum.summable.mul_right _)

theorem tail_pos (n : ℕ) : 0 < tail n := by
  exact tsum_pos (tail_summable n) (fun k => (tailTerm_pos n k).le) 0 (tailTerm_pos n 0)

/-- Improved explicit analytic tail bound, with no finite-truncation premise. -/
theorem tail_le_sharp (n : ℕ) : tail n ≤ 47/(225*((n : ℝ)+1)^2) := by
  have h := tsum_le_tsum (tailTerm_le n) (tail_summable n)
    (geometric_weight_hasSum.summable.mul_right ((47/15)/((n : ℝ)+1)^2))
  have hs := (geometric_weight_hasSum.mul_right ((47/15)/((n : ℝ)+1)^2)).tsum_eq
  rw [hs] at h
  change tail n ≤ _ at h
  have hn : (n : ℝ)+1 ≠ 0 := by positivity
  calc
    tail n ≤ (1/15)*((47/15)/((n : ℝ)+1)^2) := h
    _ = 47/(225*((n : ℝ)+1)^2) := by field_simp; ring

/-- The original handoff bound is a consequence of the stronger one. -/
theorem tail_le_eight (n : ℕ) : tail n ≤ 8/(15*((n : ℝ)+1)^2) := by
  apply (tail_le_sharp n).trans
  have hden : 0 < ((n : ℝ)+1)^2 := by positivity
  apply (div_le_div_iff₀ (by positivity) (by positivity)).2
  nlinarith

theorem tail_recursion (n : ℕ) :
    16 * tail n = forcing ((n : ℝ)+1) + tail (n+1) := by
  have hsplit := tsum_eq_zero_add (tail_summable n)
  have hshift : (∑' k : ℕ, tailTerm n (k+1)) = (1/16 : ℝ) * tail (n+1) := by
    rw [tail, ← tsum_mul_left]
    apply tsum_congr
    intro k
    simp only [tailTerm, Nat.cast_add, Nat.cast_one, pow_succ]
    have harg : (n:ℝ)+((k:ℝ)+1)+1 = ((n:ℝ)+1)+k+1 := by ring
    rw [harg]
    ring
  rw [hshift] at hsplit
  simp only [tailTerm, Nat.cast_zero, add_zero, zero_add, pow_one] at hsplit
  change tail n = _ at hsplit
  linarith

/-- The first omitted source coefficient gives a sharper rational enclosure. -/
theorem tail_le_source (n : ℕ) : tail n ≤ forcing ((n : ℝ)+1)/15 := by
  have hp : ∀ k, tailTerm n k ≤ (1/16 : ℝ)^(k+1)*forcing ((n : ℝ)+1) := by
    intro k
    exact mul_le_mul_of_nonneg_left (forcing_nat_add_le n k) (by positivity)
  have h := tsum_le_tsum hp (tail_summable n)
    (geometric_weight_hasSum.summable.mul_right (forcing ((n : ℝ)+1)))
  rw [(geometric_weight_hasSum.mul_right (forcing ((n : ℝ)+1))).tsum_eq] at h
  change tail n ≤ _ at h
  convert h using 1 <;> ring

theorem tail_gt_source (n : ℕ) : forcing ((n : ℝ)+1)/16 < tail n := by
  have ht := tail_recursion n
  have hp := tail_pos (n+1)
  linarith

theorem tail_le_shifted (n : ℕ) : tail n ≤ 1/(8*(n : ℝ)+1)^2 := by
  have hn : (0:ℝ) ≤ n := by positivity
  have hf := forcing_le_shifted (x := (n:ℝ)+1) (by linarith)
  have heq : 8*((n:ℝ)+1)-7 = 8*(n:ℝ)+1 := by ring
  rw [heq] at hf
  apply (tail_le_source n).trans
  have hd : 0 < (8*(n:ℝ)+1)^2 := by positivity
  apply (div_le_div_iff₀ (by norm_num) hd).2
  have hb := (le_div_iff₀ hd).1 hf
  nlinarith

/-- The recurrence before reducing modulo one. -/
def liftedOrbit : ℕ → ℝ
  | 0 => 0
  | n+1 => 16 * liftedOrbit n + forcing ((n : ℝ)+1)

theorem lifted_orbit_tail_identity (n : ℕ) :
    liftedOrbit n + tail n = 16^n * tail 0 := by
  induction n with
  | zero => simp [liftedOrbit]
  | succ n ih =>
    rw [liftedOrbit, pow_succ]
    have ht := tail_recursion n
    nlinarith

/-- A genuine clock-inclusive semiconjugacy; no stationary clock is asserted. -/
theorem corrected_clock_semiconjugacy (n : ℕ) (x : ℝ) :
    (16*x + forcing ((n : ℝ)+1)) + tail (n+1) = 16*(x+tail n) := by
  have ht := tail_recursion n
  linarith

def seriesValue : ℝ := 16 * tail 0

/-- The standard BBP coefficient series is exactly the defined source value. -/
theorem series_bbp_hasSum :
    HasSum (fun k : ℕ => (1/16 : ℝ)^k *
      (4/(8*(k:ℝ)+1) - 2/(8*(k:ℝ)+4) - 1/(8*(k:ℝ)+5) - 1/(8*(k:ℝ)+6)))
      seriesValue := by
  have h := (tail_summable 0).hasSum.mul_left (16 : ℝ)
  change HasSum (fun k => 16*tailTerm 0 k) seriesValue at h
  apply h.congr_fun
  intro k
  have hk : (0:ℝ) ≤ k := by positivity
  simp only [tailTerm, Nat.cast_zero, zero_add]
  rw [forcing_bbp_fractions (by linarith : (1:ℝ) ≤ (k:ℝ)+1), pow_succ]
  have h1 : 8*((k:ℝ)+1)-7 = 8*(k:ℝ)+1 := by ring
  have h2 : 8*((k:ℝ)+1)-4 = 8*(k:ℝ)+4 := by ring
  have h3 : 8*((k:ℝ)+1)-3 = 8*(k:ℝ)+5 := by ring
  have h4 : 8*((k:ℝ)+1)-2 = 8*(k:ℝ)+6 := by ring
  rw [h1, h2, h3, h4]
  ring

/-- Source-neutral transport of an independently proved standard BBP sum. -/
theorem seriesValue_eq_of_hasSum (z : ℝ)
    (h : HasSum (fun k : ℕ => (1/16 : ℝ)^k *
      (4/(8*(k:ℝ)+1) - 2/(8*(k:ℝ)+4) - 1/(8*(k:ℝ)+5) - 1/(8*(k:ℝ)+6))) z) :
    seriesValue = z := series_bbp_hasSum.unique h

theorem series_orbit_transport (n : ℕ) :
    16^n * seriesValue = liftedOrbit (n+1) + tail (n+1) := by
  rw [lifted_orbit_tail_identity, seriesValue, pow_succ]
  ring

/-- Exact orbit in the circle group R/Z; no choice of a fractional representative. -/
def circleOrbit (n : ℕ) : AddCircle (1 : ℝ) := liftedOrbit n

theorem circle_orbit_recursion (n : ℕ) :
    circleOrbit (n+1) = (16 : ℕ) • circleOrbit n +
      (forcing ((n : ℝ)+1) : AddCircle (1 : ℝ)) := by
  simp only [circleOrbit, liftedOrbit, AddCircle.coe_add]
  rw [← AddCircle.coe_nsmul, nsmul_eq_mul]
  norm_num

theorem circle_series_transport (n : ℕ) :
    dist (circleOrbit (n+1)) ((16^n * seriesValue : ℝ) : AddCircle (1 : ℝ)) ≤
      47/(225*((n : ℝ)+2)^2) := by
  rw [dist_comm, series_orbit_transport, dist_eq_norm]
  simp only [circleOrbit, AddCircle.coe_add, add_sub_cancel_left]
  have hq : ‖(tail (n+1) : AddCircle (1 : ℝ))‖ ≤ |tail (n+1)| := by
    simpa only [Real.norm_eq_abs] using
      (quotient_norm_mk_le' (AddSubgroup.zmultiples (1 : ℝ)) (tail (n+1)))
  rw [abs_of_pos (tail_pos (n+1))] at hq
  apply hq.trans
  simpa only [Nat.cast_add, Nat.cast_one, add_assoc, one_add_one_eq_two] using
    tail_le_sharp (n+1)

/-- Classical BBP source identity is explicit proof debt in this specialization.
It is neither normality nor a newly introduced axiom. -/
theorem pi_circle_transport (bbp_identity : seriesValue = Real.pi) (n : ℕ) :
    dist (circleOrbit (n+1)) ((16^n * Real.pi : ℝ) : AddCircle (1 : ℝ)) ≤
      47/(225*((n : ℝ)+2)^2) := by
  rw [← bbp_identity]
  exact circle_series_transport n

end

end ObservationalSUCC.BaileyCrandall
