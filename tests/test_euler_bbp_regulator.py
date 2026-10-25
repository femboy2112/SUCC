"""Independent finite source, residue partition and endpoint controls."""
import unittest
from fractions import Fraction as Q

from observational_succ import euler_bbp_regulator as b
from observational_succ.bbp_source_memory import forcing
from observational_succ.bbp_prime_window_signed_intervals import machin_pi_interval


class EulerBBPRegulatorTests(unittest.TestCase):
    def test_original_forcing_is_preserved(self):
        for n in range(1, 257):
            self.assertEqual(b.source_power_term(n), forcing(n))

    def test_finite_hurwitz_source_identity(self):
        for count in (0, 1, 2, 5, 12):
            for s in (0, 1, 2, 4):
                for z in (Q(0), Q(1, 16), Q(2, 3), Q(1)):
                    self.assertEqual(b.source_prefix(count, s, z),
                                     b.source_hurwitz_prefix(count, s, z))

    def test_residue_partition_uses_actual_indices(self):
        for p in (2, 3, 5, 6, 11):
            for s in (0, 1, 2, 3):
                for a in (Q(1, 8), Q(1), Q(7, 3)):
                    z = Q(3, 4)
                    expected = sum((z**n/(n+a)**s for n in range(p*3)), Q())
                    self.assertEqual(expected, b.lerch_refined_prefix(s, a, z, p, 3))

    def test_two_prime_refinements_commute_with_residue_reindexing(self):
        # Two different enumeration orders, compared with literal source time.
        for p, q in ((2, 3), (3, 5), (2, 7)):
            for s in (1, 2):
                z, a = Q(1, 2), Q(5, 8)
                first = sum((z**(p*j+i)/(p*j+i+a)**s
                             for i in range(p) for j in range(q*2)), Q())
                second = sum((z**(q*j+i)/(q*j+i+a)**s
                              for i in range(q) for j in range(p*2)), Q())
                self.assertEqual(first, second)
                self.assertEqual(first, b.lerch_prefix(s, a, z, p*q*2))

    def test_tail_bound_against_independent_deeper_partial_sums(self):
        # For strict lower, subtract a certified later upper from the earlier
        # lower; all finite intermediate mass is independently accumulated.
        for s in (1, 2, 3, 5):
            for N in (1, 3, 10):
                M = 8*N+13
                mass = sum((forcing(n) if s == 1 else
                            Q(4, (8*n-7)**s)-Q(2, (8*n-4)**s)
                            -Q(1, (8*n-3)**s)-Q(1, (8*n-2)**s)
                            for n in range(N+1, M+1)), Q())
                lo, hi = b.source_tail_bracket(N, s)
                later_lo, later_hi = b.source_tail_bracket(M, s)
                self.assertLess(mass, hi)
                self.assertGreater(mass+later_hi, lo)
                self.assertLess(mass+later_lo, hi)

    def test_bbp_geometric_value_against_independent_machin(self):
        # A finer independent enclosure lies inside the source enclosure.
        ml, mh = machin_pi_interval(32)
        for count in (2, 4, 8, 12):
            lo, hi = b.source_sum_interval(count, 1, Q(1, 16))
            self.assertLess(lo, ml)
            self.assertGreater(hi, mh)

    def test_geometric_tail_is_positive_and_monotone(self):
        for z in (Q(0), Q(1, 16), Q(3, 4), Q(1)):
            for s in (1, 2, 4):
                previous = b.source_sum_interval(1, s, z)
                for N in (2, 4, 8):
                    current = b.source_sum_interval(N, s, z)
                    # Intervals need not be nested in the unweighted estimate;
                    # they must intersect and their widths must shrink.
                    self.assertLessEqual(max(previous[0], current[0]),
                                         min(previous[1], current[1]))
                    self.assertLessEqual(current[1]-current[0], previous[1]-previous[0])
                    previous = current

    def test_zero_endpoint_and_cofinal_limits_are_distinct(self):
        self.assertEqual(sum(b.COEFFICIENTS), 0)
        for N in (1, 5, 20):
            self.assertEqual(b.source_prefix(N, 0), 0)
        self.assertEqual(b.balanced_boundary_zero_value(), Q(15, 8))
        self.assertEqual(b.cofinal_limit_for_power_clock(2), Q(15, 16))
        self.assertEqual(b.cofinal_limit_for_power_clock(3), Q(5, 4))
        self.assertNotEqual(b.cofinal_limit_for_power_clock(2), b.balanced_boundary_zero_value())

    def test_wrong_residue_scale_fails(self):
        # Omitting p^-s or using z instead of z^p silently changes the source.
        correct = b.lerch_prefix(2, Q(1, 8), Q(1, 16), 6)
        raw = sum((Q(1, 16)**j*b.lerch_prefix(2, (Q(1, 8)+j)/3,
                                            Q(1, 16), 2)
                   for j in range(3)), Q())
        self.assertNotEqual(correct, raw)
        self.assertNotEqual(correct, raw/9)

    def test_domain_guards(self):
        for bad in (True, 1.0, -1):
            with self.assertRaises(ValueError):
                b.source_power_term(1, bad)
        with self.assertRaises(ValueError):
            b.source_sum_interval(0)
        with self.assertRaises(ValueError):
            b.source_tail_bracket(1, 0)
        with self.assertRaises(ValueError):
            b.lerch_prefix(1, Q(0), Q(1, 2), 3)
        with self.assertRaises(ValueError):
            b.lerch_refined_prefix(1, Q(1), Q(2), 3, 2)
        # Without this guard m=400,dps=70 silently returned 0 instead of
        # approximately .9485, due to cancellation of enormous Hurwitz terms.
        with self.assertRaises(ValueError):
            b.numerical_power_clock(400, dps=70)


if __name__ == '__main__':
    unittest.main()
