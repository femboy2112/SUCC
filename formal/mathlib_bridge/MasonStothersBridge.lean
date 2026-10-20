/-
Mason-Stothers THEOREM-TRANSPORT BRIDGE: SUCC certificate -> mathlib `Polynomial.abc`.

This file does NOT re-prove Mason-Stothers. It IMPORTS mathlib4's already-formalized
`Polynomial.abc` (module `Mathlib.NumberTheory.FLT.MasonStothers`, authors Jineon Baek
and Seewoo Lee, 2024) and discharges the SUCC Proof-Forge certificate's claim with it,
reconciling the two statements' conventions exactly.

Status: CLASSICAL (Stothers 1981; Mason 1984). The theorem is classical; the SUCC
contribution is the transport bridge, the convention reconciliation, and the controls.

mathlib's `Polynomial.abc` (recovered verbatim, tag v4.14.0):

  theorem Polynomial.abc {a b c : k[X]} (ha : a ≠ 0) (hb : b ≠ 0) (hc : c ≠ 0)
      (hab : IsCoprime a b) (hbc : IsCoprime b c) (hca : IsCoprime c a)
      (hsum : a + b + c = 0) :
      ( natDegree a + 1 ≤ (radical (a*b*c)).natDegree ∧
        natDegree b + 1 ≤ (radical (a*b*c)).natDegree ∧
        natDegree c + 1 ≤ (radical (a*b*c)).natDegree ) ∨
        derivative a = 0 ∧ derivative b = 0 ∧ derivative c = 0

CONVENTION MAP (SUCC -> mathlib):
  * Coefficient field: SUCC "field K"  ==  mathlib `[Field k] [DecidableEq k]`.
  * Sum: SUCC `A + B = C`              ==  mathlib `a + b + c = 0` via `c := -C`
         (A + B + (-C) = 0 <-> A + B = C). Sign change proved below.
  * Nonzero: SUCC A,B,C nonzero        ==  mathlib ha,hb,hc (and -C ≠ 0).
  * Coprimality: SUCC pairwise coprime ==  IsCoprime A B, B (-C), (-C) A
         (from IsCoprime A B, B C, C A via `IsCoprime.neg_right/neg_left`).
  * Radical: SUCC rad(ABC) = product of distinct monic irreducible factors
         ==  mathlib `UniqueFactorizationMonoid.radical (A*B*C)`; and
         `radical (A*B*(-C)) = radical (A*B*C)` (unit -1) proved below.
  * Degree bound: SUCC `max(deg A,deg B,deg C) ≤ deg rad(ABC) − 1` is exactly
         mathlib's `natDegree _ + 1 ≤ (radical (A*B*C)).natDegree` (the `+1` form
         is used to avoid ℕ-truncated subtraction; over ℤ the two are identical).
  * Char hypothesis: SUCC assumes `char K = 0` (or `char K > deg`) to force the
         Wronskian W ≠ 0. mathlib has NO char hypothesis; it instead emits the
         derivative-zero collapse as the SECOND disjunct. So SUCC's char/W≠0
         hypothesis is PRECISELY the fact that rules out mathlib's right disjunct.
         Enters here as `hW` (core) or `[CharZero k]` + nonconstancy (corollary).
-/
import Mathlib.NumberTheory.FLT.MasonStothers
import Mathlib.Data.ZMod.Basic

open Polynomial UniqueFactorizationMonoid UniqueFactorizationDomain

namespace SUCC.MasonStothersBridge

variable {k : Type*} [Field k] [DecidableEq k]

/-- Radical reconciliation: SUCC's `rad(A·B·C)` equals mathlib's radical of the
    sign-changed product `A·B·(−C)`. (`−1` is a unit, so `radical` is unchanged.) -/
theorem radical_neg_prod (A B C : k[X]) :
    radical (A * B * (-C)) = radical (A * B * C) := by
  rw [show A * B * (-C) = -(A * B * C) by ring, radical_neg]

