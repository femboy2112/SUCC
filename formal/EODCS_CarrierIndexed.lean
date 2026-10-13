/-!
# Carrier-indexed histories: original source is invariant, reports transport

Lean 4.14.0; no mathlib. The source carrier is the architectural object.
A lawful action U : A -> C -> (Report × C) changes CURRENT carrier state
and emits a report. The ORIGINAL source index is a separate, immutable
coordinate; source propositions are not silently reinterpreted after U.

A checked quotient q : C -> D may transport reports and current states only
if BOTH the joint one-step report and the successor-current squares commute.
Under these exact hypotheses, all finite action-word histories commute, and
the original index stays unchanged. A report-only equality is insufficient.

This module formalizes deterministic total actions and exact predicate support.
Stochastic joint-kernel finite reindexing, partial access and real physical
source completeness are separately checked/derived outside this Lean module.
-/

namespace CarrierIndexed

universe u v w z

def CarrierReports {A : Type u} {C : Type v} {R : Type w}
    (step : A → C → R × C) : C → List A → List R
  | _, [] => []
  | c, a :: rest =>
      (step a c).1 :: CarrierReports step (step a c).2 rest

def CarrierEndpoint {A : Type u} {C : Type v} {R : Type w}
    (step : A → C → R × C) : C → List A → C
  | c, [] => c
  | c, a :: rest => CarrierEndpoint step (step a c).2 rest

/-- The original index is the exact SAME value after any finite history.
This is accounting, not a claim that an observer knows the original state. -/
def CarrierRunSource {Original : Type u} {A : Type v} {C : Type w}
    {R : Type z} (step : A → C → R × C)
    (original : Original) (current : C) (word : List A) :
    Original × C :=
  (original, CarrierEndpoint step current word)

theorem carrier_original_is_invariant
    {Original : Type u} {A : Type v} {C : Type w}
    {R : Type z} (step : A → C → R × C)
    (original : Original) (current : C) (word : List A) :
    (CarrierRunSource step original current word).1 = original := by
  rfl

/-- Actual report histories are natural under a commuting source square.
The proof does NOT assume surjectivity, invertibility, probability or
a physical right to execute incompatible counterfactual words. -/
theorem all_finite_carrier_reports_transport
    {A : Type u} {C : Type v} {D : Type w} {R : Type z}
    (fine : A → C → R × C) (coarse : A → D → R × D)
    (q : C → D)
    (report_square : ∀ a c, (fine a c).1 = (coarse a (q c)).1)
    (carrier_square : ∀ a c, q (fine a c).2 = (coarse a (q c)).2) :
    ∀ c word, CarrierReports fine c word =
      CarrierReports coarse (q c) word := by
  intro c word
  induction word generalizing c with
  | nil => rfl
  | cons a rest ih =>
      change (fine a c).1 :: CarrierReports fine (fine a c).2 rest =
        (coarse a (q c)).1 :: CarrierReports coarse (coarse a (q c)).2 rest
      rw [report_square a c, ih ((fine a c).2), carrier_square a c]

theorem all_finite_carrier_endpoints_transport
    {A : Type u} {C : Type v} {D : Type w} {R : Type z}
    (fine : A → C → R × C) (coarse : A → D → R × D)
    (q : C → D)
    (report_square : ∀ a c, (fine a c).1 = (coarse a (q c)).1)
    (carrier_square : ∀ a c, q (fine a c).2 = (coarse a (q c)).2) :
    ∀ c word, q (CarrierEndpoint fine c word) =
      CarrierEndpoint coarse (q c) word := by
  intro c word
  induction word generalizing c with
  | nil => rfl
  | cons a rest ih =>
      change q (CarrierEndpoint fine (fine a c).2 rest) =
        CarrierEndpoint coarse (coarse a (q c)).2 rest
      rw [ih ((fine a c).2), carrier_square a c]

/-- An arbitrary source-indexed support relation is pushed forward
over CURRENT state only. The quantified original source is retained. -/
def PushCarrierSupport {Original : Type u} {C : Type v} {D : Type w}
    (q : C → D) (support : Original → C → Prop) :
    Original → D → Prop :=
  fun original d => ∃ c, support original c ∧ q c = d

theorem original_support_survives_carrier_pushforward
    {Original : Type u} {C : Type v} {D : Type w}
    (q : C → D) (support : Original → C → Prop)
    (original : Original) :
    (∃ c, support original c) ↔
    (∃ d, PushCarrierSupport q support original d) := by
  constructor
  · rintro ⟨c, hc⟩
    exact ⟨q c, c, hc, rfl⟩
  · rintro ⟨d, c, hc, _⟩
    exact ⟨c, hc⟩

/-- A valid claim about ORIGINAL source identity remains valid after
a current-state-only quotient, since its original support is preserved. -/
theorem original_claim_transport
    {Original : Type u} {C : Type v} {D : Type w}
    {Target : Type z}
    (q : C → D) (support : Original → C → Prop)
    (target : Original → Target) (value : Target)
    (source_claim : ∀ x, (∃ c, support x c) → target x = value) :
    ∀ x, (∃ d, PushCarrierSupport q support x d) →
      target x = value := by
  intro x coarseSupported
  exact source_claim x
    ((original_support_survives_carrier_pushforward q support x).mpr
      coarseSupported)

/-- One-step lawful q:C->D and r:D->E compose into a lawful r∘q:C->E.
Without actual commuting report and successor squares this is false. -/
theorem carrier_comparison_composes
    {A : Type u} {C : Type v} {D : Type w} {E : Type z}
    {R : Type u}
    (fine : A → C → R × C)
    (mid : A → D → R × D)
    (outer : A → E → R × E)
    (q : C → D) (r : D → E)
    (h₁ : ∀ a c, (fine a c).1 = (mid a (q c)).1 ∧
                     q (fine a c).2 = (mid a (q c)).2)
    (h₂ : ∀ a d, (mid a d).1 = (outer a (r d)).1 ∧
                     r (mid a d).2 = (outer a (r d)).2) :
    ∀ a c, (fine a c).1 = (outer a (r (q c))).1 ∧
           (r ∘ q) (fine a c).2 =
             (outer a (r (q c))).2 := by
  intro a c
  constructor
  · calc
      (fine a c).1 = (mid a (q c)).1 := (h₁ a c).1
      _ = (outer a (r (q c))).1 := (h₂ a (q c)).1
  · calc
      (r ∘ q) (fine a c).2 = r (q (fine a c).2) := rfl
      _ = r (mid a (q c)).2 := by rw [(h₁ a c).2]
      _ = (outer a (r (q c))).2 := (h₂ a (q c)).2

end CarrierIndexed
