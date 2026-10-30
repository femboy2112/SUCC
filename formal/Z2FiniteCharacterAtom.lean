import Std.Tactic

/-!
# Z/2^n — the finite atom of the Z_2 character-group correspondence

Pinned compiler: Lean 4.14.0. No Mathlib. This file proves ONLY the finite
level of the correspondence between the 2-adic integers Z_2 and its (Pontryagin)
dual Q_2/Z_2, the group of dyadic rationals mod 1.

Every finite atom of the correspondence is the finite cyclic group

    Z/2^n  ≃  { a / 2^n : 0 ≤ a < 2^n }  (dyadic rationals of denominator 2^n).

At the fixed level `n` we prove:

  * `lift` maps a character label `a : Z/2^n` to the dyadic rational `a / 2^n`
    represented by the pair `(a, 2^n)` (numerator, denominator).

  * `dyadic_lift_injective` — two labels coincide iff their dyadic lifts
    coincide: `lift a = lift a' ↔ a = a'`.  (Equivalently the characters
    `χ_a, χ_a'` agree on every element iff `a ≡ a' mod 2^n`.)

  * `dyadic_lift_surjective` — at the fixed level every dyadic rational with
    denominator `2^n` (and numerator `< 2^n`) is realized by some `a : Z/2^n`,
    and the realizing label is unique.

  * `character_map_injective` — the additive character `χ_a(x) = (a·x) mod 2^n`
    is injective in `a` (evaluation at the generator `1` recovers `a` exactly).

  * `character_map_surjective` — every additive homomorphism `φ : Z/2^n → Z/2^n`
    is of the form `χ_a` for `a = φ(1)`: the finite character group of `Z/2^n`
    is exactly `Z/2^n` realized by dyadic labels.

BOUNDARY (stated, not attempted): the inverse-limit assembly of these atoms
into the full character group `Hom(Z_2, S¹) ≃ Q_2/Z_2`, and the 2-adic /
Prüfer-2 topology, require Mathlib's topology and category/library
infrastructure. Those are OUT OF SCOPE here; this file is the finite atom only.
-/

namespace ObservationalSUCC.Z2FiniteCharacterAtom

set_option maxRecDepth 10000
set_option maxHeartbeats 4000000

/-- The finite cyclic group `Z/2^n`, realised as the residues `0 .. 2^n - 1`. -/
abbrev Z2n (n : Nat) := Fin (2 ^ n)

