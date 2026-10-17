"""Disjoint finite algorithms agree: lcm deltas vs quotient incidence inversion."""
import unittest
from fractions import Fraction
from math import lcm
from observational_succ.clock_incidence_inversion import (
    clock_divisors,incidence_mobius,clock_log_increment_ratio,
    incidence_prime_jets,incidence_lcm_compatibility,
    missing_incidence_arrow_mutation,
)
from observational_succ.orbit_clock_genesis import (
    ClockSourceError,minimal_clock_growth,join_irreducible_periods
)

class IncidenceAlgebraTests(unittest.TestCase):
    def test_mobius_first_twenty(self):
        mu=incidence_mobius(20)
        self.assertEqual(tuple(mu[n] for n in range(1,21)),
                         (1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,0))

    def test_divisibility_recursion_independent_from_lcm(self):
        mu=incidence_mobius(150)
        for n in range(1,151):
            self.assertEqual(sum(mu[d] for d in clock_divisors(n)),int(n==1))

    def test_source_prime_power_jets_match_lcm_deltas_to_300(self):
        lcm_rows=minimal_clock_growth(300)
        jets=incidence_prime_jets(300)
        for a,b in zip(lcm_rows,jets):
            self.assertEqual(Fraction(a['new_capacity_factor']),b['ratio'],a['horizon'])

    def test_independent_product_exactly_recovers_minimal_clock(self):
        for n in (1,2,3,4,6,8,12,30,60,100,300):
            j=incidence_lcm_compatibility(n)
            L=1
            for k in range(1,n+1):L=lcm(L,k)
            self.assertEqual(j['reconstructed_joint_index'],L)
            self.assertFalse(j['is_full_universal_clock'])

    def test_prime_power_jet_selector_matches_join_irreducibles(self):
        jets=incidence_prime_jets(120)
        active=tuple(j['n'] for j in jets if j['ratio']>1)
        self.assertEqual(active,join_irreducible_periods(120))

    def test_composite_nonprimepower_impulses_vanish(self):
        jets={j['n']:j['ratio'] for j in incidence_prime_jets(40)}
        self.assertEqual(jets[6],1)
        self.assertEqual(jets[10],1)
        self.assertEqual(jets[12],1)
        self.assertEqual(jets[30],1)
        self.assertEqual(jets[8],2)
        self.assertEqual(jets[9],3)
        self.assertEqual(jets[25],5)

    def test_forged_quotient_omission_is_detectable(self):
        gate=missing_incidence_arrow_mutation(6,2)
        self.assertTrue(gate['arrow_was_required'])
        self.assertFalse(gate['source_is_full_quotient_diagram'])
        self.assertTrue(gate['mutation_rejected_by_canonical_divisor_oracle'])
        with self.assertRaises(ClockSourceError):missing_incidence_arrow_mutation(6,4)

    def test_missing_divisor_coefficient_rejected(self):
        mu=incidence_mobius(20)
        del mu[2]
        with self.assertRaises(ClockSourceError):clock_log_increment_ratio(6,mu)

    def test_finite_test_source_never_claims_global_prime_totality(self):
        r=incidence_lcm_compatibility(100)
        self.assertTrue(r['no_prime_or_lcm_oracle_in_source_algorithm'])
        self.assertFalse(r['is_full_universal_clock'])

    def test_input_typing(self):
        with self.assertRaises(ClockSourceError):incidence_mobius(True)
        with self.assertRaises(ClockSourceError):clock_divisors(1.5)
        with self.assertRaises(ClockSourceError):clock_log_increment_ratio(0,{1:1})

if __name__=='__main__':unittest.main()
