import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset
import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

/-!
Finite Fejer innovation core, pinned Lean/mathlib 4.14.0.

The real symmetric pair kernel has constant diagonal H^2 and row sum m*q_m.
Those explicitly stated hypotheses bridge the complex Fourier Gram calculation
to this finite kernel. No source cancellation, equidistribution, analytic limit,
or complex-character representation is formalized here.

The exceptional-step conclusion is conditional on the displayed good-step
bound; signed q_m-H is never replaced by its absolute value.
-/

open scoped BigOperators

namespace ObservationalSUCC.SpectralPurity

def rawEnergy (H : ℝ) (q : ℕ → ℝ) : ℕ → ℝ
  | 0 => 0
  | n+1 => rawEnergy H q n + H^2 + 2*(n:ℝ)*q n

def pairEnergy (K : ℕ → ℕ → ℝ) (N : ℕ) : ℝ :=
  ∑ i ∈ Finset.range N, ∑ j ∈ Finset.range N, K i j

def signedInnovation (H : ℝ) (q : ℕ → ℝ) (N : ℕ) : ℝ :=
  ∑ m ∈ Finset.range N, (m:ℝ)*(q m-H)

def badWeight (bad : ℕ → Prop) [DecidablePred bad] (N : ℕ) : ℝ :=
  ∑ m ∈ Finset.range N, if bad m then (m:ℝ) else 0

theorem raw_energy_sum (H : ℝ) (q : ℕ → ℝ) (N : ℕ) :
    rawEnergy H q N = (N:ℝ)*H^2 +
      2*∑ m ∈ Finset.range N, (m:ℝ)*q m := by
  induction N with
  | zero => simp [rawEnergy]
  | succ N ih =>
      simp only [rawEnergy, ih, Finset.sum_range_succ, Nat.cast_add,
        Nat.cast_one]
      ring

theorem pair_energy_succ (K : ℕ → ℕ → ℝ) (H : ℝ)
    (symm : ∀ i j, K i j = K j i) (diag : ∀ i, K i i = H^2)
    (N : ℕ) :
    pairEnergy K (N+1) = pairEnergy K N + H^2 +
      2*∑ j ∈ Finset.range N, K N j := by
  simp only [pairEnergy, Finset.sum_range_succ, Finset.sum_add_distrib]
  rw [diag N]
  have h : (∑ i ∈ Finset.range N, K i N) =
      ∑ i ∈ Finset.range N, K N i := by
    apply Finset.sum_congr rfl
    intro i _
    exact symm i N
  rw [h]
  ring

theorem pair_energy_eq_raw (K : ℕ → ℕ → ℝ) (H : ℝ) (q : ℕ → ℝ)
    (symm : ∀ i j, K i j = K j i) (diag : ∀ i, K i i = H^2)
    (row : ∀ m, (∑ j ∈ Finset.range m, K m j) = (m:ℝ)*q m)
    (N : ℕ) : pairEnergy K N = rawEnergy H q N := by
  induction N with
  | zero => simp [pairEnergy, rawEnergy]
  | succ N ih =>
      rw [pair_energy_succ K H symm diag N, row N, ih]
      simp only [rawEnergy]
      ring

theorem sum_time_weights (N : ℕ) :
    (∑ m ∈ Finset.range N, (m:ℝ)) = (N:ℝ)*((N:ℝ)-1)/2 := by
  induction N with
  | zero => simp
  | succ N ih =>
      simp only [Finset.sum_range_succ, ih, Nat.cast_add, Nat.cast_one]
      ring