/-- A dyadic rational of denominator `2^n`: numerator `< 2^n`, denominator `2^n`. -/
def Dyadic (n : Nat) := { m : Nat // m < 2 ^ n }

/-- `0 < 2^n` for every `n`. -/
theorem two_pow_pos (n : Nat) : 0 < 2 ^ n := Nat.pow_pos (by decide : 0 < 2)

/-- `1 < 2^n` for `n ≥ 1`, so that `1` reduces and `1 % 2^n = 1`. -/
theorem one_lt_two_pow (n : Nat) (h : 0 < n) : 1 < 2 ^ n := by
  have hle : 2 ≤ 2 ^ n := Nat.pow_le_pow_of_le_right (by decide : 0 < 2) (Nat.succ_le_of_lt h)
  omega

/-- Addition on `Z/2^n`. -/
def addZ2n {n : Nat} (a b : Z2n n) : Z2n n :=
  ⟨(a.val + b.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩

/-- The generator `1` of `Z/2^n`. -/
def gen {n : Nat} : Z2n n := ⟨1 % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩

/-- Lift a character label `a : Z/2^n` to the dyadic rational `a / 2^n`,
represented by the pair `(numerator, denominator)`. -/
def lift {n : Nat} (a : Z2n n) : Nat × Nat := (a.val, 2 ^ n)

/-- The additive character `χ_a` of `Z/2^n` determined by the label `a`.
The primitive `2^n`-th root of unity is represented by its exponent residue:
`χ_a(x) = (a·x) mod 2^n`. This is the complete finite phase data — no topology
or complex numbers are smuggled in. -/
def char {n : Nat} (a x : Z2n n) : Z2n n :=
  ⟨(a.val * x.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩

/-- The residue `a.val` is already reduced: `a.val % 2^n = a.val`. -/
theorem val_mod_self {n : Nat} (a : Z2n n) : a.val % (2 ^ n) = a.val :=
  Nat.mod_eq_of_lt a.isLt

/-- `(v + v) % m = v` with `0 < m` and `v < m` forces `v = 0`: a nonzero residue
cannot be a proper idempotent under addition mod `m`. -/
theorem double_mod_eq_self_implies_zero {m v : Nat} (hv : v < m)
    (h : (v + v) % m = v) : v = 0 := by
  have divalg := Nat.mod_add_div (v + v) m
  rw [h] at divalg
  have hq : m * ((v + v) / m) = v := Nat.add_left_cancel divalg
  by_cases hqpos : 0 < (v + v) / m
  · have hq1 : 1 ≤ (v + v) / m := hqpos
    have hmul : m ≤ m * ((v + v) / m) := by
      calc
        m = m * 1 := by rw [Nat.mul_one]
        _ ≤ m * ((v + v) / m) := Nat.mul_le_mul_left m hq1
    have : m ≤ v := by rw [← hq]; exact hmul
    exfalso; exact (Nat.not_lt_of_ge this) hv
  · have hq0 : (v + v) / m = 0 := Nat.eq_zero_of_le_zero (Nat.le_of_not_gt hqpos)
    rw [hq0, Nat.mul_zero] at hq
    exact hq.symm

/-- The dyadic lift is injective: `lift a = lift a' ↔ a = a'`.

The forward direction is exactly "two dyadic labels `a/2^n`, `a'/2^n` are equal
iff `a ≡ a' mod 2^n`", because equality of the represented pairs is equality of
numerators, and equality of numerators is equality of residues `a = a'` in
`Z/2^n = Fin (2^n)`. -/
theorem dyadic_lift_injective {n : Nat} (a a' : Z2n n) :
    lift a = lift a' ↔ a = a' := by
  constructor
  · intro h
    have hnum : a.val = a'.val := by
      exact congrArg Prod.fst h
    exact Fin.ext hnum
  · intro h
    rw [h]

/-- At the fixed level every dyadic rational `a/2^n` with `0 ≤ a < 2^n` is
realized by a unique character label: `lift` is surjective onto `Dyadic n`
(identified with its numerator/denominator pair). -/
theorem dyadic_lift_surjective {n : Nat} :
    ∀ d : Dyadic n, ∃ a : Z2n n, lift a = (d.val, 2 ^ n) := by
  intro d
  refine ⟨⟨d.val, d.property⟩, rfl⟩

/-- The realization is a bijection `Z/2^n ≃ Dyadic n` at the fixed level,
recorded as a plain pair of mutually-inverse functions (no `Equiv` import). -/
def dyadicTo {n : Nat} (a : Z2n n) : Dyadic n := ⟨a.val, a.isLt⟩
def dyadicFrom {n : Nat} (d : Dyadic n) : Z2n n := ⟨d.val, d.property⟩

theorem dyadicTo_from {n : Nat} (d : Dyadic n) : dyadicTo (dyadicFrom d) = d := rfl
theorem dyadicFrom_to {n : Nat} (a : Z2n n) : dyadicFrom (dyadicTo a) = a := rfl

/-- The character evaluated at the generator recovers the label `a` exactly
(for `n > 0`, when `1 % 2^n = 1`; for `n = 0` the group is trivial). -/
theorem char_at_gen_is_label {n : Nat} (a : Z2n n) (h : 0 < n) :
    char a (gen (n := n)) = a := by
  apply Fin.ext
  show (a.val * (1 % (2 ^ n))) % (2 ^ n) = a.val
  have h1 : 1 % (2 ^ n) = 1 := Nat.mod_eq_of_lt (one_lt_two_pow n h)
  rw [h1, Nat.mul_one, val_mod_self a]

/-- Injectivity via characters: if the additive characters `χ_a` and `χ_a'`
agree on every element, then `a = a'`. Evaluation at the generator recovers the
label exactly. -/
theorem character_map_injective {n : Nat} (a a' : Z2n n) (h : 0 < n)
    (hsame : ∀ x : Z2n n, char a x = char a' x) : a = a' := by
  have e : char a (gen (n := n)) = char a' (gen (n := n)) := hsame (gen (n := n))
  have hl : char a (gen (n := n)) = a := char_at_gen_is_label a h
  have hr : char a' (gen (n := n)) = a' := char_at_gen_is_label a' h
  exact (hl.symm.trans e).trans hr

/-- An additive homomorphism sends the zero element to the zero element. -/
theorem hom_zero {n : Nat} (φ : Z2n n → Z2n n)
    (additive : ∀ x y : Z2n n, φ (addZ2n x y) = addZ2n (φ x) (φ y)) :
    φ ⟨0, two_pow_pos n⟩ = ⟨0, two_pow_pos n⟩ := by
  let z : Z2n n := ⟨0, two_pow_pos n⟩
  have hz : addZ2n z z = z := by
    apply Fin.ext; rfl
  have add0 : φ z = addZ2n (φ z) (φ z) := by
    rw [← hz]; exact additive z z
  apply Fin.ext
  show (φ z).val = 0
  have hval : ((φ z).val + (φ z).val) % (2 ^ n) = (φ z).val :=
    (congrArg Fin.val add0).symm
  exact double_mod_eq_self_implies_zero (φ z).isLt hval

/-- `(k % m + 1) % m = (k + 1) % m`, valid when `1 % m = 1` (i.e. `m > 1`). -/
theorem mod_add_one {m k : Nat} (hm : 1 % m = 1) : (k % m + 1) % m = (k + 1) % m := by
  calc
    (k % m + 1) % m = (k % m + 1 % m) % m := by rw [hm]
    _ = (k + 1) % m := by rw [← Nat.add_mod]

/-- `(k * a % m + a) % m = ((k+1) * a) % m`, valid when `a % m = a`
(i.e. `a` is already reduced). -/
theorem mod_mul_add {m k a : Nat} (ha : a % m = a) :
    (k * a % m + a) % m = ((k + 1) * a) % m := by
  calc
    (k * a % m + a) % m = (k * a % m + a % m) % m := by rw [ha]
    _ = (k * a + a) % m := by rw [← Nat.add_mod]
    _ = ((k + 1) * a) % m := by rw [Nat.add_mul, Nat.one_mul]

/-- The character group at level `n` is realized by dyadic labels: every
additive homomorphism `φ : Z/2^n → Z/2^n` is determined by its value on the
generator and coincides with `χ_{φ(1)}` on every element. This is the finite
surjectivity of the correspondence: the map `a ↦ χ_a` (equivalently `a ↦ a/2^n`)
hits every finite character. -/
theorem character_map_surjective {n : Nat} (φ : Z2n n → Z2n n)
    (additive : ∀ x y : Z2n n, φ (addZ2n x y) = addZ2n (φ x) (φ y))
    (h : 0 < n) :
    ∃ a : Z2n n, ∀ x : Z2n n, φ x = char a x := by
  let a : Z2n n := φ (gen (n := n))
  refine ⟨a, ?_⟩
  intro x
  -- φ(x) = φ(x·1) = x·φ(1) = (a·x) mod 2^n = char a x
  have hmain : ∀ (k : Nat), φ ⟨k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ =
      ⟨(k * a.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ := by
    intro k
    induction k with
    | zero =>
      have hz : φ ⟨0 % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ = ⟨0, two_pow_pos n⟩ := by
        change φ ⟨0, two_pow_pos n⟩ = ⟨0, two_pow_pos n⟩
        exact hom_zero φ additive
      rw [hz]
      apply Fin.ext
      show (0 : Nat) = (0 * a.val) % (2 ^ n)
      rw [Nat.zero_mul, Nat.mod_eq_of_lt (two_pow_pos n)]
    | succ k ih =>
      have h1 : 1 % (2 ^ n) = 1 := Nat.mod_eq_of_lt (one_lt_two_pow n h)
      have ha : a.val % (2 ^ n) = a.val := val_mod_self a
      have hk : ⟨Nat.succ k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ =
          addZ2n ⟨k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ (gen (n := n)) := by
        apply Fin.ext
        show Nat.succ k % (2 ^ n) = (k % (2 ^ n) + (1 % (2 ^ n))) % (2 ^ n)
        rw [h1]
        exact (mod_add_one h1).symm
      calc
        φ ⟨Nat.succ k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩
            = φ (addZ2n ⟨k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ (gen (n := n))) := by rw [hk]
        _ = addZ2n (φ ⟨k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩) a := by
              exact additive ⟨k % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ (gen (n := n))
        _ = addZ2n ⟨(k * a.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ a := by rw [ih]
        _ = ⟨(Nat.succ k * a.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ := by
              apply Fin.ext
              change (k * a.val % (2 ^ n) + a.val) % (2 ^ n) = (Nat.succ k * a.val) % (2 ^ n)
              exact mod_mul_add ha
  -- x.val < 2^n so x.val % 2^n = x.val, hence x = ⟨x.val % 2^n⟩
  have hmain_x := hmain x.val
  have hxred : ⟨x.val % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ = x := by
    apply Fin.ext; exact val_mod_self x
  rw [hxred] at hmain_x
  calc
    φ x = ⟨(x.val * a.val) % (2 ^ n), Nat.mod_lt _ (two_pow_pos n)⟩ := hmain_x
    _ = char a x := by
        apply Fin.ext
        show (x.val * a.val) % (2 ^ n) = (a.val * x.val) % (2 ^ n)
        rw [Nat.mul_comm]

#print axioms dyadic_lift_injective
#print axioms dyadic_lift_surjective
#print axioms character_map_injective
#print axioms char_at_gen_is_label
#print axioms character_map_surjective

end ObservationalSUCC.Z2FiniteCharacterAtom
