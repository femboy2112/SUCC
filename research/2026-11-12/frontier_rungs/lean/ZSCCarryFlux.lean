import Mathlib.Algebra.Order.Floor
import Mathlib.Algebra.Polynomial.Eval.Defs
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Data.Real.Basic
import Mathlib.MeasureTheory.Integral.FundThmCalculus
import Mathlib.Analysis.SpecialFunctions.Log.Deriv
import Mathlib.Analysis.SpecialFunctions.Log.Base
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring
import Mathlib.Tactic.FunProp

/-!
# Kernel checks for small exact lemmas of ZSC (CARRY_FLUX.md, 2026-11-11 dossier)

Source dossier: `research/2026-11-11/innovation_arithmetic_decoupling/CARRY_FLUX.md`.

* L1  ZSC-06(d): partial fraction of the null relation (any field), the polynomial
  factorisations of ZSC-06(a)/(d)/(f)3 in `ℚ[X]`, the coefficient vector `A_0`, the
  vanishing of `∫_0^1 (z²-4z+2)/m(z) dz` and of `∫_0^1 g_0(z)/(16-z⁸) dz` over `ℝ`, and
  `L(A_0) = Σ_j A_j v_j = 0` with `v_j` in the file's integral form.
* L2  ZSC-02 locality lemma, both parts, for every real `ξ`, every position `n` and every
  run length `k`; plus the two-digit form `d0 = ⌊16y⌋`, `d1 = ⌊16(16y - d0)⌋`, `0 ≤ y < 1`.
* L3  ZSC-03 renewal lemma: the abstract arithmetic kernel (every real seed, any forcing
  that is nonnegative and at most `r(n+1)` from `n+1` on), the four-pole forcing bounds
  (`r(n+1) > 0`, `r` decreasing, `r(n+1) ≤ 15/((8n+1)(8n+2))`), `J(n)` defined with the
  real base-16 logarithm, `J(n) ≥ ⌊log_4 2n⌋`, its integer form, and the renewal lemma itself.

Not formalised here: the BBP series form `v_j = Σ_k 16^(-k-1)/(8k+j)`, Baker rigidity
(ZSC-06(e)), the RIO-09 upper window for the zero run, ZSC-03 Corollaries 1-2, and every
statistical, Diophantine or asymptotic statement of the dossier.  The four-pole forcing is
encoded by its closed form `rPi`; that it equals `∫_0^1 z^(8n-8) g_π(z) dz` is not formalised.
Theorems whose name begins with `refute_` prove the NEGATION of a mutated (false) nearby
statement; they are controls, not dossier claims.
-/

open Polynomial

namespace ObservationalSUCC.ZSCCarryFlux

/-! ## L1 — ZSC-06(d) null relation, algebraic part -/

/-- ZSC-06(d), first display: `(z²-4z+2)/m(z) = z/(z²-2) - (z-1)/(z²-2z+2)` with
`m = (2-z²)(z²-2z+2)`, in every field, wherever the two denominators are nonzero. -/
theorem zsc06_null_partial_fraction {K : Type*} [Field K] (z : K)
    (h1 : z ^ 2 - 2 ≠ 0) (h2 : z ^ 2 - 2 * z + 2 ≠ 0) :
    (z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) =
      z / (z ^ 2 - 2) - (z - 1) / (z ^ 2 - 2 * z + 2) := by
  have h3 : (2 - z ^ 2) ≠ 0 := by
    intro h; apply h1; linear_combination -h
  rw [div_sub_div _ _ h1 h2, div_eq_div_iff (mul_ne_zero h3 h2) (mul_ne_zero h1 h2)]
  ring

/-- ZSC-06(a): `16 - z⁸ = K(z)·m(z)`, `K = (z²+2)(z²+2z+2)`, `m = (2-z²)(z²-2z+2)`. -/
theorem zsc06_sixteen_factorisation :
    (16 - X ^ 8 : ℚ[X]) =
      ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * ((2 - X ^ 2) * (X ^ 2 - 2 * X + 2)) := by
  ring

/-- ZSC-06(a): the authentic numerator `g_π = 4 - 2z³ - z⁴ - z⁵ = K(z)(1-z)`. -/
theorem zsc06_authentic_numerator :
    ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (1 - X : ℚ[X]) = 4 - 2 * X ^ 3 - X ^ 4 - X ^ 5 := by
  ring

/-- ZSC-06(d): `g_0 = K(z)(z²-4z+2) = 8 - 8z - 4z² - 8z³ - 2z⁴ - 2z⁵ + z⁶`. -/
theorem zsc06_null_numerator :
    ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (X ^ 2 - 4 * X + 2 : ℚ[X]) =
      8 - 8 * X - 4 * X ^ 2 - 8 * X ^ 3 - 2 * X ^ 4 - 2 * X ^ 5 + X ^ 6 := by
  ring

/-- The coefficient vector `A_0 = (8,-8,-4,-8,-2,-2,1,0)`: entry `i` is the coefficient of
`z^i` (`0 ≤ i ≤ 7`); every index `i ≥ 8` is `0`. -/
def A0 : ℕ → ℚ
  | 0 => 8
  | 1 => -8
  | 2 => -4
  | 3 => -8
  | 4 => -2
  | 5 => -2
  | 6 => 1
  | _ => 0

/-- ZSC-06(d): `g_0 = Σ_{i<8} A_0(i) z^i`. -/
theorem zsc06_null_coefficient_vector :
    ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (X ^ 2 - 4 * X + 2 : ℚ[X]) =
      ∑ i ∈ Finset.range 8, C (A0 i) * X ^ i := by
  simp [Finset.sum_range_succ, A0, map_ofNat C]
  ring

