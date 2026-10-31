"""Independently verify source-derived Gamma/Golden/Euler 2D Fourier surfaces.
Research-only; auxiliary observation model, no pi digit normality.
"""
import unittest
from math import comb, factorial
import sympy as s

z,w,t=s.symbols('z w t')
lam=(s.sqrt(5)-1)/2

def H(zv,wv):
    return 1/(3-zv-wv)**2

def M(sv,zv,wv):
    return 3**sv*s.gamma(sv+2)/(3-zv-wv)**(sv+2)

def D(zv,wv):
    d=3-zv-wv
    return (1-s.EulerGamma+s.log(3)-s.log(d))/d**2-lam**2/(3-lam*zv-lam*wv)**2

def mass(j,k):
    return s.Rational((j+k+1)*comb(j+k,j),3**(j+k+2))

def contrast(j,k):
    return s.harmonic(j+k+1)-s.EulerGamma-lam**(j+k+2)

class GammaSurface(unittest.TestCase):
    def test_conditional_gamma_rank(self):
        for j in range(5):
            for k in range(5):
                # integrate exact gamma--Poisson joint density over y
                v=s.integrate(t**(j+k+1)*s.exp(-3*t)/(factorial(j)*factorial(k)),(t,0,s.oo))
                self.assertEqual(v,mass(j,k))

    def test_shared_mellin_and_harmonic(self):
        for j,k in [(0,0),(1,0),(1,1),(2,3)]:
            weight=mass(j,k)
            # conditional Z=3Y has Gamma(j+k+2, rate 1)
            Elog=s.digamma(j+k+2)
            self.assertEqual(s.simplify(Elog-(s.harmonic(j+k+1)-s.EulerGamma)),0)
            self.assertEqual(s.simplify((1+lam)**(-(j+k+2))-lam**(j+k+2)),0)
            self.assertTrue(weight>0)

    def test_bivariate_mellin_derivative(self):
        J=s.diff(M(t,z,w),t).subs(t,0)
        ans=(1-s.EulerGamma+s.log(3)-s.log(3-z-w))/(3-z-w)**2
        self.assertEqual(s.simplify(J-ans),0)

    def test_bivariate_golden_laplace(self):
        self.assertEqual(s.simplify(1/(3+3*lam-z-w)**2-lam**2/(3-lam*z-lam*w)**2),0)

    def test_origin_oily_marc(self):
        self.assertEqual(s.simplify(D(0,0)-(lam-s.EulerGamma)/9),0)

    def test_fourier_coefficients(self):
        for j,k in [(0,0),(0,1),(1,0),(1,1),(2,2),(1,3)]:
            deriv=s.diff(D(z,w),z,j,w,k).subs({z:0,w:0})/(factorial(j)*factorial(k))
            target=mass(j,k)*contrast(j,k)
            self.assertEqual(s.simplify(deriv-target),0)

    def test_clock_split_preserves_golden(self):
        zz=s.symbols('zz')
        expr=4/(4-2*zz)**2
        self.assertEqual(s.simplify(expr-1/(2-zz)**2),0)
        self.assertEqual(s.simplify(expr.subs(zz,lam**2)-lam**2),0)

    def test_fourier_surface_margins(self):
        self.assertEqual(s.simplify(H(z,1)-1/(2-z)**2),0)
        self.assertEqual(s.simplify(H(1,w)-1/(2-w)**2),0)
        self.assertEqual(s.simplify(H(s.Integer(1),s.Integer(1))),1)

if __name__=='__main__':unittest.main(verbosity=2)
