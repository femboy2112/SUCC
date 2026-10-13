"""Independent X10 regression controls for the boundaries of the synthesis."""
import unittest
from fractions import Fraction as Q
from scripts.swarm_cross_x10_probe import (
    basis_add, generated_observable_algebra, word_orbit_relation,
    les_convolution, jet_controls, observed_paths, total_variation,
)


class X10BoundaryTests(unittest.TestCase):
    def test_invariant_linear_span_does_not_supply_all_repaired_observables(self):
        # Swap two bits: affine functions are invariant but miss the product.
        report, swap = (0,0,1,1), (0,2,1,3)
        self.assertEqual(len(generated_observable_algebra(report, (swap,))), 4)
        linear = {}
        for vector in ((1,1,1,1), report, (0,1,0,1)):
            basis_add(linear, vector)
        self.assertEqual(len(linear), 3)
        self.assertTrue(basis_add(linear, (0,0,0,1)))

    def test_constant_report_does_not_reconstruct_hidden_original_state(self):
        self.assertEqual(word_orbit_relation((0,0), ((0,1),)),
                         {(0,0),(0,1),(1,0),(1,1)})
        self.assertEqual(len(generated_observable_algebra((0,0), ((0,1),))), 1)

    def test_path_bound_requires_uniform_source_defect(self):
        kernel = ((Q(1),Q(0),Q(0)), (Q(0),Q(0),Q(1)), (Q(0),Q(0),Q(1)))
        candidate = ((Q(1),Q(0)), (Q(0),Q(1)))
        actual = observed_paths(kernel, (0,0,1), (Q(0),Q(1),Q(0)), 1)
        guessed = observed_paths(candidate, (0,1), (Q(1),Q(0)), 1)
        error = total_variation(actual, guessed)
        self.assertEqual(error, 1)
        self.assertGreater(error, Q(1,3))  # Mean source-row defect is insufficient.

    def test_filtered_force_is_not_only_a_pressure_gradient(self):
        self.assertEqual(les_convolution(2), (0,Q(3,2)))
        self.assertEqual(les_convolution(101), (0,Q(201,2)))

    def test_finite_jet_hierarchy_has_both_negative_and_positive_controls(self):
        control = jet_controls()
        self.assertEqual(len(control['unbounded_degree_counterexamples']), 12)
        self.assertEqual(control['bounded_degree_exact_flow_checks'], 28)
        for case in control['unbounded_degree_counterexamples']:
            self.assertTrue(all(x == 0 for x in case['reported_jets']))
            self.assertGreater(case['missing_jet'], 0)


if __name__ == '__main__':
    unittest.main()
