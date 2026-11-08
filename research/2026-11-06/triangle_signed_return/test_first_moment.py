"""Preregistered authentic first-moment exact arithmetic and independent CAS controls."""
import unittest
from fractions import Fraction as F
from experiment import source,four_poles
from first_moment import (A,weighted_pole_coefficients,exact_prefix,positive_remainder,
                          source_shadow,run)

class MomentControls(unittest.TestCase):
    def test_source_coefficients_and_poles(self):
        d=weighted_pole_coefficients()
        self.assertEqual(d,(F(7,2),-F(1),-F(3,8),-F(1,4)))
        for n in range(1,300):
            self.assertEqual(source(n),four_poles(n))
            self.assertGreater(positive_remainder(n),0)

    def test_exact_partial_sum_is_increasing(self):
        prev=exact_prefix(1)
        for N in range(2,72):
            now=exact_prefix(N)
            self.assertEqual(now-prev,positive_remainder(N))
            prev=now

    def test_preregistered_moment_tail_check(self):
        data=run()
        self.assertEqual(data['linear_harmonic_coefficient_exact'],'15/64')
        self.assertEqual([v['N'] for v in data['exact_source_moment_tail_results']],[128,512,1024])
        self.assertEqual(data['real_weyl_saving'],'OPEN')

    def test_rational_shadow_is_not_same_moment(self):
        # The rational shadow’s weighted source has no log divergence.
        for n in range(4,129):
            self.assertLess(abs(source_shadow(n)),F(10,n**3))

if __name__=='__main__':unittest.main()
