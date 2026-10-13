import Std

/-!
Source-relative kernel of obstruction-guided experiment synthesis.
No mathematical priority claim. No physical source authenticity theorem.
The Python search, stochastic code, runtime bounds and discovery benchmark are
NOT formalized by this file. Standard Lean logic only; no imported domain library.
-/
set_option autoImplicit false
namespace SUCC
universe u v w

def run {X : Type u} {A : Type v} (step : A → X → X) : X → List A → X
  | x, [] => x
  | x, a :: as => run step (step a x) as

def Stable {X : Type u} {A : Type v}
    (step : A → X → X) (R : X → X → Prop) : Prop :=
  ∀ a x y, R x y → R (step a x) (step a y)

def BehaviourEq {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (x y : X) : Prop :=
  ∀ word, obs (run step x word) = obs (run step y word)

theorem run_append {X : Type u} {A : Type v} (step : A → X → X)
    (x : X) (p q : List A) :
    run step x (p ++ q) = run step (run step x p) q := by
  induction p generalizing x with
  | nil => rfl
  | cons a p ih => exact ih (step a x)

theorem stable_run {X : Type u} {A : Type v} (step : A → X → X)
    (R : X → X → Prop) (hs : Stable step R) (word : List A) :
    ∀ x y, R x y → R (run step x word) (run step y word) := by
  induction word with
  | nil => intro x y h; exact h
  | cons a word ih =>
    intro x y h
    exact ih (step a x) (step a y) (hs a x y h)

theorem behavioural_refl {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (x : X) : BehaviourEq step obs x x := by
  intro word
  rfl

theorem behavioural_symm {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (x y : X)
    (h : BehaviourEq step obs x y) : BehaviourEq step obs y x := by
  intro word
  exact (h word).symm

theorem behavioural_trans {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (x y z : X)
    (h : BehaviourEq step obs x y) (k : BehaviourEq step obs y z) :
    BehaviourEq step obs x z := by
  intro word
  exact (h word).trans (k word)

theorem behavioural_observes {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (x y : X)
    (h : BehaviourEq step obs x y) : obs x = obs y := h []

theorem behavioural_stable {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) : Stable step (BehaviourEq step obs) := by
  intro a x y h word
  exact h (a :: word)

theorem behavioural_largest {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (R : X → X → Prop)
    (hs : Stable step R) (ho : ∀ x y, R x y → obs x = obs y) :
    ∀ x y, R x y → BehaviourEq step obs x y := by
  intro x y h word
  exact ho _ _ (stable_run step R hs word x y h)

theorem separating_word_is_necessary {X : Type u} {A : Type v} {Y : Type w}
    (step : A → X → X) (obs : X → Y) (R : X → X → Prop)
    (hs : Stable step R) (ho : ∀ x y, R x y → obs x = obs y)
    (x y : X) (word : List A)
    (different : obs (run step x word) ≠ obs (run step y word)) : ¬ R x y := by
  intro related
  exact different (behavioural_largest step obs R hs ho x y related word)

theorem repair_fusion {X : Type u} {A : Type v} {Y Z : Type w}
    (step : A → X → X) (left : X → Y) (right : X → Z) (x y : X) :
    BehaviourEq step (fun x => (left x, right x)) x y ↔
      BehaviourEq step left x y ∧ BehaviourEq step right x y := by
  constructor
  · intro h
    constructor
    · intro word; exact congrArg Prod.fst (h word)
    · intro word; exact congrArg Prod.snd (h word)
  · intro h word
    exact Prod.ext (h.1 word) (h.2 word)

theorem functor_run {X : Type u} {Y : Type v} {A : Type w}
    (stepX : A → X → X) (stepY : A → Y → Y) (q : X → Y)
    (square : ∀ a x, q (stepX a x) = stepY a (q x))
    (word : List A) (x : X) : q (run stepX x word) = run stepY (q x) word := by
  induction word generalizing x with
  | nil => rfl
  | cons a word ih =>
    change q (run stepX (stepX a x) word) = run stepY (stepY a (q x)) word
    rw [ih, square a x]

theorem kernel_stability_iff_descent {X : Type u} {Y : Type v}
    (q : X → Y) (surj : ∀ y, ∃ x, q x = y) (step : X → X) :
    (∀ x y, q x = q y → q (step x) = q (step y)) ↔
    ∃ next : Y → Y, ∀ x, q (step x) = next (q x) := by
  constructor
  · intro stable
    classical
    let choose : Y → X := fun y => Classical.choose (surj y)
    have chosen : ∀ y, q (choose y) = y := fun y => Classical.choose_spec (surj y)
    refine ⟨fun y => q (step (choose y)), ?_⟩
    intro x
    exact stable x (choose (q x)) (chosen (q x)).symm
  · intro h x y equal
    obtain ⟨next, square⟩ := h
    rw [square x, square y, equal]

theorem descended_update_unique {X : Type u} {Y : Type v}
    (q : X → Y) (surj : ∀ y, ∃ x, q x = y) (step : X → X)
    (f g : Y → Y) (hf : ∀ x, q (step x) = f (q x))
    (hg : ∀ x, q (step x) = g (q x)) : f = g := by
  funext y
  obtain ⟨x, hx⟩ := surj y
  rw [← hx]
  exact (hf x).symm.trans (hg x)

def image {X : Type u} {Y : Type v} (f : X → Y) (P : X → Prop) : Y → Prop :=
  fun y => ∃ x, P x ∧ f x = y

theorem image_preimage_adjunction {X : Type u} {Y : Type v}
    (f : X → Y) (P : X → Prop) (Q : Y → Prop) :
    (∀ y, image f P y → Q y) ↔ (∀ x, P x → Q (f x)) := by
  constructor
  · intro h x hp
    exact h (f x) ⟨x, hp, rfl⟩
  · intro h y witness
    obtain ⟨x, hp, hx⟩ := witness
    rw [← hx]
    exact h x hp

theorem archive_pruning_sound {Model Witness : Type u}
    (valid : Model → Prop) (passes : Model → Witness → Prop)
    (obstruction : Witness) (necessary : ∀ m, valid m → passes m obstruction)
    (m : Model) (fails : ¬ passes m obstruction) : ¬ valid m := by
  intro hm
  exact fails (necessary m hm)

#print axioms run_append
#print axioms stable_run
#print axioms behavioural_largest
#print axioms separating_word_is_necessary
#print axioms repair_fusion
#print axioms functor_run
#print axioms kernel_stability_iff_descent
#print axioms descended_update_unique
#print axioms image_preimage_adjunction
#print axioms archive_pruning_sound
end SUCC
