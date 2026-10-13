import Std.Tactic
/-!
# CAMBRIAN C: time-varying nondeterministic history realization

Lean 4.14, core + Std only.  No topology library is imported.
This is the finitely branching (Koenig) specialization of the dossier's
compact closed-graph realization theorem, not its full topological proof.

State types may change with time.  The transition relation need not be
deterministic, stationary, total, or invertible.  Each source state has a
COMPLETE finite list of possible successors.  An arbitrarily extendable
state then has one genuine infinite compatible history.  The selected
branch is classical and need not be computable from finite data.
-/
namespace ObservationalSUCC

universe u

def CambrianCanFollow {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop) :
    (t : Nat) → Nat → S t → Prop
  | _, 0, _ => True
  | t, d+1, s => ∃ next : S (t+1),
      R t s next ∧ CambrianCanFollow R (t+1) d next

theorem cambrian_can_follow_truncate
    {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop) :
    ∀ d t (s : S t) e, e ≤ d →
      CambrianCanFollow R t d s → CambrianCanFollow R t e s := by
  intro d
  induction d with
  | zero =>
      intro t s e he _
      have : e = 0 := by omega
      subst e
      trivial
  | succ d ih =>
      intro t s e he path
      cases e with
      | zero => trivial
      | succ e =>
          obtain ⟨next, edge, tail⟩ := path
          exact ⟨next, edge, ih (t+1) next e (by omega) tail⟩

/-- A finite menu cannot offer arbitrarily deep coherent witnesses unless
one menu member itself survives every depth.  Completeness of the menu
and downward closure are explicit hypotheses. -/
theorem cambrian_finite_coherent_choice
    {X : Type u} (menu : List X) (P : Nat → X → Prop)
    (down : ∀ e d x, e ≤ d → P d x → P e x)
    (every : ∀ d, ∃ x, x ∈ menu ∧ P d x) :
    ∃ x, x ∈ menu ∧ ∀ d, P d x := by
  classical
  induction menu with
  | nil =>
      obtain ⟨x, mem, _⟩ := every 0
      simp at mem
  | cons a rest ih =>
      by_cases all : ∀ d, P d a
      · exact ⟨a, by simp, all⟩
      · have bad : ∃ d, ¬ P d a := by
          by_cases witnessed : ∃ d, ¬ P d a
          · exact witnessed
          · apply False.elim
            apply all
            intro d
            by_cases hd : P d a
            · exact hd
            · exact False.elim (witnessed ⟨d, hd⟩)
        obtain ⟨k, hk⟩ := bad
        have remaining : ∀ d, ∃ x, x ∈ rest ∧ P d x := by
          intro d
          obtain ⟨x, mem, hx⟩ := every (max d k)
          have neq : x ≠ a := by
            intro equal
            subst x
            exact hk (down k (max d k) a (Nat.le_max_right d k) hx)
          have tailmem : x ∈ rest := by
            rcases List.mem_cons.mp mem with equal | tail
            · exact False.elim (neq equal)
            · exact tail
          exact ⟨x, tailmem,
            down d (max d k) x (Nat.le_max_left d k) hx⟩
        obtain ⟨x, mem, hx⟩ := ih remaining
        exact ⟨x, by simp [mem], hx⟩

def CambrianExtendable {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop)
    (t : Nat) (s : S t) : Prop :=
  ∀ d, CambrianCanFollow R t d s

theorem cambrian_extendable_successor
    {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop)
    (menu : (t : Nat) → S t → List (S (t+1)))
    (complete : ∀ t s next, R t s next → next ∈ menu t s)
    (t : Nat) (s : S t) (deep : CambrianExtendable R t s) :
    ∃ next, R t s next ∧ CambrianExtendable R (t+1) next := by
  let P : Nat → S (t+1) → Prop := fun d next =>
    R t s next ∧ CambrianCanFollow R (t+1) d next
  have every : ∀ d, ∃ next, next ∈ menu t s ∧ P d next := by
    intro d
    obtain ⟨next, edge, path⟩ := deep (d+1)
    exact ⟨next, complete t s next edge, edge, path⟩
  have down : ∀ e d next, e ≤ d → P d next → P e next := by
    intro e d next order hp
    exact ⟨hp.1, cambrian_can_follow_truncate
      R d (t+1) next e order hp.2⟩
  obtain ⟨next, _, all⟩ :=
    cambrian_finite_coherent_choice (menu t s) P down every
  exact ⟨next, (all 0).1, fun d => (all d).2⟩

