"""Independent audits of C20/C21 and the X05 continuation simulator contract."""
import unittest
from scripts.swarm_x05_probe import (
    audit_garbling, audit_minimal_counterexample, audit_policies, audit_transport,
)


class CrossDomainPolicyTransportTests(unittest.TestCase):
    def test_binary_closed_formula_audits_garbling_solver(self):
        self.assertEqual(audit_garbling()['binary_pairs'], 625)

    def test_complete_tree_replay_audits_bellman_solver(self):
        self.assertEqual(audit_policies()['policy_comparisons'], 1548)

    def test_stochastic_intertwiner_preserves_original_joint_history_laws(self):
        result = audit_transport()
        self.assertTrue(result['stochastic_transport'])
        self.assertEqual(result['availability_cost_backaction_mutations_rejected'], 3)

    def test_two_original_state_minimal_erasure_counterexample(self):
        self.assertEqual(audit_minimal_counterexample()['original_states'], 2)


if __name__ == '__main__':
    unittest.main()
