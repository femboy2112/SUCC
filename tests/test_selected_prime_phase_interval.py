"""True rational-interval certified finite joint signed BBP interference, not normality."""
from __future__ import annotations
import json
from fractions import Fraction as F
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/'research/2026-11-01/selected_prime_phase'
if str(DIR) not in sys.path:sys.path.insert(0,str(DIR))
from finite_interval_oracle import arctan_bounds,pi_bounds,exp_phase_interval,certify
from prime_phase import birth


class SelectedPrimeIntervalTests(unittest.TestCase):
    def test_independent_machin_pi_enclosure(self):
        lo,hi=pi_bounds()
        self.assertLess(F(3),lo)
        self.assertLess(lo,hi)
        self.assertLess(hi,F(22,7))
        a,b=arctan_bounds(F(1,5))
        self.assertGreater(b-a,F(0))
        self.assertLess(b-a,F(1,10**20))

    def test_phase_error_all_rational(self):
        for x in [F(1,3),F(1234,5671),F(0),F(1,257),F(256,257)]:
            co,si,err=exp_phase_interval(x,3,pi_bounds())
            self.assertTrue(isinstance(co,F) and isinstance(si,F))
            self.assertLess(err,F(1,10**8))

    def test_exact_joint_signed_cancellation(self):
        d=certify()
        self.assertEqual(d['status'],'CERTIFIED_EXACT_RATIONAL_INTERVAL')
        for case in d['cases']:
            threshold=F(1,16) if case['h']==1 else F(1,8)
            self.assertLess(F(case['upper_L1']),threshold)
            self.assertEqual(F(case['certified_strict_less_than']),threshold)
            for axis in ('real_interval','imag_interval'):
                self.assertLess(F(case[axis][0]),F(case[axis][1]))

    def test_exact_receipt_roundtrip(self):
        saved=json.loads((DIR/'FINITE_SIGNED_INTERVAL_RECEIPT.json').read_text())
        self.assertEqual(certify(),saved)

    def test_primary_period_four_vs_original_joint(self):
        b=birth(257)
        self.assertEqual((b.n,b.first_reuse,b.length),(33,129,96))
        # Strict rational lower bound for the primary-only 96-step mean.
        lower=(F(1)-F(176,1799)**2/F(2))/F(2)
        self.assertGreater(lower,F(49,100))
        joint=next(c for c in certify()['cases'] if c['h']==1)
        self.assertLess(F(joint['upper_L1']),F(1,16))
        self.assertGreater(lower-F(joint['upper_L1']),F(2,5))

if __name__=='__main__':unittest.main()
