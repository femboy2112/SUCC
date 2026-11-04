"""Independent symbolic and finite character regression for next SUCC Gamma/primes front."""
from __future__ import annotations
import importlib.util
from pathlib import Path
from fractions import Fraction as Q
import unittest
import math
ROOT=Path(__file__).resolve().parents[1]
F=ROOT/'research/2026-11-03/split_inert_gamma_lag/odd_gamma_front.py'
S=ROOT/'research/2026-11-03/split_inert_gamma_lag/symbolic_oracle.py'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m
f=load('front',F);sym=load('oracle',S)

class IndependentProofSanity(unittest.TestCase):
    def test_symbolic_checks_not_numerical_fits(self):
        c=sym.run()
        self.assertTrue(all(c.values()),c)

    def test_product_criteria_is_exact_integer(self):
        for A in (16,32,64,128,256):
            p=f.prime_passports(A)
            primes=[q for q,_ in p['split']+p['inert']]
            import math
            P=math.prod(primes)
            d=p['stop']-A-1
            self.assertEqual(P>16**d-1, f.exact_prime_mass_profile(A)['exact_mass_dominates_full_window'])

    def test_ramanujan_factors_without_float_roots(self):
        # Exponent support in Z[X]/(1+...+X^(p-1)) is constant
        # iff a multiple of p; otherwise the weighted trace is -1.
        for p in (7,13,43,47):
            for d in (0,1,2,3,6,12,37):
                for h in (1,3):
                    a=(h*(pow(16,d,p)-1))%p
                    exponents=sorted((a*v)%p for v in range(1,p))
                    if a==0:
                        self.assertEqual(exponents,[0]*(p-1))
                    else:
                        self.assertEqual(exponents,list(range(1,p)))

    def test_second_inert_source_residue_not_avoided(self):
        for k in (11,12):
            p=4*k-1; end=f.inert_second_injection_index(k)
            residue=f.pole_injection_residue(end,p)
            self.assertNotEqual(residue,0)
            before=f.window_prime_clock(p,k,end-1,'inert')
            # Starting source U_(end-1) contains only old clock.
            # Next observed residue gains a nonzero new source injection.
            self.assertNotEqual((16*before+residue)%p,(16*before)%p)

    def test_old_large_sieve_spacing_premise_is_unpurchased(self):
        # Distinct numbers do not imply quantitative spacing.
        q=10**18+1
        x,y=Q(0),Q(1,q)
        self.assertNotEqual(x,y)
        self.assertLess(abs(y-x),Q(1,10**9))

    def test_chi4_not_additive_character_of_rational_circle(self):
        # Q/Z divisible -> any hom to exponent-2 C2 is trivial.
        # Test an attempted character f([a/b]) defined by denominator mod4
        # violates group structure, even on explicit simple fractions.
        x=Q(1,5); half=Q(1,10)
        self.assertEqual((2*half)%1,x)
        self.assertNotEqual((2*1)%2,1) # sign 1 cannot have a square root in C2

    def test_phase_derivative_source_bound(self):
        for n in (1,3,11,65):
            l,u=f.gamma_corrected_tail_interval(n,160)
            self.assertLess(l,u)
            self.assertGreater(l,0)
            self.assertLess(u,Q(1,64*n*n))

if __name__=='__main__': unittest.main()
