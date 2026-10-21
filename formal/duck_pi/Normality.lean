import Mathlib.MeasureTheory.Integral.Periodic
import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Topology.Instances.Complex
import Mathlib.Tactic

/-!
# Canonical digit blocks, real-pi targets, and a checked conditional bridge

Normality is defined by frequencies of canonical floor-selected digit blocks,
not by renaming Fourier cancellation. The right endpoint of every cylinder is
excluded, fixing the terminating (rather than recurring maximal-digit)
expansion at rational endpoints. Every start position is counted, so blocks
overlap. Fourier and Haar statements are separate predicates. This file does
not assert the missing Weyl or interval/Haar equivalences, nor pi normality.
-/

noncomputable section

open scoped BigOperators Topology
open Filter MeasureTheory

namespace ObservationalSUCC.DuckPi

def digitOrbit (b : ℕ) (x : ℝ) (n : ℕ) : ℝ := (b : ℝ) ^ n * x

def canonicalBlock (b k n : ℕ) (x : ℝ) : ℕ :=
  ⌊(b : ℝ) ^ k * Int.fract (digitOrbit b x n)⌋₊

def blockFrequency (b k a N : ℕ) (x : ℝ) : ℝ :=
  ((Finset.range N).filter (fun n => canonicalBlock b k n x = a)).card / (N : ℝ)

/-- Words of length k are encoded by 0,...,b^k-1. All starting positions,
including overlapping occurrences, enter `blockFrequency`. -/
def NormalTo (b : ℕ) (x : ℝ) : Prop :=
  2 ≤ b ∧ ∀ k : ℕ, 0 < k → ∀ a : ℕ, a < b ^ k →
    Tendsto (fun N => blockFrequency b k a N x) atTop (𝓝 ((b : ℝ) ^ k)⁻¹)

def AbsolutelyNormal (x : ℝ) : Prop := ∀ b : ℕ, 2 ≤ b → NormalTo b x

def PiNormal16 : Prop := NormalTo 16 Real.pi
def PiNormal2 : Prop := NormalTo 2 Real.pi
def PiNormal10 : Prop := NormalTo 10 Real.pi
def PiAbsolutelyNormal : Prop := AbsolutelyNormal Real.pi

def intervalFrequency (u : ℕ → ℝ) (a c : ℝ) (N : ℕ) : ℝ :=
  ((Finset.range N).filter (fun n => Int.fract (u n) ∈ Set.Ico a c)).card / (N : ℝ)

def UniformDistributionModOne (u : ℕ → ℝ) : Prop :=
  ∀ a c : ℝ, 0 ≤ a → a ≤ c → c ≤ 1 →
    Tendsto (intervalFrequency u a c) atTop (𝓝 (c - a))

def circleOrbit (b : ℕ) (x : ℝ) (n : ℕ) : AddCircle (1 : ℝ) :=
  (digitOrbit b x n : ℝ)

/-- The actual period-one Haar volume from mathlib. -/
def circleHaar : Measure (AddCircle (1 : ℝ)) := volume

def HaarUniformDistribution (u : ℕ → AddCircle (1 : ℝ)) : Prop :=
  ∀ F : AddCircle (1 : ℝ) → ℝ, Continuous F →
    Tendsto (fun N : ℕ => (∑ n ∈ Finset.range N, F (u n)) / (N : ℝ))
      atTop (𝓝 (∫ z, F z ∂circleHaar))

def weylMean (u : ℕ → ℝ) (h : ℤ) (N : ℕ) : ℂ :=
  (∑ n ∈ Finset.range N,
    Complex.exp (2 * (Real.pi : ℂ) * Complex.I * (h : ℂ) * (u n : ℂ))) / (N : ℂ)

def FourierCancellation (u : ℕ → ℝ) : Prop :=
  ∀ h : ℤ, h ≠ 0 → Tendsto (weylMean u h) atTop (𝓝 0)

def PiFourierCancellation16 : Prop := FourierCancellation (digitOrbit 16 Real.pi)

theorem canonicalBlock_lt {b : ℕ} (hb : 2 ≤ b) (k n : ℕ) (x : ℝ) :
    canonicalBlock b k n x < b ^ k := by
  have hbpos : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hm : (0 : ℝ) < (b : ℝ) ^ k := pow_pos hbpos _
  rw [canonicalBlock, Nat.floor_lt (mul_nonneg hm.le (Int.fract_nonneg _))]
  push_cast
  nlinarith [Int.fract_lt_one (digitOrbit b x n)]

