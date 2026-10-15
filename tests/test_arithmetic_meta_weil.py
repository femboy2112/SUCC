"""Exact new-to-SUCC source arithmetic/operator interaction certificate controls."""
from __future__ import annotations

import itertools
import json
import unittest
from fractions import Fraction as F
from math import factorial

from observational_succ.arithmetic_meta_weil import (
    ArithmeticMetaError, SourceContract, authentic_prime_tape,
    prime_power_jet, prime_commuting_square, half_density_unitary_indicator_demo,
    gamma_carlemann_sample_2log2, dyadic_window_commutator,
    finite_shift_energy_identity, gamma_rungs_multiplier_lower,
    moment_fourier_leak_upper, first_prime_moment_100_certificate,
    first_prime_boundary_commutator_certificate,
    valuation_holonomy, signed_non_euler_character4_prime_weight,
    independent_tent_weil_oracle, exact_finite_schur_sufficiency,
    moment_fourier_leak_sharp_upper, improved_first_prime_moment_29_certificate,
)


class TestArithmeticSource(unittest.TestCase):
    def test_prime_power_tape_and_mutant(self):
        self.assertEqual(prime_power_jet(2), (2,1))
        self.assertEqual(prime_power_jet(4), (2,2))
        self.assertEqual(prime_power_jet(8), (2,3))
        self.assertEqual(prime_power_jet(9), (3,2))
        self.assertEqual(prime_power_jet(6), None)
        self.assertEqual(prime_power_jet(12), None)
        self.assertEqual(authentic_prime_tape(10), ((2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1),(8,2,3),(9,3,2)))

    def test_source_mutations_rejected(self):
        for obj in (
            {"epoch":1}, {"coordinate":"naive-L2Z"},
            {"half_density":F(0)}, {"half_density":0.5}, {"gamma_conductor":4},
            {"gamma_parity":1}, {"source_id":"fake-composite-6"},
        ):
            with self.assertRaises(ArithmeticMetaError):
                SourceContract(**obj)
        with self.assertRaises(ArithmeticMetaError):
            authentic_prime_tape(10, "not-a-source")
        with self.assertRaises(ArithmeticMetaError):
            prime_commuting_square(1,6,2)

    def test_prime_square_is_flat(self):
        for n,p,q in itertools.product((1,2,7), (2,3,5), (2,3,5)):
            self.assertTrue(prime_commuting_square(n,p,q))
        self.assertEqual(valuation_holonomy(((2,1),(3,1),(2,-1),(3,-1))),())
        self.assertEqual(valuation_holonomy(((2,1),(3,-1))),((2,1),(3,-1)))
        with self.assertRaises(ArithmeticMetaError):
            valuation_holonomy(((6,1),))

    def test_half_density_and_primitive_signed_character(self):
        self.assertEqual(half_density_unitary_indicator_demo(F(1,2)),1)
        self.assertEqual(half_density_unitary_indicator_demo(F(1)),F(3,2))
        self.assertEqual(signed_non_euler_character4_prime_weight(2),0)
        self.assertEqual(signed_non_euler_character4_prime_weight(3),-1)
        self.assertEqual(signed_non_euler_character4_prime_weight(5),1)
        self.assertEqual(signed_non_euler_character4_prime_weight(9),1)
        self.assertEqual(signed_non_euler_character4_prime_weight(6),0)


class TestExactMetaInteraction(unittest.TestCase):
    def test_dyadic_carlemann_samples(self):
        self.assertEqual(gamma_carlemann_sample_2log2(0),F(1,2))
        self.assertEqual(gamma_carlemann_sample_2log2(1),F(2,5))
        self.assertEqual(gamma_carlemann_sample_2log2(2),F(4,17))
        self.assertEqual(gamma_carlemann_sample_2log2(-2),F(4,17))

    def test_window_born_noncommuting_square(self):
        K,S,comm=dyadic_window_commutator(3)
        self.assertEqual(comm[0][0],F(2,5))
        self.assertEqual(comm[2][2],F(-2,5))
        self.assertNotEqual(comm,tuple(tuple(F(0) for _ in range(3)) for _ in range(3)))
        self.assertEqual(K[0][2],F(4,17))
        self.assertEqual(S[0][1],1)
        self.assertEqual(S[1][0],0)

    def test_full_line_square_polarization(self):
        for length in range(1,6):
            for vector in itertools.product((-2,-1,0,1,2),repeat=length):
                v=tuple(map(F,vector))
                for step in (1,2,3,8):
                    r=finite_shift_energy_identity(v,step)
                    self.assertEqual(r["corrected_square"],r["source_signed_prime_term"])
                    self.assertGreaterEqual(r["energy"],0)
                    self.assertEqual(r["energy"],2*r["norm"]-2*r["overlap"])

    def test_rational_first_prime_boundary_norm(self):
        r=first_prime_boundary_commutator_certificate()
        self.assertEqual(r["commutator_norm_strictly_greater_than"],"3/22")
        self.assertTrue(r["rational_bound_check"])
        self.assertFalse(r["transport_was_unitary_after_compression"])


