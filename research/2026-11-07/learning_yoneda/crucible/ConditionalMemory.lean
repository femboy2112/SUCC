/-!
Conditional historical memory, a small algebraic certificate.
Lean 4.14 core only. Existing SUCC O65 supplies the classical graph-coloring
interpretation. This file certifies only the conditional decoder equivalence,
its obstruction, and an explicit C5 alphabet witness. It does not certify
BBP analysis, graph chromatic optimality in general, or any normality theorem.
-/
set_option autoImplicit false
namespace LearningYoneda.Crucible
universe u v w z r

def Consistent {H : Type u} {T : Type v} {P : Type w}
    {M : Type z} {A : Type r}
    (transcript : H → T) (physical : H → P) (target : H → A)
    (memory : T → M) : Prop :=
  ∀ x y, physical x = physical y →
    memory (transcript x) = memory (transcript y) → target x = target y

/-- Necessity does not assume the observer can access the whole history. -/
theorem decoder_requires_consistency
    {H : Type u} {T : Type v} {P : Type w} {M : Type z} {A : Type r}
    (transcript : H → T) (physical : H → P) (target : H → A)
    (memory : T → M) (decode : P → M → A)
    (correct : ∀ x, decode (physical x) (memory (transcript x)) = target x) :
    Consistent transcript physical target memory := by
  intro x y hp hm
  rw [← correct x, ← correct y, hp, hm]

/-- A section is required only for realized physical-memory pairs. -/
def Realized {H : Type u} {T : Type v} {P : Type w} {M : Type z}
    (transcript : H → T) (physical : H → P) (memory : T → M) :=
  { pair : P × M // ∃ h, (physical h, memory (transcript h)) = pair }

def report {H : Type u} {T : Type v} {P : Type w} {M : Type z}
    (transcript : H → T) (physical : H → P) (memory : T → M) (h : H) :
    Realized transcript physical memory :=
  ⟨(physical h, memory (transcript h)), h, rfl⟩

theorem realized_decoder_iff_consistent
    {H : Type u} {T : Type v} {P : Type w} {M : Type z} {A : Type r}
    (transcript : H → T) (physical : H → P) (target : H → A)
    (memory : T → M) :
    (∃ decode : Realized transcript physical memory → A,
      ∀ h, decode (report transcript physical memory h) = target h) ↔
    Consistent transcript physical target memory := by
  constructor
  · rintro ⟨decode, correct⟩ x y hp hm
    have same : report transcript physical memory x =
        report transcript physical memory y := by
      apply Subtype.eq
      exact Prod.ext hp hm
    rw [← correct x, ← correct y, same]
  · intro consistent
    classical
    let representative : Realized transcript physical memory → H :=
      fun pair => Classical.choose pair.property
    let decode : Realized transcript physical memory → A :=
      fun pair => target (representative pair)
    refine ⟨decode, ?_⟩
    intro h
    have witness := Classical.choose_spec
      (report transcript physical memory h).property
    exact consistent (representative (report transcript physical memory h)) h
      (congrArg Prod.fst witness) (congrArg Prod.snd witness)

/-- If the accessible transcript and physical state both alias opposite
targets, no amount of transcript-only memory can repair the missing access. -/
theorem hidden_conflict_blocks_all_memory
    {H : Type u} {T : Type v} {P : Type w} {M : Type z} {A : Type r}
    (transcript : H → T) (physical : H → P) (target : H → A)
    (x y : H) (ht : transcript x = transcript y)
    (hp : physical x = physical y) (bad : target x ≠ target y) :
    ¬ ∃ memory : T → M, Consistent transcript physical target memory := by
  rintro ⟨memory, sound⟩
  exact bad (sound x y hp (congrArg memory ht))

/-- Five adjacent inequalities cannot be satisfied with a binary alphabet. -/
theorem c5_has_no_binary_code (a b c d e : Bool) :
    ¬ (a ≠ b ∧ b ≠ c ∧ c ≠ d ∧ d ≠ e ∧ e ≠ a) := by
  cases a <;> cases b <;> cases c <;> cases d <;> cases e <;> decide

/-- A three-symbol alphabet suffices for this explicitly listed C5. -/
theorem c5_three_symbols_work :
    (0 : Fin 3) ≠ 1 ∧ (1 : Fin 3) ≠ 0 ∧
    (0 : Fin 3) ≠ 1 ∧ (1 : Fin 3) ≠ 2 ∧ (2 : Fin 3) ≠ 0 := by
  decide

#print axioms decoder_requires_consistency
#print axioms realized_decoder_iff_consistent
#print axioms hidden_conflict_blocks_all_memory
#print axioms c5_has_no_binary_code
#print axioms c5_three_symbols_work
end LearningYoneda.Crucible
