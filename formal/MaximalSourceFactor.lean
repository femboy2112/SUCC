/-!
Maximal source novelty: the finite-factor and exact-decoder kernel.
Lean 4.14.0 standalone; no mathlib, source-randomness axiom, or sorry.

This file deliberately proves only algebraic obstruction lemmas.
Algorithmic randomness, density of random shift orbits, and the existence
of an incompressible source are classical external inputs, NOT formalized.
-/
namespace ObservationalSUCC.MaximalSourceFactor

universe u v

/-- Exact reconstruction on every source state demands an injective report. -/
theorem exact_recovery_requires_injective
    {X : Type u} {Report : Type v}
    (observe : X → Report) (decode : Report → X)
    (recover : ∀ x, decode (observe x) = x) :
    Function.Injective observe := by
  intro x y hxy
  calc
    x = decode (observe x) := (recover x).symm
    _ = decode (observe y) := congrArg decode hxy
    _ = y := recover y

/-- A fixed source point excludes every equivariant factor with
    fixed-point-free target dynamics. Continuity is not needed. -/
theorem fixed_point_blocks_clock_factor
    {X : Type u} {Clock : Type v}
    (step : X → X) (tick : Clock → Clock)
    (source : X)
    (fixed : step source = source)
    (no_fixed_clock : ∀ c : Clock, tick c ≠ c) :
    ¬ ∃ (read : X → Clock), ∀ x, read (step x) = tick (read x) := by
  intro h
  obtain ⟨read, equivariant⟩ := h
  have eq : read source = tick (read source) := by
    simpa [fixed] using equivariant source
  exact no_fixed_clock (read source) eq.symm

def BitTape := Nat → Bool
def shift (x : BitTape) : BitTape := fun n => x (n + 1)
def zeroTape : BitTape := fun _ => false

theorem zero_is_fixed : shift zeroTape = zeroTape := rfl

theorem bool_flip_has_no_fixed_point (b : Bool) : (!b) ≠ b := by
  cases b <;> decide

/-- Not even a set-theoretic equivariant two-cycle factor exists on the
    ENTIRE full shift, because its all-zero tape is a fixed point. -/
theorem full_binary_shift_has_no_two_clock :
    ¬ ∃ (q : BitTape → Bool), ∀ x, q (shift x) = !(q x) := by
  exact fixed_point_blocks_clock_factor shift (fun b : Bool => !b)
    zeroTape zero_is_fixed bool_flip_has_no_fixed_point

end ObservationalSUCC.MaximalSourceFactor
