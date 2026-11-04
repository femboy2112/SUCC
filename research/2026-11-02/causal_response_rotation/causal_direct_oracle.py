#!/usr/bin/env python3
"""Numerical direct-seed quadrature oracle; float-only diagnostic, NOT proof.

Independent from the formal Fourier coefficient/difference-pair calculation.
"""
from math import pi, ceil, log2
from cmath import exp
from fractions import Fraction as Q
from functools import lru_cache
import unittest

@lru_cache(None)
def signed_source(n):
    return (Q(4,8*n-7)-Q(2,8*n-4)-Q(1,8*n-3)-Q(1,8*n-2))

@lru_cache(None)
def true_orbit(n):
    return Q() if n==0 else 16*true_orbit(n-1)+signed_source(n)

@lru_cache(None)
def shadow_orbit(n):
    return 16**n*Q(47,240)-sum((Q(1,16**j)*signed_source(n+j)
                                 for j in range(1,n+2)),Q())

def unit_phase(fr):
    return exp(2j*pi*float(fr%1))

def grid_certificate(seq,N,h):
    grid=1<<ceil(log2(2*h*16**N+1))
    vals=[unit_phase(h*seq(n)) for n in range(N+1)]
    picks={n:0j for n in range(1,N+1)}
    normsum=0.
    for t in range(grid):
        base=exp(2j*pi*t/grid)
        # Independent direct unit-circle evaluation by repeated exponents
        ph=sum(vals[n]*base**(h*16**n) for n in range(N+1))
        density=abs(ph)**2/(N+1)
        normsum+=density/grid
        for n in picks:
            k=h*(16**n-1)
            picks[n]+=density*base**(-k)/grid
    return grid,normsum,picks,vals

class DirectOracle(unittest.TestCase):
    def test_explicit_seed_integrals_recover_original_and_shadow(self):
        for seq in (true_orbit,shadow_orbit):
            for N in (2,3):
                for h in (1,2):
                    grid,total,got,vals=grid_certificate(seq,N,h)
                    self.assertGreater(grid,2*h*16**N)
                    self.assertLess(abs(total-1),1e-10)
                    for n,c in got.items():
                        target=vals[n]*vals[0].conjugate()/(N+1)
                        self.assertLess(abs(c-target),3e-10,(N,h,n,abs(c-target)))

if __name__=='__main__':unittest.main(verbosity=2)
