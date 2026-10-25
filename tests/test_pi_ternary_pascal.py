"""Independent exact calibrations and hostile controls for ternary filters."""
from fractions import Fraction as Q
from math import comb
import unittest

from observational_succ.bbp_two_adic import rational_mod
from observational_succ.pi_pascal_source import (
    difference_valuation, rational_valuation,
)
from observational_succ.pi_ternary_pascal import (
    FILTERS, alternating_mass, alternating_words, ambiguous_cylinders,
    base81_reset_source, base81_reset_forcing, base81_reset_mahler,
    bernoulli_cdf, bernoulli_multiplied_half, dyadic_filtered_mod,
    dyadic_mahler, endpoint_denominator_possible, filter_error_interval,
    filter_power, filtered_source, local_transport, phase_from_cover,
    source_states, ternary4_lift,
)


def original_source(last):
    values = [Q()]
    for n in range(1, last+1):
        r = Q(4, 8*n-7)-Q(2, 8*n-4)-Q(1, 8*n-3)-Q(1, 8*n-2)
        values.append(16*values[-1]+r)
    return values


def difference(values, start, order):
    return sum((comb(order, i)*(-1)**(order-i)*values[start+i]
                for i in range(order+1)), Q())


def atan_interval(d, terms):
    s = sum((Q((-1)**j, (2*j+1)*d**(2*j+1))
             for j in range(terms)), Q())
    e = Q(1, (2*terms+1)*d**(2*terms+1))
    return (s, s+e) if terms % 2 == 0 else (s-e, s)


def alpha_interval(terms=240):
    a, b = atan_interval(5, terms), atan_interval(239, terms)
    return a[0]-b[1]/4, a[1]-b[0]/4


class TernaryFilterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.values = original_source(220)
        cls.alpha = alpha_interval()

    def test_classical_weighted_rows(self):
        for n in range(80):
            self.assertEqual(sum(comb(n, j)*2**j for j in range(n+1)), 3**n)

    def test_original_source_is_retained(self):
        self.assertEqual(tuple(self.values[:145]), source_states(144))

    def test_filter_spectral_values(self):
        for name, (_, _, q) in FILTERS.items():
            for k in range(20):
                a, b = filter_power(name, k)
                self.assertEqual(sum(c*16**j for j, c in enumerate(a)), b*q**k)

    def test_ternary4_literal_weighted_pascal(self):
        for k in range(73):
            value = sum((comb(k, j)*(-1)**(k-j)*self.values[j]/4**j
                         for j in range(k+1)), Q())
            self.assertEqual(value, filtered_source("ternary4", k))

    def test_base81_newton_expansion(self):
        for k in range(41):
            value = sum((Q(comb(k, j), 3**j)*difference(self.values, j, j)
                         for j in range(k+1)), Q())
            self.assertEqual(value, filtered_source("base81", k))

    def assert_moment_certificate(self, name, k, start):
        value = filtered_source(name, k, start)
        q = FILTERS[name][2]
        sign = (-1)**k if name in ("ternary4", "ternary5") else 1
        independent = sorted(sign*(q**k*16**start*a-value) for a in self.alpha)
        lower, upper = filter_error_interval(name, k, start, terms=4)
        self.assertLess(0, lower)
        self.assertLess(lower, independent[0])
        self.assertLess(independent[1], upper)

    def test_positive_kernel_calibration(self):
        for name in FILTERS:
            for k in range(15):
                for start in (0, 3, 8):
                    self.assert_moment_certificate(name, k, start)

    def test_positive_kernel_fresh_region(self):
        for name in FILTERS:
            for k, start in ((25, 19), (41, 31), (72, 64)):
                self.assert_moment_certificate(name, k, start)

    def test_local_source_transport_identities(self):
        for name in FILTERS:
            for n in range(65):
                value, q, error = local_transport(name, n)
                self.assertEqual(value-q*self.values[n], error)
                self.assertGreater(error, 0)

    def test_odd_sign_mutant_rejected(self):
        value = filtered_source("ternary4", 7)
        self.assertGreater(value, 3**7*self.alpha[1])
        self.assertGreater(filter_error_interval("ternary4", 7)[0], 0)

    def test_positive_pascal_does_not_have_vanishing_absolute_error(self):
        # A finite adverse value calibrates the proved growing-error asymptotic.
        self.assertGreater(filter_error_interval("positive8", 128)[0], 1)

    def test_three_filter_minimum_denominator_endpoint_receipt(self):
        self.assertEqual([endpoint_denominator_possible(3, b) for b in range(1, 6)],
                         [False, False, False, True, True])

    def test_all_ternary_powers_exclude_denominators_one_and_two(self):
        for m in range(1, 41):
            self.assertFalse(endpoint_denominator_possible(3**m, 1))
            self.assertFalse(endpoint_denominator_possible(3**m, 2))
            self.assertEqual(endpoint_denominator_possible(3**m, 3), m % 4 == 0)

    def test_endpoint_test_is_not_claimed_sufficient(self):
        # Both endpoints pass, but adding a polynomial vanishing at0,1,16
        # can violate the interior bound without changing any endpoint.
        t = Q(1, 2)
        mutated = (t-4)/4 + 10*t*(t-1)*(t-16)
        self.assertTrue(endpoint_denominator_possible(3, 4))
        self.assertGreater(abs(mutated), 1)

    def test_kernel_interval_bounds(self):
        for j in range(257):
            t = Q(j, 256)
            self.assertTrue(-1 <= (t-4)/4 <= Q(-3, 4))
            self.assertTrue(Q(11, 12) <= 1-t*(1-t)/3 <= 1)

    def test_cover_readout_keeps_integer_lift(self):
        for name in ("ternary4", "ternary5", "base81"):
            for k in range(1, 25):
                value = filtered_source(name, k)
                b = FILTERS[name][1]**k
                h = b*value
                c = h.numerator//h.denominator
                self.assertEqual(phase_from_cover(h % 1, c % b, b), value % 1)

    def test_dropped_carry_mutant_is_visible(self):
        h = self.values[1]
        correct = filtered_source("ternary4", 1) % 1
        dropped = (h % 1)/4
        self.assertEqual(correct-dropped, Q(3, 4))

    def test_ternary4_exact_denominator_valuation(self):
        for k in range(1, 145):
            self.assertEqual(rational_valuation(ternary4_lift(k)), rational_valuation(Q(k)))
            self.assertEqual(rational_valuation(filtered_source("ternary4", k)),
                             rational_valuation(Q(k))-2*k)

    def test_base81_source_is_dyadically_integral(self):
        for k in range(1, 73):
            self.assertEqual(rational_valuation(filtered_source("base81", k)),
                             rational_valuation(Q(k)))

    def test_reset_source_initial_and_positive_recurrence(self):
        for start in (0, 1, 2, 3, 8, 19):
            self.assertEqual(base81_reset_source(start, 0), 0)
            for k in range(25):
                forcing_value = base81_reset_forcing(start, k)
                self.assertGreater(forcing_value, 0)
                self.assertEqual(base81_reset_source(start, k+1)
                                 -81*base81_reset_source(start, k), forcing_value)

    def test_reset_source_keeps_mahler_profile(self):
        for start in (0, 1, 2, 3, 19):
            for j in range(1, 41):
                self.assertEqual(rational_valuation(base81_reset_mahler(start, j)),
                                 difference_valuation(j))

    def test_reset_source_independent_real_shadow(self):
        for start in (2, 3, 8):
            beta = tuple(16**start*a-self.values[start] for a in self.alpha)
            for k in (1, 8, 25, 41):
                source = base81_reset_source(start, k)
                error = tuple(81**k*b-source for b in beta)
                lower, upper = filter_error_interval("base81", k, start, terms=5)
                self.assertLess(lower, error[0])
                self.assertLess(error[1], upper)

    def test_reset_forcing_is_completely_monotone_finite_control(self):
        for start in (2, 3, 8):
            values = [base81_reset_forcing(start, k) for k in range(25)]
            for k in range(1, 13):
                self.assertGreater((-1)**k*difference(values, 0, k), 0)

    def test_dyadic_mahler_profile(self):
        for kind in ("ternary4", "base81"):
            for k, a in enumerate(dyadic_mahler(kind, 72)[1:], 1):
                self.assertEqual(rational_valuation(a), difference_valuation(k))

    def test_translated_difference_profile(self):
        for kind in ("ternary4", "base81"):
            values = [ternary4_lift(k) if kind == "ternary4"
                      else filtered_source(kind, k) for k in range(106)]
            for start, orders in ((0, range(1, 25)), (8, range(1, 25)),
                                  (19, (25, 31)), (64, (25, 41))):
                for k in orders:
                    self.assertEqual(rational_valuation(difference(values, start, k)),
                                     difference_valuation(k))

    def test_modular_evaluator_and_full_permutations(self):
        for kind in ("ternary4", "base81"):
            for bits in range(1, 10):
                labels = [dyadic_filtered_mod(kind, n, bits) for n in range(2**bits)]
                self.assertEqual(sorted(labels), list(range(2**bits)))
            for n in (0, 1, 17, 41, 72):
                value = ternary4_lift(n) if kind == "ternary4" else filtered_source(kind, n)
                self.assertEqual(dyadic_filtered_mod(kind, n, 64), rational_mod(value, 64))

    def test_dyadic_negative_indices_are_periodic(self):
        for kind in ("ternary4", "base81"):
            for n in (-1, -17, -129):
                self.assertEqual(dyadic_filtered_mod(kind, n, 8),
                                 dyadic_filtered_mod(kind, n % 256, 8))

    def test_invalid_arithmetic_inputs(self):
        for call in (lambda: filtered_source("bad", 1),
                     lambda: filter_power("base81", -1),
                     lambda: filter_power("base81", True),
                     lambda: filter_error_interval("base81", 1, terms=0),
                     lambda: phase_from_cover(Q(1), 0, 3),
                     lambda: phase_from_cover(Q(0), 3, 3),
                     lambda: dyadic_filtered_mod("base81", 0, 0)):
            with self.assertRaises(ValueError):
                call()


