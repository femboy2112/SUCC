/-!
# Hereditary predicates and source-faithful ancestral reachability

Standalone Lean 4.14.0, with no domain-library imports.

The hereditary-predicate characterization is classical (Frege; Principia
Mathematica I, Section E and *90).  This file uses modern reflexive-transitive
closure on the whole type.  Principia restricts the reflexive case to the field
of the relation; an isolated state is therefore handled differently here.
This is a modern formalization of the principle, not of Principia's type system.

The endpoint criterion is an elementary SUCC synthesis.  It preserves reachable
reports from EACH selected source state, not steps, lengths, actions, costs,
probabilities, source identity, or an infinite-orbit distribution.  The stronger
trace/path statements remain in FutureSafeForgetting.lean.
-/

set_option autoImplicit false

namespace ObservationalSUCC.PrincipiaAncestral

universe u v

inductive Reach {X : Type u} (R : X → X → Prop) : X → X → Prop where
  | refl (x : X) : Reach R x x
  | tail {x y z : X} : Reach R x y → R y z → Reach R x z

def ForwardClosed {X : Type u} (R : X → X → Prop) (P : X → Prop) : Prop :=
  ∀ x y, P x → R x y → P y

def Saturate {X : Type u} {O : Type v} (q : X → O) (P : X → Prop)
    (x : X) : Prop := ∃ y, P y ∧ q y = q x

def QuotientEdge {X : Type u} {O : Type v} (R : X → X → Prop)
    (q : X → O) (a b : O) : Prop :=
  ∃ x y, q x = a ∧ q y = b ∧ R x y

def EndpointExact {X : Type u} {O : Type v} (R : X → X → Prop)
    (q : X → O) : Prop :=
  ∀ x b, Reach (QuotientEdge R q) (q x) b ↔
    ∃ y, Reach R x y ∧ q y = b

/-- A hereditary predicate propagates along every finite source path. -/
theorem reach_preserves {X : Type u} {R : X → X → Prop} {x y : X}
    (path : Reach R x y) (P : X → Prop) (closed : ForwardClosed R P)
    (initial : P x) : P y := by
  induction path with
  | refl => exact initial
  | tail pathSoFar edge ih => exact closed _ _ ih edge

/-- Reachability is exactly preservation of every hereditary predicate. -/
theorem reach_iff_hereditary {X : Type u} (R : X → X → Prop) (x y : X) :
    Reach R x y ↔ ∀ P : X → Prop, ForwardClosed R P → P x → P y := by
  constructor
  · intro path P closed initial
    exact reach_preserves path P closed initial
  · intro all
    exact all (Reach R x) (fun _ _ pathSoFar edge => Reach.tail pathSoFar edge)
      (Reach.refl x)

/-- A relation-preserving map sends every finite path to a path. -/
theorem reach_maps {X : Type u} {O : Type v}
    {R : X → X → Prop} {Q : O → O → Prop} (q : X → O)
    (maps : ∀ x y, R x y → Q (q x) (q y)) {x y : X}
    (path : Reach R x y) : Reach Q (q x) (q y) := by
  induction path with
  | refl => exact Reach.refl _
  | tail pathSoFar edge ih => exact Reach.tail ih (maps _ _ edge)

/-- Existential quotient edges always preserve forward reachability. -/
theorem quotient_reach_forward {X : Type u} {O : Type v}
    (R : X → X → Prop) (q : X → O) {x y : X}
    (path : Reach R x y) : Reach (QuotientEdge R q) (q x) (q y) := by
  exact reach_maps q (fun a b edge => ⟨a, b, rfl, rfl, edge⟩) path

/-- For one selected source, only the saturation of that source's reachable
set must be hereditary.  This is weaker than exactness at every source. -/
theorem selected_endpoint_exact_iff_saturated_reach_closed
    {X : Type u} {O : Type v} (R : X → X → Prop) (q : X → O) (x : X) :
    (∀ b, Reach (QuotientEdge R q) (q x) b ↔
      ∃ y, Reach R x y ∧ q y = b) ↔
    ForwardClosed R (Saturate q (Reach R x)) := by
  constructor
  · intro exactAt s t saturated edge
    obtain ⟨u, path, same⟩ := saturated
    have toS : Reach (QuotientEdge R q) (q x) (q s) :=
      same ▸ quotient_reach_forward R q path
    have toT : Reach (QuotientEdge R q) (q x) (q t) :=
      Reach.tail toS ⟨s, t, rfl, rfl, edge⟩
    exact (exactAt (q t)).mp toT
  · intro saturatedClosed b
    constructor
    · intro observed
      let image : O → Prop := fun c => ∃ y, Reach R x y ∧ q y = c
      have imageClosed : ForwardClosed (QuotientEdge R q) image := by
        intro a c atA edge
        obtain ⟨z, path, qz⟩ := atA
        obtain ⟨s, t, qs, qt, st⟩ := edge
        have satS : Saturate q (Reach R x) s := ⟨z, path, qz.trans qs.symm⟩
        obtain ⟨w, reachW, qw⟩ := saturatedClosed s t satS st
        exact ⟨w, reachW, qw.trans qt⟩
      exact reach_preserves observed image imageClosed ⟨x, Reach.refl x, rfl⟩
    · intro original
      obtain ⟨y, path, report⟩ := original
      exact report ▸ quotient_reach_forward R q path

