"""Finite Pascal--Gamma negative-integer tangent tests; no pi normality claims."""
import unittest
from math import comb
import mpmath as mp
mp.mp.dps = 115

def difference(n, m):
    return mp.fsum((-1)**j*comb(n,j)*mp.mpf(j+1)**m*mp.log(j+1) for j in range(n+1))

def integral(n, m):
    assert n>m>=0
    f=lambda t:mp.exp(-t)*(-mp.expm1(-t))**n/t**(m+1) if t else mp.mpf(n==m+1)
    return mp.quad(f,[0,1,5,mp.inf])

def ratio_pascal(m,M):
    eta=mp.altzeta(-m)
    assert m%2==1
    return (mp.power(2,m+1)*mp.log(2)/(mp.power(2,m+1)-1)
        -mp.fsum(difference(n,m)/mp.power(2,n+1) for n in range(M+1))/eta)

class AllNegativeIntegers(unittest.TestCase):
 def test_values_truncate_at_grade_m(self):
    for m in range(0,8):
        for n in range(m+1,m+8):
            self.assertEqual(sum((-1)**j*comb(n,j)*(j+1)**m for j in range(n+1)),0)
 def test_derivative_sign_for_high_grades(self):
    for m in (0,1,2,3,5,7):
        for n in (m+1,m+2,m+4):
            a=difference(n,m)
            self.assertGreater((-1)**(m+1)*a,0)
 def test_mellin_integral_for_every_parity(self):
    for m in (0,1,2,3,5,7):
        for n in (m+1,m+3):
            predicted=(-1)**(m+1)*mp.factorial(m)*integral(n,m)
            self.assertLess(abs(predicted-difference(n,m)),mp.mpf('1e-99'))
 def test_monotone_tangent_bounds(self):
    for m in (0,1,2,3,5,7):
        self.assertGreater(integral(m+1,m),integral(m+3,m))
 def test_odd_reflected_prime_weight_identity(self):
    for m in (1,3,5,7):
        lhs=mp.diff(mp.zeta,-m)/mp.zeta(-m)
        rhs=mp.log(2*mp.pi)+mp.euler-mp.harmonic(m)-mp.diff(mp.zeta,m+1)/mp.zeta(m+1)
        self.assertLess(abs(lhs-rhs),mp.mpf('1e-99'))
 def test_odd_pascal_quantified_tail(self):
    for m in (1,3,5,7):
        M=48
        pred=ratio_pascal(m,M)
        actual=mp.diff(mp.zeta,-m)/mp.zeta(-m)
        bound=mp.factorial(m)*integral(m+1,m)/(abs(mp.altzeta(-m))*mp.power(2,M+1))
        self.assertLess(abs(pred-actual),bound)
 def test_even_trivial_zero_tangent_prime_product(self):
    for k in (1,2,3,4):
        m=2*k
        self.assertEqual(mp.zeta(-m),0)
        predicted=(-1)**k*mp.factorial(m)/(2*(2*mp.pi)**m)*mp.zeta(m+1)
        self.assertLess(abs(mp.diff(mp.zeta,-m)-predicted),mp.mpf('1e-95'))
 def test_even_pascal_gradient_regulator(self):
    for m in (2,4,6):
        M=50
        deriv=-mp.fsum(difference(n,m)/mp.power(2,n+1) for n in range(M+1))
        target=(1-mp.power(2,m+1))*mp.diff(mp.zeta,-m)
        bound=mp.factorial(m)*integral(m+1,m)/mp.power(2,M+1)
        self.assertLess(abs(deriv-target),bound)

if __name__ == '__main__':unittest.main()
