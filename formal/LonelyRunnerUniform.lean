import Std.Tactic

/-!
Finite combinatorial core of the binary/3 fixed-phase local-rule obstruction.
True means a removed binary velocity, false means retained with phase -delta.
The paper proves that locality is equivalent to this pattern condition.
This file proves the all-length packing bound and the positive-gain depth
consequence. It does not formalize circle distance, affine phase resonance,
the real-polyhedral reduction, or the shifted Lonely Runner conjecture.
-/

namespace ObservationalSUCC.LonelyRunnerUniform

def removedCount : List Bool → Nat
  | [] => 0
  | false :: xs => removedCount xs
  | true :: xs => removedCount xs + 1

def admissible : List Bool → Prop
  | [] => True
  | false :: xs => admissible xs
  | true :: false :: xs => admissible xs
  | true :: true :: _ => False
  | [true] => False

/-- Every removal needs a distinct immediately following retained runner. -/
theorem packing_bound (xs : List Bool) (h : admissible xs) :
    2 * removedCount xs ≤ xs.length := by
  match xs with
  | [] => simp [removedCount]
  | false :: ys =>
      have ih := packing_bound ys h
      simp only [removedCount, List.length_cons]
      omega
  | true :: false :: ys =>
      have ih := packing_bound ys h
      simp only [removedCount, List.length_cons]
      omega
  | true :: true :: ys => exact False.elim h
  | [true] => exact False.elim h
termination_by xs.length

/-- In this family there are J-1 binary positions and gain = removals-1. -/
theorem positive_gain_requires_depth_five (J : Nat) (xs : List Bool)
    (h : admissible xs) (length_eq : xs.length = J-1)
    (gain_positive : 2 ≤ removedCount xs) : 5 ≤ J := by
  have hpack := packing_bound xs h
  omega

theorem first_saving_pattern_admissible :
    admissible [true,false,true,false] := by simp [admissible]

theorem first_saving_pattern_count :
    removedCount [true,false,true,false] = 2 := by decide

theorem first_saving_largest_velocity : 3 * 2^(5+1) = 192 := by decide

end ObservationalSUCC.LonelyRunnerUniform

#print axioms ObservationalSUCC.LonelyRunnerUniform.packing_bound
#print axioms ObservationalSUCC.LonelyRunnerUniform.positive_gain_requires_depth_five
