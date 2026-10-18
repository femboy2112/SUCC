"""Independent exact universal divisor cancellation and Tate Gamma remainder controls."""
import unittest
from fractions import Fraction as Q
from math import isqrt

from observational_succ.mobius_tate_gamma_remainder import (
    MobiusGammaError, independent_mobius, factor_support, exact_divisor_cancel,
    finite_tate_gamma_remainder, omitted_prime_mutant,
)
from observational_succ.oriented_mobius_adelic import number_moebius


class MobiusTateGammaTests(unittest.TestCase):
    def test_exact_divisor_convolution_for_all_early_source_integers(self):
        for n in range(1,251):
            r=exact_divisor_cancel(n)
            self.assertEqual(r['arithmetic_convolution_sum'],int(n==1))
            self.assertEqual(r['factorized_prime_cancellation'],int(n==1))
            self.assertTrue(r['is_unit_delta'])
            self.assertFalse(r['completed_Weil_PSD_proved'])

    def test_independent_mobius_prime_support_and_squareful_contrast(self):
        for n in range(1,400):
            self.assertEqual(independent_mobius(n),number_moebius(n))
            for p in factor_support(n):
                self.assertEqual(n%p,0)
                self.assertTrue(all(p%d for d in range(2,isqrt(p)+1)))
        self.assertEqual(independent_mobius(4),0)
        self.assertEqual(independent_mobius(6),1)
        self.assertEqual(independent_mobius(8),0)
        self.assertEqual(independent_mobius(30),-1)

    def test_true_Tate_finite_zeta_times_Mobius_leaves_Gamma(self):
        for ps in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            for beta in (2,4,6,8):
                r=finite_tate_gamma_remainder(ps,beta)
                self.assertTrue(r['finite_places_exactly_cancel'])
                self.assertEqual(r['genuine_Tate_finite_zeta'] *
                                 r['genuine_Mobius_convolution_inverse'],1)
                self.assertNotEqual(r['genuine_Tate_finite_zeta'] *
                                    r['wrong_squarefree_positive_norm'],1)
                self.assertNotEqual(r['genuine_Tate_finite_zeta'] *
                                    r['wrong_full_negative_towers'],1)
                self.assertEqual(r['Tate_pole_residues'],(Q(-1),Q(1)))
                self.assertFalse(r['completed_Weil_trace_identified'])
                self.assertFalse(r['can_invert_zeta_at_every_critical_zero'])
        self.assertEqual(finite_tate_gamma_remainder((2,3),2)
                         ['remaining_archimedean_Gamma_R_monomial'],(1,-1))
        self.assertEqual(finite_tate_gamma_remainder((2,3),4)
                         ['remaining_archimedean_Gamma_R_monomial'],(1,-2))
        self.assertEqual(finite_tate_gamma_remainder((2,3),6)
                         ['remaining_archimedean_Gamma_R_monomial'],(2,-3))

    def test_full_prime_source_mutation_leaves_nontrivial_residue(self):
        for p in (2,3,5,7):
            for beta in (2,3,4):
                r=omitted_prime_mutant(p,beta)
                self.assertEqual(r['missing_Euler_source_residual'],Q(p**beta-1,p**beta))
                self.assertFalse(r['equals_Arch_Gamma_only'])

    def test_domain_and_fake_euler_place_rejected(self):
        for ps in ((6,),(2,6),(2,2),(3,2),()):
            with self.assertRaises(MobiusGammaError):
                finite_tate_gamma_remainder(ps,2)
        for beta in (1,3,0,True,Q(2)):
            with self.assertRaises(MobiusGammaError):
                finite_tate_gamma_remainder((2,),beta)
        for n in (0,-1,True,Q(2)):
            with self.assertRaises(MobiusGammaError):
                exact_divisor_cancel(n)
        with self.assertRaises(MobiusGammaError):
            omitted_prime_mutant(6,2)


if __name__=="__main__":
    unittest.main()
