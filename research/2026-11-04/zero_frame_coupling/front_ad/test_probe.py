import unittest
from fractions import Fraction as F
import probe


class SourceJetRigidityTests(unittest.TestCase):
    def test_complete_exact_receipt(self):
        result=probe.run()
        self.assertEqual(result['status'],'EXACT_SOURCE_JET_AND_SEED_CHECKS_PASS')
        self.assertEqual(result['exact_seed_rotation_checks'],504)
        self.assertEqual(result['first_carry_disagreement_seed_1_over_5'],1)

    def test_density_ratio_on_exact_rational_arguments(self):
        for t in (F(1,7),F(2,5),F(3,5),F(4,5),F(9,10)):
            po=sum((c*t**j for j,c in enumerate(probe.ORIG)),F(0))
            pr=sum((c*t**j for j,c in enumerate(probe.RAD)),F(0))
            rho=-pr/(16-t**8)
            ratio=4*(t-1)*(16-t**8)/(t**8*(t*t-4*t+2))
            self.assertEqual(po/(t**8*rho),ratio)

    def test_canonical_extra_order_can_worsen_residual(self):
        b=probe.series_coefficients(192)
        z=probe.source_stream(193,probe.RAD)
        e64=probe.residual(1,64,b,z)
        e128=probe.residual(1,128,b,z)
        e192=probe.residual(1,192,b,z)
        self.assertLess(e64,e128)
        self.assertLess(e128,e192)
        self.assertGreater(e192,probe.forcing(1,probe.ORIG))

    def test_nonresonant_seed_is_visible_to_first_lag(self):
        self.assertNotEqual((15*F(1,7))%1,0)
        self.assertEqual((15*F(1,5))%1,0)


if __name__=='__main__':
    unittest.main()
