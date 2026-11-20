"""Reproducible exact/finite controls for wavefront theorem PR #674.

Finite tests do not prove the classical PNT, Karamata or pi-normality.
"""
import cmath
from fractions import Fraction
from math import exp, isqrt, log, pi, sqrt
import unittest


def primes(limit):
    f = bytearray(b'\x01') * (limit + 1)
    f[0:2] = b'\x00\x00'
    for p in range(2, isqrt(limit)+1):
        if f[p]:
            f[p*p:limit+1:p] = b'\x00' * len(f[p*p:limit+1:p])
    return [p for p in range(7, limit+1) if f[p]]


def history(N):
    return [(p, (p*p-1)//8) for p in primes(isqrt(8*N+1))]


def source(n, mutant=False):
    a=8*n-7
    q=(Fraction(4,a)-Fraction(2,a+3)-Fraction(1,a+4)-Fraction(1,a+5))
    return q + (Fraction(2,a*(a+1)*(a+2)) if mutant else 0)


def primary(q,p):
    b=q.denominator; power=1
    while b%p==0:
        b//=p; power*=p
    return Fraction((q.numerator*pow(b,-1,power))%power,power)


def cdf(N,u,beta):
    records=history(N)
    return (sum(p**beta for p,n in records if n<=u*N)
            /sum(p**beta for p,n in records))


class WavefrontClock(unittest.TestCase):
    def test_prime_square_source_marks(self):
        for p in primes(749):
            n=(p*p-1)//8
            self.assertEqual(8*n+1,p*p)
            self.assertEqual(primary(source(n+1),p),Fraction(4,p*p))
            self.assertEqual(primary(source(n+1,True),p),Fraction(5,p*p))

    def test_sieve_count_and_raw_profile(self):
        self.assertEqual(len(history(6)),1)
        self.assertLess(abs(cdf(50_000_000,.25,0)-.5),.08)

    def test_jacobian_weight_spurious_haar(self):
        self.assertLess(abs(cdf(50_000_000,.25,1)-.25),.06)
        self.assertLess(abs(cdf(50_000_000,.75,1)-.75),.06)

    def test_padicsquared_weight_biases_wavefront(self):
        self.assertLess(cdf(50_000_000,.5,4),.25)

    def test_fresnel_spectrum_finite_calibration(self):
        N=50_000_000; rec=history(N)
        estimate=sum(cmath.exp(2j*pi*n/N) for _,n in rec)/len(rec)
        m=10000
        fresnel=sum(cmath.exp(2j*pi*((j+.5)/m)**2) for j in range(m))/m
        self.assertLess(abs(estimate-fresnel),.08)

    def test_laplace_abelian_finite_calibration(self):
        s=1e-6
        L=sum(exp(-s*(p*p-1)/8) for p in primes(30_000))
        self.assertLess(abs(sqrt(s)*log(1/s)*L-sqrt(8*pi)),.25)

    def test_weak_stationary_moments(self):
        for alpha in (.5,1,1.5,2.5):
            for m in range(1,8):
                lhs=m*alpha/(m+alpha)
                rhs=alpha*(1-alpha/(m+alpha))
                self.assertAlmostEqual(lhs,rhs,places=13)

    def test_unamplified_mutant_spectrum_loses_marks(self):
        rec=history(20_000_000)
        gap=abs(sum((cmath.exp(2j*pi*5/p**2)-cmath.exp(2j*pi*4/p**2))
                    for p,_ in rec)/len(rec))
        upper=2*pi*sum(1/p**2 for p,_ in rec)/len(rec)
        self.assertLessEqual(gap,upper+1e-14)

    def test_short_memory_gate_not_global(self):
        B=10_000_000
        count=len(history(2*B))
        self.assertLess(count*log(B)/B,.01)
        self.assertGreater(count*sqrt(B)*log(B)/B,1.)


if __name__ == '__main__':
    unittest.main()
