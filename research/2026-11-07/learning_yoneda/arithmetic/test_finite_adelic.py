import unittest
from math import gcd, prod
from fractions import Fraction as Q
import finite_adelic as f
import independent_oracle as oracle


class FiniteAdelicTests(unittest.TestCase):
    def test_main_selected_orbit_compatibility(self):
        from observational_succ.selected_orbit import SelectedOrbit
        original=SelectedOrbit()
        for n,u in enumerate(f.history(156)):
            self.assertEqual(original.state(n),u%1)

    def test_four_pole_combined_identity(self):
        for n in range(1,157):
            literal=4/Q(8*n-7)-2/Q(8*n-4)-1/Q(8*n-3)-1/Q(8*n-2)
            combined=Q(120*n*n-89*n+16,(2*n-1)*(4*n-1)*(8*n-7)*(8*n-3))
            self.assertEqual(f.forcing(n),literal)
            self.assertEqual(f.forcing(n),combined)
            self.assertNotEqual(f.forcing(n)+Q(1,8*n-7),combined)

    def test_exact_hostile_epoch(self):
        w=f.construct(5,17,19,9,Q(1,2**18),f.primes_through(8*35))
        f.verify(w)
        self.assertEqual(oracle.check(w),72)
        self.assertNotEqual(w['seed'],0)
        self.assertGreater(w['seed'].denominator,1)
        self.assertEqual(gcd(w['seed'].denominator,prod(w['primes'])),1)

    def test_prime_principal_part_mutant(self):
        for p in (3,5,7,11,47):
            self.assertEqual(f.principal(Q(0),p),0)
            self.assertNotEqual(f.principal(Q(1,p),p),0)
            for n in range(5):
                self.assertNotEqual(f.principal(Q(16**n,p),p),0)

    def test_carry_erasure_is_not_two_adic_state(self):
        u=f.history(1)[1]
        self.assertEqual(u,Q(47,15))
        self.assertNotEqual(f.residue(u,16),f.residue(u%1,16))
        self.assertEqual(f.principal(u,3),f.principal(u%1,3))

    def test_sign_and_empty_tail(self):
        w=f.construct(3,11,1,8,Q(1,2**20),(3,5,7))
        _,_,residuals,_=f.verify(w)
        self.assertGreaterEqual(residuals[0],0)
        self.assertLessEqual(residuals[0],w['eta'])
        oracle.check(w)

    def test_fixed_eta_geometric_sharpening(self):
        w=f.construct(3,17,17,8,Q(1,8),(3,5,7,11))
        _,_,_,lower=f.verify(w)
        delta=w['seed']-w['center']
        actual=sum((16**n*delta)**2 for n in range(w['A'],w['B']+1))/w['L']
        geometric=w['eta']**2*(1-Q(1,256**w['L']))/(w['L']*(1-Q(1,256)))
        self.assertLessEqual(actual,geometric)
        self.assertGreater(lower[1],1-Q(1,w['A']))

    def test_source_bound(self):
        for n in range(2,351):
            self.assertLess(f.forcing(n),Q(1,n*n))
            self.assertGreater(f.forcing(n),0)

    def test_invalid_chronology(self):
        for args in [(3,3,1,1,Q(1,8)),(0,1,0,1,Q(1,8)),(0,1,1,-1,Q(1,8))]:
            with self.assertRaises(ValueError):
                f.construct(*args,(3,5))

    def test_reject_invalid_prime_collections(self):
        for primes in ((1,), (2,), (9,), (15,), (True,), (3.0,), (3,3), [5,5], "3"):
            with self.subTest(primes=primes), self.assertRaises(ValueError):
                f.construct(0,1,1,0,Q(1,8),primes)
        self.assertEqual(f.prime_set({7,3,5}),(3,5,7))
        self.assertEqual(f.prime_set(()),())

    def test_principal_rejects_nonprimes_and_inexact_rationals(self):
        for p in (0,1,2,4,9,-3,True,3.0):
            with self.subTest(p=p), self.assertRaises(ValueError):
                f.principal(Q(0),p)
        for value in (0.5,True,"1/3"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                f.principal(value,3)

    def test_reject_inexact_chronology_seed_and_precision(self):
        valid=[0,1,1,0,Q(1,8)]
        for index in range(4):
            for bad in (True,1.0,Q(1)):
                args=valid.copy()
                args[index]=bad
                with self.subTest(index=index,bad=bad), self.assertRaises(ValueError):
                    f.construct(*args,(3,5))
        for eta in (0.125,True,"1/8"):
            with self.subTest(eta=eta), self.assertRaises(ValueError):
                f.construct(0,1,1,0,eta,(3,5))
        for seed in (0.5,True):
            with self.subTest(seed=seed), self.assertRaises(ValueError):
                f.history(2,seed)


if __name__=='__main__':
    unittest.main()
