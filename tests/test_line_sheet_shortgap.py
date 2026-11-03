"""Finite original BBP prime-product nonrepeat controls, NOT scale proof."""
import importlib.util
import math
import unittest
from pathlib import Path
P=Path(__file__).resolve().parents[1]/'research'/'2026-11-02'/'line_sheet_gamma'/'line_sheet.py'
S=importlib.util.spec_from_file_location('line_sheet_nonrepeat',P)
ls=importlib.util.module_from_spec(S);S.loader.exec_module(ls)

class ShortGapSourceControls(unittest.TestCase):
    def test_short_lag_multi_prime_nonalias_on_finite_epochs(self):
        for A in (32,64,128,256,512):
            ps=ls.epoch_prime_family(A)
            for d in range(1,A//5+1):
                self.assertTrue(any(pow(16,d,p)!=1 for p in ps))

    def test_original_rational_selected_phase_nonrepeat(self):
        for A in (16,32,64,128):
            U=ls.original_states(2*A-1)
            for n in range(A,2*A):
                for d in range(1,min(A//5+1,2*A-n)):
                    self.assertNotEqual((U[n+d]-U[n]).denominator,1)
                    self.assertNotEqual((3*(U[n+d]-U[n])).denominator,1)

    def test_finite_prime_logmass_exceeds_shortlag(self):
        for A in (64,128,256,512):
            ps=ls.epoch_prime_family(A)
            # This is a finite diagnostic. Asymptotic log product=A+o(A)
            # follows from classical PNT in progression, not these checks.
            self.assertGreater(sum(math.log(p) for p in ps),
                               (A//5)*math.log(16))

if __name__=='__main__': unittest.main()
