/-!
# Nondeterministic source / public-belief policy descent

Pinned core Lean 4.14, no imports. A public policy branches only on retained
outcomes, not the hidden source state. Sure safety includes action availability
and every authorized nondeterministic successor. It is not almost-sure safety
or a probability law. The state type may include immutable source tags.
-/
namespace ObservationalSUCC.Round2.PublicBelief

universe u v w x

inductive Policy (A : Type v) (O : Type w) : Type (max v w)
  | stop : Policy A O
  | act : A → (O → Policy A O) → Policy A O

def Enabled {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) (s : S) (a : A) : Prop :=
  ∃ o t, edge s a o t

def Post {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) (belief : S → Prop) (a : A) (o : O) : S → Prop :=
  fun t => ∃ s, belief s ∧ edge s a o t

def SourceSafe {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) : Policy A O → S → Prop
  | .stop, _ => True
  | .act a next, s => Enabled edge s a ∧ ∀ o t, edge s a o t → SourceSafe edge (next o) t

def BeliefSafe {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) : Policy A O → (S → Prop) → Prop
  | .stop, _ => True
  | .act a next, belief =>
      (∀ s, belief s → Enabled edge s a) ∧
      ∀ o, BeliefSafe edge (next o) (Post edge belief a o)

/-- A single common PUBLIC policy is safe precisely when it is source-safe
from every compatible private state. The policy quantifier stays OUTSIDE
the state quantifier; no state-dependent controller is smuggled in. -/
theorem belief_safe_iff_all_sources
    {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) :
    ∀ policy belief, BeliefSafe edge policy belief ↔
      ∀ s, belief s → SourceSafe edge policy s := by
  intro policy
  induction policy with
  | stop =>
      intro belief
      constructor
      · intro _ _ _; exact True.intro
      · intro _; exact True.intro
  | act a next ih =>
      intro belief
      constructor
      · rintro ⟨enabled, tails⟩ s hs
        refine ⟨enabled s hs, ?_⟩
        intro o t edge_st
        exact (ih o (Post edge belief a o)).mp (tails o) t ⟨s, hs, edge_st⟩
      · intro all
        refine ⟨fun s hs => (all s hs).1, ?_⟩
        intro o
        apply (ih o (Post edge belief a o)).mpr
        rintro t ⟨s, hs, edge_st⟩
        exact (all s hs).2 o t edge_st

def Horizon {A : Type v} {O : Type w} : Nat → Policy A O → Prop
  | 0, .stop => True
  | 0, .act _ _ => False
  | _ + 1, .stop => False
  | n + 1, .act _ next => ∀ o, Horizon n (next o)

/-- Exact finite-horizon controller existence, with no premature stopping
and the same observation-based controller for all source possibilities. -/
theorem uniform_controller_iff
    {S : Type u} {A : Type v} {O : Type w}
    (edge : S → A → O → S → Prop) (belief : S → Prop) (n : Nat) :
    (∃ policy, Horizon n policy ∧ BeliefSafe edge policy belief) ↔
    (∃ policy, Horizon n policy ∧ ∀ s, belief s → SourceSafe edge policy s) := by
  constructor
  · rintro ⟨policy, depth, safe⟩
    exact ⟨policy, depth, (belief_safe_iff_all_sources edge policy belief).mp safe⟩
  · rintro ⟨policy, depth, safe⟩
    exact ⟨policy, depth, (belief_safe_iff_all_sources edge policy belief).mpr safe⟩

def Image {S : Type u} {Q : Type x} (q : S → Q) (belief : S → Prop) : Q → Prop :=
  fun y => ∃ s, belief s ∧ q s = y

/-- Every quotient successor must lift from the PARTICULAR representative s.
The converse prevents the quotient from omitting actual source branches. -/
def ExactQuotient {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop)
    (down : Q → A → O → Q → Prop) : Prop :=
  ∀ s a o y, down (q s) a o y ↔ ∃ t, edge s a o t ∧ q t = y

def FiberUniform {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop) : Prop :=
  ∀ s t, q s = q t → ∀ a o y,
    (∃ z, edge s a o z ∧ q z = y) ↔ (∃ z, edge t a o z ∧ q z = y)

/-- Necessary and sufficient for a quotient that retains all branches and
lifts every quotient edge from every fixed original representative. No
choice or finite-carrier assumption is needed for the relational quotient. -/
theorem exact_quotient_exists_iff
    {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop) :
    (∃ down, ExactQuotient q edge down) ↔ FiberUniform q edge := by
  constructor
  · rintro ⟨down, square⟩ s t eq a o y
    exact Iff.trans (square s a o y).symm (by rw [eq]; exact square t a o y)
  · intro uniform
    let down : Q → A → O → Q → Prop :=
      fun x a o y => ∃ s, q s = x ∧ ∃ t, edge s a o t ∧ q t = y
    refine ⟨down, ?_⟩
    intro s a o y
    constructor
    · rintro ⟨t, ht, h⟩
      exact (uniform t s ht a o y).mp h
    · intro h
      exact ⟨s, rfl, h⟩

theorem quotient_enabled_iff
    {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop)
    (down : Q → A → O → Q → Prop) (exactQ : ExactQuotient q edge down)
    (s : S) (a : A) : Enabled edge s a ↔ Enabled down (q s) a := by
  constructor
  · rintro ⟨o, t, h⟩
    exact ⟨o, q t, (exactQ s a o (q t)).mpr ⟨t, h, rfl⟩⟩
  · rintro ⟨o, y, h⟩
    obtain ⟨t, ht, _⟩ := (exactQ s a o y).mp h
    exact ⟨o, t, ht⟩

