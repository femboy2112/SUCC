/-!
Core Lean 4.14 algebra used by the paper's finite-group harmonic argument.
The inverse representative is an explicit hypothesis. Existence of that
representative, divergent series, Fourier analysis, and bounded operators
are paper proofs, not consequences certified by this file.
-/

namespace ObservationalSUCC.Round2

/-- A fixed inverse residue transfers an entire multiplicative residue
class to the identity class, including the trivial modulus 1. -/
theorem residue_transfer (q r t n : Nat)
    (inverse : (t * r) % q = 1 % q) (member : n % q = r % q) :
    (t * n) % q = 1 % q := by
  rw [Nat.mul_mod, member, ← Nat.mul_mod]
  exact inverse

/-- Multiplication by a positive representative has no collisions within
one class. This is the injection needed to transfer harmonic mass. -/
theorem transfer_injective (t : Nat) (positive : 0 < t) :
    ∀ a b : Nat, t * a = t * b → a = b := by
  intro a b equal
  exact Nat.eq_of_mul_eq_mul_left positive equal

/-- The transferred point stays in the multiplicative monoid and in a
controlled prefix. No finiteness or prime assumptions are hidden here. -/
theorem controlled_monoid_transfer
    (M : Nat → Prop) (closed : ∀ a b, M a → M b → M (a * b))
    (q r t n N C : Nat) (ht : M t) (hn : M n)
    (inverse : (t * r) % q = 1 % q) (member : n % q = r % q)
    (htC : t ≤ C) (hnN : n ≤ N) :
    M (t * n) ∧ (t * n) % q = 1 % q ∧ t * n ≤ C * N := by
  exact ⟨closed t n ht hn, residue_transfer q r t n inverse member,
    Nat.mul_le_mul htC hnN⟩

end ObservationalSUCC.Round2

#print axioms ObservationalSUCC.Round2.residue_transfer
#print axioms ObservationalSUCC.Round2.transfer_injective
#print axioms ObservationalSUCC.Round2.controlled_monoid_transfer
