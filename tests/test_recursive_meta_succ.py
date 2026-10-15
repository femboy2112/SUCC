"""Exact finite controls for recursive source-model interactions and holonomy.

A separate Cartesian-product brute oracle checks the algebraic claims; the
paper Hilbert-space theorem is NOT claimed to be Lean/formally verified here.
"""
from __future__ import annotations
import unittest
from fractions import Fraction as F
from itertools import combinations, product

from observational_succ.recursive_meta_succ import (
    Derivation, MetaError, ModelSystem, RelationLaw, SignedCycle, SignedEdge,
    SignedGraph, SourceWorld, OrthogonalEdge, OrthogonalMetaGraph, even_parity_world, minimal_missing_interaction,
    reconstruction_arity, repair_ghost, shadow_system, shift_approximate_invariance,
)


def bits_world(n, chosen, source="source-A", epoch=0):
    return SourceWorld(source, epoch, "fixed-bits", tuple("x%d" % i for i in range(n)),
                       (("0", "1"),)*n, tuple(sorted(chosen)))


def independently_reconstruct(world, k):
    """Independent membership-test oracle; never calls the implementation join."""
    allowed = []
    for state in product(*world.domains):
        passes = True
        for size in range(1, k+1):
            for ix in combinations(range(len(world.coordinates)), size):
                view = tuple(state[i] for i in ix)
                if not any(tuple(s[i] for i in ix) == view for s in world.states):
                    passes = False
                    break
            if not passes:
                break
        if passes:
            allowed.append(state)
    return tuple(allowed)


def typed_edge(name, start, end, sign, weight=1, source_id="fixed-source", epoch=0, basis="oriented-real"):
    return SignedEdge(name, start, end, sign, weight, source_id, epoch, basis)


