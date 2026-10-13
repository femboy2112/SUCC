# Independent implementation review: public-policy realization plans

Status: **OBSERVED**, exact finite hostile checks; not a formal verification or
an independent-model replication. Reviewer: NO-GHOST engine subagent, reviewing
the principal agent's separately written `observational_succ/no_ghost_policy.py`.
Reviewed implementation SHA-256:
`0a7d1398b0595cefc186198b90910accbe00e27fae2bef3c95e0f9f43beb705b`.

## Scope and verdict

No discrepancy was found between the compiler's public realization-plan
equations and its independently implemented probability replay on the tested
finite contracts. The examined source of correctness is specific: at any public
history `h`, every compatible private path has the **same policy factor**
`r_h`, while its original-preparation/chance factor is retained separately.
This makes `r_child = u_(h,a)` correct for every possible receipt child; chance
weights do not belong in that realization-plan equality. Leaf probability is
`J0 * product(K) * r_leaf`.

The compiler checks availability over every positive private possibility at a
public node. Neither a private branch token nor the original source label
selects an action. A public history includes past actions and receipts, so
different choices cannot silently merge information sets and break perfect
recall. Empty nonterminal menus impose `r_h = 0`; this correctly makes a forced
positive-chance dead end infeasible rather than discarding its mass.

The result applies to the declared finite decision horizon and contract. It
does not claim an infinite policy, universal physical executability, free
reading of the source, or equivalence under forgetting public action history.

## Exact checks actually run

1. `python -m unittest tests.test_no_ghost tests.test_no_ghost_policy`: **45 tests
   passed**, including forced and partial-chance dead ends, hidden-enabledness
   rejection, source-supported hidden-oracle obstruction, fixed chance laws,
   zero horizon, rational primal/dual checks and bounded-search statuses.
2. An additional asymmetric two-source fixture had prior `(1/3, 2/3)`, three
   occurrence labels `a,b,c`, one current state and horizon 2. For action index
   `j in {0,1,2}`, source `s in {0,1}`, and most recent public bit `z` (zero at
   the root), its chance of reporting 1 was `(1+s+j+z)/6`. Every unperformed
   action was available. Its compiled tree had **48 private leaves, 31 public
   nodes and 46 realization variables**.
3. All **192 deterministic public decision assignments** on that fixture were
   checked. For each, constructing the realization vector directly as the
   product of its declared public action probabilities satisfied the compiled
   equations. Compiler leaf weights exactly matched independent replay; their
   sum was 1 and their source marginals remained `(1/3,2/3)`. Reconstructing the
   policy with `system.policy` and replaying it preserved the same law.
4. **12 rational randomized adaptive policies** on the same fixture also
   matched exactly: root choices were uniform, and the first remaining action
   had probability `q` after public bit 0 and `t` after public bit 1, with
   `q in {0,1/5,1/2,1}` and `t in {0,1/3,1}`.
5. The updated `scripts/no_ghost_probe.py` directly constructs its fixtures
   without importing tests. Its JSON receipt includes a source-supported,
   prior-preserving perfect-guess coupling rejected by the public-policy
   equations with an exact Farkas witness; it also includes a positive
   read-then-guess policy, independently replayed. The `read` instrument is
   expressly present in the repaired contract; the solver does not create it.

These are finite executable probes, not proofs that every admissible contract
works. The accompanying manuscript provides the general realization-plan
argument.

## Trust boundary discovered by mutation

`PolicySystem.weights` verifies the supplied vector against **that object's**
matrix. It does not authenticate that a supplied `PolicySystem` was compiled
from a specified original contract. The following mutation was actually run:

```python
from dataclasses import replace
forged = replace(system, atoms=tuple(
    replace(a, mass=2*a.mass) for a in system.atoms))
assert sum(forged.weights(valid_realization)) == 2
```

This is a trust-boundary calibration, not a counterexample to correctness of
`compile_public_policy`: the mutated object was never produced by that
compiler. An operational certificate verifier must reconstruct or authenticate
the compilation from its declared model and compare independent replay against
the claimed law. Checking only `A r=b, r>=0` for attacker-supplied matrix and
atom metadata is insufficient. The main probe's positive certificate therefore
also compares actual replay from the source contract against predicted weights.

**Integrator remediation, independently executable:** the root subsequently
added `verify_policy_solution`, which rebuilds the system from the original
model and checks equality of compiled metadata before independent replay, and
`verify_policy_obstruction`, which reconstructs source-derived equations before
checking the dual. Regressions reject doubled atom weights, foreign source
metadata, sign-mutated duals and insufficient verification budgets. The policy
suite now contains 12 passing tests. The review's inspected hash above refers
to the earlier version; final fingerprints are in `VALIDATION.json`.

No root implementation files were modified by this review. The next
verdict-changing probe would be a compiled (unmutated) finite contract whose
verified realization vector and reconstructed public policy produce different
source-indexed private-history laws under independent replay.
