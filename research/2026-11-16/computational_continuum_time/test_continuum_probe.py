"""Independent stdlib regression tests for source-labelled continuum-time claims."""
import unittest
from fractions import Fraction

from continuum_probe import (
    forcing, rational_history, source_tail_interval,
    completed_orbit_interval, solenoid_history, solenoid_shift,
    fractional_part, relative_winding, complex_phase,
    path_distance_squared, integer_deck_metric_bound,
    gamma_alpha_one_upper_bound, gamma_translation_multiplier,
    gamma_variance_identity,
)


class TestContinuumTime(unittest.TestCase):
    def test_four_signed_poles(self):
        self.assertEqual(forcing(1), Fraction(47, 15))
        for n in range(1, 30):
            self.assertGreater(forcing(n), 0)

    def test_strictly_decaying_forcing(self):
        for n in range(1, 30):
            self.assertGreater(forcing(n), forcing(n+1))

    def test_zero_seed_and_integer_deck(self):
        for n in range(0, 12):
            self.assertEqual(rational_history(n, Fraction(3)) - rational_history(n), 3*16**n)

    def test_source_completion_interval(self):
        # Exact rational Machin bounds, not a double-precision pi equality.
        def arctan_bounds(z, terms=54):
            val = sum(((-1)**j * z**(2*j+1) / (2*j+1)
                       for j in range(terms)), Fraction())
            delta = z**(2*terms+1) / (2*terms+1)
            return ((val, val+delta) if terms % 2 == 0
                    else (val-delta, val))
        a_lo, a_hi = arctan_bounds(Fraction(1,5))
        b_lo, b_hi = arctan_bounds(Fraction(1,239))
        pi_lo, pi_hi = 16*a_lo-4*b_hi, 16*a_hi-4*b_lo
        for n in range(0, 8):
            lo, hi = completed_orbit_interval(n, 17)
            factor = Fraction(16**n,16)
            self.assertLess(lo, factor*pi_lo)
            self.assertGreater(hi, factor*pi_hi)

    def test_tail_bounds(self):
        for n in range(0, 14):
            lo, hi = source_tail_interval(n, 0)
            self.assertEqual(lo, 0)
            self.assertEqual(hi, forcing(n+1)/15)

    def test_solenoid_inverse_limit(self):
        for x in (Fraction(1, 7), Fraction(23, 19), Fraction(-31, 11)):
            c = solenoid_history(x, 14)
            self.assertTrue(all(fractional_part(16*c[j+1]) == c[j] for j in range(len(c)-1)))

    def test_natural_extension_shift(self):
        x = Fraction(23, 13)
        c = solenoid_history(x, 12)
        d = solenoid_shift(c)
        self.assertEqual(d, solenoid_history(16*x, 12))

    def test_integer_lifts_same_present_circle(self):
        x = Fraction(23, 13)
        for k in (-23, -1, 1, 16, 32):
            self.assertEqual(solenoid_history(x, 1), solenoid_history(x+k, 1))
            for n in range(6):
                self.assertEqual(fractional_part(16**n*x), fractional_part(16**n*(x+k)))

    def test_integer_lifts_different_prehistory(self):
        x = Fraction(7, 19)
        for k in (-23, -1, 1, 16, 32):
            self.assertNotEqual(solenoid_history(x, 7), solenoid_history(x+k, 7))

    def test_indistinguishable_to_depth_if_divisible(self):
        x = Fraction(1, 7)
        k = 16**3
        c = solenoid_history(x, 6)
        d = solenoid_history(x+k, 6)
        self.assertEqual(c[:4], d[:4])
        self.assertNotEqual(c[4], d[4])

    def test_winding_exact_integer_counts(self):
        for k in (-3, -1, 0, 1, 5):
            for n in range(0, 8):
                self.assertEqual(relative_winding(k, n), k*(16**(n+1)-16**n))

    def test_phase_integer_deck_vs_fractional(self):
        for k in (1, 2):
            for n in (0, 1):
                self.assertAlmostEqual(abs(complex_phase(float(n), float(k))-1), 0, delta=1e-11)
        self.assertGreater(abs(complex_phase(0.125, 1)-1), 0.1)
        self.assertLess(abs(complex_phase(0.25, 1)-1), 1e-11)
        self.assertLess(abs(complex_phase(0.5, 1)-1), 1e-11)

    def test_metric_exact_deck_bound(self):
        for k in (1, 2, 5, 11):
            got = path_distance_squared(0, float(k), 8192)
            lo, hi = integer_deck_metric_bound(k)
            self.assertTrue(lo <= got <= hi, (k, lo, got, hi))
            self.assertGreater(got, 1.8)

    def test_metric_translation_symmetry(self):
        self.assertAlmostEqual(path_distance_squared(0.33, 1.33, 2048),
                               path_distance_squared(2.33, 3.33, 2048), places=8)

    def test_metric_triangle(self):
        a = path_distance_squared(0.1, 0.7, 2048)**0.5
        b = path_distance_squared(0.7, 1.2, 2048)**0.5
        c = path_distance_squared(0.1, 1.2, 2048)**0.5
        self.assertLessEqual(c, a+b+1e-8)

    def test_nonzero_source_lift(self):
        with self.assertRaises(ValueError):
            gamma_alpha_one_upper_bound(0, 3)
        self.assertLess(gamma_alpha_one_upper_bound(1, 3), 0.001)

    def test_gamma_multipliers_semigroup(self):
        for w in (0, 0.5, 2, 11):
            x = gamma_translation_multiplier(0.7, w)
            y = gamma_translation_multiplier(1.4, w)
            z = gamma_translation_multiplier(2.1, w)
            self.assertLess(abs(x*y-z), 1e-12)

    def test_gamma_variance_decomposition(self):
        v = [complex(1,1), complex(-1,0), complex(0,3)]
        p = [.2,.4,.4]
        total, square_mean, variance = gamma_variance_identity(v,p)
        self.assertAlmostEqual(total, square_mean+variance)
        self.assertGreater(variance, 0)

    def test_not_a_metric_on_unlabelled_circle(self):
        self.assertAlmostEqual(abs(complex_phase(0,0)-complex_phase(0,1)), 0, delta=1e-12)
        self.assertGreater(path_distance_squared(0,1,4096), 1.8)


if __name__ == "__main__":
    unittest.main()
