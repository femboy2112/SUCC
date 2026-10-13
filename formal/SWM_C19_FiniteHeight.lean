import Std.Tactic

/-!
Finite-height support actualization, Lean 4.14 core + Std.
This proves the abstract bounded-rank mechanism, not the quantum operator
instantiation. Positivity, pulled-back effects, kernel dimensions and their
rank-reflection property remain explicitly paper-proved in C19 and its review.
No stabilization index is computed or bounded by the rank cap.
-/
namespace ObservationalSUCC.SWM_C19

theorem bounded_mono_eventually_constant (d : Nat) (r : Nat → Nat)
    (mono : ∀ m n, m ≤ n → r m ≤ r n)
    (cap : ∀ n, r n ≤ d) :
    ∃ N, ∀ n, N ≤ n → r n = r N := by
  classical
  induction d with
  | zero =>
      refine ⟨0, ?_⟩
      intro n _
      have hn := cap n
      have h0 := cap 0
      omega
  | succ d ih =>
      by_cases hit : ∃ N, r N = d + 1
      · obtain ⟨N, hN⟩ := hit
        refine ⟨N, ?_⟩
        intro n hn
        have hm := mono N n hn
        have hb := cap n
        omega
      · apply ih
        intro n
        have hb := cap n
        have he : r n ≠ d + 1 := fun h => hit ⟨n, h⟩
        omega

universe u

theorem finite_height_prefix_realization {X : Type u}
    (P : Nat → X → Prop) (r : Nat → Nat) (d : Nat)
    (mono : ∀ m n, m ≤ n → r m ≤ r n)
    (cap : ∀ n, r n ≤ d)
    (shrink : ∀ m n, m ≤ n → ∀ x, P n x → P m x)
    (sameRank : ∀ m n, m ≤ n → r m = r n → ∀ x, P m x ↔ P n x)
    (every : ∀ n, ∃ x, P n x) :
    ∃ x, ∀ n, P n x := by
  obtain ⟨N, stable⟩ := bounded_mono_eventually_constant d r mono cap
  obtain ⟨x, hx⟩ := every N
  refine ⟨x, ?_⟩
  intro n
  by_cases hn : n ≤ N
  · exact shrink n N hn x hx
  · have hN : N ≤ n := by omega
    exact (sameRank N n hN (stable n hN).symm x).mp hx

#print axioms bounded_mono_eventually_constant
#print axioms finite_height_prefix_realization
end ObservationalSUCC.SWM_C19