/-- Finitely branching realization for changing source types and arbitrary
time-dependent nondeterministic transition relations. -/
theorem cambrian_nondeterministic_history_realization
    {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop)
    (menu : (t : Nat) → S t → List (S (t+1)))
    (complete : ∀ t s next, R t s next → next ∈ menu t s)
    (start : S 0) (deep : CambrianExtendable R 0 start) :
    ∃ history : (t : Nat) → S t,
      history 0 = start ∧ ∀ t, R t (history t) (history (t+1)) := by
  classical
  let E : Nat → Type u := fun t => {s : S t // CambrianExtendable R t s}
  let next : (t : Nat) → E t → E (t+1) := fun t state =>
    let witness := cambrian_extendable_successor
      R menu complete t state.val state.property
    ⟨Classical.choose witness, (Classical.choose_spec witness).2⟩
  let branch : (t : Nat) → E t :=
    fun t => Nat.rec (motive := fun t => E t)
      ⟨start, deep⟩ (fun t state => next t state) t
  refine ⟨fun t => (branch t).val, rfl, ?_⟩
  intro t
  change R t (branch t).val (next t (branch t)).val
  exact (Classical.choose_spec
    (cambrian_extendable_successor R menu complete
      t (branch t).val (branch t).property)).1

/-- A COMPLETE finite list of initial source states may supply different
states at each finite horizon.  Finite branching still forces one initial
state and one infinite source history; a uniform finite state bound is
not assumed. -/
theorem cambrian_finite_prefixes_realize_one_history
    {S : Nat → Type u}
    (R : (t : Nat) → S t → S (t+1) → Prop)
    (menu : (t : Nat) → S t → List (S (t+1)))
    (complete : ∀ t s next, R t s next → next ∈ menu t s)
    (initial : List (S 0))
    (prefixes : ∀ d, ∃ s, s ∈ initial ∧ CambrianCanFollow R 0 d s) :
    ∃ history : (t : Nat) → S t,
      history 0 ∈ initial ∧ ∀ t, R t (history t) (history (t+1)) := by
  obtain ⟨s, mem, deep⟩ := cambrian_finite_coherent_choice
    initial (fun d s => CambrianCanFollow R 0 d s)
    (fun e d s le path => cambrian_can_follow_truncate R d 0 s e le path)
    prefixes
  obtain ⟨history, start, lawful⟩ :=
    cambrian_nondeterministic_history_realization R menu complete s deep
  exact ⟨history, by rw [start]; exact mem, lawful⟩

def CambrianCountdown (_ : Nat) (x y : Nat) : Prop := x = y+1

/-- Sharp failure without a finite initial source menu: a natural
countdown admits depth d exactly when its original state is at least d. -/
theorem cambrian_countdown_depth_iff :
    ∀ d t s, CambrianCanFollow CambrianCountdown t d s ↔ d ≤ s := by
  intro d
  induction d with
  | zero =>
      intro t s
      constructor
      · intro _; exact Nat.zero_le s
      · intro _; trivial
  | succ d ih =>
      intro t s
      constructor
      · rintro ⟨next, edge, tail⟩
        have smaller := (ih (t+1) next).mp tail
        change s = next+1 at edge
        omega
      · intro le
        refine ⟨s-1, ?_, ?_⟩
        · change s = (s-1)+1
          omega
        · apply (ih (t+1) (s-1)).mpr
          omega

theorem cambrian_countdown_all_finite_depths :
    ∀ d, ∃ s, CambrianCanFollow CambrianCountdown 0 d s := by
  intro d
  exact ⟨d, (cambrian_countdown_depth_iff d 0 d).mpr (Nat.le_refl d)⟩

theorem cambrian_countdown_no_infinite_history :
    ¬ ∃ history : Nat → Nat,
      ∀ t, CambrianCountdown t (history t) (history (t+1)) := by
  rintro ⟨history, edges⟩
  have budget : ∀ n, history n + n = history 0 := by
    intro n
    induction n with
    | zero => simp
    | succ n ih =>
        have edge := edges n
        change history n = history (n+1)+1 at edge
        omega
  have exhausted := budget (history 0+1)
  omega

end ObservationalSUCC

#print axioms ObservationalSUCC.cambrian_finite_prefixes_realize_one_history
#print axioms ObservationalSUCC.cambrian_countdown_no_infinite_history
