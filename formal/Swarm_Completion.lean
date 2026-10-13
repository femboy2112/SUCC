import Std.Tactic
/-!
SWM-B09/B13/B16: finite-restriction threads, finite proof support, and
marker-exclusion source-state debt. Pinned Lean 4.14, core + Std only.
This does NOT formalize the product topology, its closure/homeomorphism,
Tychonoff compactness, or Gödel's incompleteness theorems.
-/
namespace ObservationalSUCC.SwarmCompletion
universe u v w

def CoherentRows {O : Type u} (rows : Nat → Nat → O) : Prop :=
  ∀ h k n, n < h → n < k → rows h n = rows k n

def ThreadProfile {O : Type u} (rows : Nat → Nat → O) (n : Nat) : O :=
  rows (n+1) n

theorem coherent_rows_are_profile_restrictions
    {O : Type u} (rows : Nat → Nat → O) (coherent : CoherentRows rows) :
    ∀ h n, n < h → rows h n = ThreadProfile rows n := by
  intro h n hn
  exact coherent h (n+1) n hn (Nat.lt_succ_self n)

theorem thread_profile_unique
    {O : Type u} (rows : Nat → Nat → O) (profile : Nat → O)
    (agrees : ∀ h n, n < h → rows h n = profile n) :
    ∀ n, ThreadProfile rows n = profile n := by
  intro n
  exact agrees (n+1) n (Nat.lt_succ_self n)

/-- A coherent thread of source-admissible finite prefixes determines
exactly one globally defined finite-compatible profile. No ONE source
state realizing all coordinates is asserted. -/
theorem admissible_thread_iff_finite_profile_compatibility
    {S : Type u} {O : Type v} (trace : S → Nat → O)
    (rows : Nat → Nat → O) (coherent : CoherentRows rows) :
    (∀ h, ∃ s : S, ∀ n, n < h → trace s n = rows h n) ↔
    (∀ h, ∃ s : S, ∀ n, n < h → trace s n = ThreadProfile rows n) := by
  constructor
  · intro admissible h
    obtain ⟨s, agrees⟩ := admissible h
    refine ⟨s, ?_⟩
    intro n hn
    exact (agrees n hn).trans
      (coherent_rows_are_profile_restrictions rows coherent h n hn)
  · intro compatible h
    obtain ⟨s, agrees⟩ := compatible h
    refine ⟨s, ?_⟩
    intro n hn
    exact (agrees n hn).trans
      (coherent_rows_are_profile_restrictions rows coherent h n hn).symm

/-- Every finite support in an increasing union occurs together at a
finite stage. This is a finitary proof-support theorem, not reflection. -/
theorem finite_support_has_common_stage
    {P : Type u} (stage : Nat → P → Prop)
    (monotone : ∀ i j, i ≤ j → ∀ p, stage i p → stage j p)
    (support : List P)
    (present : ∀ p, p ∈ support → ∃ n, stage n p) :
    ∃ N, ∀ p, p ∈ support → stage N p := by
  induction support with
  | nil =>
      refine ⟨0, ?_⟩
      intro p hp
      cases hp
  | cons a rest ih =>
      obtain ⟨i, atI⟩ := present a (by simp)
      have tailPresent : ∀ p, p ∈ rest → ∃ n, stage n p := by
        intro p hp
        exact present p (by simp [hp])
      obtain ⟨j, atJ⟩ := ih tailPresent
      refine ⟨max i j, ?_⟩
      intro p hp
      have split : p = a ∨ p ∈ rest := by simpa using hp
      cases split with
      | inl eq =>
          subst p
          exact monotone i (max i j) (Nat.le_max_left i j) a atI
      | inr mem =>
          exact monotone j (max i j) (Nat.le_max_right i j) p (atJ p mem)

def Iterate {S : Type u} (step : S → S) : Nat → S → S
  | 0, s => s
  | n+1, s => step (Iterate step n s)

theorem iterate_add {S : Type u} (step : S → S) (s : S) (n k : Nat) :
    Iterate step (n+k) s = Iterate step k (Iterate step n s) := by
  induction k with
  | zero => simp [Iterate]
  | succ k ih =>
      rw [Nat.add_succ]
      change step (Iterate step (n+k) s) = step (Iterate step k (Iterate step n s))
      exact congrArg step ih

/-- Arbitrary alphabets and nonconstant interior reports are permitted.
Only the terminal marker must be absent throughout the preceding gap. -/
theorem marker_exclusion_gap_forces_distinct_source_states
    {S : Type u} {O : Type v} (step : S → S) (report : S → O)
    (s : S) (start stop i j : Nat)
    (order : start ≤ i ∧ i < j ∧ j ≤ stop)
    (excluded : ∀ t, start ≤ t → t < stop →
      report (Iterate step t s) ≠ report (Iterate step stop s)) :
    Iterate step i s ≠ Iterate step j s := by
  intro same
  have equalFuture : Iterate step (i+(stop-j)) s =
      Iterate step (j+(stop-j)) s := by
    rw [iterate_add step s i (stop-j), iterate_add step s j (stop-j), same]
  have earlier : start ≤ i+(stop-j) ∧ i+(stop-j) < stop := by omega
  have reaches : j+(stop-j) = stop := by omega
  rw [reaches] at equalFuture
  exact excluded (i+(stop-j)) earlier.1 earlier.2 (congrArg report equalFuture)

end ObservationalSUCC.SwarmCompletion
