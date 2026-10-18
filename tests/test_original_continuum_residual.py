"""Exact continuum signed Suzuki action, source-pinned and fail-closed tests."""
import unittest
from fractions import Fraction as F
from observational_succ import original_continuum_residual as R
from observational_succ import clamped_k_residual_bridge as B


class IndependentTaylorConvolution(unittest.TestCase):
    def test_ou_absolute_moments_by_closed_polynomials(self):
        K=R._convolution_powers((F(1),),2)
        self.assertEqual(K[0],(F(1),))
        self.assertEqual(K[1],(F(1,4),F(0),F(1)))
        self.assertEqual(K[2],(F(1,12),F(0),F(1)))
        W=R._convolution_powers((F(0),F(1)),1)
        self.assertEqual(W[0],(F(0),))
        self.assertEqual(W[1],(F(0),-F(1,4),F(0),F(1,3)))

    def test_taylor_source_independent_three_small_rungs(self):
        for p in ((F(1),),(F(0),F(1)),(F(0),F(0),F(1))):
            for J,M in ((1,24),(2,32),(4,56)):
                approx,e=R.gamma_ou_taylor_sum(p,J,M)
                self.assertGreaterEqual(e,0)
                self.assertLess(e,F(1,10**6))
                self.assertIsInstance(approx,tuple)
                self.assertTrue(all(type(z) is F for z in approx))

    def test_source_free_lawful_matching_primitives_and_parities(self):
        for i in range(1,5):
            x=R.high_boundary_match(i)
            self.assertTrue(x["H2_zero_extended"])
            self.assertEqual(x["low"],i)
            self.assertEqual(x["matched_high"],(5,6,5,6)[i-1])
            self.assertEqual(x["norm_sq"],R.norm_squared(x["h"]))
            self.assertEqual(B.value(x["h"],F(1,2)),0)
            self.assertEqual(B.value(B.derivative(x["h"]),F(-1,2)),0)
            for t in (F(1,2),-F(1,3),F(3,4)):
                z=R.high_boundary_match(i,t)
                self.assertEqual(B.value(B.derivative(z["h"]),F(1,2)),0)
                self.assertGreater(z["second_derivative_norm_sq"],0)
        for bad in (0,5,True,3.4):
            with self.assertRaises(R.OriginalResidualError):
                R.high_boundary_match(bad)

    def test_polar_even_odd_and_source_free_approximation_error(self):
        c,s,e=R.polar_taylor(18)
        self.assertEqual(c[1],0)
        self.assertEqual(s[0],0)
        self.assertGreater(e,0)
        self.assertLess(e,F(1,10**24))
        with self.assertRaises(R.OriginalResidualError):
            R.polar_taylor(1)
        for bad in (0,True,1.25,33):
            with self.assertRaises(R.OriginalResidualError):
                R.gamma_ou_taylor_sum((F(1),),bad,40)


class ArchivedOriginalSignedSuzuki(unittest.TestCase):
    def test_frozen_signed_source_parameters(self):
        p=R.source_parameters()
        self.assertEqual(p["sha"],R.SOURCE_SHA)
        self.assertEqual(p["real_gamma_count"],1)
        self.assertEqual(p["half_density"],"1/2")
        self.assertTrue(F(5,8)<p["b"]<F(3,4))
        self.assertGreater(p["db"],0)
        self.assertGreater(p["dc"],0)
        self.assertTrue(p["source_type"]=="ORIGINAL_SUZUKI_SIGNED_PRIMITIVE")

    def test_authentic_infinite_gamma_tail_lower_is_true_quadratic_form(self):
        from observational_succ.gamma_fredholm_completion import gamma_tail_H01_lower
        h=R.high_boundary_match(1)["h"]
        p=R.authentic_Gamma_tail_energy_lower_matrix((h,),16)
        self.assertEqual(p[0][0],gamma_tail_H01_lower(16,
                           R.derivative_norm_squared(h),
                           R.norm_squared(B.derivative(B.derivative(h)))))
        for J in (4,8,12,16):
            F1=R.high_boundary_match(1)["h"]
            F3=R.high_boundary_match(3)["h"]
            g=R.authentic_Gamma_tail_energy_lower_matrix((F1,F3),J)
            self.assertEqual(g[0][1],g[1][0])
            self.assertEqual(len(g),2)
        with self.assertRaises(R.OriginalResidualError):
            R.authentic_Gamma_tail_energy_lower_matrix((R.low_primitive(1),),8)

    def test_original_exp_antiderivative_vs_independent_entire_action(self):
        h=R.frozen_operator_matrix_holdout(J=2,M=44,P=18)
        self.assertEqual(h["original_source_sha"],R.SOURCE_SHA)
        self.assertEqual(len(h["independent_exp_matrix_vs_Taylor_continuum_action"]),6)
        for name,e in h["independent_exp_matrix_vs_Taylor_continuum_action"].items():
            self.assertTrue(e["independent_enclosures_intersect"],name)
            self.assertGreater(F(e["rigorous_action_pair_error_upper"]),0)

    def test_original_four_mode_continuum_residual_scoped(self):
        result=R.source_residual_schur_trial(J=8,M=80,P=18,fit=True)
        self.assertEqual(result["frozen_source_git_blob"],R.SOURCE_SHA)
        self.assertTrue(result["one_real_Gamma_contact_two_completed_poles"])
        self.assertEqual(len(result["four_original_parity_Schur_blocks"]),2)
        self.assertFalse(result["RH_proved"])
        for key,block in result["four_original_parity_Schur_blocks"].items():
            self.assertEqual(len(block["combined_residual_norm_upper_each"]),2)
            self.assertTrue(block["trial_is_in_original_high_domain"])
            self.assertFalse(block["missing_full_residual_norm_source_certificate"])
            self.assertGreater(F(block["source_kappa"]),0)
        # Do NOT force positivity; original source result must report actual sign.

    def test_no_source_positivity_laundered_by_Galerkin(self):
        for bad in (0,-1,1.0,True):
            with self.assertRaises((R.OriginalResidualError,TypeError)):
                R.safe_ratio_round(1,bad)
        with self.assertRaises(R.OriginalResidualError):
            R.source_residual_schur_trial(J=0)
        with self.assertRaises(R.OriginalResidualError):
            R.source_residual_schur_trial(J=33)
        with self.assertRaises(R.OriginalResidualError):
            R.source_residual_schur_trial(eta=0)


if __name__=="__main__":
    unittest.main()
