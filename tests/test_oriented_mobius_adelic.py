"""Original-source exact controls for negative counting, Möbius orientation and ideles."""
import unittest
from fractions import Fraction as Q
from itertools import combinations

from observational_succ.oriented_mobius_adelic import (
    NegativeCountingError, DifferenceCount, reversal_ring_obstruction,
    PrimeIncidence, omega_parity, number_moebius, valuations,
    source_succ_sign_edges, rational_prime_valuations,
    diagonal_norm_character_receipt, uniform_negative_no_global_character,
    signed_local_euler_factor,
)


class NegativeCountingAndAdelicDescentTests(unittest.TestCase):
    def test_group_completion_is_difference_before_integer_realization(self):
        one=DifferenceCount(1,0)
        self.assertTrue(DifferenceCount(5,4).equivalent(one))
        self.assertTrue(DifferenceCount(2,6).equivalent(DifferenceCount(4,8)))
        self.assertEqual(one.reverse().integer_value(),-1)
        self.assertEqual(DifferenceCount(3,2).times(DifferenceCount(1,4)).integer_value(),-3)
        self.assertTrue(one.add(one.reverse()).equivalent(DifferenceCount(0,0)))
        r=reversal_ring_obstruction()
        self.assertTrue(r['preserves_additive_group'])
        self.assertFalse(r['preserves_unital_multiplication'])
        self.assertEqual(r['product_of_reversed_units'],1)
        self.assertEqual(r['reversed_product_of_units'],-1)

    def test_mobius_equals_parity_conjugated_zeta_on_all_boolean_lattices(self):
        primes=(2,3,5,7)
        for k in range(1,5):
            c=PrimeIncidence(primes[:k],(1,)*k)
            r=c.verdict()
            self.assertTrue(r['oriented_positive_zeta_equals_inverse'])
            self.assertTrue(r['moebius_is_exact_incidence_inverse'])
            self.assertEqual(r['unresolved_prime_power_obstruction_count'],0)
            for a in c.states:
                for b in c.states:
                    self.assertEqual(c.moebius(a,b),c.oriented_zeta(a,b))

    def test_independent_boolean_mobius_interval_oracle(self):
        c=PrimeIncidence((2,3,5),(1,1,1))
        for a in c.states:
            for b in c.states:
                if c.comparable(a,b):
                    intermediate=[u for u in c.states if c.comparable(a,u) and c.comparable(u,b)]
                    direct=sum(c.moebius(a,u) for u in intermediate)
                    self.assertEqual(direct,int(a==b))
                    self.assertEqual(c.moebius(a,b),(-1)**sum(y-x for x,y in zip(a,b)))
                else:
                    self.assertEqual(c.moebius(a,b),0)

    def test_first_repeated_prime_falsifies_orientation_inverse(self):
        for p in (2,3,5):
            c=PrimeIncidence((p,),(2,))
            r=c.verdict()
            self.assertFalse(r['oriented_positive_zeta_equals_inverse'])
            self.assertEqual(c.zeta((0,),(2,)),1)
            self.assertEqual(c.moebius((0,),(2,)),0)
            self.assertEqual(c.oriented_zeta((0,),(2,)),1)
            self.assertEqual(c.moebius((0,),(1,)),-1)
            self.assertEqual(c.moebius((1,),(2,)),-1)
            self.assertTrue(r['first_obstruction'])
            self.assertTrue(r['moebius_is_exact_incidence_inverse'])
        self.assertFalse(PrimeIncidence((2,3),(1,2)).verdict()['oriented_positive_zeta_equals_inverse'])

    def test_exact_arithmetic_mobius_vs_liouville_on_p_p2_and_fake6(self):
        cases={1:(1,1),2:(-1,-1),3:(-1,-1),4:(0,1),
               6:(1,1),8:(0,-1),9:(0,1),12:(0,-1),30:(-1,-1)}
        for n,(mu,lam) in cases.items():
            self.assertEqual(number_moebius(n),mu)
            self.assertEqual(omega_parity(n),lam)
        self.assertEqual(valuations(6),{2:1,3:1})
        self.assertEqual(valuations(36),{2:2,3:2})

    def test_succ_vs_fucc_parity_gauge_needs_source_transport(self):
        r=source_succ_sign_edges((1,2,3,4,5))
        self.assertEqual(dict(r['transported_unit_succ_edge_signs'])[1],-1)
        self.assertEqual(dict(r['transported_unit_succ_edge_signs'])[2],+1)
        self.assertFalse(r['is_uniform_orientation_on_succ'])
        for p in (2,3,5):
            for n in range(1,60):
                self.assertEqual(omega_parity(p*n)*omega_parity(n),-1)

    def test_norm_character_diagonal_transport_exact_without_log_floats(self):
        from observational_succ.tate_idelic_zeta import product_formula_rational
        for q in (Q(1),Q(2),Q(3),Q(6),Q(7,12),Q(25,18),Q(1,100),Q(245,16)):
            r=diagonal_norm_character_receipt(q)
            self.assertTrue(r['sum_is_zero_for_every_prime'])
            self.assertTrue(r['descends_to_idelic_class_norm_character'])
            self.assertEqual(product_formula_rational(q),1)
            self.assertEqual(dict(r['finite_logp_coefficients']),
                             {p:-k for p,k in dict(r['arch_real_logp_coefficients']).items()})
        self.assertEqual(rational_prime_valuations(Q(18,35)),{2:1,3:2,5:-1,7:-1})

    def test_uniform_minus_idele_descent_no_go_has_two_independent_primes(self):
        for p,q in ((2,3),(2,5),(3,7),(11,13)):
            witness=uniform_negative_no_global_character(p,q)
            self.assertFalse(witness['continuous_arch_unitary_norm_character_can_compensate'])
            self.assertFalse(witness['a_ramified_Hecke_character_was_ruled_out'])
            self.assertTrue(witness['unique_factorization_implies_log_ratio_irrational'])

    def test_signed_tate_local_factors_retain_source_direction(self):
        for p in (2,3,5,7):
            for beta in (2,3,4):
                plus=signed_local_euler_factor(p,beta,+1)
                minus=signed_local_euler_factor(p,beta,-1)
                self.assertEqual(plus['Tate_zeta_local'],plus['phase_twisted_local'])
                self.assertNotEqual(minus['phase_twisted_local'],plus['phase_twisted_local'])
                self.assertEqual(plus['coefficient_at_p_squared'],minus['coefficient_at_p_squared'])
                self.assertEqual(minus['coefficient_at_p_squared'],1)
                self.assertEqual(minus['coefficient_at_p'],-1)

    def test_source_mutants_and_invalid_incidence_rejected(self):
        for bad in (0,-1,True,2.5):
            with self.assertRaises(NegativeCountingError):
                DifferenceCount(bad,1)
        with self.assertRaises(NegativeCountingError):
            PrimeIncidence((6,),(1,))
        with self.assertRaises(NegativeCountingError):
            PrimeIncidence((3,2),(1,1))
        with self.assertRaises(NegativeCountingError):
            PrimeIncidence((2,2),(1,1))
        with self.assertRaises(NegativeCountingError):
            PrimeIncidence((2,),(0,))
        with self.assertRaises(NegativeCountingError):
            PrimeIncidence((2,),(7,))
        with self.assertRaises(NegativeCountingError):
            uniform_negative_no_global_character(2,2)
        for bad in (True,0,Q(-1),2.2):
            with self.assertRaises(NegativeCountingError):
                rational_prime_valuations(bad)
        for e in (0,2,True,Q(-1),'minus'):
            with self.assertRaises(NegativeCountingError):
                signed_local_euler_factor(2,2,e)


if __name__=="__main__":
    unittest.main()
