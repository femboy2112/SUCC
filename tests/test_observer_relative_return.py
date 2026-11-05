"""Independent exact and numerical tests for two-clock BBP radial return.

This module uses only stdlib and authentic original source taps. Numerical
finite values calibrate already-derived paper statements; they are not proof.
"""
from __future__ import annotations
from fractions import Fraction as Q
import cmath
import math
import unittest

RAD=(Q(2),Q(-2),Q(-1),Q(-2),Q(-1,2),Q(-1,2),Q(1,4),Q(0))
ANG=(Q(2),Q(2),Q(1),Q(0),Q(-1,2),Q(-1,2),Q(-1,4),Q(0))
ORIG=(Q(4),Q(0),Q(0),Q(-2),Q(-1),Q(-1),Q(0),Q(0))

def r(n,w=RAD):
    return sum((c/Q(8*(n-1)+j) for j,c in enumerate(w,1)),Q(0))

def state_prefix(n,w):
    states=[Q(0)]
    for j in range(1,n+1):
        states.append(16*states[-1]+r(j,w))
    return states

def stable_exact_lag(n,ell,depth=48):
    """Difference of two radial FUTURE tails, without π or state subtraction."""
    total=Q(0)
    for m in range(1,depth+1):
        z=Q(0)
        for j,c in enumerate(RAD,1):
            if c:
                d=8*(n+m-1)+j
                z+=c/Q(d*(d+8*ell))
        total+=Q(8*ell,16**m)*z
    return total

def stable_float_lag(n,ell,depth=23):
    total=0.
    for m in range(1,depth+1):
        s=0.
        for j,c in enumerate(RAD,1):
            if c:
                d=8*(n+m-1)+j
                s+=float(c)/(d*(d+8*ell))
        total+=(8*ell/16.**m)*s
    return total

def e(x):
    return cmath.exp(2j*math.pi*x)

def sharp(A,q,ell=1):
    H=int(q*A*A)
    return sum((e((H*stable_float_lag(n,ell))%1) for n in range(A,2*A)),0j)/A

def endpoint(q,ell=1):
    return 8/(math.pi*1j*ell*q)*(8*e(-ell*q/128)-e(-ell*q/32))

def continuum(q,ell=1,steps=2048):
    """Composite Simpson, different from the discrete source-tail oracle."""
    def f(j):
        x=1+j/steps
        return e(-ell*q/(32*x*x))
    total=f(0)+f(steps)
    for j in range(1,steps):
        total+=(4 if j%2 else 2)*f(j)
    return total/(3*steps)

def bump(x):
    if x<=1 or x>=2:
        return 0.
    s=(x-1)*(2-x)
    return math.exp(4-1/s)

def smooth(A,q,ell=1):
    H=int(q*A*A)
    return sum((bump(n/A)*e((H*stable_float_lag(n,ell))%1)
                for n in range(A,2*A)),0j)/A

class ObserverRelativeReturn(unittest.TestCase):
    def test_01_literal_source_preserved(self):
        self.assertEqual(tuple(a+z for a,z in zip(ANG,RAD)),ORIG)
        self.assertEqual(r(1,RAD),Q(2,105))
        for n in range(2,250):
            self.assertLess(r(n,RAD),0)

    def test_02_exact_lag_repayment_for_two_clock_times(self):
        states=state_prefix(116,RAD)
        for ell in (1,2,5):
            for n in (1,2,17,53,101):
                rhs=16**ell*states[n]+sum(
                    (16**(ell-j)*r(n+j,RAD) for j in range(1,ell+1)),Q(0))
                self.assertEqual(rhs,states[n+ell])
                self.assertLess(states[n+ell],states[n])

    def test_03_independent_future_tail_difference(self):
        states=state_prefix(115,RAD)
        for ell in (1,2,5):
            for n in (1,17,53,101):
                exact=states[n+ell]-states[n]
                self.assertLess(abs(exact-stable_exact_lag(n,ell)),Q(1,10**42))

    def test_04_exact_flat_transport_and_integer_carry(self):
        states=state_prefix(90,RAD)
        for H in (1,3,17,1024):
            for n,m,k in ((0,1,9),(3,17,53),(7,49,89)):
                a=H*(states[m]-states[n])
                b=H*(states[k]-states[m])
                c=H*(states[k]-states[n])
                self.assertEqual(a+b,c)
                self.assertEqual((a+b)%1,c%1)

    def test_05_nonzero_seed_can_be_phase_invisible_to_finite_clock(self):
        # 16^n/5 = 1/5 mod1: this is seed ambiguity, not a nonnormality proof.
        s=Q(1,5)
        for n in (0,1,2,7,21,65):
            self.assertEqual((16**n*s)%1,s)
        # A 1/5 seed adds a constant circle rotation, and hence cancels
        # EXACTLY in all lag characters (though it changes the initial seed).
        states=state_prefix(22,RAD)
        for n in (1,5,15):
            raw=(states[n+1]+16**(n+1)*s)-(states[n]+16**n*s)
            self.assertEqual((raw-(states[n+1]-states[n]))%1,0)
            self.assertNotEqual(raw,states[n+1]-states[n])

    def test_06_two_independent_numerical_lag_oracles(self):
        for ell in (1,2):
            for n in (307,953,1901,4099):
                self.assertLess(abs(float(stable_exact_lag(n,ell,depth=38))-
                                    stable_float_lag(n,ell)),1e-12)

    def test_07_continuum_correspondence_declared_finite_cases(self):
        for A in (307,953,1901):
            for q in (16,32,64):
                self.assertLess(abs(sharp(A,q)-continuum(q)),5/A)

    def test_08_sharp_endpoint_analytic_order_calibration(self):
        for A in (1901,8191):
            for q in (64,256,1024):
                c=sharp(A,q)
                main=endpoint(q)
                self.assertLess(abs(c-main),600/q**2+0.5*q/A)
            self.assertGreater(1024*abs(sharp(A,1024)),15)

    def test_09_smooth_window_does_not_certify_sharp_window(self):
        A=1901
        vals={q:abs(smooth(A,q)) for q in (256,512,1024)}
        self.assertLess(vals[256],.012)
        self.assertLess(vals[512],.0012)
        self.assertLess(vals[1024],.0001)
        self.assertGreater(abs(sharp(A,1024)),.015)
        self.assertLess(vals[1024],abs(sharp(A,1024))/100)

if __name__=="__main__":
    unittest.main()
