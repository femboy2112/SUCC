"""Independent exact-rational Suzuki first-onset adversarial controls."""
from __future__ import annotations
import unittest
from fractions import Fraction as Q
from observational_succ.suzuki_first_prime import (
    SuzukiWavefrontError, prime_power, atanh_log_interval,
    genuine_prime_weight_interval, first_prime_wavefront, hs_squared,
    prime_differential_form, prime_kernel_form_piecewise, l2_piecewise, translated_overlap,
    neumann_quadratic, onset_archimedean_certificate,
    derivative_norm2_piecewise, low_regularization_certificate,
)


def wave_pair(sign: int):
    """Two triangular hats separated by rational c=7/10 on [-2/5,2/5]."""
    return ((Q(-2,5),Q(0)),(Q(-3,8),Q(1)),(Q(-7,20),Q(0)),
            (Q(3,10),Q(0)),(Q(13,40),Q(sign)),(Q(7,20),Q(0)),
            (Q(2,5),Q(0)))


class SuzukiFirstPrimeTests(unittest.TestCase):
    def test_authentic_prime_power_and_fake_six(self):
        self.assertEqual(prime_power(2),(2,1))
        self.assertEqual(prime_power(4),(2,2))
        self.assertEqual(prime_power(9),(3,2))
        self.assertIsNone(prime_power(6))
        self.assertIsNone(prime_power(12))
        self.assertIsNone(prime_power(10))
        with self.assertRaises(SuzukiWavefrontError):
            genuine_prime_weight_interval(6)
        with self.assertRaises(SuzukiWavefrontError):
            prime_power(1)

    def test_log_arithmetic_intervals(self):
        l2,u2=atanh_log_interval(2,10)
        l3,u3=atanh_log_interval(3,15)
        self.assertTrue(Q(69,100)<l2<u2<Q(7,10))
        self.assertTrue(Q(109,100)<l3<u3<Q(11,10))
        self.assertLess(u2-l2,Q(1,10**9))
        l4,u4=atanh_log_interval(4,25)
        self.assertTrue(2*l2<l4<2*u2 and 2*l2<u4<2*u2)

    def test_first_prime_threshold_and_scale(self):
        s=first_prime_wavefront(Q(2,5))
        self.assertEqual(s["first_prime"],2)
        self.assertEqual(s["prime_power_source"],"Lambda(2)=log 2; no other active prime powers")
        self.assertTrue(Q(s["kernel_HS_lower"])>0)
        self.assertLess(Q(s["kernel_HS_upper"]),Q(1,50))
        self.assertGreater(Q(s["differentiated_operator_norm_lower"]),Q(48,100))
        self.assertFalse(s["RH_proved"])
        for a in (Q(1,4),Q(3,5),Q(11,20)):
            with self.assertRaises(SuzukiWavefrontError):
                first_prime_wavefront(a)
        with self.assertRaises(SuzukiWavefrontError):
            first_prime_wavefront(.4)

    def test_exact_hs_scaling_w4(self):
        b=Q(7,11)
        a=Q(2,5);c=Q(7,10)
        w=2*a-c
        self.assertEqual(hs_squared(a,c,b),b*b*w**4/6)
        # At half the corner width HS decreases by factor 4 (HS² by 16).
        a2=(c+w/2)/2
        self.assertEqual(hs_squared(a2,c,b),hs_squared(a,c,b)/16)
        with self.assertRaises(SuzukiWavefrontError):
            hs_squared(Q(1,4),c,b)

    def test_prime_shift_pair_has_sharp_pm_b_rayleigh(self):
        c=Q(7,10);b=Q(9,13)
        plus,minus=wave_pair(1),wave_pair(-1)
        self.assertGreater(l2_piecewise(plus),0)
        self.assertEqual(l2_piecewise(plus),l2_piecewise(minus))
        self.assertEqual(prime_differential_form(plus,c,b),-b*l2_piecewise(plus))
        self.assertEqual(prime_differential_form(minus,c,b),+b*l2_piecewise(minus))
        self.assertEqual(translated_overlap(plus,c),-translated_overlap(minus,c))
        self.assertEqual(prime_differential_form(plus,c/2,b),Q(0))

    def test_independent_double_integral_of_source_ramp(self):
        # Compare two genuinely different exact algorithms: translate overlap
        # after IBP versus direct two-dimensional ramp integration.
        for sign in (1,-1):
            v=wave_pair(sign)
            for c in (Q(7,10),Q(13,20),Q(3,5),Q(1,3)):
                for b in (Q(1,2),Q(9,13)):
                    self.assertEqual(prime_kernel_form_piecewise(v,c,b),
                                     prime_differential_form(v,c,b))
        for pts in (
            ((Q(-1),0),(Q(-3,5),2),(Q(0),-1),(Q(4,5),3),(Q(1),0)),
            ((Q(-1,2),0),(Q(-1,4),3),(Q(1,6),-2),(Q(1,2),0)),
        ):
            for c in (Q(1,5),Q(2,3),Q(4,5)):
                self.assertEqual(prime_kernel_form_piecewise(pts,c,Q(5,7)),
                                 prime_differential_form(pts,c,Q(5,7)))

    def test_cross_boundary_mutation_changes_signal(self):
        v=wave_pair(1)
        c=Q(7,10);b=Q(9,13)
        self.assertNotEqual(prime_differential_form(v,c,b),
                            prime_differential_form(v,c,b/2))
        self.assertNotEqual(prime_differential_form(v,c,b),
                            prime_differential_form(v,Q(3,5),b))

    def test_derivative_budget_and_hs_spectral_bound(self):
        for sign in (1,-1):
            v=wave_pair(sign)
            self.assertGreater(derivative_norm2_piecewise(v),0)
            for b in (Q(2,3),Q(9,13)):
                r=low_regularization_certificate(v,Q(2,5),Q(7,10),b)
                self.assertTrue(r["proved_cauchy_schwarz_for_test"])
                self.assertFalse(r["uniform_L2_relative_bound_derived"])
                self.assertFalse(r["RH_proved"])
        with self.assertRaises(SuzukiWavefrontError):
            low_regularization_certificate(wave_pair(1),Q(1,2),Q(7,10),Q(1))

    def test_exact_neumann_inverse_quadratic(self):
        for a in (Q(1,4),Q(2,5),Q(3,4),Q(7,5)):
            steps=((-a,Q(0),Q(1)),(Q(0),a,Q(-1)))
            form,integral=neumann_quadratic(steps,a)
            self.assertEqual(form,integral)
            self.assertEqual(form,2*a**3/3)
        with self.assertRaises(SuzukiWavefrontError):
            neumann_quadratic(((Q(-1),Q(0),Q(1)),
                               (Q(0),Q(1),Q(1))),Q(1))

    def test_uniform_boundary_positivity_beyond_prime_onset(self):
        r=onset_archimedean_certificate()
        self.assertEqual(r["full_Weil_form_lower_over_L2"],"8/35")
        self.assertTrue(all(r["constant_inequality_checks"].values()))
        self.assertTrue(r["uses_complete_real_place"])
        self.assertFalse(r["all_Cc_infinity_positivity_proved"])
        self.assertFalse(r["lambda_a_positive_proved"])
        self.assertFalse(r["RH_proved"])


if __name__=='__main__': unittest.main()
