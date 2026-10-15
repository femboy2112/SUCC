"""APOLLO: source-authentic second and third distributional jet checks."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.one_object_transport import (
    OneObjectError, contact_rational_increment, anchored_kernel
)
from observational_succ.apollo_derivative_jets import (
    quadratic_gauge_kernel_shift, second_derivative_gauge_shift,
    third_derivative_gauge_shift, exact_source_gauge_negative_direction,
    genuine_prime_third_jet, true_third_prime_wavefronts,
    third_origin_contact_offset, cubic_gauge_discrimination,
    polynomial_derivative, polynomial_moment, repeated_compact_primitive,
    compact_polynomial_moment_certificate,
    third_distribution_bump_pair, exact_local_gamma_slope_bound,
)


class ApolloThirdGaugeTheorems(unittest.TestCase):
    def test_quadratic_gauge_rank_one_exact_all_rational(self):
        base=lambda t:-t*t
        for c,x,y in product((Q(-3,2),Q(0),Q(1,7),Q(9)),
                             (Q(-2),Q(1,4),Q(2)),
                             (Q(-1,3),Q(1),Q(3))):
            mutated=lambda t:base(t)+c*t*t
            delta=anchored_kernel(mutated,x,y)-anchored_kernel(base,x,y)
            self.assertEqual(delta,quadratic_gauge_kernel_shift(c,x,y))
            self.assertEqual(second_derivative_gauge_shift(c),-2*c)
            self.assertEqual(third_derivative_gauge_shift(c),0)

    def test_third_observer_cannot_see_authentic_negative_gauge(self):
        item=exact_source_gauge_negative_direction(Q(1,4),64,128)
        self.assertTrue(item["strict_negative_mutant_certified"])
        self.assertLess(item["mutant_interval"][1],0)
        self.assertEqual(item["original_interval"][0]>0,True)
        self.assertFalse(item["source_authentic_mutant"])
        self.assertTrue(item["third_derivative_unchanged"])
        self.assertFalse(item["RH_proved"])

    def test_nonzero_mass_anchors_quadratic_mode_without_conflating_contact(self):
        for c,m in product((Q(-7),Q(0),Q(1,3),Q(8)),(Q(-2),Q(1,2),Q(3))):
            item=cubic_gauge_discrimination(m,c)
            self.assertEqual(item["third_source_difference"],0)
            self.assertEqual(item["source_Weil_pairing_difference"],-2*c*m)
            self.assertEqual(item["quadratic_gauge_fixed_if_pairing_equal"],c==0)
            self.assertTrue(item["source_contact_delta_not_equivalent_to_constant_mode"])
        with self.assertRaises(OneObjectError):
            cubic_gauge_discrimination(0,1)


class ApolloPrimeWavefronts(unittest.TestCase):
    def test_original_prime_jets_are_exact_SHA_pinned(self):
        for n,p,k in ((2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),
                      (8,2,3),(9,3,2),(16,2,4),(27,3,3),(49,7,2)):
            j=genuine_prime_third_jet(n)
            self.assertEqual((j.n,j.p,j.exponent),(n,p,k))
            self.assertLess(j.log_n_interval[0],j.log_n_interval[1])
            self.assertGreater(j.delta_prime_weight_interval[0],0)
            self.assertTrue(j.authentic_source)

    def test_fake_composites_and_wrong_inputs_refused(self):
        for n in (6,10,12,14,15,18,20,21,30):
            with self.subTest(n=n),self.assertRaises(OneObjectError):
                genuine_prime_third_jet(n)
        for n in (0,1,129,True,2.0):
            with self.assertRaises(OneObjectError):
                genuine_prime_third_jet(n)

    def test_rational_cutoffs_exact_enclosed(self):
        self.assertEqual(true_third_prime_wavefronts(Q(1,2)),())
        self.assertEqual(tuple(j.n for j in true_third_prime_wavefronts(1)),(2,))
        self.assertEqual(tuple(j.n for j in true_third_prime_wavefronts(2)),
                         (2,3,4,5,7))
        for bad in (-1,0,5,True,1.5):
            with self.assertRaises(OneObjectError):
                true_third_prime_wavefronts(bad)

    def test_exact_origin_delta_prime_counterterm(self):
        self.assertEqual(third_origin_contact_offset(0),0)
        self.assertEqual(third_origin_contact_offset(1),-2)
        for J in range(1,40):
            self.assertEqual(third_origin_contact_offset(J),
                             contact_rational_increment(J)
                             -sum((Q(4,4*j+1) for j in range(J)),Q()))
            self.assertLess(third_origin_contact_offset(J+1),
                            third_origin_contact_offset(J))


class ApolloMomentRangeTests(unittest.TestCase):
    def test_compact_derivative_moment_nulls_and_first_nonzero(self):
        for m,power in product((1,2,3),(7,8,10)):
            d=compact_polynomial_moment_certificate(m,power)
            self.assertEqual(d["moment_nulls"],tuple(Q() for _ in range(m)))
            self.assertNotEqual(d["first_nonzero_moment"],0)
            self.assertTrue(d["primitive_recovered"])
            self.assertEqual(d["unobserved_moment_dimension"],m)
            self.assertFalse(d["finite_polynomial_test_is_Cc_infinity"])
            self.assertFalse(d["RH_proved"])

    def test_known_integral_and_derivative(self):
        self.assertEqual(polynomial_moment((Q(1),Q(2)),0),2)
        self.assertEqual(polynomial_moment((Q(1),Q(2)),1),Q(7,6))
        self.assertEqual(polynomial_derivative((Q(3),Q(4),Q(5)),2),(Q(10),))
        self.assertEqual(repeated_compact_primitive((Q(6),),2),
                         (Q(0),Q(0),Q(3)))
        for bad in (True,-1,4,0):
            with self.assertRaises(OneObjectError):
                compact_polynomial_moment_certificate(bad)


class ApolloSourceDistributionalThirdTests(unittest.TestCase):
    def test_third_distribution_weil_vs_suzuki_9_holdouts(self):
        from mpmath import mp
        for radius,j in product((Q(1,2),Q(1),Q(2)),(0,2,6)):
            datum=third_distribution_bump_pair(radius,j,65)
            self.assertLess(datum["residual_abs"],mp.mpf("1e-43"))
            self.assertFalse(datum["all_test_Weil_positive"])
            self.assertFalse(datum["RH_proved"])
            self.assertEqual(tuple(x.n for x in true_third_prime_wavefronts(radius)),
                             datum["source_prime_labels"])

    def test_contact_at_origin_delta_prime_detected(self):
        from mpmath import mp
        for j in (0,3,8):
            good=third_distribution_bump_pair(1,j,65)
            bad=third_distribution_bump_pair(1,j,65,Q(2,7))
            self.assertLess(good["residual_abs"],mp.mpf("1e-43"))
            self.assertLess(abs(bad["residual_abs"]-mp.mpf(2)/7),
                            mp.mpf("1e-43"))
            self.assertTrue(bad["origin_contact_detected"])

    def test_full_gamma_slope_identity_and_geometric_tail(self):
        from mpmath import mp
        for radius,j in product((Q(1,8),Q(1,2),Q(1),Q(2)),(2,8,32)):
            o=exact_local_gamma_slope_bound(radius,j,75)
            self.assertLess(o["absolute_error"],
                            o["analytic_tail_evaluation"]+mp.mpf("1e-65"))
            self.assertFalse(o["numerical_rounding_certified"])
        for bad in (0,-1,Q(5),True):
            with self.assertRaises(OneObjectError):
                exact_local_gamma_slope_bound(bad,3)

    def test_bad_high_derivative_domains_rejected(self):
        for r,J in ((0,2),(Q(1),65),(Q(5),0),(True,1)):
            with self.assertRaises(OneObjectError):
                third_distribution_bump_pair(r,J)


if __name__=="__main__":
    unittest.main()
