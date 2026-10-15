"""APOLLO true Euler-active Weil domain theorem, original SHA source and controls."""
import unittest
from fractions import Fraction as F

from observational_succ.apollo_prime_domain import (
    PrimeDomainError,
    FIRST_SPARSE_MEASURE,ALL_FIVE_SPARSE_MEASURE,
    gamma_sixteen_fraction,dyadic_gamma_4096_lower,
    first_prime_sparse_domain,prime_two_pair_packet_domain,
    full_five_source_a_one_sparse_domain,
    any_five_prime_activation_pair,isolated_prime_sixteen_packet,
    exact_packet_overlap_bump,
    synthetic_sparse_budget,source_support_union_gate,
    prime_packet_low_moment_rank,
)
from observational_succ.apollo_derivative_jets import genuine_prime_third_jet
from observational_succ.apollo_krein_factor import (
    authentic_sharp_small_window_hilbert_factor,
)


class FirstActualPrimeActiveSparseDomainTests(unittest.TestCase):
    def test_sixteen_real_gamma_rational_source_and_general_support_budget(self):
        S16=sum((F(4,4*j+1) for j in range(16)),F())
        self.assertEqual(gamma_sixteen_fraction(),S16)
        self.assertGreater(S16-16*F(1,32)-F(43,8)-1-F(1,128), F(1,10))
        for m in (F(1,64),F(1,128),F(1,50),FIRST_SPARSE_MEASURE):
            item=first_prime_sparse_domain(m)
            self.assertEqual(item.active_prime_labels,(2,))
            self.assertEqual(item.ambient_halfwidth,F(1,2))
            self.assertEqual(item.support_measure_upper,m)
            self.assertEqual(item.gamma_mode_count,16)
            self.assertGreater(item.strict_rational_lower,F(1,10))
            self.assertEqual(item.uniform_weil_l2_floor,F(1,10))
            self.assertTrue(item.conditional_on_measured_support)
            self.assertTrue(item.all_tests_in_domain)
            self.assertTrue(item.h01_test_domain_extension_by_continuity)
            self.assertFalse(item.bounded_operator_on_all_L2_claimed)
            self.assertFalse(item.full_ambient_weil_positivity_proved)
            self.assertFalse(item.RH_proved)

    def test_exact_two_packet_prime2_active_domain_with_nonzero_transfer(self):
        p=prime_two_pair_packet_domain()
        self.assertEqual(p["union_measure"],F(1,32))
        self.assertEqual(p["Gamma_rungs"],16)
        self.assertEqual(p["exact_prime_overlap_upper_ratio"],F(1,2))
        self.assertGreater(p["all_test_Q_over_L2_strict_rational_lower"],F(3,5))
        self.assertEqual(p["uniform_weil_L2_lower"],F(3,5))
        self.assertTrue(p["nonzero_prime_transfer_possible"])
        self.assertTrue(p["valid_for_every_complex_Cc_infinity_test_on_fixed_E"])
        self.assertFalse(p["PR107_original_low_short_sign_proved"])
        self.assertGreater(p["actual_prime_shift_interval"][0],F(2,3))
        self.assertLess(p["actual_prime_shift_interval"][1],F(7,10))
        self.assertLess(p["right_U_endpoint_intervals"][1][1],F(1,2))
        self.assertGreater(p["right_U_endpoint_intervals"][0][0],F(0))
        self.assertTrue(genuine_prime_third_jet(2).authentic_source)

    def test_prime_activity_is_a_real_source_perturbation_not_fake_covariance(self):
        # A deliberately DOUBLED primitive impulse violates strict source upper.
        authentic=first_prime_sparse_domain()
        fake=synthetic_sparse_budget(16,F(1,32),F(43,8),F(2),F(1,128))
        self.assertGreater(authentic.strict_rational_lower,F(1,10))
        self.assertLess(fake["candidate_lower"],0)
        self.assertFalse(fake["candidate_positive"])
        self.assertFalse(fake["original_source_authenticated"])
        # Missing the critical sixteenth Gamma rung loses the >1/10 margin.
        omitted=synthetic_sparse_budget(15,F(1,32),F(43,8),F(1),F(1,128))
        self.assertLess(omitted["candidate_lower"],F(1,10))
        self.assertFalse(omitted["original_source_authenticated"])

    def test_support_domain_refuses_broad_and_untyped_requests(self):
        for m in (F(1,16),0,-1,True,0.03,"1/64"):
            with self.subTest(m=m),self.assertRaises(PrimeDomainError):
                first_prime_sparse_domain(m)
        for J,m,C,pole,prime in (
            (0,F(1,32),F(1),F(1),F(1)),
            (16,F(1,32),F(1),F(1),F(-1)),
            (True,F(1,32),F(1),F(1),F(1)),
        ):
            with self.assertRaises(PrimeDomainError):
                synthetic_sparse_budget(J,m,C,prime,pole)


