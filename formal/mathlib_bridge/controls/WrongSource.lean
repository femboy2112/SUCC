/-
SOURCE-MISMATCH / WRONG-CONCLUSION CONTROL  (this file MUST FAIL to elaborate).

This is a genuine machine-checked negative control, not a comment. It is NOT a
build target of the `mathlib_bridge` lean_lib (whose glob is the single root
module `MasonStothersBridge`), so `lake build` never touches it. It is elaborated
on its own:

    cd formal/mathlib_bridge && lake env lean controls/WrongSource.lean

and a NONZERO exit code is the receipt. CI asserts exactly that nonzero exit.

What it demonstrates: this proposed stronger conclusion is rejected by the kernel.
mathlib's `Polynomial.abc`, transported through `succ_mason_stothers_charZero`,
yields `natDegree A + 1 ≤ deg rad(A*B*C)`. Here we demand the strictly stronger
(false) bound `natDegree A + 2 ≤ deg rad(A*B*C)`. That conclusion does not follow
-- e.g. with `A = X`, `B = 1`, `C = X + 1` it would read `1 + 2 = 3 ≤ deg rad = 2`,
which is false -- so Lean's kernel refuses the term with a `type mismatch`. Were
the bridge able to produce the `+2` bound, this file would compile and the control
would (correctly) be reported as broken.

Pinned to mathlib tag v4.14.0 (commit 4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84);
the error text is toolchain-stable:

  type mismatch
    (succ_mason_stothers_charZero hA hB hC hAB hBC hCA hsum hnc).left
  has type
    A.natDegree + 1 ≤ (radical (A * B * C)).natDegree : Prop
  but is expected to have type
    A.natDegree + 2 ≤ (radical (A * B * C)).natDegree : Prop
-/
import MasonStothersBridge

open Polynomial UniqueFactorizationMonoid UniqueFactorizationDomain
open SUCC.MasonStothersBridge

/-- MUST NOT elaborate: `+2` is strictly stronger than the proved `+1` bound. -/
example {k : Type*} [Field k] [DecidableEq k] [CharZero k]
    {A B C : k[X]} (hA : A ≠ 0) (hB : B ≠ 0) (hC : C ≠ 0)
    (hAB : IsCoprime A B) (hBC : IsCoprime B C) (hCA : IsCoprime C A)
    (hsum : A + B = C)
    (hnc : ¬ (A.natDegree = 0 ∧ B.natDegree = 0 ∧ C.natDegree = 0)) :
    A.natDegree + 2 ≤ (radical (A * B * C)).natDegree :=
  (succ_mason_stothers_charZero hA hB hC hAB hBC hCA hsum hnc).1
