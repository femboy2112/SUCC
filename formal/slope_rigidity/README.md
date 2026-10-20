# Primitive determinant rigidity: formal research project

This project targets the discrete invariant behind the primitive abc moment
argument. It uses Lean 4.14.0 and mathlib
`4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84`, matching the existing formal projects.
The mathematics is classical; the integrated formal foundation is new to SUCC.
No academic novelty is claimed.

The imported elementary mechanisms can be checked directly at the pinned sources:
[`IsCoprime.mul_dvd` and coprime cancellation](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/RingTheory/Coprime/Basic.lean),
[`Nat.Coprime.isCoprime` for the integer embedding](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/RingTheory/Coprime/Lemmas.lean),
and [`Nat.coprime_self_add_right`](https://github.com/leanprover-community/mathlib4/blob/4bbdccd9c5f862bf90ff12f0a9e2c8be032b9a84/Mathlib/Data/Nat/GCD/Basic.lean).
Our bridge composes these classical facts into the exact determinant statement;
it does not add unproved analytic hypotheses to the formal environment.

For natural numbers with positive `c,c'`, additive relations `a+b=c`,
`a'+b'=c'`, coprimality `gcd(a,b)=gcd(a',b')=1`, distinct triples, and pairwise
coprime moduli `d,e,f` satisfying `d|a,a'`, `e|b,b'`, `f|c,c'`, the target theorem
`ObservationalSUCC.PrimitiveSlope.primitive_determinant_gap` is

\[
def\le |ac'-a'c|.
\]

The proof is split into independently inspectable obligations:

- `determinant_divisibility_int` works for integer additive triples. The `d`
  and `f` channels divide the determinant directly; the `e` channel uses
  `ac'-a'c=ab'-a'b`. Coprimality multiplies the three divisibility statements.
- `determinant_divisibility` transports natural moduli into that exact integer
  identity. It does not use truncated natural subtraction.
- `reduced_pair_injective` proves equality of reduced numerator/denominator
  pairs from cross-product equality. Mutual denominator divisibility gives
  denominator equality, then positive-denominator cancellation gives the
  numerator. This is a second argument independent of the modular channels.
- `primitive_triple_determinant_ne_zero` uses `gcd(a,a+b)=gcd(a,b)` and the
  injectivity theorem. The second summand is recovered from the additive relation.
- `modulus_le_natAbs` proves the elementary size bound for a nonzero multiple.

Exact controls give equal slopes `(1,1,2)` and `(2,2,4)` without primitivity, and
determinant `4` for triples `(2,2,4),(2,4,6)` with shared moduli `d=e=f=2`, whose
product `8` does not divide the determinant. A separate elaboration check rejects
deleting the second primitivity assumption and replacing the gap by `def+1`.

Dividing the proved determinant inequality by `cc'`, then using `cc'≤X²`,
is the paper proof of real slope separation `≥def/X²`. Summing adjacent gaps in
`(0,1)` gives `N_X(d,e,f)≤1+X²/(def)` for positive `d,e,f`. **Those final real
division and finite ordered-counting steps, the moment bound, and its Euler
product are not claimed as formalized by this module.**

## Verification status and reproduction

The checked-in Lean source is a formalization candidate until a successful real
kernel run is recorded. No receipt is manufactured. Run the dispatch-only
`Primitive slope kernel research` workflow on the exact research commit, or:

```sh
cd formal/slope_rigidity
lake exe cache get Mathlib/RingTheory/Coprime/Lemmas.lean Mathlib/Data/Nat/GCD/Basic.lean Mathlib/Tactic/Ring.lean Mathlib/Tactic/NormNum.lean
cd ../..
python3 formal/slope_rigidity/check.py /tmp/succ-slope-audit
```

With existing project caches, link the same pinned `.lake/packages` directory
instead of downloading another copy. The checker rebuilds the local theorem,
exports all actual theorem types and recursive axioms, and records source hashes
and failed mutation logs. Successful output has schema `succ.lean.research.v1`
and status `KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED`; it is deliberately not an
automatically admitted Level C record. Standard allowed axioms are `propext`,
`Classical.choice`, `Quot.sound`. Full logs and an encoded complete record appear
in the workflow artifact and job output. The coordinator must review the actual
run before any claim-status promotion.
