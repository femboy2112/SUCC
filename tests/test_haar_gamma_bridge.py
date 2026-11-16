"""Exact controls for a declared classical model and authentic source measure."""
import unittest
from fractions import Fraction as F

from observational_succ.duck_bbp import forcing
from observational_succ.haar_gamma_bridge import (
    gamma_transition, gamma_haar_certificate, haar_projection,
    source_mass_interval, source_power_moment, source_haar_level_energy,
    source_residual_variance, source_haar_certificate, RationalInterval,
)


PATH = ((-1, 1, 0, 0), (1, -2, 1, 0), (0, 1, -2, 1), (0, 0, 1, -1))


def product(a, b):
    return tuple(tuple(sum(x*y for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def difference(a, b):
    return tuple(tuple(x-y for x, y in zip(r, s)) for r, s in zip(a, b))


def energy(a, vector):
    return sum(vector[i]*a[i][j]*vector[j] for i in range(len(a)) for j in range(len(a)))


class GammaHaarTests(unittest.TestCase):
    def test_literal_four_state_resolvent(self):
        expected = ((13, 5, 2, 1), (5, 10, 4, 2), (2, 4, 10, 5), (1, 2, 5, 13))
        self.assertEqual(gamma_transition(PATH, 1), tuple(tuple(F(x, 21) for x in r) for r in expected))

    def test_markov_normalization_and_resolvent_equation(self):
        for rate in (F(1, 3), F(1), F(7, 2)):
            g = gamma_transition(PATH, 1, rate)
            for row in g:
                self.assertEqual(sum(row), 1)
                self.assertTrue(all(x >= 0 for x in row))
            for i in range(4):
                for j in range(4):
                    lhs = sum((rate*(i == k)-PATH[i][k])*g[k][j] for k in range(4))
                    self.assertEqual(lhs, rate*(i == j))

    def test_nonzero_defect_is_fully_classical(self):
        cert = gamma_haar_certificate(PATH, 1, 1)
        v = (1, 1, -1, -1)
        self.assertEqual(cert.defect, tuple(tuple(F(x*y, 196) for y in v) for x in v))
        self.assertEqual(cert.trace_energy, F(1, 49))
        self.assertEqual(energy(cert.defect, v), F(4, 49))
        self.assertEqual(cert.defect, cert.hidden_grams[0])

    def test_constants_full_resolution_and_zero_depth_are_null(self):
        for depth, level in ((1, 0), (1, 2), (0, 1)):
            cert = gamma_haar_certificate(PATH, depth, level)
            self.assertEqual(cert.trace_energy, 0)
            self.assertTrue(all(x == 0 for row in cert.defect for x in row))

    def test_source_preserving_lumping_control(self):
        independent_pairs = ((-1, 1, 0, 0), (1, -1, 0, 0), (0, 0, -2, 2), (0, 0, 2, -2))
        self.assertEqual(gamma_haar_certificate(independent_pairs, 3, 1).trace_energy, 0)
        self.assertGreater(gamma_haar_certificate(PATH, 3, 1).trace_energy, 0)

    def test_two_hidden_levels_add_and_do_not_cancel(self):
        n = 8
        rows = [[0]*n for _ in range(n)]
        for j in range(n-1):
            rate = j+1
            rows[j][j+1] = rows[j+1][j] = rate
            rows[j][j] -= rate
            rows[j+1][j+1] -= rate
        cert = gamma_haar_certificate(rows, 2, 1, F(3, 2))
        self.assertEqual(len(cert.hidden_grams), 2)
        self.assertTrue(all(sum(m[i][i] for i in range(n)) > 0 for m in cert.hidden_grams))
        for i in range(n):
            for j in range(n):
                self.assertEqual(cert.defect[i][j], sum(m[i][j] for m in cert.hidden_grams))

    def test_depth_is_not_monotone_hidden_energy(self):
        one = gamma_haar_certificate(PATH, 1, 1).trace_energy
        eight = gamma_haar_certificate(PATH, 8, 1).trace_energy
        self.assertGreater(one, eight)
        self.assertGreater(eight, 0)

    def test_directed_cycle_kills_unqualified_positive_defect(self):
        # Independent literal positive stochastic Gamma resolvent of L=S-I.
        g = tuple(tuple(F(x, 15) for x in r) for r in
                  ((8, 4, 2, 1), (1, 8, 4, 2), (2, 1, 8, 4), (4, 2, 1, 8)))
        p = haar_projection(4, 1)
        compressed = product(product(p, g), p)
        defect = difference(product(product(product(p, g), g), p), product(compressed, compressed))
        v = (1, 1, -1, -1)
        self.assertEqual(energy(defect, v), F(-4, 25))
        directed = ((-1, 1, 0, 0), (0, -1, 1, 0), (0, 0, -1, 1), (1, 0, 0, -1))
        with self.assertRaises(ValueError):
            gamma_transition(directed, 1)

    def test_invalid_generators_and_domains(self):
        bad = ((), ((0, 0, 0),)*3, ((1, 0), (0, 0)), ((1, -1), (-1, 1)),
               ((-1.0, 1.0), (1.0, -1.0)), ((False, 0), (0, 0)))
        for matrix in bad:
            with self.subTest(matrix=matrix), self.assertRaises(ValueError):
                gamma_transition(matrix, 1)
        for depth in (-1, True, 17, F(1, 2)):
            with self.assertRaises(ValueError):
                gamma_transition(PATH, depth)
        for rate in (0, -1, 1.0, True):
            with self.assertRaises(ValueError):
                gamma_transition(PATH, 1, rate)
        for level in (-1, 3, True):
            with self.assertRaises(ValueError):
                gamma_haar_certificate(PATH, 1, level)


class OriginalSourceHaarTests(unittest.TestCase):
    def test_literal_source_matches_canonical_bbp_prefix(self):
        for terms in (1, 2, 7, 16):
            interval = source_mass_interval(terms=terms)
            prefix = sum((forcing(n)/16**n for n in range(1, terms+1)), F())
            self.assertEqual(interval.lower, prefix)
            self.assertEqual(interval.width, F(4, 15*16**terms))

    def test_source_channel_mutation_is_detected(self):
        authentic = source_mass_interval(terms=16)
        # Dropping the last negative source channel adds at least integral x^5/16=1/96.
        mutant_lower = authentic.lower+F(1, 96)
        self.assertGreater(mutant_lower, authentic.upper)

    def test_geometric_enclosures_nest_and_are_additive(self):
        for left, right in ((F(0), F(1)), (F(1, 7), F(5, 8)), (F(31, 32), F(1))):
            coarse = source_mass_interval(left, right, terms=5)
            fine = source_mass_interval(left, right, terms=13)
            self.assertLessEqual(coarse.lower, fine.lower)
            self.assertLessEqual(fine.upper, coarse.upper)
            mid = (left+right)/2
            l, r = source_mass_interval(left, mid), source_mass_interval(mid, right)
            whole = source_mass_interval(left, right)
            self.assertEqual(l.lower+r.lower, whole.lower)
            self.assertEqual(l.upper+r.upper, whole.upper)

    def test_exact_source_polynomial_moments(self):
        self.assertEqual(source_power_moment(0, 1, 1), F(1, 8))
        self.assertEqual(source_power_moment(0, 1, 2), F(7, 80))
        self.assertEqual(source_power_moment(0, F(1, 2), 1), F(3, 32))
        self.assertEqual(source_power_moment(F(1, 2), 1, 1), F(1, 32))
        for power in (1, 3, 9, 16):
            parts = sum((source_power_moment(F(j, 8), F(j+1, 8), power) for j in range(8)), F())
            self.assertEqual(parts, source_power_moment(0, 1, power))

    def test_native_covariance_has_certified_positive_size(self):
        v = source_residual_variance(0)
        self.assertGreater(v.lower, F(4, 100))
        self.assertLess(v.upper, F(41, 1000))
        self.assertLess(v.width, F(1, 10**16))

    def test_each_hidden_level_positive_and_remainder_decreases(self):
        previous = source_residual_variance(0, terms=12)
        for level in range(5):
            e = source_haar_level_energy(level, terms=12)
            residual = source_residual_variance(level+1, terms=12)
            self.assertGreater(e.lower, 0)
            self.assertGreater(residual.lower, 0)
            self.assertLess(residual.upper, previous.lower)
            self.assertLessEqual(residual.upper, F(1, 4*4**(level+1)))
            self.assertLessEqual(e.lower+residual.lower, previous.upper)
            self.assertGreaterEqual(e.upper+residual.upper, previous.lower)
            previous = residual

    def test_detail_sum_accounts_for_full_covariance(self):
        for power in (1, 2, 5):
            cert = source_haar_certificate(3, power=power, terms=14)
            lower = sum(e.lower for e in cert.level_energies)+cert.residual_variance.lower
            upper = sum(e.upper for e in cert.level_energies)+cert.residual_variance.upper
            self.assertLessEqual(lower, cert.total_variance.upper)
            self.assertGreaterEqual(upper, cert.total_variance.lower)
            self.assertLessEqual(cert.residual_variance.upper, cert.analytic_residual_bound)

    def test_fresh_higher_precision_confirms_all_intervals(self):
        for level in (0, 2, 4):
            low_precision = source_haar_level_energy(level, power=3, terms=8)
            holdout = source_haar_level_energy(level, power=3, terms=21)
            self.assertLessEqual(low_precision.lower, holdout.lower)
            self.assertLessEqual(holdout.upper, low_precision.upper)

    def test_invalid_interval_and_source_domains(self):
        for a, b in ((0, 0), (1, 0), (-1, 1), (0, 2), (0.0, 1), (False, 1)):
            with self.assertRaises(ValueError):
                source_mass_interval(a, b)
        for terms in (0, 65, True, 2.0):
            with self.assertRaises(ValueError):
                source_mass_interval(terms=terms)
        for power in (0, 9, True):
            with self.assertRaises(ValueError):
                source_haar_certificate(1, power=power)
        with self.assertRaises(ValueError):
            source_haar_certificate(8)
        with self.assertRaises(ValueError):
            RationalInterval(1, 0)


if __name__ == '__main__':
    unittest.main()
