from fractions import Fraction as Q
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import independent_phase_check as pc
import carry_controls as cc


class IndependentPhaseArithmetic(unittest.TestCase):
    def test_dyadic_modular_sum_contains_separate_fraction_recurrence(self):
        states,_=cc.unwrapped(80)
        for n in (1,2,3,7,17,31,59,80):
            for bits in (20,64,192):
                lo,hi,scale,terms=pc.modular_source_interval(n,bits)
                x=states[n] % 1
                self.assertEqual(terms,4*n)
                # The returned lift may straddle the cut at 1; test all
                # possible neighboring integer translates without rounding.
                self.assertTrue(any(Q(lo,scale)<=x+k<=Q(hi,scale) for k in (-1,0,1)))

    def test_exact_binary_endpoint_conversion(self):
        self.assertEqual(pc.endpoint_fraction((0,3,-7,2)),Q(3,128))
        self.assertEqual(pc.endpoint_fraction((1,5,8,3)),Q(-1280))
        self.assertEqual(pc.endpoint_fraction((0,0,0,0)),0)


if __name__=='__main__':
    unittest.main()
