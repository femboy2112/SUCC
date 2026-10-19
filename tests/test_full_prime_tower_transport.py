"""Exact conditioning of full Tate valuation shells to projective p+1 sector."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.full_prime_tower_transport import (
    PrimeTowerError, FullPrimeTower, projective_from_tate_crosscheck,
    finite_tower_tate_crosscheck, finite_full_valuation_cylinder,
)


class FullPrimeTowerTransportTests(unittest.TestCase):
    def test_exact_geometric_local_probabilities_and_tails(self):
        for p in (2,3,5,7):
            for beta in (1,2,3):
                plus=FullPrimeTower(p,beta,epsilon=1)
                minus=FullPrimeTower(p,beta,epsilon=-1)
                r=Q(1,p**beta)
                for K in (0,1,2,3,6):
                    positive=plus.prefix(K)
                    negative=minus.prefix(K)
                    self.assertEqual(positive['tail_probability'],r**(K+1))
                    self.assertEqual(sum(row[1] for row in positive['valuations'])+
                                     positive['tail_probability'],1)
                    self.assertEqual(tuple(row[1] for row in positive['valuations']),
                                     tuple(row[1] for row in negative['valuations']))
                    self.assertEqual(tuple(row[2] for row in negative['valuations']),
                                     tuple((-1)**k for k in range(K+1)))
                    self.assertTrue(negative['signed_Mellin_not_probabilities'])

    def test_original_projective_p_plus_one_is_CONDITIONING_not_coarsening(self):
        for p in (2,3,5,7,11):
            x=projective_from_tate_crosscheck(p)
            self.assertEqual(x['conditional_mass'],(Q(p,p+1),Q(1,p+1)))
            self.assertEqual(x['coarse_nonzero_valuation_mass'],Q(1,p))
            self.assertEqual(x['missing_p_squared_and_higher_mass'],Q(1,p*p))
            self.assertTrue(x['phase_is_declared_not_forced_by_conditioning'])
            self.assertNotEqual(x['conditional_mass'][1],x['coarse_nonzero_valuation_mass'])
        self.assertEqual(FullPrimeTower(2).conditional_squarefree()['conditional_k1'],Q(1,3))
        self.assertEqual(FullPrimeTower(2).r,Q(1,2))

    def test_beta_dependence_shows_p_plus_one_not_universal_for_other_s(self):
        p=3
        self.assertEqual(FullPrimeTower(p,1).conditional_squarefree()['conditional_k1'],Q(1,4))
        self.assertEqual(FullPrimeTower(p,2).conditional_squarefree()['conditional_k1'],Q(1,10))
        self.assertEqual(FullPrimeTower(p,3).conditional_squarefree()['conditional_k1'],Q(1,28))

    def test_full_prime_power_tate_Mellin_not_squarefree_or_signed_relabel(self):
        for p in (2,3,5):
            for beta in (2,3,4):
                pos=FullPrimeTower(p,beta,+1)
                neg=FullPrimeTower(p,beta,-1)
                self.assertEqual(pos.linear_mellin_factor(),Q(p**beta,p**beta-1))
                self.assertEqual(neg.linear_mellin_factor(),Q(p**beta,p**beta+1))
                self.assertNotEqual(pos.linear_mellin_factor(),
                                    1+Q(1,p**beta))
                self.assertNotEqual(pos.linear_mellin_factor(),neg.linear_mellin_factor())
                self.assertEqual(pos.phase_sensitive_shift_expectation()['absolute_square'],
                                 neg.phase_sensitive_shift_expectation()['absolute_square'])
                self.assertEqual(pos.phase_sensitive_shift_expectation()['sign'],+1)
                self.assertEqual(neg.phase_sensitive_shift_expectation()['sign'],-1)

    def test_canonical_actual_Tate_crosscheck_all_unramified_prime_powers(self):
        for primes in ((2,),(2,3),(2,3,5),(2,3,5,7)):
            for beta in (2,3):
                rec=finite_tower_tate_crosscheck(primes,beta,depth=5)
                self.assertTrue(rec['agreement_all_local_prime_powers'])
                self.assertEqual(rec['source_real_Tate_Euler'],rec['independent_full_tower_product'])
                self.assertFalse(rec['squarefree_projective_product_equal_to_full_zeta'])

    def test_chi_minus3_mutant_preserves_ramified_place_distinction(self):
        self.assertEqual(FullPrimeTower(3,beta=2).chi_minus_3_factor()['Euler_factor'],1)
        self.assertFalse(FullPrimeTower(3,beta=2).chi_minus_3_factor()['local_Hecke_character_itself_vanishes'])
        self.assertEqual(FullPrimeTower(2,beta=2).chi_minus_3_factor()['phase'],-1)
        self.assertEqual(FullPrimeTower(7,beta=2).chi_minus_3_factor()['phase'],+1)
        self.assertEqual(FullPrimeTower(7,beta=2).chi_minus_3_factor()['Euler_factor'],Q(49,48))

    def test_full_cylinder_truncation_and_independent_bruteforce(self):
        for primes in ((),(2,),(2,3),(2,3,5)):
            for depth in (0,1,2,3):
                rec=finite_full_valuation_cylinder(primes,depth,beta=2)
                brute=Q(0)
                for ks in product(*(range(depth+1) for _ in primes)):
                    q=Q(1)
                    for p,k in zip(primes,ks):
                        q*=Q(p*p-1,p*p)*Q(1,p**(2*k))
                    brute+=q
                self.assertEqual(rec['finite_retained_mass'],brute)
                self.assertEqual(rec['finite_retained_mass'],rec['truncated_mass_formula'])
                self.assertGreaterEqual(rec['omitted_tail_mass'],0)

    def test_rejects_source_mutations_and_fake_p6(self):
        for p in (6,4,1,True,2.5):
            with self.assertRaises(PrimeTowerError):
                FullPrimeTower(p)
        for beta in (0,-1,True,Q(2)):
            with self.assertRaises(PrimeTowerError):
                FullPrimeTower(2,beta)
        for eps in (0,2,True,Q(-1),'minus'):
            with self.assertRaises(PrimeTowerError):
                FullPrimeTower(2,epsilon=eps)
        with self.assertRaises(PrimeTowerError):
            FullPrimeTower(2,source_id="")
        with self.assertRaises(PrimeTowerError):
            FullPrimeTower(2,epoch=True)
        with self.assertRaises(PrimeTowerError):
            finite_tower_tate_crosscheck((3,2))
        with self.assertRaises(PrimeTowerError):
            finite_full_valuation_cylinder((2,2),3)


if __name__=="__main__":
    unittest.main()
