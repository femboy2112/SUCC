"""Independent exact checks and failure controls for authentic Pascal kernels."""
import unittest
from fractions import Fraction as Q
from math import comb

from observational_succ.bbp_source_memory import tail_interval
from observational_succ.pi_pascal_kernel import (
    absolute_shadow_endpoint_obstructions,
    beta_with_integer_second,
    coherent_filter_degree,
    filter_carry_modulus,
    filtered_phase_from_carry,
    forcing_pascal_beta_bounds,
    forcing_pascal_moment,
    pascal_pi_interval,
    rational_filter_coefficients,
    scaled_pascal_error_interval,
    scaled_pascal_forcing,
    scaled_pascal_source,
    signed_pascal_source,
    source_pascal_row,
    tail_pascal_interval,
)


def literal_forcing(n):
    return Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)


def literal_states(count):
    values = [Q()]
    for n in range(1, count+1):
        values.append(16*values[-1]+literal_forcing(n))
    return values


def literal_difference(values):
    row = list(values)
    while len(row) > 1:
        row = [b-a for a, b in zip(row, row[1:])]
    return row[0]


def convolve(left, right):
    out = [Q()] * (len(left)+len(right)-1)
    for j, a in enumerate(left):
        for k, b in enumerate(right):
            out[j+k] += a*b
    return tuple(out)


def machin_interval(terms=26):
    def atan(q):
        value = sum((Q((-1)**j, (2*j+1)*q**(2*j+1))
                     for j in range(terms)), Q())
        remainder = Q(1, (2*terms+1)*q**(2*terms+1))
        return ((value, value+remainder) if terms % 2 == 0
                else (value-remainder, value))
    a, b = atan(5)
    c, d = atan(239)
    return 16*a-4*d, 16*b-4*c


