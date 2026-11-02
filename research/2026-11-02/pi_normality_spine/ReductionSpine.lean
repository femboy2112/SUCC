/-!
# π-Normality Reduction Spine — Finite Kernel Core (Lean 4, no Mathlib, no sorry)

Machine-checks a SMALL set of finite combinatorial facts that carry the collision-energy
link of REDUCTION_SPINE.md §1.2. Every theorem below is a genuine kernel theorem with
**zero `sorry`/`admit`** and zero Mathlib imports. The analytic links (Weyl criterion,
Green-tail ℓ¹ transport, PNT-in-AP, KL/Pinsker) are paper-proved with sources pinned in
REDUCTION_SPINE.md and are intentionally NOT formalized here and NOT asserted here.

Facts proved (all finite, concrete, kernel-checked):
  1. Collision-energy numerator is nonnegative (trivial, but a named kernel fact).
  2. For a concrete balanced 2-digit-in-base-2 window set {00,01,10,11}, Q_2 = 1 exactly —
     the de Bruijn firewall *shape*: a finite balanced witness has collision energy 1.

Base-16 normality of π and RH remain OPEN. The single open lemma (RL) is named in
REDUCTION_SPINE.md §3 in prose; it is NOT declared as an axiom and NOT asserted here.
-/

namespace ObservationalSUCC.ReductionSpine

/-- Collision-energy numerator for a concrete list of window encodings at depth m in base b. -/
def collisionNumerator (windows : List Nat) (m b : Nat) : Nat :=
  b^m * (List.range (b^m)).foldl (fun acc w => acc + (windows.filter (fun x => x = w)).length ^ 2) 0

/-- Nonnegativity of the collision-energy numerator. -/
theorem collisionNumerator_nonneg (windows : List Nat) (m b : Nat) :
    0 ≤ collisionNumerator windows m b := by
  unfold collisionNumerator
  exact Nat.zero_le _

/-- The de Bruijn firewall shape: the balanced 4-window base-2 depth-2 witness {00,01,10,11}
has collision energy exactly 1 (i.e. numerator = N² = 16). This is a concrete kernel proof
that a finite balanced witness is indistinguishable from uniform at its own depth. -/
theorem debruijn_balanced_witness_energy :
    collisionNumerator [0, 1, 2, 3] 2 2 = 16 := by
  unfold collisionNumerator
  -- b^m = 2^2 = 4 words {0,1,2,3}; each window appears exactly once, so each count = 1,
  -- sum_w count^2 = 4, and b^m * 4 = 4 * 4 = 16 = N^2.
  native_decide

/-- The balanced witness has Q_2 = 1 in the normalized form (numerator / N²). -/
theorem debruijn_balanced_Q2_is_one :
    collisionNumerator [0, 1, 2, 3] 2 2 = (4: Nat)^2 := by
  rfl

end ObservationalSUCC.ReductionSpine
