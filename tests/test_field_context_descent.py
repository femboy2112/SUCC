"""Hostile tests for carrier/observation/claim squares and actual source holonomy."""
import random
import unittest
from dataclasses import replace

from observational_succ.field_relative_closure import FiniteField,ClosureError
from observational_succ.field_context_descent import (
    audit_descent,SourceVoltageGraph,VoltageCertificate,LoopWitness,
)


def make(states,observations,target, *,sid="physical",basis="common"):
    return FiniteField(sid,basis,tuple(states),{"observe":tuple(observations)},
                       {"target":tuple(target)})

class DescentGates(unittest.TestCase):
    def test_invertible_original_carrier_frame_preserves_truth_and_proof(self):
        x=make((0,1,2),(0,1,2),(0,1,2))
        y=make((0,1,2),(2,0,1),(1,2,0),sid="updated")
        # Source map 0->1, 1->2, 2->0; reported new observations are 0,1,2;
        # target transformed is 2,0,1 and DOES NOT coincide with old target.
        r=audit_descent(x,y,(1,2,0),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance)
        self.assertFalse(r.truth_square)
        self.assertTrue(r.updated_report_proves_original_claim)
        self.assertEqual(r.truth_witness,0)

    def test_complete_three_gate_square(self):
        x=make((0,1,2),(0,1,2),(0,1,2))
        y=make((0,1,2),(2,0,1),(2,0,1),sid="updated")
        r=audit_descent(x,y,(1,2,0),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance)
        self.assertTrue(r.truth_square)
        self.assertTrue(r.updated_report_proves_original_claim)
        self.assertIsNone(r.truth_witness)

    def test_commuting_observations_do_not_preserve_original_parity(self):
        x=make((0,1),(0,1),(0,1))
        y=make((0,1),(0,0),(0,0),sid="mutated")
        r=audit_descent(x,y,(0,0),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance)
        self.assertFalse(r.truth_square)
        self.assertFalse(r.updated_report_proves_original_claim)
        self.assertEqual(r.loss_witness,(0,1))

    def test_truth_and_updated_decodability_do_not_imply_covariance(self):
        x=make((0,1),(0,0),(0,1))
        y=make((0,1),(0,1),(0,1),sid="enriched")
        r=audit_descent(x,y,(0,1),("observe",),("observe",),"target","target")
        self.assertFalse(r.covariance)
        self.assertTrue(r.truth_square)
        self.assertTrue(r.updated_report_proves_original_claim)
        self.assertEqual(r.covariance_witness,(0,1))

    def test_covariance_and_truth_not_sufficient_for_proof(self):
        x=make((0,1),(0,0),(0,1))
        y=make((0,1),(0,0),(0,1),sid="unchanged")
        r=audit_descent(x,y,(0,1),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance)
        self.assertTrue(r.truth_square)
        self.assertFalse(r.updated_report_proves_original_claim)

    def test_claim_invariant_even_when_carrier_map_not_injective(self):
        x=make((0,1,2),(0,1,2),(0,0,1))
        y=make((0,1),(0,1),(0,1),sid="quotient")
        r=audit_descent(x,y,(0,0,1),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance)
        self.assertTrue(r.truth_square)
        self.assertTrue(r.updated_report_proves_original_claim)

    def test_forged_missing_source_mapping_is_rejected(self):
        x=make((0,1),(0,1),(0,1));y=make((0,),(0,),(0,),sid="new")
        with self.assertRaisesRegex(ClosureError,"total"):
            audit_descent(x,y,(0,),("observe",),("observe",),"target","target")
        with self.assertRaisesRegex(ClosureError,"actual"):
            audit_descent(x,y,(0,100),("observe",),("observe",),"target","target")

    def test_source_event_outcome_basis_scope_is_not_empirically_authenticated(self):
        x=make((0,1),(0,1),(0,1))
        y=make((0,1),(0,1),(0,1),sid="self-asserted")
        r=audit_descent(x,y,(0,1),("observe",),("observe",),"target","target")
        self.assertTrue(r.covariance and r.truth_square)
        self.assertEqual(r.new_source_id,"self-asserted")


