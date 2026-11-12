"""Exact regression tests for the arithmetic water wavefront.
The tests cover finite identities only; Goldbach remains OPEN.
"""
import unittest
from fractions import Fraction
from math import gcd
from independent_audit import run

def phi(n):
    return sum(gcd(k,n)==1 for k in range(n))

def local_K(m,r):
    return sum(gcd(u,m)==1 and gcd(r-u,m)==1 for u in range(m))

class TestDeepWater(unittest.TestCase):
    def test_independent_counterfeit(self):
        result=run()
        self.assertEqual((result.get('source_prime_count',result.get('base_primes')),
                          result.get('Goldbach_unordered_original',result.get('original_pairs_unordered')),
                          result.get('Goldbach_unordered_mutant',result.get('fake_pairs_unordered'))),
                         (574,165,0))
        self.assertEqual((result['original_signed_margin'] if 'original_signed_margin' in result else result['original_signed'],
                          result['mutant_signed_margin'] if 'mutant_signed_margin' in result else result['mutant_signed']),
                         (280,-50))
    def test_crt_sigma(self):
        expected={(2,0):Fraction(2),(6,0):Fraction(3),
                  (6,2):Fraction(3,2),(12,0):Fraction(3),
                  (12,2):Fraction(3,2),(30,0):Fraction(15,4)}
        for (m,r),value in expected.items():
            self.assertEqual(Fraction(m*local_K(m,r),phi(m)**2),value)
    def test_group_ring_conservation(self):
        for m in (2,6,12,30):
            self.assertEqual(sum(local_K(m,r) for r in range(m)),phi(m)**2)
    def test_haar_uniform_under_unit_multiplication(self):
        for m in (6,12,30,60):
            units={u for u in range(m) if gcd(u,m)==1}
            for ell in range(2,31):
                self.assertEqual({ell*u%m for u in units}==units,gcd(ell,m)==1)
    def test_additive_charge_vs_multiplicative_twist(self):
        for mod in (3,5,7,12):
            for n in range(6,61):
                for a in range(2,n-1):
                    self.assertEqual((a+(n-a))%mod,n%mod)
        self.assertNotEqual((2+6)%7,(2*6)%7)

if __name__=='__main__':
    unittest.main()
