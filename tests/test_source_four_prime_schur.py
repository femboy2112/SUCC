"""Full first-prime original signed source four-column residual and Schur replay."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.source_four_center_gram import (
    SourceCenterError,authentic_four_mode_finite_center_moment,
    B3_weighted_center_tail_upper,authentic_four_center_certificate,
    robust_center_energy_for_direction,_poly_moment
)
from observational_succ.source_four_prime_schur import CertifiedFourPrimeSchurTrial
from observational_succ.source_prime_center_alignment import (
    _original_finite_center_derivative_integral,
    certified_true_P1_center_residual
)
from observational_succ.suzuki_legendre_source import legendre_polynomial
from observational_succ.direct_quotient_schur import exact_psd


class OriginalFourDerivativeSource(unittest.TestCase):
    def test_p1_original_center_integrator_independent_replay(self):
        for J in (1,4,8):
            fresh=authentic_four_mode_finite_center_moment(1,J,0)
            inherited=_original_finite_center_derivative_integral(1,J)
            self.assertLessEqual(max(fresh.lo,inherited.lo),min(fresh.hi,inherited.hi))
        # True prime2 does not touch C0: source mode 2 derivative is odd.
        self.assertEqual(authentic_four_mode_finite_center_moment(2,3,0).lo,F(0))
        self.assertEqual(authentic_four_mode_finite_center_moment(2,3,0).hi,F(0))
        self.assertEqual(authentic_four_mode_finite_center_moment(3,3,1).lo,F(0))
        self.assertEqual(authentic_four_mode_finite_center_moment(3,3,1).hi,F(0))

    def test_independent_center_polynomial_weights(self):
        s=F(1,8)
        self.assertEqual(_poly_moment(legendre_polynomial(0,F(1,2)),0),F(1,4))
        self.assertEqual(_poly_moment(legendre_polynomial(2,F(1,2)),0),-F(15,128))
        self.assertEqual(_poly_moment(legendre_polynomial(1,F(1,2)),1),F(1,384))
        self.assertEqual(_poly_moment(legendre_polynomial(3,F(1,2)),1),-F(15,4096))

    def test_true_gamma_weighted_center_tail_monotone(self):
        for k in (1,2,3,4):
            t=0 if k%2 else 1
            self.assertGreater(B3_weighted_center_tail_upper(k,20,t),0)
            self.assertGreater(B3_weighted_center_tail_upper(k,20,t),
                               B3_weighted_center_tail_upper(k,64,t))

    def test_real_even_block_offdiagonal_measured_rankone_sign(self):
        from observational_succ.source_four_center_gram import authenticated_center_rankone_cross_intervals
        c=authentic_four_center_certificate(J=64,J_G=64)
        cross=authenticated_center_rankone_cross_intervals(c)
        pair=cross["P2_P4_measured_odd_center"]
        self.assertGreater(pair["lower"],0)
        self.assertEqual(pair["sign"],"STRICT_POSITIVE")
        self.assertTrue(pair["whole_Gram_cross_sign_NOT_certified"])
        other=cross["P1_P3_measured_even_center"]
        self.assertLessEqual(other["lower"],0)
        self.assertGreaterEqual(other["upper"],0)
        self.assertEqual(other["sign"],"AMBIGUOUS")

    def test_full_source_center_intervals_and_parity_block(self):
        c=authentic_four_center_certificate(J=64,J_G=64)
        self.assertEqual(c["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(c["source_prime"],(2,2))
        self.assertTrue(c["original_p1_replay_agrees"])
        previous=certified_true_P1_center_residual(J=64,J_G=64)
        self.assertGreater(F(4)*c["actual_p1_abs_center_integral_lower"]**2,F(0))
        self.assertGreater(previous["true_P1_center_energy_certified_lower"],F(0))
        low,high=c["intervals"][0]
        prior_low,prior_high=previous["true_P1_projected_residual_center_moment_interval"]
        self.assertLessEqual(max(low,prior_low),min(high,prior_high))
        M=c["center_nominal_ranktwo_Gram"]
        for i in range(4):
            self.assertLessEqual(c["nominal"][i]-c["errors"][i],c["intervals"][i][0])
            self.assertGreaterEqual(c["nominal"][i]+c["errors"][i],c["intervals"][i][1])
            for j in range(4):
                self.assertEqual(M[i][j],M[j][i])
                if (i-j)%2:self.assertEqual(M[i][j],0)
        self.assertGreater(c["center_Loewner_error_radii_by_parity"]["odd"],0)

    def test_Young_loewner_lower_is_valid_for_all_interval_corner_sources(self):
        c=authentic_four_center_certificate(J=64,J_G=64)
        m=c["nominal"];e=c["errors"]
        from observational_succ.source_four_prime_schur import _parity_lower
        low_odd=_parity_lower((0,2),m,e,F(4),F(1,8))
        low_even=_parity_lower((1,3),m,e,F(768),F(1,8))
        L=tuple(tuple(low_odd[i][j]+low_even[i][j]
                      for j in range(4)) for i in range(4))
        for signs in product((-1,1),repeat=4):
            v=tuple(m[i]+signs[i]*e[i] for i in range(4))
            true=tuple(tuple((F(4) if i%2==0 else F(768))*v[i]*v[j]
                             if (i-j)%2==0 else F(0) for j in range(4))
                       for i in range(4))
            diff=tuple(tuple(true[i][j]-L[i][j] for j in range(4))
                       for i in range(4))
            self.assertTrue(exact_psd(diff),f"Young source matrix lower fails at {signs}")

    def test_real_directional_center_bounds_never_exceed_any_corner_gram(self):
        c=authentic_four_center_certificate(J=64,J_G=64)
        m=c["nominal"];e=c["errors"]
        dirs=((1,0,0,0),(1,0,1,0),(1,0,-1,0),
              (0,1,0,1),(0,1,0,-1),(1,2,3,4))
        for x in dirs:
            bound=robust_center_energy_for_direction(c,x)
            for signs in product((-1,1),repeat=4):
                v=tuple(m[i]+signs[i]*e[i] for i in range(4))
                true=F(4)*(x[0]*v[0]+x[2]*v[2])**2+\
                      F(768)*(x[1]*v[1]+x[3]*v[3])**2
                self.assertLessEqual(bound,true)

    def test_invalid_original_source_gates(self):
        for k,J,t in ((0,64,0),(1,0,0),(5,64,0),(1,129,0),(1,4,2),(True,4,0)):
            with self.assertRaises(SourceCenterError):
                authentic_four_mode_finite_center_moment(k,J,t)
        with self.assertRaises(SourceCenterError):
            authentic_four_center_certificate(J_G=2)


class SignedS4AllFourSource(unittest.TestCase):
    def test_full_four_source_matrix_and_true_p1_improvement(self):
        c=CertifiedFourPrimeSchurTrial(J_center=64,J_G=64,J_deriv=2)
        self.assertEqual(c["source_sha"],"0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(c["source_true_prime_power"],(2,2))
        self.assertTrue(c["actual_source_P1_independent_replay"])
        self.assertGreater(c["source_direction_certificates"]["P1"]["strict_arithmetic_saving"],
                           F(13,100000))
        self.assertFalse(c["RH_proved"])
        self.assertIn(c["arithmetic_source_four_S4_verdict"],
                      ("AMBIGUOUS","POSITIVE_CERTIFIED_FIRST_WINDOW"))
        for i in range(4):
            for j in range(4):
                self.assertEqual(c["source_corrected_four_S4_Loewner_lower"][i][j],
                                 c["source_corrected_four_S4_Loewner_lower"][j][i])
                if (i-j)%2:
                    self.assertEqual(c["center_Loewner_improvement_matrix"][i][j],F(0))
        self.assertFalse(c["source_positive_S4_first_window"] and c["RH_proved"])

    def test_bad_interval_Young_parameter_fail_closed(self):
        for eta in (0,-F(1,10),True,F(2),0.5):
            with self.assertRaises(SourceCenterError):
                CertifiedFourPrimeSchurTrial(eta=eta)


if __name__=="__main__":
    unittest.main()
