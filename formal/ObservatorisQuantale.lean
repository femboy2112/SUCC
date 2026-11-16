/-!
# Weighted ancestral reachability under an observation quotient

Standalone Lean 4.14.0, with no domain-library imports.

`formal/PrincipiaAncestral.lean` treats Boolean reachability.  This file
replaces truth values by an arbitrary value structure `K` with a preorder,
arbitrary suprema, a multiplication and a unit, assuming ONLY the inequalities
listed in `LaxQuantale`.  Every unital quantale satisfies them (commutativity,
antisymmetry and the reverse inequalities are never used), so the results hold
in particular for

* truth values: reachability (the instance `propQ` below; `star_propQ_iff`),
* `([0,∞], ≥, +)`: least cost / shortest time,
* `([0,∞], ≤, ·)` and `(max, min)`: best-path relevance and bottleneck,
* sets of words of a monoid: path languages (trace-level statements).

Enriched closure, Yoneda-style characterisations and may/must abstraction are
classical.  The assembly — the four-way exactness criterion over an arbitrary
value structure, its selected-start form and the must-side bound — is a
new-to-project elementary synthesis; no scholarly novelty is claimed.  A
successful compilation proves these encoded statements relative to their
axiom dependencies.  It does not authenticate any source model, and it says
nothing about signed (non-idempotent) weights, where cancellation occurs.
-/

set_option autoImplicit false

namespace ObservationalSUCC.ObservatorisQuantale

universe u v w

/-- The inequalities actually used.  Every unital quantale is an instance. -/
structure LaxQuantale (V : Type u) where
  le : V → V → Prop
  mul : V → V → V
  one : V
  sSup : (V → Prop) → V
  le_refl : ∀ a, le a a
  le_trans : ∀ {a b c}, le a b → le b c → le a c
  le_sSup : ∀ {S : V → Prop} {a}, S a → le a (sSup S)
  sSup_le : ∀ {S : V → Prop} {b}, (∀ a, S a → le a b) → le (sSup S) b
  mul_mono : ∀ {a b c d}, le a b → le c d → le (mul a c) (mul b d)
  mul_sSup_le : ∀ (a : V) (S : V → Prop),
    le (mul a (sSup S)) (sSup (fun t => ∃ s, S s ∧ t = mul a s))
  sSup_mul_le : ∀ (S : V → Prop) (a : V),
    le (mul (sSup S) a) (sSup (fun t => ∃ s, S s ∧ t = mul s a))
  mul_assoc_le : ∀ a b c, le (mul a (mul b c)) (mul (mul a b) c)
  mul_assoc_ge : ∀ a b c, le (mul (mul a b) c) (mul a (mul b c))
  mul_one_le : ∀ a, le (mul a one) a
  le_mul_one : ∀ a, le a (mul a one)
  le_one_mul : ∀ a, le a (mul one a)

section Core

variable {V : Type u} {X : Type v} {Y : Type w}

/-- Weights of finite paths from a fixed start; the empty path has weight `one`. -/
inductive PathW (K : LaxQuantale V) (R : X → X → V) (x : X) : X → V → Prop where
  | refl : PathW K R x x K.one
  | tail {y z : X} {p : V} : PathW K R x y p → PathW K R x z (K.mul p (R y z))

/-- Weighted reflexive-transitive closure: the supremum of all path weights. -/
def star (K : LaxQuantale V) (R : X → X → V) (x z : X) : V :=
  K.sSup (PathW K R x z)

/-- A `V`-valued hereditary predicate (a potential). -/
def Closed (K : LaxQuantale V) (R : X → X → V) (φ : X → V) : Prop :=
  ∀ u v, K.le (K.mul (φ u) (R u v)) (φ v)

/-- Existential ("may") observation relation. -/
def quot (K : LaxQuantale V) (R : X → X → V) (q : X → Y) (a b : Y) : V :=
  K.sSup (fun r => ∃ u v, q u = a ∧ q v = b ∧ r = R u v)

/-- Universal ("must") observation relation: the meet over the source fibre,
written as the supremum of the common lower bounds. -/
def quotAll (K : LaxQuantale V) (R : X → X → V) (q : X → Y) (a b : Y) : V :=
  K.sSup (fun t => ∀ u, q u = a →
    K.le t (K.sSup (fun r => ∃ v, q v = b ∧ r = R u v)))

/-- Direct image of a potential along the observation. -/
def push (K : LaxQuantale V) (q : X → Y) (φ : X → V) (b : Y) : V :=
  K.sSup (fun t => ∃ u, q u = b ∧ t = φ u)