class PascalRealKernelTests(unittest.TestCase):
    def test_beta_product_against_literal_polynomial_integral(self):
        for a in (Q(1, 8), Q(1, 2), Q(5, 8), Q(7, 3), Q(32)):
            for k in range(12):
                direct = sum((Q((-1)**j*comb(k, j))/(a+j)
                              for j in range(k+1)), Q())
                self.assertEqual(beta_with_integer_second(a, k), direct)

    def test_authentic_moments_calibration(self):
        for n in range(17):
            for k in range(17):
                values = [literal_forcing(n+j+1) for j in range(k+1)]
                self.assertEqual(forcing_pascal_moment(n, k),
                                 (-1)**k*literal_difference(values))

    def test_fresh_orders_and_starting_indices(self):
        for n in (19, 31, 64, 127):
            for k in range(17, 41):
                values = [literal_forcing(n+j+1) for j in range(k+1)]
                moment = forcing_pascal_moment(n, k)
                self.assertEqual(moment, (-1)**k*literal_difference(values))
                low, high = forcing_pascal_beta_bounds(n, k)
                self.assertLess(low, moment)
                self.assertLess(moment, high)

    def test_beta_bounds_and_all_parameter_positivity(self):
        for n in (0, 1, 4, 16):
            for k in (0, 1, 2, 7, 16, 40):
                low, high = forcing_pascal_beta_bounds(n, k)
                value = forcing_pascal_moment(n, k)
                self.assertTrue(0 < low < value < high)

    def test_positive_geometric_tail_intervals_refine(self):
        for n in (0, 1, 7, 31):
            for k in (0, 1, 5, 17, 40):
                a, b = tail_pascal_interval(n, k, 3)
                c, d = tail_pascal_interval(n, k, 4)
                moment = forcing_pascal_moment(n, k)
                self.assertTrue(moment/16 < a < c < d < b < moment/15)

    def test_tail_interval_against_independent_signed_tail_enclosures(self):
        for n in (0, 1, 4):
            for k in range(8):
                low = high = Q()
                for j in range(k+1):
                    coefficient = (-1)**j * comb(k, j)
                    a, b = tail_interval(n+j, 14)
                    low += coefficient * (a if coefficient >= 0 else b)
                    high += coefficient * (b if coefficient >= 0 else a)
                a, b = tail_pascal_interval(n, k, 7)
                self.assertLess(max(a, low), min(b, high))

    def test_pascal_source_against_literal_difference_triangle(self):
        values = literal_states(40)
        for k in range(41):
            self.assertEqual(signed_pascal_source(k),
                             literal_difference(values[:k+1]))
            self.assertEqual(source_pascal_row(0, k), signed_pascal_source(k))
        for n, k in ((1, 4), (7, 9), (19, 17)):
            self.assertEqual(source_pascal_row(n, k),
                             literal_difference(values[n:n+k+1]))
            self.assertEqual(source_pascal_row(n, k, 1),
                             sum((comb(k, j)*values[n+j]
                                  for j in range(k+1)), Q()))

    def test_pi_intervals_against_independent_machin_formula_and_sign_mutant(self):
        ml, mh = machin_interval()
        for k in range(1, 13):
            low, high = pascal_pi_interval(k, 6)
            self.assertLess(max(ml, low), min(mh, high))
        k = 5
        a = signed_pascal_source(k)
        lower, upper = tail_pascal_interval(0, k, 6)
        # Treating the odd-order correction as positive is decisively false.
        mutated_low = Q(16, 15**k)*(a+lower)
        self.assertGreater(mutated_low, mh)
        self.assertGreater(upper, lower)

    def test_scaled_sources_and_exact_block_forcing(self):
        for q, degree in ((2, 1), (3, 1), (5, 1), (13, 1),
                          (17, 2), (16, 4), (3, 2)):
            for k in range(7):
                value = scaled_pascal_source(q, degree, k)
                self.assertEqual(value, Q(q, 15**degree)**k
                                 * source_pascal_row(0, degree*k))
                force = scaled_pascal_forcing(q, degree, k)
                self.assertEqual(scaled_pascal_source(q, degree, k+1),
                                 q*value+force)
                self.assertGreater((-1)**(degree*k)*force, 0)

    def test_scaled_error_enclosure_against_independent_pi_interval(self):
        pl, ph = machin_interval(40)
        for q, degree in ((3, 1), (5, 1), (13, 1), (15, 1), (17, 2)):
            for k in range(1, 8):
                source = scaled_pascal_source(q, degree, k)
                a, b = scaled_pascal_error_interval(q, degree, k, 6)
                signed_low = q**k*pl/16-source
                signed_high = q**k*ph/16-source
                if degree*k % 2:
                    signed_low, signed_high = -signed_high, -signed_low
                self.assertLess(max(a, signed_low), min(b, signed_high))

    def test_all_prime_filter_composition_and_power_coherence(self):
        for q, r in ((2, 2), (2, 3), (3, 5), (7, 13), (17, 19)):
            d, e = coherent_filter_degree(q), coherent_filter_degree(r)
            self.assertEqual(coherent_filter_degree(q*r), d+e)
            self.assertEqual(convolve(rational_filter_coefficients(q, d),
                                      rational_filter_coefficients(r, e)),
                             rational_filter_coefficients(q*r, d+e))
            self.assertLessEqual(q, 15**d)
        self.assertEqual([coherent_filter_degree(q) for q in (2, 4, 16)],
                         [1, 2, 4])
        for q, d, m, k in ((2, 1, 2, 4), (2, 1, 4, 3), (3, 1, 3, 2),
                            (17, 2, 2, 3)):
            self.assertEqual(scaled_pascal_source(q**m, m*d, k),
                             scaled_pascal_source(q, d, m*k))

    def test_exact_carry_readout_and_missing_coordinate_mutant(self):
        for q, degree in ((2, 1), (3, 1), (5, 1), (13, 1), (17, 2)):
            for k in range(1, 7):
                source = signed_pascal_source(degree*k)
                carry = source.numerator // source.denominator
                modulus = filter_carry_modulus(q, degree, k)
                readout = filtered_phase_from_carry(source % 1, carry % modulus,
                                                     q, degree, k)
                self.assertEqual(readout, scaled_pascal_source(q, degree, k) % 1)
        self.assertEqual(filter_carry_modulus(3, 1, 7), 5**7)
        self.assertEqual(filter_carry_modulus(5, 1, 7), 3**7)
        # Same input circle phase, two possible integral lifts, two outputs.
        self.assertNotEqual(filtered_phase_from_carry(Q(1, 7), 0, 3, 1, 1),
                            filtered_phase_from_carry(Q(1, 7), 1, 3, 1, 1))
        source = signed_pascal_source(1)
        self.assertNotEqual(filtered_phase_from_carry(source % 1, 0, 3, 1, 1),
                            scaled_pascal_source(3, 1, 1) % 1)

    def test_integer_filter_obstructions_and_scope(self):
        for q in (2, 3, 5, 7, 11, 13):
            self.assertIn("zero", absolute_shadow_endpoint_obstructions(q))
        self.assertEqual(absolute_shadow_endpoint_obstructions(17), ("one",))
        for q in (15, 16, 225, 240, 256):
            self.assertEqual(absolute_shadow_endpoint_obstructions(q), ())
        self.assertEqual(rational_filter_coefficients(3, 1), (Q(-1, 5), Q(1, 5)))

    def test_positive_moment_counterfeit_retains_filters_without_uniform_law(self):
        for q, d in ((2, 1), (3, 1), (5, 1), (13, 1), (17, 2)):
            coefficients = (Q(1),)
            for k in range(1, 8):
                coefficients = convolve(coefficients, rational_filter_coefficients(q, d))
                fake_states = [Q(16**n, 2)-Q(1, (n+1)*(n+2))
                               for n in range(d*k+1)]
                value = sum((a*u for a, u in zip(coefficients, fake_states)), Q())
                error = Q(q, 15**d)**k / (d*k+2)
                self.assertEqual(value, Q(q**k, 2)-(-1)**(d*k)*error)
                atom = Q(1, 2) if q % 2 else Q()
                distance = (value-atom) % 1
                self.assertEqual(min(distance, 1-distance), error)

    def test_exact_domain_validation(self):
        bad_calls = [
            lambda: beta_with_integer_second(0.5, 2),
            lambda: beta_with_integer_second(Q(), 2),
            lambda: forcing_pascal_moment(True, 1),
            lambda: forcing_pascal_moment(0, -1),
            lambda: tail_pascal_interval(0, 1, 0),
            lambda: signed_pascal_source(-1),
            lambda: source_pascal_row(0, 1, 0),
            lambda: scaled_pascal_source(1, 1, 2),
            lambda: scaled_pascal_source(3, 0, 2),
            lambda: coherent_filter_degree(True),
            lambda: filtered_phase_from_carry(0.5, 0, 3, 1, 2),
            lambda: filtered_phase_from_carry(Q(1), 0, 3, 1, 2),
            lambda: filtered_phase_from_carry(Q(), 25, 3, 1, 2),
        ]
        for call in bad_calls:
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
