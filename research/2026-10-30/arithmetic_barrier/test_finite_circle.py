"""Instrument regression tests, separate from infinite mathematical claims."""
import unittest
from fractions import Fraction as F
from finite_circle import (SCALE, PI_LO, PI_HI, character, interval, mul,
                           selected_intervals, source_phases, occupancy,
                           full_sum_certificate)


class FiniteCircleTests(unittest.TestCase):
    def test_known_exact_quadrants(self):
        for q, re, im in ((0,1,0),(F(1,4),0,1),(F(1,2),-1,0),(F(3,4),0,-1)):
            r, s = character(q)
            self.assertLessEqual(r[0], re*SCALE)
            self.assertGreaterEqual(r[1], re*SCALE)
            self.assertLessEqual(s[0], im*SCALE)
            self.assertGreaterEqual(s[1], im*SCALE)
            self.assertLess(r[1]-r[0], 10**8)
            self.assertLess(s[1]-s[0], 10**8)

    def test_negative_multiplication_outward(self):
        exact = F(-2,3)*F(8,7)
        lo, hi = mul(interval(F(-2,3)), interval(F(8,7)))
        self.assertLessEqual(F(lo,SCALE), exact)
        self.assertGreaterEqual(F(hi,SCALE), exact)

    def test_pi_rational_interval(self):
        self.assertLess(F(333,106), PI_LO)
        self.assertLess(PI_HI, F(355,113))
        self.assertLess(PI_HI-PI_LO,F(1,10**100))

    def test_tail_refinement_nests(self):
        coarse = selected_intervals(64, 0)
        fine = selected_intervals(64, 8)
        for (a,b),(c,d) in zip(coarse,fine):
            self.assertLessEqual(a,c)
            self.assertLessEqual(d,b)

    def test_original_256_counts_recovered_independently(self):
        counts = occupancy(selected_intervals(256),16)
        self.assertEqual(counts["ambiguous"], [])
        self.assertEqual(counts["lower"], [17,18,18,15,14,12,16,18,19,24,13,13,14,16,13,16])

    def test_coherent_and_zero_frequency_do_not_cancel(self):
        coherent = [(F(0),F(0))]*32
        row = full_sum_certificate(coherent,1,32,1)
        self.assertFalse(row["strictly_below_quarter"])
        self.assertLessEqual(row["normalized_modulus_millionths"][0],10**6)
        self.assertGreaterEqual(row["normalized_modulus_millionths"][1],10**6)
        self.assertFalse(full_sum_certificate(selected_intervals(32),1,32,0)["strictly_below_quarter"])

    def test_exact_and_eventual_alias_arithmetic(self):
        # Circle alias after denominator's radix power dies; 1/7 is not one.
        for n in range(4,20):
            self.assertEqual((16**n*F(3,16**4)) % 1, 0)
            self.assertEqual((16**n*F(1,15)) % 1, F(1,15))
            self.assertNotEqual((16**n*F(1,7)) % 1, 0)

    def test_source_recurrence(self):
        self.assertEqual(source_phases(1),[F(2,15)])


if __name__ == "__main__":
    unittest.main(verbosity=2)
