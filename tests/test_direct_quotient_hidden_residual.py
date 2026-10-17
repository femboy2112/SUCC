"""Exact polynomial countermodel to endpoint-only observation (no SymPy needed)."""
import unittest
from fractions import Fraction as F
from observational_succ.direct_quotient_schur import certified_projector_first_upper


def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out


def integrate(a):
    return sum((x*(F(1,2)**(i+1)-F(-1,2)**(i+1))/F(i+1) for i,x in enumerate(a)),F(0))


def poly_eval(a,x): return sum((v*x**i for i,v in enumerate(a)),F(0))


class HighResidualWitness(unittest.TestCase):
    # P5(2t)-P7(2t), exact rational coefficients.
    h=(F(0),F(65,8),F(0),F(-455,2),F(0),F(1638),F(0),F(-3432))
    hp=tuple((j+1)*v for j,v in enumerate(h[1:]))
    hpp=tuple((j+1)*v for j,v in enumerate(hp[1:]))

    def test_endpoint_moments_invisible_but_energy_52(self):
        self.assertEqual(poly_eval(self.h,F(1,2)),0)
        self.assertEqual(poly_eval(self.h,F(-1,2)),0)
        for k in range(4):
            self.assertEqual(integrate([F(0)]*k+list(self.hp)),0)
        self.assertEqual(integrate(multiply(self.hp,self.hp)),52)

    def test_projector_first_error_valid_on_hidden_high_mode(self):
        # |h''(t)| <= sum|coeff|*2^-degree=9282 on [-1/2,1/2].
        L=sum((abs(v)*F(1,2)**k for k,v in enumerate(self.hpp)),F(0))
        self.assertEqual(L,9282)
        grid=8
        positive=[((poly_eval(self.hp,F(2*q+1,2*grid)),)*2,
                   (F(0),F(0)),(F(0),F(0)),(F(0),F(0)))
                  for q in range(grid//2)]
        r=certified_projector_first_upper(positive,(L,0,0,0),(0,0,0,0))
        self.assertGreaterEqual(r['quotient_loewner_upper'][0][0],F(52))
        self.assertFalse(r['analytic_premises_authenticated'])


if __name__=='__main__': unittest.main()