/-- Exact cylinder identification, with the canonical half-open convention. -/
theorem canonicalBlock_eq_iff {b : ℕ} (hb : 2 ≤ b) (k n a : ℕ) (x : ℝ) :
    canonicalBlock b k n x = a ↔
      Int.fract (digitOrbit b x n) ∈
        Set.Ico ((a : ℝ) / (b : ℝ) ^ k) (((a : ℝ) + 1) / (b : ℝ) ^ k) := by
  have hbpos : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hm : (0 : ℝ) < (b : ℝ) ^ k := pow_pos hbpos _
  rw [canonicalBlock, Nat.floor_eq_iff (mul_nonneg hm.le (Int.fract_nonneg _))]
  simp only [Set.mem_Ico, div_le_iff₀ hm, lt_div_iff₀ hm]
  constructor <;> rintro ⟨h₁, h₂⟩ <;> constructor <;> nlinarith

theorem blockFrequency_eq_intervalFrequency {b : ℕ} (hb : 2 ≤ b)
    (k a N : ℕ) (x : ℝ) :
    blockFrequency b k a N x = intervalFrequency (digitOrbit b x)
      ((a : ℝ) / (b : ℝ) ^ k) (((a : ℝ) + 1) / (b : ℝ) ^ k) N := by
  unfold blockFrequency intervalFrequency
  congr 2
  ext n
  simp only [Finset.mem_filter, canonicalBlock_eq_iff hb]

/-- A real conditional implication. Its input is interval equidistribution;
it is not an unconditional pi theorem or a proof of Weyl's criterion. -/
theorem uniformDistribution_digitOrbit_implies_normal {b : ℕ} (hb : 2 ≤ b)
    (x : ℝ) (hu : UniformDistributionModOne (digitOrbit b x)) : NormalTo b x := by
  refine ⟨hb, ?_⟩
  intro k _ a ha
  have hbpos : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hm : (0 : ℝ) < (b : ℝ) ^ k := pow_pos hbpos _
  have ha' : (a : ℝ) + 1 ≤ (b : ℝ) ^ k := by exact_mod_cast (Nat.succ_le_of_lt ha)
  have hlow : (0 : ℝ) ≤ (a : ℝ) / (b : ℝ) ^ k := div_nonneg (by positivity) hm.le
  have horder : (a : ℝ) / (b : ℝ) ^ k ≤ ((a : ℝ) + 1) / (b : ℝ) ^ k :=
    div_le_div_of_nonneg_right (by linarith) hm.le
  have hupper : ((a : ℝ) + 1) / (b : ℝ) ^ k ≤ 1 :=
    (div_le_one hm).mpr ha'
  have hc := hu _ _ hlow horder hupper
  have hwidth : ((a : ℝ) + 1) / (b : ℝ) ^ k - (a : ℝ) / (b : ℝ) ^ k =
      ((b : ℝ) ^ k)⁻¹ := by ring
  rw [hwidth] at hc
  simpa only [blockFrequency_eq_intervalFrequency hb] using hc

theorem pi_interval_equidistribution_implies_normal16
    (hu : UniformDistributionModOne (digitOrbit 16 Real.pi)) : PiNormal16 :=
  uniformDistribution_digitOrbit_implies_normal (by norm_num) Real.pi hu

theorem absoluteNormal_implies_normal10 (h : PiAbsolutelyNormal) : PiNormal10 :=
  h 10 (by norm_num)

/-- Rational endpoint convention: a terminating zero tail stays zero. -/
theorem canonicalBlock_zero (b k n : ℕ) : canonicalBlock b k n 0 = 0 := by
  simp [canonicalBlock, digitOrbit]

theorem zero_not_normal (b : ℕ) : ¬ NormalTo b 0 := by
  intro h
  have hb : 2 ≤ b := h.1
  have hlim := h.2 1 (by norm_num) 1 (by simpa using h.1)
  have hzero : (fun N => blockFrequency b 1 1 N 0) = fun _ : ℕ => (0 : ℝ) := by
    funext N
    simp [blockFrequency, canonicalBlock_zero]
  rw [hzero] at hlim
  have heq : (0 : ℝ) = ((b : ℝ) ^ 1)⁻¹ := tendsto_nhds_unique tendsto_const_nhds hlim
  have hbpos : (0 : ℝ) < b := by exact_mod_cast (show 0 < b by omega)
  have hipos : (0 : ℝ) < ((b : ℝ) ^ 1)⁻¹ := inv_pos.mpr (by simpa using hbpos)
  linarith

theorem zero_orbit_not_uniform {b : ℕ} (hb : 2 ≤ b) :
    ¬ UniformDistributionModOne (digitOrbit b 0) := by
  intro hu
  exact zero_not_normal b (uniformDistribution_digitOrbit_implies_normal hb 0 hu)

theorem circleHaar_total_mass : circleHaar Set.univ = 1 := by
  simpa [circleHaar] using (AddCircle.measure_univ (1 : ℝ))

end ObservationalSUCC.DuckPi
