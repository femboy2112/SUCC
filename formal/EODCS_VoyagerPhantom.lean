/-!
# VOYAGER II — source-realization gap at the ideal observational limit

A mathematical infinite future record can be compatible with every
finite prefix without being realized by any original source state.

Source S: binary streams that become permanently false at some finite
source-dependent time (eventually-zero).
Instrument: head report; lawful successor: left shift.

For every finite horizon h, one genuine S-state matches the all-true
profile for its first h observations. There is no ONE S-state matching
all future reports of that profile. These statements do not depend on
floating point calculations, RH zeros, or a physical infinite experiment.
-/
namespace ObservationalSUCC

def EventuallyZero (stream : Nat → Bool) : Prop :=
  ∃ N : Nat, ∀ n : Nat, N ≤ n → stream n = false

def ZeroTailApproximation (h : Nat) (n : Nat) : Bool :=
  if n < h then true else false

theorem zero_tail_approximant_in_source (h : Nat) :
    EventuallyZero (ZeroTailApproximation h) := by
  refine ⟨h, ?_⟩
  intro n hn
  by_cases hlt : n < h
  · have impossible : n < n := Nat.lt_of_lt_of_le hlt hn
    exact False.elim ((Nat.lt_irrefl n) impossible)
  · simp [ZeroTailApproximation, hlt]

theorem zero_tail_matches_first_h_reports (h : Nat) :
    ∀ n : Nat, n < h → ZeroTailApproximation h n = true := by
  intro n hn
  simp [ZeroTailApproximation, hn]

theorem all_true_finite_horizon_source_realizable :
    ∀ h : Nat, ∃ stream : Nat → Bool,
      EventuallyZero stream ∧
      (∀ n : Nat, n < h → stream n = true) := by
  intro h
  exact ⟨ZeroTailApproximation h,
         zero_tail_approximant_in_source h,
         zero_tail_matches_first_h_reports h⟩

theorem all_true_not_originally_realizable :
    ¬ EventuallyZero (fun _ : Nat => true) := by
  rintro ⟨N, allLaterFalse⟩
  have impossible : true = false := allLaterFalse N (Nat.le_refl N)
  cases impossible

def StreamShift (stream : Nat → Bool) (n : Nat) : Bool :=
  stream (n+1)

def IteratedStreamShift : Nat → (Nat → Bool) → (Nat → Bool)
  | 0, stream => stream
  | k+1, stream => IteratedStreamShift k (StreamShift stream)

theorem shift_head_observes_original_index (h : Nat) (stream : Nat → Bool) :
    IteratedStreamShift h stream 0 = stream h := by
  induction h generalizing stream with
  | zero => rfl
  | succ h ih =>
      change IteratedStreamShift h (StreamShift stream) 0 =
        stream (h+1)
      exact ih (StreamShift stream)

/-- Eventual-zero original carriers remain in their carrier class after
one shift, so the negative result is not due to an illegal update. -/
theorem eventually_zero_closed_under_shift
    (stream : Nat → Bool) (h : EventuallyZero stream) :
    EventuallyZero (StreamShift stream) := by
  obtain ⟨N, tail⟩ := h
  refine ⟨N, ?_⟩
  intro n hn
  exact tail (n+1) (Nat.le_trans hn (Nat.le_succ n))

/-- The syntactically compatible all-true infinite profile is NOT an
original state in this source type, even though every finite observation
horizon has an exact lawful source witness. -/
theorem finite_stage_compatibility_does_not_force_actualization :
    (∀ h : Nat, ∃ stream : Nat → Bool,
      EventuallyZero stream ∧
      ∀ n : Nat, n < h → stream n = true)
    ∧
    ¬ (∃ stream : Nat → Bool,
       EventuallyZero stream ∧ ∀ n : Nat, stream n = true) := by
  constructor
  · exact all_true_finite_horizon_source_realizable
  · rintro ⟨stream, ⟨N, tail⟩, allTrue⟩
    have bad : stream N = false := tail N (Nat.le_refl N)
    have good : stream N = true := allTrue N
    rw [good] at bad
    cases bad

end ObservationalSUCC
