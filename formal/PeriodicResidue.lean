/-!
# Periodic residue clock: the load-bearing lemma behind the tail enclosure

Pinned standalone Lean 4.14.0, no mathlib.  Formalizes the exact periodicity
fact powering `observational_succ/periodic_tail_enclosure.py` (claim PTE-01):
the residue clock `k ↦ k % n` is `L`-periodic whenever `n ∣ L`, and
periodicity is preserved under pointwise addition, so any finite linear
combination of residue clocks over a modulus family is lcm-periodic.

No zeta, no zero location, no real analysis: pure `Nat`-modular arithmetic.
-/

namespace PeriodicResidue

/-- `(k + L) % n = k % n` whenever `n > 0` and `n ∣ L`.  This single
statement is what the whole two-sided enclosure reduces to. -/
theorem residue_periodic (k n L : Nat) (hn : 0 < n) (hdiv : n ∣ L) :
    (k + L) % n = k % n := by
  have hL0 : L % n = 0 := Nat.dvd_iff_mod_eq_zero.mp hdiv
  rw [Nat.add_mod, hL0]
  exact Nat.mod_eq_of_lt (Nat.mod_lt k hn)

/-- The clock is `n`-periodic: reflexivity of divisibility. -/
theorem clock_periodic (k n : Nat) (hn : 0 < n) : (k + n) % n = k % n := by
  exact residue_periodic k n n hn ⟨1, by simp⟩

/-- Periodicity is preserved under pointwise addition: if both `f` and `g`
have period `L` then `f + g` does.  Lifts single-modulus periodicity to any
finite linear combination of residue clocks (by structural induction over the
family, one addition at a time). -/
theorem sum_periodic {α : Type} [Add α]
    (f g : Nat → α) (L : Nat)
    (hf : ∀ k, f (k + L) = f k) (hg : ∀ k, g (k + L) = g k) :
    ∀ k, f (k + L) + g (k + L) = f k + g k := by
  intro k
  rw [hf k, hg k]

/-- The synchronized cell `L` vanishes for every modulus dividing `L`:
`L % n = 0`.  This is the exact reason the blackout defect `|1 - F(L)|^2 = 1`
in the tail-split enclosure (TS-01): every residue clock reads 0 at the lcm
cell. -/
theorem blackout_cell_vanishes (n L : Nat) (hdiv : n ∣ L) : L % n = 0 :=
  Nat.dvd_iff_mod_eq_zero.mp hdiv

end PeriodicResidue
