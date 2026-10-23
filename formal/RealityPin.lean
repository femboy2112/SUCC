/-!
# Reality Pin: finite observational selection and source-return budget

Standalone Lean 4.14.0; no external libraries. Integer intervals represent
fixed-unit readings (rational readings may first be scaled by a common
positive denominator). Theorems are conditional on a supplied model family,
source-faithful prediction map, honest error bounds, and the stated probe set.
They do not authenticate a physical measurement or prove that the family is
exhaustive. No spectral, rational interpolation, or operator theorem is
claimed to be formalized here.
-/

namespace ObservationalSUCC.RealityPin

universe u v w

/-- Inclusive integer error interval. A negative radius gives no valid reading. -/
def Within (x y radius : Int) : Prop := y - radius ≤ x ∧ x ≤ y + radius

/-- Exact source readings and independent instrument calibration imply that
the true candidate survives after theory and measurement errors are added. -/
theorem calibrated_source_survives (prediction actual reading theory instrument : Int)
    (model_error : Within prediction actual theory)
    (measurement_error : Within actual reading instrument) :
    Within prediction reading (theory + instrument) := by
  unfold Within at *
  omega

/-- If two candidate error intervals contain one reading, their predictions
cannot be separated by more than the sum of their budgets. -/
theorem common_reading_bounds_gap (left right reading leftRadius rightRadius : Int)
    (hl : Within left reading leftRadius)
    (hr : Within right reading rightRadius) :
    left - right ≤ leftRadius + rightRadius ∧
      right - left ≤ leftRadius + rightRadius := by
  unfold Within at *
  omega

def Survivor {Model : Type u} {Probe : Type v}
    (prediction : Model → Probe → Int) (reading : Probe → Int)
    (radius : Model → Probe → Int) (observed : Probe → Prop) (m : Model) : Prop :=
  ∀ q, observed q → Within (prediction m q) (reading q) (radius m q)

/-- A predeclared separation margin identifies any two survivors modulo the
declared gauge. Quantifiers cover the entire supplied family, not samples.
`Model = Fin n` and `Probe = Fin k` give the finite-family certificate. -/
theorem separated_survivors_are_gauge_equivalent
    {Model : Type u} {Probe : Type v}
    (prediction : Model → Probe → Int) (reading : Probe → Int)
    (radius : Model → Probe → Int) (observed : Probe → Prop)
    (gauge : Model → Model → Prop)
    (separated : ∀ m n, ¬ gauge m n → ∃ q, observed q ∧
      (radius m q + radius n q < prediction m q - prediction n q ∨
       radius m q + radius n q < prediction n q - prediction m q))
    {m n : Model}
    (hm : Survivor prediction reading radius observed m)
    (hn : Survivor prediction reading radius observed n) : gauge m n := by
  apply Classical.byContradiction
  intro different
  obtain ⟨q, hq, gap⟩ := separated m n different
  have bounds := common_reading_bounds_gap _ _ _ _ _ (hm q hq) (hn q hq)
  rcases gap with gap | gap <;> omega

/-- End-to-end conditional identification: a named true source belongs to
the declared model type, calibrated readings keep it in the fiber, and the
strict separation margin forces every survivor into its gauge class. -/
theorem calibrated_identification_within_declared_family
    {Model : Type u} {Probe : Type v}
    (prediction : Model → Probe → Int) (actual reading : Probe → Int)
    (theory : Model → Probe → Int) (instrument : Probe → Int)
    (observed : Probe → Prop) (gauge : Model → Model → Prop)
    (truth : Model)
    (source_bound : ∀ q, observed q → Within (prediction truth q) (actual q) (theory truth q))
    (instrument_bound : ∀ q, observed q → Within (actual q) (reading q) (instrument q))
    (separated : ∀ m n, ¬ gauge m n → ∃ q, observed q ∧
      ((theory m q + instrument q) + (theory n q + instrument q) <
         prediction m q - prediction n q ∨
       (theory m q + instrument q) + (theory n q + instrument q) <
         prediction n q - prediction m q))
    (candidate : Model)
    (survives : Survivor prediction reading
      (fun m q => theory m q + instrument q) observed candidate) : gauge candidate truth := by
  have true_survives : Survivor prediction reading
      (fun m q => theory m q + instrument q) observed truth := by
    intro q hq
    exact calibrated_source_survives _ _ _ _ _ (source_bound q hq) (instrument_bound q hq)
  exact separated_survivors_are_gauge_equivalent prediction reading
    (fun m q => theory m q + instrument q) observed gauge separated survives true_survives

