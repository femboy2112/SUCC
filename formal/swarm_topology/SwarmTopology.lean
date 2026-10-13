import Mathlib.Topology.Compactness.Compact
import Mathlib.Topology.Constructions
import Mathlib.Topology.Separation.Basic

/-!
SWM-B09: genuine product-topology closure and compact-source realization.
Pinned mathlib4 v4.14.0 commit4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84.
The source image, finite-coordinate compatibility, and completion are distinct.
-/
namespace ObservationalSUCC.SwarmTopology
open Set
universe u v w

variable {S : Type u} {W : Type v} {O : Type w}
variable [TopologicalSpace O] [DiscreteTopology O]

def FiniteCompatible (trace : S → W → O) (profile : W → O) : Prop :=
  ∀ F : Finset W, ∃ s : S, ∀ n ∈ F, trace s n = profile n

/-- Arbitrary index sets, not only sequential prefix experiments. -/
theorem closure_iff_finite_compatible (trace : S → W → O) (profile : W → O) :
    profile ∈ closure (Set.range trace) ↔ FiniteCompatible trace profile := by
  classical
  constructor
  · intro inClosure F
    let cylinder : Set (W → O) := (F : Set W).pi (fun n => {profile n})
    have cylinderOpen : IsOpen cylinder :=
      isOpen_set_pi F.finite_toSet (fun _ _ => isOpen_discrete _)
    have profileIn : profile ∈ cylinder := by
      intro n hn
      exact Set.mem_singleton (profile n)
    obtain ⟨other, otherIn, otherSource⟩ :=
      mem_closure_iff.mp inClosure cylinder cylinderOpen profileIn
    obtain ⟨s, rfl⟩ := otherSource
    refine ⟨s, ?_⟩
    intro n hn
    exact otherIn n hn
  · intro compatible
    apply mem_closure_iff.mpr
    intro neighborhood neighborhoodOpen profileIn
    obtain ⟨F, values, localValues, included⟩ :=
      isOpen_pi_iff.mp neighborhoodOpen profile profileIn
    obtain ⟨s, agrees⟩ := compatible F
    refine ⟨trace s, included ?_, ⟨s, rfl⟩⟩
    intro n hn
    rw [agrees n hn]
    exact (localValues n hn).2

/-- Exact source-actualization criterion, with no compactness premise. -/
theorem all_compatible_realized_iff_closed_image (trace : S → W → O) :
    (∀ profile, FiniteCompatible trace profile → ∃ s, trace s = profile) ↔
      IsClosed (Set.range trace) := by
  constructor
  · intro realized
    apply closure_eq_iff_isClosed.mp
    apply Set.Subset.antisymm
    · intro profile inClosure
      exact realized profile ((closure_iff_finite_compatible trace profile).mp inClosure)
    · exact subset_closure
  · intro closedImage profile compatible
    have inClosure := (closure_iff_finite_compatible trace profile).mpr compatible
    rw [closedImage.closure_eq] at inClosure
    exact inClosure

/-- Compactness and continuity concern the DECLARED source, not a guessed
model or an observed finite prefix. -/
theorem compact_continuous_source_realizes
    [TopologicalSpace S] [CompactSpace S]
    (trace : S → W → O)
    (coordinateContinuous : ∀ n, Continuous (fun s => trace s n))
    (profile : W → O) (compatible : FiniteCompatible trace profile) :
    ∃ s, trace s = profile := by
  have closedImage : IsClosed (Set.range trace) :=
    (isCompact_range (continuous_pi coordinateContinuous)).isClosed
  exact (all_compatible_realized_iff_closed_image trace).mpr closedImage profile compatible

/-- Compact positive control: the complete product source with identity
trace satisfies actualization for EVERY finite-compatible profile. -/
theorem full_profile_source_positive_control (profile : W → O) :
    ∃ source : W → O, (fun n => source n) = profile := by
  exact ⟨profile, rfl⟩

/-- The actual inverse-system thread space: every finite restriction is
source-admissible, and overlapping coordinates agree. -/
def ThreadCondition (trace : S → W → O)
    (rows : (F : Finset W) → (F → O)) : Prop :=
  (∀ F : Finset W, ∃ s : S, ∀ n : F, rows F n = trace s n.val) ∧
  (∀ F G n (hF : n ∈ F) (hG : n ∈ G),
    rows F ⟨n, hF⟩ = rows G ⟨n, hG⟩)