class TestMetaStructure(unittest.TestCase):
    def setUp(self):
        self.world = bits_world(4, (("0","0","0","1"),("1","1","1","0")))

    def test_nested_model_of_model_derives_new_constraints(self):
        w=self.world
        names=("x0","x1","x2","x3")
        ab=w.source_law("AB",names[:2])
        bc=w.source_law("BC",names[1:3])
        cd=w.source_law("CD",names[2:])
        m=ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(ab,bc,cd),w)
        self.assertEqual(len(m.joint_candidates()),2)
        d1=m.strongest_consequence(("x0","x2"),("AB","BC"),name="AC")
        self.assertEqual(d1.relation.rows,(("0","0"),("1","1")))
        self.assertTrue(m.check_derivation(d1))
        m1=m.with_derived(d1)
        d2=m1.strongest_consequence(("x0","x3"),("AC","CD"),name="AD")
        self.assertEqual(d2.relation.rows,(("0","1"),("1","0")))
        self.assertTrue(m1.check_derivation(d2))
        self.assertEqual(m1.with_derived(d2).joint_candidates(),m.joint_candidates())
        self.assertNotIn("AD", [l.name for l in m.laws])
        # Without the interaction CD, the deeper AD constraint cannot be derived.
        outer=m.strongest_consequence(("x0","x3"),("AB","BC"),name="weakAD")
        self.assertEqual(len(outer.relation.rows),4)
        self.assertTrue(all(len(v)==4 for _,v in outer.witnesses))

    def test_source_conflict_and_false_grounded_projection_fail(self):
        w=self.world
        ab=w.source_law("AB",("x0","x1"))
        err=RelationLaw("wrong-source","source-Z",w.epoch,w.basis,("x2",),(("0",),))
        with self.assertRaises(MetaError):
            ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(ab,err),w)
        stale=RelationLaw("wrong-epoch",w.source_id,99,w.basis,("x2",),(("0",),))
        with self.assertRaises(MetaError):
            ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(ab,stale),w)
        invented=RelationLaw("false-source",w.source_id,w.epoch,w.basis,("x0",),(("0",),),"SOURCE_PROJECTION")
        with self.assertRaises(MetaError):
            ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(invented,),w)
        forged=RelationLaw("forged",w.source_id,w.epoch,w.basis,("x0",),(("0",),("1",)),"SOURCE_PROJECTION")
        # Full x0 projection is 0,1 here so this one is honest.
        ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(forged,),w)
        fake=RelationLaw("extra",w.source_id,w.epoch,w.basis,("x0","x1"),
                         (("0","0"),("0","1"),("1","1")),"SOURCE_PROJECTION")
        with self.assertRaises(MetaError):
            ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(fake,),w)
        with self.assertRaises(MetaError):
            w.source_law("bad-scope",("x1","x0"))
        with self.assertRaises(MetaError):
            ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(ab,),None)

    def test_derived_certificate_mutations_cannot_change_source(self):
        w=self.world
        m=shadow_system(w,2)
        d=m.strongest_consequence(("x0","x3"),name="test")
        self.assertTrue(m.check_derivation(d))
        mutation=RelationLaw("test", w.source_id,w.epoch,w.basis,("x0","x3"),(("0","0"),),
                             "MODEL_DERIVED",d.relation.parents)
        altered=Derivation(mutation,d.witnesses,d.parent_names,d.original_joint_count)
        self.assertFalse(m.check_derivation(altered))
        with self.assertRaises(MetaError):
            m.with_derived(altered)
        altered2=Derivation(d.relation,d.witnesses,d.parent_names,d.original_joint_count,True,True)
        self.assertFalse(m.check_derivation(altered2))

    def test_pairwise_gluing_without_global_source_can_be_empty(self):
        w=bits_world(3,(("0","0","0"),))
        vals_eq=(("0","0"),("1","1"))
        vals_neq=(("0","1"),("1","0"))
        a=RelationLaw("AB",w.source_id,w.epoch,w.basis,("x0","x1"),vals_eq)
        b=RelationLaw("BC",w.source_id,w.epoch,w.basis,("x1","x2"),vals_eq)
        c=RelationLaw("AC",w.source_id,w.epoch,w.basis,("x0","x2"),vals_neq)
        m=ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,(a,b,c),None)
        for pairs in ((a,b),(b,c),(a,c)):
            self.assertTrue(ModelSystem(w.source_id,w.epoch,w.basis,w.coordinates,w.domains,pairs).joint_candidates())
        self.assertEqual(m.joint_candidates(),())
        self.assertFalse(m.entails(())['entailed'])
        self.assertEqual(m.entails(())['status'], "INCONSISTENT_THEORY")
        self.assertFalse(m.entails(())['physical_joint_execution_verified'])

    def test_projection_closure_conservative_and_idempotent(self):
        w=self.world
        m=shadow_system(w,2)
        before=m.joint_candidates()
        s1=m.saturate(4)
        self.assertEqual(before,s1.joint_candidates())
        s2=s1.saturate(4)
        self.assertEqual(s1.joint_candidates(),s2.joint_candidates())
        self.assertEqual(tuple(x.name for x in s1.laws),tuple(x.name for x in s2.laws))
        with self.assertRaises(MetaError):
            m.saturate(5)

    def test_exhaustive_three_bit_arity_lattice(self):
        universe=tuple(product(("0","1"),repeat=3))
        for mask in range(1,1<<len(universe)):
            chosen=tuple(row for j,row in enumerate(universe) if mask & (1<<j))
            w=bits_world(3,chosen)
            C={}
            for k in range(1,4):
                C[k]=shadow_system(w,k).joint_candidates()
                self.assertEqual(C[k],independently_reconstruct(w,k))
                self.assertTrue(set(chosen).issubset(C[k]))
            self.assertEqual(C[3],chosen)
            # Closure semilattice: cl_k(cl_j(S))=cl_min(k,j)(S).
            for j in range(1,4):
                wj=bits_world(3,C[j])
                for k in range(1,4):
                    self.assertEqual(shadow_system(wj,k).joint_candidates(),C[min(k,j)])

    def test_strict_higher_arity_parity_and_indistinguishable_rivals(self):
        for n in range(3,7):
            e=even_parity_world(n,0)
            o=even_parity_world(n,1)
            self.assertEqual(reconstruction_arity(e),n)
            full_count=2**n
            for k in range(1,n):
                self.assertEqual(len(shadow_system(e,k).joint_candidates()),full_count)
                self.assertEqual(tuple(l.rows for l in shadow_system(e,k).laws),
                                 tuple(l.rows for l in shadow_system(o,k).laws))
            self.assertEqual(set(shadow_system(e,n).joint_candidates()),set(e.states))
            self.assertTrue(set(e.states).isdisjoint(set(o.states)))

    def test_minimal_justified_interaction_repairs_a_ghost(self):
        w=even_parity_world(5)
        m=shadow_system(w,2)
        self.assertEqual(len(m.ghosts()),16)
        ghost=m.ghosts()[0]
        self.assertEqual(len(minimal_missing_interaction(w,ghost)),5)
        refined,receipt=repair_ghost(m,ghost,"new-parity-law")
        self.assertEqual(set(refined.joint_candidates()),set(w.states))
        self.assertEqual(receipt.separating_scope,w.coordinates)
        self.assertTrue(receipt.source_mathematically_declared_only)
        with self.assertRaises(MetaError):
            repair_ghost(m,w.states[0])
        with self.assertRaises(MetaError):
            minimal_missing_interaction(w,w.states[0])
        with self.assertRaises(MetaError):
            repair_ghost(refined,ghost)


