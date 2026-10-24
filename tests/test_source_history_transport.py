"""Independent assignment calibration of exact circular history transport."""

from dataclasses import replace
from fractions import Fraction as Q
from itertools import combinations_with_replacement, product
import unittest

from observational_succ.pi_source_collision import prime_window
from observational_succ.source_history_stationarity import (
    PositiveHistoryMixture, apply_history_filter,
)
from observational_succ.source_history_transport import (
    AtomicProbability, PREREGISTERED_HISTORY_DEPTHS, PREREGISTERED_PRIMES,
    brute_force_equal_weight_w1, circle_w1, circle_w1_certificate,
    empirical_law, history_average, history_preservation_certificate,
    multiplication_pushforward, validate_circle_w1_certificate,
)


class CircleTransportTests(unittest.TestCase):
    def test_wrap_cost_rejects_sorted_line_surrogate(self):
        first, second = empirical_law((0,)), empirical_law((Q(9, 10),))
        self.assertEqual(circle_w1(first, second), Q(1, 10))
        self.assertNotEqual(circle_w1(first, second), Q(9, 10))
        self.assertEqual(circle_w1(first, empirical_law((Q(1, 2),))), Q(1, 2))
        self.assertEqual(circle_w1(first, first), 0)

    def test_all_small_multisets_against_all_assignment_permutations(self):
        cases = assignments = 0
        for modulus, sizes in ((3, (1, 2, 3)), (5, (2,))):
            points = tuple(Q(j, modulus) for j in range(modulus))
            for size in sizes:
                supports = tuple(combinations_with_replacement(points, size))
                for first, second in product(supports, repeat=2):
                    oracle = brute_force_equal_weight_w1(first, second)
                    mu, nu = empirical_law(first), empirical_law(second)
                    cert = circle_w1_certificate(mu, nu)
                    self.assertEqual(cert.cost, oracle['cost'])
                    self.assertTrue(validate_circle_w1_certificate(mu, nu, cert))
                    cases += 1
                    assignments += oracle['assignments_enumerated']
        self.assertEqual(cases, 370)
        self.assertEqual(assignments, 1131)

    def test_distinct_denominators_and_duplicate_masses_against_assignments(self):
        cases = (
            ((0, Q(1, 7), Q(3, 5), Q(9, 10)),
             (Q(1, 6), Q(2, 7), Q(8, 9), Q(11, 12))),
            ((0, 0, Q(1, 2), Q(1, 2), Q(7, 8)),
             (Q(1, 10), Q(1, 5), Q(1, 5), Q(4, 5), Q(9, 10))),
            ((Q(-1, 10), 0, Q(1, 11), Q(2, 3), Q(4, 5), Q(8, 7)),
             (Q(1, 13), Q(1, 7), Q(3, 8), Q(5, 11), Q(9, 10), Q(13, 10))),
        )
        for first, second in cases:
            self.assertEqual(circle_w1(empirical_law(first), empirical_law(second)),
                             brute_force_equal_weight_w1(first, second)['cost'])

    def test_weighted_law_matches_repeated_equal_weight_atoms(self):
        first = AtomicProbability(((0, Q(1, 2)), (Q(1, 3), Q(1, 3)),
                                   (Q(4, 5), Q(1, 6))))
        second = AtomicProbability(((Q(9, 10), Q(1, 3)), (Q(1, 2), Q(2, 3))))
        expanded_first = (0, 0, 0, Q(1, 3), Q(1, 3), Q(4, 5))
        expanded_second = (Q(9, 10), Q(9, 10))+(Q(1, 2),)*4
        self.assertEqual(circle_w1(first, second),
                         brute_force_equal_weight_w1(expanded_first, expanded_second)['cost'])

    def test_exact_dual_witness_and_mutations(self):
        first = empirical_law((0, Q(1, 5), Q(9, 10)))
        second = empirical_law((Q(1, 10), Q(2, 5), Q(3, 5)))
        cert = circle_w1_certificate(first, second)
        self.assertTrue(validate_circle_w1_certificate(first, second, cert))
        for mutated in (
            replace(cert, cost=cert.cost+Q(1, 1000)),
            replace(cert, flux_shift=cert.flux_shift+1),
            replace(cert, dual_slopes=(Q(2),)+cert.dual_slopes[1:]),
            replace(cert, dual_potential=cert.dual_potential[:-1]+(Q(1),)),
            replace(cert, cost=float(cert.cost)),
            replace(cert, flux=cert.flux[:-1]),
        ):
            self.assertFalse(validate_circle_w1_certificate(first, second, mutated))

    def test_rotation_symmetry_triangle_and_tripling_lipschitz(self):
        laws = tuple(empirical_law(points) for points in (
            (0, Q(1, 7), Q(9, 10)),
            (Q(1, 3), Q(1, 3), Q(5, 8)),
            (Q(2, 9), Q(4, 7), Q(12, 13)),
        ))
        for first, second in product(laws, repeat=2):
            distance = circle_w1(first, second)
            self.assertEqual(distance, circle_w1(second, first))
            rotated = tuple(AtomicProbability(tuple((x+Q(11, 17), mass)
                              for x, mass in law.atoms)) for law in (first, second))
            self.assertEqual(distance, circle_w1(*rotated))
            self.assertLessEqual(circle_w1(multiplication_pushforward(first),
                                          multiplication_pushforward(second)),
                                 3*distance)
            for third in laws:
                self.assertLessEqual(distance, circle_w1(first, third)+circle_w1(third, second))

    def test_canonicalization_merges_wrap_and_zero_masses(self):
        law = AtomicProbability(((0, Q(1, 4)), (1, Q(1, 4)),
                                 (Q(-1, 3), Q(1, 2)), (Q(1, 7), 0)))
        self.assertEqual(law.atoms, ((Q(), Q(1, 2)), (Q(2, 3), Q(1, 2))))

    def test_probability_domain_guards(self):
        for atoms in ((), None, {0: 1}, ((0, -1), (Q(1, 2), 2)),
                      ((0, Q(1, 2)),), ((0.0, 1),), ((0, 1.0),),
                      ((True, 1),), ((0, True),), ((0, 1, 2),)):
            with self.assertRaises(ValueError):
                AtomicProbability(atoms)
        for points in ((), None, {0: 1}, (0.5,), (True,)):
            with self.assertRaises(ValueError):
                empirical_law(points)
        law = empirical_law((0,))
        with self.assertRaises(ValueError):
            circle_w1((0,), law)
        with self.assertRaises(ValueError):
            validate_circle_w1_certificate(law, law, None)

    def test_assignment_oracle_domain_and_budget(self):
        for first, second in (((), ()), ((0,), (0, 1)), ((0,)*9, (0,)*9),
                              ((0.5,), (0,)), ((True,), (0,)), ({0: 1}, (0,))):
            with self.assertRaises(ValueError):
                brute_force_equal_weight_w1(first, second)


