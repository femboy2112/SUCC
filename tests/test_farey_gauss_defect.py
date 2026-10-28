"""Independent finite checks of the exact geometric and logarithmic clocks."""
import sys
import unittest
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from observational_succ.farey_gauss_defect import (
    golden_path,golden_interval,log_integer_interval,gamma_interval,
    oily_defect_interval,gauss_digit_tail_interval,farey_mediant)

class FareyGaussTests(unittest.TestCase):
    def test_fibonacci_successor_and_determinant(self):
        seq=[Q(0),Q(1),Q(1,2),Q(2,3),Q(3,5),Q(5,8),Q(8,13)]
        self.assertEqual([golden_path(k) for k in range(len(seq))],seq)
        for n in range(1,60):
            x=golden_path(n)
            self.assertEqual(golden_path(n+1),1/(1+x))
            lo,hi=golden_interval(n)
            self.assertLess(hi-lo,Q(1,n))

    def test_exact_farey_neighbor_and_negative(self):
        self.assertEqual(farey_mediant((0,1),(1,0)),(1,1))
        self.assertEqual(farey_mediant((1,2),(2,3)),(3,5))
        with self.assertRaises(ValueError):farey_mediant((0,1),(2,3))

    def test_gauss_tail_telescope_interval(self):
        for N in (1,2,3,6,15,50):
            increments=[gauss_digit_tail_interval(k,22) for k in range(1,N+1)]
            low=sum((a for a,b in increments),Q())
            high=sum((b for a,b in increments),Q())
            target_low,target_high=log_integer_interval(N+1,22)
            self.assertLessEqual(low,target_high)
            self.assertGreaterEqual(high,target_low)

    def test_gamma_and_oily_certification(self):
        import math
        for n in (8,30,64,128):
            glo,ghi=gamma_interval(n)
            self.assertLess(float(glo),0.5772156649015329)
            self.assertGreater(float(ghi),0.5772156649015329)
            lo,hi=oily_defect_interval(n)
            omega=(math.sqrt(5)-1)/2-0.5772156649015329
            self.assertLess(float(lo),omega)
            self.assertGreater(float(hi),omega)
        self.assertGreater(oily_defect_interval(64)[0],0)

    def test_rejects_wrong_types_and_invalid_ranges(self):
        for bad in (-1,0,1.5):
            with self.assertRaises(ValueError):gamma_interval(bad)
        with self.assertRaises(ValueError):golden_path(True)
        with self.assertRaises(ValueError):log_integer_interval(2,0)

if __name__=='__main__':unittest.main()