class FiveRealPrimePowerSparseDomainTests(unittest.TestCase):
    def test_full_true_prime_active_source_budget_a_le_one(self):
        # The EXACT dyadic block bound, not a sampled 4096-rung spectrum.
        s16=gamma_sixteen_fraction()
        exact_lower=s16+8*F(2,3)-sum((F(1,4*2**k) for k in range(4,12)),F())
        self.assertEqual(dyadic_gamma_4096_lower(),exact_lower)
        self.assertGreater(exact_lower,F(12))
        for m in (F(1,32768),ALL_FIVE_SPARSE_MEASURE):
            c=full_five_source_a_one_sparse_domain(m)
            self.assertEqual(c.ambient_halfwidth,F(1))
            self.assertEqual(c.active_prime_labels,(2,3,4,5,7))
            self.assertEqual(c.gamma_mode_count,4096)
            self.assertGreater(c.strict_rational_lower,F(1,2))
            self.assertEqual(c.uniform_weil_l2_floor,F(1,2))
            self.assertTrue(c.all_tests_in_domain)
            self.assertFalse(c.full_ambient_weil_positivity_proved)
            self.assertFalse(c.RH_proved)
        strict=exact_lower-4096*F(1,16384)-F(43,8)-2*F(73,24)-2*F(1,16384)
        self.assertGreater(strict,F(1,2))

    def test_each_of_all_five_original_arithmetic_waves_can_act_on_its_packet_domain(self):
        for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7)):
            c=any_five_prime_activation_pair(n)
            self.assertEqual(c["active_prime_power"],n)
            self.assertEqual(c["original_primitive_prime"],p)
            self.assertEqual(c["only_matching_prime_overlap"],n)
            self.assertTrue(c["all_other_prime_transfer_zero"])
            self.assertEqual(c["L2_pairwise_overlap_ratio_upper"],F(1,2))
            self.assertGreater(c["strict_exact_margin"],F(5))
            self.assertEqual(c["true_source_Weil_L2_lower"],F(5))
            self.assertEqual(c["support_measure_upper"],F(1,16384))
            self.assertTrue(c["source_derived_Hilbert_contraction_on_linear_test_domain"])
            self.assertFalse(c["point_kernel_Gram_positive_on_all_of_minus1_to1"])
            self.assertFalse(c["RH_proved"])
            self.assertGreater(c["translated_endpoint_intervals"][0][0],F(-1))
            self.assertLess(c["translated_endpoint_intervals"][1][1],F(1))
            self.assertTrue(genuine_prime_third_jet(n).authentic_source)

    def test_nonEuler_fake6_mutant_is_not_admissible_on_the_source_domain(self):
        for invalid in (6,8,9,10,1,0,-3,True):
            with self.assertRaises(PrimeDomainError):
                any_five_prime_activation_pair(invalid)
        for width in (F(1,64),F(1,100),0,True,0.00001):
            with self.assertRaises(PrimeDomainError):
                any_five_prime_activation_pair(2,width)

    def test_a_one_domain_budget_rejects_unsupported_support_measure(self):
        for m in (F(1,8192),F(1,10000),0,-1,True,0.00001):
            with self.assertRaises(PrimeDomainError):
                full_five_source_a_one_sparse_domain(m)


class SignedWeilPacketPolynomialsAndPR107InterfaceTests(unittest.TestCase):
    def test_exact_beta_norm_and_prime_transfer_ratio_independent_of_logarithm(self):
        for width in (F(1,64),F(1,32768)):
            for exponent in (4,5,8):
                o=exact_packet_overlap_bump(width,exponent)
                self.assertGreater(o["one_packet_exact_L2"],0)
                self.assertEqual(o["two_packet_exact_L2"],2*o["one_packet_exact_L2"])
                self.assertEqual(o["one_prime_translated_overlap"],o["one_packet_exact_L2"])
                self.assertEqual(o["relative_prime_overlap"],F(1,2))
                self.assertFalse(o["finite_polynomial_is_Cc_infinity"])
                self.assertTrue(o["smooth_equal_translate_witness_exists"])

    def test_original_first_prime_shorting_domain_uses_neumann_not_unweighted_metric(self):
        # Exact original-source DOMAIN comparison with PR #107, not an import
        # or mathematical claim that its still-unverified low Schur has sign.
        first=prime_two_pair_packet_domain()
        self.assertIn("Neumann K=V*V",first["PR107_comparison_metric"])
        self.assertIn("L2_zero",first["PR107_ambient_operator"])
        self.assertGreater(first["uniform_weil_L2_lower"],F(369,10000))
        self.assertFalse(first["PR107_original_low_short_sign_proved"])
        earlier=authentic_sharp_small_window_hilbert_factor(F(1,12))
        self.assertTrue(earlier["positive_feature_Psi_a_exists_by_completion"])
        self.assertFalse(earlier["all_a_and_RH_proved"])

    def test_original_prime_pair_and_synthetic_noncommuting_sum_no_go(self):
        # Relative positive diagonals do not determine an off-diagonal sign:
        # exact rational [[1,-2],[-2,1]] is indefinite despite both axes >0.
        A=((F(1),F(-2)),(F(-2),F(1)))
        self.assertGreater(A[0][0],0)
        self.assertGreater(A[1][1],0)
        self.assertLess(A[0][0]*A[1][1]-A[0][1]**2,0)
        for bad in (0,F(1,2),True,0.0125):
            with self.assertRaises(PrimeDomainError):
                exact_packet_overlap_bump(bad)



