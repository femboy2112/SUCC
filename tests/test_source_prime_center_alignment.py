"""Independent source-gated actual P1 center residual and B3 Gamma-tail tests.

Critical distinction: no fitted vector g. The source-adapter takes the
original signed Suzuki P1 derivative, original completed mixed derivative
moments, and a separately proved omitted Gamma H1 tail. Strict interval
exclusion of zero is the pass criterion, never a numerical point estimate.
"""
import unittest
from fractions import Fraction as F

from observational_succ.source_prime_center_alignment import (
    SourceCenterError,_original_finite_center_derivative_integral,
    _original_B3_center_integral_tail,certified_true_P1_center_residual,
)


class OriginalSourceCenterResidualTests(unittest.TestCase):
    def test_real_P1_center_excludes_zero_after_original_infinite_Gamma_tail(self):
        result=certified_true_P1_center_residual(J=64,J_G=64)
        self.assertEqual(result["source_sha"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(result["real_prime_tape"],(2,2))
        self.assertTrue(result["actual_p1_low_high_residual_not_model"])
        self.assertGreater(result["true_P1_abs_center_moment_certified_lower"],0)
        self.assertGreater(result["true_P1_center_energy_certified_lower"],0)
        self.assertGreater(result["true_P1_source_prime_dual_saving_lower"],0)
        self.assertFalse(result["source_nonstrict_when_interval_hits_zero"])
        self.assertEqual(result["source_signed_S4_sign"],"UNVERIFIED")
        self.assertFalse(result["RH_proved"])

    def test_original_even_center_parity_uses_zero_finite_source_integral(self):
        # P2 is even; the derivative of the original even-symmetric G P2 is
        # odd and its full centered integral is zero. Rational intervals from
        # finite source coefficients must contain zero, not manufacture sign.
        z=_original_finite_center_derivative_integral(2,8)
        self.assertLessEqual(z.lo,F(0))
        self.assertGreaterEqual(z.hi,F(0))

    def test_proved_original_B3_omitted_Gamma_tail_drops_with_J(self):
        t20=_original_B3_center_integral_tail(1,20)
        t64=_original_B3_center_integral_tail(1,64)
        t128=_original_B3_center_integral_tail(1,128)
        self.assertTrue(F(0)<t128<t64<t20)
        self.assertLess(t64,F(1,1000))

    def test_missing_or_forged_source_parameters_fail_closed(self):
        for k,J in ((0,64),(True,64),(1,0),(1,129),(1,True)):
            with self.assertRaises(SourceCenterError):
                _original_finite_center_derivative_integral(k,J)
        for k,J in ((3,64),(1,0),(1,129)):
            with self.assertRaises(SourceCenterError):
                _original_B3_center_integral_tail(k,J)
        with self.assertRaises(SourceCenterError):
            certified_true_P1_center_residual(J=64,J_G=2)


if __name__=="__main__":
    unittest.main()
