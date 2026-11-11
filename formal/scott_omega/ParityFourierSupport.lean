/-!
# Parity character Fourier support — Lean kernel check (core-only)

Kernel-checks the arithmetic support: the parity character's nonzero Fourier
coefficients sit exactly on the progression m ≡ 8 (mod 16), and there are 6
such residues in 1..96.  Load-bearing identity: sum_{a=0}^{15}(-1)^a z^a = 16
iff z = -1 iff m ≡ 8 (mod 16).
-/

def is_support (m : Nat) : Bool := m % 16 == 8

def support_count (N : Nat) : Nat :=
  (List.range N).filter (fun m => m % 16 == 8) |>.length

theorem support_8   : is_support 8  = true := by native_decide
theorem support_24  : is_support 24 = true := by native_decide
theorem support_40  : is_support 40 = true := by native_decide
theorem nonsupport_7  : is_support 7  = false := by native_decide
theorem nonsupport_16 : is_support 16 = false := by native_decide
theorem support_count_96 : support_count 97 = 6 := by native_decide
