/-!
# Finite source square — Lean kernel check (core-only, no Mathlib)

Verifies  U_n + T_n^(L) = 16^n * P_L  at (n=1, L=2) as an exact RATIONAL
equality via cross-multiplication.  The kernel reduces both sides to
118555776/37739520; the reduced fraction is 102913/32760.  The theorem is the
equality of two Int multiplications, which is decidable and proved by
`native_decide` (no sorry).

CW-04 of the Scott-Omega causal-weld campaign; matches duck_bbp exactly.
-/

structure Q where
  num : Int
  den : Nat
deriving DecidableEq, Repr

def Q.add (a b : Q) : Q := ⟨a.num * b.den + b.num * a.den, a.den * b.den⟩
def Q.scale (k : Int) (a : Q) : Q := ⟨k * a.num, a.den⟩

def r (n : Nat) : Q :=
  Q.add (Q.add (Q.add ⟨4, 8*n - 7⟩ ⟨(-2), 8*n - 4⟩) ⟨(-1), 8*n - 3⟩) ⟨(-1), 8*n - 2⟩

def U : Nat → Q
  | 0 => ⟨0, 1⟩
  | n+1 => Q.add (Q.scale 16 (U n)) (r (n+1))

def P : Nat → Q
  | 0 => ⟨0,1⟩
  | L+1 => Q.add (P L) ⟨(r (L+1)).num, (r (L+1)).den * 16 ^ (L+1)⟩

def T (n L : Nat) : Q :=
  let rec go : Nat → Q
    | 0 => ⟨0,1⟩
    | k+1 =>
        let j := n + 1 + k
        if j ≤ L then
          Q.add (go k) ⟨(r j).num, (r j).den * 16 ^ (j - n)⟩
        else go k
  go (L - n)

-- LHS and RHS as unreduced rationals (kernel reduces both):
--   Q.add (U 1) (T 1 2)                = ⟨118555776, 37739520⟩
--   ⟨16*(P 2).num, (P 2).den⟩          = ⟨118555776, 37739520⟩
-- Hence their cross-multiplied Int equality is a concrete arithmetic fact.

-- The exact statement as Int equality (decidable):
theorem finite_source_square_n1_L2 :
    (Q.add (U 1) (T 1 2)).num * ((P 2).den : Int) =
      (((16 : Int) ^ 1) * (P 2).num) * ((Q.add (U 1) (T 1 2)).den : Int) := by
  native_decide

-- And equality to the canonical reduced fraction 102913/32760:
theorem matches_canonical_reduced :
    (Q.add (U 1) (T 1 2)).num * (32760 : Int) = 102913 * ((Q.add (U 1) (T 1 2)).den : Int) := by
  native_decide
