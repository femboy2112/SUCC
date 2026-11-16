"""Independent finite checks and mutation controls, not a proof of RH."""
from fractions import Fraction as F
from math import lcm
import random
import unittest
from certify import (coefficients, mobius, value_at, prefix_direct, prefix_mobius,
                     pair_mean, tail_constants, norm_interval, verify_record)


def exact_partial(c, T):
    return sum((value_at(c, n)**2/F(n*(n+1)) for n in range(1, T+1)), F())


def log_two_interval(terms=60):
    x = F(1, 3)
    lo = 2*sum((x**(2*j+1)/(2*j+1) for j in range(terms)), F())
    return lo, lo+2*x**(2*terms+1)/((2*terms+1)*(1-x*x))


class CertificateTests(unittest.TestCase):
    def test_mobius_divisor_identity(self):
        for n in range(1, 201):
            self.assertEqual(sum(mobius(d) for d in range(1, n+1) if n % d == 0), int(n == 1))

    def test_prefix_rigidity_and_repair(self):
        for n in range(1, 21):
            c = {k: F(-mobius(k)) for k in range(2, n+1)}
            c[n+1] = (n+1)*sum((F(mobius(k), k) for k in range(1, n+1)), F())
            self.assertTrue(prefix_direct(c, n))
            self.assertTrue(prefix_mobius(c, n))
            c[n+1] += F(1, 97)
            self.assertFalse(prefix_direct(c, n))
            self.assertFalse(prefix_mobius(c, n))

    def test_direct_structured_agreement(self):
        rng = random.Random(618619)
        for _ in range(100):
            c = {k: F(rng.randint(-3, 3), rng.randint(1, 7)) for k in range(2, 10)}
            for n in range(1, 10):
                self.assertEqual(prefix_direct(c, n), prefix_mobius(c, n))

    def test_pair_mean_full_periods(self):
        for k in range(2, 17):
            for ell in range(2, 17):
                L = lcm(k, ell)
                actual = sum((F(n % k, k)*F(n % ell, ell) for n in range(1, L+1)), F())/L
                self.assertEqual(actual, pair_mean(k, ell))

    def test_missing_gcd_term_mutation(self):
        wrong = F((2-1)*(2-1), 4*2*2)
        self.assertNotEqual(wrong, pair_mean(2, 2))
        self.assertEqual(pair_mean(2, 2), F(1, 8))

    def test_signed_square_mean_full_period(self):
        for c in ({2: F(3), 3: F(-2)}, {4: F(1, 3), 6: F(-5, 7), 7: F(2)}):
            L = lcm(*c)
            actual = sum((value_at(c, n)**2 for n in range(1, L+1)), F())/L
            self.assertEqual(tail_constants(c)[0], actual)

    def test_cyclic_pair_discrepancy(self):
        for k in range(2, 8):
            for ell in range(2, 8):
                L, mean = lcm(k, ell), pair_mean(k, ell)
                for phase in range(L):
                    partial = F()
                    for j in range(1, L+1):
                        n = phase+j
                        partial += F(n % k, k)*F(n % ell, ell)-mean
                        self.assertLessEqual(abs(partial), F(L, 4))

    def test_known_log_two_norm(self):
        truth_lo, truth_hi = log_two_interval()
        for T in (20, 100, 1000):
            lo, hi = norm_interval({2: F(2)}, T)
            self.assertLessEqual(lo, truth_lo)
            self.assertGreaterEqual(hi, truth_hi)

    def test_null_and_finitely_supported_target(self):
        lo, hi = norm_interval({}, 10)
        self.assertLessEqual(lo, 0)
        self.assertGreaterEqual(hi, 0)
        target = {1: F(3, 7), 9: F(-2)}
        exact = sum((x*x/F(n*(n+1)) for n, x in target.items()), F())
        lo, hi = norm_interval({}, 10, target=target)
        self.assertLessEqual(lo, exact)
        self.assertGreaterEqual(hi, exact)

    def test_target_shift_identity(self):
        c, target = {2: F(2)}, {1: F(1)}
        a, b = norm_interval(c, 100)
        x, y = norm_interval(c, 100, target=target)
        self.assertEqual(a-x, F(1, 2))
        self.assertEqual(b-y, F(1, 2))

    def test_interval_overlaps_independent_crude_interval(self):
        c = {2: F(1, 3), 3: F(-5, 7), 5: F(3, 2)}
        partial = exact_partial(c, 200)
        crude_upper = partial+sum(abs(x) for x in c.values())**2/201
        lo, hi = norm_interval(c, 40)
        self.assertLessEqual(lo, crude_upper)
        self.assertGreaterEqual(hi, partial)

    def test_positive_negative_certificates(self):
        pos = {'name': 'positive', 'prefix_length': 1, 'coefficients': {'2': '2'}, 'expected': 'LT_1'}
        neg = {'name': 'negative', 'prefix_length': 4,
               'coefficients': {'2': '1', '3': '1', '5': '5/6'}, 'expected': 'GT_1'}
        self.assertEqual(verify_record(pos, 1000)['status'], 'LT_1')
        self.assertEqual(verify_record(neg, 1000)['status'], 'GT_1')

    def test_certificate_binding_mutations(self):
        r = {'name': 'bad', 'prefix_length': 1, 'coefficients': {'2': '3'}}
        with self.assertRaises(ValueError):
            verify_record(r, 100)
        r['coefficients'] = {'2': '2'}
        r['expected'] = 'GT_1'
        with self.assertRaises(ValueError):
            verify_record(r, 100)

    def test_invalid_input(self):
        for raw in ({'1': '1'}, {'02': '1'}, {'2': 1}, {'2': 'nan'}):
            with self.assertRaises((ValueError, TypeError)):
                coefficients(raw)
        for T in (0, -1, 1.5):
            with self.assertRaises(ValueError):
                norm_interval({}, T)
        with self.assertRaises(ValueError):
            norm_interval({}, 10, target={11: F(1)})


if __name__ == '__main__':
    unittest.main()