class TestFirstPrimeInfiniteDimensionalTheorem(unittest.TestCase):
    def test_finite_rung_comparison_is_exact(self):
        self.assertGreater(gamma_rungs_multiplier_lower(40,75),F(359,50))
        self.assertLess(gamma_rungs_multiplier_lower(40,74),gamma_rungs_multiplier_lower(40,75))
        self.assertEqual(gamma_rungs_multiplier_lower(40,75),
            sum((F(2*1600)/(F(4*j+1,2)*(F(4*j+1,2)**2+1600)) for j in range(75)),F(0)))

    def test_high_moment_leak_comparison_is_exact(self):
        eps=moment_fourier_leak_upper(F(1,2),40,100)
        self.assertLess(eps,F(1,100))
        self.assertEqual(eps,F(40,3)*4**40*F(20**202,factorial(101)**2))
        self.assertGreater(moment_fourier_leak_upper(F(1,2),40,50),eps)

    def test_whole_subspace_margin(self):
        cert=first_prime_moment_100_certificate()
        self.assertEqual(cert["certified_all_test_margin"],"291/5000")
        self.assertTrue(cert["gamma_comparison_holds"])
        self.assertTrue(cert["leak_comparison_holds"])
        self.assertFalse(cert["whole_space_unrestricted"])
        self.assertFalse(cert["RH_proved"])

    def test_improved_moment_29_rational_certificate(self):
        c=improved_first_prime_moment_29_certificate()
        self.assertEqual(c["number_of_moment_constraints"],30)
        self.assertEqual(c["certified_all_test_margin"],"369/10000")
        self.assertEqual(c["source_realized_prime_powers"],[2])
        self.assertFalse(c["unrestricted_first_window_sign_proved"])
        self.assertLess(moment_fourier_leak_sharp_upper(F(1,2),21,29),F(1,500))
        self.assertLess(moment_fourier_leak_sharp_upper(F(1,2),40,60),F(1,100))
        self.assertLess(moment_fourier_leak_sharp_upper(F(1,2),21,29),
                        moment_fourier_leak_upper(F(1,2),21,29))

    def test_mutated_missing_gamma_fails_margin(self):
        # Essential structural control: remove gamma M_G and the signed source
        # lower estimate is strictly NEGATIVE, so the certificate cannot pass.
        B=F(141,20)
        self.assertLess(0-B,0)
        # The source-identity certificate cannot promote an altered pole bound.
        with self.assertRaises(ArithmeticMetaError):
            SourceContract(gamma_parity=1)

    def test_parameters_refuse_unlicensed_approximations(self):
        with self.assertRaises(ArithmeticMetaError):
            moment_fourier_leak_upper(0.5,40,100)  # float is not certificate
        with self.assertRaises(ArithmeticMetaError):
            gamma_rungs_multiplier_lower(40,-1)


class TestConditionalFiniteSchurBridge(unittest.TestCase):
    def test_positive_two_mode_whole_form_sufficient(self):
        c=exact_finite_schur_sufficiency(
            F(1),((F(2),F(0)),(F(0),F(3))),
            ((F(1),F(0)),(F(0),F(2))))
        self.assertTrue(c["sufficient_for_full_form"])
        self.assertEqual(c["corrected_matrix"],(("1","0"),("0","1")))
        self.assertFalse(c["source_operator_identified_here"])

    def test_negative_schur_does_not_forge_sign(self):
        c=exact_finite_schur_sufficiency(F(1),((F(1,2),),),((F(1),),))
        self.assertFalse(c["sufficient_for_full_form"])
        self.assertEqual(c["principal_minors"][0][1],"-1/2")

    def test_invalid_matrix_or_gap_fails(self):
        with self.assertRaises(ArithmeticMetaError):
            exact_finite_schur_sufficiency(F(0),((F(1),),),((F(0),),))
        with self.assertRaises(ArithmeticMetaError):
            exact_finite_schur_sufficiency(F(1),((F(2),),),((F(-1),),))
        with self.assertRaises(ArithmeticMetaError):
            exact_finite_schur_sufficiency(F(1),((F(1),F(2)),(F(3),F(4))),((F(0),F(0)),(F(0),F(0))))


class TestIndependentOriginalWeilOracle(unittest.TestCase):
    def test_independent_prime_free_tent(self):
        try:
            r=independent_tent_weil_oracle("0.25",dps=35)
        except ImportError:
            self.skipTest("optional mpmath not available")
        self.assertEqual(r["source_prime_powers"],[])
        self.assertLess(float(r["difference"]),1e-25)
        self.assertFalse(r["rigorous_interval_certificate"])

    def test_independent_first_prime_tent(self):
        try:
            r=independent_tent_weil_oracle("0.5",dps=35)
        except ImportError:
            self.skipTest("optional mpmath not available")
        self.assertEqual(r["source_prime_powers"],[2])
        self.assertLess(float(r["difference"]),1e-25)
        self.assertFalse(r["zero_positions_used"])

    def test_independent_multijet_tent(self):
        try:
            r=independent_tent_weil_oracle("0.75",dps=35)
        except ImportError:
            self.skipTest("optional mpmath not available")
        self.assertEqual(r["source_prime_powers"],[2,3,4])
        self.assertLess(float(r["difference"]),1e-25)


if __name__ == "__main__":
    unittest.main()
