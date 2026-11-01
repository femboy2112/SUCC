"""Independent source/cosine comparisons and clipped transport counterchecks."""
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT/path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


T = load('_fireworks_transport', 'research/2026-10-31/signed_lag_fireworks/transport.py')
I = load('_fireworks_interval', 'research/2026-10-31/signed_lag_fireworks/interval_oracle.py')
P = load('_fireworks_parent', 'research/2026-10-31/selected_lag_tomography/selected_lag.py')


class FireworksTransportTests(unittest.TestCase):
    def test_source_representation_and_circle_recurrence(self):
        for n in range(1, 121):
            self.assertEqual(I.source(n), P.r(n))
        for s in (F(0), F(1, 7), F(-7, 19)):
            self.assertEqual(I.circle_states(80, s), tuple(u % 1 for u in P.original_states(80, s)))

    def test_independent_pi_enclosures_overlap(self):
        for d in (4, 12, 28):
            a, b = I.pi_interval(d)
            c, e = P._machin_pi_bracket(40)
            self.assertLessEqual(max(a, c), min(b, e))
            self.assertLess(b-a, F(1, 16**(d-1)))

    def test_exact_trigonometric_roots(self):
        for x, y in ((0, 1), (F(1, 6), F(1, 2)), (F(1, 4), 0),
                     (F(1, 3), F(-1, 2)), (F(1, 2), -1), (F(3, 4), 0)):
            a, b = I.cosine(x)
            self.assertLessEqual(a, y)
            self.assertLessEqual(y, b)
            self.assertLessEqual(b-a, F(1, 10**10))

    def test_independent_cosine_instruments(self):
        for q in (7, 17, 31):
            for j in range(q):
                a, b = I.cosine(F(j, q))
                c, d = P.cos_interval(F(j, q))
                self.assertLessEqual(max(a, c), min(b, d))
        # Huge exact denominators and both sides of a dyadic-cell boundary.
        for x in (F(1, 4)+F(1, 10**500+3), F(1, 4)-F(1, 10**500+3)):
            a, b = I.cosine(x)
            c, d = P.cos_interval(x)
            self.assertLessEqual(max(a, c), min(b, d))

    def test_pointwise_source_clipping(self):
        for n in (1, 2, 7, 31):
            for k in (1, 2, 3, 5):
                for h in (1, 3, 11):
                    chord = min(F(2), F(44*h, 7)*P.lag_forcing(n, k))
                    self.assertLessEqual(chord, T.point_error(n, k, h))

    def test_integral_bound_covers_partial_clipped_sums(self):
        for k, h in ((1, 1), (2, 3), (3, 5), (6, 11)):
            grid = 2**32
            bound = F(T.ceil_sqrt_fraction(F(11*h*(16**k-1), 14)*grid**2), grid)
            partial = sum((T.point_error(n, k, h) for n in range(1, 500)), F(0))
            self.assertLessEqual(partial, bound)

    def test_actual_vs_reduced_signed_intervals(self):
        for N, K, h in ((24, 3, 1), (39, 5, 3), (65, 3, 11)):
            U = I.circle_states(N)
            (a, b), _ = I.score_from_states(U, K, h, actual=True)
            (c, d), _ = I.score_from_states(U, K, h)
            budget = T.weighted_error(N, K, h)
            self.assertLessEqual(max(b-c, d-a), budget)

    def test_new_budget_dominates_old_and_closed_formula(self):
        for N, K, h in ((128, 4, 1), (1024, 5, 3), (4096, 6, 11)):
            new = T.weighted_error(N, K, h)
            old = P.vdc_lag_error_bound_rational(K, N, h)['weighted_rational_upper']
            self.assertLessEqual(new, old)
            self.assertLessEqual(new, T.simple_error(N, K, h))
        self.assertLess(T.weighted_error(4096, 6, 1), F(1, 20))

    def test_clock_and_asymptotic_budget(self):
        for j in range(1, 80):
            N = 4**j
            self.assertEqual(T.doubled_clock(N-1), j-1)
            self.assertEqual(T.doubled_clock(N), j)
            self.assertEqual(T.simple_error(N, j, 1), F(8, 9*j*j) if j>1 else 0)

    def test_invalid_inputs_and_negative_energy_rejected(self):
        for args in ((0, 1, 1), (4, 5, 1), (4, 2, 0), (4, True, 1)):
            with self.assertRaises(ValueError):
                T.weighted_error(*args)
        with self.assertRaises(ValueError):
            T.certificate(4096, 4, 1, (-9, -8))
        self.assertEqual(T.weighted_error(100, 1, 3), 0)


if __name__ == '__main__':
    unittest.main()
