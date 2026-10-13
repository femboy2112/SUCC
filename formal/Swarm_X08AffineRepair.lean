import Std.Tactic

/-! X08: any reflexive, transitive successor-stable relation on Nat is
stable under every natural affine map. The finite cyclic classification,
valuation-memory theorem and arithmetic log/covariance audits are paper
proofs with independent exact controls, not formalized by this module. -/

namespace SwarmX08

theorem translation_stable {R : Nat → Nat → Prop}
    (succ_stable : ∀ {x y}, R x y → R (x + 1) (y + 1))
    {x y : Nat} (related : R x y) (offset : Nat) :
    R (x + offset) (y + offset) := by
  induction offset with
  | zero => simpa using related
  | succ offset ih =>
      simpa [Nat.add_assoc] using succ_stable ih

theorem dilation_stable {R : Nat → Nat → Prop}
    (refl : ∀ x, R x x)
    (trans : ∀ {x y z}, R x y → R y z → R x z)
    (succ_stable : ∀ {x y}, R x y → R (x + 1) (y + 1))
    {x y : Nat} (related : R x y) (slope : Nat) :
    R (slope * x) (slope * y) := by
  induction slope with
  | zero => simpa using refl 0
  | succ slope ih =>
      have first : R (slope * x + x) (slope * y + x) :=
        translation_stable (R := R) succ_stable ih x
      have second : R (slope * y + x) (slope * y + y) := by
        simpa [Nat.add_comm] using
          translation_stable (R := R) succ_stable related (slope * y)
      simpa [Nat.succ_mul] using trans first second

theorem affine_stable {R : Nat → Nat → Prop}
    (refl : ∀ x, R x x)
    (trans : ∀ {x y z}, R x y → R y z → R x z)
    (succ_stable : ∀ {x y}, R x y → R (x + 1) (y + 1))
    {x y : Nat} (related : R x y) (slope offset : Nat) :
    R (slope * x + offset) (slope * y + offset) := by
  exact translation_stable (R := R) succ_stable
    (dilation_stable (R := R) refl trans succ_stable related slope) offset

end SwarmX08
