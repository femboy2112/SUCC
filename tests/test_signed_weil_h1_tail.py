"""Exact-rational tests for source-only signed Weil spectral H¹ tail.

No zeta zero coordinates are inputs.  Synthetic forms are explicitly negative
controls, not competing Weil models.  Continuous results have dossier proofs.
"""
from __future__ import annotations

from fractions import Fraction as Q
from pathlib import Path
from tempfile import TemporaryDirectory
from shutil import copy2
import json
import unittest

from observational_succ.signed_weil_h1_tail import (
    SOURCE, SignedTailError, log_unit_bounds, log_bounds, exp_upper,
    source_count, absolute_zero_tail_weight, signed_tail_operator_bound,
    first_pair_receipt, certified_pair_operator, spectral_split_contract,
    finite_shadow_countermodel, concentrated_tent_H1,
    corrected_original_Gamma_error, two_chart_signed_gluing_bound, receipt,
)

class SignedTailTests(unittest.TestCase):
    def test_01_exact_log2_growth_constant(self):
        l,h=log_bounds(2)
        self.assertLess(Q(2,3),l)
        self.assertLess(h,Q(7,10))
        for x in (1,Q(3,2),2):
            self.assertLessEqual(*log_unit_bounds(Q(x)))

    def test_02_log_multiplicative_interval(self):
        for p in (2,3,4,7,17,100):
            a,b=log_bounds(p)
            x,y=log_bounds(p*p)
            self.assertLessEqual(x,2*b)
            self.assertGreaterEqual(y,2*a)

    def test_03_rational_exp_growth(self):
        e=exp_upper(Q(1))
        self.assertLess(Q(8,3),e)
        self.assertLess(e,Q(11,4))
        for x in (Q(),Q(1,5),Q(1,2),Q(2),Q(5)):
            self.assertGreaterEqual(exp_upper(x),1)

    def test_04_theta_jensen_allzero_count_conservative(self):
        for T in (2,3,14,16,20,100,10**6):
            c=source_count(T)
            self.assertGreaterEqual(c['absolute_count_upper'],0)
            self.assertFalse(c['zero_coordinates_read'])
            self.assertEqual(c['source_proof'],'theta_order_one_growth_Jensen_RH_independent')

    def test_05_reject_source_substitution(self):
        for s in ('FAKE_SIX','THETA_WEAK_SOURCE','AUTHENTIC_NOT_OURS'):
            with self.assertRaises(SignedTailError): source_count(100, s)

    def test_06_exact_h1_dyadic_formula(self):
        for t in (2,16,1000,10**9):
            tail=absolute_zero_tail_weight(t,1)
            self.assertEqual(Q(tail['weight_upper']),
                             28*log_bounds(16*t)[1]/t)

    def test_07_general_higher_sobolev_exponent(self):
        for m in (2,3,4,7):
            q=Q(1,2**(2*m-1))
            t=100
            value=14*Q(t)**(1-2*m)*(log_bounds(8*t)[1]/(1-q)
                                             +log_bounds(2)[1]*q/(1-q)**2)
            self.assertEqual(Q(absolute_zero_tail_weight(t,m)['weight_upper']),value)

    def test_08_h1_tail_shrinks_for_all_states(self):
        seq=[Q(signed_tail_operator_bound(Q(1,2),t)['signed_remainder_form_norm_upper'])
             for t in (2,16,100,1000,10**6)]
        self.assertTrue(all(x>y>0 for x,y in zip(seq,seq[1:])))
        self.assertLess(seq[-1],Q(1,1000))
        self.assertGreater(seq[0],50)

    def test_09_higher_smoothness_improves_tail(self):
        for m in (1,2,3,4):
            x=Q(signed_tail_operator_bound(Q(1,2),1000,m)['signed_remainder_form_norm_upper'])
            self.assertGreater(x,0)
        self.assertLess(Q(signed_tail_operator_bound(Q(1,2),1000,2)['signed_remainder_form_norm_upper']),
                        Q(signed_tail_operator_bound(Q(1,2),1000,1)['signed_remainder_form_norm_upper']))

    def test_10_typed_domains_all_test_h1(self):
        r=signed_tail_operator_bound(1,100)
        self.assertTrue(r['zeros_off_line_allowed'])
        self.assertFalse(r['finite_known_zero_list_required'])
        self.assertTrue(r['original_completed_Weil_identity_required'])
        self.assertFalse(r['full_Weil_positive'])
        self.assertIn('H_0^1',r['norm'])

    def test_11_invalid_inputs(self):
        calls=[lambda:source_count(Q(3,2)),lambda:source_count(10**21),
               lambda:log_bounds(Q(3,4)),lambda:exp_upper(6),
               lambda:signed_tail_operator_bound(0,16),
               lambda:signed_tail_operator_bound(6,16),
               lambda:signed_tail_operator_bound(1,1),
               lambda: absolute_zero_tail_weight(2,9),
               lambda:signed_tail_operator_bound(True,16),
               lambda:log_unit_bounds(Q(3))]
        for call in calls:
            with self.assertRaises(SignedTailError):call()

    def test_12_authentic_parent_receipt_Git_blob(self):
        c=first_pair_receipt()
        self.assertEqual(c['receipt_sha'], '8f5ae1135701a933ba4946cb0b584bba4a355a47')
        self.assertEqual(Q(c['radius']),Q(1,500))
        self.assertTrue(c['positive_pair_exists'])
        self.assertEqual(c['gamma_lower'],'141327/10000')

    def test_13_forged_parent_evidence_rejected(self):
        with TemporaryDirectory() as tmp:
            f=Path(tmp)/'bad_receipt.json'
            data=json.loads(Path('research/2026-10-14/THETA_COMPLEX_CONTOUR_RECEIPT.json').read_text())
            data['radius']='1/250'
            f.write_text(json.dumps(data))
            with self.assertRaises(SignedTailError):first_pair_receipt(f)

    def test_14_positive_pair_phase_error(self):
        p=certified_pair_operator(Q(1,2))
        self.assertEqual(p['midpoint_kernel_operator_error_upper'],str(Q(1,250)))
        self.assertEqual(p['max_pair_operator_norm'],'2')
        self.assertTrue(p['other_zeros_undetermined'])
        self.assertFalse(p['full_Weil_PSD'])

    def test_15_positive_pair_is_never_full_low_spectrum(self):
        x=spectral_split_contract(Q(1,2),16)
        self.assertTrue(x['certified_pair_positive'])
        self.assertGreater(x['uncertified_middle_count_upper'],0)
        self.assertFalse(x['all_mid_zeros_known_critical'])
        self.assertFalse(x['full_Weil_positive'])

    def test_16_reject_height_below_certified_pair(self):
        for t in (2,10,14):
            with self.assertRaises(SignedTailError):spectral_split_contract(Q(1,2),t)

    def test_17_generic_negative_middle_model(self):
        r=finite_shadow_countermodel()
        self.assertEqual(r['negative_model_middle'],'-1')
        self.assertTrue(r['high_tail_exactly_zero'])
        self.assertTrue(r['same_certified_pair'])
        self.assertFalse(r['models_arithmetic_completed_xi'])

    def test_18_source_only_h1_not_six_derivatives(self):
        for t in (16,32,64,128,256,512):
            r=signed_tail_operator_bound(Q(1,2),t)
            self.assertEqual(r['Sobolev_order'],1)
            self.assertIn('H_0^1',r['norm'])

    def test_19_finite_count_upper_does_not_assert_RH(self):
        r=source_count(1000)
        self.assertFalse(r['RH_proved'])
        self.assertGreater(r['absolute_count_upper'],2)

    def test_20_receipt_roundtrip(self):
        r=receipt()
        self.assertEqual(json.loads(json.dumps(r)),r)
        self.assertFalse(r['complete_Weil_sign_proved'])
        self.assertFalse(r['RH_proved'])

    def test_21_source_zero_count_order_one_vs_quadratic_growth(self):
        # At a high height, the Jensen order-one envelope is strictly smaller
        # than the preexisting coarse quadratic count 8(T+3/2)^2.
        t=100000
        self.assertLess(source_count(t)['absolute_count_upper'],8*(t+2)**2)

    def test_22_H1_concentration_no_sixth_derivative(self):
        for eps in (Q(1,2),Q(1,4),Q(1,10),Q(1,10000)):
            info=concentrated_tent_H1(eps)
            self.assertLess(Q(info['norm_H1_squared']),Q(8,3))
            self.assertEqual(Q(info['derivative_L2_squared']),2)
            self.assertFalse(info['six_derivatives_classically_integrable'])
        self.assertGreater(Q(concentrated_tent_H1(Q(1,10))['norm_H1_squared']),2)

    def test_23_corrected_original_Gamma_exact_CW11(self):
        for J in (1,2,8,64,512):
            A=Q(4*J+1,2)
            expected=max(Q(9,8*A*A)+Q(1,2*A*A*A),
                         Q(1,2*A*A)+Q(2,A*A*A))
            self.assertEqual(corrected_original_Gamma_error(J),expected)
        self.assertLess(corrected_original_Gamma_error(512),
                        corrected_original_Gamma_error(64))

    def test_24_two_chart_arithmetic_spectral_defect(self):
        r=two_chart_signed_gluing_bound(Q(1,2),64,10**6)
        eps=Q(r['arithmetic_signed_H1_error_upper'])
        delta=Q(r['spectral_signed_H1_error_upper'])
        self.assertEqual(Q(r['two_chart_signed_H1_error_upper']),eps+delta)
        self.assertLess(eps+delta,Q(11,10000))
        self.assertTrue(r['neither_chart_auto_positive'])
        self.assertTrue(r['low_spectral_values_not_generated_by_this_bound'])
        self.assertFalse(r['RH_proved'])

    def test_25_invalid_arithmetic_rung(self):
        for bad in (0,100001,True,Q(3,2)):
            with self.assertRaises(SignedTailError):corrected_original_Gamma_error(bad)

    def test_26_two_chart_bounds_decay_independently(self):
        x=Q(two_chart_signed_gluing_bound(Q(1,2),8,1000)['two_chart_signed_H1_error_upper'])
        y=Q(two_chart_signed_gluing_bound(Q(1,2),64,10**6)['two_chart_signed_H1_error_upper'])
        z=Q(two_chart_signed_gluing_bound(Q(1,2),512,10**9)['two_chart_signed_H1_error_upper'])
        self.assertTrue(x>y>z>0)

    def test_27_no_ell2_identification_from_phase(self):
        p=certified_pair_operator(Q(2,3))
        self.assertEqual(Q(p['midpoint_kernel_operator_error_upper']),8*Q(2,3)**2*Q(1,500))
        self.assertFalse(p['full_Weil_PSD'])

if __name__=='__main__':unittest.main()
