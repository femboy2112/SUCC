"""Exact normalization controls for the fixed-resolution arithmetic proof.

These do not test the infinite Selberg--Delange conclusion. They test the
finite parity, diagonal and reindexing identities used to apply it.
"""
from fractions import Fraction as F
import unittest

from damped_filters import coefficients, polynomial, response
from goldbach_filters import prime_grade_histogram


def sieve_omega(limit):
    """Separate additive prime-power sieve; no production factorizer import."""
    prime = [True] * (limit + 1)
    prime[:2] = [False, False]
    out = [0] * (limit + 1)
    for p in range(2, limit + 1):
        if not prime[p]:
            continue
        for composite in range(p * p, limit + 1, p):
            prime[composite] = False
        power = p
        while power <= limit:
            for multiple in range(power, limit + 1, power):
                out[multiple] += 1
            power *= p
    return out


class FixedResolutionNormalizationTests(unittest.TestCase):
    def test_even_odd_partial_sum_constants_have_exact_origin(self):
        omega = sieve_omega(90)
        for s in (F(1, 2), F(1, 3), F(3, 4)):
            for size in (9, 16, 31, 45, 90):
                total = sum((s**omega[m] for m in range(1, size+1)), F())
                even = sum((s**omega[m] for m in range(2, size+1, 2)), F())
                odd = sum((s**omega[m] for m in range(1, size+1, 2)), F())
                half = sum((s**omega[m] for m in range(1, size//2+1)), F())
                self.assertEqual(even, s*half)
                self.assertEqual(total, even+odd)

    def test_unordered_triangle_requires_positive_diagonal_correction(self):
        for size in (2, 3, 7, 16, 41):
            omega = sieve_omega(2*size)
            for s in (F(1, 2), F(1, 3), F(3, 4)):
                shell_sum = sum((response(prime_grade_histogram(n), s)
                                 for n in range(2, size+1)), F())
                ordered = sum((s**(omega[a]+omega[b])
                               for a in range(2, 2*size-1)
                               for b in range(2, 2*size-a+1)
                               if (a+b) % 2 == 0), F())
                diagonal = sum((s**(2*omega[a]) for a in range(2, size+1)), F())
                self.assertEqual(shell_sum, (ordered+diagonal)/(2*s*s))
                self.assertNotEqual(shell_sum, ordered/(2*s*s))

    def test_dropping_parity_adds_genuine_wrong_midpoints(self):
        size, s = 7, F(1, 2)
        omega = sieve_omega(2*size)
        all_pairs = same_parity = F()
        for a in range(2, 2*size-1):
            for b in range(a, 2*size-a+1):
                weight = s**(omega[a]+omega[b]-2)
                all_pairs += weight
                if (a+b) % 2 == 0:
                    same_parity += weight
        self.assertGreater(all_pairs, same_parity)
        self.assertEqual(same_parity, sum((response(prime_grade_histogram(n), s)
                                         for n in range(2, size+1)), F()))

    def test_first_coefficient_and_filtering_commute_with_finite_midpoint_sum(self):
        omega = sieve_omega(38)
        for degree in (2, 4, 6, 8):
            for t in (F(1, 2), F(1, 3)):
                weights = coefficients(degree, t)
                denominator = F(1)
                for j in range(1, degree):
                    denominator *= 1-t**j
                self.assertEqual(weights[1], -t**(degree*(degree-1)//2)/denominator)
                from_responses = sum((weights[r]*response(prime_grade_histogram(n), t**r)
                                      for n in range(2, 20)
                                      for r in range(1, degree+1)), F())
                from_grades = sum((polynomial(weights, t**(omega[n+a]+omega[n-a]-2))
                                   for n in range(2, 20)
                                   for a in range(n-1)), F())
                self.assertEqual(from_responses, from_grades)


if __name__ == "__main__":
    unittest.main()
