"""Exact-rational original Gaussian theta contour and Weil-local tests."""
import unittest
import json
from fractions import Fraction as Q
from math import pi,log,exp,cos,sin

from observational_succ.theta_complex_contour import (
    S,I,SourceContourError,pi_iv,log_iv,exp_neg_iv,cos_sin_iv,
    source_only_candidate,first_critical_contour,center_integrals,
    analytic_second_upper,receipt,
)
from observational_succ.theta_suzuki_shadow import (
    authentic_local_weil_rank_one,localized_mass_lower,fake_even_germ,shadow_impostor_inside_critical_strip,paired_original_Weil_window,paired_phase_kernel_interval,
)

class TestSourceContour(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.proof=first_critical_contour()

    def test_integer_directed_interval_edges(self):
        a=I.of(Q(1,3));b=I.of(Q(2,7))
        for op,expect in ((a+b,Q(13,21)),(a-b,Q(1,21)),(a*b,Q(2,21)),(a/b,Q(7,6))):
            self.assertLessEqual(op.lower(),expect)
            self.assertGreaterEqual(op.upper(),expect)
        self.assertEqual((I.of(Q(1,4))**2).middle(),Q(1,16))

    def test_original_Machin_pi_log(self):
        p=pi_iv();l=log_iv(8)
        self.assertTrue(p.lower()<Q(22,7) and p.lower()>3)
        self.assertTrue(abs(float(p.middle())-pi)<1e-14)
        self.assertTrue(abs(float(l.middle())-log(8))<1e-14)

    def test_original_exponential_is_outward(self):
        for k in (Q(0),Q(1,3),Q(3),Q(12),Q(27)):
            x=exp_neg_iv(I.of(k))
            self.assertTrue(x.lo>=0)
            self.assertTrue(float(x.lower())-1e-15<=exp(-float(k))<=float(x.upper())+1e-15)

    def test_trig_is_outward(self):
        for x in (Q(),Q(1,10),Q(1),Q(3),Q(8),Q(15)):
            c,s=cos_sin_iv(I.of(x))
            self.assertAlmostEqual(float(c.middle()),cos(float(x)),places=13)
            self.assertAlmostEqual(float(s.middle()),sin(float(x)),places=13)
            self.assertTrue(c.width()<Q(1,10**20))
            self.assertTrue(s.width()<Q(1,10**20))

    def test_source_only_candidate_not_external_zero_oracle(self):
        self.assertEqual(source_only_candidate(),Q(141347,10000))
        self.assertEqual(self.proof['site'],source_only_candidate())

    def test_first_contour_strict_rouche(self):
        d=self.proof
        self.assertTrue(d['certified_exactly_one'])
        self.assertTrue(d['critical_line_by_reflection'])
        self.assertTrue(d['zero_is_simple'])
        self.assertGreater(d['strict_rouche_margin'],Q(1,1_000_000))
        self.assertLess(d['center_abs_upper'],Q(1,8_000_000))
        self.assertGreater(d['derivative_abs_lower'],Q(1,750))
        self.assertLess(d['F_second_upper'],Q(3,4))

    def test_contains_only_one_original_source_zero(self):
        self.assertEqual(self.proof['radius'],Q(1,500))
        self.assertEqual(self.proof['site'],Q(141347,10000))
        self.assertTrue(self.proof['no_external_zero_lookup'])
        self.assertFalse(self.proof['RH_proved'])

    def test_simpson_has_independent_missing_source_budgets(self):
        d=self.proof['source_stats']
        self.assertTrue(all(d[x]>0 for x in ('simpson_B_upper','simpson_S_upper',
                                              'missing_integer_B_upper','missing_integer_S_upper',
                                              'time_B_upper','time_S_upper')))
        self.assertLess(d['simpson_B_upper'],Q(1,10**9))
        self.assertLess(d['simpson_S_upper'],Q(1,10**9))
        self.assertLess(d['time_B_upper'],Q(1,10**10))
        self.assertLess(d['time_S_upper'],Q(1,10**9))

    def test_derivative_second_uniform_honest(self):
        self.assertGreater(analytic_second_upper(Q(141347,10000),Q(1,500)),0)
        self.assertRaises(SourceContourError,analytic_second_upper,1,0)
        self.assertRaises(SourceContourError,analytic_second_upper,1,2)

    def test_wrong_primitive_or_domain_rejected(self):
        with self.assertRaises(SourceContourError):cos_sin_iv(I.of(17))
        with self.assertRaises(SourceContourError):exp_neg_iv(I.of(-1))
        with self.assertRaises(SourceContourError):first_critical_contour(Q(14),Q(1,500))
        with self.assertRaises(SourceContourError):center_integrals(modes=6,cells=512)
        with self.assertRaises(SourceContourError):center_integrals(cells=513)

    def test_noncertified_contour_cannot_manufacture_spectral_sign(self):
        with self.assertRaises(SourceContourError):authentic_local_weil_rank_one({'certified_exactly_one':False})
        with self.assertRaises(SourceContourError):authentic_local_weil_rank_one({'certified_exactly_one':True,'critical_line_by_reflection':False})

    def test_positive_local_weil_summand_is_not_global_Weil(self):
        d=authentic_local_weil_rank_one(self.proof)
        self.assertTrue(d['local_spectral_PSD'])
        self.assertTrue(d['local_zero_simple'])
        self.assertFalse(d['completed_Weil_global_PSD'])
        self.assertFalse(d['all_other_zero_contributions_controlled'])

    def test_explicit_normalized_bump_lower_bound(self):
        x=localized_mass_lower(Q(1,100))
        self.assertEqual(Q(x['localized_rank_one_Weil_lower']),Q(791*791,800*800))
        self.assertTrue(Q(x['localized_rank_one_Weil_lower'])>Q(97,100))
        self.assertFalse(x['global_signed_Weil_PSD'])
        with self.assertRaises(SourceContourError):localized_mass_lower(1)

    def test_fake_entire_germ_same_jets_different_off_line_divisor(self):
        f=fake_even_germ(1,16)
        self.assertEqual(f['first_changed_coefficient_degree'],4)
        self.assertEqual(f['multiplier_high_coefficient'],str(Q(1,16**4)))
        self.assertTrue(f['creates_noncritical_zeros'])
        self.assertFalse(f['preserves_full_euler_theta_germ'])

    def test_fake_inside_actual_critical_strip_preserves_small_shadows(self):
        d=shadow_impostor_inside_critical_strip()
        self.assertTrue(d['same_original_a0_a1'])
        self.assertLess(Q(d['strict_fock_norm_squared_upper']),Q(1,3))
        self.assertEqual(d['off_critical_inside_strip_root'],'z=1/4+20i; s=3/4+20i')
        self.assertFalse(d['original_Weil_arithmetic_source'])
        self.assertFalse(d['RH_proved'])

    def test_true_pair_weil_window_has_source_phase_error(self):
        x=paired_original_Weil_window(Q(1,2))
        self.assertEqual(x['positive_rank_upper'],2)
        self.assertEqual(Q(x['operator_norm_upper']),2)
        self.assertEqual(Q(x['midpoint_phase_operator_error_upper']),Q(1,250))
        self.assertTrue(x['source_generated_phase'])
        self.assertFalse(x['full_signed_Weil_PSD'])

    def test_genuine_pair_kernel_rational_phase_enclosure(self):
        from math import cos
        for t in (Q(0),Q(1,5),Q(1,2),Q(4,5),Q(1)):
            v=paired_phase_kernel_interval(t)
            lo,hi=Q(v['true_original_kernel_lower']),Q(v['true_original_kernel_upper'])
            self.assertLess(lo,hi)
            self.assertTrue(float(lo)-1e-14<=2*cos(float(source_only_candidate())*float(t))<=float(hi)+1e-14)
        with self.assertRaises(SourceContourError):paired_phase_kernel_interval(Q(3,2))

    def test_reproducible_JSON_pure_Fraction_receipt(self):
        d=receipt()
        self.assertEqual(d,json.loads(json.dumps(d)))
        self.assertEqual(d['source'],'AUTHENTIC_ONE_GAUSSIAN_INTEGER_THETA')
        self.assertTrue(d['local_residue_positive'])
        self.assertFalse(d['entire_Weil_sign_claimed'])

if __name__=='__main__':unittest.main()
