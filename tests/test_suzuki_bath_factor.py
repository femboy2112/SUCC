import unittest
from fractions import Fraction as Q
import math
from observational_succ.suzuki_bath_factor import (
    alpha,bath_weight,bath_tail_mass_interval,bath_tail_operator_norm_upper,
    gamma_linear_coefficient_interval,elementary_rational_ou_psd,bath_source_receipt,
    certified_prime_free_small_interval,high_frequency_bath_tail_lower,
)
from observational_succ.suzuki_prime_boundary import SuzukiWavefrontError


class SuzukiBathFactorTests(unittest.TestCase):
    def test_actual_gamma_source_coefficients_not_magic_psd(self):
        self.assertEqual(alpha(0),Q(1,2))
        self.assertEqual(alpha(1),Q(5,2))
        self.assertEqual(bath_weight(0),Q(4))
        self.assertEqual(bath_weight(1),Q(4,25))
        lo,hi=gamma_linear_coefficient_interval()
        independent=0.5772156649015329+math.pi/2+3*math.log(2)+math.log(math.pi)
        self.assertLessEqual(float(lo),independent)
        self.assertGreaterEqual(float(hi),independent)

    def test_monotone_gamma_ou_tail_and_operator_envelope(self):
        previous=Q(1_000)
        for N in (1,2,4,8,16,32,64,128):
            lo,hi=bath_tail_mass_interval(N)
            self.assertGreater(lo,0)
            self.assertGreater(hi,lo)
            self.assertLess(hi,previous)
            previous=hi
            # independent 5000-mode finite subset lies below tail upper.
            finite=sum((bath_weight(j) for j in range(N,N+500)),Q())
            self.assertLess(finite,hi)
            self.assertEqual(bath_tail_operator_norm_upper(N,Q(1)),2*hi)

    def test_positive_ou_convolution_finite_rational_independent_factor(self):
        for rho in (Q(1,2),Q(2,3),Q(1,5)):
            for vec in ((Q(1),Q(-1)), (Q(1),Q(2),Q(-7)),
                        (Q(),Q(),Q(),Q(1)),(Q(1,3),Q(-4,7),Q(8,3),Q(-1))):
                c=elementary_rational_ou_psd(rho,vec)
                self.assertTrue(c["nonnegative"])
                self.assertEqual(c["quadratic"],c["independent_positive_factor"])

    def test_first_rigorous_unconditional_whole_interval_positivity(self):
        for a,N in ((Q(1,12),64),(Q(1,16),64),(Q(1,20),48)):
            c=certified_prime_free_small_interval(a,N)
            self.assertTrue(c["lambda_a_strictly_positive_certified"])
            self.assertGreater(Q(c["lambda_a_whole_space_lower_rational"]),0)
            self.assertTrue(c["all_smaller_radii_included"])
            self.assertTrue(c["gamma_pole_terms_accounted_for"])
            self.assertFalse(c["global_RH_proved"])
        for bad in (Q(1,2),Q(1),0.08,Q(-1,16)):
            with self.assertRaises(SuzukiWavefrontError):
                certified_prime_free_small_interval(bad,32)

    def test_positive_tail_can_be_tiny_in_G_but_unbounded_in_DGD(self):
        for N in (1,4,32):
            previous=Q()
            for omega in (64,256,1024,4096):
                r=high_frequency_bath_tail_lower(N,omega)
                b=Q(r["m_tail_at_frequency_lower"])
                self.assertGreaterEqual(b,previous)
                previous=b
            self.assertGreater(Q(high_frequency_bath_tail_lower(N,4096)["m_tail_at_frequency_lower"]),0)
        self.assertTrue(high_frequency_bath_tail_lower(4,1024)["cannot_bound_differentiated_tail_by_small_compact_G_norm"])

    def test_source_decomposition_against_independent_direct_lerch_formula(self):
        import mpmath as mp
        mp.mp.dps=55
        X=[mp.mpf(0),mp.mpf(1)/4,mp.mpf(3)/5]
        U=[mp.mpf(1),mp.mpf(-2),mp.mpf(1)]
        C=mp.euler+mp.pi/2+3*mp.log(2)+mp.log(mp.pi)
        def direct(t):
            return (-8*(mp.cosh(t/2)-1)+C*t/2 -
                    (mp.zeta(2,mp.mpf(1)/4)-mp.exp(-t/2)*
                     mp.lerchphi(mp.exp(-2*t),2,mp.mpf(1)/4))/4)
        def resolved(t):
            positive_bath=mp.exp(-t/2)*mp.lerchphi(mp.exp(-2*t),2,mp.mpf(1)/4)/4
            return positive_bath+C*t/2-8*mp.cosh(t/2)
        q=sum((U[i]*U[j]*direct(abs(X[i]-X[j]))
               for i in range(3) for j in range(3)),mp.mpf(0))
        r=sum((U[i]*U[j]*resolved(abs(X[i]-X[j]))
               for i in range(3) for j in range(3)),mp.mpf(0))
        self.assertLess(abs(q-r),mp.mpf('1e-48'))

    def test_controls_are_not_mislabeled_as_real_prime_measurements(self):
        r=bath_source_receipt()
        self.assertTrue(r["genuine_prime_power_translations_must_be_added"])
        self.assertEqual(r["signed_inverse_neumann_term"],"-C K_a")
        self.assertFalse(r["RH_proved"])
        self.assertTrue(elementary_rational_ou_psd(Q(1,2),(Q(1),))["not_an_actual_prime_kernel"])
        for rho in (Q(0),Q(1),Q(3,2),0.5):
            with self.assertRaises(SuzukiWavefrontError):
                elementary_rational_ou_psd(rho,(1,2))


if __name__=='__main__':unittest.main()
