/-!
# Source-typed finite-action word closure (Lean 4.14, no mathlib)

"Indistinguishable within the tools" is a relative statement.
Given an equivalence (or even a binary relation) that agrees on present
observation and is preserved by EVERY available action, no finite
sequence drawn from those actions separates two related states.

No theorem that an externally available new physical sensor exists;
no claim that the sources have the same ontology; no physical infinity.
-/

namespace ObservationalSUCC

universe u v w

def RunWord {S : Type u} {Action : Type v}
    (step : Action → S → S) : List Action → S → S
  | [], s => s
  | a :: rest, s => RunWord step rest (step a s)

/-- Any congruent pair retains identical outputs under each available
finite experiment word, even if the hidden source states differ. -/
theorem no_available_finite_word_separates
    {S : Type u} {Action : Type v} {Report : Type w}
    (q : S → Report) (step : Action → S → S) (equiv : S → S → Prop)
    (output_respects : ∀ s t, equiv s t → q s = q t)
    (actions_respect : ∀ a s t, equiv s t →
      equiv (step a s) (step a t))
    (s t : S) (h : equiv s t) :
    ∀ word : List Action,
      q (RunWord step word s) = q (RunWord step word t) := by
  intro word
  induction word generalizing s t with
  | nil =>
      exact output_respects s t h
  | cons a rest ih =>
      change q (RunWord step rest (step a s)) =
        q (RunWord step rest (step a t))
      exact ih (step a s) (step a t) (actions_respect a s t h)

/-- Observable noncommutation is decisive evidence of source-level
noncommutation, but the converse is false when q erases the mismatch. -/
theorem visible_commutator_implies_source_commutator
    {S : Type u} {Report : Type v}
    (q : S → Report) (U V : S → S) (s : S)
    (observed : q (U (V s)) ≠ q (V (U s))) :
    U (V s) ≠ V (U s) := by
  intro same
  exact observed (congrArg q same)

/-- A source change cannot hide an observable commutator behind a mere
syntactic renaming if an actually injective reporter is available. -/
theorem injective_report_detects_source_inequality
    {S : Type u} {Report : Type v}
    (q : S → Report) (injective : ∀ x y, q x = q y → x = y)
    (x y : S) (different : x ≠ y) :
    q x ≠ q y := by
  intro reports_equal
  exact different (injective x y reports_equal)

end ObservationalSUCC
