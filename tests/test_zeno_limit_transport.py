"""Zeno finite SUCC, Achilles/Arrow/Stadium and analytic failure controls."""
import unittest
from fractions import Fraction as Q
from observational_succ import zeno_limit_transport as z


class GeometricZenoTests(unittest.TestCase):
    def setUp(self):
        self.s=z.GeometricSUCC("real-math-source",3,"rational-line",0,1,Q(1,2))

    def test_exact_succ_closed_form(self):
        for n in range(25):
            self.assertEqual(self.s.state(n),1-Q(1,2**n))
            self.assertEqual(self.s.signed_remainder(n),Q(1,2**n))
            self.assertEqual(self.s.successor(n),self.s.state(n+1))
            self.assertLess(self.s.state(n),1)

    def test_clock_ordinal_report_is_not_a_physical_supertask(self):
        for n in range(30):
            self.assertEqual(self.s.finite_clock(n),1-Q(1,2**n))
            self.assertLess(self.s.finite_clock(n),1)
        self.assertFalse(self.s.cauchy_pair(3,20)["proves_physical_omega_action"])

    def test_zeno_cauchy_and_explicit_modulus(self):
        for n in range(8):
            for m in range(n,25):
                cert=self.s.cauchy_pair(n,m)
                self.assertLessEqual(cert["separation"],cert["tail_upper"])
                self.assertEqual(cert["tail_upper"],Q(1,2**n))
        self.assertEqual(self.s.modulus(Q(1,100)),7)
        self.assertEqual(self.s.modulus(Q(1,1024)),10)
        for n in range(1,11):
            self.assertLessEqual(self.s.error(self.s.modulus(Q(1,2**n))),
                                 Q(1,2**n))
        with self.assertRaises(z.ZenoError):
            self.s.modulus(Q(1,2**30),budget=10)

    def test_affine_transport_uses_proved_lipschitz_law(self):
        for n in (0,1,3,10):
            data=self.s.affine_observer(n,Q(-3,2),Q(4))
            self.assertEqual(data["global_target"],Q(5,2))
            self.assertEqual(data["Lipschitz"],Q(3,2))
            self.assertTrue(data["lower"]<=Q(5,2)<=data["upper"])
            self.assertFalse(data["physical_infinite_run_certified"])

    def test_source_stamp_mismatch_is_not_permitted(self):
        with self.assertRaises(z.ZenoError):
            z.GeometricSUCC("",0,"b",0,1,Q(1,2))
        with self.assertRaises(z.ZenoError):
            z.GeometricSUCC("s",-1,"b",0,1,Q(1,2))
        with self.assertRaises(z.ZenoError):
            z.GeometricSUCC("s",0,"b",0,1,0.5)
        with self.assertRaises(z.ZenoError):
            z.GeometricSUCC("s",0,"b",0,1,1)

    def test_all_finite_snapshots_miss_endpoint(self):
        for n in (1,2,3,4,8,20):
            assert self.s.state(n)<1
            a,b=self.s.interval(n)
            self.assertTrue(a<=1<=b)


class ZenoFourMotionControls(unittest.TestCase):
    def test_achilles_and_tortoise_exact_source(self):
        A=z.AchillesSUCC(Q(9,10),Q(1),Q(1,10))
        self.assertEqual(A.ratio,Q(1,10))
        self.assertEqual(A.catch_time,Q(1))
        for n in range(1,8):
            c=A.finite_checkpoint(n)
            self.assertEqual(c["time"],1-Q(1,10**n))
            self.assertEqual(c["remaining_gap"],Q(9,10**(n+1)))
            self.assertGreater(c["remaining_gap"],0)
            self.assertFalse(c["infinite_catchup_actions_executed"])

    def test_stationary_tortoise_and_invalid_speeds(self):
        A=z.AchillesSUCC(Q(3),Q(3),Q(0))
        self.assertEqual(A.finite_checkpoint(1)["remaining_gap"],0)
        for fn in (
            lambda:z.AchillesSUCC(Q(-1),1,0),
            lambda:z.AchillesSUCC(1,1,1),
            lambda:z.AchillesSUCC(1,1,2),
            lambda:z.AchillesSUCC(1,1,0.5),
        ):
            with self.assertRaises(z.ZenoError):fn()

    def test_arrow_instant_snapshot_does_not_identify_velocity(self):
        x=z.arrow_snapshot_alias(Q(7,4))
        self.assertEqual(x["static_readout"],0)
        self.assertEqual(x["velocity_candidates"],(Q(0),Q(1)))
        self.assertFalse(x["instantaneous_velocity_identified_from_position_only"])
        self.assertEqual(x["future_delta_at_t0_plus_one"],1)

    def test_stadium_frame_transport_control(self):
        s=z.stadium_relative_frame(Q(1,2))
        self.assertEqual(s["relative_displacement"],1)
        self.assertEqual(s["one_body_displacement"],Q(1,2))
        self.assertEqual(s["relative_speed"],2)
        self.assertFalse(s["independent_interleaved_clocks_validated"])


class PropertyTransportNegativeTests(unittest.TestCase):
    def test_pointwise_limit_not_uniform(self):
        for n in (1,2,3,4,5,10,50,100):
            witness=z.pointwise_nonuniform_witness(n)
            self.assertGreaterEqual(witness["finite_value"],Q(1,2))
            self.assertLess(witness["point"],1)
            self.assertFalse(witness["closedness_preservation_from_pointwise_claimed"])

    def test_uniform_functions_not_uniform_derivatives(self):
        for n in (1,2,4,8,32,128):
            result=z.derivative_nontransport(n)
            self.assertEqual(result["uniform_function_error_bound"],Q(1,n))
            self.assertEqual(result["derivative_at_one"],1)
            self.assertEqual(result["limit_function_derivative_at_one"],0)

    def test_analytic_continuation_stability_is_not_identity(self):
        for n in (1,2,4,12,30):
            report=z.analytic_continuation_instability(n)
            self.assertEqual(report["inner_sup_upper"]*report["value_at_z_four"],1)
            self.assertFalse(report["numerical_continuation_stable_without_growth_bound"])
            self.assertFalse(report["identity_theorem_violated"])

    def test_generic_future_halting_alias(self):
        for horizon in (0,2,10,50):
            c=z.halting_alias_at_finite_horizon(horizon,horizon+101)
            self.assertEqual(c["candidate_limits"],(Q(),Q(1)))
            self.assertFalse(c["finite_prefix_identifies_global_limit"])
        with self.assertRaises(z.ZenoError):
            z.halting_alias_at_finite_horizon(5,4)

    def test_unsound_infinitary_input_types(self):
        s=z.GeometricSUCC("s",0,"b",0,1,Q(1,2))
        with self.assertRaises(z.ZenoError):s.state(4.0)
        with self.assertRaises(z.ZenoError):s.cauchy_pair(5,4)
        with self.assertRaises(z.ZenoError):s.modulus(0)
        with self.assertRaises(z.ZenoError):s.affine_observer(2,0.5,0)


if __name__=="__main__":
    unittest.main()
