"""Exact algebra, hostile mutations and independent quadrature of log mixtures."""
from fractions import Fraction as Q
import unittest

from observational_succ import bbp_log_mixture as lm
from observational_succ.bbp_natural_carrier import exact_forcing
from observational_succ.gamma_bbp_signed_coherence import green_tail_interval


class BBPLogMixtureTests(unittest.TestCase):
    def test_original_four_poles_recovered_on_fresh_indices(self):
        for n in (1,2,3,7,31,97,257,1009):
            self.assertEqual(lm.source_mixture_mass(n), exact_forcing(n))
            self.assertTrue(lm.source_authentication_check(n))
        # Dropping one pole pair is detected by the original source.
        a=Q(8*97-7)
        mutated=sum((Q(v*d)/(a*(a+d)) for d,v in ((3,2),(4,1))),Q())
        self.assertNotEqual(mutated,exact_forcing(97))

    def test_exact_probability_moments(self):
        self.assertEqual(lm.tail_base_moment(0),1)
        self.assertEqual(lm.tail_base_moment(1),Q(7,2))
        self.assertEqual(lm.tail_base_moment(2),Q(55,3))
        # Independent finite integration / summation approaches exact moments below.
        for k in (0,1,2,3):
            partial=sum((Q(v,16**j)*Q((8*j-7+d)**(k+1)-(8*j-7)**(k+1),k+1)
                         for j in range(1,20) for d,v in lm.POLE_DIFFERENCES),Q())
            self.assertGreater(lm.tail_base_moment(k),partial)
            self.assertLess(lm.tail_base_moment(k)-partial,Q(1,10**12))

    def test_global_bounds_against_independent_green_intervals(self):
        for n in (1,2,11,32,127,1024):
            lo,hi=lm.tail_jensen_bounds(n)
            t=green_tail_interval(n,16)
            self.assertLess(lo,t.lower)
            self.assertLess(t.upper,hi)
            eta=lm.tail_log_mixture_certificate(n)
            self.assertGreater(eta.eta_lower,0)
            self.assertLess(eta.eta_upper,Q(7,16*n))
            self.assertFalse(eta.pi_normality_proved)

    def test_mellin_mean_against_density_quadrature(self):
        import mpmath as mp
        with mp.workdps(60):
            conv=lambda q:mp.mpf(q.numerator)/q.denominator
            for n in (1,5,41):
                a=mp.mpf(8*n)
                # Integrate original signed source kernel after t=y/a.
                def density(y):
                    if not y:return mp.mpf(0)
                    t=y/a
                    p=-2*mp.expm1(-3*t)-mp.expm1(-4*t)-mp.expm1(-5*t)
                    return mp.exp(-y-t)*p/(16-mp.exp(-8*t))/a
                mass=mp.quad(density,[0,1,mp.inf])
                logmean=mp.quad(lambda y:density(y)*mp.log(y),[0,1,mp.inf])/mass
                eta=1-mp.euler-logmean
                cert=lm.tail_log_mixture_certificate(n,14,30)
                self.assertLess(conv(cert.mass_lower),mass)
                self.assertLess(mass,conv(cert.mass_upper))
                self.assertLess(conv(cert.eta_lower),eta)
                self.assertLess(eta,conv(cert.eta_upper))

    def test_source_log_identity_against_separate_quadrature(self):
        import mpmath as mp
        # At the largest index the exact log interval is narrower than 1e-170.
        # A low-precision numeric oracle would round it to a single endpoint.
        with mp.workdps(220):
            conv=lambda q:mp.mpf(q.numerator)/q.denominator
            for n in (1,13,73):
                a=mp.mpf(8*n-7)
                raw=mp.quad(lambda u: sum(v*mp.log(1+u/a)/(a+u)**2
                            for d,v in lm.POLE_DIFFERENCES if u<d),[0,3,4,5])
                value=raw/conv(exact_forcing(n))
                lo,hi=lm.source_log_defect_interval(n,32)
                self.assertLess(conv(lo),value)
                self.assertLess(value,conv(hi))

    def test_shape_two_laplace_and_mutated_shape_one(self):
        for n in (16,256,4096):
            lo,hi=lm.tail_laplace_interval(n,Q(1),16)
            # Shape two limit 1/4; finite rates are larger than base a.
            self.assertGreater(lo,Q(1,4))
            self.assertLess(hi,Q(1,3))
            self.assertLess(hi-Q(1,4),Q(1,n))
            self.assertLess(hi,Q(1,2))  # Exp(1) prediction is rejected.
        self.assertEqual(lm.tail_laplace_interval(3,0),(Q(1),Q(1)))

    def test_all_n_asymptotic_error_certificate(self):
        for n in (16,31,128,509,2048):
            c=lm.tail_log_mixture_certificate(n,16,28)
            a=Q(8*n)
            self.assertLessEqual(Q(7,2)/a-55/a**2,c.eta_lower)
            self.assertLess(c.eta_upper,Q(7,2)/a)
            # Both exact intervals support the finite scope of the limit 4/49.
            low=c.mass_lower/c.eta_upper**2
            high=c.mass_upper/c.eta_lower**2
            self.assertLess(low,high)
            self.assertLess(abs((low+high)/2-Q(4,49)),Q(1,n))

    def test_invalid_domains_fail_closed(self):
        for n in (0,-1,True,1.5):
            with self.assertRaises(ValueError):lm.tail_log_mixture_certificate(n)
        with self.assertRaises(ValueError):lm.tail_laplace_interval(1,0.5)
        with self.assertRaises(ValueError):lm.tail_laplace_interval(1,-1)
        with self.assertRaises(ValueError):lm.tail_log_mixture_certificate(1,0)
        with self.assertRaises(ValueError):lm.tail_base_moment(True)

    def test_same_moments_zero_anchor_rational_counterfeit(self):
        for k in (0,1,2):
            self.assertEqual(lm.counterfeit_moment(k),lm.tail_base_moment(k))
        self.assertNotEqual(lm.counterfeit_moment(3),lm.tail_base_moment(3))
        self.assertEqual(lm.counterfeit_orbit(0),0)
        for n in (1,2,3,17,53):
            self.assertGreater(lm.counterfeit_forcing(n),0)
            self.assertEqual(lm.counterfeit_orbit(n),
                             16*lm.counterfeit_orbit(n-1)+lm.counterfeit_forcing(n))
            self.assertNotEqual(lm.counterfeit_forcing(n),exact_forcing(n))
        alpha=lm.counterfeit_tail(0)
        h=alpha.denominator
        # At h, the expanding rational part is always an integer. Thus the
        # phase tends to zero as -h*T*_n, implying mean character tends to one.
        for n in (1,17,37):
            self.assertEqual((h*16**n*alpha).denominator,1)
            self.assertEqual(h*lm.counterfeit_orbit(n),
                             h*16**n*alpha-h*lm.counterfeit_tail(n))

    def test_relative_mellin_loss_has_summable_upper_envelope(self):
        self.assertEqual(lm.relative_mellin_loss_bound(1,0),0)
        for n in (1,2,64,999):
            self.assertEqual(lm.relative_mellin_loss_bound(n,1),Q(55,192*n*n))
        self.assertEqual(lm.relative_mellin_loss_bound(1,100),1)
        self.assertEqual(lm.relative_mellin_loss_bound(4,-3),
                         lm.relative_mellin_loss_bound(4,3))


if __name__ == '__main__':
    unittest.main()
