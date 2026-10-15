"""Exact interval quadrature tests: source proof is monotone+Taylor+Poisson."""
import unittest
from fractions import Fraction as Q
from observational_succ.source_model_interval_quadrature import (
    SourceInteractionError, atan_interval, pi_bounds, sqrt_rational,
    fourth_root_rational, exp_neg_bounds, _weight_bounds, certified_real_xi,
)


class RealXiCertifiedQuadrature(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.critical=certified_real_xi(Q(1,2),2,8,512)
        cls.negative=certified_real_xi(-2,2,8,512)
        cls.positive=certified_real_xi(3,2,8,512)

    def test_critical_symmetric_weight_regression(self):
        self.assertEqual(_weight_bounds(Q(1),Q(1,2)),(Q(2),Q(2)))
        self.assertEqual(_weight_bounds(Q(16),Q(1,2)),(Q(1,4),Q(1,4)))
        self.assertEqual(_weight_bounds(Q(1),Q(-2)),(Q(2),Q(2)))
        self.assertEqual(_weight_bounds(Q(1),Q(3)),(Q(2),Q(2)))

    def test_rational_Machin_pi_bounds_and_arctan(self):
        lo,hi=pi_bounds()
        self.assertTrue(Q(3)<lo<hi<Q(22,7))
        a,b=atan_interval(Q(1,5),12)
        c,d=atan_interval(Q(1,5),24)
        self.assertLess(d-c,b-a)

    def test_sqrt_and_quarter_bounds_are_exact(self):
        for q in (Q(1),Q(2),Q(3,7),Q(7,2),Q(16),Q(81,16)):
            lo,hi=sqrt_rational(q)
            self.assertLessEqual(lo*lo,q)
            self.assertLessEqual(q,hi*hi)
            a,b=fourth_root_rational(q)
            self.assertLessEqual(a**4,q)
            self.assertLessEqual(q,b**4)

    def test_exact_exp_negative_bound_order(self):
        pi_lo,pi_hi=pi_bounds()
        for n in (1,2,3):
            for t in (Q(1),Q(2),Q(7,3)):
                lo,hi=exp_neg_bounds(pi_lo*n*n*t,pi_hi*n*n*t)
                self.assertTrue(0<=lo<=hi<=1)

    def test_entire_critical_real_source_is_inside_certified_interval(self):
        x=self.critical
        self.assertTrue(x['fully_rational_numerical_enclosure'])
        self.assertGreater(Q(x['xi_lower']),Q(59,120))
        self.assertLess(Q(x['xi_lower']),Q(1,2))
        self.assertLess(Q(x['xi_upper']),Q(1,2))
        self.assertLess(Q(x['xi_width_upper']),Q(1,5000))

    def test_negative_Euler_exterior_xi_has_certified_real_interval(self):
        x=self.negative
        self.assertLess(Q(x['xi_lower']),Q(57394,100000))
        self.assertGreater(Q(x['xi_upper']),Q(57394,100000))
        self.assertTrue(x['fully_rational_numerical_enclosure'])
        self.assertLess(Q(x['xi_width_upper']),Q(1,200))

    def test_negative_and_positive_dual_are_exactly_identical(self):
        for field in ('xi_lower','xi_upper','xi_width_upper',
                      'theta_quadrature_lower','theta_quadrature_upper'):
            self.assertEqual(self.negative[field],self.positive[field])

    def test_more_finite_samples_shrink_width(self):
        a=certified_real_xi(Q(1,2),2,8,256)
        b=certified_real_xi(Q(1,2),2,8,1024)
        self.assertLess(Q(b['xi_width_upper']),Q(a['xi_width_upper']))

    def test_exterior_source_full_nonzero_certificate(self):
        for s in (-2,3):
            x=certified_real_xi(s,2,8,128)
            self.assertGreater(Q(x['xi_lower']),Q(1,2))

    def test_invalid_states_fail_not_get_fabricated(self):
        for call in (
            lambda: certified_real_xi(4),
            lambda: certified_real_xi(Q(1,3)),
            lambda: certified_real_xi(Q(1,2),0),
            lambda: certified_real_xi(Q(1,2),2,1),
            lambda: certified_real_xi(Q(1,2),2,8,4),
            lambda: exp_neg_bounds(Q(3),Q(2)),
            lambda: sqrt_rational(0),
        ):
            with self.assertRaises(SourceInteractionError):
                call()


if __name__=='__main__':
    unittest.main()
