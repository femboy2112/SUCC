/-!
# NO-GHOST: complete constraints and rigid history transport

Pinned standalone Lean 4.14.0, without mathlib.

`source_supported_constraint_gluing` proves an explicitly source-relative,
unique gluing theorem. A proposed execution is an assignment to a declared
variable family. Constraint locality and complete constraint coverage are
hypotheses, not consequences of compatible public reports. The original
source is provided with admissibility evidence; no source is synthesized.

`source_indexed_all_priors_iff_complete_kernel` proves the complete joint
kernel criterion, including its Dirac-preparation converse. Coefficients
are abstract with explicit unit laws; normalization and positive evidence
remain separate hypotheses of a concrete stochastic instrument model.

`invariant_transport_path_independent` proves coherence when each schedule's
private history embeds injectively in a common, fully retained invariant.
This is a sufficient rigidity hypothesis, not a claim that any physical
carrier possesses such an invariant or that arbitrary chosen diamonds are
coherent. `bit_comparisons_fail_braid` records the strict distinction.
-/

namespace ObservationalSUCC.NoGhost

universe u v w x y

namespace ConstraintCover

variable {Source : Type u} {Variable : Type v} {Value : Type w}
    {Context : Type x} {Constraint : Type y}

/-- A local record's values outside its context carry no meaning. -/
def Compatible (scope : Context → Variable → Prop)
    (record : Context → Variable → Value) : Prop :=
  ∀ i j a, scope i a → scope j a → record i a = record j a

/-- A cover has an explicit owner for each variable; no choice is hidden. -/
def glue (owner : Variable → Context)
    (record : Context → Variable → Value) : Variable → Value :=
  fun a => record (owner a) a

theorem glue_restricts
    (scope : Context → Variable → Prop)
    (owner : Variable → Context) (owner_covers : ∀ a, scope (owner a) a)
    (record : Context → Variable → Value)
    (compatible : Compatible scope record) :
    ∀ i a, scope i a → glue owner record a = record i a := by
  intro i a ha
  exact compatible (owner a) i a (owner_covers a) ha

theorem glue_unique
    (scope : Context → Variable → Prop)
    (owner : Variable → Context) (owner_covers : ∀ a, scope (owner a) a)
    (record : Context → Variable → Value)
    (candidate : Variable → Value)
    (restricts : ∀ i a, scope i a → candidate a = record i a) :
    candidate = glue owner record := by
  funext a
  exact restricts (owner a) a (owner_covers a)

/-- The key locality law: each constraint uses ONLY its declared variables. -/
def ConstraintLocal (support : Constraint → Variable → Prop)
    (law : Source → Constraint → (Variable → Value) → Prop) : Prop :=
  ∀ source k f g,
    (∀ a, support k a → f a = g a) →
    (law source k f ↔ law source k g)

theorem glue_preserves_complete_constraints
    (scope : Context → Variable → Prop)
    (owner : Variable → Context) (owner_covers : ∀ a, scope (owner a) a)
    (record : Context → Variable → Value)
    (compatible : Compatible scope record)
    (support : Constraint → Variable → Prop)
    (law : Source → Constraint → (Variable → Value) → Prop)
    (locality : ConstraintLocal support law)
    (complete : ∀ k, ∃ i, ∀ a, support k a → scope i a)
    (source : Source)
    (locally_lawful : ∀ i k,
      (∀ a, support k a → scope i a) → law source k (record i)) :
    ∀ k, law source k (glue owner record) := by
  intro k
  obtain ⟨i, hi⟩ := complete k
  have agree : ∀ a, support k a → glue owner record a = record i a := by
    intro a ha
    exact glue_restricts scope owner owner_covers record compatible i a (hi a ha)
  exact (locality source k (glue owner record) (record i) agree).mpr
    (locally_lawful i k hi)

/-- Complete private interfaces and all constraints yield a unique lawful
global assignment over the GIVEN admissible original source.

