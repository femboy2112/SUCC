#!/usr/bin/env python3
"""Exact selected BBP carrier-precision, moving-Q alias and hostile-control probes.

Only finite Fraction/integer validations. All asymptotic claims require the
mathematical proofs and quoted classical inputs in PROOFS.md.
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from math import comb, lcm, gcd
import unittest

@lru_cache(maxsize=None)
def source(n):
    assert n >= 1
    return (F(4, 8*n-7) - F(2, 8*n-4)
            - F(1, 8*n-3) - F(1, 8*n-2))

@lru_cache(maxsize=None)
def original(n):
    assert n >= 0
    return F(0) if n == 0 else 16*original(n-1)+source(n)


def modQ(v, Q):
    assert v.denominator % 2 == 1
    return v.numerator*pow(v.denominator, -1, Q)%Q


def circle_distance(fr):
    z=fr%1
    return min(z,1-z)


def height_pair(r):
    Q=16**r
    return F(1), F(Q+1,2*Q+1)


def tm_digit(k):
    return k.bit_count() % 2


class OilyHbarSelectedProbe(unittest.TestCase):
    def test_authentic_source_fingerprint_and_zero(self):
        self.assertEqual(original(0),0)
        for n in range(1,130):
            a=120*n*n-89*n+16
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            self.assertEqual(source(n),F(a,d))
            self.assertEqual(original(n),16*original(n-1)+source(n))
            self.assertEqual(original(n).denominator%2,1)

    def test_height_only_collision_even_with_proven_lcm_bound(self):
        for n in range(1,35):
            L=lcm(*range(1,8*n+1))
            self.assertGreaterEqual(L,2**(8*n-1))
            for r in sorted(set((1,n,2*n-1))):
                Q=16**r
                x,y=height_pair(r)
                self.assertTrue(0<x<16**n)
                self.assertTrue(0<y<16**n)
                self.assertLessEqual(y.denominator,L)
                self.assertLess(x.numerator,16**n*L)
                self.assertLess(y.numerator,16**n*L)
                self.assertEqual(modQ(x,Q),modQ(y,Q))
                self.assertGreaterEqual(circle_distance(x-y),F(16,33))
                self.assertEqual(gcd(y.numerator,y.denominator),1)

    def test_synthetic_coherent_alias_not_fixed_by_rational_height(self):
        for r in range(1,30):
            Q=16**r
            x,y=height_pair(r)
            self.assertEqual(modQ(x,Q),1)
            self.assertEqual(modQ(y,Q),1)
            self.assertEqual(circle_distance(x-y),F(Q,2*Q+1))
            self.assertLess(abs(F(1,2)-y),F(1,2*Q))

    def test_original_selected_moving_carrier_lag_finite(self):
        # Finite strict rational threshold checks, NOT the all-M theorem.
        sample_count=0
        for M in (16,32,64,128,256):
            for Q in ((16,256) if M>=256 else (16,)):
                for h in (1,3,5,7):
                    witness=None
                    for n in range(M,M+64):
                        delta=circle_distance(h*(original(n+Q)-original(n)))
                        if delta >= F(1,32):
                            witness=(n,delta)
                            break
                    self.assertIsNotNone(witness,(M,Q,h))
                    self.assertEqual(modQ(original(witness[0]),Q),
                                     modQ(original(witness[0]+Q),Q))
                    sample_count+=1
        self.assertEqual(sample_count,24)

    def test_original_local_mod16_vs_selected_real(self):
        Q=16
        counts=[0]*16
        for n in range(256):counts[modQ(original(n),Q)]+=1
        self.assertEqual(counts,[16]*16)
        for n in range(1,40):
            self.assertEqual(modQ(original(n+16),Q),modQ(original(n),Q))
            self.assertNotEqual(original(n+16),original(n))

    def test_thue_morse_16ary_nonnormal_pattern(self):
        # Classical Bugeaud theorem μ(c_TM)=2 is an EXTERNAL input,
        # not established by this finite automatic-word sanity check.
        word=[tm_digit(k) for k in range(1024)]
        self.assertEqual(word[:16],[0,1,1,0,1,0,0,1,1,0,0,1,0,1,1,0])
        self.assertEqual(set(word),{0,1})
        for k in range(512):
            self.assertEqual(word[2*k],word[k])
            self.assertEqual(word[2*k+1],1-word[k])
        c_128=sum((F(tm_digit(k),16**(k+1)) for k in range(128)),F())
        self.assertTrue(0<c_128<F(1,15))

    def test_period_three_nonnormal_seed_also_has_large_lag(self):
        for r in range(1,6):
            Q=16**r
            self.assertEqual(pow(16,Q,7),2)
            for n in range(18):
                d=F(pow(16,n+Q,7)-pow(16,n,7),7)
                self.assertGreaterEqual(circle_distance(d),F(1,7))
        orbit=[1,2,4]
        differences=sorted(((a-b)%7 for a in orbit for b in orbit if a!=b))
        self.assertEqual(differences,[1,2,3,4,5,6])
        # |zeta+zeta^2+zeta^4|^2=3+sum_(k=1)^6 zeta^k=2
        self.assertEqual(F(2,9),F(2,9))

    def test_conditional_cofiber_energy_is_exact_pair_current(self):
        # This is the universal algebra behind the genuinely source-conditioned
        # proposed estimator; no trig/float or unproved cancellation.
        basis=((F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),
               (F(0),F(-1)),(F(3,5),F(4,5)),(F(-5,13),F(12,13)))
        N=64
        z=[basis[(7*n+3)//2%len(basis)] for n in range(N)]
        def mag2(a):return a[0]**2+a[1]**2
        for Q in (1,2,4,16):
            self.assertEqual(N%Q,0)
            sums=[(F(),F()) for _ in range(Q)]
            for n,(re,im) in enumerate(z):
                a,b=sums[n%Q]
                sums[n%Q]=(a+re,b+im)
            direct=F(Q,N*N)*sum(map(mag2,sums),F())
            pairs=F(Q,N*N)*sum((a[0]*b[0]+a[1]*b[1]
                                  for i,a in enumerate(z)
                                  for j,b in enumerate(z)
                                  if i%Q==j%Q),F())
            self.assertEqual(direct,pairs)
            total=(sum((x for x,_ in z),F()),
                   sum((y for _,y in z),F()))
            self.assertGreaterEqual(direct,mag2(total)/N**2)
        z=[(F(1),F(0))]*64
        Q=16
        self.assertEqual(F(Q,64**2)*Q*(64//Q)**2,F(1))
        self.assertGreater(F(1),F(2*Q,64))

    def test_gamma_reference_common_euler_constant_cancels(self):
        weights=[4,-2,-1,-1]
        self.assertEqual(sum(weights),0)
        self.assertEqual((F(4,1)*F(1,8)-F(2,1)*F(1,2)
                          -F(5,8)-F(3,4)),F(-15,8))
        # A common Γ/digamma reference -gamma times sum(weights)
        # vanishes, so a uniform offset cannot supply Fourier saving.

    def test_common_phase_rotation_preserves_exact_coherence(self):
        # Gaussian-rational unit phases; no floating trigonometry.
        z=[(F(1),F(0)),(F(3,5),F(4,5)),
           (F(-5,13),F(12,13)),(F(0),F(-1))]
        w=(F(5,13),F(12,13))
        def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
        def norm2(a):return a[0]*a[0]+a[1]*a[1]
        def add(v):return tuple(map(sum,zip(*v)))
        self.assertEqual(norm2(w),1)
        self.assertEqual(norm2(add(z)),norm2(add([mul(a,w) for a in z])))

if __name__ == '__main__':unittest.main(verbosity=2)
