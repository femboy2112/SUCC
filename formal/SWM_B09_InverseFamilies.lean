/-!
# SWM-B09: actual inverse families of finite source-image reports

Standalone Lean 4.14.0, no mathlib. Index all finite lists of probes,
ordered by inclusion of their underlying membership predicates. Repeated
probes and permutations are harmless because coordinates are indexed by
probe values, not list positions. The empty stage records source
inhabitation; it is not silently assumed to contain a point.

Kernel target: inverse-family <-> finite-compatible-profile equivalence,
source-stage restriction surjectivity, and a constructive positive
control on all binary streams. This does NOT claim that mathlib's product
topology, compactness or topological homeomorphism has been formalized.
-/
namespace ObservationalSUCC.SWM_B09

universe u v w k

def Compatible {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (profile : W → O) : Prop :=
  ∀ F : List W, ∃ s : S, ∀ a, a ∈ F → trace s a = profile a

def Stage {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (F : List W) :=
  { r : { a : W // a ∈ F } → O //
      ∃ s : S, ∀ a, r a = trace s a.val }

def Includes {W : Type v} (F G : List W) : Prop :=
  ∀ a, a ∈ F → a ∈ G

def restrictStage {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} {F G : List W}
    (inc : Includes F G) (r : Stage trace G) : Stage trace F :=
  ⟨fun a => r.val ⟨a.val, inc a.val a.property⟩, by
    obtain ⟨s, hs⟩ := r.property
    exact ⟨s, fun a => hs ⟨a.val, inc a.val a.property⟩⟩⟩

theorem stage_restriction_identity
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} {F : List W} (r : Stage trace F) :
    restrictStage (fun _ member => member) r = r := by
  apply Subtype.ext
  rfl

theorem stage_restriction_composition
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} {F G H : List W}
    (fg : Includes F G) (gh : Includes G H) (r : Stage trace H) :
    restrictStage fg (restrictStage gh r) =
      restrictStage (fun a member => gh a (fg a member)) r := by
  apply Subtype.ext
  rfl

theorem stage_restriction_surjective
    {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (F G : List W) (inc : Includes F G) :
    ∀ r : Stage trace F, ∃ t : Stage trace G, restrictStage inc t = r := by
  intro r
  obtain ⟨s, hs⟩ := r.property
  refine ⟨⟨fun a => trace s a.val, ⟨s, fun _ => rfl⟩⟩, ?_⟩
  apply Subtype.ext
  funext a
  exact (hs a).symm

structure InverseFamily {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) where
  coordinate : (F : List W) → Stage trace F
  coherent : ∀ F G (inc : Includes F G),
    restrictStage inc (coordinate G) = coordinate F

def decode {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} (x : InverseFamily trace) (a : W) : O :=
  (x.coordinate [a]).val ⟨a, by simp⟩

theorem coordinate_is_singleton_decode
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} (x : InverseFamily trace)
    (F : List W) (a : W) (member : a ∈ F) :
    (x.coordinate F).val ⟨a, member⟩ = decode x a := by
  have inc : Includes [a] F := by
    intro b hb
    have eq : b = a := by simpa using hb
    subst b
    exact member
  have eq := x.coherent [a] F inc
  exact congrArg (fun r : Stage trace [a] => r.val ⟨a, by simp⟩) eq

theorem decode_compatible
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} (x : InverseFamily trace) :
    Compatible trace (decode x) := by
  intro F
  obtain ⟨s, hs⟩ := (x.coordinate F).property
  refine ⟨s, ?_⟩
  intro a member
  exact (hs ⟨a, member⟩).symm.trans
    (coordinate_is_singleton_decode x F a member)

