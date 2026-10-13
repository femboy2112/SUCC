import Std.Tactic
/-!
# Voyager III: quantified finite-horizon memory debt

A deterministic finite source cannot pass through a long interval of
zero reports and then a one report while repeating an intermediate
source state. If the output is 0 for all times start <= n < stop
and is 1 at stop, the source states on [start,stop] are pairwise
distinct. In the power-of-two pulse example, take start=2^k+1,
stop=2^(k+1): an exact observation through stop forces at least 2^k
distinct source states.

The proof is VALID for arbitrary deterministic stationary source S and
does not read a global completion, execute infinitely many observations,
or claim a physical memory system was actually inspected.
-/
namespace ObservationalSUCC

universe u

def MemoryIter {S : Type u} (step : S → S) : Nat → S → S
  | 0, s => s
  | n+1, s => step (MemoryIter step n s)

theorem memory_iter_add {S : Type u}
    (step : S → S) (s : S) (n k : Nat) :
    MemoryIter step (n+k) s =
      MemoryIter step k (MemoryIter step n s) := by
  induction k with
  | zero =>
      simp [MemoryIter]
  | succ k ih =>
      rw [Nat.add_succ]
      change step (MemoryIter step (n+k) s) =
        step (MemoryIter step k (MemoryIter step n s))
      exact congrArg step ih

theorem repeated_source_state_repeats_all_later_reports
    {S : Type u} (step : S → S) (report : S → Bool)
    (s : S) (i j : Nat)
    (same : MemoryIter step i s = MemoryIter step j s) :
    ∀ k, report (MemoryIter step (i+k) s) =
      report (MemoryIter step (j+k) s) := by
  intro k
  rw [memory_iter_add step s i k,
      memory_iter_add step s j k, same]

/-- A zero-report gap followed by a one-report endpoint has no
repeated original source state anywhere in that half-open interval
together with the one endpoint. -/
theorem zero_gap_forces_distinct_source_states
    {S : Type u} (step : S → S) (report : S → Bool)
    (s : S) (start stop i j : Nat)
    (order : start ≤ i ∧ i < j ∧ j ≤ stop)
    (zeros : ∀ t : Nat, start ≤ t → t < stop →
       report (MemoryIter step t s) = false)
    (one : report (MemoryIter step stop s) = true) :
    MemoryIter step i s ≠ MemoryIter step j s := by
  intro same
  have runEqual := repeated_source_state_repeats_all_later_reports
     step report s i j same (stop-j)
  have earlier : start ≤ i+(stop-j) ∧ i+(stop-j) < stop := by
    omega
  have earlierZero :=
    zeros (i+(stop-j)) earlier.1 earlier.2
  have laterOne :
      report (MemoryIter step (j+(stop-j)) s) = true := by
    have h : j+(stop-j) = stop := by omega
    rw [h]
    exact one
  rw [earlierZero, laterOne] at runEqual
  cases runEqual

/-- The p states at the positions p+1,...,2p are all distinct if
the report contains the required zero gap ending at the next pulse.
The finite cardinal N>=p consequence is ordinary pigeonhole. -/
theorem pulse_gap_injective_states
    {S : Type u} (step : S → S) (report : S → Bool)
    (s : S) (p : Nat) (positive : 0 < p)
    (zeros : ∀ t : Nat, p+1 ≤ t → t < 2*p →
       report (MemoryIter step t s) = false)
    (one : report (MemoryIter step (2*p) s) = true) :
    Function.Injective
      (fun i : Fin p => MemoryIter step (p+1+i.val) s) := by
  intro i j eq
  by_cases hij : i.val < j.val
  · have notSame := zero_gap_forces_distinct_source_states
        step report s (p+1) (2*p) (p+1+i.val) (p+1+j.val)
        (by constructor <;> omega) zeros one
    exact False.elim (notSame eq)
  · by_cases hji : j.val < i.val
    · have notSame := zero_gap_forces_distinct_source_states
          step report s (p+1) (2*p) (p+1+j.val) (p+1+i.val)
          (by constructor <;> omega) zeros one
      exact False.elim (notSame eq.symm)
    · apply Fin.ext
      omega

end ObservationalSUCC
