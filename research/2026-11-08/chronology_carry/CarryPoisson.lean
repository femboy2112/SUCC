import Std

/-!
Kernel-checkable integer-coordinate skeleton of the finite carry Poisson
identity. Rational Gaussian tables can be cleared to a common denominator,
and the theorem applied to each coordinate separately.

NOT formalized here: BBP source bounds, phase intervals, complex norms,
equidistribution, the finite-field clock, or any asymptotic cancellation.
There are no user-added axioms or admitted lemmas in this file. The printed
axiom audit records Lean's standard logical dependencies.
-/

namespace SUCC.ChronologyCarry

def total (f : Nat → Int) : Nat → Int
  | 0 => 0
  | n+1 => total f n + f n

theorem difference_telescope (f : Nat → Int) (n : Nat) :
    total (fun j => f (j+1) - f j) n = f n - f 0 := by
  induction n with
  | zero => simp [total]
  | succ n ih => simp only [total]; omega

theorem poisson_sum (g psi p : Nat → Int) (mu : Int)
    (law : ∀ j, g j = mu + psi j - p j) (n : Nat) :
    total g n = (n : Int)*mu + psi 0 - psi n +
      total (fun j => psi (j+1) - p j) n := by
  induction n with
  | zero => simp [total]
  | succ n ih =>
    simp only [total]
    have cast : ((n+1 : Nat) : Int) = (n : Int)+1 := by omega
    rw [cast, Int.add_mul, Int.one_mul]
    have step := law n
    omega

theorem poisson_sum_with_defect (g psi p defect : Nat → Int) (mu : Int)
    (law : ∀ j, g j = mu + psi j - p j + defect j) (n : Nat) :
    total g n = (n : Int)*mu + psi 0 - psi n +
      total (fun j => psi (j+1) - p j) n + total defect n := by
  induction n with
  | zero => simp [total]
  | succ n ih =>
    simp only [total]
    have cast : ((n+1 : Nat) : Int) = (n : Int)+1 := by omega
    rw [cast, Int.add_mul, Int.one_mul]
    have step := law n
    omega

theorem frozen_control_split (f g : Nat → Int) (n : Nat) :
    total f n = total g n + total (fun j => f j - g j) n := by
  induction n with
  | zero => simp [total]
  | succ n ih => simp only [total]; omega

#print axioms difference_telescope
#print axioms poisson_sum
#print axioms poisson_sum_with_defect
#print axioms frozen_control_split

end SUCC.ChronologyCarry
