"""Adversarial finite FinSet pullback, bridge synthesis, and emergent invariants."""
from __future__ import annotations
import unittest
import random
from fractions import Fraction as Q
from itertools import combinations,product
from observational_succ.relational_model_genetics import (
    GeneticsError,Port,Capsule,PairedSourceTable,BridgeCandidate,binary_capsule,
    pullback,verify_pullback,chain_join,minimal_inconsistent_models,project,
    functional_dependencies,emergent_dependencies,invent_bijective_bridges,
    transport_capsule,bridge_repair_demo,
)


class TestTypedFinitePullback(unittest.TestCase):
    def setUp(self):
        self.a=binary_capsule('A','arith','source','x','y',1)
        self.b=binary_capsule('B','heat','source','y','z',1)

    def test_new_law_from_models_individually_unable_to_express_it(self):
        cert=pullback(self.a,self.b)
        self.assertTrue(verify_pullback(self.a,self.b,cert))
        self.assertEqual(project(cert.merged,('x','z')),(('0','0'),('1','1')))
        new=emergent_dependencies(self.a,self.b,cert.merged)
        self.assertIn(('x','z',(('0','0'),('1','1'))),new)
        self.assertNotIn('z',{p.name for p in self.a.ports})
        self.assertNotIn('x',{p.name for p in self.b.ports})

    def test_direct_relation_proof_to_every_joint_state(self):
        merged=pullback(self.a,self.b).merged
        for row in merged.rows:
            x,y,z=tuple(int(c) for c in row)
            self.assertEqual(x^y,1)
            self.assertEqual(y^z,1)
            self.assertEqual(x,z)

    def test_no_automatic_cross_source_gluing(self):
        forged=binary_capsule('B','heat','other','y','z',1)
        with self.assertRaises(GeneticsError):pullback(self.a,forged)

    def test_no_automatic_cross_epoch(self):
        changed=binary_capsule('B','heat','source','y','z',1,epoch=1)
        with self.assertRaises(GeneticsError):pullback(self.a,changed)

    def test_no_automatic_cross_basis(self):
        changed=binary_capsule('B','heat','source','y','z',1,basis='reinterpreted')
        with self.assertRaises(GeneticsError):pullback(self.a,changed)

    def test_wrong_port_domain_rejected(self):
        c=Capsule('C','alien','source',0,'binary-v1',
                  (Port('y',('hot','cold')),Port('z',('0','1'))),
                  (('hot','0'),('cold','1')))
        with self.assertRaises(GeneticsError):pullback(self.a,c)

    def test_no_common_port_gives_product_not_spurious_dependency(self):
        c=binary_capsule('C','unrelated','source','u','v',0)
        join=pullback(self.a,c)
        self.assertEqual(len(join.merged.rows),len(self.a.rows)*len(c.rows))
        self.assertEqual(emergent_dependencies(self.a,c,join.merged),())

    def test_pairwise_sat_but_global_unsat(self):
        c=binary_capsule('C','adversary','source','x','z',1)
        models=(self.a,self.b,c)
        for subset in combinations(models,2):
            self.assertIsNotNone(chain_join(subset))
        self.assertIsNone(chain_join(models))
        self.assertEqual(minimal_inconsistent_models(models),('A','B','C'))

    def test_parity_loop_zero_is_realized(self):
        c=binary_capsule('C','concordant','source','x','z',0)
        m=chain_join((self.a,self.b,c))
        self.assertIsNotNone(m)
        self.assertEqual(len(m.rows),2)

    def test_empty_two_way_stays_unrealized(self):
        a=Capsule('A','C','source',0,'basis',(Port('x',('0','1')),),(('0',),))
        b=Capsule('B','C','source',0,'basis',(Port('x',('0','1')),),(('1',),))
        c=pullback(a,b)
        self.assertFalse(c.realized)
        self.assertIsNone(c.merged)
        self.assertTrue(verify_pullback(a,b,c))
        self.assertEqual(minimal_inconsistent_models((a,b)),('A','B'))

    def test_wrong_forged_pair_certificate_rejected(self):
        c=pullback(self.a,self.b)
        bad=type(c)(c.merged,c.shared,c.left_rows,c.right_rows,(),None)
        with self.assertRaises(GeneticsError):verify_pullback(self.a,self.b,bad)

    def test_forged_extra_global_state_is_rejected(self):
        c=pullback(self.a,self.b)
        assert c.merged is not None
        fake=Capsule('fraud',c.merged.context,c.merged.source_id,
                     c.merged.epoch,c.merged.basis,c.merged.ports,
                     c.merged.rows+(('0','0','0'),))
        forged=type(c)(fake,c.shared,c.left_rows,c.right_rows,c.compatible_pairs,None)
        self.assertFalse(verify_pullback(self.a,self.b,forged))

    def test_natural_join_associative_up_to_canonical_port_order(self):
        c=binary_capsule('C','third','source','z','w',1)
        left=chain_join((self.a,self.b,c))
        right=chain_join((self.a,chain_join((self.b,c))))
        self.assertEqual(left.signature(),right.signature())
        self.assertEqual(set(left.rows),set(right.rows))
        self.assertEqual(project(left,('x','w')),(('0','1'),('1','0')))

    def test_100_seeded_joins_against_independent_brute_force(self):
        rng=random.Random(20261012)
        for _ in range(100):
            names1=('x','y');names2=('y','z')
            ar=tuple(row for row in product('01',repeat=2) if rng.randrange(2)) or (('0','0'),)
            br=tuple(row for row in product('01',repeat=2) if rng.randrange(2)) or (('1','1'),)
            ports=lambda names:tuple(Port(n,('0','1')) for n in names)
            a=Capsule('A','arith','source',0,'basis',ports(names1),ar)
            b=Capsule('B','thermal','source',0,'basis',ports(names2),br)
            expected={(x,y,z) for x,y in ar for yy,z in br if yy==y}
            cert=pullback(a,b)
            self.assertTrue(verify_pullback(a,b,cert))
            if expected:
                self.assertEqual(set(cert.merged.rows),expected)
            else:self.assertIsNone(cert.merged)


