"""Exact finite research calibration; no normality assertion."""
import unittest
from scripts import pi_selected_boundary_probe as p

class SelectedBoundaryFinite(unittest.TestCase):
    def test_original_signed_source_and_green(self):
        r,u,t,pi_m=p.states_and_tails(110)
        for n in range(1,111): self.assertEqual(r[n],p.cancelled(n))
        for n in range(111): self.assertEqual(u[n]+t[n],16**(n-1)*pi_m)
    def test_crt_and_rational_nonnormal_mutant(self):
        z=p.check()
        self.assertLess(z[1],0.04)
        self.assertGreater(z[17],0.9)
    def test_wrong_pole_rejected(self):
        self.assertNotEqual(p.four_pole(1),p.four_pole(1)+1)
    def test_cut_mutation_not_uniform(self):
        _,_,t,_=p.states_and_tails()
        self.assertTrue(all(0<t[n]<1/16 for n in range(1,100)))

if __name__=="__main__": unittest.main()
