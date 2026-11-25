import unittest
from dataclasses import replace
from observational_succ.principia_knowledge_volume import (
    make_source, analyze, target_determined, verify_volume, InvalidLinearSource, rank
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
    def test_knowledge_volume_not_trusted_without_source_replay(self):
        src=make_source([[1,0]],{'swap':[[0,1],[1,0]]})
        actual=analyze(src,2)
        self.assertEqual(verify_volume(src,actual,2),actual)
        with self.assertRaises(InvalidLinearSource):
            verify_volume(src,replace(actual,dimensions=(2,2,2)),2)
    def test_full_exact_rank_can_have_weak_real_resolution(self):
        from fractions import Fraction
        n=1000000
        src=make_source([[1,0]],{'weak':[[1,Fraction(1,n)],[0,1]]})
        vol=analyze(src,1)
        self.assertEqual(vol.dimensions,(1,2))
        self.assertEqual(vol.report_rows[1][1],Fraction(1,n))
        # The two independent rows have determinant only 1/n.
        det=vol.report_rows[0][0]*vol.report_rows[1][1]-vol.report_rows[0][1]*vol.report_rows[1][0]
        self.assertEqual(det,Fraction(1,n))
    def test_no_actions_does_not_invent_future_information(self):
        src=make_source([[1,0]],{})
        self.assertEqual(analyze(src,4).dimensions,(1,1,1,1,1))

if __name__=='__main__':unittest.main()
