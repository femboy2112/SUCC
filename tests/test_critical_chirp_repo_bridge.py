"""Only in actual SUCC checkout: test source contract and both native integer lifts."""
import sys,unittest
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'research'/'2026-11-04'/'critical_chirp'))
from critical_chirp import forcing,forcing_polynomial,exact_phase_epoch
from observational_succ.integer_bbp_carrier import forcing_pair,source_states
from observational_succ.bbp_natural_carrier import orbit_state

class SourceNativeChirpBridge(unittest.TestCase):
    def test_original_immutable_forcing_pairs(self):
        for n in range(1,121):
            r=forcing(n)
            self.assertEqual(r,forcing_polynomial(n))
            self.assertEqual((r.numerator,r.denominator),forcing_pair(n))

    def test_unwrapped_zero_seed_and_lcm(self):
        states=source_states(120)
        u=F(0)
        for n in range(0,121):
            if n>0: u=16*u+forcing(n)
            self.assertEqual(F(states[n].numerator,states[n].conductor),u)
            if n in (0,1,2,3,6,16,40,80,120):
                self.assertEqual(orbit_state(n).rational,u)

    def test_original_circle_epoch(self):
        s=source_states(96)
        for A in (8,16,32,48):
            a=exact_phase_epoch(A)
            b=tuple(F(x.remainder,x.conductor) for x in s[A:2*A])
            self.assertEqual(a,b)
