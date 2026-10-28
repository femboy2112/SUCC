"""Different arithmetic evaluation of exactly the same Taylor polynomials."""
from fractions import Fraction as Q
from math import factorial
import unittest
from observational_succ.chiral_target_descent import _taylor_pair


class IntegerHornerAgreement(unittest.TestCase):
    def test_matches_original_rational_taylor(self):
        for angle in (Q(0), Q(1, 7), Q(-4, 3), Q(22, 7),
                      Q(1234567890123456789, 2**59)):
            for terms in (2, 3, 9, 18, 24):
                cosine = sum(((-1)**k * angle**(2*k)/factorial(2*k)
                              for k in range(terms)), Q(0))
                sine = sum(((-1)**k * angle**(2*k+1)/factorial(2*k+1)
                            for k in range(terms)), Q(0))
                self.assertEqual(_taylor_pair(angle, terms), (cosine, sine))


if __name__ == '__main__':
    unittest.main()
