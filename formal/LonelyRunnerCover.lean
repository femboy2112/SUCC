import Mathlib.Data.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
Source-labelled closed interval chains cover every real point of [0,1].
This proves the mathematical certificate semantics, not the Python parser,
SHA256 implementation, integer arithmetic runtime, or a particular JSON file.
-/

namespace SUCC.LonelyRunnerCover

variable {α : Type*}

/-- A nonempty chain, with overlap at its current frontier. -/
inductive ClosedChain (left right : α → ℝ) : ℝ → ℝ → List α → Prop
  | last {a b : ℝ} {x : α}
      (hl : left x ≤ a) (hr : b ≤ right x) :
      ClosedChain left right a b [x]
  | step {a b : ℝ} {x : α} {xs : List α}
      (hl : left x ≤ a) (tail : ClosedChain left right (right x) b xs) :
      ClosedChain left right a b (x :: xs)

/-- Every point of the closed target interval lies in a labelled interval. -/
theorem closed_chain_cover {left right : α → ℝ} {a b : ℝ} {xs : List α}
    (chain : ClosedChain left right a b xs) :
    ∀ t : ℝ, a ≤ t → t ≤ b → ∃ x ∈ xs, left x ≤ t ∧ t ≤ right x := by
  induction chain with
  | last hl hr =>
      intro t hat htb
      exact ⟨_, by simp, le_trans hl hat, le_trans htb hr⟩
  | @step a b x xs hl tail ih =>
      intro t hat htb
      by_cases htr : t ≤ right x
      · exact ⟨_, by simp, le_trans hl hat, htr⟩
      · obtain ⟨x, hx, hleft, hright⟩ := ih t (le_of_not_ge htr) htb
        exact ⟨x, List.mem_cons_of_mem _ hx, hleft, hright⟩

/-- Endpoint transport preserves the original shift, velocity and winding. -/
theorem source_interval_transport (v s δ t left right : ℝ) (k : ℤ)
    (hv : 0 < v)
    (hleft : ((k : ℝ) - s - δ) / v ≤ left)
    (hright : right ≤ ((k : ℝ) - s + δ) / v)
    (htleft : left ≤ t) (htright : t ≤ right) :
    |s + v * t - (k : ℝ)| ≤ δ := by
  have hlo : ((k : ℝ) - s - δ) / v ≤ t := le_trans hleft htleft
  have hhi : t ≤ ((k : ℝ) - s + δ) / v := le_trans htright hright
  have hlo' : (k : ℝ) - s - δ ≤ t * v := (div_le_iff₀ hv).mp hlo
  have hhi' : t * v ≤ (k : ℝ) - s + δ := (le_div_iff₀ hv).mp hhi
  apply abs_le.mpr
  constructor <;> nlinarith

/-- Full interval-chain semantics, quantified over all real times in [0,1]. -/
theorem closed_chain_runner_sound {n : ℕ} (v s : Fin n → ℝ) (δ : ℝ)
    (left right : (Fin n × ℤ) → ℝ) (arcs : List (Fin n × ℤ))
    (chain : ClosedChain left right 0 1 arcs)
    (source : ∀ x ∈ arcs, 0 < v x.1 ∧
      ((x.2 : ℝ) - s x.1 - δ) / v x.1 ≤ left x ∧
      right x ≤ ((x.2 : ℝ) - s x.1 + δ) / v x.1) :
    ∀ t : ℝ, 0 ≤ t → t ≤ 1 →
      ∃ i : Fin n, ∃ k : ℤ, |s i + v i * t - (k : ℝ)| ≤ δ := by
  intro t ht0 ht1
  obtain ⟨x, hx, hl, hr⟩ := closed_chain_cover chain t ht0 ht1
  obtain ⟨hv, hleft, hright⟩ := source x hx
  exact ⟨x.1, x.2,
    source_interval_transport (v x.1) (s x.1) δ t (left x) (right x)
      x.2 hv hleft hright hl hr⟩

/-- Integer speeds transport a witness by any integral time translation. -/
theorem integer_time_transport (v k m : ℤ) (s t δ : ℝ)
    (h : |s + (v : ℝ) * t - (k : ℝ)| ≤ δ) :
    |s + (v : ℝ) * (t + (m : ℝ)) - ((k + v*m : ℤ) : ℝ)| ≤ δ := by
  have identity : s + (v : ℝ) * (t + (m : ℝ)) - ((k + v*m : ℤ) : ℝ) =
      s + (v : ℝ) * t - (k : ℝ) := by
    push_cast
    ring
  rw [identity]
  exact h

end SUCC.LonelyRunnerCover