/-- ZSC-06(d), coefficientwise: for every `i`, the `z^i` coefficient of
`K(z)(z²-4z+2)` is `A_0(i)`; so `g_0` has proper form (degree `≤ 7`) and vector `A_0`. -/
theorem zsc06_null_coeff (i : ℕ) :
    (((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (X ^ 2 - 4 * X + 2 : ℚ[X])).coeff i = A0 i := by
  rw [zsc06_null_coefficient_vector, finset_sum_coeff]
  simp only [coeff_C_mul_X_pow]
  rw [Finset.sum_ite_eq]
  split_ifs with h
  · rfl
  · obtain ⟨k, rfl⟩ : ∃ k, i = k + 8 := ⟨i - 8, by simp at h; omega⟩
    rfl

/-- ZSC-06(f)3: `g_H = (16-z⁸)(3-2z) + g_0 = 2z⁹ - 3z⁸ + z⁶ - 2z⁵ - 2z⁴ - 8z³ - 4z² - 40z + 56`. -/
theorem zsc06_hostile_numerator :
    (16 - X ^ 8 : ℚ[X]) * (3 - 2 * X) +
        (8 - 8 * X - 4 * X ^ 2 - 8 * X ^ 3 - 2 * X ^ 4 - 2 * X ^ 5 + X ^ 6) =
      2 * X ^ 9 - 3 * X ^ 8 + X ^ 6 - 2 * X ^ 5 - 2 * X ^ 4 - 8 * X ^ 3 - 4 * X ^ 2 - 40 * X + 56 := by
  ring

/-- ZSC-06(d), second display: `∫_0^1 (z²-4z+2)/m(z) dz = 0`, by the antiderivative
`½ log(2-z²) - ½ log(z²-2z+2)` (here `|z²-2| = 2-z²` on `[0,1]`). -/
theorem zsc06_null_integral :
    ∫ z in (0:ℝ)..1, (z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) = 0 := by
  have hA : ∀ x ∈ Set.uIcc (0:ℝ) 1, 2 - x ^ 2 ≠ 0 := by
    intro x hx
    rw [Set.uIcc_of_le zero_le_one] at hx
    obtain ⟨h0, h1⟩ := hx
    nlinarith
  have hB : ∀ x : ℝ, x ^ 2 - 2 * x + 2 ≠ 0 := by
    intro x; nlinarith [sq_nonneg (x - 1)]
  have hderiv : ∀ x ∈ Set.uIcc (0:ℝ) 1, HasDerivAt
      (fun z => (1 / 2) * Real.log (2 - z ^ 2) - (1 / 2) * Real.log (z ^ 2 - 2 * z + 2))
      ((x ^ 2 - 4 * x + 2) / ((2 - x ^ 2) * (x ^ 2 - 2 * x + 2))) x := by
    intro x hx
    have d1 : HasDerivAt (fun z : ℝ => 2 - z ^ 2) (-(2 * x)) x := by
      simpa using (hasDerivAt_pow 2 x).const_sub 2
    have d2 : HasDerivAt (fun z : ℝ => z ^ 2 - 2 * z + 2) (2 * x - 2) x := by
      have := ((hasDerivAt_pow 2 x).sub ((hasDerivAt_id x).const_mul 2)).add_const 2
      simpa using this
    have := ((d1.log (hA x hx)).const_mul (1 / 2)).sub ((d2.log (hB x)).const_mul (1 / 2))
    convert this using 1
    field_simp [hA x hx, hB x]
    ring
  have hcont : ContinuousOn
      (fun x : ℝ => (x ^ 2 - 4 * x + 2) / ((2 - x ^ 2) * (x ^ 2 - 2 * x + 2)))
      (Set.uIcc 0 1) := by
    apply ContinuousOn.div (by fun_prop) (by fun_prop)
    intro x hx
    exact mul_ne_zero (hA x hx) (hB x)
  rw [intervalIntegral.integral_eq_sub_of_hasDerivAt hderiv hcont.intervalIntegrable]
  norm_num

/-- ZSC-06(d): `∫_0^1 g_0(z)/(16-z⁸) dz = 0` (the BBP series form
`v_j = Σ_k 16^(-k-1)/(8k+j)` is not formalised). -/
theorem zsc06_null_period_integral :
    ∫ z in (0:ℝ)..1,
        (8 - 8 * z - 4 * z ^ 2 - 8 * z ^ 3 - 2 * z ^ 4 - 2 * z ^ 5 + z ^ 6) / (16 - z ^ 8) = 0 := by
  refine Eq.trans ?_ zsc06_null_integral
  apply intervalIntegral.integral_congr
  intro x hx
  rw [Set.uIcc_of_le zero_le_one] at hx
  obtain ⟨h0, h1⟩ := hx
  have hA : 2 - x ^ 2 ≠ 0 := by nlinarith
  have hB : x ^ 2 - 2 * x + 2 ≠ 0 := by nlinarith [sq_nonneg (x - 1)]
  have hK : (x ^ 2 + 2) * (x ^ 2 + 2 * x + 2) ≠ 0 := by
    apply mul_ne_zero <;> nlinarith [sq_nonneg (x + 1)]
  have h16 : (16 : ℝ) - x ^ 8 ≠ 0 := by
    have : (16 : ℝ) - x ^ 8 = ((x ^ 2 + 2) * (x ^ 2 + 2 * x + 2)) *
        ((2 - x ^ 2) * (x ^ 2 - 2 * x + 2)) := by ring
    rw [this]; exact mul_ne_zero hK (mul_ne_zero hA hB)
  simp only
  rw [div_eq_div_iff h16 (mul_ne_zero hA hB)]
  ring

/-- **ZSC-06(d): `L(A_0) = Σ_j A_j v_j = 0`** with the periods in the file's integral form
`v_j = ∫_0^1 z^(j-1)/(16-z⁸) dz` (here indexed by `i = j-1 = 0,…,7`). -/
theorem zsc06_L_A0_eq_zero :
    ∑ i ∈ Finset.range 8, (A0 i : ℝ) * ∫ z in (0:ℝ)..1, z ^ i / (16 - z ^ 8) = 0 := by
  have hint : ∀ i : ℕ, IntervalIntegrable (fun z : ℝ => z ^ i / (16 - z ^ 8))
      MeasureTheory.volume 0 1 := by
    intro i
    apply ContinuousOn.intervalIntegrable
    apply ContinuousOn.div (by fun_prop) (by fun_prop)
    intro x hx
    rw [Set.uIcc_of_le zero_le_one] at hx
    have : x ^ 8 ≤ 1 := pow_le_one₀ hx.1 hx.2
    intro h; linarith
  simp_rw [← intervalIntegral.integral_const_mul]
  rw [← intervalIntegral.integral_finset_sum (fun i _ => (hint i).const_mul _)]
  refine Eq.trans ?_ zsc06_null_period_integral
  apply intervalIntegral.integral_congr
  intro x _
  simp [Finset.sum_range_succ, A0]
  ring

/-! ## L2 — ZSC-02 locality lemma -/

/-- Base-16 digit `d_i(y) = ⌊16 {16^i y}⌋` (`{·}` = `Int.fract`). -/
noncomputable def hexDigit (y : ℝ) (i : ℕ) : ℤ := ⌊16 * Int.fract (16 ^ i * y)⌋

lemma hexDigit_nonneg (y : ℝ) (i : ℕ) : 0 ≤ hexDigit y i := by
  unfold hexDigit
  apply Int.floor_nonneg.mpr
  have := Int.fract_nonneg (16 ^ i * y)
  linarith

lemma hexDigit_le (y : ℝ) (i : ℕ) : hexDigit y i ≤ 15 := by
  unfold hexDigit
  have h := Int.fract_lt_one (16 ^ i * y)
  have : ⌊16 * Int.fract (16 ^ i * y)⌋ < 16 := Int.floor_lt.mpr (by push_cast; linarith)
  omega

lemma hexDigit_shift (ξ : ℝ) (n i : ℕ) : hexDigit ξ (n + i) = hexDigit (16 ^ n * ξ) i := by
  unfold hexDigit
  rw [show (16 : ℝ) ^ (n + i) * ξ = 16 ^ i * (16 ^ n * ξ) by ring]

/-- One base-16 shift: `16 {16^i y} = d_i + {16^(i+1) y}`. -/
lemma fract_step (y : ℝ) (i : ℕ) :
    16 * Int.fract (16 ^ i * y) = hexDigit y i + Int.fract (16 ^ (i + 1) * y) := by
  unfold hexDigit
  have e : (16 : ℝ) ^ (i + 1) * y =
      16 * Int.fract (16 ^ i * y) + ((16 * ⌊16 ^ i * y⌋ : ℤ) : ℝ) := by
    have := Int.floor_add_fract (16 ^ i * y)
    push_cast
    rw [pow_succ]
    linear_combination (-16) * this
  rw [e, Int.fract_add_int]
  exact (Int.floor_add_fract _).symm

/-- Run identity: if `d_0 = … = d_(k-1) = j` then `15{y} - j = (15{16^k y} - j)/16^k`. -/
lemma run_identity (y : ℝ) (j : ℤ) :
    ∀ k : ℕ, (∀ i < k, hexDigit y i = j) →
      15 * Int.fract y - j = (15 * Int.fract (16 ^ k * y) - j) / 16 ^ k := by
  intro k
  induction k with
  | zero => intro _; simp
  | succ k ih =>
    intro h
    have hk : hexDigit y k = j := h k (Nat.lt_succ_self k)
    rw [ih (fun i hi => h i (Nat.lt_succ_of_lt hi))]
    have step := fract_step y k
    rw [hk] at step
    rw [div_eq_div_iff (by positivity) (by positivity)]
    linear_combination (15 * (16 : ℝ) ^ k) * step

/-- ZSC-02 Lemma 1 at position 0: a run `d_0 = … = d_(k-1)` forces `‖15 y‖ ≤ 15·16^(-k)`,
with `‖t‖ = |t - round t|` the distance to the nearest integer. -/
theorem zsc02_locality_run_zero (y : ℝ) (k : ℕ) (h : ∀ i < k, hexDigit y i = hexDigit y 0) :
    |15 * y - round (15 * y)| ≤ 15 / 16 ^ k := by
  have hid := run_identity y (hexDigit y 0) k h
  have hj0 : (0 : ℝ) ≤ hexDigit y 0 := by exact_mod_cast hexDigit_nonneg y 0
  have hj15 : (hexDigit y 0 : ℝ) ≤ 15 := by exact_mod_cast hexDigit_le y 0
  have hF0 := Int.fract_nonneg (16 ^ k * y)
  have hF1 := Int.fract_lt_one (16 ^ k * y)
  have hpos : (0 : ℝ) < 16 ^ k := by positivity
  calc |15 * y - round (15 * y)|
      ≤ |15 * y - ((15 * ⌊y⌋ + hexDigit y 0 : ℤ) : ℝ)| := round_le _ _
    _ = |15 * Int.fract y - hexDigit y 0| := by
        rw [← Int.self_sub_floor]; push_cast; ring_nf
    _ = |15 * Int.fract (16 ^ k * y) - hexDigit y 0| / 16 ^ k := by
        rw [hid, abs_div, abs_of_pos hpos]
    _ ≤ 15 / 16 ^ k := by
        rw [div_le_div_iff_of_pos_right hpos, abs_le]
        constructor <;> linarith

/-- **ZSC-02 Lemma 1** (file statement, every real `ξ`, every position `n`, every `k`):
if `d_n = d_(n+1) = … = d_(n+k-1)` then `‖15 y_n‖ ≤ 15·16^(-k)`, `y_n = 16^n ξ`. -/
theorem zsc02_locality_run (ξ : ℝ) (n k : ℕ)
    (h : ∀ i < k, hexDigit ξ (n + i) = hexDigit ξ n) :
    |15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| ≤ 15 / 16 ^ k := by
  apply zsc02_locality_run_zero
  intro i hi
  rw [← hexDigit_shift, ← hexDigit_shift, add_zero]
  exact h i hi

/-- ZSC-02 Lemma 2 at position 0: `‖15 y‖ < 1/256` forces `d_0 = d_1`. -/
theorem zsc02_locality_change_zero (y : ℝ) (h : |15 * y - round (15 * y)| < 1 / 256) :
    hexDigit y 0 = hexDigit y 1 := by
  have hf0 := Int.fract_nonneg y
  have hf1 := Int.fract_lt_one y
  obtain ⟨tlo, thi⟩ := abs_lt.mp h
  set t : ℝ := 15 * y - round (15 * y) with ht
  set j : ℤ := round (15 * y) - 15 * ⌊y⌋ with hj
  have key : 15 * Int.fract y = (j : ℝ) + t := by
    rw [ht, hj, ← Int.self_sub_floor]; push_cast; ring
  have jlo : -1 < j := by
    have : ((-1 : ℤ) : ℝ) < j := by push_cast; linarith
    exact_mod_cast this
  have jhi : j < 16 := by
    have : (j : ℝ) < ((16 : ℤ) : ℝ) := by push_cast; linarith
    exact_mod_cast this
  -- the two margins of the file: `j + 256 t ∈ [0, 15)`
  have C : 0 ≤ (j : ℝ) + 256 * t := by
    rcases (show j = 0 ∨ 1 ≤ j by omega) with h0 | h1
    · have : (j : ℝ) = 0 := by exact_mod_cast h0
      rw [this] at key ⊢; linarith
    · have : (1 : ℝ) ≤ j := by exact_mod_cast h1
      linarith
  have D : (j : ℝ) + 256 * t < 15 := by
    rcases (show j = 15 ∨ j ≤ 14 by omega) with h0 | h1
    · have : (j : ℝ) = 15 := by exact_mod_cast h0
      rw [this] at key ⊢; linarith
    · have : (j : ℝ) ≤ 14 := by exact_mod_cast h1
      linarith
  have hj0 : (0 : ℝ) ≤ j := by exact_mod_cast (show 0 ≤ j by omega)
  have hj15 : (j : ℝ) ≤ 15 := by exact_mod_cast (show j ≤ 15 by omega)
  have d0 : ⌊16 * Int.fract y⌋ = j := by
    rw [Int.floor_eq_iff]; constructor <;> linarith
  have e : (16 : ℝ) ^ 1 * y = 16 * Int.fract y + ((16 * ⌊y⌋ : ℤ) : ℝ) := by
    have := Int.floor_add_fract y
    push_cast; linear_combination (-16) * this
  have d1 : ⌊16 * Int.fract ((16 : ℝ) ^ 1 * y)⌋ = j := by
    rw [e, Int.fract_add_int, ← Int.self_sub_floor, d0, Int.floor_eq_iff]
    constructor <;> linarith
  unfold hexDigit
  rw [d1, pow_zero, one_mul, d0]

/-- **ZSC-02 Lemma 2** (file statement, every real `ξ`, every position `n`):
if `‖15 y_n‖ < 1/256` then `d_n = d_(n+1)`. -/
theorem zsc02_locality_change (ξ : ℝ) (n : ℕ)
    (h : |15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| < 1 / 256) :
    hexDigit ξ n = hexDigit ξ (n + 1) := by
  have := zsc02_locality_change_zero (16 ^ n * ξ) h
  rwa [← hexDigit_shift, ← hexDigit_shift, add_zero] at this

/-- The brief's two-digit form for `0 ≤ y < 1`, `d0 = ⌊16y⌋`, `d1 = ⌊16(16y - d0)⌋`:
(a) `d0 = d1 → ‖15y‖ ≤ 15/256` (the case `k = 2` of Lemma 1);
(b) `‖15y‖ < 1/256 → d0 = d1` (Lemma 2). -/
theorem zsc02_two_digit_form (y : ℝ) (hy0 : 0 ≤ y) (hy1 : y < 1) :
    (⌊16 * y⌋ = ⌊16 * (16 * y - ⌊16 * y⌋)⌋ → |15 * y - round (15 * y)| ≤ 15 / 256) ∧
    (|15 * y - round (15 * y)| < 1 / 256 → ⌊16 * y⌋ = ⌊16 * (16 * y - ⌊16 * y⌋)⌋) := by
  have h0 : hexDigit y 0 = ⌊16 * y⌋ := by
    unfold hexDigit; rw [pow_zero, one_mul, Int.fract_eq_self.mpr ⟨hy0, hy1⟩]
  have h1 : hexDigit y 1 = ⌊16 * (16 * y - ⌊16 * y⌋)⌋ := by
    unfold hexDigit; rw [pow_one, ← Int.self_sub_floor]
  constructor
  · intro hd
    have := zsc02_locality_run_zero y 2 (by
      intro i hi
      interval_cases i
      · rfl
      · rw [h0, h1]; exact hd.symm)
    norm_num at this ⊢
    exact this
  · intro hd
    rw [← h1, ← h0]
    exact zsc02_locality_change_zero y hd

/-! ## L3 — ZSC-03 renewal lemma -/

/-- Abstract renewal kernel (every real seed).  `U (m+1) = 16 U m + r (m+1)` for all `m`;
the carry is `κ_m = ⌊U_m⌋ - 16 ⌊U_(m-1)⌋`.  If the forcing after `n+1` is nonnegative and
at most `r(n+1)`, `κ_(n+1) = 16`, and `(16/15)·16^J·r(n+1) ≤ 1`, then
`κ_(n+2) = … = κ_(n+1+J) = 0`. -/
theorem zsc03_renewal_kernel (U r : ℕ → ℝ) (n J : ℕ)
    (hrec : ∀ m, U (m + 1) = 16 * U m + r (m + 1))
    (hnonneg : ∀ i, 0 ≤ r (n + 1 + i))
    (hle : ∀ i, r (n + 1 + i) ≤ r (n + 1))
    (h16 : ⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16)
    (hJ : 16 / 15 * 16 ^ J * r (n + 1) ≤ 1) :
    ∀ j, 1 ≤ j → j ≤ J → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0 := by
  set ρ := r (n + 1) with hρ
  have hρ0 : 0 ≤ ρ := by simpa using hnonneg 0
  -- the state just after the 16 lies in `[0, ρ)`
  have hfr : U (n + 1) - ⌊U (n + 1)⌋ < ρ := by
    have h1 := hrec n
    have hu := Int.fract_lt_one (U n)
    have hfl : (⌊U (n + 1)⌋ : ℝ) = 16 * ⌊U n⌋ + 16 := by
      have : ⌊U (n + 1)⌋ = 16 * ⌊U n⌋ + 16 := by omega
      rw [this]; push_cast; ring
    rw [hfl, h1, ← hρ]
    rw [← Int.self_sub_floor] at hu
    linarith
  -- invariant: `0 ≤ U(n+1+j) - 16^j ⌊U(n+1)⌋ < ρ (16^(j+1) - 1)/15` while no carry
  have inv : ∀ j, 0 ≤ U (n + 1 + j) - 16 ^ j * ⌊U (n + 1)⌋ ∧
      U (n + 1 + j) - 16 ^ j * ⌊U (n + 1)⌋ < ρ * (16 ^ (j + 1) - 1) / 15 := by
    intro j
    induction j with
    | zero =>
      simp only [add_zero, pow_zero, one_mul]
      refine ⟨by linarith [Int.floor_le (U (n + 1))], by linarith⟩
    | succ j ih =>
      obtain ⟨lo, hi⟩ := ih
      have hr := hrec (n + 1 + j)
      have hn := hnonneg (j + 1)
      have hl := hle (j + 1)
      rw [show n + 1 + (j + 1) = n + 1 + j + 1 by ring] at hn hl ⊢
      rw [hr]
      have e1 : (16 : ℝ) ^ (j + 1) = 16 ^ j * 16 := pow_succ _ _
      have e2 : (16 : ℝ) ^ (j + 1 + 1) = 16 ^ j * 256 := by ring
      rw [e1] at hi
      rw [e2, e1]
      constructor <;> linarith
  intro j hj1 hjJ
  have hfloor : ∀ i, i ≤ J → ⌊U (n + 1 + i)⌋ = 16 ^ i * ⌊U (n + 1)⌋ := by
    intro i hi
    obtain ⟨lo, hi'⟩ := inv i
    rw [Int.floor_eq_iff]
    push_cast
    have hpow : (16 : ℝ) ^ i ≤ 16 ^ J := pow_le_pow_right₀ (by norm_num) hi
    have hc : ρ * (16 ^ (i + 1) - 1) / 15 ≤ 1 := by
      have : ρ * (16 ^ (i + 1) - 1) / 15 ≤ 16 / 15 * 16 ^ J * ρ := by
        rw [pow_succ]; nlinarith
      linarith
    constructor <;> linarith
  obtain ⟨j', rfl⟩ : ∃ j', j = j' + 1 := ⟨j - 1, by omega⟩
  rw [hfloor (j' + 1) hjJ, show n + (j' + 1) = n + 1 + j' by ring, hfloor j' (by omega)]
  ring

/-- The four-pole authentic forcing `r(m) = 4/(8m-7) - 2/(8m-4) - 1/(8m-3) - 1/(8m-2)`
(proper form `A_π = (4,0,0,-2,-1,-1,0,0)`). -/
noncomputable def rPi (m : ℕ) : ℝ :=
  4 / (8 * (m : ℝ) - 7) - 2 / (8 * (m : ℝ) - 4) - 1 / (8 * (m : ℝ) - 3) - 1 / (8 * (m : ℝ) - 2)

lemma rPi_succ (n : ℕ) : rPi (n + 1) =
    4 / (8 * (n : ℝ) + 1) - 2 / (8 * (n : ℝ) + 4) - 1 / (8 * (n : ℝ) + 5) - 1 / (8 * (n : ℝ) + 6) := by
  unfold rPi; push_cast; ring_nf

/-- `r(n+1) > 0` for every `n ≥ 0`. -/
theorem rPi_succ_pos (n : ℕ) : 0 < rPi (n + 1) := by
  rw [rPi_succ]
  have hx : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have key : 4 / (8 * (n : ℝ) + 1) - 2 / (8 * (n : ℝ) + 4) - 1 / (8 * (n : ℝ) + 5) -
      1 / (8 * (n : ℝ) + 6) = (120 * (n : ℝ) ^ 2 + 151 * n + 47) /
        ((2 * n + 1) * (4 * n + 3) * (8 * n + 1) * (8 * n + 5)) := by
    field_simp; ring
  rw [key]; positivity

/-- `r(n+1) ≤ 15/((8n+1)(8n+2))` (ZSC-03 proof). -/
theorem rPi_succ_le (n : ℕ) : rPi (n + 1) ≤ 15 / ((8 * (n : ℝ) + 1) * (8 * n + 2)) := by
  rw [rPi_succ]
  have hx : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  have key : 15 / ((8 * (n : ℝ) + 1) * (8 * n + 2)) -
      (4 / (8 * (n : ℝ) + 1) - 2 / (8 * (n : ℝ) + 4) - 1 / (8 * (n : ℝ) + 5) -
        1 / (8 * (n : ℝ) + 6)) = (352 * (n : ℝ) ^ 2 + 432 * n + 131) /
        (2 * (2 * n + 1) * (4 * n + 1) * (4 * n + 3) * (8 * n + 1) * (8 * n + 5)) := by
    field_simp; ring
  have : 0 ≤ (352 * (n : ℝ) ^ 2 + 432 * n + 131) /
      (2 * (2 * n + 1) * (4 * n + 1) * (4 * n + 3) * (8 * n + 1) * (8 * n + 5)) := by positivity
  linarith

/-- `r` is decreasing on `m ≥ 1`: `r(n+2) ≤ r(n+1)`. -/
theorem rPi_succ_antitone (n : ℕ) : rPi (n + 2) ≤ rPi (n + 1) := by
  rw [show n + 2 = (n + 1) + 1 by ring, rPi_succ, rPi_succ]
  have hx : (0 : ℝ) ≤ n := Nat.cast_nonneg n
  push_cast
  have key : (4 / (8 * (n : ℝ) + 1) - 2 / (8 * (n : ℝ) + 4) - 1 / (8 * (n : ℝ) + 5) -
        1 / (8 * (n : ℝ) + 6)) -
      (4 / (8 * ((n : ℝ) + 1) + 1) - 2 / (8 * ((n : ℝ) + 1) + 4) - 1 / (8 * ((n : ℝ) + 1) + 5) -
        1 / (8 * ((n : ℝ) + 1) + 6)) =
      3 * (40960 * (n : ℝ) ^ 5 + 220672 * n ^ 4 + 453632 * n ^ 3 + 443480 * n ^ 2 +
        206712 * n + 36903) /
      ((2 * n + 1) * (2 * n + 3) * (4 * n + 3) * (4 * n + 7) * (8 * n + 1) * (8 * n + 5) *
        (8 * n + 9) * (8 * n + 13)) := by
    field_simp; ring
  have : 0 ≤ 3 * (40960 * (n : ℝ) ^ 5 + 220672 * n ^ 4 + 453632 * n ^ 3 + 443480 * n ^ 2 +
        206712 * n + 36903) /
      ((2 * n + 1) * (2 * n + 3) * (4 * n + 3) * (4 * n + 7) * (8 * n + 1) * (8 * n + 5) *
        (8 * n + 9) * (8 * n + 13)) := by positivity
  linarith

lemma rPi_le_of_ge (n i : ℕ) : rPi (n + 1 + i) ≤ rPi (n + 1) := by
  induction i with
  | zero => simp
  | succ i ih =>
    have := rPi_succ_antitone (n + i)
    rw [show n + 1 + (i + 1) = n + i + 2 by ring]
    rw [show n + 1 + i = n + i + 1 by ring] at ih
    linarith

/-- **ZSC-03, `J(n) ≥ ⌊log_4 2n⌋`, integer form.**  For `n ≥ 1` and every `L` with
`4^L ≤ 2n`, `(16/15)·16^L·r(n+1) ≤ 1`.  Since `J(n)` is the largest `j` with
`(16/15)·16^j·r(n+1) ≤ 1`, this is `J(n) ≥ ⌊log_4 2n⌋`, i.e. `4^(J(n)+1) > 2n`. -/
theorem zsc03_window (n L : ℕ) (hn : 1 ≤ n) (hL : 4 ^ L ≤ 2 * n) :
    16 / 15 * 16 ^ L * rPi (n + 1) ≤ 1 := by
  have hx : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have h4 : ((4 : ℝ) ^ L) ≤ 2 * n := by exact_mod_cast hL
  have h16 : (16 : ℝ) ^ L ≤ 4 * (n : ℝ) ^ 2 := by
    have : (16 : ℝ) ^ L = (4 ^ L) ^ 2 := by rw [← pow_mul, mul_comm, pow_mul]; norm_num
    rw [this]
    have h0 : (0 : ℝ) ≤ 4 ^ L := by positivity
    nlinarith
  have hr := rPi_succ_le n
  have hr0 := (rPi_succ_pos n).le
  have hden : (0 : ℝ) < (8 * n + 1) * (8 * n + 2) := by positivity
  calc 16 / 15 * 16 ^ L * rPi (n + 1) ≤ 16 / 15 * (4 * (n : ℝ) ^ 2) * rPi (n + 1) := by
        gcongr
    _ ≤ 16 / 15 * (4 * (n : ℝ) ^ 2) * (15 / ((8 * (n : ℝ) + 1) * (8 * n + 2))) := by
        gcongr
    _ ≤ 1 := by
        rw [mul_div_assoc', div_le_one hden]
        nlinarith

/-- **ZSC-03 renewal lemma for the authentic forcing, every real seed `s`.**
`U_0 = s`, `U_(m+1) = 16 U_m + r(m+1)`; if `n ≥ 1`, `κ_(n+1) = 16` and `4^L ≤ 2n`
(i.e. `L ≤ ⌊log_4 2n⌋`), then `κ_(n+2) = … = κ_(n+1+L) = 0`. -/
theorem zsc03_renewal_authentic (U : ℕ → ℝ) (n L : ℕ)
    (hrec : ∀ m, U (m + 1) = 16 * U m + rPi (m + 1))
    (hn : 1 ≤ n) (hL : 4 ^ L ≤ 2 * n)
    (h16 : ⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16) :
    ∀ j, 1 ≤ j → j ≤ L → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0 :=
  zsc03_renewal_kernel U rPi n L hrec
    (fun i => by rw [show n + 1 + i = (n + i) + 1 by ring]; exact (rPi_succ_pos _).le)
    (rPi_le_of_ge n) h16 (zsc03_window n L hn hL)

/-- The file's `J(n) = ⌊log_16(15/(16 r(n+1)))⌋` (an integer; real base-16 logarithm). -/
noncomputable def Jn (n : ℕ) : ℤ := ⌊Real.logb 16 (15 / (16 * rPi (n + 1)))⌋

/-- `j ≤ J(n)` iff `(16/15)·16^j·r(n+1) ≤ 1`, for natural `j`. -/
theorem Jn_le_iff (n j : ℕ) : (j : ℤ) ≤ Jn n ↔ 16 / 15 * 16 ^ j * rPi (n + 1) ≤ 1 := by
  have hr := rPi_succ_pos n
  have hY : (0 : ℝ) < 15 / (16 * rPi (n + 1)) := by positivity
  unfold Jn
  rw [Int.le_floor, Int.cast_natCast, Real.le_logb_iff_rpow_le (by norm_num) hY,
    Real.rpow_natCast, le_div_iff₀ (by positivity)]
  constructor <;> intro h <;> linarith

/-- **ZSC-03: `J(n) ≥ ⌊log_4(2n)⌋`** for `n ≥ 1` (file statement, real logarithms). -/
theorem zsc03_J_ge (n : ℕ) (hn : 1 ≤ n) : ⌊Real.logb 4 (2 * (n : ℝ))⌋ ≤ Jn n := by
  unfold Jn
  apply Int.floor_mono
  have hr := rPi_succ_pos n
  have hle := rPi_succ_le n
  have hx : (1 : ℝ) ≤ n := by exact_mod_cast hn
  have hY : 4 * (n : ℝ) ^ 2 ≤ 15 / (16 * rPi (n + 1)) := by
    rw [le_div_iff₀ (by positivity)]
    have : rPi (n + 1) * ((8 * n + 1) * (8 * n + 2)) ≤ 15 := by
      rwa [le_div_iff₀ (by positivity)] at hle
    nlinarith
  have h16 : Real.logb 16 (4 * (n : ℝ) ^ 2) ≤ Real.logb 16 (15 / (16 * rPi (n + 1))) :=
    Real.logb_le_logb_of_le (by norm_num) (by positivity) hY
  have e : Real.logb 16 (4 * (n : ℝ) ^ 2) = Real.logb 4 (2 * n) := by
    have h4 : Real.log 4 ≠ 0 := (Real.log_pos (by norm_num)).ne'
    rw [show (4 : ℝ) * n ^ 2 = (2 * n) ^ 2 by ring, show (16 : ℝ) = 4 ^ 2 by norm_num]
    unfold Real.logb
    rw [Real.log_pow, Real.log_pow]
    field_simp
    ring
  linarith

/-- **ZSC-03 renewal lemma, file form** (authentic forcing, every real seed, every `n`):
if `κ_(n+1) = 16` then `κ_(n+2) = … = κ_(n+1+J(n)) = 0`. -/
theorem zsc03_renewal_lemma (U : ℕ → ℝ) (n : ℕ)
    (hrec : ∀ m, U (m + 1) = 16 * U m + rPi (m + 1))
    (h16 : ⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16) :
    ∀ j : ℕ, 1 ≤ j → (j : ℤ) ≤ Jn n → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0 := by
  intro j hj1 hjJ
  exact zsc03_renewal_kernel U rPi n j hrec
    (fun i => by rw [show n + 1 + i = (n + i) + 1 by ring]; exact (rPi_succ_pos _).le)
    (rPi_le_of_ge n) h16 ((Jn_le_iff n j).mp hjJ) j hj1 le_rfl

/-! ## Refutations of mutated (false) nearby statements -/

/-- Mutant of the null integral (numerator constant `2` replaced by `3`): the integral is
`∫_0^1 1/m > 0`, so it is not `0`. -/
theorem refute_null_integral_numerator :
    ∫ z in (0:ℝ)..1, (z ^ 2 - 4 * z + 3) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) ≠ 0 := by
  have hA : ∀ x ∈ Set.uIcc (0:ℝ) 1, (2 - x ^ 2) * (x ^ 2 - 2 * x + 2) ≠ 0 := by
    intro x hx
    rw [Set.uIcc_of_le zero_le_one] at hx
    obtain ⟨h0, h1⟩ := hx
    apply mul_ne_zero <;> nlinarith [sq_nonneg (x - 1)]
  have hc : ∀ p : ℝ → ℝ, Continuous p → IntervalIntegrable
      (fun x => p x / ((2 - x ^ 2) * (x ^ 2 - 2 * x + 2))) MeasureTheory.volume 0 1 := by
    intro p hp
    exact (ContinuousOn.div hp.continuousOn (by fun_prop) hA).intervalIntegrable
  have h1 := hc (fun x => x ^ 2 - 4 * x + 2) (by fun_prop)
  have h2 := hc (fun _ => 1) (by fun_prop)
  have hsplit : ∫ z in (0:ℝ)..1, (z ^ 2 - 4 * z + 3) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) =
      (∫ z in (0:ℝ)..1, (z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2))) +
        ∫ z in (0:ℝ)..1, 1 / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) := by
    rw [← intervalIntegral.integral_add h1 h2]
    apply intervalIntegral.integral_congr
    intro x _
    simp only
    ring
  rw [hsplit, zsc06_null_integral, zero_add]
  refine (intervalIntegral.intervalIntegral_pos_of_pos_on h2 (fun x hx => ?_) zero_lt_one).ne'
  obtain ⟨h0, h1⟩ := hx
  apply div_pos one_pos
  apply mul_pos <;> nlinarith [sq_nonneg (x - 1)]

