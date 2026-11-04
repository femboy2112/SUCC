#!/usr/bin/env python3
"""Exact original-BBP carrier-hbar and cross-completion tests (stdlib only).

Finite checks calibrate; PNT, mu(pi) and infinite limits are PAPER proofs.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
from math import comb
import unittest

@lru_cache(None)
def r(n):
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

def rmod(n,q):
    a=120*n*n-89*n+16
    d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
    assert d&1
    return (a*pow(d,-1,q))%q

def fmod(n,level):
    q=16**level
    return sum(16**j*rmod(n-j,q) for j in range(level))%q

@lru_cache(None)
def U(n):
    return F(0) if n==0 else 16*U(n-1)+r(n)

def v2(x):
    if x==0:return None
    return (abs(x.numerator)&-abs(x.numerator)).bit_length() - (x.denominator&-x.denominator).bit_length()

ATOMS=((F(1,80),F(93606744115,32218183998)),
       (F(5,16),F(992400341,7594857270)),
       (F(1,2),F(1011071983,11951906967)),
       (F(63,80),F(23100710,1823277183)))

def a_r(n):
    return sum((w*x**(n-1) for x,w in ATOMS),F())

def prod(p,q):
    z=[F()]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):z[i+j]+=a*b
    return z

def echo_psi4():
    p=[F(1)]
    for _ in range(5):
        p=prod(p,[-F(1,4),F(1)])
        p=prod(p,[F(1,2),-F(1)])
    for _ in range(4):
        p=[(i+1)*p[i+1] for i in range(len(p)-1)]
    return p

def echo_delta(n):
    p=echo_psi4()
    eps=F(1,1000*sum(abs(x) for x in p))
    a,b=F(1,4),F(1,2)
    return eps*sum((c*(b**(n+i)-a**(n+i))/(n+i) for i,c in enumerate(p)),F())

class CarrierHBarExact(unittest.TestCase):
    def test_source_is_original_four_poles(self):
        for n in range(-11,130):
            a=120*n*n-89*n+16
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            self.assertEqual(r(n),F(a,d))
        self.assertEqual(r(1),F(47,15))

    def test_every_original_finite_carrier_level_permutation(self):
        for level in range(1,5):
            q=16**level
            u=0
            seen=bytearray(q)
            for n in range(q):
                if n:u=(16*u+rmod(n,q))%q
                a=fmod(n,level)
                self.assertEqual(a,u)
                self.assertFalse(seen[a])
                seen[a]=1
            self.assertTrue(all(seen))
            self.assertEqual(fmod(0,level),0)
            self.assertEqual(fmod(q,level),0)

    def test_genuine_backward_zero_400_bits_calibration(self):
        mod=16**100
        self.assertEqual(sum(16**j*rmod(-j,mod) for j in range(100))%mod,0)

    def test_carrier_vs_real_two_exact_selected_counterexamples(self):
        for level,n,threshold in [(1,16,F(3,16)),(2,256,F(3,8))]:
            q=16**level
            u=U(n)
            self.assertEqual(fmod(n,level),0)
            self.assertEqual(u.numerator*pow(u.denominator,-1,q)%q,0)
            x=u%1
            self.assertGreater(min(x,1-x),threshold)

    def test_real_carry_cofiber_is_exact_not_local_phase(self):
        for level in (1,2,3):
            q=16**level
            for n in (0,1,2,4,8,16,31,63,96):
                a=fmod(n,level)
                u=U(n)
                t=(u-a)/q
                self.assertEqual(u,a+q*t)
                self.assertEqual(t.denominator%2,1)
                self.assertEqual(u%1,(q*t)%1)
                self.assertEqual((u/q)%1,(F(a,q)+t)%1)

    def test_real_histogram_not_local_haar_at_N256(self):
        h={16:Counter(),256:Counter()}
        local={16:Counter(),256:Counter()}
        matches={16:0,256:0}
        for n in range(256):
            u=U(n);f=u%1
            for q,level in ((16,1),(256,2)):
                a=fmod(n,level)
                b=(q*f.numerator)//f.denominator
                local[q][a]+=1
                h[q][b]+=1
                matches[q]+=int(a==b)
        self.assertEqual(sorted(local[16].values()),[16]*16)
        self.assertEqual(sorted(local[256].values()),[1]*256)
        self.assertEqual((min(h[16].values()),max(h[16].values())),(12,23))
        self.assertEqual(len(h[256]),163)
        self.assertEqual(matches,{16:22,256:1})

    def test_real_selected_fixed_lag_has_finite_noalias_witnesses(self):
        for q,level in ((16,1),(256,2)):
            for h in (1,3,5):
                hits=0
                for n in range(20,220):
                    self.assertEqual(fmod(n,level),fmod(n+q,level))
                    z=(h*(U(n+q)-U(n)))%1
                    if min(z,1-z)>=F(1,32):hits+=1
                self.assertGreater(hits,100)

    def test_rational_atom_zero_passport_fails_original_at_level_one(self):
        for n in range(1,5):self.assertEqual(r(n),a_r(n))
        alpha=sum((w/(16-x) for x,w in ATOMS),F())
        self.assertEqual(alpha,F(4062342947075618,20689342837729335))
        self.assertEqual(v2(alpha),1)
        for x,w in ATOMS:
            self.assertLess(v2(x),4)
            self.assertGreater(w,0)
        backward=sum((w/(x-16) for x,w in ATOMS),F())
        self.assertEqual(backward,-alpha)
        self.assertNotEqual(backward.numerator*pow(backward.denominator,-1,16)%16,0)
        self.assertEqual(fmod(0,1),0)

    def test_entire_positive_echo_breaks_two_adic_integrality(self):
        self.assertEqual([echo_delta(n) for n in range(1,5)],[F()]*4)
        self.assertLess(abs(echo_delta(5)),F(1,1000))
        self.assertEqual(v2(echo_delta(5)),-16)
        self.assertEqual((r(5)+echo_delta(5)).denominator%2,0)

    def test_periodic_nonnormal_seed_fools_even_linear_fixed_lag_energy(self):
        residues=[pow(16,n,7) for n in range(3)]
        self.assertEqual(residues,[1,2,4])
        self.assertEqual(sorted((a-b)%7 for a in residues for b in residues if a!=b),
                         [1,2,3,4,5,6])
        for level in range(1,5):
            q=16**level
            self.assertEqual(q%3,1)
            for n in range(33):
                self.assertIn((pow(16,n+q,7)-pow(16,n,7))%7,[1,2,4])

    def test_exact_hbar_box_filter_integer_winding(self):
        for level in range(1,8):
            for n in range(level,25):
                self.assertEqual(16**(n-level)%1,0)
            self.assertEqual(sum((F(16**n,16**level) for n in range(level)),F()),
                             (1-F(1,16**level))/15)

if __name__=='__main__':unittest.main(verbosity=2)
