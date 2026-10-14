import unittest
from fractions import Fraction as Q
from math import isqrt
from observational_succ.suzuki_prime_boundary import (
    SuzukiWavefrontError, prime_power, source_jet, first_prime_window,
    ratio_window, tent_certificate, positive_dilation_log_energy_envelope,
    full_strength_energy_debt, sampled_fake_source_control, complete_receipt,
    validate_arithmetic_jet,
)


class SuzukiPrimeBoundaryTests(unittest.TestCase):
    def test_source_prime_powers_not_fake_six(self):
        expect={2:(2,1),3:(3,1),4:(2,2),5:(5,1),6:None,
                8:(2,3),9:(3,2),10:None,12:None,16:(2,4),25:(5,2)}
        for n, value in expect.items():
            self.assertEqual(prime_power(n), value)
            if value is None:
                self.assertEqual(source_jet(n)["weight"], "0")

    def test_independent_trial_division_source(self):
        for n in range(2,1500):
            div=[d for d in range(2,isqrt(n)+1) if n%d==0]
            pp=prime_power(n)
            if not div:
                self.assertEqual(pp,(n,1))
            elif pp:
                p,j=pp
                self.assertTrue(all(p%d for d in range(2,isqrt(p)+1)))
                self.assertEqual(p**j,n)

    def test_first_window_integer_inequality(self):
        v=first_prime_window(Q(3,5))
        self.assertEqual(v["delta_over_log_n"],"1/5")
        self.assertEqual(v["only_active_arithmetic_jet"],2)
        self.assertEqual(v["g_raw_HS_sq_over_c_sq_log_n_fourth"],"1/3750")
        self.assertFalse(v["pole_gamma_part_included"])
        for invalid in (Q(1,2),Q(4,5),Q(1),Q(1,3)):
            with self.assertRaises(SuzukiWavefrontError):
                first_prime_window(invalid)

    def test_jet_geometric_shape(self):
        for n in (2,3,4,5,8,9,27):
            r=ratio_window(n,Q(3,5))
            self.assertEqual(r["differentiated_op_norm_over_c"], "1")
            self.assertEqual(r["g_raw_HS_sq_over_c_sq_log_n_fourth"],"1/3750")
        with self.assertRaises(SuzukiWavefrontError):
            ratio_window(6,Q(3,5))

    def test_independently_integrated_tent_moments(self):
        # Integral of x^2 over [0,delta/2] doubled, direct elementary calculus.
        for d in (Q(1,5),Q(1,4),Q(2,7),Q(1,40)):
            r=tent_certificate(d)
            each=2*(d/2)**3/3
            self.assertEqual(Q(r["shift_overlap_in_dimensionless_variable"]),each)
            self.assertEqual(Q(r["norm2_in_dimensionless_variable"]),2*each)
            self.assertEqual(Q(r["H1_seminorm_sq_in_dimensionless_variable"]),2*d)
            self.assertEqual(Q(r["H1_over_L2_in_dimensionless_variable"]),12/d**2)
            self.assertEqual(Q(r["symmetric_Rayleigh_over_c"]),-1)
            self.assertEqual(Q(r["antisymmetric_Rayleigh_over_c"]),1)

    def test_exact_two_block_chirality(self):
        # Matrix -[[0,1],[1,0]] has eigen-directions (1,1), (1,-1).
        for l,r in ((1,1),(3,3),(4,-4),(2,-7)):
            numerator=-2*l*r
            norm=l*l+r*r
            self.assertLessEqual(abs(numerator),norm)
        self.assertEqual(-2*Q(1)*Q(1)/(1+1),-1)
        self.assertEqual(-2*Q(1)*Q(-1)/(1+1),1)

    def test_exact_rational_fourier_debt_certificate(self):
        for m in (1,2,4,8,16,32):
            d=Q(1,2**(2*m))
            low=Q(full_strength_energy_debt(m)["needed_log_energy_over_mass_at_full_prime_shift_at_least"])
            self.assertGreater(low,0)
            self.assertEqual(low, Q(m,3)*(1-Q(4,3)/2**m))
            e=positive_dilation_log_energy_envelope(d,m,Q(1),max(Q(1),low))
            self.assertGreaterEqual(Q(e["certified_abs_prime_form_over_c_upper"]),1)

    def test_conditional_bound_not_wrongly_called_observation(self):
        c=positive_dilation_log_energy_envelope(Q(1,9),3,Q(1),Q(5))
        self.assertTrue(c["conditional_on_energy_ceiling"])
        self.assertFalse(c["RH_proved"])
        for args in ((Q(-1),3,1,3),(Q(1),0,1,3),
                     (Q(1),3,3,1),(Q(1),3,Q(1,2),Q(1,3)),
                     (0.25,3,1,3)):
            with self.assertRaises(SuzukiWavefrontError):
                positive_dilation_log_energy_envelope(*args)

    def test_source_negative_controls(self):
        r=sampled_fake_source_control()
        self.assertTrue(r["fake_composite_6_is_zero"])
        self.assertEqual(r["correctly_excluded"],[6,10,12])
        self.assertFalse(complete_receipt()["RH_proved"])

    def test_source_authentication_mutations_without_fitted_phases(self):
        self.assertTrue(validate_arithmetic_jet(4,2,2,Q(1,2),4)['accepted'])
        self.assertFalse(validate_arithmetic_jet(6,6,1,Q(1,2),6)['accepted'])
        self.assertTrue(validate_arithmetic_jet(6,6,1,Q(1,2),6)['fake_composite_rejected'])
        self.assertTrue(validate_arithmetic_jet(4,2,2,Q(2,3),4)['wrong_half_density_rejected'])
        self.assertTrue(validate_arithmetic_jet(4,2,2,Q(1,2),2)['wrong_log_phase_rejected'])
        self.assertFalse(validate_arithmetic_jet(4,2,2,Q(1,2),2)['accepted'])
        self.assertFalse(validate_arithmetic_jet(4,2,3,Q(1,2),4)['accepted'])

    def test_bad_types_not_ghost_sources(self):
        for n in (1,0,-2,2.0,True):
            with self.assertRaises(SuzukiWavefrontError):
                prime_power(n)
        with self.assertRaises(SuzukiWavefrontError):
            ratio_window(2,0.6)


if __name__ == "__main__":
    unittest.main()