/-- Mutant of L1 (sign flipped): false already at `z = 0` over `ℚ`. -/
theorem refute_partial_fraction_sign_flip :
    ¬ ∀ z : ℚ, z ^ 2 - 2 ≠ 0 → z ^ 2 - 2 * z + 2 ≠ 0 →
      (z ^ 2 - 4 * z + 2) / ((2 - z ^ 2) * (z ^ 2 - 2 * z + 2)) =
        z / (z ^ 2 - 2) + (z - 1) / (z ^ 2 - 2 * z + 2) := by
  intro H
  have := H 0 (by norm_num) (by norm_num)
  norm_num at this

/-- Mutant of the `A_0` expansion (coefficient of `z³` sign-flipped): false (evaluate at 1). -/
theorem refute_null_numerator_coefficient :
    ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * (X ^ 2 - 4 * X + 2 : ℚ[X]) ≠
      8 - 8 * X - 4 * X ^ 2 + 8 * X ^ 3 - 2 * X ^ 4 - 2 * X ^ 5 + X ^ 6 := by
  intro h
  have := congrArg (Polynomial.eval (1 : ℚ)) h
  simp at this
  norm_num at this

/-- Mutant of the factorisation (`2 - z²` replaced by `2 + z²`): false (evaluate at 1). -/
theorem refute_sixteen_factorisation :
    (16 - X ^ 8 : ℚ[X]) ≠
      ((X ^ 2 + 2) * (X ^ 2 + 2 * X + 2)) * ((2 + X ^ 2) * (X ^ 2 - 2 * X + 2)) := by
  intro h
  have := congrArg (Polynomial.eval (1 : ℚ)) h
  simp at this
  norm_num at this

