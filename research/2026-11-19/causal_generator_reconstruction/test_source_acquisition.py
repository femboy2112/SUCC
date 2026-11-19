"""Calibrated exact checks for SOURCE_ACQUISITION.md; no infinite inference."""
import unittest
from fractions import Fraction as Q
from itertools import combinations

import source_acquisition as sa


class SourceAcquisitionTests(unittest.TestCase):
    def test_all_early_schedules(self):
        theta = (Q(2, 7), Q(4), Q(-2), Q(-1), Q(-1))
        states = sa.states_through(8, theta[1:], theta[0])
        for times in combinations(range(9), 5):
            with self.subTest(times=times):
                self.assertEqual(sa.recover(times, [states[t] for t in times]), theta)
                self.assertGreater(sa.determinant(sa.block_matrix(times)), 0)

    def test_later_and_fibonacci_schedules(self):
        schedules = ((3, 7, 18, 31, 54), (17, 23, 41, 73, 91),
                     (0, 55, 89, 144, 233), (55, 56, 57, 58, 59))
        theta = (Q(-3, 11), Q(5, 3), Q(-7, 5), Q(2, 9), Q(11, 4))
        states = sa.states_through(233, theta[1:], theta[0])
        for times in schedules:
            with self.subTest(times=times):
                data = [states[t] for t in times]
                self.assertEqual(sa.recover(times, data), theta)
                self.assertEqual(sa.matvec(sa.sampling_matrix(times), theta), data)

    def test_positive_block_expansion(self):
        for times in ((0, 1, 2, 3, 4), (2, 4, 7, 9, 12), (0, 3, 4, 6, 8)):
            self.assertEqual(sa.determinant(sa.block_matrix(times)),
                             sa.block_determinant_expansion(times))

    def test_raw_jacobian_and_consecutive_formula(self):
        for n in (0, 1, 9, 32):
            times = tuple(range(n, n + 5))
            det = sa.determinant(sa.sampling_matrix(times))
            self.assertEqual(det, 16**sum(times) * sa.determinant(sa.block_matrix(times)))
            self.assertEqual(det, 16**n * sa.cauchy_determinant(range(n + 1, n + 5)))

    def test_precision_bounds_are_sharp(self):
        times = (2, 5, 8, 11, 14)
        matrix = sa.sampling_matrix(times)
        inv = sa.inverse(matrix)
        errors = [Q(j + 1, 1000) for j in range(5)]
        budgets = sa.precision_budget(times, errors)
        for j in range(5):
            signed = [e if a >= 0 else -e for a, e in zip(inv[j], errors)]
            error = sa.matvec(inv, signed)
            self.assertEqual(abs(error[j]), budgets[j])
        raw_volume = sa.knowledge_volume(times, errors)
        normalized = [[x / 16**t for x in row] for t, row in zip(times, matrix)]
        normalized_box = Q(1)
        for t, e in zip(times, errors):
            normalized_box *= 2 * e / 16**t
        self.assertEqual(raw_volume, normalized_box / abs(sa.determinant(normalized)))

    def test_four_samples_have_an_explicit_invisible_direction(self):
        # The last column of the inverse changes only the fifth sampled value.
        times = (0, 2, 7, 11, 19)
        matrix = sa.sampling_matrix(times)
        inv = sa.inverse(matrix)
        delta = [row[4] for row in inv]
        self.assertTrue(any(delta))
        self.assertEqual(sa.matvec(matrix, delta), [0, 0, 0, 0, 1])
        mutated = sa.states_through(times[-1], delta[1:], delta[0])
        self.assertEqual([mutated[t] for t in times[:4]], [0] * 4)
        self.assertEqual(mutated[times[-1]], 1)

    def test_source_and_seed_mutations_are_detected(self):
        times = (1, 4, 9, 16, 25)
        for seed, coefficients in ((Q(), sa.AUTHENTIC), (Q(1, 16), sa.AUTHENTIC),
                                   (Q(), (4, -2, -1, 0))):
            states = sa.states_through(times[-1], coefficients, seed)
            self.assertEqual(sa.recover(times, [states[t] for t in times]),
                             (seed, *map(Q, coefficients)))

    def test_wrapped_alias_is_an_actual_counterexample(self):
        a = sa.states_through(15)
        b = sa.states_through(15, seed=Q(1, 16))
        for n in range(1, 16):
            self.assertEqual(a[n] % 1, b[n] % 1)
            self.assertEqual(b[n] - a[n], 16**(n - 1))
        times = (1, 3, 6, 10, 15)
        self.assertNotEqual(sa.recover(times, [a[t] for t in times]),
                            sa.recover(times, [b[t] for t in times]))

    def test_wrong_block_weights_fail(self):
        times = (0, 2, 4, 6, 8)
        data = [sa.states_through(8)[t] for t in times]
        v = [x / 16**t for t, x in zip(times, data)]
        w = [v[i] - v[i - 1] for i in range(1, 5)]
        wrong = [[sum((Q(1, 8 * n - d) for n in range(a + 1, b + 1)), Q())
                  for d in sa.POLES] for a, b in zip(times, times[1:])]
        self.assertNotEqual(sa.matvec(sa.inverse(wrong), w), list(sa.AUTHENTIC))

    def test_delayed_out_of_family_source_is_not_authenticated(self):
        a = sa.states_through(10)
        b = a[:6]
        for n in range(6, 11):
            b.append(16 * b[-1] + sa.forcing(n) + (1 if n == 6 else 0))
        self.assertEqual(a[:6], b[:6])
        self.assertNotEqual(a[6], b[6])

    def test_completion_bound_covers_finite_future(self):
        for c in (sa.AUTHENTIC, (3, -8, 1, 2)):
            for m in (0, 1, 3, 8):
                tail = sum((sa.forcing(n, c) / 16**n for n in range(m + 1, m + 20)), Q())
                self.assertLessEqual(abs(tail), sa.completion_error_bound(c, m))

    def test_domain_rejections(self):
        for times in ((0, 1, 2, 3, 3), (0, 1, 2, 3), (-1, 0, 1, 2, 3),
                      (0, 1, 2, 3, Q(4))):
            with self.assertRaises(ValueError):
                sa.sampling_matrix(times)
        with self.assertRaises(ValueError):
            sa.inverse([[1, 1], [1, 1]])
        with self.assertRaises(ValueError):
            sa.block_determinant_expansion((0, 10, 20, 30, 40), max_terms=100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
