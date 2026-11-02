/-!
# Prime-Cofactor Non-Conspiracy, Midy Complementarity, and Universal Radix Coercivity
# Standalone Lean 4.14.0 Kernel Certificate (No Mathlib)

Scope and authority:
This file proves the finite integer and modular algebraic cores underlying the
2026-11-02 theorem-building mega-round:
1. Euclidean Primary-Cofiber Step Decomposition and Carry-Digit Bound (`0 ≤ κ < 16`).
2. Midy Hexadecimal Carry-Complement Law (`κ_j + κ_{j+M} = 15`) and exact
   half-period `p`-primary annihilation for even-order primes.
3. Universal Radix-`B` Coercivity Identity `(B+1)a^2 + B(B+1)b^2 - (a+Bb)^2 = B(a-b)^2`,
   its `(B+1)^2` total-weight law, and the exact AM-GM optimality gap `(x - B)^2`.
4. Prime Stroboscope Chiral Involution `J_4`, fixed-point characterization `A + 4C = 0`,
   authentic BBP invariance, and first-octave `47/15` residue identity.
5. `p ≡ 5 (mod 8)` Quarter-Group Oddness (`((p-1)/4) % 2 = 1`, forcing `ord_p(16)` odd)
   and Laurent Clock Pole-Dominance (`4 < 2·4^d + 5^d + 6^d` for all `d ≥ 1`).

Firewall:
These are exact finite algebraic theorems in Lean 4.14.0. They do NOT formalize
complex exponential sums, analytic PNT-in-AP asymptotics, Zeilberger-Zudilin's
irrationality measure `μ(π) < 15/2`, base-16 normality of π, or RH.
-/

namespace ObservationalSUCC.PrimeCofactorCore

set_option autoImplicit false

/-! ## 1. Euclidean Primary-Cofiber Step & Hexadecimal Carry-Digit Bounds -/

/-- The hexadecimal primary carry digit `κ(p, a) = ⌊16a / p⌋`. -/
def primaryCarry (p a : Nat) : Nat := (16 * a) / p

/-- The next primary residue `a'(p, a) = (16a) mod p`. -/
def primaryNext (p a : Nat) : Nat := (16 * a) % p

/-- Exact Euclidean step decomposition: `16 * a = p * primaryCarry p a + primaryNext p a`. -/
theorem primary_step_euclidean (p a : Nat) :
    16 * a = p * primaryCarry p a + primaryNext p a := by
  unfold primaryCarry primaryNext
  have h := Nat.div_add_mod (16 * a) p
  omega

/-- Whenever `a < p`, the primary carry digit `⌊16a / p⌋` lies strictly below `16`. -/
theorem primary_carry_lt_sixteen (p a : Nat) (ha : a < p) :
    primaryCarry p a < 16 := by
  unfold primaryCarry
  have hpos : 0 < p := by omega
  have hmul : 16 * a < 16 * p := by omega
  exact (Nat.div_lt_iff_lt_mul hpos).mpr hmul

/-- Whenever `0 < p`, the next primary residue lies strictly below `p`. -/
theorem primary_next_lt (p a : Nat) (hp : 0 < p) :
    primaryNext p a < p := by
  unfold primaryNext
  exact Nat.mod_lt (16 * a) hp

