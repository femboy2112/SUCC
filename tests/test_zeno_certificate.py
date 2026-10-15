"""Exact, source-qualified hostile controls for the Zeno SUCC paper theorems."""
from __future__ import annotations

import itertools
import unittest
from fractions import Fraction as F

from observational_succ.zeno_certificate import (
    Stamp, GeometricZeno, AchillesZeno, RationalRootBracket,
    ThomsonLamp, HiddenTailMutant, IntervalEvidence, FormalLimit,
    enclosed_limit_sign, signed_weil_zeno_gate, gamma_tail_budget,
    gamma_tail_partial, gemini_bad_gamma_bound, hilbert_shadow,
    arrow_snapshot_countermodel, stadium_relative_motion, typed_history,
    ZenoTypeError, meta_limit_dependency,
)

SOURCE = Stamp("authentic-zeta", 0, "log-half-density", "test-H1(-a,a)")
OTHER = Stamp("fake-six", 0, "log-half-density", "test-H1(-a,a)")
EPOCH = Stamp("authentic-zeta", 1, "log-half-density", "test-H1(-a,a)")
BASIS = Stamp("authentic-zeta", 0, "wrong-density", "test-H1(-a,a)")
DOMAIN = Stamp("authentic-zeta", 0, "log-half-density", "test-L2")

class TestDichotomy(unittest.TestCase):
    def setUp(self):
        self.z = GeometricZeno(SOURCE, 0, F(1,2), F(1,2))

    def test_exact_universal_stage_law_cases(self):
        for n in range(36):
            self.assertEqual(self.z.stage(n), 1-F(1,2**n))
            self.assertEqual(self.z.increment_at(n), F(1,2**(n+1)))
            self.assertEqual(self.z.tail(n), F(1,2**n))
            self.assertEqual(self.z.stage(n+1)-self.z.stage(n),self.z.increment_at(n))

    def test_limit_is_math_not_event(self):
        a = self.z.mathematical_limit()
        self.assertEqual(a.value,1)
        self.assertFalse(a.physical_event_executed)
        for n in range(50):
            self.assertLess(self.z.stage(n),a.value)
            self.assertTrue(self.z.finite_error_certificate(n)["passes_exact_identity"])

    def test_binary_modulus_exact(self):
        for k in range(30):
            n=self.z.stage_for_dyadic_error(k)
            self.assertEqual(n,k)
            self.assertLessEqual(self.z.tail(n),F(1,2**k))
            if n: self.assertGreater(self.z.tail(n-1),F(1,2**k))

    def test_general_ratios_and_nonzero_origins(self):
        for inc,ratio in itertools.product((F(1),F(7,5),F(0)),(F(0),F(1,3),F(2,5),F(9,10))):
            z=GeometricZeno(SOURCE,F(-4,3),inc,ratio)
            for n in range(20):
                self.assertTrue(z.finite_error_certificate(n)["passes_exact_identity"])
                self.assertGreaterEqual(z.tail(n),0)
                if n>=1: self.assertLessEqual(z.tail(n),z.tail(n-1))
            m=z.stage_for_dyadic_error(7)
            self.assertLessEqual(z.tail(m),F(1,128))

    def test_reject_float_and_noncontraction(self):
        for rate in (F(1),F(2),F(-1)):
            with self.assertRaises(ZenoTypeError):GeometricZeno(SOURCE,0,1,rate)
        with self.assertRaises(ZenoTypeError):GeometricZeno(SOURCE,0,F(-1),F(1,2))
        with self.assertRaises(ZenoTypeError):GeometricZeno(SOURCE,0,1,0.5)
        with self.assertRaises(ZenoTypeError):self.z.stage(-1)

    def test_omega_not_performed(self):
        for n in (0,1,1000):
            h=typed_history(n)
            self.assertEqual(h["finite_steps"],n)
            self.assertFalse(h["mathematical_limit_entails_executed_event"])
            self.assertFalse(h["a_last_omega_event"])
        with self.assertRaises(ZenoTypeError):FormalLimit(SOURCE,F(1),physical_event_executed=True)

