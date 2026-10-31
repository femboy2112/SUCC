from fractions import Fraction
from math import isqrt, log
from unittest import TestCase,main
from logjet_probe import (COEFF,OFFSETS,potential,logarithmic_source,
 multiplicative_carrier,logjet_selected,source_product,source_product_abel,
 v_p_integer,v_p_fraction,carrier_valuation_vector,predicted_v2,
 initial_seed_first_jet_difference)

MUTANT=(5,-5,0,0)
class LogJetTests(TestCase):
 def test_potential_is_positive(self):
    for n in range(1,101):
        self.assertGreater(potential(8*n-7),0)
 def test_source_equals_original_four_pole(self):
    for n in range(1,301):
        a=8*n-7
        self.assertEqual(logarithmic_source(a),Fraction(4,a)-Fraction(2,a+3)-Fraction(1,a+4)-Fraction(1,a+5))
 def test_selected_first_jet(self):
    self.assertEqual(logjet_selected(0),0)
    self.assertEqual(logjet_selected(1),Fraction(47,15))
    for n in range(0,50):
        self.assertEqual(logjet_selected(n+1),16*logjet_selected(n)+logarithmic_source(8*(n+1)-7))
 def test_multiplicative_closed_form(self):
    for n in range(0,4):
        self.assertEqual(multiplicative_carrier(n),source_product_abel(n))
 def test_exact_2adic_slope(self):
    for n in range(1,5):
        self.assertEqual(v_p_fraction(multiplicative_carrier(n),2),predicted_v2(n))
 def test_all_primes_match_direct_rational(self):
    for n in range(0,5):
        q=multiplicative_carrier(n)
        v=carrier_valuation_vector(n)
        for p in (2,3,5,7,11,13,17,19,23,31,41,47):
            self.assertEqual(v.get(p,0),v_p_fraction(q,p))
 def test_seed_is_invisible_in_potential_values(self):
    for n in range(0,15):
        self.assertEqual(initial_seed_first_jet_difference(n,Fraction(7,11)),16**n*Fraction(7,11))
 def test_positive_same_rank_mutant_has_different_prime_2_slope(self):
    for n in range(1,5):
        self.assertEqual(v_p_fraction(multiplicative_carrier(n,MUTANT),2),predicted_v2(n,True))
        self.assertNotEqual(multiplicative_carrier(n),multiplicative_carrier(n,MUTANT))
 def test_same_first_jet_gamma_rank_but_not_source_second(self):
    self.assertEqual(-sum(c*d for c,d in zip(COEFF,OFFSETS)),15)
    self.assertEqual(-sum(c*d for c,d in zip(MUTANT,OFFSETS)),15)
    self.assertNotEqual(sum(c*d*d for c,d in zip(COEFF,OFFSETS)),sum(c*d*d for c,d in zip(MUTANT,OFFSETS)))
 def test_all_primes_product_identity(self):
    from math import prod
    for n in range(1,5):
        v=carrier_valuation_vector(n)
        positive=prod(p**e for p,e in v.items() if e>0)
        negative=prod(p**(-e) for p,e in v.items() if e<0)
        self.assertEqual(Fraction(positive,negative),multiplicative_carrier(n))

if __name__=='__main__':main()
