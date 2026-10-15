"""Analytic continuation conditioning and signed two-axis SUCC noncommutation."""
import unittest
from fractions import Fraction as Q
from observational_succ import zeno_analytic_shapes as a


class CertifiedAnalyticShapeTests(unittest.TestCase):
    def test_three_circle_equality_for_authenticated_monomial(self):
        for n in (0,1,2,5,20):
            model=a.EntireMonomialSource(1,2,n)
            report=model.three_circle_exact()
            self.assertEqual(report["M_inner"],Q(1,2**n))
            self.assertEqual(report["M_middle"],Q(1))
            self.assertEqual(report["M_outer"],Q(2**n))
            self.assertEqual(report["interpolation_squared_upper"],Q(1))
            self.assertFalse(report["authentic_zeta_global_growth_authenticated"])

    def test_inner_small_is_useless_if_outer_grows(self):
        for n in (1,3,10,20):
            report=a.EntireMonomialSource(1,2,n).claimed_inner_only_stability()
            self.assertLess(report["inner_value"],1)
            self.assertGreater(report["outer_value"],1)
            self.assertEqual(report["middle_value"],1)
            self.assertFalse(report["inner_data_alone_certifies_outer"])

    def test_with_proved_global_growth_one_gets_inner_bound(self):
        for n in range(1,15):
            # Different exact source h_n(z)=(z/4)^n has M(4)=1.
            data=a.EntireMonomialSource(1,4,n).three_circle_exact()
            self.assertEqual(data["M_inner"],Q(1,4**n))
            self.assertEqual(data["M_middle"],Q(1,2**n))
            self.assertEqual(data["M_outer"],Q(1))
            self.assertEqual(data["M_middle"]**2,
                             data["M_inner"]*data["M_outer"])

    def test_hypothesis_reporting_does_not_authenticate_premises(self):
        c=a.conditional_three_circle_upper(Q(1,64),Q(1))
        self.assertEqual(c["squared_midpoint_bound_if_premises_hold"],Q(1,64))
        self.assertFalse(c["outer_bound_source_authenticated"])
        self.assertFalse(c["holomorphic_domain_source_authenticated"])
        with self.assertRaises(a.AnalyticShapeError):
            a.conditional_three_circle_upper(-1,1)

    def test_source_and_radius_mutations(self):
        for fn in (
            lambda:a.EntireMonomialSource(1,0,3),
            lambda:a.EntireMonomialSource(0.1,2,3),
            lambda:a.EntireMonomialSource(1,2,2.0),
            lambda:a.EntireMonomialSource(1,2,3).three_circle_exact(1,3,4),
        ):
            with self.assertRaises(a.AnalyticShapeError):fn()


class SignedTwoAxisZenoTests(unittest.TestCase):
    def test_signed_rectangles_match_closed_formula(self):
        for n in range(0,18):
            for m in range(1,18):
                result=a.signed_double_successor(n,m)
                self.assertEqual(result["signed_rectangle_total"],
                                 min(n,m)-min(n,m-1))
                self.assertFalse(result["Fubini_or_Tonelli_without_signed_absolute_convergence"])

    def test_iterated_orders_disagree(self):
        for n in range(1,20):
            # After M>N, every row cancels exactly, giving 0.
            self.assertEqual(a.signed_double_successor(n,n+1)["signed_rectangle_total"],0)
            # After N>=M, first-column/last-row boundary leaves 1.
            self.assertEqual(a.signed_double_successor(n+1,n)["signed_rectangle_total"],1)

    def test_diagonal_refinement_not_a_joint_limit(self):
        for n in (1,2,3,5,10,15):
            result=a.signed_double_diagonal(n)
            self.assertEqual(result["equal_horizons"],1)
            self.assertEqual(result["one_extra_column"],0)
            self.assertFalse(result["joint_limit_exists"])

    def test_composition_order_not_a_lawful_gluing_without_summability(self):
        x=a.signed_double_successor(7,8)
        y=a.signed_double_successor(8,7)
        self.assertNotEqual(x["signed_rectangle_total"],y["signed_rectangle_total"])
        with self.assertRaises(a.AnalyticShapeError):
            a.signed_double_successor(7,0)
        with self.assertRaises(a.AnalyticShapeError):
            a.signed_double_successor(1.0,8)




class PositiveTwoAxisGlobalization(unittest.TestCase):
    def test_positive_tonelli_source_and_exact_joint_tail(self):
        for N in range(0,9):
            for M in range(1,9):
                p=a.positive_double_successor(N,M)
                self.assertEqual(p["finite_value"],
                     (1-Q(1,2**N))*(1-Q(1,3**M)))
                self.assertEqual(p["global_limit"],1)
                self.assertEqual(p["tail_exact"],1-p["finite_value"])
                self.assertLessEqual(p["tail_exact"],p["tail_2axis_upper"])
                self.assertTrue(p["joint_limit_with_effective_modulus"])
                self.assertTrue(p["both_iterated_limits_equal"])

    def test_signed_and_positive_models_share_finite_axes_not_limits(self):
        for N in (1,2,5,8):
            signed=a.signed_double_diagonal(N)
            unsigned=a.positive_double_successor(N,N)
            self.assertFalse(signed["joint_limit_exists"])
            self.assertTrue(unsigned["joint_limit_with_effective_modulus"])
            self.assertNotEqual(unsigned["finite_value"],signed["equal_horizons"])

    def test_positivity_and_rate_do_not_prove_physical_supertask(self):
        p=a.positive_double_successor(8,12)
        self.assertLess(p["tail_2axis_upper"],Q(1,100))
        self.assertFalse(p["physical_omega_action_executed"])


if __name__=="__main__":
    unittest.main()
