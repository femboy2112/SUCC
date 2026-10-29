"""Research-only SUCC primitive-totient Pasadena/Pascal–Gamma algebra checks.

Run from repository checkout:
  python research/2026-10-29/totient_pascal_gamma/primitive_source_probe.py

Imports only the pinned ancestor PR #370 Pascal source. This is a short
reauthored remote probe. The full separately validated 13-test suite
and SymPy/mpmath controls are supplied in the companion research bundle.
No pi-normality or mathematical theorem is inferred from finite tests.
"""
from __future__ import annotations

from fractions import Fraction as F
from math import comb, gcd
from pathlib import Path
import runpy
import unittest

parent = Path(__file__).resolve().parents[1] / "pascal_oily_bbp" / "pascal_oily_probe.py"
ancestor = runpy.run_path(str(parent))
forcing = ancestor["forcing"]
pascal_packet = ancestor["pascal_packet"]
R = ancestor["positive_carrier_r"]

def mobius(n: int) -> int:
    if n <= 0: raise ValueError("positive index")
    value,answer,prime=n,1,2
    while prime*prime<=value:
        if value%prime==0:
            value//=prime
            answer=-answer
            if value%prime==0:return 0
            while value%prime==0:value//=prime
        prime+=1
    return -answer if value>1 else answer

def endpoint_weight(j):
    return F(j+1,2**(j+2))

def primitive_mass(q,z=F(1)):
    if q<1:raise ValueError("positive q")
    out=F()
    for d in range(1,q+1):
        if q%d:continue
        t=(F(z)/2)**d
        out+=mobius(d)*(1+(d-1)*t)/(4*(1-t)**2)
    return out

def finite_joint(n,z,t):
    """Exact E[z^J exp(-t 2(8n-7)X)] for rational z,t>=0."""
    a=8*n-7
    if t<0:raise ValueError("nonnegative t")
    return sum((F(comb(n,k))*z**(n-k)*(1-z)**k*
                R(a+2*a*t+8*k) for k in range(n+1)),F())/R(a)

def finite_primitive(n,q):
    return sum((w for j,w in enumerate(pascal_packet(n))
                if gcd(j,q)==1),F())

def rprime(a):
    return -F(4,a*a)+F(2,(a+3)**2)+F(1,(a+4)**2)+F(1,(a+5)**2)

def covariance_J_Z(n):
    a=8*n-7
    return 2*a*n*(rprime(a+8)/R(a)
                  -rprime(a)*R(a+8)/(R(a)**2))

def original_carry_states(length,seed=F(0)):
    x=F(seed)%1
    values=[x];carries=[None]
    for k in range(1,length+1):
        raw=16*x+forcing(k)
        carry=raw.numerator//raw.denominator
        x=raw-carry
        values.append(x); carries.append(carry)
    return values,carries

class PrimitiveChecks(unittest.TestCase):
    def test_parent_four_poles(self):
        self.assertEqual(forcing(1),F(47,15))
        for n in (1,2,10,37):
            self.assertEqual(forcing(n),R(8*n-7))

    def test_joint_Pascal_transform(self):
        for n in (2,5,11,23):
            p=pascal_packet(n)
            for z in (F(),F(1,2),F(1),F(-1)):
                self.assertEqual(finite_joint(n,z,F()),
                     sum((p[j]*z**j for j in range(n+1)),F()))
            self.assertEqual(finite_joint(n,F(1),F(1,2)),
                             R(2*(8*n-7))/R(8*n-7))

    def test_primitive_totient(self):
        self.assertEqual(primitive_mass(2),F(4,9))
        self.assertEqual(primitive_mass(16),F(4,9))
        self.assertEqual(primitive_mass(3),F(29,49))
        self.assertEqual(primitive_mass(6),F(416,1323))
        for n in (2,5,11,23):
            self.assertEqual(finite_primitive(n,2),finite_primitive(n,16))
            self.assertEqual(finite_primitive(n,2),
               (F(1)-finite_joint(n,F(-1),F()))/2)

    def test_bivariate_limit(self):
        for z,t in ((F(0),F(0)),(F(1,2),F(1,3)),(F(1),F(1,2))):
            self.assertLess(abs(finite_joint(160,z,t)
                           -F(1)/(2-z+2*t)**2),F(1,15))

    def test_original_first_jet(self):
        for n in (100,180):
            a=8*n-7
            value=a*(finite_primitive(n,2)-F(4,9))
            self.assertLess(abs(value-F(271,405)),F(1,8))
        self.assertLess(abs(covariance_J_Z(180)-4),F(1,8))

    def test_lag_and_literal_carry_not_proxy(self):
        for seed in (F(),F(1,7),F(1,15)):
            states,cc=original_carry_states(20,seed)
            for n in (2,4,8):
                for j in range(5):
                    lag=sum((16**(j-k)*forcing(n+k)
                             for k in range(1,j+1)),F())
                    self.assertEqual(states[n+j],(16**j*states[n]+lag)%1)
                    self.assertEqual(16*states[n+j-1]+forcing(n+j)-cc[n+j],
                                     states[n+j])

    def test_primitive_rank_filter_is_not_normality(self):
        # Exactly uniform source weights do not cancel a constant phase.
        for n in (6,20,50):
            p=pascal_packet(n)
            self.assertEqual(sum((v for j,v in enumerate(p) if j&1),F()),
                             finite_primitive(n,2))
        # Stable inverse of C_2(S)=4S/(4-S^2)^2 is a formal identity.
        for z in (F(),F(1,3),F(1,2),F(1)):
            C=4*z/(4-z*z)**2
            self.assertEqual((4-z*z)**2*C,4*z)

if __name__=="__main__":
    unittest.main(verbosity=2)
