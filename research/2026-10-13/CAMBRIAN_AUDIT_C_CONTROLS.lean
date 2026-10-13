/- Audit appendix. The runner prepends the exact new Cambrian module,
   so this file needs no import of a separately built local olean. -/
namespace CambrianAudit
open ObservationalSUCC

def GrowingState (t : Nat) : Type := Nat × Fin (t+1)
def GrowingZero (t : Nat) : Fin (t+1) := ⟨0, by omega⟩
def GrowingRelation (t : Nat) (s : GrowingState t)
    (next : GrowingState (t+1)) : Prop :=
  next.2.val = 0 ∧
    (next.1 = s.1+t+1 ∨ next.1 = s.1+t+2)
def GrowingMenu (t : Nat) (s : GrowingState t) :
    List (GrowingState (t+1)) :=
  [(s.1+t+1, GrowingZero (t+1)),
   (s.1+t+2, GrowingZero (t+1)),
   (s.1, GrowingZero (t+1))]

theorem growing_menu_complete :
    ∀ t s next, GrowingRelation t s next → next ∈ GrowingMenu t s := by
  intro t s next edge
  rcases edge with ⟨tag, first | second⟩
  · have equal : next = (s.1+t+1, GrowingZero (t+1)) := by
      apply Prod.ext
      · exact first
      · apply Fin.ext
        exact tag
    rw [equal]
    simp [GrowingMenu]
  · have equal : next = (s.1+t+2, GrowingZero (t+1)) := by
      apply Prod.ext
      · exact second
      · apply Fin.ext
        exact tag
    rw [equal]
    simp [GrowingMenu]

theorem growing_menu_contains_non_successor (t : Nat) (s : GrowingState t) :
    (s.1, GrowingZero (t+1)) ∈ GrowingMenu t s ∧
      ¬ GrowingRelation t s (s.1, GrowingZero (t+1)) := by
  constructor
  · simp [GrowingMenu]
  · intro edge
    rcases edge.2 with first | second <;> omega

theorem growing_relation_is_nondeterministic (t : Nat) (s : GrowingState t) :
    ∃ next other : GrowingState (t+1),
      GrowingRelation t s next ∧ GrowingRelation t s other ∧ next ≠ other := by
  refine ⟨(s.1+t+1, GrowingZero (t+1)),
    (s.1+t+2, GrowingZero (t+1)),
    ⟨rfl, Or.inl rfl⟩, ⟨rfl, Or.inr rfl⟩, ?_⟩
  intro equal
  have values := congrArg Prod.fst equal
  omega

theorem growing_can_follow : ∀ d t (s : GrowingState t),
    CambrianCanFollow GrowingRelation t d s := by
  intro d
  induction d with
  | zero => intro t s; trivial
  | succ d ih =>
      intro t s
      exact ⟨(s.1+t+1, GrowingZero (t+1)),
        ⟨rfl, Or.inl rfl⟩, ih (t+1) _⟩

theorem growing_infinite_state_history :
    ∃ history : (t : Nat) → GrowingState t,
      history 0 = (0, GrowingZero 0) ∧
        ∀ t, GrowingRelation t (history t) (history (t+1)) := by
  exact cambrian_nondeterministic_history_realization
    GrowingRelation GrowingMenu growing_menu_complete
    (0, GrowingZero 0) (fun d => growing_can_follow d 0 _)

/- A single fixed root has infinitely many successors. Every finite
   depth exists, yet no infinite branch does. -/
def InfiniteRootRelation (t x y : Nat) : Prop := t = 0 ∨ x = y+1

theorem countdown_embeds_after_root :
    ∀ d t s, 0 < t →
      CambrianCanFollow CambrianCountdown t d s →
      CambrianCanFollow InfiniteRootRelation t d s := by
  intro d
  induction d with
  | zero => intro t s _ _; trivial
  | succ d ih =>
      intro t s positive path
      obtain ⟨next, edge, tail⟩ := path
      exact ⟨next, Or.inr edge, ih (t+1) next (by omega) tail⟩

theorem infinite_root_arbitrarily_extendable :
    CambrianExtendable InfiniteRootRelation 0 0 := by
  intro depth
  cases depth with
  | zero => trivial
  | succ d =>
      exact ⟨d, Or.inl rfl,
        countdown_embeds_after_root d 1 d (by omega)
          ((cambrian_countdown_depth_iff d 1 d).mpr (Nat.le_refl d))⟩

theorem infinite_root_no_infinite_history :
    ¬ ∃ history : Nat → Nat,
      ∀ t, InfiniteRootRelation t (history t) (history (t+1)) := by
  rintro ⟨history, edges⟩
  apply cambrian_countdown_no_infinite_history
  refine ⟨fun n => history (n+1), ?_⟩
  intro n
  rcases edges (n+1) with zero | edge
  · omega
  · exact edge

def ListMaximum (xs : List Nat) : Nat := xs.foldr Nat.max 0

theorem listed_below_maximum (xs : List Nat) :
    ∀ x, x ∈ xs → x ≤ ListMaximum xs := by
  induction xs with
  | nil => intro x mem; simp at mem
  | cons a rest ih =>
      intro x mem
      rcases List.mem_cons.mp mem with equal | tail
      · subst x
        exact Nat.le_max_left a (ListMaximum rest)
      · exact Nat.le_trans (ih x tail) (Nat.le_max_right a (ListMaximum rest))

theorem infinite_root_has_no_finite_complete_menu (xs : List Nat) :
    ¬ ∀ next, InfiniteRootRelation 0 0 next → next ∈ xs := by
  intro complete
  have mem := complete (ListMaximum xs+1) (Or.inl rfl)
  have bound := listed_below_maximum xs (ListMaximum xs+1) mem
  omega

def Alternating (d : Nat) (x : Bool) : Prop :=
  if d = 0 then x = true else x = false

theorem alternating_every_depth_has_a_finite_menu_witness :
    ∀ d, ∃ x : Bool, x ∈ [true, false] ∧ Alternating d x := by
  intro d
  cases d with
  | zero => exact ⟨true, by simp, by simp [Alternating]⟩
  | succ n => exact ⟨false, by simp, by simp [Alternating]⟩

theorem alternating_no_uniform_witness :
    ¬ ∃ x : Bool, ∀ d, Alternating d x := by
  rintro ⟨x, all⟩
  have first := all 0
  have second := all 1
  simp [Alternating] at first second
  rw [first] at second
  cases second

theorem alternating_lacks_downward_closure :
    ¬ ∀ e d x, e ≤ d → Alternating d x → Alternating e x := by
  intro down
  have impossible := down 0 1 false (by decide) (by simp [Alternating])
  simp [Alternating] at impossible

end CambrianAudit

#print axioms CambrianAudit.growing_menu_complete
#print axioms CambrianAudit.growing_menu_contains_non_successor
#print axioms CambrianAudit.growing_relation_is_nondeterministic
#print axioms CambrianAudit.growing_infinite_state_history
#print axioms CambrianAudit.infinite_root_arbitrarily_extendable
#print axioms CambrianAudit.infinite_root_no_infinite_history
#print axioms CambrianAudit.infinite_root_has_no_finite_complete_menu
#print axioms CambrianAudit.alternating_every_depth_has_a_finite_menu_witness
#print axioms CambrianAudit.alternating_no_uniform_witness
#print axioms CambrianAudit.alternating_lacks_downward_closure
