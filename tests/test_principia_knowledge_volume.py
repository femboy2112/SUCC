import unittest
from dataclasses import replace
from observational_succ.principia_knowledge_volume import (
    make_source, analyze, target_determined, InvalidLinearSource, rank
)

class KnowledgeVolumeTests(unittest.TestCase):
    def test_hidden_coordinate_emerges_under_swap(self):
        src=make_source([[1,0]],{'swap':[[0,1],[1,0]]})
        k=analyze(src,2)
        self.assertEqual(k.dimensions,(1,2,2))
        self.assertFalse(target_determined(analyze(src,0),[0,1]))
        self.assertTrue(target_determined(analyze(src,1),[0,1]))
        self.assertIn(('swap',),k.independent_paths)
    def test_nilpotent_three_step_chain(self):
        src=make_source([[1,0,0]],{'shift':[[0,1,0],[0,0,1],[0,0,0]]})
        k=analyze(src,4)
        self.assertEqual(k.dimensions,(1,2,3,3,3))
        self.assertTrue(target_determined(k,[0,0,1]))
        self.assertIn(('shift','shift'),k.independent_paths)
    def test_duplicate_reports_and_identity_paths_do_not_increase_rank(self):
        src=make_source([[1,0],[1,0]],{'id':[[1,0],[0,1]],'also_id':[[1,0],[0,1]]})
        k=analyze(src,3)
        self.assertEqual(k.dimensions,(1,1,1,1))
        self.assertEqual(len(k.independent_paths),1)
    def test_source_mutation_rejected(self):
        src=make_source([[1,0]],{'swap':[[0,1],[1,0]]})
        with self.assertRaises(InvalidLinearSource): analyze(replace(src,name='fake'),2)
    def test_nonsquare_action_rejected(self):
        with self.assertRaises(InvalidLinearSource): make_source([[1,0]],{'bad':[[1,0]]})
    def test_exact_rational_rank(self):
        self.assertEqual(rank([[1,0,1],[0,1,1],[1,1,2]],3),2)
    def test_no_actions_does_not_invent_future_information(self):
        src=make_source([[1,0]],{})
        self.assertEqual(analyze(src,4).dimensions,(1,1,1,1,1))

if __name__=='__main__':unittest.main()
