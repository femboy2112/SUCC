"""Tests for the parity Fourier reconstruction (F-11)."""
import unittest
import mpmath as mp

from observational_succ import parity_fourier_reconstruction as pfr


class ParityFourierReconstructionTests(unittest.TestCase):
    def test_completed_digits_are_pi(self):
        # First digits are 2,4,3,15,6 = 243F6... (hex digits of pi).
        self.assertEqual([pfr.completed_digit(n) for n in range(1, 6)],
                         [2, 4, 3, 15, 6])

    def test_reconstruction_approximates_direct(self):
        # Truncated Fourier reconstruction is close to the direct parity mean
        # and converges as H grows.
        A = 32
        P_direct = mp.mpf(sum(pfr.parity(n) for n in range(A, 2 * A))) / A
        P_low = pfr.fourier_reconstruct(A, 48)
        P_high = pfr.fourier_reconstruct(A, 192)
        self.assertLess(abs(P_high - P_direct), abs(P_low - P_direct))

    def test_reconstruction_within_tolerance(self):
        A = 32
        P_direct = mp.mpf(sum(pfr.parity(n) for n in range(A, 2 * A))) / A
        P_fourier = pfr.fourier_reconstruct(A, 192)
        self.assertLess(abs(P_fourier - P_direct), 0.1)


if __name__ == '__main__':
    unittest.main()
