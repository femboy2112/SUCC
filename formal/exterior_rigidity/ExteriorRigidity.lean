import Mathlib.LinearAlgebra.Matrix.Determinant.Basic
import Mathlib.Algebra.GCDMonoid.Finset
import Mathlib.Algebra.GCDMonoid.Nat
import Mathlib.Data.Int.GCD
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.Ring

/-!
# Source-indexed exterior divisibility

The finite dimension is an arbitrary finite index type. Columns are source
points, rows are arithmetic coordinates. The effective shared-prime modulus is
proved by combining divisibility channels using finite gcds; no pairwise
coprimality assumption is inserted. This file does not prove a counting theorem,
a global weighted moment, or a rank-stratum census.
-/

set_option autoImplicit false

open scoped BigOperators
open Finset

namespace ObservationalSUCC.ExteriorRigidity

variable {n : Type*} [Fintype n] [DecidableEq n]

/-- Rowwise divisibility multiplies in the determinant over any commutative ring. -/
theorem row_product_dvd_det {R : Type*} [CommRing R]
    (A : Matrix n n R) (d : n → R) (hrows : ∀ i j, d i ∣ A i j) :
    (∏ i, d i) ∣ A.det := by
  classical
  let B : Matrix n n R := fun i j => Classical.choose (hrows i j)
  refine ⟨Matrix.det B, ?_⟩
  rw [← Matrix.det_mul_column d B]
  congr 1
  ext i j
  exact Classical.choose_spec (hrows i j)

/-- Replacing one row by the complete source sum leaves the determinant unchanged. -/
theorem source_sum_replacement {R : Type*} [CommRing R]
    (A : Matrix n n R) (i : n) :
    (A.updateRow i (∑ k, A k)).det = A.det := by
  simpa using Matrix.det_updateRow_sum A i (fun _ => (1 : R))

/-- Every replaced row gives a distinct valid arithmetic divisibility channel. -/
theorem source_sum_channel {R : Type*} [CommRing R]
    (A : Matrix n n R) (d : n → R) (q : R) (i : n)
    (hrows : ∀ k j, d k ∣ A k j) (hsum : ∀ j, q ∣ ∑ k, A k j) :
    (∏ k, Function.update d i q k) ∣ A.det := by
  rw [← source_sum_replacement A i]
  apply row_product_dvd_det
  intro k j
  by_cases hk : k = i
  · subst k
    simpa [Matrix.updateRow_apply, Finset.sum_apply] using hsum j
  · simpa [Matrix.updateRow_apply, hk] using hrows k j

/-- Clearing a single replaced-row factor gives the common full-product channel. -/
theorem source_sum_scaled_channel {R : Type*} [CommRing R]
    (A : Matrix n n R) (d : n → R) (q : R) (i : n)
    (hrows : ∀ k j, d k ∣ A k j) (hsum : ∀ j, q ∣ ∑ k, A k j) :
    (∏ k, d k) * q ∣ d i * A.det := by
  have h := mul_dvd_mul_left (d i) (source_sum_channel A d q i hrows hsum)
  have hu : (∏ k, Function.update d i q k) = q * ∏ k ∈ univ.erase i, d k := by
    simpa only [Finset.sdiff_singleton_eq_erase] using
      Finset.prod_update_of_mem (Finset.mem_univ i) d q
  have hp := Finset.mul_prod_erase univ d (Finset.mem_univ i)
  have heq : d i * (∏ k, Function.update d i q k) = (∏ k, d k) * q := by
    rw [hu, ← hp]
    ring
  rwa [heq] at h

/-- The row product divides the nonnegative determinant magnitude exactly. -/
theorem row_product_dvd_natAbs (A : Matrix n n ℤ) (d : n → ℕ)
    (hrows : ∀ i j, (d i : ℤ) ∣ A i j) :
    (∏ i, d i) ∣ A.det.natAbs := by
  have hz : ((∏ i, d i : ℕ) : ℤ) ∣ A.det := by
    simpa only [Nat.cast_prod] using row_product_dvd_det A (fun i => (d i : ℤ)) hrows
  simpa only [Int.natAbs_ofNat] using Int.natAbs_dvd_natAbs.mpr hz