/-- Adding actual probe results shrinks, never expands, the survivor fiber. -/
theorem observer_refinement_shrinks_fiber
    {Model : Type u} {Probe : Type v}
    (prediction : Model → Probe → Int) (reading : Probe → Int)
    (radius : Model → Probe → Int) (earlier later : Probe → Prop)
    (refinement : ∀ q, earlier q → later q) (m : Model)
    (survives : Survivor prediction reading radius later m) :
    Survivor prediction reading radius earlier m := by
  intro q hq
  exact survives q (refinement q hq)

/-- A reserved second observation can reject a model that survived calibration.
This theorem uses the new reading; it never manufactures or predicts it. -/
theorem holdout_rejects_candidate
    {Model : Type u} {Probe : Type v}
    (prediction : Model → Probe → Int) (reading : Probe → Int)
    (radius : Model → Probe → Int) (observed : Probe → Prop)
    (m : Model) (holdout : Probe)
    (mismatch : ¬ Within (prediction m holdout) (reading holdout) (radius m holdout)) :
    ¬ Survivor prediction reading radius
      (fun q => observed q ∨ q = holdout) m := by
  intro survives
  exact mismatch (survives holdout (Or.inr rfl))

/-- Strict separation is sharp: two distinct predictions separated by exactly
twice the error radius can share one inclusive-boundary reading. -/
theorem equality_margin_counterexample :
    Within 0 1 1 ∧ Within 2 1 1 ∧ (0 : Int) ≠ 2 := by
  unfold Within
  decide

def ObservableEq {Model : Type u} {Probe : Type v} {Value : Type w}
    (prediction : Model → Probe → Value) (m n : Model) : Prop :=
  ∀ q, prediction m q = prediction n q

/-- A probe-language quotient identifies precisely what every allowed probe
can see. A complete decoder into any proposed physical report forces that
report to be constant on observational fibers. -/
theorem exact_decoder_requires_observable_invariance
    {Model : Type u} {Probe : Type v} {Value : Type w} {Report : Type}
    (prediction : Model → Probe → Value) (physical : Model → Report)
    (decode : (Probe → Value) → Report)
    (correct : ∀ m, decode (prediction m) = physical m)
    {m n : Model} (same : ObservableEq prediction m n) : physical m = physical n := by
  have profiles : prediction m = prediction n := funext same
  calc
    physical m = decode (prediction m) := (correct m).symm
    _ = decode (prediction n) := congrArg decode profiles
    _ = physical n := correct n

/-- Equality of all source predictions is an equivalence relation. -/
theorem observable_equivalence
    {Model : Type u} {Probe : Type v} {Value : Type w}
    (prediction : Model → Probe → Value) :
    (∀ m, ObservableEq prediction m m) ∧
    (∀ m n, ObservableEq prediction m n → ObservableEq prediction n m) ∧
    (∀ m n k, ObservableEq prediction m n → ObservableEq prediction n k →
      ObservableEq prediction m k) := by
  refine ⟨?_, ?_, ?_⟩
  · intro m q; rfl
  · intro m n h q; exact (h q).symm
  · intro m n k hmn hnk q; exact (hmn q).trans (hnk q)

