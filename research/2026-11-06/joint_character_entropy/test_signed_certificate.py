"""Rational signed Weyl proof obligation: finite certified intervals only."""
import unittest
from fractions import Fraction
from independent_oracle import machin_pi16_interval
from joint_entropy import original_states, tail_enclosure
from signed_certificate import (M,GRID,PI_GRID,PI_CEILING,certified_pi_grid,
    frac_pow_series,lagrange_error,norm_interval,certified_weyl,
    source_completed_samples,short_receipt)


class SignedCertificateTests(unittest.TestCase):
    def test_pi_rational_enclosure_is_independently_anchored(self):
        grid,error=certified_pi_grid()
        lo,hi=machin_pi16_interval(80,26)
        self.assertLessEqual(grid,16*lo)
        self.assertGreaterEqual(grid+error,16*hi)
        self.assertLess(error,Fraction(1,10**16))

    def test_taylor_polynomial_at_zero(self):
        c,s=frac_pow_series(Fraction(0))
        self.assertEqual((c,s),(Fraction(1),Fraction(0)))
        self.assertLess(lagrange_error(),Fraction(1,10**11))

    def test_error_budget_always_nonnegative(self):
        self.assertGreater(lagrange_error(),0)
        with self.assertRaises(ValueError):
            norm_interval(Fraction(0),Fraction(0),Fraction(-1))

    def test_root_grid_cancels_two_modes_with_rational_certificate(self):
        original=tuple((Fraction(i,16),Fraction(i,16)) for i in range(16))
        for h in (1,2):
            r=certified_weyl(original,h)
            self.assertLess(r['upper'],Fraction(1,10**6))
            self.assertEqual(r['lower'],0)

    def test_periodic_completion_counterseed_never_saves(self):
        fixed=tuple((Fraction(1,5),Fraction(1,5)) for _ in range(223))
        for h in (1,2):
            r=certified_weyl(fixed,h)
            self.assertLess(r['lower'],1)
            self.assertGreater(r['lower'],Fraction(99,100))
            self.assertGreater(r['upper'],1)

    def test_source_selected_epoch_certificates_are_nontrivial(self):
        for A in (223,457):
            samples=source_completed_samples(A)
            for h in (1,2):
                r=certified_weyl(samples,h)
                self.assertLess(r['upper'],Fraction(1))
                self.assertGreater(r['lower'],0)
                self.assertLess(r['upper']-r['lower'],Fraction(1,10**10))

    def test_source_enclosures_are_not_fake_point_values(self):
        for A in (223,457):
            samples=source_completed_samples(A)
            self.assertTrue(all(hi>lo for lo,hi in samples))
            self.assertTrue(all(hi-lo < Fraction(1,10**15) for lo,hi in samples))

    def test_character_input_rejection(self):
        with self.assertRaises(ValueError):
            certified_weyl(tuple(),1)
        with self.assertRaises(ValueError):
            certified_weyl(((Fraction(0),Fraction(1)),),1)
        with self.assertRaises(ValueError):
            certified_weyl(((Fraction(0),Fraction(0)),),0)

    def test_gauge_integer_shift_does_not_change_bound(self):
        base=((Fraction(1,5),Fraction(1,5)),)
        shift=((Fraction(6,5),Fraction(6,5)),)
        x=certified_weyl(base,2)
        y=certified_weyl(shift,2)
        self.assertEqual((x['lower'],x['upper']), (y['lower'],y['upper']))


if __name__=='__main__':
    unittest.main(verbosity=2)