/-- Integer-cleared cofiber recurrence step:
If `U_scaled = q * a + p * W_scaled` and `U_next = 16 * U_scaled + R_next`,
with `16 * a = p * κ + a'`, then `U_next = q * a' + (p * (16 * W_scaled + q * κ) + R_next)`. -/
theorem scaled_cofiber_step_identity (p q a a' kappa W_scaled R_next : Int)
    (heuc : 16 * a = p * kappa + a') :
    16 * (q * a + p * W_scaled) + R_next =
      q * a' + (p * (16 * W_scaled + q * kappa) + R_next) := by
  have hdist1 : 16 * (q * a + p * W_scaled) = 16 * (q * a) + 16 * (p * W_scaled) :=
    Int.mul_add 16 (q * a) (p * W_scaled)
  have hqa : 16 * (q * a) = q * (16 * a) := by
    rw [← Int.mul_assoc, Int.mul_comm 16 q, Int.mul_assoc]
  have hqa2 : q * (16 * a) = q * (p * kappa) + q * a' := by
    rw [heuc, Int.mul_add]
  have hdist2 : p * (16 * W_scaled + q * kappa) = p * (16 * W_scaled) + p * (q * kappa) :=
    Int.mul_add p (16 * W_scaled) (q * kappa)
  have hpw : 16 * (p * W_scaled) = p * (16 * W_scaled) := by
    rw [← Int.mul_assoc, Int.mul_comm 16 p, Int.mul_assoc]
  have hpqk : q * (p * kappa) = p * (q * kappa) := by
    rw [← Int.mul_assoc, Int.mul_comm q p, Int.mul_assoc]
  omega

/-! ## 2. Midy Hexadecimal Carry-Complementarity & Half-Period Annihilation -/

/-- Half-period residue sum: `a + (p - a) = p` for `a ≤ p`. -/
theorem midy_residue_sum (p a : Nat) (ha : a ≤ p) :
    a + (p - a) = p := by
  omega

/-- Key arithmetic lemma: if `0 < p`, `u + v = 16 * p`, and `0 < u % p` (so `p ∤ u`),
then `(u / p) + (v / p) = 15` and `(u % p) + (v % p) = p`. -/
theorem complementary_div_mod_fifteen (p u v : Nat)
    (hp : 0 < p) (hsum : u + v = 16 * p) (hrem_pos : 0 < u % p) :
    (u / p) + (v / p) = 15 ∧ (u % p) + (v % p) = p := by
  have hu : p * (u / p) + u % p = u := Nat.div_add_mod u p
  have hv : p * (v / p) + v % p = v := Nat.div_add_mod v p
  have hlt_u : u % p < p := Nat.mod_lt u hp
  have hlt_v : v % p < p := Nat.mod_lt v hp
  have hcomb : p * ((u / p) + (v / p)) + ((u % p) + (v % p)) = p * 16 := by
    calc
      p * ((u / p) + (v / p)) + ((u % p) + (v % p))
        = (p * (u / p) + u % p) + (p * (v / p) + v % p) := by
            rw [Nat.mul_add]
            omega
      _ = u + v := by rw [hu, hv]
      _ = 16 * p := hsum
      _ = p * 16 := Nat.mul_comm 16 p
  have hq15 : (u / p) + (v / p) = 15 := by
    apply Decidable.byContradiction
    intro hne
    rcases Nat.lt_or_gt_of_ne hne with hlt | hgt
    · have hle14 : (u / p) + (v / p) ≤ 14 := by omega
      have hmul14 : p * ((u / p) + (v / p)) ≤ p * 14 := Nat.mul_le_mul_left p hle14
      omega
    · have hge16 : 16 ≤ (u / p) + (v / p) := by omega
      have hmul16 : p * 16 ≤ p * ((u / p) + (v / p)) := Nat.mul_le_mul_left p hge16
      omega
  have hmul15 : p * ((u / p) + (v / p)) = p * 15 := by
    rw [hq15]
  constructor
  · exact hq15
  · omega

/-- Midy Hexadecimal Carry-Complement Theorem:
For any modulus `0 < p` and residue `a ≤ p` such that `p ∤ 16a` (always true for odd primes `p` and `0 < a < p`),
the carry digits at `a` and `p - a` sum to `15`, and their next residues sum to `p`. -/
theorem midy_hex_carry_complement_fifteen (p a : Nat)
    (hp : 0 < p) (ha : a ≤ p) (hrem_pos : 0 < (16 * a) % p) :
    primaryCarry p a + primaryCarry p (p - a) = 15 ∧
    primaryNext p a + primaryNext p (p - a) = p := by
  unfold primaryCarry primaryNext
  apply complementary_div_mod_fifteen p (16 * a) (16 * (p - a)) hp
  · rw [← Nat.mul_add, midy_residue_sum p a ha]
  · exact hrem_pos

/-- Half-period `p`-annihilation identity:
In `p`-cleared coordinates, adding `U_j = q * a + p * W_j` and `U_{j+M} = q * (p - a) + p * W_{j+M}`
yields `p * (q + W_j + W_{j+M})`, which is an exact multiple of `p` (so `v_p(U_j + U_{j+M}) ≥ 0`). -/
theorem half_period_primary_annihilation (p q a W1 W2 : Int) :
    (q * a + p * W1) + (q * (p - a) + p * W2) = p * (q + W1 + W2) := by
  have h1 : q * a + q * (p - a) = q * p := by
    rw [← Int.mul_add]
    have h2 : a + (p - a) = p := by omega
    rw [h2]
  have h3 : q * p = p * q := Int.mul_comm q p
  have h4 : p * (q + W1 + W2) = p * q + p * W1 + p * W2 := by
    rw [Int.mul_add, Int.mul_add]
  omega

/-! ## 3. Universal Radix-`B` Coercivity & AM-GM Weight Minimality -/

/-- Helper algebraic expansion for `(a - b)^2` over `Int`. -/
theorem int_sub_sq (a b : Int) :
    (a - b) * (a - b) = a * a - 2 * (a * b) + b * b := by
  rw [Int.mul_sub, Int.sub_mul, Int.sub_mul]
  have hcomm : b * a = a * b := Int.mul_comm b a
  rw [hcomm]
  omega

/-- Universal Radix-`B` Coercivity Gap Identity:
`((B + 1) * a^2 + B * (B + 1) * b^2) - (a + B * b)^2 = B * (a - b)^2`.
At `B = 16`, `B + 1 = 17` and `B * (B + 1) = 272`, recovering `GlobalSigned.lean`. -/
theorem universal_radix_square_gap (B a b : Int) :
    ((B + 1) * (a * a) + B * (B + 1) * (b * b)) - (a + B * b) * (a + B * b) =
      B * ((a - b) * (a - b)) := by
  have h1 : (B + 1) * (a * a) = B * (a * a) + a * a := by
    rw [Int.add_mul, Int.one_mul]
  have h2 : B * (B + 1) * (b * b) = B * B * (b * b) + B * (b * b) := by
    rw [Int.mul_add, Int.mul_one, Int.add_mul]
  have h3 : (a + B * b) * (a + B * b) = a * a + 2 * (B * (a * b)) + B * B * (b * b) := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]
    have hab1 : a * (B * b) = B * (a * b) := by
      rw [← Int.mul_assoc, Int.mul_comm a B, Int.mul_assoc]
    have hab2 : (B * b) * a = B * (a * b) := by
      rw [Int.mul_assoc, Int.mul_comm b a]
    have hbb : (B * b) * (B * b) = B * B * (b * b) := by
      rw [Int.mul_assoc, ← Int.mul_assoc b B b, Int.mul_comm b B, Int.mul_assoc B b b, ← Int.mul_assoc]
    rw [hab1, hab2, hbb]
    omega
  have h4 : B * ((a - b) * (a - b)) = B * (a * a) - 2 * (B * (a * b)) + B * (b * b) := by
    rw [int_sub_sq, Int.mul_add, Int.mul_sub]
    have h2ab : B * (2 * (a * b)) = 2 * (B * (a * b)) := by
      rw [← Int.mul_assoc, Int.mul_comm B 2, Int.mul_assoc]
    rw [h2ab]
  omega

/-- The total adjacent weight in the universal radix-`B` coercivity identity is `(B + 1)^2`. -/
theorem universal_radix_total_weight (B : Int) :
    (B + 1) + B * (B + 1) = (B + 1) * (B + 1) := by
  have h : (1 + B) * (B + 1) = 1 * (B + 1) + B * (B + 1) := Int.add_mul 1 B (B + 1)
  have hcomm : (1 + B) = (B + 1) := Int.add_comm 1 B
  rw [hcomm, Int.one_mul] at h
  exact h.symm

/-- Exact AM-GM Weight Minimality Gap:
For any Cauchy-Schwarz parameter `x` (where `u = 1 + x` and `v = B^2 + B^2/x`),
clearing `x` gives `x * (1 + B^2 + x) + B^2 - x * (B + 1)^2 = (x - B)^2`,
proving that `x = B` (`u = B + 1`, `v = B(B + 1)`, total weight `(B + 1)^2`) is the unique global minimizer. -/
theorem radix_weight_minimality_gap (B x : Int) :
    x * (1 + B * B + x) + B * B - x * ((B + 1) * (B + 1)) = (x - B) * (x - B) := by
  have h1 : (B + 1) * (B + 1) = B * B + 2 * B + 1 := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]
    omega
  have h2 : x * (1 + B * B + x) = x + x * (B * B) + x * x := by
    rw [Int.mul_add, Int.mul_add, Int.mul_one]
  have h3 : x * (B * B + 2 * B + 1) = x * (B * B) + 2 * (x * B) + x := by
    rw [Int.mul_add, Int.mul_add, Int.mul_one]
    have hx2b : x * (2 * B) = 2 * (x * B) := by
      rw [← Int.mul_assoc, Int.mul_comm x 2, Int.mul_assoc]
    rw [hx2b]
  rw [h1, h2, h3, int_sub_sq]
  omega