class TestAchilles(unittest.TestCase):
    def test_positive_speed_loop(self):
        for gap,va,vt in ((1,3,1),(7,5,2),(3,10,9),(2,4,0)):
            a=AchillesZeno(SOURCE,F(gap),F(va),F(vt))
            self.assertEqual(a.catch_time,F(gap,va-vt))
            for n in range(20):
                self.assertTrue(a.finite_identity(n))
                self.assertEqual(a.catch_time-a.time_at(n),a.catch_time*a.ratio**n)
                self.assertGreaterEqual(a.gap_at(n),0)

    def test_wrong_speed_disallowed(self):
        for vt in (3,4):
            with self.assertRaises(ZenoTypeError):AchillesZeno(SOURCE,1,3,vt)

class TestArrowAndStadium(unittest.TestCase):
    def test_single_snapshot_cannot_determine_velocity(self):
        r=arrow_snapshot_countermodel()
        self.assertTrue(r["same_position"])
        self.assertEqual(r["instantaneous_displacement"],0)
        self.assertNotEqual(r["velocity_static"],r["velocity_moving"])

    def test_stadium_relative_frame_and_time(self):
        for d,v in itertools.product((F(1,6),F(1),F(7,4)),(F(1),F(3,5))):
            x=stadium_relative_motion(d,v)
            self.assertEqual(x["B_vs_C_distance"],2*x["B_vs_A_distance"])
            self.assertEqual(x["time_from_A"],x["time_from_C"])
            self.assertEqual(x["time_from_A"],d)

class TestCompletionAndNoGhost(unittest.TestCase):
    def test_sqrt2_nested_rational_intervals_real_not_Q(self):
        x=RationalRootBracket(SOURCE)
        prev=(F(1),F(2))
        for n in range(50):
            lo,hi=x.bounds(n)
            self.assertLess(lo*lo,2)
            self.assertGreater(hi*hi,2)
            self.assertEqual(hi-lo,F(1,2**n))
            self.assertGreaterEqual(lo,prev[0])
            self.assertLessEqual(hi,prev[1])
            prev=lo,hi
        self.assertIn("NO_RATIONAL_ROOT",x.source_actualization())

    def test_thomson_lamp_time_converges_state_does_not(self):
        x=ThomsonLamp(SOURCE)
        self.assertFalse(x.convergent_endpoint_in_discrete_bits())
        for n in range(100):
            self.assertEqual(1-x.time_at(n),F(1,2**n))
            self.assertNotEqual(x.state_at(n),x.state_at(n+1))

    def test_no_uniform_tail_from_finite_prefix(self):
        for n in range(22):
            m=HiddenTailMutant(SOURCE,n)
            self.assertTrue(m.same_prefix())
            self.assertEqual(m.limit_pair(),(1,2))
            self.assertEqual(m.baseline(n),m.mutated(n))
            self.assertEqual(m.mutated(n+1)-m.baseline(n+1),1)

    def test_source_bearing_gate(self):
        stage=IntervalEvidence(SOURCE,F(1,10),F(1,9))
        for s in (OTHER,EPOCH,BASIS,DOMAIN):
            with self.assertRaises(ZenoTypeError):stage.validate_same_source(s)
        self.assertFalse(meta_limit_dependency([(SOURCE,SOURCE),(SOURCE,EPOCH)]))
        self.assertTrue(meta_limit_dependency([(SOURCE,SOURCE)]))

