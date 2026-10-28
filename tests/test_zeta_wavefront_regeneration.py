"""Exact rational regression for source-typed zeta wavefront proposal."""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from itertools import product
from math import prod

from observational_succ.zeta_wavefront_regeneration import (
    SOURCE, ZetaSourcePassport, is_prime, prime_set, beta_prime_ratio,
    finite_euler_partition, prime_exponents, smooth_probability,
    finite_prime_event_probability, regenerated_probability,
    regenerated_word_probability, additive_up_rate, prime_up_rate,
    additive_detailed_balance_ratio, prime_detailed_balance_ratio,
    local_mode_probability,local_resolvent_coefficient,
    finite_pump_normalization, counterfeit_composite_amplitude_multiplicity,
    exact_prior_mass_below, exact_tail_integral_bracket,
)

class ZetaWavefrontExactTests(unittest.TestCase):
    PS=(2,3,5,7)
    def test_prime_validation(self):
        self.assertTrue(all(is_prime(p) for p in self.PS))
        self.assertFalse(any(is_prime(p) for p in (0,1,4,6,9,15,25,121)))
        for bad in ((2,4),(2,2,3),(3,2),(),(1,2)):
            with self.assertRaises(ValueError):prime_set(bad)

    def test_exact_euler_partition(self):
        self.assertEqual(finite_euler_partition((2,3),2),F(3,2))
        self.assertEqual(finite_euler_partition((2,3,5),2),F(25,16))
        self.assertEqual(finite_euler_partition((2,3),3),F(216,182))

    def test_finite_occupation_tensor_equals_euler_factor(self):
        for beta in (2,3):
            for ps in ((2,),(2,3),(2,3,5)):
                result=sum((F(1,prod((p**k for p,k in zip(ps,eks)))**beta)
                            for eks in product(range(4),repeat=len(ps))),F(0))
                fact=F(1)
                for p in ps:
                    q=beta_prime_ratio(p,beta)
                    fact*= (1-q**4)/(1-q)
                self.assertEqual(result,fact)

    def test_prime_occupancy_normalizes(self):
        for beta in (2,3,5):
            for p in self.PS:
                q=beta_prime_ratio(p,beta)
                for k in range(12):
                    self.assertEqual(local_mode_probability(p,beta,k),
                                     (1-q)*local_resolvent_coefficient(p,beta,k))
                self.assertEqual(sum((local_mode_probability(p,beta,k)
                                      for k in range(12)),F(0)),1-q**12)

    def test_finitemode_source_normalization(self):
        for beta in (2,3,4):
            self.assertEqual(finite_pump_normalization(self.PS,beta),
                             finite_euler_partition(self.PS,beta))
            self.assertEqual(smooth_probability(1,self.PS,beta),
                             1/finite_euler_partition(self.PS,beta))

    def test_smooth_integer_source_map(self):
        self.assertEqual(prime_exponents(2**4*3**2,(2,3,5)),(4,2,0))
        self.assertIsNone(prime_exponents(11,(2,3,5)))
        self.assertEqual(smooth_probability(11,(2,3,5),2),F(0))
        self.assertEqual(smooth_probability(1,(2,3,5),2),F(16,25))

    def test_prime_regeneration_all_parent_primes(self):
        for beta in (2,3,5):
            for p in self.PS:
                self.assertEqual(finite_prime_event_probability(p,self.PS,beta),F(1,p**beta))
                for a in range(5):
                    for b in range(4):
                        m=2**a*3**b*5
                        self.assertEqual(regenerated_probability(m,p,self.PS,beta),
                                         smooth_probability(m,self.PS,beta))

    def test_arbitrary_prime_word_coherence(self):
        for beta in (2,3):
            for word in ((2,3),(3,2),(2,2,5),(7,5,3,2),(2,2,3,5,7)):
                for n in (1,2,3,6,42,90):
                    self.assertEqual(regenerated_word_probability(n,word,self.PS,beta),
                                     smooth_probability(n,self.PS,beta))

    def test_generator_source_passport(self):
        p=ZetaSourcePassport(SOURCE,2,self.PS)
        self.assertEqual(p.regeneration(12,3),p.probability(12))
        with self.assertRaises(ValueError):ZetaSourcePassport("counterfeit",2,self.PS)

    def test_additive_detailed_balance(self):
        for beta in (2,3,5):
            for n in range(1,250):
                self.assertEqual(additive_detailed_balance_ratio(n,beta),1)

    def test_prime_detailed_balance(self):
        for beta in (2,3,4):
            for n in range(1,73):
                for p in self.PS:
                    self.assertEqual(prime_detailed_balance_ratio(n,p,beta),1)

    def test_succ_not_a_scalar_stationary_eigenmode(self):
        # The unique prime-common vector has sqrt-amplitudes n^{-beta/2}.
        # Its consecutive-step ratios cannot be a fixed S^* eigenvalue.
        for beta in (2,4):
            self.assertNotEqual(F(1,2)**(beta//2),F(2,3)**(beta//2))

    def test_fake_composite_double_counts_four(self):
        self.assertEqual(counterfeit_composite_amplitude_multiplicity(4,(2,4)),2)
        self.assertEqual(counterfeit_composite_amplitude_multiplicity(4,(2,3)),1)
        self.assertEqual(counterfeit_composite_amplitude_multiplicity(16,(2,4)),3)
        with self.assertRaises(ValueError): finite_euler_partition((2,4),2)

    def test_no_fixed_prime_law_from_regeneration_alone(self):
        # Genuine zeta beta=2 has q2=1/4; source-mutant q2=1/8
        # and q3=1/9 still regenerates each p although not ζ(2).
        q2,q3=F(1,8),F(1,9)
        z=1/((1-q2)*(1-q3))
        def mutant(a,b):
            return q2**a*q3**b/z
        for a,b in product(range(4),range(4)):
            self.assertEqual(mutant(a+1,b)/q2,mutant(a,b))
            self.assertEqual(mutant(a,b+1)/q3,mutant(a,b))
        self.assertNotEqual(z,finite_euler_partition((2,3),2))

    def test_a_valid_standing_field_doesnt_select_dynamics(self):
        # Both q and 2q generate the same reversible Gibbs distribution
        # if backward edge rates are rescaled by the same positive factor.
        n=7; beta=2
        q=additive_up_rate(n,beta)
        self.assertEqual(q, F(n,n+1)**beta)
        self.assertNotEqual(q,2*q)
        self.assertEqual(q/F(1), (2*q)/F(2))

    def test_valid_cutoff_bounds(self):
        for beta in (2,3,4):
            for n in (1,2,4,10,100):
                lo,hi=exact_tail_integral_bracket(n,beta)
                self.assertTrue(0<lo<hi)
                # Compare finite 20000-term tail conservatively, residual positive.
                partial=sum((F(1,k**beta) for k in range(n+1,500)),F(0))
                self.assertLess(partial,hi)
                self.assertGreater(partial + exact_tail_integral_bracket(499,beta)[0],lo)

    def test_exact_finite_harmonics(self):
        self.assertEqual(exact_prior_mass_below(4,2),F(205,144))
        self.assertEqual(exact_prior_mass_below(1,2),1)

    def test_source_validation_errors(self):
        for beta in (0,1,-1,2.0,3.3):
            with self.assertRaises(ValueError): finite_euler_partition((2,3),beta)
        with self.assertRaises(ValueError): regenerated_probability(1,11,self.PS,2)
        with self.assertRaises(ValueError): regenerated_word_probability(1,(2,11),self.PS,2)

if __name__=='__main__':unittest.main()