/-- Specialization at BBP radix `B = 16`: weights are `17`, `272`, and total `289 = 17^2`. -/
theorem bbp_radix16_specialization :
    (16 + 1 : Int) = 17 ∧ 16 * (16 + 1 : Int) = 272 ∧ (16 + 1 : Int) * (16 + 1) = 289 := by
  decide

/-- Pairwise (`l_infinity`-balanced) Radix-`B` Coercivity Gap Identity:
`((B * B + 1) * (a * a + b * b)) - (a - B * b)^2 = (B * a + b)^2`.
At `B = 16`, `B^2 + 1 = 257`, recovering the pairwise operator constant of `#305`. -/
theorem pairwise_radix_square_gap (B a b : Int) :
    (B * B + 1) * (a * a + b * b) - (a - B * b) * (a - B * b) =
      (B * a + b) * (B * a + b) := by
  have h1 : (B * B + 1) * (a * a + b * b) =
      B * B * (a * a) + B * B * (b * b) + a * a + b * b := by
    rw [Int.add_mul, Int.one_mul, Int.mul_add]
    omega
  have h2 : (a - B * b) * (a - B * b) = a * a - 2 * (B * (a * b)) + B * B * (b * b) := by
    rw [int_sub_sq]
    have hab : a * (B * b) = B * (a * b) := by
      rw [← Int.mul_assoc, Int.mul_comm a B, Int.mul_assoc]
    have hbb : (B * b) * (B * b) = B * B * (b * b) := by
      rw [Int.mul_assoc, ← Int.mul_assoc b B b, Int.mul_comm b B, Int.mul_assoc B b b, ← Int.mul_assoc]
    have h2ab : 2 * (B * (a * b)) = 2 * (a * (B * b)) := by rw [hab]
    rw [← h2ab, hbb]
  have h3 : (B * a + b) * (B * a + b) = B * B * (a * a) + 2 * (B * (a * b)) + b * b := by
    rw [Int.add_mul, Int.mul_add, Int.mul_add]
    have hba1 : (B * a) * b = B * (a * b) := Int.mul_assoc B a b
    have hba2 : b * (B * a) = B * (a * b) := by
      rw [← Int.mul_assoc, Int.mul_comm b B, Int.mul_assoc, Int.mul_comm b a]
    have haa : (B * a) * (B * a) = B * B * (a * a) := by
      rw [Int.mul_assoc, ← Int.mul_assoc a B a, Int.mul_comm a B, Int.mul_assoc B a a, ← Int.mul_assoc]
    rw [hba1, hba2, haa]
    omega
  omega

