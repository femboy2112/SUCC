import FutureSafeForgetting
import ObservatorisQuantale

/-!
A labelled exact partial system induces Fable's Boolean endpoint exactness,
for every choice of allowed action/cost labels. Whole labelled words preserve
their actual costs by the existing SUCC path-lift theorem. A second example
separates the one-sided left unit of the inherited value-structure contract.
-/

set_option autoImplicit false
namespace ObservationalSUCC.TenaciousBridge
universe u v w z q
variable {X : Type u} {Y : Type q} {A : Type v} {O : Type w} {C : Type z}

/-- The same filter applies to a source step and to its labelled lift. -/
def admittedEdge (M : FutureSafeForgetting.System X A O C) (allow : A → C → Prop) (x y : X) : Prop :=
  ∃ a c, allow a c ∧ M.step a x = some (y, c)

/-- Every representative can realize the SAME legal step with the SAME cost.
This implies Fable's weaker closure-level criterion for that filtered relation. -/
theorem descent_edgeRealised (M : FutureSafeForgetting.System X A O C) (T : FutureSafeForgetting.System Y A O C)
    (q : X → Y) (law : FutureSafeForgetting.Descends M T q) (allow : A → C → Prop) :
    ObservatorisQuantale.EdgeRealised ObservatorisQuantale.propQ (admittedEdge M allow) q := by
  intro x y x' eq e
  obtain ⟨a, c, allowed, step⟩ := e
  have proj : T.step a (q x) = some (q y, c) := by
    simpa only [step, FutureSafeForgetting.mapStep] using (law.2 a x).symm
  have proj' : T.step a (q x') = some (q y, c) := by rw [eq]; exact proj
  obtain ⟨y', src, eq'⟩ :=
    FutureSafeForgetting.quotient_step_lifts_from_each_representative M T q law a x' (q y) c proj'
  have lifted : admittedEdge M allow x' y' := ⟨a, c, allowed, src⟩
  have reach := ObservatorisQuantale.Reach.tail (ObservatorisQuantale.Reach.refl x') lifted
  have path := (ObservatorisQuantale.star_propQ_iff (admittedEdge M allow) x' y').mpr reach
  exact ⟨_, ⟨y', eq', rfl⟩, path⟩

theorem descent_endpointExact (M : FutureSafeForgetting.System X A O C) (T : FutureSafeForgetting.System Y A O C)
    (q : X → Y) (law : FutureSafeForgetting.Descends M T q) (allow : A → C → Prop) :
    ObservatorisQuantale.EndpointExact ObservatorisQuantale.propQ (admittedEdge M allow) q :=
  (ObservatorisQuantale.exact_iff_edgeRealised ObservatorisQuantale.propQ (admittedEdge M allow) q).mpr
    (descent_edgeRealised M T q law allow)

/-- One descent law yields both filtered, unlabelled endpoint exactness and
the stronger original path-lifting contract retaining the ordered cost list. -/
theorem endpointExact_and_wordLift (M : FutureSafeForgetting.System X A O C) (T : FutureSafeForgetting.System Y A O C)
    (q : X → Y) (law : FutureSafeForgetting.Descends M T q) (allow : A → C → Prop) :
    ObservatorisQuantale.EndpointExact ObservatorisQuantale.propQ (admittedEdge M allow) q ∧
      ∀ (word : List A) (s : X) (b : Y) (costs : List C),
        FutureSafeForgetting.execute T word (q s) = some (b, costs) →
        ∃ last, FutureSafeForgetting.execute M word s = some (last, costs) ∧ q last = b :=
  ⟨descent_endpointExact M T q law allow,
   FutureSafeForgetting.quotient_path_lifts_from_each_representative M T q law⟩

/-- Predicates on Bool, ordered by inclusion. A product retains the first
predicate provided the second is inhabited. Suprema are pointwise unions. -/
def inhabitedRight : ObservatorisQuantale.LaxQuantale (Bool → Prop) where
  le P Q := ∀ i, P i → Q i
  one _ := True
  mul P Q i := P i ∧ ∃ j, Q j
  sSup U i := ∃ P, U P ∧ P i
  le_refl _ _ h := h
  le_trans h k i hi := k i (h i hi)
  le_sSup h _ hi := ⟨_, h, hi⟩
  sSup_le h i := fun ⟨P, hU, hi⟩ => h P hU i hi
  mul_mono h k i := fun ⟨hp, j, hq⟩ => ⟨h i hp, j, k j hq⟩
  mul_sSup_le _ _ _ := fun ⟨hp, j, Q, hU, hq⟩ =>
    ⟨_, ⟨Q, hU, rfl⟩, hp, j, hq⟩
  sSup_mul_le _ _ _ := fun ⟨⟨P, hU, hp⟩, hq⟩ =>
    ⟨_, ⟨P, hU, rfl⟩, hp, hq⟩
  mul_assoc_le _ _ _ _ := fun ⟨hp, j, hq, k, hr⟩ => ⟨⟨hp, j, hq⟩, k, hr⟩
  mul_assoc_ge _ _ _ _ := fun ⟨⟨hp, j, hq⟩, k, hr⟩ => ⟨hp, j, hq, k, hr⟩
  mul_one_le _ _ := fun h => h.1
  le_mul_one _ _ := fun h => ⟨h, false, True.intro⟩
  le_one_mul _ i := fun h => ⟨True.intro, i, h⟩

/-- Left deflation fails at the singleton {true} although every inherited
LaxQuantale field is satisfied. -/
theorem left_unit_can_expand :
    ¬ inhabitedRight.le (inhabitedRight.mul inhabitedRight.one (fun i => i = true))
      (fun i => i = true) := by
  intro h
  have contradiction : false = true := h false ⟨True.intro, true, rfl⟩
  cases contradiction

end ObservationalSUCC.TenaciousBridge
