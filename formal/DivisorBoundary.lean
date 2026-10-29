import Mathlib.Algebra.BigOperators.Ring
import Mathlib.Data.Nat.Defs
import Mathlib.Tactic.Ring
import Lean.Elab.Tactic.Omega

/-!
The exact finite boundary identity behind the divisor-jump commutator.
The target is any commutative ring (in particular the complex numbers).
No BBP cancellation, spectral claim, or analytic limit is assumed or proved.
The square-root Hilbert normalization and the bijection between pair-space
edges and divisor jumps are proved in the paper dossier, not in this file.
-/

open scoped BigOperators

namespace ObservationalSUCC.DivisorBoundary

variable {R : Type*} [CommRing R]

theorem ray_telescope (f : ℕ → R) (b q : ℕ) :
    (∑ a ∈ Finset.range q, (f ((a + 2) * b) - f ((a + 1) * b))) =
      f ((q + 1) * b) - f b := by
  induction q with
  | zero => simp
  | succ q ih =>
      rw [Finset.sum_range_succ, ih]
      ring

def edgeSum (N : ℕ) (f : ℕ → R) : R :=
  ∑ i ∈ Finset.range N,
    ∑ a ∈ Finset.range (N / (i + 1) - 1),
      (f ((a + 2) * (i + 1)) - f ((a + 1) * (i + 1)))

def boundarySum (N : ℕ) (f : ℕ → R) : R :=
  ∑ i ∈ Finset.range N, f ((N / (i + 1)) * (i + 1))

def selectedSum (N : ℕ) (f : ℕ → R) : R :=
  ∑ i ∈ Finset.range N, f (i + 1)

theorem signed_boundary_identity (N : ℕ) (f : ℕ → R) :
    edgeSum N f = boundarySum N f - selectedSum N f := by
  unfold edgeSum boundarySum selectedSum
  rw [← Finset.sum_sub_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  have hiN : i + 1 ≤ N := by
    have := Finset.mem_range.mp hi
    omega
  have hq : 1 ≤ N / (i + 1) :=
    (Nat.le_div_iff_mul_le (by omega)).mpr (by simpa using hiN)
  have heq : N / (i + 1) - 1 + 1 = N / (i + 1) := by omega
  rw [ray_telescope, heq]

theorem flat_phase_boundary (N : ℕ) (c : R) :
    boundarySum N (fun _ => c) = selectedSum N (fun _ => c) := by
  rfl

theorem flat_phase_edge_zero (N : ℕ) (c : R) :
    edgeSum N (fun _ => c) = 0 := by
  rw [signed_boundary_identity, flat_phase_boundary, sub_self]

end ObservationalSUCC.DivisorBoundary

#print axioms ObservationalSUCC.DivisorBoundary.ray_telescope
#print axioms ObservationalSUCC.DivisorBoundary.signed_boundary_identity
#print axioms ObservationalSUCC.DivisorBoundary.flat_phase_boundary
#print axioms ObservationalSUCC.DivisorBoundary.flat_phase_edge_zero
