"""Exact permutation gauge witnesses; abelianized probes must fail where required."""
import unittest
from dataclasses import replace
from itertools import permutations
from observational_succ.nonabelian_local_global import (
    GroupEdge,GroupGraph,NonAbelianError,ident,mul,inverse,sign,
    construct_group_chart,glue_group_charts,verify_group_verdict,
    s3_commutator_square,
)

class NonAbelianLocalGlobalTests(unittest.TestCase):
    def test_s3_group_inverse_associativity_and_sign(self):
        group=list(permutations(range(3)))
        for a in group:
            self.assertEqual(mul(a,inverse(a)),ident(3))
            for b in group:
                self.assertEqual(sign(mul(a,b)),sign(a)*sign(b))
                for c in group:
                    self.assertEqual(mul(mul(a,b),c),mul(a,mul(b,c)))

    def test_commutator_obstructs_despite_trivial_sign(self):
        g,cs=s3_commutator_square()
        o=glue_group_charts(g,cs)
        self.assertEqual(o.status,'OBSTRUCTED')
        self.assertNotEqual(o.obstruction_product,ident(3))
        self.assertEqual(sign(o.obstruction_product),1)
        self.assertEqual(len(o.obstruction_cycle),4)
        verify_group_verdict(g,cs,o)

    def test_nonabelian_flat_positive_control(self):
        a=(1,0,2);b=(0,2,1)
        g,old=s3_commutator_square()
        transports=(a,b,inverse(a))
        final=inverse(mul(transports[2],mul(transports[1],transports[0])))
        d=g.edges[-1]
        good=replace(g,name='S3-flat-example',edges=g.edges[:-1]+(replace(d,transport=final),))
        cs=tuple(construct_group_chart(good,'l'+e.key,(e.key,)) for e in good.edges)
        verdict=glue_group_charts(good,cs)
        self.assertEqual(verdict.status,'GLUED')
        verify_group_verdict(good,cs,verdict)
        self.assertEqual(len(verdict.vertex_sections),4)

    def test_single_chart_already_detects_curvature_if_loop_inside(self):
        g,_=s3_commutator_square()
        with self.assertRaises(NonAbelianError):
            construct_group_chart(g,'all',tuple(e.key for e in g.edges))

    def test_forged_section_and_wrong_source_rejected(self):
        g,cs=s3_commutator_square()
        wrong=replace(cs[0],source_digest='wrong')
        with self.assertRaises(NonAbelianError):glue_group_charts(g,(wrong,)+cs[1:])
        changed=replace(cs[0],sections=tuple((v,ident(3)) for v,_ in cs[0].sections))
        with self.assertRaises(NonAbelianError):glue_group_charts(g,(changed,)+cs[1:])

    def test_false_claimed_group_holonomy_rejected(self):
        g,cs=s3_commutator_square();v=glue_group_charts(g,cs)
        with self.assertRaises(NonAbelianError):
            verify_group_verdict(g,cs,replace(v,obstruction_product=ident(3)))
        with self.assertRaises(NonAbelianError):
            verify_group_verdict(g,cs,replace(v,obstruction_cycle=v.obstruction_cycle[:-1]))

    def test_parallel_group_overlap_detects_two_vertex_defect(self):
        a=(1,0,2);b=(0,2,1)
        g=GroupGraph('parallel',('u','v'),(GroupEdge('e1','u','v',a),GroupEdge('e2','u','v',b)),3)
        charts=tuple(construct_group_chart(g,'c'+e.key,(e.key,)) for e in g.edges)
        v=glue_group_charts(g,charts)
        self.assertEqual(v.status,'OBSTRUCTED')
        self.assertEqual(len(v.overlaps),2)
        verify_group_verdict(g,charts,v)

    def test_identity_trivial_group(self):
        e=ident(1)
        g=GroupGraph('trivial',('a','b','c'),(GroupEdge('ab','a','b',e),GroupEdge('bc','b','c',e)),1)
        cs=tuple(construct_group_chart(g,x,(x,)) for x in ('ab','bc'))
        r=glue_group_charts(g,cs)
        self.assertEqual(r.status,'GLUED')
        verify_group_verdict(g,cs,r)

if __name__=='__main__':unittest.main()