def encode {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O}
    (z : { profile : W → O // Compatible trace profile }) :
    InverseFamily trace where
  coordinate F := ⟨fun a => z.val a.val, by
    obtain ⟨s, hs⟩ := z.property F
    exact ⟨s, fun a => (hs a.val a.property).symm⟩⟩
  coherent F G inc := by
    apply Subtype.ext
    rfl

theorem decode_encode
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O}
    (z : { profile : W → O // Compatible trace profile }) :
    decode (encode z) = z.val := by
  rfl

theorem inverse_family_ext
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} {x y : InverseFamily trace}
    (h : x.coordinate = y.coordinate) : x = y := by
  cases x
  cases y
  cases h
  rfl

theorem encode_decode
    {S : Type u} {W : Type v} {O : Type w}
    {trace : S → W → O} (x : InverseFamily trace) :
    encode ⟨decode x, decode_compatible x⟩ = x := by
  apply inverse_family_ext
  funext F
  apply Subtype.ext
  funext a
  exact (coordinate_is_singleton_decode x F a.val a.property).symm

/-- Explicit mutually inverse maps; no topological claims are hidden. -/
theorem inverse_families_equivalent_to_finitely_compatible_profiles
    {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) :
    (∀ x : InverseFamily trace,
      encode ⟨decode x, decode_compatible x⟩ = x) ∧
    (∀ z : { profile : W → O // Compatible trace profile },
      decode (encode z) = z.val) :=
  ⟨encode_decode, decode_encode⟩

def originalFamily {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (s : S) : InverseFamily trace :=
  encode ⟨trace s, fun _ => ⟨s, fun _ _ => rfl⟩⟩

/-- Surjectivity of the source map has exactly the global-realizer gate;
finite stage surjectivity above is insufficient by itself. -/
theorem source_family_surjective_iff_realization
    {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) :
    (∀ x : InverseFamily trace, ∃ s, originalFamily trace s = x) ↔
    (∀ z : W → O, Compatible trace z → ∃ s, trace s = z) := by
  constructor
  · intro allFamilies z compatible
    obtain ⟨s, hs⟩ := allFamilies (encode ⟨z, compatible⟩)
    exact ⟨s, congrArg decode hs⟩
  · intro allProfiles x
    obtain ⟨s, hs⟩ := allProfiles (decode x) (decode_compatible x)
    refine ⟨s, ?_⟩
    apply inverse_family_ext
    funext F
    apply Subtype.ext
    funext a
    change trace s a.val = (x.coordinate F).val a
    exact (congrFun hs a.val).trans
      (coordinate_is_singleton_decode x F a.val a.property).symm

/-- A chosen stage schedule is adequate only when it is cofinal for
ENTIRE finite families, not merely when every single probe appears. -/
theorem cofinal_stage_testing_iff_compatible
    {S : Type u} {W : Type v} {O : Type w} {K : Type k}
    (trace : S → W → O) (profile : W → O) (schedule : K → List W)
    (cofinal : ∀ F : List W, ∃ k, Includes F (schedule k)) :
    Compatible trace profile ↔
      (∀ k, ∃ s : S,
        ∀ a, a ∈ schedule k → trace s a = profile a) := by
  constructor
  · intro compatible k
    exact compatible (schedule k)
  · intro stages F
    obtain ⟨k, inc⟩ := cofinal F
    obtain ⟨s, hs⟩ := stages k
    exact ⟨s, fun a member => hs a (inc a member)⟩

def constantTrace (source : Bool) (_probe : Bool) : Bool := source

/-- Minimal two-source/two-probe hostile control: every singleton
report is possible, but the heterogeneous pair has no common source. -/
theorem singleton_stage_marginals_do_not_imply_joint_compatibility :
    (∀ a : Bool, ∃ s, constantTrace s a = a) ∧
    ¬ Compatible constantTrace (fun a => a) := by
  constructor
  · intro a
    exact ⟨a, rfl⟩
  · intro compatible
    obtain ⟨s, hs⟩ := compatible [false, true]
    have hf : s = false := hs false (by simp)
    have ht : s = true := hs true (by simp)
    have impossible : false = true := hf.symm.trans ht
    cases impossible

/-- The empty stage detects an empty source, even with no legal probes.
No source-actualization premise is hidden in the inverse-family type. -/
theorem empty_source_has_no_inverse_family
    {W : Type v} {O : Type w} (trace : Empty → W → O) :
    ¬ Nonempty (InverseFamily trace) := by
  rintro ⟨x⟩
  obtain ⟨s, _⟩ := (x.coordinate []).property
  cases s

/-- A lawful source action extends to the ideal profile completion by
reindexing probes. Each finite witness changes its carrier lawfully;
the theorem does not assert a common original realizer. -/
theorem lawful_action_preserves_compatible_profiles
    {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (update : S → S) (reindex : W → W)
    (law : ∀ s a, trace (update s) a = trace s (reindex a))
    (z : W → O) (compatible : Compatible trace z) :
    Compatible trace (fun a => z (reindex a)) := by
  intro F
  obtain ⟨s, hs⟩ := compatible (F.map reindex)
  refine ⟨update s, ?_⟩
  intro a member
  exact (law s a).trans
    (hs (reindex a) (List.mem_map.mpr ⟨a, member, rfl⟩))

/-- Nontrivial compact positive control in paper topology: adjacent-bit
derivative on Cantor space, whose fibers have two possible preparations.
This file kernel-checks the constructive surjectivity, NOT compactness. -/
def integrateBinary (z : Nat → Bool) : Nat → Bool
  | 0 => false
  | n + 1 => Bool.xor (integrateBinary z n) (z n)

def binaryDerivative (x : Nat → Bool) (n : Nat) : Bool :=
  Bool.xor (x n) (x (n + 1))

theorem derivative_integration (z : Nat → Bool) :
    binaryDerivative (integrateBinary z) = z := by
  funext n
  change Bool.xor (integrateBinary z n)
    (Bool.xor (integrateBinary z n) (z n)) = z n
  cases integrateBinary z n <;> cases z n <;> rfl

theorem binary_derivative_source_all_profiles_realized :
    ∀ z : Nat → Bool, ∃ x : Nat → Bool, binaryDerivative x = z := by
  intro z
  exact ⟨integrateBinary z, derivative_integration z⟩

theorem binary_derivative_source_family_surjective :
    ∀ x : InverseFamily binaryDerivative,
      ∃ s, originalFamily binaryDerivative s = x := by
  apply (source_family_surjective_iff_realization binaryDerivative).mpr
  intro z _
  exact binary_derivative_source_all_profiles_realized z

#print axioms stage_restriction_identity
#print axioms stage_restriction_composition
#print axioms stage_restriction_surjective
#print axioms coordinate_is_singleton_decode
#print axioms decode_compatible
#print axioms inverse_families_equivalent_to_finitely_compatible_profiles
#print axioms source_family_surjective_iff_realization
#print axioms cofinal_stage_testing_iff_compatible
#print axioms singleton_stage_marginals_do_not_imply_joint_compatibility
#print axioms empty_source_has_no_inverse_family
#print axioms lawful_action_preserves_compatible_profiles
#print axioms binary_derivative_source_all_profiles_realized
#print axioms binary_derivative_source_family_surjective

end ObservationalSUCC.SWM_B09
