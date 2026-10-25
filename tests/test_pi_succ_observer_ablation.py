"""Full factorial readout, source holdout and adversarial no-leak controls."""
from fractions import Fraction as Q
from itertools import combinations
import unittest

from observational_succ.pi_succ_observer_ablation import (
    SourceObservation, source_observations, certified_digit_at_n,
    dyadic_residue, complete_factorial, full_four_way_interaction,
    feature_mutation, train_exact_model, brier_error,
)
from observational_succ.bbp_natural_carrier import exact_forcing, certified_hex_digit

class JointFactorialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows=source_observations(16,560)

    def test_source_digit_certificates_against_independent_exact_machine(self):
        for row in self.rows[:50]:
            d=certified_hex_digit(row.n,8)
            self.assertIsNotNone(d)
            self.assertEqual(row.digit,d[0])
        self.assertTrue(all(0<=r.digit<16 for r in self.rows))

    def test_predeclared_disjoint_holdout(self):
        self.assertEqual(self.rows[0].n,16)
        train=tuple(r for r in self.rows if 16<=r.n<256)
        test=tuple(r for r in self.rows if 256<=r.n<512)
        self.assertFalse(set(r.n for r in train)&set(r.n for r in test))
        f=complete_factorial(train,test)
        self.assertEqual(len(f),16)
        self.assertTrue(all(isinstance(x,Q) and x>=0 for x in f.values()))
        self.assertTrue(isinstance(full_four_way_interaction(f),Q))

    def test_all_16_required_to_calculate_interaction(self):
        rows=self.rows[:32]
        f=complete_factorial(rows[:16],rows[16:32])
        f.pop((0,1,2,3))
        with self.assertRaises(ValueError): full_four_way_interaction(f)

    def test_reindexed_prime_mutant_breaks_source_alignment(self):
        train=self.rows[:240];test=self.rows[240:]
        mutated=feature_mutation(test,3,7)
        self.assertEqual([r.zero_gate for r in mutated],[r.zero_gate for r in test])
        self.assertTrue(any(a.features[3]!=b.features[3] for a,b in zip(mutated,test)))
        out=complete_factorial(train,mutated)
        self.assertEqual(len(out),16)

    def test_full_observation_does_not_mechanically_force_gate(self):
        # An exactly constant gate has perfect Brier prediction independent
        # of the number of instrument families; a feature tower alone does
        # not establish Haar frequencies or any normality theorem.
        train=tuple(SourceObservation(n,0,(n%2,n%3,n%5,n%7),0)
                   for n in range(1,97))
        hold=tuple(SourceObservation(n,0,(n%2,n%3,n%5,n%7),0)
                   for n in range(97,193))
        f=complete_factorial(train,hold)
        self.assertEqual(len(f),16)
        self.assertTrue(all(x>=0 for x in f.values()))
        self.assertTrue(all(r.zero_gate==1 for r in hold))

    def test_source_checks_and_input_rejection(self):
        with self.assertRaises(ValueError):dyadic_residue(Q(1,2),4)
        with self.assertRaises(ValueError):source_observations(0,20)
        with self.assertRaises(ValueError):certified_digit_at_n(0,Q())
        with self.assertRaises(ValueError):feature_mutation(self.rows,5)
        with self.assertRaises(ValueError):complete_factorial((),self.rows)

if __name__=='__main__':unittest.main()
