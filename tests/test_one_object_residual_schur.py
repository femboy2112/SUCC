"""Adversarial exact algebra + authentic-source gate for zero-shift shorting."""
from __future__ import annotations

import importlib.util
import unittest
from fractions import Fraction as F

from observational_succ.one_object_residual_schur import (
    ResidualShortingError, ORIGINAL_SUZUKI_BLOB, KAPPA,
    add, det, eye, exact, finite_residual_certificate, hilbert_scan,
    hilbert_signed_operator_norm_budget, inverse, is_symmetric, matrix,
    mul, original_first_window_source_budget, original_source_cancellation_certificate, parent_original_source_contract,
    psd, rayleigh, scale, schema_receipt, signed_hilbert_matrix_sum, trans,
)


def sample(low_shift=F(1,120), factor=F(0)):
    K=((F(1,4),0),(0,F(1,9)))
    D=((F(1,2),0),(0,F(1,3)))
    B=((F(1,4),F(1,6)),)
    A=((F(5,24)+low_shift,),)
    H=((factor*F(1,2),),(factor*F(1,2),))
    return finite_residual_certificate(A,B,D,K,H,F(1,2))


class ExactAlgebra(unittest.TestCase):
    def test_determinant_exact(self):
        self.assertEqual(det(matrix(((2,3),(5,7)))),-1)
        self.assertEqual(det(matrix(((0,1),(1,0)))),-1)

    def test_inverse_exact(self):
        A=matrix(((3,1),(1,2)))
        self.assertEqual(mul(A,inverse(A)),eye(2))

    def test_psd_includes_singular(self):
        self.assertTrue(psd(((1,1),(1,1))))
        self.assertFalse(psd(((1,2),(2,1))))
        self.assertFalse(psd(((0,1),(1,0))))

    def test_psd_nonleading_negative_witness(self):
        self.assertFalse(psd(((1,0,0),(0,1,2),(0,2,1))))

    def test_symmetric_transpose(self):
        self.assertTrue(is_symmetric(matrix(((0,1),(1,0)))))
        self.assertFalse(is_symmetric(matrix(((0,1),(2,0)))))

    def test_wrong_bool_float_laundering(self):
        for bad in (False,True,0.5,1.0):
            with self.assertRaises(ResidualShortingError):exact(bad)

    def test_dimension_mismatch(self):
        with self.assertRaises(ResidualShortingError):mul(matrix(((1,2),)),matrix(((1,2),)))

    def test_singular_source_high_metric_rejected(self):
        with self.assertRaises(ResidualShortingError):finite_residual_certificate(((1,),),((1,1),),((1,0),(0,1)),((1,0),(0,0)),((0,),(0,)),F(1,2))

    def test_high_positivity_not_assumed(self):
        with self.assertRaises(ResidualShortingError):finite_residual_certificate(((1,),),((1,1),),((F(1,8),0),(0,F(1,8))),((1,0),(0,1)),((0,),(0,)),F(1,2))

    def test_nonselfadjoint_source_rejected(self):
        with self.assertRaises(ResidualShortingError):finite_residual_certificate(((1,),),((1,1),),((1,2),(0,1)),((1,0),(0,1)),((0,),(0,)),F(1,2))

    def test_negative_kappa_rejected(self):
        with self.assertRaises(ResidualShortingError):finite_residual_certificate(((1,),),((1,1),),((1,0),(0,1)),((1,0),(0,1)),((0,),(0,)),F(-1))

    def test_exact_true_short(self):
        a=sample(factor=F(1))
        self.assertEqual(a.exact_short,((F(1,120),),))
        self.assertEqual(a.lower_schur,a.upper_schur)
        self.assertEqual(a.residual,((F(),),(F(),)))
        self.assertFalse(a.RH_proved)

    def test_zero_trial_fails_to_certify_positive(self):
        a=sample(factor=F(0))
        self.assertLess(a.lower_schur[0][0],0)
        self.assertGreater(a.upper_schur[0][0],0)
        self.assertEqual(a.exact_short[0][0],F(1,120))

    def test_intermediate_trial_sound_two_sided(self):
        for k in range(1,11):
            a=sample(factor=1-F(1,2**k))
            self.assertLessEqual(a.lower_schur[0][0],a.exact_short[0][0])
            self.assertLessEqual(a.exact_short[0][0],a.upper_schur[0][0])
            self.assertEqual(a.upper_resolvent[0][0]-a.lower_resolvent[0][0],F(1,4**k))

    def test_negative_short_witness_is_preserved(self):
        a=sample(low_shift=F(-1,120),factor=F(1))
        self.assertEqual(a.upper_schur[0][0],-F(1,120))
        self.assertEqual(rayleigh(a.exact_short,(1,)),-F(1,120))
        self.assertTrue(a.mathematically_synthetic)

    def test_multi_low_block_exact(self):
        K=matrix(((F(1,4),0),(0,F(1,9))))
        D=matrix(((F(1,2),0),(0,F(1,3))))
        B=matrix(((F(1,4),F(1,6)),(F(1,8),F(-1,12))))
        trial=mul(inverse(D),trans(B))
        R=mul(B,trial)
        A=add(R,scale(eye(2),F(1,128)))
        cert=finite_residual_certificate(A,B,D,K,trial,F(1,2))
        self.assertEqual(cert.lower_schur,scale(eye(2),F(1,128)))
        self.assertTrue(psd(cert.exact_short))

    def test_wrong_signed_block_not_positive(self):
        a=sample(low_shift=F(-1,120),factor=F(1))
        self.assertFalse(psd(a.exact_short))

    def test_every_valid_finite_trial_lower_stays_lower(self):
        for k in range(0,13):
            a=sample(factor=F(k,12))
            self.assertTrue(psd(add(a.exact_short,a.lower_schur,-1)))
            self.assertTrue(psd(add(a.upper_schur,a.exact_short,-1)))


