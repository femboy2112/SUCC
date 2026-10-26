import Std.Tactic

/-!
# Prime-clock complete-period projection: finite algebraic kernel

Lean 4.14.0; no mathlib. All claims are finite algebraic identities.
The coefficient type is any supplied additive commutative monoid with a
left-distributive multiplication annihilating zero. Thus no analytic, prime,
BBP, complex-exponential, or asymptotic fact is postulated by this file.

The paper applies `periodic_contraction` to complex coefficients and divides
by B*L (B,L positive). Complex Hilbert orthogonality and the BGK theorem are
not formalized here. No axioms or sorry declarations.
-/

namespace ObservationalSUCC.PrimeClockProjection

class SumAlgebra (α : Type u) extends Zero α, Add α, Mul α where
  add_zero (a : α) : a + 0 = a
  zero_add (a : α) : 0 + a = a
  add_assoc (a b c : α) : (a + b) + c = a + (b + c)
  add_comm (a b : α) : a + b = b + a
  mul_zero (a : α) : a * 0 = 0
  mul_add (a b c : α) : a * (b + c) = a * b + a * c

variable {α : Type u} [SumAlgebra α]

instance : Std.Associative (fun a b : α => a + b) :=
  ⟨SumAlgebra.add_assoc⟩
instance : Std.Commutative (fun a b : α => a + b) :=
  ⟨SumAlgebra.add_comm⟩

def finiteSum : Nat → (Nat → α) → α
  | 0, _ => 0
  | n + 1, f => finiteSum n f + f n

@[simp] theorem finiteSum_zero (f : Nat → α) : finiteSum 0 f = 0 := rfl
@[simp] theorem finiteSum_succ (n : Nat) (f : Nat → α) :
    finiteSum (n+1) f = finiteSum n f + f n := rfl

@[simp] theorem finiteSum_all_zero (n : Nat) :
    finiteSum n (fun _ => (0 : α)) = 0 := by
  induction n with
  | zero => rfl
  | succ n ih => simp only [finiteSum_succ, ih, SumAlgebra.add_zero]

/-- Equality is needed only at the finite indices actually read. -/
theorem finiteSum_congr (n : Nat) (f g : Nat → α)
    (equal : ∀ j, j < n → f j = g j) : finiteSum n f = finiteSum n g := by
  induction n with
  | zero => rfl
  | succ n ih =>
    rw [finiteSum_succ, finiteSum_succ]
    rw [ih (by intro j hj; exact equal j (by omega)), equal n (by omega)]

theorem finiteSum_add (n : Nat) (f g : Nat → α) :
    finiteSum n (fun j => f j + g j) = finiteSum n f + finiteSum n g := by
  induction n with
  | zero => simp only [finiteSum_zero, SumAlgebra.add_zero]
  | succ n ih =>
    simp only [finiteSum_succ, ih]
    ac_rfl

theorem finiteSum_mul_left (n : Nat) (a : α) (f : Nat → α) :
    finiteSum n (fun j => a * f j) = a * finiteSum n f := by
  induction n with
  | zero => simp only [finiteSum_zero, SumAlgebra.mul_zero]
  | succ n ih => simp only [finiteSum_succ, ih, SumAlgebra.mul_add]

/-- Finite Fubini: exchange two complete rectangular index ranges. -/
theorem finiteSum_swap (B L : Nat) (f : Nat → Nat → α) :
    finiteSum B (fun b => finiteSum L (fun j => f b j)) =
    finiteSum L (fun j => finiteSum B (fun b => f b j)) := by
  induction B with
  | zero => simp only [finiteSum_zero, finiteSum_all_zero]
  | succ B ih =>
    simp only [finiteSum_succ, ih, finiteSum_add]

