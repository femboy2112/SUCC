"""Exact bridges between the Second Forge results and existing SUCC machinery.

Each test replays an EXISTING SUCC object through a new statement, so that the
claimed relationship in SUCC_INTEGRATION.md is executable rather than verbal.
"""
from fractions import Fraction as Q
from itertools import combinations
import random
import unittest

from observational_succ.ancestral_observer import audit_ancestral_observer
from observational_succ.carrier_relative_targets import (
    Carrier, Instrument, behavioral_partition, observable_algebra,
)
from observational_succ.future_safe_quotient import Edge, Machine, State
from observational_succ.observatoris_response_geometry import (
    matrix, quotient_pattern, structural_distance,
)


def random_carrier(rng, size, instruments, outputs):
    return Carrier("random", size, tuple(
        Instrument(f"i{k}", f"chart{k}",
                   tuple(Q(rng.randrange(outputs)) for _ in range(size)),
                   tuple(rng.randrange(size) for _ in range(size)))
        for k in range(instruments)))


def saturation(blocks, subset):
    return frozenset(x for block in blocks if set(block) & subset for x in block)


def galois_closure(basis, size, subset):
    """Common zeros of every function in span(basis) that vanishes on subset.

    Exact rational linear algebra: f = sum c_i b_i vanishes on `subset` iff c is
    in the null space of the basis rows restricted to `subset`.
    """
    rows = [[b[x] for b in basis] for x in sorted(subset)]      # |subset| x dim
    dim = len(basis)
    pivots, reduced = [], []
    for row in rows:
        row = list(row)
        for piv, r in zip(pivots, reduced):
            if row[piv] != 0:
                factor = row[piv]
                row = [u - factor * v for u, v in zip(row, r)]
        lead = next((i for i, v in enumerate(row) if v != 0), None)
        if lead is None:
            continue
        row = [v / row[lead] for v in row]
        for k, r in enumerate(reduced):
            if r[lead] != 0:
                factor = r[lead]
                reduced[k] = [u - factor * v for u, v in zip(r, row)]
        pivots.append(lead)
        reduced.append(row)
    free = [i for i in range(dim) if i not in pivots]
    null = []
    for f in free:
        vec = [Q(0)] * dim
        vec[f] = Q(1)
        for piv, r in zip(pivots, reduced):
            vec[piv] = -r[f]
        null.append(vec)
    closed = set()
    for x in range(size):
        if all(sum(c * b[x] for c, b in zip(vec, basis)) == 0 for vec in null):
            closed.add(x)
    return frozenset(closed)


class ContextualZeroIsSaturation(unittest.TestCase):
    def test_zero_ideal_closure_equals_behavioural_saturation(self):
        # For the observer algebra A of CARRIER_RELATIVE_TARGETS section 2 and a
        # possible-state set B: the common zeros of {f in A : f = 0 on B} are
        # exactly the union of behaviour classes meeting B.
        rng = random.Random(20261114)
        nontrivial = 0
        for _ in range(60):
            c = random_carrier(rng, rng.randint(2, 5), rng.randint(1, 2), 2)
            blocks = behavioral_partition(c)
            basis = [row.values for row in observable_algebra(c).rows]
            self.assertEqual(len(basis), len(blocks))
            for r in range(1, c.size + 1):
                for subset in combinations(range(c.size), r):
                    subset = frozenset(subset)
                    sat = saturation(blocks, subset)
                    self.assertEqual(galois_closure(basis, c.size, subset), sat)
                    nontrivial += sat != subset
        self.assertGreater(nontrivial, 0)


class AncestralChainIsACostGhost(unittest.TestCase):
    """SUCC's PAP-04 chain a -> b -> c with reports A, A, B."""

    def setUp(self):
        states = tuple(State(n, "src", o) for n, o in (("a", "A"), ("b", "A"), ("c", "B")))
        edges = (Edge("a", "go", "b", Q(1)), Edge("b", "go", "c", Q(1)))
        self.machine = Machine(states, ("go",), edges)
        self.labels = ("A", "A", "B")

    def test_endpoint_exact_over_truth_values(self):
        for start in ("a", "b", "c"):
            self.assertTrue(audit_ancestral_observer(self.machine, self.labels, start).endpoint_exact)

    def test_not_exact_over_costs_and_the_quotient_errs_low(self):
        # Same table read over step counts: the quotient reaches B from the
        # report of `a` in one step; the source needs two.  Exactness does not
        # transport backwards along the cost -> truth change of base, and the
        # quotient distance is a lower bound, never an upper bound (CG-2).
        a = matrix(((0, 0, 0), (1, 0, 0), (0, 1, 0)))
        source = structural_distance(a)
        quotient = structural_distance(quotient_pattern(a, (0, 0, 1)))
        self.assertEqual(source[0][2], 2)
        self.assertEqual(quotient[0][1], 1)
        self.assertLess(quotient[0][1], source[0][2])
        # from the other representative the quotient distance is attained
        self.assertEqual(source[1][2], quotient[0][1])

    def test_three_state_ghost_is_a_truth_level_failure(self):
        states = tuple(State(n, "src", o) for n, o in (("a", "A"), ("b", "A"), ("c", "B")))
        ghost = Machine(states, ("go",), (Edge("b", "go", "c", Q(1)),))
        audit = audit_ancestral_observer(ghost, self.labels, "a")
        self.assertFalse(audit.endpoint_exact)
        self.assertEqual(audit.ghost_reports, ("B",))
        a = matrix(((0, 0, 0), (0, 0, 0), (0, 1, 0)))
        self.assertIsNone(structural_distance(a)[0][2])
        self.assertEqual(structural_distance(quotient_pattern(a, (0, 0, 1)))[0][1], 1)


if __name__ == "__main__":
    unittest.main()