`admissible` must encode the actual original-source contract. `law` must
encode every preparation, transition, enabledness, ancestry and resource
constraint in the concrete application. No adequacy of that encoding is
asserted by this generic theorem. -/
theorem source_supported_constraint_gluing
    (scope : Context → Variable → Prop)
    (owner : Variable → Context) (owner_covers : ∀ a, scope (owner a) a)
    (record : Context → Variable → Value)
    (compatible : Compatible scope record)
    (support : Constraint → Variable → Prop)
    (law : Source → Constraint → (Variable → Value) → Prop)
    (locality : ConstraintLocal support law)
    (complete : ∀ k, ∃ i, ∀ a, support k a → scope i a)
    (admissible : Source → Prop) (source : Source)
    (source_supported : admissible source)
    (locally_lawful : ∀ i k,
      (∀ a, support k a → scope i a) → law source k (record i)) :
    ∃ global : Source × (Variable → Value),
      global.1 = source ∧ admissible global.1 ∧
      (∀ i a, scope i a → global.2 a = record i a) ∧
      (∀ k, law global.1 k global.2) ∧
      (∀ other : Source × (Variable → Value),
        other.1 = source →
        (∀ i a, scope i a → other.2 a = record i a) → other = global) := by
  refine ⟨(source, glue owner record), rfl, source_supported, ?_, ?_, ?_⟩
  · exact glue_restricts scope owner owner_covers record compatible
  · exact glue_preserves_complete_constraints scope owner owner_covers record
      compatible support law locality complete source locally_lawful
  · intro other hs hr
    have hv := glue_unique scope owner owner_covers record other.2 hr
    exact Prod.ext hs hv

end ConstraintCover

namespace CompleteKernel

variable {Source : Type u} {Current : Type v} {Atom : Type w} {Weight : Type x}

/-- The following theorem requires only these two elementary coefficient
laws. Nonnegative rational coefficients are an intended specialization;
positivity and normalization are separate event-model obligations. -/
structure Coefficients (Weight : Type x) where
  zero : Weight
  one : Weight
  add : Weight → Weight → Weight
  mul : Weight → Weight → Weight
  one_mul : ∀ x, mul one x = x
  add_zero : ∀ x, add x zero = x

/-- A source-indexed finite, unnormalized mixture. The source argument is
retained, never summed out. `Atom` must include all event-labelled receipts
and the full interface that the intended comparison is to preserve. -/
def law (coeff : Coefficients Weight)
    (kernel : Source → Current → Atom → Weight)
    (source : Source) (atom : Atom) : List (Current × Weight) → Weight
  | [] => coeff.zero
  | (current, weight) :: rest =>
      coeff.add (coeff.mul weight (kernel source current atom))
        (law coeff kernel source atom rest)

theorem complete_kernel_implies_all_prior_laws
    (coeff : Coefficients Weight)
    (left right : Source → Current → Atom → Weight)
    (same_kernel : ∀ source current atom,
      left source current atom = right source current atom) :
    ∀ source atom prior,
      law coeff left source atom prior = law coeff right source atom prior := by
  intro source atom prior
  induction prior with
  | nil => rfl
  | cons head rest ih =>
      rcases head with ⟨current, weight⟩
      change coeff.add (coeff.mul weight (left source current atom))
          (law coeff left source atom rest) =
        coeff.add (coeff.mul weight (right source current atom))
          (law coeff right source atom rest)
      rw [same_kernel source current atom, ih]

/-- Necessity uses the actual Dirac preparation `(current, one)`.
If the physical preparation menu excludes a Dirac, this converse may not
be invoked for that state; the theorem quantifies over ALL finite priors. -/
theorem source_indexed_all_priors_iff_complete_kernel
    (coeff : Coefficients Weight)
    (left right : Source → Current → Atom → Weight) :
    (∀ source atom prior,
      law coeff left source atom prior = law coeff right source atom prior) ↔
    (∀ source current atom, left source current atom = right source current atom) := by
  constructor
  · intro same_laws source current atom
    have dirac := same_laws source atom [(current, coeff.one)]
    simpa only [law, coeff.one_mul, coeff.add_zero] using dirac
  · exact complete_kernel_implies_all_prior_laws coeff left right

end CompleteKernel

namespace RigidTransport

variable {Schedule : Type u} {History : Schedule → Type v} {Invariant : Type w}

/-- An authorized, directed adjacent comparison edge. Reverse edges and
their inverse equations, when required, belong to the supplied graph. -/
inductive Path (Edge : Schedule → Schedule → Type x) :
    Schedule → Schedule → Type (max u x)
  | nil (s : Schedule) : Path Edge s s
  | cons {s t r : Schedule} : Edge s t → Path Edge t r → Path Edge s r

def Path.transport
    {Edge : Schedule → Schedule → Type x}
    (compare : ∀ {s t : Schedule}, Edge s t → History s → History t) :
    {s t : Schedule} → Path Edge s t → History s → History t
  | _, _, .nil _, h => h
  | _, _, .cons e p, h => Path.transport compare p (compare e h)

