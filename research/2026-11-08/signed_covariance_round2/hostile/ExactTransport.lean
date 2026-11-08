/-!
Exact unwrapped affine transport, Lean 4.14 core only.

The carrier is Int: for a fixed finite rational source horizon, a common
denominator turns its states and forcing into integers. This file proves
only the resulting recurrence algebra. The choice of that denominator,
the four original rational poles, prime principal parts, complex characters,
analytic estimates, and pi normality are NOT formalized here.
-/
set_option autoImplicit false
namespace SignedCovariance.Hostile

/-- Every source event is kept in chronological order; time zero is explicit. -/
def state (r : Nat → Int) (seed : Int) : Nat → Int
  | 0 => seed
  | n + 1 => 16 * state r seed n + r (n + 1)

/-- Unwrapped finite forcing accumulated after time n. -/
def window (r : Nat → Int) (n : Nat) : Nat → Int
  | 0 => 0
  | ell + 1 => 16 * window r n ell + r (n + ell + 1)

theorem literal_zero_boundary (r : Nat → Int) : state r 0 0 = 0 := rfl

theorem exact_transport (r : Nat → Int) (seed : Int) (n ell : Nat) :
    state r seed (n + ell) = (16 : Int) ^ ell * state r seed n + window r n ell := by
  induction ell with
  | zero => simp [window]
  | succ ell ih =>
    simpa [state, window, Int.mul_add, Int.pow_succ', Int.mul_assoc,
      Int.add_assoc, Nat.add_assoc] using
      congrArg (fun x : Int => 16 * x + r (n + ell + 1)) ih

/-- Changed seeds retain the same forcing but add the exact expanding term. -/
theorem seed_dependence (r : Nat → Int) (seed : Int) (n : Nat) :
    state r seed n = state r 0 n + (16 : Int) ^ n * seed := by
  induction n with
  | zero => simp [state]
  | succ n ih =>
    simp only [state]
    rw [ih]
    simp [Int.pow_succ', Int.mul_add, Int.mul_assoc,
      Int.add_assoc, Int.add_comm, Int.add_left_comm]

/-- Source transport composes by retaining the first window's expanded value. -/
theorem window_composition (r : Nat → Int) (n a b : Nat) :
    window r n (a + b) = (16 : Int) ^ b * window r n a + window r (n + a) b := by
  induction b with
  | zero => simp [window]
  | succ b ih =>
    simpa [window, Int.mul_add, Int.pow_succ', Int.mul_assoc,
      Int.add_assoc, Nat.add_assoc] using
      congrArg (fun x : Int => 16 * x + r (n + a + b + 1)) ih

#print axioms literal_zero_boundary
#print axioms exact_transport
#print axioms seed_dependence
#print axioms window_composition
end SignedCovariance.Hostile