/-- Concatenate adjacent finite intervals, retaining every boundary term. -/
theorem finiteSum_append (M N : Nat) (f : Nat → α) :
    finiteSum (M+N) f =
    finiteSum M f + finiteSum N (fun j => f (M+j)) := by
  induction N with
  | zero => simp only [Nat.add_zero, finiteSum_zero, SumAlgebra.add_zero]
  | succ N ih =>
    simp only [Nat.add_succ, finiteSum_succ, ih, SumAlgebra.add_assoc]

/-- Every t < B*L appears once as t=b*L+j, b<B, j<L. -/
theorem finiteSum_blocks (B L : Nat) (f : Nat → α) :
    finiteSum (B*L) f =
    finiteSum B (fun b => finiteSum L (fun j => f (b*L+j))) := by
  induction B with
  | zero => simp only [Nat.zero_mul, finiteSum_zero]
  | succ B ih =>
    rw [Nat.succ_mul, finiteSum_append, finiteSum_succ, ih]

/-- Exact contraction against a clock constant on each repeated position.
The hypothesis is deliberately explicit: no periodicity is inferred from a
source name or from numerical agreement. Degenerate B=0 or L=0 is valid for
the sum identity; normalized means separately require B,L positive. -/
theorem periodic_contraction (B L : Nat) (u v : Nat → α)
    (periodic : ∀ b j, b < B → j < L → u (b*L+j) = u j) :
    finiteSum (B*L) (fun t => u t * v t) =
    finiteSum L (fun j => u j *
      finiteSum B (fun b => v (b*L+j))) := by
  rw [finiteSum_blocks, finiteSum_swap]
  apply finiteSum_congr
  intro j hj
  calc
    finiteSum B (fun b => u (b*L+j) * v (b*L+j)) =
        finiteSum B (fun b => u j * v (b*L+j)) := by
      apply finiteSum_congr
      intro b hb
      rw [periodic b j hb hj]
    _ = u j * finiteSum B (fun b => v (b*L+j)) :=
      finiteSum_mul_left B (u j) (fun b => v (b*L+j))

/-- Fiber-zero source information cannot couple to a repeated prime clock. -/
theorem zero_fiber_annihilation (B L : Nat) (u v : Nat → α)
    (periodic : ∀ b j, b < B → j < L → u (b*L+j) = u j)
    (zero_fibers : ∀ j, j < L → finiteSum B (fun b => v (b*L+j)) = 0) :
    finiteSum (B*L) (fun t => u t * v t) = 0 := by
  rw [periodic_contraction B L u v periodic]
  calc
    finiteSum L (fun j => u j * finiteSum B (fun b => v (b*L+j))) =
        finiteSum L (fun _ => (0 : α)) := by
      apply finiteSum_congr
      intro j hj
      rw [zero_fibers j hj, SumAlgebra.mul_zero]
    _ = 0 := finiteSum_all_zero L

/-- Equal fiber sums are indistinguishable by every repeated clock weight. -/
theorem equal_fibers_equal_coupling (B L : Nat) (u v w : Nat → α)
    (periodic : ∀ b j, b < B → j < L → u (b*L+j) = u j)
    (equal_fibers : ∀ j, j < L →
      finiteSum B (fun b => v (b*L+j)) = finiteSum B (fun b => w (b*L+j))) :
    finiteSum (B*L) (fun t => u t * v t) =
    finiteSum (B*L) (fun t => u t * w t) := by
  rw [periodic_contraction B L u v periodic, periodic_contraction B L u w periodic]
  apply finiteSum_congr
  intro j hj
  rw [equal_fibers j hj]

/-- An explicit familiar model proves the algebraic hypotheses consistent. -/
instance : SumAlgebra Int where
  zero := 0
  add := Int.add
  mul := Int.mul
  add_zero := Int.add_zero
  zero_add := Int.zero_add
  add_assoc := Int.add_assoc
  add_comm := Int.add_comm
  mul_zero := Int.mul_zero
  mul_add := Int.mul_add

#print axioms periodic_contraction
#print axioms zero_fiber_annihilation
#print axioms equal_fibers_equal_coupling

end ObservationalSUCC.PrimeClockProjection
