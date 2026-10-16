"""Fast exact tests; universal analytical claims are proved in the dossier."""
import unittest
from fractions import Fraction as Q
from observational_succ.unit_prime_succ import (SourceError,prime,prime_list,
    path,braid,prime_smooth,finite_equivalence,ratio_bounds,linear_ratio_bounds,
    log_successor_bounds,adjoint_defect_prefix,probe)

class UnitPrimeTest(unittest.TestCase):
    def test_weighted_braid(self):
        for n in (1,3,7,55):
            for p in (2,3,5,11):
                self.assertEqual(braid(n,p,3),(p*(n+1),Q(n,p*(n+1))**3))
    def test_two_paths(self):
        for b in (1,2,3):
            self.assertEqual(path(tuple([("S",1)]*11),b),
                             path((("V",2),("V",2),("V",3)),b))
    def test_wrong_commutation(self):
        self.assertNotEqual(path((("V",2),("S",1)),1),
                            path((("S",1),("V",2)),1))
    def test_fake_primes(self):
        self.assertFalse(prime(6))
        for fn in (lambda:path((("V",6),),2),
                   lambda:prime_smooth((2,3,6),60,2),
                   lambda:prime_smooth((2,2,3),60,2),
                   lambda:braid(1,9,2)):
            with self.assertRaises(SourceError):fn()
    def test_independent_jet_enum(self):
        self.assertEqual(prime_list(11),(2,3,5,7,11))
        m=prime_smooth((2,3),100,2)
        self.assertEqual(m[72],Q(1,72**2))
        self.assertNotIn(7,m)
    def test_finite_match(self):
        for p in (2,3,5,11):
            r=finite_equivalence(p,100,2)
            self.assertEqual(r["unit_weight"],1)
            self.assertTrue(all(n>p for n in r["unseen"]))
    def test_ratio_intervals(self):
        for p in (2,3,7,11):
            a=ratio_bounds(p,2);b=linear_ratio_bounds(p,2)
            self.assertLessEqual(a[0],b[1]);self.assertLessEqual(b[0],a[1])
    def test_log_clock_and_defect(self):
        self.assertEqual(log_successor_bounds(1),(Q(1,2),Q(1)))
        self.assertEqual(adjoint_defect_prefix(10,2),((1,),(1,3,5,7,9)))
    def test_bool_mutants(self):
        with self.assertRaises(SourceError):path((),True)
    def test_probe(self):
        self.assertTrue(probe()["exact_finite_checks"])

if __name__=="__main__":unittest.main()
