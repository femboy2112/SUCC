"""Exact checks of reassembled local Pisot/BBP source fingerprints.

This does not claim independent origin, transcendence, or π normality.
"""
import unittest
from fractions import Fraction as F
from math import comb

class PisotFixedPointControls(unittest.TestCase):
    def test_source_and_symmetric_exact(self):
        for j in range(0,41):
            x=F(j,40);delta=1-x
            if x==1:continue
            R=delta/((2-x*x)*(x*x-2*x+2))
            sym=delta/(2-x)**2
            h=x*delta/(2-x)
            self.assertEqual(R,sym/(1-h*h))
            for M in range(3):
                approx=sym*sum((h**(2*i) for i in range(M+1)),F(0))
                self.assertEqual(R-approx,R*h**(2*M+2))
                self.assertGreaterEqual(R-approx,0)

    def test_endpoint_grade_law(self):
        for j in range(15):
            w=F(j+1,2**(j+2))
            self.assertGreater(w,0)
        self.assertEqual(sum((F(j+1,2**(j+2)) for j in range(16)), F(0)),F(1)-F(18,2**17))

    def test_original_pi_packet_ratio(self):
        a=F(2)
        for j in range(36):
            self.assertEqual(a,F(2**(j+1),(2*j+1)*comb(2*j,j)))
            a=a*F(j+1,2*j+3)

    def test_pisot_quadratic_pell_trace(self):
        from observational_succ.pisot_hopf_arithmetic_relativity import (
            pisot_quadratic_coefficients,pisot_quadratic_trace)
        for m in (1,2,5):
            for n in range(2,35):
                a,b=pisot_quadratic_coefficients(m,n)
                self.assertEqual(a,m*pisot_quadratic_coefficients(m,n-1)[0]
                                 +pisot_quadratic_coefficients(m,n-1)[1])
                self.assertEqual(pisot_quadratic_trace(m,n),m*pisot_quadratic_trace(m,n-1)
                                 +pisot_quadratic_trace(m,n-2))

if __name__=='__main__':unittest.main()
