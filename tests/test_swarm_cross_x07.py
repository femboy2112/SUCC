"""Boundary regressions for X07's source-indexed stochastic trace object."""
import unittest
from fractions import Fraction as Q
from itertools import product
from observational_succ.swarm_probability import StochasticInstrument, compose, commutation_defect
from scripts.swarm_cross_x07_probe import (
    matrix,multiply,normalize,mass,original_support,path_sum,boundary_controls,
    bayes_and_wealth_controls,coordinate_kernel,
)


class X07BoundaryTests(unittest.TestCase):
    def test_deterministic_instruments_still_need_deterministic_preparation(self):
        result = boundary_controls()['mixed_preparation_not_single_F48_preparation']
        self.assertEqual(result['mixed_outcome_supports'], [[0], [0]])
        self.assertEqual(result['pure_outcome_supports'], [[[0], []], [[], [0]]])

    def test_C17_C22_against_independent_atom_path_sums(self):
        instruments = [StochasticInstrument(str(i),'source','S','S',2,
                       tuple(((report,after,Q(1)),) for report,after in choices))
                       for i,choices in enumerate(product(tuple(product(range(2),repeat=2)),repeat=2))]
        for first,second in product(instruments,repeat=2):
            combined = compose(first,second)
            all_commute = True
            for a,b in product(range(2),repeat=2):
                ka = matrix(tuple(tuple(sum(p for report,z,p in row if report == a and z == y)
                                  for y in range(2)) for row in first.rows))
                kb = matrix(tuple(tuple(sum(p for report,z,p in row if report == b and z == y)
                                  for y in range(2)) for row in second.rows))
                all_commute = all_commute and multiply(ka,kb) == multiply(kb,ka)
                for x in range(2):
                    point = (tuple(Q(i == x) for i in range(2)),)
                    expected = path_sum(point,(ka,kb))[0]
                    actual = tuple(sum(p for report,y,p in combined.rows[x]
                                       if report == (a,b) and y == z) for z in range(2))
                    self.assertEqual(expected,actual)
            self.assertEqual(commutation_defect(first,second) is None,all_commute)

    def test_joint_original_law_is_stronger_than_current_and_record_law(self):
        result = boundary_controls()['same_outcome_mass_and_current_law_different_originals']
        self.assertEqual(result['event_mass'],Q(1,2))
        self.assertNotEqual(result['originals_ab'],result['originals_ba'])

    def test_positive_normalized_agreement_does_not_certify_likelihoods(self):
        result = boundary_controls()['same_normalized_joint_law_different_likelihoods']
        self.assertEqual(result,{'ab_mass':Q(1,4),'ba_mass':Q(1,8)})

    def test_zero_is_a_total_measure_state_but_has_no_posterior(self):
        zero = matrix(((0,0),(0,0)))
        law = ((Q(1),Q(0)),)
        self.assertEqual(mass(multiply(law,zero)),0)
        self.assertIsNone(normalize(multiply(law,zero)))
        self.assertEqual(original_support(multiply(law,zero)),frozenset())

    def test_typed_variable_carrier_composition_preserves_originals(self):
        law = ((Q(1,3),Q(0)),(Q(0),Q(2,3)))
        a = matrix(((Q(1,2),Q(1,2),0),(0,0,1)))
        b = matrix(((Q(1,4),),(Q(1,2),),(Q(3,4),)))
        result = multiply(multiply(law,a),b)
        self.assertEqual(result,path_sum(law,(a,b)))
        self.assertEqual(result,((Q(1,8),),(Q(1,2),)))
        with self.assertRaises(ValueError):
            multiply(b,a)

    def test_distinct_local_noisy_reset_events_commute(self):
        a,b = coordinate_kernel(0,0),coordinate_kernel(1,1)
        self.assertEqual(multiply(a,b),multiply(b,a))
        # Same-coordinate events cannot be freely exchanged.
        self.assertNotEqual(multiply(a,coordinate_kernel(0,1)),
                            multiply(coordinate_kernel(0,1),a))

    def test_duplicate_wealth_uses_conditional_likelihood(self):
        result = bayes_and_wealth_controls()
        self.assertEqual(result['duplicate_lr_expectation'],1)
        self.assertEqual(result['marginal_reuse_expectation'],Q(7,3))
        self.assertGreater(result['false_wealth_crossing'],result['purported_ville_bound'])

    def test_nonprobability_weights_rejected(self):
        for bad in (((0.5,0.5),),((True,0),),((-1,1),),((1,1),)):
            with self.assertRaises(ValueError):
                matrix(bad)


if __name__ == '__main__':
    unittest.main()
