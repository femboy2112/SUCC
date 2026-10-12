"""Exact source-matched positive laws and negative observer controls."""
import math
import random
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.logistic_observer_tree import (
    ObserverTreeError, Source, PrefixReceipt, TerminalReceipt,
    logistic, tent, inverse_tent_branch, cylinder, cylinder_mass,
    cylinders_at, symbolic_path, inverse_word, forward_uncertainty,
    join_observers, join_interval, transfer_polynomial, transfer_depth,
    equilibrium_mean, exact_completion_depth, arcsine_moment, chebyshev_mode,
    report_information, zero_lag_one_covariance_receipt,
    lipschitz_uniform_bound_pi_coefficient, period_two_bifurcation_receipt,
    forward_pullback_polynomial,
)


def eval_polynomial(coeff, x):
    return sum(float(c)*x**k for k,c in enumerate(coeff))


class TreeSourceTests(unittest.TestCase):
    def test_logistic_exact_rational_grounding(self):
        self.assertEqual(logistic(F(1,4)),F(3,4))
        self.assertEqual(logistic(F(3,4)),F(3,4))
        self.assertEqual(logistic(0),0)

    def test_origin_is_observer_record_not_logistic_zero(self):
        self.assertEqual(logistic(logistic(0)),0)  # exact fixed point, not chaos
        self.assertEqual(cylinder(()),(F(0),F(1)))

    def test_no_floating_point_proof_certificates(self):
        for call in (lambda:logistic(.2),lambda:tent(.2),
                     lambda:inverse_tent_branch(0,.2),
                     lambda:transfer_polynomial((1,0.5)),
                     lambda:join_interval(PrefixReceipt(Source('a',0),(0,)),
                         Source('a',0),1,0.25,F(3,4))):
            with self.assertRaises(ObserverTreeError):call()

    def test_source_and_version_checked(self):
        with self.assertRaises(ObserverTreeError):Source('a',-1)
        with self.assertRaises(ObserverTreeError):Source('',0)
        with self.assertRaises(ObserverTreeError):Source('a',False)
        a=Source('one',0)
        with self.assertRaises(ObserverTreeError):PrefixReceipt(a,(0,2))
        with self.assertRaises(ObserverTreeError):PrefixReceipt(a,(True,))

    def test_full_exact_partition_and_counting(self):
        for n in range(10):
            records=cylinders_at(n)
            self.assertEqual(len(records),1<<n)
            intervals=sorted(interval for word,interval in records)
            self.assertEqual(intervals[0][0],0)
            self.assertEqual(intervals[-1][1],1)
            self.assertEqual(sum((b-a for a,b in intervals),F(0)),1)
            self.assertEqual(sum((cylinder_mass(word) for word,_ in records),F(0)),1)
            self.assertTrue(all(b-a==F(1,2**n) for a,b in intervals))
            self.assertTrue(all(intervals[i][1]==intervals[i+1][0]
                                for i in range(len(intervals)-1)))

    def test_cylinder_direct_iterator_and_orbit_endpoints(self):
        for n in range(1,8):
            for bits in product((0,1),repeat=n):
                a,b=cylinder(bits)
                self.assertEqual(tuple(sorted((inverse_word(bits,0),inverse_word(bits,1)))),(a,b))
                for endpoint in (a,b):
                    x=endpoint
                    for _ in range(n):x=tent(x)
                    self.assertIn(x,(F(0),F(1)))

    def test_independent_actual_symbolic_itineraries(self):
        for n in range(1,10):
            for bits in product((0,1),repeat=n):
                # Center of cylinder strictly avoids all itinerary boundaries.
                a,b=cylinder(bits)
                midpoint=(a+b)/2
                self.assertEqual(symbolic_path(midpoint,n),bits)
        self.assertEqual(symbolic_path(F(1,5),6),(0,0,1,0,1,0))

    def test_critical_tie_explicitly_excluded(self):
        with self.assertRaisesRegex(ObserverTreeError,'Critical'):
            symbolic_path(F(1,2),1)
        with self.assertRaises(ObserverTreeError):symbolic_path(F(1,4),2)
        with self.assertRaises(ObserverTreeError):inverse_tent_branch(3,F(1,2))

    def test_exact_future_fiber_restoration(self):
        bs=(1,0,1,1,0)
        for t in range(0,len(bs)+4):
            expected=cylinder(bs[t:])
            self.assertEqual(forward_uncertainty(bs,t),expected)
            if t <= len(bs):
                a,b=cylinder(bs)
                x,y=a,b
                for _ in range(t):x,y=tent(x),tent(y)
                self.assertEqual(tuple(sorted((x,y))),expected)
        self.assertEqual(forward_uncertainty(bs,len(bs)),(0,1))

    def test_chaotic_state_half_is_not_deterministic_two_state_factor(self):
        a,b=F(1,8),F(3,8)
        self.assertEqual(symbolic_path(a,1),symbolic_path(b,1))
        self.assertNotEqual(symbolic_path(tent(a),1),symbolic_path(tent(b),1))

    def test_n_words_have_n_bits_no_data_free_compression(self):
        for n in range(13):
            for k in range(n+1):
                r=report_information(n,k)
                self.assertEqual(r['distinct_reports']*r['maximum_fiber'],2**n)
                self.assertEqual(r['report_entropy_bits']+r['unresolved_history_bits'],n)
                self.assertFalse(r['zero_entropy_dynamical_factor_proved'])
        with self.assertRaises(ObserverTreeError):report_information(4,5)


