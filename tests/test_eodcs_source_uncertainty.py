"""Source coupling ranges and delayed evidence: exact adversarial controls."""
import unittest
from fractions import Fraction as Q
from itertools import product

from observational_succ.relational_model_genetics import GeneticsError
from observational_succ.eodcs_source_uncertainty import (
    HypothesisMarginals, ConditionalTwoReceipt, EventBatch,
    posterior_both_yes_interval, posterior_two_yes,
    epoch_conditioned_updates, uncertainty_demo,
)
from observational_succ.source_coupling_bounds import frechet_bounds


class TestCouplingPosteriors(unittest.TestCase):
    def test_sharp_interval_beats_assumed_independence(self):
        h = HypothesisMarginals("s", 0, "b", Q(3, 4), Q(3, 4))
        k = HypothesisMarginals("s", 0, "b", Q(1, 4), Q(1, 4))
        r = posterior_both_yes_interval(Q(1, 2), h, k)
        self.assertEqual((r.lower, r.upper), (Q(2, 3), Q(1)))
        self.assertTrue(r.lower < Q(9, 10) < r.upper)
        self.assertEqual(r.h_joint_bounds, (Q(1, 2), Q(3, 4)))
        self.assertEqual(r.k_joint_bounds, (Q(0), Q(1, 4)))

    def test_all_rational_admissible_couplings_land_in_interval(self):
        vals = [Q(i, 4) for i in range(5)]
        for hp, hq, kp, kq in product(vals, repeat=4):
            h = HypothesisMarginals("s", 0, "b", hp, hq)
            k = HypothesisMarginals("s", 0, "b", kp, kq)
            bh, bk = frechet_bounds(hp, hq), frechet_bounds(kp, kq)
            if bh.upper == 0 and bk.upper == 0:
                with self.assertRaises(GeneticsError):
                    posterior_both_yes_interval(Q(1, 2), h, k)
                continue
            r = posterior_both_yes_interval(Q(1, 2), h, k)
            for t in (bh.lower, (bh.lower+bh.upper)/2, bh.upper):
                for u in (bk.lower, (bk.lower+bk.upper)/2, bk.upper):
                    if t + u:
                        posterior = t/(t+u)
                        self.assertLessEqual(r.lower, posterior)
                        self.assertLessEqual(posterior, r.upper)
            self.assertEqual(r.lower, min(r.attainable_corner_posteriors))
            self.assertEqual(r.upper, max(r.attainable_corner_posteriors))

    def test_marginals_do_not_jointly_transport_across_versions(self):
        h = HypothesisMarginals("s", 0, "b", Q(1, 2), Q(1, 2))
        k = HypothesisMarginals("s", 1, "b", Q(1, 2), Q(1, 2))
        with self.assertRaises(GeneticsError):
            posterior_both_yes_interval(Q(1, 2), h, k)

    def test_probability_type_is_exact_only(self):
        with self.assertRaises(GeneticsError):
            HypothesisMarginals("s", 0, "b", 0.75, Q(1, 2))
        with self.assertRaises(GeneticsError):
            HypothesisMarginals("s", -1, "b", Q(1), Q(1))

    def test_second_receipt_is_same_latent_no_double_count(self):
        receipt = ConditionalTwoReceipt("s", 0, "b",
                                        Q(3, 4), Q(1, 4), Q(1), Q(1))
        self.assertEqual(posterior_two_yes(Q(1, 2), receipt), Q(3, 4))

    def test_explicit_independent_conditional_kernel_changes_posterior(self):
        receipt = ConditionalTwoReceipt("s", 0, "b",
                                        Q(3, 4), Q(1, 4), Q(3, 4), Q(1, 4))
        self.assertEqual(posterior_two_yes(Q(1, 2), receipt), Q(9, 10))

    def test_impossible_condition_is_not_explanatory_certainty(self):
        receipt = ConditionalTwoReceipt("s", 0, "b",
                                        Q(0), Q(0), Q(1), Q(1))
        with self.assertRaises(GeneticsError):
            posterior_two_yes(Q(1, 2), receipt)

    def test_prior_extremes_remain_extremes_when_observation_possible(self):
        h = HypothesisMarginals("s", 0, "b", Q(1), Q(1))
        k = HypothesisMarginals("s", 0, "b", Q(1), Q(1))
        self.assertEqual(posterior_both_yes_interval(Q(0), h, k).lower, Q(0))
        self.assertEqual(posterior_both_yes_interval(Q(1), h, k).upper, Q(1))


class TestDelayedUpdates(unittest.TestCase):
    def test_delayed_receipt_updates_event_not_report_epoch(self):
        a = EventBatch("s", "b", 0, 2, Q(3, 4), Q(1, 4))
        b = EventBatch("s", "b", 1, 2, Q(1, 3), Q(2, 3))
        r = epoch_conditioned_updates({0: Q(1, 2), 1: Q(1, 2), 2: Q(1, 2)},
                                       (b, a), source_id="s", basis="b")
        self.assertEqual(r, {0: Q(3, 4), 1: Q(1, 3), 2: Q(1, 2)})

    def test_undeclared_independent_evidence_for_same_epoch_rejected(self):
        a = EventBatch("s", "b", 0, 1, Q(2, 3), Q(1, 3))
        with self.assertRaises(GeneticsError):
            epoch_conditioned_updates({0: Q(1, 2)}, (a, a),
                                       source_id="s", basis="b")

    def test_epoch_prior_is_not_created_from_thin_air(self):
        a = EventBatch("s", "b", 1, 1, Q(2, 3), Q(1, 3))
        with self.assertRaises(GeneticsError):
            epoch_conditioned_updates({0: Q(1, 2)}, (a,),
                                       source_id="s", basis="b")

    def test_source_basis_mismatch_is_a_transport_gap(self):
        a = EventBatch("different", "b", 0, 1, Q(2, 3), Q(1, 3))
        with self.assertRaises(GeneticsError):
            epoch_conditioned_updates({0: Q(1, 2)}, (a,),
                                       source_id="s", basis="b")

    def test_source_event_cannot_arrive_before_it_exists(self):
        with self.assertRaises(GeneticsError):
            EventBatch("s", "b", 2, 1, Q(1), Q(0))

    def test_noisy_evidence_remains_weight_not_deductive_proof(self):
        report = uncertainty_demo()
        self.assertEqual(report["robust_posterior_interval"], ["2/3", "1"])
        self.assertEqual(report["duplicated_conditional_receipt_posterior"], "3/4")
        self.assertEqual(report["new_conditionally_independent_receipt_posterior"], "9/10")
        self.assertEqual(report["source_event_epoch_posteriors"], {"0": "3/4", "1": "1/3"})
        self.assertFalse(report["physical_calibration_claimed"])
        self.assertFalse(report["cross_epoch_transition_assumed"])


if __name__ == "__main__":
    unittest.main()
