"""Hostile controls for band-uniform rational Gamma_R de-aliasing.

Every exact certificate is arithmetic in Fraction; optional mpmath observations
are independent numerical tests, NOT the origin of any theorem or sign claim.
"""
from fractions import Fraction as F
import unittest

from observational_succ.gamma_band_dealias import (
    GammaBandError, uniform_phase_filter, gamma_r_band_certificate,
    compact_mellin_band_bound, sampled_gamma_r, gamma_r_jet_certificate,
)


class ExactRationalCertification(unittest.TestCase):
    def test_phase_filter_proves_all_nonmultiples_cancel(self):
        for q in (1, 2, 3, 4, 5, 7, 16):
            for k in range(-3*q, 3*q+1):
                self.assertEqual(uniform_phase_filter(q,k), int(k%q==0))
        # A normalized q-offset system can NEVER cancel its q-th harmonic.
        self.assertEqual(uniform_phase_filter(4,4), 1)
        self.assertEqual(uniform_phase_filter(4,1), 0)
        self.assertEqual(uniform_phase_filter(4,-3), 0)

    def test_source_band_result_is_entirely_exact_arithmetic(self):
        x=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
              left_steps=350,right_steps=16,interleaves=2,taylor_order=80)
        self.assertEqual(x['effective_spacing'],F(1,4))
        self.assertEqual(x['first_surviving_alias_imaginary_pi_multiplier'],16)
        self.assertEqual(x['conservative_rational_band_margin'],40)
        self.assertEqual(x['gamma_integral_majorant'],5)
        self.assertEqual(x['source_event_count'],367)
        for field in ('alias_error_upper','left_tail_upper','right_tail_upper','total_upper'):
            self.assertIsInstance(x[field], F)
            self.assertGreater(x[field],0)
        self.assertEqual(x['total_upper'],x['alias_error_upper']+
                         x['left_tail_upper']+x['right_tail_upper'])
        self.assertLess(x['total_upper'],F(1,10**7))
        self.assertFalse(x['actual_prime_source_authenticated'])
        self.assertFalse(x['RH_proved'])

    def test_additional_source_events_improve_same_physical_band(self):
        coarse=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
            left_steps=175,right_steps=8,taylor_order=80)
        fine=gamma_r_band_certificate(F(1,2),F(1,2),F(3,2),8,
            interleaves=2,left_steps=350,right_steps=16,taylor_order=80)
        self.assertLess(fine['alias_error_upper'],coarse['alias_error_upper'])
        self.assertLess(fine['total_upper'],coarse['total_upper'])
        self.assertGreater(fine['source_event_count'],coarse['source_event_count'])

    def test_mutations_and_invalid_bands_are_rejected(self):
        good=dict(spacing=F(1,2),sigma_min=F(1,2),sigma_max=F(3,2),
                  imag_radius=8,left_steps=350,right_steps=16)
        bad=[
            dict(spacing=F(0)),dict(spacing=0.5),dict(spacing=True),
            dict(sigma_min=F(0)),dict(sigma_min=F(2)),
            dict(sigma_max=F(0)),dict(imag_radius=-1),
            dict(imag_radius=48,interleaves=2),
            dict(imag_radius=24,interleaves=1),
            dict(interleaves=0),dict(interleaves=2.0),
            dict(interleaves=True),dict(left_steps=True),
            dict(right_steps=-1),dict(left_steps=50000,right_steps=1),
            dict(taylor_order=0),dict(taylor_order=257),
        ]
        for mutation in bad:
            d=good.copy()
            d.update(mutation)
            with self.subTest(mutation=mutation), self.assertRaises(GammaBandError):
                gamma_r_band_certificate(**d)
        for q,k in ((0,1),(2,True),(65,1),(2,1000001)):
            with self.assertRaises(GammaBandError):
                uniform_phase_filter(q,k)

    def test_cauchy_jet_bound_is_exact_and_rejects_missing_collar(self):
        x=gamma_r_jet_certificate(F(1,4),F(1,2),F(3,2),8,
            collar=F(1,4),jet_order=2,left_steps=500,right_steps=18,
            taylor_order=100)
        self.assertIsInstance(x['jet_error_upper'],F)
        self.assertEqual(x['jet_error_upper'],32*x['expanded_band_total_upper'])
        self.assertFalse(x['RH_proved'])
        for collar in (0,F(1,2),0.2):
            with self.assertRaises(GammaBandError):
                gamma_r_jet_certificate(F(1,4),F(1,2),1,8,
                    collar=collar,jet_order=1)

    def test_short_right_window_rejected_for_large_sigma(self):
        with self.assertRaises(GammaBandError):
            gamma_r_band_certificate(F(1,4),1,100,0,left_steps=40,right_steps=0)

    def test_tate_log_compact_interface_conditional_norm(self):
        # b(u)=(1-u^2)^2 on |u|<=1, zero elsewhere is W^{2,1};
        # ||b''||_1=32/(3*sqrt(3)) < 7, independently elementary.
        # Set phi(x)=x^(-1/2)b(log(x)) and sigma=1, so g_sigma=b.
        x=compact_mellin_band_bound(F(1,4),8,7,derivative_order=2)
        self.assertIsInstance(x['bound'],F)
        self.assertGreater(x['bound'],0)
        self.assertLess(x['bound'],F(1,10))
        self.assertTrue(x['conditional_on_verified_L1_bound'])
        self.assertFalse(x['source_identity_checked'])
        with self.assertRaises(GammaBandError):
            compact_mellin_band_bound(F(1,4),0,3,derivative_order=1)
        with self.assertRaises(GammaBandError):
            compact_mellin_band_bound(F(1,4),0,0.1,derivative_order=2)
        with self.assertRaises(GammaBandError):
            compact_mellin_band_bound(F(1,4),48,7,derivative_order=2)


class IndependentAnalyticControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            import mpmath as mp
        except ImportError as exc:
            raise unittest.SkipTest('Optional mpmath research readout absent') from exc
        cls.mp=mp

    def test_multi_point_band_certificate_survives_hostile_points(self):
        mp=self.mp
        a,b=F(1,2),F(3,2)
        with mp.workdps(65):
            for h,q,left,right in ((F(1,2),1,180,9),
                                     (F(1,2),2,360,18),
                                     (F(1,4),1,360,18)):
                cert=gamma_r_band_certificate(h,a,b,8,interleaves=q,
                      left_steps=left,right_steps=right,taylor_order=100)
                bound=mp.mpf(cert['total_upper'].numerator)/cert['total_upper'].denominator
                for real in (mp.mpf('0.5'),mp.mpf('1'),mp.mpf('1.5')):
                    for imag in (-8,-3,0,3,8):
                        obs=sampled_gamma_r(mp.mpc(real,imag),h,interleaves=q,
                            left_steps=left,right_steps=right,dps=70)
                        with self.subTest(h=h,q=q,real=real,imag=imag):
                            self.assertLess(obs['observed_absolute_error'],bound)
                            self.assertLess(obs['coherent_chart_disagreement'],mp.mpf('1e-58'))

    def test_exact_multi_observer_interleave_matches_refined_lattice(self):
        mp=self.mp
        with mp.workdps(70):
            for q in (2,3,4,7):
                read=sampled_gamma_r(mp.mpc('.75','8'),F(1,3),
                    interleaves=q,left_steps=275,right_steps=22,dps=70)
                self.assertLess(read['coherent_chart_disagreement'],mp.mpf('1e-60'))
                self.assertEqual(read['number_of_events'],298)

    def test_old_alias_is_removed_but_new_alias_remains(self):
        mp=self.mp
        with mp.workdps(55):
            h=F(1,2)
            p=8*mp.pi
            old=sampled_gamma_r(mp.mpc(1,p),h,left_steps=400,right_steps=20,dps=70)
            new=sampled_gamma_r(mp.mpc(1,p),h,interleaves=2,
                                left_steps=800,right_steps=40,dps=70)
            self.assertGreater(abs(old['refined']),mp.mpf('0.99'))
            self.assertLess(abs(new['refined']),mp.mpf('1e-6'))
            self.assertGreater(abs(old['refined'])/abs(new['refined']),mp.mpf('1e6'))
            shifted=sampled_gamma_r(mp.mpc(1,2*p),h,interleaves=2,
                                    left_steps=800,right_steps=40,dps=70)
            zero=sampled_gamma_r(1,h,interleaves=2,
                                 left_steps=800,right_steps=40,dps=70)
            self.assertLess(abs(shifted['refined']-zero['refined']),mp.mpf('1e-50'))

    def test_mutated_single_event_is_not_exponentially_suppressed(self):
        # An unapproved extra source atom at u=0 adds (h/q)*eta*e^-pi,
        # constant in Im(s), unlike the claimed exponential analytic alias rate.
        mp=self.mp
        with mp.workdps(55):
            h=F(1,2)
            eta=mp.mpf('0.25')
            a=sampled_gamma_r(mp.mpc('.5','6'),h,interleaves=2,
                              left_steps=350,right_steps=16,dps=65)
            b=a['refined']+mp.mpf('0.25')*eta*mp.exp(-mp.pi)
            self.assertGreater(abs(b-a['true_gamma_r']),mp.mpf('1e-3'))
            self.assertLess(a['observed_absolute_error'],mp.mpf('1e-7'))

    def test_analytic_gamma_jets_within_exact_cauchy_certificate(self):
        mp=self.mp
        with mp.workdps(65):
            cert=gamma_r_jet_certificate(F(1,4),F(1,2),F(3,2),8,
                collar=F(1,4),jet_order=2,left_steps=500,right_steps=18,
                taylor_order=100)
            B=mp.mpf(cert['jet_error_upper'].numerator)/cert['jet_error_upper'].denominator
            for z in (mp.mpc('.5','8'),mp.mpc('1','3'),mp.mpc('1.5','-8')):
                d=mp.mpf('0.25')
                clock2=d*mp.fsum((n*d/2)**2 *mp.exp(z*(n*d)/2-mp.pi*mp.exp(n*d))
                    for n in range(-500,19))
                target2=mp.diff(lambda w: mp.power(mp.pi,-w/2)*mp.gamma(w/2),z,2)
                self.assertLess(abs(clock2-target2),B)

    def test_compact_tate_mellin_bump_and_negative_control_bound(self):
        mp=self.mp
        with mp.workdps(65):
            h=F(1,4)
            cert=compact_mellin_band_bound(h,8,7,derivative_order=2)
            B=mp.mpf(cert['bound'].numerator)/cert['bound'].denominator
            # phi(x)=x^-1/2*(1-(log x)^2)^2_+, source sigma=1.
            for t in (-8,-3,0,3,8):
                wave=lambda u: (1-u*u)**2*mp.exp(mp.j*t*u/2)
                center=mp.quad(wave,[-1,0,1])
                actual=mp.mpf('0.25')*mp.fsum(wave(mp.mpf(n)/4)
                                             for n in range(-3,4))
                self.assertLess(abs(actual-center),B)


if __name__=='__main__':
    unittest.main()