class SixteenGammaModeAuthenticIsolatedPrimeDomains(unittest.TestCase):
    def test_all_five_genuine_prime_wavefronts_with_broader_support(self):
        for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7)):
            d=isolated_prime_sixteen_packet(n)
            self.assertEqual(d["active_original_prime_power"],n)
            self.assertEqual(d["primitive_prime"],p)
            self.assertEqual(d["Gamma_modes"],16)
            self.assertEqual(d["halfwidth"],F(1))
            self.assertEqual(d["support_measure_upper"],F(1,64))
            self.assertEqual(d["half_shift_overlap_norm_ratio"],F(1,2))
            self.assertTrue(d["isolated_wavefront"])
            self.assertTrue(d["other_four_prime_overlaps_exactly_zero"])
            self.assertGreater(d["strict_rational_margin"],F(1,2))
            self.assertTrue(d["source_positive_Hilbert_contraction_exists_on_CcE"])
            self.assertFalse(d["full_ambient_G_a_positive"])
            self.assertFalse(d["RH_proved"])
        # Compare to the more restrictive 4096-mode point carrier:
        self.assertLess(isolated_prime_sixteen_packet(7)["strict_rational_margin"],
                        any_five_prime_activation_pair(7)["strict_exact_margin"])

    def test_isolated_packet_budget_controls(self):
        for length in (F(1,128),F(1,256),F(1,1024)):
            d=isolated_prime_sixteen_packet(7,length)
            self.assertEqual(d["support_measure_upper"],2*length)
            self.assertGreater(d["strict_rational_margin"],F(1,2))
        for n in (6,8,0,1,True):
            with self.assertRaises(PrimeDomainError):
                isolated_prime_sixteen_packet(n)
        for length in (F(1,64),F(0),True,0.005):
            with self.assertRaises(PrimeDomainError):
                isolated_prime_sixteen_packet(2,length)



class ApolloGluingAndLowMomentDomainGuards(unittest.TestCase):
    def test_exact_source_measure_union_keeps_all_cross_terms(self):
        c=source_support_union_gate(F(1,2),(F(1,64),F(1,64)))
        self.assertEqual(c["union_bound"],F(1,32))
        self.assertEqual(c["source_certified_signed_Weil_L2_floor"],F(1,10))
        self.assertTrue(c["all_cross_terms_covered_by_source_budget"])
        self.assertTrue(c["componentwise_positivity_alone_would_be_insufficient"])
        d=source_support_union_gate(F(1),(F(1,32768),F(1,32768)))
        self.assertEqual(d["union_bound"],F(1,16384))
        self.assertEqual(d["source_certified_signed_Weil_L2_floor"],F(1,2))
        self.assertFalse(d["original_Weil_global_sign_proved"])

    def test_too_large_union_is_unverified_not_a_negative_source_witness(self):
        for a,parts in (
            (F(1,2),(F(1,32),F(1,32))),
            (F(1),(F(1,16384),F(1,16384))),
            (F(1,2),(F(1,64),F(1,32))),
        ):
            with self.assertRaises(PrimeDomainError):
                source_support_union_gate(a,parts)
        for a,parts in (
            (F(2), (F(1,32),)),
            (F(1,2),(0,)),
            (F(1,2),(True,)),
            (F(1,2),()),
        ):
            with self.assertRaises(PrimeDomainError):
                source_support_union_gate(a,parts)

    def test_exact_vandermonde_all_30_low_moments_reachable_without_sign_claim(self):
        for r in (1,2,5,12,30):
            c=prime_packet_low_moment_rank(2,r)
            self.assertEqual(c["moment_rank"],r)
            self.assertEqual(len(c["strict_rational_nodes"]),r)
            self.assertTrue(c["Vandermonde_determinant_positive"])
            self.assertGreater(c["Vandermonde_determinant"],0)
            self.assertTrue(c["true_Cc_infinity_moment_map_surjective"])
            self.assertTrue(c["Legendre_1_to_rank_projection_of_u_i_fprime_surjective"])
            self.assertFalse(c["uniform_inverse_moment_norm_bound_supplied"])
            self.assertFalse(c["original_Legendre_low_Schur_sign_proved"])
            self.assertFalse(c["RH_proved"])
        for n,r in ((6,30),(2,0),(2,31),(True,30),(2,3.0)):
            with self.assertRaises(PrimeDomainError):
                prime_packet_low_moment_rank(n,r)
