import Std.Tactic

/-! Discrete SWM-E33 transport lemmas, pinned Lean 4.14.
No claim about cyclic stabilizer completeness, Euler logarithms, Gamma,
Weil positivity or RH is kernel-checked in this file. -/

namespace SwarmArithmetic

structure Affine where
  slope : Nat
  offset : Nat
  deriving DecidableEq

def Affine.apply (a : Affine) (n : Nat) : Nat := a.slope * n + a.offset

def Affine.compose (a b : Affine) : Affine :=
  ⟨a.slope * b.slope, a.slope * b.offset + a.offset⟩

theorem affine_apply_compose (a b : Affine) (n : Nat) :
    (a.compose b).apply n = a.apply (b.apply n) := by
  simp [Affine.compose, Affine.apply, Nat.mul_add, Nat.mul_assoc, Nat.add_assoc]

theorem affine_compose_assoc (a b c : Affine) :
    (a.compose b).compose c = a.compose (b.compose c) := by
  cases a
  cases b
  cases c
  simp [Affine.compose, Nat.mul_add, Nat.mul_assoc, Nat.add_assoc]

theorem affine_representation_faithful (a b : Affine)
    (same : ∀ n, a.apply n = b.apply n) : a = b := by
  have hzero := same 0
  have hone := same 1
  simp [Affine.apply] at hzero hone
  have hslope : a.slope = b.slope := by omega
  cases a
  cases b
  simp_all

theorem successor_shape (h : Nat → Nat)
    (succ : ∀ n, h (n+1) = h n + 1) (n : Nat) :
    h n = h 0 + n := by
  induction n with
  | zero => simp
  | succ n ih =>
      rw [succ, ih]
      simp [Nat.add_assoc]

theorem successor_double_rigidity (h : Nat → Nat)
    (succ : ∀ n, h (n+1) = h n + 1)
    (double : ∀ n, h (2*n) = 2*h n) :
    ∀ n, h n = n := by
  have hzero := double 0
  simp at hzero
  have base : h 0 = 0 := by omega
  intro n
  rw [successor_shape h succ n, base]
  simp

theorem no_classifier_on_equal_report
    {S O : Type} (report : S → O) (target : S → Bool) (a b : S)
    (same : report a = report b) (different : target a ≠ target b) :
    ¬ ∃ classify : O → Bool, ∀ s, classify (report s) = target s := by
  rintro ⟨classify, correct⟩
  apply different
  calc
    target a = classify (report a) := (correct a).symm
    _ = classify (report b) := congrArg classify same
    _ = target b := correct b

end SwarmArithmetic
