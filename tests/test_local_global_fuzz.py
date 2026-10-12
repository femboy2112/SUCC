"""Seeded holdouts against independent graph integration and chart-gauge mutation."""
import random
import unittest
from dataclasses import replace
from collections import deque
from observational_succ.local_global_descent import (
    VoltageSource,Dart,construct_chart,assemble_charts,verify_result,edge_chart_cover,
)
from observational_succ.cycle_support_budget import fundamental_cycle_certificate


def graph_oracle(graph):
    # Independent path consistency implementation (no chart / overlap imports).
    values={};edges=[]
    for d in graph.darts:
        edges.append((d.tail,d.head,d.displacement))
        edges.append((d.head,d.tail,tuple(-x for x in d.displacement)))
    for root in graph.vertices:
        if root in values:continue
        values[root]=(0,)*graph.dimension
        pending=[root]
        while pending:
            current=pending.pop()
            for u,v,voltage in edges:
                if u!=current:continue
                suggestion=tuple(a+b for a,b in zip(values[u],voltage))
                if v not in values:
                    values[v]=suggestion
                    pending.append(v)
                elif values[v]!=suggestion:
                    return False
    return True


class FuzzGluing(unittest.TestCase):
    def test_independent_global_verdict_across_600_seeded_laws(self):
        rng=random.Random(20261012)
        for sample in range(600):
            n=rng.randrange(1,9)
            vv=tuple(range(n))
            m=rng.randrange(0,14)
            edges=tuple(Dart('e'+str(i),rng.choice(vv),rng.choice(vv),
                       (rng.randrange(-3,4),rng.randrange(-3,4))) for i in range(m))
            graph=VoltageSource('seeded-'+str(sample),vv,edges,2)
            expected=graph_oracle(graph)
            # A nonzero self-loop is locally impossible, otherwise every edge
            # patch is individually integrable; local impossibility is still
            # a valid negative verdict.
            try:
                specs=edge_chart_cover(graph)
                cs=tuple(construct_chart(graph,name,ids,lone_vertex=lone) for name,ids,lone in specs)
            except ValueError:
                self.assertFalse(expected)
                continue
            result=assemble_charts(graph,cs)
            verify_result(graph,cs,result)
            self.assertEqual(result.status=='GLUED',expected,(sample,graph))
            self.assertEqual(fundamental_cycle_certificate(graph).global_exact,expected)

    def test_gauge_mutations_do_not_change_verdict(self):
        rng=random.Random(12021012)
        for n in range(3,12):
            vertices=tuple((i,) for i in range(n))
            for wrong in (False,True):
                darts=tuple(Dart(str(i),vertices[i],vertices[(i+1)%n],
                        (1 if i<n-1 else (1 if wrong else 1-n),)) for i in range(n))
                graph=VoltageSource(f'gm-{n}-{wrong}',vertices,darts,1,n)
                specs=edge_chart_cover(graph)
                charts=tuple(construct_chart(graph,name,ids,lone_vertex=v) for name,ids,v in specs)
                shifts={c.name:rng.randrange(-1000,1000) for c in charts}
                shifted=tuple(replace(c,potentials=tuple((v,(p[0]+shifts[c.name],))
                             for v,p in c.potentials)) for c in charts)
                r=assemble_charts(graph,shifted)
                verify_result(graph,shifted,r)
                self.assertEqual(r.status=='GLUED',not wrong)

if __name__=='__main__':unittest.main()
