"""Sharp Fourier discrimination scale for authentic BBP carry shrinking targets.

Exact arithmetic for source/bandwidth/grade, independent numerical tests only
for Fejer sine pulse. Source-specific information bounds, NOT pi normality.
"""
from fractions import Fraction as F
from math import pi
import unittest
import mpmath as mp


def forcing(n):
    a=8*n-7
    return F(6,a*(a+3))+F(4,a*(a+4))+F(5,a*(a+5))

def exact_bandwidth(n):
    r=forcing(n)
    if n<3: raise ValueError("source index n>=3")
    # Smallest positive integer M with M*r>=4.
    return (4*r.denominator+r.numerator-1)//r.numerator

def grade(n):
    L=0
    while 16**(L+1)<=n*n:L+=1
    return L

def grade_weight(j):return F(j+1,2**(j+2))

class ResolutionTests(unittest.TestCase):
    def test_original_source_bandwidth_scaling(self):
        for n in (3,4,8,16,32,64,128,256,1024):
            r=forcing(n)
            M=exact_bandwidth(n)
            self.assertGreaterEqual(M*r,4)
            self.assertLess((M-1)*r,4)
            self.assertGreater(M,4*n*n)
            self.assertLess(r,F(1,2*n*n))

    def test_oily_moving_grade_bounds(self):
        for n in (3,4,8,16,32,64,128,256,1024):
            L=grade(n)
            w=grade_weight(L)
            # Squaring eliminates any floating-point sqrt(n).
            self.assertGreaterEqual(16**L,F(n*n,16))
            self.assertLessEqual(16**L,n*n)
            self.assertGreaterEqual(16*n*w*w,(L+1)**2)
            self.assertLess(4*n*w*w,(L+1)**2)

    def test_fejer_two_point_sep(self):
        mp.mp.dps=80
        for n in (3,8,16,32,64,256):
            r=forcing(n);M=exact_bandwidth(n)
            delta=mp.mpf(r.numerator)/(2*r.denominator)
            val=(mp.sin(mp.pi*M*delta)/(M*mp.sin(mp.pi*delta)))**2
            self.assertLess(val,mp.mpf(1)/16)

    def test_frequency_lower_bound(self):
        # Bernstein implies H>=1/(2pi r)>n²/pi; test strict source inputs.
        for n in range(3,140):
            self.assertGreater(F(1,2*forcing(n)),F(n*n))

if __name__=='__main__':unittest.main(verbosity=2)
