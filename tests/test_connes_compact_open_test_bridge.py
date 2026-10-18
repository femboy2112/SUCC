"""Exact independent local p-adic Haar/Connes off-identity test controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.connes_compact_open_test_bridge import (
    LocalTraceTestError, LocalScaleBall, vp, abs_p, local_linear_test_pairing,
)
from observational_succ.connes_oriented_scaling import (
    local_fixed_point, RationalScale,
)


class ConnesCompactOpenTraceTests(unittest.TestCase):
    def test_independent_residue_Haar_oracle_for_unit_balls(self):
        for p,c,r in ((2,3,2),(3,4,2),(5,6,2),(2,5,3),(3,10,3)):
            x=LocalScaleBall(p,Q(c),r)
            M=r+3
            modulus=p**M
            brute=sum(u%p != 0 and (u-c)%p**r==0 for u in range(modulus))
            phi=(p-1)*p**(M-1)
            self.assertEqual(x.multiplicative_volume,Q(brute,phi))
            self.assertEqual(x.trace_pairing,x.multiplicative_volume*x.off_identity_scalar)
            self.assertTrue(x.receipt()['test_is_genuine_locally_constant_compact_support'])
            self.assertFalse(x.receipt()['identity_contact_known'])

    def test_actual_local_connes_fixed_point_scalar_matches_original_source(self):
        for p,c,r in ((2,Q(3),2),(3,Q(4),2),(5,Q(6),2),
                      (2,Q(1,2),1),(3,Q(1,3),1),
                      (2,Q(5,2),2),(3,Q(2,3),2)):
            ball=LocalScaleBall(p,c,r)
            fixed=local_fixed_point(RationalScale(c),p,8)
            self.assertTrue(fixed.stabilized)
            self.assertEqual(ball.off_identity_scalar,fixed.off_identity_coefficient)
            self.assertEqual(ball.trace_pairing,
                             ball.additive_volume/
                             ((1-Q(1,p))*abs_p(c,p)*abs_p(1-c,p)))

    def test_reciprocal_ball_Haar_and_symmetric_trace_transport(self):
        for p,c,r in ((2,Q(3),2),(3,Q(4),2),(5,Q(6),2),
                      (2,Q(1,2),1),(3,Q(1,3),1),
                      (2,Q(4),3),(3,Q(9),3)):
            ball=LocalScaleBall(p,c,r)
            inverse=ball.inverse()
            self.assertEqual(inverse.inverse(),ball)
            self.assertEqual(ball.multiplicative_volume,inverse.multiplicative_volume)
            self.assertEqual(ball.half_density_integral_squared,inverse.half_density_integral_squared)
            self.assertTrue(ball.reciprocal_transport()['symmetric_half_density_invariant'])
            self.assertFalse(ball.reciprocal_transport()['all_place_Weil_identified'])

    def test_concrete_unit_normalizations(self):
        self.assertEqual(LocalScaleBall(2,Q(3),2).trace_pairing,Q(1))
        self.assertEqual(LocalScaleBall(3,Q(4),2).trace_pairing,Q(1,2))
        x=LocalScaleBall(2,Q(1,2),1)
        self.assertEqual(x.multiplicative_volume,Q(1,2))
        self.assertEqual(x.off_identity_scalar,Q(1,2))
        self.assertEqual(x.trace_pairing,Q(1,4))
        self.assertEqual(x.half_density_integral_squared,Q(1,8))

    def test_exact_linear_span_and_signed_coefficients(self):
        a=LocalScaleBall(2,Q(3),2)
        b=LocalScaleBall(2,Q(5),3)
        rec=local_linear_test_pairing(((a,Q(3,2)),(b,Q(-2)),(a,Q(1,2))))
        self.assertEqual(rec['test_integral'],2*a.trace_pairing-2*b.trace_pairing)
        self.assertTrue(rec['local_geometric_distribution_agreement'])
        self.assertFalse(rec['Weil_PSD_proved'])

    def test_fake_prime_identity_touch_measure_and_source_mutants(self):
        for p in (6,4,0,1,True,Q(2)):
            with self.assertRaises(LocalTraceTestError):
                LocalScaleBall(p,Q(3),2)
        for c in (0,1,True,2.0):
            with self.assertRaises(LocalTraceTestError):
                LocalScaleBall(2,c,3)
        with self.assertRaises(LocalTraceTestError):
            LocalScaleBall(2,Q(3),1)  # identity belongs to center+2 Z2
        with self.assertRaises(LocalTraceTestError):
            LocalScaleBall(2,Q(4),2)  # zero belongs to center+4 Z2
        with self.assertRaises(LocalTraceTestError):
            LocalScaleBall(2,Q(3),True)
        with self.assertRaises(LocalTraceTestError):
            LocalScaleBall(2,Q(3),2,source_id="")
        with self.assertRaises(LocalTraceTestError):
            LocalScaleBall(2,Q(3),2,epoch=True)
        with self.assertRaises(LocalTraceTestError):
            local_linear_test_pairing(((LocalScaleBall(2,Q(3),2),1),
                                        (LocalScaleBall(3,Q(4),2),1)))
        with self.assertRaises(LocalTraceTestError):
            local_linear_test_pairing(((LocalScaleBall(2,Q(3),2),True),))
        with self.assertRaises(LocalTraceTestError):
            vp(Q(0),2)


if __name__=="__main__":
    unittest.main()
