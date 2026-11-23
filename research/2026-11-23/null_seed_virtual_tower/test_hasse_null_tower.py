"""Exact finite Hasse-jet null information and p-adic / Archimedean calibration."""
from math import factorial
from fractions import Fraction
import unittest


class HasseNullTests(unittest.TestCase):
    def test_factorial_blindness_in_residue_fields(self):
        # F(z)=z^p. Ordinary order-p derivative is p!, zero modulo p;
        # its Hasse order-p derivative is the unit coefficient 1.
        for p in (2, 3, 5, 7):
            ordinary = factorial(p)
            hasse = 1
            self.assertEqual(ordinary % p, 0)
            self.assertNotEqual(hasse % p, 0)

    def test_scale_and_prime_height_compose_exactly(self):
        # Base-16 root scales 16^-1,16^-2,16^-3 and p^m null coefficient
        # make the same integer polynomial nonzero and arithmetically huge.
        b, p, m, depth = 16, 3, 4, 3
        coeff = [0, p**m]
        for j in range(1, depth+1):
            nxt = [0]*(len(coeff)+1)
            for idx, a in enumerate(coeff):
                nxt[idx] += a
                nxt[idx+1] -= b**j*a
            coeff = nxt
        height = p**m*b**(depth*(depth+1)//2)
        self.assertEqual(abs(coeff[-1]), height)
        self.assertTrue(all(a % p**m == 0 for a in coeff))
        self.assertEqual(coeff[1], p**m)
        for j in range(1,depth+1):
            t = Fraction(1,b**j)
            self.assertEqual(sum(a*t**k for k,a in enumerate(coeff)),0)
        self.assertGreaterEqual(sum(map(abs, coeff)), height)


if __name__ == '__main__':
    unittest.main()
