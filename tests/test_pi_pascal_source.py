"""Exact source identities, fresh Pascal holdouts and rejected shortcuts."""
from fractions import Fraction as Q
from math import comb, factorial
import unittest

from observational_succ import pi_pascal_source as pascal
from observational_succ.bbp_two_adic import forcing_mod, particular_mod, rational_mod


def four_poles(t):
    t = Q(t)
    return (4/(8*t-7)-2/(8*t-4)-1/(8*t-3)-1/(8*t-2))


def signed_row_difference(function, start, order):
    return sum(((-1)**(order-j)*comb(order, j)*function(start+j)
                for j in range(order+1)), Q(0))


def direct_source(last):
    result = [Q(0)]
    for n in range(1, last+1):
        result.append(16*result[-1]+four_poles(n))
    return result


class PascalSourceIdentityTests(unittest.TestCase):
    def test_reciprocal_product_formula(self):
        for start in (-17, 0, 1, Q(1, 3), Q(-7, 5)):
            for order in (0, 1, 2, 7, 16):
                for slope, offset, _ in pascal.POLES:
                    direct = signed_row_difference(
                        lambda x: 1/(slope*Q(x)+offset), start, order)
                    self.assertEqual(pascal.reciprocal_difference(
                        start, order, slope, offset), direct)

    def test_fixed_calibration_integer_grid(self):
        for start in range(17):
            for order in range(1, 17):
                exact = pascal.forcing_difference(start, order)
                self.assertEqual(exact, signed_row_difference(four_poles, start, order))
                self.assertEqual(pascal.rational_valuation(exact),
                                 pascal.difference_valuation(order))

    def test_preregistered_fresh_orders_and_starts(self):
        for start in (19, 31, 64, 127):
            for order in range(17, 41):
                exact = pascal.forcing_difference(start, order)
                self.assertEqual(exact, signed_row_difference(four_poles, start, order))
                self.assertEqual(pascal.rational_valuation(exact),
                                 order-1+pascal.rational_valuation(factorial(order)))

    def test_two_integral_rational_starts(self):
        for start in (Q(1, 3), Q(-7, 5), Q(1009, 17)):
            for order in (1, 2, 7, 16, 31):
                value = pascal.forcing_difference(start, order)
                self.assertEqual(value, signed_row_difference(four_poles, start, order))
                self.assertEqual(pascal.rational_valuation(value),
                                 pascal.difference_valuation(order))

    def test_authentic_source_differences_fresh_grid(self):
        values = direct_source(167)
        for start in (19, 31, 64, 127):
            for order in range(17, 41):
                value = signed_row_difference(lambda n: values[n], start, order)
                self.assertEqual(pascal.rational_valuation(value),
                                 pascal.difference_valuation(order))
                bits = pascal.difference_valuation(order)+7
                self.assertEqual(pascal.source_difference_mod(start, order, bits),
                                 rational_mod(value, bits))

    def test_exact_first_correction_valuation(self):
        values = direct_source(61)
        for start in (0, 1, 19, 31):
            for order in (1, 2, 7, 16, 30):
                source = signed_row_difference(lambda n: values[n], start, order)
                defect = source-pascal.forcing_difference(start, order)
                self.assertEqual(pascal.rational_valuation(defect),
                                 pascal.difference_valuation(order)+4)

    def test_mahler_values_against_direct_source(self):
        values = direct_source(40)
        source = pascal.mahler_coefficients("source", 40)
        forcing = pascal.mahler_coefficients("forcing", 40)
        self.assertEqual(source[0], 0)
        self.assertEqual(forcing[0], Q(16, 21))
        for k in range(41):
            self.assertEqual(source[k], signed_row_difference(lambda n: values[n], 0, k))
            self.assertEqual(forcing[k], signed_row_difference(four_poles, 0, k))
        self.assertEqual(forcing[1], Q(83, 35))

    def test_binomial_reconstruction_at_nonnegative_integer_inputs(self):
        source = direct_source(31)
        for kind in ("forcing", "source"):
            coefficients = pascal.mahler_coefficients(kind, 31)
            for n in range(32):
                value = sum((coefficients[k]*comb(n, k) for k in range(n+1)), Q(0))
                self.assertEqual(value, four_poles(n) if kind == "forcing" else source[n])

    def test_profile_is_not_full_source_authentication(self):
        # Changing the higher-valuation slope-8 pole changes values while
        # retaining the complete unique-minimum valuation mechanism.
        for start in (0, 19):
            for order in (1, 2, 7, 17, 40):
                correct = pascal.forcing_difference(start, order)
                mutant = correct+pascal.reciprocal_difference(start, order, 8, -3)
                self.assertNotEqual(mutant, correct)
                self.assertEqual(pascal.rational_valuation(mutant),
                                 pascal.difference_valuation(order))

    def test_removing_dominant_pole_breaks_profile(self):
        for order in (1, 2, 7, 17, 40):
            mutant = pascal.forcing_difference(19, order) + Q(1, 2)*(
                pascal.reciprocal_difference(19, order, 2, -1))
            self.assertEqual(pascal.rational_valuation(mutant),
                             2*order-1+pascal.rational_valuation(factorial(order)))
            self.assertNotEqual(pascal.rational_valuation(mutant),
                                pascal.difference_valuation(order))


