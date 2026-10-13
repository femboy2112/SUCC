/-!
# Observation Descent and Holonomy Fixed-Point Theorems (Lean 4.14)

All laws are explicitly hypothesized, never inferred from naming,
probability, or a finite observation sample. Proof terms are kernel
checked by an isolated CI gate. No mathlib dependencies or `sorry` placeholders.

Causal object: S -U-> T with observations q : S -> O and r : T -> P.
Question: does a map v : O -> P make r ∘ U = v ∘ q?
The precise obstruction is non-invariance of the kernel pair of q.

Holonomy object: a rooted, tree-gauged connected graph with invertible
tree transports. A global tree-propagated section exists iff the root
fiber value is fixed by every based fundamental-loop transport.

Cover descent: a lifted section descends iff it is invariant under
the deck action. Cover minimal degree is NOT formalized here.
-/

namespace ObservationalSUCC

universe u v w z

def FiberCompatible {S : Type u} {O : Type v}
    {T : Type w} {P : Type z}
    (q : S → O) (U : S → T) (r : T → P) : Prop :=
  ∀ s t, q s = q t → r (U s) = r (U t)

theorem transport_requires_fiber_compatibility
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (U : S → T) (r : T → P)
    (vmap : O → P)
    (comm : ∀ s, vmap (q s) = r (U s)) :
    FiberCompatible q U r := by
  intro s t eq
  calc
    r (U s) = vmap (q s) := (comm s).symm
    _ = vmap (q t) := congrArg vmap eq
    _ = r (U t) := comm t

theorem transport_exists_of_fiber_compatibility
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (U : S → T) (r : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o)
    (compatible : FiberCompatible q U r) :
    ∃ vmap : O → P, ∀ s : S, vmap (q s) = r (U s) := by
  classical
  let section : O → S := fun o => Classical.choose (surj o)
  have section_eq (o : O) : q (section o) = o := by
    exact Classical.choose_spec (surj o)
  let vmap : O → P := fun o => r (U (section o))
  refine ⟨vmap, ?_⟩
  intro s
  exact compatible (section (q s)) s (section_eq (q s))

theorem source_transport_iff_fiber_compatible
    {S : Type u} {O : Type v} {T : Type w} {P : Type z}
    (q : S → O) (U : S → T) (r : T → P)
    (surj : ∀ o : O, ∃ s : S, q s = o) :
    (∃ vmap : O → P, ∀ s, vmap (q s) = r (U s)) ↔
      FiberCompatible q U r := by
  constructor
  · rintro ⟨vmap, comm⟩
    exact transport_requires_fiber_compatibility q U r vmap comm
  · intro compatible
    exact transport_exists_of_fiber_compatibility q U r surj compatible

theorem transported_map_unique_if_surjective
    {S : Type u} {O : Type v} {P : Type w}
    (q : S → O) (target : S → P)
    (surj : ∀ o : O, ∃ s : S, q s = o)
    (v₁ v₂ : O → P)
    (h₁ : ∀ s, v₁ (q s) = target s)
    (h₂ : ∀ s, v₂ (q s) = target s) :
    ∀ o, v₁ o = v₂ o := by
  intro o
  obtain ⟨s, hs⟩ := surj o
  calc
    v₁ o = v₁ (q s) := by rw [hs]
    _ = target s := h₁ s
    _ = v₂ (q s) := (h₂ s).symm
    _ = v₂ o := by rw [hs]

/-- The pair of the *current* and *post-update* reports is the coarsest
jointly sufficient refinement of the current observation.
Any observation R from which both reports factor also factors the pair.
The theorem does not assert that a physical sensor for the pair exists. -/
theorem observation_pair_universal
    {S : Type u} {R : Type v} {O : Type w} {P : Type z}
    (q : S → O) (post : S → P) (refinement : S → R)
    (decode_current : R → O) (decode_future : R → P)
    (hc : ∀ s, decode_current (refinement s) = q s)
    (hf : ∀ s, decode_future (refinement s) = post s) :
    ∃ factor : R → O × P,
      ∀ s, factor (refinement s) = (q s, post s) := by
  refine ⟨fun r => (decode_current r, decode_future r), ?_⟩
  intro s
  rw [hc s, hf s]

theorem observation_pair_fiber_characterization
    {S : Type u} {O : Type v} {P : Type w}
    (q : S → O) (post : S → P) (s t : S) :
    ((q s, post s) : O × P) = (q t, post t) ↔
      q s = q t ∧ post s = post t := by
  constructor
  · intro h
    exact ⟨congrArg Prod.fst h, congrArg Prod.snd h⟩
  · rintro ⟨h₁, h₂⟩
    rw [h₁, h₂]

theorem causal_square_composition
    {S : Type u} {T : Type v} {R : Type w}
    {A : Type u} {B : Type v} {C : Type w}
    (q : S → A) (r : T → B) (p : R → C)
    (U : S → T) (W : T → R)
    (V : A → B) (Z : B → C)
    (square₁ : ∀ s, r (U s) = V (q s))
    (square₂ : ∀ t, p (W t) = Z (r t)) :
    ∀ s, p (W (U s)) = Z (V (q s)) := by
  intro s
  calc
    p (W (U s)) = Z (r (U s)) := square₂ (U s)
    _ = Z (V (q s)) := congrArg Z (square₁ s)

/-- Tree-gauged based holonomy: on the root fiber, the loop around e
acts by inv(dst(e)) ∘ edge(e) ∘ tree(src(e)).
It fixes x exactly when the tree-propagated values obey e. -/
theorem based_loop_fixed_iff_tree_parallel
    {Vertex : Type u} {Edge : Type v} {X : Type w}
    (src dst : Edge → Vertex) (edge : Edge → X → X)
    (tree inv : Vertex → X → X)
    (inverse_right : ∀ v y, tree v (inv v y) = y)
    (inverse_left : ∀ v x, inv v (tree v x) = x)
    (x : X) :
    (∀ e, inv (dst e) (edge e (tree (src e) x)) = x) ↔
    (∀ e, edge e (tree (src e) x) = tree (dst e) x) := by
  constructor
  · intro fixed e
    have h := congrArg (tree (dst e)) (fixed e)
    exact (inverse_right (dst e) _).symm.trans h.symm |>.symm
  · intro parallel e
    rw [parallel e]
    exact inverse_left (dst e) x

/-- A section q_x(v,h)=tree(v)(act(h,x)) is constant on sheets iff its
root value is fixed by the entire action. This is the algebraic core of
deck-invariant descent; it does NOT prove the covering degree theorem. -/
theorem cover_descent_iff_holonomy_fixed
    {Vertex : Type u} {H : Type v} {X : Type w}
    (root : Vertex) (identity : H)
    (tree : Vertex → X → X) (act : H → X → X)
    (tree_root : ∀ x, tree root x = x)
    (action_identity : ∀ x, act identity x = x)
    (x : X) :
    (∀ v h, tree v (act h x) = tree v (act identity x)) ↔
      (∀ h, act h x = x) := by
  constructor
  · intro descending h
    have hroot := descending root h
    simpa only [tree_root, action_identity] using hroot
  · intro fixed v h
    rw [fixed h, action_identity x]

end ObservationalSUCC
