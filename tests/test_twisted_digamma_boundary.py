"""Exact controls and independent analytic oracles for the twisted Euler source."""
from fractions import Fraction as Q
import unittest
import mpmath as mp

from observational_succ.twisted_digamma_boundary import (
    alternating_reciprocal_prefix, alternating_reciprocal_interval,
    beta_integer_second, reciprocal_gamma_word, alternating_euler_interval,
    dyadic_euler_certificate, dyadic_finite_weights, normalized_euler_interval,
    bbp_alternating_interval, bbp_digamma_interval, finite_resolvent_defect,
)
from observational_succ.zero_one_gamma_bridge import GammaBridgeError
from observational_succ.bbp_source_memory import forcing


def m(x):
    return mp.mpf(x.numerator)/x.denominator


class TwistedDigammaTests(unittest.TestCase):
    def contains(self, interval, value):
        self.assertLessEqual(m(interval.lower), value)
        self.assertGreaterEqual(m(interval.upper), value)

    def test_positive_beta_expansion_against_digamma(self):
        with mp.workdps(90):
            for a in (Q(1,8), Q(1,2), Q(1), Q(7,3), Q(101,4)):
                truth=(mp.digamma((m(a)+1)/2)-mp.digamma(m(a)/2))/2
                for depth in (0,1,8,37):
                    self.contains(alternating_reciprocal_interval(a,depth),truth)

    def test_beta_rational_integral_independent_binomial(self):
        from math import comb
        for a in (Q(1,7),Q(1),Q(9,4)):
            for k in range(12):
                integral=sum((Q((-1)**j*comb(k,j))/(a+j) for j in range(k+1)),Q())
                self.assertEqual(beta_integer_second(a,k),integral)

    def test_alternating_finite_successor_boundary(self):
        for a in (Q(1,8),Q(1),Q(31,7)):
            for count in (1,2,7,16):
                value=alternating_reciprocal_prefix(a,count)+alternating_reciprocal_prefix(a+1,count)
                self.assertEqual(value,1/a+Q((-1)**(count-1))/(a+count))
                self.assertNotEqual(value,1/a)  # Dropped-boundary mutation.

    def test_gamma_word_exact_reciprocal_transport(self):
        for a in (Q(1,3),Q(1),Q(23,4)):
            for initial in (Q(1),Q(3,7)):
                value=initial
                for steps in range(12):
                    word=reciprocal_gamma_word(a,steps)
                    self.assertEqual(word.apply(initial),value)
                    value=(a+steps)/(2*value)
            two=reciprocal_gamma_word(a,2)
            self.assertEqual(two.multiplier,(a+1)/a)
            self.assertNotEqual(two.multiplier,1)  # Two twists are not identity.

    def test_gamma_word_against_gamma_and_reflection(self):
        with mp.workdps(90):
            def ratio(a): return mp.gamma((a+1)/2)/mp.gamma(a/2)
            for a in (mp.mpf(1)/8,mp.mpf(1)/3,mp.mpf(3)/4):
                self.assertLess(abs(ratio(a)*ratio(a+1)-a/2),mp.mpf('1e-75'))
                self.assertLess(abs(ratio(a)/ratio(1-a)-mp.tan(mp.pi*a/2)),mp.mpf('1e-75'))

    def test_dilated_euler_against_gamma_quotient(self):
        with mp.workdps(90):
            for d in (Q(1,2),Q(1),Q(2),Q(5),Q(16),Q(128)):
                truth=mp.log(2)/m(d)-mp.log(mp.sqrt(mp.pi)*mp.gamma(1+1/(2*m(d)))/mp.gamma(mp.mpf(1)/2+1/(2*m(d))))
                for count in (0,1,8,17):
                    self.contains(alternating_euler_interval(d,count,40),truth)

    def test_unit_twist_returns_log_four_over_pi_not_gamma(self):
        with mp.workdps(90):
            interval=alternating_euler_interval(1,32,40)
            self.contains(interval,mp.log(4/mp.pi))
            self.assertLess(m(interval.upper),mp.euler)

    def test_dyadic_telescope_preserves_every_finite_source_cell(self):
        for levels in range(7):
            for blocks in (1,3,7):
                weights=dyadic_finite_weights(levels,blocks)
                self.assertTrue(all(w==1 for w in weights.values()))
                if levels:
                    # Omitting the final coarse tail breaks exactly its source cells.
                    self.assertNotEqual(weights[2**levels]-2**levels,1)

    def test_dyadic_gamma_interval_and_normalization_cocycle(self):
        with mp.workdps(90):
            for levels in (0,1,4,8):
                cert=dyadic_euler_certificate(levels,24,40)
                self.contains(cert.total,mp.euler)
                self.assertEqual(cert.tail.upper,Q(5,6*2**levels))
                shifted=normalized_euler_interval(Q(3,7),levels=levels,count=24,logarithm_terms=40)
                self.assertEqual(shifted.lower,cert.total.lower-Q(3,7))
                self.assertEqual(shifted.upper,cert.total.upper-Q(3,7))
                self.contains(shifted,mp.euler-mp.mpf(3)/7)

    def test_dilation_asymptotic_independent_gamma_oracle(self):
        with mp.workdps(100):
            for d in (20,100,1000):
                b=mp.mpf(1)/d
                actual=b*mp.log(2)-mp.log(mp.sqrt(mp.pi)*mp.gamma(1+b/2)/mp.gamma((1+b)/2))
                # Absolute termwise Taylor bound, not a fitted asymptotic rate.
                self.assertLess(abs(actual-mp.pi**2/(24*d*d)),mp.zeta(3)/(3*d**3))

    def test_bbp_four_rays_agree_with_direct_alternating_source(self):
        with mp.workdps(90):
            shifts=(mp.mpf(1)/8,mp.mpf(1)/2,mp.mpf(5)/8,mp.mpf(3)/4)
            truth=sum(c*(mp.digamma((a+1)/2)-mp.digamma(a/2))/16
                      for c,a in zip((4,-2,-1,-1),shifts))
            self.contains(bbp_digamma_interval(48),truth)
            for count in (0,1,2,31,32):
                self.contains(bbp_alternating_interval(count),truth)

    def test_finite_resolvent_boundary_and_wrong_multiplier_mutation(self):
        values=tuple(forcing(n) for n in range(1,10))
        for b in (Q(16),Q(-1),Q(3,2)):
            defect,expected=finite_resolvent_defect(values,b)
            self.assertEqual(defect,expected)
            self.assertNotEqual(defect,0)
        self.assertNotEqual(finite_resolvent_defect(values,16)[0],
                            finite_resolvent_defect(values,-1)[0])

    def test_domain_guards(self):
        for a in (0,-1,0.5,True):
            with self.assertRaises(GammaBridgeError):alternating_reciprocal_interval(a)
        for count in (-1,True,1.5):
            with self.assertRaises(GammaBridgeError):alternating_euler_interval(1,count)
        with self.assertRaises(GammaBridgeError):reciprocal_gamma_word(1,2).apply(0)
        with self.assertRaises(GammaBridgeError):finite_resolvent_defect((Q(1),Q(2)),0)
        with self.assertRaises(GammaBridgeError):dyadic_finite_weights(12,10)
        with self.assertRaises(GammaBridgeError):normalized_euler_interval(0.3)


if __name__ == '__main__':
    unittest.main()