/-- A valid observational geometry can collapse genuinely different sources:
an entirely dark Boolean label survives every natural-number probe. -/
theorem hidden_label_counterexample :
    ObservableEq (fun (_ : Bool) (_ : Nat) => (0 : Nat)) false true ∧ false ≠ true := by
  constructor
  · intro q; rfl
  · decide

/-- Nearest-neighbor source history on the nonnegative depth line. Self-loops
are allowed; every step has distance at most one. The length is the number
of performed steps, not the number of vertices. -/
inductive DepthWalk : Nat → Nat → Nat → Prop
  | nil (a : Nat) : DepthWalk a a 0
  | step {a b c length : Nat} :
      a ≤ b + 1 → b ≤ a + 1 → DepthWalk b c length →
      DepthWalk a c (length + 1)

/-- Every finite history has enough source steps to cover its depth change. -/
theorem walk_displacement_bound {a b length : Nat}
    (walk : DepthWalk a b length) : a ≤ b + length ∧ b ≤ a + length := by
  induction walk with
  | nil a => omega
  | step hab hba tail ih => omega

/-- A boundary history which reaches depth r and returns uses at least 2r
steps. The weighted nonzero leading coefficient needs separate algebra;
this certificate proves only the universal source-history horizon bound. -/
theorem boundary_return_requires_twice_depth {r inward outward : Nat}
    (toDepth : DepthWalk 0 r inward) (back : DepthWalk r 0 outward) :
    2 * r ≤ inward + outward := by
  have forwardBound := walk_displacement_bound toDepth
  have returnBound := walk_displacement_bound back
  omega

/-- Before 2r steps there is no such out-and-back history, even with loops. -/
theorem short_history_cannot_visit_depth_and_return {r inward outward : Nat}
    (short : inward + outward < 2 * r) :
    ¬ (DepthWalk 0 r inward ∧ DepthWalk r 0 outward) := by
  rintro ⟨toDepth, back⟩
  have lower := boundary_return_requires_twice_depth toDepth back
  omega

/-- The 2r budget is sharp for this declared nearest-neighbor source:
there are histories of exactly r steps in each direction. -/
theorem straight_depth_histories (a r : Nat) :
    DepthWalk a (a + r) r ∧ DepthWalk (a + r) a r := by
  induction r generalizing a with
  | zero => exact ⟨DepthWalk.nil a, DepthWalk.nil a⟩
  | succ r ih =>
      constructor
      · have onward := (ih (a + 1)).1
        have endpoint : a + 1 + r = a + (r + 1) := by omega
        rw [endpoint] at onward
        exact DepthWalk.step (by omega) (by omega) onward
      · exact DepthWalk.step (by omega) (by omega) (ih a).2

end ObservationalSUCC.RealityPin

#print axioms ObservationalSUCC.RealityPin.calibrated_source_survives
#print axioms ObservationalSUCC.RealityPin.common_reading_bounds_gap
#print axioms ObservationalSUCC.RealityPin.separated_survivors_are_gauge_equivalent
#print axioms ObservationalSUCC.RealityPin.calibrated_identification_within_declared_family
#print axioms ObservationalSUCC.RealityPin.observer_refinement_shrinks_fiber
#print axioms ObservationalSUCC.RealityPin.holdout_rejects_candidate
#print axioms ObservationalSUCC.RealityPin.equality_margin_counterexample
#print axioms ObservationalSUCC.RealityPin.exact_decoder_requires_observable_invariance
#print axioms ObservationalSUCC.RealityPin.observable_equivalence
#print axioms ObservationalSUCC.RealityPin.hidden_label_counterexample
#print axioms ObservationalSUCC.RealityPin.walk_displacement_bound
#print axioms ObservationalSUCC.RealityPin.boundary_return_requires_twice_depth
#print axioms ObservationalSUCC.RealityPin.short_history_cannot_visit_depth_and_return
#print axioms ObservationalSUCC.RealityPin.straight_depth_histories
