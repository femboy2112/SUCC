"""Calibration of the source-only angular response at the radial moment zero.
The sign theorem is analytic; numerical quadrature is not a proof certificate
and is NOT a test of pi's base-16 Weyl orbit.
"""
import unittest
from fractions import Fraction as Q
import sympy as sp
import mpmath as mp

RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def radial_t(t):
    return -sum(mp.mpf(w.numerator)/w.denominator*t**j for j,w in enumerate(RAD))/(16-t**8)

def radial_moment(n,k):
    result=mp.mpf(0)
    for j,w in enumerate(RAD,1):
        if not w: continue
        x=mp.mpf(n)+mp.mpf(j)/8
        B=mp.beta(x,k+1)
        for m in range(1,61):
            result -= mp.mpf(w.numerator)/w.denominator*B/(8*16**m)
            B*=x/(x+k+1)
            x+=1
    return result

def angular_imag_beta(n,k,q=1):
    def integrand(u):
        t=u**mp.mpf('0.125')
        angle=mp.atan(t-1)+mp.pi/8
        return u**(n-mp.mpf(7)/8)*(1-u)**k*radial_t(t)*mp.sin(q*angle)/8
    tau=2-mp.sqrt(2)
    cuts=[mp.mpf('0'),mp.mpf('.002'),mp.mpf('.005'),mp.mpf('.01'),tau**8,mp.mpf('.02'),mp.mpf('.04'),mp.mpf('.1'),mp.mpf(1)]
    return mp.quad(integrand,cuts)/(mp.beta(n+mp.mpf(1)/8,k+1)/8)

class AngularResponse(unittest.TestCase):
    def test_01_exact_source_mixed_constant(self):
        root=2-sp.sqrt(2)
        sigma=1-root**8
        u0=root**8
        x=sp.symbols('x')
        p=sum(sp.Rational(w.numerator,w.denominator)*x**j for j,w in enumerate(RAD))
        cp=sp.simplify(-sp.diff(p,x).subs(x,root)*sigma*root/(128*(16-u0)))
        self.assertEqual(cp,(3825*sp.sqrt(2)-5406)/2048)
        self.assertGreater(float(cp),0)
        self.assertAlmostEqual(float(cp),.00164398245951589925,places=13)
        self.assertEqual(sp.simplify((root-1)**2+1),2*root)

    def test_02_angular_monotonicity_and_signed_support(self):
        # Source radial density changes sign at tau, and angular coordinate
        # theta=atan(t-1)+pi/4 has positive derivative everywhere [0,1].
        x=sp.symbols('x')
        p=sum(sp.Rational(w.numerator,w.denominator)*x**j for j,w in enumerate(RAD))
        g=sp.factor(p)
        self.assertEqual(sp.rem(g,x*x-4*x+2,domain=sp.QQ),0)
        self.assertGreater(float(p.subs(x,sp.Rational(1,2))),0)
        self.assertLess(float(p.subs(x,sp.Rational(3,4))),0)

    def test_03_numerical_root_n5(self):
        mp.mp.dps=65
        k=mp.findroot(lambda z:radial_moment(5,z),(mp.mpf(335),mp.mpf(342)))
        self.assertGreater(k,338)
        self.assertLess(k,339)
        self.assertLess(abs(radial_moment(5,k)),mp.mpf('1e-40'))
        resp=angular_imag_beta(5,k)
        self.assertGreater(resp,0)
        expected=(3825*mp.sqrt(2)-5406)/2048
        self.assertLess(abs(5*resp/expected-1),mp.mpf('.05'))

    def test_04_numerical_root_n10(self):
        mp.mp.dps=65
        k=mp.findroot(lambda z:radial_moment(10,z),(mp.mpf(690),mp.mpf(697)))
        self.assertGreater(k,693)
        self.assertLess(k,695)
        self.assertLess(abs(radial_moment(10,k)),mp.mpf('1e-40'))
        resp=angular_imag_beta(10,k)
        self.assertGreater(resp,0)
        expected=(3825*mp.sqrt(2)-5406)/2048
        self.assertLess(abs(10*resp/expected-1),mp.mpf('.03'))

if __name__=='__main__':unittest.main()