class TestZenoPositiveCone(unittest.TestCase):
    def test_valid_closed_property_sign_budget(self):
        strong=IntervalEvidence(SOURCE,F(1,4),F(3,10))
        neg=IntervalEvidence(SOURCE,F(-3,10),F(-1,4))
        touch=IntervalEvidence(SOURCE,F(-1,100),F(1,100))
        self.assertIn("STRICT_POSITIVE",enclosed_limit_sign(strong,F(1,8),SOURCE))
        self.assertIn("STRICT_NEGATIVE",enclosed_limit_sign(neg,F(1,8),SOURCE))
        self.assertIn("UNDECIDED",enclosed_limit_sign(touch,F(1,8),SOURCE))

    def test_no_unlicensed_positive_slack(self):
        pos=IntervalEvidence(SOURCE,F(1,10),F(1,5))
        self.assertIn("UNDECIDED",enclosed_limit_sign(pos,F(1,4),SOURCE))
        with self.assertRaises(ZenoTypeError):enclosed_limit_sign(pos,F(-1),SOURCE)
        with self.assertRaises(ZenoTypeError):enclosed_limit_sign(pos,F(0),OTHER)

    def test_closed_vs_open_boundary_countermodel(self):
        z=GeometricZeno(SOURCE,0,F(1,2),F(1,2))
        for n in range(20):
            self.assertLess(z.stage(n),1)  # OPEN target is true at every finite n
        self.assertFalse(z.mathematical_limit().value<1) # but false at the limit
        for n in range(20): self.assertLessEqual(z.stage(n),1) # CLOSED target survives

class TestGammaWeil(unittest.TestCase):
    def test_tail_bounds_exact_and_asymptotic(self):
        for j in range(1,120):
            b=gamma_tail_budget(j)
            self.assertGreater(b,0)
            self.assertLess(gamma_tail_partial(j,300),b)
            self.assertLessEqual(b,F(18,j*j)) # crude uniform O(J^-2)
            self.assertGreater(b,gamma_tail_budget(j+1))

    def test_false_gemini_budget_rejected(self):
        # Even the FIRST true Gamma rung is larger than 1/(8 J^2)
        self.assertGreater(F(16,5**3),gemini_bad_gamma_bound(1))
        self.assertGreater(gamma_tail_partial(1,50),gemini_bad_gamma_bound(1))
        self.assertGreater(gamma_tail_budget(1),gemini_bad_gamma_bound(1))

    def test_gamma_truncation_gate_fixed_test_not_RH(self):
        j=5
        pos=IntervalEvidence(SOURCE,F(1,10),F(1,8))
        neg=IntervalEvidence(SOURCE,F(-2),F(-1))
        tiny=IntervalEvidence(SOURCE,F(-1,1000),F(1,1000))
        self.assertIn("TEST_NONNEGATIVE",signed_weil_zeno_gate(pos,j,F(1),SOURCE))
        self.assertIn("TEST_NEGATIVE",signed_weil_zeno_gate(neg,j,F(1),SOURCE))
        self.assertIn("UNDECIDED",signed_weil_zeno_gate(tiny,j,F(1),SOURCE))

    def test_bounded_tail_might_rescue_negative_truncation(self):
        # Never infer negativity from merely Q_J<0 when Gamma remainder positive.
        j=1
        ev=IntervalEvidence(SOURCE,F(-1,100),F(-1,100))
        self.assertIn("UNDECIDED",signed_weil_zeno_gate(ev,j,F(1),SOURCE))

    def test_hostile_source_mismatch_and_fake_sobolev(self):
        ev=IntervalEvidence(SOURCE,F(-2),F(-1))
        for fake in (OTHER,EPOCH,BASIS,DOMAIN):
            with self.assertRaises(ZenoTypeError):signed_weil_zeno_gate(ev,4,F(1),fake)
        with self.assertRaises(ZenoTypeError):signed_weil_zeno_gate(ev,4,F(-1),SOURCE)

    def test_hidden_negative_coordinate_beyond_every_fixed_prefix(self):
        for m in (5,50,1000):
            for n in (0,1,m-1):
                self.assertEqual(hilbert_shadow(m,n),(1,)*n)
            self.assertEqual(hilbert_shadow(m,m)[-1],-1)
        # A distinct global operator can have arbitrarily many identical positive shadows.

    def test_all_finite_corners_not_same_as_one_finite_corner(self):
        for m in (1,8,111):
            assert  all(x==1 for x in hilbert_shadow(m,m-1))
            assert any(x==-1 for x in hilbert_shadow(m,m))

