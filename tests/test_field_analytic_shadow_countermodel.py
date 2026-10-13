"""Positive counterexample: reflection and any prescribed finite jet cannot pin zeros."""
import unittest
from fractions import Fraction as F
from observational_succ.field_analytic_shadow_countermodel import symmetric_jet_with_forced_offline_zero

class AnalyticCountermodelTests(unittest.TestCase):
    def test_any_finite_jet_order_0_through_12_has_real_polynomial_offline_zero(self):
        for n in range(13):
            r=symmetric_jet_with_forced_offline_zero(n)
            self.assertEqual(r['status'],"EXACT_FINITE_JET_REFLECTION_INSUFFICIENT")
            self.assertEqual(r['zero_real'],F(1,4))
            self.assertEqual(r['zero_imag'],F(1,10))
            self.assertEqual(r['coefficients'][0],1)
            self.assertTrue(all(x==0 for x in r['coefficients'][1:n+1]))
            self.assertTrue(all(type(x) is F for x in r['coefficients']))
            self.assertFalse(r['actual_Riemann_xi_used_or_modified'])

    def test_noncanonical_zero_can_be_moved_through_many_rational_strip_points(self):
        for re in (F(1,10),F(1,4),F(3,4),F(9,10)):
            for im in (F(1,10),F(-1,9),F(2,7)):
                r=symmetric_jet_with_forced_offline_zero(4,real_part=re,imag_part=im)
                self.assertEqual(r['zero_real'],re)
                self.assertEqual(r['zero_imag'],im)

    def test_real_midline_and_real_axis_are_outside_this_constructor_domain(self):
        for bad in (F(0),F(1),F(1,2),F(-1,2)):
            with self.assertRaises(ValueError):
                symmetric_jet_with_forced_offline_zero(5,real_part=bad)
        with self.assertRaises(ValueError):
            symmetric_jet_with_forced_offline_zero(5,imag_part=F(0))

    def test_unbounded_symbolic_order_is_budgeted(self):
        with self.assertRaises(ValueError):
            symmetric_jet_with_forced_offline_zero(300)

    def test_complex_floating_zero_is_never_treated_as_exact(self):
        with self.assertRaises(ValueError):
            symmetric_jet_with_forced_offline_zero(4,real_part=0.25)

if __name__=='__main__':unittest.main()
