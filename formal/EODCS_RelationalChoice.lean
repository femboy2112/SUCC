/-!
# EODCS III — Set-valued source transport and observable choice

A source transition need not be functional: from state s it may admit
multiple successor states. This is a mathematical possibility relation,
NOT an inferred probability distribution or a physical branching event.

The target of the observable update is then a subset of reports,
represented by a predicate P → Prop. A valid observational transition
exists precisely when the *entire observable successor support* is
constant on each fiber of the old observation.

Lean 4.14, no mathlib, no sorry/admit/axioms. Physical-source access,
empirical calibration and possibility-vs-probability remain independent.
-/
namespace ObservationalSUCC

universe u v w z

def FutureSupport {S : Type u} {T : Type v} {P : Type w}
    (next : S → T → Prop) (qNext : T → P)
    (s : S) (p : P) : Prop :=
  ∃ t : T, next s t ∧ qNext t = p

def SupportCompatible {S : Type u} {O : Type v}
    {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P) : Prop :=
  ∀ s t : S, q s = q t →
    ∀ p : P,
      (FutureSupport next qNext s p ↔ FutureSupport next qNext t p)

theorem support_transition_requires_fiber_invariance
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (V : O → P → Prop)
    (square : ∀ s p, V (q s) p ↔ FutureSupport next qNext s p) :
    SupportCompatible q next qNext := by
  intro s t h p
  calc
    FutureSupport next qNext s p ↔ V (q s) p := (square s p).symm
    _ ↔ V (q t) p := by rw [h]
    _ ↔ FutureSupport next qNext t p := square t p

theorem support_transition_exists_of_fiber_invariance
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o)
    (invariant : SupportCompatible q next qNext) :
    ∃ V : O → P → Prop,
      ∀ s p, V (q s) p ↔ FutureSupport next qNext s p := by
  classical
  let pick : O → S := fun o => Classical.choose (surj o)
  have hs (o : O) : q (pick o) = o :=
    Classical.choose_spec (surj o)
  refine ⟨fun o p => FutureSupport next qNext (pick o) p, ?_⟩
  intro s p
  exact invariant (pick (q s)) s (hs (q s)) p

theorem support_transport_iff_fiber_invariance
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o) :
    (∃ V : O → P → Prop,
        ∀ s p, V (q s) p ↔ FutureSupport next qNext s p) ↔
      SupportCompatible q next qNext := by
  constructor
  · rintro ⟨V, square⟩
    exact support_transition_requires_fiber_invariance q next qNext V square
  · intro invariant
    exact support_transition_exists_of_fiber_invariance q next qNext
      surj invariant

/-- A set-valued transition is representable by a deterministic OBSERVED
output if all successor states have the same qNext report and the
successor relation is inhabited. The source next may remain nondeterministic. -/
theorem unique_future_report_of_nonempty_singleton_support
    {S : Type u} {T : Type v} {P : Type w}
    (next : S → T → Prop) (qNext : T → P)
    (s : S)
    (nonempty : ∃ t, next s t)
    (constant : ∀ t u, next s t → next s u → qNext t = qNext u) :
    ∃ p : P,
      FutureSupport next qNext s p ∧
      ∀ p' : P, FutureSupport next qNext s p' → p' = p := by
  obtain ⟨witness, hw⟩ := nonempty
  refine ⟨qNext witness, ⟨witness, hw, rfl⟩, ?_⟩
  intro p' hp'
  obtain ⟨t, ht, report⟩ := hp'
  exact report.symm.trans (constant t witness ht hw)