class HolonomyCertificates(unittest.TestCase):
    def test_three_locally_integrable_edges_have_nonzero_global_loop(self):
        edges=((0,1,(1,)),(1,2,(1,)),(2,0,(1,)))
        for a,b,c in edges:
            local=SourceVoltageGraph("circle",0,(a,b),((a,b,c),),1)
            self.assertEqual(local.integrate().status,"GLOBAL_POTENTIAL")
        g=SourceVoltageGraph("circle",0,(0,1,2),edges,1)
        report=g.integrate()
        self.assertEqual(report.status,"NONZERO_HOLONOMY")
        self.assertEqual(abs(report.escape.translation[0]),3)
        self.assertTrue(g.verify(report))

    def test_self_loop_with_period_displacement_fails(self):
        g=SourceVoltageGraph("one-residue",0,(0,),((0,0,(5,0)),),2)
        r=g.integrate()
        self.assertEqual(r.status,"NONZERO_HOLONOMY")
        self.assertEqual(r.escape.translation,(5,0))
        self.assertTrue(g.verify(r))

    def test_parallel_darts_can_hide_escape(self):
        g=SourceVoltageGraph("parallel",0,(0,1),((0,1,(1,)),(0,1,(5,))),1)
        r=g.integrate()
        self.assertEqual(r.status,"NONZERO_HOLONOMY")
        self.assertEqual(abs(r.escape.translation[0]),4)
        self.assertTrue(g.verify(r))

    def test_all_exact_edges_glue_even_if_potential_not_constant(self):
        g=SourceVoltageGraph("path",0,(0,1,2),((0,1,(1,2)),(1,2,(4,3))),2)
        r=g.integrate()
        self.assertEqual(r.status,"GLOBAL_POTENTIAL")
        self.assertEqual(dict(r.potentials)[2],(5,5))
        self.assertTrue(g.verify(r))

    def test_disconnected_components_have_independent_gauges(self):
        g=SourceVoltageGraph("two",0,(0,1,2,3),((0,1,(1,)),(2,3,(2,))),1)
        c=g.integrate();self.assertEqual(c.status,"GLOBAL_POTENTIAL")
        self.assertEqual(dict(c.potentials)[2],(0,))
        self.assertTrue(g.verify(c))

    def test_gauge_shift_is_valid_but_wrong_vertex_potential_is_not(self):
        g=SourceVoltageGraph("gauge",0,(0,1),((0,1,(1,)),),1)
        r=g.integrate()
        shifted=replace(r,potentials=((0,(100,)),(1,(101,))))
        self.assertTrue(g.verify(shifted))
        with self.assertRaisesRegex(ClosureError,"False"):
            g.verify(replace(r,potentials=((0,(0,)),(1,(7,)))))

    def test_forged_source_version_invalidates_both_types(self):
        g=SourceVoltageGraph("gauge",0,(0,1),((0,1,(1,)),),1)
        c=g.integrate()
        with self.assertRaisesRegex(ClosureError,"Mismatched"):
            g.verify(replace(c,source_version=1))
        with self.assertRaisesRegex(ClosureError,"Mismatched"):
            g.verify(replace(c,source_id="false-source"))

    def test_forged_closed_walk_translation_invalid(self):
        g=SourceVoltageGraph("loop",0,(0,),((0,0,(2,)),),1)
        c=g.integrate()
        with self.assertRaisesRegex(ClosureError,"closed"):
            g.verify(replace(c,escape=replace(c.escape,translation=(3,))))

    def test_forged_partial_walk_invalid(self):
        g=SourceVoltageGraph("loop",0,(0,1),((0,1,(2,)),(1,0,(3,))),1)
        c=g.integrate()
        with self.assertRaises(ClosureError):
            g.verify(replace(c,escape=LoopWitness(0,((0,1),),(2,))))

    def test_zero_displacement_full_cycle_glues(self):
        g=SourceVoltageGraph("flat",0,(0,1,2),((0,1,(2,)),(1,2,(1,)),(2,0,(-3,))),1)
        c=g.integrate();self.assertEqual(c.status,"GLOBAL_POTENTIAL")
        self.assertTrue(g.verify(c))

    def test_empty_source_edge_set_is_trivially_integrable(self):
        g=SourceVoltageGraph("isolated",0,(0,1),(),2)
        c=g.integrate();self.assertEqual(c.status,"GLOBAL_POTENTIAL")
        self.assertTrue(g.verify(c))

    def test_missing_directed_edge_certificate_forgery_detected(self):
        g=SourceVoltageGraph("four",0,(0,1,2),((0,1,(1,)),(1,2,(1,)),(2,0,(1,))),1)
        with self.assertRaises(ClosureError):
            g.verify(VoltageCertificate("GLOBAL_POTENTIAL","four",0,
                potentials=((0,(0,)),(1,(1,)))))

    def test_malformed_voltage_is_never_rounded_to_a_valid_real(self):
        with self.assertRaises(ClosureError):
            SourceVoltageGraph("x",0,(0,),((0,0,(1.0,)),),1)

    def test_authentic_norm5_gaussian_sieve_has_nonzero_source_holonomy(self):
        # True Gaussian split factors 2±i of norm 5; arithmetic from scratch.
        Q=5
        verts=tuple((x,y) for x in range(Q) for y in range(Q)
                    if (x*x+y*y)%5 != 0)
        self.assertEqual(len(verts),16)
        V=set(verts)
        steps=((1,0),(-1,0),(0,1),(0,-1))
        edges=tuple((v,((v[0]+s[0])%Q,(v[1]+s[1])%Q),s)
                    for v in verts for s in steps
                    if ((v[0]+s[0])%Q,(v[1]+s[1])%Q) in V)
        g=SourceVoltageGraph("authentic-p5-Gaussian-norm-sieve",0,verts,edges,2)
        c=g.integrate()
        self.assertEqual(c.status,"NONZERO_HOLONOMY")
        self.assertTrue(g.verify(c))
        self.assertTrue(any(c.escape.translation))
        self.assertTrue(all(d%5==0 for d in c.escape.translation))
        # Escape in the SIEVE, not necessarily a Gaussian-prime-only escape.

    def test_authentic_norm5_and13_sieve_glues_all_local_edges(self):
        Q=65
        verts=tuple((x,y) for x in range(Q) for y in range(Q)
                    if (x*x+y*y)%5 and (x*x+y*y)%13)
        self.assertEqual(len(verts),2304)
        V=set(verts)
        steps=((1,0),(-1,0),(0,1),(0,-1))
        edges=tuple((v,((v[0]+s[0])%Q,(v[1]+s[1])%Q),s)
                    for v in verts for s in steps
                    if ((v[0]+s[0])%Q,(v[1]+s[1])%Q) in V)
        self.assertEqual(len(edges),4356)
        g=SourceVoltageGraph("authentic-p5-p13-sieve",0,verts,edges,2)
        c=g.integrate()
        self.assertEqual(c.status,"GLOBAL_POTENTIAL")
        self.assertTrue(g.verify(c))
        # Independent connected-component count, with all graph edges.
        adj={v:set() for v in verts}
        for u,v,_ in edges:
            adj[u].add(v);adj[v].add(u)
        unseen=set(verts)
        sizes=[]
        while unseen:
            start=unseen.pop();stack=[start];size=0
            while stack:
                v=stack.pop();size+=1
                for nxt in adj[v]:
                    if nxt in unseen:
                        unseen.remove(nxt);stack.append(nxt)
            sizes.append(size)
        self.assertEqual(len(sizes),243)
        self.assertEqual(max(sizes),580)

    def test_source_loop_witness_fuzz_with_independent_cycle_checker(self):
        rng=random.Random(580104)
        # Independent root-potential Bellman-style relaxation (no path oracle).
        for _ in range(450):
            n=rng.randint(1,6)
            d=rng.choice((1,2))
            edges=tuple((rng.randrange(n),rng.randrange(n),
                         tuple(rng.randrange(-2,3) for _ in range(d)))
                        for _ in range(rng.randrange(0,9)))
            g=SourceVoltageGraph("seeded",0,tuple(range(n)),edges,d)
            report=g.integrate()
            # Independent constraint propagation on EVERY oriented edge until fixpoint.
            vals={}
            reachable={v:set() for v in range(n)}
            for u,v,_ in edges:
                reachable[u].add(v);reachable[v].add(u)
            is_consistent=True
            for base in range(n):
                if base in vals:continue
                vals[base]=(0,)*d
                frontier=[base]
                while frontier:
                    u=frontier.pop()
                    for a,b,w in edges:
                        for v,delta in ((b,w),) if u==a else ():
                            expect=tuple(x+y for x,y in zip(vals[u],delta))
                            if v not in vals:vals[v]=expect;frontier.append(v)
                            elif vals[v]!=expect:is_consistent=False
                        for v,delta in ((a,tuple(-x for x in w)),) if u==b else ():
                            expect=tuple(x+y for x,y in zip(vals[u],delta))
                            if v not in vals:vals[v]=expect;frontier.append(v)
                            elif vals[v]!=expect:is_consistent=False
            self.assertEqual(report.status=="GLOBAL_POTENTIAL",is_consistent)
            self.assertTrue(g.verify(report))

if __name__=='__main__':unittest.main()
