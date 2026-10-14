"""Source-first exact-rational Taylor jets, moment Gram, and Plato-shadow controls."""
import unittest
from fractions import Fraction as Q
from math import factorial
from observational_succ.theta_taylor_jets import (
    JetError, Interval, exact, down, up, log_interval, pi_interval,
    exp_minus_point, exp_minus_interval, exp_interval_nonneg,
    source_weight, time_tail_upper, mode_tail_upper, jets,
    rouche_center_certificate, general_taylor_disk,
    certified_midpoint_polynomial, source_hankel_two_by_two,
    stieltjes_moments, unseen_moment_lower, B_real_interval, theta_source_kernel_real,
    positive_shadow_countermodel, fake_offline_zero_with_same_early_jets, one_point_shadow_blindspot,
    receipt,
)


class CertifiedThetaJets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.full = jets(20, 3, 8, 1536)

    def test_gaussian_original_jets_no_zero_source(self):
        self.assertEqual(self.full['source'], 'authentic_unweighted_integer_Gaussian_theta')
        self.assertEqual(len(self.full['a']), 21)
        self.assertFalse(self.full['RH_proved'])
        self.assertFalse(self.full['nontrivial_zero_inputs'])

    def test_immutable_outward_pi_and_log(self):
        p0,p1 = pi_interval()
        self.assertTrue(Q(3)<p0<p1<Q(22,7))
        for x in (Q(1),Q(3,2),Q(2),Q(3),Q(17,4),Q(8)):
            a,b = log_interval(x)
            self.assertLessEqual(a,b)
            self.assertGreaterEqual(a,0)
        self.assertEqual(log_interval(Q(1)),(Q(),Q()))

    def test_original_source_replay_refuses_forged_jets(self):
        mutated=dict(self.full)
        altered=list(mutated['a'])
        altered[0]=Interval(Q(9,10),Q(1))
        mutated['a']=tuple(altered)
        with self.assertRaises(JetError):
            rouche_center_certificate(mutated,Q(11,2),13)
        mutated['a']=self.full['a']
        mutated['source']='fake_composite6_as_Euler_place'
        with self.assertRaises(JetError):
            rouche_center_certificate(mutated,Q(11,2),13)

    def test_rational_exp_minus_certificate(self):
        for x in (Q(),Q(1,10),Q(1),Q(3),Q(20),Q(50),Q(180)):
            a,b=exp_minus_point(x)
            self.assertTrue(Q()<=a<=b<=1)
        self.assertEqual(exp_minus_point(Q()),(Q(1),Q(1)))
        for x in (Q(1,5),Q(2),Q(13,2)):
            lo,hi=exp_minus_interval(x,x+Q(1,10))
            self.assertTrue(0<=lo<=hi<=1)

    def test_interval_probes_reject_ghost_inputs(self):
        for f in (lambda: exact(.5),lambda: jets(20,3,8,7),
                  lambda: jets(100,3,8,300),lambda: log_interval(Q(20)),
                  lambda: exp_minus_point(Q(-1)),lambda: pi_interval(2),
                  lambda: exp_interval_nonneg(Q(70))):
            with self.assertRaises(JetError):f()

    def test_positive_moment_source_beyond_borehole(self):
        b=self.full['b']
        self.assertTrue(all(0<=x.lo<=x.hi for x in b)
                        and all(x.lo>0 for x in b[:13]))
        self.assertTrue(b[0].hi<Q(1,50))
        self.assertTrue(b[1].hi<Q(1,5000))
        self.assertTrue(b[10].hi<Q(1,10**20))

    def test_even_coefficients_from_source_identity(self):
        a,b=self.full['a'],self.full['b']
        self.assertEqual(a[0],Interval(Q(1,2),Q(1,2))-b[0]*Q(1,4))
        for j in range(1,21):
            self.assertEqual(a[j],b[j-1]-b[j]*Q(1,4))
        self.assertTrue(all(x.lo>0 for x in a[:13]))

    def test_uniform_certified_global_Fock_continuation(self):
        R=Q(11,2)
        c=general_taylor_disk(self.full,R,13)
        self.assertLess(c['remainder_absolute_upper'],Q(1,100000))
        self.assertEqual(c['degree'],20)
        self.assertFalse(c['nontrivial_zero_inputs'])

    def test_no_zeros_in_radius_5_5(self):
        x=rouche_center_certificate(self.full,Q(11,2),13)
        self.assertTrue(x['certified_zero_free'])
        self.assertEqual(x['zero_count'],0)
        self.assertGreater(x['margin_lower'],Q(1,250))
        self.assertFalse(x['RH_proved'])

    def test_no_claim_farther_than_certified(self):
        x=rouche_center_certificate(self.full,Q(28,5),13)
        self.assertFalse(x['certified_zero_free'])
        self.assertIsNone(x['zero_count'])

    def test_sharper_finite_theta_measurement(self):
        coarse=jets(8,2,6,96)
        medium=jets(8,3,8,256)
        refined=jets(8,3,8,512)
        self.assertLess(refined['b'][0].hi-refined['b'][0].lo,
                        medium['b'][0].hi-medium['b'][0].lo)
        # All enclosures arise from the same immutable integer-theta source.
        for j in range(6):
            self.assertLessEqual(medium['b'][j].lo,refined['b'][j].hi)
            self.assertLessEqual(refined['b'][j].lo,medium['b'][j].hi)
            self.assertLessEqual(coarse['b'][j].lo,refined['b'][j].hi)
            self.assertLessEqual(refined['b'][j].lo,coarse['b'][j].hi)

    def test_each_source_tail_is_rigorous_positive(self):
        for j in range(11):
            self.assertTrue(time_tail_upper(j,Q(8))>=0)
            self.assertTrue(mode_tail_upper(j,3)>=0)
            self.assertLessEqual(mode_tail_upper(j,3), mode_tail_upper(j,2))

    def test_conditional_source_polynomial_separates_two_errors(self):
        a=certified_midpoint_polynomial(self.full,Q(11,2),13)
        self.assertEqual(len(a['coefficient_midpoints']),21)
        self.assertEqual(a['uniform_complex_error'],
                         a['finite_observer_error']+a['analytic_tail'])
        self.assertLess(a['uniform_complex_error'],Q(1,100))
        self.assertFalse(a['finite_observer_identifies_full_curve'])

    def test_stieltjes_positive_hankel_minors(self):
        c=source_hankel_two_by_two(self.full)
        self.assertTrue(c['both_strictly_positive_certified'])
        self.assertGreater(c['hankel_det'].lo,0)
        self.assertGreater(c['shifted_hankel_det'].lo,0)
        self.assertFalse(c['completed_Weil_PSD_proved'])

    def test_moment_linear_map_is_mathematically_exact(self):
        m=stieltjes_moments(self.full,4)
        for j in range(5):
            a,b=m[j],self.full['b'][j]
            fac=4**j*factorial(2*j)
            self.assertEqual(a.lo,b.lo*fac)
            self.assertEqual(a.hi,b.hi*fac)

    def test_stieltjes_moments_predict_unseen_future_bound(self):
        future=unseen_moment_lower(self.full,0)
        m2=stieltjes_moments(self.full,2)[2]
        self.assertEqual(future['observed_moments'],(0,1))
        self.assertEqual(future['predicted_next_index'],2)
        self.assertTrue(0 < future['certified_lower'] < m2.lo)
        self.assertFalse(future['completed_Weil_PSD_proved'])

    def test_positive_hankel_does_not_mean_arbitrary_positive_moments(self):
        # A source can have positive moment entries but impossible covariance.
        m0,m1,m2=Q(1),Q(2),Q(1)
        self.assertLess(m0*m2-m1*m1,0)

    def test_theta_source_kernel_symmetry(self):
        d=self.full
        a=theta_source_kernel_real(d,Q(1),Q(2))
        b=theta_source_kernel_real(d,Q(2),Q(1))
        c=theta_source_kernel_real(d,Q(1),Q(-2))
        self.assertEqual(a,b)
        self.assertEqual(c,theta_source_kernel_real(d,Q(1),Q(2)))  # cosh-even
        self.assertGreater(a.lo,0)

    def test_real_B_kernel_at_origin(self):
        d=self.full
        self.assertEqual(theta_source_kernel_real(d,0,0),d['b'][0])
        self.assertEqual(B_real_interval(d,0),d['b'][0])

    def test_explicit_two_positive_sources_share_first_jets(self):
        x=positive_shadow_countermodel()
        self.assertEqual(x['shared_m0_m1'],[1,5])
        self.assertEqual(x['distinct_m2'],[41,29])
        self.assertEqual(x['first_different_B_coefficient'],Q(1,32))
        self.assertTrue(x['both_sources_positive'])
        self.assertFalse(x['finite_moments_prove_unique_source'])

    def test_source_gaussian_fock_even_jet_impostor_has_offline_zero(self):
        fake=fake_offline_zero_with_same_early_jets(self.full,20)
        self.assertEqual(fake['chosen_off_critical_location'],(20,20))
        self.assertTrue(fake['first_two_even_jets_match_exactly'])
        self.assertTrue(fake['inside_prior_Fock_budget'])
        self.assertLess(fake['source_uniform_Fock_norm2_upper'],1)
        self.assertFalse(fake['full_original_Euler_germ_preserved'])
        # Exact 4th-power witness for the selected off-line point.
        mul=lambda x,y: (x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0])
        w2=mul((20,20),(20,20))
        self.assertEqual(mul(w2,w2),(-640000,0))

    def test_all_early_jets_do_not_identify_full_source(self):
        h=one_point_shadow_blindspot(self.full,8)
        self.assertEqual(h['perturbation_power'],18)
        self.assertTrue(h['all_past_jets_preserved'])
        self.assertFalse(h['same_original_Euler_germ'])

    def test_plato_cave_does_not_imply_weil_sign(self):
        r=receipt()
        self.assertTrue(r['rouche_radius_11_over_2']['certified_zero_free'])
        self.assertTrue(r['theta_stieltjes_Hankel']['both_strictly_positive_certified'])
        self.assertFalse(r['theta_stieltjes_Hankel']['completed_Weil_PSD_proved'])
        self.assertFalse(r['RH_proved'])


if __name__=='__main__':
    unittest.main()
