"""Original finite-adeles Tate test and full finite Ramanujan Fourier oracles."""
import unittest
from fractions import Fraction as F
from math import gcd,prod

from observational_succ.adelic_mobius_tate_test import (
    AdelicMobiusError, FiniteTateMobiusTest,
)
from observational_succ.mobius_index_infinity import (
    finite_sieve_count,squarefree_mobius_tape,sieve_projection,
)


class FiniteTateMobiusTests(unittest.TestCase):
    def test_every_integer_sieve_equals_actual_compact_open_Tate_test(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            t=FiniteTateMobiusTest(ps)
            for n in range(1,151):
                r=t.on_integer(n)
                independent=int(gcd(n,prod(ps,start=1))==1)
                self.assertEqual(r['original_integer_value'],independent)
                self.assertEqual(r['Tate_finite_adele_indicator_value'],independent)
                self.assertTrue(r['exact_source_restriction_commutes'])
                self.assertFalse(r['signed_Well_positivity_proved'])
                self.assertEqual(r['original_integer_value'],
                                 sieve_projection(n,ps)['projection_diagonal'])

    def test_additive_Haar_is_actual_Tate_ball_sum_and_CRT_count(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            t=FiniteTateMobiusTest(ps)
            M=t.modulus
            actual=t.additive_haar()
            self.assertEqual(actual['actual_RationalCoset_source_mass'],
                             prod((F(p-1,p) for p in ps),start=F(1)))
            self.assertEqual(actual['actual_RationalCoset_source_mass'],
                             finite_sieve_count(ps,3*M)['normalized_trace'])
            self.assertTrue(actual['original_tate_Schwartz_Bruhat_generator_span'])
            self.assertFalse(actual['is_global_completed_Weil_distribution'])

    def test_original_Tate_coset_terms_have_correct_true_Fourier_support(self):
        for ps in ((2,),(2,3),(2,3,5)):
            t=FiniteTateMobiusTest(ps)
            M=t.modulus
            source=dict(squarefree_mobius_tape(ps))
            for d,sign,coset in t.terms():
                self.assertEqual(sign,source[d])
                self.assertEqual(coset.scale,F(d))
                self.assertEqual(coset.shift,0)
                self.assertEqual(coset.additive_haar_volume,F(1,d))
                for q in (F(0),F(1,M),F(2,M),F(1,7)):
                    expected=(d*q).denominator==1
                    self.assertEqual(coset.dual_diagonal(q)['dual_within_finite_support'],
                                     expected)
                    independent=coset.dual_source_crosscheck(q)
                    self.assertTrue(independent['annihilator_support_crosschecked'])
                    self.assertEqual(independent['independent_Tate_negative_phase'],0)

    def test_full_Fourier_Ramanujan_values_cross_divisor_oracle(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            t=FiniteTateMobiusTest(ps)
            M=t.modulus
            mu=dict(squarefree_mobius_tape(ps))
            for a in range(-M,2*M):
                r=t.ramanujan_oracle(a)
                independent=sum((d*mu[M//d] for d in range(1,M+1)
                                 if M%d==0 and a%d==0),0)
                self.assertEqual(r['independent_CRT_Ramanujan_integer'],independent)
                self.assertEqual(r['independent_divisor_Ramanujan_integer'],independent)
                self.assertEqual(r['actual_finite_Tate_Fourier'],F(independent,M))
                self.assertTrue(r['Fourier_phase_source_consistent'])
                self.assertFalse(r['all_place_Weil_positive'])

    def test_fourier_can_have_negative_values_while_original_operator_is_PSD(self):
        t=FiniteTateMobiusTest((2,3))
        self.assertEqual(t.Fourier_at_rational(F(0))['Fourier_value'],F(1,3))
        self.assertEqual(t.Fourier_at_rational(F(1,6))['Fourier_value'],F(1,6))
        self.assertEqual(t.Fourier_at_rational(F(1,2))['Fourier_value'],F(-1,3))
        self.assertEqual(t.Fourier_at_rational(F(1,3))['Fourier_value'],F(-1,6))
        self.assertEqual(t.Fourier_at_rational(F(1,7))['Fourier_value'],0)
        self.assertTrue(t.on_integer(6)['exact_source_restriction_commutes'])
        self.assertEqual(t.on_integer(6)['original_integer_value'],0)

    def test_exact_full_CRT_Fourier_Plancherel_no_numeric_truncation(self):
        for ps in ((),(2,),(2,3),(2,3,5),(2,3,5,7)):
            t=FiniteTateMobiusTest(ps)
            result=t.exact_plancherel()
            M=t.modulus
            values=result['all_M_Fourier_values']
            self.assertEqual(len(values),M)
            self.assertEqual(sum((v*v for v in values),F(0)),
                             result['original_additive_haar_norm_sq'])
            self.assertEqual(result['dual_original_Fourier_norm_sq'],
                             result['original_additive_haar_norm_sq'])
            self.assertTrue(result['exact_finite_Tate_Poisson_Plancherel'])
            self.assertTrue(result['all_original_finite_places_retained'])
            self.assertTrue(result['no_Arch_Gamma_contact_or_global_Connes_trace'])

    def test_source_receipt_and_independent_finite_trace_budget(self):
        t=FiniteTateMobiusTest((2,3,5),source_id="Q-standard-Tate",epoch=1)
        r=t.source_receipt(17,211)
        self.assertEqual(r['source_primes'],(2,3,5))
        self.assertEqual(r['original_integer']['original_integer_value'],1)
        self.assertEqual(r['actual_Tate_additive_Haar'],F(4,15))
        self.assertLessEqual(abs(r['integer_cutoff_trace']-r['actual_Tate_additive_Haar']),
                             r['rational_error_upper'])
        self.assertFalse(r['all_place_multiplicative_Connes_trace'])
        self.assertFalse(r['one_real_Gamma_two_poles_and_contact'])
        self.assertFalse(r['RH_proved'])

    def test_fake_euler_places_and_missing_source_domains_rejected(self):
        for ps in ((6,),(4,),(3,2),(2,2),(True,),tuple(range(2,12))):
            with self.assertRaises(AdelicMobiusError):
                FiniteTateMobiusTest(ps)
        for value in ('',True,None):
            with self.assertRaises(AdelicMobiusError):
                FiniteTateMobiusTest((2,),source_id=value)
        with self.assertRaises(AdelicMobiusError):
            FiniteTateMobiusTest((2,),epoch=True)
        t=FiniteTateMobiusTest((2,3))
        for n in (0,True,1.1):
            with self.assertRaises(AdelicMobiusError):
                t.on_integer(n)
        for q in (True,1.3):
            with self.assertRaises(AdelicMobiusError):
                t.Fourier_at_rational(q)
        with self.assertRaises(AdelicMobiusError):
            t.ramanujan_oracle(F(1,2))
        with self.assertRaises(AdelicMobiusError):
            t.source_receipt(1,0)


if __name__=="__main__":
    unittest.main()
