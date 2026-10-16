"""Certified rational authentic Suzuki anchored source minors (finite only)."""
import unittest
from fractions import Fraction as F

from observational_succ.one_object_transport import OneObjectError
from observational_succ.one_object_kernel_certificates import (
    authentic_suzuki_g_interval, authentic_kernel_interval, source_two_point_minor,
)


class AuthenticSignedSourceMinorTests(unittest.TestCase):
    def test_zero_anchor_and_equality_symmetry(self):
        for J in (8,32,128):
            self.assertEqual(authentic_suzuki_g_interval(0,J),(F(0),F(0)))
            self.assertEqual(authentic_kernel_interval(0,F(1,4),J),(F(0),F(0)))
            self.assertEqual(authentic_kernel_interval(F(1,4),F(1,2),J),
                             authentic_kernel_interval(F(1,2),F(1,4),J))
            self.assertEqual(authentic_suzuki_g_interval(F(1,2),J),
                             authentic_suzuki_g_interval(-F(1,2),J))

    def test_original_source_rational_gram_minor(self):
        # Strict sign is required from outward intervals, never from floats.
        r=source_two_point_minor(F(1,4),F(1,2),128)
        self.assertEqual(r["verdict"],"PROVED_FINITE_SOURCE_POSITIVE")
        self.assertGreater(r["Kxx"][0],0)
        self.assertGreater(r["Kyy"][0],0)
        self.assertGreater(r["determinant"][0],0)
        self.assertFalse(r["RH_proved"])
        self.assertFalse(r["nontrivial_zeros_used"])

    def test_reject_false_sign_certificates_and_bad_domains(self):
        for bad in (True,0.5,F(9,4)):
            with self.assertRaises(OneObjectError):
                authentic_suzuki_g_interval(bad,32)
        for J in (0,-1,129,True):
            with self.assertRaises(OneObjectError):
                authentic_suzuki_g_interval(F(1,2),J)
        with self.assertRaises(OneObjectError):
            source_two_point_minor(F(1,2),F(1,2),128)
        with self.assertRaises(OneObjectError):
            source_two_point_minor(0,F(1,2),128)


if __name__=="__main__":
    unittest.main()
