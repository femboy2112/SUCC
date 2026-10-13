"""Source-relative, causally licensed parallel E observer network tests."""
import unittest
from fractions import Fraction as F
from observational_succ.covariant_observer_frames import (
   LorentzFrame,EventPoint,CausalEvent,CausalLedger,FrameError)
from observational_succ.asynchronous_e_tower import (
   OriginalCarrierTheory,EvidenceTower,TowerError,asynchronous_e_demo)


class AsynchronousEProofTests(unittest.TestCase):
    def setUp(self):
        self.theory=OriginalCarrierTheory('S','bits-1',('00','01','10','11'),
                            {'a':(0,0,1,1),'b':(0,1,0,1)},
                            {'XOR':(0,1,1,0),'a':(0,0,1,1)})
        self.ledger=CausalLedger((
             CausalEvent('a',EventPoint(0,-1),'probe','S',(),('a',1,'bits-1')),
             CausalEvent('b',EventPoint(0,1),'probe','S',(),('b',0,'bits-1')),
             CausalEvent('E1',EventPoint(1,0),'checkpoint','S',('a',)),
             CausalEvent('E2',EventPoint(2,0),'checkpoint','S',('b','E1')),
             CausalEvent('E0',EventPoint(0,0),'checkpoint','S')))
        self.tower=EvidenceTower(self.ledger,self.theory)

    def test_two_spacelike_probes_travel_at_lightspeed_then_conclude(self):
        self.assertEqual(self.tower.decide('E0','XOR')['status'],'UNRESOLVED')
        self.assertEqual(self.tower.decide('E1','XOR')['status'],'UNRESOLVED')
        self.assertEqual(self.tower.decide('E2','XOR')['status'],'PROVED')
        self.assertEqual(self.tower.decide('E2','XOR')['claim_value'],1)
        self.assertEqual(self.tower.decide('E2','XOR')['causal_probe_count'],2)
        self.assertEqual(self.tower.decide('E1','a')['claim_value'],1)

    def test_original_source_not_recovered_from_hidden_simulator_label(self):
        self.assertEqual(self.theory.simulated_probe('a','10'),1)
        self.assertEqual(self.theory.simulated_probe('b','10'),0)
        result=self.tower.decide('E2','XOR')
        self.assertNotIn('original_source',result)
        self.assertFalse(result['physical_sensor_authentication'])

    def test_minimal_proof_support_exact(self):
        d=self.tower.minimal_support('E2','XOR')
        self.assertEqual(d['minimum_size'],2)
        self.assertEqual(d['support'],('a','b'))
        self.assertEqual(self.tower.minimal_support('E1','XOR')['status'],'UNRESOLVED')
        self.assertEqual(self.tower.minimal_support('E1','a')['minimum_size'],1)

    def test_coordinates_do_not_change_certified_ancestry(self):
        B=LorentzFrame.boost('x',F(1,3))
        r=self.tower.claim_frame_invariance('E0','XOR',LorentzFrame.identity(),B)
        self.assertTrue(r['different_coordinate_cuts'])
        self.assertTrue(r['same_causal_receipts'])
        self.assertEqual(r['causal_receipt_count'],0)
        r2=self.tower.claim_frame_invariance('E2','XOR',LorentzFrame.identity(),B)
        self.assertEqual(r2['decision'],'PROVED')

    def test_parent_relay_is_not_implied_by_common_carrier(self):
        led=CausalLedger((self.ledger.get('a'),self.ledger.get('b'),
                  CausalEvent('E',EventPoint(4,0),'checkpoint','S',('a',))))
        tower=EvidenceTower(led,self.theory)
        self.assertEqual(tower.decide('E','XOR')['status'],'UNRESOLVED')

    def test_impossible_instant_reception_rejected(self):
        with self.assertRaises(FrameError):
            CausalLedger((self.ledger.get('a'),
              CausalEvent('E',EventPoint(0,0),'checkpoint','S',('a',))))

    def test_wrong_basis_and_probe_names_rejected(self):
        with self.assertRaises(TowerError):
            EvidenceTower(CausalLedger((CausalEvent('x',EventPoint(0,0),'probe','S',(),('a',0,'old')),)),self.theory)
        with self.assertRaises(TowerError):
            EvidenceTower(CausalLedger((CausalEvent('x',EventPoint(0,0),'probe','S',(),('unknown',0,'bits-1')),)),self.theory)

    def test_wrong_carrier_identity_rejected(self):
        alt=OriginalCarrierTheory('ANOTHER','bits-1',('00','01','10','11'),
                                  self.theory.probes,self.theory.claims)
        with self.assertRaises(TowerError):EvidenceTower(self.ledger,alt)

    def test_pairwise_consistent_but_jointly_false_receipts_rejected(self):
        led=CausalLedger((
            CausalEvent('a0',EventPoint(0,-1),'probe','S',(),('a',0,'bits-1')),
            CausalEvent('a1',EventPoint(0,1),'probe','S',(),('a',1,'bits-1')),
            CausalEvent('E',EventPoint(1,0),'checkpoint','S',('a0','a1'))))
        self.assertEqual(EvidenceTower(led,self.theory).decide('E','XOR')['status'],
                         'INCONSISTENT_SOURCE')

    def test_documented_carrier_theory_immutable_after_construction(self):
        mutable={'a':(0,0,1,1)}
        t=OriginalCarrierTheory('S','b',(0,1,2,3),mutable,{'A':(0,0,1,1)})
        mutable['a']=(1,1,1,1)
        self.assertEqual(t.probes['a'],(0,0,1,1))
        with self.assertRaises(TypeError):t.probes['a']=(1,1,1,1)

    def test_no_unbounded_physical_claims_in_demo(self):
        report=asynchronous_e_demo()
        self.assertEqual(report['early_status'],'UNRESOLVED')
        self.assertEqual(report['late_status'],'PROVED')
        self.assertFalse(report['real_carrier_authentication'])

    def test_undelivered_probe_does_not_exist_for_receiver(self):
        r=self.tower.decide('E1','XOR')
        self.assertNotIn('b',r['causal_probes'])
        self.assertEqual(r['causal_probes'],('a',))