/-- Unification of the adjacent-branch operator matrix norm `1^2 + (B+1)^2 + B^2`
with the sum of the pairwise (`B^2 + 1`) and trajectory-summed (`(B + 1)^2`) constants (`257 + 289 = 546` at `B = 16`). -/
theorem adjacent_branch_norm_unification (B : Int) :
    1 + (B + 1) * (B + 1) + B * B = (B * B + 1) + (B + 1) * (B + 1) := by
  omega

/-- Direct two-step radix-16 transport `(16^2 + 1)^2 = 66049` strictly beats
iterated one-step transport `289^2 = 83521` by `17472 = 32 * 546`, and `10^6 < 16^5`. -/
theorem two_step_direct_and_decimal_hex_enclosure :
    (289 : Nat) * 289 - (16^2 + 1) * (16^2 + 1) = 17472 ∧
    (10 : Nat)^6 < 16^5 ∧
    (16 : Nat)^5 - 10^6 = 48576 := by
  decide

/-! ## 4. Prime Stroboscope Chiral Involution & `47/15` First-Octave Identity -/

/-- Scaled stroboscopic coefficient involution `J_4(A, B, C, D) = (-16C, 4B, -A, 4D)`. -/
def stroboscopeJ4 (v : Int × Int × Int × Int) : Int × Int × Int × Int :=
  match v with
  | (A, B, C, D) => (-16 * C, 4 * B, -A, 4 * D)