variable (K : LaxQuantale V)

theorem path_mul_le_of_closed {R : X → X → V} {φ : X → V}
    (hφ : Closed K R φ) {x z : X} {p : V} (path : PathW K R x z p) :
    K.le (K.mul (φ x) p) (φ z) := by
  induction path with
  | refl => exact K.mul_one_le _
  | tail _ ih =>
      exact K.le_trans (K.mul_assoc_le _ _ _)
        (K.le_trans (K.mul_mono ih (K.le_refl _)) (hφ _ _))

/-- A potential propagates along the whole weighted closure. -/
theorem closed_star {R : X → X → V} {φ : X → V} (hφ : Closed K R φ) (x z : X) :
    K.le (K.mul (φ x) (star K R x z)) (φ z) := by
  refine K.le_trans (K.mul_sSup_le _ _) (K.sSup_le ?_)
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro path e => subst e; exact path_mul_le_of_closed K hφ path

theorem one_le_star (R : X → X → V) (x : X) : K.le K.one (star K R x x) :=
  K.le_sSup PathW.refl

theorem edge_le_star (R : X → X → V) (s t : X) : K.le (R s t) (star K R s t) :=
  K.le_trans (K.le_one_mul _) (K.le_sSup (PathW.tail PathW.refl))

/-- The closure from a fixed start is itself a potential. -/
theorem star_closed (R : X → X → V) (x : X) : Closed K R (star K R x) := by
  intro u v
  refine K.le_trans (K.sSup_mul_le _ _) (K.sSup_le ?_)
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro path e => subst e; exact K.le_sSup (PathW.tail path)

theorem path_le_of_closed {R : X → X → V} {φ : X → V} (hφ : Closed K R φ)
    {x z : X} (initial : K.le K.one (φ x)) {p : V} (path : PathW K R x z p) :
    K.le p (φ z) := by
  induction path with
  | refl => exact initial
  | tail _ ih => exact K.le_trans (K.mul_mono ih (K.le_refl _)) (hφ _ _)

/-- **Weighted PAP-01.**  The closure from `x` is the least potential whose
value at `x` dominates the unit.  Together with `star_closed` and
`one_le_star` this characterises `star K R x` up to the preorder. -/
theorem star_le_of_closed {R : X → X → V} {φ : X → V} (hφ : Closed K R φ)
    {x : X} (initial : K.le K.one (φ x)) (z : X) :
    K.le (star K R x z) (φ z) :=
  K.sSup_le (fun _ path => path_le_of_closed K hφ initial path)

theorem edge_le_quot (R : X → X → V) (q : X → Y) (u v : X) :
    K.le (R u v) (quot K R q (q u) (q v)) :=
  K.le_sSup ⟨u, v, rfl, rfl, rfl⟩

/-- **Weighted PAP-02.**  The observation quotient never under-reports a
source connection: source closure is bounded by quotient closure. -/
theorem star_le_quot_star (R : X → X → V) (q : X → Y) (x z : X) :
    K.le (star K R x z) (star K (quot K R q) (q x) (q z)) := by
  refine star_le_of_closed K (φ := fun z => star K (quot K R q) (q x) (q z)) ?_
    (one_le_star K _ _) z
  intro u v
  exact K.le_trans (K.mul_mono (K.le_refl _) (edge_le_quot K R q u v))
    (star_closed K (quot K R q) (q x) (q u) (q v))

theorem le_push (q : X → Y) (φ : X → V) (u : X) :
    K.le (φ u) (push K q φ (q u)) :=
  K.le_sSup ⟨u, rfl, rfl⟩

theorem push_star_le_quot_star (R : X → X → V) (q : X → Y) (x : X) (b : Y) :
    K.le (push K q (star K R x) b) (star K (quot K R q) (q x) b) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro u hu =>
      cases hu with
      | intro e1 e2 => subst e1; subst e2; exact star_le_quot_star K R q x u

/-- Selected-start exactness: no quotient endpoint value is invented. -/
def ExactAt (R : X → X → V) (q : X → Y) (x : X) : Prop :=
  ∀ b, K.le (star K (quot K R q) (q x) b) (push K q (star K R x) b)

def EndpointExact (R : X → X → V) (q : X → Y) : Prop :=
  ∀ x, ExactAt K R q x

