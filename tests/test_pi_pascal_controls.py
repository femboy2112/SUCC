from fractions import Fraction as Q
from math import comb, factorial
import unittest

from observational_succ.pi_pascal_controls import (
    monic_moment_polynomials, pascal_endpoint_budget, pascal_weights,
    pascal_window_average, polynomial_inner, positive_moment_countermodel,
    rational_coset_near, valuation_two,
)


def authentic_values(depth):
    values = [Q()]
    for n in range(1, depth + 1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        values.append(16*values[-1]+r)
    return values


def difference(values, start, order):
    return sum(((-1)**(order-j)*comb(order, j)*values[start+j]
                for j in range(order+1)), Q())


class PositiveMomentControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = authentic_values(10)
        cls.reference = tuple(difference(cls.source, 0, n)/factorial(n)
                              for n in range(1, 11))
        cls.model = positive_moment_countermodel(cls.reference, 9)

    def test_exact_first_orthogonal_polynomials(self):
        p = monic_moment_polynomials(3)
        self.assertEqual(p[1], (Q(-1, 3), Q(1)))
        self.assertEqual(p[2], (Q(1, 10), Q(-4, 5), Q(1)))
        self.assertEqual(p[3], (Q(-1, 35), Q(3, 7), Q(-9, 7), Q(1)))
        for i in range(4):
            for j in range(i):
                self.assertEqual(polynomial_inner(p[i], p[j]), 0)

    def test_mass_and_positive_density_certificate(self):
        m = self.model
        self.assertEqual(m.moment(0), 1)
        self.assertLess(m.perturbation_bound, Q(1, 2))
        self.assertGreater(2-m.perturbation_bound, Q(3, 2))
        for x in (Q(), Q(1, 7), Q(1, 2), Q(8, 9), Q(1)):
            actual = sum((a*x**j for j, a in enumerate(m.density)), Q())
            self.assertLess(abs(actual-2), Q(1, 2))

    def test_every_certified_jet_matches_authentic_coset(self):
        m = self.model
        values = [m.unwrapped(n) for n in range(m.depth+1)]
        for n in range(1, m.depth+1):
            actual = difference(values, 0, n)/factorial(n)
            self.assertEqual(actual, m.newton[n-1])
            self.assertEqual(valuation_two(actual), n-1)
            delta = actual-m.reference[n-1]
            self.assertTrue(delta == 0 or valuation_two(delta) >= n-1+m.precision)

    def test_translated_jets_and_normalized_precision(self):
        values = [self.model.unwrapped(n) for n in range(11)]
        for k in range(1, 11):
            nu = 2*k-k.bit_count()-1
            for start in range(11-k):
                got = difference(values, start, k)
                self.assertEqual(valuation_two(got), nu)
                error = got-difference(self.source, start, k)
                self.assertTrue(error == 0 or valuation_two(error) >= nu+9)

    def test_recurrence_zero_and_literal_carry_fifteen(self):
        m = self.model
        self.assertEqual(m.unwrapped(0), 0)
        for n in range(1, 25):
            self.assertEqual(m.unwrapped(n), 16*m.unwrapped(n-1)+m.forcing(n))
            self.assertGreater(m.forcing(n), 0)
            self.assertEqual(m.unwrapped(n).__floor__(), 16**n-1)
            raw = 16*m.phase(n-1)+m.forcing(n)
            self.assertEqual(raw.__floor__(), 15)

    def test_positive_moments_and_complete_monotonicity(self):
        m = self.model
        moments = [m.moment(n) for n in range(25)]
        forcing = [m.forcing(n+1) for n in range(25)]
        for n in (0, 1, 7, 16):
            for k in range(1, 8):
                self.assertGreater((-1)**k*difference(moments, n, k), 0)
                self.assertGreater((-1)**k*difference(forcing, n, k), 0)

    def test_quadratic_real_clustering_while_jets_match(self):
        m = self.model
        n0 = 64
        phases = [m.phase(n) for n in range(n0, n0+24)]
        bound = Q(5, 2*(n0+1)*(n0+2))
        self.assertLess(max(phases)-min(phases), bound)
        self.assertTrue(all(Q(99, 100) < x < 1 for x in phases))
        self.assertNotEqual(m.forcing(1), Q(47, 15))

    def test_fresh_precision_and_depth(self):
        source = authentic_values(7)
        reference = [difference(source, 0, n)/factorial(n) for n in range(1, 8)]
        m = positive_moment_countermodel(reference, 21)
        self.assertLess(m.perturbation_bound, Q(1, 2))
        for n, (got, wanted) in enumerate(zip(m.newton, reference), 1):
            delta = got-wanted
            self.assertTrue(delta == 0 or valuation_two(delta) >= n-1+21)

    def test_bad_reference_and_precision_rejected(self):
        for refs, precision in (([], 1), ([Q(2)], 1), ([Q(1), Q(1)], 1),
                                ([Q(1)], 0), ([Q(1)], True)):
            with self.assertRaises(ValueError):
                positive_moment_countermodel(refs, precision)

    def test_dense_coset_is_not_integer_rounding(self):
        result = rational_coset_near(Q(1, 10**20), Q(1), 17, Q(1, 10**24))
        self.assertLess(abs(result-Q(1, 10**20)), Q(1, 10**24))
        self.assertEqual(valuation_two(result), 0)
        self.assertTrue(result == 1 or valuation_two(result-1) >= 17)
        self.assertGreater(result.denominator, 10**20)

    def test_wrong_density_sign_breaks_prescribed_jet(self):
        m = self.model
        wrong_first = 16-(Q(1, 3)-m.perturbations[0]*Q(1, 36))
        self.assertNotEqual(wrong_first, m.newton[0])


class PascalAveragingControls(unittest.TestCase):
    def test_row_mass_and_mean(self):
        for order in range(21):
            weights = pascal_weights(order)
            self.assertEqual(sum(weights), 1)
            self.assertEqual(sum(j*w for j, w in enumerate(weights)), Q(order, 2))

    def test_constant_observable_survives_every_order(self):
        for order in (0, 1, 4, 17):
            self.assertEqual(pascal_window_average([Q(3, 7)]*(23+order), 23, order), Q(3, 7))

    def test_periodic_law_average_is_unchanged(self):
        orbit = [Q(1), Q(-2), Q(4)]
        for order in (1, 7, 19):
            data = [orbit[j % 3] for j in range(30+order)]
            self.assertEqual(pascal_window_average(data, 30, order), Q(1))

    def test_endpoint_budget_is_sharp(self):
        n, order = 23, 7
        values = [Q(-1)]*order+[Q()]*(n-order)+[Q(1)]*order
        before = sum(values[:n])/n
        after = pascal_window_average(values, n, order)
        self.assertEqual(after-before, pascal_endpoint_budget(n, order, 1))

    def test_malformed_inputs_rejected(self):
        with self.assertRaises(ValueError):
            pascal_window_average([Q(1)], 2, 0)
        with self.assertRaises(ValueError):
            pascal_window_average([0.5], 1, 0)
        for x in (-1, True, Q(2)):
            with self.assertRaises(ValueError):
                pascal_weights(x)
        with self.assertRaises(ValueError):
            pascal_endpoint_budget(4, 2, -1)


if __name__ == "__main__":
    unittest.main()