/-- `J_4(J_4(v)) = 16 • v` for every 4-pole coefficient vector `v`. -/
theorem stroboscope_involution_square (A B C D : Int) :
    stroboscopeJ4 (stroboscopeJ4 (A, B, C, D)) = (16 * A, 16 * B, 16 * C, 16 * D) := by
  unfold stroboscopeJ4
  dsimp
  have hA : -16 * -A = 16 * A := by omega
  have hB : 4 * (4 * B) = 16 * B := by omega
  have hC : -(-16 * C) = 16 * C := by omega
  have hD : 4 * (4 * D) = 16 * D := by omega
  rw [hA, hB, hC, hD]

/-- A 4-pole vector `(A, B, C, D)` is fixed by the stroboscopic involution (`J_4 v = 4 v`)
if and only if `A + 4 * C = 0` (`A = -4C`). -/
theorem stroboscope_fixed_iff_bbp_ratio (A B C D : Int) :
    stroboscopeJ4 (A, B, C, D) = (4 * A, 4 * B, 4 * C, 4 * D) ↔ A + 4 * C = 0 := by
  unfold stroboscopeJ4
  dsimp
  constructor
  · intro h
    have h1 : -16 * C = 4 * A := congrArg Prod.fst h
    omega
  · intro h
    have h1 : -16 * C = 4 * A := by omega
    have h3 : -A = 4 * C := by omega
    rw [h1, h3]

/-- The authentic BBP 4-pole coefficient vector `(4, -2, -1, -1)` is a stroboscopic fixed point,
whereas the counterfeit `(5, -2, -1, -1)` is not. -/
theorem bbp_stroboscope_fixed_and_mutant_broken :
    stroboscopeJ4 (4, -2, -1, -1) = (16, -8, -4, -4) ∧
    stroboscopeJ4 (5, -2, -1, -1) ≠ (20, -8, -4, -4) := by
  decide

/-- First-octave Quadratic Reciprocity Synchronization numerator identity:
Both `p ≡ 1 (mod 8)` and `p ≡ 5 (mod 8)` arrive at `j = (3p+1)/4` with exact
60-cleared residue `4 * 60 - 2 * 15 - 1 * 12 - 1 * 10 = 188 = 4 * 47` (`188/60 = 47/15 = U_1`). -/
theorem first_octave_synchronization_47_15 :
    30 * 4 - 15 - 6 - 5 = 2 * 47 ∧
    4 * 60 - 2 * 15 - 1 * 12 - 1 * 10 = 4 * 47 := by
  decide

/-! ## 5. `p ≡ 5 (mod 8)` Quarter-Group Oddness & Laurent Pole Dominance -/

/-- For every natural number `p` with `p % 8 = 5`, the quarter-group order `(p - 1) / 4` is odd.
By Lagrange's theorem, since `16 = 2^4`, `ord_p(16)` divides `(p - 1) / 4` and is therefore odd! -/
theorem p_mod8_five_quarter_odd (p : Nat) (hp : p % 8 = 5) :
    ((p - 1) / 4) % 2 = 1 := by
  omega

