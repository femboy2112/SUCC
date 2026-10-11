"""Source-sensitive local/global equivalence: tested without global leakage."""
import unittest
import subprocess
import sys
import json

from observational_succ import Engine, Frame, ONE, Scalar, run_arithmetic, DomainError, BudgetExceeded
from observational_succ.local_global import compare_local_global, prefix_demo


class LocalGlobalTests(unittest.TestCase):
    def test_same_prefix_future_mutation_invisible(self):
        genuine=run_arithmetic(3)
        mutant=run_arithmetic(12,overrides={6:Scalar("8/7")})
        result=compare_local_global(genuine,mutant,3,shadow_targets=(6,12,30))
        self.assertEqual(result['status'],'equivalent_on_declared_observations')
        self.assertFalse(result['global_suffix_read'])
        self.assertEqual(result['observations_checked'],3)
        self.assertEqual(result['shadow_comparisons'][0]['local_shadow']['weight'],
                         Scalar(-1).data())
        self.assertEqual(result['shadow_comparisons'][1]['local_shadow']['weight'],
                         Scalar(1).data())
        self.assertTrue(all(x['equal'] for x in result['shadow_comparisons']))

    def test_same_mutation_becomes_observable_at_6(self):
        local=run_arithmetic(6)
        mutant=run_arithmetic(12,overrides={6:Scalar("8/7")})
        c=compare_local_global(local,mutant,6)
        self.assertEqual(c['status'],'distinguished')
        self.assertEqual(c['first_difference_at_observation'],6)
        self.assertTrue(c['shadow_comparisons'][0]['local_shadow']['integrated'])
        self.assertTrue(c['shadow_comparisons'][0]['equal'])
        self.assertFalse(c['shadow_comparisons'][0]['source_agrees'])
        self.assertEqual(c['shadow_comparisons'][0]['global_connected_source_restricted']['connected'],
                         Scalar("1/7").data())
        # Both history combinatorics agree; the actualized source differs.
        self.assertEqual(c['shadow_comparisons'][0]['local_shadow']['occurrences'],
                         c['shadow_comparisons'][0]['global_shadow_restricted']['occurrences'])

    def test_pending_future_not_invented(self):
        local=run_arithmetic(2)
        global_model=run_arithmetic(12)
        c=compare_local_global(local,global_model,3)
        self.assertEqual(c['status'],'incomplete_observation')
        self.assertEqual(c['local_integrations'],2)

    def test_model_predictions_can_differ_despite_identical_observations(self):
        a=Engine(arithmetic=True)
        b=Engine(arithmetic=True)
        a.predict(6,ONE,"prediction from A")
        b.predict(6,Scalar("8/7"),"prediction from B")
        for n in range(1,4):
            a.advance(ONE,context="same",probe="arithmetic")
            b.advance(ONE,context="same",probe="arithmetic")
        self.assertNotEqual(a.state['expectations'],b.state['expectations'])
        r=compare_local_global(a,b,3)
        self.assertEqual(r['status'],'equivalent_on_declared_observations')
        self.assertFalse(r['internal_model_equality_claimed'])

    def test_context_is_an_accessible_coordinate(self):
        a,b=Engine(arithmetic=True),Engine(arithmetic=True)
        for _ in range(3):
            a.advance(ONE,context="laboratory",probe="coefficient")
            b.advance(ONE,context="orbit",probe="coefficient")
        self.assertEqual(compare_local_global(a,b,3)['first_difference_at_observation'],1)
        self.assertEqual(compare_local_global(a,b,3,require_same_protocol=False)['status'],
                         'equivalent_on_declared_observations')

    def test_incompatible_frames_or_conductors_rejected(self):
        with self.assertRaises(DomainError):
            compare_local_global(run_arithmetic(1),run_arithmetic(1,kind='chi5'),1)
        with self.assertRaises(DomainError):
            compare_local_global(Engine(Frame('mod','modular',(1,),2)),
                                 run_arithmetic(3),2)

    def test_reversed_history_requires_a_new_comparator(self):
        e=run_arithmetic(3)
        e.reverse_last()
        with self.assertRaises(DomainError):
            compare_local_global(e,run_arithmetic(3),2)

    def test_empty_horizon_or_illegal_shadow(self):
        a,b=run_arithmetic(3),run_arithmetic(3)
        self.assertEqual(compare_local_global(a,b,0,shadow_targets=())['status'],
                         'equivalent_on_declared_observations')
        with self.assertRaises(BudgetExceeded):
            compare_local_global(a,b,3,shadow_targets=(100,))

    def test_cli_new_observation_modes(self):
        cmds=[
            ['yoneda-demo'],
            ['local-global-demo'],
            ['probe-budget','--budget','3','--a','6','--b','12'],
            ['probe-budget','--budget','10000','--lcm-horizon','10000'],
        ]
        out=[]
        for args in cmds:
            result=subprocess.run([sys.executable,'-m','observational_succ']+args,
                                  capture_output=True,text=True,timeout=90)
            self.assertEqual(result.returncode,0,result.stderr)
            out.append(json.loads(result.stdout))
        self.assertTrue(out[0]['comparison']['thin_indistinguishable'])
        self.assertFalse(out[0]['comparison']['path_indistinguishable'])
        self.assertEqual(out[1]['local_at_6_vs_realized_mutant']['first_difference_at_observation'],6)
        self.assertEqual(out[2]['certificate']['verdict'],'indistinguishable_within_budget')
        self.assertEqual(out[3]['certificate']['first_discriminating_value'],'16384')

    def test_demonstration(self):
        r=prefix_demo()
        self.assertEqual(r['local_at_3_vs_future_mutant']['status'],
                         'equivalent_on_declared_observations')
        self.assertEqual(r['local_at_6_vs_realized_mutant']['status'],'distinguished')


if __name__ == '__main__':
    unittest.main()
