/-!
Exact integer coefficient transport for Fibonacci circle returns (Lean core).
A pair (a,b) denotes a+b*alpha, subject only in the PAPER interpretation to
alpha^2=1-alpha. This file verifies the integer recurrences. It does not
formalize the real root, its irrationality, circle reconstruction, curvature,
noise bounds, Fourier frames, BBP source authentication, or pi normality.
-/
set_option autoImplicit false
namespace SignalFrontier.FibonacciClock

abbrev Coeff := Int × Int

def fibPair : Nat → Coeff
  | 0 => (0, 1)
  | n + 1 => ((fibPair n).2, (fibPair n).1 + (fibPair n).2)

/-- Multiplication by -alpha in Z[alpha]/(alpha^2+alpha-1). -/
def negAlpha (x : Coeff) : Coeff := (-x.2, x.2 - x.1)

def returnCoeff : Nat → Coeff
  | 0 => (0, 1)
  | n + 1 => negAlpha (returnCoeff n)

theorem return_coefficients (n : Nat) :
    returnCoeff n = (-(fibPair n).1, (fibPair n).2) := by
  induction n with
  | zero => rfl
  | succ n ih =>
    simp [returnCoeff, fibPair, negAlpha, ih, Int.sub_eq_add_neg,
      Int.add_comm]

/-- The signed return at clock F_(n+1) is F_(n+1)*alpha-F_n. -/
theorem exact_one_step (n : Nat) :
    returnCoeff (n+1) = (-(fibPair n).2,
      (fibPair n).1 + (fibPair n).2) := by
  rw [return_coefficients]
  rfl

/-- Iterated resolution transport preserves the accumulated history. -/
def advance (k : Nat) (x : Coeff) : Coeff :=
  match k with
  | 0 => x
  | j + 1 => negAlpha (advance j x)

theorem resolution_transport (n k : Nat) :
    returnCoeff (n+k) = advance k (returnCoeff n) := by
  induction k with
  | zero => rfl
  | succ k ih =>
    simpa [returnCoeff, advance, Nat.add_assoc] using congrArg negAlpha ih

#print axioms return_coefficients
#print axioms exact_one_step
#print axioms resolution_transport
end SignalFrontier.FibonacciClock
