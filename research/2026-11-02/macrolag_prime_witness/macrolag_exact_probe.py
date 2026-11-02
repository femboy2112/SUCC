#!/usr/bin/env python3
"""Exact bounded probes for macroscopic BBP temporal prime witnesses.

These are independent finite checks, NOT a substitute for PNT-AP in the proof.
"""
from fractions import Fraction as F
from math import isqrt
from functools import lru_cache
import unittest

@lru_cache(maxsize=None)
def source(n):
    assert n>=1
    return F(4,8*n-7)-F(2,8*n-4)-F(1,8*n-3)-F(1,8*n-2)

@lru_cache(maxsize=None)
def source_combined(n):
    a=8*n-7
    return F(15*a*a+121*a+240, a*(a+3)*(a+4)*(a+5))

@lru_cache(maxsize=None)
def U(n):
    if n==0: return F(0)
    return 16*U(n-1)+source(n)

@lru_cache(maxsize=None)
def d(n):
    return sum((F(1,16**j)*source(n+j) for j in range(1,n+2)),F())

@lru_cache(maxsize=None)
def fake_U(n):
    return 16**n*F(47,240)-d(n)


def primes_below(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[:2]=b'\x00\x00'
    for i in range(2,isqrt(N)+1):
        if sieve[i]: sieve[i*i::i]=b'\x00'*(((N-i*i)//i)+1)
    return [p for p in range(N+1) if sieve[p]]

PRIMES=primes_below(2000)

def vp(fr,p):
    if fr==0: return None
    a,b=abs(fr.numerator),fr.denominator
    v=0
    while a%p==0:a//=p;v+=1
    while b%p==0:b//=p;v-=1
    return v

def born(p):
    assert p%4==1
    if p%8==1:return (p+7)//8,4
    return (p+3)//8,-1

class MacrolagExactTests(unittest.TestCase):
    def test_two_original_four_pole_implementations(self):
        for n in range(1,180): self.assertEqual(source(n),source_combined(n))

    def test_original_macrolag_p_birth_differences(self):
        count=0
        for m in range(9,66,4):
            for lag in sorted({1,2,3,max(1,m//8),m//4,m//2,(3*m)//4}):
                n=m+lag
                if n> int(1.75*m): continue
                for p in PRIMES:
                    if p<=2*n or p>=8*m or p%4!=1 or pow(16,lag,p)==1:continue
                    j,c=born(p)
                    self.assertTrue(j<=m<(p+1)//2)
                    self.assertEqual(vp(U(m),p),-1)
                    self.assertEqual(vp(U(n),p),-1)
                    self.assertEqual(vp(U(n)-U(m),p),-1)
                    self.assertEqual((16**(n-j)-16**(m-j))*c%p,(16**(m-j)*c*(pow(16,lag,p)-1))%p)
                    count+=1
        self.assertGreater(count,500)

    def test_mutant_still_zero_seed_positive_and_exponential_shadow(self):
        q=F(47,240)
        self.assertEqual(d(0),q)
        self.assertEqual(fake_U(0),0)
        for n in range(1,71):
            src=fake_U(n)-16*fake_U(n-1)
            correction=F(1,16**n)*source(2*n)+F(1,16**(n+1))*source(2*n+1)
            self.assertEqual(src,source(n)-correction)
            self.assertGreater(src,0)
            self.assertLess(src,source(n))
            self.assertGreater(d(n),0)
            self.assertLess(d(n),F(2,15))
            self.assertEqual((16**n*q-F(2,15)).denominator,1)
            self.assertEqual((fake_U(n)-F(2,15)+d(n)).denominator,1)

    def test_mutant_macrolag_p_witness_and_real_coherence(self):
        count=0
        for m in range(8,55,3):
            n=(3*m)//2
            self.assertTrue(n>m and n<2*m)
            diff=fake_U(n)-fake_U(m)
            # Because the q contributions differ by an integer, the
            # fractional real difference is positive d_m-d_n -> 0.
            self.assertEqual(diff-(d(m)-d(n)),int(diff-(d(m)-d(n))))
            self.assertGreater(d(m)-d(n),0)
            self.assertLess(d(m)-d(n),F(1,m*m))
            for p in PRIMES:
                if not (8*m<p<8*n and p%4==1):continue
                self.assertGreater(p,4*n+1)
                self.assertEqual(vp(d(m),p),-1)
                self.assertGreaterEqual(vp(d(n),p),0)
                self.assertEqual(vp(diff,p),-1)
                count+=1
        self.assertGreater(count,50)

    def test_original_all_lag_newborn_prime_support(self):
        count = 0
        for m in range(9, 53, 5):
            for n in (m+1, m+m//3, 2*m-1, 3*m, 5*m):
                for p in PRIMES:
                    if not(max(8*m,2*n)<p<8*n and p%4==1): continue
                    self.assertGreaterEqual(vp(U(m),p),0)
                    self.assertEqual(vp(U(n)-U(m),p),-1)
                    count += 1
        self.assertGreater(count, 100)

    def test_mutant_shared_and_newborn_global_support(self):
        shared_count = newborn_count = 0
        for m in range(10, 45, 4):
            for n in range(m+1, min(3*m,110)):
                ell=n-m
                if n<2*m:
                    shared=(p for p in PRIMES if p%4==1 and 8*n<p<16*m and pow(16,ell,p)!=1)
                    newborn=(p for p in PRIMES if p%4==1 and 16*m+8<p<16*n)
                else:
                    shared=()
                    newborn=(p for p in PRIMES if p%4==1 and 8*n+8<p<16*n)
                diff=fake_U(n)-fake_U(m)
                for p in shared:
                    self.assertEqual(vp(diff,p),-1)
                    shared_count += 1
                for p in newborn:
                    self.assertEqual(vp(diff,p),-1)
                    newborn_count += 1
        self.assertGreater(shared_count,100)
        self.assertGreater(newborn_count,100)

    def test_rational_shadow_first_N_prefix(self):
        for n in range(0,26):
            self.assertEqual(fake_U(n),16**n*F(47,240)-d(n))
        for n in range(1,26):
            # finite forcing mutant, same all-polynomial-order source
            self.assertLess(abs(fake_U(n)-16**n*F(47,240)),F(1,n*n))

if __name__=='__main__':unittest.main(verbosity=2)
