"""Exact rational Weyl-orbit source-selection *error* gates, not cancellation."""
import unittest
from fractions import Fraction as Q
from observational_succ.vacuum_phase_transport import certified_weyl_phase_transport
from observational_succ.vacuum_parameter_bbp import VacuumBridgeError, krylov_certificate

class WeylSelectedFiniteHorizonTests(unittest.TestCase):
    def test_exact_proved_phase_bound(self):
        for h,N,d in ((1,8,3),(1,16,6),(1,24,8),(1,32,11),(3,12,6)):
            x=certified_weyl_phase_transport(h,N,d)
            c=krylov_certificate(d)
            self.assertEqual(x.rational_reference,(c.lower+c.upper)/2)
            self.assertEqual(x.pi_distance_cap,(c.upper-c.lower)/2)
            self.assertEqual(x.normalized_weyl_gap_cap,
                  Q(8*abs(h)*(16**N-1),15*N)*x.pi_distance_cap)
            self.assertEqual(x.absolute_weyl_gap_cap,N*x.normalized_weyl_gap_cap)
            self.assertTrue(x.bound_is_source_selected)
            self.assertFalse(x.cancellation_proved)
    def test_two_sided_phase_budget_becomes_small_linearly_in_horizon(self):
        for N,d in ((8,3),(16,6),(24,8),(32,11)):
            b=certified_weyl_phase_transport(1,N,d)
            self.assertLess(b.normalized_weyl_gap_cap,Q(1,1000))
    def test_nonzero_character_and_domain_restrictions(self):
        for args in ((0,10,3),(1,0,3),(1,10,0),('h',2,2)):
            with self.assertRaises(VacuumBridgeError):certified_weyl_phase_transport(*args)
    def test_frequency_scaling_symmetry(self):
        x=certified_weyl_phase_transport(1,12,6)
        y=certified_weyl_phase_transport(-3,12,6)
        self.assertEqual(y.normalized_weyl_gap_cap,3*x.normalized_weyl_gap_cap)

if __name__=='__main__':unittest.main()
