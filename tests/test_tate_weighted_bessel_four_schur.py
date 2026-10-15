"""Hostile exact original Weil FOUR-moment weighted spectral-Bessel proof tests."""
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.tate_weighted_bessel_four_schur import (
    WeightedBesselSourceError, _bessel_source_coefficients,
    _bessel_series_absolute_error,
    _finite_bessel_integral_polynomial,
    weighted_Bessel_leakage_upper,
    exact_fraction_bytes,
    source_weighted_four_moment_certificate,
    true_four_low_suzuki_interface,
)
from observational_succ.tate_bessel_seven_schur import (
    spherical_bessel_polynomial_l2,original_seven_moment_weil_certificate
)
from observational_succ.tate_suzuki_fourier_schur import gamma_fourier_multiplier_lower
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial,poly_primitive_zero_at_left,poly_mul,poly_integral,poly_eval
)
from observational_succ.suzuki_moment_schur import inverse_neumann_boundary_channels


class ExactWeightedSphericalBesselBands(unittest.TestCase):
    def test_original_Bessel_series_coefficients_match_an_independent_closed_form(self):
        for l in (4,5,7,15):
            coeff=_bessel_source_coefficients(l,12)
            for k,c in enumerate(coeff):
                odd=1
                for j in range(1,2*(l+k)+2,2):
                    odd*=j
                expected=F((-1)**k,2**k*factorial(k)*odd)
                self.assertEqual(c,expected,msg=f"l={l},k={k}")
            delta=_bessel_series_absolute_error(l,coeff,F(13,2))
            old=spherical_bessel_polynomial_l2(l,12,F(13,2))
            self.assertEqual(delta,old["pointwise_absolute_Bessel_remainder_upper"])
            self.assertGreater(delta,0)

    def test_exact_rational_fourier_cell_antiderivative_has_positive_differences(self):
        group,_=_finite_bessel_integral_polynomial(4,16,12)
        self.assertGreater(len(group),10)
        def integrated(z):
            return sum((coef*z**n for n,coef in group),F())
        last=F(0)
        for k in range(1,17):
            x=F(13*k,2*16)
            val=integrated(x)
            self.assertGreater(val,last)
            last=val

    def test_original_gamma_weighted_loss_is_analytically_below_source_budget(self):
        c=weighted_Bessel_leakage_upper()
        self.assertEqual(c["source"],"CLASSICAL_LEGENDRE_BESSEL_TRUE_GAMMA_WEIGHTED_ENCLOSURE")
        self.assertEqual(c["a"],F(1,2))
        self.assertEqual(c["Omega"],F(13))
        self.assertEqual(c["Gamma_real_modes"],128)
        self.assertEqual(c["vanishing_moments"],4)
        self.assertEqual(c["spectral_cells"],96)
        self.assertEqual(c["finite_angular_modes"],tuple(range(4,16)))
        self.assertEqual(c["angular_power_series_order"],12)
        self.assertEqual(c["Young_rational_slack"],F(1,1000))
        self.assertTrue(c["weighted_low_Fourier_leakage_below_2013over10000"])
        self.assertLess(c["weighted_low_Fourier_leakage_exact_upper"],F(2013,10000))
        self.assertGreater(c["Gamma_multiplier_exact"],F(6097,1000))
        self.assertGreater(c["omitted_angular_mode_tail"],0)
        self.assertTrue(c["source_all_finite_band_and_angular_errors_included"])
        self.assertFalse(c["RH_proved"])

    def test_weighted_left_endpoint_enclosure_improves_with_resolution(self):
        a=weighted_Bessel_leakage_upper(spectral_cells=32)
        b=weighted_Bessel_leakage_upper(spectral_cells=64)
        c=weighted_Bessel_leakage_upper(spectral_cells=96)
        self.assertGreater(a["weighted_low_Fourier_leakage_exact_upper"],
                           b["weighted_low_Fourier_leakage_exact_upper"])
        self.assertGreater(b["weighted_low_Fourier_leakage_exact_upper"],
                           c["weighted_low_Fourier_leakage_exact_upper"])
        self.assertLess(c["weighted_low_Fourier_leakage_exact_upper"],F(1,4))

    def test_lower_moment_method_does_not_invent_negative_original_zeta(self):
        c=weighted_Bessel_leakage_upper(m=3,spectral_cells=96)
        mG=c["Gamma_multiplier_exact"]
        mW=c["weighted_low_Fourier_leakage_exact_upper"]
        polar=F(8)*F(1,4)**6/factorial(3)**2
        self.assertLess(mG-mW-F(47,8)-polar,0)
        self.assertFalse(c["RH_proved"])

    def test_wrong_real_Gamma_parity_is_not_an_authentic_source_certificate(self):
        o=F(13);o2=o*o
        wrong=sum((F(4,4*j+3)*o2/(o2+F((4*j+3)**2,4))
                   for j in range(128)),F())
        self.assertLess(wrong,F(6097,1000))
        self.assertGreater(gamma_fourier_multiplier_lower(o,128),F(6097,1000))
        self.assertFalse(source_weighted_four_moment_certificate()["RH_proved"])

    def test_bad_source_coefficients_and_unbounded_angular_approximations_fail(self):
        for opts in (
            dict(m=0),dict(m=True),dict(Omega=0),
            dict(Omega=13.0),dict(a=0),
            dict(angular_modes=4),dict(series_order=33),
            dict(error_slack=0),dict(spectral_cells=1),
        ):
            with self.assertRaises(WeightedBesselSourceError):
                weighted_Bessel_leakage_upper(**opts)