/-- The canonical augmented report (q(s), observable successor support)
is the coarsest mathematically sufficient refinement of q that
can determine the full set-valued successor law. -/
theorem support_pair_universal
    {S : Type u} {A : Type v} {O : Type w} {P : Type z}
    (q : S → O) (support : S → P → Prop)
    (alternative : S → A)
    (decodeOld : A → O) (decodeNext : A → P → Prop)
    (old : ∀ s, decodeOld (alternative s) = q s)
    (future : ∀ s p, decodeNext (alternative s) p ↔ support s p) :
    ∃ F : A → O × (P → Prop),
      ∀ s : S,
        F (alternative s) = (q s, support s) := by
  classical
  refine ⟨fun a => (decodeOld a, decodeNext a), ?_⟩
  intro s
  apply Prod.ext
  · exact old s
  · funext p
    exact propext (future s p)


/-- The tight existential ("may") abstraction of successor reports
over all original states with the same present observation o. -/
def MayReport {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (o : O) (p : P) : Prop :=
  ∃ s : S, q s = o ∧ FutureSupport next qNext s p

/-- The common-possibility ("possible at every hidden state") lower bound.
This is NOT "p must occur": it means p belongs to every hidden state's
successor support. The must-occur proposition is instead that the entire
may support satisfies a claimed predicate. -/
def CommonPossible {S : Type u} {O : Type v}
    {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (o : O) (p : P) : Prop :=
  ∀ s : S, q s = o → FutureSupport next qNext s p

theorem source_support_bounded_by_may_common
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (s : S) (p : P) :
    CommonPossible q next qNext (q s) p →
    FutureSupport next qNext s p ∧
    MayReport q next qNext (q s) p := by
  intro common
  have membership : FutureSupport next qNext s p :=
    common s rfl
  exact ⟨membership,⟨s,rfl,membership⟩⟩

/-- If supports are fiber-invariant, then upper and lower approximations
coincide on every observation in the source's image. -/
theorem support_invariant_implies_exact_envelopes
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o)
    (invariant : SupportCompatible q next qNext) :
    ∀ o p, MayReport q next qNext o p ↔
      CommonPossible q next qNext o p := by
  intro o p
  constructor
  · rintro ⟨s, hs, supp⟩ t ht
    exact (invariant s t (hs.trans ht.symm) p).mp supp
  · intro common
    obtain ⟨s,hs⟩ := surj o
    exact ⟨s,hs,common s hs⟩

/-- This equivalence exactly diagnoses the source-relative obstruction:
may/must-common overlap collapses to a single support law iff the entire
successor support descends through the observation quotient. -/
theorem exact_envelopes_iff_support_transport
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o) :
    (∀ o p, MayReport q next qNext o p ↔
      CommonPossible q next qNext o p) ↔
      SupportCompatible q next qNext := by
  constructor
  · intro equal s t same p
    constructor
    · intro sp
      have may : MayReport q next qNext (q s) p :=
        ⟨s,rfl,sp⟩
      exact ((equal (q s) p).mp may) t same.symm
    · intro tp
      have may : MayReport q next qNext (q t) p :=
        ⟨t,rfl,tp⟩
      exact ((equal (q t) p).mp may) s same
  · exact support_invariant_implies_exact_envelopes q next qNext surj

/-- The may set is the least sound overapproximation at each report:
any output predicate containing every source support must contain May. -/
theorem may_is_least_sound_overapproximation
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (upper : O → P → Prop)
    (sound : ∀ s p, FutureSupport next qNext s p → upper (q s) p) :
    ∀ o p, MayReport q next qNext o p → upper o p := by
  intro o p
  rintro ⟨s,hs,supp⟩
  rw [← hs]
  exact sound s p supp

/-- The common possible set is the largest sound underapproximation:
any output predicate lying inside *every* source support lies inside it. -/
theorem common_is_greatest_sound_underapproximation
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (next : S → T → Prop) (qNext : T → P)
    (lower : O → P → Prop)
    (sound : ∀ s p, lower (q s) p → FutureSupport next qNext s p) :
    ∀ o p, lower o p → CommonPossible q next qNext o p := by
  intro o p low s hs
  rw [← hs] at low
  exact sound s p low

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

end ObservationalSUCC