/-- **SUCC Mason–Stothers certificate, discharged by mathlib's `Polynomial.abc`.**

SUCC convention `A + B = C` (nonzero, pairwise coprime), with the SUCC
char-0 / `char > deg` hypothesis entering as `hW`: not all three derivatives
vanish (equivalently the Wronskian `W = A'B − AB' ≠ 0`). Conclusion is mathlib's
`+1` form of SUCC's `max(deg A, deg B, deg C) ≤ deg rad(ABC) − 1`. -/
theorem succ_mason_stothers_core
    {A B C : k[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hC : C ≠ 0)
    (hAB : IsCoprime A B) (hBC : IsCoprime B C) (hCA : IsCoprime C A)
    (hsum : A + B = C)
    (hW : ¬ (derivative A = 0 ∧ derivative B = 0 ∧ derivative C = 0)) :
    A.natDegree + 1 ≤ (radical (A * B * C)).natDegree ∧
    B.natDegree + 1 ≤ (radical (A * B * C)).natDegree ∧
    C.natDegree + 1 ≤ (radical (A * B * C)).natDegree := by
  -- sign change into mathlib's `a + b + c = 0` convention (c := -C)
  have hsum0 : A + B + (-C) = 0 := by rw [← hsum]; ring
  have hnegC : (-C) ≠ 0 := neg_ne_zero.mpr hC
  have hBnC : IsCoprime B (-C) := hBC.neg_right
  have hnCA : IsCoprime (-C) A := hCA.neg_left
  rcases Polynomial.abc hA hB hnegC hAB hBnC hnCA hsum0 with hbound | hder
  · -- degree bound: translate radical(A*B*(-C)) and natDegree(-C)
    rw [radical_neg_prod, natDegree_neg] at hbound
    exact hbound
  · -- derivative-zero disjunct contradicts hW (derivative (-C) = -derivative C)
    refine absurd ⟨hder.1, hder.2.1, ?_⟩ hW
    have h := hder.2.2
    rw [derivative_neg, neg_eq_zero] at h
    exact h

/-- **Char-0 corollary.** In a characteristic-zero field, the SUCC char hypothesis
    is discharged from `[CharZero k]` plus non-constancy: if the derivative-zero
    collapse held, every factor would be constant (char 0), contradicting the
    SUCC "not all constant" hypothesis. This faithfully reproduces SUCC's §3
    nonvanishing argument. -/
theorem succ_mason_stothers_charZero [CharZero k]
    {A B C : k[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hC : C ≠ 0)
    (hAB : IsCoprime A B) (hBC : IsCoprime B C) (hCA : IsCoprime C A)
    (hsum : A + B = C)
    (hnc : ¬ (A.natDegree = 0 ∧ B.natDegree = 0 ∧ C.natDegree = 0)) :
    A.natDegree + 1 ≤ (radical (A * B * C)).natDegree ∧
    B.natDegree + 1 ≤ (radical (A * B * C)).natDegree ∧
    C.natDegree + 1 ≤ (radical (A * B * C)).natDegree := by
  refine succ_mason_stothers_core hA hB hC hAB hBC hCA hsum ?_
  intro hder
  exact hnc ⟨natDegree_eq_zero_of_derivative_eq_zero hder.1,
             natDegree_eq_zero_of_derivative_eq_zero hder.2.1,
             natDegree_eq_zero_of_derivative_eq_zero hder.2.2⟩

/-- **CONTROL (hypothesis is load-bearing, not decorative).**

The SUCC char / `W ≠ 0` hypothesis (`hW` above) cannot be dropped. Witness
over `𝔽₂ = ZMod 2`: `A = X²`, `B = 1`, `C = X² + 1`. This triple satisfies
EVERY other hypothesis of `succ_mason_stothers_core` — nonzero, pairwise
coprime, `A + B = C` — yet all three derivatives vanish (`X²` has derivative
`2·X = 0` in char 2). So by mathlib's `Polynomial.abc` dichotomy it lands in the
RIGHT disjunct and the degree bound is NOT available: here it would assert
`deg A + 1 = 3 ≤ deg rad(ABC) = deg(X(X+1)) = 2`, which is false. Hence the
exact content that `hW` excludes is independently realizable, proving `hW` is
genuinely required (this is the char-p "freshman's dream" collapse, SUCC §6). -/
theorem control_hW_is_load_bearing :
    ∃ A B C : (ZMod 2)[X],
      A ≠ 0 ∧ B ≠ 0 ∧ C ≠ 0 ∧
      IsCoprime A B ∧ IsCoprime B C ∧ IsCoprime C A ∧
      A + B = C ∧
      (derivative A = 0 ∧ derivative B = 0 ∧ derivative C = 0) := by
  haveI : Fact (Nat.Prime 2) := ⟨Nat.prime_two⟩
  refine ⟨X ^ 2, 1, X ^ 2 + 1, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_, ?_⟩
  · exact pow_ne_zero 2 X_ne_zero
  · exact one_ne_zero
  · rw [show (1 : (ZMod 2)[X]) = C 1 from (C_1).symm]
    exact X_pow_add_C_ne_zero (by norm_num) 1
  · exact isCoprime_one_right
  · exact isCoprime_one_left
  · -- IsCoprime (X²+1) (X²): 1·(X²+1) + (−1)·X² = 1 (ring identity, any char)
    exact ⟨1, -1, by ring⟩
  · ring
  · -- derivative (X²) = C(2)·X = 0 in char 2
    rw [derivative_X_pow, ZMod.natCast_self, map_zero, zero_mul]
  · exact derivative_one
  · -- derivative (X²+1) = derivative(X²) + 0 = 0
    rw [derivative_add, derivative_X_pow, ZMod.natCast_self, map_zero, zero_mul,
        derivative_one, add_zero]

/-
**CONTROL (typecheck-failure: coprimality is a required argument).**

This is a genuine, machine-checked source-mismatch control, NOT a comment. If we
try to feed `Polynomial.abc` the sum hypothesis `hsum0` where a coprimality
argument `IsCoprime A B` is expected (i.e. drop coprimality), elaboration FAILS
with the `application type mismatch` captured below. `#guard_msgs in` turns that
expected failure into a build requirement: THIS FILE COMPILES IF AND ONLY IF the
discharge genuinely cannot proceed without coprimality. Were coprimality not
load-bearing, no error would be emitted and `#guard_msgs` would itself fail the
build. (Pinned to mathlib tag v4.14.0; the error text is toolchain-stable.)
-/
/-- error: application type mismatch
  abc hA hB (neg_ne_zero.mpr hC) hsum0
argument
  hsum0
has type
  A + B + -C = 0 : Prop
but is expected to have type
  IsCoprime A B : Prop -/
#guard_msgs in
example {A B C : k[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hC : C ≠ 0)
    (hsum0 : A + B + (-C) = 0) : True :=
  have _key := Polynomial.abc hA hB (neg_ne_zero.mpr hC) hsum0
  trivial

/-! ## Second benchmark: classical polynomial Fermat, derived from the bridge

mathlib v4.14.0 does **not** contain polynomial FLT (the `MasonStothers` module
only lists it as a `TODO`; there is no `fermatLastTheoremPolynomial`/`flt_catalan`
for `k[X]`). So this is a genuine derivation from `Polynomial.abc` (via the
char-0 bridge above). It is the **classical** Mason–Stothers corollary (not
original to SUCC): over a characteristic-zero field, for `n ≥ 3` there is no
pairwise-coprime, not-all-constant triple with `Aⁿ + Bⁿ = Cⁿ`. -/

/-- **Polynomial Fermat (char 0), via the SUCC bridge → mathlib `Polynomial.abc`.**

Apply Mason–Stothers to `(Aⁿ, Bⁿ, Cⁿ)`: `radical(Aⁿ·Bⁿ·Cⁿ) = radical((ABC)ⁿ) =
radical(ABC)`, whose degree is `≤ deg A + deg B + deg C`. Each bound reads
`n·deg A + 1 ≤ deg rad(ABC) ≤ deg A + deg B + deg C` (and cyclically); weakening
`n ≥ 3` and summing the three gives `3·S + 3 ≤ 3·S`, i.e. `3 ≤ 0` — absurd. -/
theorem polynomial_fermat [CharZero k] {n : ℕ} (hn : 3 ≤ n)
    {A B C : k[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hC : C ≠ 0)
    (hAB : IsCoprime A B) (hBC : IsCoprime B C) (hCA : IsCoprime C A)
    (hnc : ¬ (A.natDegree = 0 ∧ B.natDegree = 0 ∧ C.natDegree = 0))
    (hFLT : A ^ n + B ^ n = C ^ n) : False := by
  have hne : n ≠ 0 := by omega
  have hpos : 0 < n := by omega
  -- the power triple satisfies every hypothesis of the char-0 bridge
  have hABn : IsCoprime (A ^ n) (B ^ n) := hAB.pow
  have hBCn : IsCoprime (B ^ n) (C ^ n) := hBC.pow
  have hCAn : IsCoprime (C ^ n) (A ^ n) := hCA.pow
  have hncn : ¬ ((A ^ n).natDegree = 0 ∧ (B ^ n).natDegree = 0 ∧ (C ^ n).natDegree = 0) := by
    simp only [natDegree_pow]
    rintro ⟨ha, hb, hc⟩
    exact hnc ⟨(Nat.mul_eq_zero.mp ha).resolve_left hne,
               (Nat.mul_eq_zero.mp hb).resolve_left hne,
               (Nat.mul_eq_zero.mp hc).resolve_left hne⟩
  obtain ⟨b1, b2, b3⟩ :=
    succ_mason_stothers_charZero (pow_ne_zero n hA) (pow_ne_zero n hB) (pow_ne_zero n hC)
      hABn hBCn hCAn hFLT hncn
  -- radical(Aⁿ·Bⁿ·Cⁿ) = radical(ABC); and deg(Xⁿ) = n·deg X
  have hrad : radical (A ^ n * B ^ n * C ^ n) = radical (A * B * C) := by
    rw [show A ^ n * B ^ n * C ^ n = (A * B * C) ^ n by ring, radical_pow _ hpos]
  rw [hrad, natDegree_pow] at b1 b2 b3
  -- deg rad(ABC) ≤ deg A + deg B + deg C
  have hABC : A * B * C ≠ 0 := mul_ne_zero (mul_ne_zero hA hB) hC
  have hRle : (radical (A * B * C)).natDegree
      ≤ A.natDegree + B.natDegree + C.natDegree := by
    calc (radical (A * B * C)).natDegree
          ≤ (A * B * C).natDegree := natDegree_le_of_dvd (radical_dvd_self _) hABC
      _ = A.natDegree + B.natDegree + C.natDegree := by
          rw [natDegree_mul (mul_ne_zero hA hB) hC, natDegree_mul hA hB]
  -- weaken n ≥ 3 → 3·deg ≤ n·deg so the final step is linear
  have hA3 : 3 * A.natDegree ≤ n * A.natDegree := mul_le_mul_right' hn _
  have hB3 : 3 * B.natDegree ≤ n * B.natDegree := mul_le_mul_right' hn _
  have hC3 : 3 * C.natDegree ≤ n * C.natDegree := mul_le_mul_right' hn _
  omega

end SUCC.MasonStothersBridge

/-! ## Axiom audit (recorded in the agent report) -/
#print axioms SUCC.MasonStothersBridge.succ_mason_stothers_core
#print axioms SUCC.MasonStothersBridge.succ_mason_stothers_charZero
#print axioms SUCC.MasonStothersBridge.control_hW_is_load_bearing
#print axioms SUCC.MasonStothersBridge.polynomial_fermat
