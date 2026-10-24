"""Exact adversarial receipts: BBP source typing, Hankel memory and false bounds."""
import unittest
from fractions import Fraction as Q
from math import comb
from observational_succ.bbp_source_memory import (
    POLE_DATA, forcing, forcing_integral_exact, pole_moment,
    positive_source_kernel, tail_interval, first_hankel_interval,
    cauchy_matrix, fraction_determinant, recover_pole_weights,
    forced_step, source_alpha_interval, rational_counterfeit_tail,
    rational_counterfeit_forcing, exact_prime_path_flips,
    false_deepseek_cost_bound_witness
)

class BBPSourceTyping(unittest.TestCase):
    def test_signed_pole_moment_hierarchy(self):
        assert [pole_moment(k) for k in range(5)] == [
            Q(),Q(15,64),Q(151,512),Q(1209,4096),Q(8995,32768)]
        self.assertEqual(sum(w for _,w in POLE_DATA),0)
        for a,_ in POLE_DATA:
            self.assertEqual((16*a)%1,0)

    def test_positive_kernel_and_integral(self):
        for t in (Q(),Q(1,100),Q(1,4),Q(1,2),Q(3,4),Q(99,100)):
            self.assertGreater(positive_source_kernel(t),0)
        self.assertEqual(positive_source_kernel(Q(1)),0)
        for n in range(1,80):
            self.assertEqual(forcing(n),forcing_integral_exact(n))
            self.assertGreater(forcing(n),0)
        with self.assertRaises(ValueError):
            positive_source_kernel(Q(2))

    def test_four_source_readouts_authenticate_pole_weights(self):
        mat=cauchy_matrix()
        self.assertEqual(fraction_determinant(mat),
                         Q(8388608,1224171073125))
        observed=[forcing(n) for n in range(1,5)]
        self.assertEqual(observed,[Q(47,15),Q(106,819),Q(829,19635),
                                  Q(316,15225)])
        self.assertEqual(recover_pole_weights(observed),
                         tuple(w for _,w in POLE_DATA))
        altered=observed[:];altered[2]+=Q(1,10**9)
        self.assertNotEqual(recover_pole_weights(altered),
                            tuple(w for _,w in POLE_DATA))
        with self.assertRaises(ValueError):
            recover_pole_weights(observed[:3])

    def test_bounded_tail_selected_source_not_initial_alias(self):
        self.assertEqual(forced_step(Q(),1),Q(2,15))
        self.assertEqual(forced_step(Q(1,3),1),Q(7,15))
        for k in range(1,8):
            lo,hi=tail_interval(0,k)
            self.assertTrue(0<lo<hi<Q(1,4))
            a,b=source_alpha_interval(Q(0),k)
            c,d=source_alpha_interval(Q(1,3),k)
            self.assertEqual((c-a,d-b),(Q(1,3),Q(1,3)))
            self.assertFalse(c<=Q(1,3)<=d)
        with self.assertRaises(ValueError):
            tail_interval(-1)


    def test_global_positive_beta_tail_enclosure(self):
        from observational_succ.bbp_source_memory import (
            source_tail_beta_bracket,source_tail_sharp_beta_bracket)
        for n in range(0,45):
            low,high=source_tail_beta_bracket(n)
            sharp,upper=source_tail_sharp_beta_bracket(n)
            actual_low,actual_high=tail_interval(n,7)
            self.assertLess(low,actual_low)
            self.assertGreater(high,actual_high)
            self.assertLess(sharp,actual_low)
            self.assertGreater(upper,actual_high)
            self.assertGreaterEqual(sharp,low)
        # The analytic rate, not finite sampling, proves n² t_n -> 1/64.
        n=100
        B=source_tail_beta_bracket(n)[1]
        self.assertLess(Q(4,(8*n+1)*(8*n+2)*(8*n+3))/B,Q(1,100))

    def test_stieltjes_tail_hankel_positive_source_certificate(self):
        for K in (2,4,7):
            lo,hi=first_hankel_interval(K)
            self.assertGreater(lo,Q(1,2200))
            self.assertGreater(hi,lo)
        for n in range(20):
            for K in (2,3,4):
                a,b=tail_interval(n,K)
                aa,bb=tail_interval(n,K+1)
                self.assertLess(a,aa)
                self.assertLess(bb,b)

    def test_positive_infinite_rank_does_not_imply_normality(self):
        self.assertEqual(rational_counterfeit_tail(0),Q(1,2))
        for n in range(1,40):
            self.assertGreater(rational_counterfeit_forcing(n),0)
            self.assertEqual(16*rational_counterfeit_tail(n-1)
                             -rational_counterfeit_forcing(n),
                             rational_counterfeit_tail(n))
        # The counterfeit tail is int_0^1 u^n(1-u)du. It has continuous
        # positive density and full Hankel rank but selected rational orbit.
        self.assertEqual((16*rational_counterfeit_tail(0))%1,0)
        for n in range(1,14):
            self.assertEqual((16**n*rational_counterfeit_tail(0))%1,0)


class DeepSeekFalseImplications(unittest.TestCase):
    def test_prime_path_is_not_endpoint_difference(self):
        # All cos(n*pi/4) signs for odd n are +/-sqrt(2)/2.
        self.assertEqual(exact_prime_path_flips(1),0)
        self.assertEqual(exact_prime_path_flips(15),2)
        self.assertEqual(exact_prime_path_flips(255),2)
        witness=false_deepseek_cost_bound_witness()
        self.assertEqual(witness["lhs_over_sqrt2"],Q(4,3))
        self.assertEqual(witness["claimed_upper"],Q(4,3))
        # Thus the actual left side is (4/3)*sqrt(2)>4/3.

    def test_wrong_domain_pole_covering_does_not_erase_source(self):
        for a,_ in POLE_DATA:
            self.assertEqual(16*a%1,0)
        self.assertEqual(pole_moment(1),Q(15,64))
        self.assertEqual(forcing(1),Q(47,15))
        self.assertNotEqual(forcing(1),0)


    def test_positive_rational_noncoboundaries_have_arbitrary_decay(self):
        from observational_succ.bbp_source_memory import (
            high_order_rational_forcing, high_order_partial_fractions,
            high_order_pole_invariant)
        for order in range(1,8):
            self.assertNotEqual(high_order_pole_invariant(order,16),0)
            self.assertEqual(high_order_pole_invariant(order,16),
                             (-15)**order)
            for n in range(1,26):
                value=high_order_rational_forcing(n,order)
                self.assertGreater(value,0)
                self.assertEqual(value,high_order_partial_fractions(n,order))
            self.assertLessEqual(high_order_rational_forcing(100,order)*100**(order+1),
                                 __import__('math').factorial(order))
        # Source-class restriction matters: exponential 16^-n is a
        # coboundary with a non-rational q(n)=16^-n/255.
        for n in range(2,12):
            q=lambda k: Q(1,255*16**k)
            self.assertEqual(16*q(n-1)-q(n),Q(1,16**n))

    def test_rational_counterfeit_is_not_identical_BBP_source(self):
        self.assertNotEqual(rational_counterfeit_forcing(1),forcing(1))
        self.assertEqual(forced_step(Q(),1),Q(2,15))
        self.assertNotEqual(forced_step(Q(1,3),1),Q(1,3))

if __name__ == "__main__":
    unittest.main()
