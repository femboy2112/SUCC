import Mathlib.Topology.Constructions
import Mathlib.Topology.Separation.Basic
import Mathlib.Topology.Homeomorph
import SWM_B09_InverseFamilies

/-!
# SWM-B09: native product-topology closure and inverse-limit homeomorphism

Dependency: mathlib v4.14.0, exact commit
4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84; compiler Lean 4.14.0.
This file uses mathlib's actual closure, product and induced topologies,
Homeomorph, compactness, and Hausdorff separation. No alternative meaning
of "closure" is introduced. The source class may be infinite or empty.

The inverse-family topology is induced from the product of finite-stage
source-image subspaces. It is not pulled back from the desired closure:
continuity in both directions is proved independently below.
-/

noncomputable section

namespace ObservationalSUCC.SWM_B09

open Set

universe u v w t

variable {S : Type u} {W : Type v} {O : Type w}

theorem mem_closure_range_iff_compatible
    [TopologicalSpace O] [DiscreteTopology O]
    (trace : S → W → O) (z : W → O) :
    z ∈ closure (range trace) ↔ Compatible trace z := by
  classical
  constructor
  · intro hz F
    let I : Finset W := F.toFinset
    let cylinder : Set (W → O) := (I : Set W).pi (fun a => {z a})
    have hopen : IsOpen cylinder :=
      isOpen_set_pi I.finite_toSet (fun _ _ => isOpen_discrete _)
    have hmem : z ∈ cylinder := by
      intro a _
      rfl
    obtain ⟨y, hy, hs⟩ := mem_closure_iff.mp hz cylinder hopen hmem
    obtain ⟨s, rfl⟩ := hs
    refine ⟨s, ?_⟩
    intro a ha
    have hi : a ∈ (I : Set W) := by simpa [I] using ha
    simpa using hy a hi
  · intro compatible
    apply mem_closure_iff.mpr
    intro neighborhood hopen hz
    obtain ⟨I, neighborhoods, hlocal, hsub⟩ :=
      isOpen_pi_iff.mp hopen z hz
    obtain ⟨s, hs⟩ := compatible I.toList
    refine ⟨trace s, hsub ?_, ⟨s, rfl⟩⟩
    intro a ha
    have agreement : trace s a = z a := hs a (by simpa using ha)
    rw [agreement]
    exact (hlocal a ha).2

theorem closure_range_eq_compatible
    [TopologicalSpace O] [DiscreteTopology O] (trace : S → W → O) :
    closure (range trace) = {z | Compatible trace z} := by
  ext z
  exact mem_closure_range_iff_compatible trace z

/-- The topology comes from the actual product of stage subspaces. -/
instance stageTopologicalSpace [TopologicalSpace O]
    (trace : S → W → O) (F : List W) : TopologicalSpace (Stage trace F) := by
  unfold Stage
  infer_instance

instance inverseFamilyTopologicalSpace [TopologicalSpace O]
    (trace : S → W → O) : TopologicalSpace (InverseFamily trace) :=
  TopologicalSpace.induced InverseFamily.coordinate inferInstance

/-- The elementary topological inverse-limit universal property: a
continuous compatible cone has exactly one continuous factorization. -/
theorem inverse_family_topological_limit_universal
    {X : Type t} [TopologicalSpace X] [TopologicalSpace O]
    (trace : S → W → O)
    (legs : ∀ F : List W, X → Stage trace F)
    (commute : ∀ F G (inc : Includes F G) x,
      restrictStage inc (legs G x) = legs F x)
    (continuous_legs : ∀ F, Continuous (legs F)) :
    ∃! lift : X → InverseFamily trace,
      Continuous lift ∧ ∀ x F, (lift x).coordinate F = legs F x := by
  let lift : X → InverseFamily trace := fun x =>
    ⟨fun F => legs F x, fun F G inc => commute F G inc x⟩
  refine ⟨lift, ⟨?_, by intro x F; rfl⟩, ?_⟩
  · apply continuous_induced_rng.mpr
    exact continuous_pi continuous_legs
  · intro other hother
    funext x
    apply inverse_family_ext
    funext F
    exact hother.2 x F