/-- The exact endpoint criterion: quotienting creates no new reachable report
from any chosen source iff saturating each hereditary predicate keeps it
hereditary.  No finiteness, surjectivity, or choice assumption is required. -/
theorem endpoint_exact_iff_saturation_closed {X : Type u} {O : Type v}
    (R : X → X → Prop) (q : X → O) :
    EndpointExact R q ↔
      ∀ P : X → Prop, ForwardClosed R P → ForwardClosed R (Saturate q P) := by
  constructor
  · intro exactEndpoints P closed x y sx edge
    obtain ⟨u, pu, same⟩ := sx
    have observed : Reach (QuotientEdge R q) (q u) (q y) := by
      exact Reach.tail (Reach.refl _) ⟨x, y, same.symm, rfl, edge⟩
    obtain ⟨v, path, report⟩ := (exactEndpoints u (q y)).mp observed
    exact ⟨v, reach_preserves path P closed pu, report⟩
  · intro saturation x b
    constructor
    · intro observed
      let P : X → Prop := Reach R x
      have closed : ForwardClosed R P := fun _ _ pathSoFar edge => Reach.tail pathSoFar edge
      have saturatedClosed := saturation P closed
      let image : O → Prop := fun c => ∃ y, P y ∧ q y = c
      have imageClosed : ForwardClosed (QuotientEdge R q) image := by
        intro a c atA edge
        obtain ⟨z, pz, qz⟩ := atA
        obtain ⟨s, t, qs, qt, st⟩ := edge
        have satS : Saturate q P s := ⟨z, pz, qz.trans qs.symm⟩
        obtain ⟨w, pw, qw⟩ := saturatedClosed s t satS st
        exact ⟨w, pw, qw.trans qt⟩
      exact reach_preserves observed image imageClosed ⟨x, Reach.refl x, rfl⟩
    · intro original
      obtain ⟨y, path, report⟩ := original
      rw [← report]
      exact quotient_reach_forward R q path

def SameReachableReports {X : Type u} {O : Type v} (R : X → X → Prop)
    (q : X → O) : Prop :=
  ∀ x y, q x = q y → ∀ b,
    (∃ z, Reach R x z ∧ q z = b) ↔ (∃ z, Reach R y z ∧ q z = b)

/-- An equivalent test compares entire reachable-report sets inside each
observation fiber; one-step successor sets need not agree. -/
theorem endpoint_exact_iff_same_reachable_reports {X : Type u} {O : Type v}
    (R : X → X → Prop) (q : X → O) :
    EndpointExact R q ↔ SameReachableReports R q := by
  constructor
  · intro exactEndpoints x y same b
    constructor
    · intro original
      have observed := (exactEndpoints x b).mpr original
      exact (exactEndpoints y b).mp (same ▸ observed)
    · intro original
      have observed := (exactEndpoints y b).mpr original
      exact (exactEndpoints x b).mp (same.symm ▸ observed)
  · intro sameReports
    apply (endpoint_exact_iff_saturation_closed R q).mpr
    intro P closed x y sx edge
    obtain ⟨u, pu, same⟩ := sx
    have fromX : ∃ z, Reach R x z ∧ q z = q y :=
      ⟨y, Reach.tail (Reach.refl x) edge, rfl⟩
    obtain ⟨v, path, report⟩ := (sameReports u x same (q y)).mpr fromX
    exact ⟨v, reach_preserves path P closed pu, report⟩

/-- A closed source invariant obstructs a reachable report without enumerating
source paths. The premises are finite-checkable on a declared finite carrier. -/
theorem closed_invariant_excludes_report {X : Type u} {O : Type v}
    (R : X → X → Prop) (q : X → O) (P : X → Prop) (x : X) (b : O)
    (closed : ForwardClosed R P) (initial : P x)
    (excludes : ∀ y, P y → q y ≠ b) :
    ¬ ∃ y, Reach R x y ∧ q y = b := by
  intro lifted
  obtain ⟨y, path, report⟩ := lifted
  exact excludes y (reach_preserves path P closed initial) report

/-- An observed quotient path and a hereditary source obstruction certify
that the observer invents a reachable endpoint for this selected source. -/
theorem invariant_refutes_endpoint_exact {X : Type u} {O : Type v}
    (R : X → X → Prop) (q : X → O) (P : X → Prop) (x : X) (b : O)
    (closed : ForwardClosed R P) (initial : P x)
    (excludes : ∀ y, P y → q y ≠ b)
    (observed : Reach (QuotientEdge R q) (q x) b) :
    ¬ EndpointExact R q := by
  intro exactEndpoints
  exact closed_invariant_excludes_report R q P x b closed initial excludes
    ((exactEndpoints x b).mp observed)

#check reach_preserves
#print axioms reach_preserves
#check reach_iff_hereditary
#print axioms reach_iff_hereditary
#check reach_maps
#print axioms reach_maps
#check quotient_reach_forward
#print axioms quotient_reach_forward
#check selected_endpoint_exact_iff_saturated_reach_closed
#print axioms selected_endpoint_exact_iff_saturated_reach_closed
#check endpoint_exact_iff_saturation_closed
#print axioms endpoint_exact_iff_saturation_closed
#check endpoint_exact_iff_same_reachable_reports
#print axioms endpoint_exact_iff_same_reachable_reports
#check closed_invariant_excludes_report
#print axioms closed_invariant_excludes_report
#check invariant_refutes_endpoint_exact
#print axioms invariant_refutes_endpoint_exact

end ObservationalSUCC.PrincipiaAncestral
