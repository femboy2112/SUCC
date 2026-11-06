import unittest
from fractions import Fraction as F
import probe


class BDEExactTests(unittest.TestCase):
    def test_rational_sources_and_shadow_receipt(self):
        receipt=probe.run()
        self.assertEqual(receipt['status'],'FINITE_EXACT_CHECKS_PASS')
        self.assertEqual(receipt['pair_audit']['unordered_pairs'],8128)

    def test_nonunit_frequency_is_rejected(self):
        with self.assertRaises(ValueError):
            probe.lock_adjustment(F(1,7),F(1,100),3,9)

    def test_explicit_derivative_threshold(self):
        self.assertEqual(probe.derivative_constant(2),F(18413,6561))
        self.assertEqual(probe.derivative_constant(3),F(5708452,295245))
        self.assertLess(32*probe.derivative_constant(2),128)
        self.assertLess(F(16,3)*probe.derivative_constant(3),128)

    def test_tail_sign_control_rejects_angular_channel(self):
        u,w=probe.source_streams(37)
        low,high=probe.radial_derivative_interval(37,0)
        self.assertTrue(low<(2*u[37]-w[37])/4<high)
        self.assertFalse(low<(2*u[37]+w[37])/4<high)


if __name__=='__main__':
    unittest.main()