theorem continuous_decode [TopologicalSpace O] (trace : S → W → O) :
    Continuous (decode : InverseFamily trace → W → O) := by
  apply continuous_pi
  intro a
  have hcoord : Continuous
      (fun x : InverseFamily trace => x.coordinate [a]) :=
    (continuous_apply [a]).comp continuous_induced_dom
  have hvalue : Continuous
      (fun x : InverseFamily trace => (x.coordinate [a]).val) :=
    continuous_subtype_val.comp hcoord
  exact (continuous_apply ⟨a, by simp⟩).comp hvalue

theorem continuous_encode [TopologicalSpace O] (trace : S → W → O) :
    Continuous (encode : {z : W → O // Compatible trace z} → InverseFamily trace) := by
  apply continuous_induced_rng.mpr
  apply continuous_pi
  intro F
  apply Continuous.subtype_mk
  apply continuous_pi
  intro a
  exact (continuous_apply a.val).comp continuous_subtype_val

def inverseFamilyClosureHomeomorph
    [TopologicalSpace O] [DiscreteTopology O] (trace : S → W → O) :
    InverseFamily trace ≃ₜ {z : W → O // z ∈ closure (range trace)} where
  toFun x := ⟨decode x,
    (mem_closure_range_iff_compatible trace (decode x)).mpr (decode_compatible x)⟩
  invFun z := encode ⟨z.val,
    (mem_closure_range_iff_compatible trace z.val).mp z.property⟩
  left_inv x := encode_decode x
  right_inv z := by
    apply Subtype.ext
    rfl
  continuous_toFun :=
    (continuous_decode trace).subtype_mk _
  continuous_invFun := by
    have hbridge : Continuous
        (fun z : {z : W → O // z ∈ closure (range trace)} =>
          (⟨z.val, (mem_closure_range_iff_compatible trace z.val).mp z.property⟩ :
            {z : W → O // Compatible trace z})) :=
      continuous_subtype_val.subtype_mk _
    exact (continuous_encode trace).comp hbridge

theorem global_realization_iff_closed_trace_image
    [TopologicalSpace O] [DiscreteTopology O] (trace : S → W → O) :
    (∀ z : W → O, Compatible trace z → ∃ s, trace s = z) ↔
    IsClosed (range trace) := by
  constructor
  · intro realizers
    apply closure_eq_iff_isClosed.mp
    apply Set.Subset.antisymm
    · intro z hz
      exact realizers z ((mem_closure_range_iff_compatible trace z).mp hz)
    · exact subset_closure
  · intro hclosed z compatible
    have hz := (mem_closure_range_iff_compatible trace z).mpr compatible
    rw [hclosed.closure_eq] at hz
    exact hz

theorem source_family_surjective_iff_closed_trace_image
    [TopologicalSpace O] [DiscreteTopology O] (trace : S → W → O) :
    (∀ x : InverseFamily trace, ∃ s, originalFamily trace s = x) ↔
    IsClosed (range trace) :=
  (source_family_surjective_iff_realization trace).trans
    (global_realization_iff_closed_trace_image trace)

theorem compact_continuous_source_realizes_compatible_profile
    [TopologicalSpace S] [CompactSpace S]
    [TopologicalSpace O] [DiscreteTopology O]
    (trace : S → W → O)
    (reports_continuous : ∀ a, Continuous (fun s => trace s a))
    (z : W → O) (compatible : Compatible trace z) :
    ∃ s, trace s = z := by
  have htrace : Continuous trace := continuous_pi reports_continuous
  have hclosed : IsClosed (range trace) := (isCompact_range htrace).isClosed
  exact (global_realization_iff_closed_trace_image trace).mpr hclosed z compatible

theorem compact_continuous_source_family_surjective
    [TopologicalSpace S] [CompactSpace S]
    [TopologicalSpace O] [DiscreteTopology O]
    (trace : S → W → O)
    (reports_continuous : ∀ a, Continuous (fun s => trace s a)) :
    ∀ x : InverseFamily trace, ∃ s, originalFamily trace s = x := by
  apply (source_family_surjective_iff_realization trace).mpr
  intro z compatible
  exact compact_continuous_source_realizes_compatible_profile
    trace reports_continuous z compatible

theorem finite_alphabet_trace_closure_compact
    [TopologicalSpace O] [Finite O] (trace : S → W → O) :
    IsCompact (closure (range trace)) :=
  isClosed_closure.isCompact

theorem coordinate_image_closure_eq
    [TopologicalSpace O] [DiscreteTopology O]
    (trace : S → W → O) (a : W) :
    (fun z : W → O => z a) '' closure (range trace) =
      range (fun s => trace s a) := by
  apply Set.Subset.antisymm
  · rintro value ⟨z, hz, rfl⟩
    have maps : MapsTo (fun z : W → O => z a) (range trace)
        (range (fun s => trace s a)) := by
      rintro _ ⟨s, rfl⟩
      exact ⟨s, rfl⟩
    exact maps.closure_left (continuous_apply a) (isClosed_discrete _) hz
  · rintro value ⟨s, rfl⟩
    exact ⟨trace s, subset_closure ⟨s, rfl⟩, rfl⟩

/-- Sharp compactness criterion; a common finite alphabet is unnecessary. -/
theorem trace_closure_compact_iff_each_probe_finite_image
    [TopologicalSpace O] [DiscreteTopology O] (trace : S → W → O) :
    IsCompact (closure (range trace)) ↔
      ∀ a, (range (fun s => trace s a)).Finite := by
  rw [Pi.isCompact_iff_of_isClosed isClosed_closure]
  simp only [coordinate_image_closure_eq trace, isCompact_iff_finite]

theorem continuous_profile_reindexing [TopologicalSpace O] (r : W → W) :
    Continuous (fun z : W → O => fun a => z (r a)) :=
  continuous_pi (fun a => continuous_apply (r a))

theorem lawful_action_preserves_trace_closure
    [TopologicalSpace O] [DiscreteTopology O]
    (trace : S → W → O) (update : S → S) (reindex : W → W)
    (law : ∀ s a, trace (update s) a = trace s (reindex a))
    (z : W → O) (hz : z ∈ closure (range trace)) :
    (fun a => z (reindex a)) ∈ closure (range trace) := by
  apply (mem_closure_range_iff_compatible trace _).mpr
  exact lawful_action_preserves_compatible_profiles trace update reindex law z
    ((mem_closure_range_iff_compatible trace z).mp hz)

theorem binary_derivative_continuous : Continuous binaryDerivative := by
  apply continuous_pi
  intro n
  have hxor : Continuous (fun p : Bool × Bool => Bool.xor p.1 p.2) :=
    continuous_of_discreteTopology
  have hfirst : Continuous (fun x : Nat → Bool => x n) := continuous_apply n
  have hnext : Continuous (fun x : Nat → Bool => x (n + 1)) := continuous_apply (n + 1)
  exact hxor.comp (hfirst.prod_mk hnext)

/-- The compact continuous-source theorem is applied to an infinite source,
not merely assumed from an explicit algebraic right inverse. -/
theorem cantor_compact_source_actualizes_every_compatible_derivative
    (z : Nat → Bool) (compatible : Compatible binaryDerivative z) :
    ∃ source : Nat → Bool, binaryDerivative source = z := by
  apply compact_continuous_source_realizes_compatible_profile
    binaryDerivative (continuous_pi_iff.mp binary_derivative_continuous) z compatible

#print axioms mem_closure_range_iff_compatible
#print axioms closure_range_eq_compatible
#print axioms inverseFamilyClosureHomeomorph
#print axioms inverse_family_topological_limit_universal
#print axioms source_family_surjective_iff_closed_trace_image
#print axioms compact_continuous_source_realizes_compatible_profile
#print axioms compact_continuous_source_family_surjective
#print axioms finite_alphabet_trace_closure_compact
#print axioms trace_closure_compact_iff_each_probe_finite_image
#print axioms lawful_action_preserves_trace_closure
#print axioms cantor_compact_source_actualizes_every_compatible_derivative

end ObservationalSUCC.SWM_B09
