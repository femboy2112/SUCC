/-!
# Duck Principle: from behavioral resemblance to certified structure

Status: standalone Lean 4.14 proof *candidate*, pending CI/kernel replay.

The source/target action interface is DECLARED, not discovered by resemblance.
A commuting action square transports every finite experiment. Conversely,
a target observer separating all states by available action-words converts
a failed candidate factor into a distinguishing experiment.

An erased reporter supplies a counterexample: observational agreement for
every experiment does not by itself certify a proposed factor. This file
does not claim an unrestricted inference from resemblance, a classification
of physical sources, or any result on normality of pi, RH, or ABC.

No mathlib imports, axioms, sorry, native_decide, or unsafe features.
-/

namespace ObservationalSUCC.Duck

universe u v w z

/-- Apply a finite action word in temporal order. -/
def runWord {Act : Type u} {X : Type v}
    (step : Act → X → X) : List Act → X → X
  | [], x => x
  | a :: rest, x => runWord step rest (step a x)

/-- An A-shaped factor of B: every declared action square commutes. -/
def IsFactor {Act : Type u} {B : Type v} {A : Type w}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A) : Prop :=
  ∀ (action : Act) (b : B),
    project (stepB action b) = stepA action (project b)

/-- Factor maps preserve every finite action word, not just one step. -/
theorem factor_all_words
    {Act : Type u} {B : Type v} {A : Type w}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A)
    (factor : IsFactor stepB stepA project)
    (word : List Act) (b : B) :
    project (runWord stepB word b) =
      runWord stepA word (project b) := by
  induction word generalizing b with
  | nil => rfl
  | cons action rest ih =>
      change project (runWord stepB rest (stepB action b)) =
        runWord stepA rest (stepA action (project b))
      calc
        project (runWord stepB rest (stepB action b)) =
            runWord stepA rest (project (stepB action b)) :=
              ih (stepB action b)
        _ = runWord stepA rest (stepA action (project b)) := by
              rw [factor action b]

/-- Any target observation transported through a factor agrees for all words. -/
theorem factor_preserves_observations
    {Act : Type u} {B : Type v} {A : Type w} {Out : Type z}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A) (observe : A → Out)
    (factor : IsFactor stepB stepA project)
    (word : List Act) (b : B) :
    observe (project (runWord stepB word b)) =
      observe (runWord stepA word (project b)) := by
  exact congrArg observe (factor_all_words stepB stepA project factor word b)

/-- Composition of honest factor maps is an honest factor map. -/
theorem factors_compose
    {Act : Type u} {B : Type v} {A : Type w} {C : Type z}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (stepC : Act → C → C) (project : B → A) (transport : A → C)
    (first : IsFactor stepB stepA project)
    (second : IsFactor stepA stepC transport) :
    IsFactor stepB stepC (fun b => transport (project b)) := by
  intro action b
  change transport (project (stepB action b)) =
    stepC action (transport (project b))
  rw [first action b, second action (project b)]

/-- A faithful (injective) probe turns apparent one-step commutation
into actual one-step commutation, *for an already proposed map*. -/
theorem faithful_probe_certifies_factor
    {Act : Type u} {B : Type v} {A : Type w} {Out : Type z}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A) (observe : A → Out)
    (faithful : ∀ x y : A, observe x = observe y → x = y)
    (agrees : ∀ action b,
      observe (project (stepB action b)) =
        observe (stepA action (project b))) :
    IsFactor stepB stepA project := by
  intro action b
  exact faithful _ _ (agrees action b)

/-- Finite probe completion requires a declared budget and a target
state-separation theorem; a finite set of matching observations alone
is not such a theorem. -/
theorem bounded_separating_probes_certify_factor
    {Act : Type u} {B : Type v} {A : Type w} {Out : Type z}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A) (observe : A → Out) (budget : Nat)
    (separates : ∀ x y : A,
      (∀ word : List Act, word.length ≤ budget →
        observe (runWord stepA word x) =
          observe (runWord stepA word y)) → x = y)
    (agrees : ∀ action b (word : List Act),
      word.length ≤ budget →
        observe (runWord stepA word (project (stepB action b))) =
          observe (runWord stepA word (stepA action (project b)))) :
    IsFactor stepB stepA project := by
  intro action b
  apply separates
  intro word length_bound
  exact agrees action b word length_bound

/-- With a separating target probe family, every failed candidate
factor has a concrete action and a finite distinguishing target word.
This is existence, not a cost or algorithmic-efficiency bound. -/
theorem failed_factor_yields_separating_experiment
    {Act : Type u} {B : Type v} {A : Type w} {Out : Type z}
    (stepB : Act → B → B) (stepA : Act → A → A)
    (project : B → A) (observe : A → Out)
    (separates : ∀ x y : A,
      (∀ word : List Act,
        observe (runWord stepA word x) =
          observe (runWord stepA word y)) → x = y)
    (failure : ¬ IsFactor stepB stepA project) :
    ∃ action : Act, ∃ b : B, ∃ word : List Act,
      observe (runWord stepA word (project (stepB action b))) ≠
        observe (runWord stepA word (stepA action (project b))) := by
  classical
  by_contra no_witness
  apply failure
  intro action b
  apply separates
  intro word
  by_contra different
  exact no_witness ⟨action, b, word, different⟩

/-- Countermodel: two different dynamics with a completely erasing report. -/
def flipStep : Unit → Bool → Bool := fun _ b => !b
def idleStep : Unit → Bool → Bool := fun _ b => b
def erased (_ : Bool) : Unit := ()

/-- Every experiment produces the same erased report, for either source. -/
theorem erased_systems_mimic_every_word (word : List Unit) (b : Bool) :
    erased (runWord flipStep word b) =
      erased (runWord idleStep word b) := rfl

/-- Yet the proposed identity projection does NOT commute with the steps. -/
theorem erased_resemblance_does_not_certify_identity :
    ¬ IsFactor flipStep idleStep (fun b : Bool => b) := by
  intro factor
  have impossible : (true : Bool) = false := factor () false
  cases impossible

end ObservationalSUCC.Duck
