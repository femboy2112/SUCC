"""Finite-precision acquisition tests with independent finite-alphabet controls."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.tenacious_acquisition import (
    ContractError, IntervalAction, best_interval_schedule, central_radius,
)

IDENTITY = ((1, 0), (0, 1))


class CenteredAcquisitionTests(unittest.TestCase):
    def test_diagonal_slab_with_noncoordinate_objective(self):
        radius, point = central_radius((1, 1), (2, 1), [((1, 1), Q(1, 4))])
        self.assertEqual(radius, Q(5, 4))
        self.assertEqual(point, (1, Q(-3, 4)))

    def test_destructive_order_and_noise_floor(self):
        # Erase the other coordinate immediately after it has been used.
        move = IntervalAction(((0, 1), (0, 0)), (1, 0), Q(1, 4), 1)
        first = IntervalAction(IDENTITY, (1, 0), Q(1, 4), 1)
        radius, word, hidden = best_interval_schedule((1, 1), (1, 1), (move, first), 2)
        self.assertEqual((radius, word), (Q(1, 2), (1, 0)))
        self.assertEqual(sum(hidden), radius)

    def test_compare_with_actual_finite_record_game(self):
        # Grid includes maximizing zero-cell pair. Branching permits either
        # readout at a closed cell boundary, as required by the sensor contract.
        pts = tuple(product((Q(-1), Q(-1, 4), Q(0), Q(1, 4), Q(1)), repeat=2))
        centers = tuple(Q(i, 2) for i in range(-2, 3))
        def game(states, budget):
            values = [sum(x) for x in states]
            best = (max(values)-min(values))/2
            if budget:
                for axis in (0, 1):
                    children = [tuple(x for x in states if abs(x[axis]-z) <= Q(1, 4))
                                for z in centers]
                    best = min(best, max(game(child, budget-1) for child in children if child))
            return best
        actions = tuple(IntervalAction(IDENTITY, v, Q(1, 4), 1)
                        for v in ((1, 0), (0, 1)))
        for cost in range(3):
            self.assertEqual(game(pts, cost), best_interval_schedule((1, 1),(1, 1),actions,cost)[0])

    def test_zero_width_degenerate_box_and_zero_budget(self):
        self.assertEqual(central_radius((0, 2), (8, -1))[0], 2)
        sensor = IntervalAction(((1,),), (1,), 0, 2)
        self.assertEqual(best_interval_schedule((1,), (1,), [sensor], 1)[:2], (1, ()))
        self.assertEqual(best_interval_schedule((1,), (1,), [sensor], 2)[:2], (0, (0,)))

    def test_invalid_contracts(self):
        for malformed in ((IDENTITY, (1,), 0, 1), (IDENTITY, (1, 0), -1, 1),
                          (IDENTITY, (0, 1), 0, True), (IDENTITY, (1, 0), 0.5, 1)):
            with self.assertRaises(ContractError):
                IntervalAction(*malformed)
        with self.assertRaises(ContractError):
            central_radius((1,), (1,), [((1, 0), 0)])
        with self.assertRaises(ContractError):
            best_interval_schedule((), (), (), 0)