if __name__=='__main__':unittest.main()

class CofinalCheckpointTests(unittest.TestCase):
    def test_two_asynchronous_E_chains_converge_without_same_clock(self):
        theory=OriginalCarrierTheory('S','bits-1',('00','01','10','11'),
                    {'a':(0,0,1,1),'b':(0,1,0,1)}, {'XOR':(0,1,1,0)})
        led=CausalLedger((
           CausalEvent('a',EventPoint(0,-1),'probe','S',(),('a',1,'bits-1')),
           CausalEvent('b',EventPoint(0,1),'probe','S',(),('b',0,'bits-1')),
           CausalEvent('A1',EventPoint(1,-F(1,2)),'checkpoint','S',('a',)),
           CausalEvent('B1',EventPoint(1,F(1,2)),'checkpoint','S',('b',)),
           CausalEvent('A2',EventPoint(3,-F(1,2)),'checkpoint','S',('A1','b')),
           CausalEvent('B2',EventPoint(4,F(1,2)),'checkpoint','S',('B1','a'))))
        tower=EvidenceTower(led,theory)
        A=tower.checkpoint_chain(('A1','A2'),'XOR')
        B=tower.checkpoint_chain(('B1','B2'),'XOR')
        self.assertEqual(A['first_proof_index'],1)
        self.assertEqual(B['first_proof_index'],1)
        self.assertEqual(A['final_claim_value'],B['final_claim_value'])
        self.assertEqual(A['final_claim_value'],1)
        self.assertEqual(set(A['final_probe_ids']),set(B['final_probe_ids']))

    def test_checkpoint_chain_cannot_skip_earlier_source_history(self):
        theory=OriginalCarrierTheory('S','b',(0,1),{'read':(0,1)},{'t':(0,1)})
        led=CausalLedger((
             CausalEvent('p',EventPoint(0,0),'probe','S',(),('read',1,'b')),
             CausalEvent('A',EventPoint(1,0),'checkpoint','S',('p',)),
             CausalEvent('B',EventPoint(2,0),'checkpoint','S',('p',))))
        tower=EvidenceTower(led,theory)
        with self.assertRaisesRegex(TowerError,'not causally descended'):
            tower.checkpoint_chain(('A','B'),'t')
        self.assertEqual(tower.checkpoint_chain(('A',),'t')['first_proof_index'],0)