/-- Mutant of ZSC-02 Lemma 2 (threshold `1/256` replaced by `1/200`): false at
`y = 249/3750` (`15y = 249/250`, digits `1, 0`).  So `1/256` cannot be raised to `1/200`. -/
theorem refute_locality_change_threshold :
    ¬ ∀ (ξ : ℝ) (n : ℕ), |15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| < 1 / 200 →
      hexDigit ξ n = hexDigit ξ (n + 1) := by
  intro H
  have hround : round (15 * ((16 : ℝ) ^ 0 * (249 / 3750))) = 1 := by
    rw [round_eq, Int.floor_eq_iff]; norm_num
  have h := H (249 / 3750) 0 (by rw [hround]; norm_num [abs_lt])
  have e0 : hexDigit (249 / 3750) 0 = 1 := by
    unfold hexDigit
    rw [pow_zero, one_mul, Int.fract_eq_self.mpr ⟨by norm_num, by norm_num⟩, Int.floor_eq_iff]
    norm_num
  have e1 : hexDigit (249 / 3750) 1 = 0 := by
    unfold hexDigit
    have hfl : ⌊(16 : ℝ) ^ 1 * (249 / 3750)⌋ = 1 := by rw [Int.floor_eq_iff]; norm_num
    rw [← Int.self_sub_floor, hfl, Int.floor_eq_iff]
    norm_num
  rw [zero_add, e0, e1] at h
  exact absurd h (by norm_num)

