import unittest
from fractions import Fraction as F
from period_fiber import *

class PeriodFiberTests(unittest.TestCase):
    def test_original(self):
        self.assertEqual(forcing(Q,1),F(47,15))
        self.assertEqual(Q,(4,0,0,-2,-1,-1))
    def test_exact_family(self):
        for m,N in [(2,0),(4,1),(7,3),(9,6)]:certificate(m,N)
    def test_minimal_beta_formula(self):
        for m in (2,4,7):
            c=construction(m,0)
            for n in range(1,31):
                self.assertEqual(delta_orbit(c,n),c['epsilon']*8*n*beta(8*n+1,m+2))
    def test_chronological_coboundary(self):
        c=construction(6,4)
        for n in range(1,35):
            self.assertEqual(forcing(c['source'],n)-forcing(Q,n),
                delta_orbit(c,n)-16*delta_orbit(c,n-1))
    def test_endpoint_condition_necessary(self):
        self.assertEqual(integral(derivative((0,1))),1)
    def test_forcing_changes_after_prefix(self):
        c=construction(3,2)
        self.assertEqual(forcing(c['D'],1),0)
        self.assertEqual(forcing(c['D'],2),0)
        self.assertGreater(forcing(c['D'],3),0)
    def test_domains(self):
        for args in [(1,0),(2,-1)]:
            with self.assertRaises(ValueError):orthogonal(*args)
        with self.assertRaises(ValueError):forcing(Q,0)

if __name__=='__main__':unittest.main()