/-- Exact source quotienting commutes with full public belief update. -/
theorem image_post_iff
    {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop)
    (down : Q → A → O → Q → Prop) (exactQ : ExactQuotient q edge down)
    (belief : S → Prop) (a : A) (o : O) (y : Q) :
    Image q (Post edge belief a o) y ↔ Post down (Image q belief) a o y := by
  constructor
  · rintro ⟨t, ⟨s, hs, hst⟩, ht⟩
    exact ⟨q s, ⟨s, hs, rfl⟩, (exactQ s a o y).mpr ⟨t, hst, ht⟩⟩
  · rintro ⟨x, ⟨s, hs, hq⟩, hxy⟩
    rw [← hq] at hxy
    obtain ⟨t, hst, ht⟩ := (exactQ s a o y).mp hxy
    exact ⟨t, ⟨s, hs, hst⟩, ht⟩

/-- Every public policy, including its universal nondeterministic obligations,
is preserved and reflected by a representative-wise exact quotient. -/
theorem source_policy_descent_iff
    {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop)
    (down : Q → A → O → Q → Prop) (exactQ : ExactQuotient q edge down) :
    ∀ policy s, SourceSafe edge policy s ↔ SourceSafe down policy (q s) := by
  intro policy
  induction policy with
  | stop => intro s; exact Iff.rfl
  | act a next ih =>
      intro s
      constructor
      · rintro ⟨enabled, tails⟩
        refine ⟨(quotient_enabled_iff q edge down exactQ s a).mp enabled, ?_⟩
        intro o y h
        obtain ⟨t, hst, ht⟩ := (exactQ s a o y).mp h
        rw [← ht]
        exact (ih o t).mp (tails o t hst)
      · rintro ⟨enabled, tails⟩
        refine ⟨(quotient_enabled_iff q edge down exactQ s a).mpr enabled, ?_⟩
        intro o t hst
        exact (ih o t).mpr (tails o (q t) ((exactQ s a o (q t)).mpr ⟨t, hst, rfl⟩))

theorem belief_policy_descent_iff
    {S : Type u} {Q : Type x} {A : Type v} {O : Type w}
    (q : S → Q) (edge : S → A → O → S → Prop)
    (down : Q → A → O → Q → Prop) (exactQ : ExactQuotient q edge down)
    (policy : Policy A O) (belief : S → Prop) :
    BeliefSafe edge policy belief ↔ BeliefSafe down policy (Image q belief) := by
  rw [belief_safe_iff_all_sources, belief_safe_iff_all_sources]
  constructor
  · intro all y hy
    obtain ⟨s, hs, hq⟩ := hy
    rw [← hq]
    exact (source_policy_descent_iff q edge down exactQ policy s).mp (all s hs)
  · intro all s hs
    exact (source_policy_descent_iff q edge down exactQ policy s).mpr
      (all (q s) ⟨s, hs, rfl⟩)

/-- Counterexample to exchanging the public-controller and private-state
quantifiers. Each hidden bit permits its own action; no action fits both. -/
theorem private_choices_do_not_glue :
    (∀ s : Bool, ∃ a : Bool, s = a) ∧
    ¬ (∃ a : Bool, ∀ s : Bool, s = a) := by
  constructor
  · intro s; exact ⟨s, rfl⟩
  · rintro ⟨a, all⟩
    have bad : false = true := Eq.trans (all false) (all true).symm
    cases bad

/-- In the explicit guard family, guard j is enabled exactly away from
private state j. Its public safety reveals non-membership in the belief. -/
theorem guard_safe_iff_absent {S : Type u} (belief : S → Prop) (j : S) :
    (∀ s, belief s → s ≠ j) ↔ ¬ belief j := by
  constructor
  · intro safe present; exact safe j present rfl
  · intro absent s present eq
    exact absent (eq ▸ present)

/-- Different beliefs cannot be merged by an exact safe-menu interface when
the guard grammar separates their membership. Counting gives the finite
exponential lower bound in the paper; that cardinality step is not formalized. -/
theorem differing_beliefs_have_separating_guard
    {S : Type u} (left right : S → Prop) (j : S)
    (present : left j) (absent : ¬ right j) :
    (∀ s, right s → s ≠ j) ∧ ¬ (∀ s, left s → s ≠ j) := by
  constructor
  · exact (guard_safe_iff_absent right j).mpr absent
  · intro safe; exact (guard_safe_iff_absent left j).mp safe present

end ObservationalSUCC.Round2.PublicBelief

#print axioms ObservationalSUCC.Round2.PublicBelief.belief_safe_iff_all_sources
#print axioms ObservationalSUCC.Round2.PublicBelief.uniform_controller_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.exact_quotient_exists_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.quotient_enabled_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.image_post_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.source_policy_descent_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.belief_policy_descent_iff
#print axioms ObservationalSUCC.Round2.PublicBelief.private_choices_do_not_glue
#print axioms ObservationalSUCC.Round2.PublicBelief.guard_safe_iff_absent
#print axioms ObservationalSUCC.Round2.PublicBelief.differing_beliefs_have_separating_guard