/-- Mutant of ZSC-02 Lemma 1 (constant `15·16^(-k)` replaced by `14·16^(-k)`): false at
`ξ = 255/256`, `n = 0`, `k = 2` (digits `F, F`, `‖15ξ‖ = 15/256`).  The constant is attained. -/
theorem refute_locality_run_constant :
    ¬ ∀ (ξ : ℝ) (n k : ℕ), (∀ i < k, hexDigit ξ (n + i) = hexDigit ξ n) →
      |15 * (16 ^ n * ξ) - round (15 * (16 ^ n * ξ))| ≤ 14 / 16 ^ k := by
  intro H
  have e0 : hexDigit (255 / 256) 0 = 15 := by
    unfold hexDigit
    rw [pow_zero, one_mul, Int.fract_eq_self.mpr ⟨by norm_num, by norm_num⟩, Int.floor_eq_iff]
    norm_num
  have e1 : hexDigit (255 / 256) 1 = 15 := by
    unfold hexDigit
    have hfl : ⌊(16 : ℝ) ^ 1 * (255 / 256)⌋ = 15 := by rw [Int.floor_eq_iff]; norm_num
    rw [← Int.self_sub_floor, hfl, Int.floor_eq_iff]
    norm_num
  have h := H (255 / 256) 0 2 (by
    intro i hi
    interval_cases i
    · rfl
    · rw [zero_add, e1, e0])
  have hround : round (15 * ((16 : ℝ) ^ 0 * (255 / 256))) = 15 := by
    rw [round_eq, Int.floor_eq_iff]; norm_num
  rw [hround] at h
  norm_num [abs_le] at h

