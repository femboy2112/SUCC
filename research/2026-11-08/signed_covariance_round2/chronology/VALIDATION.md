# Executed finite validation

Protocol was written before measurements and included in root's preregistration
commit d613c66a. Exact commands, from the research worktree:

```sh
python3 -m unittest discover -s research/2026-11-08/signed_covariance_round2/chronology -p 'test_*.py'
python3 research/2026-11-08/signed_covariance_round2/chronology/oracle.py --output research/2026-11-08/signed_covariance_round2/chronology/RECEIPTS.json
```

Both exited0. Eight unit tests pass. The independent literal Fraction recurrence
and integer/Fraction oracle report1,186,678 counted instances, including
1,163,205 terms in finite Fourier completion,18,288 lag phases,1,143 moment
multisets,1,098 actual-source transcripts,432 literal source-clock comparisons,
585 wrong-seed local-history matches,36 word-law cases, and12 sharp carry
endpoints. These are distinct sizes of finite checks, not1,186,678 theorems or
unit tests. See the complete count map and raw exact distributions in
[RECEIPTS.json](RECEIPTS.json).

The implementation imports no prior source/clock code. It reconstructs every
unwrapped state with Fraction arithmetic from the literal four poles and zero,
then reduces its p-principal part using the actual denominator. Algebraic clock
formulas are checked against those states. Fourier completion is checked by
coefficient enumeration in Z[X]/(X^p-1), independently of exponential evaluation.
No floating-point phase or pi input is used. The checker verifies all declared
prime cases; no cases were dropped or tuned after running.

This is implementation independence within the same model/reasoner family,
not external scholarly verification. The asymptotic BK/PNT imports and paper
proofs are not proved by the finite checks. No new Lean claim is made.
The selector review is an independent derivation of the parent's proposed
proof, not an independent source for the classical CP input.

A second fresh-output replay to `/tmp/succ-round2-chronology-replay.json`
completed with exit0 and was byte-identical under `cmp` to the retained receipt.
Retained receipt SHA-256:
`57b3da1e11a3a2794d97ac08c26182caa26b9dcaff1e56e02c1fca7d0517ec52`.

## CH7 digit-memory leakage addendum

`LEAKAGE_PROTOCOL.md` was written before these verification measurements.
Three added unit tests bring this front's total to11 passing tests.

```sh
python3 -m unittest discover -s research/2026-11-08/signed_covariance_round2/chronology -p 'test_*.py'
python3 research/2026-11-08/signed_covariance_round2/chronology/leakage_oracle.py --output research/2026-11-08/signed_covariance_round2/chronology/LEAKAGE_RECEIPTS.json
```

Both completed with exit0. The fixed9-prime grid with d=1..4 and h=1,2,3,5
gives144 certified phase-variance bounds,144 leakage lower bounds,144 original-
source signed projection checks and144 changed-complement controls, plus36
exact rational real-variance cases:612 counted instances. The pi caps pi<22/7
and pi²<10 are themselves checked against the inherited Machin enclosure.

These added observations reuse `covariance_forge/intervals.py`; this dependency
is shared and is not a new independent phase implementation. The underlying
unwrapped Fraction source and rational cell-variance calculations remain this
front's independent implementation. The changed complement b=conjugate(a) is
explicitly a hostile algebraic control, not an authenticated BBP source.
No all-epoch empirical trend or asymptotic estimate is inferred from these cases.

Fresh-output replay to `/tmp/succ-round2-leakage-replay.json` completed with
exit0 and was byte-identical under `cmp`. Retained receipt SHA-256:
`a0c0006f60acc1db003820c9bb1243c0b0fd2341bfd4175a40bf8d9b2daa9ddf`.

Independent same-model paper review by hostile found CH7 sound, without a
separate implementation review. Cube then reviewed both CH7 and its finite
implementation, finding no substantive defect. Its requested quantifier
clarification was applied: leakage tends to1 for each fixed h!=0; varying h
additionally requires |h|/16^d->0 and mu->0. Final theorem file SHA-256:
`5edaa0a79b40b6f80c14fc2801d7aa089ceb88a5cc6f2f02f9bfc667a0577c10`.
These are independent reasoner reviews sharing the same model and inherited
classical source inputs, not external refereeing.
Cube also independently reran the three added tests and612-instance fresh
leakage replay; tests passed and its JSON matched the retained receipt exactly.
Its durable final review is [cube/CH7_REVIEW.json](../cube/CH7_REVIEW.json).