class TestSignedSecondOrderHolonomy(unittest.TestCase):
    def setUp(self):
        self.graph=SignedGraph("fixed-source",0,"oriented-real",("A","B","C"),
            (typed_edge("ab","A","B",1),typed_edge("bc","B","C",1),
             typed_edge("ca","C","A",-1)))
        self.cycle=SignedCycle("A",(("ab",True),("bc",True),("ca",True)))

    def test_frustrated_cycle_yields_sharp_root_energy(self):
        g=self.graph
        self.assertEqual(g.oriented_cycle(self.cycle),(-1,F(3)))
        self.assertIsNone(g.signed_assignment())
        discovered=g.find_frustrated_cycle()
        self.assertIsNotNone(discovered)
        self.assertEqual(g.oriented_cycle(discovered)[0],-1)
        self.assertEqual(g.holonomy_root_lower_bound(self.cycle),F(4,3))
        self.assertEqual(g.energy({"A":F(1),"B":F(1,3),"C":F(-1,3)}),F(4,3))
        # Exhaustive rational control on a small grid, independent direct sums.
        for b,c in product((F(-1),F(-1,2),F(-1,3),F(0),F(1,3),F(1,2),F(1)),repeat=2):
            self.assertGreaterEqual(g.energy({"A":1,"B":b,"C":c}),F(4,3))
        self.assertEqual(g.signed_cycle_boolean_lower_bound(self.cycle),1)
        for assignment in product((-1,1),repeat=3):
            x=dict(zip(g.vertices,assignment))
            self.assertGreaterEqual(g.boolean_frustration(x),1)
        self.assertEqual(min(g.boolean_frustration(dict(zip(g.vertices,a))) for a in product((-1,1),repeat=3)),1)

    def test_positive_holonomy_has_zero_energy_section(self):
        g=SignedGraph("fixed-source",0,"oriented-real",("A","B","C"),
            (typed_edge("ab","A","B",1),typed_edge("bc","B","C",1),
             typed_edge("ca","C","A",1)))
        self.assertEqual(g.oriented_cycle(self.cycle)[0],1)
        self.assertIsNone(g.find_frustrated_cycle())
        x=g.signed_assignment()
        self.assertIsNotNone(x)
        self.assertEqual(g.energy(x),0)
        with self.assertRaises(MetaError):
            g.explicit_coercivity_constant(self.cycle)

    def test_full_space_global_coercivity_bound(self):
        g=self.graph
        gap=g.explicit_coercivity_constant(self.cycle)
        self.assertGreater(gap,0)
        self.assertLess(gap,1)
        for xs in product((F(-2),F(-1),F(0),F(1),F(2)),repeat=3):
            x=dict(zip(g.vertices,xs))
            E=g.energy(x)
            self.assertGreaterEqual(E,gap*sum(z*z for z in xs))

    def test_disconnected_component_refuses_wrong_global_gap(self):
        g=SignedGraph("fixed-source",0,"oriented-real",("A","B","C","isolated"),self.graph.edges)
        with self.assertRaises(MetaError):
            g.explicit_coercivity_constant(self.cycle)
        self.assertEqual(g.energy({"A":0,"B":0,"C":0,"isolated":5}),0)

    def test_fractional_cycle_packing_is_global_valid_inequality(self):
        edges=(
            typed_edge("ab","A","B",1,source_id="original-source",basis="exact-signed"),
            typed_edge("bc","B","C",1,source_id="original-source",basis="exact-signed"),
            typed_edge("ca","C","A",-1,source_id="original-source",basis="exact-signed"),
            typed_edge("de","D","E",1,source_id="original-source",basis="exact-signed"),
            typed_edge("ef","E","F",1,source_id="original-source",basis="exact-signed"),
            typed_edge("fd","F","D",-1,source_id="original-source",basis="exact-signed"))
        g=SignedGraph("original-source",0,"exact-signed",("A","B","C","D","E","F"),edges)
        cy1=SignedCycle("A",(("ab",True),("bc",True),("ca",True)))
        cy2=SignedCycle("D",(("de",True),("ef",True),("fd",True)))
        self.assertEqual(g.verify_fractional_cycle_packing(((cy1,F(1)),(cy2,F(1)))),2)
        for xs in product((-1,1),repeat=6):
            self.assertGreaterEqual(g.boolean_frustration(dict(zip(g.vertices,xs))),2)
        with self.assertRaises(MetaError):
            g.verify_fractional_cycle_packing(((cy1,F(2)),))
        with self.assertRaises(MetaError):
            g.verify_fractional_cycle_packing(((cy1,F(-1)),))

    def test_mutated_cycle_witness_rejected(self):
        for witness in (
            SignedCycle("A",(("ab",True),("bc",True))),
            SignedCycle("A",(("ab",True),("ca",True))),
            SignedCycle("A",(("ab",False),("bc",True),("ca",True))),
            SignedCycle("A",(("ab",True),("bc",True),("ca",True),("ab",True))),
        ):
            with self.assertRaises(MetaError):
                self.graph.oriented_cycle(witness)
        with self.assertRaises(MetaError):
            typed_edge("float","A","B",1,0.5)
        with self.assertRaises(MetaError):
            typed_edge("negative","A","B",1,-1)
        with self.assertRaises(MetaError):
            SignedGraph("fixed-source",0,"oriented-real",("A","B"),
                        (typed_edge("bad-source","A","B",1,source_id="another-source"),))

    def test_infinite_hilbert_no_gap_negative_control(self):
        self.assertEqual(shift_approximate_invariance(0),2)
        self.assertEqual(shift_approximate_invariance(10),F(2,21))
        for n in (1,3,10,100):
            self.assertGreater(shift_approximate_invariance(n),0)
            self.assertLess(shift_approximate_invariance(2*n+1),shift_approximate_invariance(n))
        with self.assertRaises(MetaError):
            shift_approximate_invariance(-1)


