"""Correlated-observation source certificates independently reject double counting."""
import unittest
from fractions import Fraction as Q
from observational_succ.contextual_heuristics import ModelProbe, HeuristicError
from observational_succ.heuristic_joint_noise import FiniteJointNoise,repeated_measurement_witness


class JointNoiseTests(unittest.TestCase):
    def test_same_physical_latent_replayed_is_not_new_independent_evidence(self):
        w=repeated_measurement_witness()
        self.assertTrue(w["initial_source"]["source_conditional_law_verified"])
        self.assertFalse(w["naive_reuse"]["source_conditional_law_verified"])
        self.assertTrue(w["sourced_conditional"]["source_conditional_law_verified"])
        self.assertEqual(w["naive_reuse"]["first_witness"][0],"H0")

    def test_genuinely_independent_product_noise_changes_second_likelihood(self):
        # Two independent Bernoulli(1/2) bits on 4 equally likely latent states.
        law=FiniteJointNoise(
            weights={"H":(Q(1,4),)*4},
            outcome_tables={"H":{"first":("yes","yes","no","no"),
                                 "second":("yes","no","yes","no")}})
        next_probe=ModelProbe("second","c",("yes","no"),{"H":(Q(1,2),Q(1,2))})
        self.assertTrue(law.verify_claimed_conditional(next_probe,(("first","yes"),))["source_conditional_law_verified"])

    def test_joint_source_incomplete_table_rejected(self):
        with self.assertRaises(HeuristicError):
            FiniteJointNoise({"H":(Q(1,2),Q(1,2))},{"H":{"bad":("y",)}})

    def test_false_kernel_has_exact_counterexample(self):
        source=FiniteJointNoise({"H":(Q(2,3),Q(1,3))},
                                {"H":{"p":("y","n")}})
        forged=ModelProbe("p","c",("y","n"),{"H":(Q(1,2),Q(1,2))})
        r=source.verify_claimed_conditional(forged)
        self.assertFalse(r["source_conditional_law_verified"])
        self.assertEqual(r["first_witness"],("H",(Q(2,3),Q(1,3)),
                                             (Q(1,2),Q(1,2))))

    def test_observation_history_not_source_zero_probability(self):
        source=FiniteJointNoise({"H":(Q(1,2),Q(1,2))},{"H":{"p":("y","n")}})
        with self.assertRaises(HeuristicError):
            source.conditioned_distribution("H","p",("y","n"),(("p","alien"),))

if __name__=="__main__":unittest.main()
