"""Regression: rederive saved source-typed Bayesian/shape receipts from live code."""
import json
import unittest
from pathlib import Path
from fractions import Fraction as Q

from observational_succ.heuristic_bridge_discovery import holdout_shape_demo
from observational_succ.heuristic_joint_noise import repeated_measurement_witness
from observational_succ.contextual_heuristics import syntax_clone_counterexample
from observational_succ.heuristic_shape_learning import learning_demo
from observational_succ.heuristic_evidence_martingales import adaptive_crossing_probability


def to_json(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,dict):return {str(k):to_json(x) for k,x in v.items()}
    if isinstance(v,(tuple,list)):return [to_json(x) for x in v]
    return v


class SavedHeuristicReceipt(unittest.TestCase):
    def test_saved_source_model_sections_are_recomputed(self):
        repo=Path(__file__).resolve().parent.parent
        saved=json.loads((repo/'research/2026-10-12/CONTEXTUAL_HEURISTIC_RECEIPT.json').read_text())
        self.assertEqual(saved['positive_stieltjes_alias'],to_json(holdout_shape_demo()))
        self.assertEqual(saved['shared_latent_double_count_rejected'],to_json(repeated_measurement_witness()))
        self.assertEqual(saved['syntax_duplicate_counterexample'],to_json(syntax_clone_counterexample()))
        self.assertEqual(saved['learned_analogy'],to_json(learning_demo()))
        self.assertFalse(saved['physical_source_authenticated'])
        self.assertFalse(saved['Weil_positivity_or_RH_proved'])

if __name__=='__main__': unittest.main()
