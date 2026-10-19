"""Exact source-tail resolvent theorem, endpoint controls and fresh holdouts."""
import unittest
from fractions import Fraction as F

from observational_succ import clamped_k_residual_bridge as B
from observational_succ import original_continuum_residual as R
from observational_succ import gamma_tail_resolvent_refinement as T


class RationalGammaTailTheorem(unittest.TestCase):
    def test_power_intervals_contain_later_rational_partial_sum(self):
        for J in (1,8,24):
            for power in (3,4,5):
                lo,hi = T.tail_power_interval(J,power,count=32)
                # Independent later partial sum plus its own integral tail.
                finite = T.finite_power_sum(J,J+96,power)
                d = 4*(J+96)+1
                il = F(1,4*(power-1)*d**(power-1))
                self.assertLessEqual(lo,finite+il)
                self.assertGreaterEqual(hi,finite+il+F(1,d**power))
                self.assertLess(lo,hi)

    def test_original_ou_resolvent_ode_and_both_endpoint_conditions(self):
        for h in ((F(1),), (F(0),F(1)), R.high_boundary_match(3)['h']):
            for alpha in (F(1,2),F(17,2),F(97,2)):
                v = T.exact_ou_resolvent_polynomial(h,alpha)
                p,dp = v['polynomial'],B.derivative(v['polynomial'])
                self.assertEqual(B.add(B.derivative(dp),B.scale(p,-alpha*alpha)),
                                 B.scale(h,-2*alpha))
                self.assertEqual(B.value(dp,-R.A)-alpha*B.value(p,-R.A)
                                 -2*alpha*v['left'],0)
                self.assertEqual(B.value(dp,R.A)+alpha*B.value(p,R.A)
                                 +2*alpha*v['right'],0)

    def test_endpoint_expansion_matches_full_resolvent_exactly(self):
        for i in range(1,5):
            h = R.high_boundary_match(i,F(1,100))['h']
            h2 = B.derivative(B.derivative(h))
            h3,h4 = B.derivative(h2),B.derivative(B.derivative(h2))
            for alpha in (F(7,2),F(33,2)):
                full = T.exact_ou_resolvent_polynomial(h,alpha)
                bulk = T.exact_ou_resolvent_polynomial(h4,alpha)
                expected = B.add(B.scale(h2,-2/alpha**3),
                                 B.scale(bulk['polynomial'],-1/alpha**4))
                actual = B.add(B.scale(h,2/alpha),B.scale(full['polynomial'],-1))
                self.assertEqual(actual,expected)
                left = B.value(h2,-R.A)/alpha**3-B.value(h3,-R.A)/alpha**4
                right = B.value(h2,R.A)/alpha**3+B.value(h3,R.A)/alpha**4
                self.assertEqual(-full['left'],left-bulk['left']/alpha**4)
                self.assertEqual(-full['right'],right-bulk['right']/alpha**4)
                # Mutating either authentic boundary orientation is observable.
                if B.value(h3,-R.A):
                    self.assertNotEqual(-full['left'],
                        B.value(h2,-R.A)/alpha**3+B.value(h3,-R.A)/alpha**4
                        -bulk['left']/alpha**4)

    def test_h2_endpoints_are_paid_not_silently_promoted_to_h4_zero(self):
        h = R.high_boundary_match(1)['h']
        v = T.gamma_tail_resolvent_bound(h,24)
        self.assertGreater(v['endpoint_second_derivative_error_upper'],0)
        self.assertGreater(v['endpoint_third_derivative_error_upper'],0)
        self.assertFalse(v['requires_zero_second_or_third_endpoint_traces'])
        self.assertLess(v['corrected_action_error_upper'],
                        v['uncorrected_parent_action_error_upper'])
        h4 = (F(1),)
        for _ in range(4):h4=B.mul(h4,(F(1),F(0),F(-4)))
        z = T.gamma_tail_resolvent_bound(h4,24)
        self.assertEqual(z['endpoint_second_derivative_error_upper'],0)
        self.assertEqual(z['endpoint_third_derivative_error_upper'],0)
        self.assertGreater(z['interior_fourth_derivative_error_upper'],0)

    def test_refinement_is_not_assumed_to_dominate_at_every_depth(self):
        v = T.gamma_tail_resolvent_bound(R.high_boundary_match(2)['h'],8)
        self.assertGreater(v['corrected_action_error_upper'],
                           v['uncorrected_parent_action_error_upper'])
        self.assertFalse(v['RH_proved'])

    def test_invalid_domains_and_shells_fail_closed(self):
        for h in ((F(1),),R.low_primitive(1),(1.0,)):
            with self.assertRaises((T.TailResolventError,R.OriginalResidualError)):
                T.gamma_tail_resolvent_bound(h,8)
        for J in (0,-1,True,2.0):
            with self.assertRaises(T.TailResolventError):
                T.tail_power_interval(J,3)
        with self.assertRaises(T.TailResolventError):T.tail_power_interval(8,1)
        with self.assertRaises(T.TailResolventError):T.finite_power_sum(8,8,3)
        with self.assertRaises(T.TailResolventError):
            T.source_tail_resolvent_schur_trial(8,fit='pretend_positive')

    def test_mutated_contact_halfdensity_or_source_sha_rejected(self):
        p = R.source_parameters()
        h = R.high_boundary_match(1)['h']
        for mutated in (dict(p,contact=p['contact']+1),dict(p,w=F(0)),
                        dict(p,real_gamma_count=2),dict(p,sha='false')):
            with self.assertRaises(T.TailResolventError):
                T.corrected_source_action(h,8,80,parameters=mutated)

    def test_fresh_unfitted_original_source_and_mutation_holdouts(self):
        v = T.independent_original_source_holdouts()
        self.assertEqual(v['frozen_source_git_blob'],R.SOURCE_SHA)
        self.assertEqual(v['heldout_Gamma_shell'],(13,23))
        self.assertTrue(v['full_signed_channels_intersect'])
        self.assertTrue(v['source_shell_intersects'])
        self.assertTrue(v['omitted_leading_Laplacian_mutant_disjoint'])
        self.assertTrue(v['reversed_leading_sign_mutant_disjoint'])
        self.assertFalse(v['RH_proved'])


if __name__=='__main__':unittest.main()