class TestBridgeDiscovery(unittest.TestCase):
    def setUp(self):
        self.tbl=PairedSourceTable('source',0,'basis',Port('clock',('0','1')),
                                   Port('thermal',('cold','warm')),
                                   (('s0','0','cold'),('s1','1','warm')),True)

    def test_discover_missing_semantic_arrow(self):
        bridges=invent_bijective_bridges(self.tbl)
        self.assertEqual(len(bridges),1)
        self.assertEqual(dict(bridges[0].mapping),{'0':'cold','1':'warm'})

    def test_false_semantic_arrow_fails_source_table(self):
        candidate=dict(zip(('0','1'),('warm','cold')))
        self.assertFalse(all(candidate[l]==r for _,l,r in self.tbl.observations))
        self.assertNotIn(tuple(candidate.items()),tuple(b.mapping for b in invent_bijective_bridges(self.tbl)))

    def test_incomplete_sample_retains_multiple_possible_bridges(self):
        table=PairedSourceTable('source',0,'basis',Port('clock',('0','1','2')),
                                Port('thermal',('red','blue','green')),
                                (('s0','0','red'),),False)
        bridges=invent_bijective_bridges(table)
        self.assertEqual(len(bridges),2)
        self.assertTrue(all(not x.complete_source_class for x in bridges))

    def test_bijective_bridge_require_equal_domain_cardinality(self):
        t=PairedSourceTable('source',0,'basis',Port('clock',('0','1')),
                            Port('thermal',('red','blue','green')),(('s0','0','red'),),False)
        self.assertEqual(invent_bijective_bridges(t),())

    def test_false_source_version_rejected(self):
        candidate=invent_bijective_bridges(self.tbl)[0]
        c=Capsule('C','thermal','source',1,'basis',(Port('thermal',('cold','warm')),),
                  (('cold',),('warm',)))
        with self.assertRaises(GeneticsError):transport_capsule(c,candidate)

    def test_bridge_injection_alias_rejected(self):
        candidate=invent_bijective_bridges(self.tbl)[0]
        c=Capsule('C','thermal','source',0,'basis',(Port('thermal',('cold','warm')),
                     Port('clock',('0','1'))),(('cold','0'),('warm','1')))
        with self.assertRaises(GeneticsError):transport_capsule(c,candidate)

    def test_bridge_demo_new_sourced_relation(self):
        d=bridge_repair_demo()
        self.assertEqual(d['joint_relation_x_z'],(('0','0'),('1','1')))
        self.assertTrue(d['new_relation_not_present_in_either_parent'])
        self.assertFalse(d['external_carrier_authenticated'])

    def test_invalid_port_rejects_nonexact_domain(self):
        with self.assertRaises(GeneticsError):Port('x',('0','0'))
        with self.assertRaises(GeneticsError):Port('x',())
        with self.assertRaises(GeneticsError):Port('',('0',))

    def test_all_source_rows_unique(self):
        with self.assertRaises(GeneticsError):PairedSourceTable(
            's',0,'b',Port('x',('0','1')),Port('y',('a','b')),
            (('state','0','a'),('state','1','b')))


if __name__=='__main__':unittest.main()
