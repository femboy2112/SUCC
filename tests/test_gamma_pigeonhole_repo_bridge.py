"""Native SUCC arithmetic bridge: run in actual repo checkout, not isolated scratch."""
import sys
import unittest
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"research"/"2026-11-04"/"gamma_pigeonhole"))
from gamma_pigeonhole import forcing,clock_state,birth_register,prime
from observational_succ.integer_bbp_carrier import (forcing_pair,source_states,step)
from observational_succ.bbp_natural_carrier import orbit_state


class GammaNativeSourceBridge(unittest.TestCase):
    def test_exact_forcing_reduced_pair(self):
        for n in range(1,101):
            x=forcing(n)
            self.assertEqual(forcing_pair(n),(x.numerator,x.denominator))

    def test_original_zero_seed_common_lcm_and_numerator(self):
        states=source_states(64)
        for n in (0,1,2,3,6,10,12,13,24,40,64):
            a,q,_=clock_state(n)
            self.assertEqual((a,q),(states[n].numerator,states[n].conductor))
            self.assertEqual(F(a,q),orbit_state(n).rational)

    def test_p_birth_passport_checked_against_canonical_lift(self):
        states=source_states(40)
        for n in (3,6,10,12,13,15,18,30,40):
            if prime(8*n-7):
                z=birth_register(n)
                self.assertEqual(z["A"],states[n].numerator)
                self.assertEqual(z["Q"],states[n].conductor)
                self.assertEqual(z["p_residue"],4)

if __name__=="__main__":
    unittest.main()