def FibreConstant (R : X → X → V) (q : X → Y) : Prop :=
  ∀ x x', q x = q x' → ∀ b,
    K.le (push K q (star K R x) b) (push K q (star K R x') b)

def PushClosed (R : X → X → V) (q : X → Y) : Prop :=
  ∀ φ, Closed K R φ → Closed K (quot K R q) (push K q φ)

def SatClosed (R : X → X → V) (q : X → Y) : Prop :=
  ∀ φ, Closed K R φ → Closed K R (fun s => push K q φ (q s))

/-- If the saturation of one potential is a source potential, then its direct
image is a quotient potential.  No hypothesis on the potential is needed. -/
theorem push_closed_of_sat_closed (R : X → X → V) (q : X → Y) (φ : X → V)
    (h : Closed K R (fun s => push K q φ (q s))) :
    Closed K (quot K R q) (push K q φ) := by
  intro a b
  refine K.le_trans (K.mul_sSup_le _ _) (K.sSup_le ?_)
  intro t ht
  cases ht with
  | intro r hr =>
      cases hr with
      | intro hr e =>
          cases hr with
          | intro u hu =>
              cases hu with
              | intro v hv =>
                  cases hv with
                  | intro ha hv =>
                      cases hv with
                      | intro hb er =>
                          subst e; subst er; subst ha; subst hb
                          exact h u v

theorem exactAt_of_push_closed (R : X → X → V) (q : X → Y) (x : X)
    (h : Closed K (quot K R q) (push K q (star K R x))) : ExactAt K R q x :=
  fun b => star_le_of_closed K h
    (K.le_trans (one_le_star K R x) (le_push K q (star K R x) x)) b

/-- **Selected-start criterion (weighted form of PAP-03, equation (5)).** -/
theorem exactAt_iff_saturated_star_closed (R : X → X → V) (q : X → Y) (x : X) :
    ExactAt K R q x ↔ Closed K R (fun s => push K q (star K R x) (q s)) := by
  constructor
  · intro exact s t
    have h1 : K.le (push K q (star K R x) (q s))
        (star K (quot K R q) (q x) (q s)) := push_star_le_quot_star K R q x (q s)
    exact K.le_trans (K.mul_mono h1 (edge_le_quot K R q s t))
      (K.le_trans (star_closed K (quot K R q) (q x) (q s) (q t)) (exact (q t)))
  · intro h
    exact exactAt_of_push_closed K R q x (push_closed_of_sat_closed K R q _ h)

theorem fibreConstant_of_exact (R : X → X → V) (q : X → Y)
    (h : EndpointExact K R q) : FibreConstant K R q := by
  intro x x' e b
  have h1 := push_star_le_quot_star K R q x b
  rw [e] at h1
  exact K.le_trans h1 (h x' b)

theorem satClosed_of_fibreConstant (R : X → X → V) (q : X → Y)
    (h : FibreConstant K R q) : SatClosed K R q := by
  intro φ hφ s t
  refine K.le_trans (K.sSup_mul_le _ _) (K.sSup_le ?_)
  intro t' ht'
  cases ht' with
  | intro a ha =>
      cases ha with
      | intro ha e =>
          cases ha with
          | intro u hu =>
              cases hu with
              | intro hu ea =>
                  subst e; subst ea
                  have h1 : K.le (R s t) (push K q (star K R u) (q t)) :=
                    K.le_trans (edge_le_star K R s t)
                      (K.le_trans (le_push K q (star K R s) t)
                        (h s u hu.symm (q t)))
                  have h2 : K.le (K.mul (φ u) (push K q (star K R u) (q t)))
                      (push K q φ (q t)) := by
                    refine K.le_trans (K.mul_sSup_le _ _) (K.sSup_le ?_)
                    intro t'' ht''
                    cases ht'' with
                    | intro c hc =>
                        cases hc with
                        | intro hc e' =>
                            cases hc with
                            | intro v hv =>
                                cases hv with
                                | intro hv ec =>
                                    subst e'; subst ec
                                    have h3 := le_push K q φ v
                                    rw [hv] at h3
                                    exact K.le_trans (closed_star K hφ u v) h3
                  exact K.le_trans (K.mul_mono (K.le_refl _) h1) h2

theorem pushClosed_of_satClosed (R : X → X → V) (q : X → Y)
    (h : SatClosed K R q) : PushClosed K R q :=
  fun φ hφ => push_closed_of_sat_closed K R q φ (h φ hφ)

theorem exact_of_pushClosed (R : X → X → V) (q : X → Y)
    (h : PushClosed K R q) : EndpointExact K R q :=
  fun x => exactAt_of_push_closed K R q x (h _ (star_closed K R x))

/-- **Weighted PAP-03.**  All-start endpoint exactness, fibre-constancy of
pushed-forward closures, preservation of potentials by direct image and by
saturation are equivalent over every value structure satisfying
`LaxQuantale`. -/
theorem exact_iff_fibreConstant (R : X → X → V) (q : X → Y) :
    EndpointExact K R q ↔ FibreConstant K R q :=
  ⟨fibreConstant_of_exact K R q, fun h =>
    exact_of_pushClosed K R q
      (pushClosed_of_satClosed K R q (satClosed_of_fibreConstant K R q h))⟩

theorem exact_iff_satClosed (R : X → X → V) (q : X → Y) :
    EndpointExact K R q ↔ SatClosed K R q :=
  ⟨fun h => satClosed_of_fibreConstant K R q (fibreConstant_of_exact K R q h),
   fun h => exact_of_pushClosed K R q (pushClosed_of_satClosed K R q h)⟩

theorem exact_iff_pushClosed (R : X → X → V) (q : X → Y) :
    EndpointExact K R q ↔ PushClosed K R q :=
  ⟨fun h => pushClosed_of_satClosed K R q
      (satClosed_of_fibreConstant K R q (fibreConstant_of_exact K R q h)),
   exact_of_pushClosed K R q⟩

/-- Every source edge is realised, up to its weight, by the closure from EVERY
representative of its start report: "one-step may is below closure must". -/
def EdgeRealised (R : X → X → V) (q : X → Y) : Prop :=
  ∀ u v x', q x' = q u → K.le (R u v) (push K q (star K R x') (q v))

/-- **A fifth form of exactness** (found on paper by the delegated quotient
geometry workstream, formalised here): all-start exactness holds iff every
source edge is realised from every representative of its start report. -/
theorem exact_iff_edgeRealised (R : X → X → V) (q : X → Y) :
    EndpointExact K R q ↔ EdgeRealised K R q := by
  constructor
  · intro h u v x' e
    exact K.le_trans (edge_le_star K R u v)
      (K.le_trans (le_push K q (star K R u) v)
        (fibreConstant_of_exact K R q h u x' e.symm (q v)))
  · intro h x
    refine exactAt_of_push_closed K R q x ?_
    intro a b
    refine K.le_trans (K.mul_sSup_le _ _) (K.sSup_le ?_)
    intro t ht
    cases ht with
    | intro r hr =>
        cases hr with
        | intro hr e =>
            cases hr with
            | intro u hu =>
                cases hu with
                | intro v hv =>
                    cases hv with
                    | intro ha hv =>
                        cases hv with
                        | intro hb er =>
                            subst e; subst er; subst ha; subst hb
                            refine K.le_trans (K.sSup_mul_le _ _) (K.sSup_le ?_)
                            intro t' ht'
                            cases ht' with
                            | intro s hs =>
                                cases hs with
                                | intro hs e' =>
                                    cases hs with
                                    | intro z hz =>
                                        cases hz with
                                        | intro hz es =>
                                            subst e'; subst es
                                            refine K.le_trans
                                              (K.mul_mono (K.le_refl _) (h u v z hz)) ?_
                                            refine K.le_trans (K.mul_sSup_le _ _)
                                              (K.sSup_le ?_)
                                            intro t'' ht''
                                            cases ht'' with
                                            | intro c hc =>
                                                cases hc with
                                                | intro hc e'' =>
                                                    cases hc with
                                                    | intro w hw =>
                                                        cases hw with
                                                        | intro hw ec =>
                                                            subst e''; subst ec
                                                            have h3 := le_push K q (star K R x) w
                                                            rw [hw] at h3
                                                            exact K.le_trans
                                                              (closed_star K (star_closed K R x) z w) h3

/-- The direct image of a closure from an actual start is always a potential
for the universal ("must") quotient. -/
theorem push_star_closed_quotAll (R : X → X → V) (q : X → Y) (x : X) :
    Closed K (quotAll K R q) (push K q (star K R x)) := by
  intro a b
  refine K.le_trans (K.sSup_mul_le _ _) (K.sSup_le ?_)
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro hs e =>
          cases hs with
          | intro u hu =>
              cases hu with
              | intro hu es =>
                  subst e; subst es
                  have h1 : K.le (quotAll K R q a b)
                      (K.sSup (fun r => ∃ v, q v = b ∧ r = R u v)) :=
                    K.sSup_le (fun _ ht => ht u hu)
                  refine K.le_trans (K.mul_mono (K.le_refl _) h1) ?_
                  refine K.le_trans (K.mul_sSup_le _ _) (K.sSup_le ?_)
                  intro t' ht'
                  cases ht' with
                  | intro r hr =>
                      cases hr with
                      | intro hr e' =>
                          cases hr with
                          | intro v hv =>
                              cases hv with
                              | intro hv er =>
                                  subst e'; subst er
                                  have h3 := le_push K q (star K R x) v
                                  rw [hv] at h3
                                  exact K.le_trans (star_closed K R x u v) h3

/-- **Must-side bound.**  Every value of the must-quotient closure from an
actual observation is realised by the source from EVERY chosen start in the
fibre.  With `push_star_le_quot_star` this is the two-sided sandwich
`must* ≤ source ≤ may*`. -/
theorem quotAll_star_le_push_star (R : X → X → V) (q : X → Y) (x : X) (b : Y) :
    K.le (star K (quotAll K R q) (q x) b) (push K q (star K R x) b) :=
  star_le_of_closed K (push_star_closed_quotAll K R q x)
    (K.le_trans (one_le_star K R x) (le_push K q (star K R x) x)) b

/-! ## The adjunction between potentials upstairs and downstairs -/

/-- The least potential above an arbitrary `V`-predicate. -/
def closure (R : X → X → V) (ψ : X → V) (b : X) : V :=
  K.sSup (fun t => ∃ a, t = K.mul (ψ a) (star K R a b))

theorem le_closure (R : X → X → V) (ψ : X → V) (b : X) :
    K.le (ψ b) (closure K R ψ b) :=
  K.le_trans (K.le_mul_one _)
    (K.le_trans (K.mul_mono (K.le_refl _) (one_le_star K R b))
      (K.le_sSup ⟨b, rfl⟩))

theorem closure_closed (R : X → X → V) (ψ : X → V) :
    Closed K R (closure K R ψ) := by
  intro u v
  refine K.le_trans (K.sSup_mul_le _ _) (K.sSup_le ?_)
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro hs e =>
          cases hs with
          | intro a ea =>
              subst e; subst ea
              exact K.le_trans (K.mul_assoc_ge _ _ _)
                (K.le_trans (K.mul_mono (K.le_refl _) (star_closed K R a u v))
                  (K.le_sSup ⟨a, rfl⟩))

theorem closure_le_of_closed {R : X → X → V} {ψ : X → V}
    (hψ : Closed K R ψ) (b : X) : K.le (closure K R ψ b) (ψ b) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro a e => subst e; exact closed_star K hψ a b

theorem closure_mono (R : X → X → V) {φ ψ : X → V}
    (h : ∀ a, K.le (φ a) (ψ a)) (b : X) :
    K.le (closure K R φ b) (closure K R ψ b) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro a e =>
      subst e
      exact K.le_trans (K.mul_mono (h a) (K.le_refl _)) (K.le_sSup ⟨a, rfl⟩)

/-- Pulling a quotient potential back along the observation gives a source
potential.  This direction needs no hypothesis on the observation. -/
theorem pullback_closed (R : X → X → V) (q : X → Y) {ψ : Y → V}
    (hψ : Closed K (quot K R q) ψ) : Closed K R (fun u => ψ (q u)) := by
  intro u v
  exact K.le_trans (K.mul_mono (K.le_refl _) (edge_le_quot K R q u v))
    (hψ (q u) (q v))

/-- **The adjunction.**  `L = closure ∘ push` is left adjoint to pullback
`ψ ↦ ψ ∘ q` between predicates upstairs and potentials downstairs. -/
theorem closure_push_adjunction (R : X → X → V) (q : X → Y) (φ : X → V)
    {ψ : Y → V} (hψ : Closed K (quot K R q) ψ) :
    (∀ b, K.le (closure K (quot K R q) (push K q φ) b) (ψ b)) ↔
      (∀ u, K.le (φ u) (ψ (q u))) := by
  constructor
  · intro h u
    exact K.le_trans (le_push K q φ u)
      (K.le_trans (le_closure K (quot K R q) (push K q φ) (q u)) (h (q u)))
  · intro h b
    have h1 : ∀ a, K.le (push K q φ a) (ψ a) := by
      intro a
      refine K.sSup_le ?_
      intro t ht
      cases ht with
      | intro u hu =>
          cases hu with
          | intro e1 e2 => subst e1; subst e2; exact h u
    exact K.le_trans (closure_mono K (quot K R q) h1 b)
      (closure_le_of_closed K hψ b)

/-- The left adjoint sends the source closure from `x` to the quotient closure
from `q x` (one inequality; the other is `quot_star_le_closure_push_star`). -/
theorem closure_push_star_le_quot_star (R : X → X → V) (q : X → Y) (x : X)
    (b : Y) :
    K.le (closure K (quot K R q) (push K q (star K R x)) b)
      (star K (quot K R q) (q x) b) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro a e =>
      subst e
      exact K.le_trans
        (K.mul_mono (push_star_le_quot_star K R q x a) (K.le_refl _))
        (closed_star K (star_closed K (quot K R q) (q x)) a b)

theorem quot_star_le_closure_push_star (R : X → X → V) (q : X → Y) (x : X)
    (b : Y) :
    K.le (star K (quot K R q) (q x) b)
      (closure K (quot K R q) (push K q (star K R x)) b) :=
  K.le_trans (K.le_one_mul _)
    (K.le_trans
      (K.mul_mono (K.le_trans (one_le_star K R x) (le_push K q (star K R x) x))
        (K.le_refl _))
      (K.le_sSup ⟨q x, rfl⟩))

/-- **Exactness is the vanishing of the ghost defect.**  The selected start is
exact precisely when the left adjoint adds nothing to the direct image of its
closure, i.e. when that direct image is already a quotient potential. -/
theorem exactAt_iff_closure_push_le (R : X → X → V) (q : X → Y) (x : X) :
    ExactAt K R q x ↔
      ∀ b, K.le (closure K (quot K R q) (push K q (star K R x)) b)
        (push K q (star K R x) b) := by
  constructor
  · intro h b
    exact K.le_trans (closure_push_star_le_quot_star K R q x b) (h b)
  · intro h b
    exact K.le_trans (quot_star_le_closure_push_star K R q x b) (h b)

/-! ## Exactness as commutation of two closure operators

`closure K R` is the dynamical closure (what the carrier can reach) and
`sat K q` is the observational closure (what the observer cannot separate).
All-start exactness holds precisely when "evolve, then blur" is already
idempotent, i.e. is itself a closure operator. -/

/-- Saturation: the observational closure of a predicate. -/
def sat (q : X → Y) (φ : X → V) (u : X) : V := push K q φ (q u)

theorem le_sat (q : X → Y) (φ : X → V) (u : X) : K.le (φ u) (sat K q φ u) :=
  le_push K q φ u

theorem sat_mono (q : X → Y) {φ φ' : X → V} (h : ∀ u, K.le (φ u) (φ' u))
    (u : X) : K.le (sat K q φ u) (sat K q φ' u) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro e1 e2 =>
          subst e2
          exact K.le_trans (h s) (K.le_sSup ⟨s, e1, rfl⟩)

theorem sat_idem (q : X → Y) (φ : X → V) (u : X) :
    K.le (sat K q (sat K q φ) u) (sat K q φ u) := by
  refine K.sSup_le ?_
  intro t ht
  cases ht with
  | intro s hs =>
      cases hs with
      | intro e1 e2 =>
          subst e2
          show K.le (push K q φ (q s)) (push K q φ (q u))
          rw [e1]
          exact K.le_refl _

theorem closed_of_closure_le {R : X → X → V} {φ : X → V}
    (h : ∀ b, K.le (closure K R φ b) (φ b)) : Closed K R φ := by
  intro u v
  exact K.le_trans (K.mul_mono (le_closure K R φ u) (K.le_refl _))
    (K.le_trans (closure_closed K R φ u v) (h v))

/-- **Exactness ⇔ `sat ∘ closure` is idempotent.** -/
theorem satClosed_iff_sat_closure_idempotent (R : X → X → V) (q : X → Y) :
    SatClosed K R q ↔
      ∀ (φ : X → V) (u : X),
        K.le (sat K q (closure K R (sat K q (closure K R φ))) u)
          (sat K q (closure K R φ) u) := by
  constructor
  · intro h φ u
    have closedSat : Closed K R (sat K q (closure K R φ)) :=
      h _ (closure_closed K R φ)
    exact K.le_trans
      (sat_mono K q (fun b => closure_le_of_closed K closedSat b) u)
      (sat_idem K q (closure K R φ) u)
  · intro h φ hφ
    refine closed_of_closure_le K (φ := sat K q φ) ?_
    intro b
    have h1 : K.le (closure K R (sat K q φ) b)
        (closure K R (sat K q (closure K R φ)) b) :=
      closure_mono K R (fun a => sat_mono K q (fun c => le_closure K R φ c) a) b
    have h2 := le_sat K q (closure K R (sat K q (closure K R φ))) b
    have h3 := h φ b
    have h4 : K.le (sat K q (closure K R φ) b) (sat K q φ b) :=
      sat_mono K q (fun c => closure_le_of_closed K hφ c) b
    exact K.le_trans h1 (K.le_trans h2 (K.le_trans h3 h4))

end Core

/-! ## Change of value structure

Exactness transports along homomorphisms of value structures.  The strict
hierarchy `endpoint < cost < trace` of the Boolean development is a chain of
such changes (path languages → cost → truth); the converse transport fails,
as the finite receipts in the research package show. -/

section BaseChange

variable {V : Type u} {W : Type u} {X : Type v} {Y : Type w}

/-- A homomorphism of value structures, stated through the preorders. -/
structure QHom (K : LaxQuantale V) (L : LaxQuantale W) (h : V → W) : Prop where
  mono : ∀ {a b}, K.le a b → L.le (h a) (h b)
  map_sSup_le : ∀ S : V → Prop,
    L.le (h (K.sSup S)) (L.sSup (fun t => ∃ s, S s ∧ t = h s))
  map_mul_le : ∀ a b, L.le (h (K.mul a b)) (L.mul (h a) (h b))
  mul_map_le : ∀ a b, L.le (L.mul (h a) (h b)) (h (K.mul a b))
  map_one_le : L.le (h K.one) L.one
  one_le_map : L.le L.one (h K.one)

variable {K : LaxQuantale V} {L : LaxQuantale W} {h : V → W}

theorem map_star_le (hom : QHom K L h) (R : X → X → V) (x z : X) :
    L.le (h (star K R x z)) (star L (fun u v => h (R u v)) x z) := by
  refine L.le_trans (hom.map_sSup_le _) (L.sSup_le ?_)
  intro t ht
  cases ht with
  | intro p hp =>
      cases hp with
      | intro path e =>
          subst e
          have key : ∃ p', PathW L (fun u v => h (R u v)) x z p' ∧ L.le (h p) p' := by
            induction path with
            | refl => exact ⟨_, PathW.refl, hom.map_one_le⟩
            | tail _ ih =>
                cases ih with
                | intro p' hp' =>
                    exact ⟨_, PathW.tail hp'.1,
                      L.le_trans (hom.map_mul_le _ _)
                        (L.mul_mono hp'.2 (L.le_refl _))⟩
          cases key with
          | intro p' hp' => exact L.le_trans hp'.2 (L.le_sSup hp'.1)

theorem star_map_le (hom : QHom K L h) (R : X → X → V) (x z : X) :
    L.le (star L (fun u v => h (R u v)) x z) (h (star K R x z)) := by
  refine L.sSup_le ?_
  intro p' path
  have key : ∃ p, PathW K R x z p ∧ L.le p' (h p) := by
    induction path with
    | refl => exact ⟨_, PathW.refl, hom.one_le_map⟩
    | tail _ ih =>
        cases ih with
        | intro p hp =>
            exact ⟨_, PathW.tail hp.1,
              L.le_trans (L.mul_mono hp.2 (L.le_refl _)) (hom.mul_map_le _ _)⟩
  cases key with
  | intro p hp => exact L.le_trans hp.2 (hom.mono (K.le_sSup hp.1))

theorem star_mono_rel (L : LaxQuantale W) {S S' : X → X → W}
    (hS : ∀ u v, L.le (S u v) (S' u v)) (x z : X) :
    L.le (star L S x z) (star L S' x z) := by
  refine star_le_of_closed L (φ := star L S' x) ?_ (one_le_star L S' x) z
  intro u v
  exact L.le_trans (L.mul_mono (L.le_refl _) (hS u v)) (star_closed L S' x u v)

theorem push_mono (L : LaxQuantale W) (q : X → Y) {φ φ' : X → W}
    (hφ : ∀ u, L.le (φ u) (φ' u)) (b : Y) :
    L.le (push L q φ b) (push L q φ' b) := by
  refine L.sSup_le ?_
  intro t ht
  cases ht with
  | intro u hu =>
      cases hu with
      | intro e1 e2 =>
          subst e1; subst e2
          exact L.le_trans (hφ u) (le_push L q φ' u)

/-- **Change of base.**  Selected-start exactness over `K` implies
selected-start exactness of the image relation over `L`. -/
theorem exactAt_map (hom : QHom K L h) (R : X → X → V) (q : X → Y) (x : X)
    (exact : ExactAt K R q x) :
    ExactAt L (fun u v => h (R u v)) q x := by
  intro b
  have step1 : L.le (star L (quot L (fun u v => h (R u v)) q) (q x) b)
      (star L (fun a c => h (quot K R q a c)) (q x) b) := by
    refine star_mono_rel L ?_ (q x) b
    intro a c
    refine L.sSup_le ?_
    intro t ht
    cases ht with
    | intro u hu =>
        cases hu with
        | intro v hv =>
            cases hv with
            | intro ha hv =>
                cases hv with
                | intro hc e =>
                    subst e
                    exact hom.mono (K.le_sSup ⟨u, v, ha, hc, rfl⟩)
  have step2 := star_map_le hom (quot K R q) (q x) b
  have step3 : L.le (h (star K (quot K R q) (q x) b))
      (h (push K q (star K R x) b)) := hom.mono (exact b)
  have step4 : L.le (h (push K q (star K R x) b))
      (push L q (fun u => h (star K R x u)) b) := by
    refine L.le_trans (hom.map_sSup_le _) (L.sSup_le ?_)
    intro t ht
    cases ht with
    | intro s hs =>
        cases hs with
        | intro hs e =>
            cases hs with
            | intro u hu =>
                cases hu with
                | intro e1 e2 =>
                    subst e; subst e2
                    exact L.le_sSup ⟨u, e1, rfl⟩
  have step5 : L.le (push L q (fun u => h (star K R x u)) b)
      (push L q (star L (fun u v => h (R u v)) x) b) :=
    push_mono L q (fun u => map_star_le hom R x u) b
  exact L.le_trans step1 (L.le_trans step2 (L.le_trans step3
    (L.le_trans step4 step5)))

end BaseChange

/-! ## The truth-value instance recovers ordinary reachability -/

/-- Propositions ordered by implication, with conjunction as multiplication. -/
def propQ : LaxQuantale Prop where
  le a b := a → b
  mul a b := a ∧ b
  one := True
  sSup S := ∃ p, S p ∧ p
  le_refl _ := id
  le_trans f g := fun a => g (f a)
  le_sSup hS := fun ha => ⟨_, hS, ha⟩
  sSup_le h := fun ⟨p, hp, pp⟩ => h p hp pp
  mul_mono f g := fun ⟨a, c⟩ => ⟨f a, g c⟩
  mul_sSup_le _ _ := fun ⟨ha, p, hp, pp⟩ => ⟨_, ⟨p, hp, rfl⟩, ha, pp⟩
  sSup_mul_le _ _ := fun ⟨⟨p, hp, pp⟩, ha⟩ => ⟨_, ⟨p, hp, rfl⟩, pp, ha⟩
  mul_assoc_le _ _ _ := fun ⟨ha, hb, hc⟩ => ⟨⟨ha, hb⟩, hc⟩
  mul_assoc_ge _ _ _ := fun ⟨⟨ha, hb⟩, hc⟩ => ⟨ha, hb, hc⟩
  mul_one_le _ := fun h => h.1
  le_mul_one _ := fun h => ⟨h, True.intro⟩
  le_one_mul _ := fun h => ⟨True.intro, h⟩

inductive Reach {X : Type v} (R : X → X → Prop) : X → X → Prop where
  | refl (x : X) : Reach R x x
  | tail {x y z : X} : Reach R x y → R y z → Reach R x z

theorem reach_of_path {X : Type v} {R : X → X → Prop} {x z : X} {p : Prop}
    (path : PathW propQ R x z p) : p → Reach R x z := by
  induction path with
  | refl => intro _; exact Reach.refl x
  | tail _ ih => intro h; exact Reach.tail (ih h.1) h.2

/-- Over truth values the weighted closure IS reflexive-transitive closure. -/
theorem star_propQ_iff {X : Type v} (R : X → X → Prop) (x z : X) :
    star propQ R x z ↔ Reach R x z := by
  constructor
  · intro h
    cases h with
    | intro p hp => exact reach_of_path hp.1 hp.2
  · intro h
    induction h with
    | refl => exact ⟨True, PathW.refl, True.intro⟩
    | tail _ step ih =>
        cases ih with
        | intro p hp => exact ⟨_, PathW.tail hp.1, hp.2, step⟩

end ObservationalSUCC.ObservatorisQuantale
