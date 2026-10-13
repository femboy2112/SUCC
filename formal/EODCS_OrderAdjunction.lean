/-!
# EODCS: order-theoretic functor composition and Galois connection lemmas

Self-contained Lean 4 proof candidate, independent of mathlib. This file
is deliberately NOT labelled kernel-verified until an actual Lean invocation
has compiled it. Python finite checks are separate instruments.

Hypotheses are explicit: the relations and maps are arbitrary until their
specific monotonicity, reflexivity, and antisymmetry assumptions are supplied.
-/

namespace ObservationalSUCC

universe u v w

def Monotone {A : Type u} {B : Type v}
    (ra : A → A → Prop) (rb : B → B → Prop) (f : A → B) : Prop :=
  ∀ {x y : A}, ra x y → rb (f x) (f y)

theorem monotone_comp
    {A : Type u} {B : Type v} {C : Type w}
    (ra : A → A → Prop) (rb : B → B → Prop) (rc : C → C → Prop)
    (f : A → B) (g : B → C)
    (hf : Monotone ra rb f) (hg : Monotone rb rc g) :
    Monotone ra rc (fun x => g (f x)) := by
  intro x y hxy
  exact hg (hf hxy)

def IsAdjunction {A : Type u} {B : Type v}
    (ra : A → A → Prop) (rb : B → B → Prop)
    (f : A → B) (g : B → A) : Prop :=
  ∀ x y, rb (f x) y ↔ ra x (g y)

theorem adjunction_unit
    {A : Type u} {B : Type v}
    (ra : A → A → Prop) (rb : B → B → Prop)
    (f : A → B) (g : B → A)
    (reflB : ∀ y, rb y y)
    (adj : IsAdjunction ra rb f g) (x : A) :
    ra x (g (f x)) := by
  exact (adj x (f x)).mp (reflB (f x))

theorem adjunction_counit
    {A : Type u} {B : Type v}
    (ra : A → A → Prop) (rb : B → B → Prop)
    (f : A → B) (g : B → A)
    (reflA : ∀ x, ra x x)
    (adj : IsAdjunction ra rb f g) (y : B) :
    rb (f (g y)) y := by
  exact (adj (g y) y).mpr (reflA (g y))

theorem right_adjoint_unique
    {A : Type u} {B : Type v}
    (ra : A → A → Prop) (rb : B → B → Prop)
    (f : A → B) (g₁ g₂ : B → A)
    (reflA : ∀ x, ra x x)
    (antisymA : ∀ x y, ra x y → ra y x → x = y)
    (h₁ : IsAdjunction ra rb f g₁)
    (h₂ : IsAdjunction ra rb f g₂) :
    ∀ y, g₁ y = g₂ y := by
  intro y
  apply antisymA
  · exact (h₂ (g₁ y) y).mp ((h₁ (g₁ y) y).mpr (reflA (g₁ y)))
  · exact (h₁ (g₂ y) y).mp ((h₂ (g₂ y) y).mpr (reflA (g₂ y)))

end ObservationalSUCC
