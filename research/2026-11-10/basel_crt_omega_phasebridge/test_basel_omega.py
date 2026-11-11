#!/usr/bin/env python3
"""Exact Basel/CRT/Omega identities and thermal trace calibration."""
import math
import unittest
from fractions import Fraction
import mpmath as mp
import sympy as sp

def cycle_laplacian(M):
    L=sp.zeros(M)
    for i in range(M):
        L[i,i]+=2
        L[i,(i+1)%M]-=1
        L[i,(i-1)%M]-=1
    return L

def green_trace(M):
    J=sp.ones(M)/M
    return sp.trace((cycle_laplacian(M)+J).inv())-1

def B(first,last,p):
    R=sp.zeros(last-first+1)
    for start in range(p,last+1,p):
        if start<first or start+p-1>last: continue
        for n in range(start,start+p):
            for m in range(start,start+p):
                R[n-first,m-first]=sp.Rational(1,p)
    return R

def C(first,last):
    x,y=B(first,last,2),B(first,last,3)
    return x*y-y*x

def diag_weight(n):
    if n==1: return Fraction(0)
    if n in (2,3): return Fraction(1,12)
    if n in (4,5): return Fraction(1,18)
    return Fraction(1+int(n%6 in (2,3)),18)

class BaselTests(unittest.TestCase):
    def test_crt(self):
        for k in (1,2,3):
            M=6**k
            self.assertEqual(len({(n%2**k,n%3**k) for n in range(M)}),M)
    def test_multiplicative_2_3_residual(self):
        for n in range(1,1200):
            m,a,b=n,0,0
            while m%2==0: m//=2; a+=1
            while m%3==0: m//=3; b+=1
            self.assertEqual((2**a)*(3**b)*m,n)
            self.assertEqual(math.gcd(m,6),1)
    def test_cycle_green(self):
        for M in (6,12,18):
            self.assertEqual(green_trace(M),sp.Rational(M*M-1,12))
    def test_refinement_diamond(self):
        p=sp.Rational(-1,12)
        t2=lambda x:4*x+sp.Rational(1,4)
        t3=lambda x:9*x+sp.Rational(2,3)
        self.assertEqual(t2(p),p)
        self.assertEqual(t3(p),p)
        for x in (sp.S(0),sp.Rational(5,7)):
            self.assertEqual(t2(t3(x)),t3(t2(x)))
            self.assertEqual(t2(t3(x)),36*x+sp.Rational(35,12))
    def test_commutator_blocks(self):
        bulk,bdy=C(6,11),C(1,5)
        self.assertEqual(bulk.T,-bulk)
        self.assertEqual(bdy.T,-bdy)
        self.assertEqual(bulk**3,-sp.Rational(2,9)*bulk)
        la=sp.Symbol("lambda")
        self.assertEqual(sp.expand(bulk.charpoly(la).as_expr()-la**4*(la**2+sp.Rational(2,9))),0)
        self.assertEqual(sp.expand(bdy.charpoly(la).as_expr()-la**3*(la**2+sp.Rational(5,36))),0)
        self.assertEqual(list((-bulk**2).diagonal()),[sp.Rational(1,18),sp.Rational(1,18),sp.Rational(1,9),sp.Rational(1,9),sp.Rational(1,18),sp.Rational(1,18)])
        self.assertEqual(list((-bdy**2).diagonal()),[0,sp.Rational(1,12),sp.Rational(1,12),sp.Rational(1,18),sp.Rational(1,18)])
    def test_haar_energy(self):
        for p in (2,3,6):
            a=(1-sp.Rational(1,p*p))/12
            self.assertEqual(a/(1-sp.Rational(1,p*p)),sp.Rational(1,12))
    def test_thermal_symbolic(self):
        z,l=sp.symbols("z l")
        expr=(z+z/9+l/8+z/12)/18-sp.Rational(1,18)-sp.Rational(1,36)*(sp.Rational(1,4)+sp.Rational(1,9))
        self.assertEqual(sp.simplify(expr-(sp.Rational(43,648)*z+l/144-sp.Rational(85,1296))),0)
    def test_thermal_numerical_with_tail(self):
        mp.mp.dps=50
        z2=mp.zeta(2)
        l=(mp.polygamma(1,mp.mpf(1)/3)-mp.polygamma(1,mp.mpf(2)/3))/9
        pred=mp.mpf(43)/648*z2+l/144-mp.mpf(85)/1296
        N=24000
        obs=math.fsum(float(diag_weight(n))/(n*n) for n in range(1,N+1))
        self.assertTrue(0<float(pred)-obs<1/(9*N))
        self.assertAlmostEqual(float(pred/z2),0.02978469949560278,places=14)
    def test_archimedean_height_gap(self):
        for k in (2,4,8,16):
            n=1+6**k
            self.assertEqual(n%2**k,1)
            self.assertEqual(n%3**k,1)
            self.assertLess(Fraction(1,n*n),1)
if __name__=="__main__":
    unittest.main(verbosity=2)