class DualObserverJoinTests(unittest.TestCase):
    def setUp(self):
        self.source=Source('one-physical-carrier',7)

    def test_joint_exact_reconstruction_is_source_and_time_typed(self):
        endpoint=F(2,7)
        for n in range(9):
            for bits in product((0,1),repeat=n):
                prefix=PrefixReceipt(self.source,bits)
                terminal=TerminalReceipt(self.source,n,endpoint)
                result=join_observers(prefix,terminal)
                a,b=cylinder(bits)
                self.assertTrue(a<result['theta_initial']<b)
                self.assertEqual(result['orbit'][0],inverse_word(bits,endpoint))
                self.assertEqual(result['orbit'][-1],endpoint)
                self.assertFalse(result['actual_physical_source_authenticated'])

    def test_ambiguous_endpoint_alone_has_two_preimages(self):
        y=F(1,3)
        l=join_observers(PrefixReceipt(self.source,(0,)),TerminalReceipt(self.source,1,y))
        r=join_observers(PrefixReceipt(self.source,(1,)),TerminalReceipt(self.source,1,y))
        self.assertEqual(tent(l['theta_initial']),tent(r['theta_initial']))
        self.assertNotEqual(l['theta_initial'],r['theta_initial'])
        self.assertEqual(l['theta_initial'],F(1,6))
        self.assertEqual(r['theta_initial'],F(5,6))

    def test_same_source_id_not_physical_authentication(self):
        # A forged branch report with the SAME metadata still glues to
        # the genuine endpoint, but selects a different predecessor.
        y=TerminalReceipt(self.source,1,F(1,3))
        a=join_observers(PrefixReceipt(self.source,(0,)),y)
        b=join_observers(PrefixReceipt(self.source,(1,)),y)
        self.assertEqual(a['endpoint'],b['endpoint'])
        self.assertNotEqual(a['theta_initial'],b['theta_initial'])
        self.assertFalse(a['actual_physical_source_authenticated'])
        self.assertFalse(b['actual_physical_source_authenticated'])

    def test_two_sided_completion_is_not_free_source_identity(self):
        p=PrefixReceipt(self.source,(0,1,0))
        y=TerminalReceipt(Source(self.source.name,8),3,F(1,3))
        with self.assertRaises(ObserverTreeError):join_observers(p,y)
        with self.assertRaises(ObserverTreeError):join_observers(
            p,TerminalReceipt(self.source,2,F(1,3)))
        with self.assertRaises(ObserverTreeError):TerminalReceipt(self.source,1,F(1))

    def test_endpoint_precision_contraction_exact(self):
        for n in range(1,11):
            bits=tuple((k*7)%2 for k in range(n))
            prefix=PrefixReceipt(self.source,bits)
            a,b=join_interval(prefix,self.source,n,F(1,4),F(3,4))
            self.assertEqual(b-a,F(1,2**(n+1)))
            self.assertTrue(cylinder(bits)[0]<=a<=b<=cylinder(bits)[1])

    def test_interval_source_and_geometry_mutants_rejected(self):
        p=PrefixReceipt(self.source,(0,1))
        for source,n,a,b in (
            (Source('forged',7),2,F(1,4),F(3,4)),
            (self.source,1,F(1,4),F(3,4)),
            (self.source,2,F(3,4),F(1,4)),
            (self.source,2,F(0),F(1,4)),
        ):
            with self.assertRaises(ObserverTreeError):join_interval(p,source,n,a,b)


