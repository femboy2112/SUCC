/-!
# Partial labelled source quotient and exact causal descent

Core Lean 4.14; no external dependencies. A label can retain an outcome,
exact cost and occurrence token. Partiality is retained as `none`.
No physical source authentication, probability coupling, infinite execution,
or preservation of discarded private-state identity is asserted.
-/

namespace ObservationalSUCC.InstituteCausal

universe u v w x

def project {S : Type u} {Q : Type v} {L : Type w}
    (q : S → Q) : Option (L × S) → Option (L × Q)
  | none => none
  | some (l, s) => some (l, q s)

def run {S : Type u} {A : Type v} {L : Type w}
    (step : S → A → Option (L × S)) : List A → S → Option (List L × S)
  | [], s => some ([], s)
  | a :: rest, s =>
      match step s a with
      | none => none
      | some (l, t) =>
          match run step rest t with
          | none => none
          | some (ls, z) => some (l :: ls, z)

def FiberCongruent {S : Type u} {Q : Type v} {A : Type w} {L : Type x}
    (q : S → Q) (step : S → A → Option (L × S)) : Prop :=
  ∀ s t, q s = q t → ∀ a, project q (step s a) = project q (step t a)

/-- Local congruence preserves enabledness, every retained label, and the
next quotient state. Surjectivity forbids inventing unsourced quotient points. -/
theorem quotient_exists_iff_fiber_congruent
    {S : Type u} {Q : Type v} {A : Type w} {L : Type x}
    (q : S → Q) (step : S → A → Option (L × S))
    (surj : ∀ y, ∃ s, q s = y) :
    (∃ down : Q → A → Option (L × Q),
      ∀ s a, down (q s) a = project q (step s a)) ↔
      FiberCongruent q step := by
  constructor
  · rintro ⟨down, square⟩ s t eq a
    rw [← square s a, ← square t a, eq]
  · intro congruent
    classical
    let pick : Q → S := fun y => Classical.choose (surj y)
    have picked (y : Q) : q (pick y) = y := Classical.choose_spec (surj y)
    refine ⟨fun y a => project q (step (pick y) a), ?_⟩
    intro s a
    exact congruent (pick (q s)) s (picked (q s)) a

/-- All finite action words preserve the complete label word and terminal
quotient point; a failed action remains failure. -/
theorem run_naturality
    {S : Type u} {Q : Type v} {A : Type w} {L : Type x}
    (q : S → Q) (step : S → A → Option (L × S))
    (down : Q → A → Option (L × Q))
    (square : ∀ s a, down (q s) a = project q (step s a)) :
    ∀ word s, run down word (q s) = project q (run step word s) := by
  intro word
  induction word with
  | nil => intro s; rfl
  | cons a rest ih =>
      intro s
      simp only [run, square]
      cases hs : step s a with
      | none => rfl
      | some pair =>
          obtain ⟨l, t⟩ := pair
          simp only [project, ih]
          cases hr : run step rest t with
          | none => rfl
          | some pair => cases pair; rfl

/-- An accepted quotient word lifts from EVERY chosen source representative,
not merely from a fresh representative selected separately at each step. -/
theorem every_representative_lifts
    {S : Type u} {Q : Type v} {A : Type w} {L : Type x}
    (q : S → Q) (step : S → A → Option (L × S))
    (down : Q → A → Option (L × Q))
    (square : ∀ s a, down (q s) a = project q (step s a))
    (word : List A) (s : S) (labels : List L) (y : Q)
    (accepted : run down word (q s) = some (labels, y)) :
    ∃ t, run step word s = some (labels, t) ∧ q t = y := by
  rw [run_naturality q step down square] at accepted
  cases hr : run step word s with
  | none => simp [hr, project] at accepted
  | some pair =>
      obtain ⟨ls, t⟩ := pair
      have eq : (ls, q t) = (labels, y) := by
        exact Option.some.inj (by simpa only [hr, project] using accepted)
      have hl : ls = labels := congrArg Prod.fst eq
      have hq : q t = y := congrArg Prod.snd eq
      refine ⟨t, ?_, hq⟩
      rw [hl]

/-- The complete quotient criterion: local kernel compatibility is necessary
and sufficient for a commuting quotient and universal finite-history lifting. -/
theorem lawful_quotient_iff
    {S : Type u} {Q : Type v} {A : Type w} {L : Type x}
    (q : S → Q) (step : S → A → Option (L × S))
    (surj : ∀ y, ∃ s, q s = y) :
    FiberCongruent q step ↔
    ∃ down : Q → A → Option (L × Q),
      (∀ s a, down (q s) a = project q (step s a)) ∧
      (∀ word s, run down word (q s) = project q (run step word s)) ∧
      (∀ word s labels y, run down word (q s) = some (labels, y) →
        ∃ t, run step word s = some (labels, t) ∧ q t = y) := by
  constructor
  · intro compatible
    obtain ⟨down, square⟩ :=
      (quotient_exists_iff_fiber_congruent q step surj).mpr compatible
    exact ⟨down, square, run_naturality q step down square,
      every_representative_lifts q step down square⟩
  · rintro ⟨down, square, _, _⟩
    exact (quotient_exists_iff_fiber_congruent q step surj).mp ⟨down, square⟩

