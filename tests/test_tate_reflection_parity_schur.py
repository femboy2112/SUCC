"""Original zeta reflection parity separates polar signs and lowers low Schur rank."""
import unittest
from fractions import Fraction as F

from observational_succ.tate_reflection_parity_schur import (
    reflection_parity_15_low_source_certificate
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial, poly_primitive_zero_at_left,
    poly_eval, poly_integral, poly_mul
)


class SourceTrueReflectionParity(unittest.TestCase):
    def test_exact_14_even_and_16_odd_moment_Weil_sign(self):
        z=reflection_parity_15_low_source_certificate()
        self.assertEqual(z["source"],"TRUE_ZETA_TATE_GAMMA_REFLECTION_PARITY_WEIL")
        self.assertEqual(z["original_suzuki_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(z["true_active_prime_powers"],(2,))
        self.assertEqual(z["even_f_zero_moment_count"],14)
        self.assertEqual(z["even_f_Gamma_modes"],256)
        self.assertEqual(z["even_f_Fourier_cutoff"],F(217,20))
        self.assertEqual(z["even_f_negative_source_upper"],F(47,8))
        self.assertTrue(z["even_f_negative_sinh_pole_vanishes"])
        self.assertGreater(z["even_f_source_gap_strict_lower"],F(1,140))
        self.assertEqual(z["odd_f_zero_moment_count"],16)
        self.assertTrue(z["odd_f_positive_cosh_pole_vanishes"])
        self.assertGreater(z["odd_f_source_gap_strict_lower"],F(1,20))
        self.assertFalse(z["rank15_low_Schur_sign_certified"])
        self.assertFalse(z["RH_proved"])

    def test_true_low_selector_is_7_odd_plus_8_even_modes_not_first_fifteen(self):
        z=reflection_parity_15_low_source_certificate()
        self.assertEqual(z["source_low_indices"],tuple(range(1,15))+(16,))
        self.assertEqual(z["odd_derivative_low_modes_even_primitive"],
                         tuple(range(1,14,2)))
        self.assertEqual(z["even_derivative_low_modes_odd_primitive"],
                         tuple(range(2,17,2)))
        self.assertEqual(z["reflection_parity_block_dimensions"],(7,8))
        self.assertEqual(z["low_dimension"],15)
        self.assertEqual(z["full_true_high_operator_G_at_least_kappa_K"],F(1,140))
        self.assertEqual(z["true_zero_shift_R0_operator_norm_strict_upper"],
                         F(847,80))
        self.assertTrue(z["relative_kappa_worse_than_rank18"])
        self.assertFalse(z["all_a_global_positive_Weil_proved"])

    def test_actual_legendre_high_modes_map_to_correct_parity_moment_subspaces(self):
        a=F(1,2)
        for j,m,expected_even in ((15,14,True),(17,14,True),(18,16,False),(20,16,False)):
            u=legendre_polynomial(j,a)
            f=poly_primitive_zero_at_left(u,a)
            self.assertEqual(poly_eval(f,-a),0)
            self.assertEqual(poly_eval(f,a),0)
            self.assertEqual(all((i%2==0 or c==0 for i,c in enumerate(f))),
                             expected_even)
            for k in range(m):
                power=tuple([F(0)]*k+[F(1)])
                moment=poly_integral(poly_mul(f,power),-a,a)
                self.assertEqual(moment,0,msg=f"Legendre index {j}; moment {k}")

    def test_parity_matters_even_if_finite_original_prime_part_is_signed(self):
        z=reflection_parity_15_low_source_certificate()
        self.assertLess(z["even_f_negative_source_upper"],F(95,16))
        self.assertGreater(z["even_f_source_gap_strict_lower"],0)
        self.assertFalse(z["rank15_low_Schur_sign_certified"])


if __name__=="__main__":
    unittest.main()
