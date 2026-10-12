"""Exact source-sharing, epistemic sufficiency and Dirichlet holography falsifiers."""
import unittest
from fractions import Fraction as F
from itertools import product

from observational_succ.shared_carrier_descent import (
    CarrierDescentError, SharedSource, Evidence, SharedCarrierGraph,
)


def bits_source():
    return SharedSource("one-carrier", 3,"stable-basis",tuple(range(8)),
        {"a":tuple((s>>2)&1 for s in range(8)),
         "b":tuple((s>>1)&1 for s in range(8)),
         "c":tuple(s&1 for s in range(8))},
        {"parity":tuple((s.bit_count()&1) for s in range(8)),
         "first":tuple((s>>2)&1 for s in range(8))})


def wheel():
    return SharedCarrierGraph("disk-carrier",5,
        ("b0","b1","b2","b3","hub"),
        ("b0","b1","b2","b3"),
        (("b0","b1",1),("b1","b2",1),("b2","b3",1),("b3","b0",1),
         ("hub","b0",1),("hub","b1",1),("hub","b2",1),("hub","b3",1)))


class SharedCarrierDescentTests(unittest.TestCase):
    def test_one_source_all_boundary_e_towers_can_determine_claim(self):
        m=bits_source()
        receipts=tuple(m.report(probe,5,"E@"+probe) for probe in ("a","b","c"))
        self.assertEqual(m.fiber(receipts),(5,))
        self.assertEqual(m.conclude(receipts,"parity")["value"],0)
        self.assertEqual(m.factorization(("a","b","c"),"parity")["all_sources_separated"],True)

    def test_sparse_boundary_not_enough_even_on_same_source(self):
        m=bits_source()
        out=m.factorization(("a","b"),"parity")
        self.assertFalse(out["factors"])
        a,b=out["counterexample"]
        self.assertEqual((a>>2,a>>1&1),(b>>2,b>>1&1))
        self.assertNotEqual(m.claims["parity"][a],m.claims["parity"][b])
        partial=tuple(m.report(p,5,"E@"+p) for p in ("a","b"))
        self.assertEqual(m.conclude(partial,"parity")["status"],"UNRESOLVED")
        self.assertEqual(m.conclude(partial,"first")["status"],"PROVED")

    def test_cross_talk_does_not_separate_aliases(self):
        m=bits_source()
        p=("a","b")
        a,b=m.factorization(p,"parity")["counterexample"]
        # Every deterministic relay/replay of the original reports is identical.
        ta=tuple(m.report(i,a,"A"+i).outcome for i in p)
        tb=tuple(m.report(i,b,"B"+i).outcome for i in p)
        self.assertEqual(ta,tb)
        self.assertNotEqual(m.claims["parity"][a],m.claims["parity"][b])

    def test_three_pairwise_compatible_reports_not_globally_sourced(self):
        even=SharedSource("single-even-parity",0,"B",(0,3,5,6),
             {str(k):tuple((s>>k)&1 for s in (0,3,5,6)) for k in (0,1,2)},
             {"parity":(0,0,0,0)})
        forged=tuple(Evidence("single-even-parity",0,"B",str(k),1,"E"+str(k))
                     for k in (0,1,2))
        r=even.pairwise_and_global_consistency(forged)
        self.assertTrue(r["pairwise_realizable"])
        self.assertFalse(r["globally_realizable"])
        self.assertEqual(even.conclude(forged,"parity")["status"],"INCONSISTENT_SOURCE")

    def test_stale_source_or_basis_cannot_be_laundered(self):
        m=bits_source()
        real=m.report("a",5,"Alice")
        for e in (Evidence("wrong",3,"stable-basis","a",1,"Alice"),
                  Evidence("one-carrier",4,"stable-basis","a",1,"Alice"),
                  Evidence("one-carrier",3,"wrong","a",1,"Alice"),
                  Evidence("one-carrier",3,"stable-basis","absent",1,"Alice")):
            with self.assertRaises(CarrierDescentError):m.fiber((real,e))

    def test_contradictory_source_reports_are_not_false_proofs(self):
        m=bits_source()
        data=(Evidence("one-carrier",3,"stable-basis","a",1,"E"),
              Evidence("one-carrier",3,"stable-basis","a",0,"E"))
        self.assertEqual(m.conclude(data,"first")["status"],"INCONSISTENT_SOURCE")

    def test_unmeasured_target_not_smuggled_from_source_truth(self):
        m=bits_source()
        self.assertEqual(m.conclude((),"parity")["status"],"UNRESOLVED")
        self.assertFalse(m.factorization((),"parity")["factors"])

    def test_laplacian_and_harmonic_unique_wheel(self):
        g=wheel()
        b={"b0":F(1),"b1":F(0),"b2":F(0),"b3":F(0)}
        f=g.complete_harmonic(b)
        self.assertEqual(f["hub"],F(1,4))
        self.assertEqual(g.flux(f)["hub"],0)
        self.assertEqual(g.energy(f),g.boundary_energy(b))
        r=g.completion_receipt(b)
        self.assertEqual(r["reconstructed_interior"],(("hub",F(1,4)),))
        self.assertFalse(r["physical_source_authenticated"])

    def test_exact_dtn_schur_symmetry_constant_kernel(self):
        g=wheel()
        N=g.boundary_operator()
        self.assertEqual(len(N),4)
        self.assertTrue(all(sum(row,F(0))==0 for row in N))
        self.assertEqual(N[0][0],F(11,4))
        self.assertEqual(N[0][1],F(-5,4))
        for i,j in product(range(4),repeat=2):
            self.assertEqual(N[i][j],N[j][i])
        self.assertEqual(g.boundary_energy({v:F(7) for v in g.boundary}),0)

    def test_variational_gap_if_interior_state_is_not_harmonic(self):
        g=wheel()
        b={v:F(i) for i,v in enumerate(g.boundary)}
        solution=g.complete_harmonic(b)
        trial=dict(solution);trial["hub"]+=F(3,2)
        self.assertEqual(g.energy(trial)-g.energy(solution),F(9,2))
        self.assertEqual(g.flux(trial)["hub"],F(6))
        # SAME carrier and SAME boundary, different nonharmonic bulk.
        self.assertTrue(all(solution[v]==trial[v] for v in g.boundary))
        self.assertNotEqual(solution["hub"],trial["hub"])

    def test_strongly_nontrivial_interior_two_sites(self):
        g=SharedCarrierGraph("two-layer",0,("b0","b1","u","v"),("b0","b1"),
                             (("b0","u",1),("u","v",1),("v","b1",1)))
        b={"b0":F(0),"b1":F(1)}
        f=g.complete_harmonic(b)
        self.assertEqual(f["u"],F(1,3))
        self.assertEqual(f["v"],F(2,3))
        self.assertEqual(g.energy(f),F(1,6))
        self.assertEqual(g.boundary_operator(),((F(1,3),F(-1,3)),(F(-1,3),F(1,3))))

    def test_disconnected_boundary_anchored_components_allowed(self):
        g=SharedCarrierGraph("two-islands",0,("b0","u","b1","v"),("b0","b1"),
                             (("b0","u",1),("b1","v",2)))
        f=g.complete_harmonic({"b0":1,"b1":3})
        self.assertEqual((f["u"],f["v"]),(1,3))
        self.assertEqual(g.boundary_operator(),((F(0),F(0)),(F(0),F(0))))

    def test_hidden_component_or_invalid_conductance_rejected(self):
        with self.assertRaisesRegex(CarrierDescentError,"reach boundary"):
            SharedCarrierGraph("bad",0,("b","i"),("b",),())
        for w in (F(0),F(-1),0.25):
            with self.assertRaises(CarrierDescentError):
                SharedCarrierGraph("bad",0,("b","i"),("b",),(("b","i",w),))
        with self.assertRaises(CarrierDescentError):
            SharedCarrierGraph("bad",0,("b","i"),("b",),(("b","i",1),("i","b",2)))

    def test_every_small_path_network_exact_boundary_operator(self):
        for n in range(3,9):
            nodes=tuple(range(n))
            g=SharedCarrierGraph("finite-path",n,nodes,(0,n-1),
                 tuple((i,i+1,F(i+1,i+2)) for i in range(n-1)))
            b={0:F(2,3),n-1:F(7,5)}
            f=g.complete_harmonic(b)
            self.assertEqual(g.energy(f),g.boundary_energy(b))
            self.assertTrue(all(g.flux(f)[v]==0 for v in g.interiors))
            resistance=sum((F(1)/w for _,_,w in g.edges),F(0))
            c=F(1)/resistance
            self.assertEqual(g.boundary_operator(),((c,-c),(-c,c)))

    def test_no_claim_of_physical_or_archimedean_identification(self):
        g=wheel()
        r=g.completion_receipt({v:F(0) for v in g.boundary})
        self.assertTrue(r["harmonic_law_assumed"])
        self.assertFalse(r["physical_source_authenticated"])
        self.assertNotIn("Gamma",r)
        self.assertNotIn("Weil",r)