theorem signed_sum_rewrite (H : ℝ) (q : ℕ → ℝ) (N : ℕ) :
    signedInnovation H q N =
      (∑ m ∈ Finset.range N, (m:ℝ)*q m) -
      H*((N:ℝ)*((N:ℝ)-1)/2) := by
  simp only [signedInnovation, mul_sub, Finset.sum_sub_distrib]
  rw [show (∑ m ∈ Finset.range N, (m:ℝ)*H) =
      H*(∑ m ∈ Finset.range N, (m:ℝ)) by
    rw [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro i _
    ring]
  rw [sum_time_weights]
  ring

theorem sequential_normalized_identity (H : ℝ) (q : ℕ → ℝ) (N : ℕ)
    (hH : H ≠ 0) (hN : N ≠ 0) :
    rawEnergy H q N / ((N:ℝ)^2*H) - 1 =
      (H-1)/(N:ℝ) + 2*signedInnovation H q N/((N:ℝ)^2*H) := by
  rw [raw_energy_sum, signed_sum_rewrite]
  have hn : (N:ℝ) ≠ 0 := by exact_mod_cast hN
  field_simp
  <;> ring

theorem exceptional_signed_sum_bound (H eta : ℝ) (q : ℕ → ℝ)
    (bad : ℕ → Prop) [DecidablePred bad] (N : ℕ)
    (hH : 0 ≤ H) (heta : 0 ≤ eta)
    (upper : ∀ m ∈ Finset.range N, q m ≤ H^2)
    (good : ∀ m ∈ Finset.range N, ¬bad m → q m ≤ H*(1+eta)) :
    signedInnovation H q N ≤
      eta*H*((N:ℝ)*((N:ℝ)-1)/2) + H^2*badWeight bad N := by
  have point : ∀ m ∈ Finset.range N,
      (m:ℝ)*(q m-H) ≤ eta*H*(m:ℝ) +
        H^2*(if bad m then (m:ℝ) else 0) := by
    intro m hm
    have hm0 : (0:ℝ) ≤ m := by positivity
    have heh : 0 ≤ eta*H := mul_nonneg heta hH
    by_cases hb : bad m
    · simp only [hb, if_true]
      have hu := upper m hm
      have hd : q m-H ≤ eta*H+H^2 := by linarith
      have hp := mul_le_mul_of_nonneg_left hd hm0
      nlinarith
    · simp only [hb, if_false, mul_zero, add_zero]
      have hg := good m hm hb
      have hd : q m-H ≤ eta*H := by nlinarith
      have hp := mul_le_mul_of_nonneg_left hd hm0
      nlinarith
  have total := Finset.sum_le_sum point
  unfold signedInnovation
  refine le_trans total ?_
  rw [Finset.sum_add_distrib, ← Finset.mul_sum, ← Finset.mul_sum,
    sum_time_weights]
  exact le_rfl

theorem exceptional_normalized_bound (H eta : ℝ) (q : ℕ → ℝ)
    (bad : ℕ → Prop) [DecidablePred bad] (N : ℕ)
    (hH : 0 < H) (hN : 0 < N) (heta : 0 ≤ eta)
    (upper : ∀ m ∈ Finset.range N, q m ≤ H^2)
    (good : ∀ m ∈ Finset.range N, ¬bad m → q m ≤ H*(1+eta)) :
    rawEnergy H q N/((N:ℝ)^2*H)-1 ≤
      (H-1)/(N:ℝ) + eta*((N:ℝ)-1)/(N:ℝ) +
      2*H*badWeight bad N/(N:ℝ)^2 := by
  rw [sequential_normalized_identity H q N (ne_of_gt hH) (Nat.ne_of_gt hN)]
  have hs := exceptional_signed_sum_bound H eta q bad N (le_of_lt hH) heta upper good
  have hn : (0:ℝ) < N := by exact_mod_cast hN
  have hd : 0 < (N:ℝ)^2*H := by positivity
  have bound := div_le_div_of_nonneg_right (mul_le_mul_of_nonneg_left hs (by norm_num : (0:ℝ) ≤ 2)) (le_of_lt hd)
  have expr : 2*(eta*H*((N:ℝ)*((N:ℝ)-1)/2)+H^2*badWeight bad N)/
      ((N:ℝ)^2*H) = eta*((N:ℝ)-1)/(N:ℝ) +
      2*H*badWeight bad N/(N:ℝ)^2 := by
    field_simp
    <;> ring
  rw [expr] at bound
  linarith

/-- Deleting an independently specified sparse source subset costs at most
    H^2*N*card(s) in the unnormalized signed innovation sum. -/
theorem discarded_innovation_bound (H : ℝ) (q : ℕ → ℝ)
    (s : Finset ℕ) (N : ℕ) (hH : 1 ≤ H)
    (time : ∀ m ∈ s, m ≤ N)
    (lower : ∀ m ∈ s, 0 ≤ q m)
    (upper : ∀ m ∈ s, q m ≤ H^2) :
    |∑ m ∈ s, (m:ℝ)*(q m-H)| ≤ H^2*(N:ℝ)*(s.card:ℝ) := by
  have point : ∀ m ∈ s, |(m:ℝ)*(q m-H)| ≤ H^2*(N:ℝ) := by
    intro m hm
    have hm0 : (0:ℝ) ≤ m := by positivity
    have hmn : (m:ℝ) ≤ N := by exact_mod_cast time m hm
    have hl := lower m hm
    have hu := upper m hm
    have hd : |q m-H| ≤ H^2 := by
      apply abs_le.mpr
      constructor <;> nlinarith
    rw [abs_mul, abs_of_nonneg hm0]
    calc
      (m:ℝ)*|q m-H| ≤ (m:ℝ)*H^2 := mul_le_mul_of_nonneg_left hd hm0
      _ ≤ H^2*(N:ℝ) := by nlinarith [sq_nonneg H]
  calc
    |∑ m ∈ s, (m:ℝ)*(q m-H)| ≤ ∑ m ∈ s, |(m:ℝ)*(q m-H)| :=
      Finset.abs_sum_le_sum_abs _ _
    _ ≤ ∑ _m ∈ s, H^2*(N:ℝ) := Finset.sum_le_sum point
    _ = H^2*(N:ℝ)*(s.card:ℝ) := by simp; ring

theorem discarded_normalized_bound (H : ℝ) (q : ℕ → ℝ)
    (s : Finset ℕ) (N : ℕ) (hH : 1 ≤ H) (hN : 0 < N)
    (time : ∀ m ∈ s, m ≤ N)
    (lower : ∀ m ∈ s, 0 ≤ q m)
    (upper : ∀ m ∈ s, q m ≤ H^2) :
    |2*(∑ m ∈ s, (m:ℝ)*(q m-H))/((N:ℝ)^2*H)| ≤
      2*H*(s.card:ℝ)/(N:ℝ) := by
  have hh : 0 < H := by linarith
  have hn : (0:ℝ) < N := by exact_mod_cast hN
  have hd : 0 < (N:ℝ)^2*H := by positivity
  have hs := discarded_innovation_bound H q s N hH time lower upper
  rw [abs_div, abs_mul, abs_of_pos hd, abs_of_pos (by norm_num : (0:ℝ) < 2)]
  have hb := div_le_div_of_nonneg_right
    (mul_le_mul_of_nonneg_left hs (by norm_num : (0:ℝ) ≤ 2)) (le_of_lt hd)
  have he : 2*(H^2*(N:ℝ)*(s.card:ℝ))/((N:ℝ)^2*H) =
      2*H*(s.card:ℝ)/(N:ℝ) := by field_simp; ring
  rw [he] at hb
  exact hb

end ObservationalSUCC.SpectralPurity

#print axioms ObservationalSUCC.SpectralPurity.raw_energy_sum
#print axioms ObservationalSUCC.SpectralPurity.pair_energy_succ
#print axioms ObservationalSUCC.SpectralPurity.pair_energy_eq_raw
#print axioms ObservationalSUCC.SpectralPurity.sum_time_weights
#print axioms ObservationalSUCC.SpectralPurity.signed_sum_rewrite
#print axioms ObservationalSUCC.SpectralPurity.sequential_normalized_identity
#print axioms ObservationalSUCC.SpectralPurity.exceptional_signed_sum_bound
#print axioms ObservationalSUCC.SpectralPurity.exceptional_normalized_bound
#print axioms ObservationalSUCC.SpectralPurity.discarded_innovation_bound
#print axioms ObservationalSUCC.SpectralPurity.discarded_normalized_bound
