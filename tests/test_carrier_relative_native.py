"""Native host integration: requires actual existing SUCC modules, no shims."""
import unittest
from fractions import Fraction as Q
from observational_succ.carrier_relative_targets import (
    Target, from_contextual_field, observable_algebra, behavioral_partition,
    plan_target, target_obstruction,
)
from observational_succ.coherent_zero_relations import Poly, ZeroRelation
from observational_succ.contextual_zero_navigation import SourceField, Probe, Move
from observational_succ.field_limit_compactness import finite_closed_cylinder_prefix
from observational_succ.succ_internal_matrix_walk import PhasePoly, original_state


class NativeTargetDescentTests(unittest.TestCase):
    def test_contextual_observer_can_know_parity_without_position(self):
        x = Poly.var(("x",), "x")
        parity = (2*x**3-9*x**2+10*x)*Q(1, 3)
        world = SourceField("Z4:source", ("x",), tuple((Q(i),) for i in range(4)),
            (ZeroRelation("Z4:source", "state-polynomial", x*(x-1)*(x-2)*(x-3)),),
            (Probe("Z4:source", "parity", parity, 1),),
            (Move("Z4:source", "succ", (1, 2, 3, 0), 1),))
        carrier = from_contextual_field(world)
        t = Target(world.source_id, "parity", (Q(0), Q(1), Q(0), Q(1)))
        hidden = Target(world.source_id, "whole-position", tuple(map(Q, range(4))))
        self.assertEqual(behavioral_partition(carrier), ((0, 2), (1, 3)))
        self.assertIsNotNone(observable_algebra(carrier).express(carrier, t))
        self.assertEqual(plan_target(carrier, t, 1).worst_cost, 1)
        self.assertEqual(target_obstruction(carrier, hidden), (0, 2))

    def test_inherited_finite_cylinder_is_not_an_infinite_proof(self):
        receipt = finite_closed_cylinder_prefix(((0,), (0, 1), (0, 1, 0)))
        self.assertTrue(receipt['finite_closed_fibers_have_nonempty_intersection'])
        self.assertFalse(receipt['finitely_verified_global_source'])

    def test_matrix_target_descends_under_global_phase_gauge(self):
        points = tuple(original_state(n) for n in range(1, 5))
        def purity(points, width):
            total = PhasePoly.zero()
            for x in points:
                for y in points:
                    for k in range(width):
                        for j in range(width):
                            total = total+PhasePoly.monomial((k-j)*(x-y))
            return total / (len(points)**2)
        for width in (2, 3):
            self.assertEqual(purity(points, width), purity(tuple(x+Q(2, 7) for x in points), width))
        self.assertNotEqual(points, tuple(x+Q(2, 7) for x in points))


if __name__ == '__main__':
    unittest.main()