if __name__=="__main__":unittest.main()

class StrongSourceAndEnergyOracles(unittest.TestCase):
    def test_small_connected_weighted_graphs(self):
        import random
        rng=random.Random(9070)
        for case in range(110):
            n=rng.randrange(3,8)
            vertices=tuple(f'v{i}' for i in range(n))
            boundary=(vertices[0],vertices[-1])
            edges=[(vertices[i],vertices[i+1],F(rng.randrange(1,5))) for i in range(n-1)]
            existing={frozenset((u,v)) for u,v,w in edges}
            for i in range(n):
                for j in range(i+2,n):
                    if rng.randrange(3)==0:
                        k=frozenset((vertices[i],vertices[j]))
                        if k not in existing:
                            existing.add(k);edges.append((vertices[i],vertices[j],F(rng.randrange(1,5))))
            carrier=SharedCarrierGraph('seeded-structural-carrier',case,vertices,boundary,tuple(edges))
            b={boundary[0]:F(rng.randrange(-7,8),3),
               boundary[1]:F(rng.randrange(-7,8),5)}
            f=carrier.complete_harmonic(b)
            self.assertEqual(carrier.energy(f),carrier.boundary_energy(b))
            self.assertTrue(all(carrier.flux(f)[v]==0 for v in carrier.interiors))
            drift=F(rng.randrange(-5,6),3)
            shifted={v:value+drift for v,value in b.items()}
            f2=carrier.complete_harmonic(shifted)
            self.assertTrue(all(f2[v]-f[v]==drift for v in vertices))
            self.assertEqual(carrier.energy(f),carrier.energy(f2))
            if carrier.interiors:
                j=carrier.interiors[0]
                candidate=dict(f);candidate[j]+=1
                self.assertGreater(carrier.energy(candidate),carrier.energy(f))

    def test_many_claims_fiber_factorization_are_exact(self):
        for n in range(2,5):
            states=tuple(range(1<<n))
            observations={f'x{i}':tuple((x>>i)&1 for x in states) for i in range(n)}
            subset=tuple(observations)[:-1]
            for mask in (0,1,(1<<(1<<n))-1,0b1010101010101010 & ((1<<(1<<n))-1)):
                claims={'target':tuple((mask>>j)&1 for j in states)}
                model=SharedSource('X',0,'B',states,observations,claims)
                reports=model.factorization(subset,'target')
                brute={}
                expected=True
                for j,x in enumerate(states):
                    key=tuple(observations[p][j] for p in subset)
                    if key in brute and brute[key]!=claims['target'][j]:expected=False
                    brute[key]=claims['target'][j]
                self.assertEqual(reports['factors'],expected)
                self.assertTrue(model.factorization(tuple(observations),'target')['factors'])

