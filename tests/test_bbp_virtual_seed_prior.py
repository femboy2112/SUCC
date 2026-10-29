"""Exact original-source certificates for the prior/selection firewall."""
from fractions import Fraction as F
import unittest

from observational_succ.bbp_virtual_seed_prior import (
    authentic_forcing, rational_source_passport, selected_rational_state,
    haar_seed_character_expectation, finite_coherent_tail,changed_seed_abs_bound,
    comoving_arithmetic_state,comoving_arithmetic_increment,comoving_completion_error_upper,
)

class BBPPriorFirewallTests(unittest.TestCase):
    def test_literal_four_original_poles(self):
        for n in range(1,121):
            self.assertEqual(authentic_forcing(n),rational_source_passport(n))
            self.assertGreater(authentic_forcing(n),0)

    def test_strict_quadratic_tail_majorization(self):
        for n in range(2,600):
            self.assertLessEqual(authentic_forcing(n),F(5,3*n*n))

    def test_real_selected_zero_seed(self):
        self.assertEqual(selected_rational_state(0),0)
        u=F(0)
        for n in range(1,19):
            u=16*u+authentic_forcing(n)
            self.assertEqual(u,selected_rational_state(n,0))

    def test_coherent_exceptional_seed_rational_enclosure(self):
        for n in (1,2,3,5,12,20):
            bounds=[finite_coherent_tail(n,j) for j in (0,1,4,8,12)]
            self.assertTrue(all(lower<upper for lower,upper in bounds))
            for k in range(1,len(bounds)):
                self.assertTrue(bounds[k-1][0]<bounds[k][0]<bounds[k][1]<bounds[k-1][1])
            self.assertLess(-bounds[0][0],changed_seed_abs_bound(n)+F(1))

    def test_global_changed_seed_tail_bound(self):
        for n in (1,2,3,10,20):
            lower,upper=finite_coherent_tail(n,20)
            self.assertLessEqual(-lower,changed_seed_abs_bound(n))
            self.assertLess(upper,0)

    def test_ensemble_expectation_is_not_selected_expectation(self):
        for n in range(6):
            for h in (-3,-1,1,2,7):
                self.assertEqual(haar_seed_character_expectation(h,n),0)
        self.assertEqual(selected_rational_state(0,0),0)
        # The actual seed s=0 has E[e(h U_0)] = 1, unlike Haar.
        self.assertEqual(haar_seed_character_expectation(1,0),0)

    def test_comoving_lift_is_original_zero_seed_expanding_dynamics(self):
        for seed in (F(0),F(1,3),F(-2,7)):
            self.assertEqual(comoving_arithmetic_state(0,seed),seed)
            for n in range(1,40):
                self.assertEqual(comoving_arithmetic_state(n,seed)-comoving_arithmetic_state(n-1,seed),
                                 comoving_arithmetic_increment(n))
                self.assertEqual(comoving_arithmetic_state(n,seed)-comoving_arithmetic_state(n,0),seed)

    def test_comoving_source_tail_certificate(self):
        for n in (1,2,4,10,18):
            self.assertEqual(comoving_completion_error_upper(n),changed_seed_abs_bound(n)/16**n)
            lower,upper=finite_coherent_tail(n,20)
            self.assertTrue(F(0)<-upper<-lower<=changed_seed_abs_bound(n))

    def test_invalid_inputs(self):
        for f,args in ((authentic_forcing,(0,)),(selected_rational_state,(-1,)),
                       (finite_coherent_tail,(0,5)),(finite_coherent_tail,(3,-1)),
                       (haar_seed_character_expectation,(0,3))):
            with self.assertRaises(ValueError):f(*args)

if __name__=='__main__': unittest.main()
