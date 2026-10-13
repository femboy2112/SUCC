import Mathlib.Topology.Compactness.Compact

/-!
Compact-policy stopping core. The action/history induction establishing
openness is a separate paper proof in ROOT_POLICY_COMPACTNESS.md. This file
kernel-checks the exact compactness implication, not full policy semantics.
-/
namespace ObservationalSUCC.SwarmPolicyCompactness
open Set

universe u
variable {S : Type u} [TopologicalSpace S] [CompactSpace S]

/-- A fixed total stopping-time function whose bounded-halting sets are
open has one uniform finite bound on a compact original source. -/
theorem compact_stopping_depth_bound (stop : S → Nat)
    (haltOpen : ∀ n : Nat, IsOpen {s : S | stop s ≤ n}) :
    ∃ N : Nat, ∀ s : S, stop s ≤ N := by
  let halt : Nat → Set S := fun n => {s | stop s ≤ n}
  have cover : (Set.univ : Set S) ⊆ ⋃ n, halt n := by
    intro s _
    exact Set.mem_iUnion.mpr ⟨stop s, Nat.le_refl _⟩
  have directed : Directed (· ⊆ ·) halt := by
    intro m n
    refine ⟨max m n, ?_, ?_⟩
    · intro s hs
      exact Nat.le_trans hs (Nat.le_max_left m n)
    · intro s hs
      exact Nat.le_trans hs (Nat.le_max_right m n)
  obtain ⟨N, bound⟩ := isCompact_univ.elim_directed_cover halt haltOpen cover directed
  exact ⟨N, fun s => bound (Set.mem_univ s)⟩

end ObservationalSUCC.SwarmPolicyCompactness
