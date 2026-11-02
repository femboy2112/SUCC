#!/usr/bin/env python3
"""Exact finite tests for causal response lacunary rotation of SUCC orbits.

All phase information is encoded as rational angles mod 1; no floating
trigonometry, no pi digits and no claim of asymptotic normality.
"""
from fractions import Fraction as Q
from functools import lru_cache
from collections import defaultdict
from math import comb
import unittest

@lru_cache(None)
def r(n):
    a=8*n-7
    return Q(4,a)-Q(2,a+3)-Q(1,a+4)-Q(1,a+5)

@lru_cache(None)
def U(n):
    return Q(0) if n==0 else 16*U(n-1)+r(n)

@lru_cache(None)
def d(n):
    return sum((r(n+j)/16**j for j in range(1,n+2)),Q(0))

@lru_cache(None)
def shadow(n):
    return Q(47,240)*16**n-d(n)

def mod_one(angle):
    return angle % 1

def spectrum(phases,b,h):
    """Intensity Fourier coefficients as EXACT fractional phasor angles.

    Key is integer causal seed Fourier frequency, value is list of phasor
    exponent angles Q/Z. Zero-mode multiplicity is len(phases).
    """
    out=defaultdict(list)
    for n,a in enumerate(phases):
        for m,c in enumerate(phases):
            out[h*(b**n-b**m)].append(mod_one(h*(a-c)))
    return dict(out)

def compositions(total, length):
    if length==1:
        yield (total,)
        return
    for k in range(total+1):
        for tail in compositions(total-k,length-1):
            yield (k,)+tail

def collision_groups(base, order, positions=3):
    groups=defaultdict(list)
    for counts in compositions(order,positions):
        freq=sum(c*base**j for j,c in enumerate(counts))
        groups[freq].append(counts)
    return [v for v in groups.values() if len(v)>1]

class CausalResponseTest(unittest.TestCase):
    def test_injective_causal_differences_all_bases(self):
        for b in (2,3,5,16):
            for M in (2,3,6,9):
                diffs={}
                for n in range(M):
                    for m in range(M):
                        if n==m:continue
                        k=b**n-b**m
                        self.assertNotIn(k,diffs)
                        diffs[k]=(n,m)
                self.assertEqual(len(diffs),M*(M-1))

    def test_original_and_shadow_exact_intensity_phase_retrieval(self):
        for seq in (U,shadow):
            for h in (1,3,7):
                for N in range(1,9):
                    phases=[seq(n) for n in range(N+1)]
                    sp=spectrum(phases,16,h)
                    self.assertEqual(sp[0],[Q(0)]*(N+1))
                    for k,v in sp.items():
                        if k:self.assertEqual(len(v),1)
                    for n in range(1,N+1):
                        k=h*(16**n-1)
                        self.assertEqual(sp[k][0],mod_one(h*(seq(n)-seq(0))))
                    # Each offzero coefficient of normalized causal intensity
                    # has modulus 1/(N+1), hence weak convergence to Haar.
                    self.assertEqual(len(sp)-1,N*(N+1))

    def test_same_source_seed_gauge_is_translation(self):
        seed=Q(3,17)
        for N in range(1,8):
            phases=[U(n) for n in range(N+1)]
            displaced=[U(n)+16**n*seed for n in range(N+1)]
            sp=spectrum(phases,16,3)
            shifted=spectrum(displaced,16,3)
            self.assertEqual(sp.keys(),shifted.keys())
            for k in sp:
                self.assertEqual([mod_one(a+k*seed) for a in sp[k]],shifted[k])

    def test_moments_fourth_universality(self):
        for N in range(1,10):
            M=N+1
            offdiag=sum(len(v)**2 for k,v in spectrum([U(n) for n in range(M)],16,1).items() if k)
            self.assertEqual(offdiag,M*(M-1))
            self.assertEqual(M*M+offdiag,M*(2*M-1))
            self.assertEqual(Q(offdiag,M*M),Q(N,N+1))

    def test_first_equal_length_resonance_at_base_plus_one(self):
        for b in (2,3,4,5,16):
            for q in range(1,b+1):
                self.assertFalse(collision_groups(b,q,3),(b,q))
            hits=collision_groups(b,b+1,3)
            self.assertTrue(hits,b)
            a=(b,0,1); c=(0,b+1,0)
            self.assertTrue(any(a in hit and c in hit for hit in hits),b)

    def test_first_radic_34th_moment_resonance_is_source_only(self):
        for seq,forcing in ((U,r),(shadow,lambda j: r(j)-r(2*j)/16**j-r(2*j+1)/16**(j+1))):
            for n in range(0,21):
                self.assertEqual(16*seq(n)+seq(n+2)-17*seq(n+1),forcing(n+2)-forcing(n+1))
            # The same exact resonance survives ANY starting seed.
            seed=Q(4,7)
            for n in range(0,8):
                s=lambda j:seq(j)+16**j*seed
                self.assertEqual(16*s(n)+s(n+2)-17*s(n+1),
                                 forcing(n+2)-forcing(n+1))

    def test_source_vs_causal_dilation_power_two_routes(self):
        for seq,forcing in ((U,r),(shadow,lambda j: r(j)-r(2*j)/16**j-r(2*j+1)/16**(j+1))):
            for n in range(0,25):
                # Phases of Z_(n+1)/Z_n^16 -> source forcing.
                self.assertEqual(mod_one(seq(n+1)-16*seq(n)),mod_one(forcing(n+1)))
                # Phases of (Z_n)^16/Z_n(16s) -> selected state.
                self.assertEqual(mod_one(15*seq(n)),mod_one((16-1)*seq(n)))
                # Z_(n+1)/Z_n(16s) -> chronological unit difference.
                self.assertEqual(mod_one(seq(n+1)-seq(n)),
                                 mod_one(15*seq(n)+forcing(n+1)))

    def test_exponential_causal_resolution_floor(self):
        for b in (2,3,16):
            for N in range(1,9):
                ds=[abs(b**N-b**m) for m in range(N)]
                self.assertEqual(min(ds),(b-1)*b**(N-1))
                self.assertEqual(max(ds),b**N-1)

if __name__=='__main__':unittest.main(verbosity=2)
