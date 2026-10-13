import SwarmTopology

/-!
SWM-X01: completion transport and the actualization reflection gate.
Action commutation implies the trace intertwiner by word induction on paper.
This module starts at that precise trace intertwiner. It does not formalize
the finite-coordinate injectivity criterion or the compact image equality.
-/
namespace ObservationalSUCC.SwarmX01CompletionTransport
open ObservationalSUCC.SwarmTopology

universe u v w z t
variable {X : Type u} {Y : Type v} {W : Type w} {O : Type z} {P : Type t}
variable [TopologicalSpace O] [DiscreteTopology O]
variable [TopologicalSpace P] [DiscreteTopology P]

def completionMap (tx : X → W → O) (ty : Y → W → P)
    (f : X → Y) (k : O → P)
    (intertwine : ∀ x n, ty (f x) n = k (tx x n))
    (profile : CompatibleProfile tx) : CompatibleProfile ty := by
  refine ⟨fun n => k (profile.val n), ?_⟩
  intro F
  obtain ⟨x, agrees⟩ := profile.property F
  refine ⟨f x, ?_⟩
  intro n hn
  rw [intertwine, agrees n hn]

theorem completionMap_continuous (tx : X → W → O) (ty : Y → W → P)
    (f : X → Y) (k : O → P)
    (intertwine : ∀ x n, ty (f x) n = k (tx x n)) :
    Continuous (completionMap tx ty f k intertwine) := by
  apply Continuous.subtype_mk
  apply continuous_pi
  intro n
  have hk : Continuous k := continuous_of_discreteTopology
  exact hk.comp ((continuous_apply n).comp continuous_subtype_val)

theorem completionMap_injective_of_report_injective
    (tx : X → W → O) (ty : Y → W → P)
    (f : X → Y) (k : O → P)
    (intertwine : ∀ x n, ty (f x) n = k (tx x n))
    (hk : Function.Injective k) :
    Function.Injective (completionMap tx ty f k intertwine) := by
  intro p q same
  apply Subtype.ext
  funext n
  apply hk
  exact congrFun (congrArg Subtype.val same) n

def sourceProfile (tx : X → W → O) (x : X) : CompatibleProfile tx :=
  ⟨tx x, fun _ => ⟨x, fun _ _ => rfl⟩⟩

theorem completionMap_source_natural
    (tx : X → W → O) (ty : Y → W → P)
    (f : X → Y) (k : O → P)
    (intertwine : ∀ x n, ty (f x) n = k (tx x n)) (x : X) :
    completionMap tx ty f k intertwine (sourceProfile tx x) =
      sourceProfile ty (f x) := by
  apply Subtype.ext
  funext n
  exact (intertwine x n).symm

/-- Surjective source transport and injective completion transport reflect
actual realization. Neither premise can simply be dropped. -/
theorem actualization_reflects
    (tx : X → W → O) (ty : Y → W → P)
    (f : X → Y) (k : O → P)
    (intertwine : ∀ x n, ty (f x) n = k (tx x n))
    (hf : Function.Surjective f)
    (hinj : Function.Injective (completionMap tx ty f k intertwine))
    (p : CompatibleProfile tx)
    (realized : ∃ y, sourceProfile ty y = completionMap tx ty f k intertwine p) :
    ∃ x, sourceProfile tx x = p := by
  obtain ⟨y, hy⟩ := realized
  obtain ⟨x, rfl⟩ := hf y
  refine ⟨x, hinj ?_⟩
  rw [completionMap_source_natural]
  exact hy

/-- With exactly preserved reports, a surjective source map gives a
surjective completion map even for infinite discrete report alphabets. -/
theorem completionMap_surjective_same_reports
    (tx : X → W → O) (ty : Y → W → O) (f : X → Y)
    (intertwine : ∀ x n, ty (f x) n = tx x n)
    (hf : Function.Surjective f) :
    Function.Surjective (completionMap tx ty f id intertwine) := by
  intro p
  have compatible : FiniteCompatible tx p.val := by
    intro F
    obtain ⟨y, agrees⟩ := p.property F
    obtain ⟨x, rfl⟩ := hf y
    refine ⟨x, ?_⟩
    intro n hn
    rw [← intertwine]
    exact agrees n hn
  exact ⟨⟨p.val, compatible⟩, rfl⟩

end ObservationalSUCC.SwarmX01CompletionTransport