abbrev InverseThread (trace : S → W → O) :=
  {rows : (F : Finset W) → (F → O) // ThreadCondition trace rows}

abbrev CompatibleProfile (trace : S → W → O) :=
  {profile : W → O // FiniteCompatible trace profile}

noncomputable def profileToThread (trace : S → W → O)
    (profile : CompatibleProfile trace) : InverseThread trace := by
  classical
  refine ⟨fun F n => profile.val n.val, ?_, ?_⟩
  · intro F
    obtain ⟨s, agrees⟩ := profile.property F
    exact ⟨s, fun n => (agrees n.val n.property).symm⟩
  · intro F G n hF hG
    rfl

noncomputable def threadToProfile (trace : S → W → O)
    (thread : InverseThread trace) : CompatibleProfile trace := by
  classical
  let profile : W → O := fun n => thread.val {n} ⟨n, by simp⟩
  refine ⟨profile, ?_⟩
  intro F
  obtain ⟨s, agrees⟩ := thread.property.1 F
  refine ⟨s, ?_⟩
  intro n hn
  exact (agrees ⟨n, hn⟩).symm.trans (thread.property.2 F {n} n hn (by simp))

theorem thread_profile_left_inverse (trace : S → W → O) :
    Function.LeftInverse (threadToProfile trace) (profileToThread trace) := by
  intro profile
  apply Subtype.ext
  funext n
  rfl

theorem thread_profile_right_inverse (trace : S → W → O) :
    Function.RightInverse (threadToProfile trace) (profileToThread trace) := by
  classical
  intro thread
  apply Subtype.ext
  funext F n
  exact (thread.property.2 F {n.val} n.val n.property (by simp)).symm

/-- The forward inverse-system comparison is continuous in the genuine
product/subspace topologies. -/
theorem profileToThread_continuous (trace : S → W → O) :
    Continuous (profileToThread trace) := by
  apply Continuous.subtype_mk
  exact continuous_pi (fun F => continuous_pi (fun n =>
    (continuous_apply n.val).comp continuous_subtype_val))

/-- The inverse comparison reads a singleton row for each coordinate,
so it too is continuous, not merely a set-level bijection. -/
theorem threadToProfile_continuous (trace : S → W → O) :
    Continuous (threadToProfile trace) := by
  classical
  apply Continuous.subtype_mk
  exact continuous_pi (fun n => (continuous_apply (⟨n, by simp⟩ : ({n} : Finset W))).comp
    ((continuous_apply ({n} : Finset W)).comp continuous_subtype_val))

/-- Completion is the literal product-topology closure, not a proxy flag. -/
theorem completion_eq_closure (trace : S → W → O) :
    {profile : W → O | FiniteCompatible trace profile} = closure (Set.range trace) := by
  ext profile
  exact (closure_iff_finite_compatible trace profile).symm

/-- The finite-alphabet completion is compact in its actual topology. -/
theorem finite_alphabet_completion_compact [Finite O] (trace : S → W → O) :
    IsCompact {profile : W → O | FiniteCompatible trace profile} := by
  rw [completion_eq_closure]
  exact isClosed_closure.isCompact

/-- Positive control actually instantiates the compact-source theorem on
an infinite product of finite discrete reports, using Tychonoff's instance. -/
theorem compact_full_profile_source_control [Finite O] (profile : W → O) :
    ∃ source : W → O, (fun n => source n) = profile := by
  apply compact_continuous_source_realizes (fun source : W → O => source)
    (fun n => continuous_apply n) profile
  intro F
  exact ⟨profile, fun n hn => rfl⟩

/-- Full homeomorphism data for the actual finite-restriction inverse
system and the closed observational completion. The equality above identifies
the profile subtype with the product closure; both maps preserve topology. -/
theorem inverse_limit_completion_topological_equivalence (trace : S → W → O) :
    ∃ (f : CompatibleProfile trace → InverseThread trace)
      (g : InverseThread trace → CompatibleProfile trace),
      Continuous f ∧ Continuous g ∧ Function.LeftInverse g f ∧
      Function.RightInverse g f := by
  exact ⟨profileToThread trace, threadToProfile trace,
    profileToThread_continuous trace, threadToProfile_continuous trace,
    thread_profile_left_inverse trace, thread_profile_right_inverse trace⟩

end ObservationalSUCC.SwarmTopology
