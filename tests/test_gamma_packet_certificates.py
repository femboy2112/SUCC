"""Source-gated finite real Gamma packets, exact rational and adversarial."""
import unittest
from fractions import Fraction as F
from observational_succ.gamma_packet_certificates import (
    PacketError, finite_packet_lower, finite_repair_bound,
    original_fifth_mode_packet, paired_mode_negative_control,
)
from observational_succ.gamma_fredholm_completion import (
    gamma_tail_H01_lower,gamma_tail_source_upper,
)


class ExactPacketAlgebra(unittest.TestCase):
    def test_rung_packet_is_difference_of_true_tail_bounds(self):
        n,d=F(2136,77),F(1296)
        for stop in (65,128,192,200,256,512):
            self.assertEqual(finite_packet_lower(64,stop,n,d),
                             gamma_tail_H01_lower(64,n,d)-gamma_tail_source_upper(stop,n))

    def test_certificate_depth_monotonic(self):
        n,d=F(2136,77),F(1296)
        seq=[finite_packet_lower(64,j,n,d) for j in (65,100,128,200,256,512)]
        self.assertEqual(seq,sorted(seq))

    def test_bounded_finite_repair_synthetic(self):
        r=finite_repair_bound(64,-F(740,1000000),-F(739,1000000),F(2136,77),1296)
        self.assertLess(F(r["signed_prefix_interval"][1]),0)
        self.assertGreater(F(r["signed_energy_after_packet_lower"]),0)
        self.assertTrue(r["minimum_stop_under_THIS_bound"])
        self.assertFalse(r["actual_first_sign_crossing_found"])
        self.assertFalse(r["S4_positive_proved"])
        j=r["stop_exclusive"]
        self.assertLessEqual(-F(740,1000000)+finite_packet_lower(
            64,j-1,F(2136,77),1296),0)

    def test_signed_mode_coupling_counterexample(self):
        r=paired_mode_negative_control()
        self.assertEqual(r["basis_diagonal"],("1","1"))
        self.assertEqual(r["coupled_energy"],"-2")
        self.assertFalse(r["authentic_negative_witness"])

    def test_fail_closed(self):
        for a,b in ((0,64),(64,64),(65,64),(True,65),(64,65.1)):
            with self.assertRaises(PacketError):
                finite_packet_lower(a,b,1,0)
        for x in (True,1.2,"1/0"):
            with self.assertRaises(PacketError):
                finite_packet_lower(64,65,x,0)
        for args in ((64,1,2,1,0),(64,-1,0,1,0),
                     (64,-100,-99,1,0),(64,2,1,1,0)):
            with self.assertRaises(PacketError):
                finite_repair_bound(*args)
        with self.assertRaises(PacketError):
            finite_repair_bound(64,-F(740,10**6),-F(739,10**6),
                                 F(2136,77),1296,max_stop=65)


class ActualSuzukiSource(unittest.TestCase):
    def test_original_strict_finite_gamma_packet(self):
        try:
            import observational_succ.tate_suzuki_shorting
        except ImportError:
            self.skipTest("Original frozen Suzuki signed source unavailable")
        r=original_fifth_mode_packet()
        self.assertEqual(r["source_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(r["prime_wavefront"],((2,2),))
        self.assertEqual(r["start"],64)
        self.assertGreater(r["stop_exclusive"],64)
        self.assertGreater(F(r["consecutive_original_gamma_packet_lower"]),0)
        self.assertGreater(F(r["signed_energy_after_packet_lower"]),0)
        self.assertFalse(r["S4_positive_proved"])
        self.assertFalse(r["RH_proved"])


if __name__=="__main__":
    unittest.main()