class TrueWeilFourMomentPositivity(unittest.TestCase):
    def test_full_completed_zeta_source_sign_certified_for_all_four_moment_tests(self):
        d=source_weighted_four_moment_certificate()
        self.assertEqual(d["source"],"SHA_PINNED_ORIGINAL_COMPLETED_ZETA_FIRST_PRIME")
        self.assertEqual(d["source_suzuki_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(d["genuine_prime_power_labels"],(2,))
        self.assertEqual(d["vanishing_polynomial_moments"],4)
        self.assertGreater(d["exact_positive_Gamma_multiplier"],F(6097,1000))
        self.assertLess(d["exact_weighted_Bessel_leakage_upper"],F(2013,10000))
        self.assertEqual(d["negative_pole_moment_tail_upper"],F(1,4718592))
        self.assertLess(d["negative_pole_moment_tail_upper"],F(1,1000000))
        self.assertEqual(d["elementary_rational_lower"],F(20699,1000000))
        self.assertGreater(d["original_Weil_L2_lower_exact"],F(1,50))
        self.assertTrue(d["completed_Weil_four_moment_strictly_above_1over50"])
        self.assertTrue(d["genuine_four_moment_infinite_dimensional_test_class"])
        self.assertFalse(d["first_prime_all_test_Weil_positivity_proved"])
        self.assertFalse(d["RH_proved"])

    def test_fraction_source_checksum_is_not_fitted_float_or_unbounded_decimal_text(self):
        a=exact_fraction_bytes(F(1,3))
        b=exact_fraction_bytes(F(1,4))
        self.assertNotEqual(a,b)
        v=source_weighted_four_moment_certificate()
        self.assertEqual(
            v["source_fraction_bytes_sha256"],
            "3bf2ddfaa032fd93768204fe48ba201211e1e743402467fb419fde20cf76c765"
        )

    def test_true_four_low_suzuki_Neumann_bridge_retains_sign_and_boundaries(self):
        s=true_four_low_suzuki_interface()
        self.assertEqual(s["source"],"ORIGINAL_SUZUKI_SIGNED_FOUR_LOW_ZERO_SHIFT")
        self.assertEqual(s["low_Legendre_modes"],(1,2,3,4))
        self.assertEqual(s["low_dimension"],4)
        self.assertEqual(s["reflection_parity_low_blocks"],(2,2))
        self.assertEqual(s["genuine_high_relative_K_kappa"],F(1,50))
        self.assertEqual(s["genuine_R0_zero_shift_norm_upper"],F(121,32))
        self.assertEqual(s["K_low_high_source_boundary_rank"],2)
        self.assertTrue(s["zero_shift_Douglas_range_and_finiteness"])
        self.assertFalse(s["actual_complete_low_4x4_S0_sign_proved"])
        self.assertFalse(s["all_a_global_Weil_positive_proved"])
        self.assertFalse(s["RH_proved"])

    def test_source_suzuki_high_legendre_primitive_has_exactly_four_null_moments(self):
        a=F(1,2)
        for n in (5,6,7,9):
            u=legendre_polynomial(n,a)
            primitive=poly_primitive_zero_at_left(u,a)
            self.assertEqual(poly_eval(primitive,-a),0)
            self.assertEqual(poly_eval(primitive,a),0)
            for k in range(4):
                mon=(F(0),)*k+(F(1),)
                self.assertEqual(
                    poly_integral(poly_mul(primitive,mon),-a,a),0,
                    msg=f"source Legendre mode n={n} moment k={k}"
                )
        self.assertEqual(inverse_neumann_boundary_channels(a,4)[
            "K_low_high_cross_rank"],2)

    def test_previous_authentic_seven_moment_theorem_is_preserved(self):
        old=original_seven_moment_weil_certificate()
        self.assertTrue(old["genuine_original_Q_zeta_strictly_above_K_1over16"])
        self.assertGreater(old["simple_rational_L2_gap_lower"],F(1,16))
        self.assertFalse(old["RH_proved"])


if __name__=="__main__":
    unittest.main()
