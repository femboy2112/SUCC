"""Live SUCC integration tests; require the COMPLETE repo checkout.

Intentionally not part of the local partial-checkout 30-method report.
Hosted CI should exercise this against actual existing source modules.
"""
import unittest
from fractions import Fraction as Q

from observational_succ.bbp_natural_carrier import exact_forcing, orbit_state
from observational_succ.bbp_source_memory import forcing
from observational_succ.pi_succ_lag_bridge import lag_source
from observational_succ.pascal_lucas_quotient import zeta_apply
from observational_succ.harmonic_mirror_succ import (
    bbp_mirror_forcing, unipotent_shear, source_pole_moment,
)


class LiveSUCCMirrorIntegration(unittest.TestCase):
    def test_three_authentic_forcing_implementations_agree(self):
        for n in range(1,65):
            self.assertEqual(bbp_mirror_forcing(n), exact_forcing(n))
            self.assertEqual(bbp_mirror_forcing(n), forcing(n))

    def test_natural_section_obeys_original_four_rays(self):
        for n in range(0,23):
            self.assertEqual(orbit_state(n+1).rational,
                16*orbit_state(n).rational+bbp_mirror_forcing(n+1))

    def test_harmonic_source_lag_is_lifted_not_circle_model(self):
        for n,k in ((1,1),(1,3),(5,2),(7,4),(11,5)):
            self.assertEqual(orbit_state(n+k).rational-16**k*orbit_state(n).rational,
                             lag_source(n,k))

    def test_same_unipotent_one_digit_generator_different_types(self):
        self.assertEqual(unipotent_shear(1),((1,0),(1,1)))
        self.assertEqual(zeta_apply(2,1,(Q(3),Q(5))), (Q(3),Q(8)))
        self.assertEqual(source_pole_moment(0),0)
        self.assertEqual(source_pole_moment(1),15)

if __name__=="__main__": unittest.main()
