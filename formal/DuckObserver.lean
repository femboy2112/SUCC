import DuckPrinciple
import FutureSafeForgetting

/-!
# Observable Duck quotients and finite closed-relation certificates

The source transitions and readout are declared mathematical data.  A checked
finite relation is a witness for the universally quantified closure theorem;
no inference from sampling, physical authenticity, or algorithmic optimality
is hidden in that theorem.  This file reuses the original Duck word semantics
and proves compatibility with the existing FutureSafeForgetting interface.
-/
set_option autoImplicit false

namespace ObservationalSUCC.Duck.Observer
open ObservationalSUCC.Duck
universe u v w z q

/-- Same action and output types are required; source identities are not inferred. -/
def Morphism {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y) : Prop :=
  IsFactor stepX stepY f ∧ ∀ x, observeX x = observeY (f x)

theorem identity_morphism {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) :
    Morphism step observe step observe (fun x => x) := by
  exact ⟨fun _ _ => rfl, fun _ => rfl⟩

theorem compose_morphism
    {Act : Type u} {X : Type v} {Y : Type w} {Z : Type q} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out)
    (stepZ : Act → Z → Z) (observeZ : Z → Out) (f : X → Y) (g : Y → Z)
    (hf : Morphism stepX observeX stepY observeY f)
    (hg : Morphism stepY observeY stepZ observeZ g) :
    Morphism stepX observeX stepZ observeZ (fun x => g (f x)) := by
  refine ⟨factors_compose stepX stepY stepZ f g hf.1 hg.1, ?_⟩
  intro x
  exact (hf.2 x).trans (hg.2 (f x))

theorem morphism_word_readout
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y)
    (hf : Morphism stepX observeX stepY observeY f)
    (word : List Act) (x : X) :
    observeX (runWord stepX word x) = observeY (runWord stepY word (f x)) := by
  rw [hf.2, factor_all_words stepX stepY f hf.1]

