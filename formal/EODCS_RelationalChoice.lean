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

end ObservationalSUCC