class PascalFinitePrecisionTests(unittest.TestCase):
    def test_exact_minimal_degree_bounds(self):
        for bits in range(1, 258):
            degree = pascal.minimal_mahler_degree(bits)
            self.assertLess(pascal.difference_valuation(degree), bits)
            self.assertGreaterEqual(pascal.difference_valuation(degree+1), bits)
            self.assertGreaterEqual(degree, (bits+1)//2)
            self.assertLessEqual(degree, (bits+bits.bit_length())//2)

    def test_minimal_polynomial_matches_independent_modular_evaluator(self):
        for bits in (1, 2, 3, 4, 7, 16, 31, 64, 129):
            for index in (-91, -1, 0, 1, 19, 127, (1 << 120)+577):
                self.assertEqual(pascal.newton_mod(index, bits, "forcing"),
                                 forcing_mod(index, bits))
                self.assertEqual(pascal.newton_mod(index, bits, "source"),
                                 particular_mod(index, bits))

    def test_omitting_last_degree_fails_at_its_own_integer_index(self):
        for bits in (1, 3, 7, 16, 31, 65):
            degree = pascal.minimal_mahler_degree(bits)
            for kind in ("forcing", "source"):
                c = pascal.mahler_coefficients(kind, degree)
                omitted = sum((c[k]*comb(degree, k) for k in range(degree)), Q(0))
                actual = (forcing_mod(degree, bits) if kind == "forcing"
                          else particular_mod(degree, bits))
                self.assertNotEqual(rational_mod(omitted, bits), actual)
                self.assertEqual((actual-rational_mod(omitted, bits)) % (1 << bits),
                                 rational_mod(c[-1], bits))

    def test_degree_obstruction_uses_function_difference(self):
        for degree in (1, 2, 7, 16):
            polynomial = lambda t: sum(Q((-1)**j, j+1)*t**j for j in range(degree))
            self.assertEqual(signed_row_difference(polynomial, 0, degree), 0)
            self.assertNotEqual(signed_row_difference(four_poles, 0, degree), 0)

    def test_sharp_uniform_error_integer_witness(self):
        source = direct_source(28)
        for degree in (0, 1, 2, 7, 16):
            expected = pascal.difference_valuation(degree+1)
            for kind in ("forcing", "source"):
                coefficients = pascal.mahler_coefficients(kind, degree)
                for n in range(degree+12):
                    polynomial = sum((coefficients[k]*comb(n, k)
                                      for k in range(min(degree, n)+1)), Q(0))
                    value = four_poles(n) if kind == "forcing" else source[n]
                    valuation = pascal.rational_valuation(value-polynomial)
                    if valuation is not None:
                        self.assertGreaterEqual(valuation, expected)
                    if n == degree+1:
                        self.assertEqual(valuation, expected)

    def test_pascal_row_and_binary_carry_steps(self):
        for order in range(1, 129):
            row = [comb(order, j) for j in range(order+1)]
            self.assertEqual(sum(row), 1 << order)
            self.assertEqual(sum(x % 2 for x in row), 1 << order.bit_count())
            self.assertEqual(pascal.difference_valuation(order+1)
                             - pascal.difference_valuation(order),
                             1+pascal.rational_valuation(order+1))

    def test_real_magnitude_of_exact_dyadic_polynomial_is_tiny(self):
        values = direct_source(128)
        for n, bits in ((16, 8), (31, 16), (64, 16), (128, 16)):
            degree = pascal.minimal_mahler_degree(bits)
            coefficients = pascal.mahler_coefficients("source", degree)
            polynomial = sum((coefficients[k]*comb(n, k)
                              for k in range(degree+1)), Q(0))
            ratio = abs(polynomial)/values[n]
            bound = Q(16, 15)*(degree+1)*(17*n)**degree/16**n
            self.assertLessEqual(ratio, bound)
            self.assertEqual(rational_mod(polynomial, bits),
                             rational_mod(values[n], bits))
            if n == 128:
                self.assertEqual(degree, 9)
                self.assertLess(bound, Q(1, 2**400))


class PascalOddPrimeTests(unittest.TestCase):
    def test_exact_odd_prime_pole_counts(self):
        for start in (-7, 0, 1, 19):
            for order in (0, 1, 7, 17, 40):
                for slope, offset, coefficient in pascal.POLES:
                    term = coefficient*pascal.reciprocal_difference(start, order, slope, offset)
                    for prime in (3, 5, 7, 11, 13, 17):
                        rows = pascal.odd_pole_counts(start, order, slope, offset, prime)
                        self.assertTrue(all(count-factorial_count in (0, 1)
                                            for _, count, factorial_count in rows))
                        self.assertEqual(pascal.odd_pole_valuation(
                            start, order, slope, offset, prime),
                            pascal.rational_valuation(term, prime))

    def test_odd_prime_minimum_term_shortcut_is_false(self):
        terms = [coefficient*pascal.reciprocal_difference(0, 1, slope, offset)
                 for slope, offset, coefficient in pascal.POLES]
        self.assertEqual([pascal.rational_valuation(t, 3) for t in terms],
                         [0, -1, 0, -1])
        self.assertEqual(sum(terms), Q(83, 35))
        self.assertEqual(pascal.rational_valuation(sum(terms), 3), 0)
        self.assertNotEqual(min(pascal.rational_valuation(t, 3) for t in terms),
                            pascal.rational_valuation(sum(terms), 3))

    def test_lucas_operator_control_at_odd_primes(self):
        for prime in (3, 5, 7, 11, 13):
            for order in (17, 31, 40, 64):
                for place in range(order+1):
                    n, k, product = order, place, 1
                    while n or k:
                        a, b = n % prime, k % prime
                        product *= comb(a, b) if b <= a else 0
                        n //= prime
                        k //= prime
                    self.assertEqual(comb(order, place) % prime, product % prime)

    def test_domain_guards(self):
        for invalid in (0, -1, True, Q(1, 2)):
            with self.assertRaises(ValueError):
                pascal.difference_valuation(invalid)
        with self.assertRaises(ValueError):
            pascal.forcing_difference(Q(1, 2), 1)
        with self.assertRaises(ValueError):
            pascal.reciprocal_difference(0, 1, 2, 0)
        with self.assertRaises(ValueError):
            pascal.newton_mod(1, 3, "counterfeit")
        with self.assertRaises(ValueError):
            pascal.rational_valuation(3, 9)
        with self.assertRaises(ValueError):
            pascal.odd_pole_counts(1, 2, 3, 1, 5)
        with self.assertRaises(ValueError):
            pascal.odd_pole_counts(1, 2, 2, 1, 2)
        self.assertIsNone(pascal.rational_valuation(0))


if __name__ == "__main__":
    unittest.main()
