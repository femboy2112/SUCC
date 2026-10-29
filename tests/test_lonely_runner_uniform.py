import itertools
import unittest
from fractions import Fraction as F

from observational_succ.lonely_runner_uniform import (
    AffineRunner,UniformRule,poliakova_rule,responsible_residues,resonance_interval,
    coverage_gap,check_local_uniform,gap_counterexample,circle_distance,
    resonant_phase_candidates,useful_beta_bound,binary_ladder_rule,binary_ladder_condition,
    compress_added_velocities,
)


class UniformRuleTests(unittest.TestCase):
    def test_literal_published_rule_all_residue_cells(self):
        rule=poliakova_rule();receipt=check_local_uniform(rule)
        self.assertEqual(rule.removed,(8,32,192))
        self.assertEqual(rule.gain,1);self.assertEqual(rule.largest_affected,192)
        self.assertTrue(receipt['local_uniform']);self.assertEqual(receipt['checked_cells'],184)

    def test_closed_interval_endpoints_and_real_gaps(self):
        self.assertIsNone(coverage_gap([(F(-1),F(0)),(F(0),F(1))]))
        self.assertEqual(coverage_gap([(F(-1),F(-1,3)),(F(1,3),F(1))]),0)
        self.assertEqual(coverage_gap([(F(-9,10),F(1))]),-1)
        self.assertEqual(coverage_gap([(F(-1),F(9,10))]),1)
        self.assertEqual(resonance_interval(8,1,AffineRunner(12,F(1,2),F(1,2))),
                         (F(-1),F(1,3)))
        self.assertIsNone(resonance_interval(8,1,AffineRunner(12,F(0),F(1,2))))

    def test_q_over_two_unit_condition_rejects_false_rule(self):
        self.assertEqual(responsible_residues(6),(1,2,4,5))
        # Checking gcd(k,q)=1 instead would incorrectly certify this rule.
        rule=UniformRule((6,),(),(AffineRunner(3,F(1,2),F(0)),))
        receipt=check_local_uniform(rule)
        self.assertFalse(receipt['local_uniform']);self.assertEqual(receipt['gap']['k'],2)
        counter=gap_counterexample(rule,**receipt['gap'])
        self.assertGreater(F(counter['rescuer_distances']['3']),F(counter['delta']))

    def test_naive_192_to_190_mutation_actual_counterexample(self):
        baseline=poliakova_rule()
        rule=UniformRule((8,32,190),baseline.rephased,baseline.added)
        receipt=check_local_uniform(rule)
        self.assertEqual(receipt['gap'],{'q':190,'k':1,'z':'-1'})
        counter=gap_counterexample(rule,**receipt['gap'])
        self.assertEqual((counter['N'],counter['time']),(192,'96/18335'))
        delta,time=F(counter['delta']),F(counter['time'])
        self.assertTrue(all(circle_distance(q*time)>delta for q in range(2,190,2)))
        self.assertEqual(circle_distance(190*time),delta)
        self.assertTrue(all(F(d)>delta for d in counter['rescuer_distances'].values()))

    def test_negative_raw_time_is_normalized_and_valid(self):
        rule=UniformRule((2,),(),())
        counter=gap_counterexample(rule,2,0,F(-1))
        time=F(counter['time']);self.assertTrue(0<=time<1)
        self.assertLessEqual(circle_distance(2*time),F(counter['delta']))

    def test_resonant_phase_and_beta_reductions_are_exact(self):
        rule=poliakova_rule()
        for runner in rule.rescuers:
            self.assertIn(runner.alpha,resonant_phase_candidates(rule,runner.velocity))
            bound=useful_beta_bound(rule,runner.velocity)
            self.assertLessEqual(abs(runner.beta),bound)
            useless=AffineRunner(runner.velocity,runner.alpha,bound+1)
            self.assertTrue(all(resonance_interval(q,k,useless) is None
                                for q in rule.affected for k in responsible_residues(q)))

    def test_binary_ladder_full_pattern_classification_small_depths(self):
        for depth in range(2,6):
            exponents=tuple(range(3,depth+2));valid=[]
            for mask in itertools.product((False,True),repeat=len(exponents)):
                removed=tuple(k for k,b in zip(exponents,mask) if b)
                rule=binary_ladder_rule(depth,removed)
                actual=check_local_uniform(rule)['local_uniform']
                self.assertEqual(actual,binary_ladder_condition(depth,removed))
                if actual:valid.append((len(removed),removed))
            maximum=max(n for n,_ in valid)
            self.assertEqual(maximum,(depth-1)//2)
            if depth==5:self.assertEqual([r for n,r in valid if n==maximum],[(3,5)])

    def test_first_gain_and_larger_attaining_patterns(self):
        for depth in range(2,9):
            removed=tuple(range(3,depth+1,2))
            rule=binary_ladder_rule(depth,removed)
            self.assertTrue(binary_ladder_condition(depth,removed))
            self.assertEqual(rule.gain,(depth-1)//2-1)
            if rule.gain>0:self.assertGreaterEqual(rule.largest_affected,192)
        self.assertEqual(binary_ladder_rule(5,(3,5)),poliakova_rule())

    def test_added_velocity_compression_resonance_and_interval_inclusion(self):
        rule=UniformRule((4,6),(),(AffineRunner(37,F(1,4),F(1,3)),
            AffineRunner(13,F(2,3),F(-2)),AffineRunner(25,F(1,2),F(3))))
        compressed=compress_added_velocities(rule)
        self.assertEqual(tuple(r.velocity for r in compressed.added),(25,1,13))
        self.assertEqual(compressed.gain,rule.gain)
        for before,after in zip(rule.added,compressed.added):
            self.assertLessEqual(after.velocity,before.velocity)
            self.assertLess(after.velocity,3*12)
            self.assertEqual(after.alpha,before.alpha)
            self.assertEqual(after.beta,F(after.velocity,before.velocity)*before.beta)
            for q in rule.affected:
                for k in responsible_residues(q):
                    self.assertEqual((F(before.velocity*k,q)+before.alpha)%1,
                                     (F(after.velocity*k,q)+after.alpha)%1)
                    old=resonance_interval(q,k,before)
                    if old is not None:
                        new=resonance_interval(q,k,after)
                        self.assertIsNotNone(new)
                        self.assertLessEqual(new[0],old[0]);self.assertGreaterEqual(new[1],old[1])

    def test_compression_preserves_actual_local_rule_and_empty_case(self):
        base=poliakova_rule()
        inflated=UniformRule(base.removed,base.rephased,
            base.added+(AffineRunner(1347,F(0),F(7)),))
        compressed=compress_added_velocities(inflated)
        self.assertEqual(compressed.added[-1].velocity,195)
        self.assertTrue(check_local_uniform(inflated)['local_uniform'])
        self.assertTrue(check_local_uniform(compressed)['local_uniform'])
        empty=UniformRule((),(AffineRunner(2,F(0),F(0)),),())
        self.assertEqual(compress_added_velocities(empty),empty)

    def test_domain_and_false_counterexample_guards(self):
        with self.assertRaises(TypeError):AffineRunner(3,0.25,0)
        with self.assertRaises(ValueError):UniformRule((3,),(),())
        with self.assertRaises(ValueError):UniformRule((4,),(AffineRunner(4,0,0),),())
        with self.assertRaises(ValueError):binary_ladder_rule(1,())
        with self.assertRaises(ValueError):binary_ladder_rule(3,(3,3))
        with self.assertRaises(ValueError):gap_counterexample(poliakova_rule(),8,1,0)


if __name__=='__main__':unittest.main()