/-- The effective shared-prime modulus divides the determinant magnitude. -/
theorem effective_shared_prime_modulus (A : Matrix n n ℤ) (d : n → ℕ) (q : ℕ)
    (hq : 0 < q) (hrows : ∀ i j, (d i : ℤ) ∣ A i j)
    (hsum : ∀ j, (q : ℤ) ∣ ∑ i, A i j) :
    ((∏ i, d i) * q / Nat.gcd q (univ.gcd d)) ∣ A.det.natAbs := by
  let P := ∏ i, d i
  let g := univ.gcd d
  let z := A.det.natAbs
  have hp : P ∣ z := row_product_dvd_natAbs A d hrows
  have hchannels : ∀ i, P * q ∣ d i * z := by
    intro i
    have hz : ((P * q : ℕ) : ℤ) ∣ (d i : ℤ) * A.det := by
      simpa [P, Nat.cast_prod] using
        source_sum_scaled_channel A (fun k => (d k : ℤ)) (q : ℤ) i hrows hsum
    simpa only [Int.natAbs_mul, Int.natAbs_ofNat] using Int.natAbs_dvd_natAbs.mpr hz
  have hg : P * q ∣ g * z := by
    have h := Finset.dvd_gcd (s := (univ : Finset n)) (f := fun i => d i * z)
      (fun i _ => hchannels i)
    simpa [g, Finset.gcd_mul_right] using h
  have hqz : P * q ∣ q * z := by
    obtain ⟨k, hk⟩ := hp
    refine ⟨k, ?_⟩
    rw [hk]
    ring
  have hboth : P * q ∣ Nat.gcd q g * z := by
    have h := Nat.dvd_gcd hqz hg
    rwa [Nat.gcd_mul_right] at h
  have hpositive : 0 < Nat.gcd q g := Nat.gcd_pos_of_pos_left g hq
  have hfactor : Nat.gcd q g * (P * q / Nat.gcd q g) = P * q :=
    Nat.mul_div_cancel' (dvd_mul_of_dvd_right (Nat.gcd_dvd_left q g) P)
  apply Nat.dvd_of_mul_dvd_mul_left hpositive
  rwa [hfactor]

/-- One globally primitive column forces the gcd of the row moduli to be one. -/
theorem primitive_column_forces_modulus_gcd_one
    (A : Matrix n n ℤ) (d : n → ℕ) (j : n)
    (hrows : ∀ i k, (d i : ℤ) ∣ A i k)
    (hprimitive : univ.gcd (fun i => (A i j).natAbs) = 1) :
    univ.gcd d = 1 := by
  apply Nat.dvd_one.mp
  rw [← hprimitive]
  apply Finset.dvd_gcd
  intro i _
  apply (Finset.gcd_dvd (Finset.mem_univ i)).trans
  simpa only [Int.natAbs_ofNat] using Int.natAbs_dvd_natAbs.mpr (hrows i j)

/-- Global primitivity restores the full product, even for overlapping prime moduli. -/
theorem primitive_full_product (A : Matrix n n ℤ) (d : n → ℕ) (q : ℕ) (j : n)
    (hq : 0 < q) (hrows : ∀ i k, (d i : ℤ) ∣ A i k)
    (hsum : ∀ k, (q : ℤ) ∣ ∑ i, A i k)
    (hprimitive : univ.gcd (fun i => (A i j).natAbs) = 1) :
    (∏ i, d i) * q ∣ A.det.natAbs := by
  have h := effective_shared_prime_modulus A d q hq hrows hsum
  rw [primitive_column_forces_modulus_gcd_one A d j hrows hprimitive] at h
  simpa using h

/-- An exact determinant bound below a divisor forces vanishing.
This lemma takes the size bound as a hypothesis; it does not assert Hadamard's bound. -/
theorem determinant_vanishes_below_modulus (A : Matrix n n ℤ) (E : ℕ)
    (hdiv : E ∣ A.det.natAbs) (hbound : A.det.natAbs < E) : A.det = 0 := by
  by_contra hne
  have hz : 0 < A.det.natAbs := Int.natAbs_pos.mpr hne
  exact (not_le_of_gt hbound) (Nat.le_of_dvd hz hdiv)

/-- Dropping primitivity really loses a shared prime: the full modulus 16 fails. -/
theorem nonprimitive_shared_prime_control :
    (Matrix.det (!![(2 : ℤ), 4, 2; 2, 2, 4; 2, 2, 2])).natAbs = 8 ∧
    ¬ (16 : ℕ) ∣ (Matrix.det (!![(2 : ℤ), 4, 2; 2, 2, 4; 2, 2, 2])).natAbs := by
  norm_num [Matrix.det_fin_three, Matrix.vecHead, Matrix.vecTail]

/-- Two different positive, globally primitive three-summand points can exceed
the cubic modulus threshold. This is a finite counterexample, not an asymptotic count. -/
theorem higher_dimensional_nonsingleton_control :
    (1001 : ℕ) + 3006 + 2003 = 6010 ∧
    (2002 : ℕ) + 5010 + 2003 = 9015 ∧
    Nat.gcd (Nat.gcd 1001 3006) 2003 = 1 ∧
    Nat.gcd (Nat.gcd 2002 5010) 2003 = 1 ∧
    1001 ∣ (1001 : ℕ) ∧ 1001 ∣ (2002 : ℕ) ∧
    1002 ∣ (3006 : ℕ) ∧ 1002 ∣ (5010 : ℕ) ∧
    2003 ∣ (2003 : ℕ) ∧ 3005 ∣ (6010 : ℕ) ∧ 3005 ∣ (9015 : ℕ) ∧
    6010 ≤ (9015 : ℕ) ∧
    (1001, 3006, 2003, 6010) ≠ ((2002, 5010, 2003, 9015) : ℕ × ℕ × ℕ × ℕ) ∧
    (9015 : ℕ) ^ 3 < 1001 * 1002 * 2003 * 3005 := by
  norm_num

end ObservationalSUCC.ExteriorRigidity