/-- Mutant of the window (`2n` replaced by `4n`, i.e. `J(n) ≥ ⌊log_4 4n⌋`): false at
`n = 1`, `L = 1`. -/
theorem refute_window_four_n :
    ¬ ∀ n L : ℕ, 1 ≤ n → 4 ^ L ≤ 4 * n → 16 / 15 * 16 ^ L * rPi (n + 1) ≤ 1 := by
  intro H
  have h := H 1 1 le_rfl le_rfl
  rw [rPi_succ] at h
  norm_num at h

/-- Mutant of the renewal kernel (zero run claimed through `J+1`): false for the constant
forcing `r ≡ 15/256`, `J = 1`, seed `1 - 1/65536` (`κ = 16, 0, 15`). -/
theorem refute_renewal_kernel_overrun :
    ¬ ∀ (U r : ℕ → ℝ) (n J : ℕ),
      (∀ m, U (m + 1) = 16 * U m + r (m + 1)) →
      (∀ i, 0 ≤ r (n + 1 + i)) → (∀ i, r (n + 1 + i) ≤ r (n + 1)) →
      ⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16 → 16 / 15 * 16 ^ J * r (n + 1) ≤ 1 →
      ∀ j, 1 ≤ j → j ≤ J + 1 → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0 := by
  intro H
  let U : ℕ → ℝ := fun m => 16 ^ m * (65535 / 65536) + 15 / 256 * (16 ^ m - 1) / 15
  have hrec : ∀ m, U (m + 1) = 16 * U m + 15 / 256 := by
    intro m; simp only [U]; rw [pow_succ]; ring
  have hU0 : ⌊U 0⌋ = 0 := by simp only [U]; rw [Int.floor_eq_iff]; norm_num
  have hU1 : ⌊U 1⌋ = 16 := by simp only [U]; rw [Int.floor_eq_iff]; norm_num
  have hU2 : ⌊U 2⌋ = 256 := by simp only [U]; rw [Int.floor_eq_iff]; norm_num
  have hU3 : ⌊U 3⌋ = 4111 := by simp only [U]; rw [Int.floor_eq_iff]; norm_num
  have h := H U (fun _ => 15 / 256) 0 1 hrec (fun _ => by norm_num) (fun _ => le_rfl)
    (by rw [zero_add, hU1, hU0]; norm_num) (by norm_num) 2 (by norm_num) (by norm_num)
  rw [show (0 : ℕ) + 1 + 2 = 3 by rfl, show (0 : ℕ) + 2 = 2 by rfl, hU3, hU2] at h
  norm_num at h

