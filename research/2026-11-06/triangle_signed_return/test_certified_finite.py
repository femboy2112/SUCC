"""Scoped finite arithmetic certification checks; not an asymptotic normality proof."""
import unittest
from fractions import Fraction as F
from certified_finite import (arctan_bounds_inverse, pi_interval, error_budget,
                              approximate_real_character, certified_energy, run)
from experiment import raw_orbit

class FiniteIntervalControls(unittest.TestCase):
    def test_arctan_alternating_bounds(self):
        for a in (5,239):
            for terms in range(1,9):
                lo,hi = arctan_bounds_inverse(a,terms)
                self.assertLess(lo,hi)
                # Two successive partial sums bracket the infinite alternating sum.
                other = sum(((-1)**j * F(1,(2*j+1)*a**(2*j+1))
                            for j in range(terms+1)), F(0))
                self.assertLessEqual(lo,other)
                self.assertLessEqual(other,hi)
    def test_rational_pi_and_uniform_errors(self):
        lo,hi=pi_interval()
        self.assertLess(F(3),lo)
        self.assertLess(hi,F(22,7))
        mid,eps,err,actual=error_budget()
        self.assertTrue(lo<mid<hi)
        self.assertLess(actual,eps)
        self.assertLess(eps*(2+eps),err)
    def test_approximate_character_poles_and_periodicity(self):
        pi_mid,_,_,_=error_budget()
        for h in (1,2,-1):
            for x in (F(0),F(1,16),F(2,3),F(17,31)):
                a=approximate_real_character(x,h,pi_mid)
                b=approximate_real_character(x+1,h,pi_mid)
                self.assertEqual(a,b)
                self.assertTrue(all(isinstance(v,F) for v in a))
    def test_original_finite_certified_signs(self):
        report=run()
        self.assertEqual(report['pi_base16_normality'],'OPEN')
        self.assertEqual([(v['N'],v['h'],v['Q'],v['verdict']) for v in report['cases']], [
            (512,1,4,'CERTIFIED_BELOW_DIAGONAL'),
            (512,1,8,'CERTIFIED_ABOVE_DIAGONAL'),
            (512,1,16,'CERTIFIED_BELOW_DIAGONAL'),
            (768,2,4,'AMBIGUOUS'),
            (768,2,8,'CERTIFIED_BELOW_DIAGONAL'),
            (768,2,16,'CERTIFIED_BELOW_DIAGONAL')])

if __name__=='__main__':unittest.main()
