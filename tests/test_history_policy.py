"""Prospectively registered source-only experiment-selection policy."""
import importlib.util
from pathlib import Path
from unittest.mock import patch
from fractions import Fraction as Q
import unittest
P=Path(__file__).resolve().parents[1]/'research/2026-11-05/history_shell/history_policy.py'
spec=importlib.util.spec_from_file_location('history_policy',P)
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)

class HistoryPolicy(unittest.TestCase):
    def test_01_source_only_probe_choice_does_not_require_selected_history(self):
        with patch.object(p,'original_epoch',side_effect=AssertionError('selected state forbidden during choice')):
            for A,d in ((211,5),(419,5),(829,6)):
                v=p.source_only_candidates(A,d)
                self.assertEqual(len(v),3)
                self.assertGreater(v[0][0],v[1][0])
                self.assertEqual(v[0][3],3)

    def test_02_preregistered_fresh_original_branch_counts(self):
        expected={(211,5):(2,3,39),(419,5):(2,3,15),(829,6):(3,3,153)}
        for (A,d),(m,k,count) in expected.items():
            v=p.choose_then_observe(A,d)
            self.assertEqual((v['m'],v['k'],v['selected']),(m,k,count))
            self.assertTrue(v['coherent_certified'])
            self.assertNotEqual(v['expected'],Q(count))

    def test_03_brier_score_not_a_truth_or_authentication_metric(self):
        for A,d in ((211,5),(419,5),(829,6)):
            v=p.choose_then_observe(A,d)
            self.assertGreater(v['brier_selected'],v['brier_coherent'])
            self.assertGreater(v['brier_reference'],0)
            self.assertTrue(-1<float(v['selected_innovation'])<1)

if __name__=='__main__':unittest.main()
