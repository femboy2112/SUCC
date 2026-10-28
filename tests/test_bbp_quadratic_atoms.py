"""Exact base-8 BBP atomic decomposition and genuinely independent analytic holdouts.

New mathematical interface is source-typed; none of these tests claims to
prove pi normality or the asymptotics of signed Weyl sums.
"""
import unittest
from fractions import Fraction as F

from observational_succ import bbp_quadratic_atoms as a


class AtomicPolynomials(unittest.TestCase):
    def test_exact_polynomial_annihilation(self):
        cert = a.source_polynomial_certificate()
        for k in ('P_equals_boundary_times_cancelled', 'octic_factorizes',
                  'reduced_identity', 'numerator_endpoint_zero', 'first_endpoint_jet'):
            self.assertTrue(cert[k])
        self.assertEqual(a.D_MINIMAL, (F(1), F(-1), F(), F(1, 2), -F(1, 4)))

    def test_minimal_rational_denominator_coprime(self):
        # Under this chosen rational-transfer model 4 states are minimal.
        num = a.BOUNDARY
        den = a.D_MINIMAL
        self.assertEqual(len(den)-1, 4)
        # Numerator has only root t=1, but denominator D(1)=1/4.
        self.assertEqual(sum(num), 0)
        self.assertEqual(sum(den), F(1, 4))
        _, rem = a.pdivmod(den, num)
        self.assertNotEqual(rem, (F(0),))

    def test_two_clock_source_decomposition(self):
        # 1-t^8/16 = (1-t^4/4)(1+t^4/4)
        plus=(F(1),F(0),F(0),F(0),F(1,4))
        minus=(F(1),F(0),F(0),F(0),-F(1,4))
        first=(F(4), F(2), F(0), F(-1))
        second=(F(0), F(-2), F(0), F(-1))
        self.assertEqual(a.pmul(plus,minus),a.OCTIC)
        self.assertEqual(a.padd(a.pmul(first,minus),a.pmul(second,plus)),a.P_SOURCE)

    def test_matrix_eighth_common_return_not_fourth(self):
        c=a.matrix_atoms_certificate()
        self.assertTrue(all(v for k,v in c.items() if k not in
                            ('least_common_positive_scalar_return',
                             'minimal_real_state_dimension_for_this_reduced_transfer')))
        self.assertEqual(c['least_common_positive_scalar_return'],8)
        self.assertNotEqual(a.mpow(a.G_GAUSSIAN,4),a.mpow(a.H_REAL,4))
        self.assertNotEqual(a.mpow(a.G_GAUSSIAN,2),a.mpow(a.H_REAL,2))

    def test_fourth_order_impulse_recovers_sparse_bbp(self):
        impulse=a.filter_coefficients(160)
        self.assertEqual(impulse[:8],a.BBP_TAPS)
        for n,v in enumerate(impulse):
            self.assertEqual(v,a.return_tap(n))
        self.assertEqual(impulse[8],F(1,4))
        self.assertEqual(impulse[11],-F(1,8))

    def test_four_pole_moment_from_two_atom_filter(self):
        for n in range(1,200):
            self.assertEqual(a.authentic_fourpole(n),a.moment_from_taps(n))
            self.assertGreater(a.authentic_fourpole(n),0)
        for n in range(1,18):
            self.assertEqual(a.paired_four_clock_prefix(n),a.bbp_prefix(n))

    def test_changed_pole_fails_source_zero(self):
        counterfeit = a.padd(a.P_SOURCE, (F(0),F(0),F(0),F(0),F(0),F(1)))
        self.assertNotEqual(sum(counterfeit),F(0))
        self.assertNotEqual(a.pmul(counterfeit,a.D_MINIMAL),
                            a.pmul(a.BOUNDARY,a.OCTIC))


