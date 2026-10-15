"""Hostile exact Tate/Suzuki seven-moment Bessel versus old Taylor proof."""
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.tate_bessel_seven_schur import (
    BesselSchurError, odd_double_factorial,
    spherical_bessel_polynomial_l2,
    exact_legendre_low_frequency_enclosure,
    original_seven_moment_weil_certificate,
    original_seven_low_suzuki_schur_interface,
)
from observational_succ.tate_suzuki_fourier_schur import (
    gamma_fourier_multiplier_lower, moment_taylor_low_fourier_fraction
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial, poly_primitive_zero_at_left,
    poly_eval, poly_mul, poly_integral
)
from observational_succ.suzuki_moment_schur import inverse_neumann_boundary_channels


class ExactSphericalBesselFourierProjector(unittest.TestCase):
    def test_double_factorial_and_true_spherical_series(self):
        self.assertEqual(odd_double_factorial(1),1)
        self.assertEqual(odd_double_factorial(3),3)
        self.assertEqual(odd_double_factorial(15),2027025)
        self.assertEqual(odd_double_factorial(41),13113070457687988603440625)
        with self.assertRaises(BesselSchurError):
            odd_double_factorial(14)
        with self.assertRaises(BesselSchurError):
            odd_double_factorial(True)

    def test_every_polynomial_integral_is_exact_positive_and_error_geometric(self):
        A=F(49,8)
        for l in (7,8,11,19):
            for order in (6,10,12):
                z=spherical_bessel_polynomial_l2(l,order,A)
                self.assertGreater(z["polynomial_L2_squared_exact"],0)
                self.assertGreater(z["pointwise_absolute_Bessel_remainder_upper"],0)
                self.assertLess(z["geometric_next_ratio_upper"],F(1))
                self.assertTrue(z["rigorous_for_every_real_z_from_zero_to_A"])
        x=spherical_bessel_polynomial_l2(7,6,A)
        y=spherical_bessel_polynomial_l2(7,10,A)
        self.assertGreater(x["pointwise_absolute_Bessel_remainder_upper"],
                           y["pointwise_absolute_Bessel_remainder_upper"])

    def test_exponential_projection_uses_exact_bessel_moment_space_not_Taylor_surrogate(self):
        b=exact_legendre_low_frequency_enclosure()
        self.assertEqual(b["source"],"CLASSICAL_LEGENDRE_BESSEL_FOURIER_ORIGINAL_L2")
        self.assertEqual(b["vanishing_power_moments"],7)
        self.assertEqual(b["spherical_Bessel_exact_modes_from"],7)
        self.assertEqual(b["spherical_Bessel_exact_modes_through"],19)
        self.assertEqual(b["Taylor_order"],10)
        self.assertEqual(b["series_square_slack"],F(1,10000))
        self.assertTrue(b["low_Fourier_mass_below_1_over_61"])
        self.assertLess(b["low_Fourier_mass_fraction_strict_upper"],F(1,61))
        self.assertGreater(b["low_Fourier_mass_fraction_strict_upper"],F(1,100))
        # Old uniform Taylor estimate cannot handle seven moments here.
        old=moment_taylor_low_fourier_fraction(F(1,2),F(49,4),7)
        self.assertGreater(old,b["low_Fourier_mass_fraction_strict_upper"]*100)
        smaller=exact_legendre_low_frequency_enclosure(m=6)
        self.assertGreater(smaller["low_Fourier_mass_fraction_strict_upper"],F(1,20))
        self.assertFalse(smaller["low_Fourier_mass_below_1_over_61"])

    def test_source_omitted_l_modes_and_series_tails_were_not_ghosts(self):
        good=exact_legendre_low_frequency_enclosure(m=7,L=20,order=10)
        fine=exact_legendre_low_frequency_enclosure(m=7,L=22,order=12)
        self.assertGreater(good["spherical_Bessel_high_l_tail"],0)
        self.assertLess(fine["spherical_Bessel_high_l_tail"],
                        good["spherical_Bessel_high_l_tail"])
        self.assertLess(fine["low_Fourier_mass_fraction_strict_upper"],F(1,61))
        self.assertFalse(fine["RH_proved"])

    def test_independent_numeric_spherical_bessel_holdout_no_proof_status(self):
        import mpmath as mp
        with mp.workdps(42):
            z=mp.mpf(49)/8
            l=7
            actual=mp.sqrt(mp.pi/(2*z))*mp.besselj(l+mp.mpf(1)/2,z)
            est=spherical_bessel_polynomial_l2(l,10,F(49,8))
            delta=est["pointwise_absolute_Bessel_remainder_upper"]
            # Independently evaluate polynomial with the defining Bessel
            # recurrence. Numeric is ONLY a negative-control calibration.
            coefficients=[F(1,odd_double_factorial(2*l+1))]
            for k in range(10):
                coefficients.append(-coefficients[-1]/(2*(k+1)*(2*l+2*k+3)))
            approx=mp.fsum((mp.mpf(c.numerator)/c.denominator*z**(l+2*k)
                            for k,c in enumerate(coefficients)))
            upper=mp.mpf(delta.numerator)/delta.denominator
            self.assertLess(abs(actual-approx),upper)

    def test_invalid_source_omega_and_approximation_are_rejected(self):
        for fn,args in (
            (odd_double_factorial,(2,)),
            (spherical_bessel_polynomial_l2,(3,0,F(20))),
            (spherical_bessel_polynomial_l2,(3,10,F(-1))),
            (spherical_bessel_polynomial_l2,(3,10,2.5)),
            (exact_legendre_low_frequency_enclosure,(0,)),
            (exact_legendre_low_frequency_enclosure,(True,)),
        ):
            with self.assertRaises(BesselSchurError):
                fn(*args)


