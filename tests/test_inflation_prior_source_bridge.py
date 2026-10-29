"""Source identity checks against existing SUCC Main XIII/PR344 Oily modules."""
import unittest
from fractions import Fraction as F

from observational_succ.causal_inflation_prior import oily_parameters, oily_matrix_power
from observational_succ.bbp_virtual_seed_prior import authentic_forcing
from observational_succ.chiral_virtual_phase_prior import authentic_chiral_tap

try:
    from observational_succ.wavefront_oracle_two_stage import SourceGeometry
    from observational_succ.wavefront_oscillator_completion import (
        oily_packet_matrix,packet_matrix_coefficient,stationary_oily_source,
        source_signed_tap,signed_four_pole_moment,
    )
except ImportError:
    SourceGeometry=None


@unittest.skipIf(SourceGeometry is None, 'requires PR344 modules in checked-out source tree')
class FullSourceBridgeTests(unittest.TestCase):
    def test_original_two_loop_rates_match_main(self):
        for x in (F(0),F(1,8),F(1,2),F(3,4),F(1)):
            s=SourceGeometry(x)
            self.assertEqual((s.u,s.v),oily_parameters(x))
            self.assertEqual(oily_packet_matrix(x),oily_matrix_power(x,1))

    def test_exact_packet_grade_and_resolvent_reconstruction(self):
        for x in (F(0),F(1,5),F(1,2),F(4,5),F(1)):
            for j in range(12):
                self.assertEqual(packet_matrix_coefficient(x,j),
                                 (1-x)/4*oily_matrix_power(x,j+1)[0][1])
            if x<1:
                u,v=oily_parameters(x)
                self.assertEqual(stationary_oily_source(x),F(1-x,4)/(1-u)/(1-v))

    def test_literal_signed_four_poles_unchanged(self):
        for n in range(1,64):
            self.assertEqual(authentic_forcing(n),signed_four_pole_moment(n))

    def test_exact_contracting_source_chiral_taps(self):
        for n in range(96):
            self.assertEqual(authentic_chiral_tap(n),source_signed_tap(n))

if __name__=='__main__':unittest.main()
