import unittest
from fractions import Fraction as Q
import probe as p


class ObserverSymbolTests(unittest.TestCase):
    def test_independent_recurrence_laurent_coefficients(self):
        self.assertEqual(p.radial_coefficients(4)[1:],
                         (Q(1,32), -Q(5,256), Q(27,2048), -Q(209,16384)))

    def test_fresh_exact_receipt(self):
        receipt = p.receipt()
        self.assertEqual(len(receipt["observer_rows"]), 3)
        self.assertEqual(len(receipt["source_rows"]), 3)

    def test_endpoint_operator_constants_are_attained(self):
        for A in (1, 7, 13):
            for index in (0, A-1):
                points = [(Q(0), Q(0)) for _ in range(A)]
                points[index] = (Q(1), Q(0))
                weight = Q(8*A**3, 3*(A+index)**3)
                weighted = [(weight*x, weight*y) for x,y in points]
                self.assertEqual(p.maximal_squared(weighted), weight**2*p.maximal_squared(points))

    def test_full_weighted_zero_does_not_zero_maximal_norm(self):
        A = 2
        w0, w1 = Q(8,3), Q(8*A**3,3*(A+1)**3)
        points = [(w1/w0,Q(0)),(-Q(1),Q(0))]
        weighted = [(w0*points[0][0],Q(0)),(w1*points[1][0],Q(0))]
        self.assertEqual(sum(x for x,y in weighted), 0)
        self.assertGreater(p.maximal_squared(weighted), 0)
        self.assertGreater(p.maximal_squared(points), 0)

    def test_radial_source_zero_and_original_positive_factorization(self):
        self.assertEqual(p.polynomial_remainder(p.RADIAL[:-1], (2,-4,1)), ())
        self.assertNotEqual(p.polynomial_remainder(p.ORIGINAL[:-1], (2,-4,1)), ())
        B = [Q(4),Q(4),Q(4),Q(2),Q(1)]
        product = B+[Q(0)]
        for j,c in enumerate(B):
            product[j+1] -= c
        self.assertEqual(tuple(product), p.ORIGINAL[:6])

    def test_coherent_integer_lag_never_removes_leading_chirp(self):
        for ell in range(-20,21):
            coefficient = Q(1,64)+Q(ell,32)
            self.assertNotEqual(coefficient, 0)
            self.assertEqual(1/(2*abs(coefficient)), Q(32,abs(2*ell+1)))


if __name__ == "__main__":
    unittest.main()