class HistoryPreservationTests(unittest.TestCase):
    def test_midpoint_identity_and_exact_telescoping_boundary(self):
        for points in ((0, Q(1, 5)), (Q(1, 7), Q(3, 8), Q(11, 13))):
            mu = empirical_law(points)
            for depth, multiplier in product((1, 2, 3, 4, 8), (1, 2, 3, 5)):
                cert = history_preservation_certificate(mu, depth, multiplier)
                self.assertEqual(cert['averaged_one_step_defect'], cert['exact_boundary_term'])
                self.assertLessEqual(cert['beta'], cert['exact_bound'])
                self.assertLessEqual(cert['exact_bound'], cert['universal_bound'])
                if depth == 2:
                    self.assertEqual(2*cert['epsilon'], cert['beta'])

    def test_constant_sources_survive_without_haar_conclusion(self):
        for point, depth in product((0, Q(1, 2)), (2, 4, 8)):
            mu = empirical_law((point,))
            cert = history_preservation_certificate(mu, depth)
            self.assertEqual(cert['beta'], 0)
            self.assertEqual(cert['epsilon'], 0)
            self.assertEqual(history_average(mu, depth), mu)
            self.assertEqual(len(mu.atoms), 1)

    def test_base16_fixed_point_need_not_preserve_tripling_history(self):
        mu = empirical_law((Q(1, 5),))
        self.assertEqual(multiplication_pushforward(mu, 16), mu)
        cert = history_preservation_certificate(mu, 4)
        self.assertEqual(cert['beta'], Q(2, 5))
        # Unique coupling from a Dirac mass: distances 0,2/5,2/5,1/5.
        self.assertEqual(cert['epsilon'], Q(1, 4))
        self.assertGreater(cert['epsilon'], 0)

    def test_signed_q5_preservation_does_not_imply_tripling_invariance(self):
        weights = (Q(), Q(3, 8), Q(1, 8), Q(1, 8), Q(3, 8))
        signed_filter = (0, 1, 1, -1)
        output = apply_history_filter(weights, 3, signed_filter)
        self.assertEqual(output, weights)
        mu = AtomicProbability(tuple((Q(j, 5), mass) for j, mass in enumerate(weights)))
        self.assertEqual(multiplication_pushforward(mu, 16), mu)
        self.assertEqual(circle_w1(multiplication_pushforward(mu), mu), Q(1, 10))
        self.assertEqual(history_preservation_certificate(mu, 4)['epsilon'], Q(1, 20))
        with self.assertRaises(ValueError):
            PositiveHistoryMixture(signed_filter)

    def test_history_domain_guards(self):
        mu = empirical_law((0,))
        for depth in (0, -1, True, Q(2), 2.0):
            with self.assertRaises(ValueError):
                history_average(mu, depth)
            with self.assertRaises(ValueError):
                history_preservation_certificate(mu, depth)
        for multiplier in (0, -1, True, Q(3), 3.0):
            with self.assertRaises(ValueError):
                multiplication_pushforward(mu, multiplier)

    def test_prespecified_windows_and_authentic_source_control(self):
        self.assertEqual(PREREGISTERED_PRIMES, (137, 281, 521))
        self.assertEqual(PREREGISTERED_HISTORY_DEPTHS, (2, 4, 8))
        # A small authenticated control keeps the unit suite bounded. The
        # CLI receipt evaluates and retains all nine preregistered windows.
        window = prime_window(41)
        state, independent = Q(), []
        for n in range(1, 4*window.start+1):
            forcing = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
            state = (16*state+forcing) % 1
            if n > window.start:
                independent.append(state)
        self.assertEqual(tuple(independent), window.states)
        cert = history_preservation_certificate(empirical_law(independent), 2)
        self.assertTrue(cert['j2_midpoint_identity'])
        self.assertGreater(cert['beta'], 0)


if __name__ == '__main__':
    unittest.main()