/-- Final reports for ALL words also include every intermediate prefix report. -/
def BehaviorEq {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (x y : X) : Prop :=
  ∀ word : List Act, observe (runWord step word x) = observe (runWord step word y)

theorem behavior_step {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (x y : X)
    (same : BehaviorEq step observe x y) (a : Act) :
    BehaviorEq step observe (step a x) (step a y) := by
  intro word
  exact same (a :: word)

/-- A finite executable certificate may instantiate R by its complete pair table.
Both observation agreement and closure are essential, for every declared action. -/
theorem closed_relation_all_words
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (R : X → Y → Prop)
    (reports : ∀ x y, R x y → observeX x = observeY y)
    (closed : ∀ a x y, R x y → R (stepX a x) (stepY a y))
    (x : X) (y : Y) (related : R x y) (word : List Act) :
    observeX (runWord stepX word x) = observeY (runWord stepY word y) := by
  induction word generalizing x y with
  | nil => exact reports x y related
  | cons a rest ih => exact ih (stepX a x) (stepY a y) (closed a x y related)

def behaviorSetoid {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) : Setoid X where
  r := BehaviorEq step observe
  iseqv := {
    refl := fun _ _ => rfl
    symm := fun {x y} same word => (same word).symm
    trans := fun {x y z} first second word => (first word).trans (second word) }

def BehaviorQuotient {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) := Quotient (behaviorSetoid step observe)

def project {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (x : X) :
    BehaviorQuotient step observe := Quotient.mk (behaviorSetoid step observe) x

def quotientStep {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (a : Act) :
    BehaviorQuotient step observe → BehaviorQuotient step observe :=
  Quotient.lift (fun x => project step observe (step a x))
    (fun x y same => Quotient.sound (behavior_step step observe x y same a))

def quotientObserve {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) : BehaviorQuotient step observe → Out :=
  Quotient.lift observe (fun _ _ same => same [])

theorem quotient_is_morphism {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) :
    Morphism step observe (quotientStep step observe) (quotientObserve step observe)
      (project step observe) := by
  exact ⟨fun _ _ => rfl, fun _ => rfl⟩

theorem quotient_equality_iff_behavior {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (x y : X) :
    project step observe x = project step observe y ↔ BehaviorEq step observe x y := by
  exact ⟨Quotient.exact, Quotient.sound⟩

theorem quotient_is_behaviorally_separated
    {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out)
    (a b : BehaviorQuotient step observe) :
    BehaviorEq (quotientStep step observe) (quotientObserve step observe) a b → a = b := by
  refine Quotient.inductionOn₂ a b ?_
  intro x y same
  apply Quotient.sound
  intro word
  rw [morphism_word_readout step observe _ _ (project step observe)
        (quotient_is_morphism step observe),
      morphism_word_readout step observe _ _ (project step observe)
        (quotient_is_morphism step observe)]
  exact same word

/-- Any exact observation-preserving factor can only merge behaviorally equal states. -/
theorem factor_fibers_refine_behavior
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y)
    (hf : Morphism stepX observeX stepY observeY f)
    (x y : X) (same : f x = f y) : BehaviorEq stepX observeX x y := by
  intro word
  rw [morphism_word_readout stepX observeX stepY observeY f hf,
      morphism_word_readout stepX observeX stepY observeY f hf, same]

/-- A behaviorally separated target identifies precisely the observable quotient. -/
theorem separated_factor_respects_behavior
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y)
    (hf : Morphism stepX observeX stepY observeY f)
    (separates : ∀ a b, BehaviorEq stepY observeY a b → a = b)
    (x y : X) (same : BehaviorEq stepX observeX x y) : f x = f y := by
  apply separates
  intro word
  rw [← morphism_word_readout stepX observeX stepY observeY f hf,
      ← morphism_word_readout stepX observeX stepY observeY f hf]
  exact same word

/-- Universal descent for maps constant on behavioral classes, with uniqueness. -/
theorem quotient_universal
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) (f : X → Y)
    (respects : ∀ x y, BehaviorEq step observe x y → f x = f y) :
    ∃ lift : BehaviorQuotient step observe → Y,
      (∀ x, lift (project step observe x) = f x) ∧
      ∀ other : BehaviorQuotient step observe → Y,
        (∀ x, other (project step observe x) = f x) → ∀ q, other q = lift q := by
  refine ⟨Quotient.lift f respects, (fun _ => rfl), ?_⟩
  intro other commutes q
  exact Quotient.inductionOn q (fun x => commutes x)

/-- The universal lift is itself an observed morphism into any separated target. -/
theorem separated_target_factorization
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y)
    (hf : Morphism stepX observeX stepY observeY f)
    (separates : ∀ a b, BehaviorEq stepY observeY a b → a = b) :
    ∃ lift : BehaviorQuotient stepX observeX → Y,
      Morphism (quotientStep stepX observeX) (quotientObserve stepX observeX)
        stepY observeY lift ∧
      (∀ x, lift (project stepX observeX x) = f x) ∧
      ∀ other : BehaviorQuotient stepX observeX → Y,
        (∀ x, other (project stepX observeX x) = f x) → ∀ q, other q = lift q := by
  let respects := separated_factor_respects_behavior stepX observeX stepY observeY f hf separates
  let lift : BehaviorQuotient stepX observeX → Y := Quotient.lift f respects
  refine ⟨lift, ?_, (fun _ => rfl), ?_⟩
  · constructor
    · intro a q
      exact Quotient.inductionOn q (fun x => hf.1 a x)
    · intro q
      exact Quotient.inductionOn q (fun x => hf.2 x)
  · intro other commutes q
    exact Quotient.inductionOn q (fun x => commutes x)

/-- Preserve the existing partial-action/cost semantics on the total unit-cost slice. -/
def asPartial {Act : Type u} {X : Type v} {Out : Type z}
    (step : Act → X → X) (observe : X → Out) :
    ObservationalSUCC.FutureSafeForgetting.System X Act Out Unit where
  observe := observe
  step := fun a x => some (step a x, ())

theorem morphism_iff_existing_descent
    {Act : Type u} {X : Type v} {Y : Type w} {Out : Type z}
    (stepX : Act → X → X) (observeX : X → Out)
    (stepY : Act → Y → Y) (observeY : Y → Out) (f : X → Y) :
    Morphism stepX observeX stepY observeY f ↔
    ObservationalSUCC.FutureSafeForgetting.Descends
      (asPartial stepX observeX) (asPartial stepY observeY) f := by
  constructor
  · intro h
    refine ⟨h.2, ?_⟩
    intro a x
    change some (f (stepX a x), ()) = some (stepY a (f x), ())
    rw [h.1 a x]
  · intro h
    refine ⟨?_, h.1⟩
    intro a x
    have pairEq : (f (stepX a x), ()) = (stepY a (f x), ()) :=
      Option.some.inj (h.2 a x)
    exact congrArg Prod.fst pairEq

end ObservationalSUCC.Duck.Observer
