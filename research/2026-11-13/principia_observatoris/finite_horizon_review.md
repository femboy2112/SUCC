# Finite-horizon theorem forge and audit

## Ownership and authority

This is the local derivation/audit record for
[Book IV](../../../docs/principia_observatoris/04_horizons_completion.md).
It was prepared by a separate same-model workstream. This is useful task
separation, not external peer review, independent model agreement, or a formal
kernel receipt. The root must separately review the statements and integration.
No external physical measurement was performed.

The inherited baseline is PR #618 at
`ab31057590a59b2bfbd5dbcd7126b2aefc7a2b55`, with main at
`db9fb4b84672050efa79b13377f1e73364598a14`. This work read `AGENTS.md`,
`docs/METHOD.md`, all nine sections of the founding note,
`docs/CARRIER_RELATIVE_TARGETS.md`, and the Principia ancestral supplement.
No archival source was edited.

## Hole contract and final verdict

**Question.** Which authenticated source restrictions force every genuine
future response disagreement to have a bounded finite witness?

**Candidate before proof.** For two finite-dimensional switched response laws
of dimensions `n,m`, inequivalence has a word witness of length at most
`n+m−1`. The bound is about exact response laws and declared lawful words,
not finite stochastic outcome samples or single-copy target acquisition.

**Verdict: CLASSICAL / PROVED PAPER.** PO-H2–H3 prove the stronger accessible
rank bound `r−rank(B)`. The proof closes the finite-versus-all-word comparison
edge for that restricted model class. It does not authenticate its own model
class. PO-H4–H5 establish the recurrence/Hankel interface and explicitly kill
inference of global low rank from a finite low-rank block.

**Novelty tax.** The core result is classical weighted-automaton equivalence
and finite realization theory. No new theorem priority is claimed. The source
promise/access distinction, combined sharp examples, and stable response-bank
certificate are the contribution to this manuscript's organization. The
finite discrimination theorem is not a reformulation of π normality; its
hypotheses have not been established for the asymptotic arithmetic target.

**Strongest reusable quantitative residual.** PO-H10 gives
`||CL_wB||≤ε κ K β` from a complete reachable basis, a finite response error
bound, basis conditioning, and a uniform semigroup bound. This is a proved
conditional estimate, not a fitted noise extrapolation. Each missing factor
has an exact scalar countermodel.

## Proof and assumption audit

| Item | Check made | Outcome / boundary |
|---|---|---|
| Word order | Column states use `L_w=L_last…L_first` | Recursion adds new final actions on the left; matches actual execution |
| Zero preparation | `B=0` handled before subtracting its rank | Every response zero; no invalid negative horizon |
| Multiple preparations | Start rank is `rank B`, not input dimension | Rank-deficient input ports do not buy false horizon improvements |
| Stabilization | Equality of two consecutive spans implies invariance | No appeal to observed rank stabilization without known actions |
| Pair comparison | Block-diagonal updates, stacked preparation, signed readout | Difference of the two actual laws, without mixing sources |
| Sharpness | Rational Lagrange-weight mode split | First mismatch exactly at `n+m−1`, even both dimensions positive |
| Finite machines | Moore convention includes present readout at length zero | Bound `N−k`; instrument output-before-transition may need one extra readout action |
| Recurrences | Coefficients supplied: `d` values; only separate order bounds: `d₁+d₂` values | Quantifiers not conflated |
| Hankel promise | Uses full infinite rank, not a sampled block | Delayed spike has zero sampled block but full rank `J+1` |
| Stochastic access | Bernoulli `1/3` and `2/3` have common finite support | Exact law distinction does not give finite zero-error identification |
| Cost | Finite witness length, query cost and description length separated | `N`-query adversary and halting reduction retained |
| Completion | Fixed continuous map, same source, explicit moduli when used | Discontinuous and moving-probe counterexamples retained |
| Robust bank | Norms on `U,R,W`; coordinates in `l1`; `K` uniform in words | Submultiplicative bound is well typed; stability and conditioning are not inferred |

**Next falsifier.** Attempt to remove any one of the global dimension promise,
exact common response typing, reachable-basis completeness, stability, or
conditioning premises. The retained models already refute the unrestricted
versions. An experimentally useful extension requires a lawful preparation
policy and certified error/access costs, rather than a new name for the same
finite algebraic span.

## Primary-source provenance check

