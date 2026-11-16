import unittest
from fractions import Fraction as Q

from observational_succ.ym_coupled_wilson import (
    LinkGraph, Polynomial, build_wilson_certificate, constant_polynomial,
    evaluate, factorwise_density, factorwise_error_bound, haar_integral,
    link_quaternion, sphere_monomial_moment, taylor_polynomial,
    wilson_expectation, word_holonomy, word_trace,
)


class CoupledWilsonTests(unittest.TestCase):
    def test_sphere_moments_and_unit_ideal(self):
        self.assertEqual(sphere_monomial_moment((2, 0, 0, 0)), Q(1, 4))
        self.assertEqual(sphere_monomial_moment((4, 0, 0, 0)), Q(1, 8))
        self.assertEqual(sphere_monomial_moment((2, 2, 0, 0)), Q(1, 24))
        self.assertEqual(sphere_monomial_moment((6, 0, 0, 0)), Q(5, 64))
        self.assertEqual(sphere_monomial_moment((1, 2, 0, 0)), 0)
        q = link_quaternion(1, 0)
        sphere_relation = sum((coordinate**2 for coordinate in q), constant_polynomial(1, -1))
        self.assertEqual(haar_integral(sphere_relation**2), 0)
        self.assertEqual(haar_integral(sphere_relation * (q[0]**2 + 3*q[1]**4)), 0)

    def test_quaternion_order_is_visible_to_trace(self):
        ijk = (Q(0), Q(1), Q(0), Q(0), Q(0), Q(0), Q(1), Q(0), Q(0), Q(0), Q(0), Q(1))
        self.assertEqual(evaluate(word_trace(3, (1, 2, 3)), ijk), -1)
        self.assertEqual(evaluate(word_trace(3, (2, 1, 3)), ijk), 1)
        ij = ijk[:8]
        self.assertEqual(evaluate(word_trace(2, (1, 2, -1, -2)), ij), -1)
        self.assertEqual(evaluate(word_trace(2, (1, -1, 2, -2)), ij), 1)

    def test_inverse_and_reversal_preserve_expected_invariants(self):
        hol = word_holonomy(1, (1, -1))
        self.assertEqual(haar_integral((hol[0] - 1)**2), 0)
        self.assertTrue(all(not coordinate.terms for coordinate in hol[1:]))
        self.assertEqual(word_trace(2, (1, 2, 1)), word_trace(2, (-1, -2, -1)))

    def test_shared_link_moments_refute_independent_loop_mutant(self):
        x, y = link_quaternion(2, 0)[0], link_quaternion(2, 1)[0]
        z, t = word_trace(2, (1, 2)), word_trace(2, (1, -2))
        self.assertEqual(haar_integral(x*y*z), Q(1, 16))
        self.assertEqual(haar_integral(z*t), Q(-1, 8))
        self.assertEqual(haar_integral(z*z*t*t), Q(1, 12))
        self.assertEqual(haar_integral(z) * haar_integral(t), 0)

    def test_closed_source_graph_is_required(self):
        graph = LinkGraph(3, ((0, 1), (1, 2), (2, 0)))
        self.assertEqual(graph.closed_word((1, 2, 3)), (1, 2, 3))
        self.assertEqual(graph.closed_word((-3, -2, -1)), (-3, -2, -1))
        for word in ((1, 2), (1, 3, 2), (0,), (4,)):
            with self.assertRaises(ValueError):
                graph.closed_word(word)

    def test_two_interacting_loops_have_nonfactorizing_partition(self):
        graph = LinkGraph(1, ((0, 0), (0, 0)))
        beta, gamma = Q(1, 2), Q(1, 3)
        density = factorwise_density(graph, ((1, 2), (1, -2)), (beta, gamma), (2, 2))
        expected = 1 + (beta**2 + gamma**2 - beta*gamma)/8 + beta**2*gamma**2/48
        self.assertEqual(haar_integral(density), expected)
        self.assertNotEqual(expected, (1 + beta**2/8)*(1 + gamma**2/8))

    def test_source_density_couples_individual_link_observables(self):
        graph = LinkGraph(1, ((0, 0), (0, 0)))
        x, y = link_quaternion(2, 0)[0], link_quaternion(2, 1)[0]
        self.assertEqual(wilson_expectation(graph, ((1, 2),), (Q(1, 2),), (2,), x*y), Q(1, 33))
        self.assertEqual(wilson_expectation(graph, ((1, 2),), (Q(1, 2),), (2,), x), 0)
        self.assertEqual(wilson_expectation(graph, ((1, 2),), (Q(1, 2),), (2,), y), 0)

    def test_factorwise_even_weights_positive_at_hostile_endpoints(self):
        x = link_quaternion(1, 0)[0]
        for degree in (0, 2, 4, 6):
            polynomial = taylor_polynomial(3*x, degree)
            for value in (Q(-1), Q(-1, 2), Q(0), Q(1)):
                self.assertGreater(evaluate(polynomial, (value, 0, 0, 0)), 0)
        self.assertLess(evaluate(taylor_polynomial(3*x, 1), (-1, 0, 0, 0)), 0)

    def test_zero_coupling_certificate_recovers_haar(self):
        graph = LinkGraph(1, ((0, 0),))
        x = link_quaternion(1, 0)[0]
        certificate = build_wilson_certificate(graph, ((1,),), (0,), x**2, Q(1, 1000))
        self.assertEqual(certificate.expectation, Q(1, 4))
        self.assertEqual(certificate.error_bound, 0)
        self.assertEqual(certificate.degrees, (0,))

    def test_nonzero_certificate_pays_requested_error(self):
        graph = LinkGraph(1, ((0, 0), (0, 0)))
        observable = word_trace(2, (1, 2))
        certificate = build_wilson_certificate(graph, ((1, 2),), (Q(1, 8),), observable, Q(1, 100))
        self.assertGreater(certificate.partition, 0)
        self.assertLessEqual(certificate.error_bound, certificate.tolerance)
        self.assertTrue(all(degree % 2 == 0 for degree in certificate.degrees))
        # Multiplication pushes product Haar to Haar: the shared-link loop
        # has the same single-loop law, without changing other observables.
        single = LinkGraph(1, ((0, 0),))
        x = link_quaternion(1, 0)[0]
        self.assertEqual(certificate.expectation,
                         wilson_expectation(single, ((1,),), certificate.betas, certificate.degrees, x))

    def test_rational_error_budget_and_validation(self):
        self.assertEqual(factorwise_error_bound((Q(1, 2),), (2,), 1), Q(1, 8))
        graph = LinkGraph(1, ((0, 0),))
        x = link_quaternion(1, 0)[0]
        for bad in (0.5, True):
            with self.assertRaises(TypeError):
                factorwise_density(graph, ((1,),), (bad,), (2,))
        for betas, degrees in (((-1,), (2,)), ((1,), (1,)), ((1,), ())):
            with self.assertRaises(ValueError):
                factorwise_density(graph, ((1,),), betas, degrees)
        with self.assertRaises(ValueError):
            build_wilson_certificate(graph, ((1,),), (1,), x, 0)
        with self.assertRaises(ValueError):
            haar_integral(Polynomial(1, {(0,): 1}))

    def test_global_taylor_square_can_destroy_reflection_positivity(self):
        x, y = link_quaternion(2, 0)[0], link_quaternion(2, 1)[0]
        density = taylor_polynomial(x+y, 2)**2
        f, reflected_f = -4+5*x+5*x*x, -4+5*y+5*y*y
        partition = haar_integral(density)
        numerator = haar_integral(f*reflected_f*density)
        self.assertEqual(partition, Q(69, 32))
        self.assertEqual(numerator, Q(-71, 512))
        self.assertEqual(numerator/partition, Q(-71, 1104))


if __name__ == "__main__":
    unittest.main()
