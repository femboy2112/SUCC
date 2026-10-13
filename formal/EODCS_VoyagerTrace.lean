/-!
# VOYAGER I: universal observational trace and finite-refutation compactness

Pinned Lean 4.14, no mathlib, no admitted assertions.
An arbitrary source S with lawful actions A and a report q admits the
canonical trace s |-> (w |-> q(U_w(s))) in O^(A*). The trace remembers every
finite allowable experiment without identifying hidden source ontology.

Finite-source dichotomy: if a *complete* source enumeration has N entries,
an unrealizable entire trace has a refuting list of N finite probes (one
per source entry). Conversely, if every finite list of probes is matched
by SOME source state, ONE source state matches all probes.

This is a mathematical finite-source theorem, not physical source
authentication, a bound on actual execution, or an RH proof.
-/
namespace ObservationalSUCC

universe u v w z

def VoyagerRun {S : Type u} {A : Type v}
    (step : A → S → S) : S → List A → S
  | s, [] => s
  | s, a :: rest => VoyagerRun step (step a s) rest

def VoyagerTrace {S : Type u} {A : Type v} {O : Type w}
    (step : A → S → S) (report : S → O)
    (s : S) (word : List A) : O :=
  report (VoyagerRun step s word)

/-- The left-derivative of a future trace is exactly the trace at the
source successor. This is a lawful context-transport identity. -/
theorem voyager_trace_derivative
    {S : Type u} {A : Type v} {O : Type w}
    (step : A → S → S) (report : S → O)
    (a : A) (s : S) (word : List A) :
    VoyagerTrace step report (step a s) word =
      VoyagerTrace step report s (a :: word) := by
  rfl

/-- Every source/observation-preserving morphism induces identical trace
laws. This requires the *actual action squares*, not equal-looking labels. -/
theorem voyager_run_morphism
    {S : Type u} {T : Type v} {A : Type w}
    (stepS : A → S → S) (stepT : A → T → T) (f : S → T)
    (square : ∀ a s, f (stepS a s) = stepT a (f s)) :
    ∀ s word, f (VoyagerRun stepS s word) =
      VoyagerRun stepT (f s) word := by
  intro s word
  induction word generalizing s with
  | nil => rfl
  | cons a rest ih =>
      change f (VoyagerRun stepS (stepS a s) rest) =
        VoyagerRun stepT (stepT a (f s)) rest
      calc
        f (VoyagerRun stepS (stepS a s) rest) =
          VoyagerRun stepT (f (stepS a s)) rest := ih (stepS a s)
        _ = VoyagerRun stepT (stepT a (f s)) rest := by
          rw [square a s]

theorem voyager_trace_naturality
    {S : Type u} {T : Type v} {A : Type w} {O : Type z}
    (stepS : A → S → S) (stepT : A → T → T)
    (reportS : S → O) (reportT : T → O) (f : S → T)
    (square : ∀ a s, f (stepS a s) = stepT a (f s))
    (readout : ∀ s, reportT (f s) = reportS s) :
    ∀ s word, VoyagerTrace stepT reportT (f s) word =
      VoyagerTrace stepS reportS s word := by
  intro s word
  unfold VoyagerTrace
  rw [← voyager_run_morphism stepS stepT f square s word]
  exact readout (VoyagerRun stepS s word)

/-- The all-context observational relation is closed under every
authorized state-changing action. -/
theorem voyager_trace_kernel_action_congruence
    {S : Type u} {A : Type v} {O : Type w}
    (step : A → S → S) (report : S → O)
    (s t : S)
    (same : ∀ word, VoyagerTrace step report s word =
      VoyagerTrace step report t word) :
    ∀ a word, VoyagerTrace step report (step a s) word =
      VoyagerTrace step report (step a t) word := by
  intro a word
  rw [voyager_trace_derivative step report a s word,
      voyager_trace_derivative step report a t word]
  exact same (a :: word)

/-- Every source state is a witness for each finite subset of its own
infinite mathematical trace. -/
def FinitelyCompatible {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (profile : W → O) : Prop :=
  ∀ probes : List W,
    ∃ s : S, ∀ w, w ∈ probes → trace s w = profile w

theorem realized_implies_finitely_compatible
    {S : Type u} {W : Type v} {O : Type w}
    (trace : S → W → O) (profile : W → O)
    (actual : ∃ s, ∀ w, trace s w = profile w) :
    FinitelyCompatible trace profile := by
  obtain ⟨s, hs⟩ := actual
  intro probes
  exact ⟨s, fun w _ => hs w⟩

/-- **Finite source refutation dichotomy.** If a global profile is not
realizable by any member of a COMPLETE enumerated finite source S,
one can refute it with at most one probe per listed source state.
No topology, cardinal arithmetic, unverified oracle or empirical source
hypothesis is hidden in this finite combinatorial theorem. -/
theorem finite_enumeration_realization_or_refutation
    {S : Type u} {W : Type v} {O : Type w}
    (states : List S) (cover : ∀ s : S, s ∈ states)
    (trace : S → W → O) (profile : W → O) :
    (∃ s, ∀ w, trace s w = profile w) ∨
    (∃ probes : List W,
        probes.length = states.length ∧
        ∀ s : S, ∃ w, w ∈ probes ∧ trace s w ≠ profile w) := by
  classical
  by_cases global : ∃ s : S, ∀ w, trace s w = profile w
  · exact Or.inl global
  · right
    have mismatches : ∀ s : S, ∃ w, trace s w ≠ profile w := by
      intro s
      by_cases witnessed : ∃ w, trace s w ≠ profile w
      · exact witnessed
      · apply False.elim
        apply global
        refine ⟨s, ?_⟩
        intro w
        by_cases equal : trace s w = profile w
        · exact equal
        · exact False.elim (witnessed ⟨w, equal⟩)
    let chooseWord : S → W := fun s => Classical.choose (mismatches s)
    refine ⟨states.map chooseWord, ?_, ?_⟩
    · simp
    · intro s
      refine ⟨chooseWord s, ?_, ?_⟩
      · exact List.mem_map.mpr ⟨s, cover s, rfl⟩
      · exact Classical.choose_spec (mismatches s)

/-- **Finite-source realization theorem.** Every finitely compatible
global observation profile is represented by ONE original source state
if the exact source class has a complete finite enumeration.
Infinitary source classes do NOT satisfy this theorem without additional
compactness/realization hypotheses. -/
theorem finite_enumeration_compatible_implies_realized
    {S : Type u} {W : Type v} {O : Type w}
    (states : List S) (cover : ∀ s : S, s ∈ states)
    (trace : S → W → O) (profile : W → O)
    (compatible : FinitelyCompatible trace profile) :
    ∃ s, ∀ w, trace s w = profile w := by
  rcases finite_enumeration_realization_or_refutation
      states cover trace profile with original | ⟨probes, _, forbids⟩
  · exact original
  · obtain ⟨s, agreesOnList⟩ := compatible probes
    obtain ⟨w, mem, wrong⟩ := forbids s
    exact False.elim (wrong (agreesOnList w mem))

end ObservationalSUCC
