"""Original source Gamma contact: singular bare Zeno sum, finite renormalized product."""
import unittest
from fractions import Fraction as Q
from observational_succ import zeno_gamma_contact as g


class GammaContactZenoTests(unittest.TestCase):
    def test_bare_ladder_diverges_and_contact_repairs(self):
        records=[g.source_gamma_contact(n) for n in (2,4,8,12,16)]
        for p in records:
            self.assertGreater(p["bare_gamma_kernel_interval"][0],0)
            self.assertGreater(p["renormalized_difference_interval"][0],0)
            self.assertGreater(p["renormalized_product_interval"][0],0)
            self.assertFalse(p["actual_contact_value_at_x_zero_directly_evaluated"])
            self.assertFalse(p["original_test_compact_support_authenticated"])
            self.assertFalse(p["full_signed_weil_form_identified"])
        for prev,next_ in zip(records,records[1:]):
            self.assertLess(prev["bare_gamma_kernel_interval"][1],
                            next_["bare_gamma_kernel_interval"][0])
            self.assertGreater(prev["renormalized_difference_interval"][0],
                               next_["renormalized_difference_interval"][1])

    def test_renormalized_product_tends_to_half_without_assuming_it_at_zero(self):
        for n in (4,8,12,16):
            r=g.source_gamma_contact(n)
            lo,hi=r["renormalized_product_interval"]
            self.assertLess(lo,Q(1,2)+r["distance_to_contact"])
            self.assertGreater(hi,Q(1,2)-r["distance_to_contact"])
            self.assertEqual(r["analytic_limit_from_classical_elementary_exp"],"1/2")
        p=g.source_gamma_contact(16)
        self.assertLess(p["renormalized_product_interval"][1]-
                        p["renormalized_product_interval"][0],Q(1,10**12))

    def test_calibrate_against_independent_high_precision_oracle(self):
        try:import mpmath as mp
        except ImportError:self.skipTest("optional high precision diagnostic")
        mp.mp.dps=70
        for n in (1,3,7,12):
            result=g.source_gamma_contact(n)
            x=mp.mpf(1)/2**n
            reference=(2*(1-mp.exp(-x/2))*mp.exp(-x/2)
                       /(-mp.expm1(-2*x)))
            low,high=result["renormalized_product_interval"]
            a=mp.mpf(low.numerator)/low.denominator
            b=mp.mpf(high.numerator)/high.denominator
            self.assertLessEqual(a,reference)
            self.assertGreaterEqual(b,reference)

    def test_invalid_source_contact_direct_evaluation(self):
        with self.assertRaises(g.ZenoContactError):
            g.false_bare_at_contact()
        for bad in (0,17,2.0,-1):
            with self.assertRaises(g.ZenoContactError):
                g.source_gamma_contact(bad)


if __name__=="__main__":
    unittest.main()
