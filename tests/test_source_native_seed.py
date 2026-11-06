import sys,unittest
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"research"/"2026-11-04"/"alias_valve"))
import source_native_seed as s

class SeedCarrierTests(unittest.TestCase):
    def test_source_independent_polynomial_and_oddness(self):
        for n in range(1,180):
            self.assertEqual(s.source_force(n),s.collapsed_force(n))
            self.assertEqual(s.source_force(n).denominator%2,1)

    def test_every_large_prime_appears_in_source_lattice(self):
        for A in (8,16,32,64):
            B=s.source_conductor(A)
            for p in range(7,8*A):
                if any(p%d==0 for d in range(2,int(p**0.5)+1)):
                    continue
                if p <= 4*A-1 or (p<=8*A-7 and p%4==1):
                    self.assertEqual(B%p,0,(A,p))

    def test_early_conductor_threshold_is_finite_not_all_A(self):
        self.assertTrue(s.native_epoch(64)['certified_early'])
        self.assertFalse(s.native_epoch(12)['certified_early'])
        for A in (40,48,64,96):
            p=s.native_epoch(A)
            self.assertTrue(p['certified_early'])
            self.assertNotEqual(p['seed'],0)
            self.assertEqual(p['B']%p['seed_den'],0)
            self.assertLess(p['width'],F(1,32*A*A))

    def test_counterseed_clusters_but_zero_seed_not_assumed(self):
        for A,q in ((40,4),(48,8),(64,16)):
            p=s.native_epoch(A)
            J=s.energy(p['phase_cloud'],q)
            self.assertGreaterEqual(J,q*(1-q*p['width']))
            self.assertGreater(J,F(99*q,100))
            self.assertEqual(s.original_orbit(1)[0],F(0))
            self.assertNotEqual(p['phase_cloud'],s.original_orbit(2*A-1)[A:2*A])

    def test_virtual_field_uniform_then_coalesces(self):
        for K in (1,2,3):
            for n in range(K+2):
                cloud=s.finite_virtual_seed_field(K,n)
                self.assertEqual(len(cloud),16**K)
                self.assertEqual(len(set(cloud)),16**max(0,K-n))
                self.assertTrue(all(cloud.count(x)==16**min(K,n) for x in set(cloud)))
                self.assertIn(s.original_orbit(n)[-1], cloud)
                if n>=K:
                    self.assertEqual(len(set(cloud)),1)

    def test_nearest_rational_and_past_conductor(self):
        for A in (8,12,24,32,64):
            p=s.native_epoch(A)
            self.assertLessEqual(p['alignment'], F(1,2*p['B']))
            self.assertEqual(p['seed'].denominator%2,1)
            self.assertTrue(all(x.denominator%2==1 for x in p['phase_cloud']))

    def test_counterseed_witness_escalation(self):
        for A in (32,40,48,64,96):
            p=s.native_epoch(A)
            self.assertGreater(p['seed_bits'],2*A)
            self.assertLess(p['alignment'],F(1,2*p['B'])+F(1,10**1000))

if __name__=='__main__':unittest.main()
