# Proof-Direction Oracle — execution receipts and claim limits

**Date:** 2026-11-17. **Scope:** finite source-authenticated checks for [PDO-01–07](PROOF_DIRECTION_ORACLE.md). R0 and π-normality remain OPEN. This is not a proof that any powerful objective adviser already knows an excluded-source invariant.

## Focused test execution

Executed locally:

~~~sh
python -m unittest -v /mnt/data/test_proof_direction_oracle.py
~~~

**Result: 10 tests PASS, 0 failures, 0 errors.** The exact tested 5,969-byte script is committed as [tests/test_proof_direction_oracle.py](../../../tests/test_proof_direction_oracle.py). The Git blob SHA computed locally and the SHA retrieved from GitHub for that branch **match byte-for-byte**:

~~~text
b925476d8d0d6de874bc7b3a969fc42bb392b1cc
~~~

The test uses only Python standard-library Fraction/integer arithmetic, not floating-point π, randomized digits, or assumed shell statistics. Its controls include:

- Every tested finite hexadecimal cylinder (including edge prefixes) contains a terminating orbit locked at phase 1 and an orbit fixed at phase e(1/15) with R0 true.
- Earlier phase discrepancy can be made arbitrarily small by increasing the common-prefix horizon; at clock m the new lawful exact probe distinguishes the pair.
- Advice that is a deterministic function of the identical old evidence cannot split the source fiber.
- The literal original zero-seeded four-pole terminal U_(2B) is cross-checked against the direct weighted BBP sum.
- Honest per-shell witness sets are recomputed independently; a forged seed, duplicated indices, a single witness, and unsupported additional positions are rejected.
- Exact threshold-energy inequalities and a one-strong-position-per-shell counterexample distinguish finite witness existence from a uniform positive-density theorem.

## Verified finite original-BBP witness receipts

For threshold ε=1/4, a proposed finite certificate consists of the exact original U_(2B), the positions whose backward radial distances are at least ε, and an admissible density θ=1/4. The independent checker re-computes everything exactly:

| B | Verified witness count | Exact fraction | Terminal rational R_B (decimal view) | Result |
|---:|---:|---:|---:|---|
| 16 | 6 | 3/8 | 0.075084310973 | PASS |
| 32 | 14 | 7/16 | 0.079825201617 | PASS |
| 64 | 33 | 33/64 | 0.088161132374 | PASS |
| 128 | 66 | 33/64 | 0.089051047282 | PASS |

These counts are **in-sample finite observations**, not frozen prospective holdouts and not evidence of an all-late-shell lower bound. The chosen θ=1/4 works for these four finite samples; its eventual validity is unproved.

## Independent symbolic cross-check

A separate SymPy implementation, independent of the test module, exactly confirmed the opposite-R0 cylinder construction for m in {1,3,7}, A in {0,1,16^m−1}, and later clocks n=m+k for k in {0,1,2,10}. The checks verified the same m-digit prefix and exact future circle residues 0 versus 1/15 in **36 clock comparisons**. This shares the same classical algebra, not an independent source witness.

## What the oracle can and cannot do

The checker certifies one shell at a time. It has no operation which can accept “all sufficiently late shells” from a finite list of successful examples. A prover may propose a finite source-valid inductive invariant or a global proof term, but it must then pass a sound independent verifier. This is a *proof-generation strategy*, not an assumed truth/reachability oracle.

The positive witness-density threshold equivalence in the manuscript is elementary algebra and is proved for all bounded distances; no finite test is substituted for that derivation. No actual oracle direction has yet supplied a new, globally uniform source-carry/cofactor lower bound.

**Not executed/claimed in this update:** full root 14,577+ SUCC tests, provenance/observer/ordinal gates, Lean proof kernel, external blind refereeing, final-head GitHub CI, original-source all-shell R0, or full base-16 π normality. The full-suite receipt for earlier commit 8627230a belongs to that earlier exact tree and is not recycled as validation of this head.

## Next verdict-changing probe

Freeze a proposed symbolic source invariant about the **zero-selected integer winding and actual odd-denominator/cofactor history** that outputs a rational ε, θ and constructs a valid positive fraction of terminal backward directions for every B≥B0. Verify its exact hypotheses and universal induction, not only its observed finite successes. Challenge it first with the terminating and fixed-nonunit cylinder pair, locked wrong seed s=−π/16, dyadic winding erasure, sparse irrational cold-shell source, and causal impulse/initial-seed history alias.