theorem path_preserves_invariant
    {Edge : Schedule → Schedule → Type x}
    (invariant : ∀ s, History s → Invariant)
    (compare : ∀ {s t : Schedule}, Edge s t → History s → History t)
    (edge_preserves : ∀ {s t : Schedule} (e : Edge s t) (h : History s),
      invariant t (compare e h) = invariant s h) :
    ∀ {s t : Schedule} (p : Path Edge s t) (h : History s),
      invariant t (Path.transport (History := History) @compare p h) = invariant s h := by
  intro s t p
  induction p with
  | nil s => intro h; rfl
  | cons e p ih =>
      intro h
      exact (ih (compare e h)).trans (edge_preserves e h)

/-- Every authorized path has the same transport if complete retained
private-history data are injectively represented in one common object.
In particular every braid, commuting square and loop commutes.
This does not assume that the common invariant is observable. -/
theorem invariant_transport_path_independent
    {Edge : Schedule → Schedule → Type x}
    (invariant : ∀ s, History s → Invariant)
    (injective : ∀ s h k, invariant s h = invariant s k → h = k)
    (compare : ∀ {s t : Schedule}, Edge s t → History s → History t)
    (edge_preserves : ∀ {s t : Schedule} (e : Edge s t) (h : History s),
      invariant t (compare e h) = invariant s h)
    {s t : Schedule} (p q : Path Edge s t) :
    ∀ h : History s, Path.transport (History := History) @compare p h = Path.transport (History := History) @compare q h := by
  intro h
  apply injective t
  exact (path_preserves_invariant invariant compare edge_preserves p h).trans
    (path_preserves_invariant invariant compare edge_preserves q h).symm

/-- Rigidity plus both directed edges forces mutual inverses. -/
theorem invariant_comparisons_are_inverse
    (invariant : ∀ s, History s → Invariant)
    (injective : ∀ s h k, invariant s h = invariant s k → h = k)
    {s t : Schedule} (forward : History s → History t)
    (backward : History t → History s)
    (hf : ∀ h, invariant t (forward h) = invariant s h)
    (hb : ∀ h, invariant s (backward h) = invariant t h) :
    (∀ h, backward (forward h) = h) ∧
    (∀ h, forward (backward h) = h) := by
  constructor
  · intro h
    exact injective s _ _ ((hb (forward h)).trans (hf h))
  · intro h
    exact injective t _ _ ((hf (backward h)).trans (hb h))

end RigidTransport

namespace Countermodels

def xor (x y : Bool) : Bool := if x then !y else y
def R (p : Bool × Bool) : Bool × Bool := (p.1, xor p.1 p.2)
def R12 (p : Bool × Bool × Bool) : Bool × Bool × Bool :=
  (p.1, xor p.1 p.2.1, p.2.2)
def R23 (p : Bool × Bool × Bool) : Bool × Bool × Bool :=
  (p.1, p.2.1, xor p.2.1 p.2.2)

theorem bit_comparison_involutive : ∀ p, R (R p) = p := by
  intro p
  rcases p with ⟨x, y⟩
  cases x <;> cases y <;> rfl

/-- Algebraic calibration ONLY; physical realizability requires the typed
carrier construction in the research manuscript and executable model. -/
theorem bit_comparisons_fail_braid :
    R12 (R23 (R12 (false, true, false))) ≠
      R23 (R12 (R23 (false, true, false))) := by
  decide

/-- Two compatible singleton records can miss an uncovered joint law.
The demanded global law is equality of the two coordinates. -/
theorem omitted_joint_constraint_blocks_gluing :
    ¬ ∃ assignment : Bool → Bool,
      assignment false = false ∧ assignment true = true ∧
      assignment false = assignment true := by
  rintro ⟨assignment, hfalse, htrue, law⟩
  have bad : false = true := hfalse.symm.trans (law.trans htrue)
  cases bad

end Countermodels

#print axioms ConstraintCover.glue_restricts
#print axioms ConstraintCover.glue_unique
#print axioms ConstraintCover.glue_preserves_complete_constraints
#print axioms ConstraintCover.source_supported_constraint_gluing
#print axioms CompleteKernel.complete_kernel_implies_all_prior_laws
#print axioms CompleteKernel.source_indexed_all_priors_iff_complete_kernel
#print axioms RigidTransport.path_preserves_invariant
#print axioms RigidTransport.invariant_transport_path_independent
#print axioms RigidTransport.invariant_comparisons_are_inverse
#print axioms Countermodels.bit_comparison_involutive
#print axioms Countermodels.bit_comparisons_fail_braid
#print axioms Countermodels.omitted_joint_constraint_blocks_gluing

end ObservationalSUCC.NoGhost
