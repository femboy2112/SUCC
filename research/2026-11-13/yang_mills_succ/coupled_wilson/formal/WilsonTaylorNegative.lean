import Std
/-!
Exact rational certificate for a proposed SU(2) reflection-positivity
counterexample. The identification of the supplied moment functional with
Haar integration is separate. This file proves the moment-to-Gram computation
and its negative direction.
No claim about continuum Yang-Mills endpoints is made.
-/
namespace SUCC.WilsonTaylor

def moment (n : Nat) : Rat :=
  match n with
  | 0 => 1
  | 2 => 1 / 4
  | 4 => 1 / 8
  | 6 => 5 / 64
  | _ => 0

-- Integrate x^i y^j [1 + 2(x+y) + 2(x+y)^2 + (x+y)^3 + (x+y)^4/4]
-- using the product functional M(x^a y^b) = moment a * moment b.
-- Every argument to moment is at most 6; values above 6 are unused.
def derivedGram (i j : Fin 3) : Rat :=
  moment i.val * moment j.val +
  2 * (moment (i.val+1) * moment j.val + moment i.val * moment (j.val+1)) +
  2 * (moment (i.val+2) * moment j.val + 2 * moment (i.val+1) * moment (j.val+1) +
    moment i.val * moment (j.val+2)) +
  (moment (i.val+3) * moment j.val + 3 * moment (i.val+2) * moment (j.val+1) +
    3 * moment (i.val+1) * moment (j.val+2) + moment i.val * moment (j.val+3)) +
  (1 / 4) * (moment (i.val+4) * moment j.val +
    4 * moment (i.val+3) * moment (j.val+1) +
    6 * moment (i.val+2) * moment (j.val+2) +
    4 * moment (i.val+1) * moment (j.val+3) + moment i.val * moment (j.val+4))

def gram (i j : Fin 3) : Rat :=
  match i.val, j.val with
  | 0, 0 => 69 / 32
  | 0, 1 | 1, 0 => 13 / 16
  | 0, 2 | 2, 0 => 179 / 256
  | 1, 1 => 5 / 16
  | 1, 2 | 2, 1 => 1 / 4
  | _, _ => 113 / 512

theorem moment_to_gram : ∀ i j : Fin 3, derivedGram i j = gram i j := by decide +kernel

def quadratic (v : Fin 3 → Rat) : Rat :=
  v 0 * gram 0 0 * v 0 + v 0 * gram 0 1 * v 1 + v 0 * gram 0 2 * v 2 +
  v 1 * gram 1 0 * v 0 + v 1 * gram 1 1 * v 1 + v 1 * gram 1 2 * v 2 +
  v 2 * gram 2 0 * v 0 + v 2 * gram 2 1 * v 1 + v 2 * gram 2 2 * v 2

def witness (i : Fin 3) : Rat := if i.val = 0 then -4 else 5

theorem negative_direction : quadratic witness = -71 / 512 := by decide +kernel

theorem partition_positive : (0 : Rat) < gram 0 0 := by decide +kernel

theorem normalized_negative_direction :
    quadratic witness / gram 0 0 = -71 / 1104 := by decide +kernel

theorem not_positive_semidefinite : ¬ (∀ v : Fin 3 → Rat, 0 ≤ quadratic v) := by
  intro h
  exact (show ¬ ((0 : Rat) ≤ quadratic witness) by decide +kernel) (h witness)

#print axioms moment_to_gram
#print axioms negative_direction
#print axioms partition_positive
#print axioms normalized_negative_direction
#print axioms not_positive_semidefinite
end SUCC.WilsonTaylor
