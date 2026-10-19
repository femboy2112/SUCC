import EODCS_RelationalChoice
/-!
# Source-relational descent extension (2026-10-19)

This imports the hash-frozen EODCS III kernel as-is. Do not change its bytes.
The appended theorems strengthen image-local support transport without AC,
exhibit exact off-image/fiber failures, and establish the existential
left-adjoint property of MayReport. Compiled by the dedicated module gate.
-/
namespace ObservationalSUCC
universe u v w z
/-!
## EODCS IV: choice-free relational descent (2026-10-19)

This strengthens the earlier classical representative-selector construction.
No surjectivity or choice is needed to construct a RELATION on reports:
the existential source pushforward (MayReport) already does the job.
The comparison law is asserted only on realized q(s) observations.

For reports outside image(q), MayReport is empty while CommonPossible
is vacuously true. This prevents silently globalizing image-local claims.
Theorems here use no `classical` tactic or `Classical.choose`.
-/

/-- Exact successor-support descent through an observation quotient without
choice and without surjectivity; construction is the existing MayReport. -/
theorem support_transition_exists_choice_free
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (invariant : SupportCompatible q next qNext) :
    ∃ V : O → P → Prop,
      ∀ s p, V (q s) p ↔ FutureSupport next qNext s p := by
  refine ⟨MayReport q next qNext, ?_⟩
  intro s p
  constructor
  · rintro ⟨t, same, support⟩
    exact (invariant t s same p).mp support
  · intro support
    exact ⟨s, rfl, support⟩

/-- The source-indexed RELATIONAL descent theorem has no global-choice
or source-surjectivity premise. This is not a deterministic selector. -/
theorem support_transport_iff_fiber_invariance_choice_free
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P) :
    (∃ V : O → P → Prop,
        ∀ s p, V (q s) p ↔ FutureSupport next qNext s p) ↔
      SupportCompatible q next qNext := by
  constructor
  · rintro ⟨V, square⟩
    exact support_transition_requires_fiber_invariance q next qNext V square
  · intro invariant
    exact support_transition_exists_choice_free q next qNext invariant

/-- Tight may/common-possible bounds agree on the OBSERVED image under
fiber invariance, even if unreachable reports exist in O. -/
theorem exact_envelopes_on_image_choice_free
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (invariant : SupportCompatible q next qNext) :
    ∀ s p, MayReport q next qNext (q s) p ↔
      CommonPossible q next qNext (q s) p := by
  intro s p
  constructor
  · rintro ⟨t, same, support⟩ x eqx
    exact (invariant t x (same.trans eqx.symm) p).mp support
  · intro common
    exact ⟨s, rfl, common s rfl⟩

/-- Outside image(q), existential may-support is false and the universal
common-possible relation is true by empty quantification. Hence
unrestricted equality of envelopes needs an image/inhabitation hypothesis. -/
theorem empty_observation_fiber_separates_envelopes
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (o : O) (p : P)
    (unreachable : ∀ s : S, q s ≠ o) :
    ¬ MayReport q next qNext o p ∧
      CommonPossible q next qNext o p := by
  constructor
  · rintro ⟨s, same, _⟩
    exact unreachable s same
  · intro s same
    exact False.elim (unreachable s same)


/-- A concrete discordant source-fiber pair blocks ANY report-level
successor-support relation. This is an exact obstruction witness, not a
global undecidability theorem or an empirical source identity test. -/
theorem fiber_disagreement_refutes_relational_descent
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (different : ∃ s t : S, ∃ p : P,
      q s = q t ∧ FutureSupport next qNext s p ∧
      ¬ FutureSupport next qNext t p) :
    ¬ (∃ V : O → P → Prop,
        ∀ s p, V (q s) p ↔ FutureSupport next qNext s p) := by
  intro descended
  have invariant : SupportCompatible q next qNext :=
    (support_transport_iff_fiber_invariance_choice_free q next qNext).mp
      descended
  obtain ⟨s, t, p, same, yes, no⟩ := different
  exact no ((invariant s t same p).mp yes)


/-- The existential direct image MayReport is left adjoint, in the
pointwise implication order on report predicates, to precomposition by
q. This is the precise categorical universal property of relation-valued
source pushforward, constructively proved without AC/LEM/surjectivity. -/
theorem may_report_left_adjunction
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (upper : O → P → Prop) :
    (∀ o p, MayReport q next qNext o p → upper o p) ↔
      (∀ s p, FutureSupport next qNext s p → upper (q s) p) := by
  constructor
  · intro bound s p support
    exact bound (q s) p ⟨s, rfl, support⟩
  · intro pointwise o p
    rintro ⟨s, same, support⟩
    cases same
    exact pointwise s p support
end ObservationalSUCC
