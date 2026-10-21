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

**KERNEL_CHECKED_NOT_AUTHORITY_ADMITTED**, 2026-10-20. All nine declarations
were checked by the actual pinned Lean kernel in
[run 39508738928](https://github.com/femboy2112/SUCC/actions/runs/39508738928),
job `118924873774`, on PR #211 head
`e3d01df4a53a4e291d0e16a20d530493c10c6901`. GitHub checked out its synthetic merge
commit `3cd6019562bc530b16764e4ec6e9acae6fe53742`; the record's eight exact source
hashes all match the research head's audited source files. The formal build and
exports succeeded on the first run. The `missing_reducedness` and `oversized_gap`
negative elaboration controls were both rejected. No proof shortcut occurred in
the accepted source or theorem exports.

The [actual build record](receipts/kernel-observation-39508738928.json) was
reconstructed from the complete encoded record in the hosted job log and checked
independently by the coordinator. Its file SHA256 is
`094a35e5ed7dae06d99efb159e6283a674862f5441499f6f60e0efa12614cdc1`;
canonical JSON SHA256 is
`a8d7f0884a558771c82a676a9a14f6a8cdd8abe6f410fc026f4bb2541622d924`.
All nine theorem type digests were recomputed successfully. The main determinant
gap's exact type digest is
`0830694aeba6822f94ee18b12e46d93baaaf238b89d9f7963b75285324471d01`.

The axiom audit is precise: integer determinant divisibility and the noncoprime
modulus control use `propext, Quot.sound`; natural-to-integer divisibility,
the absolute-value bound and the nonprimitive control use `propext`; the other
four declarations use `propext, Classical.choice, Quot.sound`. No other axiom
occurs. This is kernel verification of the stated discrete arithmetic theorems,
not a formal proof of the subsequent real counting argument or moment theorem.
The research record has **not** been added to the separate runtime proof-authority
catalogue; a JSON file does not perform that admission.

To reproduce, run `Primitive slope kernel research` on the exact research sources,
or:

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

## Main VIII installed authority

The historical research receipt above remains unadmitted. Its nine exact types have now been rebuilt in the shared three-project pipeline and admitted through the new source-bound 19-theorem record. See [actual admission review](../kernel_audit/MAIN_VIII_ADMISSION_REVIEW.md). This admits the typed determinant declarations, not the full weighted-moment theorem.
