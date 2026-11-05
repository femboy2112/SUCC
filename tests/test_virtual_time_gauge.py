"""Calibrate exact BBP source gauge and Fourier scale crossover.

Numerical checks of a separately proved asymptotic are NOT asymptotic proofs.
"""
from fractions import Fraction as Q
from math import cos, sin, pi
import unittest

ANG=(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
P=tuple(a+r for a,r in zip(ANG,RAD))

def r(n,w):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(w,1)),Q())

def tail(x):
    return -sum(16.0**(-m)*sum(float(c)/(8*(x+m-1)+j)
                    for j,c in enumerate(RAD,1)) for m in range(1,24))

def e(x): return complex(cos(2*pi*x),sin(2*pi*x))
def avg(A,H): return sum((e(H*tail(n)) for n in range(A,2*A)),0j)/A
def crossover(tau,steps=4096):
    return sum((e(tau/(32*(1+(j+.5)/steps))) for j in range(steps)),0j)/steps

class TimeGauge(unittest.TestCase):
    def test_01_conjugacy_exact_source_fractions(self):
        z=Q()
        for n in range(1,181):
            nz=16*z+r(n,RAD)
            for x in (Q(0),Q(1,5),Q(-3,7)):
                left=16*x+r(n,ANG)+nz
                right=16*(x+z)+r(n,P)
                self.assertEqual(left,right)
            z=nz
            self.assertGreater(z,0)
            self.assertLess(z,Q(1,32*n+16))

    def test_02_pointwise_small_gauge_at_fixed_frequency(self):
        for A in (128,256,512):
            for n in (A,3*A//2,2*A-1):
                self.assertLess(tail(n),1/(32*n+16))
                self.assertGreater(tail(n),0)

    def test_03_linear_observer_frequency_crossover(self):
        tau=32
        integral=crossover(tau)
        for A in (256,512,1024):
            self.assertLess(abs(avg(A,tau*A)-integral),.005)

    def test_04_quadratic_observer_frequency_cancellation_calibration(self):
        for A in (256,512,1024):
            self.assertLess(abs(avg(A,A*A)),.1)

if __name__=='__main__': unittest.main()
