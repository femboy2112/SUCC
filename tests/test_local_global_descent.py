"""Independent finite arithmetic/local-to-global certificates and mutation controls."""
import unittest
from dataclasses import replace
from itertools import product
from observational_succ.local_global_descent import (
    Dart, VoltageSource, Chart, DescentError, construct_chart, assemble_charts,
    verify_result, spanning_chart_cover, edge_chart_cover, add, neg, sub,
)


def cycle_graph(winding=1):
    return VoltageSource('cycle3',((0,),(1,),(2,)),
        (Dart('a',(0,),(1,),(1,)), Dart('b',(1,),(2,),(1,)),
         Dart('c',(2,),(0,),(1 if winding else -2,))),1,3)


class GluingTests(unittest.TestCase):
    def test_three_edge_local_proofs_fail_to_glue_on_winding_cycle(self):
        g=cycle_graph(1)
        charts=tuple(construct_chart(g,'climber-'+d.key,(d.key,)) for d in g.darts)
        outcome=assemble_charts(g,charts)
        self.assertEqual(outcome.status,'OBSTRUCTED')
        self.assertEqual(abs(outcome.obstruction.displacement[0]),3)
        self.assertTrue(outcome.obstruction.lifted_walk)
        verify_result(g,charts,outcome)

    def test_three_edge_zero_winding_glues_from_independent_charts(self):
        g=cycle_graph(0)
        charts=tuple(construct_chart(g,'climber-'+d.key,(d.key,)) for d in g.darts)
        outcome=assemble_charts(g,charts)
        self.assertEqual(outcome.status,'GLUED')
        verify_result(g,charts,outcome)
        self.assertEqual([v for _,v in outcome.global_potential],[(0,),(1,),(2,)])

    def test_disconnected_overlap_two_edge_cycle_detected(self):
        g=VoltageSource('two-parallel',((0,),(1,)),
            (Dart('a',(0,),(1,),(1,)), Dart('b',(0,),(1,),(4,))),1,3)
        charts=(construct_chart(g,'left',('a',)),construct_chart(g,'right',('b',)))
        o=assemble_charts(g,charts)
        self.assertEqual(o.status,'OBSTRUCTED')
        self.assertEqual(abs(o.obstruction.displacement[0]),3)
        self.assertEqual(len(o.overlaps),2)
        verify_result(g,charts,o)

    def test_two_connected_disjoint_components_both_glue(self):
        g=VoltageSource('two-components',(0,1,2,3),(Dart('a',0,1,(3,)),Dart('b',2,3,(7,))),1)
        cs=(construct_chart(g,'c1',('a',)),construct_chart(g,'c2',('b',)))
        o=assemble_charts(g,cs)
        self.assertEqual(o.status,'GLUED')
        verify_result(g,cs,o)
        self.assertEqual(len(o.global_potential),4)

    def test_isolated_vertex_has_local_global_chart(self):
        g=VoltageSource('point',(3,),(),1)
        c=construct_chart(g,'point',(),lone_vertex=3)
        o=assemble_charts(g,(c,))
        verify_result(g,(c,),o)
        self.assertEqual(o.status,'GLUED')

    def test_chart_independence_up_to_affine_gauge(self):
        g=cycle_graph(0)
        c0=construct_chart(g,'A',('a','b'))
        c1=construct_chart(g,'B',('b','c'))
        shifted=replace(c1,potentials=tuple((v,add(p,(303,))) for v,p in c1.potentials))
        o=assemble_charts(g,(c0,shifted))
        self.assertEqual(o.status,'GLUED')
        verify_result(g,(c0,shifted),o)
        self.assertEqual([p for _,p in o.global_potential],[(0,),(1,),(2,)])

    def test_overlap_cycle_receipt_mutations_rejected(self):
        g=cycle_graph(1)
        cs=tuple(construct_chart(g,'c'+d.key,(d.key,)) for d in g.darts)
        r=assemble_charts(g,cs)
        for corrupt in (
            replace(r.obstruction,displacement=(0,)),
            replace(r.obstruction,lifted_walk=(('a',1),)),
            replace(r.obstruction,cycle=r.obstruction.cycle[:-1]),
        ):
            with self.assertRaises(DescentError):verify_result(g,cs,replace(r,obstruction=corrupt))

    def test_forged_normalized_chart_gauge_receipt_rejected(self):
        g=cycle_graph(0)
        cs=tuple(construct_chart(g,'chart'+e.key,(e.key,)) for e in g.darts)
        r=assemble_charts(g,cs)
        verify_result(g,cs,r)
        fake=replace(r,chart_shifts=tuple((name,(shift[0]+1,) if i==0 else shift)
                                          for i,(name,shift) in enumerate(r.chart_shifts)))
        with self.assertRaisesRegex(DescentError,'declared patch gauge'):
            verify_result(g,cs,fake)

    def test_missing_source_edge_and_vertex_refuse_global_claim(self):
        g=cycle_graph(0)
        cs=(construct_chart(g,'a',('a',)),construct_chart(g,'b',('b',)))
        with self.assertRaisesRegex(DescentError,'dart coverage'):
            assemble_charts(g,cs)
        with self.assertRaises(DescentError):
            assemble_charts(g,(cs[0],))

    def test_forged_local_equation_and_source_refused(self):
        g=cycle_graph(0)
        c=construct_chart(g,'a',('a',))
        with self.assertRaises(DescentError):
            assemble_charts(g,(replace(c,source_digest='forged'),))
        with self.assertRaises(DescentError):
            assemble_charts(g,(replace(c,potentials=((c.vertices[0],(4,)),(c.vertices[1],(12,)))),))

    def test_connected_cover_constructor_large_cycle_and_refinement(self):
        for n in range(3,11):
            verts=tuple((i,) for i in range(n))
            darts=tuple(Dart(str(i),verts[i],verts[(i+1)%n],
                             (1 if i<n-1 else (1-n if n%2 else 1),)) for i in range(n))
            g=VoltageSource(f'cycle{n}',verts,darts,1,n)
            edge_specs=edge_chart_cover(g)
            cs=tuple(construct_chart(g,name,ids,lone_vertex=v) for name,ids,v in edge_specs)
            o=assemble_charts(g,cs)
            verify_result(g,cs,o)
            self.assertEqual(o.status,'GLUED' if n%2 else 'OBSTRUCTED')
            if n%2:
                forest_specs=spanning_chart_cover(g)
                good=tuple(construct_chart(g,name,ids,lone_vertex=v) for name,ids,v in forest_specs)
                verify_result(g,good,assemble_charts(g,good))

    def test_orthogonal_direction_independence(self):
        v=((0,0),(1,0),(1,1),(0,1))
        good=(Dart('a',v[0],v[1],(1,0)),Dart('b',v[1],v[2],(0,1)),
              Dart('c',v[2],v[3],(-1,0)),Dart('d',v[3],v[0],(0,-1)))
        for mutation in ((0,0),(0,3)):
            darts=good[:-1]+(Dart('d',v[3],v[0],mutation if mutation!=(0,0) else (0,-1)),)
            if mutation==(0,3):
                g=VoltageSource('square',v,darts,2)
            else:
                g=VoltageSource('square',v,darts,2)
            cs=tuple(construct_chart(g,'n'+d.key,(d.key,)) for d in g.darts)
            o=assemble_charts(g,cs)
            verify_result(g,cs,o)
            self.assertEqual(o.status,'OBSTRUCTED' if mutation==(0,3) else 'GLUED')

    def test_authentic_gaussian_5_17_escape_gluing_obstruction(self):
        from observational_succ.gaussian_holonomy import GaussianSieve, quotient_holonomy
        sieve = GaussianSieve(((1,2),(1,4)))  # authentic rational split primes 5,17
        report = quotient_holonomy(sieve,1)
        witness = report.nonzero_cycle
        self.assertIsNotNone(witness)
        witness.verify(sieve,1)
        pts = witness.points
        vertices = tuple(dict.fromkeys(sieve.residue(z) for z in pts[:-1]))
        darts = tuple(Dart('w:'+str(i),sieve.residue(pts[i]),
                      sieve.residue(pts[i+1]),step)
                      for i,step in enumerate(witness.steps))
        graph = VoltageSource('authentic Gaussian P={5,17} escaping subgraph',
                              vertices,darts,2,sieve.period)
        specs = edge_chart_cover(graph)
        charts = tuple(construct_chart(graph,name,ids,lone_vertex=lone)
                       for name,ids,lone in specs)
        glued = assemble_charts(graph,charts)
        verify_result(graph,charts,glued)
        self.assertEqual(glued.status,'OBSTRUCTED')
        self.assertEqual(abs(glued.obstruction.displacement[0]),85)
        self.assertEqual(glued.obstruction.displacement[1],0)
        self.assertTrue(glued.obstruction.lifted_walk)

    def test_empty_incomplete_and_nonconnected_chart_rejection(self):
        g=VoltageSource('islands',(0,1,2,3),(Dart('a',0,1,(1,)),Dart('b',2,3,(1,))),1)
        with self.assertRaisesRegex(DescentError,'not connected'):
            construct_chart(g,'bad',('a','b'))
        with self.assertRaises(DescentError):
            assemble_charts(g,())


if __name__=='__main__':unittest.main()
