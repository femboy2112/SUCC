"""Small exact regression checks for the spectral audit and minimax witness."""
from fractions import Fraction as Q
import unittest

from independent_oracle import (
    alias_moments, difference_piecewise, fejer_by_pairs, fejer_moment,
    forcing, forcing_combined, pi_interval, scaled_weight,
    source_transcript,
)


class SpectralAuditTests(unittest.TestCase):
    def test_sharp_real_law_constant_and_competing_mode(self):
        lo, hi = pi_interval()
        ratio = Q(116281, 205)
        self.assertEqual(scaled_weight(2, lo*lo)/scaled_weight(32, lo*lo), ratio)
        self.assertLess((hi*hi+8)/8*Q(255**2, 257), ratio)

    def test_fejer_independent_square_amplitude_coefficients(self):
        for M in (3, 5, 11):
            for h in range(-2*M, 2*M+1):
                self.assertEqual(fejer_moment(M, h), fejer_by_pairs(M, h))

    def test_positive_law_alias_pair_has_exact_low_band(self):
        for h in range(-17, 18):
            self.assertEqual(*alias_moments(17, h))
        self.assertEqual(alias_moments(17, 34), (Q(1, 2), Q(0)))

    def test_exact_piecewise_tail(self):
        for h in range(-101, 102):
            a, b = alias_moments(19, h)
            self.assertEqual(a-b, difference_piecewise(19, h))

    def test_unlimited_finite_memory_does_not_split_witness(self):
        for N in (0, 1, 3, 5):
            self.assertEqual(*source_transcript(11*16**N, 11, N))

    def test_next_time_exposes_previously_missing_mode(self):
        H, N = 19, 3
        M = H*16**N
        self.assertEqual(*source_transcript(M, H, N))
        self.assertEqual(alias_moments(M, 3*16**(N+1)), (Q(1, 2), Q(0)))

    def test_source_preserves_all_signed_poles(self):
        self.assertEqual(forcing(1), Q(47, 15))
        for n in (1, 2, 17, 61, 151):
            self.assertEqual(forcing(n), forcing_combined(n))


if __name__ == "__main__":
    unittest.main()
