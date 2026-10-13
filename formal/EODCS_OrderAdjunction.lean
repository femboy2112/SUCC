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


/-- A source-honest universal order quotient criterion: surjective F with
order-lifting, and an F-fiber-constant monotone h, factors uniquely through F.
This is stronger than a table-only check and uses only Classical.choice for
the witness-selection function. No assumption that arbitrary surjective
monotone maps have ordered lifts is made. -/
theorem sufficient_order_quotient_factorization
    {A : Type u} {B : Type v} {C : Type w}
    (ra : A → A → Prop) (rb : B → B → Prop) (rc : C → C → Prop)
    (f : A → B) (h : A → C)
    (surj : ∀ y : B, ∃ x : A, f x = y)
    (fiber : ∀ x x' : A, f x = f x' → h x = h x')
    (hmono : Monotone ra rc h)
    (lifts : ∀ y z : B, rb y z →
      ∃ x x' : A, f x = y ∧ f x' = z ∧ ra x x') :
    ∃ g : B → C,
      (∀ x : A, g (f x) = h x) ∧
      Monotone rb rc g ∧
      (∀ g' : B → C, (∀ x : A, g' (f x) = h x) →
         ∀ y : B, g' y = g y) := by
  classical
  let s : B → A := fun y => Classical.choose (surj y)
  have sec (y : B) : f (s y) = y := by
    exact Classical.choose_spec (surj y)
  let g : B → C := fun y => h (s y)
  have factor (x : A) : g (f x) = h x := by
    exact fiber (s (f x)) x (sec (f x))
  have mono : Monotone rb rc g := by
    intro y z hyz
    obtain ⟨x, x', hx, hz, hxx'⟩ := lifts y z hyz
    have gx : g y = h x := by
      exact fiber (s y) x (by
        calc
          f (s y) = y := sec y
          _ = f x := hx.symm)
    have gz : g z = h x' := by
      exact fiber (s z) x' (by
        calc
          f (s z) = z := sec z
          _ = f x' := hz.symm)
    rw [gx, gz]
    exact hmono hxx'
  refine ⟨g, factor, mono, ?_⟩
  intro g' hg' y
  obtain ⟨x, hx⟩ := surj y
  calc
    g' y = g' (f x) := by rw [hx]
    _ = h x := hg' x
    _ = g (f x) := (factor x).symm
    _ = g y := by rw [hx]

end ObservationalSUCC
