"""Independent binary source-law and incomplete-marginal coupling adversaries."""
import unittest
import random
from fractions import Fraction as Q
from observational_succ.relational_model_genetics import GeneticsError
from observational_succ.source_coupling_bounds import (
    frechet_bounds,JointBinarySource,combine_heuristic_marginals_demo,
)

class TestCouplingBounds(unittest.TestCase):
    def test_example_not_equal_to_independence(self):
        b=frechet_bounds(Q(2,3),Q(3,4))
        self.assertEqual((b.lower,b.independent,b.upper),(Q(5,12),Q(1,2),Q(2,3)))
        for t in (b.lower,b.independent,b.upper):
            src=JointBinarySource('mathematical',0,'two-bit',b.realize(t))
            self.assertEqual((src.p,src.q),(Q(2,3),Q(3,4)))
            self.assertEqual(src.intersection,t)

    def test_exhaustive_grid_frechet_bounds_and_extreme_couplings(self):
        for i in range(13):
            for j in range(13):
                a,b=Q(i,12),Q(j,12)
                interval=frechet_bounds(a,b)
                self.assertLessEqual(interval.lower,interval.upper)
                for t in {interval.lower,interval.upper,interval.independent}:
                    s=JointBinarySource('declared',0,'b',interval.realize(t))
                    self.assertEqual(s.p,a)
                    self.assertEqual(s.q,b)
                    self.assertEqual(s.intersection,t)
                    self.assertEqual(s.verify_independent(),t==a*b)

    def test_rank_lower_bound_for_hidden_conditional_independence(self):
        hi=frechet_bounds(Q(1,2),Q(1,2)).realize(Q(1,2))
        s=JointBinarySource('source',0,'binary',hi)
        self.assertEqual(s.minimum_latent_cardinality_lower_bound,2)
        self.assertEqual(s.det,Q(1,4))
        ind=JointBinarySource('source',0,'binary',frechet_bounds(Q(1,2),Q(1,2)).realize(Q(1,4)))
        self.assertEqual(ind.minimum_latent_cardinality_lower_bound,1)
        self.assertEqual(ind.det,0)

    def test_nonindependent_shared_latent_requires_two_states(self):
        law=JointBinarySource('src',0,'b',((Q(1,2),Q(0)),(Q(0),Q(1,2))))
        self.assertEqual(law.conditional_y_given_x(),((Q(1),Q(0)),(Q(0),Q(1))))
        self.assertEqual(law.minimum_latent_cardinality_lower_bound,2)

    def test_forbidden_probability_in_exact_2x2(self):
        b=frechet_bounds(Q(2,3),Q(3,4))
        for t in (Q(0),Q(1)):
            with self.assertRaises(GeneticsError):b.realize(t)

    def test_unnormalized_and_wrong_source_rejected(self):
        with self.assertRaises(GeneticsError):JointBinarySource('src',0,'b',((Q(1,2),Q(1,2)),(Q(1,2),Q(0))))
        with self.assertRaises(GeneticsError):JointBinarySource('src',0,'b',((Q(-1,4),Q(3,4)),(Q(1,4),Q(1,4))))
        with self.assertRaises(GeneticsError):JointBinarySource('',0,'b',((Q(1),Q(0)),(Q(0),Q(0))))

    def test_float_not_exact_evidence(self):
        with self.assertRaises(GeneticsError):frechet_bounds(.5,Q(1,2))

    def test_static_report_retains_nonquantum_scope(self):
        m=combine_heuristic_marginals_demo()
        self.assertTrue(m['missing_joint_source_implies_no_unique_posterior'])
        self.assertFalse(m['quantum_entanglement_claimed'])

if __name__=='__main__':unittest.main()
