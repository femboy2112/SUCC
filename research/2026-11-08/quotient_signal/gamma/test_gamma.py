"""Finite regression and hostile checks, separate from all-N paper claims."""
from fractions import Fraction as F
import unittest
import oracle as q


class GammaResidualTests(unittest.TestCase):
    def test_source_from_independent_integral(self):
        for n in range(1, 128):
            self.assertEqual(q.source(n), q.source_integral(n))

    def test_effective_tail_bound(self):
        for n in (1, 2, 3, 17, 113, 509, 1009):
            lo, hi = q.tail_interval(n)
            self.assertLess(hi, F(1, 64*n*n))
            self.assertGreater(lo, F(1, 64*n*n)-F(7, 512*n**3))

    def test_dyadic_rounding_is_outward(self):
        for lo, hi in ((F(-1, 3), F(2, 7)), (F(1, 8), F(1, 8))):
            result = q.outward_dyadic((lo, hi), 12)
            self.assertLessEqual(F(int(result["lo"]), 2**12), lo)
            self.assertGreaterEqual(F(int(result["hi"]), 2**12), hi)

    def test_constant_is_inside_independent_first_window(self):
        c_lo, c_hi = q.constant_interval()
        t_lo, t_hi = q.tail_interval(1)
        self.assertGreater(t_lo-F(1, 64)-c_hi, 0)
        self.assertLess(t_hi-F(1, 64)-c_lo, F(7, 512))

    def test_seed_boundary_is_not_removed_from_lift(self):
        seed = F(1, 7)
        source = F()
        shifted = seed
        for n in range(1, 33):
            source = 16*source+q.source(n)
            shifted = 16*shifted+q.source(n)
            self.assertEqual(shifted-source, seed*16**n)

    def test_wrong_first_pole_fails_tail_scale(self):
        n = 97
        lower = sum(((q.source(n+j)+F(1, 8*(n+j)-7))/16**j
                     for j in range(1, 25)), F())
        self.assertGreater(lower, F(1, 64*n*n))

    def test_invalid_domains_are_rejected(self):
        for n in (0, -1, True, F(1, 2)):
            with self.assertRaises(ValueError):
                q.source(n)
        with self.assertRaises(ValueError):
            q.tail_interval(1, 0)


if __name__ == "__main__":
    unittest.main()
