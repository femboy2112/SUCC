"""Actual Tate finite p-adic Schwartz–Bruhat Fourier, scale and source tests."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_finite_bruhat_observers import (
    TateFiniteFieldError, finite_bruhat_chart, cyclic_character_sum,
    finite_cyclotomic_fourier, exact_tate_finite_plancherel,
    refine_support_chart, refine_constancy_chart,
    finite_tate_refinement_square, conductor_three_probe_gap,
    finite_tate_coset_discriminator,
    exact_tate_distribution_dual_compatibility,
    original_tate_haar_dual_and_fourier_contact,
)
from observational_succ.tate_local_contract import unramified_ball_pair, ZETA3, QRootMinus3


class GenuineFiniteTateWindows(unittest.TestCase):
    def test_each_local_finite_chart_has_exact_dimension_and_Haar(self):
        for p,M,N,Q in ((2,0,0,1),(2,0,2,4),
                        (3,0,1,3),(3,1,0,3),(5,1,1,25)):
            d=finite_bruhat_chart(p,M,N)
            self.assertEqual(d["finite_complex_dimension"],Q)
            self.assertEqual(d["input_additive_Haar_cell"],F(1,p**N))
            self.assertEqual(d["dual_additive_Haar_cell"],F(1,p**M))
            self.assertEqual((d["dual_support_exponent_M"],
                              d["dual_constancy_exponent_N"]),(N,M))
            self.assertEqual(d["additive_character"],"exp(+2*pi*i*{x}_p)")
            self.assertTrue(d["entire_local_Qp_has_infinitely_many_points"])
            self.assertFalse(d["all_complex_coefficients_automatically_computable"])
            self.assertFalse(d["RH_proved"])

    def test_exact_finite_character_orthogonality(self):
        for q in (2,3,4,5,8,9,16,25):
            for k in range(-2*q,2*q+1):
                self.assertEqual(cyclic_character_sum(q,k),
                                 q if k%q==0 else 0)

    def test_haar_normalized_self_dual_exact_Fourier_and_parseval(self):
        cases=(
            (2,0,0,(1,)),
            (2,0,2,(1,-1,2,3)),
            (3,0,1,(0,1,-1)),
            (3,1,0,(1,0,0)),
            (5,0,1,(2,-1,1,0,1)),
        )
        for p,M,N,c in cases:
            d=exact_tate_finite_plancherel(p,M,N,c)
            self.assertEqual(d["input_exact_L2_squared"],
                             d["dual_exact_L2_squared"])
            self.assertEqual(d["double_Fourier_coefficients"],
                             tuple(F(c[(-k)%len(c)]) for k in range(len(c))))
            self.assertTrue(d["isometry_certified_by_character_orthogonality"])
            self.assertTrue(d["dual_support_constancy_interchanged"])
            self.assertFalse(d["full_adelic_Weil_source_identified"])
            self.assertFalse(d["RH_proved"])

    def test_local_ball_selfdual_reproduces_authentic_Tate_T1(self):
        p=3
        chart=finite_cyclotomic_fourier(p,0,0,(1,))
        self.assertEqual(chart["dual_symbolic_rows"],(((0,F(1)),),))
        classical=unramified_ball_pair(p,0,2,+1)
        self.assertEqual(classical.zeta,F(9,8))
        self.assertEqual(classical.p,3)

    def test_tate_support_and_constancy_refinements_commute_with_Fourier(self):
        for p,M,N,c in ((2,0,0,(1,)), (2,0,1,(1,-1)),
                        (3,0,1,(0,1,-1)), (3,1,0,(1,0,0))):
            g=finite_tate_refinement_square(p,M,N,c)
            self.assertTrue(g["support_refinement_dual_constancy_square"])
            self.assertTrue(g["constancy_refinement_dual_support_square"])
            self.assertTrue(g["character_orthogonality_for_wrong_dual_cosets"])
            self.assertTrue(g["Haar_factor_preserved"])
            self.assertTrue(g["direct_limit_of_all_finite_Schwartz_Bruhat_charts"])
            self.assertFalse(g["full_Weil_quadratic_positivity_derived"])
            self.assertFalse(g["RH_proved"])
        self.assertEqual(refine_support_chart(2,0,1,(1,-1)),(F(1),0,F(-1),0))
        self.assertEqual(refine_constancy_chart(2,0,1,(1,-1)),(F(1),F(-1),F(1),F(-1)))

    def test_actual_ramified_conductor_three_repairs_observation_source_gap(self):
        r=conductor_three_probe_gap()
        self.assertEqual(r["p"],3)
        self.assertEqual(r["true_coarse_unit_observation"],0)
        self.assertEqual(r["fine_source_coefficients"],(F(0),F(1),F(-1)))
        self.assertEqual(r["fine_phase_norm_squared"],F(1,3))
        self.assertEqual((ZETA3-ZETA3**2)/3,QRootMinus3(0,F(1,3)))
        self.assertTrue(r["new_conductor_coset_probe_repairs_sigma_gap"])
        self.assertTrue(r["fine_nonzero_Gauss_phase"])
        self.assertFalse(r["global_Weil_sign_proved"])
        self.assertFalse(r["RH_proved"])

    def test_complete_conductor_coset_probes_separate_actual_source_from_zero(self):
        a=finite_tate_coset_discriminator(3,0,1,(0,1,-1),(0,0,0))
        self.assertEqual(a["source"],"GENUINE_LOCAL_TATE_SCHWARTZ_BRUHAT_COSET_OBSERVER")
        self.assertEqual(a["first_distinguishing_coset"],1)
        self.assertEqual(a["exact_coset_Haar_pairing_difference"],F(1,3))
        self.assertTrue(a["finite_witness_of_distinct_source"])
        self.assertTrue(a["complete_coset_probe_family_jointly_separating"])
        self.assertFalse(a["observer_assumed_to_have_physical_probe_access"])
        self.assertFalse(a["RH_proved"])
        same=finite_tate_coset_discriminator(3,0,1,(0,1,-1),(0,1,-1))
        self.assertTrue(same["all_coefficients_identical"])
        self.assertIsNone(same["first_distinguishing_coset"])
        self.assertFalse(same["finite_witness_of_distinct_source"])

    def test_finite_arithmetic_source_probe_has_no_ontic_privilege(self):
        x=finite_tate_coset_discriminator(2,0,2,(1,2,3,4),(1,2,-3,4))
        self.assertEqual(x["first_distinguishing_coset"],2)
        self.assertEqual(x["exact_coset_Haar_pairing_difference"],F(3,2))
        self.assertFalse(x["observer_assumed_to_have_physical_probe_access"])
        with self.assertRaises(TateFiniteFieldError):
            finite_tate_coset_discriminator(6,0,1,(1,0),(0,0))

    def test_true_additive_Haar_is_coherent_inverse_limit_of_test_duals(self):
        for p,M,N,c,input_exact,contact in (
            (2,0,1,(1,-1),F(0),F(1)),
            (3,0,1,(2,1,-1),F(2,3),F(2)),
            (3,1,0,(1,0,0),F(1),F(1)),
        ):
            d=original_tate_haar_dual_and_fourier_contact(p,M,N,c)
            self.assertEqual(d["original_integral_exact"],input_exact)
            self.assertEqual(d["Fourier_dual_integral_exact"],contact)
            self.assertEqual(d["original_value_at_zero_exact"],contact)
            self.assertTrue(d["original_Haar_dual_source_gluing"])
            self.assertTrue(d["Fourier_Haar_distribution_equals_evaluation_at_zero"])
            self.assertTrue(d["test_colimit_dual_distribution_inverse_limit"])
            self.assertFalse(d["real_global_Weil_contact_identified"])
            self.assertFalse(d["RH_proved"])

    def test_wrong_source_dual_coefficient_blocks_are_not_phantom_global_Haar(self):
        p,M,N=3,0,1
        old=(F(1,3),)*3
        sup=(F(1,3),)*9
        con=(F(1,9),)*9
        good=exact_tate_distribution_dual_compatibility(p,M,N,old,sup,con)
        self.assertTrue(good["source_functional_coherently_glued"])
        self.assertTrue(good["support_square_commutes"])
        self.assertTrue(good["constancy_square_commutes"])
        self.assertTrue(good["dual_is_inverse_limit_of_finite_dimensional_vector_spaces"])
        self.assertTrue(good["finite_dimensional_complex_stage_is_not_a_finite_set"])
        self.assertFalse(good["unbounded_complex_stage_automatically_compact"])
        bad_con=list(con);bad_con[0]+=F(1,9)
        bad=exact_tate_distribution_dual_compatibility(
            p,M,N,old,sup,tuple(bad_con)
        )
        self.assertTrue(bad["support_square_commutes"])
        self.assertFalse(bad["constancy_square_commutes"])
        self.assertFalse(bad["source_functional_coherently_glued"])
        self.assertFalse(bad["RH_proved"])

    def test_fake_composite_bad_Haar_and_wrong_coefficient_type_fail_closed(self):
        for p,M,N in ((6,0,0),(1,0,0),(2,-1,0),(3,1,-1),(True,0,0),
                      (2,0,7),(3,True,0)):
            with self.assertRaises(TateFiniteFieldError):
                finite_bruhat_chart(p,M,N)
        for p,M,N,c in ((2,0,1,(1,)),(2,0,1,(1,1.5)),(2,0,1,(True,0))):
            with self.assertRaises(TateFiniteFieldError):
                finite_cyclotomic_fourier(p,M,N,c)
        for q,k in ((0,2),(2,True),(2,1.3)):
            with self.assertRaises(TateFiniteFieldError):
                cyclic_character_sum(q,k)


if __name__=="__main__":
    unittest.main()
