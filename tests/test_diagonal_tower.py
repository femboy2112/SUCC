"""Adversarial finite independent controls for the climbing-tower epistemic macro-SUCC."""
import unittest
from dataclasses import replace
from itertools import combinations

from observational_succ.diagonal_tower import (
    DiagonalTower, Link, Node, Probe, SourceModel, TowerError,
    TowerNetwork, completed_climb, ice_climber_tower, destructive_diamond_counterexample,
)


class DiagonalTowerTests(unittest.TestCase):
    def test_three_floor_tower_certifies_top_parity_one_epistemic_step(self):
        t=completed_climb(3,45)
        self.assertEqual(t.known['E'],{'evt:p'+str(i) for i in range(6)})
        self.assertTrue(t.ready())
        c=t.macro_succ()
        self.assertEqual(c.target_value,'1')
        self.assertEqual(c.compatible_sources,('101101',))
        self.assertEqual(c.semantic_minimal,('evt:p4','evt:p5'))
        self.assertEqual(c.causal_closure,tuple('evt:p'+str(i) for i in range(6)))
        self.assertEqual(c.macro_updates,1)
        self.assertEqual(c.transport_count,14)
        self.assertEqual(len(t.issued),6)
        with self.assertRaises(TowerError): t.macro_succ()

    def test_every_source_in_three_floor_universe_replays_and_decides_correctly(self):
        model,_=ice_climber_tower(3)
        for i in range(len(model.sources)):
            c=completed_climb(3,i).macro_succ()
            self.assertEqual(c.target_value,model.target[i])
            self.assertEqual(c.compatible_sources,(model.sources[i],))
            self.assertEqual(set(c.semantic_minimal),{'evt:p4','evt:p5'})
            self.assertEqual(len(c.causal_closure),6)

    def test_climbing_cannot_skip_joint_prerequisites(self):
        m,g=ice_climber_tower()
        t=DiagonalTower(m,g)
        with self.assertRaisesRegex(TowerError,'prerequisite'):
            t.perform_probe('A1',45)
        t.perform_probe('A0',45)
        t.perform_probe('B0',45)
        t.transmit('A0','A1')
        with self.assertRaisesRegex(TowerError,'prerequisite'):
            t.perform_probe('A1',45)
        t.transmit('B0','A1')
        t.perform_probe('A1',45)
        with self.assertRaisesRegex(TowerError,'prerequisite'):
            t.perform_probe('A2',45)

    def test_early_top_floor_values_do_not_launder_physical_history(self):
        t=completed_climb(3,45,descend=False)
        for level in (2,1):
            t.transmit(f'A{level}',f'B{level-1}')
            t.transmit(f'B{level}',f'A{level-1}')
        t.transmit('A0','E',('evt:p4',))
        t.transmit('B0','E',('evt:p5',))
        self.assertEqual(t.semantic_target(t.known['E']),'1')
        self.assertFalse(t.ready())
        with self.assertRaisesRegex(TowerError,'down-closure'):
            t.macro_succ()
        t.transmit('A0','E')
        # The second leg has no remaining delta: the proof is a union, not
        # a double-counting of records forwarded along multiple routes.
        self.assertTrue(t.ready())
        self.assertEqual(t.macro_succ().target_value,'1')

    def test_asynchronous_base_delivery_confluent(self):
        a=completed_climb(3,45,descend=False)
        b=completed_climb(3,45,descend=False)
        for t in (a,b):
            for level in (2,1):
                t.transmit(f'A{level}',f'B{level-1}')
                t.transmit(f'B{level}',f'A{level-1}')
        a.transmit('A0','E');a.transmit('B0','E')
        b.transmit('B0','E');b.transmit('A0','E')
        self.assertEqual(a.known['E'],b.known['E'])
        self.assertEqual(a.macro_succ().compatible_sources,b.macro_succ().compatible_sources)
        self.assertEqual(a.last_certificate.semantic_minimal,b.last_certificate.semantic_minimal)

    def test_duplicate_transmissions_idempotent_but_explicit(self):
        t=completed_climb(3,45)
        before=set(t.known['E'])
        t.transmit('A0','E',('evt:p4',))
        self.assertEqual(before,t.known['E'])
        self.assertEqual(t.macro_succ().target_value,'1')
        with self.assertRaisesRegex(TowerError,'Empty'):
            t.transmit('A0','E')

    def test_missing_independence_not_assumed_from_multiple_climbers(self):
        t=completed_climb(3,45)
        source_bit=t.model.probes[0].outputs
        self.assertTrue(all(z in ('0','1') for z in source_bit))
        self.assertEqual(len(t.issued),6)
        # This source-space count (64) is declared and independently validated;
        # distinct observer names do not supply independent source evidence.
        self.assertEqual(len(t.model.sources),64)
        self.assertEqual(t.semantic_target(('evt:p0',)),None)
        self.assertEqual(t.semantic_target(('evt:p1',)),None)

    def test_fiber_intersection_commutes_on_all_received_subsets(self):
        t=completed_climb(3,45)
        ids=sorted(t.known['E'])
        all_subsets=[frozenset(s) for k in range(7) for s in combinations(ids,k)]
        for i in range(0,len(all_subsets),5):
            a=all_subsets[i]
            for j in range(0,len(all_subsets),7):
                b=all_subsets[j]
                left=set(t.source_fiber(a | b))
                right=set(t.source_fiber(a)) & set(t.source_fiber(b))
                self.assertEqual(left,right)

    def test_unlicensed_link_is_not_an_epistemic_transfer(self):
        t=completed_climb()
        with self.assertRaisesRegex(TowerError,'Unlicensed'):
            t.transmit('A2','E')
        with self.assertRaisesRegex(TowerError,'Unlicensed'):
            t.transmit('E','A0')
        with self.assertRaisesRegex(TowerError,'unowned'):
            t.transmit('A0','E',('evt:unissued',))
        with self.assertRaisesRegex(TowerError,'duplicate'):
            t.transmit('A0','E',('evt:p0','evt:p0'))

    def test_cross_lane_descent_and_one_level_type_safety(self):
        with self.assertRaisesRegex(TowerError,'diagonally'):
            TowerNetwork((Node('E',-1,'E'),Node('A1',1,'A'),Node('A0',0,'A')),
                         (Link('A1','A0','descent'),))
        with self.assertRaisesRegex(TowerError,'exactly one floor'):
            TowerNetwork((Node('E',-1,'E'),Node('A2',2,'A'),Node('B0',0,'B')),
                         (Link('A2','B0','descent'),))

    def test_missing_parent_and_forged_context_rejected(self):
        for mutation in (lambda r: replace(r,parent_ids=()),
                         lambda r: replace(r,source_id='other-source'),
                         lambda r: replace(r,basis_id='basis-v2'),
                         lambda r: replace(r,origin='B2'),
                         lambda r: replace(r,level=0)):
            t=completed_climb()
            t.issued['evt:p4']=mutation(t.issued['evt:p4'])
            with self.assertRaises(TowerError): t.macro_succ()

    def test_cannot_change_true_source_mid_climb_or_remeasure(self):
        m,g=ice_climber_tower()
        t=DiagonalTower(m,g)
        t.perform_probe('A0',45)
        with self.assertRaisesRegex(TowerError,'replayed'):
            t.perform_probe('A0',45)
        with self.assertRaisesRegex(TowerError,'Inconsistent true source'):
            t.perform_probe('B0',44)

    def test_E_requires_nonempty_evidence_and_a_sufficient_goal(self):
        m,g=ice_climber_tower()
        t=DiagonalTower(m,g)
        with self.assertRaisesRegex(TowerError,'No received'):
            t.macro_succ()
        t.perform_probe('A0',45);t.perform_probe('B0',45)
        t.transmit('A0','E');t.transmit('B0','E')
        self.assertFalse(t.ready())
        with self.assertRaisesRegex(TowerError,'indistinguishable'):
            t.macro_succ()

    def test_stable_metadata_not_authenticated_source_truth(self):
        t=completed_climb()
        old=t.issued['evt:p0']
        t.issued['evt:p0']=replace(old,observed=('1' if old.observed=='0' else '0'))
        # If someone can overwrite the stipulated trusted registry, the
        # mathematics cannot detect source-tampering by inspecting labels.
        c=t.macro_succ()
        self.assertEqual(c.target_value,'1')
        self.assertNotEqual(c.compatible_sources,('101101',))

    def test_multiple_tower_heights_and_single_epistemic_commit(self):
        for levels in (2,3,4):
            t=completed_climb(levels,2**(2*levels)-3)
            c=t.macro_succ()
            self.assertEqual(len(c.semantic_minimal),2)
            self.assertEqual(len(c.causal_closure),2*levels)
            self.assertEqual(c.macro_updates,1)
            self.assertGreater(c.transport_count,1)

    def test_reject_incompatible_source_and_duplicate_names(self):
        m,g=ice_climber_tower()
        with self.assertRaises(TowerError):
            SourceModel(m.source_id,m.basis_id,('s0','s0'),m.probes,m.target)
        with self.assertRaises(TowerError):
            SourceModel(m.source_id,m.basis_id,m.sources,m.probes+(m.probes[0],),m.target)
        with self.assertRaises(TowerError):
            DiagonalTower(m,TowerNetwork((Node('E',-1,'E'),),( )))


    def test_readiness_explicitly_distinguishes_semantic_and_causal_lamps(self):
        t=completed_climb(3,45,descend=False)
        self.assertEqual(t.readiness_report()['status'],'NO_EVIDENCE')
        for level in (2,1):
            t.transmit(f'A{level}',f'B{level-1}')
            t.transmit(f'B{level}',f'A{level-1}')
        t.transmit('A0','E',('evt:p4',))
        t.transmit('B0','E',('evt:p5',))
        first=t.readiness_report()
        self.assertEqual(first['semantic_target'],'1')
        self.assertEqual(first['status'],'CAUSAL_RECEIPTS_MISSING')
        self.assertEqual(first['missing_causal_ids'],tuple(f'evt:p{i}' for i in range(4)))
        t.transmit('A0','E')
        self.assertEqual(t.readiness_report()['status'],'PROOF_READY')
        self.assertEqual(t.proof_costs()['receiver_epistemic_macro_updates'],0)
        t.macro_succ()
        self.assertEqual(t.proof_costs()['receiver_epistemic_macro_updates'],1)
        self.assertEqual(t.proof_costs()['local_physical_measurements'],6)
        self.assertGreater(t.proof_costs()['event_references_carried'],6)

    def test_unresolved_claim_has_rival_pair_replaying_same_observations(self):
        m,g=ice_climber_tower()
        t=DiagonalTower(m,g)
        t.perform_probe('A0',45);t.transmit('A0','E')
        report=t.readiness_report()
        self.assertEqual(report['status'],'UNRESOLVED_CLAIM')
        x,y=report['countermodel_pair']
        ix,iy=m.sources.index(x),m.sources.index(y)
        self.assertNotEqual(m.target[ix],m.target[iy])
        self.assertEqual(m.probe('p0').outputs[ix],m.probe('p0').outputs[iy])

    def test_top_branch_cut_blocks_proof_but_not_other_descents(self):
        t=completed_climb(3,45,descend=False)
        t.transmit('B2','A1')
        # The A2->B1 diagonal is deliberately unavailable in this schedule.
        t.transmit('B1','A0')
        t.transmit('A1','B0')
        t.transmit('A0','E');t.transmit('B0','E')
        r=t.readiness_report()
        self.assertEqual(r['status'],'UNRESOLVED_CLAIM')
        self.assertIsNone(r['semantic_target'])
        self.assertNotIn('evt:p4',t.known['E'])
        with self.assertRaises(TowerError):t.macro_succ()
        # Repair with one truthful authorized diagonal; no private source access at E.
        t.transmit('A2','B1')
        t.transmit('B1','A0')
        t.transmit('A0','E')
        self.assertEqual(t.readiness_report()['status'],'PROOF_READY')
        self.assertEqual(t.macro_succ().target_value,'1')


    def test_destructive_actions_do_not_commute_as_evidence(self):
        r=destructive_diamond_counterexample()
        self.assertEqual(r['AB_observations'],{'A':1,'B':0})
        self.assertEqual(r['BA_observations'],{'A':0,'B':1})
        self.assertEqual(r['common_endpoint'],(0,0))
        self.assertFalse(r['commuting_evidence_square'])

    def test_forged_absent_parent_returns_typed_error(self):
        t=completed_climb()
        r=t.issued['evt:p4']
        t.issued['evt:p4']=replace(r,parent_ids=('evt:nonexistent',))
        with self.assertRaisesRegex(TowerError,'Unissued causal parent'):
            t.macro_succ()


if __name__=='__main__':
    unittest.main()
