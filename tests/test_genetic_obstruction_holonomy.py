"""Inherited edge rules can be lawful despite impossible global section."""
import unittest
import random
from observational_succ.relational_model_genetics import GeneticsError
from observational_succ.genetic_obstruction_holonomy import (
    ParityEdge,discover_holonomy,verify_cycle_witness,transport_along_path,
    obstruction_language_demo,brute_force_has_global_section,
)

class HolonomyMutationTests(unittest.TestCase):
    def setUp(self):
        self.edges=(ParityEdge('A','x','y',1),ParityEdge('B','y','z',1),
                    ParityEdge('C','x','z',1))

    def test_exact_nonflat_cycle_witness(self):
        c=discover_holonomy(self.edges)
        self.assertIsNone(c.global_potential)
        self.assertTrue(c.obstruction.nontrivial)
        self.assertTrue(verify_cycle_witness(self.edges,c.obstruction))

    def test_pathwise_transport_after_global_failure_is_lawful(self):
        c=discover_holonomy(self.edges)
        start=c.obstruction.cycle_nodes[0]
        word=c.obstruction.edge_names
        s=transport_along_path(self.edges,start,word,0)
        self.assertEqual(s['endpoint'],start)
        self.assertEqual(s['terminal_value'],1)
        self.assertEqual(transport_along_path(self.edges,start,word+word,0)['terminal_value'],0)

    def test_one_flip_repairs_flatness_but_may_change_source_claim(self):
        fixed=self.edges[:2]+(ParityEdge('C','x','z',0),)
        c=discover_holonomy(fixed)
        self.assertIsNotNone(c.global_potential)
        self.assertIsNone(c.obstruction)
        self.assertTrue(brute_force_has_global_section(fixed))
        self.assertFalse(brute_force_has_global_section(self.edges))

    def test_forged_walk_rejected(self):
        c=discover_holonomy(self.edges)
        witness=c.obstruction
        x=type(witness)(witness.edge_names,witness.cycle_nodes,0)
        self.assertFalse(verify_cycle_witness(self.edges,x))
        x=type(witness)(witness.edge_names[:-1],witness.cycle_nodes,1)
        self.assertFalse(verify_cycle_witness(self.edges,x))

    def test_uncomposable_word_refused(self):
        with self.assertRaises(GeneticsError):transport_along_path(
            self.edges,'x',('B',),0)

    def test_forged_source_union_rejected(self):
        b=(self.edges[0],ParityEdge('B','y','z',1,'other'))
        with self.assertRaises(GeneticsError):discover_holonomy(b)

    def test_self_loop_nonflat(self):
        a=(ParityEdge('loop','x','x',1),)
        cert=discover_holonomy(a)
        self.assertTrue(verify_cycle_witness(a,cert.obstruction))
        self.assertFalse(brute_force_has_global_section(a))

    def test_reversed_paths_in_z2(self):
        p=(ParityEdge('edge','x','y',1),)
        self.assertEqual(transport_along_path(p,'x',('edge',),0)['terminal_value'],1)
        self.assertEqual(transport_along_path(p,'y',('edge',),0)['terminal_value'],1)

    def test_independent_exhaustive_binary_assignment_oracle(self):
        rng=random.Random(20261013)
        for _ in range(240):
            n=rng.randint(2,7)
            m=rng.randint(n,2*n+2)
            edges=[]
            for j in range(m):
                u,v=(str(rng.randrange(n)),str(rng.randrange(n)))
                edges.append(ParityEdge(f'e{j}',u,v,rng.randrange(2)))
            edges=tuple(edges)
            c=discover_holonomy(edges)
            oracle=brute_force_has_global_section(edges)
            self.assertEqual(c.global_potential is not None,oracle)
            if c.obstruction:
                self.assertTrue(verify_cycle_witness(edges,c.obstruction))
                self.assertEqual(c.obstruction.accumulated_shift,1)
            else:
                d=dict(c.global_potential)
                self.assertTrue(all(d[e.u]^d[e.v]==e.shift for e in edges))

    def test_full_demo_scope(self):
        result=obstruction_language_demo()
        self.assertEqual(result['holonomy'],1)
        self.assertFalse(result['global_single_valued_potential_exists'])
        self.assertTrue(result['original_constraints_not_silently_deleted'])
        self.assertFalse(result['physical_ontology_claimed'])

if __name__=='__main__':unittest.main()