class TestOrthogonalMetaMetaLayer(unittest.TestCase):
    """The decisive meta-meta control: two zero-gap loops jointly become coercive."""

    def setUp(self):
        I=((1,0),(0,1))
        H1=((1,0),(0,-1))  # fixes horizontal axis
        H2=((-1,0),(0,1))  # fixes vertical axis
        def edge(name,u,v,U):
            return OrthogonalEdge(name,u,v,U,F(1),"meta-source",0,"real-2D")
        self.edges=(edge("ra","R","A",I),edge("ab","A","B",I),
                    edge("br","B","R",H1),edge("rc","R","C",I),
                    edge("cd","C","D",I),edge("dr","D","R",H2))
        self.graph=OrthogonalMetaGraph("meta-source",0,"real-2D",("R","A","B","C","D"),self.edges)
        self.c1=SignedCycle("R",(("ra",True),("ab",True),("br",True)))
        self.c2=SignedCycle("R",(("rc",True),("cd",True),("dr",True)))

    def test_noncoercive_cycles_jointly_certify_full_positive_gap(self):
        graph=self.graph
        h1,r1=graph.cycle(self.c1)
        h2,r2=graph.cycle(self.c2)
        self.assertEqual(h1,((F(1),F(0)),(F(0),F(-1))))
        self.assertEqual(h2,((F(-1),F(0)),(F(0),F(1))))
        self.assertEqual((r1,r2),(F(3),F(3)))
        # Each separately FIXES a nonzero vector, so no one-cycle δ>0.
        with self.assertRaises(MetaError):
            graph.certify_joint_gap((self.c1,),(F(1),),F(1))
        with self.assertRaises(MetaError):
            graph.certify_joint_gap((self.c2,),(F(1),),F(1))
        receipt=graph.certify_joint_gap((self.c1,self.c2),(F(1),F(1)),F(4))
        self.assertEqual(receipt.joint_gram,((F(4),F(0)),(F(0),F(4))))
        self.assertEqual(receipt.full_state_coercivity,F(1,23))
        self.assertFalse(receipt.has_unconditional_Weil_identification)
        self.assertFalse(receipt.physical_source_authenticated)
        # Independent direct-energy tests, not used to build the certificate.
        for j in range(256):
            V=[]
            for k in range(10):
                z=((j*137 + k*17 + k*k) % 11)-5
                V.append(F(z,5))
            values={node:(V[2*i],V[2*i+1]) for i,node in enumerate(graph.vertices)}
            E=graph.energy(values)
            norm=sum(x*x+y*y for x,y in values.values())
            self.assertGreaterEqual(E,receipt.full_state_coercivity*norm)

    def test_exact_mutations_reject_false_global_coupling(self):
        g=self.graph
        # Overstated gap, injected negative coefficients, missed source IDs,
        # and a mutant second holonomy identical to first must all be rejected.
        with self.assertRaises(MetaError):
            g.certify_joint_gap((self.c1,self.c2),(F(1),F(1)),F(5))
        with self.assertRaises(MetaError):
            g.certify_joint_gap((self.c1,self.c2),(F(-1),F(1)),F(1))
        with self.assertRaises(MetaError):
            g.certify_joint_gap((self.c1,SignedCycle("C",(("cd",True),("dr",True),("rc",True)))),(F(1),F(1)),F(1))
        wrong=OrthogonalEdge("wrong","R","A",((1,0),(0,1)),F(1),"other-source",0,"real-2D")
        with self.assertRaises(MetaError):
            OrthogonalMetaGraph("meta-source",0,"real-2D",g.vertices,g.edges+(wrong,))
        with self.assertRaises(MetaError):
            OrthogonalEdge("nonunitary","R","A",((2,0),(0,1)),F(1),"meta-source",0,"real-2D")
        mutant=OrthogonalEdge("dr","D","R",((1,0),(0,1)),F(1),"meta-source",0,"real-2D")
        # Second loop has now identity holonomy: only first reflection remains.
        gm=OrthogonalMetaGraph("meta-source",0,"real-2D",g.vertices,g.edges[:-1]+(mutant,))
        with self.assertRaises(MetaError):
            gm.certify_joint_gap((self.c1,self.c2),(F(1),F(1)),F(1))

    def test_single_rational_rotation_is_a_well_typed_holonomy(self):
        I=((1,0),(0,1))
        U=((F(3,5),-F(4,5)),(F(4,5),F(3,5)))
        def edge(name,u,v,mat):
            return OrthogonalEdge(name,u,v,mat,F(1),"rotation-source",0,"real-2D")
        g=OrthogonalMetaGraph("rotation-source",0,"real-2D",("A","B","C"),
                              (edge("ab","A","B",I),edge("bc","B","C",I),edge("ca","C","A",U)))
        cycle=SignedCycle("A",(("ab",True),("bc",True),("ca",True)))
        H,R=g.cycle(cycle)
        self.assertEqual(H,tuple(tuple(z for z in row) for row in U))
        self.assertEqual(R,3)
        # (I-U)^T(I-U) = 4/5 I, so δ=4/5 is source-derived exact.
        result=g.certify_joint_gap((cycle,),(F(1),),F(4,5))
        self.assertEqual(result.joint_gram,((F(4,5),F(0)),(F(0),F(4,5))))
        self.assertGreater(result.full_state_coercivity,0)
        self.assertGreater(g.energy({"A":(F(1),F(0)),"B":(F(1),F(0)),"C":(F(1),F(0))}),0)


if __name__ == "__main__":
    unittest.main()
