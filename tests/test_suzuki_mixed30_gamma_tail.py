"""Authentic completed Gamma O(J^-2) source bounds for Suzuki mixed moments."""
import unittest
from fractions import Fraction as F

from observational_succ.suzuki_mixed30_gamma_tail import (
    CompletedMixedGammaError,gamma_mixed_spectral_tail,
    true_mixed_legendre_tail_bound,authentic_infinite_gamma_mixed_rows,
    completed_mixed_gamma_two_stage_intersection,
)
from observational_succ.suzuki_legendre_source import _pinned_source


class OriginalGammaNeumannTailAnalyticTests(unittest.TestCase):
    def test_exact_real_gamma_ou_tail_upper_decreases_and_bounds_partial_sum(self):
        previous=None
        for J in (1,2,3,4,8,16,32,64):
            d=4*J+1
            bound=gamma_mixed_spectral_tail(J)
            self.assertEqual(bound,F(1,d*d)+F(8,d*d*d))
            partial=sum((F(8,(4*j+1)**3) for j in range(J,J+100)),F())
            self.assertLess(partial,bound)
            if previous is not None:self.assertLess(bound,previous)
            previous=bound
        for J in (0,65,True,F(1),1.5):
            with self.assertRaises(CompletedMixedGammaError):
                gamma_mixed_spectral_tail(J)

    def test_source_specific_30x30_legendre_derivative_coefficients(self):
        for J in (1,4,16,64):
            for k,i in ((1,1),(1,2),(2,1),(2,2),(15,17),(30,30)):
                factor=true_mixed_legendre_tail_bound(J,k,i)
                self.assertEqual(
                    factor,(2*i*(i+1)+4*k*(k+1))*gamma_mixed_spectral_tail(J))
                self.assertGreater(factor,0)
        for k,i in ((0,1),(1,0),(31,1),(1,31),(True,1),(2,1.5)):
            with self.assertRaises(CompletedMixedGammaError):
                true_mixed_legendre_tail_bound(1,k,i)


class AuthenticatedCompletedSuzukiMixedMomentSourceTests(unittest.TestCase):
    def test_finite_J_true_original_source_is_extended_without_claiming_RH(self):
        out=authentic_infinite_gamma_mixed_rows(1,6,(1,2,3))
        src=_pinned_source()
        self.assertEqual(out.source,"SHA_PINNED_AUTHENTIC_COMPLETED_ZETA_SUZUKI_MIXED30")
        self.assertEqual(out.original_source_blob,
                         "0cc8510b71d178fc79e8d410a86d8b6014cf9178")
        self.assertEqual(len(out.completed_matrix_enclosures),6)
        self.assertTrue(out.all_original_parity_zero_entries_retained)
        self.assertTrue(out.original_infinite_Gamma_integral_enclosed)
        self.assertFalse(out.pure_H1_derivative_Gram_computed)
        self.assertFalse(out.original_low_30_Schur_PSD_proved)
        self.assertFalse(out.RH_proved)
        for k,(actual,full,bounds) in enumerate(zip(
                out.source_finite_matrix,out.completed_matrix_enclosures,
                out.gamma_tail_factors),1):
            for i,orig,cert,tail in zip(out.low_modes,actual,full,bounds):
                if (k+i)%2:
                    self.assertEqual((cert.lo,cert.hi),(F(),F()))
                    self.assertEqual(tail,F())
                else:
                    self.assertEqual(tail,true_mixed_legendre_tail_bound(1,k,i))
                    self.assertEqual(cert.lo,orig.lo-tail)
                    self.assertEqual(cert.hi,orig.hi+tail)
                    self.assertEqual(type(cert),src.I)

    def test_exact_same_true_source_two_Gamma_stages_have_nonempty_intersection(self):
        for J1,J2,rank,modes in ((1,2,3,(1,)),
                                  (1,3,5,(1,2)),
                                  (2,3,3,(2,))):
            q=completed_mixed_gamma_two_stage_intersection(J1,J2,rank,modes)
            self.assertTrue(q["all_true_entries_source_consistent"])
            self.assertLess(q["J2_gamma_tail_bound"],q["J1_gamma_tail_bound"])
            self.assertFalse(q["original_low_Schur_sign_proved"])
            for row in q["source_completed_mixed_intersection"]:
                for a,b in row:self.assertLessEqual(a,b)
        with self.assertRaises(CompletedMixedGammaError):
            completed_mixed_gamma_two_stage_intersection(3,2,3,(1,))

    def test_full_30_basis_first_mode_returns_all_rows_with_exact_parity(self):
        out=authentic_infinite_gamma_mixed_rows(1,30,(1,))
        self.assertEqual(out.rank,30)
        self.assertEqual(len(out.completed_matrix_enclosures),30)
        self.assertEqual(tuple(out.low_modes),(1,))
        for k,row in enumerate(out.completed_matrix_enclosures,1):
            self.assertEqual(len(row),1)
            if k%2==0:self.assertEqual((row[0].lo,row[0].hi),(F(),F()))
        self.assertFalse(out.original_low_30_Schur_PSD_proved)

    def test_source_identity_guard_refuses_fake_primitive_and_bad_matrix_domains(self):
        src=_pinned_source()
        self.assertIsNone(src.real_prime_power(6))
        for J,rank,modes in (
            (0,3,(1,)),(65,3,(1,)),(1,0,(1,)),(1,31,(1,)),
            (1,2,(1,1)),(1,2,(0,)),(1,2,(31,)),(1,2,(True,)),
        ):
            with self.assertRaises((CompletedMixedGammaError,ValueError)):
                authentic_infinite_gamma_mixed_rows(J,rank,modes)


if __name__=="__main__":
    unittest.main()
