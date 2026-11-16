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
        # quotient distance is a lower bound, never an upper bound (QG-2).
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


def cyclic_map(modulus, f):
    """Pattern matrix of x -> f(x) on Z/modulus, as edges x -> f(x)."""
    return matrix(tuple(tuple(int(f(u) % modulus == v) for u in range(modulus))
                        for v in range(modulus)))


def reachable_reports(a, labels, start):
    dist = structural_distance(a)[start]
    return {labels[v] for v in range(len(a)) if dist[v] is not None}


class SuccessorAndMultiplierUnderObservation(unittest.TestCase):
    """SUCC (x -> x+1) and FUCC-2 (x -> 2x) on Z/12 under two observations."""

    N = 12

    def exact_levels(self, a, labels):
        truth = cost = True
        dq = structural_distance(quotient_pattern(a, labels))
        ds = structural_distance(a)
        for x in range(self.N):
            for b in set(labels):
                source = [ds[x][z] for z in range(self.N)
                          if labels[z] == b and ds[x][z] is not None]
                quotient = dq[labels[x]][b]
                if (quotient is None) != (not source):
                    truth = False
                elif source and min(source) != quotient:
                    cost = False
        return truth, truth and cost

    def test_residue_observation_is_exact_for_both_operations(self):
        residue = tuple(x % 3 for x in range(self.N))
        self.assertEqual(self.exact_levels(cyclic_map(self.N, lambda x: x + 1), residue),
                         (True, True))
        self.assertEqual(self.exact_levels(cyclic_map(self.N, lambda x: 2 * x), residue),
                         (True, True))

    def test_magnitude_observation_of_successor_is_a_cost_ghost_only(self):
        # Blocks {0..3}, {4..7}, {8..11}: every report is eventually reached from
        # every start, but the quotient claims one step where a carry needs four.
        magnitude = tuple(x // 4 for x in range(self.N))
        succ = cyclic_map(self.N, lambda x: x + 1)
        self.assertEqual(self.exact_levels(succ, magnitude), (True, False))
        self.assertEqual(structural_distance(succ)[0][4], 4)
        self.assertEqual(structural_distance(quotient_pattern(succ, magnitude))[0][1], 1)

    def test_magnitude_observation_of_multiplier_is_a_truth_ghost(self):
        # 0 is fixed by doubling, 1 is not, and both are read as "small".
        magnitude = tuple(x // 4 for x in range(self.N))
        fucc = cyclic_map(self.N, lambda x: 2 * x)
        self.assertEqual(self.exact_levels(fucc, magnitude)[0], False)
        self.assertEqual(reachable_reports(fucc, magnitude, 0), {0})
        self.assertEqual(reachable_reports(fucc, magnitude, 1), {0, 1, 2})
        # hereditary invariant {0} is the obstruction certificate (PAP-05)
        self.assertEqual(structural_distance(fucc)[0], (0,) + (None,) * 11)


if __name__ == "__main__":
    unittest.main()
