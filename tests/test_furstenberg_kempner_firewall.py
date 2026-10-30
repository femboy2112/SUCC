"""Finite exact control for a rigorously proved binary sparse-digit counterexample.

Tests never establish transcendence/irrationality exponent: peer-reviewed source
is cited in KEMPNER_FURSTENBERG_FIREWALL.md. Infinite measure convergence
follows from the independent combinatorial window count proof there.
"""
import unittest
from fractions import Fraction


def kempner_truncation(max_power: int) -> Fraction:
    if type(max_power) is not int or not (0 <= max_power <= 15):
        raise ValueError("max_power must be an integer from 0 to 15")
    denominator = 1 << (1 << max_power)
    numerator = sum(1 << ((1 << max_power) - (1 << j))
                    for j in range(max_power + 1))
    return Fraction(numerator, denominator)


def shifts_with_one_in_next_window(N: int, L: int):
    if type(N) is not int or type(L) is not int or N < 1 or L < 1:
        raise ValueError("positive integer N,L required")
    return tuple(n for n in range(N)
                 if any(n < (1 << j) <= n + L
                        for j in range((N+L).bit_length())))


class KempnerFurstenbergTest(unittest.TestCase):
    def test_exact_binary_digit_positions(self):
        x = kempner_truncation(10)
        for j in range(11):
            k = 1 << j
            digit = (x.numerator >> (x.denominator.bit_length()-1-k)) & 1
            self.assertEqual(digit, 1)
        for k in range(1,1025):
            digit=(x.numerator >> (1024-k)) & 1
            self.assertEqual(digit, int(k & (k-1)==0))

    def test_sparse_windows_exact_prefix_and_count_bound(self):
        for N,L in ((32,3),(128,5),(400,12),(1024,20)):
            bad=shifts_with_one_in_next_window(N,L)
            self.assertLessEqual(len(bad), L*(1+(N+L).bit_length()-1))
            self.assertLess(len(bad),N)
            # The next L bits of a binary real after shift n are precisely
            # the original positions n+1,...,n+L.
            for n in range(N):
                first_L = tuple(int((n+k)&(n+k-1)==0) for k in range(1,L+1))
                self.assertEqual(n in bad, any(first_L))

    def test_small_radix_carry_orbit_finite_only(self):
        x=kempner_truncation(10)
        for n in range(50):
            shifted=(x*(1<<n))%1
            for L in (3,5,8):
                if n not in shifts_with_one_in_next_window(50,L):
                    self.assertLess(shifted,Fraction(1,1<<L))

    def test_countermodel_defeats_pointwise_entropy_shortcut(self):
        # For an N-bit sample, the number of distinct length-L windows is
        # not empirical Shannon entropy. This tests a finite structural
        # statement only, not the asymptotic zero-entropy theorem.
        N=4096
        digits=[int(k>0 and k&(k-1)==0) for k in range(1,N+1)]
        for L in (4,8,16,32):
            words={tuple(digits[k:k+L]) for k in range(N-L+1)}
            self.assertLessEqual(len(words), 4*L+2)

    def test_invalid_inputs(self):
        for value in (-1,16,1.0):
            with self.assertRaises(ValueError):kempner_truncation(value)
        with self.assertRaises(ValueError):shifts_with_one_in_next_window(10,0)


if __name__ == '__main__':
    unittest.main()
