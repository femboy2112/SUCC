from fractions import Fraction as Q
from math import gcd
import unittest
from hostile_exact import literal_history, source_sigma, two_prime_clock, vprime


class HostileExactTests(unittest.TestCase):
    def test_sharp_height_boundary_is_not_closed(self):
        qstar = max(q for q in range(1, 30) if gcd(q, 30) == 1)
        witness = Q(6, qstar)
        self.assertEqual(witness, Q(6, 29))
        self.assertEqual(vprime(witness, 2), 1)
        self.assertEqual(vprime(witness, 3), 1)
        self.assertEqual(vprime(witness, 5), 0)
        self.assertNotEqual(witness, 0)

    def test_carry_fiber_upper_boundary_is_excluded(self):
        u = literal_history(23)
        sigma = source_sigma(u)
        self.assertTrue(all((x+16**n*sigma/2)//1 == x//1 for n, x in enumerate(u)))
        self.assertTrue(any((x+16**n*sigma)//1 != x//1 for n, x in enumerate(u)))

    def test_integer_seed_shift_needs_initial_lift(self):
        u = literal_history(13)
        shifted = [x+16**n for n, x in enumerate(u)]
        self.assertNotEqual(u[0]//1, shifted[0]//1)
        self.assertEqual([u[n]//1-16*(u[n-1]//1) for n in range(1, 14)],
                         [shifted[n]//1-16*(shifted[n-1]//1) for n in range(1, 14)])

    def test_fixed_support_clock_has_strong_signed_covariance(self):
        path, square, lower = two_prime_clock(13, 17)
        self.assertEqual(square, Q(42, 48841))
        self.assertEqual(lower, Q(48001, 48841))
        self.assertGreater(lower, Q(98, 100))
        self.assertEqual(path[0], 0)


if __name__ == "__main__":
    unittest.main()