class ActualAnalyticSourceBounds(unittest.TestCase):
    def test_source_derivative_upper(self):
        d=original_first_window_source_budget()
        self.assertLess(d['coarse_gprime_L1_upper'],22)
        self.assertEqual(d['coarse_gprime_L1_upper'],F(65,3))
        self.assertEqual(d['sharpened_gprime_L1_strict_upper'],F(11,40))
        self.assertEqual(d['sharpened_gprime_L2_strict_upper'],F(2,5))
        self.assertEqual(d['kappa'],F(369,10000))
        self.assertTrue(d['no_spectral_gap_claimed'])

    def test_zero_shift_uniform_resolvent_bound_is_finite(self):
        d=original_first_window_source_budget()
        self.assertEqual(d['coarse_resolvent_operator_norm_upper'],F(4840000,369))
        self.assertEqual(d['resolvent_operator_norm_strict_upper'],F(3025,1476))
        self.assertFalse(d['RH_proved'])

    def test_j_vs_n_genuine_analytic_Zeno(self):
        prev=F(1_000_000)
        for depth in range(1,16):
            r=hilbert_signed_operator_norm_budget(depth,2**depth)
            self.assertLess(r['total_signed_operator_error_strict_upper'],prev)
            prev=r['total_signed_operator_error_strict_upper']
        self.assertLess(prev,F(1,1000))

    def test_signed_source_cancellation_happens_at_all_scales(self):
        r=original_source_cancellation_certificate()
        self.assertEqual(r['cells'],4096)
        self.assertGreater(r['gprime_L1_lower'],F(1,4))
        self.assertLess(r['gprime_L1_STRICT_upper'],F(11,40))
        self.assertLess(r['gprime_L2_squared_STRICT_upper'],F(4,25))

    def test_large_improvement_is_not_rh(self):
        d=original_first_window_source_budget()
        self.assertGreater(d['coarse_resolvent_operator_norm_upper'] /
                           d['resolvent_operator_norm_strict_upper'],F(5000))
        self.assertFalse(d['RH_proved'])

    def test_gamma_tail_one_sided_label(self):
        r=hilbert_signed_operator_norm_budget(6,16)
        self.assertEqual(r['kernel_H1_projection_error_strict_upper'],F(1,80))
        self.assertEqual(r['authentic_gamma_tail_upper'],F(1,65)+F(4,65**2))
        self.assertTrue(r['requires_original_signed_source_cell_integrals'])

    def test_nonoriginal_source_rejected(self):
        for bad in (False,'genuine',None,1):
            with self.assertRaises(ResidualShortingError):hilbert_signed_operator_norm_budget(3,5,bad)

    def test_invalid_hilbert_parameters(self):
        for p in [(-1,1),(31,1),(2,0),(True,3),(3,3.0)]:
            with self.assertRaises(ResidualShortingError):hilbert_signed_operator_norm_budget(*p)

    def test_hilbert_visits_exactly_once(self):
        for depth in range(0,6):
            rows=hilbert_scan(depth)
            self.assertEqual(len(rows),4**depth)
            self.assertEqual(len(set(rows)),4**depth)
            self.assertTrue(all(abs(a[0]-b[0])+abs(a[1]-b[1])==1 for a,b in zip(rows,rows[1:])))

    def test_signed_hilbert_scan_no_free_positivity(self):
        M=((F(2),F(-5)),(F(-5),F(3)))
        self.assertEqual(signed_hilbert_matrix_sum(M,1),(-F(5),-F(5)))
        self.assertFalse(psd(M))

    def test_source_receipt_unresolved(self):
        r=schema_receipt()
        self.assertEqual(r['trial_correct_lower_schur'],F(1,120))
        self.assertFalse(r['RH_proved'])
        self.assertTrue(r['one_object_source_contract_requires_checkout'])


source_installed=importlib.util.find_spec('observational_succ.suzuki_legendre_source') is not None


@unittest.skipUnless(source_installed,'Original PR85/PR106 modules not present in isolated overlay; CI must execute')
class GenuineTateWeilSuzukiImport(unittest.TestCase):
    def test_original_hash_and_completed_profile(self):
        report=parent_original_source_contract()
        self.assertEqual(report['source_git_blob_sha'],ORIGINAL_SUZUKI_BLOB)
        self.assertFalse(report['Weil_positivity_proved'])
        self.assertFalse(report['Connes_global_trace_identified'])
        self.assertEqual(report['contact_one_mode_increment'],F(2))
        self.assertTrue(report['original_screw_value_checked_against_derivative'])
        self.assertTrue(report['wrong_contact_mutation_rejected'])

    def test_actual_tate_odd_character_must_not_be_zeta(self):
        from observational_succ.tate_weil_source_bridge import TateWeilProfile
        self.assertNotEqual(TateWeilProfile.canonical('zeta'),TateWeilProfile.canonical('chi_minus_3'))
        self.assertTrue(TateWeilProfile.canonical('chi_minus_3').parity==1)

    def test_original_mode_and_second_suzuki_contract(self):
        from observational_succ.one_object_transport import contact_rational_increment
        self.assertEqual(contact_rational_increment(0),F(0))
        self.assertEqual(contact_rational_increment(1),F(2))
        self.assertEqual(contact_rational_increment(2),F(2)+F(4,5)-F(2,3))


if __name__=='__main__':
    unittest.main()
