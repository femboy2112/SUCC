from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from intervals import SCALE, Box, Interval, phase, mean, contains_rational, pi_box
from source import common_history, direct_modular_residue, principal_pair, matched_seed
from observational_succ.selected_orbit import original_forcing
from observational_succ.pi_succ_character_intervals import characteristic_interval, machin_pi_interval
from finite_adelic import principal, construct


class InstrumentTests(unittest.TestCase):
    def test_outward_operations_signed_and_zero_crossing(self):
        samples = [Q(-7, 3), Q(-1, 11), Q(0), Q(2, 7), Q(12, 5)]
        for x in samples:
            a = Interval.ratio(x.numerator, x.denominator)
            self.assertTrue(contains_rational(a.square(), x*x))
            for y in samples:
                b = Interval.ratio(y.numerator, y.denominator)
                self.assertTrue(contains_rational(a*b, x*y))
                self.assertTrue(contains_rational(a+b, x+y))
                self.assertTrue(contains_rational((a-b).divide(7), (x-y)/7))

    def test_exact_quadrants_and_wraps(self):
        for k in range(-13, 18):
            box = phase(k, 4)
            re, im = ((1, 0), (0, 1), (-1, 0), (0, -1))[k % 4]
            self.assertTrue(contains_rational(box.re, re))
            self.assertTrue(contains_rational(box.im, im))
            self.assertLess(box.re.hi-box.re.lo, 1000)

    def test_independent_fraction_taylor_calibration(self):
        pi = machin_pi_interval(20)
        values = [Q(n, 37) for n in range(-40, 41)]
        values += [Q(1, 8)+Q(e, 10**40) for e in (-1, 0, 1)]
        values += [Q(123456789, 10**100+39), Q(10**100+38, 10**100+39)]
        for value in values:
            observed = phase(value.numerator, value.denominator)
            independent = characteristic_interval(value, pi, 16)
            for actual, lo, hi in ((observed.re, *independent[:2]),
                                   (observed.im, *independent[2:])):
                self.assertLessEqual(Q(actual.lo, SCALE), hi)
                self.assertGreaterEqual(Q(actual.hi, SCALE), lo)
                self.assertLess(Q(actual.hi-actual.lo, SCALE), Q(1, 10**18))

    def test_character_product_transport_and_conjugation(self):
        for n in range(19):
            a, b = phase(n, 19), phase(7*n+1, 23)
            product = a*b
            target = phase(23*n+19*(7*n+1), 19*23)
            self.assertTrue(product.re.overlaps(target.re))
            self.assertTrue(product.im.overlaps(target.im))
            negative = phase(-n, 19)
            self.assertEqual(a.conjugate(), negative)

    def test_bilinear_covariance_is_not_hermitian(self):
        a = [phase(0), phase(1, 4)]
        w = mean([x*x for x in a])
        c = w-mean(a)*mean(a)
        self.assertTrue(contains_rational(c.re, 0))
        self.assertTrue(contains_rational(c.im, Q(-1, 2)))
        self.assertFalse(contains_rational(c.re, Q(1, 2)))

    def test_independent_source_recurrence_and_modular_sum(self):
        data = common_history(140)
        D, residues = data['denominator'], data['residues']
        state = Q(0)
        for n in range(141):
            if n:
                state = 16*state+original_forcing(n)
            self.assertEqual(Q(residues[n], D), state % 1)
            for p in (3, 5, 7, 17, 41):
                numerator, denominator = principal_pair(residues[n], D, p)
                self.assertEqual(Q(numerator, denominator), principal(state, p))
            if n in (0, 1, 7, 29, 71, 139, 140):
                self.assertEqual(residues[n], direct_modular_residue(n, D))
        self.assertEqual(Q(data['final_unwrapped_numerator'], D), state)

    def test_shadow_matches_independent_previous_construction(self):
        A = 17
        data = common_history(2*A-1, A)
        seed, center, M = matched_seed(data, A, 9, Q(1, 2**18), (3, 5, 7, 41))
        previous = construct(5, A, A, 9, Q(1, 2**18), (3, 5, 7, 41))
        self.assertEqual((seed, center, M), (previous['seed'], previous['center'], previous['M']))

    def test_reject_inexact_malformed_domains(self):
        for args in ((True, 3), (0.1, 3), (1, 0), (1, -3)):
            with self.assertRaises(ValueError):
                phase(*args)
        for args in ((True, 0), (10, 11), (0, 0)):
            with self.assertRaises(ValueError):
                common_history(*args)
        with self.assertRaises(ValueError):
            principal_pair(1, 3, 9)
        with self.assertRaises(ValueError):
            mean([])


if __name__ == '__main__':
    unittest.main()