class BinaryCarryControlTests(unittest.TestCase):
    def test_ambiguous_cylinder_count(self):
        for q in (3, 5, 7, 9, 13, 81):
            for m in range(1, 6):
                for extra in range(3):
                    L = q.bit_length()+extra
                    cells = ambiguous_cylinders(q, m, L)
                    self.assertEqual(len(cells), (q-1)*2**m)
                    for j in cells:
                        lo, hi = Q(j, 2**(m+L)), Q(j+1, 2**(m+L))
                        low_word = (q*lo*2**m).numerator//(q*lo*2**m).denominator
                        high_word = -((-q*hi*2**m).numerator//(-q*hi*2**m).denominator)-1
                        self.assertNotEqual(low_word, high_word)

    def test_tripling_ambiguity_is_two_alternating_suffixes(self):
        for m in range(1, 6):
            for L in range(2, 10):
                expected = {prefix*2**L+w for prefix in range(2**m)
                            for w in alternating_words(L)}
                self.assertEqual(set(ambiguous_cylinders(3, m, L)), expected)

    def test_bernoulli_uniform_cdf(self):
        for d in range(1, 34):
            for n in range(d+1):
                self.assertEqual(bernoulli_cdf(Q(n, d), Q(1, 2)), Q(n, d))

    def test_bernoulli_thirds_and_tripling(self):
        for p in (Q(1, 4), Q(1, 3), Q(1, 2), Q(2, 3), Q(3, 4)):
            d = 1-p+p*p
            self.assertEqual(bernoulli_cdf(Q(1, 3), p), (1-p)**2/d)
            expected = 1-p+p*(1-p)*(2*p-1)/d
            self.assertEqual(bernoulli_multiplied_half(3, p), expected)
        self.assertEqual(bernoulli_multiplied_half(3, Q(1, 4)), Q(33, 52))

    def test_bernoulli_fixed_doubling_and_failed_base81_symmetry(self):
        p = Q(1, 4)
        for q in (2, 4, 16):
            self.assertEqual(bernoulli_multiplied_half(q, p), 1-p)
        self.assertNotEqual(bernoulli_multiplied_half(81, p), 1-p)

    def test_alternation_synchronizes_without_preserving_law(self):
        p = Q(1, 4)
        for length in range(1, 41):
            expected = (2*(p*(1-p))**(length//2) if length % 2 == 0
                        else (p*(1-p))**(length//2))
            self.assertEqual(alternating_mass(length, p), expected)
        self.assertLess(alternating_mass(40, p), Q(1, 10**12))
        self.assertEqual((1-p)-bernoulli_multiplied_half(3, p), Q(3, 26))

    def test_four_phase_average_can_have_extra_symmetry(self):
        x = Q(1, 5)
        self.assertEqual(16*x % 1, x)
        self.assertNotEqual(3*x % 1, x)
        law = sorted(2**r*x % 1 for r in range(4))
        self.assertEqual(sorted(3*y % 1 for y in law), law)
        self.assertEqual(81*x % 1, x)

    def test_phase_addition_identity_without_independence(self):
        for x in (Q(1, 5), Q(3, 17), Q(29, 97)):
            for k in range(12):
                self.assertEqual(sum(comb(k, j)*(2**j*x % 1)
                                     for j in range(k+1)) % 1, 3**k*x % 1)

    def test_invalid_control_inputs(self):
        for call in (lambda: ambiguous_cylinders(4, 3, 4),
                     lambda: ambiguous_cylinders(81, 3, 3),
                     lambda: bernoulli_cdf(Q(1, 3), Q(0)),
                     lambda: bernoulli_cdf(0.5, Q(1, 4)),
                     lambda: alternating_words(0)):
            with self.assertRaises(ValueError):
                call()


if __name__ == "__main__":
    unittest.main()
