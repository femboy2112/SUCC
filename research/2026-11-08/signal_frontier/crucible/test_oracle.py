import unittest
from fractions import Fraction as F
import oracle as o


class SourceCalibration(unittest.TestCase):
    def test_integer_jet_and_uncancelled_routes(self):
        self.assertEqual(o.coefficients(6),[1,2,4,10,25,60,144])
        self.assertEqual(o.coefficients(24),o.coefficients_uncancelled(24))

    def test_beta_by_independent_monomial_integration(self):
        from math import comb
        for n in (2,9,57):
            for k in range(1,9):
                monomials=sum((F((-1)**j*comb(k-1,j),n+j) for j in range(k)),F())
                self.assertEqual(o.beta(n,k),monomials)

    def test_source_kernel_polynomial_identity(self):
        q=(4,4,4,2,1)
        d=(4,-4,0,2,-1)  # (2-x^2)(x^2-2x+2)
        product=[0]*9
        for i,x in enumerate(q):
            for j,y in enumerate(d):
                product[i+j]+=x*y
        self.assertEqual(product,[16,0,0,0,0,0,0,0,-1])

    def test_first_orders_have_declared_polarity(self):
        for n in (1,17,211):
            lo,hi=o.tail_interval(n)
            a0,_=o.approximation(n,0)
            a1,_=o.approximation(n,1)
            self.assertLess(a1,lo)
            self.assertLess(hi,a0)

    def test_lag_gain_requires_actual_difference(self):
        n=37
        lo,hi=o.tail_interval(n)
        later=o.tail_interval(n+1)
        self.assertLess(hi-later[0],F(1,32*n**3))
        # Single phase has n^-2 scale and cannot borrow the n^-3 lag bound.
        self.assertGreater(lo,F(1,32*n**3))

    def test_invalid_domains(self):
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError):
                o.tail_interval(n)
        with self.assertRaises(ValueError):
            o.approximation(1,-2)

    def test_protocol_cases(self):
        result=o.run()
        self.assertEqual(result["point_checks"],56)
        self.assertEqual(result["lag_checks"],280)
        self.assertEqual(result["mutation_checks"],3)


if __name__=="__main__":
    unittest.main()
