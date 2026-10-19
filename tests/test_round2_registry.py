"""Actual integrated graph controls; metadata checks do not prove its prose."""
from copy import deepcopy
import json
from pathlib import Path
import unittest
from observational_succ.institute_audit import audit_registry
from observational_succ.source_proof_certificate import CapsuleError

ROOT=Path(__file__).resolve().parents[1]


class ActualGraphControls(unittest.TestCase):
    def setUp(self):
        self.graph=json.loads((ROOT/'research/2026-10-18/institute/theorem_registry.json').read_text())

    def claim(self,cid):
        return next(c for c in self.graph['claims'] if c['claim_id']==cid)

    def reject(self):
        with self.assertRaises(CapsuleError): audit_registry(self.graph,ROOT)

    def test_real_graph_retains_history_and_checks_new_sources(self):
        ids={c['claim_id']for c in self.graph['claims']}
        self.assertTrue({f'INS-{i:02d}'for i in range(1,23)}<=ids)
        out=audit_registry(self.graph,ROOT)
        self.assertEqual(out['theorems_proved_by_this_audit'],[])
        self.assertFalse(out['RH_proved'])

    def test_paper_forward_proof_cannot_become_kernel(self):
        self.claim('INS-15')['authority']='LEAN_KERNEL_PROVED'
        self.reject()

    def test_topology_mutation_is_rejected(self):
        self.claim('INS-16')['signature']['topology']='operator norm convergence'
        self.reject()

    def test_inherited_hypothesis_deletion_is_rejected(self):
        self.claim('INS-16')['hypotheses'].remove(self.claim('INS-15')['hypotheses'][0])
        self.reject()

    def test_fake_source_identity_is_rejected(self):
        self.claim('INS-18')['git_sources'][0]['blob']='0'*40
        self.reject()

    def test_stale_kernel_evidence_is_rejected(self):
        ev=next(x for x in self.claim('INS-19')['evidence'] if x['kind']=='LEAN_SOURCE')
        ev['sha256']='0'*64
        self.reject()
