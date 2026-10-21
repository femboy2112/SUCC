import Mathlib.RingTheory.Coprime.Lemmas
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Primitive determinant rigidity

Classical arithmetic, formalized for the primitive abc weighted-moment argument.
The module proves the determinant/divisibility and reduced-slope injectivity
obligations. It does not formalize the full weighted-moment or counting theorem.
-/

set_option autoImplicit false

namespace ObservationalSUCC.PrimitiveSlope

/-- The three independent divisibility channels in an additive triple. -/
theorem determinant_divisibility_int
    {a b c a' b' c' d e f : ℤ}
    (hs : a + b = c) (hs' : a' + b' = c')
    (hde : IsCoprime d e) (hdf : IsCoprime d f) (hef : IsCoprime e f)
    (hda : d ∣ a) (hda' : d ∣ a')
    (heb : e ∣ b) (heb' : e ∣ b')
    (hfc : f ∣ c) (hfc' : f ∣ c') :
    d * e * f ∣ a * c' - a' * c := by
  have hd : d ∣ a * c' - a' * c :=
    dvd_sub (dvd_mul_of_dvd_left hda c') (dvd_mul_of_dvd_left hda' c)
  have he : e ∣ a * c' - a' * c := by
    have he' : e ∣ a * b' - a' * b :=
      dvd_sub (dvd_mul_of_dvd_right heb' a) (dvd_mul_of_dvd_right heb a')
    have hid : a * c' - a' * c = a * b' - a' * b := by
      rw [← hs, ← hs']
      ring
    rw [hid]
    exact he'
  have hf : f ∣ a * c' - a' * c :=
    dvd_sub (dvd_mul_of_dvd_right hfc' a) (dvd_mul_of_dvd_right hfc a')
  exact (hdf.mul_left hef).mul_dvd (hde.mul_dvd hd he) hf

/-- Natural divisibility transports exactly to the integer determinant. -/
theorem nat_dvd_int_cast {d a : ℕ} (h : d ∣ a) : (d : ℤ) ∣ (a : ℤ) := by
  rcases h with ⟨k, hk⟩
  refine ⟨(k : ℤ), ?_⟩
  simpa only [Nat.cast_mul] using congrArg (fun n : ℕ => (n : ℤ)) hk

/-- The prescribed pairwise-coprime modulus divides the signed determinant. -/
theorem determinant_divisibility
    {a b c a' b' c' d e f : ℕ}
    (hs : a + b = c) (hs' : a' + b' = c')
    (hde : d.Coprime e) (hdf : d.Coprime f) (hef : e.Coprime f)
    (hda : d ∣ a) (hda' : d ∣ a')
    (heb : e ∣ b) (heb' : e ∣ b')
    (hfc : f ∣ c) (hfc' : f ∣ c') :
    ((d * e * f : ℕ) : ℤ) ∣ (a : ℤ) * c' - (a' : ℤ) * c := by
  have hsZ : (a : ℤ) + b = c := by
    simpa only [Nat.cast_add] using congrArg (fun n : ℕ => (n : ℤ)) hs
  have hsZ' : (a' : ℤ) + b' = c' := by
    simpa only [Nat.cast_add] using congrArg (fun n : ℕ => (n : ℤ)) hs'
  simpa only [Nat.cast_mul] using determinant_divisibility_int hsZ hsZ'
    hde.isCoprime hdf.isCoprime hef.isCoprime
    (nat_dvd_int_cast hda) (nat_dvd_int_cast hda')
    (nat_dvd_int_cast heb) (nat_dvd_int_cast heb')
    (nat_dvd_int_cast hfc) (nat_dvd_int_cast hfc')

/-- Equal cross-products of reduced nonnegative fractions force equal pairs. -/
theorem reduced_pair_injective
    {a c a' c' : ℕ} (hc : 0 < c) (hc' : 0 < c')
    (hac : a.Coprime c) (hac' : a'.Coprime c')
    (h : a * c' = a' * c) : a = a' ∧ c = c' := by
  have hcc' : c ∣ c' := hac.symm.dvd_of_dvd_mul_left
    ⟨a', h.trans (mul_comm a' c)⟩
  have hc'c : c' ∣ c := hac'.symm.dvd_of_dvd_mul_left
    ⟨a, h.symm.trans (mul_comm a c')⟩
  have heq : c = c' := Nat.dvd_antisymm hcc' hc'c
  subst c'
  exact ⟨mul_right_cancel₀ (Nat.ne_of_gt hc) h, rfl⟩

/-- Distinct primitive triples have a nonzero signed determinant. -/
theorem primitive_triple_determinant_ne_zero
    {a b c a' b' c' : ℕ} (hc : 0 < c) (hc' : 0 < c')
    (hs : a + b = c) (hs' : a' + b' = c')
    (hab : a.Coprime b) (hab' : a'.Coprime b')
    (hne : (a, b, c) ≠ (a', b', c')) :
    (a : ℤ) * c' - (a' : ℤ) * c ≠ 0 := by
  intro hz
  have hac : a.Coprime c := hs ▸ Nat.coprime_self_add_right.mpr hab
  have hac' : a'.Coprime c' := hs' ▸ Nat.coprime_self_add_right.mpr hab'
  have hint : ((a * c' : ℕ) : ℤ) = ((a' * c : ℕ) : ℤ) := by
    simpa only [Nat.cast_mul] using sub_eq_zero.mp hz
  obtain ⟨ha, he⟩ := reduced_pair_injective hc hc' hac hac' (Int.ofNat.inj hint)
  have hsum : a' + b = a' + b' := by
    calc
      a' + b = c' := by simpa [ha, he] using hs
      _ = a' + b' := hs'.symm
  have hb : b = b' := Nat.add_left_cancel hsum
  exact hne (by simp [ha, hb, he])

/-- A nonzero integer multiple has absolute size at least its natural modulus. -/
theorem modulus_le_natAbs {D : ℕ} {z : ℤ} (hdiv : (D : ℤ) ∣ z) (hz : z ≠ 0) :
    D ≤ z.natAbs := by
  rcases hdiv with ⟨k, hk⟩
  have hk0 : k ≠ 0 := by
    intro hkz
    apply hz
    simp [hkz] at hk
    exact hk
  have hkpos : 0 < k.natAbs := Nat.pos_of_ne_zero (by simpa using hk0)
  rw [hk, Int.natAbs_mul, Int.natAbs_ofNat]
  exact Nat.le_mul_of_pos_right D hkpos

/-- The load-bearing discrete separation invariant used in the paper proof. -/
theorem primitive_determinant_gap
    {a b c a' b' c' d e f : ℕ}
    (hc : 0 < c) (hc' : 0 < c')
    (hs : a + b = c) (hs' : a' + b' = c')
    (hab : a.Coprime b) (hab' : a'.Coprime b')
    (hne : (a, b, c) ≠ (a', b', c'))
    (hde : d.Coprime e) (hdf : d.Coprime f) (hef : e.Coprime f)
    (hda : d ∣ a) (hda' : d ∣ a')
    (heb : e ∣ b) (heb' : e ∣ b')
    (hfc : f ∣ c) (hfc' : f ∣ c') :
    d * e * f ≤ ((a : ℤ) * c' - (a' : ℤ) * c).natAbs :=
  modulus_le_natAbs
    (determinant_divisibility hs hs' hde hdf hef hda hda' heb heb' hfc hfc')
    (primitive_triple_determinant_ne_zero hc hc' hs hs' hab hab' hne)

/-- Nonprimitive equal slopes show why reducedness cannot be dropped. -/
theorem nonprimitive_control :
    (1 : ℕ) * 4 = 2 * 2 ∧ (1, 1, 2) ≠ (2, 2, 4) ∧ ¬ Nat.Coprime 2 2 := by
  norm_num

/-- Shared modulus factors do not multiply independently. -/
theorem noncoprime_moduli_control : ¬ (8 : ℤ) ∣ 2 * 6 - 2 * 4 := by
  norm_num

end ObservationalSUCC.PrimitiveSlope

#print axioms ObservationalSUCC.PrimitiveSlope.determinant_divisibility
#print axioms ObservationalSUCC.PrimitiveSlope.reduced_pair_injective
#print axioms ObservationalSUCC.PrimitiveSlope.primitive_triple_determinant_ne_zero
#print axioms ObservationalSUCC.PrimitiveSlope.primitive_determinant_gap