inductive Path {S : Type u} {L : Type v} (edge : S → L → S → Prop) :
    S → List L → S → Prop
  | nil (s) : Path edge s [] s
  | cons {s t z l ls} : edge s l t → Path edge t ls z → Path edge s (l :: ls) z

/-- Source identity is retained by the actual path when every authorized
edge preserves it; equality of public reports is not a replacement for this. -/
theorem path_preserves_source
    {S : Type u} {L : Type v} {Origin : Type w}
    (edge : S → L → S → Prop) (origin : S → Origin)
    (faithful : ∀ s l t, edge s l t → origin s = origin t)
    {s t : S} {word : List L} (path : Path edge s word t) :
    origin s = origin t := by
  induction path with
  | nil => rfl
  | cons hst tail ih => exact Eq.trans (faithful _ _ _ hst) ih

/-- Forward belief propagation uses the complete current source support. -/
def reachable {S : Type u} {L : Type v} (edge : S → L → S → Prop) :
    List L → (S → Prop) → S → Prop
  | [], initial, z => initial z
  | l :: ls, initial, z =>
      reachable edge ls (fun t => ∃ s, initial s ∧ edge s l t) z

/-- Exact source-indexed gluing for arbitrary relations and finite transcripts.
No independence, stochastic coupling, finite carrier, or local choice of
incompatible representatives is assumed. -/
theorem reachable_iff_single_source_path
    {S : Type u} {L : Type v} (edge : S → L → S → Prop) :
    ∀ word initial z, reachable edge word initial z ↔
      ∃ s, initial s ∧ Path edge s word z := by
  intro word
  induction word with
  | nil =>
      intro initial z
      constructor
      · intro hz; exact ⟨z, hz, Path.nil z⟩
      · rintro ⟨s, hs, path⟩; cases path; exact hs
  | cons l ls ih =>
      intro initial z
      change reachable edge ls (fun t => ∃ s, initial s ∧ edge s l t) z ↔ _
      rw [ih]
      constructor
      · rintro ⟨t, ⟨s, hs, hst⟩, tail⟩
        exact ⟨s, hs, Path.cons hst tail⟩
      · rintro ⟨s, hs, path⟩
        cases path with
        | cons hst tail => exact ⟨_, ⟨s, hs, hst⟩, tail⟩

/-- A backward exclusion certificate, independent of the forward search.
At the empty suffix, no state can be excluded; at l::ls every possible
matching successor must already have an exclusion proof. -/
inductive Excluded {S : Type u} {L : Type v} (edge : S → L → S → Prop) :
    List L → S → Prop
  | step {l ls s} : (∀ t, edge s l t → Excluded edge ls t) →
      Excluded edge (l :: ls) s

theorem exclusion_refutes_path
    {S : Type u} {L : Type v} (edge : S → L → S → Prop)
    {word : List L} {s z : S} (excluded : Excluded edge word s) :
    ¬ Path edge s word z := by
  intro path
  induction path with
  | nil => cases excluded
  | cons hst tail ih =>
      cases excluded with
      | step all => exact ih (all _ hst)

/-- Completeness of backward exclusion is constructive; it does not assume
decidability or an enumerable carrier. Python supplies finite exact oracles. -/
theorem no_path_iff_excluded
    {S : Type u} {L : Type v} (edge : S → L → S → Prop) :
    ∀ word s, (¬ ∃ z, Path edge s word z) ↔ Excluded edge word s := by
  intro word
  induction word with
  | nil =>
      intro s
      constructor
      · intro absent; exact False.elim (absent ⟨s, Path.nil s⟩)
      · intro impossible; cases impossible
  | cons l ls ih =>
      intro s
      constructor
      · intro absent
        apply Excluded.step
        intro t hst
        apply (ih t).mp
        rintro ⟨z, tail⟩
        exact absent ⟨z, Path.cons hst tail⟩
      · intro excluded
        rintro ⟨z, path⟩
        exact exclusion_refutes_path edge excluded path

end ObservationalSUCC.InstituteCausal

#print axioms ObservationalSUCC.InstituteCausal.quotient_exists_iff_fiber_congruent
#print axioms ObservationalSUCC.InstituteCausal.run_naturality
#print axioms ObservationalSUCC.InstituteCausal.every_representative_lifts
#print axioms ObservationalSUCC.InstituteCausal.lawful_quotient_iff
#print axioms ObservationalSUCC.InstituteCausal.path_preserves_source
#print axioms ObservationalSUCC.InstituteCausal.reachable_iff_single_source_path
#print axioms ObservationalSUCC.InstituteCausal.exclusion_refutes_path
#print axioms ObservationalSUCC.InstituteCausal.no_path_iff_excluded