/-- Exact Index-`k` Small-Order Equivalence for `p = 4 * k * L + 1`:
For any odd order `L ≥ 3` and index `k ≥ 1`, `L^2 ≤ 4 * k * L + 1` holds if and only if `L ≤ 4 * k - 1`.
In particular, at `k = 1`, `L = 3` (`p = 13`) is the unique solution! -/
theorem small_order_index_k_iff (L k : Nat) (hL : 3 ≤ L) (hodd : L % 2 = 1) (hk : 1 ≤ k) :
    L * L ≤ 4 * k * L + 1 ↔ L ≤ 4 * k - 1 := by
  constructor
  · intro hsq
    apply Decidable.byContradiction
    intro hnot
    have hge : 4 * k + 1 ≤ L := by omega
    have hmul : (4 * k + 1) * L ≤ L * L := Nat.mul_le_mul_right L hge
    have hexp : (4 * k + 1) * L = 4 * k * L + L := by
      rw [Nat.add_mul, Nat.one_mul]
    omega
  · intro hle
    have hle4k : L ≤ 4 * k := by omega
    have hmul : L * L ≤ 4 * k * L := Nat.mul_le_mul_right L hle4k
    omega

/-- Base step of Laurent clock pole dominance: for `d ≥ 1`, `4^d ≥ 4` and `5^d ≥ 5`, `6^d ≥ 6`,
and at `d = 1..6` the exact Laurent numerator sums `2 * 4^d + 5^d + 6^d - 4` are strictly positive. -/
theorem laurent_pole_dominance_first_six_orders :
    2 * (4^1) + 5^1 + 6^1 - 4 = 15 ∧
    2 * (4^2) + 5^2 + 6^2 - 4 = 89 ∧
    2 * (4^3) + 5^3 + 6^3 - 4 = 465 ∧
    2 * (4^4) + 5^4 + 6^4 - 4 = 2429 ∧
    2 * (4^5) + 5^5 + 6^5 - 4 = 12945 ∧
    2 * (4^6) + 5^6 + 6^6 - 4 = 70469 := by
  decide

/-- Proof that `4 < 2 * 4^d + 5^d + 6^d` for every positive order `d ≥ 1`. -/
theorem laurent_pole_dominance_all_orders (d : Nat) (hd : 1 ≤ d) :
    4 < 2 * (4 ^ d) + 5 ^ d + 6 ^ d := by
  have h4 : 4 ^ 1 ≤ 4 ^ d := Nat.pow_le_pow_of_le_right (by decide : 0 < 4) hd
  have h5 : 5 ^ 1 ≤ 5 ^ d := Nat.pow_le_pow_of_le_right (by decide : 0 < 5) hd
  have h6 : 6 ^ 1 ≤ 6 ^ d := Nat.pow_le_pow_of_le_right (by decide : 0 < 6) hd
  omega

end ObservationalSUCC.PrimeCofactorCore

#print axioms ObservationalSUCC.PrimeCofactorCore.primary_step_euclidean
#print axioms ObservationalSUCC.PrimeCofactorCore.primary_carry_lt_sixteen
#print axioms ObservationalSUCC.PrimeCofactorCore.scaled_cofiber_step_identity
#print axioms ObservationalSUCC.PrimeCofactorCore.complementary_div_mod_fifteen
#print axioms ObservationalSUCC.PrimeCofactorCore.midy_hex_carry_complement_fifteen
#print axioms ObservationalSUCC.PrimeCofactorCore.half_period_primary_annihilation
#print axioms ObservationalSUCC.PrimeCofactorCore.universal_radix_square_gap
#print axioms ObservationalSUCC.PrimeCofactorCore.universal_radix_total_weight
#print axioms ObservationalSUCC.PrimeCofactorCore.radix_weight_minimality_gap
#print axioms ObservationalSUCC.PrimeCofactorCore.pairwise_radix_square_gap
#print axioms ObservationalSUCC.PrimeCofactorCore.adjacent_branch_norm_unification
#print axioms ObservationalSUCC.PrimeCofactorCore.two_step_direct_and_decimal_hex_enclosure
#print axioms ObservationalSUCC.PrimeCofactorCore.stroboscope_involution_square
#print axioms ObservationalSUCC.PrimeCofactorCore.stroboscope_fixed_iff_bbp_ratio
#print axioms ObservationalSUCC.PrimeCofactorCore.p_mod8_five_quarter_odd
#print axioms ObservationalSUCC.PrimeCofactorCore.small_order_index_k_iff
#print axioms ObservationalSUCC.PrimeCofactorCore.laurent_pole_dominance_all_orders