class PolynomialInverseTreeTests(unittest.TestCase):
    def test_source_inverse_pair_exact_polynomial(self):
        self.assertEqual(transfer_polynomial((0,1)),(F(1,2),))
        self.assertEqual(transfer_polynomial((0,0,1)),(F(1,2),F(-1,4)))
        self.assertEqual(transfer_depth((0,0,1),2),(F(3,8),))
        self.assertEqual(transfer_depth((0,0,0,1),2),(F(5,16),))

    def test_depth_and_moments_to_degree_64(self):
        for deg in range(65):
            poly=(0,)*deg+(1,)
            enough=exact_completion_depth(poly)
            self.assertEqual(transfer_depth(poly,enough),(arcsine_moment(deg),))
            self.assertEqual(equilibrium_mean(poly),arcsine_moment(deg))
            if deg > 1:
                self.assertLess(len(transfer_depth(poly,enough-1)),deg+1)

    def test_random_source_polynomials_exact_and_sufficient_depth(self):
        r=random.Random(17012026)
        for _ in range(400):
            deg=r.randint(0,24)
            poly=tuple(r.randint(-4,4) for i in range(deg))+(r.choice((-3,-2,-1,1,2,3)),)
            n=exact_completion_depth(poly)
            self.assertEqual(transfer_depth(poly,n),(equilibrium_mean(poly),))
            self.assertEqual(transfer_depth(poly,n+3),(equilibrium_mean(poly),))

    def test_chebyshev_even_halving_odd_annihilation(self):
        for k in range(0,50):
            got=transfer_polynomial(chebyshev_mode(k))
            want=chebyshev_mode(k//2) if k%2==0 else (F(0),)
            self.assertEqual(got,want)
            if k:
                self.assertEqual(transfer_depth(chebyshev_mode(k),k.bit_length()),(F(0),))

    def test_completion_depth_sharp_for_power_of_two_modes(self):
        for j in range(8):
            k=2**j
            p=chebyshev_mode(k)
            self.assertEqual(transfer_depth(p,j),chebyshev_mode(1))
            self.assertEqual(transfer_depth(p,j+1),(F(0),))

    def test_degree_halving_exact_all_positive_monomials(self):
        for deg in range(0,61):
            p=(0,)*deg+(1,)
            self.assertLessEqual(len(transfer_polynomial(p))-1,deg//2)

    def test_inverse_branch_direct_numeric_holds_out_on_mutated_roots(self):
        # This is a *diagnostic* independent of the exact rational power-sum code.
        for y in (0.0,0.17,0.41,0.73,1.0):
            u=(1-math.sqrt(1-y))/2
            v=(1+math.sqrt(1-y))/2
            for k in range(0,17):
                predicted=eval_polynomial(transfer_polynomial((0,)*k+(1,)),y)
                direct=(u**k+v**k)/2
                self.assertAlmostEqual(predicted,direct,places=10)

    def test_depth_complete_tree_numeric_conjugacy_with_symbolic_routes(self):
        # Distinct derivation from rational inverse tent branches and h(theta).
        future_theta=F(1,3)
        y=math.sin(math.pi*float(future_theta)/2)**2
        for n in range(1,9):
            for k in range(0,8):
                averaged=sum(
                    math.sin(math.pi*float(inverse_word(word,future_theta))/2)**(2*k)
                    for word in product((0,1),repeat=n)
                )/2**n
                predicted=eval_polynomial(transfer_depth((0,)*k+(1,),n),y)
                self.assertAlmostEqual(averaged,predicted,places=10)

    def test_arcsine_covariance_zero_but_dynamics_not_independent(self):
        r=zero_lag_one_covariance_receipt()
        self.assertEqual((r['E_x'],r['E_x_squared'],r['E_x_cubed']),
                         (F(1,2),F(3,8),F(5,16)))
        self.assertEqual(r['covariance'],0)
        self.assertEqual(logistic(F(1,3)),F(8,9))
        self.assertFalse(r['statistical_independence_inferred'])

    def test_conditional_variance_refutes_lossless_algebra_quotient(self):
        lx=transfer_polynomial((0,1))
        lx2=transfer_polynomial((0,0,1))
        self.assertEqual(lx,(F(1,2),))
        self.assertEqual(lx2,(F(1,2),F(-1,4)))
        self.assertNotEqual(lx2,(lx[0]**2,))
        self.assertEqual(lx2[0]-lx[0]**2,F(1,4))

    def test_one_missing_or_biased_branch_breaks_aggregate_invariant(self):
        # At y=0: two predecessors are x=0 and x=1; average is 1/2.
        self.assertEqual(logistic(0),logistic(1))
        self.assertEqual((F(0)+F(1))/2,F(1,2))
        self.assertNotEqual(F(0),F(1,2))  # one missing branch
        self.assertNotEqual(F(3,4)*0+F(1,4)*1,F(1,2))

    def test_approximate_inverse_semantics_noncritical_r_cannot_inherit_full_tree(self):
        # At r=16/5, max f_r(x)=4/5; frontier y=9/10 has no real predecessor.
        r=F(16,5)
        y=F(9,10)
        self.assertGreater(y,r/4)
        self.assertEqual(logistic(F(1,2)),1)


    def test_inverse_transfer_is_left_inverse_to_forward_koopman(self):
        r=random.Random(271828)
        for _ in range(80):
            g=tuple(r.randint(-3,3) for i in range(4))
            self.assertEqual(transfer_polynomial(forward_pullback_polynomial(g,1)),
                             transfer_depth(g,0))

    def test_moving_frontier_rate_matches_the_entire_tree(self):
        # Uniform finite completion of FIXED targets survives; a frontier
        # observable whose polynomial degree doubles every step resists
        # the depth-n averaging at every finite n.
        for n in range(7):
            front=forward_pullback_polynomial((0,1),n)
            self.assertEqual(len(front)-1,2**n)
            self.assertEqual(transfer_depth(front,n),(F(0),F(1)))
            self.assertEqual(transfer_depth(front,n+1),(F(1,2),))
            self.assertEqual(forward_pullback_polynomial(chebyshev_mode(1),n),
                             chebyshev_mode(2**n))

    def test_certified_lipschitz_uniform_bound_declared_in_pi_units(self):
        for n in range(12):
            self.assertEqual(lipschitz_uniform_bound_pi_coefficient(n,1),F(1,2**(n+2)))
        with self.assertRaises(ObserverTreeError):
            lipschitz_uniform_bound_pi_coefficient(1,F(-1))
        with self.assertRaises(ObserverTreeError):
            lipschitz_uniform_bound_pi_coefficient(1,0.1)

    def test_rational_bifurcation_period_two_positive_and_hostile_controls(self):
        stable=period_two_bifurcation_receipt(F(16,5))
        self.assertEqual(stable['center'],F(21,32))
        self.assertEqual(stable['radius_square'],F(21,1024))
        self.assertEqual(stable['period_two_derivative_multiplier'],F(4,25))
        self.assertTrue(stable['period_two_attracting'])
        unstable=period_two_bifurcation_receipt(4)
        self.assertEqual(unstable['period_two_derivative_multiplier'],-4)
        self.assertFalse(unstable['period_two_attracting'])
        self.assertFalse(unstable['validates_all_parameter_windows'])
        with self.assertRaises(ObserverTreeError):
            period_two_bifurcation_receipt(3)

    def test_bad_polynomial_and_invalid_depth_mutants(self):
        for fn in (lambda:transfer_polynomial(()),
                   lambda:transfer_depth((1,),-1),
                   lambda:arcsine_moment(-1),
                   lambda:chebyshev_mode(-1),
                   lambda:equilibrium_mean((F(1),0.1))):
            with self.assertRaises(ObserverTreeError):fn()

if __name__=='__main__': unittest.main()