class ExactBoundary(unittest.TestCase):
    def test_rational_log_weighted_completion(self):
        self.assertEqual(a.rational_radial_completion(0),F(0))
        self.assertEqual(a.rational_radial_completion(1),F(2,105))
        self.assertEqual(a.rational_radial_completion(2),F(67,90090))
        for n in range(1,15):
            self.assertGreater(a.rational_radial_completion(n),0)


    def test_angular_pi_and_radial_null_are_exact_shell_channels(self):
        cert=a.signed_channel_certificate()
        self.assertTrue(cert['taps_sum_to_original'])
        self.assertTrue(cert['angular_equals_4_over_angle'])
        self.assertTrue(cert['radial_equals_logarithmic_derivative'])
        self.assertEqual(cert['original_radial_channel_integral'], F(0))
        for n in range(0,18):
            self.assertEqual(a.radial_channel_prefix(n),a.rational_radial_completion(n))
            self.assertEqual(a.radial_channel_prefix(n)+a.angular_channel_prefix(n),
                             a.bbp_prefix(n))

    def test_analytic_source_mutant_preserves_jet_not_pi(self):
        mutant=a.same_atoms_different_source(F(1, 7))
        self.assertEqual(sum(mutant),F(0))
        self.assertEqual(-sum(i*c for i,c in enumerate(mutant)),F(15))
        self.assertNotEqual(mutant,a.P_SOURCE)
        # additional kernel eps*(1-t)^2/D_MINIMAL >0 in (0,1).
        for t in (F(1, 8), F(1, 2), F(7, 8)):
            extra=sum(c*t**i for i,c in enumerate(mutant))-sum(c*t**i for i,c in enumerate(a.P_SOURCE))
            self.assertGreater(extra,0)

    def test_gamma_two_boundary_log_moment(self):
        import mpmath as mp
        with mp.workdps(55):
            for n in (1,3,10):
                shift=a.endpoint_beta_log_rational_part(n)
                got=mp.log(8*n)+mp.mpf(shift.numerator)/shift.denominator
                den=mp.beta(8*n+1,2)
                direct=mp.quad(lambda t: t**(8*n)*(1-t)*mp.log(8*n*(1-t)),[0,1])/den
                self.assertLess(abs(got-direct),mp.mpf('1e-47'))
            n=10000
            shift=a.endpoint_beta_log_rational_part(n)
            got=mp.log(8*n)+mp.mpf(shift.numerator)/shift.denominator
            self.assertLess(abs(got-(1-mp.euler)),mp.mpf('1e-4'))

    def test_green_tail_rational_certificates(self):
        for n in (1,2,3,4,8,16,64,1024):
            lo,hi=a.green_tail_bounds(n)
            self.assertLess(F(0),lo)
            self.assertLess(lo,hi)
            self.assertEqual(hi,F(1,(8*n+1)*(8*n+2)))
            rlo,rhi=a.bbp_remainder_bounds(n)
            self.assertEqual(rlo,F(16,16**n)*lo)
            self.assertEqual(rhi,F(16,16**n)*hi)
        self.assertFalse(a.source_status()['pi_normality_proved'])

    def test_green_asymptotic_bounds_shrink(self):
        # The normalized error / leading Beta moment has exact gap 6/(8n+3).
        for n in (1,5,100,10000):
            lo,hi=a.green_tail_bounds(n)
            self.assertEqual((hi-lo)/hi,F(6,8*n+3))

    def test_real_radial_excess_positive(self):
        # (2-t^2) - ((t-1)^2+1) = 2t(1-t) strictly inside.
        for t in (F(1,9),F(1,2),F(4,5),F(99,100)):
            den=(t-1)**2+1
            self.assertEqual((2-t*t)-den,2*t*(1-t))
            self.assertGreater((2-t*t)/den,1)

    def test_finite_analytic_oracles(self):
        try:
            import mpmath as mp
        except ImportError:
            self.skipTest('mpmath diagnostics are optional; exact tests always run')
        with mp.workdps(68):
            A=lambda t:(t-1)**2+1
            Q=lambda t:(2-t*t)*A(t)
            R=lambda t:(2-t*t)/A(t)
            kernel=lambda t:16*(1-t)/Q(t)
            self.assertLess(abs(mp.quad(kernel,[0,1])-mp.pi),mp.mpf('1e-60'))
            for n in (1,2,3,4,7):
                pref=a.bbp_prefix(n)
                prefix=mp.mpf(pref.numerator)/pref.denominator
                ang=mp.quad(lambda t:4*(t**8/16)**n/A(t),[0,1])
                radial=mp.quad(lambda t:16*n/16**n*t**(8*n-1)*mp.log(R(t)),[0,1])
                r=a.rational_radial_completion(n)
                rat=mp.mpf(r.numerator)/r.denominator
                tail=mp.quad(lambda t:16*(t**8/16)**n*(1-t)/Q(t),[0,1])
                self.assertLess(abs(radial-rat),mp.mpf('1e-58'))
                self.assertLess(abs((ang-radial)-(mp.pi-prefix)),mp.mpf('1e-58'))
                self.assertLess(abs(tail-(ang-radial)),mp.mpf('1e-58'))
                lo,hi=a.bbp_remainder_bounds(n)
                self.assertGreaterEqual(mp.pi-prefix,mp.mpf(lo.numerator)/lo.denominator)
                self.assertLessEqual(mp.pi-prefix,mp.mpf(hi.numerator)/hi.denominator)


if __name__ == '__main__':
    unittest.main()