class TestInputHardening(unittest.TestCase):
    def test_bad_stamps(self):
        with self.assertRaises(ZenoTypeError):Stamp("",0,"basis","space")
        with self.assertRaises(ZenoTypeError):Stamp("valid",-1,"basis","space")
        with self.assertRaises(ZenoTypeError):Stamp("valid",0,"","space")

    def test_invalid_intervals_and_outside_arithmetic(self):
        with self.assertRaises(ZenoTypeError):IntervalEvidence(SOURCE,2,1)
        with self.assertRaises(ZenoTypeError):gamma_tail_budget(0)
        with self.assertRaises(ZenoTypeError):gamma_tail_budget(2.0)
        with self.assertRaises(ZenoTypeError):hilbert_shadow(0,1)
        with self.assertRaises(ZenoTypeError):stadium_relative_motion(-1,1)

if __name__ == '__main__':
    unittest.main()

# An additional isolated class after the primary test module. Python unittest
# discovery imports this file; the if __name__ guard above remains false.
from observational_succ.zeno_certificate import (psd_exact, ConditionalBlockSchur,
                                                 zeno_two_level_budget)

class TestFiniteGlobalSchur(unittest.TestCase):
    def test_exact_singular_psd(self):
        self.assertTrue(psd_exact(((1,1),(1,1))))
        self.assertTrue(psd_exact(((0,0),(0,0))))
        self.assertTrue(psd_exact(((0,0,0),(0,1,1),(0,1,1))))
        self.assertTrue(psd_exact(()))

    def test_exact_negative_psd_controls(self):
        self.assertFalse(psd_exact(((0,1),(1,1))))
        self.assertFalse(psd_exact(((1,2),(2,1))))
        self.assertFalse(psd_exact(((-1,),)))
        with self.assertRaises(ZenoTypeError):psd_exact(((1,2),(3,4)))

    def test_two_level_positive_conditional_certificate(self):
        q=ConditionalBlockSchur(SOURCE,((F(2),F(0)),(F(0),F(2))),
                                ((F(1),F(1,2)),(F(1,2),F(1))),F(1))
        self.assertEqual(q.finite_schur(),((F(1),F(-1,2)),(F(-1,2),F(1))))
        self.assertIn("FINITE_MATRIX_PSD",q.exact_finite_gate(SOURCE))

    def test_two_level_negative_gate_not_RH_disproof(self):
        q=ConditionalBlockSchur(SOURCE,((F(1,2),),),((F(1),),),F(1))
        self.assertIn("NOT_A_GLOBAL_NEGATIVE_WITNESS",q.exact_finite_gate(SOURCE))

    def test_negative_coupling_gram_is_not_allowed(self):
        q=ConditionalBlockSchur(SOURCE,((F(2),),),((F(-1),),),F(1))
        self.assertIn("REJECTED",q.exact_finite_gate(SOURCE))

    def test_no_fake_coercivity_source(self):
        q=ConditionalBlockSchur(SOURCE,((F(1),),),((F(1),),),F(1))
        for fake in (OTHER,EPOCH,BASIS,DOMAIN):
            with self.assertRaises(ZenoTypeError):q.exact_finite_gate(fake)
        with self.assertRaises(ZenoTypeError):
            ConditionalBlockSchur(SOURCE,((F(1),),),((F(1),),),F(0))

    def test_two_level_budget_and_mutations(self):
        self.assertEqual(zeno_two_level_budget(F(1,8),F(1,16),F(1,32)),F(7,32))
        with self.assertRaises(ZenoTypeError):zeno_two_level_budget(F(-1),0,0)

