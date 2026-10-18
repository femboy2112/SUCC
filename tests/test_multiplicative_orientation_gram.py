"""Exact independent SUCC/FUCC Gram, log energy, and two-completion controls."""
import unittest
from fractions import Fraction as Q

from observational_succ.multiplicative_orientation_gram import (
    MultiplicativeGramError, prime_valuations, totient, divisors, overlap,
    normalized_overlap_squared, quadratic_certificate, cross_prime_contrast,
    log_valuation_negative_type, prime_power_projection,
    prime_jet_Weil_weight_contract, archimedean_log_discontinuity,
)


class MultiplicativeOrientationGramTests(unittest.TestCase):
    def test_arithmetic_totient_factorization(self):
        for n in range(1,301):
            self.assertEqual(sum(totient(d) for d in divisors(n)),n)
            self.assertEqual(tuple(sorted(divisors(n))),divisors(n))
            self.assertTrue(all(n%d==0 for d in divisors(n)))
            self.assertEqual(overlap(n,n),n)

    def test_arithmetic_gram_equals_divisor_square_sum(self):
        ns=(1,2,3,4,6,9,10,12,25)
        cs=(Q(1),Q(-2,3),Q(7),Q(-2),Q(3,11),Q(0),Q(-5),Q(9,7),Q(-9))
        r=quadratic_certificate(ns,cs)
        self.assertEqual(r['quadratic'],r['positive_sum_of_squares'])
        self.assertTrue(r['normalized_kernel_PSD_by_congruence'])
        self.assertFalse(r['completed_Weil_identified'])

    def test_archimedean_gram_equals_interval_square_sum(self):
        ns=(1,2,3,4,6,9,10,12,25)
        for cs in ((1,-1,1,-1,1,-1,1,-1,1),(1,0,0,0,0,0,0,0,-1)):
            r=quadratic_certificate(ns,cs,chart='archimedean')
            self.assertEqual(r['quadratic'],r['positive_sum_of_squares'])
            self.assertGreaterEqual(r['quadratic'],0)

    def test_simultaneous_multiplication_and_divisor_chain(self):
        for m in range(1,42):
            for n in range(1,42):
                for a in (2,3,6):
                    for chart in ('arithmetic','archimedean'):
                        self.assertEqual(normalized_overlap_squared(a*m,a*n,chart=chart),
                                         normalized_overlap_squared(m,n,chart=chart))
                if m%n==0 or n%m==0:
                    self.assertEqual(overlap(m,n),overlap(m,n,chart='archimedean'))

    def test_two_psd_forms_have_indefinite_cross_prime_difference(self):
        r=cross_prime_contrast(2,3)
        self.assertTrue(r['both_completions_PSD'])
        self.assertEqual(r['unnormalized_offdiagonal_difference'],1)
        self.assertEqual((r['positive_vector_quadratic'],
                          r['negative_vector_quadratic']),(2,-2))
        self.assertFalse(r['Weil_distribution_equated'])
        self.assertEqual(cross_prime_contrast(2,8)['negative_vector_quadratic'],0)

    def test_log_filtration_energy_is_exact_sum_of_squares(self):
        cases=((1,2),(2,3),(1,4,9,10),(1,2,3,6,12,18),(4,8,16,32))
        for ns in cases:
            cs=tuple([1]*(len(ns)-1)+[1-len(ns)])
            rec=log_valuation_negative_type(ns,cs)
            self.assertTrue(rec['positive_on_zero_sum'])
            self.assertTrue(all(v>=0 for v in rec['prime_log_energy_coefficients'].values()))
        self.assertEqual(log_valuation_negative_type((2,3),(1,-1))['prime_log_energy_coefficients'],
                         {2:Q(1),3:Q(1)})
        self.assertEqual(log_valuation_negative_type((1,8),(1,-1))['prime_log_energy_coefficients'],
                         {2:Q(3)})

    def test_prime_jets_reconstruct_magnitude_not_signed_distribution(self):
        for p in (2,3,5,7,11):
            for k in (1,2,3):
                n=p**k
                if n>100000:
                    continue
                r=prime_jet_Weil_weight_contract(n)
                self.assertEqual(r['half_density_amplitude_squared'],Q(1,n))
                self.assertEqual(r['primitive_energy_coefficient_logp'],1)
                self.assertEqual(r['raw_valuation_energy_coeff_logp'],k)
                self.assertFalse(r['Weil_signed_distribution_matched'])
        for n in (1,6,10,12,15,30,42,72):
            self.assertIsNone(prime_power_projection(n))
            self.assertFalse(prime_jet_Weil_weight_contract(n)['is_prime_power'])

    def test_crosscheck_existing_connes_prime_jet_oracle(self):
        from observational_succ.connes_oriented_scaling import prime_jet_half_density
        for p in (2,3,5):
            for k in (1,2,3):
                expected=prime_jet_half_density(p,k)['half_density_coefficient_squared']
                actual=prime_jet_Weil_weight_contract(p**k)['half_density_amplitude_squared']
                self.assertEqual(actual,expected)

    def test_archimedean_log_continuity_obstruction(self):
        for n in (1,2,3,4,5,20,100,1000,50000):
            r=archimedean_log_discontinuity(n)
            self.assertEqual(r['arithmetic_normalized_squared'],Q(1,n*(n+1)))
            self.assertEqual(r['archimedean_normalized_squared'],Q(n,n+1))
            self.assertEqual(r['log_gap_ratio'],Q(n+1,n))
            self.assertFalse(r['same_log_continuous_extension_possible'])

    def test_source_and_domain_mutants_rejected(self):
        for bad in (True,0,-2,1.1,Q(2)):
            with self.assertRaises(MultiplicativeGramError):
                overlap(bad,2)
        with self.assertRaises(MultiplicativeGramError):
            quadratic_certificate((2,3),(1,))
        with self.assertRaises(MultiplicativeGramError):
            quadratic_certificate((2,3),(1,-1),chart='other')
        with self.assertRaises(MultiplicativeGramError):
            log_valuation_negative_type((2,3),(1,1))
        with self.assertRaises(MultiplicativeGramError):
            log_valuation_negative_type((1,2),('forged',-1))
        self.assertEqual(prime_valuations(6),{2:1,3:1})


if __name__=='__main__':
    unittest.main()
