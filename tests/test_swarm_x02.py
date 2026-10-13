"""Focused X02 boundaries: marginal laws versus actual point sections."""
import unittest
from fractions import Fraction as Q
from scripts.swarm_x02_probe import (
    brute_sections, decodes_target, generated_group, inverse,
    joint_from_orbit_masses, orbit_partition, posterior, push,
    simplex_vertices_by_active_constraints, tree_holonomy, uniform_on,
)


class HolonomyLawBoundaryTests(unittest.TestCase):
    def test_nonabelian_invariant_law_is_not_a_random_point_section(self):
        generators = ((1, 0, 2), (1, 2, 0))
        self.assertEqual(len(generated_group(3, generators)), 6)
        edges = ((0, 0, generators[0]), (0, 0, generators[1]))
        self.assertEqual(brute_sections((0,), edges, 3), ())
        self.assertEqual(simplex_vertices_by_active_constraints(3, generators), ((Q(1, 3),) * 3,))

    def test_existing_point_section_does_not_lift_every_law(self):
        generators = ((1, 0, 2, 3), (1, 2, 0, 3))
        vertices = simplex_vertices_by_active_constraints(4, generators)
        self.assertEqual(len(vertices), 2)
        self.assertIn((Q(0), Q(0), Q(0), Q(1)), vertices)
        self.assertIn((Q(1, 3), Q(1, 3), Q(1, 3), Q(0)), vertices)
        self.assertEqual(brute_sections((0,), ((0, 0, g) for g in generators), 4), ((3,),))

    def test_original_coupling_is_not_replaced_by_marginals(self):
        parts = ((0,), (1,))
        diagonal = joint_from_orbit_masses(2, parts, ((Q(1, 2), Q(0)), (Q(0), Q(1, 2))))
        independent = joint_from_orbit_masses(2, parts, ((Q(1, 4), Q(1, 4)), (Q(1, 4), Q(1, 4))))
        self.assertEqual(tuple(sum(row) for row in diagonal), tuple(sum(row) for row in independent))
        self.assertEqual(tuple(map(sum, zip(*diagonal))), tuple(map(sum, zip(*independent))))
        self.assertTrue(decodes_target(diagonal, (0, 1)))
        self.assertFalse(decodes_target(independent, (0, 1)))
        self.assertNotEqual(posterior(diagonal, 0), posterior(independent, 0))

    def test_target_identifiability_depends_only_on_orbit_mass_support(self):
        joint = joint_from_orbit_masses(3, ((0, 1), (2,)), ((Q(1, 3), Q(0)), (Q(0), Q(2, 3))))
        self.assertEqual(posterior(joint, 0), posterior(joint, 1))
        self.assertTrue(decodes_target(joint, (0, 1)))
        self.assertEqual(push((1, 0, 2), joint[0]), joint[0])

    def test_null_condition_and_invalid_transport_fail_closed(self):
        with self.assertRaises(ValueError):
            posterior(((Q(1), Q(0)),), 1)
        with self.assertRaises(ValueError):
            inverse((0, 0))
        with self.assertRaises(ValueError):
            tree_holonomy((0, 1), (), 2)
        with self.assertRaises(ValueError):
            joint_from_orbit_masses(2, ((0,),), ((Q(1),),))

    def test_clock_uniformity_does_not_remove_cycle_residual(self):
        shift = (1, 2, 3, 0)
        self.assertEqual(orbit_partition(4, (shift,)), ((0, 1, 2, 3),))
        self.assertEqual(push(shift, uniform_on(4, (0, 1, 2, 3))), (Q(1, 4),) * 4)
        self.assertEqual(brute_sections((0,), ((0, 0, shift),), 4), ())


if __name__ == "__main__":
    unittest.main()
