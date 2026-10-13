# NO-GHOST engine adversarial review

**Scope:** finite exact engine `observational_succ/no_ghost.py`, reviewed
2026-10-13 by a separate task agent after the first implementation. This is a
same-model collaborator review with independently chosen inputs, not a blind
independent mathematical witness or a mechanical refinement proof.

## Findings repaired before delivery

The reviewer supplied the following failing mutations to the implementation
agent, who repaired the code and added regression tests. The reviewer reran
each probe after repair; all return `False` as required.

| Mutation | Original failure mode | Final result |
|---|---|---|
| `verify_higher_failure(((0,),), ((1000000,),), 0)` | Final map image was not validated, allowing an out-of-range codomain value | Rejected |
| Boolean private comparison-map values | Python booleans could masquerade as integer indices | Rejected |
| `verify_higher_failure(((0,1),), ((1,0,2),), 0)` | The compared parallel paths had different fiber cardinalities | Rejected |
| Histories from otherwise identical models with different source IDs/bases | Metadata was absent from history identity and comparison checks | Rejected |
| Unavailability witness for `NOT_DECLARED` in a one-event malformed schedule | Access verifier did not first validate the declared whole schedule | Rejected |
| Forged current endpoint in an otherwise unchanged private path | Initial review identified a redundant-state validation risk; the implementer was concurrently adding the independent path verifier | Rejected |

The higher-coherence primitive now certifies a discrepancy between valid
finite permutations of the same index type. Physical/source lawfulness is
explicitly a separate requirement checked against model-backed fibers. It
does not infer lawful maps merely from an unequal pair of integer vectors.

After fixes the reviewer ran:

```sh
python -m unittest discover -s tests -p 'test_no_ghost.py'
```

Observed result: **32 tests passed**. The original separate private-carrier
coherence calibration has its own seven tests and is not included in that count.

## Solver calibration and mathematical check

The reviewer generated 1,200 deterministic-seed random exact rational systems
with 1--5 equations, 0--6 variables, signed numerators in `[-3,3]`, and
denominators in `[1,4]`. Every result was checked by its exact certificate
verifier. Observed counts were 355 feasible primal certificates and 845 Farkas
infeasibility certificates, with no unresolved cases at a 10,000-basis limit.
This finite calibration is not a universal correctness proof.

Reproduction:

```python
from random import Random
from fractions import Fraction as Q
from observational_succ.no_ghost import (
    solve_nonnegative, verify_primal, verify_dual,
)

r = Random(4389945)
counts = {}
for _ in range(1200):
    m, n = r.randint(1, 5), r.randint(0, 6)
    A = tuple(tuple(Q(r.randint(-3, 3), r.randint(1, 4))
                    for _ in range(n)) for _ in range(m))
    b = tuple(Q(r.randint(-3, 3), r.randint(1, 4)) for _ in range(m))
    result = solve_nonnegative(A, b, max_bases=10000)
    counts[result.status] = counts.get(result.status, 0) + 1
    if result.status == "LAWFUL_GLUING":
        assert verify_primal(A, b, result.primal)
    elif result.status == "PROBABILITY_COUPLING_FAILURE":
        assert verify_dual(A, b, result.dual)
    else:
        raise AssertionError(result)
print(counts)
```

The dual enumeration argument was also checked on paper. After exact row-rank
reduction, write the system `Cp=d` with `C` of full row rank `r`. A nonempty
normalized Farkas polyhedron `C^T y >= 0, d^T y = -1` has no lineality because
`C^T` is injective. Thus it has a vertex; at a vertex, the normalization row
and `r-1` suitably selected active column constraints span all `r` coordinates.
The implementation enumerates those choices, reconstructs original-row dual
coefficients through recorded row operations, and verifies their signs against
the original equations. The primal search similarly enumerates full-rank
column bases, allowing zero coordinates for degenerate basic solutions.
Budget exhaustion remains `UNRESOLVED`; it never substitutes for this argument.

## Source and authorization checks

An additional exact fixture used preparation weights `1/3,2/3`, two distinct
originals correlated with two current bit values, and one deterministic
measurement. Enumeration retained source/report joint masses exactly. The
operational checker accepted `1/3,2/3` and rejected the same supported paths
reweighted to `1/2,1/2`. It therefore did not mistake support for a realizable
law in this control.

The current contract is deliberately **closed world**: missing declared rows
mean unavailable instruments, not merely unknown empirical data. The engine
cannot authenticate a source, license a new measurement, certify an arbitrary
user-supplied repair's physical legality, or synthesize a general adaptive
policy. The finite repair optimizer assumes its menu was separately certified
legal and returns a minimum only within that declared menu and budget.
Conditional correctness under these contracts is the delivered claim.
