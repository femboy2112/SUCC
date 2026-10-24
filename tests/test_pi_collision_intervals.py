"""Independent exact calibration and fail-closed interval controls."""
from fractions import Fraction as Q
import unittest

from observational_succ.pi_collision_intervals import (
    SourceIntervals, atan_dyadic_bounds, machin_dyadic_bounds,
    source_intervals, tail_dyadic_bounds, certified_pair_count,
    certified_cell_counts, canonical_cells, interval_contains,
)
from observational_succ.pi_source_collision import bbp_states, small_ball_pairs


class CollisionIntervalTests(unittest.TestCase):
    def test_binary_split_against_direct_alternating_rationals(self):
        for q in (2, 5, 239):
            for bits in (8, 31, 80):
                # Independent direct series; next alternating term brackets truth.
                terms = bits+10
                partial = sum((Q((-1)**k, (2*k+1)*q**(2*k+1))
                               for k in range(terms)), Q())
                other = partial+Q((-1)**terms, (2*terms+1)*q**(2*terms+1))
                lo, hi = atan_dyadic_bounds(q, bits)
                self.assertLessEqual(Q(lo, 1 << bits), min(partial, other))
                self.assertGreaterEqual(Q(hi, 1 << bits), max(partial, other))

    def test_machin_interval_matches_exact_bbp_series(self):
        # pi/16 = sum 16^-j r(j); verify overlap using unrelated source formula.
        partial = Q()
        for j in range(1, 50):
            r = Q(4, 8*j-7)-Q(2, 8*j-4)-Q(1, 8*j-3)-Q(1, 8*j-2)
            partial += r/16**j
        remainder = Q(1, 16**49*(8*49+1)*(8*49+2))
        lo, hi = machin_dyadic_bounds(160)
        self.assertLess(Q(lo, 2**160), 16*(partial+remainder))
        self.assertGreater(Q(hi, 2**160), 16*partial)

    def test_tail_bounds_against_long_direct_fraction_sum(self):
        for n in (0, 1, 13, 260):
            partial = sum((Q(4, 8*(n+j)-7)-Q(2, 8*(n+j)-4)
                           -Q(1, 8*(n+j)-3)-Q(1, 8*(n+j)-2))/16**j
                          for j in range(1, 50))
            residual = Q(1, 16**49*(8*(n+49)+1)*(8*(n+49)+2))
            lo, hi = tail_dyadic_bounds(n, 80)
            self.assertLessEqual(Q(lo, 2**80), partial)
            self.assertGreaterEqual(Q(hi, 2**80), partial+residual)

    def test_source_and_counts_against_exact_recurrence_and_all_pairs(self):
        for p in (17, 97, 257):
            u = (p-1)//8
            exact = bbp_states(4*u)[u+1:]
            sample = source_intervals(u+1, 3*u)
            self.assertTrue(all(interval_contains(sample, i, v)
                                for i, v in enumerate(exact)))
            for cells in (3, 16, 256):
                brute = sum(min((x-y) % 1, (y-x) % 1) <= Q(1, cells)
                            for x in exact for y in exact)
                self.assertEqual(certified_pair_count(sample, cells), brute)
                self.assertEqual(brute, small_ball_pairs(exact, Q(1, cells)))
                counts = {}
                for x in exact:
                    cell = int(x*cells)
                    counts[cell] = counts.get(cell, 0)+1
                self.assertEqual(certified_cell_counts(sample, cells), counts)

    def test_boundaries_and_underresolution_fail_closed(self):
        # 4/16 threshold lies inside a pair difference interval.
        ambiguous = SourceIntervals(1, 4, ((1, 2), (5, 6)), 8, 1)
        with self.assertRaises(ArithmeticError):
            certified_pair_count(ambiguous, 4)
        with self.assertRaises(ArithmeticError):
            certified_cell_counts(SourceIntervals(1, 4, ((3, 4),), 8, 1), 4)
        with self.assertRaises(ArithmeticError):
            certified_pair_count(SourceIntervals(1, 4, ((1, 3), (2, 4)), 8, 1), 4)
        with self.assertRaises(ArithmeticError):
            source_intervals(3, 12, bits=4, tail_terms=1)
        exact_threshold = SourceIntervals(1, 4, ((1, 1), (5, 5)), 8, 0)
        self.assertEqual(certified_pair_count(exact_threshold, 4), 4)
        wrap = SourceIntervals(1, 4, ((0, 0), (15, 15)), 8, 0)
        self.assertEqual(certified_pair_count(wrap, 4), 4)

    def test_canonical_scale_and_rejected_domains(self):
        self.assertEqual([canonical_cells(p) for p in (1009, 2081, 4129, 1048601)],
                         [1, 16, 16, 256])
        for p in range(2, 200):
            m = canonical_cells(p)
            self.assertLessEqual(m**5, p*p)
            self.assertGreater((16*m)**5, p*p)
        for call in (lambda: source_intervals(0, 2),
                     lambda: atan_dyadic_bounds(1, 10),
                     lambda: tail_dyadic_bounds(1, 0),
                     lambda: canonical_cells(True),
                     lambda: certified_pair_count(SourceIntervals(1, 4, (), 8, 0), 4)):
            with self.assertRaises(ValueError):
                call()


if __name__ == '__main__':
    unittest.main()
