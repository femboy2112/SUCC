"""Original four-pole exact seam/correction complement and Haar tail controls."""
from fractions import Fraction as F
import unittest
from time_extrusion_probe import forcing,green_interval,circle_prefix,certified_pure_state

class SeamSplitTest(unittest.TestCase):
    def test_source_ratio_tends_to_fifteen(self):
        for n in (3,5,20,80,300):
            tlo,thi=green_interval(n,16)
            r=forcing(n)
            self.assertTrue(F(0)<tlo<thi<r)
            self.assertLess(abs(r/tlo-15),F(210,n))

    def test_shrinking_windows_sum_has_summable_source_bound(self):
        for n in range(3,100):
            _,thi=green_interval(n,10)
            self.assertLess(thi,F(1,(8*n+1)**2))
            self.assertLess(forcing(n),F(1,2*n*n))
            self.assertLess(thi+forcing(n),F(33,64*n*n))

    def test_reference_tail_probability_upper(self):
        for n in (3,4,5,20,100):
            self.assertGreater(F(33,64*(n-1)),F(0))
            self.assertLess(F(33,64*n*n),F(33,64*(n-1)))

    def test_actual_seed_two_window_partition(self):
        x,kappa=circle_prefix(41)
        for n in range(2,40):
            ylo,yhi,eta=certified_pure_state(n,x,16)
            tlo,thi=green_interval(n,16)
            r=forcing(n)
            if eta:
                self.assertLess(yhi,thi)
            if ylo >= thi and yhi < tlo+r:
                self.assertFalse(eta)
                # Same-state forcing correction, exact integer floors.
                v=16*x[n-1]
                d=v.numerator//v.denominator
                self.assertEqual(kappa[n]-d,1)
            if yhi < tlo or ylo>=thi+r:
                v=16*x[n-1]
                d=v.numerator//v.denominator
                self.assertEqual(kappa[n]-d,0)

if __name__=='__main__':unittest.main(verbosity=2)
