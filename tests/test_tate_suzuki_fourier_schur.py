"""Hostile, source-pinned Tate/Gamma Fourier high-moment → Suzuki Schur tests."""
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.tate_suzuki_fourier_schur import (
    FourierSchurGateError, gamma_fourier_multiplier_lower,
    moment_taylor_low_fourier_fraction, source_first_prime_spectral_budget,
    spectral_hard_gates, tate_suzuki_zero_shift_interface,
    verify_cross_source_failure_modes,
)
from observational_succ.suzuki_legendre_source import (
    legendre_polynomial, poly_primitive_zero_at_left, poly_integral,
    poly_eval, poly_derivative, authentic_full_low_entry,
)
from observational_succ.suzuki_moment_schur import (
    inverse_neumann_boundary_channels, low_inverse_neumann,
)
from observational_succ.one_object_residual_schur import (
    KAPPA as PR109_INHERITED_KAPPA,
    finite_residual_certificate, rayleigh,
)
from observational_succ.tate_eta_bernoulli import (
    eta_eisenstein_prime_transducer, tate_completed_theta_polar_split
)


class ExactFourierGammaEnergy(unittest.TestCase):
    def test_gamma_multiplier_comes_from_actual_4j_plus_one_tate_real_rungs(self):
        w=F(12)
        direct=sum(
            (F(4,4*j+1)*w*w/(w*w+F((4*j+1)**2,4))
             for j in range(32)), F()
        )
        self.assertEqual(gamma_fourier_multiplier_lower(w,32),direct)
        self.assertGreater(direct,F(6))
        self.assertLess(gamma_fourier_multiplier_lower(w,16),direct)
        self.assertGreater(gamma_fourier_multiplier_lower(F(13),32),direct)
        self.assertLess(direct,gamma_fourier_multiplier_lower(w,64))
        self.assertGreater(direct-F(95,16),F(1,16))

    def test_moment_low_Fourier_mass_with_exact_oscillatory_Taylor_not_exp(self):
        a=F(1,2);Omega=F(12)
        for m in (15,16,18,30):
            got=moment_taylor_low_fourier_fraction(a,Omega,m)
            direct=F(12,3*(2*m+1))*F(6)**(2*m)/factorial(m)**2
            self.assertEqual(got,direct)
        self.assertGreater(moment_taylor_low_fourier_fraction(a,Omega,15),F(1,100))
        self.assertLess(moment_taylor_low_fourier_fraction(a,Omega,18),F(1,30000))
        self.assertLess(moment_taylor_low_fourier_fraction(a,Omega,30),F(1,10**16))

    def test_source_high_coercivity_at_ranks16_18_30_and_scope(self):
        p15=source_first_prime_spectral_budget(15)
        p16=source_first_prime_spectral_budget(16)
        p18=source_first_prime_spectral_budget(18)
        p30=source_first_prime_spectral_budget(30)
        self.assertEqual(p16["true_prime_power_labels"],(2,))
        self.assertEqual(p16["completed_negative_budget_strict_upper"],F(95,16))
        self.assertEqual(p16["original_git_blob"],
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertLess(p15["original_Weil_L2_gap_strict_lower"],0)
        self.assertGreater(p16["original_Weil_L2_gap_strict_lower"],F(1,20))
        self.assertGreater(p18["original_Weil_L2_gap_strict_lower"],F(1,16))
        self.assertGreater(p30["original_Weil_L2_gap_strict_lower"],F(1,16))
        self.assertTrue(p16["relative_Neumann_kappa_1over20_proved"])
        self.assertTrue(p18["relative_Neumann_kappa_1over16_proved"])
        self.assertTrue(p30["relative_Neumann_kappa_1over16_proved"])
        self.assertFalse(p15["certifies_high_moment_W_zeta_positive"])
        self.assertFalse(p30["unrestricted_low_Schur_sign_proved"])
        self.assertFalse(p30["RH_proved"])
        self.assertEqual(spectral_hard_gates()["rank18_high_kappa"],F(1,16))
        self.assertEqual(PR109_INHERITED_KAPPA,F(369,10000))
        self.assertGreater(F(1,16),PR109_INHERITED_KAPPA)

    def test_wrong_real_gamma_parity_loses_original_source_certificate(self):
        w=F(12)
        wrong=sum((F(4,4*j+3)*w*w/(w*w+F((4*j+3)**2,4))
                   for j in range(32)),F())
        self.assertLess(wrong,F(95,16))
        m18=moment_taylor_low_fourier_fraction(F(1,2),w,18)
        self.assertLess(wrong*(1-m18)-F(95,16),0)
        self.assertGreater(source_first_prime_spectral_budget(18)[
            "original_Weil_L2_gap_strict_lower"],F(1,16))

    def test_invalid_source_domains_refuse_float_bool_unlicensed_moments(self):
        for w,j in ((0,32),(-1,32),(12,0),(12,513),(12,True),
                    (12.0,32),(True,32)):
            with self.assertRaises(FourierSchurGateError):
                gamma_fourier_multiplier_lower(w,j)
        for a,Om,m in ((0,12,18),(F(1,2),0,18),
                       (F(1,2),12,0),(F(1,2),12,129),
                       (F(1,2),12,True),(0.5,12,18)):
            with self.assertRaises(FourierSchurGateError):
                moment_taylor_low_fourier_fraction(a,Om,m)
        for r in (0,31,True,18.0):
            with self.assertRaises(FourierSchurGateError):
                source_first_prime_spectral_budget(r)


class ExactSUCCLegendreMomentBridge(unittest.TestCase):
    def test_legendre_high_to_primitive_moment_annihilation_rank18_and_30(self):
        a=F(1,2)
        for r in (16,18,30):
            p=legendre_polynomial(r+1,a)
            f=poly_primitive_zero_at_left(p,a)
            self.assertEqual(poly_eval(f,-a),0)
            self.assertEqual(poly_eval(f,a),0)
            self.assertEqual(poly_derivative(f),p)
            for k in range(r):
                moment=poly_integral(tuple(F(0) for _ in range(k))+
                                     tuple(f),-a,a) if False else \
                                     sum((F(c)*(a**(i+k+1)-(-a)**(i+k+1))/(i+k+1)
                                          for i,c in enumerate(f)),F())
                self.assertEqual(moment,0,msg=f"moment {k} for high mode {r+1}")
            # Orthogonal high u has positive actual Neumann quadratic energy.
            energy=poly_integral(tuple(
                sum((f[i]*f[j] for i in range(len(f))
                     for j in range(len(f)) if i+j==k),F())
                for k in range(2*len(f)-1)), -a,a)
            self.assertGreater(energy,0)

    def test_original_Neumann_boundary_channels_survive_actual_shorting(self):
        for r in (16,18,30):
            x=inverse_neumann_boundary_channels(F(1,2),r)
            self.assertEqual(x["K_low_high_cross_rank"],2)
            self.assertEqual(len(x["channels"]),2)
            self.assertFalse(x["source_G_cross_rank_only_two"])
        self.assertNotEqual(low_inverse_neumann(F(1,2),18)[0][0],F(0))

    def test_independent_tate_source_passport_and_fake_six_not_admissible(self):
        t=tate_completed_theta_polar_split(F(5,2))
        self.assertEqual(t["completed_pole_cancellation_after_xi"],F(1,2))
        self.assertEqual(t["real_Tate_archimedean"],"pi^(-s/2)*Gamma(s/2)")
        source=eta_eisenstein_prime_transducer(12)
        self.assertTrue(source["transport_preserves_genuine_von_mangoldt"])
        forged=eta_eisenstein_prime_transducer(12,True)
        self.assertFalse(forged["transport_preserves_genuine_von_mangoldt"])
        self.assertEqual(forged["composite_six_residual_prime_log_basis"],
                         {2:1,3:1})


class TrueFirstWindowZeroShift(unittest.TestCase):
    def test_source_derivative_and_new_high_Schur_passport(self):
        p18=tate_suzuki_zero_shift_interface(18)
        p30=tate_suzuki_zero_shift_interface(30)
        self.assertEqual(p18["source"],"ORIGINAL_TATE_XI_WEIL_SUZUKI")
        self.assertEqual(p18["legendre_parity_low_ranks"],(9,9))
        self.assertEqual(p30["legendre_parity_low_ranks"],(15,15))
        self.assertEqual(p18["high_operator_D_at_least_kappa_K"],F(1,16))
        self.assertEqual(p30["high_operator_D_at_least_kappa_K"],F(1,16))
        self.assertEqual(p30["zero_shift_R0_operator_norm_strict_upper"],F(121,100))
        self.assertEqual(p18["naive_norm_only_certificate_upper_below_zero"],
                         -F(187,200))
        self.assertTrue(p30["zero_shift_Douglas_cross_range_proved"])
        self.assertFalse(p30["low_source_30x30_S0_sign_certified"])
        self.assertFalse(p30["all_radii_transport_proved"])
        self.assertFalse(p30["RH_proved"])

    def test_rank16_low_reduction_and_unproved_low_short_sign(self):
        p=tate_suzuki_zero_shift_interface(16)
        self.assertEqual(p["high_operator_D_at_least_kappa_K"],F(1,20))
        self.assertEqual(p["legendre_parity_low_ranks"],(8,8))
        self.assertEqual(p["zero_shift_R0_operator_norm_strict_upper"],F(121,80))
        self.assertFalse(p["low_source_30x30_S0_sign_certified"])
        for r in (0,15,17,31,True):
            with self.assertRaises(FourierSchurGateError):
                tate_suzuki_zero_shift_interface(r)

    def test_mutation_cannot_inherit_rank16_positive_sign(self):
        g=verify_cross_source_failure_modes()
        self.assertTrue(g["mutation_loses_rank16_kappa_1over20"])
        self.assertTrue(g["fake_six_is_source_invalid_even_if_outside_this_window"])
        self.assertTrue(g["moment_rank15_negative_budget_is_NOT_counterexample_to_zeta"])
        self.assertFalse(g["RH_proved"])

    def test_imported_residual_toy_shows_both_possible_low_signs(self):
        # Calibrate generic Schur algebra; synthetic matrices never zeta data.
        A=((F(1,3),),)
        B=((F(1,4),F(1,6)),)
        K=((F(1,4),0),(0,F(1,9)))
        D=((F(1,2),0),(0,F(1,3)))
        H=((F(1,2),),(F(1,2),))
        plus=finite_residual_certificate(A,B,D,K,H,F(1,16))
        minus=finite_residual_certificate(((F(1,6),),),B,D,K,H,F(1,16))
        self.assertGreater(plus.exact_short[0][0],0)
        self.assertLess(minus.exact_short[0][0],0)
        self.assertFalse(plus.RH_proved and minus.RH_proved)

    def test_an_actual_original_source_low_entry_is_an_interval_not_Schur(self):
        # Real source original Gamma, n=2, poles, contact, no arbitrary x-grid.
        src=authentic_full_low_entry(1,1,F(1,2),J=2)
        self.assertLess(src.lo,src.hi)
        self.assertTrue(src.lo<1 and src.hi>-1)
        off=authentic_full_low_entry(1,2,F(1,2),J=2)
        self.assertEqual((off.lo,off.hi),(F(),F()))


if __name__ == "__main__":
    unittest.main()
