"""Exact adversarial checks of the proved reflection-order statements."""

from fractions import Fraction as F
from itertools import product
import unittest

from observational_succ.ym_reflection_bridge import (
    haar_moment, is_psd_exact, polynomial_product,
)
from observational_succ.ym_reflection_order import (
    even_taylor_character_coefficients, factorwise_expectation_error,
    global_square_witness, reflected_sum_pair, su2_character,
)


class ReflectionOrderTests(unittest.TestCase):
    def test_global_square_exact_negative_certificate(self):
        receipt = global_square_witness()
        self.assertEqual(receipt["partition"], F(645, 512))
        self.assertEqual(receipt["gram"], ((F(1), F(1, 1290)), (F(1, 1290), F(0))))
        self.assertEqual(receipt["witness"], (F(-1289), F(0), F(15480), F(0), F(-20640)))
        self.assertEqual(receipt["reflected_square"], -1)
        self.assertFalse(is_psd_exact(receipt["gram"]))

    def test_top_character_orthogonality_and_moving_witness(self):
        # Fresh degrees test the mechanism; the all-degree result has a proof.
        for d in (1, 2, 3, 4, 7, 10):
            character = su2_character(d)
            for j in range(d):
                self.assertEqual(sum((c * haar_moment(i + j) for i, c in enumerate(character)), F(0)), 0)
            self.assertEqual(sum((c * haar_moment(i + d) for i, c in enumerate(character)), F(0)), F(1, 2**d))
            density = (F(1),) + (F(0),) * (d - 1) + (F(1, 3),)
            self.assertEqual(reflected_sum_pair(density, character, character), 0)
            self.assertEqual(reflected_sum_pair(density, (1,), character), F(1, 3 * 2**d))

    def test_character_expansion_by_direct_polynomial_reconstruction(self):
        from math import factorial
        for beta, degree in product((F(0), F(1, 3), F(1), F(5, 2)), (0, 2, 4, 8)):
            coefficients = even_taylor_character_coefficients(beta, degree)
            self.assertTrue(all(c >= 0 for c in coefficients))
            reconstructed = [F(0)] * (degree + 1)
            for d, coefficient in enumerate(coefficients):
                for j, value in enumerate(su2_character(d)):
                    reconstructed[j] += coefficient * value
            self.assertEqual(tuple(reconstructed), tuple(beta**j / factorial(j) for j in range(degree + 1)))

    def test_factorwise_half_source_has_rank_one_reflected_form(self):
        # Two reflected disjoint plaquettes; factorwise P2(x)P2(y).
        weight = (F(1), F(1), F(1, 2))
        tests = ((F(1),), su2_character(1), su2_character(4))
        z_half = sum((c * haar_moment(j) for j, c in enumerate(weight)), F(0))
        means = []
        for test in tests:
            polynomial = polynomial_product(test, weight)
            means.append(sum((c * haar_moment(j) for j, c in enumerate(polynomial)), F(0)) / z_half)
        gram = tuple(tuple(a * b for b in means) for a in means)
        self.assertTrue(is_psd_exact(gram))
        self.assertEqual(means, [F(1), F(4, 9), F(0)])

    def test_reflection_equivariance_and_cp_do_not_replace_localization(self):
        # A deterministic pullback is a unital *-homomorphism, hence CP.
        # It commutes with swap but its positive coordinate reads both halves.
        coarse = {(a, b): (a * (1-b), b * (1-a)) for a, b in product((0, 1), repeat=2)}
        for (a, b), (c, d) in coarse.items():
            self.assertEqual(coarse[(b, a)], (d, c))
        f = (F(1), F(-2))
        reflected = sum((f[c] * f[d] / 4 for c, d in coarse.values()), F(0))
        self.assertEqual(reflected, F(-1, 2))
        # Before coarse graining the same fine positive-half form is a square.
        fine = sum((f[a] * f[b] / 4 for a, b in product((0, 1), repeat=2)), F(0))
        self.assertEqual(fine, F(1, 4))

    def test_gauge_invariant_positive_density_can_fail_reflection(self):
        # Two Z2 triangles, six edges; loop observables are gauge invariant.
        states = tuple(product((-1, 1), repeat=6))
        a = F(1, 2)
        def loops(u):
            return u[0]*u[1]*u[2], u[3]*u[4]*u[5]
        mass = F(0)
        correlation = F(0)
        for u in states:
            plus, minus = loops(u)
            weight = (1-a*plus*minus)/64
            self.assertGreater(weight, 0)
            mass += weight
            correlation += weight*plus*minus
            # A vertex flip changes its two incident edges and no loop.
            for first, second in ((0,1),(1,2),(2,0),(3,4),(4,5),(5,3)):
                changed = list(u)
                changed[first] *= -1
                changed[second] *= -1
                self.assertEqual(loops(changed), (plus, minus))
        self.assertEqual(mass, 1)
        self.assertEqual(correlation, -a)
        self.assertTrue(is_psd_exact(((1,0,0),(0,1,-a),(0,-a,1))))

    def test_error_budget_exact_arithmetic_and_input_scope(self):
        from observational_succ.ym_coupled_wilson import factorwise_error_bound
        self.assertEqual(factorwise_expectation_error((0,), (2,)), 0)
        # Predeclared small exact case, not fitted to an observed residual.
        self.assertEqual(factorwise_expectation_error((F(1,2),), (2,)), F(1,8))
        self.assertLess(factorwise_expectation_error((1,1), (20,20)), F(1,10**14))
        for betas, degrees, bound in (((F(1,2),F(2,3)),(2,4),F(7,5)), ((0,3),(0,12),2), ((),(),0)):
            self.assertEqual(factorwise_expectation_error(betas, degrees, bound),
                             factorwise_error_bound(betas, degrees, bound))
        for beta, degree in ((-1,2), (1,1), (1,-2)):
            with self.assertRaises(ValueError):
                even_taylor_character_coefficients(beta, degree)
        with self.assertRaises(TypeError):
            even_taylor_character_coefficients(0.5, 2)
        with self.assertRaises(TypeError):
            even_taylor_character_coefficients(True, 2)
        with self.assertRaises(ValueError):
            even_taylor_character_coefficients(1, True)

    def test_shared_link_reflected_source_matches_character_prediction(self):
        from observational_succ.ym_coupled_wilson import (
            LinkGraph, constant_polynomial, factorwise_density,
            haar_integral, word_trace,
        )
        # Prediction declared from the character calculation before integration:
        # Z=c0²; T eigenvalues on 1,Re(u),Re(v) give 1,1/18,1/81.
        # Reflection swaps edges 1<->3, 2<->4; loops share edges 1 and 3.
        graph = LinkGraph(3, ((0,1),(1,2),(0,1),(1,2)))
        density = factorwise_density(graph, ((-1,3),(-2,-1,3,4)), (1,1), (2,2))
        partition = haar_integral(density)
        minus = (constant_polynomial(4,1), word_trace(4,(1,)), word_trace(4,(2,)))
        plus = (constant_polynomial(4,1), word_trace(4,(3,)), word_trace(4,(4,)))
        gram = tuple(tuple(haar_integral(density*a*b)/partition for b in plus) for a in minus)
        self.assertEqual(partition, F(81,64))
        self.assertEqual(gram, ((F(1),F(0),F(0)),(F(0),F(1,18),F(0)),(F(0),F(0),F(1,81))))
        self.assertTrue(is_psd_exact(gram))


if __name__ == "__main__":
    unittest.main()
