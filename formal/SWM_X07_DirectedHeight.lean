import Std.Tactic

/-!
Directed finite-height support bottlenecks, Lean 4.14 core + Std.
The index type need not be countable. Cone positivity, faithful masses,
face rank and construction of the causal ideal diagram remain the separately
reviewed paper instantiation. No effective bottleneck finder is supplied.
-/
namespace ObservationalSUCC.SWM_X07

universe u v

theorem bounded_rank_max {D : Type u} (base : D) (r : D → Nat)
    (d : Nat) (cap : ∀ i, r i ≤ d) :
    ∃ i, ∀ j, r j ≤ r i := by
  classical
  induction d with
  | zero =>
      refine ⟨base, ?_⟩
      intro j
      have hj := cap j
      omega
  | succ d ih =>
      by_cases hit : ∃ i, r i = d + 1
      · obtain ⟨i, hi⟩ := hit
        refine ⟨i, ?_⟩
        intro j
        have hj := cap j
        omega
      · apply ih
        intro j
        have hj := cap j
        have he : r j ≠ d + 1 := fun h => hit ⟨j, h⟩
        omega

theorem greatest_dead_support {D : Type u} {X : Type v}
    (base : D) (Rel : D → D → Prop) (F : D → X → Prop)
    (r : D → Nat) (d : Nat)
    (directed : ∀ i j, ∃ k, Rel i k ∧ Rel j k)
    (monoRank : ∀ i j, Rel i j → r i ≤ r j)
    (cap : ∀ i, r i ≤ d)
    (monoDead : ∀ i j, Rel i j → ∀ x, F i x → F j x)
    (sameRank : ∀ i j, Rel i j → r i = r j → ∀ x, F i x ↔ F j x) :
    ∃ i, ∀ j x, F j x → F i x := by
  obtain ⟨i, maximal⟩ := bounded_rank_max base r d cap
  refine ⟨i, ?_⟩
  intro j x hx
  obtain ⟨k, hik, hjk⟩ := directed i j
  have heq : r i = r k := Nat.le_antisymm (monoRank i k hik) (maximal k)
  exact (sameRank i k hik heq x).mpr (monoDead j k hjk x hx)

theorem directed_rank_support_realization {D : Type u} {X : Type v}
    (base : D) (Rel : D → D → Prop) (F : D → X → Prop)
    (r : D → Nat) (d : Nat)
    (directed : ∀ i j, ∃ k, Rel i k ∧ Rel j k)
    (monoRank : ∀ i j, Rel i j → r i ≤ r j)
    (cap : ∀ i, r i ≤ d)
    (monoDead : ∀ i j, Rel i j → ∀ x, F i x → F j x)
    (sameRank : ∀ i j, Rel i j → r i = r j → ∀ x, F i x ↔ F j x)
    (every : ∀ i, ∃ x, ¬ F i x) :
    ∃ x, ∀ i, ¬ F i x := by
  obtain ⟨i, greatest⟩ := greatest_dead_support base Rel F r d
    directed monoRank cap monoDead sameRank
  obtain ⟨x, hx⟩ := every i
  refine ⟨x, ?_⟩
  intro j hj
  exact hx (greatest j x hj)

#print axioms bounded_rank_max
#print axioms greatest_dead_support
#print axioms directed_rank_support_realization
end ObservationalSUCC.SWM_X07