class OriginalCompletedWeilSevenMoments(unittest.TestCase):
    def test_genuine_first_prime_completed_Weil_sign_with_seven_moments(self):
        c=original_seven_moment_weil_certificate()
        self.assertEqual(c["source"],"SHA_PINNED_ORIGINAL_ZETA_COMPLETED_FIRST_PRIME")
        self.assertEqual(c["original_source_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(c["true_prime_power_labels"],(2,))
        self.assertEqual(c["moment_count"],7)
        self.assertEqual(c["Gamma_real_modes"],128)
        self.assertEqual(c["Fourier_Omega"],F(49,4))
        self.assertLess(c["exact_low_frequency_fraction_upper"],F(1,61))
        self.assertGreater(c["exact_Gamma_multiplier"],F(3019,500))
        self.assertLess(c["sinh_polar_moment_residual_upper"],F(1,10000))
        self.assertGreater(c["simple_rational_L2_gap_lower"],F(1,16))
        self.assertGreater(c["actual_exact_L2_gap_lower"],F(1,16))
        self.assertTrue(c["all_complex_smooth_tests_with_seven_moments"])
        self.assertFalse(c["all_original_first_window_tests_positive"])
        self.assertFalse(c["RH_proved"])

    def test_full_sinh_polar_suppression_is_source_moment_law_not_ignored_pole(self):
        m=7
        neg=8*(F(1,4)**(2*m))/factorial(m)**2
        c=original_seven_moment_weil_certificate()
        self.assertEqual(neg,c["sinh_polar_moment_residual_upper"])
        self.assertGreater(neg,0)
        self.assertEqual(c["negative_contact_plus_prime_budget"],F(47,8))

    def test_new_seven_moment_source_high_Schur_kappa_retains_true_Neumann(self):
        c=original_seven_low_suzuki_schur_interface()
        self.assertEqual(c["source"],"SHA_PINNED_ORIGINAL_SUZUKI_ZERO_SHIFT")
        self.assertEqual(c["low_unnormalized_Legendre_indices"],tuple(range(1,8)))
        self.assertEqual(c["low_dimension"],7)
        self.assertEqual(c["parity_block_low_dimensions"],(4,3))
        self.assertEqual(c["source_high_K_relative_kappa"],F(1,16))
        self.assertEqual(c["zero_shift_R0_operator_norm_strict_upper"],F(121,100))
        self.assertEqual(c["true_source_K_low_high_boundary_rank"],2)
        self.assertTrue(c["zero_shift_Douglas_range_finite"])
        self.assertFalse(c["low_7x7_actual_S0_sign_certified"])
        self.assertFalse(c["all_radius_low_sign_certified"])
        self.assertFalse(c["RH_proved"])

    def test_exact_legendre_derivative_primitive_has_all_seven_null_moments(self):
        a=F(1,2)
        # Every high Legendre basis mode maps to a function with zero
        # endpoints and vanishing first seven polynomial moments.
        for j in (8,9,10,12):
            u=legendre_polynomial(j,a)
            f=poly_primitive_zero_at_left(u,a)
            self.assertEqual(poly_eval(f,-a),0)
            self.assertEqual(poly_eval(f,a),0)
            for k in range(7):
                mon=(F(0),)*k+(F(1),)
                moment=poly_integral(poly_mul(f,mon),-a,a)
                self.assertEqual(moment,0,msg=f"legendre {j}, moment {k}")
        self.assertEqual(inverse_neumann_boundary_channels(a,7)[
            "K_low_high_cross_rank"],2)


if __name__=="__main__":
    unittest.main()
