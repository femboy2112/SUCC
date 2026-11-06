"""Hosted-checkout bridge to SUCC's existing integer source carriers.

Cannot be executed in standalone staging without the actual SUCC package.
No copy of the original production source is made into this research package.
"""
import sys
import unittest
from pathlib import Path
from math import lcm

BASE=Path(__file__).resolve().parents[1]/'research'/'2026-11-04'/'source_sound_calculus'
sys.path.insert(0,str(BASE))
from lcm_carrier import bbp_prefix, source_subgroup_clock, force, phase_address

from observational_succ.integer_bbp_carrier import source_states,forcing_pair,common_clock,step
from observational_succ.bbp_natural_carrier import orbit_state

class HostedNativeSUCCBridge(unittest.TestCase):
    def test_two_existing_bbp_engines_agree_with_lcm_source(self):
        a=bbp_prefix(32)
        b=source_states(32)
        self.assertEqual(len(a),len(b))
        for n,(x,y) in enumerate(zip(a,b)):
            self.assertEqual((x.time,x.clock,x.numerator), (y.n,y.conductor,y.numerator))
            self.assertEqual(x.unwrapped,orbit_state(n).rational)
            self.assertEqual(source_subgroup_clock(n),x.clock)
            if n:
                self.assertEqual(x.last_carry,step(b[n-1])[1])

    def test_forcing_is_the_immutable_real_source(self):
        for n in range(1,120):
            num,den=forcing_pair(n)
            self.assertEqual(force(n).numerator,num)
            self.assertEqual(force(n).denominator,den)

    def test_common_clock_maps_every_selected_phase_without_loss(self):
        states=source_states(40)
        M,addresses=common_clock(states)
        self.assertEqual(M,source_subgroup_clock(40))
        for s,addr in zip(states,addresses):
            self.assertEqual(addr,phase_address(s.remainder,s.conductor,M))
