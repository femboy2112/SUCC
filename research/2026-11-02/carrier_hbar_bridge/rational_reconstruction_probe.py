#!/usr/bin/env python3
"""Exact source-conditioned finite hbar -> real rational decoding.

Rational reconstruction is classical; the BBP height/odd-denominator
specialization is proved in PROOFS.md. No signed normality estimate.
"""
from fractions import Fraction as F
import unittest


def source(j):
    return F(4,8*j-7)-F(2,8*j-4)-F(1,8*j-3)-F(1,8*j-2)


def reconstruct(z, modulus, numerator_bound, denominator_bound):
    # Euclidean rational-reconstruction algorithm with explicit checks.
    r0,r1=modulus,z
    t0,t1=0,1
    while r1>numerator_bound:
        q=r0//r1
        r0,r1=r1,r0-q*r1
        t0,t1=t1,t0-q*t1
    if t1==0 or r1==0:
        return None
    candidate=F(r1,t1)
    if (abs(candidate.numerator)>numerator_bound or
        candidate.denominator>denominator_bound):
        return None
    if (candidate.numerator-z*candidate.denominator)%modulus:
        return None
    return candidate


class CarrierHbarRationalDecoder(unittest.TestCase):
    def test_original_59_states_exact_inverse(self):
        u=F(0); D=1
        for n in range(1,60):
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            D*=d
            u=16*u+source(n)
            self.assertLess(u,16**n)
            self.assertEqual((u.denominator*D)%u.denominator,0)
            bound=16**n*D
            limit=2*bound*D
            modulus=16
            level=1
            while modulus<=limit:
                level+=1;modulus*=16
            self.assertLess(limit,modulus)
            residue=(u.numerator*pow(u.denominator,-1,modulus))%modulus
            recovered=reconstruct(residue,modulus,bound,D)
            self.assertEqual(recovered,u,(n,level))
            # The source-independent uniqueness certificate is cross-multiply:
            # no two admissible rationals can share this residue at modulus>2HD.
            self.assertGreater(modulus,2*bound*D)

    def test_uniform_10n_hbar_lcm_reconstruction(self):
        from math import lcm
        u=F(0); L=1; j=0
        for n in range(1,201):
            while j<8*n:
                j+=1;L=lcm(L,j)
            u=16*u+source(n)
            modulus=16**(10*n)
            bound=16**n*L
            self.assertLessEqual(L,4**(8*n))
            self.assertGreater(modulus,2*bound*L)
            local=u.numerator*pow(u.denominator,-1,modulus)%modulus
            self.assertEqual(reconstruct(local,modulus,bound,L),u,n)

    def test_reduced_source_denominators_are_odd(self):
        u=F(0)
        for n in range(1,160):
            u=16*u+source(n)
            self.assertEqual(u.denominator%2,1)

    def test_wrong_residue_is_not_actual_source(self):
        u=F(0);D=1
        for n in range(1,12):
            d=(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3)
            D*=d;u=16*u+source(n)
            H=16**n*D
            modulus=16
            while modulus<=2*H*D:modulus*=16
            actual=u.numerator*pow(u.denominator,-1,modulus)%modulus
            mutant=reconstruct((actual+1)%modulus,modulus,H,D)
            self.assertNotEqual(mutant,u)

if __name__=='__main__':
    unittest.main(verbosity=2)
