import unittest
from fractions import Fraction as Q
import math
from observational_succ.suzuki_arch_intervals import (
    ArchIntervalError,atan_interval,pi_interval,log_interval,gamma_interval,
    exp_interval,exp_minus_interval,sqrt2_interval,arch_lerch_tail_interval,
    arch_screw_interval,first_source_screw_interval,
)


def inside(real, interval):
    a,b=interval
    return float(a) <= real <= float(b)


class SuzukiArchIntervalTests(unittest.TestCase):
    def test_traditional_constants_against_independent_stdlib(self):
        self.assertTrue(inside(math.pi,pi_interval()))
        self.assertTrue(inside(math.log(2),log_interval(Q(2))))
        self.assertTrue(inside(math.log(math.pi),__import__("observational_succ.suzuki_arch_intervals",fromlist=["log_pi_interval"]).log_pi_interval()))
        self.assertTrue(inside(math.sqrt(2),sqrt2_interval()))
        self.assertTrue(inside(0.5772156649015328606,gamma_interval()))

    def test_rational_exponential_bounds(self):
        for x in (Q(),Q(1,100),Q(1,2),Q(1),Q(2),Q(7,2),Q(17)):
            self.assertTrue(inside(math.exp(float(x)),exp_interval(x)))
            self.assertTrue(inside(math.exp(-float(x)),exp_minus_interval(x)))

    def test_lerch_interval_vs_independent_mpmath(self):
        import mpmath as mp
        mp.mp.dps=40
        for t in (Q(1,20),Q(1,4),Q(1,2),Q(3,4)):
            lo,hi=arch_lerch_tail_interval(t,terms=32)
            tm=mp.mpf(t.numerator)/t.denominator
            # Independent special-function closed evaluation rather than prefix/tail.
            true=(mp.zeta(2,mp.mpf(1)/4) - mp.exp(-tm/2)*
                  mp.lerchphi(mp.exp(-2*tm),2,mp.mpf(1)/4))/4
            conv=lambda q:mp.mpf(q.numerator)/q.denominator
            self.assertLessEqual(conv(lo),true)
            self.assertLessEqual(true,conv(hi))
            self.assertLess(hi-lo,Q(1,16))

    def test_completed_arch_against_mpmath_primary_formula(self):
        import mpmath as mp
        mp.mp.dps=50
        for t in (Q(1,20),Q(1,4),Q(1,2),Q(3,4)):
            lo,hi=arch_screw_interval(t,terms=48)
            tm=mp.mpf(t.numerator)/t.denominator
            true=-4*(mp.exp(tm/2)+mp.exp(-tm/2)-2)
            true-=tm/2*(mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi))
            true-=(mp.zeta(2,mp.mpf(1)/4) - mp.exp(-tm/2)*mp.lerchphi(mp.exp(-2*tm),2,mp.mpf(1)/4))/4
            conv=lambda q:mp.mpf(q.numerator)/q.denominator
            self.assertLessEqual(conv(lo),true)
            self.assertLessEqual(true,conv(hi))

    def test_full_source_prime_switch_and_rigorous_bracketing(self):
        import mpmath as mp
        mp.mp.dps=50
        for t in (Q(1,4),Q(1,2),Q(3,4),Q(4,5)):
            c=first_source_screw_interval(t,terms=40)
            lo,hi=Q(c["full_lower"]),Q(c["full_upper"])
            self.assertLessEqual(lo,hi)
            self.assertTrue(c["pole_gamma_lerch_included"])
            self.assertTrue(c["true_prime_2_half_density_included"])
            self.assertFalse(c["fake_composite_six_included"])
            tm=mp.mpf(t.numerator)/t.denominator
            arch=-4*(mp.exp(tm/2)+mp.exp(-tm/2)-2)
            arch-=tm/2*(mp.digamma(mp.mpf(1)/4)-mp.log(mp.pi))
            arch-=(mp.zeta(2,mp.mpf(1)/4)-mp.exp(-tm/2)*mp.lerchphi(mp.exp(-2*tm),2,mp.mpf(1)/4))/4
            true=arch+mp.log(2)/mp.sqrt(2)*max(mp.mpf(0),tm-mp.log(2))
            conv=lambda q:mp.mpf(q.numerator)/q.denominator
            self.assertLessEqual(conv(lo),true)
            self.assertLessEqual(true,conv(hi))
            if t<Q(2,3):
                self.assertEqual(Q(c["prime_upper"]),0)
            if t>Q(3,4)-Q(1,100):
                self.assertGreater(Q(c["prime_lower"]),0)

    def test_zero_input_and_invalid_source_readout(self):
        self.assertEqual(arch_screw_interval(Q()),(Q(),Q()))
        for t in (Q(1),Q(5,6),Q(-1,10)):
            with self.assertRaises(ArchIntervalError):
                first_source_screw_interval(t)
        with self.assertRaises(ArchIntervalError):
            arch_lerch_tail_interval(Q(-1,100))


if __name__ == '__main__':unittest.main()