/-- Mutant of the authentic renewal lemma (zero run claimed through `J(n)+1`): false for the
authentic forcing at `n = 1` (`J(1) = 0`), seed `s = (999/1000 - r(1))/16`, where
`U_1 = 999/1000`, `κ_2 = 16` and `κ_3 = 1`. -/
theorem refute_renewal_lemma_overrun :
    ¬ ∀ (U : ℕ → ℝ) (n : ℕ), (∀ m, U (m + 1) = 16 * U m + rPi (m + 1)) →
      ⌊U (n + 1)⌋ - 16 * ⌊U n⌋ = 16 →
      ∀ j : ℕ, 1 ≤ j → (j : ℤ) ≤ Jn n + 1 → ⌊U (n + 1 + j)⌋ - 16 * ⌊U (n + j)⌋ = 0 := by
  intro H
  let U : ℕ → ℝ := fun m =>
    Nat.rec ((999 / 1000 - rPi 1) / 16) (fun k u => 16 * u + rPi (k + 1)) m
  have hrec : ∀ m, U (m + 1) = 16 * U m + rPi (m + 1) := fun m => rfl
  have hU1 : U 1 = 999 / 1000 := by
    show 16 * ((999 / 1000 - rPi 1) / 16) + rPi (0 + 1) = 999 / 1000
    ring
  have hU2 : U 2 = 16 * (999 / 1000) + rPi 2 := by
    show 16 * U 1 + rPi (1 + 1) = _
    rw [hU1]
  have hU3 : U 3 = 16 * (16 * (999 / 1000) + rPi 2) + rPi 3 := by
    show 16 * U 2 + rPi (2 + 1) = _
    rw [hU2]
  have r2 : rPi 2 = 106 / 819 := by unfold rPi; norm_num
  have r3 : rPi 3 = 829 / 19635 := by unfold rPi; norm_num
  have f1 : ⌊U 1⌋ = 0 := by rw [hU1, Int.floor_eq_iff]; norm_num
  have f2 : ⌊U 2⌋ = 16 := by rw [hU2, r2, Int.floor_eq_iff]; norm_num
  have f3 : ⌊U 3⌋ = 257 := by rw [hU3, r2, r3, Int.floor_eq_iff]; norm_num
  have hJ : (0 : ℤ) ≤ Jn 1 := by
    unfold Jn
    rw [Int.floor_nonneg]
    apply Real.logb_nonneg (by norm_num)
    rw [show (1 : ℕ) + 1 = 2 by rfl, r2]
    norm_num
  have h := H U 1 hrec (by rw [show (1 : ℕ) + 1 = 2 by rfl, f2, f1]; norm_num) 1 le_rfl
    (by push_cast; linarith)
  rw [show (1 : ℕ) + 1 + 1 = 3 by rfl, show (1 : ℕ) + 1 = 2 by rfl, f3, f2] at h
  norm_num at h

end ObservationalSUCC.ZSCCarryFlux