class NestedBoundaryTowerTests(unittest.TestCase):
    def test_true_two_layer_commuting_square(self):
        g=SharedCarrierGraph("finite-carrier",4,("a","u","v","b"),("a","b"),
                             (("a","u",1),("u","v",1),("v","b",1)))
        r=g.nested_boundary_reduction(("a","u","b"))
        self.assertTrue(r["commuting_square_verified"])
        self.assertEqual(r["direct_DtN"],((F(1,3),F(-1,3)),(F(-1,3),F(1,3))))
        self.assertEqual(r["intermediate_DtN"],(
            (F(1),F(-1),F(0)),(F(-1),F(3,2),F(-1,2)),(F(0),F(-1,2),F(1,2))))
        self.assertFalse(r["independent_physical_model_attested"])

    def test_exact_nested_commutation_with_many_different_elimination_orders(self):
        import random
        rng=random.Random(91837)
        for case in range(90):
            n=rng.randrange(4,9)
            V=tuple(range(n))
            edges=[(i,i+1,F(rng.randrange(1,6))) for i in range(n-1)]
            for i in range(n):
                for j in range(i+2,n):
                    if rng.randrange(4)==0:edges.append((i,j,F(rng.randrange(1,6))))
            g=SharedCarrierGraph("same-carrier",case,V,(0,n-1),tuple(edges))
            mid=(0,n-1)+tuple(i for i in range(1,n-1) if rng.randrange(2))
            for chosen in (mid,tuple(V),g.boundary):
                out=g.nested_boundary_reduction(chosen)
                self.assertEqual(out['direct_DtN'],out['composed_DtN'])
                self.assertEqual(out['carrier_id'],'same-carrier')

    def test_wrong_boundary_refinement_rejected(self):
        g=wheel()
        for subset in (("b0","b1"),("b0","b1","b2","b3","x"),
                       ("b0","b1","b2","b3","b3")):
            with self.assertRaises(CarrierDescentError):
                g.nested_boundary_reduction(subset)