- [Kiefer, Murawski, Ouaknine, Wachter and Worrell,
  *On the Complexity of Equivalence and Minimisation for Q-weighted Automata*](https://www.cs.ox.ac.uk/james.worrell/fossacs12-journal.pdf),
  Proposition 3.1: checked the full paper's span/short-witness formulation.
  It directly precedes the finite comparison argument used here.
- [Tzeng, *A Polynomial-Time Algorithm for the Equivalence of Probabilistic
  Automata*](https://doi.org/10.1137/0221017), SIAM J. Comput. 21(2), 1992,
  216–227: official publisher metadata/abstract checked for the earlier
  algorithmic lineage; the paywalled full article was not used as a proof
  dependency.
- [Kiefer, *Notes on Equivalence and Minimization of Weighted Automata*](https://arxiv.org/pdf/2009.01217),
  Proposition 2.2 and Theorem 2.3, checked in the author's full text: confirms
  the non-new status and the standard `n₁+n₂−1` bound. The manuscript gives
  its own short elementary proof instead of redistributing the paper.

No theorem is marked new because a source search missed a predecessor. The
literature audit is bounded; it does not establish exhaustive priority.

## Executed preparatory exact checks

The following independent small implementation was executed successfully with
Python's integers and `fractions.Fraction`. It does not import the repository's
new linear-closure code. The binary action matrices and signed preparation /
readout vectors are an exhaustive bounded family, not a universal proof.
The proof supplies the infinite lift.

```json
{
  "holdout_max_word_length": 5,
  "sharp_pair": [["1/3", "1/3"], ["1/2", "1/2"], ["1/2", "1/2"], ["1/2", "-1/2"]],
  "shortened_horizon_mutant_rejected": true,
  "switched_2d_models": 20736,
  "vandermonde_sharp_dimensions": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
  "zero_through_length_1_models": 5152
}
```

To replay the exact check from any working directory:

```python
from fractions import Fraction as Q
from itertools import product
from math import prod
import json

sharp = []
for N in range(2, 13):
    nodes = range(N)
    ds = [Q(1, prod(j-l for l in nodes if l != j)) for j in nodes]
    ys = [sum(d * Q(j)**k for d, j in zip(ds, nodes)) for k in range(N)]
    assert ys == [Q(0)] * (N-1) + [Q(1)]
    sharp.append(N)

matrices = list(product((0, 1), repeat=4))
vectors = list(product((-1, 0, 1), repeat=2))
def mv(A, v):
    return (A[0]*v[0] + A[1]*v[1], A[2]*v[0] + A[3]*v[1])
def dot(c, v):
    return c[0]*v[0] + c[1]*v[1]

models = vanishing = 0
for A, B, b, c in product(matrices, matrices, vectors, vectors):
    models += 1
    if all(dot(c, v) == 0 for v in [b, mv(A, b), mv(B, b)]):
        vanishing += 1
        frontier = [b]
        for depth in range(6):
            assert all(dot(c, v) == 0 for v in frontier)
            frontier = [mv(M, v) for v in frontier for M in (A, B)]

L1, L2 = (0, 0, 0, 1), (2, 0, 0, 3)
b1 = b2 = (Q(1), Q(1))
c1, c2 = (Q(-1, 6), Q(1, 2)), (Q(1, 2), Q(-1, 6))
pairs = []
for k in range(4):
    pairs.append((dot(c1, b1), dot(c2, b2)))
    b1, b2 = mv(L1, b1), mv(L2, b2)
assert all(a == b for a, b in pairs[:3])
assert pairs[3][0] - pairs[3][1] == 1
print(json.dumps({
    'vandermonde_sharp_dimensions': sharp,
    'switched_2d_models': models,
    'zero_through_length_1_models': vanishing,
    'holdout_max_word_length': 5,
    'shortened_horizon_mutant_rejected': True,
    'sharp_pair': [[str(a), str(b)] for a, b in pairs]
}, sort_keys=True))
```

## Cross-audit of Book V

Reviewed PO-C1–C4 and their countermodels in
[Book V](../../../docs/principia_observatoris/05_effective_classicality.md).
The exact instrument descent is well typed: nonnegative kernel entries arise
from positive operators in the commutative algebra, and complete instrument
unitality gives the required joint outcome/next-state normalization. The
approximate `Nε` result is sound because it tracks **unnormalized** quantum
branches and the full outcome stack; no rare-outcome posterior is divided by
its probability. The calibration must hold for every reachable conditional
state; the chapter uses the stronger all-state hypothesis explicitly.

One proof-clarity repair was recommended to the root: for randomized policies,
condition on the entire private random seed and average afterward, or include
action choices and relevant private memory in the branch label. This avoids
treating correlated private randomness as if it were independent at every
outcome-only history. The mathematical bound survives that repair. No other
load-bearing error was found in this bounded same-model audit.
