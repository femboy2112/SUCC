"""Exact radix-twisted transport and numerical reciprocal-clock calibration.

No imported π digits, no Haar samples, no altered BBP source contract.
Source-selected all-time results are proved in RECIPROCAL_CLOCK.md; finite
floating checks are observations, not proofs of limiting cancellations.
"""
from __future__ import annotations
from fractions import Fraction as Q
import cmath,math,unittest

RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))

def source(n):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(RAD,1)),Q())

def states(n):
    z=[Q(0)]
    for k in range(1,n+1):
        z.append(16*z[-1]+source(k))
    return z

def stable_lag(n,ell,depth=23):
    d=0.
    for m in range(1,depth+1):
        s=0.
        for j,c in enumerate(RAD,1):
            if c:
                k=8*(n+m-1)+j
                s+=float(c)/(k*(k+8*ell))
        d+=(8*ell/16.**m)*s
    return d

def e(x):return cmath.exp(2j*math.pi*x)

def weight(x):return 8/(3*x**3)

def weighted(A,q,ell=1):
    H=int(q*A*A)
    return sum((weight(n/A)*e((H*stable_lag(n,ell))%1)
                for n in range(A,2*A)),0j)/A

def uniform(A,q,ell=1):
    H=int(q*A*A)
    return sum((e((H*stable_lag(n,ell))%1)
                for n in range(A,2*A)),0j)/A

def exact_sinc(q,ell):
    t=3*math.pi*ell*q/128
    return e(-5*ell*q/256)*(math.sin(t)/t if t else 1)

def link(z,n,m,h):
    return h*(z[m]-16**(m-n)*z[n])

class ReciprocalClock(unittest.TestCase):
    def test_01_normalized_jacobian_and_root_of_unity_endpoints(self):
        self.assertEqual(Q(4,3)*(Q(1)-Q(1,4)),Q(1))
        for ell in (1,2,3,-1):
            for k in (1,2,5):
                q=128*k
                self.assertEqual(Q(-ell*q,32)%1,0)
                self.assertEqual(Q(-ell*q,128)%1,0)
                self.assertEqual(Q(3*ell*q,128).denominator,1)

    def test_02_exact_twisted_radix_transport(self):
        z=states(80)
        for n,m,k in ((0,1,5),(1,3,7),(3,17,53),(7,38,79)):
            for h in (1,3,17):
                self.assertEqual(link(z,n,k,h),
                    link(z,m,k,h)+link(z,n,m,16**(k-m)*h))
                self.assertEqual(link(z,n,m,h),
                    h*sum((16**(m-j)*source(j)
                           for j in range(n+1,m+1)),Q(0)))

    def test_03_naive_untransported_frequency_fails(self):
        z=states(16)
        n,m,k,h=1,3,7,3
        wrong=link(z,m,k,h)+link(z,n,m,h)
        self.assertNotEqual((wrong-link(z,n,k,h))%1,0)

    def test_04_tuned_reciprocal_observer_zero_finite_checks(self):
        for A in (307,953,1901):
            for ell in (1,2):
                for q in (128,256):
                    # All theoretical continuum integrals are exactly zero.
                    self.assertLess(abs(weighted(A,q,ell)),4*ell/A)

    def test_05_weighted_sinc_nonzero_and_finite_error(self):
        for A in (307,953,1901):
            for ell in (1,2):
                for q in (32,64):
                    self.assertLess(abs(weighted(A,q,ell)-exact_sinc(q,ell)),
                                    4*ell/A)

    def test_06_sharp_clock_and_jacobian_clock_differ(self):
        A,q=1901,128
        self.assertGreater(abs(uniform(A,q)),.12)
        self.assertLess(abs(weighted(A,q)),.001)
        self.assertGreater(abs(uniform(A,q))/abs(weighted(A,q)),100)

    def test_07_rational_source_zero_seed_not_haarlike(self):
        z=states(150)
        for n in range(1,150):
            self.assertGreater(z[n],0)
            self.assertLess(z[n],Q(1,32*n+16))

if __name__=="__main__":unittest.main()
